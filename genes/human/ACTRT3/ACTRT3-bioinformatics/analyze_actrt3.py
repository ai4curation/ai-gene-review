"""Does ACTRT3 keep the residues that make an actin an actin, and is its GO:0005200
already rejected by PAINT in the sibling clades of the very node that donated it?

ACTRT3 (Q9BYD9, ARP-T3 / ARPM1) has no experimental human GO annotation for molecular
function, and its only experimentally grounded locations reach it from the mouse
orthologue Actrt3 (Q8BXF8): perinuclear theca and male germ cell nucleus. Its cytoskeletal
record is two PANTHER/PAINT rows -- `GO:0015629 actin cytoskeleton` and
`GO:0005200 structural constituent of cytoskeleton` -- plus three UniProt SubCell IEA rows
and one inter-ontology IEA step. Two opposite errors are available:

  (a) accepting a filament/cytoskeleton-constituent claim because the protein carries an
      actin fold, which is reading an activity off a fold name; and
  (b) declaring "fold without function" without checking whether the residues that make
      actin an actin are still present.

Both are decided by measurement, so everything below is computed at run time from live
data. The structural machinery (contact detection, alignment, substitution classing,
two-scheme sensitivity) follows genes/human/ACTL8/ACTL8-bioinformatics/analyze_actl8.py so
that the tallies are numerically comparable with that merged sibling review; the panel,
the third contact set and analyses B/C/D are specific to ACTRT3.

Analysis 1 -- nucleotide site.
  Residues contacting ATP and its associated cation are computed from the coordinates of
  PDB 2BTF chain A (beta-actin), never taken from memory. The chain's own observed sequence
  and numbering are globally aligned to ACTRT3 and to a control panel, so conservation is
  read off an alignment rather than off a position number.

Analysis 2 -- profilin interface.
  2BTF is the profilin:beta-actin complex, so the SAME structure yields the profilin-binding
  surface as the residues of chain A within the cutoff of the profilin chain. This is the
  one interaction ACTRT3 has any experimental support for: mouse ArpM1 co-immunoprecipitates
  profilin III (PMID:18692047), and UniProt records `Interacts with PFN3` by similarity. So
  the profilin surface is a directed prediction, not a fishing expedition.

Analysis 3 -- filament protomer interface.
  "Actin cytoskeleton" and "structural constituent of cytoskeleton" are claims about
  polymerisation, so the same treatment is applied to the protomer-protomer interface of
  PDB 6DJO (four protomers of F-actin).

  Controls run in both directions, which is what makes the result interpretable:
  conventional actins (must score near-perfect); Drosophila Arp53D, a divergent actin that
  *does* polymerise; ACTR1A/Arp1, which polymerises into the dynactin filament and is the
  weakest true polymeriser available; ACTR10/Arp11 and ACTR3/Arp3, which do not homopolymerise;
  and ACTL8, whose merged review earned a REMOVE on this same measurement with the same
  structures and cutoffs.

Analysis B -- has PAINT already rejected GO:0005200 in sibling clades?
  The repository's PAINT export for PTHR11937 is scanned for every node carrying a *negated*
  (IRD) GO:0005200, and for nodes carrying the general parent GO:0005198 instead. QuickGO is
  then asked which human genes each such node annotates. This tests, rather than asserts,
  whether ACTRT3's GO:0005200 is a survivor of a rejection sweep that has already reached its
  neighbours.

Analysis C -- donor homogeneity of the two donating nodes.
  For each PANTHER node in ACTRT3's WITH/FROM, the node's PAINT *seed* set (the experimentally
  annotated descendants that justify the term) is separated from the node's *recipient* set
  (the human genes the term propagates to), and every member of both is aligned locally to
  beta-actin. A broad term is correct when its donors disagree; it is over-propagation when
  the donors agree and the recipient is the outlier. The two cases are distinguished here
  rather than assumed.

Analysis D -- relatives census, re-derived live.
  ACTL8's merged review reports that ACTL8 carries 11 IBA rows against a median of 2 across
  the eight divergent human actin-like / actin-related-T proteins. That census is recomputed
  from QuickGO here rather than read off the sibling review.

Analysis E -- the mouse orthologue that carries the only experimental evidence.
  Q8BXF8 is aligned to Q9BYD9 and its own QuickGO evidence for each term it donates is
  fetched, so an ortholog transfer is distinguished from a paralog transfer by measurement.

A missing local input is a hard error naming the command that regenerates it. An ambiguous or
empty remote answer is reported, not silently dropped.

Usage:  uv run python analyze_actrt3.py
Writes: results.json, RESULTS.md
"""

from __future__ import annotations

import csv
import io
import json
import statistics
from collections import Counter
from pathlib import Path

import requests
from Bio import Align
from Bio.Align import substitution_matrices
from Bio.Data.PDBData import protein_letters_3to1_extended as THREE_TO_ONE
from Bio.PDB import MMCIFParser, NeighborSearch

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
REPO_ROOT = GENE_DIR.parents[2]
GOA_TSV = GENE_DIR / "ACTRT3-goa.tsv"
PAINT_TSV = REPO_ROOT / "interpro" / "panther" / "PTHR11937" / "PTHR11937-paint.tsv"
PANTHER_ENTRIES = REPO_ROOT / "interpro" / "panther" / "PTHR11937" / "PTHR11937-entries.csv"

CONTACT_CUTOFF = 4.0  # Angstrom, heavy atom to heavy atom; same as the ACTL8 analysis
SECOND_SHELL_CUTOFF = 5.0

ACTRT3 = "Q9BYD9"
MOUSE_ACTRT3 = "Q8BXF8"
ACTB = "P60709"

