"""Tests for the Schnoes-style trusted-cutoff check of enzyme annotations."""

import threading
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

import pytest

from ai_gene_review.validation import enzyme_family_cutoff
from ai_gene_review.validation.enzyme_family_cutoff import (
    FamilyScore,
    NCBIfam,
    _read_with_retry,
    check,
    classify_hit,
    is_complete_ec,
    rank_closest,
    scan_library,
    verdict_for,
)

TC = (300.0, 300.0)
NC = (200.0, 200.0)


def score(
    seq: float | None,
    *,
    target: bool = True,
    family_type: str = "equivalog",
    acc: str = "TIGR00001.1",
    nc: tuple[float, float] | None = NC,
) -> FamilyScore:
    """A FamilyScore whose domain score equals its sequence score."""
    return FamilyScore(
        accession=acc,
        product_name=f"family {acc}",
        family_type=family_type,
        ec_numbers=[],
        go_terms=[],
        is_target=target,
        seq_score=seq,
        dom_score=seq,
        tc=TC,
        nc=nc,
    )


@pytest.mark.parametrize(
    "seq,dom,expected",
    [
        (None, None, "NO_HIT"),
        (350.0, 350.0, "ABOVE_TC"),
        (300.0, 300.0, "ABOVE_TC"),
        # --cut_tc semantics: a strong full-sequence score with a weak best domain fails
        (350.0, 250.0, "BETWEEN_NC_TC"),
        (250.0, 250.0, "BETWEEN_NC_TC"),
        (150.0, 150.0, "BELOW_NC"),
    ],
)
def test_classify_hit(seq, dom, expected):
    assert classify_hit(seq, dom, TC, NC) == expected


@pytest.mark.parametrize(
    "seq,expected", [(350.0, "ABOVE_TC"), (250.0, "BELOW_TC"), (None, "NO_HIT")]
)
def test_classify_hit_without_noise_cutoff(seq, expected):
    """A model with no NC line has no lenient band to place a sub-TC hit in."""
    assert classify_hit(seq, seq, TC, None) == expected


def test_domain_target_in_lenient_band_is_not_btc():
    """A domain-level target between NC and TC was not measured below its noise cutoff."""
    verdict, note, _ = verdict_for([score(250.0, family_type="domain")])
    assert verdict == "BETWEEN_NC_TC"
    assert "domain-level" in note


def test_btc_without_noise_cutoff_says_so():
    verdict, note, _ = verdict_for([score(250.0, nc=None)])
    assert verdict == "BTC"
    assert "no curated noise cutoff" in note
    _, note_with_nc, _ = verdict_for([score(150.0)])
    assert note_with_nc == "target family hit only below its noise cutoff"


@pytest.mark.parametrize(
    "scores,expected_verdict,expected_better",
    [
        ([], "NO_MODEL", 0),
        ([score(500.0, target=False)], "NO_MODEL", 1),
        ([score(500.0)], "ABOVE_TC", 0),
        # overlapping families for different reactions both pass: reported, not ranked
        ([score(500.0), score(600.0, target=False, acc="TIGR00002.1")], "ABOVE_TC", 1),
        ([score(250.0)], "BETWEEN_NC_TC", 0),
        # Schnoes's mandelate-racemase case: below the annotated family, above another
        ([score(60.0), score(550.0, target=False, acc="TIGR00002.1")], "BTC", 1),
        ([score(None), score(400.0, target=False, acc="TIGR00002.1")], "SFA", 1),
        ([score(None)], "NO_TARGET_HIT", 0),
        # a domain-level model passing TC does not establish the reaction
        ([score(500.0, family_type="domain")], "BETWEEN_NC_TC", 0),
        # nor does a domain-level competitor count as a better-fitting family
        ([score(60.0), score(550.0, target=False, family_type="domain")], "BTC", 0),
    ],
)
def test_verdict_for(scores, expected_verdict, expected_better):
    verdict, _note, better = verdict_for(scores)
    assert verdict == expected_verdict
    assert len(better) == expected_better


@pytest.mark.parametrize(
    "ec,expected",
    [("4.2.1.11", True), ("1.1.1.-", False), ("1.-.-.-", False), ("3.5.1", False)],
)
def test_is_complete_ec(ec, expected):
    assert is_complete_ec(ec) is expected


@pytest.fixture(scope="module")
def cache_dir(tmp_path_factory):
    return tmp_path_factory.mktemp("cutoff_cache")


@pytest.mark.integration
@pytest.mark.vcr_skip  # NCBIfam table and HMMs are large binary-ish downloads
def test_enolase_passes_trusted_cutoff(cache_dir):
    """E. coli enolase is the positive control from Schnoes's own superfamily."""
    report = check("P0A6P9", ["4.2.1.11"], [], cache_dir)
    assert report.verdict == "ABOVE_TC"


