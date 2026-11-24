"""Check an enzyme annotation against family HMM trusted cutoffs (Schnoes et al. 2009).

Schnoes et al. (PMID:20011109) found that most enzyme misannotation in automatically
annotated databases is *overprediction*: a sequence is given a specific family's reaction
although it only resembles that family (it scores below the family HMM's trusted cutoff,
"BTC") or only resembles the superfamily ("SFA"). Their protocol asks, in order, whether a
sequence matches the superfamily, matches the family, keeps the functional residues, and
scores above the family's trusted cutoff. This module mechanises steps 2 and 4.

The residue step (3) is ``family_residue_validator``; the superfamily step (1) is not
attempted, because only the families InterPro already reports are scored, not the whole
library, so "no hit" here is never evidence that the protein lacks the superfamily.

Family models come from NCBIfam (which absorbed TIGRFAMs). Each model carries curated
``TC`` (trusted) and ``NC`` (noise) cutoffs, and the release table maps families to EC
numbers and GO terms. These are the same two thresholds Schnoes used as their primary and
lenient cutoffs. Following HMMER's ``--cut_tc``, a hit passes only when both its
full-sequence score and its best-domain score reach the corresponding cutoff.

Which families are scored
-------------------------
* every NCBIfam family whose EC numbers or GO terms include the annotated function
  ("target" families), and
* every NCBIfam family InterPro reports for the protein ("observed" families), so a
  competing family the protein fits better is visible, or, with ``library=True``, the
  protein's closest families from a scan of the whole function-level library.

InterPro reports only matches above each model's own threshold, so a sister family the
protein narrowly misses is invisible to the default check (ptxD, which sits just below
the GhrB model, is the worked case). The library scan closes that gap: every report then
names the families the protein is closest to, ranked by score as a fraction of each
model's trusted cutoff, whether or not they pass it.

Verdicts
--------
``ABOVE_TC``
    A target family scores at or above its trusted cutoff. Consistent with the annotation.
``BETWEEN_NC_TC``
    The best target hit lies between noise and trusted cutoffs (Schnoes's lenient
    cutoff), or only a domain-level target model passes or reaches that band. Treat as
    unresolved, not as a pass.
``BTC``
    A target family is hit but below its noise cutoff. For a model with no curated noise
    cutoff the hit is only known to be below the trusted cutoff, and the note says so.
``SFA``
    No target family is hit at all, but the protein does match other NCBIfam families.
``NO_TARGET_HIT``
    Neither target nor observed families produced a hit.
``NO_MODEL``
    No NCBIfam family carries the function. Inconclusive: NCBIfam is prokaryote-centred,
    so this is the expected result for most eukaryote-specific enzymes.

Every verdict also reports any non-target family that the protein passes at TC. Below a
cutoff this is the Schnoes mandelate-racemase case, where the sequence instead fits the
fuconate dehydratase family; on an ``ABOVE_TC`` verdict it marks overlapping families
for different reactions, which the scores alone cannot rank. A below-cutoff verdict is a reason to look closer, not a
reason to remove an experimental annotation: true but divergent family members also
score below TC.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import time
import urllib.error
import urllib.request
from dataclasses import asdict, dataclass, field
from pathlib import Path
from functools import lru_cache
from typing import TYPE_CHECKING, Iterable

import yaml

from ai_gene_review.validation.family_residue_validator import SequenceCache

if TYPE_CHECKING:
    import pyhmmer

NCBIFAM_BASE = "https://ftp.ncbi.nlm.nih.gov/hmm/current"
INTERPRO_NCBIFAM = (
    "https://www.ebi.ac.uk/interpro/api/entry/ncbifam/protein/uniprot/{acc}/"
)
QUICKGO_XREFS = "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/{go}/xrefs"

# Family types whose name commits to a specific function. "domain", "repeat" and
# "superfamily" models describe structure shared across functions, so a TC pass on one
# of those is not reported as support for a specific reaction.
FUNCTIONAL_TYPES = {
    "equivalog",
    "equivalog_domain",
    "hypoth_equivalog",
    "hypoth_equivalog_domain",
    "exception",
    "subfamily",
    "subfamily_domain",
    "paralog",
    "paralog_domain",
    "PfamEq",
    "PfamAutoEq",
}


@dataclass
class Family:
    """One NCBIfam model's release-table metadata."""

    accession: str  # versioned NCBIfam accession, e.g. TIGR01060.2
    source_id: str  # unversioned id InterPro uses, e.g. TIGR01060
    label: str
    family_type: str
    product_name: str
    ec_numbers: list[str]
    go_terms: list[str]


