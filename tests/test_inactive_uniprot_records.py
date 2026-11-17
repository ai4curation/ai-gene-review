"""Exercise inactive and malformed UniProt responses over real local HTTP."""

import http.server
import json
import threading
import urllib.error
from contextlib import contextmanager

import pytest

from ai_gene_review.validation import family_residue_validator as validator
from ai_gene_review.validation.finding_residue_mappings import _check_side
from ai_gene_review.validation.gene_residue_claims import ClaimOutcome, _check_position


@pytest.fixture
def record_server(monkeypatch):
    """Change only the endpoint; use the actual fetch, JSON and cache paths."""
    @contextmanager
    def serve(payload, status=200, *, raw=False):
        body = payload if raw else json.dumps(payload).encode()
        requests = []

        class Handler(http.server.BaseHTTPRequestHandler):
            def do_GET(self):
                requests.append((self.path, self.headers.get("User-Agent")))
                self.send_response(status)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)

            def log_message(self, format, *args):
                pass

        with http.server.ThreadingHTTPServer(("127.0.0.1", 0), Handler) as server:
            thread = threading.Thread(
                target=server.serve_forever,
                kwargs={"poll_interval": 0.01},
                daemon=True,
            )
            thread.start()
            url = f"http://127.0.0.1:{server.server_port}/uniprotkb/{{acc}}.json"
            monkeypatch.setattr(validator, "UNIPROT_JSON", url)
            try:
                yield requests, url
            finally:
                server.shutdown()
                thread.join(timeout=5)
                assert not thread.is_alive()
    return serve


@pytest.mark.parametrize("getter", ["get", "sequence_version"])
@pytest.mark.parametrize("record", [
    {"entryType": "Inactive"},
    {"entryType": "Inactive", "inactiveReason": None},
    {"inactiveReason": {"inactiveReasonType": "DELETED"}},
    {
        "entryType": "Inactive",
        "inactiveReason": {
            "inactiveReasonType": "DELETED",
            "deletedReason": "Deleted from sequence source (ENSEMBL)",
        },
    },
])
def test_explicit_inactivity_is_remembered_without_disk_marker(
    tmp_path, record_server, getter, record
):
    """Both entry points fail explicitly, once, and never save inactivity to disk."""
    with record_server(record) as (requests, _):
        cache = validator.SequenceCache(tmp_path)
        with pytest.raises(validator.InactiveEntryError):
            getattr(cache, getter)("UniProtKB:C0H4F3")
        for method in (cache.get, cache.sequence_version):
            with pytest.raises(validator.InactiveEntryError):
                method("C0H4F3")
        assert requests == [("/uniprotkb/C0H4F3.json", "ai-gene-review")]
        assert not list(tmp_path.iterdir())


@pytest.mark.parametrize("getter", ["get", "sequence_version"])
@pytest.mark.parametrize("record", [
    {},
    {"entryType": "UniProtKB reviewed (Swiss-Prot)"},
    {"inactiveReason": {}},
    {"inactiveReason": "DELETED"},
    {"sequence": None},
    {"sequence": {}},
    {"sequence": {"value": None}},
    {"sequence": {"value": ""}},
    {"sequence": {"value": "   "}},
    {"sequence": {"value": "MACD*"}},
    {"sequence": {"value": ["M", "A"]}},
    [],
    None,
])
def test_unexpected_payload_is_a_contextual_error_not_inactivity(
    tmp_path, record_server, getter, record
):
    """A successful HTTP status cannot turn invalid source data into a curation FAIL."""
    with record_server(record) as (requests, url):
        cache = validator.SequenceCache(tmp_path)
        with pytest.raises(RuntimeError) as caught:
            getattr(cache, getter)("UniProtKB:P12345")
        assert "P12345" in str(caught.value)
        assert url.format(acc="P12345") in str(caught.value)
        assert isinstance(caught.value.__cause__, (KeyError, TypeError, ValueError))
        assert not cache._inactive
        assert len(requests) == 1
        assert not list(tmp_path.iterdir())