# Control panel. Each entry is here because it fixes one end of an interpretation:
# conventional actins bound the "must polymerise" end, Arp53D and Arp1 are divergent actins
# that nevertheless assemble, Arp11/Arp3 do not homopolymerise, ACTL8 is the merged sibling
# review that earned a REMOVE on this same measurement, and ACTRT1/ACTRT2 are ACTRT3's own
# CDD clade (cd13397, ASKHA_NBD_actin_Arp-T1-3).
PANEL = {
    "P60709": "ACTB (human beta-actin; polymerises; IBA donor)",
    "P63261": "ACTG1 (human gamma-actin; polymerises; IBA donor)",
    "P68133": "ACTA1 (human alpha-skeletal actin; polymerises; IBA donor)",
    "P68032": "ACTC1 (human alpha-cardiac actin; polymerises; IBA donor)",
    "P45891": "Arp53D (Drosophila actin-like 53D; DIVERGENT and polymerises; IBA donor)",
    "P61163": "ACTR1A (human alpha-centractin/Arp1; polymerises in dynactin)",
    "P42025": "ACTR1B (human beta-centractin/Arp1B; polymerises in dynactin)",
    "Q9NZ32": "ACTR10 (human Arp11; does NOT homopolymerise)",
    "P61160": "ACTR2 (human Arp2)",
    "P61158": "ACTR3 (human Arp3)",
    "Q9H568": "ACTL8 (human actin-like 8; merged review REMOVEd its filament rows)",
    "Q8TDG2": "ACTRT1 (human ARP-T1; same CDD clade as ACTRT3)",
    "Q8TDY3": "ACTRT2 (human ARP-T2 / ARPM2; same CDD clade as ACTRT3)",
    "Q9Y615": "ACTL7A (human actin-like 7A; PT protein, ACTRT3 co-IP partner)",
    "Q9Y614": "ACTL7B (human actin-like 7B)",
    "Q8TC94": "ACTL9 (human actin-like 9)",
    "Q5JWF8": "ACTL10 (human actin-like 10)",
}

# The eight divergent relatives, as accessions, so "best preserved of the clade" is computed
# inside this run rather than compared against another script's table.
DIVERGENT = ["Q9BYD9", "Q8TDG2", "Q8TDY3", "Q9Y615", "Q9Y614", "Q9H568", "Q8TC94", "Q5JWF8"]

# Structures. 2BTF is profilin:beta-actin, so it supplies BOTH the nucleotide site and the
# profilin surface from one set of coordinates; 6DJO is a four-protomer F-actin filament.
ATP_STRUCTURE = ("2BTF", "A", ("ATP", "SR"))  # ATP plus the Sr(II) occupying the Mg site
PROFILIN_STRUCTURE = ("2BTF", "A", "P")  # actin chain A, profilin auth chain P
FILAMENT_STRUCTURE = "6DJO"

EXPERIMENTAL_CODES = {
    "EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "HTP", "HDA", "HMP", "HGI", "HEP",
}

# The eight divergent human actin-like / actin-related-T proteins, i.e. the set ACTL8's
# merged review used for its census. Kept identical so the recomputation is comparable.
RELATIVES = {
    "Q9H568": "ACTL8",
    "Q9Y615": "ACTL7A",
    "Q9Y614": "ACTL7B",
    "Q8TC94": "ACTL9",
    "Q5JWF8": "ACTL10",
    "Q8TDG2": "ACTRT1",
    "Q8TDY3": "ACTRT2",
    "Q9BYD9": "ACTRT3",
}

SESSION = requests.Session()
SESSION.headers.update({"Accept": "application/json"})


# --------------------------------------------------------------------------------- io


def require(path: Path, fix: str) -> Path:
    if not path.exists():
        raise FileNotFoundError(f"missing required input {path}\n  regenerate with: {fix}")
    return path


def get_json(url: str, params: dict | None = None) -> dict:
    r = SESSION.get(url, params=params, timeout=180)
    r.raise_for_status()
    return r.json()


