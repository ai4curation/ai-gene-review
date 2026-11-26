"""Pinned inputs for time-split benchmarks: GO release GAFs, GO release ontologies, UniProt.

Everything is read from a local cache (``.cache/benchmark`` by default) so a
benchmark can be rechecked offline once its sources are fetched. GO release
files are addressed by release date, which pins them; UniProt is current-only
and its release is recorded from the response header.

GAF dates are not creation dates: GO re-stamps the date column when a row is
re-exported (an IPI from a 2021 paper carries 20260725 in the 2026-08-05
release), so newness is decided by absence from the baseline release, never by
the date column.
"""

from __future__ import annotations

import gzip
import hashlib
import math
from collections import defaultdict
from collections.abc import Iterable, Iterator
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

import requests

DEFAULT_CACHE = Path(".cache/benchmark")
GO_RELEASE_BASE = "https://release.geneontology.org"
UNIPROT_REST = "https://rest.uniprot.org/uniprotkb"

#: CAFA's experimental evidence codes.
CAFA_EVIDENCE = ("EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "TAS", "IC")
#: Codes treated as experimental knowledge when judging novelty and knowledge category.
EXPERIMENTAL_EVIDENCE = frozenset(
    {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "HTP", "HDA", "HMP", "HGI", "HEP"}
    | {"TAS", "IC", "NAS"}
)
ASPECT_ROOTS = {"F": "GO:0003674", "P": "GO:0008150", "C": "GO:0005575"}
NAMESPACE_ASPECT = {
    "molecular_function": "F",
    "biological_process": "P",
    "cellular_component": "C",
}


@dataclass(frozen=True)
class Annotation:
    """One GAF 2.2 row, reduced to the fields benchmarks use.

    >>> row = "UniProtKB\\tP1\\tABC\\tenables\\tGO:0004672\\tPMID:1\\tIDA\\t\\tF\\tname\\t\\tprotein\\ttaxon:9606\\t20250101\\tUniProt"
    >>> a = Annotation.from_gaf_line(row)
    >>> (a.protein, a.term, a.evidence, a.negated, a.aspect)
    ('UniProtKB:P1', 'GO:0004672', 'IDA', False, 'F')
    >>> Annotation.from_gaf_line(row.replace("enables", "NOT|enables")).negated
    True
    """

    protein: str
    symbol: str
    qualifier: str
    negated: bool
    term: str
    reference: str
    evidence: str
    with_from: str
    aspect: str
    name: str
    date: str
    assigned_by: str

    @classmethod
    def from_gaf_line(cls, line: str) -> "Annotation":
        """Parse a tab-separated GAF row (GAF 2.1/2.2)."""
        f = line.rstrip("\n").split("\t")
        qualifiers = f[3].split("|") if f[3] else []
        return cls(
            protein=f"{f[0]}:{f[1]}",
            symbol=f[2],
            qualifier="|".join(q for q in qualifiers if q != "NOT"),
            negated="NOT" in qualifiers,
            term=f[4],
            reference=f[5].split("|")[0],
            evidence=f[6],
            with_from=f[7],
            aspect=f[8],
            name=f[9],
            date=f[13],
            assigned_by=f[14],
        )

    @property
    def experimental(self) -> bool:
        """True when the evidence code counts as experimental knowledge."""
        return self.evidence in EXPERIMENTAL_EVIDENCE


def read_gaf(path: Path) -> list[Annotation]:
    """Read a (possibly gzipped) GAF into annotations."""
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt") as handle:
        return [Annotation.from_gaf_line(line) for line in handle if line[0] != "!"]


def sha256(path: Path) -> str:
    """Hex SHA-256 of a file."""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def gaf_urls(release: str, gaf_code: str) -> list[str]:
    """Candidate URLs for a species GAF in a GO release, newest layout first.

    GO moved per-species files to ``annotations/gaf/<CODE>-uniprot.gaf.gz`` in
    2026; earlier releases use ``annotations/goa_<code>.gaf.gz``.

    >>> gaf_urls("2025-06-01", "HUMAN")[1]
    'https://release.geneontology.org/2025-06-01/annotations/goa_human.gaf.gz'
    """
    base = f"{GO_RELEASE_BASE}/{release}/annotations"
    return [
        f"{base}/gaf/{gaf_code.upper()}-uniprot.gaf.gz",
        f"{base}/goa_{gaf_code.lower()}.gaf.gz",
    ]


def ontology_url(release: str) -> str:
    """URL of go-basic.obo in a GO release."""
    return f"{GO_RELEASE_BASE}/{release}/ontology/go-basic.obo"


def _download(url: str, dest: Path) -> bool:
    """Download ``url`` to ``dest``; return False on HTTP 404."""
    response = requests.get(url, stream=True, timeout=120)
    if response.status_code == 404:
        return False
    response.raise_for_status()
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_suffix(dest.suffix + ".part")
    with open(tmp, "wb") as handle:
        for chunk in response.iter_content(1 << 20):
            handle.write(chunk)
    tmp.rename(dest)
    return True


@dataclass
class ReleaseFiles:
    """Local paths of one GO release's species GAF and ontology."""

    release: str
    gaf: Path
    gaf_url: str
    ontology: Path
    ontology_url: str


def release_dir(cache: Path, release: str) -> Path:
    """Cache folder for a GO release."""
    return cache / "go-release" / release


def fetch_release(
    release: str, gaf_code: str, cache: Path = DEFAULT_CACHE
) -> ReleaseFiles:
    """Fetch (if absent) a GO release's species GAF and go-basic.obo into the cache."""
    folder = release_dir(cache, release)
    gaf = folder / f"{gaf_code.upper()}.gaf.gz"
    url_record = folder / f"{gaf_code.upper()}.gaf.url"
    if not gaf.exists():
        for url in gaf_urls(release, gaf_code):
            if _download(url, gaf):
                url_record.write_text(url)
                break
        else:
            raise FileNotFoundError(f"no {gaf_code} GAF in GO release {release}")
    obo = folder / "go-basic.obo"
    if not obo.exists() and not _download(ontology_url(release), obo):
        raise FileNotFoundError(f"no go-basic.obo in GO release {release}")
    return ReleaseFiles(
        release=release,
        gaf=gaf,
        gaf_url=url_record.read_text().strip()
        if url_record.exists()
        else gaf_urls(release, gaf_code)[0],
        ontology=obo,
        ontology_url=ontology_url(release),
    )


def snapshot(name: str, url: str, path: Path, release: str) -> dict:
    """SourceSnapshot record for a pinned file."""
    return {
        "name": name,
        "url": url,
        "release": release,
        "sha256": sha256(path),
        "retrieved": date.fromtimestamp(path.stat().st_mtime).isoformat(),
    }


@dataclass
class Ontology:
    """The parts of a go-basic.obo release that benchmark checks need.

    >>> obo = '''[Term]
    ... id: GO:0000001
    ... name: root
    ... namespace: molecular_function
    ...
    ... [Term]
    ... id: GO:0000002
    ... name: child
    ... namespace: molecular_function
    ... alt_id: GO:0000009
    ... is_a: GO:0000001 ! root
    ...
    ... [Term]
    ... id: GO:0000003
    ... name: old
    ... namespace: molecular_function
    ... is_obsolete: true
    ... replaced_by: GO:0000002
    ... '''
    >>> o = Ontology.parse(obo.splitlines())
    >>> sorted(o.ancestors("GO:0000002"))
    ['GO:0000001', 'GO:0000002']
    >>> o.resolve("GO:0000009"), o.resolve("GO:0000003"), o.aspect("GO:0000002")
    ('GO:0000002', 'GO:0000002', 'F')
    """

    names: dict[str, str] = field(default_factory=dict)
    namespaces: dict[str, str] = field(default_factory=dict)
    parents: dict[str, set[str]] = field(default_factory=dict)
    obsolete: set[str] = field(default_factory=set)
    replaced_by: dict[str, str] = field(default_factory=dict)
    alt_ids: dict[str, str] = field(default_factory=dict)
    _ancestors: dict[str, frozenset[str]] = field(default_factory=dict, repr=False)

    @classmethod
    def parse(cls, lines: Iterable[str]) -> "Ontology":
        """Parse OBO lines; only [Term] stanzas, is_a and part_of edges."""
        onto = cls()
        current: str | None = None
        in_term = False
        for raw in lines:
            line = raw.strip()
            if line.startswith("["):
                in_term = line == "[Term]"
                current = None
                continue
            if not in_term or ": " not in line:
                continue
            tag, value = line.split(": ", 1)
            value = value.split(" ! ")[0].strip()
            if tag == "id":
                current = value
                onto.parents.setdefault(current, set())
            elif current is None:
                continue
            elif tag == "name":
                onto.names[current] = value
            elif tag == "namespace":
                onto.namespaces[current] = value
            elif tag == "is_a":
                onto.parents[current].add(value)
            elif tag == "relationship" and value.startswith("part_of "):
                onto.parents[current].add(value.split()[1])
            elif tag == "is_obsolete" and value == "true":
                onto.obsolete.add(current)
            elif tag == "replaced_by":
                onto.replaced_by[current] = value
            elif tag == "alt_id":
                onto.alt_ids[value] = current
        return onto

    @classmethod
    def load(cls, path: Path) -> "Ontology":
        """Load a go-basic.obo file."""
        with open(path) as handle:
            return cls.parse(handle)

    def resolve(self, term: str) -> str:
        """Map an alt_id or replaced obsolete id to the live primary id."""
        term = self.alt_ids.get(term, term)
        return self.replaced_by.get(term, term)

    def ancestors(self, term: str) -> frozenset[str]:
        """Reflexive is_a/part_of ancestors of a term."""
        cached = self._ancestors.get(term)
        if cached is not None:
            return cached
        result = {term}
        for parent in self.parents.get(term, ()):
            result |= self.ancestors(parent)
        frozen = frozenset(result)
        self._ancestors[term] = frozen
        return frozen

    def aspect(self, term: str) -> str | None:
        """F, P or C for a term, or None when unknown."""
        return NAMESPACE_ASPECT.get(self.namespaces.get(term, ""))

    def label(self, term: str) -> str | None:
        """Term name."""
        return self.names.get(term)


@dataclass
class InformationContent:
    """Annotation-frequency information content over a GAF, with is_a/part_of closure.

    IC(t) = -log2((n(t) + 1) / (N + 1)), where n(t) counts proteins annotated
    to t or a descendant and N counts proteins annotated in t's aspect.

    >>> o = Ontology(parents={"R": set(), "A": {"R"}, "B": {"R"}}, namespaces={k: "molecular_function" for k in "RAB"})
    >>> ic = InformationContent.from_terms(o, {"p1": {"A"}, "p2": {"A"}, "p3": {"B"}, "p4": {"B"}})
    >>> round(ic.ic("A"), 3), round(ic.ic("R"), 3)
    (0.737, 0.0)
    >>> round(ic.lin("A", "B"), 3), ic.lin("A", "A")
    (0.0, 1.0)
    """

    ontology: Ontology
    counts: dict[str, int]
    totals: dict[str, int]

    @classmethod
    def from_terms(
        cls, ontology: Ontology, protein_terms: dict[str, set[str]]
    ) -> "InformationContent":
        """Build from protein -> annotated terms."""
        counts: dict[str, int] = defaultdict(int)
        totals: dict[str, int] = defaultdict(int)
        for terms in protein_terms.values():
            closure: set[str] = set()
            for term in terms:
                closure |= ontology.ancestors(ontology.resolve(term))
            for term in closure:
                counts[term] += 1
            for aspect in {ontology.aspect(t) for t in closure} - {None}:
                totals[aspect] += 1  # type: ignore[index]
        return cls(ontology, dict(counts), dict(totals))

    def ic(self, term: str) -> float:
        """Information content in bits."""
        total = self.totals.get(self.ontology.aspect(term) or "", 0)
        return abs(math.log2((self.counts.get(term, 0) + 1) / (total + 1)))

    def lin(self, a: str, b: str) -> float:
        """Lin similarity: 2 IC(MICA) / (IC(a) + IC(b))."""
        if a == b:
            return 1.0
        common = self.ontology.ancestors(a) & self.ontology.ancestors(b)
        denominator = self.ic(a) + self.ic(b)
        if not common or denominator == 0:
            return 0.0
        return 2 * max(self.ic(t) for t in common) / denominator


def uniprot_stream(
    query: str, fields: str, cache: Path, name: str
) -> tuple[list[dict[str, str]], str]:
    """Run a UniProtKB stream query (TSV), cached by ``name``; return rows and UniProt release."""
    folder = cache / "uniprot"
    path = folder / f"{name}.tsv"
    release_path = folder / f"{name}.release"
    if not path.exists():
        response = requests.get(
            f"{UNIPROT_REST}/stream",
            params={"query": query, "fields": fields, "format": "tsv"},
            timeout=300,
        )
        response.raise_for_status()
        folder.mkdir(parents=True, exist_ok=True)
        path.write_text(response.text)
        release_path.write_text(response.headers.get("X-UniProt-Release", "unknown"))
    lines = path.read_text().splitlines()
    header = lines[0].split("\t")
    rows = [dict(zip(header, line.split("\t"))) for line in lines[1:] if line]
    return rows, release_path.read_text().strip()


def uniprot_entry(accession: str, cache: Path) -> str:
    """Current UniProtKB flat-file text for an accession, cached."""
    path = cache / "uniprot" / "entries" / f"{accession}.txt"
    if not path.exists():
        response = requests.get(f"{UNIPROT_REST}/{accession}.txt", timeout=60)
        response.raise_for_status()
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(response.text)
    return path.read_text()


def panther_subfamilies(rows: Iterable[dict[str, str]]) -> dict[str, str]:
    """Map UniProtKB:acc -> PANTHER subfamily from a UniProt TSV with a PANTHER column.

    >>> panther_subfamilies([{"Entry": "P1", "PANTHER": "PTHR1:SF2;PTHR1;"}])
    {'UniProtKB:P1': 'PTHR1:SF2'}
    """
    result = {}
    for row in rows:
        subfamilies = [p for p in row.get("PANTHER", "").split(";") if ":SF" in p]
        if subfamilies:
            result[f"UniProtKB:{row['Entry']}"] = subfamilies[0]
    return result


def by_protein(annotations: Iterable[Annotation]) -> dict[str, list[Annotation]]:
    """Group annotations by protein."""
    grouped: dict[str, list[Annotation]] = defaultdict(list)
    for annotation in annotations:
        grouped[annotation.protein].append(annotation)
    return dict(grouped)


def iter_positive(annotations: Iterable[Annotation]) -> Iterator[Annotation]:
    """Annotations without the NOT qualifier."""
    return (a for a in annotations if not a.negated)


UNIPROT_RECORD_FIELDS = "accession,id,protein_name,gene_primary,organism_name,organism_id,sequence_version,sequence"


def uniprot_records(
    accessions: Iterable[str], cache: Path
) -> dict[str, dict[str, str]]:
    """Current UniProtKB name, sequence and sequence version per accession, cached per accession."""
    folder = cache / "uniprot" / "records"
    folder.mkdir(parents=True, exist_ok=True)
    wanted = sorted(set(accessions))
    missing = [acc for acc in wanted if not (folder / f"{acc}.tsv").exists()]
    for start in range(0, len(missing), 100):
        chunk = missing[start : start + 100]
        response = requests.get(
            f"{UNIPROT_REST}/stream",
            params={
                "query": " OR ".join(f"accession:{acc}" for acc in chunk),
                "fields": UNIPROT_RECORD_FIELDS,
                "format": "tsv",
            },
            timeout=300,
        )
        response.raise_for_status()
        lines = response.text.splitlines()
        for line in lines[1:]:
            accession = line.split("\t", 1)[0]
            (folder / f"{accession}.tsv").write_text(lines[0] + "\n" + line + "\n")
    records = {}
    for acc in wanted:
        path = folder / f"{acc}.tsv"
        if path.exists():
            header, row = path.read_text().splitlines()[:2]
            records[acc] = dict(zip(header.split("\t"), row.split("\t")))
    return records


def parse_sortpubdate(value: str) -> str | None:
    """ISO date from PubMed's sortpubdate.

    >>> parse_sortpubdate("2025/06/03 00:00")
    '2025-06-03'
    >>> parse_sortpubdate("") is None
    True
    """
    return value[:10].replace("/", "-") if value else None


def pubmed_dates(pmids: Iterable[str], cache: Path) -> dict[str, str]:
    """PubMed publication dates (sortpubdate) for bare PMIDs, cached in one JSON file."""
    import json

    path = cache / "pubmed-dates.json"
    known: dict[str, str | None] = json.loads(path.read_text()) if path.exists() else {}
    missing = sorted(set(pmids) - set(known))
    for start in range(0, len(missing), 200):
        chunk = missing[start : start + 200]
        response = requests.get(
            "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi",
            params={
                "db": "pubmed",
                "id": ",".join(chunk),
                "retmode": "json",
                "tool": "ai-gene-review",
            },
            timeout=120,
        )
        response.raise_for_status()
        payload = response.json()["result"]
        for pmid in chunk:
            known[pmid] = parse_sortpubdate(
                (payload.get(pmid) or {}).get("sortpubdate", "")
            )
    if missing:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(known, indent=0, sort_keys=True))
    return {pmid: d for pmid in pmids if (d := known.get(pmid))}