@pytest.mark.parametrize("getter", ["get", "sequence_version"])
@pytest.mark.parametrize("status,body,cause_type", [
    (404, b"not found", urllib.error.HTTPError),
    (200, b"<html>not JSON</html>", json.JSONDecodeError),
])
def test_retrieval_errors_keep_context_and_cause(
    tmp_path, record_server, getter, status, body, cause_type
):
    """Protocol/HTTP failures propagate without being caught as inactive claims."""
    with record_server(body, status, raw=True) as (requests, url):
        cache = validator.SequenceCache(tmp_path)
        with pytest.raises(RuntimeError) as caught:
            getattr(cache, getter)("P12345")
        assert url.format(acc="P12345") in str(caught.value)
        cause = caught.value.__cause__
        assert isinstance(cause, cause_type)
        if isinstance(cause, urllib.error.HTTPError):
            cause.close()
        assert not cache._inactive
        assert len(requests) == 1
        assert not list(tmp_path.iterdir())


def test_active_record_still_populates_and_reuses_sequence_and_version(
    tmp_path, record_server
):
    """The valid-record path writes the same sequence/version files as before."""
    record = {"sequence": {"value": "MACD"}, "entryAudit": {"sequenceVersion": 7}}
    with record_server(record) as (requests, _):
        cache = validator.SequenceCache(tmp_path)
        assert cache.get("P12345") == "MACD"
        assert cache.sequence_version("P12345") == 7
        assert (tmp_path / "P12345.seq").read_text() == "MACD"
        assert (tmp_path / "P12345.sv").read_text() == "7"
        assert validator.SequenceCache(tmp_path).get("P12345") == "MACD"
        assert len(requests) == 1


@pytest.mark.parametrize("kind", ["ANCHOR", "TARGET", "AS_REPORTED", "CANONICAL"])
def test_inactive_claim_paths_keep_the_accession_position_and_hard_failure(
    tmp_path, record_server, kind
):
    """Historical unavailability is visible, without claiming a residue mismatch."""
    record = {
        "entryType": "Inactive",
        "inactiveReason": {"inactiveReasonType": "DELETED"},
    }
    spec = {"accession": "UniProtKB:C0H4F3", "position": 68, "residue": "E"}
    with record_server(record) as (requests, _):
        cache = validator.SequenceCache(tmp_path)
        if kind in {"AS_REPORTED", "CANONICAL"}:
            result = _check_side(cache, spec, "reported", "G", "PMID:1", kind)
        else:
            result, observed = _check_position(cache, spec, "claim", "G", "GO:1", kind)
            assert observed is None
        assert result.outcome is ClaimOutcome.FAIL
        assert "UniProtKB:C0H4F3:68" in result.detail
        assert "inactive" in result.detail
        assert len(requests) == 1
        assert not list(tmp_path.iterdir())


DELETED = {
    "entryType": "Inactive",
    "inactiveReason": {"inactiveReasonType": "DELETED"},
}
CACHED_SEQUENCE = "M" * 67 + "E"
PINNED_POSITION = {
    "accession": "UniProtKB:C0H4F3",
    "position": 68,
    "residue": "E",
    "sequence_version": 1,
}


def _pinned_family_review():
    """Return a pinned anchor followed by an independent, checkable anchor."""
    return {
        "family_id": "PANTHER:PTHR21340",
        "residue_sites": [
            {
                "site_id": "deleted",
                "anchor": {"id": "UniProtKB:C0H4F3"},
                "anchor_sequence_version": 1,
                "residues": [{"position": 68, "expected": ["E"]}],
            },
            {
                "site_id": "live",
                "anchor": {"id": "UniProtKB:P12345"},
                "residues": [{"position": 3, "expected": ["C"]}],
            },
        ],
    }


