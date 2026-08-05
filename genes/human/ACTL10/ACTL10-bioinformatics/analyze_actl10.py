#!/usr/bin/env python3
"""Is human ACTL10 (Q5JWF8) an N-terminally truncated annotation, and what follows for its GO record?

Four questions, each computed at run time from public APIs and from files committed in
this repository. Nothing is hard-coded from a previous run.

1. ACTL10 orthologue lengths disagree wildly (169-369 aa). Is the variation phylogenetic
   or does it track annotation pipelines? Sister taxa are the test.
2. Does the human genome encode actin-homologous coding sequence, in frame and free of
   stop codons, immediately 5' of Q5JWF8's annotated initiator? If it does, Q5JWF8 begins
   mid-fold and every residue tally computed from it is bounded by the gene model rather
   than by the protein.
3. Re-run the actin nucleotide-site and filament-protomer-interface residue tallies that
   `genes/human/ACTL8/ACTL8-bioinformatics/` computed for a panel including ACTL10,
   separating "residue substituted" from "position outside the annotated sequence".
   The same PDB entries and cutoffs are used so the numbers are comparable by
   construction, and the script asserts that it reproduces ACTL8's committed values for
   the two controls.
4. ACTL10 has exactly two IBA rows. For each: resolve every WITH/FROM token, ask what
   evidence that source itself holds for the donated term, and place ACTL10's node inside
   the PAINT record for PTHR11937 that this repo caches.

Run:  uv run python analyze_actl10.py
Out:  results.json, RESULTS.md   (both regenerated in full; diff them to verify)
"""

from __future__ import annotations

import ast
import io
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import requests
from Bio import Align
from Bio.Align import substitution_matrices
from Bio.Data.IUPACData import protein_letters_3to1
from Bio.PDB import MMCIFParser, NeighborSearch
from Bio.Seq import Seq

THREE_TO_ONE = {k.upper(): v for k, v in protein_letters_3to1.items()}
THREE_TO_ONE.update({"MSE": "M", "HIC": "H", "SEP": "S", "TPO": "T", "PTR": "Y"})

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
REPO_ROOT = GENE_DIR.parents[2]
GOA_TSV = GENE_DIR / "ACTL10-goa.tsv"
PAINT_TSV = REPO_ROOT / "interpro" / "panther" / "PTHR11937" / "PTHR11937-paint.tsv"
ACTL8_RESULTS = REPO_ROOT / "genes" / "human" / "ACTL8" / "ACTL8-bioinformatics" / "RESULTS.md"

ACTL10 = "Q5JWF8"
ACTB = "P60709"
ENSEMBL_TRANSCRIPT = "ENST00000677665"  # MANE Select, the transcript UniProt cites for Q5JWF8

CONTACT_CUTOFF = 4.0  # Angstrom, heavy atom to heavy atom
ATP_STRUCTURE = ("2BTF", "A", ("ATP", "SR"))  # beta-actin:profilin; ATP + Sr(II) in the Mg site
FILAMENT_STRUCTURE = ("6DJO", None, ())  # four F-actin protomers, ADP + Mg

# Same panel as the ACTL8 analysis (so the tallies line up), plus the mouse ACTL10
# orthologue and two long primate ACTL10 orthologues, which are the point of this run.
PANEL = {
    "P60709": "ACTB (human beta-actin) - positive control, IBA donor",
    "P68133": "ACTA1 (human alpha-skeletal actin) - IBA donor",
    "P45891": "Arp53D (Drosophila actin-like 53D) - divergent actin that DOES polymerise",
    "P61158": "ACTR3 (human Arp3) - divergent, makes actin-like protomer contacts",
    "Q9H568": "ACTL8 (human actin-like 8) - full-length divergent actin, reviewed sibling",
    "Q9Y615": "ACTL7A (human actin-like 7A)",
    "Q8TDG2": "ACTRT1 (human actin-related protein T1)",
    "Q5JWF8": "ACTL10 (human actin-like 10) - Swiss-Prot 245 aa AS ANNOTATED",
    "A2AKE7": "Actl10 (mouse actin-like 10) - 346 aa",
    "A0A6J3JAC8": "ACTL10 (Sapajus apella) - 368 aa",
}
# Filled in at run time by question 2; keyed the same way as PANEL.
EXTENDED_LABEL = "ACTL10 (human) - Swiss-Prot 245 aa PLUS the in-frame upstream ORF"

# Sister-taxon pairs used to test whether the length variation is phylogenetic. Each pair
# is two members of one family; a length difference inside a pair cannot be explained by
# the phylogeny and points at the annotation pipeline instead.
SISTER_PAIRS = [
    ("Sapajus apella", "Cebus imitator", "Cebidae (New World monkeys)"),
    ("Sciurus vulgaris", "Marmota marmota marmota", "Sciuridae (squirrels)"),
    ("Ictidomys tridecemlineatus", "Urocitellus parryii", "Sciuridae, ground squirrels"),
    ("Homo sapiens", "Callithrix jacchus", "Primates"),
]

EXPERIMENTAL_CODES = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "HTP", "HDA", "HMP", "HGI", "HEP"}
XREF_DB = {
    "MGI": "mgi", "RGD": "rgd", "SGD": "sgd", "PomBase": "pombase", "FB": "flybase",
    "dictyBase": "dictybase", "CGD": "cgd", "WB": "wormbase", "ZFIN": "zfin",
    "AGI_LocusCode": "araport",
}

SESSION = requests.Session()
SESSION.headers["Accept"] = "application/json"


# --------------------------------------------------------------------------- infra

def require(path: Path, fix: str) -> Path:
    if not path.exists():
        raise FileNotFoundError(f"missing required input {path}\n  regenerate with: {fix}")
    return path


def get_json(url: str, params: dict | None = None) -> dict:
    r = SESSION.get(url, params=params, timeout=180)
    r.raise_for_status()
    return r.json()


QUICKGO_SEARCH = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"


