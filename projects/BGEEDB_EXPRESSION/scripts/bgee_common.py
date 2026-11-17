"""Shared machinery for the BGEEDB_EXPRESSION pilots.

Three pieces, none of which carries biological conclusions of its own:

1. **Ontology bridge.** GO logical definitions (go-plus) name the anatomy a
   process acts on: ``eye development`` = development
   ``results_in_development_of`` UBERON:0000970 eye. ``go_anatomy`` returns
   those UBERON/CL fillers for a GO term (walking up is_a/part_of/regulates to
   the nearest ancestor that has some, when the term itself has none).
   UBERON + CL give an "is within" closure (is_a, part_of, has soma location)
   and a one-step "develops into" relation (inverse develops_from), so a Bgee
   call on one entity can be compared with a GO anatomy target.

2. **Bgee readers.** The per-species "simple" call files (present *and* absent
   calls per anatomical entity, all stages merged) are streamed and filtered
   to the genes asked for; the REST API supplies stage-resolved present calls
   and OMA orthologs. Everything is cached under ``.cache/bgee_expression``.

3. **Classification.** ``classify_annotation`` compares a GO term's anatomy
   with a gene's calls and returns one of the classes documented in
   ``CLASSES``. It never turns expression into a function claim; it only
   says whether the expression record is consistent with the claim.

Run from the repository root. Ontology files are downloaded on first use.
"""

from __future__ import annotations

import csv
import gzip
import json
import pickle
import time
import urllib.parse
import urllib.request
from collections import defaultdict, deque
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, Optional

REPO = Path(__file__).resolve().parents[3]
PROJECT = REPO / "projects" / "BGEEDB_EXPRESSION"
DATA = PROJECT / "data"
RESULTS = PROJECT / "results"
CACHE = REPO / ".cache" / "bgee_expression"
ONT = CACHE / "ontology"
CALLS = CACHE / "calls"
API_CACHE = CACHE / "api"

BGEE_RELEASE = "Bgee 15.2"
BGEE_API = "https://www.bgee.org/api/"
BGEE_FTP = "https://www.bgee.org/ftp/current/download/calls/expr_calls/"
SPECIES = {"human": ("Homo_sapiens", 9606), "mouse": ("Mus_musculus", 10090)}

ONTOLOGY_URLS = {
    "go-plus.json": "http://purl.obolibrary.org/obo/go/extensions/go-plus.json",
    "uberon-basic.obo": "http://purl.obolibrary.org/obo/uberon/basic.obo",
    "cl.obo": "http://purl.obolibrary.org/obo/cl.obo",
    "mmusdv.obo": "http://purl.obolibrary.org/obo/mmusdv.obo",
}

# Anatomy fillers that say nothing about where a gene acts.
UNINFORMATIVE_TARGETS = {
    "CL:0000000",  # cell
    "CL:0000003",  # native cell
    "CL:0000548",  # animal cell
    "CL:0000255",  # eukaryotic cell
    "UBERON:0000468",  # multicellular organism
    "UBERON:0000061",  # anatomical structure
    "UBERON:0001062",  # anatomical entity
    "UBERON:0000465",  # material anatomical entity
    "UBERON:0010000",  # multicellular anatomical structure
    "UBERON:0000062",  # organ
    "UBERON:0000467",  # anatomical system
}
BROAD_TARGET = 500  # an anatomy with more descendants than this explains only broadly

# Bgee samples that contain nearly everything; never accepted as a "container"
# match (they would make every anatomy-bearing term trivially consistent).
CONTAINER_EXCLUDE = {
    "UBERON:0000465",  # material anatomical entity
    "UBERON:0000467",  # anatomical system
    "UBERON:0000468",  # multicellular organism
    "UBERON:0000922",  # embryo
    "UBERON:0007811",  # craniocervical region
}

# GO -> GO edges walked when a term has no anatomy of its own.
GO_UP_PREDICATES = {
    "is_a",
    "http://purl.obolibrary.org/obo/BFO_0000050",  # part of
    "http://purl.obolibrary.org/obo/RO_0002211",  # regulates
    "http://purl.obolibrary.org/obo/RO_0002212",  # negatively regulates
    "http://purl.obolibrary.org/obo/RO_0002213",  # positively regulates
}