def uniprot_sequence(acc: str) -> str:
    r = SESSION.get(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta", timeout=120)
    r.raise_for_status()
    seq = "".join(line.strip() for line in r.text.splitlines()[1:])
    if not seq:
        raise RuntimeError(f"UniProt returned no sequence for {acc}")
    return seq


def uniprot_entry(acc: str) -> dict:
    """Fetch one accession and refuse to return a different protein.

    A merged or deleted accession answers a search with somebody else's entry, which is the
    quietest possible false negative, so the requested accession is checked explicitly.
    """
    data = get_json(
        "https://rest.uniprot.org/uniprotkb/search",
        {"query": f"accession:{acc}", "size": 5,
         "fields": "accession,id,reviewed,protein_name,gene_names,organism_name,length"},
    )
    hits = data.get("results", [])
    exact = [h for h in hits if h["primaryAccession"] == acc]
    if not exact:
        raise RuntimeError(
            f"accession {acc} did not come back as primaryAccession; got "
            f"{[h['primaryAccession'] for h in hits] or 'nothing'} -- the entry is merged or dead"
        )
    e = exact[0]
    desc = e.get("proteinDescription", {})
    name = (desc.get("recommendedName", {}).get("fullName", {}).get("value")
            or (desc.get("submissionNames") or [{}])[0].get("fullName", {}).get("value")
            or "(no name)")
    return {
        "accession": e["primaryAccession"],
        "entry_name": e.get("uniProtkbId"),
        "reviewed": "TrEMBL" if "unreviewed" in (e.get("entryType") or "") else "Swiss-Prot",
        "name": name,
        "genes": [g.get("geneName", {}).get("value") for g in e.get("genes", []) if g.get("geneName")],
        "organism": e.get("organism", {}).get("scientificName"),
        "length": e.get("sequence", {}).get("length"),
    }


def fetch_cif(pdb_id: str) -> str:
    r = SESSION.get(f"https://files.rcsb.org/download/{pdb_id.upper()}.cif", timeout=300)
    r.raise_for_status()
    return r.text


# ------------------------------------------------------------ structure -> residues


def polymer_residues(chain):
    return [res for res in chain
            if res.id[0] != "W" and res.get_resname().upper() in THREE_TO_ONE]


def chain_sequence(residues) -> str:
    return "".join(THREE_TO_ONE[res.get_resname().upper()] for res in residues)


def _record(hits, res, dist, key, value):
    rec = hits.setdefault(res.id[1], {"resname": res.get_resname(), key: set(), "min_dist": dist})
    rec[key].add(value)
    rec["min_dist"] = min(rec["min_dist"], dist)


def _finish(hits, key):
    for rec in hits.values():
        rec[key] = sorted(rec[key])
        rec["min_dist"] = round(rec["min_dist"], 2)
    return hits


def ligand_contacts(model, chain_id: str, ligand_names, cutoff: float):
    chain = model[chain_id]
    residues = polymer_residues(chain)
    ligands = [res for res in chain if res.get_resname().strip() in ligand_names]
    if not ligands:
        raise RuntimeError(
            f"chain {chain_id} carries none of {sorted(ligand_names)}; the structure content "
            "has changed and the ligand list needs revisiting"
        )
    ns = NeighborSearch([a for res in residues for a in res])
    hits: dict[int, dict] = {}
    for lig in ligands:
        for atom in lig:
            for other in ns.search(atom.coord, cutoff):
                _record(hits, other.get_parent(), float(atom - other), "ligands",
                        lig.get_resname().strip())
    return residues, _finish(hits, "ligands")


def partner_chain_contacts(model, chain_id: str, partner_id: str, cutoff: float):
    """Residues of `chain_id` within `cutoff` of the named partner chain."""
    residues = polymer_residues(model[chain_id])
    partner = polymer_residues(model[partner_id])
    if not partner:
        raise RuntimeError(f"chain {partner_id} has no polymer residues; structure changed")
    ns = NeighborSearch([a for res in partner for a in res])
    hits: dict[int, dict] = {}
    for res in residues:
        for atom in res:
            for other in ns.search(atom.coord, cutoff):
                _record(hits, res, float(atom - other), "partners", other.get_parent().get_resname())
    return residues, _finish(hits, "partners"), len(partner)


def filament_interface(model, pdb_id: str, cutoff: float):
    """Residues of the most-buried protomer within `cutoff` of any other protomer."""
    chains = {c.id: polymer_residues(c) for c in model}
    chains = {k: v for k, v in chains.items() if len(v) > 200}
    if len(chains) < 3:
        raise RuntimeError(
            f"{pdb_id} yielded {len(chains)} long protein chains; an interface calculation "
            "needs a multi-protomer filament model"
        )
    best = None
    for cid, residues in chains.items():
        others = [a for k, v in chains.items() if k != cid for res in v for a in res]
        ns = NeighborSearch(others)
        hits: dict[int, dict] = {}
        for res in residues:
            for atom in res:
                for other in ns.search(atom.coord, cutoff):
                    _record(hits, res, float(atom - other), "partners",
                            other.get_parent().get_parent().id)
        if best is None or len(hits) > len(best[2]):
            best = (cid, residues, hits)
    cid, residues, hits = best
    return cid, sorted(chains), residues, _finish(hits, "partners")


# --------------------------------------------------------------------------- alignment


def aligner(matrix: str = "BLOSUM62", open_gap: float = -11, extend_gap: float = -1):
    al = Align.PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load(matrix)
    al.open_gap_score = open_gap
    al.extend_gap_score = extend_gap
    al.mode = "global"
    return al


# ACTRT3 is ~35% identical to actin, inside the range where gap placement can move. If a
# tally is an artefact of one gap model it will not survive a change of matrix and gap costs.
ALIGNMENT_SCHEMES = {
    "BLOSUM62/-11/-1": ("BLOSUM62", -11, -1),
    "BLOSUM45/-14/-2": ("BLOSUM45", -14, -2),
}


def map_positions(query_seq: str, query_numbers: list[int], target_seq: str, al):
    aln = al.align(query_seq, target_seq)[0]
    qi = ti = 0
    mapping: dict[int, tuple[int | None, str]] = {}
    identities = 0
    for qc, tc in zip(aln[0], aln[1]):
        if qc != "-":
            qi += 1
        if tc != "-":
            ti += 1
        if qc != "-":
            if tc != "-":
                mapping[query_numbers[qi - 1]] = (ti, tc)
                if qc == tc:
                    identities += 1
            else:
                mapping[query_numbers[qi - 1]] = (None, "-")
    pct = 100.0 * identities / min(len(query_seq), len(target_seq))
    return mapping, round(pct, 1), float(aln.score)


CONSERVATIVE = [set("GA"), set("ST"), set("DE"), set("KRH"), set("NQ"), set("ILVMF"), set("FYW")]


def classify(ref_aa: str, obs_aa: str) -> str:
    if obs_aa == "-":
        return "gap"
    if ref_aa == obs_aa:
        return "identical"
    if any(ref_aa in grp and obs_aa in grp for grp in CONSERVATIVE):
        return "conservative"
    return "non-conservative"


def local_identity_to(reference: str, query: str) -> dict:
    al = Align.PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score = -11
    al.extend_gap_score = -1
    al.mode = "local"
    aln = al.align(reference, query)[0]
    cols = list(zip(aln[0], aln[1]))
    ident = sum(1 for a, b in cols if a == b and a != "-")
    return {"aligned_columns": len(cols), "identities": ident,
            "pct_identity_over_aligned_block": round(100.0 * ident / len(cols), 1)}


# ----------------------------------------------------------------------- GOA / QuickGO


def split_withfrom(field: str) -> list[str]:
    return [tok for tok in field.split("|") if tok]


def quickgo_evidence(acc: str, go_id: str) -> dict:
    data = get_json(
        "https://www.ebi.ac.uk/QuickGO/services/annotation/search",
        {"geneProductId": f"UniProtKB:{acc}", "goId": go_id, "goUsage": "descendants",
         "goUsageRelationships": "is_a,part_of", "limit": 100},
    )
    results = data.get("results", [])
    return {
        "n_hits": data.get("numberOfHits", 0),
        "per_term": sorted({(r.get("goId"), r.get("goEvidence")) for r in results}),
        "has_experimental": any(r.get("goEvidence") in EXPERIMENTAL_CODES for r in results),
        "experimental_refs": sorted({r.get("reference") for r in results
                                     if r.get("goEvidence") in EXPERIMENTAL_CODES}),
    }


def mouse_annotations(acc: str) -> list[dict]:
    """Every GO annotation the mouse orthologue carries, with its WITH/FROM resolved.

    Recorded in full because the orthologue is where all of ACTRT3's experimental evidence
    lives, and because one of its rows (a profilin IPI) has no counterpart in the human GOA.
    """
    data = get_json(
        "https://www.ebi.ac.uk/QuickGO/services/annotation/search",
        {"geneProductId": f"UniProtKB:{acc}", "limit": 100},
    )
    out = []
    for r in data.get("results", []):
        # QuickGO returns db and id separately, so the prefix must be reconstructed rather
        # than assumed present -- testing `id.startswith("UniProtKB:")` silently matches
        # nothing and empties the partner column without any error.
        xrefs = [(x["db"], x["id"]) for w in (r.get("withFrom") or []) for x in w["connectedXrefs"]]
        entry = {"go_id": r["goId"], "aspect": r["goAspect"], "evidence": r["goEvidence"],
                 "qualifier": r.get("qualifier"), "reference": r["reference"],
                 "with_from": [f"{db}:{i}" for db, i in xrefs]}
        if r["goEvidence"] in EXPERIMENTAL_CODES:
            uniprot_tokens = [i for db, i in xrefs if db == "UniProtKB"]
            entry["partner_entries"] = [uniprot_entry(i) for i in uniprot_tokens]
            # An experimental row whose WITH/FROM names UniProt accessions must resolve all
            # of them; a mismatch means the resolver, not the data, is at fault.
            assert len(entry["partner_entries"]) == len(uniprot_tokens)
        out.append(entry)
    if not out:
        raise RuntimeError(f"QuickGO returned no annotations for {acc}; the accession may be dead")
    return out


def node_human_targets(node: str) -> dict:
    data = get_json(
        "https://www.ebi.ac.uk/QuickGO/services/annotation/search",
        {"withFrom": f"PANTHER:{node}", "taxonId": 9606, "limit": 200},
    )
    by_term: dict[str, set[str]] = {}
    accessions: dict[str, str] = {}
    for r in data.get("results", []):
        by_term.setdefault(r.get("goId"), set()).add(r.get("symbol"))
        accessions[r.get("symbol")] = r.get("geneProductId", "").split(":")[-1]
    return {"n_hits": data.get("numberOfHits", 0),
            "terms": {k: sorted(v) for k, v in sorted(by_term.items())},
            "accessions": dict(sorted(accessions.items()))}


def iba_panther_nodes(acc: str) -> dict:
    data = get_json(
        "https://www.ebi.ac.uk/QuickGO/services/annotation/search",
        {"geneProductId": f"UniProtKB:{acc}", "evidenceCode": "ECO:0000318", "limit": 200},
    )
    nodes: set[str] = set()
    terms: set[str] = set()
    for r in data.get("results", []):
        terms.add(r.get("goId"))
        for w in r.get("withFrom") or []:
            for x in w.get("connectedXrefs", []):
                if x.get("db") == "PANTHER":
                    nodes.add(x.get("id"))
    return {"n_iba_rows": data.get("numberOfHits", 0),
            "panther_nodes": sorted(nodes), "iba_terms": sorted(terms)}


def read_paint(path: Path) -> list[dict]:
    with path.open() as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    if not rows:
        raise RuntimeError(f"{path} has no PAINT rows")
    return rows


def human_family_members(path: Path) -> list[dict]:
    with path.open() as fh:
        rows = list(csv.DictReader(fh))
    members = {r["id"]: {"accession": r["id"], "gene": r["gene"], "name": r["name"],
                         "length": int(r["length"])}
               for r in rows if r["source_tax_id"] == "9606"}
    if not members:
        raise RuntimeError(f"{path} lists no Homo sapiens members; column layout changed")
    return sorted(members.values(), key=lambda m: m["gene"] or m["accession"])


# ------------------------------------------------------------------------------- main


def contact_block(hits, ref_by_num, maps, order):
    return {
        str(n): {
            "structure_residue": f"{ref_by_num[n]}{n}",
            "contacts": rec.get("ligands") or rec.get("partners"),
            "min_dist_A": rec["min_dist"],
            **{acc: {"position": maps[acc][n][0], "residue": maps[acc][n][1],
                     "class": classify(ref_by_num[n], maps[acc][n][1])}
               for acc in order},
        }
        for n, rec in sorted(hits.items())
    }


def tally(hits, ref_by_num, maps, order):
    return {acc: dict(Counter(classify(ref_by_num[n], maps[acc][n][1]) for n in sorted(hits)))
            for acc in order}


def main() -> None:
    require(GOA_TSV, "just fetch-gene human ACTRT3")
    require(PAINT_TSV, "ai-gene-review fetch-panther PTHR11937")
    require(PANTHER_ENTRIES, "ai-gene-review fetch-panther PTHR11937")

    results: dict = {}
    order = [ACTRT3] + list(PANEL)
    sequences = {acc: uniprot_sequence(acc) for acc in order}
    results["inputs"] = {
        "sequence_lengths": {a: len(s) for a, s in sorted(sequences.items())},
        "panel": {ACTRT3: "ACTRT3 (target)", **PANEL},
        "contact_cutoff_A": CONTACT_CUTOFF,
    }
    al = aligner()

    # ---- 2BTF supplies both the nucleotide site and the profilin surface
    pdb_id, actin_chain, ligands = ATP_STRUCTURE
    model_2btf = MMCIFParser(QUIET=True).get_structure(pdb_id, io.StringIO(fetch_cif(pdb_id)))[0]
    struct_residues, atp_hits = ligand_contacts(model_2btf, actin_chain, set(ligands), CONTACT_CUTOFF)
    _, atp_wide = ligand_contacts(model_2btf, actin_chain, set(ligands), SECOND_SHELL_CUTOFF)
    _, prof_hits, n_profilin_res = partner_chain_contacts(
        model_2btf, actin_chain, PROFILIN_STRUCTURE[2], CONTACT_CUTOFF)
    struct_seq = chain_sequence(struct_residues)
    struct_nums = [r.id[1] for r in struct_residues]
    ref_by_num = dict(zip(struct_nums, struct_seq))

    maps_2btf = {}
    align_2btf = {}
    for acc in order:
        mapping, pct, score = map_positions(struct_seq, struct_nums, sequences[acc], al)
        maps_2btf[acc] = mapping
        align_2btf[acc] = {"pct_identity_to_structure_chain": pct, "alignment_score": score}

    results["nucleotide_site"] = {
        "structure": {"pdb_id": pdb_id, "chain": actin_chain, "ligands": list(ligands),
                      "cutoff_A": CONTACT_CUTOFF, "second_shell_cutoff_A": SECOND_SHELL_CUTOFF,
                      "observed_residue_range": [struct_nums[0], struct_nums[-1]]},
        "alignments": align_2btf,
        "contacts": contact_block(atp_hits, ref_by_num, maps_2btf, order),
        "second_shell_only": sorted(f"{ref_by_num[n]}{n}" for n in atp_wide if n not in atp_hits),
        "summary": {"n_contacts": len(atp_hits), **tally(atp_hits, ref_by_num, maps_2btf, order)},
    }
    results["profilin_interface"] = {
        "structure": {"pdb_id": pdb_id, "actin_chain": actin_chain,
                      "profilin_chain": PROFILIN_STRUCTURE[2],
                      "n_profilin_residues": n_profilin_res, "cutoff_A": CONTACT_CUTOFF},
        "rationale": ("mouse ArpM1 co-immunoprecipitates profilin III (PMID:18692047) and "
                      "UniProt records `Interacts with PFN3` by similarity, so this surface is "
                      "the one ACTRT3 has directed experimental reason to retain"),
        "contacts": contact_block(prof_hits, ref_by_num, maps_2btf, order),
        "summary": {"n_contacts": len(prof_hits), **tally(prof_hits, ref_by_num, maps_2btf, order)},
    }

    # ---- filament protomer interface
    fil_cif = fetch_cif(FILAMENT_STRUCTURE)
    model_fil = MMCIFParser(QUIET=True).get_structure(
        FILAMENT_STRUCTURE, io.StringIO(fil_cif))[0]
    fil_chain, all_chains, fil_residues, fil_hits = filament_interface(
        model_fil, FILAMENT_STRUCTURE, CONTACT_CUTOFF)
    fil_seq = chain_sequence(fil_residues)
    fil_nums = [r.id[1] for r in fil_residues]
    fil_ref = dict(zip(fil_nums, fil_seq))
    maps_fil = {}
    align_fil = {}
    for acc in order:
        mapping, pct, _ = map_positions(fil_seq, fil_nums, sequences[acc], al)
        maps_fil[acc] = mapping
        align_fil[acc] = {"pct_identity_to_structure_chain": pct}
    results["filament_interface"] = {
        "structure": {"pdb_id": FILAMENT_STRUCTURE, "chains": all_chains,
                      "analysed_chain": fil_chain, "cutoff_A": CONTACT_CUTOFF},
        "alignments": align_fil,
        "contacts": contact_block(fil_hits, fil_ref, maps_fil, order),
        "summary": {"n_contacts": len(fil_hits), **tally(fil_hits, fil_ref, maps_fil, order)},
    }

    # ---- alignment sensitivity across all three contact sets
    sensitivity: dict = {}
    for scheme, (matrix, og, eg) in ALIGNMENT_SCHEMES.items():
        alt = aligner(matrix, og, eg)
        entry = {}
        for acc in order:
            m2, _, _ = map_positions(struct_seq, struct_nums, sequences[acc], alt)
            mf, _, _ = map_positions(fil_seq, fil_nums, sequences[acc], alt)
            entry[acc] = {
                "nucleotide_site": dict(Counter(classify(ref_by_num[n], m2[n][1]) for n in sorted(atp_hits))),
                "profilin_interface": dict(Counter(classify(ref_by_num[n], m2[n][1]) for n in sorted(prof_hits))),
                "filament_interface": dict(Counter(classify(fil_ref[n], mf[n][1]) for n in sorted(fil_hits))),
            }
        sensitivity[scheme] = entry
    results["alignment_sensitivity"] = sensitivity

    # ---- Analysis B: PAINT's own rejections of GO:0005200 in this family
    paint = read_paint(PAINT_TSV)
    goa_rows = list(csv.DictReader(GOA_TSV.open(), delimiter="\t"))
    actrt3_nodes = sorted({tok.split(":", 1)[1] for r in goa_rows
                           for tok in split_withfrom(r["WITH/FROM"]) if tok.startswith("PANTHER:")})
    rejected = [r for r in paint if r["go_id"] == "GO:0005200" and r["negated"] == "true"]
    asserted = [r for r in paint if r["go_id"] == "GO:0005200" and r["negated"] == "false"]
    general_instead = [r for r in paint if r["go_id"] == "GO:0005198" and r["negated"] == "false"]
    node_cache: dict[str, dict] = {}

    def targets(node: str) -> dict:
        if node not in node_cache:
            node_cache[node] = node_human_targets(node)
        return node_cache[node]

    results["paint_go0005200"] = {
        "asserted_at": [{"node": r["node"], "evidence": r["evidence"], "date": r["date"],
                         "n_seeds": len(split_withfrom(r["seeds"])),
                         "seeds": split_withfrom(r["seeds"]),
                         "human_targets": targets(r["node"])["accessions"]}
                        for r in asserted],
        "rejected_at": [{"node": r["node"], "evidence": r["evidence"], "date": r["date"],
                         "blocked_from": split_withfrom(r["seeds"]),
                         "human_targets": targets(r["node"])["accessions"],
                         "other_terms_at_node": sorted({p["go_id"] for p in paint
                                                        if p["node"] == r["node"]
                                                        and p["go_id"] != "GO:0005200"})}
                        for r in sorted(rejected, key=lambda x: x["date"])],
        "general_parent_asserted_at": [
            {"node": r["node"], "evidence": r["evidence"], "date": r["date"],
             "seeds": split_withfrom(r["seeds"]),
             "human_targets": targets(r["node"])["accessions"],
             "go0005200_also_rejected_here": any(p["node"] == r["node"] and p["go_id"] == "GO:0005200"
                                                 and p["negated"] == "true" for p in paint)}
            for r in general_instead],
        "actrt3_nodes": actrt3_nodes,
        "actrt3_go0005200_rejected_anywhere_on_its_path": [
            r["node"] for r in rejected if r["node"] in actrt3_nodes],
    }

    # ---- Analysis C: donor vs recipient composition of ACTRT3's two donating nodes
    clades = {}
    for node in actrt3_nodes:
        info = targets(node)
        seed_rows = [r for r in paint if r["node"] == node and r["negated"] == "false"]
        recipients = []
        for symbol, acc in info["accessions"].items():
            if acc not in sequences:
                sequences[acc] = uniprot_sequence(acc)
            recipients.append({"symbol": symbol, "accession": acc,
                               "length": len(sequences[acc]),
                               **local_identity_to(sequences[ACTB], sequences[acc])})
        recipients.sort(key=lambda m: -m["pct_identity_over_aligned_block"])
        clades[node] = {
            "n_human_annotations": info["n_hits"],
            "donated_terms": info["terms"],
            "paint_rows_at_node": [{"go_id": r["go_id"], "evidence": r["evidence"],
                                    "date": r["date"], "n_seeds": len(split_withfrom(r["seeds"]))}
                                   for r in seed_rows],
            "human_recipients": recipients,
        }
    id_by_acc = {m["accession"]: m["pct_identity_over_aligned_block"]
                 for c in clades.values() for m in c["human_recipients"]}
    results["donating_nodes"] = {
        "nodes": clades,
        "summary": {
            "ACTRT3_identity_to_ACTB_pct": id_by_acc.get(ACTRT3),
            "n_human_recipients_per_node": {n: len(c["human_recipients"]) for n, c in clades.items()},
        },
    }

    # ---- Analysis D: relatives census, recomputed live
    rel = {sym: {"accession": acc, **iba_panther_nodes(acc)} for acc, sym in RELATIVES.items()}
    others = [v["n_iba_rows"] for s, v in rel.items() if s != "ACTL8"]
    results["relatives"] = {
        "per_gene": dict(sorted(rel.items())),
        "summary": {
            "n_relatives_examined": len(rel),
            "ACTL8_iba_rows": rel["ACTL8"]["n_iba_rows"],
            "ACTRT3_iba_rows": rel["ACTRT3"]["n_iba_rows"],
            "median_iba_rows_excluding_ACTL8": statistics.median(others),
            "iba_rows_by_gene": {s: v["n_iba_rows"] for s, v in sorted(rel.items())},
            "genes_sharing_all_of_ACTRT3s_nodes": sorted(
                s for s, v in rel.items() if set(actrt3_nodes) <= set(v["panther_nodes"])),
        },
    }

    # ---- Analysis E: the mouse orthologue behind the only experimental evidence
    mouse = uniprot_entry(MOUSE_ACTRT3)
    sequences[MOUSE_ACTRT3] = uniprot_sequence(MOUSE_ACTRT3)
    donated = sorted({r["GO TERM"] for r in goa_rows
                      if f"UniProtKB:{MOUSE_ACTRT3}" in split_withfrom(r["WITH/FROM"])})
    _, mouse_global_pct, _ = map_positions(
        sequences[MOUSE_ACTRT3], list(range(1, len(sequences[MOUSE_ACTRT3]) + 1)),
        sequences[ACTRT3], al)
    results["mouse_orthologue"] = {
        "entry": mouse,
        "global_identity_to_human_ACTRT3": {"pct_identity": mouse_global_pct},
        "local_identity_to_human_ACTRT3": local_identity_to(sequences[ACTRT3], sequences[MOUSE_ACTRT3]),
        "local_identity_to_ACTB": local_identity_to(sequences[ACTB], sequences[MOUSE_ACTRT3]),
        "terms_it_donates_to_human_ACTRT3": donated,
        "its_own_evidence_for_each": {go: quickgo_evidence(MOUSE_ACTRT3, go) for go in donated},
        "full_annotation_set": mouse_annotations(MOUSE_ACTRT3),
    }

    # ---- ranking of the divergent clade on each of the three contact sets
    compat = {}
    for label, hits, ref, maps in (("nucleotide_site", atp_hits, ref_by_num, maps_2btf),
                                   ("profilin_interface", prof_hits, ref_by_num, maps_2btf),
                                   ("filament_interface", fil_hits, fil_ref, maps_fil)):
        t = tally(hits, ref, maps, DIVERGENT)
        # A LIST of pairs, not a dict: results.json is written with sort_keys=True, which would
        # silently re-alphabetise a dict and destroy the ranking order that is the whole point
        # of this block. Found because audit_claims.py rebuilds the RESULTS.md table row from
        # this field and the reconstruction did not match the committed report.
        compat[label] = {
            "n_contacts": len(hits),
            "compatible_identical_plus_conservative": sorted(
                ([acc, t[acc].get("identical", 0) + t[acc].get("conservative", 0)]
                 for acc in DIVERGENT), key=lambda kv: -kv[1]),
        }
    results["divergent_clade_ranking"] = {
        "accession_to_symbol": {a: (PANEL.get(a) or "ACTRT3 (target)").split(" ")[0] for a in DIVERGENT},
        "per_contact_set": compat,
    }

    # ---- family context: how many human PTHR11937 members have experimental MF at all
    members = human_family_members(PANTHER_ENTRIES)
    results["family"] = {"n_human_members_listed": len(members),
                         "members": [m["gene"] for m in members]}

    (HERE / "results.json").write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
    write_report(results, order, ref_by_num, atp_hits, prof_hits, fil_ref, fil_hits,
                 maps_2btf, maps_fil)
    print(f"wrote {HERE / 'results.json'} and {HERE / 'RESULTS.md'}")


def fmt_table(hits, ref_by_num, maps, columns, labels) -> list[str]:
    lines = ["| Structure residue | Contacts | min dist (Å) | " + " | ".join(labels[c] for c in columns) + " |",
             "|" + "---|" * (3 + len(columns))]
    for num in sorted(hits):
        rec = hits[num]
        ref_aa = ref_by_num[num]
        tag = ", ".join(rec.get("ligands") or rec.get("partners") or [])
        cells = []
        for acc in columns:
            pos, aa = maps[acc][num]
            kind = classify(ref_aa, aa)
            mark = {"identical": "", "conservative": " ~", "non-conservative": " **", "gap": ""}[kind]
            cells.append("gap" if aa == "-" else f"{aa}{pos if pos else ''}{mark}")
        lines.append(f"| {ref_aa}{num} ({rec['resname']}) | {tag} | {rec['min_dist']} | "
                     + " | ".join(cells) + " |")
    return lines


def write_report(results, order, ref_by_num, atp_hits, prof_hits, fil_ref, fil_hits,
                 maps_2btf, maps_fil) -> None:
    short = {ACTRT3: "ACTRT3"}
    for acc, desc in PANEL.items():
        short[acc] = desc.split(" ")[0]
    L: list[str] = []
    A = L.append
    A("# ACTRT3: which of actin's residues survive, and has PAINT already rejected this term next door?")
    A("")
    A("Generated by `uv run python analyze_actrt3.py`. Every number is computed at run time from")
    A("the UniProt REST API, RCSB coordinate files, QuickGO, and the repository's PANTHER/PAINT")
    A("export. Nothing here is hardcoded; re-running regenerates this file.")
    A("")
    A("Structural machinery (contact detection, alignment, substitution classing, two-scheme")
    A("sensitivity) is deliberately identical to `genes/human/ACTL8/ACTL8-bioinformatics/analyze_actl8.py`")
    A("so the tallies are directly comparable with that merged sibling review.")
    A("")

    # --- headline
    ns = results["nucleotide_site"]["summary"]
    ps = results["profilin_interface"]["summary"]
    fs = results["filament_interface"]["summary"]

    def line(s, acc):
        d = s[acc]
        return (f"{d.get('identical', 0)} identical, {d.get('conservative', 0)} conservative, "
                f"{d.get('non-conservative', 0)} non-conservative, {d.get('gap', 0)} gaps")

    A("## Headline")
    A("")
    A(f"- Nucleotide site, {ns['n_contacts']} contacts (PDB {results['nucleotide_site']['structure']['pdb_id']} "
      f"chain {results['nucleotide_site']['structure']['chain']}): ACTRT3 = {line(ns, ACTRT3)}.")
    A(f"- Profilin surface, {ps['n_contacts']} contacts (same structure, profilin chain "
      f"{results['profilin_interface']['structure']['profilin_chain']}): ACTRT3 = {line(ps, ACTRT3)}.")
    A(f"- Filament protomer interface, {fs['n_contacts']} contacts (PDB "
      f"{results['filament_interface']['structure']['pdb_id']}, chain "
      f"{results['filament_interface']['structure']['analysed_chain']}): ACTRT3 = {line(fs, ACTRT3)}.")
    A("")
    A("Controls on the same three measurements:")
    A("")
    A("| Protein | Role in the comparison | Nucleotide site | Profilin surface | Filament interface |")
    A("|---|---|---|---|---|")
    for acc in order:
        role = "target" if acc == ACTRT3 else PANEL[acc].split("(", 1)[1].rstrip(")")
        A(f"| {short[acc]} | {role} | {line(ns, acc)} | {line(ps, acc)} | {line(fs, acc)} |")
    A("")

    A("## Ranking within the divergent clade")
    A("")
    A("Chemically compatible contacts (identical + conservative) for the eight divergent human")
    A("actin-like / actin-related-T proteins, all computed in this run:")
    A("")
    r = results["divergent_clade_ranking"]
    sym = r["accession_to_symbol"]
    A("| Contact set | n | Ranking, best first |")
    A("|---|---|---|")
    for label, block in r["per_contact_set"].items():
        ranked = ", ".join(f"{sym[a]} {v}" for a, v in
                           block["compatible_identical_plus_conservative"])
        A(f"| {label} | {block['n_contacts']} | {ranked} |")
    A("")

    A("## Alignment sensitivity")
    A("")
    A("Same tallies under a second substitution matrix and gap model, for ACTRT3 only:")
    A("")
    A("| Scheme | Nucleotide site | Profilin surface | Filament interface |")
    A("|---|---|---|---|")
    for scheme, per in results["alignment_sensitivity"].items():
        d = per[ACTRT3]
        cells = []
        for k in ("nucleotide_site", "profilin_interface", "filament_interface"):
            v = d[k]
            cells.append(f"{v.get('identical', 0)}/{v.get('conservative', 0)}/"
                         f"{v.get('non-conservative', 0)}/{v.get('gap', 0)}")
        A(f"| {scheme} | " + " | ".join(cells) + " |")
    A("")
    A("(identical / conservative / non-conservative / gap)")
    A("")

    A("## Per-residue tables")
    A("")
    cols = [ACTRT3, "P60709", "P45891", "P61163", "Q9NZ32", "Q9H568", "Q8TDG2", "Q8TDY3"]
    A(f"### Nucleotide site ({results['nucleotide_site']['structure']['pdb_id']} chain "
      f"{results['nucleotide_site']['structure']['chain']}, "
      f"{results['nucleotide_site']['structure']['ligands']}, "
      f"{results['nucleotide_site']['structure']['cutoff_A']} Å)")
    A("")
    L.extend(fmt_table(atp_hits, ref_by_num, maps_2btf, cols, short))
    A("")
    A("### Profilin surface (same structure, contacts to the profilin chain)")
    A("")
    L.extend(fmt_table(prof_hits, ref_by_num, maps_2btf, cols, short))
    A("")
    A(f"### Filament protomer interface ({results['filament_interface']['structure']['pdb_id']})")
    A("")
    L.extend(fmt_table(fil_hits, fil_ref, maps_fil, cols, short))
    A("")
    A("`~` conservative, `**` non-conservative, `gap` no aligned residue.")
    A("")

    A("## PAINT's own handling of GO:0005200 inside PTHR11937")
    A("")
    p = results["paint_go0005200"]
    for r in p["asserted_at"]:
        A(f"- **Asserted** at `{r['node']}` ({r['evidence']}, {r['date']}) from {r['n_seeds']} seeds; "
          f"human recipients: {', '.join(sorted(r['human_targets'])) or 'none'}.")
    A("")
    A(f"- **Rejected** (negated IRD) at {len(p['rejected_at'])} descendant nodes:")
    A("")
    A("| Node | Date | Other terms curated at that node | Human genes at the node |")
    A("|---|---|---|---|")
    for r in p["rejected_at"]:
        A(f"| `{r['node']}` | {r['date']} | {', '.join(r['other_terms_at_node']) or '—'} | "
          f"{', '.join(sorted(r['human_targets'])) or '—'} |")
    A("")
    A("- Nodes where the **general parent** `GO:0005198 structural molecule activity` is asserted instead:")
    A("")
    A("| Node | Date | GO:0005200 also rejected here | Human genes at the node |")
    A("|---|---|---|---|")
    for r in p["general_parent_asserted_at"]:
        A(f"| `{r['node']}` | {r['date']} | {r['go0005200_also_rejected_here']} | "
          f"{', '.join(sorted(r['human_targets'])) or '—'} |")
    A("")
    A(f"ACTRT3's own donating nodes are {p['actrt3_nodes']}; GO:0005200 is rejected on that path at: "
      f"{p['actrt3_go0005200_rejected_anywhere_on_its_path'] or 'no node'}.")
    A("")

    A("## Donor versus recipient composition of ACTRT3's two donating nodes")
    A("")
    for node, c in results["donating_nodes"]["nodes"].items():
        A(f"### `{node}`")
        A("")
        A(f"- PAINT rows curated at this node: "
          + ", ".join(f"{r['go_id']} ({r['evidence']}, {r['n_seeds']} seeds, {r['date']})"
                      for r in c["paint_rows_at_node"]))
        A(f"- Terms it donates to human genes: {', '.join(sorted(c['donated_terms']))}")
        A(f"- {len(c['human_recipients'])} human recipients, by local identity to beta-actin:")
        A("")
        A("| Gene | Accession | Length | % identity to ACTB (local) |")
        A("|---|---|---|---|")
        for m in c["human_recipients"]:
            A(f"| {m['symbol']} | {m['accession']} | {m['length']} | {m['pct_identity_over_aligned_block']} |")
        A("")

    A("## Relatives census, recomputed from QuickGO")
    A("")
    s = results["relatives"]["summary"]
    A(f"ACTL8 carries {s['ACTL8_iba_rows']} IBA rows; ACTRT3 carries {s['ACTRT3_iba_rows']}; "
      f"the median across the other seven divergent relatives is {s['median_iba_rows_excluding_ACTL8']}.")
    A("")
    A("| Gene | IBA rows | PANTHER nodes | IBA terms |")
    A("|---|---|---|---|")
    for sym, v in results["relatives"]["per_gene"].items():
        A(f"| {sym} | {v['n_iba_rows']} | {', '.join(v['panther_nodes'])} | {', '.join(v['iba_terms'])} |")
    A("")

    A("## The mouse orthologue behind the only experimental evidence")
    A("")
    m = results["mouse_orthologue"]
    A(f"- `{m['entry']['accession']}` = {m['entry']['entry_name']} ({m['entry']['reviewed']}), "
      f"{m['entry']['name']}, genes {m['entry']['genes']}, {m['entry']['length']} aa.")
    A(f"- Global identity to human ACTRT3: {m['global_identity_to_human_ACTRT3']['pct_identity']}%; "
      f"local {m['local_identity_to_human_ACTRT3']['pct_identity_over_aligned_block']}%. "
      f"Local identity to beta-actin for comparison: "
      f"{m['local_identity_to_ACTB']['pct_identity_over_aligned_block']}%.")
    A(f"- Terms it donates: {', '.join(m['terms_it_donates_to_human_ACTRT3'])}")
    for go, ev in m["its_own_evidence_for_each"].items():
        A(f"  - {go}: {ev['n_hits']} annotations, codes {ev['per_term']}, "
          f"own experimental = {ev['has_experimental']}, refs {ev['experimental_refs']}")
    A("")
    A("Its complete annotation set, so that any row without a human counterpart is visible:")
    A("")
    A("| GO id | Aspect | Ev | Qualifier | Reference | WITH/FROM | Resolved experimental partner |")
    A("|---|---|---|---|---|---|---|")
    for a_ in m["full_annotation_set"]:
        partners = "; ".join(
            f"{p['accession']} {p['genes']} ({p['reviewed']}, {p['organism']})"
            for p in a_.get("partner_entries", []))
        A(f"| {a_['go_id']} | {a_['aspect'][:2].upper()} | {a_['evidence']} | {a_['qualifier']} | "
          f"{a_['reference']} | {', '.join(a_['with_from']) or '—'} | {partners or '—'} |")
    A("")

    (HERE / "RESULTS.md").write_text("\n".join(L) + "\n")


if __name__ == "__main__":
    main()
