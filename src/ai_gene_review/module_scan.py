"""Generic detection of module members in target genomes ("gap filling").

A :class:`~ai_gene_review.schema` ``ModuleReview`` document already encodes, for each
grounded leaf annoton, its *family* term(s) (InterPro / PANTHER) and its
*representative-member* / gene-product UniProt exemplars. This module reuses those
groundings to scan arbitrary target genomes for members of the module, by two
independent methods:

* **Family membership** -- for each component that carries an InterPro family term,
  count member proteins in each target proteome's taxon via the InterPro REST API
  (no extra dependencies).
* **Sequence homology** -- ``phmmer`` (via the optional ``pyhmmer`` package, which
  bundles HMMER) of each representative-member sequence against each target reference
  proteome. This is the only way to detect components that have no family model
  (e.g. a plug protein grounded solely by an exemplar).

Nothing here is organism- or module-specific: every grounding is read from the module
document, so the same tool works for any module. Used by the ``ai-gene-review
scan-module`` CLI command.
"""
from __future__ import annotations

import json
import time
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable, Optional

import yaml

INTERPRO = "https://www.ebi.ac.uk/interpro/api"
UNIPROT = "https://rest.uniprot.org"
_UA = {"User-Agent": "ai-gene-review/module-scan"}
DEFAULT_EVALUE = 1e-5


# --------------------------------------------------------------------------- #
# Component extraction from a module document
# --------------------------------------------------------------------------- #
@dataclass
class Component:
    """A grounded module leaf: its label, family term(s) and UniProt exemplar(s)."""

    label: str
    family_terms: list[str] = field(default_factory=list)  # e.g. "InterPro:IPR020360"
    exemplars: list[str] = field(default_factory=list)  # bare UniProt accessions

    @property
    def interpro_terms(self) -> list[str]:
        return [t.split(":", 1)[1] for t in self.family_terms if t.upper().startswith("INTERPRO:")]


def _participant_terms(participant: Any) -> tuple[list[str], list[str]]:
    """Return (family_term_ids, uniprot_exemplars) for one participant selector."""
    fams: list[str] = []
    exes: list[str] = []
    if not isinstance(participant, dict):
        return fams, exes

    def _term_id(holder: Any) -> Optional[str]:
        t = holder.get("term") if isinstance(holder, dict) else None
        return t.get("id") if isinstance(t, dict) else None

    fam = participant.get("family")
    if isinstance(fam, dict):
        if (tid := _term_id(fam)):
            fams.append(tid)
        for ft in fam.get("family_terms") or []:
            if isinstance(ft, dict) and ft.get("id"):
                fams.append(ft["id"])
        for rm in fam.get("representative_members") or []:
            if (rid := _term_id(rm)):
                exes.append(rid)
    for key in ("gene_product", "gene", "homolog_of", "ortholog_of"):
        holder = participant.get(key)
        if isinstance(holder, dict) and (tid := _term_id(holder)):
            exes.append(tid)
    pc = participant.get("protein_complex")
    if isinstance(pc, dict):
        for au in pc.get("active_units") or []:
            f2, e2 = _participant_terms(au.get("participant", {}) if isinstance(au, dict) else {})
            fams += f2
            exes += e2
    return fams, exes