REGULATES = {
    "http://purl.obolibrary.org/obo/RO_0002211",
    "http://purl.obolibrary.org/obo/RO_0002212",
    "http://purl.obolibrary.org/obo/RO_0002213",
}

DEVELOPMENTAL_PROCESS = "GO:0032502"
# A gene product annotated to any of these may act on cells that do not express it.
NONAUTONOMOUS_MARKERS = {
    "GO:0005576",  # extracellular region (extracellular space is obsolete in this GO release)
    "GO:0048018",  # receptor ligand activity (cytokines, hormones, growth factors)
}
# Exosome / vesicle proteomics (HDA) puts intracellular proteins such as MYH9
# under extracellular region; those annotations do not make a product act on
# other cells.
NONAUTONOMOUS_EXCLUDE = {"GO:1903561"}  # extracellular vesicle (includes extracellular exosome)

# Cells whose proteins are made from mRNA transcribed at an earlier stage, so an
# absent call on the mature cell says nothing about the protein being there.
TRANSCRIPTIONALLY_QUIESCENT = {
    "CL:0000019",  # sperm
    "CL:0000232",  # erythrocyte
    "CL:0000233",  # platelet
}

# How the expression record relates to a GO term's anatomy.
CLASSES = {
    "NO_ANATOMY": "the GO term (and its nearest ancestors) names no anatomy; expression cannot speak to it",
    "CONSISTENT_WITHIN": "present call in an entity inside a target (e.g. lens for eye development)",
    "CONSISTENT_PRECURSOR": "present call only in a structure that develops into part of a target",
    "CONSISTENT_CONTAINER": "present call only in a structure that contains a target (whole-organ sample)",
    "CONSISTENT_COLOCATED": "present call in a tissue inside the location of a target cell type (e.g. putamen for oligodendrocyte)",
    "ABSENT": "calls exist inside or around the target, and every one is absent",
    "ABSENT_REGULATOR": "as ABSENT, but the anatomy belongs to a regulated process; a regulator may act from elsewhere",
    "ABSENT_QUIESCENT": "as ABSENT, but every target is a transcriptionally quiescent cell (sperm, erythrocyte, platelet)",
    "ABSENT_DEVELOPMENTAL": "as ABSENT, but the term is developmental and the calls merge all stages (mostly adult)",
    "ABSENT_NONAUTONOMOUS": "as ABSENT, but the gene product is extracellular or a receptor ligand and may act from elsewhere",
    "NO_DATA": "Bgee has no call, present or absent, in or around any target",
}
CONSISTENT = {"CONSISTENT_WITHIN", "CONSISTENT_PRECURSOR", "CONSISTENT_CONTAINER", "CONSISTENT_COLOCATED"}


def curie(iri: str) -> str:
    """``http://purl.obolibrary.org/obo/GO_0001654`` -> ``GO:0001654``.

    >>> curie("http://purl.obolibrary.org/obo/UBERON_0000970")
    'UBERON:0000970'
    >>> curie("is_a")
    'is_a'
    """
    if "/obo/" not in iri:
        return iri
    return iri.rsplit("/", 1)[-1].replace("_", ":", 1)


def is_anatomy(cid: str) -> bool:
    return cid.startswith("UBERON:") or cid.startswith("CL:")


def fetch(url: str, dest: Path, timeout: int = 600) -> Path:
    """Download ``url`` to ``dest`` unless it is already there."""
    if dest.exists() and dest.stat().st_size > 0:
        return dest
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_suffix(dest.suffix + ".part")
    req = urllib.request.Request(url, headers={"User-Agent": "ai-gene-review/bgee-expression"})
    with urllib.request.urlopen(req, timeout=timeout) as r, tmp.open("wb") as fh:
        while chunk := r.read(1 << 20):
            fh.write(chunk)
    tmp.rename(dest)
    return dest


def ontology_file(name: str) -> Path:
    return fetch(ONTOLOGY_URLS[name], ONT / name)


