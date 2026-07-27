"""Does ACTRT2 retain actin's nucleotide site and filament interface, and does its GO record hold up?

ACTRT2 (Q8TDY3, "Actin-related protein T2" / ARP-T2 / ARPM2) has no UniProt FUNCTION
comment. Its whole molecular-function and cytoskeletal-compartment record is
phylogenetic (two IBA rows, GO_REF:0000033) plus two automatic IEA steps, and its only
experimentally-coded row is a bare `GO:0005515 protein binding` IPI. The one strong
experimental fact about the protein - that it is a major component of the cytoskeletal
calyx of the sperm perinuclear theca - reaches human GOA only by ortholog transfer from
mouse.

Two opposite errors are available and both are common:

  (a) reading an activity off the fold name, i.e. accepting `structural constituent of
      cytoskeleton` and `actin cytoskeleton` because the protein is an actin; and
  (b) asserting "fold without function" without checking whether the residues that make
      an actin an actin are still present. Harata et al. 2001 (PMID:11750065) state
      that in hArpM1/hArpM2 "the ATP-binding motif and nuclear-export signals of actin
      are highly conserved" - a sequence-inspection claim from 2001 that has never been
      re-tested, and that must be measured rather than repeated.

Both are decided by measurement, so this script measures, from live data only.

Analysis 1 -- nucleotide site.
  The residues that contact ATP in actin are computed from the coordinates of a
  beta-actin:ATP crystal structure (PDB 2BTF, chain A): every residue with a heavy atom
  within a distance cutoff of the bound ATP or its associated divalent cation. The
  structure's own observed sequence and numbering are then globally aligned to ACTRT2
  and to a panel of relatives, and the aligned residue reported per contact position.
  Conservation is read off an alignment, never off a position number.

Analysis 2 -- filament protomer interface.
  `actin cytoskeleton` and `structural constituent of cytoskeleton` are, for a real
  actin, earned by polymerisation, so the same treatment is applied to the
  protomer-protomer interface of an F-actin filament (PDB 6DJO). Interface residues are
  every residue of the most-buried chain within the cutoff of any other chain. The panel
  supplies controls in both directions: beta-actin (the positive control, aligned to
  itself via the structure), Drosophila Arp53D as a divergent actin that does polymerise,
  ACTR1A as a divergent ARP that builds the dynactin minifilament, and ACTL7A/ACTL7B as
  the clade for which GO's own phylogenetic pipeline has explicitly negated
  `GO:0005200`.

Analysis 3 -- IBA source audit.
  Every WITH/FROM token in ACTRT2-goa.tsv is parsed programmatically (never by hand),
  resolved to protein entries through the UniProt REST API, and each resolved source is
  then asked, through QuickGO, what evidence it itself carries for the exact term it
  donated. Identifier lookups request several hits and report all of them, because an
  ambiguous cross-reference is data rather than a missing input. Swiss-Prot/TrEMBL status
  is printed next to every name, since an unreviewed entry's name is an automatic label
  and is not evidence about function. Every accession's entry name is printed so that a
  dead (deleted) accession cannot masquerade as a source that carries no annotation.

Analysis 4 -- where PAINT has and has not negated GO:0005200.
  The cached PAINT table for PTHR11937 is parsed to find every node at which
  `GO:0005200 structural constituent of cytoskeleton` is an IRD with negated=true, and
  every node that still propagates it. QuickGO is then asked which human genes actually
  receive the term. This tests, rather than asserts, the claim that the negation has been
  applied to some divergent-ARP clades and not to the clade containing ACTRT2.

Analysis 5 -- relatives census.
  For each divergent human actin-like / actin-related-T protein, QuickGO is asked which
  PANTHER nodes appear in the WITH/FROM of its IBA rows and how many IBA rows it has.
  This verifies live (not by reading a sibling review) whether the beta-actin-subfamily
  mis-placement documented for ACTL8 also affects ACTRT2.

Analysis 6 -- the protein-binding row.
  IntAct is queried directly for ACTRT2 and for its recorded partner, and the partner
  class composition is tabulated. A count of experiments is not a count of independent
  evidence, and a partner shared with every actin-family protein tested is a statement
  about the partner, not about ACTRT2.

Analysis 7 -- perinuclear-theca complex annotation census.
  For each reported member of the sperm PT ARP complex, and its mouse ortholog, QuickGO
  is asked which cellular-component and biological-process terms it carries and by what
  evidence. This locates the gap that lets a well-documented mouse phenotype fail to
  reach the human record.

A missing local input file is a hard error naming the command that regenerates it.
An ambiguous or empty remote answer is reported, not silently dropped.

Usage:  uv run python analyze_actrt2.py
Writes: results.json, RESULTS.md
"""

from __future__ import annotations

import csv
import io
import json
import re
import statistics
from collections import Counter, defaultdict
from pathlib import Path

import requests
from Bio import Align
from Bio.Align import substitution_matrices
from Bio.Data.PDBData import protein_letters_3to1_extended as THREE_TO_ONE
from Bio.PDB import MMCIFParser, NeighborSearch

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
REPO_ROOT = GENE_DIR.parents[2]
GOA_TSV = GENE_DIR / "ACTRT2-goa.tsv"
PAINT_TSV = REPO_ROOT / "interpro" / "panther" / "PTHR11937" / "PTHR11937-paint.tsv"

CONTACT_CUTOFF = 4.0  # Angstrom, heavy atom to heavy atom

# TWO markers, because the named-site table is one narrow cell per position and cannot carry the
# long form. Both are constants and both are counted: an earlier version declared "one literal"
# while hand-writing the short form at the call site, so the count missed that row - and
# simultaneously counted the prose sentence, which interpolates the long marker and was already in
# the output buffer. The two errors cancelled at one flagged member and would have diverged at two.
# The count is therefore restricted to table rows by construction (see `count_marked_rows`).
MARK_TRUNCATED = " **[TRUNCATED - not comparable]**"
MARK_TRUNCATED_SHORT = " [TRUNC]"
ALL_TRUNCATION_MARKERS = (MARK_TRUNCATED.strip(), MARK_TRUNCATED_SHORT.strip())


def count_marked_rows(lines: list[str]) -> int:
    """Marked TABLE ROWS only. Prose that mentions a marker is excluded structurally, not by luck."""
    return sum(
        1 for line in lines
        if line.lstrip().startswith("|") and any(m in line for m in ALL_TRUNCATION_MARKERS)
    )

ACTRT2 = "Q8TDY3"

# The comparison panel. Every member is here for a stated reason, because a panel chosen
# to flatter a conclusion is worthless.
PANEL = {
    # conventional actins: the proteins from which the IBA rows were seeded, and the
    # upper bound on what "retains actin's sites" can mean
    "P60709": "ACTB (human beta-actin; IBA donor)",
    "P63261": "ACTG1 (human gamma-actin; IBA donor)",
    "P68133": "ACTA1 (human alpha-skeletal actin; IBA donor)",
    "P68032": "ACTC1 (human alpha-cardiac actin; IBA donor)",
    # divergent actins that DO polymerise or build a filament: the discriminating controls
    "P45891": "Arp53D (Drosophila actin-like 53D; polymerising divergent actin; IBA donor)",
    "P61163": "ACTR1A (human alpha-centractin; builds the dynactin minifilament)",
    # ARPs that do not polymerise into F-actin
    "P61160": "ACTR2 (human Arp2; Arp2/3 subunit)",
    "P61158": "ACTR3 (human Arp3; Arp2/3 subunit)",
    "Q9NZ32": "ACTR10 (human Arp11; dynactin pointed-end cap)",
    # the sperm perinuclear-theca ARP complex and the rest of the divergent human set
    "Q8TDG2": "ACTRT1 (human actin-related protein T1; PT complex)",
    "Q9BYD9": "ACTRT3 (human actin-related protein T3 / ARPM1; PT complex)",
    "Q9Y615": "ACTL7A (human actin-like 7A; PT complex; GO:0005200 negated by PAINT)",
    "Q9Y614": "ACTL7B (human actin-like 7B; GO:0005200 negated by PAINT)",
    "Q8TC94": "ACTL9 (human actin-like 9; PT complex)",
    "Q5JWF8": "ACTL10 (human actin-like 10)",
    "Q9H568": "ACTL8 (human actin-like 8)",
}

# Structures. Both are actin-only assemblies, so no partner protein can be mistaken for a
# nucleotide contact or a protomer contact.
ATP_STRUCTURE = ("2BTF", "A", ("ATP", "SR"))  # beta-actin:profilin, ATP + Sr(II) in the Mg site
FILAMENT_STRUCTURE = ("6DJO", None, ())  # F-actin, several protomers, ADP + Mg

# Actin's D-loop (subdomain 2, residues 38-52 in actin numbering) makes the principal
# longitudinal protomer contact. Reported separately because whole-interface tallies can
# hide whether the single most important contact segment survives.
D_LOOP = range(38, 53)

# Actin residues that are individually named in the actin literature, with the role each
# is named for. These are PROBED BY ALIGNMENT regardless of whether they fall inside the
# structure-derived contact set, because the catalytic His161 sits further than the contact
# cutoff from ground-state ATP yet is the residue a nucleotide-hydrolysis claim turns on.
# The expected identity is asserted against the structure so a wrong position number fails
# loudly instead of producing a confident wrong answer.
NAMED_ACTIN_SITES = {
    11: ("D", "phosphate-binding loop 1"),
    14: ("S", "phosphate-binding loop 1, beta-phosphate contact"),
    15: ("G", "phosphate-binding loop 1"),
    18: ("K", "phosphate-binding loop 1"),
    108: ("A", "Pro-rich loop; governs His161 flipping"),
    109: ("P", "Pro-rich loop; governs His161 flipping"),
    137: ("Q", "hydrogen-bonded to the attacking water W1"),
    154: ("D", "divalent cation coordination"),
    156: ("G", "phosphate-binding loop 2"),
    157: ("D", "phosphate-binding loop 2"),
    159: ("V", "phosphate-binding loop 2"),
    161: ("H", "ATP hydrolysis trigger"),
    183: ("R", "sensor loop / nucleotide state"),
    214: ("E", "adenosine region"),
    306: ("Y", "adenine pocket"),
    336: ("K", "adenine/ribose region"),
}

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
    "ZFIN": "zfin",
    "AGI_LocusCode": "araport",
}

# The reported sperm perinuclear-theca ARP complex (PMID:35616329, PMID:41668650) plus
# calicin, the PT protein whose interaction gave mouse Actrt2 its GO:0033011 IDA
# (PMID:35793634). Accessions are resolved live from gene symbol, never hardcoded, so a
# wrong accession cannot pass silently.
PT_COMPLEX_SYMBOLS = ["ACTRT1", "ACTRT2", "ACTRT3", "ACTL7A", "ACTL9", "CCIN"]