def test_inactive_lazy_version_fails_anchor_and_continues_other_sites(
    tmp_path, record_server
):
    """A legacy sequence-only cache must not hide the lazy version error path."""
    seq_file = tmp_path / "C0H4F3.seq"
    seq_file.write_text(CACHED_SEQUENCE)
    (tmp_path / "P12345.seq").write_text("MACD")
    with record_server(DELETED) as (requests, _):
        cache = validator.SequenceCache(tmp_path)
        results = validator.check_anchor_residues(_pinned_family_review(), cache)
        assert [r.outcome for r in results] == [validator.Outcome.FAIL, validator.Outcome.PASS]
        assert results[0].accession == "UniProtKB:C0H4F3"
        assert "inactive" in results[0].message
        assert len(requests) == 1
        assert seq_file.read_text() == CACHED_SEQUENCE
        assert not (tmp_path / "C0H4F3.sv").exists()


@pytest.mark.parametrize("kind", ["ANCHOR", "TARGET", "AS_REPORTED", "CANONICAL"])
def test_inactive_lazy_version_is_a_scoped_claim_failure(
    tmp_path, record_server, kind
):
    """Pinned gene/finding positions report inactivity even with cached sequence."""
    seq_file = tmp_path / "C0H4F3.seq"
    seq_file.write_text(CACHED_SEQUENCE)
    with record_server(DELETED) as (requests, _):
        cache = validator.SequenceCache(tmp_path)
        if kind in {"AS_REPORTED", "CANONICAL"}:
            result = _check_side(cache, PINNED_POSITION, "reported", "G", "PMID:1", kind)
        else:
            result, observed = _check_position(
                cache, PINNED_POSITION, "claim", "G", "GO:1", kind
            )
            assert observed is None
        assert result.outcome is ClaimOutcome.FAIL
        assert "UniProtKB:C0H4F3:68" in result.detail
        assert "inactive" in result.detail
        assert len(requests) == 1
        assert seq_file.read_text() == CACHED_SEQUENCE
        assert not (tmp_path / "C0H4F3.sv").exists()


@pytest.mark.parametrize("cached", ["sequence", "version"])
def test_observed_inactivity_takes_precedence_over_memory_hits(
    tmp_path, record_server, cached
):
    """A new inactive observation wins; no retained cache file is deleted or rewritten."""
    name, content = ("C0H4F3.seq", CACHED_SEQUENCE) if cached == "sequence" else ("C0H4F3.sv", "1")
    retained = tmp_path / name
    retained.write_text(content)
    with record_server(DELETED) as (requests, _):
        cache = validator.SequenceCache(tmp_path)
        initial = cache.get if cached == "sequence" else cache.sequence_version
        missing = cache.sequence_version if cached == "sequence" else cache.get
        assert initial("C0H4F3") == (CACHED_SEQUENCE if cached == "sequence" else 1)
        assert not requests
        with pytest.raises(validator.InactiveEntryError):
            missing("C0H4F3")
        for method in (cache.get, cache.sequence_version):
            with pytest.raises(validator.InactiveEntryError):
                method("C0H4F3")
        assert len(requests) == 1
        assert {p.name: p.read_text() for p in tmp_path.iterdir()} == {name: content}


@pytest.mark.parametrize("path", ["family", "gene", "finding"])
def test_lazy_version_transport_error_still_propagates(
    tmp_path, record_server, path
):
    """Widening the typed inactive handler must not swallow retrieval failures."""
    seq_file = tmp_path / "C0H4F3.seq"
    seq_file.write_text(CACHED_SEQUENCE)
    with record_server(b"not found", 404, raw=True) as (requests, url):
        cache = validator.SequenceCache(tmp_path)
        with pytest.raises(RuntimeError) as caught:
            if path == "family":
                validator.check_anchor_residues(_pinned_family_review(), cache)
            elif path == "gene":
                _check_position(cache, PINNED_POSITION, "claim", "G", "GO:1", "ANCHOR")
            else:
                _check_side(cache, PINNED_POSITION, "reported", "G", "PMID:1", "AS_REPORTED")
        assert url.format(acc="C0H4F3") in str(caught.value)
        cause = caught.value.__cause__
        assert isinstance(cause, urllib.error.HTTPError) and cause.code == 404
        cause.close()
        assert not cache._inactive
        assert len(requests) == 1
        assert seq_file.read_text() == CACHED_SEQUENCE
        assert not (tmp_path / "C0H4F3.sv").exists()