# ---------------------------------------------------------------------------
# OBO parsing (only what the pilots need)
# ---------------------------------------------------------------------------


def parse_obo(path: Path) -> dict[str, dict]:
    """Minimal OBO reader: id -> {name, is_a, rel: [(pred, obj)], props, xref, obsolete}."""
    terms: dict[str, dict] = {}
    cur: Optional[dict] = None
    for raw in path.open(encoding="utf-8"):
        line = raw.rstrip("\n")
        if line.startswith("["):
            cur = {"is_a": [], "rel": [], "props": {}, "xref": []} if line == "[Term]" else None
            continue
        if cur is None or ": " not in line:
            continue
        tag, val = line.split(": ", 1)
        val = val.split(" ! ")[0].strip()
        if tag == "id":
            cur["id"] = val
            terms[val] = cur
        elif tag == "name":
            cur["name"] = val
        elif tag == "is_a":
            cur["is_a"].append(val.split()[0])
        elif tag == "relationship":
            parts = val.split()
            if len(parts) >= 2:
                cur["rel"].append((parts[0], parts[1]))
        elif tag == "property_value":
            parts = val.split()
            if len(parts) >= 2:
                cur["props"][parts[0]] = parts[1].strip('"')
        elif tag == "xref":
            cur["xref"].append(val.split()[0])
        elif tag == "is_obsolete" and val == "true":
            cur["obsolete"] = True
    return terms


# ---------------------------------------------------------------------------
# Anatomy graph (UBERON + CL)
# ---------------------------------------------------------------------------

WITHIN_PREDICATES = {"part_of", "BFO:0000050", "RO:0002100"}  # part of; has soma location
DEVELOPS_FROM = {"develops_from", "RO:0002202"}


@dataclass
class Anatomy:
    names: dict[str, str]
    up: dict[str, set[str]]  # entity -> direct is_a/part_of/soma-location parents
    part_up: dict[str, set[str]]  # entity -> direct part_of/soma-location parents only
    develops_into: dict[str, set[str]]  # precursor -> structures that develop from it
    _anc: dict[str, frozenset[str]] = field(default_factory=dict)
    _desc: dict[str, int] = field(default_factory=dict)
    _desc_sets: dict[str, set[str]] = field(default_factory=dict)
    _part_desc: dict[str, set[str]] = field(default_factory=dict)

    def ancestors(self, e: str) -> frozenset[str]:
        """Reflexive is_a/part_of closure ("e is within a")."""
        hit = self._anc.get(e)
        if hit is not None:
            return hit
        seen = {e}
        todo = deque([e])
        while todo:
            x = todo.popleft()
            for p in self.up.get(x, ()):
                if p not in seen:
                    seen.add(p)
                    todo.append(p)
        out = frozenset(seen)
        self._anc[e] = out
        return out

    def within(self, e: str, target: str) -> bool:
        return target in self.ancestors(e)

    def precursor_of(self, e: str, target: str) -> bool:
        """``e`` develops (one step) into something inside ``target``."""
        return any(self.within(y, target) for y in self.develops_into.get(e, ()))

    def contains(self, e: str, target: str) -> bool:
        return e not in CONTAINER_EXCLUDE and e in self.ancestors(target)

    def descendants(self, e: str) -> set[str]:
        """Everything within ``e`` (reflexive; is_a and part_of)."""
        if not self._desc_sets:
            sets: dict[str, set[str]] = defaultdict(set)
            for x in self.names:
                for a in self.ancestors(x):
                    sets[a].add(x)
            self._desc_sets.update(sets)
        return self._desc_sets.get(e, {e})

    def descendant_count(self, e: str) -> int:
        """How many UBERON/CL classes lie within ``e`` (a breadth measure)."""
        return len(self.descendants(e))

    def parts(self, e: str) -> set[str]:
        """Everything that is part of ``e`` through part_of chains only.

        A sample of "muscle tissue" consists of its parts, not of every
        subclass of muscle tissue (muscularis mucosae of the intestine is one).
        """
        if not self._part_desc:
            rev: dict[str, set[str]] = defaultdict(set)
            for x, ps in self.part_up.items():
                for p in ps:
                    rev[p].add(x)
            self._part_desc["__built__"] = set()
            self._part_rev = rev  # type: ignore[attr-defined]
        hit = self._part_desc.get(e)
        if hit is not None:
            return hit
        rev = self._part_rev  # type: ignore[attr-defined]
        seen = {e}
        todo = [e]
        while todo:
            x = todo.pop()
            for c in rev.get(x, ()):
                if c not in seen:
                    seen.add(c)
                    todo.append(c)
        self._part_desc[e] = seen
        return seen

    def overlaps(self, sample: str, loc: str) -> bool:
        """The sampled structure has a part within ``loc`` (or one contains the other)."""
        if self.within(sample, loc) or self.within(loc, sample):
            return True
        inside = self.descendants(loc)
        return any(x in inside for x in self.parts(sample))

    def colocated(self, e: str, target: str) -> bool:
        """A cell type whose location overlaps the sampled structure ``e``.

        CL places oligodendrocytes ``part_of`` the CNS, not of each brain
        region, so a putamen sample neither contains nor lies within the cell
        type; it is co-located with it. Likewise an intestinal epithelial cell
        (part of the intestinal mucosa) is co-located with a rectum sample,
        which has a mucosa. Only locations no broader than the CNS count.
        """
        if not target.startswith("CL:") or e in CONTAINER_EXCLUDE:
            return False
        for loc in self.locations(target):
            if self.descendant_count(loc) <= 3000 and self.overlaps(e, loc):
                return True
        return False

    def locations(self, cell: str, depth: int = 2) -> set[str]:
        """UBERON structures a cell type is part of: its direct part_of (or soma
        location) parents and their parents, ``depth`` steps, never via is_a.

        Two steps keep beta cell -> islet -> endocrine pancreas but stop before
        endocrine system (which would co-locate beta cells with the adrenal).
        """
        level = set(self.part_up.get(cell, ()))
        seen = set(level)
        for _ in range(depth - 1):
            level = {p for x in level for p in self.part_up.get(x, ())} - seen
            seen |= level
        return {x for x in seen if x.startswith("UBERON:")}

    def name(self, e: str) -> str:
        return self.names.get(e, e)