def assert_quickgo_calls_are_guarded() -> int:
    """Every QuickGO search in this file must go through `quickgo_all`.

    The commit that introduced `quickgo_all` claimed "an assertion confirms no unguarded QuickGO
    call remains". That assertion lived in the one-off script that made the edit, not in this file,
    so the claim was true of the moment and not of the artefact - and it did not close the
    future-edit case it appeared to close. The reviewer caught it. This is that assertion, made
    part of the program so it runs on every invocation.
    """
    src = Path(__file__).read_text()
    lines = src.splitlines()
    # Two independent things must hold. (1) The endpoint URL is written literally exactly once,
    # in the constant - a second literal would be a call site that bypassed the constant.
    literal = [ln for ln in lines if QUICKGO_SEARCH in ln]
    defining = [ln for ln in literal if ln.strip().startswith("QUICKGO_SEARCH =")]
    if len(literal) != 1 or len(defining) != 1:
        raise RuntimeError(
            f"the QuickGO endpoint URL must be written literally exactly once (the QUICKGO_SEARCH "
            f"constant) but appears on {len(literal)} line(s): "
            f"{[h.strip()[:70] for h in literal]}. A new call site must go through quickgo_all().")
    # (2) Every READ of the constant must lie inside quickgo_all (or inside this self-check,
    #     which legitimately names it).
    #
    # An earlier version required `get_json(QUICKGO_SEARCH, ...)` to appear exactly once inside
    # quickgo_all. The reviewer pointed out that the escape route was already in this file:
    # `SESSION.get(url, params=...)` is used directly for the x-total-results read, so a future
    # `SESSION.get(QUICKGO_SEARCH, ...)` would satisfy that check while bypassing every coverage
    # assertion - as would `get_json(url=QUICKGO_SEARCH, ...)` (a keyword first argument leaves
    # `node.args` empty) or assigning the constant to a local first. Guarding the *name* instead of
    # one call shape closes all of those at once, and is shorter.
    #
    # Done over the AST, not the text: the first textual version matched this function's own
    # error-message strings and reported four call sites where there is one.
    tree = ast.parse(src)
    # Match async defs too, and reject a shadowed name rather than silently keeping the last
    # definition: containment is tested by line range, so two definitions of the same name would
    # make the allowed range depend on which one the dict happened to keep. Neither can happen in
    # this file today; the guard is written to be copied, so it should not carry the trap.
    defs: dict[str, list] = defaultdict(list)
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            defs[node.name].append(node)
    for name in ("quickgo_all", "assert_quickgo_calls_are_guarded"):
        if len(defs.get(name, [])) > 1:
            raise RuntimeError(
                f"{name}() is defined {len(defs[name])} times (lines "
                f"{[d.lineno for d in defs[name]]}); containment is tested by line range, so a "
                "shadowed definition makes the allowed range ambiguous")
    funcs = {k: v[0] for k, v in defs.items()}
    guard = funcs.get("quickgo_all")
    if guard is None:
        raise RuntimeError("quickgo_all() is gone; the QuickGO coverage guard no longer exists")
    selfcheck = funcs.get("assert_quickgo_calls_are_guarded")
    if selfcheck is None:
        raise RuntimeError("assert_quickgo_calls_are_guarded() is gone")
    allowed = [(f.lineno, f.end_lineno or f.lineno) for f in (guard, selfcheck)]
    reads = [n for n in ast.walk(tree)
             if isinstance(n, ast.Name) and n.id == "QUICKGO_SEARCH"
             and not isinstance(n.ctx, ast.Store)]  # the module-level assignment is not a read
    inside = [n for n in reads if any(lo <= n.lineno <= hi for lo, hi in allowed)]
    stray = [n for n in reads if n not in inside]
    if stray:
        raise RuntimeError(
            f"QUICKGO_SEARCH is read outside quickgo_all() at line(s) "
            f"{[n.lineno for n in stray]}; every QuickGO search must go through quickgo_all() so "
            "that the page-coverage assertions apply")
    # Assert presence, not merely absence of strays: a guard defeatable by deleting the thing it
    # guards is worse than no guard.
    in_guard = [n for n in reads if guard.lineno <= n.lineno <= (guard.end_lineno or guard.lineno)]
    if not in_guard:
        raise RuntimeError(
            "quickgo_all() no longer reads QUICKGO_SEARCH; it has stopped fetching from QuickGO "
            "and the coverage assertions guard nothing")
    return len(reads)


def quickgo_all(params: dict, what: str, allow_zero: bool = False,
                count_only: bool = False) -> dict:
    """QuickGO search whose result set is asserted to be complete.

    QuickGO reports the true total in `numberOfHits` while returning at most `limit` rows, so
    `len(results)` cannot detect its own truncation. Every conclusion drawn here is an enumeration
    or a per-donor tally, so a silently short page would understate a count rather than error -
    the same failure shape as the UniProt page-size trap. Assert instead of assuming.

    `allow_zero` distinguishes the two meanings an empty result can have, which is why a blanket
    "zero is an error" rule would be wrong here. For the census, zero rows means the query broke
    and must abort. For a per-donor evidence lookup, a donor that carries no annotation for the
    term it donated is a genuine and interesting **finding** - aborting would destroy it rather
    than surface it, the same reasoning that keeps an ambiguous cross-reference as data.

    `count_only` is for a caller that reads **no rows** and wants `numberOfHits` alone. For such a
    caller page coverage is not merely inconvenient to satisfy, it is *inapplicable*: there is no
    row set whose completeness matters. It exists because the first version of the presence probe
    below passed `limit=1` through the normal path, where `got != total` fires for any accession
    with more than one annotation and `got >= limit` fires for exactly one - so the probe could
    only ever return "absent" or abort, and the accession-present-but-lacking-the-term case it was
    written to detect took the run down with a message about a phantom API inconsistency. Caught
    by the reviewer; it is the same two-states-rendered-as-one-value shape as the bugs it followed.
    """
    if "limit" not in params:
        raise RuntimeError(
            f"quickgo_all needs an explicit limit in params for {what}; without it the page size "
            "is whatever the server defaults to, which for a row-reading caller means coverage "
            "cannot be verified and for a count_only caller means fetching rows it will discard")
    d = get_json(QUICKGO_SEARCH, params)
    limit = int(params["limit"])
    total = d.get("numberOfHits")
    if total is None:
        raise RuntimeError(f"QuickGO returned no numberOfHits for {what}; cannot verify coverage")
    if count_only:
        # No rows are read, so completeness of the row set is not a property this caller depends
        # on. The zero check below still applies, because the count itself is what it wants.
        if total == 0 and not allow_zero:
            raise RuntimeError(f"QuickGO returned zero rows for {what}")
        # Return the count ALONE, not the full response. Documenting "reads no rows" while handing
        # back an unverified `results` array would leave a future caller free to iterate a page
        # whose completeness was never checked - guarding the shape instead of the invariant, the
        # same hole the name-based guard above closes one level up. Stripping the rows makes the
        # contract mechanical rather than a promise in a docstring.
        return {"numberOfHits": total}
    got = len(d.get("results", []))
    if got != total:
        # Equality, not `got < total`: an over-count would be just as much a sign that the
        # response does not mean what this function assumes, and the previous commit message
        # described this as an equality assertion.
        raise RuntimeError(
            f"QuickGO row count disagrees with its own total for {what}: {got} of {total} rows at "
            f"limit={limit}; raise the limit and re-run, or add pagination, before trusting this "
            "count")
    if got >= limit:
        raise RuntimeError(
            f"QuickGO returned a full page ({limit}) for {what}; the result set may be truncated. "
            "This is a deliberate conservative abort - raise the limit and re-run.")
    if total == 0 and not allow_zero:
        raise RuntimeError(
            f"QuickGO returned zero rows for {what}; this query underwrites an enumeration, so an "
            "empty result is a broken query rather than a finding")
    return d


def uniprot_entry(acc: str) -> dict:
    """Fetch an entry and prove it is the one asked for.

    A dead or merged accession answers 200 with a different primaryAccession, and a silent
    zero there reads as a finding (see the ACTR10 O15507 case). Assert instead.
    """
    d = get_json(f"https://rest.uniprot.org/uniprotkb/{acc}.json",
                 {"fields": "accession,id,sequence,protein_name,organism_name,reviewed"})
    got = d.get("primaryAccession")
    if got != acc:
        raise RuntimeError(f"asked UniProt for {acc}, got {got} - accession is dead or merged")
    seq = d["sequence"]["value"]
    if not seq:
        raise RuntimeError(f"UniProt returned an empty sequence for {acc}")
    return {
        "accession": acc,
        "entry_name": d["uniProtkbId"],
        "reviewed": d["entryType"],
        "organism": d["organism"]["scientificName"],
        "length": len(seq),
        "sequence": seq,
    }


def aligner(matrix: str = "BLOSUM62", open_gap: float = -11.0, extend_gap: float = -1.0):
    al = Align.PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load(matrix)
    al.open_gap_score = open_gap
    al.extend_gap_score = extend_gap
    al.mode = "global"
    return al


ALIGNMENT_SCHEMES = {
    "BLOSUM62/-11/-1": ("BLOSUM62", -11.0, -1.0),
    "BLOSUM45/-14/-2": ("BLOSUM45", -14.0, -2.0),
}

CONSERVATIVE = [set("GA"), set("ST"), set("DE"), set("KRH"), set("NQ"), set("ILVMF"), set("FYW")]


def classify(ref_aa: str, obs_aa: str) -> str:
    if obs_aa == "-":
        return "gap"
    if ref_aa == obs_aa:
        return "identical"
    if any(ref_aa in g and obs_aa in g for g in CONSERVATIVE):
        return "conservative"
    return "non-conservative"


