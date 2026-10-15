"""Queue protocol and controller safety, without GitHub writes."""

import json

import pytest

from tests.test_auto_merge_ready_prs import HEAD_SHA, _run_main, auto_merge, make_pr


def page(numbers=(), *, more=False, total=None):
    return {"data": {"repository": {"mergeQueue": {
        "id": "queue", "entries": {
            "totalCount": len(numbers) if total is None else total,
            "pageInfo": {"hasNextPage": more, "endCursor": "cursor"},
            "nodes": [{"pullRequest": {"number": n}} for n in numbers],
        },
    }}}}


def respond(monkeypatch, payload):
    monkeypatch.setattr(auto_merge, "_gh", lambda *a, **kw: json.dumps(payload))


def test_queue_disabled(monkeypatch):
    respond(monkeypatch, [{"data": {"repository": {"mergeQueue": None}}}])
    assert not auto_merge.read_queue_state("o/r", "main").active


def test_queue_pagination(monkeypatch):
    respond(monkeypatch, [page(range(1, 101), more=True, total=101), page([101], total=101)])
    assert auto_merge.read_queue_state("o/r", "main").numbers == frozenset(range(1, 102))


@pytest.mark.parametrize("payload", [
    [], {}, [{"errors": [{"message": "denied"}]}],
    [page([1], more=True)], [page([1], total=2)], [page([1, 1])],
    [page([True])], [page([0])], [{"data": {"repository": None}}],
])
def test_unreadable_or_partial_queue_fails_closed(monkeypatch, payload):
    respond(monkeypatch, payload)
    with pytest.raises(ValueError):
        auto_merge.read_queue_state("o/r", "main")


def history(reasons, *, head=HEAD_SHA):
    return {"data": {"repository": {"pullRequest": {
        "headRefOid": head,
        "commits": {"nodes": [{"commit": {"committedDate": "2026-08-01T00:00:00Z"}}]},
        "timelineItems": {"nodes": [{"reason": r, "createdAt": d} for r, d in reasons]},
    }}}}


@pytest.mark.parametrize("count,held", [(0, False), (1, False), (2, True), (3, True)])
def test_repeated_ejections_hold_current_head(monkeypatch, count, held):
    respond(monkeypatch, history([("failed_checks", "2026-08-02T00:00:00Z")] * count))
    assert bool(auto_merge.queue_retry_hold("o/r", 42, HEAD_SHA)) is held


def test_old_and_manual_removals_do_not_hold(monkeypatch):
    respond(monkeypatch, history([
        ("failed_checks", "2026-07-01T00:00:00Z"),
        ("failed_checks", "2026-07-02T00:00:00Z"),
        ("manually_removed", "2026-08-02T00:00:00Z"),
    ]))
    assert auto_merge.queue_retry_hold("o/r", 42, HEAD_SHA) == ""


def test_history_head_movement_rejected(monkeypatch):
    respond(monkeypatch, history([], head="new-head"))
    with pytest.raises(auto_merge.HeadMovedError):
        auto_merge.queue_retry_hold("o/r", 42, HEAD_SHA)


def test_enqueue_pins_head_and_separates_credentials(monkeypatch):
    calls = []
    responses = iter([
        {"data": {"repository": {"pullRequest": {
            "id": "pr-id", "headRefOid": HEAD_SHA, "mergeQueueEntry": None,
        }}}},
        {"data": {"enqueuePullRequest": {"mergeQueueEntry": {"id": "entry"}}}},
        {},
    ])

    def gh(args, **kwargs):
        calls.append((args, kwargs))
        return json.dumps(next(responses))

    monkeypatch.setattr(auto_merge, "_gh", gh)
    assert auto_merge.enqueue_pr("o/r", 42, HEAD_SHA, "writer")
    assert calls[0][1] == {}
    assert calls[1][1] == {"token": "writer"}
    mutation = " ".join(calls[1][0])
    assert "expectedHeadOid:$head" in mutation and "jump:false" in mutation
    assert f"head={HEAD_SHA}" in calls[1][0]
    assert calls[2][1] == {"token": "writer"}


@pytest.mark.parametrize("head,entry,error", [
    (HEAD_SHA, {"id": "entry"}, False), ("new-head", None, True),
])
def test_enqueue_race_never_direct_merges(monkeypatch, head, entry, error):
    respond(monkeypatch, {"data": {"repository": {"pullRequest": {
        "id": "pr-id", "headRefOid": head, "mergeQueueEntry": entry,
    }}}})
    if error:
        with pytest.raises(auto_merge.HeadMovedError):
            auto_merge.enqueue_pr("o/r", 42, HEAD_SHA, "writer")
    else:
        assert auto_merge.enqueue_pr("o/r", 42, HEAD_SHA, "writer") is False


@pytest.fixture
def active_queue(monkeypatch):
    monkeypatch.setattr(auto_merge, "read_queue_state", lambda *_: auto_merge.QueueState(True))
    monkeypatch.setattr(auto_merge, "queue_retry_hold", lambda *_: "")
    calls = []
    monkeypatch.setattr(auto_merge, "enqueue_pr", lambda *args: calls.append(args) or True)
    return calls