@dataclass
class FamilyScore:
    """A protein's score against one family model."""

    accession: str
    product_name: str
    family_type: str
    ec_numbers: list[str]
    go_terms: list[str]
    is_target: bool
    seq_score: float | None
    dom_score: float | None
    tc: tuple[float, float]
    nc: tuple[float, float] | None  # None when the model has no curated NC line
    status: str = field(init=False)

    def __post_init__(self) -> None:
        self.status = classify_hit(self.seq_score, self.dom_score, self.tc, self.nc)


@dataclass
class CutoffReport:
    accession: str
    targets: list[str]
    ncbifam_release: str
    verdict: str
    note: str
    better_fitting_families: list[str]
    scores: list[FamilyScore]
    closest_families: list[FamilyScore] = field(default_factory=list)


def rank_closest(scores: Iterable[FamilyScore], top: int) -> list[FamilyScore]:
    """The ``top`` function-level families with the highest score as a fraction of TC.

    Ranking by the fraction of the trusted cutoff, not raw score, puts a family the
    protein narrowly misses above one it clears only because that model's cutoff is low.

    >>> f = lambda acc, s, t="equivalog": FamilyScore(acc, acc, t, [], [], False, s, s, (100.0, 100.0), None)
    >>> [x.accession for x in rank_closest([f("a", 50.0), f("b", 90.0), f("c", 200.0, "domain"), f("d", None)], 2)]
    ['b', 'a']
    """
    hits = [
        s
        for s in scores
        if s.seq_score is not None and s.family_type in FUNCTIONAL_TYPES
    ]
    return sorted(hits, key=lambda s: -(s.seq_score or 0.0) / s.tc[0])[:top]


def classify_hit(
    seq_score: float | None,
    dom_score: float | None,
    tc: tuple[float, float],
    nc: tuple[float, float] | None,
) -> str:
    """Place one hit relative to a model's trusted and noise cutoffs.

    A model with no curated noise cutoff has no lenient band, so a hit below its trusted
    cutoff is ``BELOW_TC`` rather than ``BELOW_NC``.
    """
    if seq_score is None or dom_score is None:
        return "NO_HIT"
    if seq_score >= tc[0] and dom_score >= tc[1]:
        return "ABOVE_TC"
    if nc is None:
        return "BELOW_TC"
    if seq_score >= nc[0] and dom_score >= nc[1]:
        return "BETWEEN_NC_TC"
    return "BELOW_NC"


def verdict_for(scores: list[FamilyScore]) -> tuple[str, str, list[str]]:
    """Reduce per-family scores to one verdict, a note, and better-fitting families."""
    targets = [s for s in scores if s.is_target]
    others = [s for s in scores if not s.is_target]
    better = [
        f"{s.accession} {s.product_name}"
        for s in others
        if s.status == "ABOVE_TC" and s.family_type in FUNCTIONAL_TYPES
    ]
    if not targets:
        return "NO_MODEL", "no NCBIfam family carries the annotated function", better

    functional_targets = [s for s in targets if s.family_type in FUNCTIONAL_TYPES]
    statuses = {s.status for s in functional_targets}
    if "ABOVE_TC" in statuses:
        if better:
            note = "target family passes TC, but so does a family for another reaction"
            return "ABOVE_TC", note, better
        return (
            "ABOVE_TC",
            "a functional target family passes its trusted cutoff",
            better,
        )
    if any(s.status == "ABOVE_TC" for s in targets):
        note = (
            "passes TC only for a domain-level model, which does not fix the reaction"
        )
        return "BETWEEN_NC_TC", note, better
    if "BETWEEN_NC_TC" in statuses:
        return (
            "BETWEEN_NC_TC",
            "best target hit lies between noise and trusted cutoffs",
            better,
        )
    if any(s.status == "BETWEEN_NC_TC" for s in targets):
        note = "only a domain-level target model is hit, between its noise and trusted cutoffs"
        return "BETWEEN_NC_TC", note, better
    below = [s for s in targets if s.status in {"BELOW_NC", "BELOW_TC"}]
    if below:
        if all(s.status == "BELOW_NC" for s in below):
            note = "target family hit only below its noise cutoff"
        else:
            note = "target family hit below its trusted cutoff; a hit model has no curated noise cutoff"
        return "BTC", note, better
    if any(s.status != "NO_HIT" for s in others):
        return "SFA", "no target family hit; protein matches other families", better
    return "NO_TARGET_HIT", "no scored family produced a hit", better