def load_anatomy() -> Anatomy:
    pkl = CACHE / "anatomy.pkl"
    if pkl.exists():
        with pkl.open("rb") as fh:
            return pickle.load(fh)
    names: dict[str, str] = {}
    up: dict[str, set[str]] = defaultdict(set)
    part_up: dict[str, set[str]] = defaultdict(set)
    dev: dict[str, set[str]] = defaultdict(set)
    for fname in ("uberon-basic.obo", "cl.obo"):
        for tid, t in parse_obo(ontology_file(fname)).items():
            if not is_anatomy(tid) or t.get("obsolete"):
                continue
            names.setdefault(tid, t.get("name", tid))
            for p in t["is_a"]:
                if is_anatomy(p):
                    up[tid].add(p)
            for pred, obj in t["rel"]:
                if not is_anatomy(obj):
                    continue
                if pred in WITHIN_PREDICATES:
                    up[tid].add(obj)
                    part_up[tid].add(obj)
                elif pred in DEVELOPS_FROM:
                    dev[obj].add(tid)
    an = Anatomy(names=names, up=dict(up), part_up=dict(part_up), develops_into=dict(dev))
    with pkl.open("wb") as fh:
        pickle.dump(an, fh)
    return an


# ---------------------------------------------------------------------------
# GO -> anatomy (go-plus logical definitions and existential edges)
# ---------------------------------------------------------------------------