def test_active_queue_enqueues_and_reports_honestly(monkeypatch, tmp_path, active_queue):
    code, merges, summary = _run_main(
        monkeypatch, tmp_path, args=("--execute", "--required-check", "test (3.12)"),
    )
    assert code == 0 and not merges and len(active_queue) == 1
    assert "Queued 1" in summary and "Merged 1" not in summary


def test_queue_dry_run_does_not_write(monkeypatch, tmp_path, active_queue):
    code, merges, summary = _run_main(monkeypatch, tmp_path)
    assert code == 0 and not merges and not active_queue
    assert "Would enqueue 1" in summary


@pytest.mark.parametrize("numbers,reason", [
    ([42], "already in merge queue"), (list(range(100, 150)), "queue capacity reached: 50/50 observed entries"),
])
def test_existing_entries_skip_admission(monkeypatch, tmp_path, active_queue, numbers, reason):
    monkeypatch.setattr(auto_merge, "read_queue_state",
                        lambda *_: auto_merge.QueueState(True, frozenset(numbers)))
    code, merges, summary = _run_main(monkeypatch, tmp_path)
    assert code == 0 and not merges and not active_queue and reason in summary


def test_final_check_veto_still_applies(monkeypatch, tmp_path, active_queue):
    code, merges, summary = _run_main(
        monkeypatch, tmp_path,
        views=[make_pr(number=42), make_pr(number=42, reviewDecision="CHANGES_REQUESTED")],
        args=("--execute", "--required-check", "test (3.12)"),
    )
    assert code == 0 and not merges and not active_queue
    assert "state changed" in summary


def test_enqueue_failure_never_falls_back(monkeypatch, tmp_path, active_queue):
    def fail(*args):
        raise ValueError("queue disabled during enqueue")
    monkeypatch.setattr(auto_merge, "enqueue_pr", fail)
    code, merges, summary = _run_main(
        monkeypatch, tmp_path, args=("--execute", "--required-check", "test (3.12)"),
    )
    assert code == 1 and not merges and "Failed to enqueue 1" in summary


def test_unknown_queue_state_aborts_before_discovery(monkeypatch):
    def fail(*args):
        raise ValueError("incomplete response")
    monkeypatch.setattr(auto_merge, "read_queue_state", fail)
    monkeypatch.setattr(auto_merge, "list_open_prs", lambda *_: pytest.fail("must abort"))
    assert auto_merge.main(["--repo", "o/r"]) == 1


def test_configuration_change_stops_write(monkeypatch, tmp_path, active_queue):
    states = iter([auto_merge.QueueState(True), auto_merge.QueueState(False)])
    monkeypatch.setattr(auto_merge, "read_queue_state", lambda *_: next(states))
    code, merges, summary = _run_main(
        monkeypatch, tmp_path, args=("--execute", "--required-check", "test (3.12)"),
    )
    assert code == 1 and not merges and not active_queue
    assert "configuration changed" in summary


@pytest.mark.parametrize("dry_run,fail", [(True, False), (False, False), (False, True)])
@pytest.mark.parametrize("limit,explicit", [(2, True), (50, False)])
def test_admissions_and_failed_attempts_are_bounded(monkeypatch, active_queue, dry_run, fail, limit, explicit, capsys):
    monkeypatch.setenv("GH_MERGE_TOKEN", "writer")
    monkeypatch.setattr(auto_merge, "list_open_prs", lambda *_: [make_pr(number=n) for n in range(1, limit + 3)])
    monkeypatch.setattr(auto_merge, "view_pr", lambda _, n: make_pr(number=n))
    monkeypatch.setattr(auto_merge, "list_pr_reviews", lambda *_: make_pr()["reviews"])
    monkeypatch.setattr(auto_merge, "list_pr_files", lambda *_: auto_merge.ChangedFileInventory(
        tuple(make_pr()["changed_files"]), (),
    ))
    monkeypatch.setattr(auto_merge, "view_pr_head_sha", lambda *_: HEAD_SHA)
    monkeypatch.setattr(auto_merge, "merge_pr", lambda *_: pytest.fail("direct merge forbidden"))
    history_calls = []
    monkeypatch.setattr(auto_merge, "queue_retry_hold", lambda _, n, head: history_calls.append(n) or "")
    if fail:
        def fail_enqueue(*args):
            active_queue.append(args)
            raise ValueError("mutation failed")
        monkeypatch.setattr(auto_merge, "enqueue_pr", fail_enqueue)
    code = auto_merge.main([
        "--repo", "o/r", "--dry-run" if dry_run else "--execute",
        "--required-check", "test (3.12)", "--max-queue-size", "100",
        *(["--max-enqueue-per-run", str(limit)] if explicit else []),
    ])
    assert code == int(fail)
    assert set(history_calls) == set(range(1, limit + 1))
    assert len(active_queue) == (0 if dry_run else limit)
    assert f"queue admission attempt budget reached: {limit}/{limit} attempts" in capsys.readouterr().out