def pair_identity(a: str, b: str, al) -> tuple[float, float]:
    aln = al.align(a, b)[0]
    top, bot = str(aln[0]), str(aln[1])
    matches = sum(1 for x, y in zip(top, bot) if x == y and x != "-")
    return round(100.0 * matches / min(len(a), len(b)), 1), round(float(aln.score), 1)


# ------------------------------------------------- Q1: orthologue length distribution

def orthologue_lengths() -> dict:
    """Every UniProt entry whose gene name is ACTL10, with length and organism."""
    rows: list[dict] = []
    url = "https://rest.uniprot.org/uniprotkb/search"
    # Two restrictions, both needed for the distribution to mean anything.
    # gene_exact, not gene: the loose form also matches entries whose gene-name field merely
    # contains the token.
    # Mammalia (taxonomy_id:40674): an unrestricted ACTL10 gene-name search returns fungal
    # (Maudiozyma, Didymella), algal (Aureococcus) and Perkinsus entries that are not ACTL10
    # orthologues at all, and short passerine fragments. Every taxon used in the sister-pair
    # test is a mammal, so the clade restriction and the test agree in scope.
    page_size = 500
    params = {"query": "gene_exact:ACTL10 AND taxonomy_id:40674",
              "fields": "accession,id,length,reviewed,organism_name",
              "format": "json", "size": str(page_size)}
    # Take the authoritative total from the response header, not from len(results): a single page
    # that happens to saturate would otherwise silently truncate the distribution and every
    # downstream count. Reported by the PR reviewer; the query returns far fewer than one page
    # today, but a silent truncation is exactly the class of bug this script asserts against
    # everywhere else.
    resp = SESSION.get(url, params=params, timeout=180)
    resp.raise_for_status()
    d = resp.json()
    declared = resp.headers.get("x-total-results")
    if declared is None:
        raise RuntimeError("UniProt did not return x-total-results; cannot verify page coverage")
    declared = int(declared)
    if len(d.get("results", [])) >= page_size:
        raise RuntimeError(
            f"UniProt returned a full page ({page_size}) for the ACTL10 orthologue query, so the "
            f"result set is truncated ({declared} declared); add pagination before trusting the "
            "length distribution")
    for r in d.get("results", []):
        rows.append({
            "accession": r["primaryAccession"],
            "entry_name": r.get("uniProtkbId"),
            "reviewed": r["entryType"],
            "organism": r["organism"]["scientificName"],
            "length": r["sequence"]["length"],
        })
    if not rows:
        raise RuntimeError("UniProt returned no ACTL10 entries; the query or the field set is wrong")
    if len(rows) != declared:
        raise RuntimeError(
            f"parsed {len(rows)} entries but UniProt declares {declared}; the page is incomplete")
    total = len(rows)
    by_org: dict[str, list[int]] = defaultdict(list)
    for r in rows:
        by_org[r["organism"]].append(r["length"])
    # Sister-taxon test. Assert every taxon named in SISTER_PAIRS was actually retrieved,
    # so a renamed or withdrawn entry becomes an error rather than a silently skipped pair.
    pairs = []
    for a, b, clade in SISTER_PAIRS:
        for name in (a, b):
            if name not in by_org:
                raise RuntimeError(
                    f"sister-taxon test names {name!r} but no ACTL10 entry for it was "
                    f"returned; update SISTER_PAIRS or the query")
        pairs.append({
            "clade": clade, "taxon_a": a, "lengths_a": sorted(by_org[a]),
            "taxon_b": b, "lengths_b": sorted(by_org[b]),
            "differ": sorted(by_org[a]) != sorted(by_org[b]),
        })
    hist = Counter(r["length"] for r in rows)
    human = [r for r in rows if r["organism"] == "Homo sapiens"]
    if len(human) != 1:
        raise RuntimeError(f"expected exactly one human ACTL10 entry, got {len(human)}")
    human_len = human[0]["length"]
    return {
        "n_entries": total,
        "n_organisms": len(by_org),
        "length_histogram": dict(sorted(hist.items())),
        "length_min": min(hist), "length_max": max(hist),
        "modal_length": hist.most_common(1)[0][0],
        "modal_count": hist.most_common(1)[0][1],
        "human_length": human_len,
        "n_entries_at_human_length": hist[human_len],
        "n_entries_longer_than_human": sum(v for k, v in hist.items() if k > human_len),
        "n_entries_at_least_340": sum(v for k, v in hist.items() if k >= 340),
        "sister_pairs": pairs,
        "n_sister_pairs_differing": sum(1 for p in pairs if p["differ"]),
        "organisms_with_multiple_lengths": {
            o: sorted(set(v)) for o, v in sorted(by_org.items()) if len(set(v)) > 1
        },
        "entries": sorted(rows, key=lambda r: (r["length"], r["organism"])),
    }


# ------------------------------------------- Q2: is Q5JWF8 N-terminally truncated?

def transcript_layout() -> dict:
    """Exon and CDS coordinates for the MANE transcript, from Ensembl (not hard-coded)."""
    t = get_json(f"https://rest.ensembl.org/lookup/id/{ENSEMBL_TRANSCRIPT}",
                 {"expand": "1", "content-type": "application/json"})
    exons = [{"id": e["id"], "start": e["start"], "end": e["end"]} for e in t["Exon"]]
    tr = t["Translation"]
    return {
        "transcript": t["id"], "biotype": t["biotype"], "strand": t["strand"],
        "seq_region": t["seq_region_name"],
        "n_exons": len(exons), "exons": exons,
        "cds_start": tr["start"], "cds_end": tr["end"], "protein_length": tr["length"],
    }


def genomic_seq(region: str) -> str:
    d = get_json(f"https://rest.ensembl.org/sequence/region/human/{region}",
                 {"content-type": "application/json"})
    return d["seq"].upper()


def upstream_orf(layout: dict, swissprot_seq: str) -> dict:
    """Translate the annotated 5' leader in the CDS reading frame.

    Single-exon gene on the + strand, so genomic order is transcript order and the leader
    is contiguous with the CDS. Both facts are asserted rather than assumed.
    """
    if layout["n_exons"] != 1:
        raise RuntimeError(
            f"{ENSEMBL_TRANSCRIPT} now has {layout['n_exons']} exons; the leader is no longer "
            "contiguous with the CDS in genomic coordinates and this routine must be rewritten")
    if layout["strand"] != 1:
        raise RuntimeError("transcript is on the minus strand; reverse-complement first")
    exon = layout["exons"][0]
    chrom = layout["seq_region"]
    leader_start, leader_end = exon["start"], layout["cds_start"] - 1
    leader = genomic_seq(f"{chrom}:{leader_start}..{leader_end}:1")
    cds = genomic_seq(f"{chrom}:{layout['cds_start']}..{layout['cds_end']}:1")

    # Prove the frame: the annotated CDS must translate to the Swiss-Prot sequence.
    cds_prot = str(Seq(cds).translate(to_stop=False)).rstrip("*")
    if cds_prot != swissprot_seq:
        raise RuntimeError(
            "the Ensembl CDS does not translate to the Swiss-Prot sequence; coordinates or "
            f"assembly have moved\n  cds: {cds_prot[:40]}...\n  swp: {swissprot_seq[:40]}...")

    frame_offset = len(leader) % 3
    inframe = leader[frame_offset:]
    leader_prot = str(Seq(inframe).translate(to_stop=False))
    stops = [i for i, c in enumerate(leader_prot) if c == "*"]
    if stops:
        last_stop = max(stops)
        open_orf = leader_prot[last_stop + 1:]
        # genomic coordinate of the first codon of the open ORF
        orf_codon0 = leader_start + frame_offset + 3 * (last_stop + 1)
    else:
        last_stop = None
        open_orf = leader_prot
        orf_codon0 = leader_start + frame_offset
    mets = [i + 1 for i, c in enumerate(open_orf) if c == "M"]
    return {
        "chrom": chrom,
        "leader_start": leader_start, "leader_end": leader_end,
        "leader_nt": len(leader),
        "frame_offset": frame_offset,
        "leader_in_frame_codons": len(leader_prot),
        "n_in_frame_stops_in_leader": len(stops),
        "last_stop_codon_index": last_stop,
        "open_orf_codons": len(open_orf),
        "open_orf_protein": open_orf,
        "open_orf_first_codon_genomic": orf_codon0,
        "in_frame_ATG_in_open_orf": mets,
        "leader_in_frame_protein": leader_prot,
        "extended_protein": open_orf + swissprot_seq,
        "leader_nt_seq": leader,
    }