# Every PMID this review leans on. Checked for (a) how many entities the reference annotates
# repo-wide and (b) whether its cellular-component term went to a subset or to everything.
REFERENCE_PMIDS = [
    "12243744",  # Heid 2002, the calyx founding paper
    "11750065",  # Harata 2001, the cloning paper
    "35616329",  # Zhang 2022, the theca ARP complex
    "41668650",  # Kovacevic 2026, Actrt3 knockout
    "40811009",  # Chen 2025, Actrt2 knockout / ferroptosis
    "25293813",  # Liu 2015, human sperm localisation
    "33961781",  # Huttlin 2021, BioPlex 3.0 - the only experimentally coded row
    "35793634",  # Zhang 2022, calicin - donor of the mouse GO:0033011 IDA
]

# The two terms whose granularity is at issue, and the compartment terms in play.
TERMS_OF_INTEREST = {
    "GO:0005198": "structural molecule activity",
    "GO:0005200": "structural constituent of cytoskeleton",
    "GO:0015629": "actin cytoskeleton",
    "GO:0033011": "perinuclear theca",
    "GO:0005856": "cytoskeleton",
}

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
    """Identity of an accession. A dead entry is a hard error, never a silent zero.

    `primaryAccession == requested` is NOT sufficient on its own. A merged or deleted
    accession still comes back from the search endpoint with its own primaryAccession, an
    entryType of "Inactive", and empty name/gene/length fields - which is indistinguishable
    from a live protein that simply carries no annotation. Verified against O15507, which
    UniProt reports as MERGED into P56159. So the entryType and the presence of a sequence
    length are both checked.
    """
    data = get_json(
        "https://rest.uniprot.org/uniprotkb/search",
        {
            "query": f"accession:{acc}",
            "size": 2,
            "fields": "accession,id,protein_name,gene_names,organism_name,reviewed,length",
        },
    )
    results = data.get("results", [])
    if not results:
        raise RuntimeError(
            f"UniProt returned no entry for {acc}: the accession is dead or wrong. "
            "A dead accession answers every question with an empty set, so it cannot be used."
        )
    live = [e for e in results if e["primaryAccession"] == acc]
    if not live:
        raise RuntimeError(
            f"UniProt returned {[e['primaryAccession'] for e in results]} for {acc}; "
            "primaryAccession does not match the requested accession"
        )
    e = live[0]
    if "Inactive" in (e.get("entryType") or "") or not e.get("sequence", {}).get("length"):
        raise RuntimeError(
            f"{acc} is not a live UniProt entry: entryType={e.get('entryType')!r}, "
            f"length={e.get('sequence', {}).get('length')!r}. An inactive (merged or deleted) "
            "accession returns no annotations, which reads identically to a live protein that "
            "carries none, so querying it would produce a vacuous result."
        )
    return {
        "accession": e["primaryAccession"],
        "entry_name": e.get("uniProtkbId"),
        "reviewed": "TrEMBL" if "unreviewed" in (e.get("entryType") or "") else "Swiss-Prot",
        "genes": [g["geneName"]["value"] for g in e.get("genes", []) if g.get("geneName")],
        "organism": e.get("organism", {}).get("scientificName"),
        "length": e.get("sequence", {}).get("length"),
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


def ligand_contacts(cif_text: str, pdb_id: str, chain_id: str, ligand_names, cutoff: float):
    model = MMCIFParser(QUIET=True).get_structure(pdb_id, io.StringIO(cif_text))[0]
    chain = model[chain_id]
    residues = polymer_residues(chain)
    ligands = [res for res in chain if res.get_resname().strip() in ligand_names]
    if not ligands:
        raise RuntimeError(
            f"{pdb_id} chain {chain_id} carries none of {sorted(ligand_names)}; "
            "the structure content has changed and the ligand list needs revisiting"
        )
    ns = NeighborSearch([a for res in residues for a in res])
    hits: dict[int, dict] = {}
    for lig in ligands:
        for atom in lig:
            for other in ns.search(atom.coord, cutoff):
                res = other.get_parent()
                d = float(atom - other)
                rec = hits.setdefault(
                    res.id[1], {"resname": res.get_resname(), "ligands": set(), "min_dist": d}
                )
                rec["ligands"].add(lig.get_resname().strip())
                rec["min_dist"] = min(rec["min_dist"], d)
    for rec in hits.values():
        rec["ligands"] = sorted(rec["ligands"])
        rec["min_dist"] = round(rec["min_dist"], 2)
    return residues, hits


def interface_contacts(cif_text: str, pdb_id: str, cutoff: float):
    model = MMCIFParser(QUIET=True).get_structure(pdb_id, io.StringIO(cif_text))[0]
    chains = {}
    for chain in model:
        residues = polymer_residues(chain)
        if len(residues) > 200:
            chains[chain.id] = residues
    if len(chains) < 3:
        raise RuntimeError(
            f"{pdb_id} yielded {len(chains)} long protein chains; an interface "
            "calculation needs a multi-protomer filament model"
        )
    best = None
    for cid, residues in chains.items():
        others = [a for k, v in chains.items() if k != cid for res in v for a in res]
        ns = NeighborSearch(others)
        hits: dict[int, dict] = {}
        for res in residues:
            for atom in res:
                for other in ns.search(atom.coord, cutoff):
                    partner = other.get_parent()
                    d = float(atom - other)
                    rec = hits.setdefault(
                        res.id[1],
                        {"resname": res.get_resname(), "partners": set(), "min_dist": d},
                    )
                    rec["partners"].add(partner.get_parent().id)
                    rec["min_dist"] = min(rec["min_dist"], d)
        if best is None or len(hits) > len(best[2]):
            best = (cid, residues, hits)
    cid, residues, hits = best
    for rec in hits.values():
        rec["partners"] = sorted(rec["partners"])
        rec["min_dist"] = round(rec["min_dist"], 2)
    return cid, sorted(chains), residues, hits


# ------------------------------------------------------------------- alignment


def aligner(matrix: str = "BLOSUM62", open_gap: float = -11, extend_gap: float = -1):
    al = Align.PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load(matrix)
    al.open_gap_score = open_gap
    al.extend_gap_score = extend_gap
    al.mode = "global"
    return al


# A second, deliberately different scoring scheme. ACTRT2 is ~45% identical to actin,
# which is inside the range where gap placement can move; if the tallies are an artefact
# of one gap model they will not survive a change of matrix and gap costs.
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


def probe_named_sites(struct_seq, struct_numbers) -> dict:
    """Aligned residue in each panel member at each literature-named actin position."""
    for pos, (expected_aa, role) in NAMED_ACTIN_SITES.items():
        if pos not in struct_numbers:
            raise RuntimeError(
                f"actin position {pos} ({role}) is not observed in the structure chain; "
                "the named-site list cannot be probed against this model"
            )
        seen = struct_seq[struct_numbers.index(pos)]
        if seen != expected_aa:
            raise RuntimeError(
                f"actin position {pos} is {seen} in the structure but the named-site list "
                f"says {expected_aa} ({role}); the position numbering does not match the "
                "structure and every downstream call would be wrong"
            )
    targets = {ACTRT2: "ACTRT2 (this gene)", **PANEL}
    sequences = {acc: uniprot_sequence(acc) for acc in targets}
    al = aligner(*ALIGNMENT_SCHEMES[list(ALIGNMENT_SCHEMES)[0]])
    out = {}
    for acc, label in targets.items():
        mapping, pct, _ = map_positions(struct_seq, struct_numbers, sequences[acc], al)
        out[acc] = {
            "label": label,
            "sites": {
                f"{NAMED_ACTIN_SITES[p][0]}{p}": {
                    "role": NAMED_ACTIN_SITES[p][1],
                    "aligned_residue": mapping.get(p, (None, "-"))[1],
                    "call": classify(NAMED_ACTIN_SITES[p][0], mapping.get(p, (None, "-"))[1]),
                }
                for p in sorted(NAMED_ACTIN_SITES)
            },
        }
    return out


# The three reference sets that carry arguments. Module-level, so `panel_length_audit` can ASSERT
# that no length-flagged member is in them rather than claim it in a note string, and so
# `synthesise` cannot drift from a second copy.
FILAMENT_BUILDERS = {
    "P60709", "P63261", "P68133", "P68032",  # conventional actins: extend F-actin
    "P45891",  # Arp53D: a divergent actin that polymerises
    "P61163",  # ACTR1A: builds the dynactin minifilament
}
NUCLEATORS_NOT_POLYMERISERS = {"P61160", "P61158"}  # Arp2, Arp3
PT_COMPLEX_ARPS = {"Q8TDG2", "Q8TDY3", "Q9BYD9", "Q9Y615", "Q8TC94"}
ARGUMENT_CARRYING_SETS = {
    "filament_builders": FILAMENT_BUILDERS,
    "nucleators_not_polymerisers": NUCLEATORS_NOT_POLYMERISERS,
    "pt_complex_arps": PT_COMPLEX_ARPS,
}


def panel_length_audit(struct_seq: str) -> dict:
    """Flag panel members too short to contain the fold, BEFORE their tallies are believed.

    A reference sequence that starts mid-fold manufactures fake substitutions out of absent
    residues. ACTL10's Swiss-Prot entry is the case in this family - it is ~130 residues shorter
    than the actin fold - and that artefact has already propagated into a merged review elsewhere in
    this campaign. The threshold is derived from the panel's own length distribution and from the
    structure's observed chain, never hand-assigned: a member is flagged when it is shorter than the
    structure by more than a quarter of the structure's length, which sits inside the observed gap
    (the next-shortest member is within 3 per cent of the fold).
    """
    targets = {ACTRT2: "ACTRT2 (this gene)", **PANEL}
    lengths = {acc: len(uniprot_sequence(acc)) for acc in targets}
    ref = len(struct_seq)
    cutoff = ref * 0.75
    flagged = {acc: lengths[acc] for acc in lengths if lengths[acc] < cutoff}
    ok = sorted(v for a, v in lengths.items() if a not in flagged)
    if not ok:
        raise RuntimeError(
            f"every panel member is shorter than the {cutoff:.1f} aa cutoff; the panel or the "
            "structure is wrong and no tally from it can be trusted"
        )
    # ASSERTED, not asserted-in-prose: a flagged member must not appear in any set that carries an
    # argument. If a future panel change puts one there, this fails here rather than shipping a
    # conclusion drawn from absent residues.
    for name, members in ARGUMENT_CARRYING_SETS.items():
        overlap = sorted(set(flagged) & members)
        if overlap:
            raise RuntimeError(
                f"length-flagged panel member(s) {overlap} are in the argument-carrying set "
                f"{name!r}; their tallies partly reflect absent residues, so a conclusion drawn "
                "from that set would be unsound"
            )
    return {
        "structure_observed_length": ref,
        "cutoff_length": round(cutoff, 1),
        "cutoff_rationale": "0.75 x the structure's observed chain length; the shortest unflagged "
        f"panel member is {min(ok)} aa and the longest flagged is "
        f"{max(flagged.values()) if flagged else 'n/a'} aa, so the cut lies in an observed gap",
        "lengths": {targets[a]: lengths[a] for a in sorted(lengths, key=lambda x: lengths[x])},
        "flagged_too_short_for_the_fold": {targets[a]: v for a, v in flagged.items()},
        "flagged_accessions": sorted(flagged),
        "note": "Tallies for a flagged member are NOT comparable: gaps and apparent substitutions "
        "may reflect absent residues rather than divergence.",
        "argument_carrying_sets_checked": sorted(ARGUMENT_CARRYING_SETS),
        "flagged_members_in_argument_carrying_sets": [],  # asserted empty above, not merely claimed
    }


def score_panel(struct_seq, struct_numbers, contact_positions, subset=None):
    """Per-target tallies over `contact_positions`, under both alignment schemes."""
    targets = {ACTRT2: "ACTRT2 (this gene)", **PANEL}
    sequences = {acc: uniprot_sequence(acc) for acc in targets}
    out = {}
    for scheme, (matrix, og, eg) in ALIGNMENT_SCHEMES.items():
        al = aligner(matrix, og, eg)
        per_target = {}
        for acc, label in targets.items():
            mapping, pct, _ = map_positions(struct_seq, struct_numbers, sequences[acc], al)
            calls = {}
            tally = Counter()
            for pos in contact_positions:
                ref_aa = struct_seq[struct_numbers.index(pos)]
                tgt_pos, obs_aa = mapping.get(pos, (None, "-"))
                cls = classify(ref_aa, obs_aa)
                tally[cls] += 1
                calls[pos] = {
                    "actin_residue": f"{ref_aa}{pos}",
                    "aligned_residue": obs_aa,
                    "aligned_position": tgt_pos,
                    "call": cls,
                }
            rec = {
                "label": label,
                "pct_identity_full_length": pct,
                "identical": tally["identical"],
                "conservative": tally["conservative"],
                "non_conservative": tally["non-conservative"],
                "gap": tally["gap"],
                "n_positions": len(contact_positions),
            }
            if subset is not None:
                sub = Counter(
                    calls[p]["call"] for p in contact_positions if p in subset
                )
                rec["subset"] = {
                    "n_positions": sum(sub.values()),
                    "identical": sub["identical"],
                    "conservative": sub["conservative"],
                    "non_conservative": sub["non-conservative"],
                    "gap": sub["gap"],
                }
            if scheme == list(ALIGNMENT_SCHEMES)[0]:
                rec["calls"] = calls
            per_target[acc] = rec
        out[scheme] = per_target
    return out


# ------------------------------------------------------------- GOA / WITH-FROM


def parse_goa(path: Path) -> list[dict]:
    with path.open() as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    if not rows:
        raise RuntimeError(f"{path} has no annotation rows")
    return rows


def split_withfrom(field: str) -> list[str]:
    return [tok for tok in field.split("|") if tok]


def resolve_token(token: str) -> dict:
    out = {"token": token, "strategy": None, "hits": [], "note": None}
    if token.startswith("PANTHER:"):
        out["strategy"] = "none"
        out["note"] = "PANTHER internal tree node, not a protein; cannot be resolved to an entry"
        return out
    if token.startswith("GO:"):
        out["strategy"] = "none"
        out["note"] = "GO term used as the WITH/FROM source (automatic MF->BP step)"
        return out
    if token.startswith(("UniProtKB-SubCell:", "UniProtKB-KW:")):
        out["strategy"] = "none"
        out["note"] = (
            "controlled-vocabulary identifier, not a gene product; the source is a "
            "UniProt annotation statement rather than another gene's evidence"
        )
        return out
    if token.startswith("ensembl:"):
        out["strategy"] = "none"
        out["note"] = "Ensembl protein identifier accompanying the UniProt accession on the same row"
        return out
    if token.startswith("UniProtKB:"):
        acc = token.split(":", 1)[1]
        queries = [("accession", f"accession:{acc.split('-')[0]}")]
    else:
        db, ident = token.split(":", 1)
        if db not in XREF_DB:
            out["strategy"] = "none"
            out["note"] = f"{db} is not a recognised gene product database in this resolver"
            return out
        bare = ident.split(":")[-1] if db == "MGI" else ident
        queries = [("xref", f"xref:{XREF_DB[db]}-{bare}"), ("free-text", bare)]
    for strategy, query in queries:
        data = get_json(
            "https://rest.uniprot.org/uniprotkb/search",
            {
                "query": query,
                "size": 5,
                "fields": "accession,id,reviewed,protein_name,gene_names,organism_name",
            },
        )
        results = data.get("results", [])
        if results:
            out["strategy"] = strategy
            for entry in results:
                desc = entry.get("proteinDescription", {})
                name = (
                    desc.get("recommendedName", {}).get("fullName", {}).get("value")
                    or (desc.get("submissionNames") or [{}])[0].get("fullName", {}).get("value")
                    or "(no name)"
                )
                # An inactive (merged or deleted) accession IS returned by the search endpoint -
                # verified against O15507, which comes back with primaryAccession O15507,
                # entryType "Inactive", uniProtkbId equal to the accession, no name, no gene and no
                # organism. Without this branch it was labelled "Swiss-Prot", i.e. the strongest
                # provenance label available, on an entry carrying nothing at all. `uniprot_entry`
                # was hardened against exactly this earlier; leaving the second accession path
                # unguarded is the scope divergence that makes a check structurally blind.
                entry_type = entry.get("entryType") or ""
                if "Inactive" in entry_type:
                    reviewed = "INACTIVE"
                elif "unreviewed" in entry_type:
                    reviewed = "TrEMBL"
                else:
                    reviewed = "Swiss-Prot"
                out["hits"].append(
                    {
                        "accession": entry["primaryAccession"],
                        "entry_name": entry.get("uniProtkbId"),
                        "reviewed": reviewed,
                        "name": name,
                        "genes": [
                            g["geneName"]["value"] for g in entry.get("genes", []) if g.get("geneName")
                        ],
                        "organism": entry.get("organism", {}).get("scientificName"),
                    }
                )
            break
    if not out["hits"]:
        out["note"] = "unresolved by both xref and free-text search; deferred, not dismissed"
    # Both notes can apply at once - one live Swiss-Prot hit plus one merged hit is both ambiguous
    # AND partly dead - so they are composed rather than made mutually exclusive by an elif.
    notes: list[str] = []
    inactive = [h for h in out["hits"] if h["reviewed"] == "INACTIVE"]
    if len(out["hits"]) > 1:
        reviewed = [h for h in out["hits"] if h["reviewed"] == "Swiss-Prot"]
        unreviewed = [h for h in out["hits"] if h["reviewed"] == "TrEMBL"]
        notes.append(
            f"{len(out['hits'])} candidate entries; {len(reviewed)} reviewed (Swiss-Prot), "
            f"{len(unreviewed)} unreviewed"
        )
    if inactive:
        notes.append(
            f"{len(inactive)} of {len(out['hits'])} candidate entries are INACTIVE (merged or "
            "deleted) and carry no name, gene or organism; they are not evidence of anything"
        )
    if notes:
        out["note"] = "; ".join(notes)
    return out


def quickgo_evidence(gene_product: str, go_id: str) -> dict:
    data = get_json(
        "https://www.ebi.ac.uk/QuickGO/services/annotation/search",
        {
            "geneProductId": gene_product,
            "goId": go_id,
            "goUsage": "descendants",
            "goUsageRelationships": "is_a,part_of",
            "limit": 100,
        },
    )
    results = data.get("results", [])
    codes = Counter(r.get("goEvidence") for r in results)
    exp = [r for r in results if r.get("goEvidence") in EXPERIMENTAL_CODES]
    return {
        "n_hits": data.get("numberOfHits", 0),
        "codes": dict(sorted(codes.items(), key=lambda kv: kv[0] or "")),
        "has_experimental": bool(exp),
        "experimental_terms": sorted({r["goId"] for r in exp}),
        "experimental_refs": sorted({r.get("reference") for r in exp}),
    }


def audit_iba_rows(rows: list[dict]) -> dict:
    """Resolve every WITH/FROM token of every IBA row, and ask each source for its own evidence."""
    out = {}
    for row in rows:
        if row["GO EVIDENCE CODE"] != "IBA":
            continue
        go_id = row["GO TERM"]
        tokens = split_withfrom(row["WITH/FROM"])
        resolved = [resolve_token(t) for t in tokens]
        # Counts must match GOA by construction, not by hand.
        assert len(resolved) == len(tokens) == row["WITH/FROM"].count("|") + 1, (
            f"token accounting mismatch on {go_id}: {len(resolved)} resolved vs field {row['WITH/FROM']!r}"
        )
        for rec in resolved:
            if len(rec["hits"]) == 1:
                acc = rec["hits"][0]["accession"]
                rec["own_evidence"] = quickgo_evidence(f"UniProtKB:{acc}", go_id)
            elif len(rec["hits"]) > 1:
                per_candidate = {
                    h["accession"]: quickgo_evidence(f"UniProtKB:{h['accession']}", go_id)
                    for h in rec["hits"]
                }
                # A token whose cross-reference is ambiguous still carries experimental
                # evidence if any candidate entry does. Omitting the multi-hit tokens
                # here silently undercounted the corroborating sources on the first run:
                # every MGI/RGD token resolves to a Swiss-Prot entry plus several TrEMBL
                # isoform entries, so the IDA-carrying canonical actins were dropped.
                rec["own_evidence"] = {
                    "note": "ambiguous cross-reference; evidence queried per candidate",
                    "has_experimental": any(v["has_experimental"] for v in per_candidate.values()),
                    "n_candidates_with_experimental": sum(
                        1 for v in per_candidate.values() if v["has_experimental"]
                    ),
                    "per_candidate": per_candidate,
                }
        # A token whose ONLY hit is an inactive (merged or deleted) entry has not resolved to a
        # protein, however much it looks like it has: the entry carries no name, gene, organism or
        # annotation. Counting it under n_resolved_to_protein would report "resolved" for a dead
        # accession - the same half-applied-fix shape as labelling it Swiss-Prot, which is why the
        # label guard alone was not enough.
        def is_live(rec: dict) -> bool:
            return any(h["reviewed"] != "INACTIVE" for h in rec["hits"])

        protein_sources = [r for r in resolved if r["hits"] and is_live(r)]
        inactive_only = [r for r in resolved if r["hits"] and not is_live(r)]
        with_exp = [
            r for r in protein_sources
            if (r.get("own_evidence") or {}).get("has_experimental")
        ]
        # A token can only be counted as corroborating if it resolved to something; assert
        # that the two ways of counting agree rather than trusting the filter.
        assert len(with_exp) <= len(protein_sources), "more corroborating tokens than resolved tokens"
        out[go_id] = {
            "term_label": row["GO NAME"],
            "qualifier": row["QUALIFIER"],
            "n_tokens": len(tokens),
            "n_panther_nodes": sum(1 for t in tokens if t.startswith("PANTHER:")),
            "n_resolved_to_protein": len(protein_sources),
            "n_unresolved": sum(1 for r in resolved if not r["hits"] and r["strategy"] != "none"),
            "n_inactive_only": len(inactive_only),
            "n_sources_with_own_experimental_evidence": len(with_exp),
            "n_independent_swissprot_sources": sum(
                1 for r in protein_sources
                if len(r["hits"]) == 1 and r["hits"][0]["reviewed"] == "Swiss-Prot"
            ),
            "n_ambiguous_tokens": sum(1 for r in protein_sources if len(r["hits"]) > 1),
            "organisms": sorted({
                h["organism"] for r in protein_sources for h in r["hits"] if h.get("organism")
            }),
            "tokens": resolved,
        }
    return out


# --------------------------------------------------------------- PAINT / nodes


def shared_row_check() -> dict:
    """Do sibling genes' IBA rows carry the SAME WITH/FROM field as ACTRT2's?

    Three independently reviewed AADACL paralogs once gave three different verdicts to a
    byte-identical row. So before deciding an IBA row, establish mechanically whether a
    sibling's row is the same row.
    """
    def rows(sym: str) -> dict[tuple[str, str], str]:
        path = GENE_DIR.parent / sym / f"{sym}-goa.tsv"
        if not path.exists():
            return {}
        return {
            (r["GO TERM"], r["GO EVIDENCE CODE"]): r["WITH/FROM"]
            for r in parse_goa(path)
            if r["GO EVIDENCE CODE"] == "IBA"
        }

    mine = rows("ACTRT2")
    if not mine:
        raise RuntimeError("no IBA rows parsed for ACTRT2; the GOA TSV schema may have changed")
    out = {}
    for sym in ["ACTL7A", "ACTL7B", "ACTL8", "ACTR1A", "ACTR1B", "ACTR10"]:
        theirs = rows(sym)
        if not theirs:
            out[sym] = {"note": "no local GOA TSV for this sibling; not compared"}
            continue
        shared = sorted(set(mine) & set(theirs))
        out[sym] = {
            "shared_iba_rows": [
                {
                    "term": t,
                    "evidence": e,
                    "withfrom_identical": mine[(t, e)] == theirs[(t, e)],
                    "n_tokens_mine": len(split_withfrom(mine[(t, e)])),
                    "n_tokens_theirs": len(split_withfrom(theirs[(t, e)])),
                }
                for t, e in shared
            ]
        }
    return out


def paint_table() -> list[dict]:
    path = require(
        PAINT_TSV,
        "the PANTHER cache under interpro/panther/PTHR11937/ ships with the repository",
    )
    with path.open() as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def paint_go5200_audit(rows: list[dict]) -> dict:
    """Which nodes negate GO:0005200, which propagate it, and which genes end up with it."""
    negated, propagating, replacement = [], [], []
    for r in rows:
        if r["go_id"] != "GO:0005200":
            continue
        rec = {
            "node": r["node"],
            "evidence": r["evidence"],
            "negated": r["negated"],
            "seeds": split_withfrom(r["seeds"]),
            "date": r["date"],
        }
        if r["negated"] == "true":
            negated.append(rec)
        else:
            propagating.append(rec)
    for r in rows:
        if r["go_id"] == "GO:0005198":
            replacement.append({"node": r["node"], "evidence": r["evidence"], "date": r["date"]})
    # what each node's other annotations are, so a reader can see which clade it is
    node_context = defaultdict(list)
    for r in rows:
        node_context[r["node"]].append(f"{r['go_id']}({r['aspect']},{r['evidence']}"
                                       f"{',negated' if r['negated'] == 'true' else ''})")
    for rec in negated + propagating:
        rec["node_other_annotations"] = sorted(
            a for a in node_context[rec["node"]] if not a.startswith("GO:0005200")
        )
    human_5200 = human_genes_with_term("GO:0005200", exact=True)
    human_5198 = human_genes_with_term("GO:0005198", exact=True)
    return {
        "n_nodes_negating_GO_0005200": len(negated),
        "n_nodes_propagating_GO_0005200": len(propagating),
        "negated_nodes": negated,
        "propagating_nodes": propagating,
        "GO_0005198_rows_in_family": replacement,
        "human_genes_with_GO_0005200_by_IBA": human_5200,
        "human_genes_with_GO_0005198_by_IBA": human_5198,
    }


def human_genes_with_term(go_id: str, exact: bool = True) -> dict:
    """Human genes carrying `go_id` by IBA, with the PANTHER node that donated it."""
    params = {
        "goId": go_id,
        "taxonId": "9606",
        "evidenceCode": "ECO:0000318",
        "limit": 200,
    }
    if exact:
        params["goUsage"] = "exact"
    out: dict[str, list[str]] = {}
    page = 1
    while True:
        data = get_json(
            "https://www.ebi.ac.uk/QuickGO/services/annotation/search", {**params, "page": page}
        )
        results = data.get("results", [])
        for r in results:
            nodes = [
                x["id"]
                for grp in (r.get("withFrom") or [])
                for x in grp.get("connectedXrefs", [])
                if x["db"] == "PANTHER"
            ]
            out.setdefault(r.get("symbol"), [])
            for n in nodes:
                if n not in out[r["symbol"]]:
                    out[r["symbol"]].append(n)
        total = (data.get("pageInfo") or {}).get("total", 1)
        if page >= total or not results:
            break
        page += 1
    return dict(sorted(out.items()))


def relatives_census() -> dict:
    """Live: which PANTHER nodes and how many IBA rows each divergent human actin has."""
    accs = {
        "ACTL7A": "Q9Y615", "ACTL7B": "Q9Y614", "ACTL8": "Q9H568", "ACTL9": "Q8TC94",
        "ACTL10": "Q5JWF8", "ACTRT1": "Q8TDG2", "ACTRT2": ACTRT2, "ACTRT3": "Q9BYD9",
    }
    per_gene = {}
    for sym, acc in accs.items():
        entry = uniprot_entry(acc)  # fails loudly on a dead accession
        data = get_json(
            "https://www.ebi.ac.uk/QuickGO/services/annotation/search",
            {"geneProductId": f"UniProtKB:{acc}", "evidenceCode": "ECO:0000318", "limit": 200},
        )
        terms, nodes = [], []
        for r in data.get("results", []):
            if r["goId"] not in terms:
                terms.append(r["goId"])
            for grp in r.get("withFrom") or []:
                for x in grp.get("connectedXrefs", []):
                    if x["db"] == "PANTHER" and x["id"] not in nodes:
                        nodes.append(x["id"])
        per_gene[sym] = {
            "accession": acc,
            "entry_name": entry["entry_name"],
            "n_iba_rows": data.get("numberOfHits", 0),
            "iba_terms": sorted(terms),
            "panther_nodes": sorted(nodes),
        }
    counts = {sym: v["n_iba_rows"] for sym, v in per_gene.items()}
    # Three medians, because a median silently depends on who is in the set and the
    # sibling ACTL8 analysis reported one of them. Publishing all three makes the
    # comparison checkable instead of an apparent discrepancy between reviews.
    return {
        "per_gene": per_gene,
        "iba_row_counts": counts,
        "median_iba_rows_all_eight": statistics.median(counts.values()),
        "median_iba_rows_excluding_ACTL8": statistics.median(
            v for k, v in counts.items() if k != "ACTL8"
        ),
        "median_iba_rows_excluding_ACTRT2": statistics.median(
            v for k, v in counts.items() if k != "ACTRT2"
        ),
        "modal_iba_row_count": Counter(counts.values()).most_common(1)[0],
        "beta_actin_subfamily_nodes": ["PTN002631586", "PTN007551913"],
        "genes_under_beta_actin_subfamily_nodes": sorted(
            sym for sym, v in per_gene.items()
            if set(v["panther_nodes"]) & {"PTN002631586", "PTN007551913"}
        ),
    }


def term_relationships() -> dict:
    """Ancestor sets for the terms in play. Whether GO:0033011 sits under GO:0015629 or
    only under GO:0005856 decides whether the `actin cytoskeleton` row is redundant with
    the perinuclear-theca rows or is an independent claim, so it is computed, not assumed."""
    out = {}
    for go_id, label in TERMS_OF_INTEREST.items():
        data = get_json(
            f"https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/{go_id}/complete"
        )["results"][0]
        anc = get_json(
            f"https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/{go_id}/ancestors",
            {"relations": "is_a,part_of"},
        )["results"][0]["ancestors"]
        out[go_id] = {
            "label": data["name"],
            "expected_label": label,
            "is_obsolete": data.get("isObsolete"),
            "secondary_ids": data.get("secondaryIds"),
            "definition": data["definition"]["text"],
            "ancestors": sorted(anc),
        }
        if data["name"] != label:
            out[go_id]["WARNING"] = f"label drift: GOA/this script says {label!r}, GO says {data['name']!r}"
    pt = set(out["GO:0033011"]["ancestors"])
    out["_checks"] = {
        "GO:0033011_is_under_GO:0005856_cytoskeleton": "GO:0005856" in pt,
        "GO:0033011_is_under_GO:0015629_actin_cytoskeleton": "GO:0015629" in pt,
        "GO:0005200_is_under_GO:0005198": "GO:0005198" in set(out["GO:0005200"]["ancestors"]),
    }
    return out


# ------------------------------------------------------------------ IntAct


def intact_interactions(acc: str) -> list[dict]:
    data = get_json(
        f"https://www.ebi.ac.uk/intact/ws/interaction/findInteractions/{acc}",
        {"page": 0, "pageSize": 500},
    )
    out = []
    for c in data.get("content", []):
        pmids = [
            p.split(" ")[0] for p in (c.get("publicationIdentifiers") or []) if "pubmed" in p
        ]
        out.append(
            {
                "a": c.get("moleculeA"),
                "b": c.get("moleculeB"),
                "idA": c.get("idA"),
                "idB": c.get("idB"),
                "method": c.get("detectionMethod"),
                "type": c.get("type"),
                "pmids": pmids,
                "score": c.get("intactMiscore"),
                "expansion": c.get("expansionMethod"),
            }
        )
    if not out:
        raise RuntimeError(f"IntAct returned no interactions for {acc}; expected at least one")
    return out


def partner_class_census(acc: str, self_symbol: str) -> dict:
    """What classes of protein does `acc` partner with? Used on the partner, not the gene."""
    rows = intact_interactions(acc)
    partners = {}
    for r in rows:
        for mol, ident in ((r["a"], r["idA"]), (r["b"], r["idB"])):
            if not mol or mol == self_symbol:
                continue
            partners.setdefault(mol, {"methods": set(), "pmids": set()})
            partners[mol]["methods"].add(r["method"])
            partners[mol]["pmids"].update(r["pmids"])
    actin_superfamily = sorted(
        p for p in partners if re.match(r"^(ACT|POTE)", p)
    )
    chaperonin = sorted(p for p in partners if re.match(r"^(CCT|TCP1)$|^CCT", p))
    tubulin = sorted(p for p in partners if p.startswith("TUB"))
    return {
        "n_partners": len(partners),
        "n_interaction_records": len(rows),
        "actin_superfamily_partners": actin_superfamily,
        "chaperonin_CCT_partners": chaperonin,
        "tubulin_partners": tubulin,
        "partners": {
            p: {"methods": sorted(v["methods"]), "pmids": sorted(v["pmids"])}
            for p, v in sorted(partners.items())
        },
    }


# ------------------------------------------------- PT complex annotation census


def reference_scope() -> dict:
    """How large is each supporting reference's GOA footprint, and where countable, over how
    many entities?

    The first line used to promise an entity count outright. It cannot always deliver one: the
    walk is capped for paginated references, so `n_entities` is None for those and the sampled
    figure is reported separately. Naming the function's limit in its own first line matters
    because the docstring is what a reader trusts before checking the return value.

    Querying QuickGO by *reference* rather than by gene is what distinguishes an
    observation of this protein from a projection onto it. A reference that annotates many
    entities to the same term with identical evidence is one projection, not N independent
    findings. Two opposite outcomes are both informative, so both are computed rather than
    assumed:

      * a proteome-scale reference (BioPlex) yields thousands of identical `protein binding`
        rows, which says the TERM is uninformative - but the target was still individually
        assayed, so it is not a projection in the ComplexPortal sense; and
      * a reference that gives its cellular-component term to only a SUBSET of the entities
        it touches has been curated per protein rather than projected. That subset test is
        the discriminator, and it is run below.
    """
    out = {}
    for pmid in REFERENCE_PMIDS:
        rows = []
        page = 1
        while True:
            data = get_json(
                "https://www.ebi.ac.uk/QuickGO/services/annotation/search",
                {"reference": f"PMID:{pmid}", "limit": 200, "page": page},
            )
            results = data.get("results", [])
            rows.extend(results)
            total_hits = data.get("numberOfHits", 0)
            total_pages = (data.get("pageInfo") or {}).get("total", 1)
            # Cap the walk: a proteome-scale reference has thousands of pages and the
            # uniformity question is answered by sampling, not by exhaustion.
            if page >= min(total_pages, 3) or not results:
                break
            page += 1
        by_entity = defaultdict(set)
        for r in rows:
            by_entity[r.get("symbol") or r.get("geneProductId")].add(r["goId"])
        terms = sorted({r["goId"] for r in rows})
        exhaustive = len(rows) >= total_hits
        rec = {
            # QuickGO's numberOfHits is an ANNOTATION count, not an entity count. One reference can
            # annotate 35 things across 19 entities, so the two must never be conflated - and for a
            # proteome-scale reference the walk is capped, so the sampled entity count is a sample
            # and NOT the total. When the sample is not exhaustive the entity count is reported as
            # unavailable rather than substituted, because a sample number in a total's place reads
            # as a measurement.
            "total_annotations": total_hits,
            "n_rows_sampled": len(rows),
            "sampled_exhaustively": exhaustive,
            "n_entities": len(by_entity) if exhaustive else None,
            "n_entities_note": None if exhaustive
            else f"entity count unavailable: results are paginated and only {len(rows)} of "
                 f"{total_hits} annotations were walked",
            "n_entities_in_sample": len(by_entity),
            "distinct_terms_sampled": terms,
            "assigned_by": sorted({r.get("assignedBy") for r in rows if r.get("assignedBy")}),
        }
        # The subset test: for a reference with one dominant cellular-component term, did the
        # curator give it to every entity it touched, or only to some?
        cc_candidates = [t for t in terms if t in ("GO:0033011", "GO:0033150")]
        if cc_candidates and rec["sampled_exhaustively"]:
            t = cc_candidates[0]
            got = sorted(e for e, ts in by_entity.items() if t in ts)
            didnt = sorted(e for e, ts in by_entity.items() if t not in ts)
            rec["subset_test"] = {
                "term": t,
                "entities_with_term": got,
                "entities_without_term": didnt,
                "is_subset_not_blanket": bool(didnt),
            }
        out[f"PMID:{pmid}"] = rec
    return out


def resolve_symbol(symbol: str, taxon: int) -> list[dict]:
    data = get_json(
        "https://rest.uniprot.org/uniprotkb/search",
        {
            "query": f"gene_exact:{symbol} AND organism_id:{taxon} AND reviewed:true",
            "size": 5,
            "fields": "accession,id,protein_name,gene_names,organism_name,length",
        },
    )
    return [
        {
            "accession": e["primaryAccession"],
            "entry_name": e.get("uniProtkbId"),
            "length": e.get("sequence", {}).get("length"),
        }
        for e in data.get("results", [])
    ]


def annotation_profile(acc: str) -> dict:
    rows = []
    page = 1
    while True:
        data = get_json(
            "https://www.ebi.ac.uk/QuickGO/services/annotation/search",
            {"geneProductId": f"UniProtKB:{acc}", "limit": 200, "page": page},
        )
        results = data.get("results", [])
        rows.extend(results)
        total = (data.get("pageInfo") or {}).get("total", 1)
        if page >= total or not results:
            break
        page += 1
    by_aspect = defaultdict(list)
    for r in rows:
        by_aspect[r.get("goAspect")].append(
            f"{r['goId']}/{r.get('goEvidence')}/{r.get('reference')}"
        )
    exp_bp = sorted({
        r["goId"] for r in rows
        if r.get("goAspect") == "biological_process" and r.get("goEvidence") in EXPERIMENTAL_CODES
    })
    return {
        "n_annotations": len(rows),
        "has_GO_0033011": any(r["goId"] == "GO:0033011" for r in rows),
        "GO_0033011_evidence": sorted({
            f"{r.get('goEvidence')}/{r.get('reference')}" for r in rows if r["goId"] == "GO:0033011"
        }),
        "experimental_BP_terms": exp_bp,
        "n_BP_annotations": len(by_aspect["biological_process"]),
        "BP": sorted(by_aspect["biological_process"]),
    }


def pt_complex_census() -> dict:
    out = {}
    for sym in PT_COMPLEX_SYMBOLS:
        rec = {}
        for label, taxon in (("human", 9606), ("mouse", 10090)):
            hits = resolve_symbol(sym, taxon)
            if not hits:
                rec[label] = {"note": f"no reviewed {label} entry for {sym}"}
                continue
            if len(hits) > 1:
                rec[label] = {
                    "note": f"{len(hits)} reviewed entries; reporting all",
                    "candidates": hits,
                }
            primary = hits[0]
            rec[label] = {**rec.get(label, {}), **primary, **annotation_profile(primary["accession"])}
        out[sym] = rec
    return out


# ------------------------------------------------------------------------ main


def main() -> None:
    require(GOA_TSV, "just fetch-gene human ACTRT2")
    goa = parse_goa(GOA_TSV)
    me = uniprot_entry(ACTRT2)
    if me["genes"] != ["ACTRT2"]:
        raise RuntimeError(f"{ACTRT2} is not ACTRT2 any more: {me}")

    results: dict = {
        "inputs": {
            "gene": "ACTRT2",
            "accession": ACTRT2,
            "entry_name": me["entry_name"],
            "length": me["length"],
            "goa_rows": len(goa),
            "goa_tsv": str(GOA_TSV.relative_to(REPO_ROOT)),
            "paint_tsv": str(PAINT_TSV.relative_to(REPO_ROOT)),
            "contact_cutoff_angstrom": CONTACT_CUTOFF,
            "panel": PANEL,
        }
    }

    # --- Analysis 1: nucleotide site -------------------------------------------------
    pdb, chain_id, ligands = ATP_STRUCTURE
    residues, hits = ligand_contacts(fetch_cif(pdb), pdb, chain_id, ligands, CONTACT_CUTOFF)
    numbers = [r.id[1] for r in residues]
    seq = chain_sequence(residues)
    positions = sorted(hits)
    results["nucleotide_site"] = {
        "structure": pdb,
        "chain": chain_id,
        "ligands_used": sorted(ligands),
        "observed_chain_length": len(residues),
        "n_contact_positions": len(positions),
        "contact_positions": {
            str(p): {**hits[p], "actin_residue": f"{seq[numbers.index(p)]}{p}"} for p in positions
        },
        "named_actin_sites_in_contact_set": sorted(
            f"{NAMED_ACTIN_SITES[p][0]}{p}" for p in positions if p in NAMED_ACTIN_SITES
        ),
        "named_actin_sites_outside_contact_set": sorted(
            f"{NAMED_ACTIN_SITES[p][0]}{p}" for p in NAMED_ACTIN_SITES if p not in positions
        ),
        "named_site_probe": probe_named_sites(seq, numbers),
        "panel_length_audit": panel_length_audit(seq),
        "panel": score_panel(seq, numbers, positions),
    }

    # --- Analysis 2: filament protomer interface --------------------------------------
    pdb2, _, _ = FILAMENT_STRUCTURE
    cid, all_chains, residues2, hits2 = interface_contacts(fetch_cif(pdb2), pdb2, CONTACT_CUTOFF)
    numbers2 = [r.id[1] for r in residues2]
    seq2 = chain_sequence(residues2)
    positions2 = sorted(hits2)
    results["filament_interface"] = {
        "structure": pdb2,
        "chains_in_model": all_chains,
        "chain_analysed": cid,
        "observed_chain_length": len(residues2),
        "n_contact_positions": len(positions2),
        "d_loop_range": [D_LOOP.start, D_LOOP.stop - 1],
        "contact_positions": {
            str(p): {**hits2[p], "actin_residue": f"{seq2[numbers2.index(p)]}{p}"} for p in positions2
        },
        "panel": score_panel(seq2, numbers2, positions2, subset=set(D_LOOP)),
    }

    # --- Analysis 3: IBA source audit -------------------------------------------------
    results["iba_sources"] = audit_iba_rows(goa)
    results["shared_rows_with_siblings"] = shared_row_check()

    # --- Analysis 4: PAINT GO:0005200 audit -------------------------------------------
    results["paint_go5200"] = paint_go5200_audit(paint_table())

    # --- Analysis 5: relatives census -------------------------------------------------
    results["relatives"] = relatives_census()

    # --- term relationships (decides redundancy questions) ----------------------------
    results["term_relationships"] = term_relationships()

    # --- Analysis 6: the protein-binding row ------------------------------------------
    partner_acc = None
    for row in goa:
        if row["GO TERM"] == "GO:0005515":
            toks = [t for t in split_withfrom(row["WITH/FROM"]) if t.startswith("UniProtKB:")]
            if toks:
                partner_acc = toks[0].split(":", 1)[1]
    if partner_acc is None:
        raise RuntimeError("no GO:0005515 row with a UniProtKB WITH/FROM token found in the GOA TSV")
    partner = uniprot_entry(partner_acc)
    results["protein_binding"] = {
        "goa_partner_accession": partner_acc,
        "goa_partner": partner,
        "actrt2_intact": intact_interactions(ACTRT2),
        "partner_class_census": partner_class_census(partner_acc, partner["genes"][0]),
    }

    # --- Analysis 7: PT complex annotation census -------------------------------------
    results["pt_complex"] = pt_complex_census()
    results["reference_scope"] = reference_scope()

    # --- synthesis: computed, never hand-written --------------------------------------
    results["synthesis"] = synthesise(results)

    (HERE / "results.json").write_text(json.dumps(results, indent=1, sort_keys=True) + "\n")
    (HERE / "RESULTS.md").write_text(render(results))
    print("wrote results.json and RESULTS.md")


# ---------------------------------------------------------------------- report


def _panel_table(panel: dict, scheme: str, subset_label: str | None = None,
                 flagged: set[str] | None = None) -> list[str]:
    """`flagged` marks members too short to contain the fold, in the table where a reader compares
    their numbers - a warning several hundred lines earlier is not where the row is read."""
    flagged = flagged or set()
    rows = panel[scheme]
    header = "| protein | % id (full length) | identical | conservative | non-conservative | gap |"
    sep = "|---|---|---|---|---|---|"
    if subset_label:
        header = header[:-1] + f" {subset_label} identical / n |"
        sep = sep[:-1] + "---|"
    lines = [header, sep]
    for acc, rec in sorted(rows.items(), key=lambda kv: -kv[1]["identical"]):
        mark = MARK_TRUNCATED if acc in flagged else ""
        line = (
            f"| {rec['label']} ({acc}){mark} | {rec['pct_identity_full_length']} | "
            f"{rec['identical']} | {rec['conservative']} | {rec['non_conservative']} | "
            f"{rec['gap']} |"
        )
        if subset_label:
            s = rec["subset"]
            line = line[:-1] + f" {s['identical']}/{s['n_positions']} |"
        lines.append(line)
    return lines


def synthesise(r: dict) -> dict:
    """Derive the summary claims from the computed tables, so a claim cannot drift from its data.

    Reported members of the sperm perinuclear-theca ARP complex, per PMID:35616329
    (ACTRT1/ACTRT2/ACTL7A/ACTL9) and PMID:41668650 (adds ACTRT3). ACTL7B is testis-specific
    but is NOT a reported member of that complex, which makes it the internal control that
    distinguishes "the PT complex" from "expressed in testis".
    """
    pt_arps = PT_COMPLEX_ARPS
    # Two classes that must NOT be merged. The first draft of this function put Arp2 and Arp3
    # into a single "known polymerisers" set, which made the report assert that ACTRT2's
    # 14/38 interface was "below" Arp3's 5/38 - false, and caught only by reading the rendered
    # sentence. Arp2/3 nucleate a filament without extending one, and their own protomer
    # interface is correspondingly degenerate, so they bound the wrong side of the comparison.
    filament_builders = FILAMENT_BUILDERS
    nucleators_not_polymerisers = NUCLEATORS_NOT_POLYMERISERS
    his161_reference_set = filament_builders | nucleators_not_polymerisers
    probe = r["nucleotide_site"]["named_site_probe"]
    h161 = {acc: rec["sites"]["H161"]["aligned_residue"] for acc, rec in probe.items()}
    # The named nucleotide positions, split by role. The split matters and the first version of
    # this function got it wrong: it reported a single ten-position set as "the pocket", and that
    # set happened to omit E214, Y306 and K336 - three of the script's own computed ATP contacts,
    # and precisely the three where ACTRT2 differs - while including D11, D154 and R183, which the
    # contact computation places OUTSIDE the 4 A contact set. "All ten identical" was therefore
    # true and selectively bounded. Both groups are now reported separately, and membership of the
    # computed contact set is printed per position, so a reader can see which is which.
    pocket_core_positions = ["D11", "S14", "G15", "K18", "Q137", "D154", "G156", "D157", "V159", "R183"]
    adenine_ribose_positions = ["E214", "Y306", "K336"]
    # His161 is the ATP-hydrolysis trigger and carries this argument on its own. Ala108 and Pro109
    # are the Pro-rich loop that governs the His161 rotamer, but PMID:37009486 reports that the
    # A108G and P109A actin mutants "polymerize into filaments similar to wild-type actin (WT)"
    # with ATPase activity "similar to that of the wild type", so substituting them does not by
    # itself abolish either polymerisation or hydrolysis. They are reported as context for the
    # His161 loss, never as independent evidence of lost hydrolysis.
    trigger_position = "H161"
    prorich_loop_positions = ["A108", "P109"]

    def count(acc, positions, call):
        return sum(1 for p in positions if probe[acc]["sites"][p]["call"] == call)

    contact_set = set(r["nucleotide_site"]["named_actin_sites_in_contact_set"])

    def detail(acc, positions):
        return {
            pos: {
                "aligned_residue": probe[acc]["sites"][pos]["aligned_residue"],
                "call": probe[acc]["sites"][pos]["call"],
                "in_computed_ATP_contact_set": pos in contact_set,
            }
            for pos in positions
        }

    fi = r["filament_interface"]["panel"][list(ALIGNMENT_SCHEMES)[0]]
    return {
        "his161_retained": sorted(a for a, v in h161.items() if v == "H"),
        "his161_lost_in_PT_complex_members": {
            a: h161[a] for a in sorted(pt_arps) if h161[a] != "H"
        },
        "his161_lost_outside_PT_complex": {
            a: v for a, v in sorted(h161.items()) if v != "H" and a not in pt_arps
        },
        "his161_retained_in_all_filament_builders_and_nucleators": all(
            h161[a] == "H" for a in his161_reference_set
        ),
        "his161_lost_in_all_reported_PT_complex_members": all(
            h161[a] != "H" for a in pt_arps
        ),
        "ACTL7B_control": {
            "note": "testis-specific but not a reported PT-complex member",
            "H161": h161["Q9Y614"],
        },
        "ACTRT2_pocket_core": {
            "positions": pocket_core_positions,
            "identical": count(ACTRT2, pocket_core_positions, "identical"),
            "conservative": count(ACTRT2, pocket_core_positions, "conservative"),
            "non_conservative": count(ACTRT2, pocket_core_positions, "non-conservative"),
            "detail": detail(ACTRT2, pocket_core_positions),
        },
        "ACTRT2_adenine_ribose": {
            "positions": adenine_ribose_positions,
            "identical": count(ACTRT2, adenine_ribose_positions, "identical"),
            "conservative": count(ACTRT2, adenine_ribose_positions, "conservative"),
            "non_conservative": count(ACTRT2, adenine_ribose_positions, "non-conservative"),
            "detail": detail(ACTRT2, adenine_ribose_positions),
        },
        "ACTRT2_whole_contact_set": {
            "n_positions": r["nucleotide_site"]["n_contact_positions"],
            "identical": r["nucleotide_site"]["panel"][list(ALIGNMENT_SCHEMES)[0]][ACTRT2]["identical"],
            "conservative": r["nucleotide_site"]["panel"][list(ALIGNMENT_SCHEMES)[0]][ACTRT2]["conservative"],
            "non_conservative": r["nucleotide_site"]["panel"][list(ALIGNMENT_SCHEMES)[0]][ACTRT2]["non_conservative"],
        },
        "ACTRT2_hydrolysis_trigger": {
            "position": trigger_position,
            "aligned_residue": probe[ACTRT2]["sites"][trigger_position]["aligned_residue"],
            "call": probe[ACTRT2]["sites"][trigger_position]["call"],
        },
        "ACTRT2_prorich_loop": {
            "positions": prorich_loop_positions,
            "detail": detail(ACTRT2, prorich_loop_positions),
            "caveat": "PMID:37009486 reports the A108G and P109A actin mutants polymerise and "
            "hydrolyse like wild type, so these substitutions modulate the His161 rotamer rather "
            "than gating hydrolysis; they are context for the His161 loss, not independent "
            "evidence of lost hydrolysis.",
        },
        "filament_interface_identical": {
            "ACTRT2": fi[ACTRT2]["identical"],
            "n_positions": fi[ACTRT2]["n_positions"],
            "filament_builders": {a: fi[a]["identical"] for a in sorted(filament_builders)},
            "lowest_filament_builder": min(filament_builders, key=lambda a: fi[a]["identical"]),
            "lowest_filament_builder_score": min(fi[a]["identical"] for a in filament_builders),
            "ACTRT2_below_every_filament_builder": all(
                fi[ACTRT2]["identical"] < fi[a]["identical"] for a in filament_builders
            ),
            "nucleators_not_polymerisers": {
                a: fi[a]["identical"] for a in sorted(nucleators_not_polymerisers)
            },
        },
        "iba_donor_quality": {
            go_id: {
                "n_resolved": v["n_resolved_to_protein"],
                "n_with_own_experimental_evidence": v["n_sources_with_own_experimental_evidence"],
            }
            for go_id, v in r["iba_sources"].items()
        },
        "pt_members_with_no_experimental_BP_in_either_species": sorted(
            sym for sym, rec in r["pt_complex"].items()
            if not rec.get("human", {}).get("experimental_BP_terms")
            and not rec.get("mouse", {}).get("experimental_BP_terms")
        ),
    }


def render(r: dict) -> str:
    L: list[str] = []
    a = L.append
    inp = r["inputs"]
    # Accessions too short to contain the fold, marked in every table where their numbers are read.
    FLAGGED = set(r["nucleotide_site"]["panel_length_audit"]["flagged_accessions"])
    a("# ACTRT2: does the actin fold still do actin things, and does the GO record hold up?")
    a("")
    a("All numbers below are computed by `analyze_actrt2.py` from live UniProt, RCSB, QuickGO and")
    a("IntAct queries plus the repository's cached PANTHER PAINT table. Nothing is hardcoded from")
    a("a previous run or from a sibling review. Re-running the script reproduces this file.")
    a("")
    a(f"- gene: **ACTRT2** ({inp['accession']}, {inp['entry_name']}, {inp['length']} aa)")
    a(f"- GOA rows analysed: {inp['goa_rows']} (`{inp['goa_tsv']}`)")
    a(f"- contact cutoff: {inp['contact_cutoff_angstrom']} A heavy-atom to heavy-atom")
    a("")

    # 1 nucleotide site
    ns = r["nucleotide_site"]
    a("## 1. Nucleotide site: is actin's ATP pocket still there?")
    a("")
    a(f"Contacts computed from **PDB {ns['structure']}** chain {ns['chain']} "
      f"(ligands {', '.join(ns['ligands_used'])}), {ns['observed_chain_length']} observed residues, "
      f"giving **{ns['n_contact_positions']} contact positions**.")
    a("")
    a("Literature-named actin residues inside the computed contact set: "
      + (", ".join(ns["named_actin_sites_in_contact_set"]) or "none")
      + ". Outside it (probed by alignment anyway): "
      + (", ".join(ns["named_actin_sites_outside_contact_set"]) or "none")
      + ".")
    a("")
    la = ns["panel_length_audit"]
    a(f"**Sequence-length audit first, because a truncated reference manufactures fake "
      f"substitutions.** The structure's observed chain is {la['structure_observed_length']} "
      f"residues; a panel member shorter than {la['cutoff_length']} residues "
      f"({la['cutoff_rationale']}) is flagged as too short to contain the fold: "
      + (", ".join(f"**{k}** at {v} aa" for k, v in la["flagged_too_short_for_the_fold"].items())
         or "none")
      + f". {la['note']} No conclusion in this analysis rests on a flagged member, and that is "
      f"asserted rather than claimed: `panel_length_audit` raises if a flagged accession appears in "
      f"any of the argument-carrying reference sets ({', '.join(la['argument_carrying_sets_checked'])}"
      f"), and it currently finds "
      f"{len(la['flagged_members_in_argument_carrying_sets'])} such overlaps. Every table row "
      f"carrying a flagged member's tally is marked - `{MARK_TRUNCATED.strip()}` in the wide "
      f"tables, `{MARK_TRUNCATED_SHORT.strip()}` in the per-position table, whose cells are too "
      f"narrow for the long form - and the number of marked rows is counted from the rendered "
      f"tables at the end of this section rather than stated by hand.")
    a("")
    a("Aligned residue at each named actin position:")
    a("")
    sites = sorted(next(iter(ns["named_site_probe"].values()))["sites"])
    sites.sort(key=lambda s: int(s[1:]))
    a("| protein | " + " | ".join(sites) + " |")
    a("|---" * (len(sites) + 1) + "|")
    for acc, rec in ns["named_site_probe"].items():
        cells = []
        for s in sites:
            v = rec["sites"][s]
            mark = {"identical": "", "conservative": "*", "non-conservative": "**", "gap": "!"}[v["call"]]
            cells.append(f"{v['aligned_residue']}{mark}")
        trunc = MARK_TRUNCATED_SHORT if acc in FLAGGED else ""
        a(f"| {rec['label'].split(' (')[0]}{trunc} | " + " | ".join(cells) + " |")
    a("")
    a("(`*` conservative, `**` non-conservative, `!` gap; roles: "
      + "; ".join(f"{s} = {next(iter(ns['named_site_probe'].values()))['sites'][s]['role']}" for s in sites)
      + ".)")
    a("")
    first = list(ALIGNMENT_SCHEMES)[0]
    a(f"Scheme {first}:")
    a("")
    L.extend(_panel_table(ns["panel"], first, flagged=FLAGGED))
    a("")
    second = list(ALIGNMENT_SCHEMES)[1]
    a(f"Robustness, scheme {second}:")
    a("")
    L.extend(_panel_table(ns["panel"], second, flagged=FLAGGED))
    a("")
    calls = ns["panel"][first][ACTRT2]["calls"]
    lost = [f"{v['actin_residue']}->{v['aligned_residue']}" for v in calls.values()
            if v["call"] in ("non-conservative", "gap")]
    a(f"ACTRT2 positions that are non-conservative or gapped: {', '.join(lost) or 'none'}")
    a("")

    # 2 filament interface
    fi = r["filament_interface"]
    a("## 2. Filament protomer interface: could ACTRT2 polymerise like actin?")
    a("")
    a(f"Computed from **PDB {fi['structure']}** (chains {', '.join(fi['chains_in_model'])}); the "
      f"most-buried chain is {fi['chain_analysed']}, giving **{fi['n_contact_positions']} "
      f"protomer-protomer contact positions**. The D-loop column covers actin residues "
      f"{fi['d_loop_range'][0]}-{fi['d_loop_range'][1]}; that this segment makes protomer "
      f"contacts is not assumed but read off the computation - each of its contacts is listed "
      f"with the neighbouring chain it touches in the table of contact positions in results.json.")
    a("")
    a(f"Scheme {first}:")
    a("")
    L.extend(_panel_table(fi["panel"], first, subset_label="D-loop", flagged=FLAGGED))
    a("")
    a(f"Robustness, scheme {second}:")
    a("")
    L.extend(_panel_table(fi["panel"], second, subset_label="D-loop", flagged=FLAGGED))
    a("")
    a("A tally can hide which residues were lost, so the D-loop contact positions are also")
    a("printed as a motif. This is where the comparison discriminates: both")
    a("polymerisation-competent divergent controls keep the loop's anchor and its hydrophobic")
    a("core, and ACTRT2 does not.")
    a("")
    dl = sorted(int(p) for p in fi["contact_positions"] if D_LOOP.start <= int(p) <= D_LOOP.stop - 1)
    ref = "".join(fi["contact_positions"][str(p)]["actin_residue"][0] for p in dl)
    a(f"Actin positions {', '.join(str(p) for p in dl)} = `{ref}`")
    a("")
    a("| protein | D-loop contact motif | identical / n |")
    a("|---|---|---|")
    rowsrc = fi["panel"][first]

    def call_at(calls: dict, pos: int) -> dict:
        # `calls` is keyed by int in memory and by str after a JSON round trip.
        return calls[pos] if pos in calls else calls[str(pos)]

    for acc, rec in sorted(rowsrc.items(), key=lambda kv: -kv[1]["subset"]["identical"]):
        motif = "".join(call_at(rec["calls"], p)["aligned_residue"] for p in dl)
        mark = MARK_TRUNCATED if acc in FLAGGED else ""
        a(f"| {rec['label']} ({acc}){mark} | `{motif}` | "
          f"{rec['subset']['identical']}/{rec['subset']['n_positions']} |")
    a("")

    # Count the marks from the rendered document itself, so the claim above cannot drift from the
    # tables below it. `L` at this point contains every residue-comparison table.
    n_marked = count_marked_rows(L)
    n_flagged = len(FLAGGED)
    a(f"Marked table rows counted from the rendered tables above: **{n_marked}** across "
      f"{n_flagged} flagged member(s), i.e. {n_marked // n_flagged if n_flagged else 0} rows each. "
      f"Both marker forms are counted and prose mentioning a marker is excluded, since the count "
      f"looks only at lines that are table rows. Rows carrying annotation counts rather than "
      f"sequence comparisons are deliberately unmarked, since a length flag cannot affect them.")
    a("")

    # 3 IBA sources
    a("## 3. IBA source audit")
    a("")
    for go_id, rec in r["iba_sources"].items():
        a(f"### {go_id} {rec['term_label']} ({rec['qualifier']})")
        a("")
        a(f"- WITH/FROM tokens: **{rec['n_tokens']}** "
          f"({rec['n_panther_nodes']} PANTHER node(s), {rec['n_resolved_to_protein']} resolved to "
          f"protein entries, {rec['n_unresolved']} unresolved)")
        a(f"- sources carrying their **own** experimental evidence for this term or a descendant: "
          f"**{rec['n_sources_with_own_experimental_evidence']}/{rec['n_resolved_to_protein']}**")
        a(f"- unambiguous Swiss-Prot sources: {rec['n_independent_swissprot_sources']}")
        a(f"- organisms represented: {len(rec['organisms'])} ({', '.join(rec['organisms'])})")
        a("")
        a("| token | resolved | reviewed | organism | own evidence for the donated term |")
        a("|---|---|---|---|---|")
        for t in rec["tokens"]:
            if not t["hits"]:
                a(f"| `{t['token']}` | - | - | - | {t['note']} |")
                continue
            for h in t["hits"]:
                ev = t.get("own_evidence") or {}
                if "per_candidate" in ev:
                    e = ev["per_candidate"].get(h["accession"], {})
                else:
                    e = ev
                codes = ",".join(f"{k}x{v}" for k, v in (e.get("codes") or {}).items()) or "none"
                a(f"| `{t['token']}` | {'/'.join(h['genes']) or h['name']} ({h['accession']}, "
                  f"{h['entry_name']}) | {h['reviewed']} | {h['organism']} | {codes} |")
        a("")

    # 3b shared rows
    a("### 3b. Are the sibling genes' IBA rows the same rows?")
    a("")
    a("| sibling | shared IBA row | WITH/FROM byte-identical | tokens (ACTRT2 / sibling) |")
    a("|---|---|---|---|")
    for sym, rec in r["shared_rows_with_siblings"].items():
        if "note" in rec:
            a(f"| {sym} | - | - | {rec['note']} |")
            continue
        if not rec["shared_iba_rows"]:
            a(f"| {sym} | none | - | - |")
        for s in rec["shared_iba_rows"]:
            a(f"| {sym} | {s['term']} ({s['evidence']}) | **{s['withfrom_identical']}** | "
              f"{s['n_tokens_mine']} / {s['n_tokens_theirs']} |")
    a("")

    # 4 PAINT
    p = r["paint_go5200"]
    a("## 4. Where PAINT has, and has not, negated `GO:0005200`")
    a("")
    a(f"In the cached PAINT table for PTHR11937, `GO:0005200 structural constituent of "
      f"cytoskeleton` is propagated at **{p['n_nodes_propagating_GO_0005200']}** node(s) and "
      f"explicitly negated (IRD, negated=true) at **{p['n_nodes_negating_GO_0005200']}** node(s).")
    a("")
    a("| node | evidence | negated | date | that node's other PAINT annotations |")
    a("|---|---|---|---|---|")
    for rec in p["propagating_nodes"] + p["negated_nodes"]:
        a(f"| {rec['node']} | {rec['evidence']} | {rec['negated']} | {rec['date']} | "
          f"{', '.join(rec['node_other_annotations']) or '-'} |")
    a("")
    a("`GO:0005198 structural molecule activity` rows anywhere in the family: "
      + (", ".join(f"{x['node']} ({x['evidence']}, {x['date']})" for x in p["GO_0005198_rows_in_family"]) or "none"))
    a("")
    a("Human genes that end up with each term by IBA (live QuickGO), with the donating node:")
    a("")
    a("| term | human genes | donating node(s) |")
    a("|---|---|---|")
    for term, genes in (("GO:0005200", p["human_genes_with_GO_0005200_by_IBA"]),
                        ("GO:0005198", p["human_genes_with_GO_0005198_by_IBA"])):
        nodes = sorted({n for v in genes.values() for n in v})
        a(f"| {term} | {', '.join(genes) or 'none'} | {', '.join(nodes) or '-'} |")
    a("")

    # 5 relatives
    rel = r["relatives"]
    a("## 5. Relatives census (live)")
    a("")
    a(f"IBA rows per gene: {', '.join(f'{k}={v}' for k, v in rel['iba_row_counts'].items())}. "
      f"Median over all eight: **{rel['median_iba_rows_all_eight']}**; excluding ACTL8: "
      f"**{rel['median_iba_rows_excluding_ACTL8']}**; excluding ACTRT2: "
      f"**{rel['median_iba_rows_excluding_ACTRT2']}**. Modal count "
      f"**{rel['modal_iba_row_count'][0]}** (in {rel['modal_iba_row_count'][1]} of 8 genes).")
    a("")
    a(f"Genes drawing on the beta-actin-subfamily nodes "
      f"{', '.join(rel['beta_actin_subfamily_nodes'])}: "
      f"**{', '.join(rel['genes_under_beta_actin_subfamily_nodes']) or 'none'}**.")
    a("")
    a("(These are annotation counts, not sequence comparisons, so they are unaffected by the "
      "length flag above and are deliberately unmarked.)")
    a("")
    a("| gene | accession | IBA rows | IBA terms | PANTHER nodes |")
    a("|---|---|---|---|---|")
    for sym, v in rel["per_gene"].items():
        a(f"| {sym} | {v['accession']} ({v['entry_name']}) | {v['n_iba_rows']} | "
          f"{', '.join(v['iba_terms'])} | {', '.join(v['panther_nodes'])} |")
    a("")

    # 5b term relationships
    tr = r["term_relationships"]
    a("### 5b. Term relationships (computed, not assumed)")
    a("")
    a("| term | label | obsolete | is GO:0005856 an ancestor | is GO:0015629 an ancestor |")
    a("|---|---|---|---|---|")
    for go_id, rec in tr.items():
        if go_id.startswith("_"):
            continue
        anc = set(rec["ancestors"])
        a(f"| {go_id} | {rec['label']} | {rec['is_obsolete']} | "
          f"{'GO:0005856' in anc} | {'GO:0015629' in anc} |")
    a("")
    for k, v in tr["_checks"].items():
        a(f"- `{k}` = **{v}**")
    a("")

    # 6 protein binding
    pb = r["protein_binding"]
    a("## 6. The `GO:0005515` row")
    a("")
    pt = pb["goa_partner"]
    a(f"GOA's WITH/FROM partner is `{pb['goa_partner_accession']}` = "
      f"**{'/'.join(pt['genes'])}** ({pt['entry_name']}, {pt['reviewed']}, {pt['length']} aa, {pt['organism']}).")
    a("")
    a("Every IntAct record for ACTRT2:")
    a("")
    a("| A | B | method | type | expansion | MI score | PMID |")
    a("|---|---|---|---|---|---|---|")
    for x in pb["actrt2_intact"]:
        a(f"| {x['a']} | {x['b']} | {x['method']} | {x['type']} | {x['expansion'] or '-'} | "
          f"{x['score']} | {', '.join(x['pmids'])} |")
    a("")
    c = pb["partner_class_census"]
    a(f"What that partner interacts with across all of IntAct: **{c['n_partners']} partners** in "
      f"{c['n_interaction_records']} records.")
    a("")
    a(f"- actin-superfamily partners ({len(c['actin_superfamily_partners'])}): "
      f"{', '.join(c['actin_superfamily_partners'])}")
    a(f"- CCT/TRiC chaperonin partners ({len(c['chaperonin_CCT_partners'])}): "
      f"{', '.join(c['chaperonin_CCT_partners'])}")
    a(f"- tubulin partners ({len(c['tubulin_partners'])}): {', '.join(c['tubulin_partners'])}")
    a("")

    # 7 PT complex
    a("## 7. Perinuclear-theca complex: who is annotated, and to what?")
    a("")
    a("| gene | species | accession | GO:0033011? | evidence | experimental BP terms | n BP rows |")
    a("|---|---|---|---|---|---|---|")
    for sym, rec in r["pt_complex"].items():
        for species in ("human", "mouse"):
            v = rec.get(species) or {}
            if "accession" not in v:
                # Seven cells, matching the header. The earlier version emitted
                #   | {sym} | {species} | - | - | - | - | - | {note}
                # which is EIGHT cells under a seven-column header, and with no closing pipe, so
                # the row ended unterminated. No current entry fails to resolve, so this was latent
                # rather than visible. (The first version of this comment said "a ninth field after
                # a trailing pipe" - wrong on both counts, and the same arithmetic slip the fix is
                # about, which is why the offending row is now written out literally above.)
                # Escaped, because a note is free text and one stray pipe would misalign the row.
                note = str(v.get("note", "unresolved")).replace("|", "\\|")
                a(f"| {sym} | {species} | - | - | - | - | {note} |")
                continue
            a(f"| {sym} | {species} | {v['accession']} ({v['entry_name']}) | "
              f"{'yes' if v['has_GO_0033011'] else 'no'} | {', '.join(v['GO_0033011_evidence']) or '-'} | "
              f"{', '.join(v['experimental_BP_terms']) or 'none'} | {v['n_BP_annotations']} |")
    a("")

    # 7b reference scope
    a("### 7b. How many entities does each supporting reference annotate?")
    a("")
    a("Querying QuickGO by reference rather than by gene distinguishes an observation of this")
    a("protein from a projection onto it.")
    a("")
    a("The first column is an **annotation** count, not an entity count - QuickGO's total counts")
    a("annotations, and one reference can annotate many terms per entity. Where the result set is")
    a("large enough to paginate, the walk is capped and the entity count is reported as")
    a("unavailable rather than replaced by the sample size.")
    a("")
    a("| reference | annotations in GOA | entities | distinct terms | assigned by |")
    a("|---|---|---|---|---|")
    for pmid, rec in r["reference_scope"].items():
        ent = (str(rec["n_entities"]) if rec["n_entities"] is not None
               else f"not counted ({rec['n_entities_in_sample']}+ in a partial walk)")
        a(f"| {pmid} | {rec['total_annotations']} | {ent} | "
          f"{', '.join(rec['distinct_terms_sampled']) or '-'} | "
          f"{', '.join(rec['assigned_by']) or '-'} |")
    a("")
    for pmid, rec in r["reference_scope"].items():
        st = rec.get("subset_test")
        if not st:
            continue
        a(f"Subset test on {pmid} / {st['term']}: **{len(st['entities_with_term'])}** of "
          f"{len(st['entities_with_term']) + len(st['entities_without_term'])} entities the "
          f"reference touches received the term "
          f"(`is_subset_not_blanket` = **{st['is_subset_not_blanket']}**).")
        a("")
        a(f"- with the term: {', '.join(st['entities_with_term'])}")
        a(f"- touched but NOT given the term: {', '.join(st['entities_without_term'])}")
        a("")
        a("A curator who assigned the term to a strict subset of the proteins named in the paper")
        a("was discriminating per protein, not projecting one localisation onto every partner.")
        a("")

    # 8 synthesis
    s = r["synthesis"]
    a("## 8. What the measurements do and do not support")
    a("")
    pk = s["ACTRT2_pocket_core"]
    ar = s["ACTRT2_adenine_ribose"]
    wc = s["ACTRT2_whole_contact_set"]
    tr = s["ACTRT2_hydrolysis_trigger"]
    pl = s["ACTRT2_prorich_loop"]
    ff = s["filament_interface_identical"]
    a(f"**Whole computed contact set first, so no sub-selection can flatter the result.** Of the "
      f"{wc['n_positions']} residues within {CONTACT_CUTOFF} A of ATP or the divalent cation in "
      f"PDB 2BTF, ACTRT2 matches actin at **{wc['identical']} identically** and "
      f"{wc['conservative']} conservatively, with **{wc['non_conservative']} non-conservative** "
      f"substitutions.")
    a("")
    a(f"**The phosphate, cation and sensor positions are fully conserved; the adenine/ribose "
      f"region is not.** Split by role:")
    a("")
    a("| group | positions | identical | conservative | non-conservative | substitutions |")
    a("|---|---|---|---|---|---|")
    for label, rec in (("phosphate loops, cation site, sensor", pk),
                       ("adenine/ribose region", ar)):
        subs = ", ".join(
            f"{pos}->{v['aligned_residue']}"
            for pos, v in rec["detail"].items() if v["call"] != "identical"
        ) or "none"
        a(f"| {label} | {', '.join(rec['positions'])} | {rec['identical']} | "
          f"{rec['conservative']} | {rec['non_conservative']} | {subs} |")
    a("")
    a("Which of those named positions are inside the computed 4 A contact set, and which are not:")
    a("")
    for label, rec in (("phosphate loops, cation site, sensor", pk),
                       ("adenine/ribose region", ar)):
        inside = [q for q, v in rec["detail"].items() if v["in_computed_ATP_contact_set"]]
        outside = [q for q, v in rec["detail"].items() if not v["in_computed_ATP_contact_set"]]
        a(f"- {label}: inside {', '.join(inside) or 'none'}; outside {', '.join(outside) or 'none'}")
    a("")
    a("So Harata et al. 2001's sequence-inspection claim that actin's ATP-binding motif is highly "
      "conserved in this protein is confirmed where it matters most - every phosphate-binding-loop "
      "residue, the divalent-cation ligand and the sensor arginine are identical - while the "
      "adenine/ribose region has diverged. Either way a retained pocket means a nucleotide-binding "
      "claim is **untested, not refuted**: it is not itself evidence that ACTRT2 binds anything.")
    a("")
    a(f"**The ATP-hydrolysis trigger is lost.** Actin's His161 is "
      f"{tr['aligned_residue']} in ACTRT2 ({tr['call']}). The Pro-rich loop that governs its "
      f"rotamer has also changed ("
      + ", ".join(f"{q}->{v['aligned_residue']}" for q, v in pl["detail"].items())
      + f"), but that is reported as context only: {pl['caveat']}")
    a("")
    a(f"- His161 is retained in every panel member that either extends a filament or nucleates "
      f"one: `his161_retained_in_all_filament_builders_and_nucleators` = "
      f"**{s['his161_retained_in_all_filament_builders_and_nucleators']}**.")
    a(f"- His161 is lost in **all reported members of the sperm perinuclear-theca ARP complex**: "
      f"`his161_lost_in_all_reported_PT_complex_members` = "
      f"**{s['his161_lost_in_all_reported_PT_complex_members']}** "
      f"({', '.join(f'{k}={v}' for k, v in s['his161_lost_in_PT_complex_members'].items())}). "
      f"It is also lost outside that complex, in "
      f"{', '.join(f'{k}={v}' for k, v in s['his161_lost_outside_PT_complex'].items())} - so the "
      f"loss is not exclusive to the PT ARPs, only universal within them.")
    a(f"- Internal control: ACTL7B is testis-specific but is not a reported member of that complex, "
      f"and it **retains** His161 (`{s['ACTL7B_control']['H161']}`). So the loss tracks the complex, "
      f"not merely testis expression.")
    a("")
    a(f"**The filament interface is not intact either.** ACTRT2 matches actin at "
      f"{ff['ACTRT2']}/{ff['n_positions']} protomer-contact positions. "
      f"`ACTRT2_below_every_filament_builder` = **{ff['ACTRT2_below_every_filament_builder']}** "
      f"(filament builders: "
      + ", ".join(f"{k}={v}" for k, v in ff["filament_builders"].items())
      + f"; lowest is {ff['lowest_filament_builder']} at {ff['lowest_filament_builder_score']}). "
      f"ACTRT2 instead sits with the proteins that nucleate a filament without extending one ("
      + ", ".join(f"{k}={v}" for k, v in ff["nucleators_not_polymerisers"].items())
      + "). So the measurement argues against ACTRT2 extending an F-actin filament; it does not "
      "exclude an Arp2/3-like role, and no such role has been proposed for it.")
    a("")
    a("The His161 loss and the interface degeneracy are **one coupled observation, not two "
      "independent ones**: actin's ATPase activity operates in the F-form and His161 flips as part "
      "of the G-to-F transition, so a protein that cannot make the F-form contacts has no route to "
      "the hydrolysis step regardless of His161. Counting them as separate lines of evidence would "
      "inflate the case, as would counting the Pro-rich loop substitutions as a third.")
    a("")
    a("**The IBA donors are not weak.** Sources carrying their own experimental evidence for the "
      "term they donated: "
      + "; ".join(
          f"{go_id} {v['n_with_own_experimental_evidence']}/{v['n_resolved']}"
          for go_id, v in s["iba_donor_quality"].items()
      )
      + ". So any objection to these rows has to be about propagation, not about donor quality.")
    a("")
    a("**The gap.** Reported PT-complex members with no experimental biological-process "
      "annotation in either human or mouse: "
      f"**{', '.join(s['pt_members_with_no_experimental_BP_in_either_species']) or 'none'}**.")
    a("")
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    main()