@dataclass
class GoAnatomy:
    names: dict[str, str]
    namespaces: dict[str, str]  # GO id -> biological_process | molecular_function | cellular_component
    direct: dict[str, set[tuple[str, str]]]  # GO id -> {(relation, UBERON/CL id)}
    parent_edges: dict[str, set[tuple[str, str]]]  # GO id -> {(GO parent, predicate)}
    version: str

    def targets(self, go_id: str, max_depth: int = 4) -> tuple[set[tuple[str, str]], Optional[str], int]:
        """Anatomy of ``go_id``, else of its nearest ancestors that have some.

        Returns (targets, source term, distance). Distance 0 = the term's own
        logical definition. Uninformative fillers (cell, organism) are dropped.
        """
        found, src, depth, _ = self.targets_with_mode(go_id, max_depth)
        return found, src, depth

    def targets_with_mode(
        self, go_id: str, max_depth: int = 4
    ) -> tuple[set[tuple[str, str]], Optional[str], int, bool]:
        """As ``targets``, plus whether the anatomy was reached only through a
        ``regulates`` edge (a regulator need not be expressed where the
        regulated process happens: secreted factors, hormones, guidance cues).
        """
        frontier = {go_id: False}  # term -> reached via a regulates edge
        seen = {go_id}
        for depth in range(max_depth + 1):
            found: set[tuple[str, str]] = set()
            src = None
            modes = []
            for t in sorted(frontier):
                hits = {(r, a) for r, a in self.direct.get(t, ()) if a not in UNINFORMATIVE_TARGETS}
                if hits:
                    found |= hits
                    src = src or t
                    modes.append(frontier[t])
            if found:
                return found, src, depth, all(modes)
            nxt: dict[str, bool] = {}
            for t, via_reg in frontier.items():
                for p, pred in self.parent_edges.get(t, ()):
                    if p not in seen:
                        seen.add(p)
                        nxt[p] = via_reg or pred in REGULATES
                    elif p in nxt and not (via_reg or pred in REGULATES):
                        nxt[p] = False
            frontier = nxt
            if not frontier:
                break
        return set(), None, -1, False

    def ancestors(self, go_id: str) -> set[str]:
        """Reflexive closure over is_a / part_of / regulates."""
        seen = {go_id}
        todo = [go_id]
        while todo:
            x = todo.pop()
            for p, _ in self.parent_edges.get(x, ()):
                if p not in seen:
                    seen.add(p)
                    todo.append(p)
        return seen

    def is_developmental(self, go_id: str) -> bool:
        return DEVELOPMENTAL_PROCESS in self.ancestors(go_id)

    @property
    def parents(self) -> dict[str, set[str]]:
        return {k: {p for p, _ in v} for k, v in self.parent_edges.items()}


def load_go_anatomy() -> GoAnatomy:
    pkl = CACHE / "go_anatomy.pkl"
    if pkl.exists():
        with pkl.open("rb") as fh:
            return pickle.load(fh)
    g = json.load(ontology_file("go-plus.json").open())["graphs"][0]
    names, namespaces = {}, {}
    for n in g["nodes"]:
        cid = curie(n["id"])
        if cid.startswith("GO:") and "lbl" in n:
            names[cid] = n["lbl"]
            for bpv in n.get("meta", {}).get("basicPropertyValues", []):
                if bpv.get("pred", "").endswith("hasOBONamespace"):
                    namespaces[cid] = bpv["val"]
    direct: dict[str, set[tuple[str, str]]] = defaultdict(set)
    for ax in g.get("logicalDefinitionAxioms", []):
        sub = curie(ax["definedClassId"])
        if not sub.startswith("GO:"):
            continue
        for r in ax.get("restrictions", []):
            obj = curie(r["fillerId"])
            if is_anatomy(obj):
                direct[sub].add((curie(r["propertyId"]), obj))
    parents: dict[str, set[tuple[str, str]]] = defaultdict(set)
    for e in g["edges"]:
        sub, obj, pred = curie(e["sub"]), curie(e["obj"]), e["pred"]
        if not sub.startswith("GO:"):
            continue
        if is_anatomy(obj) and pred != "is_a":
            direct[sub].add((curie(pred), obj))
        elif obj.startswith("GO:") and pred in GO_UP_PREDICATES:
            parents[sub].add((obj, pred))
    version = g.get("meta", {}).get("version", "")
    ga = GoAnatomy(names=names, namespaces=namespaces, direct=dict(direct), parent_edges=dict(parents), version=version)
    with pkl.open("wb") as fh:
        pickle.dump(ga, fh)
    return ga