def _split(value: str) -> list[str]:
    return [v.strip() for v in value.split(",") if v.strip()]


class NCBIfam:
    """NCBIfam release table and per-family HMMs, cached under ``cache_dir``."""

    def __init__(self, cache_dir: Path) -> None:
        self.cache_dir = cache_dir
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        distributed = self._distributed_models()
        # The release table also lists Pfam-derived models that NCBI does not redistribute.
        self.families = [f for f in self._load_table() if f.accession in distributed]
        self.by_source = {f.source_id: f for f in self.families if f.source_id}
        # unversioned accessions as a fallback, never shadowing a family's own source id
        for f in self.families:
            self.by_source.setdefault(f.accession.split(".")[0], f)

    def _download(self, url: str, path: Path) -> Path:
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            req = urllib.request.Request(url, headers={"User-Agent": "ai-gene-review"})
            with urllib.request.urlopen(req, timeout=120) as fh:
                path.write_bytes(fh.read())
        return path

    def release(self) -> str:
        notes = self._download(
            f"{NCBIFAM_BASE}/RELEASE_NOTES.txt", self.cache_dir / "RELEASE_NOTES.txt"
        )
        for line in notes.read_text().splitlines():
            if "Release number" in line:
                return line.split(":", 1)[1].strip()
        return "unknown"

    def _distributed_models(self) -> set[str]:
        """Accessions with an HMM file in this release's per-model directory."""
        listing = self._download(
            f"{NCBIFAM_BASE}/hmm_PGAP.HMM/", self.cache_dir / "hmm_index.html"
        )
        return set(re.findall(r'href="([^"/]+)\.HMM"', listing.read_text()))

    def _load_table(self) -> list[Family]:
        path = self._download(
            f"{NCBIFAM_BASE}/hmm_PGAP.tsv", self.cache_dir / "hmm_PGAP.tsv"
        )
        with path.open() as fh:
            header = fh.readline().lstrip("#").rstrip("\n").split("\t")
            rows = csv.DictReader(fh, fieldnames=header, delimiter="\t")
            return [
                Family(
                    accession=r["ncbi_accession"],
                    source_id=r["source_identifier"],
                    label=r["label"],
                    family_type=r["family_type"],
                    product_name=r["product_name"],
                    ec_numbers=_split(r["ec_numbers"]),
                    go_terms=_split(r["go_terms"]),
                )
                for r in rows
            ]

    def targets_for(self, ecs: Iterable[str], gos: Iterable[str]) -> list[Family]:
        ecs, gos = set(ecs), set(gos)
        return [
            f for f in self.families if ecs & set(f.ec_numbers) or gos & set(f.go_terms)
        ]

    def library(self) -> Path:
        """Pressed HMMER database of every function-level model, built once and cached.

        The release ships one file per model; they are unpacked from the release archive
        into the same folder ``hmm_path`` reads, then pressed so a scan can stream the
        profiles instead of holding about 17,000 models in memory.
        """
        prefix = self.cache_dir / "library" / "functional.hmm"
        if prefix.with_suffix(".hmm.h3m").exists():
            return prefix
        import tarfile

        import pyhmmer

        archive = self._download(
            f"{NCBIFAM_BASE}/hmm_PGAP.HMM.tgz", self.cache_dir / "hmm_PGAP.HMM.tgz"
        )
        hmm_dir = self.cache_dir / "hmm"
        hmm_dir.mkdir(parents=True, exist_ok=True)
        with tarfile.open(archive) as tar:
            for member in tar.getmembers():
                name = Path(member.name).name
                if member.isfile() and not (hmm_dir / name).exists():
                    source = tar.extractfile(member)
                    assert source is not None
                    (hmm_dir / name).write_bytes(source.read())

        def functional_hmms():
            for family in self.families:
                if family.family_type in FUNCTIONAL_TYPES:
                    with pyhmmer.plan7.HMMFile(self.hmm_path(family)) as fh:
                        yield fh.read()

        prefix.parent.mkdir(parents=True, exist_ok=True)
        pyhmmer.hmmer.hmmpress(functional_hmms(), prefix)
        return prefix

    def hmm_path(self, family: Family) -> Path:
        name = f"{family.accession}.HMM"
        return self._download(
            f"{NCBIFAM_BASE}/hmm_PGAP.HMM/{name}", self.cache_dir / "hmm" / name
        )