def _iter_annotons(obj: Any) -> Iterable[dict]:
    """Yield every annoton dict anywhere in the module tree."""
    if isinstance(obj, dict):
        for ann in obj.get("annotons") or []:
            if isinstance(ann, dict):
                yield ann
        for v in obj.values():
            yield from _iter_annotons(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from _iter_annotons(v)


def extract_components(module_data: dict) -> list[Component]:
    """Extract the grounded leaf components from a loaded ModuleReview document."""
    root = module_data.get("module", module_data)
    comps: list[Component] = []
    for ann in _iter_annotons(root):
        fams, exes = _participant_terms(ann.get("participant", {}))
        exes = [e.split(":", 1)[1] for e in exes if e.upper().startswith("UNIPROTKB:")]
        # de-dup, preserve order
        fams = list(dict.fromkeys(fams))
        exes = list(dict.fromkeys(exes))
        if not fams and not exes:
            continue
        comps.append(Component(label=ann.get("label") or ann.get("id") or "?",
                               family_terms=fams, exemplars=exes))
    return comps


# --------------------------------------------------------------------------- #
# HTTP helpers
# --------------------------------------------------------------------------- #
def _get(url: str, accept: str = "application/json", timeout: int = 60) -> Optional[bytes]:
    req = urllib.request.Request(url, headers={**_UA, "Accept": accept})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        if getattr(r, "status", 200) == 204:
            return None
        return r.read()


def interpro_members(interpro_id: str, taxon: str, page_size: int = 200) -> list[str]:
    """UniProt accessions in ``taxon`` belonging to an InterPro entry (empty if none)."""
    accs: list[str] = []
    url: Optional[str] = (f"{INTERPRO}/protein/UniProt/entry/InterPro/{interpro_id}"
                          f"/taxonomy/uniprot/{taxon}/?page_size={page_size}")
    while url:
        try:
            raw = _get(url)
        except urllib.error.HTTPError as e:
            if e.code in (204, 404):
                break
            raise
        if not raw:
            break
        data = json.loads(raw)
        for item in data.get("results", []):
            acc = item.get("metadata", {}).get("accession")
            if acc:
                accs.append(acc)
        url = data.get("next")
        time.sleep(0.2)
    return accs


def reference_proteome(taxon: str) -> Optional[str]:
    """Return the reference/representative proteome UPID for a taxon, if any."""
    raw = _get(f"{UNIPROT}/proteomes/search?query=(organism_id:{taxon})&format=json&size=10")
    if not raw:
        return None
    results = json.loads(raw).get("results", [])
    for pref in ("Reference proteome", "Representative proteome"):
        for p in results:
            if p.get("proteomeType") == pref:
                return p.get("id")
    return results[0].get("id") if results else None


def _download(url: str, dest: Path) -> Path:
    if not (dest.exists() and dest.stat().st_size > 0):
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(_get(url, accept="text/plain", timeout=300) or b"")
    return dest


# --------------------------------------------------------------------------- #
# Scans
# --------------------------------------------------------------------------- #
def scan_family_membership(components: list[Component], taxa: list[str]) -> list[dict]:
    """For each component's InterPro family term, count members in each taxon."""
    rows: list[dict] = []
    for c in components:
        iprs = c.interpro_terms
        for tax in taxa:
            if not iprs:
                rows.append(dict(component=c.label, interpro="(none)", taxon=tax,
                                 n_members="NA", members="no family model (homology only)"))
                continue
            for ipr in iprs:
                accs = interpro_members(ipr, tax)
                rows.append(dict(component=c.label, interpro=ipr, taxon=tax,
                                 n_members=len(accs), members=";".join(accs[:10])))
    return rows


def scan_homology(components: list[Component], taxa: list[str],
                  cache_dir: Path, evalue: float = DEFAULT_EVALUE,
                  source_taxon: Optional[str] = None) -> list[dict]:
    """phmmer each component exemplar against each taxon's reference proteome.

    If ``source_taxon`` (the exemplars' organism) is given, each forward best hit is
    reverse-searched against the source proteome and the rows gain ``reciprocal`` and
    ``ortholog`` (= a significant hit that is also a reciprocal best hit) columns, so
    broad-domain hits that are really paralogs are flagged rather than counted as
    orthologs.
    """
    try:
        import pyhmmer  # noqa: F401  (optional dependency)
    except ImportError as e:  # pragma: no cover
        raise RuntimeError(
            "Homology scan requires the 'pyhmmer' package (which bundles HMMER). "
            "Install it with `uv add pyhmmer` / `pip install pyhmmer`."
        ) from e
    import pyhmmer

    cache_dir.mkdir(parents=True, exist_ok=True)
    alph = pyhmmer.easel.Alphabet.amino()

    # load exemplar query sequences (first exemplar per component)
    queries = {}
    for c in components:
        if not c.exemplars:
            continue
        acc = c.exemplars[0]
        fa = _download(f"{UNIPROT}/uniprotkb/{acc}.fasta", cache_dir / f"{acc}.fasta")
        with pyhmmer.easel.SequenceFile(str(fa), digital=True, alphabet=alph) as sf:
            seq = next(iter(sf))
        seq.name = c.label.encode()
        queries[c.label] = (acc, seq)

    # optional reciprocity gate: load the exemplars' source proteome once so each
    # forward best hit can be reverse-searched (a broad-domain hit that is really a
    # paralog then fails the reciprocal check and is flagged as not an ortholog).
    src_block = None
    if source_taxon:
        src_upid = reference_proteome(source_taxon)
        if src_upid:
            src_fa = _download(f"{UNIPROT}/uniprotkb/stream?query=(proteome:{src_upid})"
                               f"&format=fasta&includeIsoform=false", cache_dir / f"{src_upid}.fasta")
            with pyhmmer.easel.SequenceFile(str(src_fa), digital=True, alphabet=alph) as sf:
                src_block = sf.read_block()

    def _seq_name(s) -> str:
        return s.name.decode() if isinstance(s.name, (bytes, bytearray)) else s.name

    rows: list[dict] = []
    for tax in taxa:
        gated = source_taxon is not None and tax != source_taxon and src_block is not None
        upid = reference_proteome(tax)
        if not upid:
            for label, (acc, _q) in queries.items():
                row = dict(component=label, taxon=tax, proteome="(none)", exemplar=acc,
                           best_hit="-", evalue="", pct_id="", detected=False)
                if gated:
                    row.update(reciprocal=False, ortholog=False)
                rows.append(row)
            continue
        fa = _download(f"{UNIPROT}/uniprotkb/stream?query=(proteome:{upid})"
                       f"&format=fasta&includeIsoform=false", cache_dir / f"{upid}.fasta")
        with pyhmmer.easel.SequenceFile(str(fa), digital=True, alphabet=alph) as sf:
            targets = sf.read_block()
        tgt_by_name = {_seq_name(s): s for s in targets} if gated else {}
        for label, (acc, q) in queries.items():
            hits = pyhmmer.plan7.Pipeline(alph).search_seq(q, targets)
            if len(hits) == 0:
                row = dict(component=label, taxon=tax, proteome=upid, exemplar=acc,
                           best_hit="-", evalue="", pct_id="", detected=False)
                if gated:
                    row.update(reciprocal=False, ortholog=False)
                rows.append(row)
                continue
            best = hits[0]
            name = _seq_name(best)
            pct = ""
            try:
                mid = best.best_domain.alignment.identity_sequence
                pct = round(100 * sum(ch.isalpha() for ch in mid) / len(mid), 1) if mid else ""
            except Exception:
                pass
            detected = best.evalue <= evalue
            row = dict(component=label, taxon=tax, proteome=upid, exemplar=acc,
                       best_hit=_acc_from_name(name), evalue=f"{best.evalue:.1e}",
                       pct_id=pct, detected=detected)
            if gated:
                reciprocal = False
                hseq = tgt_by_name.get(name)
                if hseq is not None:
                    rev = pyhmmer.plan7.Pipeline(alph).search_seq(hseq, src_block)
                    if len(rev) > 0:
                        reciprocal = _acc_from_name(_seq_name(rev[0])) == acc
                # ortholog call = a significant hit that is ALSO a reciprocal best hit
                row.update(reciprocal=reciprocal, ortholog=detected and reciprocal)
            rows.append(row)
    return rows


def _acc_from_name(name: str) -> str:
    """Extract a UniProt accession from a FASTA/hit name (``tr|ACC|ID`` -> ``ACC``)."""
    parts = name.split("|")
    return parts[1] if len(parts) >= 2 else name


def scan_rbh(components: list[Component], taxa: list[str], source_taxon: str,
             cache_dir: Path, evalue: float = DEFAULT_EVALUE) -> list[dict]:
    """Reciprocal-best-hit ortholog assignment (disambiguates paralogs).

    For every exemplar of every component: forward-search it against each target
    proteome (best hit H), then reverse-search H against the *source* proteome (the
    exemplars' own organism); the pair is a reciprocal best hit iff H maps back to
    that exemplar. This is what distinguishes true 1:1 orthologs from paralogs when a
    component's family is broad (e.g. tandem amidase paralogs AmiC1/AmiC2).
    """
    try:
        import pyhmmer  # noqa: F401
    except ImportError as e:  # pragma: no cover
        raise RuntimeError("RBH requires 'pyhmmer' (uv add pyhmmer).") from e
    import pyhmmer

    cache_dir.mkdir(parents=True, exist_ok=True)
    alph = pyhmmer.easel.Alphabet.amino()

    def _proteome_block(upid: str):
        fa = _download(f"{UNIPROT}/uniprotkb/stream?query=(proteome:{upid})"
                       f"&format=fasta&includeIsoform=false", cache_dir / f"{upid}.fasta")
        with pyhmmer.easel.SequenceFile(str(fa), digital=True, alphabet=alph) as sf:
            return sf.read_block()

    src_upid = reference_proteome(source_taxon)
    if not src_upid:
        raise RuntimeError(f"No reference proteome for source taxon {source_taxon}")
    src_block = _proteome_block(src_upid)

    # exemplars to test: (component, exemplar_acc)
    pairs = [(c, acc) for c in components for acc in c.exemplars]

    rows: list[dict] = []
    for tax in taxa:
        if tax == source_taxon:
            continue
        tgt_upid = reference_proteome(tax)
        if not tgt_upid:
            continue
        tgt_block = _proteome_block(tgt_upid)
        tgt_by_name = {(s.name.decode() if isinstance(s.name, (bytes, bytearray)) else s.name): s
                       for s in tgt_block}
        for c, acc in pairs:
            fa = _download(f"{UNIPROT}/uniprotkb/{acc}.fasta", cache_dir / f"{acc}.fasta")
            with pyhmmer.easel.SequenceFile(str(fa), digital=True, alphabet=alph) as sf:
                q = next(iter(sf))
            q.name = acc.encode()
            fwd = pyhmmer.plan7.Pipeline(alph).search_seq(q, tgt_block)
            if len(fwd) == 0:
                rows.append(dict(component=c.label, exemplar=acc, taxon=tax,
                                 fwd_hit="-", fwd_evalue="", rev_hit="", reciprocal=False))
                continue
            best = fwd[0]
            hit_full = best.name.decode() if isinstance(best.name, (bytes, bytearray)) else best.name
            hit_acc = _acc_from_name(hit_full)
            # reverse search the hit sequence against the source proteome
            hseq = tgt_by_name.get(hit_full)
            rev_acc = ""
            if hseq is not None:
                rev = pyhmmer.plan7.Pipeline(alph).search_seq(hseq, src_block)
                if len(rev) > 0:
                    rname = rev[0].name.decode() if isinstance(rev[0].name, (bytes, bytearray)) else rev[0].name
                    rev_acc = _acc_from_name(rname)
            rows.append(dict(component=c.label, exemplar=acc, taxon=tax,
                             fwd_hit=hit_acc, fwd_evalue=f"{best.evalue:.1e}",
                             rev_hit=rev_acc, reciprocal=(rev_acc == acc)))
    return rows


def load_module(path: Path) -> dict:
    return yaml.safe_load(Path(path).read_text()) or {}


def scan_module(module_path: Path, taxa: list[str], *, homology: bool = False,
                rbh: bool = False, source_taxon: Optional[str] = None,
                cache_dir: Optional[Path] = None,
                evalue: float = DEFAULT_EVALUE) -> dict[str, list[dict]]:
    """Run the family scan (and optionally homology / RBH) for one module.

    RBH requires ``source_taxon`` -- the taxon of the module's representative-member
    exemplars (e.g. Nostoc PCC 7120 = 103690 for the septal-junction module).
    """
    data = load_module(module_path)
    components = extract_components(data)
    cache = cache_dir or (Path(module_path).parent / ".scan_cache")
    out: dict[str, list[dict]] = {
        "components": [dict(component=c.label, family_terms=";".join(c.family_terms) or "(none)",
                            exemplars=";".join(c.exemplars) or "(none)") for c in components],
        "family_membership": scan_family_membership(components, taxa),
    }
    if homology:
        out["homology"] = scan_homology(components, taxa, cache, evalue, source_taxon=source_taxon)
    if rbh:
        if not source_taxon:
            raise ValueError("rbh=True requires source_taxon (the exemplars' organism taxon id)")
        out["rbh"] = scan_rbh(components, taxa, source_taxon, cache, evalue)
    return out