@pytest.mark.integration
@pytest.mark.vcr_skip
def test_prpb_isocitrate_lyase_is_below_cutoff(cache_dir):
    """P. putida PrpB is a methylisocitrate lyase that IEA calls an isocitrate lyase."""
    report = check("Q88KF6", [], ["GO:0004451"], cache_dir)
    assert report.verdict == "BTC"
    assert any("methylisocitrate lyase" in f for f in report.better_fitting_families)


def test_rank_closest_orders_by_score_over_cutoff_and_drops_domains():
    """Families are ranked by score/TC; domain models and non-hits are left out."""
    near = score(290.0, target=False, acc="NF000001.1")  # 0.97 of TC
    passes = score(330.0, target=False, acc="NF000002.1")  # 1.10 of TC
    domain = score(900.0, target=False, family_type="domain", acc="PF000003.1")
    miss = score(None, target=False, acc="NF000004.1")
    ranked = rank_closest([near, domain, miss, passes], top=5)
    assert [s.accession for s in ranked] == ["NF000002.1", "NF000001.1"]
    assert rank_closest([near, passes], top=1) == [passes]


def serve(statuses: list[tuple[int, dict[str, str]]]) -> tuple[HTTPServer, list[str]]:
    """A real local HTTP server answering each request with the next status in turn."""
    seen: list[str] = []

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:  # noqa: N802 (http.server naming)
            code, headers = statuses[min(len(seen), len(statuses) - 1)]
            seen.append(self.path)
            self.send_response(code)
            for key, value in headers.items():
                self.send_header(key, value)
            self.end_headers()
            self.wfile.write(b"ok" if code == 200 else b"")

        def log_message(self, *args: object) -> None:
            pass

    server = HTTPServer(("127.0.0.1", 0), Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server, seen


def local_request(server: HTTPServer) -> urllib.request.Request:
    """A request to the local server that bypasses any configured HTTP proxy."""
    return urllib.request.Request(f"http://127.0.0.1:{server.server_port}/x")


@pytest.fixture
def no_proxy(monkeypatch):
    """Route localhost requests directly even when the environment sets a proxy."""
    monkeypatch.setenv("no_proxy", "127.0.0.1,localhost")
    monkeypatch.setenv("NO_PROXY", "127.0.0.1,localhost")


def test_read_with_retry_waits_out_rate_limit(no_proxy):
    """Two 429 answers with Retry-After: 0, then success: the body comes back."""
    server, seen = serve(
        [(429, {"Retry-After": "0"}), (429, {"Retry-After": "0"}), (200, {})]
    )
    try:
        assert _read_with_retry(local_request(server)) == b"ok"
    finally:
        server.shutdown()
    assert len(seen) == 3


def test_read_with_retry_gives_up_after_limit(no_proxy):
    """A server that always answers 429 gets RATE_LIMIT_RETRIES attempts, then the error."""
    server, seen = serve([(429, {"Retry-After": "0"})])
    try:
        with pytest.raises(urllib.error.HTTPError) as exc:
            _read_with_retry(local_request(server))
    finally:
        server.shutdown()
    assert exc.value.code == 429
    assert len(seen) == enzyme_family_cutoff.RATE_LIMIT_RETRIES


def test_read_with_retry_does_not_retry_other_errors(no_proxy):
    """A 500 is raised at once: only rate limiting is retried."""
    server, seen = serve([(500, {})])
    try:
        with pytest.raises(urllib.error.HTTPError) as exc:
            _read_with_retry(local_request(server))
    finally:
        server.shutdown()
    assert exc.value.code == 500
    assert len(seen) == 1


@pytest.mark.integration
@pytest.mark.vcr_skip
def test_library_scan_finds_ghrb_sister_family_for_ptxd():
    """ptxD's closest family is GhrB, a model with no EC that targeted scoring never sees.

    Uses the persistent ``.cache/ncbifam`` store: the first run downloads the full
    NCBIfam HMM archive (about 450 MB) and presses the function-level library.
    """
    db = NCBIfam(Path(".cache") / "ncbifam")
    sequence = enzyme_family_cutoff.SequenceCache(Path(".cache") / "uniprot_seq").get(
        "Q88HI1"
    )
    closest = scan_library({"Q88HI1": sequence}, db)["Q88HI1"]
    assert closest[0].accession == "NF011938.0"
    assert closest[0].seq_score < closest[0].tc[0]  # near the family but outside it
    assert not closest[0].ec_numbers