RATE_LIMIT_RETRIES = 5
MAX_RETRY_WAIT = 60.0  # seconds; a server-supplied Retry-After is capped at this


def _read_with_retry(req: urllib.request.Request) -> bytes:
    """Read a URL, waiting and retrying when the server answers 429 Too Many Requests.

    InterPro and QuickGO rate-limit clients; a batch run of the check makes dozens of calls. The
    wait follows the server's Retry-After header (capped at ``MAX_RETRY_WAIT``), else
    doubles from 2 s, and gives up
    after ``RATE_LIMIT_RETRIES`` attempts by re-raising the last 429.
    """
    for attempt in range(RATE_LIMIT_RETRIES):
        try:
            with urllib.request.urlopen(req, timeout=60) as fh:
                return fh.read()
        except urllib.error.HTTPError as exc:
            if exc.code != 429 or attempt == RATE_LIMIT_RETRIES - 1:
                raise
            retry_after = exc.headers.get("Retry-After", "")
            time.sleep(
                min(float(retry_after), MAX_RETRY_WAIT)
                if retry_after.isdigit()
                else 2.0 * 2**attempt
            )
    raise AssertionError("unreachable")


def interpro_ncbifam_matches(accession: str) -> list[str]:
    """NCBIfam ids InterPro reports for a UniProt protein (empty if none), across pages."""
    url: str | None = INTERPRO_NCBIFAM.format(acc=accession)
    matches: list[str] = []
    while url:
        req = urllib.request.Request(url, headers={"Accept": "application/json"})
        try:
            body = _read_with_retry(req)
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                return matches
            raise
        if not body.strip():  # InterPro answers 204 with no body when nothing matches
            return matches
        page = json.loads(body)
        matches += [r["metadata"]["accession"] for r in page["results"]]
        url = page.get("next")
    return matches


@lru_cache(maxsize=None)
def go_ec_xrefs(go_id: str) -> tuple[str, ...]:
    """EC numbers the GO term cross-references, so a GO-only query also finds EC-only families."""
    req = urllib.request.Request(
        QUICKGO_XREFS.format(go=go_id), headers={"Accept": "application/json"}
    )
    results = json.loads(_read_with_retry(req))["results"]
    return tuple(
        x["dbId"] for r in results for x in r.get("xRefs", []) if x["dbCode"] == "EC"
    )


def is_complete_ec(ec: str) -> bool:
    """True for a full four-level EC number, which names one reaction.

    >>> is_complete_ec("4.1.3.1"), is_complete_ec("1.1.1.-"), is_complete_ec("4.2.1.n1")
    (True, False, True)
    """
    parts = ec.split(".")
    return len(parts) == 4 and "-" not in parts


def _cutoffs(
    hmm: pyhmmer.plan7.HMM,
) -> tuple[tuple[float, float], tuple[float, float] | None]:
    """Trusted cutoff, and noise cutoff or None when the model curates none."""
    tc, nc = hmm.cutoffs.trusted, hmm.cutoffs.noise
    if tc is None:
        raise ValueError(f"{hmm.accession!r} has no TC line")
    rounded_nc = None if nc is None else (round(nc[0], 1), round(nc[1], 1))
    return (round(tc[0], 1), round(tc[1], 1)), rounded_nc