# ---------------------------------------------------------------------------
# Bgee calls
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Call:
    entity: str
    name: str
    state: str  # present | absent
    quality: str  # gold | silver
    score: float  # Bgee expression score 0-100 (rank-based, comparable across genes)


def simple_calls_file(species: str) -> Path:
    fname = f"{SPECIES[species][0]}_expr_simple.tsv.gz"
    return fetch(BGEE_FTP + fname, CALLS / fname, timeout=1800)


def read_simple_calls(species: str, gene_ids: Iterable[str]) -> dict[str, list[Call]]:
    """Present and absent calls (all stages merged) for the requested Ensembl genes."""
    wanted = set(gene_ids)
    out: dict[str, list[Call]] = defaultdict(list)
    with gzip.open(simple_calls_file(species), "rt") as fh:
        reader = csv.reader(fh, delimiter="\t")
        next(reader)
        for row in reader:
            if row[0] not in wanted:
                continue
            quality = row[5].split()[0]
            try:
                score = float(row[7])
            except ValueError:
                score = float("nan")
            out[row[0]].append(Call(row[2], row[3].strip('"'), row[4], quality, score))
    return dict(out)


def write_calls_tsv(calls: dict[str, list[Call]], symbols: dict[str, str], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["gene_id", "symbol", "entity", "entity_name", "state", "quality", "score"])
        for gid in sorted(calls):
            for c in sorted(calls[gid], key=lambda c: (-c.score if c.score == c.score else 0, c.entity)):
                w.writerow([gid, symbols.get(gid, ""), c.entity, c.name, c.state, c.quality, c.score])


def read_calls_tsv(path: Path) -> tuple[dict[str, list[Call]], dict[str, str]]:
    calls: dict[str, list[Call]] = defaultdict(list)
    symbols: dict[str, str] = {}
    with path.open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            symbols[row["gene_id"]] = row["symbol"]
            calls[row["gene_id"]].append(
                Call(row["entity"], row["entity_name"], row["state"], row["quality"], float(row["score"]))
            )
    return dict(calls), symbols


def bgee_api(params: dict[str, object], cache_name: str) -> dict:
    """GET the Bgee REST API with a JSON cache. ``params`` may hold lists."""
    path = API_CACHE / cache_name
    if path.exists():
        return json.loads(path.read_text())
    query = urllib.parse.urlencode({**params, "display_type": "json"}, doseq=True)
    req = urllib.request.Request(BGEE_API + "?" + query, headers={"User-Agent": "ai-gene-review/bgee-expression"})
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                data = json.loads(r.read().decode())
            break
        except Exception:  # noqa: BLE001 - network retries
            if attempt == 3:
                raise
            time.sleep(2 ** (attempt + 1))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data))
    return data


def stage_calls(gene_id: str, species_id: int) -> list[dict]:
    """Present calls per (anatomical entity, developmental stage) from the API."""
    data = bgee_api(
        {
            "page": "gene",
            "action": "expression",
            "gene_id": gene_id,
            "species_id": species_id,
            "cond_param": ["anat_entity", "dev_stage"],
            "data_type": "all",
        },
        f"expr_stage_{species_id}_{gene_id}.json",
    )
    return data.get("data", {}).get("calls", [])


def orthologs(gene_id: str, species_id: int, target_species: int) -> list[tuple[str, str]]:
    """OMA orthologs (Bgee homologs endpoint) of ``gene_id`` in ``target_species``."""
    data = bgee_api(
        {"page": "gene", "action": "homologs", "gene_id": gene_id, "species_id": species_id},
        f"homologs_{species_id}_{gene_id}.json",
    )
    hits = []
    for grp in data.get("data", {}).get("orthologsByTaxon", []):
        for g in grp.get("genes", []):
            if g.get("species", {}).get("id") == target_species:
                hits.append((g["geneId"], g.get("name", "")))
    return sorted(set(hits))