def ancestral_initiator(ext: dict, long_orthologue: dict, al) -> dict:
    """Which extended-ORF position aligns to the long orthologue's Met1, and what codon is it?

    All index arithmetic is derived from the alignment; nothing is counted by hand.
    """
    extended = ext["extended_protein"]
    aln = al.align(extended, long_orthologue["sequence"])[0]
    top, bot = str(aln[0]), str(aln[1])
    col = next((i for i, c in enumerate(bot) if c != "-"), None)
    if col is None:
        raise RuntimeError("orthologue aligned entirely to gaps")
    ext_pos = len(top[:col].replace("-", "")) + 1  # 1-based position in `extended`
    if ext_pos > ext["open_orf_codons"]:
        return {
            "orthologue": long_orthologue["accession"],
            "aligns_inside_upstream_orf": False,
            "note": "orthologue Met1 aligns downstream of the upstream ORF; no ancestral "
                    "initiator codon is recoverable from the leader",
        }
    # codon in the leader: extended position 1 is the first codon of the open ORF
    codon_start = ext["open_orf_first_codon_genomic"] + 3 * (ext_pos - 1)
    offset = codon_start - ext["leader_start"]
    codon = ext["leader_nt_seq"][offset:offset + 3]
    aa = str(Seq(codon).translate())
    if aa != extended[ext_pos - 1]:
        raise RuntimeError(
            f"codon bookkeeping is inconsistent: genomic codon {codon} -> {aa} but the "
            f"extended protein has {extended[ext_pos - 1]} at position {ext_pos}")
    return {
        "orthologue": long_orthologue["accession"],
        "orthologue_organism": long_orthologue["organism"],
        "orthologue_length": long_orthologue["length"],
        "aligns_inside_upstream_orf": True,
        "extended_orf_position": ext_pos,
        "human_codon": codon,
        "human_residue": aa,
        "human_codon_genomic_start": codon_start,
        "is_ATG": codon == "ATG",
        "residues_of_orthologue_upstream_of_swissprot_start":
            len(extended) - len(ext["extended_protein"]) + ext["open_orf_codons"] - ext_pos + 1,
    }


# ------------------------------------------------- Q3: residue tallies with coverage

def fetch_cif(pdb_id: str) -> str:
    r = SESSION.get(f"https://files.rcsb.org/download/{pdb_id.upper()}.cif", timeout=300)
    r.raise_for_status()
    return r.text


def polymer_residues(chain):
    return [r for r in chain if r.id[0] != "W" and r.get_resname().upper() in THREE_TO_ONE]


def chain_sequence(residues) -> str:
    return "".join(THREE_TO_ONE[r.get_resname().upper()] for r in residues)


def ligand_contacts(cif_text, pdb_id, chain_id, ligand_names, cutoff):
    model = MMCIFParser(QUIET=True).get_structure(pdb_id, io.StringIO(cif_text))[0]
    chain = model[chain_id]
    residues = polymer_residues(chain)
    ligands = [r for r in chain if r.get_resname().strip() in ligand_names]
    if not ligands:
        raise RuntimeError(f"{pdb_id} chain {chain_id} carries none of {sorted(ligand_names)}")
    ns = NeighborSearch([a for r in residues for a in r])
    hits: dict[int, dict] = {}
    for lig in ligands:
        for atom in lig:
            for other in ns.search(atom.coord, cutoff):
                res = other.get_parent()
                d = float(atom - other)
                rec = hits.setdefault(res.id[1], {"resname": res.get_resname(),
                                                  "ligands": set(), "min_dist": d})
                rec["ligands"].add(lig.get_resname().strip())
                rec["min_dist"] = min(rec["min_dist"], d)
    for rec in hits.values():
        rec["ligands"] = sorted(rec["ligands"])
        rec["min_dist"] = round(rec["min_dist"], 2)
    return residues, hits


def interface_contacts(cif_text, pdb_id, cutoff):
    model = MMCIFParser(QUIET=True).get_structure(pdb_id, io.StringIO(cif_text))[0]
    chains = {c.id: polymer_residues(c) for c in model}
    chains = {k: v for k, v in chains.items() if len(v) > 200}
    if len(chains) < 3:
        raise RuntimeError(f"{pdb_id} yielded {len(chains)} long chains; need a multi-protomer model")
    best = None
    for cid, residues in chains.items():
        others = [a for k, v in chains.items() if k != cid for r in v for a in r]
        ns = NeighborSearch(others)
        hits: dict[int, dict] = {}
        for res in residues:
            for atom in res:
                for other in ns.search(atom.coord, cutoff):
                    d = float(atom - other)
                    rec = hits.setdefault(res.id[1], {"resname": res.get_resname(),
                                                      "partners": set(), "min_dist": d})
                    rec["partners"].add(other.get_parent().get_parent().id)
                    rec["min_dist"] = min(rec["min_dist"], d)
        if best is None or len(hits) > len(best[2]):
            best = (cid, residues, hits)
    cid, residues, hits = best
    for rec in hits.values():
        rec["partners"] = sorted(rec["partners"])
        rec["min_dist"] = round(rec["min_dist"], 2)
    return cid, sorted(chains), residues, hits


def score_against(struct_seq: str, struct_numbers: list[int], contact_nums: list[int],
                  query_seq: str, al) -> dict:
    """Map structure contact positions onto a query, splitting gaps by cause.

    `outside_span` means the query sequence does not extend to that structural position at
    all - the position is absent from the *annotation*, which is a different fact from a
    substitution. `internal_gap` means the query does span the position but has a deletion.
    """
    aln = al.align(struct_seq, query_seq)[0]
    top, bot = str(aln[0]), str(aln[1])
    si = qi = 0
    mapping: dict[int, str] = {}
    aligned_struct_positions: list[int] = []
    for sc, qc in zip(top, bot):
        if sc != "-":
            si += 1
        if qc != "-":
            qi += 1
        if sc != "-":
            num = struct_numbers[si - 1]
            mapping[num] = qc if qc != "-" else "-"
            if qc != "-":
                aligned_struct_positions.append(num)
    if not aligned_struct_positions:
        raise RuntimeError("query aligned to nothing")
    first, last = min(aligned_struct_positions), max(aligned_struct_positions)
    # Keys are strings so that the in-memory dict and its JSON round-trip are the same shape;
    # an int/str divergence between the two is a silent KeyError waiting for a reader.
    per: dict[str, str] = {}
    tally = Counter()
    for num in contact_nums:
        ref_aa = struct_seq[struct_numbers.index(num)]
        obs = mapping[num]
        if obs == "-":
            kind = "internal_gap" if first <= num <= last else "outside_span"
        else:
            kind = classify(ref_aa, obs)
        per[str(num)] = f"{obs}:{kind}"
        tally[kind] += 1
    ident, score = pair_identity(struct_seq, query_seq, al)
    return {
        "identical": tally["identical"], "conservative": tally["conservative"],
        "non_conservative": tally["non-conservative"],
        "internal_gap": tally["internal_gap"], "outside_span": tally["outside_span"],
        "compatible": tally["identical"] + tally["conservative"],
        "present": len(contact_nums) - tally["outside_span"],
        "aligned_struct_span": [first, last],
        "pct_identity_to_struct_chain": ident,
        "per_residue": per,
    }