def score_families(
    sequence: str,
    accession: str,
    families: list[Family],
    target_ids: set[str],
    db: NCBIfam,
) -> list[FamilyScore]:
    """Score one sequence against each family model with no reporting threshold."""
    import pyhmmer

    alphabet = pyhmmer.easel.Alphabet.amino()
    seq = pyhmmer.easel.TextSequence(
        name=accession.encode(), sequence=sequence
    ).digitize(alphabet)
    block = pyhmmer.easel.DigitalSequenceBlock(alphabet, [seq])
    scores = []
    for family in families:
        with pyhmmer.plan7.HMMFile(db.hmm_path(family)) as fh:
            hmm = fh.read()
        tc, nc = _cutoffs(hmm)
        # Schnoes scored permissively (E-value 100) to see divergent hits. Scores do not
        # depend on E-value, so report everything and judge by bit score alone, and switch
        # off HMMER's acceleration filters, which would otherwise discard a divergent
        # sequence before it is scored and turn a weak hit into a false "no hit".
        hits = next(
            pyhmmer.hmmsearch(
                [hmm],
                block,
                E=1e6,
                domE=1e6,
                Z=1,
                bias_filter=False,
                F1=1.0,
                F2=1.0,
                F3=1.0,
            )
        )
        seq_score = dom_score = None
        # One sequence in the block, so at most one hit. With the filters off every
        # sequence is scored; a non-positive bit score means the sequence fits the model
        # no better than the null model, so it is not counted as a hit.
        if len(hits) and hits[0].score > 0:
            seq_score = hits[0].score
            dom_score = max(d.score for d in hits[0].domains)
        scores.append(
            FamilyScore(
                accession=family.accession,
                product_name=family.product_name,
                family_type=family.family_type,
                ec_numbers=family.ec_numbers,
                go_terms=family.go_terms,
                is_target=family.accession in target_ids,
                seq_score=round(seq_score, 1) if seq_score is not None else None,
                dom_score=round(dom_score, 1) if dom_score is not None else None,
                tc=tc,
                nc=nc,
            )
        )
    return sorted(
        scores, key=lambda s: (not s.is_target, -(s.seq_score or float("-inf")))
    )


def scan_library(
    sequences: dict[str, str], db: NCBIfam, top: int = 5
) -> dict[str, list[FamilyScore]]:
    """Each protein's ``top`` closest function-level families across the whole library.

    Unlike ``score_families`` this keeps HMMER's acceleration filters on: it looks for
    the families a protein resembles most, which are strong enough hits to survive them,
    and a full library scan without filters would be very slow. Scores are bit scores,
    so they are comparable with ``score_families`` for any hit both report.
    """
    import pyhmmer

    alphabet = pyhmmer.easel.Alphabet.amino()
    block = pyhmmer.easel.DigitalSequenceBlock(
        alphabet,
        [
            pyhmmer.easel.TextSequence(name=acc.encode(), sequence=seq).digitize(
                alphabet
            )
            for acc, seq in sequences.items()
        ],
    )
    by_accession = {f.accession: f for f in db.families}
    closest: dict[str, list[FamilyScore]] = {}
    with pyhmmer.plan7.HMMFile(db.library()) as profiles:
        for hits in pyhmmer.hmmscan(block, profiles.optimized_profiles()):
            scores = []
            for hit in hits:
                if hit.score <= 0:
                    continue
                name = hit.name if isinstance(hit.name, str) else hit.name.decode()
                accession = (
                    hit.accession.decode()
                    if isinstance(hit.accession, bytes)
                    else hit.accession
                )
                family = by_accession.get(accession or "") or by_accession.get(name)
                if family is None:
                    continue
                scores.append((family, hit))
            query = hits.query.name
            query_name = query if isinstance(query, str) else query.decode()
            closest[query_name] = _hits_to_scores(scores, db, top)
    return closest