def bgee_gene_id(uniprot_txt: Path) -> Optional[str]:
    """Ensembl gene id from the ``DR   Bgee;`` line of a cached UniProt record."""
    if not uniprot_txt.exists():
        return None
    for line in uniprot_txt.open():
        if line.startswith("DR   Bgee;"):
            return line.split(";")[1].strip()
    return None


# ---------------------------------------------------------------------------
# Classification
# ---------------------------------------------------------------------------


@dataclass
class Verdict:
    cls: str
    targets: list[str]
    source_term: Optional[str]
    distance: int
    evidence: list[str]  # entity ids behind the verdict


def classify_annotation(
    go_id: str,
    calls: list[Call],
    go: GoAnatomy,
    anat: Anatomy,
    min_score: float = 0.0,
    qualities: tuple[str, ...] = ("gold", "silver"),
    nonautonomous: bool = False,
    stage_resolved: bool = False,
) -> Verdict:
    """Compare a GO term's anatomy with a gene's Bgee calls (see ``CLASSES``)."""
    tg, src, dist, via_regulates = go.targets_with_mode(go_id)
    targets = sorted({a for _, a in tg})
    if not targets:
        return Verdict("NO_ANATOMY", [], None, -1, [])
    calls = [c for c in calls if c.quality in qualities]
    present = [c for c in calls if c.state == "present" and c.score >= min_score]
    for kind, test in (
        ("CONSISTENT_WITHIN", anat.within),
        ("CONSISTENT_PRECURSOR", anat.precursor_of),
        ("CONSISTENT_CONTAINER", anat.contains),
        ("CONSISTENT_COLOCATED", anat.colocated),
    ):
        ev = sorted({c.entity for c in present for t in targets if test(c.entity, t)})
        if ev:
            return Verdict(kind, targets, src, dist, ev)
    related = [
        c
        for c in calls
        if any(
            anat.within(c.entity, t) or anat.contains(c.entity, t) or anat.precursor_of(c.entity, t) or anat.colocated(c.entity, t)
            for t in targets
        )
    ]
    if related:
        # every related call is absent, or present but below the score bar
        ev = sorted({c.entity for c in related})
        if all(anat.ancestors(t) & TRANSCRIPTIONALLY_QUIESCENT for t in targets):
            return Verdict("ABSENT_QUIESCENT", targets, src, dist, ev)
        if not stage_resolved and go.is_developmental(go_id):
            return Verdict("ABSENT_DEVELOPMENTAL", targets, src, dist, ev)
        if via_regulates:
            return Verdict("ABSENT_REGULATOR", targets, src, dist, ev)
        if nonautonomous:
            return Verdict("ABSENT_NONAUTONOMOUS", targets, src, dist, ev)
        return Verdict("ABSENT", targets, src, dist, ev)
    return Verdict("NO_DATA", targets, src, dist, [])


def nonautonomous_genes(rows: Iterable[dict], go: GoAnatomy, rejected: set[str]) -> set[str]:
    """Genes with a non-rejected annotation under ``NONAUTONOMOUS_MARKERS``."""
    memo: dict[str, bool] = {}
    out = set()
    for r in rows:
        if r.get("negated") or r.get("action") in rejected:
            continue
        gid = r["go_id"]
        if gid not in memo:
            anc = go.ancestors(gid)
            memo[gid] = bool(anc & NONAUTONOMOUS_MARKERS) and not (anc & NONAUTONOMOUS_EXCLUDE)
        if memo[gid]:
            out.add(r["gene"])
    return out


def explain_tissue(entity: str, targets: set[str], anat: Anatomy) -> Optional[tuple[str, str, bool]]:
    """How (if at all) a function's anatomy explains expression in ``entity``.

    Returns (relation, the most specific explaining target, broad?) or None.
    """
    for kind, test in (
        ("within", anat.within),
        ("precursor", anat.precursor_of),
        ("container", anat.contains),
        ("colocated", anat.colocated),
    ):
        hits = [t for t in targets if test(entity, t)]
        if hits:
            best = min(hits, key=anat.descendant_count)
            return kind, best, anat.descendant_count(best) > BROAD_TARGET
    return None