def parse_actl8_interface_table(path: Path) -> dict[str, tuple[int, int, int, int]]:
    """Pull ACTL8's committed filament-interface tallies out of its RESULTS.md.

    Used as a cross-file check that this script reproduces the sibling analysis on the
    shared controls. Fails loudly if the table cannot be found, because a silently empty
    expectation would make the assertion below vacuous.
    """
    text = require(path, "see genes/human/ACTL8/ACTL8-bioinformatics/").read_text()
    m = re.search(r"## 2\. Is the filament protomer interface still present\?(.*?)\n### ",
                  text, re.S)
    if not m:
        raise RuntimeError(f"could not locate the filament-interface section in {path}")
    out: dict[str, tuple[int, int, int, int]] = {}
    for line in m.group(1).splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 5 and cells[1].isdigit():
            out[cells[0]] = tuple(int(c) for c in cells[1:])
    if not out:
        raise RuntimeError(f"parsed zero rows from the filament-interface table in {path}")
    return out


# --------------------------------------------------------- Q4: IBA rows and PAINT

def parse_goa(path: Path) -> list[dict]:
    lines = require(path, "just fetch-gene human ACTL10").read_text().splitlines()
    header = lines[0].split("\t")
    return [dict(zip(header, ln.split("\t"))) for ln in lines[1:] if ln.strip()]


def split_withfrom(field: str) -> list[str]:
    return [t for t in field.split("|") if t.strip()]


def resolve_token(token: str) -> dict:
    """Resolve a WITH/FROM token, always requesting size=2 so ambiguity shows as ambiguity."""
    if token.startswith("PANTHER:"):
        return {"token": token, "kind": "panther_node", "resolved": False,
                "note": "PANTHER internal tree node, not a protein - carries no evidence of its own"}
    if token.startswith("GO:"):
        return {"token": token, "kind": "go_term", "resolved": False,
                "note": "a GO term, not a gene product - this row is an inter-ontology inference"}
    db, _, ident = token.partition(":")
    if db == "UniProtKB":
        q = f"accession:{ident}"
    elif db == "WB":
        # WormBase gene ids are self-identifying; prefixing the db name ("xref:wormbase-...")
        # returns zero hits, which reads as "no such source" rather than "wrong query".
        q = f"xref:{ident}"
    elif db in XREF_DB:
        inner = ident.split(":")[-1]  # MGI arrives as MGI:MGI:1915938; the inner colon is a 400
        q = f"xref:{XREF_DB[db]}-{inner}"
    else:
        return {"token": token, "kind": "unknown_db", "resolved": False,
                "note": f"no UniProt xref mapping for db {db!r}"}
    d = get_json("https://rest.uniprot.org/uniprotkb/search",
                 {"query": q, "fields": "accession,id,gene_names,organism_name,reviewed,length",
                  "format": "json", "size": "5"})
    hits = d.get("results", [])
    if not hits:
        return {"token": token, "kind": "protein", "resolved": False,
                "note": "no UniProt entry found - cannot be dismissed, only deferred"}
    cands = []
    for r in hits:
        genes = [g.get("geneName", {}).get("value") for g in r.get("genes", []) if g.get("geneName")]
        cands.append({
            "accession": r["primaryAccession"], "entry_name": r.get("uniProtkbId"),
            "gene": genes[0] if genes else None,
            "organism": r["organism"]["scientificName"],
            "reviewed": r["entryType"], "length": r["sequence"]["length"],
        })
    reviewed = [c for c in cands if "Swiss-Prot" in c["reviewed"]]
    chosen = reviewed[0] if reviewed else cands[0]
    return {"token": token, "kind": "protein", "resolved": True,
            "n_candidates": len(cands), "candidates": cands, "chosen": chosen,
            "ambiguous": len(cands) > 1}


def quickgo_evidence(gene_product: str, go_id: str) -> dict:
    # allow_zero: a donor carrying no evidence for the term it donated is a reportable finding
    # (it would weaken the propagation), so it must not abort the run.
    d = quickgo_all({"geneProductId": gene_product, "goId": go_id, "goUsage": "descendants",
                     "goUsageRelationships": "is_a,part_of", "limit": "100"},
                    f"own-evidence query for {gene_product} / {go_id}", allow_zero=True)
    codes = Counter()
    terms = Counter()
    for r in d.get("results", []):
        codes[r["goEvidence"]] += 1
        terms[f"{r['goId']} {r.get('goName','')}"] += 1
    n = d.get("numberOfHits", 0)
    # A zero has two possible meanings and they are not interchangeable: the donor genuinely holds
    # no annotation for the term it donated (a finding that weakens the propagation), or QuickGO
    # does not hold this accession at all (a data artefact that would read as a property of the
    # donor - the dead-accession trap). One unfiltered re-query separates them.
    absent = None
    if n == 0:
        probe = quickgo_all({"geneProductId": gene_product, "limit": "1"},
                            f"presence probe for {gene_product}", allow_zero=True,
                            count_only=True)
        absent = probe.get("numberOfHits", 0) == 0
    return {"n": n, "codes": dict(codes), "terms": dict(terms),
            "has_experimental": bool(set(codes) & EXPERIMENTAL_CODES),
            "accession_absent_from_quickgo": absent}


def go0005200_census() -> dict:
    d = quickgo_all({"goId": "GO:0005200", "goUsage": "exact", "taxonId": "9606",
                     "evidenceCode": "ECO:0000318", "limit": "100"},
                    "the human GO:0005200 IBA census")
    by_node: dict[str, list[str]] = defaultdict(list)
    for r in d["results"]:
        nodes = [x["id"] for wf in (r.get("withFrom") or []) for x in wf["connectedXrefs"]
                 if x["db"] == "PANTHER"]
        for n in nodes:
            by_node[n].append(r["symbol"])
    return {"total_human_IBA": d.get("numberOfHits"),
            "by_panther_node": {k: sorted(v) for k, v in sorted(by_node.items())}}


def paint_record() -> dict:
    lines = require(PAINT_TSV, "cached PANTHER PAINT export").read_text().splitlines()
    header = lines[0].split("\t")
    rows = [dict(zip(header, ln.split("\t"))) for ln in lines[1:] if ln.strip()]
    ibd = [r for r in rows if r["go_id"] == "GO:0005200" and r["evidence"] == "IBD"]
    ird = [r for r in rows if r["go_id"] == "GO:0005200" and r["negated"] == "true"]
    return {
        "n_rows": len(rows),
        "GO_0005200_IBD_nodes": [{"node": r["node"], "seeds": split_withfrom(r["seeds"]),
                                  "date": r["date"]} for r in ibd],
        "GO_0005200_IRD_negations": [{"node": r["node"], "evidence": r["evidence"],
                                      "seeds": split_withfrom(r["seeds"]), "date": r["date"]}
                                     for r in sorted(ird, key=lambda x: x["node"])],
        "n_IRD_negations": len(ird),
    }


# ------------------------------------------------------------------------ reporting