def _hits_to_scores(hits: list, db: NCBIfam, top: int) -> list[FamilyScore]:
    """FamilyScores for library hits, with each model's own cutoffs, closest first."""
    import pyhmmer

    scores = []
    for family, hit in hits:
        with pyhmmer.plan7.HMMFile(db.hmm_path(family)) as fh:
            tc, nc = _cutoffs(fh.read())
        scores.append(
            FamilyScore(
                accession=family.accession,
                product_name=family.product_name,
                family_type=family.family_type,
                ec_numbers=family.ec_numbers,
                go_terms=family.go_terms,
                is_target=False,
                seq_score=round(hit.score, 1),
                dom_score=round(max(d.score for d in hit.domains), 1),
                tc=tc,
                nc=nc,
            )
        )
    return rank_closest(scores, top)


def _with_closest(verdict: str, note: str, closest: list[FamilyScore]) -> str:
    """Name the closest non-target family on a verdict that leaves the protein unplaced.

    >>> f = FamilyScore("NF1.0", "GhrB", "equivalog", [], [], False, 418.1, 418.1, (492.0, 492.0), None)
    >>> _with_closest("BTC", "below", [f])
    'below; closest family NF1.0 GhrB (418.1 / 492.0)'
    >>> _with_closest("ABOVE_TC", "passes", [f])
    'passes'
    """
    if verdict not in {"BTC", "SFA", "NO_TARGET_HIT"} or not closest:
        return note
    top = closest[0]
    return f"{note}; closest family {top.accession} {top.product_name} ({top.seq_score} / {top.tc[0]})"


def check(
    accession: str,
    ecs: list[str],
    gos: list[str],
    cache_dir: Path,
    library: bool = False,
) -> CutoffReport:
    """Apply the trusted-cutoff check to one protein and one annotated activity.

    With ``library=True`` the observed families come from a whole-library scan
    (``scan_library``) instead of InterPro, and the report lists the closest families.
    """
    db = NCBIfam(cache_dir / "ncbifam")
    sequence = SequenceCache(cache_dir / "uniprot_seq").get(accession)
    # Schnoes's check is about a specific reaction. A broad GO term ("oxidoreductase
    # activity") names a class, not a family, so it is never scored as a target.
    specific_gos = [
        go for go in gos if any(is_complete_ec(ec) for ec in go_ec_xrefs(go))
    ]
    expanded = [
        ec for go in specific_gos for ec in go_ec_xrefs(go) if is_complete_ec(ec)
    ]
    targets = db.targets_for(
        [*(ec for ec in ecs if is_complete_ec(ec)), *expanded], specific_gos
    )
    closest: list[FamilyScore] = []
    if library:
        closest = scan_library({accession: sequence}, db)[accession]
        by_accession = {f.accession: f for f in db.families}
        observed = [by_accession[s.accession] for s in closest]
    else:
        observed = [
            db.by_source[i]
            for i in interpro_ncbifam_matches(accession)
            if i in db.by_source
        ]
    families = {f.accession: f for f in [*targets, *observed]}
    scores = score_families(
        sequence, accession, list(families.values()), {f.accession for f in targets}, db
    )
    verdict, note, better = verdict_for(scores)
    note = _with_closest(verdict, note, closest)
    return CutoffReport(
        accession=accession,
        targets=[*ecs, *gos],
        ncbifam_release=db.release(),
        verdict=verdict,
        note=note,
        better_fitting_families=better,
        scores=scores,
        closest_families=closest,
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("accession", help="UniProt accession")
    parser.add_argument(
        "--ec", action="append", default=[], help="EC number of the annotated activity"
    )
    parser.add_argument(
        "--go", action="append", default=[], help="GO MF id of the annotated activity"
    )
    parser.add_argument("--cache-dir", type=Path, default=Path(".cache"))
    parser.add_argument(
        "--library",
        action="store_true",
        help="find the protein's closest families by scanning the whole NCBIfam library"
        " (first use downloads and presses about 3 GB of models)",
    )
    parser.add_argument("-o", "--output", type=Path, help="Write the YAML report here")
    args = parser.parse_args(argv)
    if not args.ec and not args.go:
        parser.error("give at least one --ec or --go")

    report = check(
        args.accession, args.ec, args.go, args.cache_dir, library=args.library
    )
    text = yaml.safe_dump(asdict(report), sort_keys=False, default_flow_style=None)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    else:
        sys.stdout.write(text)
    print(f"{report.accession}: {report.verdict} ({report.note})", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
