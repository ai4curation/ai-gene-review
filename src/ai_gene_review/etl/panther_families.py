"""Build local PANTHER family/subfamily artifacts used by module validation.

PANTHER family (``PTHR12345``) and subfamily (``PTHR12345:SF7``) ids are cited
throughout module and gene-review YAML, but unlike GO they have no OBO ontology
to validate against: InterPro's API indexes only families (it returns ``204`` for
every ``:SF`` accession), and PANTHER itself exposes no term-lookup service. Such
ids were therefore entirely unchecked -- a real accession carrying an invented
label, or a label describing a completely different protein, passed validation
silently.

This module converts two upstream PANTHER files into small local artifacts that
slot into the existing validation stack:

``PANTHER<REL>_HMM_classifications`` -> ``interpro/panther/panther.obo``
    Every family and subfamily as an OBO term (``PANTHER:PTHR12345``,
    ``PANTHER:PTHR12345:SF7``), with each subfamily ``is_a`` its family. OAK
    reads this via the ``simpleobo:`` adapter, so wiring it into
    ``conf/oak_config.yaml`` gives both ``module_validator`` and the external
    ``linkml-term-validator`` existence checking, label checking, and
    family/subfamily hierarchy with no bespoke resolver code.

``PANTHER<REL>_<organism>`` sequence classifications -> ``panther-members.tsv``
    A pruned ``UniProt accession -> PTHR family:SF`` index covering the
    accessions actually cited in the repository. This is what catches a *wrong
    grounding* as opposed to a wrong label: a family descriptor whose declared
    family provably does not contain the very protein it names as its
    representative member.

Both artifacts are committed. Validation then needs no network access, and the
pinned release makes results reproducible. Regenerate with
``just build-panther-obo`` / ``just refresh-panther-members`` after a PANTHER
release bump.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, Iterator, List, NamedTuple, Optional, Set, Tuple

import requests
import yaml

PANTHER_RELEASE = "19.0"
HMM_BASE = "https://data.pantherdb.org/ftp/hmm_classifications/current_release"
HMM_URL = f"{HMM_BASE}/PANTHER{PANTHER_RELEASE}_HMM_classifications"
SEQ_BASE = (
    "https://data.pantherdb.org/ftp/sequence_classifications/current_release/"
    "PANTHER_Sequence_Classification_files"
)

FAMILY_RE = re.compile(r"^PTHR\d+$")
SUBFAMILY_RE = re.compile(r"^(PTHR\d+):(SF\d+)$")
UNIPROT_IN_LONG_ID_RE = re.compile(r"UniProtKB=(\w+)")

# Sequence-classification column indices (0-based). The file is headerless.
_SEQ_COL_LONG_ID = 0
_SEQ_COL_FAMILY_SF = 3


@dataclass(frozen=True)
class PantherEntry:
    """A PANTHER family or subfamily with its official name.

    Attributes:
        accession: Bare accession, e.g. ``PTHR13337`` or ``PTHR13337:SF6``.
        name: The official PANTHER name for that accession.
    """

    accession: str
    name: str

    @property
    def is_subfamily(self) -> bool:
        """True when this entry is a subfamily rather than a family.

        >>> PantherEntry("PTHR13337:SF6", "x").is_subfamily
        True
        >>> PantherEntry("PTHR13337", "x").is_subfamily
        False
        """
        return ":" in self.accession

    @property
    def family(self) -> str:
        """The family accession this entry belongs to (itself, if a family).

        >>> PantherEntry("PTHR13337:SF6", "x").family
        'PTHR13337'
        >>> PantherEntry("PTHR13337", "x").family
        'PTHR13337'
        """
        return self.accession.split(":", 1)[0]


def parse_hmm_classifications(lines: Iterable[str]) -> List[PantherEntry]:
    """Parse ``PANTHER<REL>_HMM_classifications`` into entries.

    The file is a headerless TSV whose first two columns are the accession and
    its name; later columns hold GO/pathway annotations that we ignore. Lines
    that are blank or whose accession is not a PANTHER family/subfamily id are
    skipped.

    >>> rows = [
    ...     "PTHR13337\\tSUCCINATE DEHYDROGENASE\\tmf#GO:1",
    ...     "PTHR13337:SF6\\tSDHD, MITOCHONDRIAL\\t",
    ...     "",
    ...     "NOTAFAMILY\\tignored",
    ... ]
    >>> [ (e.accession, e.name) for e in parse_hmm_classifications(rows) ]
    [('PTHR13337', 'SUCCINATE DEHYDROGENASE'), ('PTHR13337:SF6', 'SDHD, MITOCHONDRIAL')]
    """
    entries: List[PantherEntry] = []
    for line in lines:
        line = line.rstrip("\n").rstrip("\r")
        if not line:
            continue
        columns = line.split("\t")
        if len(columns) < 2:
            continue
        accession, name = columns[0].strip(), columns[1].strip()
        if not name:
            continue
        if not (FAMILY_RE.match(accession) or SUBFAMILY_RE.match(accession)):
            continue
        entries.append(PantherEntry(accession=accession, name=name))
    return entries


def render_obo(entries: Iterable[PantherEntry], release: str = PANTHER_RELEASE) -> Iterator[str]:
    """Render PANTHER entries as OBO stanzas, families first then subfamilies.

    Output is sorted so regeneration produces a stable diff. Each subfamily gets
    an ``is_a`` link to its family, which lets validators check that a declared
    subfamily really sits under a declared family.

    >>> entries = [PantherEntry("PTHR1:SF2", "SUB"), PantherEntry("PTHR1", "FAM")]
    >>> print("\\n".join(render_obo(entries, release="19.0")))
    format-version: 1.2
    ontology: panther
    data-version: 19.0
    <BLANKLINE>
    [Term]
    id: PANTHER:PTHR1
    name: FAM
    <BLANKLINE>
    [Term]
    id: PANTHER:PTHR1:SF2
    name: SUB
    is_a: PANTHER:PTHR1
    """
    yield "format-version: 1.2"
    yield "ontology: panther"
    yield f"data-version: {release}"

    families = sorted(
        (e for e in entries if not e.is_subfamily), key=lambda e: e.accession
    )
    subfamilies = sorted(
        (e for e in entries if e.is_subfamily), key=_subfamily_sort_key
    )
    for entry in families:
        yield ""
        yield "[Term]"
        yield f"id: PANTHER:{entry.accession}"
        yield f"name: {escape_obo_value(entry.name)}"
    for entry in subfamilies:
        yield ""
        yield "[Term]"
        yield f"id: PANTHER:{entry.accession}"
        yield f"name: {escape_obo_value(entry.name)}"
        yield f"is_a: PANTHER:{entry.family}"


def escape_obo_value(value: str) -> str:
    r"""Escape OBO tag-value special characters in a name.

    PANTHER 19.0 contains no ``!`` or ``{`` in any name, so this is currently a
    no-op -- but an unescaped ``!`` starts an OBO trailing comment, which would
    silently truncate a name and turn a *correct* label into a reported
    mismatch. Cheap insurance against a future release.

    >>> escape_obo_value("PLAIN NAME")
    'PLAIN NAME'
    >>> escape_obo_value("A ! B")
    'A \\! B'
    >>> escape_obo_value("X {y}")
    'X \\{y}'
    """
    out = value.replace("\\", "\\\\")
    for char in ("!", "{"):
        out = out.replace(char, "\\" + char)
    return out


def _subfamily_sort_key(entry: PantherEntry) -> Tuple[str, int]:
    """Sort subfamilies by family then numeric SF index (SF2 before SF10)."""
    match = SUBFAMILY_RE.match(entry.accession)
    assert match is not None  # only called for subfamilies
    return (match.group(1), int(match.group(2)[2:]))


def write_panther_obo(
    entries: Iterable[PantherEntry],
    out_path: Path,
    release: str = PANTHER_RELEASE,
) -> Path:
    """Write the PANTHER OBO artifact, returning the path written."""
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(render_obo(entries, release=release)) + "\n")
    return out_path


def fetch_hmm_classifications(
    cache_dir: Path, force_download: bool = False, url: str = HMM_URL
) -> Path:
    """Download the HMM classification file into ``cache_dir`` (cached)."""
    cache_dir = Path(cache_dir)
    cache_dir.mkdir(parents=True, exist_ok=True)
    dest = cache_dir / url.rsplit("/", 1)[-1]
    if dest.exists() and not force_download:
        return dest
    response = requests.get(url, timeout=300)
    response.raise_for_status()
    dest.write_bytes(response.content)
    return dest


def parse_sequence_classification(lines: Iterable[str]) -> Dict[str, str]:
    """Map UniProt accession -> ``PTHR family:SF`` from a sequence classification.

    The long id column encodes the accession as ``...|UniProtKB=P12345``; entries
    without a UniProt accession or without a family assignment are skipped.

    >>> rows = [
    ...     "HUMAN|HGNC=10683|UniProtKB=O14521\\tO14521\\tSDHD\\tPTHR13337:SF6\\tSDH",
    ...     "HUMAN|HGNC=1|Gene=xyz\\t\\tXYZ\\tPTHR1:SF1\\tX",
    ... ]
    >>> parse_sequence_classification(rows)
    {'O14521': 'PTHR13337:SF6'}
    """
    index: Dict[str, str] = {}
    for line in lines:
        columns = line.rstrip("\n").rstrip("\r").split("\t")
        if len(columns) <= _SEQ_COL_FAMILY_SF:
            continue
        match = UNIPROT_IN_LONG_ID_RE.search(columns[_SEQ_COL_LONG_ID])
        if not match:
            continue
        family_sf = columns[_SEQ_COL_FAMILY_SF].strip()
        if not (FAMILY_RE.match(family_sf) or SUBFAMILY_RE.match(family_sf)):
            continue
        index.setdefault(match.group(1), family_sf)
    return index


def fetch_sequence_classification(
    organism: str, cache_dir: Path, force_download: bool = False
) -> Optional[Path]:
    """Download one organism's sequence classification, or None if absent.

    PANTHER publishes these per organism under fixed slugs (``human``,
    ``e_coli``, ``pseudomonas``, ...). An unknown slug 404s, which is reported as
    ``None`` rather than raising so callers can sweep a candidate list.
    """
    cache_dir = Path(cache_dir)
    cache_dir.mkdir(parents=True, exist_ok=True)
    filename = f"PTHR{PANTHER_RELEASE}_{organism}"
    dest = cache_dir / filename
    if dest.exists() and not force_download:
        return dest
    response = requests.get(f"{SEQ_BASE}/{filename}", timeout=300)
    if response.status_code == 404:
        return None
    response.raise_for_status()
    dest.write_bytes(response.content)
    return dest


# Organism slugs covering the species curated in this repository. PANTHER
# publishes ~140 of these; fetching all of them to prune down to a few thousand
# accessions is wasteful, so the default set tracks the species actually present
# under genes/ and modules/. Extend with --organism when curating a new clade.
DEFAULT_ORGANISMS: Tuple[str, ...] = (
    "human",
    "mouse",
    "rat",
    "nematode_worm",
    "fruit_fly",
    "budding_yeast",
    "fission_yeast",
    "zebrafish",
    "arabidopsis",
    "black_cottonwood",
    "e_coli",
    "pseudomonas",
    "bacillus_subtilis",
    "salmonella",
    "mycobacterium",
    "dictyostelium",
    "candida",
    "chicken",
    "cow",
    "frog",
    "x_laevis",
)

MEMBER_INDEX_HEADER = ["uniprot_accession", "panther_family_sf"]


# Two distinct markers, because the two states have different remedies and a
# shared marker silently conflates them. "unresolved" means both PANTHER's
# per-organism files and UniProt were consulted and neither has a family -- a
# permanent fact, nothing to do. "unchecked" means the UniProt fallback was
# skipped, so the status is simply unknown -- rerun without the flag. Using one
# marker for both lets a --no-uniprot-fallback refresh be read as "no family
# exists", which is a false claim in the tool's output rather than in the file.
UNRESOLVED_MARKER = "# unresolved:"
UNCHECKED_MARKER = "# unchecked:"


class MemberIndexGaps(NamedTuple):
    """Accessions a member index holds no family for, split by why."""

    absent: Set[str]
    """Both sources consulted; PANTHER has no family. Permanent."""

    unchecked: Set[str]
    """UniProt was not consulted, so the status is unknown. Rerun to resolve."""


def render_member_index(
    index: Dict[str, str],
    unresolved: Optional[Set[str]] = None,
    consulted_uniprot: bool = True,
) -> Iterator[str]:
    """Render a member index as a sorted two-column TSV.

    ``unresolved`` accessions are recorded as a trailing comment block. Without
    it the file holds only successes, so it cannot distinguish "asked PANTHER
    and UniProt, no family exists" from "never asked" -- and any resolution rate
    read off the artifact is over an unknown denominator.

    ``consulted_uniprot`` must say whether the UniProt fallback actually ran.
    Recording "not found in UniProt" when ``--no-uniprot-fallback`` skipped that
    lookup writes a false claim into a committed artifact, which is worse than
    the omission this block replaced: a reader can recover from silence, not
    from a confident wrong statement.

    >>> print("\\n".join(render_member_index({"P2": "PTHR2", "P1": "PTHR1:SF3"})))
    uniprot_accession	panther_family_sf
    P1	PTHR1:SF3
    P2	PTHR2

    >>> for line in render_member_index({"P1": "PTHR1"}, {"P9"}):
    ...     print(line)
    uniprot_accession	panther_family_sf
    P1	PTHR1
    <BLANKLINE>
    # 1 accession(s) cited in modules/ with no PANTHER family in PANTHER's
    # per-organism classifications or in UniProt's xref_panther:
    # unresolved: P9

    With the fallback skipped, the block says only what was actually checked:

    >>> for line in render_member_index({"P1": "PTHR1"}, {"P9"}, False):
    ...     print(line)
    uniprot_accession	panther_family_sf
    P1	PTHR1
    <BLANKLINE>
    # 1 accession(s) cited in modules/ with no PANTHER family in PANTHER's
    # per-organism classifications. UniProt was NOT consulted
    # (--no-uniprot-fallback), so these are unchecked rather than absent:
    # unchecked: P9

    The marker differs, not just the prose: a shared marker would let a
    consumer read a skipped lookup as a completed one.
    """
    yield "\t".join(MEMBER_INDEX_HEADER)
    for accession in sorted(index):
        yield f"{accession}\t{index[accession]}"
    if unresolved:
        yield ""
        yield (
            f"# {len(unresolved)} accession(s) cited in modules/ with no PANTHER "
            "family in PANTHER's"
        )
        if consulted_uniprot:
            yield "# per-organism classifications or in UniProt's xref_panther:"
            marker = UNRESOLVED_MARKER
        else:
            yield "# per-organism classifications. UniProt was NOT consulted"
            yield "# (--no-uniprot-fallback), so these are unchecked rather than absent:"
            marker = UNCHECKED_MARKER
        for accession in sorted(unresolved):
            yield f"{marker} {accession}"


def load_member_index_gaps(path: Path) -> MemberIndexGaps:
    """Load the accessions a member index holds no family for, split by why.

    The programmatic counterpart to the comment block. Returning one merged set
    would let a consumer read a skipped UniProt lookup as a completed one and
    report "no PANTHER family exists" about a protein nobody asked about --
    moving the false claim out of the artifact and into the tool's output, where
    it is harder to notice.

    >>> import tempfile, pathlib
    >>> d = pathlib.Path(tempfile.mkdtemp())
    >>> _ = write_member_index({"P1": "PTHR1"}, d / "asked.tsv", {"P9"})
    >>> gaps = load_member_index_gaps(d / "asked.tsv")
    >>> sorted(gaps.absent), sorted(gaps.unchecked)
    (['P9'], [])

    >>> _ = write_member_index({"P1": "PTHR1"}, d / "skipped.tsv", {"P9"}, False)
    >>> gaps = load_member_index_gaps(d / "skipped.tsv")
    >>> sorted(gaps.absent), sorted(gaps.unchecked)
    ([], ['P9'])
    """
    path = Path(path)
    if not path.exists():
        return MemberIndexGaps(set(), set())
    absent: Set[str] = set()
    unchecked: Set[str] = set()
    for line in path.read_text().splitlines():
        if line.startswith(UNRESOLVED_MARKER):
            absent.add(line[len(UNRESOLVED_MARKER) :].strip())
        elif line.startswith(UNCHECKED_MARKER):
            unchecked.add(line[len(UNCHECKED_MARKER) :].strip())
    return MemberIndexGaps(absent, unchecked)


def write_member_index(
    index: Dict[str, str],
    out_path: Path,
    unresolved: Optional[Set[str]] = None,
    consulted_uniprot: bool = True,
) -> Path:
    """Write the pruned accession -> family index, returning the path written."""
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        "\n".join(render_member_index(index, unresolved, consulted_uniprot)) + "\n"
    )
    return out_path


def load_member_index(path: Path) -> Dict[str, str]:
    """Load a member index TSV written by :func:`write_member_index`.

    Returns an empty mapping when the artifact is absent, so validation degrades
    to "not checkable" rather than failing on a fresh checkout.
    """
    path = Path(path)
    if not path.exists():
        return {}
    index: Dict[str, str] = {}
    for line_number, line in enumerate(path.read_text().splitlines()):
        if line_number == 0 or not line.strip() or line.startswith("#"):
            continue
        accession, _, family_sf = line.partition("\t")
        if family_sf:
            index[accession.strip()] = family_sf.strip()
    return index


def build_member_index(
    accessions: Set[str],
    classification_paths: Iterable[Path],
) -> Dict[str, str]:
    """Build a pruned accession -> family index from organism classifications.

    Only ``accessions`` actually cited in the repository are retained, keeping
    the committed artifact small (a few thousand rows rather than the ~1.5M
    proteins PANTHER classifies).

    >>> import tempfile, pathlib
    >>> d = pathlib.Path(tempfile.mkdtemp())
    >>> _ = (d / "org").write_text(
    ...     "HUMAN|UniProtKB=O14521\\tO14521\\tSDHD\\tPTHR13337:SF6\\tSDH\\n"
    ...     "HUMAN|UniProtKB=P99999\\tP99999\\tOTHER\\tPTHR1:SF1\\tX\\n"
    ... )
    >>> build_member_index({"O14521"}, [d / "org"])
    {'O14521': 'PTHR13337:SF6'}
    """
    index: Dict[str, str] = {}
    for path in classification_paths:
        path = Path(path)
        if not path.exists():
            continue
        for accession, family_sf in parse_sequence_classification(
            path.read_text(errors="replace").splitlines()
        ).items():
            if accession in accessions:
                index.setdefault(accession, family_sf)
    return index


# --------------------------------------------------------------------------- #
# PAINT slice integrity
# --------------------------------------------------------------------------- #

IBD_GAF_URL = "https://data.pantherdb.org/ftp/downloads/paint/current/IBD.gaf"

# GAF columns (0-based) needed to key a node annotation.
_GAF_COL_OBJECT_ID = 1
_GAF_COL_QUALIFIER = 3
_GAF_COL_GO_ID = 4
_GAF_COL_EVIDENCE = 6

PaintRowKey = Tuple[str, str, str, bool]


def fetch_ibd_gaf(cache_dir: Path, force_download: bool = False) -> Path:
    """Download PANTHER's IBD.gaf into ``cache_dir`` (cached)."""
    cache_dir = Path(cache_dir)
    cache_dir.mkdir(parents=True, exist_ok=True)
    dest = cache_dir / "IBD.gaf"
    if dest.exists() and not force_download:
        return dest
    response = requests.get(IBD_GAF_URL, timeout=600)
    response.raise_for_status()
    dest.write_bytes(response.content)
    return dest


def parse_ibd_row_keys(lines: Iterable[str]) -> Set[PaintRowKey]:
    """Extract ``(node, go_id, evidence, negated)`` keys from IBD.gaf lines.

    >>> row = "PANTHER\\tPTN1\\tPTN1\\tNOT\\tGO:1\\tGO_REF:0000033\\tIRD\\t"
    >>> sorted(parse_ibd_row_keys(["!header", row]))
    [('PTN1', 'GO:1', 'IRD', True)]
    """
    keys: Set[PaintRowKey] = set()
    for line in lines:
        if line.startswith("!"):
            continue
        columns = line.rstrip("\n").split("\t")
        if len(columns) <= _GAF_COL_EVIDENCE:
            continue
        keys.add(
            (
                columns[_GAF_COL_OBJECT_ID],
                columns[_GAF_COL_GO_ID],
                columns[_GAF_COL_EVIDENCE],
                columns[_GAF_COL_QUALIFIER].startswith("NOT"),
            )
        )
    return keys


def index_upstream_by_node(keys: Iterable[PaintRowKey]) -> Dict[str, Set[PaintRowKey]]:
    """Group upstream IBD row keys by their PTN node.

    >>> sorted(index_upstream_by_node([("PTN1", "GO:1", "IBD", False)]))
    ['PTN1']
    """
    by_node: Dict[str, Set[PaintRowKey]] = {}
    for key in keys:
        by_node.setdefault(key[0], set()).add(key)
    return by_node


def find_pruned_paint_rows(
    committed: Dict[PaintRowKey, List[str]],
    upstream: Set[PaintRowKey],
) -> Dict[str, Set[PaintRowKey]]:
    """Return upstream rows missing from slices that already carry their node.

    Checking only ``committed - upstream`` is not enough. The loss check
    (``validate_paint_ptns``) can only fire when the slice actually contains the
    ``IRD``/``IKR`` row, so a slice with its loss rows *removed* would defeat it
    while every remaining row still verifies as genuine. Since curation PRs
    commit the very slices their PTN claims are checked against, that omission is
    the more dangerous direction.

    Only nodes already present in a slice are checked -- slices are deliberately
    per-family subsets of PAINT, so absent nodes are not a defect.

    >>> committed = {("PTN1", "GO:1", "IBD", False): ["f.tsv"]}
    >>> upstream = {("PTN1", "GO:1", "IBD", False), ("PTN1", "GO:2", "IRD", True)}
    >>> find_pruned_paint_rows(committed, upstream)
    {'PTN1': {('PTN1', 'GO:2', 'IRD', True)}}
    >>> find_pruned_paint_rows(committed, {("PTN1", "GO:1", "IBD", False)})
    {}
    """
    by_node = index_upstream_by_node(upstream)
    present: Dict[str, Set[PaintRowKey]] = {}
    for key in committed:
        present.setdefault(key[0], set()).add(key)
    pruned: Dict[str, Set[PaintRowKey]] = {}
    for node, rows in present.items():
        missing = by_node.get(node, set()) - rows
        if missing:
            pruned[node] = missing
    return pruned


def load_committed_paint_rows(panther_dir: Path) -> Dict[PaintRowKey, List[str]]:
    """Index committed ``*-paint.tsv`` rows by key -> the files declaring them."""
    import csv

    rows: Dict[PaintRowKey, List[str]] = {}
    for tsv_path in sorted(Path(panther_dir).glob("PTHR*/PTHR*-paint.tsv")):
        with open(tsv_path, newline="") as handle:
            for row in csv.DictReader(handle, delimiter="\t"):
                node = row.get("node")
                if not node:
                    continue
                key = (
                    node,
                    str(row.get("go_id") or ""),
                    str(row.get("evidence") or ""),
                    str(row.get("negated") or "").lower() == "true",
                )
                rows.setdefault(key, []).append(str(tsv_path))
    return rows


# --------------------------------------------------------------------------- #
# Label repair
# --------------------------------------------------------------------------- #

# Matches both `id: PANTHER:PTHR1` and the list-item form `- id: PANTHER:PTHR1`
# (used by `family_terms`), capturing the indent and whether a dash is present.
_LABEL_ID_RE = re.compile(r"^(\s*)(- )?id:\s*(PANTHER:PTHR\d+(?::SF\d+)?)\s*$")
_LABEL_LINE_RE = re.compile(r"^(\s*)label:\s*(.*)$")
_PLAIN_SCALAR_SAFE = re.compile(r"^[A-Za-z0-9][^:#\n]*$")


def emit_yaml_scalar(value: str) -> str:
    """Render a YAML scalar, quoting only when a plain scalar would be unsafe.

    >>> emit_yaml_scalar("SUCCINATE DEHYDROGENASE")
    'SUCCINATE DEHYDROGENASE'
    >>> emit_yaml_scalar("SDHD: mitochondrial")
    '"SDHD: mitochondrial"'
    """
    if _PLAIN_SCALAR_SAFE.match(value) and not value.endswith(" "):
        return value
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


# Words carrying no discriminating signal when comparing two protein names.
_UNINFORMATIVE_NAME_WORDS = frozenset(
    {
        "protein", "family", "member", "subunit", "related", "domain",
        "containing", "putative", "like", "homolog", "type", "chain",
        "component", "and", "the", "not", "named", "mitochondrial",
        "chloroplastic", "isoform", "factor",
    }
)


def _name_tokens(text: str) -> Set[str]:
    return {
        token
        for token in re.split(r"[^a-z0-9]+", (text or "").lower())
        if token and len(token) > 2 and token not in _UNINFORMATIVE_NAME_WORDS
    }


def label_drift(old: str, new: str) -> str:
    """Classify how far an authored label sits from the official name.

    Returns ``"cosmetic"``, ``"partial"`` or ``"divergent"``. A *divergent*
    label -- one sharing no informative word with the official name -- is a
    signal that the **id** is wrong rather than the label: an id guessed at
    random is still a hallucination even when it happens to resolve, and
    silently rewriting its label to the official name is what would hide it.

    >>> label_drift("ALDO-KETO REDUCTASE", "ALDO/KETO REDUCTASE")
    'cosmetic'
    >>> label_drift("CYTOCHROME P450 FAMILY 7", "Cytochrome P450 monooxygenase")
    'cosmetic'
    >>> label_drift("XANTHINE DEHYDROGENASE OXIDASE",
    ...             "XANTHINE PHOSPHORIBOSYLTRANSFERASE")
    'partial'
    >>> label_drift("SUCCINATE DEHYDROGENASE CYTOCHROME B SMALL SUBUNIT",
    ...             "ACIDIC LEUCINE-RICH NUCLEAR PHOSPHOPROTEIN 32")
    'divergent'
    """
    old_tokens, new_tokens = _name_tokens(old), _name_tokens(new)
    if not old_tokens or not new_tokens:
        return "partial"
    shared = old_tokens & new_tokens
    if not shared:
        return "divergent"
    if len(shared) / min(len(old_tokens), len(new_tokens)) < 0.6:
        return "partial"
    return "cosmetic"


def is_placeholder_label(label: str, curie: str) -> bool:
    """True when a label is just the id repeated, bare or as a CURIE.

    The divergence guard exists to stop a label that *names a different protein*
    being overwritten, because that pattern means the id was guessed. A label
    that merely restates its own id makes no claim about any protein, so there
    is nothing to hide and filling it in is safe. Without this exception the
    guard misfires on the ``label: PTHR13190`` convention -- an id shares no
    words with its official name, so every placeholder reads as divergent.

    >>> is_placeholder_label("PTHR13190", "PANTHER:PTHR13190")
    True
    >>> is_placeholder_label("PANTHER:PTHR13190", "PANTHER:PTHR13190")
    True
    >>> is_placeholder_label("SUCCINATE DEHYDROGENASE", "PANTHER:PTHR13190")
    False
    """
    stripped = label.strip()
    return stripped == curie or stripped == curie.split(":", 1)[-1]


def load_obo_names(path: Path) -> Dict[str, str]:
    """Load ``CURIE -> name`` from an OBO file written by :func:`write_panther_obo`."""
    names: Dict[str, str] = {}
    current: Optional[str] = None
    for line in Path(path).read_text().splitlines():
        if line.startswith("id: "):
            current = line[4:].strip()
        elif line.startswith("name: ") and current:
            names[current] = line[6:].strip()
            current = None
    return names


_SUBFAMILY_COUNT_CACHE: Dict[Path, Dict[str, int]] = {}


def load_subfamily_counts(path: Path) -> Dict[str, int]:
    """Count subfamilies per family from the PANTHER OBO (cached).

    Used to judge how much a family-level grounding actually narrows things
    down: a family split into a hundred subfamilies says little about any one
    member beyond shared ancestry.
    """
    path = Path(path)
    if path in _SUBFAMILY_COUNT_CACHE:
        return _SUBFAMILY_COUNT_CACHE[path]
    counts: Dict[str, int] = {}
    if path.exists():
        for match in re.finditer(
            r"^id: PANTHER:(PTHR\d+):SF\d+$", path.read_text(), re.MULTILINE
        ):
            counts[match.group(1)] = counts.get(match.group(1), 0) + 1
    _SUBFAMILY_COUNT_CACHE[path] = counts
    return counts


def rewrite_panther_labels(
    text: str,
    names: Dict[str, str],
    skip_curies: Optional[Set[str]] = None,
    allow_divergent: bool = False,
) -> Tuple[str, List[Tuple[str, str, str]], List[Tuple[str, str, str]]]:
    """Rewrite PANTHER family/subfamily labels to their official PANTHER names.

    Returns ``(new_text, applied, deferred)``, each change a
    ``(curie, old_label, new_label)`` triple.

    Two categories are deliberately NOT rewritten:

    * ``skip_curies`` -- ids whose *grounding* is disputed. Rewriting their
      label would replace an honestly-wrong label with an authoritative one and
      hide the mis-grounding.
    * **divergent** drifts (see :func:`label_drift`), returned in ``deferred``
      unless ``allow_divergent``. When the authored label describes a different
      protein entirely, the likely error is the id, and normalising the label
      would manufacture consistency around a guessed identifier.

    >>> names = {"PANTHER:PTHR1": "ALDO/KETO REDUCTASE"}
    >>> text = "  term:\\n    id: PANTHER:PTHR1\\n    label: ALDO-KETO REDUCTASE\\n"
    >>> new, applied, deferred = rewrite_panther_labels(text, names)
    >>> applied, deferred
    ([('PANTHER:PTHR1', 'ALDO-KETO REDUCTASE', 'ALDO/KETO REDUCTASE')], [])
    >>> print(new, end="")
      term:
        id: PANTHER:PTHR1
        label: ALDO/KETO REDUCTASE

    A divergent label is held back for review instead:

    >>> text = "  term:\\n    id: PANTHER:PTHR1\\n    label: SUCCINATE DEHYDROGENASE\\n"
    >>> new, applied, deferred = rewrite_panther_labels(text, names)
    >>> applied
    []
    >>> deferred
    [('PANTHER:PTHR1', 'SUCCINATE DEHYDROGENASE', 'ALDO/KETO REDUCTASE')]
    >>> new == text
    True
    """
    skip = skip_curies or set()
    lines = text.splitlines(keepends=True)
    changes: List[Tuple[str, str, str]] = []
    deferred: List[Tuple[str, str, str]] = []
    for index, line in enumerate(lines):
        match = _LABEL_ID_RE.match(line.rstrip("\n"))
        if not match or index + 1 >= len(lines):
            continue
        indent, dash, curie = match.group(1), match.group(2), match.group(3)
        if curie in skip:
            continue
        official = names.get(curie)
        if official is None:
            continue
        # A list item's sibling keys are indented past the "- " marker.
        expected_indent = indent + ("  " if dash else "")
        label_match = _LABEL_LINE_RE.match(lines[index + 1].rstrip("\n"))
        if not label_match or label_match.group(1) != expected_indent:
            continue
        current = str(yaml.safe_load(f"v: {label_match.group(2)}")["v"])
        if current.strip() == official:
            continue
        if (
            not allow_divergent
            and not is_placeholder_label(current, curie)
            and label_drift(current, official) == "divergent"
        ):
            deferred.append((curie, current, official))
            continue
        lines[index + 1] = f"{expected_indent}label: {emit_yaml_scalar(official)}\n"
        changes.append((curie, current, official))
    return "".join(lines), changes, deferred


# --------------------------------------------------------------------------- #
# UniProt fallback for accessions PANTHER's per-organism files do not cover
# --------------------------------------------------------------------------- #

UNIPROT_ACCESSIONS_URL = "https://rest.uniprot.org/uniprotkb/accessions"
UNIPROT_BATCH_SIZE = 100


def _best_panther_xref(cross_references: Iterable[dict]) -> Optional[str]:
    """Pick the most specific PANTHER id from a UniProt cross-reference list.

    UniProt lists both the family and the subfamily; the subfamily is preferred
    because it pins the protein more precisely, and callers only ever compare on
    the family part anyway.

    >>> _best_panther_xref([
    ...     {"database": "PANTHER", "id": "PTHR13337"},
    ...     {"database": "PANTHER", "id": "PTHR13337:SF6"},
    ...     {"database": "Pfam", "id": "PF01127"},
    ... ])
    'PTHR13337:SF6'
    >>> _best_panther_xref([{"database": "Pfam", "id": "PF01127"}]) is None
    True
    """
    ids = [
        xref["id"]
        for xref in cross_references
        if xref.get("database") == "PANTHER" and isinstance(xref.get("id"), str)
    ]
    subfamilies = [i for i in ids if SUBFAMILY_RE.match(i)]
    if subfamilies:
        return sorted(subfamilies)[0]
    families = [i for i in ids if FAMILY_RE.match(i)]
    return sorted(families)[0] if families else None


def fetch_panther_from_uniprot(accessions: Iterable[str]) -> Dict[str, str]:
    """Resolve accession -> PANTHER family/subfamily via the UniProt REST API.

    PANTHER's per-organism classification files cover only its ~140 reference
    proteomes, which leaves most curated bacterial accessions unresolvable. Those
    are exactly the entries the family-membership check would otherwise skip, so
    this fills the gap for any organism UniProt knows about.
    """
    import json
    import urllib.parse
    import urllib.request

    pending = sorted(set(accessions))
    resolved: Dict[str, str] = {}
    for start in range(0, len(pending), UNIPROT_BATCH_SIZE):
        batch = pending[start : start + UNIPROT_BATCH_SIZE]
        query = urllib.parse.urlencode(
            {
                "accessions": ",".join(batch),
                "fields": "accession,xref_panther",
                "format": "json",
            }
        )
        with urllib.request.urlopen(
            f"{UNIPROT_ACCESSIONS_URL}?{query}", timeout=120
        ) as handle:
            payload = json.load(handle)
        for record in payload.get("results", []):
            accession = record.get("primaryAccession")
            best = _best_panther_xref(record.get("uniProtKBCrossReferences", []))
            if accession and best:
                resolved[accession] = best
    return resolved