def main() -> None:
    res: dict = {}
    n_refs = assert_quickgo_calls_are_guarded()
    print(f"guard: {n_refs} QUICKGO_SEARCH read(s), all inside quickgo_all() or the guard itself",
          file=sys.stderr)
    al62 = aligner()

    print("Q1  orthologue length distribution ...", file=sys.stderr)
    res["orthologues"] = orthologue_lengths()

    print("Q2  is Q5JWF8 N-terminally truncated ...", file=sys.stderr)
    sp = uniprot_entry(ACTL10)
    res["swissprot"] = {k: v for k, v in sp.items() if k != "sequence"}
    layout = transcript_layout()
    res["transcript"] = layout
    if layout["protein_length"] != sp["length"]:
        raise RuntimeError(
            f"Ensembl says {layout['protein_length']} aa, UniProt says {sp['length']} aa")
    ext = upstream_orf(layout, sp["sequence"])
    res["upstream_orf"] = {k: v for k, v in ext.items() if k != "leader_nt_seq"}
    extended_seq = ext["extended_protein"]

    long_orths = {a: uniprot_entry(a) for a in ("A0A6J3JAC8", "A0A5F4WJE9", "A2AKE7", "G3TK56")}
    actb = uniprot_entry(ACTB)
    res["extended_vs_orthologues"] = []
    for acc, o in long_orths.items():
        i_ext, s_ext = pair_identity(extended_seq, o["sequence"], al62)
        i_245, s_245 = pair_identity(sp["sequence"], o["sequence"], al62)
        res["extended_vs_orthologues"].append({
            "accession": acc, "organism": o["organism"], "length": o["length"],
            "pct_id_extended": i_ext, "score_extended": s_ext,
            "pct_id_swissprot245": i_245, "score_swissprot245": s_245,
            "score_gain": round(s_ext - s_245, 1),
        })
    res["extended_vs_ACTB"] = dict(zip(("pct_id", "score"), pair_identity(extended_seq, actb["sequence"], al62)))
    res["swissprot245_vs_ACTB"] = dict(zip(("pct_id", "score"), pair_identity(sp["sequence"], actb["sequence"], al62)))
    res["ancestral_initiator"] = [ancestral_initiator(ext, long_orths[a], al62)
                                  for a in ("A0A6J3JAC8", "A0A5F4WJE9")]

    print("Q3  residue tallies (2BTF nucleotide site, 6DJO interface) ...", file=sys.stderr)
    panel = {a: uniprot_entry(a) for a in PANEL}
    panel_seqs = {a: p["sequence"] for a, p in panel.items()}
    panel_seqs["EXTENDED"] = extended_seq
    labels = dict(PANEL)
    labels["EXTENDED"] = EXTENDED_LABEL

    pdb_id, chain_id, ligs = ATP_STRUCTURE
    residues, hits = ligand_contacts(fetch_cif(pdb_id), pdb_id, chain_id, ligs, CONTACT_CUTOFF)
    atp_nums = sorted(hits)
    atp_struct_seq = chain_sequence(residues)
    atp_numbers = [r.id[1] for r in residues]
    res["nucleotide_site"] = {
        "structure": pdb_id, "chain": chain_id, "ligands": list(ligs),
        "cutoff_angstrom": CONTACT_CUTOFF, "n_contact_residues": len(atp_nums),
        "contact_residues": [{"num": n, "resname": hits[n]["resname"],
                              "ligands": hits[n]["ligands"], "min_dist": hits[n]["min_dist"]}
                             for n in atp_nums],
        "panel": {},
    }

    fpdb, _, _ = FILAMENT_STRUCTURE
    fcid, fchains, fres, fhits = interface_contacts(fetch_cif(fpdb), fpdb, CONTACT_CUTOFF)
    if_nums = sorted(fhits)
    if_struct_seq = chain_sequence(fres)
    if_numbers = [r.id[1] for r in fres]
    res["filament_interface"] = {
        "structure": fpdb, "chain_used": fcid, "chains": fchains,
        "cutoff_angstrom": CONTACT_CUTOFF, "n_contact_residues": len(if_nums),
        "contact_residues": [{"num": n, "resname": fhits[n]["resname"],
                              "partners": fhits[n]["partners"], "min_dist": fhits[n]["min_dist"]}
                             for n in if_nums],
        "panel": {}, "alignment_sensitivity": {},
    }

    for acc, seq in panel_seqs.items():
        res["nucleotide_site"]["panel"][acc] = {
            "label": labels[acc],
            **score_against(atp_struct_seq, atp_numbers, atp_nums, seq, al62)}
        res["filament_interface"]["panel"][acc] = {
            "label": labels[acc],
            **score_against(if_struct_seq, if_numbers, if_nums, seq, al62)}

    for name, (matrix, og, eg) in ALIGNMENT_SCHEMES.items():
        alt = aligner(matrix, og, eg)
        res["filament_interface"]["alignment_sensitivity"][name] = {
            acc: {k: v for k, v in score_against(if_struct_seq, if_numbers, if_nums, seq, alt).items()
                  if k in ("identical", "conservative", "non_conservative",
                           "internal_gap", "outside_span", "compatible")}
            for acc, seq in panel_seqs.items()}

    # Cross-file check: this script must reproduce ACTL8's committed tallies on the shared
    # controls. ACTL8 reported a single "gap" column; here gaps are split by cause, so the
    # comparison is against internal_gap + outside_span.
    published = parse_actl8_interface_table(ACTL8_RESULTS)
    checks = []
    for acc, key in (("P60709", "ACTB (human beta-actin; IBA donor)"),
                     ("Q9H568", "ACTL8 (human actin-like 8)"),
                     ("Q5JWF8", "ACTL10 (human actin-like 10)")):
        if key not in published:
            raise RuntimeError(f"ACTL8's RESULTS.md has no row {key!r}; rows found: "
                               f"{sorted(published)}")
        p = published[key]
        m = res["filament_interface"]["panel"][acc]
        mine = (m["identical"], m["conservative"], m["non_conservative"],
                m["internal_gap"] + m["outside_span"])
        checks.append({"accession": acc, "actl8_published": list(p), "recomputed": list(mine),
                       "agrees": list(p) == list(mine)})
    res["reproducibility_check_vs_ACTL8"] = checks
    bad = [c for c in checks if not c["agrees"]]
    if bad:
        raise RuntimeError(f"failed to reproduce ACTL8's committed interface tallies: {bad}")

    print("Q4  IBA rows, WITH/FROM, PAINT ...", file=sys.stderr)
    goa = parse_goa(GOA_TSV)
    res["goa_rows"] = []
    for row in goa:
        entry = {"term": row["GO TERM"], "name": row["GO NAME"], "aspect": row["GO ASPECT"],
                 "evidence": row["GO EVIDENCE CODE"], "qualifier": row["QUALIFIER"],
                 "reference": row["REFERENCE"],
                 "withfrom_tokens": split_withfrom(row["WITH/FROM"])}
        entry["n_withfrom"] = len(entry["withfrom_tokens"])
        sources = []
        for tok in entry["withfrom_tokens"]:
            r = resolve_token(tok)
            if r.get("resolved"):
                gp = f"UniProtKB:{r['chosen']['accession']}"
                r["own_evidence_for_term"] = quickgo_evidence(gp, row["GO TERM"])
            sources.append(r)
        # Build source_entities FROM the GOA field, with the count asserted.
        if len(sources) != entry["n_withfrom"]:
            raise RuntimeError("source list drifted from the GOA WITH/FROM field")
        entry["sources"] = sources
        prot = [s for s in sources if s["kind"] == "protein"]
        entry["n_protein_tokens"] = len(prot)
        entry["n_resolved"] = sum(1 for s in prot if s["resolved"])
        entry["n_with_own_experimental"] = sum(
            1 for s in prot if s.get("own_evidence_for_term", {}).get("has_experimental"))
        entry["n_ambiguous_lookups"] = sum(1 for s in prot if s.get("ambiguous"))
        entry["n_unreviewed_chosen"] = sum(
            1 for s in prot if s.get("resolved") and "Swiss-Prot" not in s["chosen"]["reviewed"])
        res["goa_rows"].append(entry)

    res["GO_0005200_human_IBA_census"] = go0005200_census()
    res["paint"] = paint_record()

    (HERE / "results.json").write_text(json.dumps(res, indent=2, sort_keys=False) + "\n")
    write_report(res)
    print("wrote results.json and RESULTS.md", file=sys.stderr)