@pytest.mark.parametrize("hold", ["two failed builds", ValueError("unreadable history")])
def test_retry_hold_prevents_writes(monkeypatch, tmp_path, active_queue, hold):
    def history_check(*args):
        if isinstance(hold, Exception):
            raise hold
        return hold
    monkeypatch.setattr(auto_merge, "queue_retry_hold", history_check)
    code, merges, summary = _run_main(
        monkeypatch, tmp_path, args=("--execute", "--required-check", "test (3.12)"),
    )
    assert code == 0 and not merges and not active_queue and str(hold) in summary


@pytest.mark.parametrize("added", [True, False])
def test_queued_draft_is_not_restored(monkeypatch, tmp_path, active_queue, added):
    monkeypatch.setattr(auto_merge, "enqueue_pr", lambda *_: added)
    draft = make_pr(number=42, isDraft=True, mergeStateStatus="DRAFT")
    ready_calls, draft_calls = [], []
    code, merges, summary = _run_main(
        monkeypatch, tmp_path, list_view=draft,
        views=[draft, make_pr(number=42)], ready_calls=ready_calls, draft_calls=draft_calls,
        args=("--execute", "--include-drafts", "--required-check", "test (3.12)"),
    )
    assert code == 0 and not merges and ready_calls == [("o/r", 42)] and not draft_calls
    assert ("Queued 1" if added else "already in merge queue") in summary


def test_full_queue_at_final_read_stops_write(monkeypatch, tmp_path, active_queue):
    states = iter([auto_merge.QueueState(True), auto_merge.QueueState(True, frozenset(range(100, 150)))])
    monkeypatch.setattr(auto_merge, "read_queue_state", lambda *_: next(states))
    code, merges, summary = _run_main(
        monkeypatch, tmp_path, args=("--execute", "--required-check", "test (3.12)"),
    )
    assert code == 0 and not merges and not active_queue
    assert "queue filled during verification: 50/50 observed entries" in summary


@pytest.mark.parametrize("stage", ["enqueue", "history"])
def test_final_head_race_is_a_benign_skip(monkeypatch, tmp_path, active_queue, stage):
    def moved(*args):
        raise auto_merge.HeadMovedError("head moved concurrently")
    if stage == "enqueue":
        monkeypatch.setattr(auto_merge, "enqueue_pr", moved)
    else:
        calls = []
        def history_check(*args):
            calls.append(args)
            return moved() if len(calls) > 1 else ""
        monkeypatch.setattr(auto_merge, "queue_retry_hold", history_check)
    code, merges, summary = _run_main(
        monkeypatch, tmp_path, args=("--execute", "--required-check", "test (3.12)"),
    )
    assert code == 0 and not merges and not active_queue
    assert "head moved concurrently" in summary


def test_removal_at_commit_time_does_not_count(monkeypatch):
    respond(monkeypatch, history([("failed_checks", "2026-08-01T00:00:00Z")] * 2))
    assert auto_merge.queue_retry_hold("o/r", 42, HEAD_SHA) == ""


def test_one_remaining_slot_is_filled_at_default_capacity(monkeypatch, tmp_path, active_queue):
    monkeypatch.setattr(auto_merge, "read_queue_state",
                        lambda *_: auto_merge.QueueState(True, frozenset(range(100, 149))))
    code, merges, summary = _run_main(
        monkeypatch, tmp_path, args=("--execute", "--required-check", "test (3.12)"),
    )
    assert code == 0 and not merges and len(active_queue) == 1
    assert "Queued 1" in summary


def test_time_budget_stops_new_admissions(monkeypatch, active_queue, capsys):
    monkeypatch.setenv("GH_MERGE_TOKEN", "writer")
    monkeypatch.setattr(auto_merge, "list_open_prs", lambda *_: [make_pr(number=n) for n in (1, 2)])
    monkeypatch.setattr(auto_merge, "view_pr", lambda _, n: make_pr(number=n))
    monkeypatch.setattr(auto_merge, "list_pr_reviews", lambda *_: make_pr()["reviews"])
    monkeypatch.setattr(auto_merge, "list_pr_files", lambda *_: auto_merge.ChangedFileInventory(
        tuple(make_pr()["changed_files"]), (),
    ))
    monkeypatch.setattr(auto_merge, "view_pr_head_sha", lambda *_: HEAD_SHA)
    clock = iter([0.0, 0.0, 120.0])
    monkeypatch.setattr(auto_merge.time, "monotonic", lambda: next(clock))
    code = auto_merge.main([
        "--repo", "o/r", "--execute", "--required-check", "test (3.12)",
        "--time-budget-seconds", "60",
    ])
    assert code == 0 and [args[1] for args in active_queue] == [1]
    assert "sweep time budget reached: 120/60s" in capsys.readouterr().out