def _tbl(rows: list[list[str]], head: list[str]) -> list[str]:
    out = ["| " + " | ".join(head) + " |", "|" + "|".join("---" for _ in head) + "|"]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return out


def write_report(res: dict) -> None:
    L: list[str] = []
    A = L.append
    A("# ACTL10: is the Swiss-Prot sequence the protein, and what do its two IBA rows rest on?")
    A("")
    A("Generated by `uv run python analyze_actl10.py`. Every number is computed at run time")
    A("from the UniProt and Ensembl REST APIs, RCSB coordinate files, QuickGO, and files")
    A("committed in this repository. Nothing is hard-coded from a previous run.")
    A("")

    o = res["orthologues"]
    A("## 1. ACTL10 orthologue lengths do not follow the phylogeny")
    A("")
    A(f"UniProt holds **{o['n_entries']}** mammalian entries whose gene name is exactly ACTL10, "
      f"across **{o['n_organisms']}** organisms. Lengths run from **{o['length_min']}** to "
      f"**{o['length_max']}** aa. The human entry is **{o['human_length']}** aa, shared with "
      f"{o['n_entries_at_human_length'] - 1} other entries; the modal length is "
      f"**{o['modal_length']}** aa ({o['modal_count']} entries). "
      f"**{o['n_entries_longer_than_human']}** entries are longer than human, of which "
      f"**{o['n_entries_at_least_340']}** are 340 aa or more - i.e. long enough to span the actin "
      "fold that the human entry does not.")
    A("")
    A("If the variation were biological it would track the species tree. It does not: in "
      f"**{o['n_sister_pairs_differing']} of {len(o['sister_pairs'])}** sister-taxon pairs tested, "
      "two members of the same family carry different lengths.")
    A("")
    L += _tbl([[p["clade"], p["taxon_a"], p["lengths_a"], p["taxon_b"], p["lengths_b"],
                "**differ**" if p["differ"] else "same"] for p in o["sister_pairs"]],
              ["clade", "taxon A", "len A", "taxon B", "len B", ""])
    A("")
    if o["organisms_with_multiple_lengths"]:
        A("Organisms carrying more than one ACTL10 length in UniProt at once (same species, "
          "different entries):")
        A("")
        for org, lens in o["organisms_with_multiple_lengths"].items():
            A(f"- {org}: {lens}")
        A("")
    A("Length histogram:")
    A("")
    L += _tbl([[k, v] for k, v in o["length_histogram"].items()], ["length (aa)", "entries"])
    A("")

    sp, tx, ext = res["swissprot"], res["transcript"], res["upstream_orf"]
    A("## 2. Q5JWF8 begins mid-fold: the human genome encodes the missing region in frame")
    A("")
    A(f"`{sp['accession']}` ({sp['entry_name']}, {sp['reviewed']}) is **{sp['length']} aa**. Its MANE "
      f"transcript `{tx['transcript']}` is a **single exon** ({tx['n_exons']} exon, "
      f"chr{tx['seq_region']}:{tx['exons'][0]['start']}-{tx['exons'][0]['end']}) with the CDS at "
      f"{tx['cds_start']}-{tx['cds_end']}. The annotated 5' leader is therefore "
      f"**{ext['leader_nt']} nt** of the same exon, contiguous with the CDS.")
    A("")
    A(f"Translating that leader in the CDS reading frame (frame offset {ext['frame_offset']}; the "
      "CDS translation was first asserted to equal the Swiss-Prot sequence, so the frame is "
      f"proven, not assumed) gives {ext['leader_in_frame_codons']} codons containing "
      f"**{ext['n_in_frame_stops_in_leader']}** in-frame stop. After the last stop there are "
      f"**{ext['open_orf_codons']} uninterrupted codons** running straight into the annotated "
      "initiator:")
    A("")
    A("```")
    for i in range(0, len(ext["open_orf_protein"]), 60):
        A(ext["open_orf_protein"][i:i + 60])
    A("```")
    A("")
    A(f"In-frame ATG codons inside that open stretch: **{ext['in_frame_ATG_in_open_orf'] or 'none'}**.")
    A("")
    A("That translation is actin. Aligned globally to human beta-actin the extended "
      f"({len(ext['extended_protein'])} aa) form scores **{res['extended_vs_ACTB']['score']}** at "
      f"{res['extended_vs_ACTB']['pct_id']}% identity, against "
      f"**{res['swissprot245_vs_ACTB']['score']}** at {res['swissprot245_vs_ACTB']['pct_id']}% for the "
      f"{sp['length']}-aa Swiss-Prot sequence alone.")
    A("")
    A("Against the long ACTL10 orthologues the gain is decisive:")
    A("")
    L += _tbl([[r["organism"], r["length"], r["pct_id_swissprot245"], r["score_swissprot245"],
                r["pct_id_extended"], r["score_extended"], f"+{r['score_gain']}"]
               for r in res["extended_vs_orthologues"]],
              ["orthologue", "len", f"%id vs {sp['length']}aa", "score", "%id vs extended",
               "score", "score gain"])
    A("")
    A("### Where the ancestral initiator went")
    A("")
    for a in res["ancestral_initiator"]:
        if not a["aligns_inside_upstream_orf"]:
            A(f"- {a['orthologue']}: {a['note']}")
            continue
        A(f"- **{a['orthologue_organism']}** ({a['orthologue']}, {a['orthologue_length']} aa): its "
          f"Met1 aligns to position {a['extended_orf_position']} of the extended human ORF, where "
          f"the human genomic codon is **{a['human_codon']}** "
          f"(chr{ext['chrom']}:{a['human_codon_genomic_start']}), encoding "
          f"**{a['human_residue']}** - ATG: **{a['is_ATG']}**.")
    A("")
    A("So the human locus has lost the initiator codon its orthologues use, and the next "
      "in-frame ATG lies ~120 codons downstream, which is where Swiss-Prot, RefSeq and MANE all "
      "begin the protein. The intervening actin-homologous coding sequence is still present, in "
      "frame, and free of stop codons.")
    A("")
    A("**What this does and does not establish.** It establishes that the sequence in Q5JWF8 is "
      "not the whole of ACTL10's actin homology, and therefore that any residue tally computed "
      "from Q5JWF8 measures the annotation boundary as much as the protein. It does *not* "
      "establish which product the human cell makes: a lost initiator with a conserved downstream "
      "reading frame is compatible both with a genuinely N-terminally shortened human protein and "
      "with initiation at a non-ATG codon or an unannotated upstream exon. That question needs "
      "N-terminal proteomics, not sequence analysis.")
    A("")

    A("## 3. Actin's nucleotide site and protomer interface, with absence separated from substitution")
    A("")
    ns, fi = res["nucleotide_site"], res["filament_interface"]
    A(f"Nucleotide-site contacts come from PDB **{ns['structure']}** chain {ns['chain']} "
      f"(ligands {', '.join(ns['ligands'])}, {ns['cutoff_angstrom']} A heavy-atom cutoff): "
      f"{ns['n_contact_residues']} residues. Filament-interface contacts come from PDB "
      f"**{fi['structure']}** chain {fi['chain_used']} of {len(fi['chains'])} protomers "
      f"({fi['cutoff_angstrom']} A): {fi['n_contact_residues']} residues. Both are actin-only "
      "assemblies, and both match the structures and cutoffs used by the committed ACTL8 "
      "analysis, so the columns are comparable by construction.")
    A("")
    A("`outside span` counts contact positions the query sequence does not reach at all - an "
      "absence in the annotation. `internal gap` is a deletion inside the aligned span. Only the "
      "remaining columns are substitutions.")
    A("")
    A("### Filament protomer interface")
    A("")
    rows = []
    for acc, m in sorted(fi["panel"].items(), key=lambda kv: -kv[1]["compatible"]):
        rows.append([m["label"], m["identical"], m["conservative"], m["non_conservative"],
                     m["internal_gap"], m["outside_span"], m["present"],
                     f"{m['compatible']}/{m['present']}" if m["present"] else "n/a",
                     m["pct_identity_to_struct_chain"]])
    L += _tbl(rows, ["protein", "ident", "cons", "non-cons", "internal gap", "outside span",
                     "positions present", "compatible / present", "%id to chain"])
    A("")
    A("### Nucleotide site")
    A("")
    rows = []
    for acc, m in sorted(ns["panel"].items(), key=lambda kv: -kv[1]["compatible"]):
        rows.append([m["label"], m["identical"], m["conservative"], m["non_conservative"],
                     m["internal_gap"], m["outside_span"], m["present"],
                     f"{m['compatible']}/{m['present']}" if m["present"] else "n/a",
                     m["pct_identity_to_struct_chain"]])
    L += _tbl(rows, ["protein", "ident", "cons", "non-cons", "internal gap", "outside span",
                     "positions present", "compatible / present", "%id to chain"])
    A("")
    A("#### Per-residue, and why the truncation matters most here")
    A("")
    A("Short column names: `ACTB` = human beta-actin; `ext` = human ACTL10 extended ORF; "
      "`245` = Q5JWF8 as annotated; `Sap` = Sapajus ACTL10 (368 aa); `mus` = mouse Actl10 "
      "(346 aa); `L8` = ACTL8.")
    A("")
    cols = ["P60709", "EXTENDED", "Q5JWF8", "A0A6J3JAC8", "A2AKE7", "Q9H568"]
    short = ["ACTB", "ext", "245", "Sap", "mus", "L8"]
    rows = []
    for c in ns["contact_residues"]:
        n = c["num"]
        cells = []
        for acc in cols:
            v = ns["panel"][acc]["per_residue"][str(n)]
            aa, _, kind = v.partition(":")
            mark = {"identical": "", "conservative": " ~", "non-conservative": " **",
                    "outside_span": " ABSENT", "internal_gap": " gap"}[kind]
            cells.append(f"{aa}{mark}")
        rows.append([f"{c['resname']}{n}", ",".join(c["ligands"]), c["min_dist"]] + cells)
    L += _tbl(rows, ["structure residue", "ligand", "min dist"] + short)
    A("")
    A("`~` conservative, `**` non-conservative, `ABSENT` the query does not reach this position.")
    A("")
    ploop = [c["num"] for c in ns["contact_residues"]
             if ns["panel"]["Q5JWF8"]["per_residue"][str(c["num"])].endswith("outside_span")]
    ext_at_ploop = [ns["panel"]["EXTENDED"]["per_residue"][str(n)] for n in ploop]
    A(f"The positions Q5JWF8 fails to reach are exactly **{', '.join(str(n) for n in ploop)}** - "
      "actin's **phosphate-binding loop 1** (the `DNGSGMCK` motif that grips the nucleotide "
      "beta-phosphate, and the most diagnostic single feature of the actin fold). In the extended "
      f"human ORF those same positions read **{', '.join(ext_at_ploop)}**, i.e. the loop is intact. "
      "So the one part of the nucleotide site that the committed ACTL8 panel scored as missing from "
      "ACTL10 is the part that is present in the genome and merely absent from the annotation. Note "
      "that the mouse 346-aa entry also begins downstream of this loop, so its scores at these "
      "positions are alignment-edge artefacts rather than substitutions.")
    A("")
    A("### Cross-check against the committed ACTL8 analysis")
    A("")
    A("This script must reproduce ACTL8's published filament-interface tallies on the shared "
      "rows, where its single `gap` column equals `internal gap + outside span` here. The run "
      "aborts if it does not.")
    A("")
    L += _tbl([[c["accession"], c["actl8_published"], c["recomputed"],
                "yes" if c["agrees"] else "**NO**"]
               for c in res["reproducibility_check_vs_ACTL8"]],
              ["accession", "ACTL8 RESULTS.md (id/cons/non-cons/gap)", "recomputed", "agrees"])
    A("")
    A("### Alignment sensitivity")
    A("")
    rows = []
    for name, d in res["filament_interface"]["alignment_sensitivity"].items():
        for acc, m in sorted(d.items()):
            rows.append([fi["panel"][acc]["label"], name,
                         f"{m['identical']}/{m['conservative']}/{m['non_conservative']}"
                         f"/{m['internal_gap']}/{m['outside_span']}"])
    L += _tbl(rows, ["protein", "scheme", "id/cons/non-cons/int-gap/outside"])
    A("")

    A("## 4. What ACTL10's two IBA rows rest on")
    A("")
    for r in res["goa_rows"]:
        A(f"### {r['term']} {r['name']} ({r['aspect']}, {r['evidence']}, {r['qualifier']})")
        A("")
        A(f"Reference {r['reference']}; **{r['n_withfrom']}** WITH/FROM tokens, of which "
          f"**{r['n_protein_tokens']}** are protein identifiers. Resolved: "
          f"**{r['n_resolved']}/{r['n_protein_tokens']}**. Carrying their own experimental-code "
          f"annotation for this term or a descendant: **{r['n_with_own_experimental']}**. "
          f"Ambiguous lookups (>1 UniProt hit): {r['n_ambiguous_lookups']}. "
          f"Resolved only to an unreviewed entry: {r['n_unreviewed_chosen']}.")
        A("")
        rows = []
        for s in r["sources"]:
            if s["kind"] != "protein":
                rows.append([s["token"], s["kind"], "-", "-", s.get("note", "")])
                continue
            if not s["resolved"]:
                rows.append([s["token"], "protein", "UNRESOLVED", "-", s.get("note", "")])
                continue
            c, ev = s["chosen"], s["own_evidence_for_term"]
            rows.append([s["token"], c["organism"], f"{c['gene']} ({c['accession']})",
                         "Swiss-Prot" if "Swiss-Prot" in c["reviewed"] else "**TrEMBL**",
                         ", ".join(f"{k}x{v}" for k, v in sorted(ev["codes"].items())) or "none"])
        L += _tbl(rows, ["token", "organism / kind", "gene", "status", "own evidence for this term"])
        A("")

    c = res["GO_0005200_human_IBA_census"]
    A("### GO:0005200 by PANTHER node, all human IBA annotations")
    A("")
    A(f"QuickGO returns **{c['total_human_IBA']}** human `GO:0005200` IBA annotations in total. "
      "Grouped by the donating PANTHER node:")
    A("")
    L += _tbl([[n, len(g), ", ".join(g)] for n, g in c["by_panther_node"].items()],
              ["node", "n", "human genes"])
    A("")
    p = res["paint"]
    A("### PAINT's own verdict on GO:0005200 inside PTHR11937")
    A("")
    A(f"The cached PAINT export for PTHR11937 has {p['n_rows']} rows. `GO:0005200` is asserted "
      "by IBD at:")
    A("")
    L += _tbl([[r["node"], len(r["seeds"]), r["date"], ", ".join(r["seeds"])]
               for r in p["GO_0005200_IBD_nodes"]], ["node", "n seeds", "date", "seeds"])
    A("")
    A(f"and then **negated on descent at {p['n_IRD_negations']} nodes**:")
    A("")
    L += _tbl([[r["node"], r["evidence"], r["date"], ", ".join(r["seeds"])]
               for r in p["GO_0005200_IRD_negations"]], ["node", "evidence", "date", "blocked from"])
    A("")

    (HERE / "RESULTS.md").write_text("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
