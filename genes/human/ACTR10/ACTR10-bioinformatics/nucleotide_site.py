"""Is the actin nucleotide site still functional in ACTR10/Arp11, or only a fold?

ACTR10 is *actin-related*: it carries Pfam PF00022 (Actin) and sits in PANTHER
PTHR11937 (ACTIN) with conventional actins. Two opposite errors are possible when
curating such a protein, and both need the same test:

* asserting the actin activities (nucleotide binding, filament polymerisation) by
  fold inheritance, when the residues have decayed; or
* asserting "fold without function" without checking whether the residues are in
  fact intact.

Three checks are run against live public data, with an internal control in every
one:

**A. Which dynactin subunits have a nucleotide modelled?**  Every PDB entry that
contains Arp11 is surveyed. Within one entry the Arp1 and beta-actin chains are the
control: if experimentalists modelled a nucleotide into those but not into Arp11,
the site is empty; if Arp11 also has one, the site is occupied.

**B. Which Arp11 residues contact that nucleotide?**  The contacts are computed
from the deposited coordinates, not asserted.

**C. Are actin's own nucleotide-contact residues conserved in ACTR10?**  The contact
set is taken from the beta-actin chain of the same structure (so both sets come from
one experiment) and mapped onto human ACTR10 through a pairwise alignment. The same
alignment tests Eckley et al. 1999's specific structural claim that Arp11 carries a
large deletion of actin residues 38-57, the subdomain-2 loop on the pointed-end
face - the feature that is supposed to make Arp11 a cap rather than a polymer.

Nothing here is hard-coded: chain identities come from the PDB's own UniProt
mapping, contacts from the coordinates, and conservation from the alignment. An
ambiguous or nucleotide-free entry is reported rather than dropped; only a genuinely
missing input (an undownloadable structure or sequence) is fatal.
"""

from __future__ import annotations

import gzip
import io
import json
import sys
import time
import urllib.parse
import urllib.request
from dataclasses import dataclass, field

from Bio.Align import PairwiseAligner, substitution_matrices
from Bio.PDB import MMCIFParser, NeighborSearch

HUMAN_ACTR10 = "Q9NZ32"
PIG_ARP10 = "I3LHK5"
HUMAN_ACTB = "P60709"

# The structure used for the atomic-contact work: highest-resolution deposited
# model of dynactin's pointed end that contains modelled nucleotides.
CONTACT_PDB = "7Z8M"
CONTACT_CUTOFF = 4.0  # angstrom, heavy atoms

NUCLEOTIDES = {"ATP", "ADP", "AMP", "ANP", "AGS", "ADX", "GTP", "GDP"}

# Actin-family roles, keyed by the UniProt accession the PDB itself reports.
# Filled in from UniProt so the script does not hard-code who is who.
ARP11_ACCS = {HUMAN_ACTR10, PIG_ARP10}


def http_json(url: str, tries: int = 4) -> dict:
    last = None
    for attempt in range(tries):
        req = urllib.request.Request(url, headers={"Accept": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=60) as fh:
                return json.load(fh)
        except Exception as exc:  # noqa: BLE001 - retried, then re-raised
            last = exc
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"GET failed after {tries} tries: {url}") from last


def fetch_fasta(acc: str) -> str:
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    with urllib.request.urlopen(url, timeout=60) as fh:
        text = fh.read().decode()
    seq = "".join(line.strip() for line in text.splitlines() if not line.startswith(">"))
    if not seq:
        raise SystemExit(f"missing input: UniProt returned no sequence for {acc}")
    return seq


def rcsb_entries_for(acc: str) -> list[str]:
    query = {
        "query": {
            "type": "terminal",
            "service": "text",
            "parameters": {
                "attribute": (
                    "rcsb_polymer_entity_container_identifiers."
                    "reference_sequence_identifiers.database_accession"
                ),
                "operator": "exact_match",
                "value": acc,
            },
        },
        "return_type": "entry",
        "request_options": {"paginate": {"start": 0, "rows": 100}},
    }
    url = "https://search.rcsb.org/rcsbsearch/v2/query?json=" + urllib.parse.quote(
        json.dumps(query)
    )
    return [r["identifier"] for r in http_json(url).get("result_set", [])]


@dataclass
class Entry:
    pdb_id: str
    resolution: float | None
    title: str
    pubmed: str | None
    chain_acc: dict[str, str] = field(default_factory=dict)
    chain_desc: dict[str, str] = field(default_factory=dict)
    chain_ligands: dict[str, set[str]] = field(default_factory=dict)


def load_entry(pdb_id: str) -> Entry:
    d = http_json(f"https://data.rcsb.org/rest/v1/core/entry/{pdb_id}")
    res = (d.get("rcsb_entry_info", {}).get("resolution_combined") or [None])[0]
    cite = d.get("rcsb_primary_citation", {})
    e = Entry(
        pdb_id=pdb_id,
        resolution=res,
        title=d["struct"]["title"],
        pubmed=cite.get("pdbx_database_id_PubMed"),
    )
    ids = d["rcsb_entry_container_identifiers"]
    for eid in ids.get("polymer_entity_ids") or []:
        pe = http_json(f"https://data.rcsb.org/rest/v1/core/polymer_entity/{pdb_id}/{eid}")
        cid = pe["rcsb_polymer_entity_container_identifiers"]
        refs = cid.get("reference_sequence_identifiers") or []
        acc = refs[0]["database_accession"] if refs else ""
        desc = pe.get("rcsb_polymer_entity", {}).get("pdbx_description", "")
        for ch in cid.get("auth_asym_ids") or []:
            e.chain_acc[ch] = acc
            e.chain_desc[ch] = desc
    for nid in ids.get("non_polymer_entity_ids") or []:
        ne = http_json(f"https://data.rcsb.org/rest/v1/core/nonpolymer_entity/{pdb_id}/{nid}")
        comp = ne["pdbx_entity_nonpoly"]["comp_id"]
        for ch in ne["rcsb_nonpolymer_entity_container_identifiers"].get("auth_asym_ids") or []:
            e.chain_ligands.setdefault(ch, set()).add(comp)
    return e


def actin_fold_role(acc: str, desc: str) -> str | None:
    """Classify a chain as Arp11, Arp1 or actin. Returns None for other subunits."""
    if acc in ARP11_ACCS or "arp11" in desc.lower() or "actin-related protein 10" in desc.lower():
        return "Arp11 (ACTR10)"
    low = desc.lower()
    if "arp1" in low or "actin related protein 1" in low or "centractin" in low:
        return "Arp1 (ACTR1A)"
    if low.startswith("actin") or "actin, cytoplasmic" in low:
        return "beta-actin"
    return None


def download_cif(pdb_id: str) -> str:
    url = f"https://files.rcsb.org/download/{pdb_id}.cif.gz"
    with urllib.request.urlopen(url, timeout=180) as fh:
        raw = fh.read()
    if not raw:
        raise SystemExit(f"missing input: could not download {pdb_id}.cif.gz from RCSB")
    return gzip.decompress(raw).decode()


@dataclass
class Contacts:
    chain: str
    ligand: str
    residues: list[tuple[int, str]]


def nucleotide_contacts(structure, cutoff: float) -> list[Contacts]:
    """Residues of each chain within `cutoff` of a nucleotide in the same chain."""
    model = next(structure.get_models())
    atoms = [a for a in model.get_atoms() if a.element != "H"]
    ns = NeighborSearch(atoms)
    out: list[Contacts] = []
    for chain in model:
        for residue in chain:
            if residue.get_resname().strip() not in NUCLEOTIDES:
                continue
            hits: dict[tuple[int, str], None] = {}
            for atom in residue:
                for near in ns.search(atom.coord, cutoff, level="R"):
                    if near is residue:
                        continue
                    if near.get_resname().strip() in NUCLEOTIDES or near.id[0] != " ":
                        continue
                    if near.get_parent().id != chain.id:
                        continue
                    hits[(near.id[1], near.get_resname().strip())] = None
            out.append(
                Contacts(chain.id, residue.get_resname().strip(), sorted(hits))
            )
    return out


def align(a: str, b: str) -> tuple[str, str]:
    aligner = PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -11
    aligner.extend_gap_score = -1
    aligner.mode = "global"
    best = aligner.align(a, b)[0]
    return str(best[0]), str(best[1])


def position_map(a_aln: str, b_aln: str) -> dict[int, int | None]:
    """1-based position in sequence A -> 1-based position in B (None if gapped)."""
    out: dict[int, int | None] = {}
    ia = ib = 0
    for ca, cb in zip(a_aln, b_aln):
        if ca != "-":
            ia += 1
        if cb != "-":
            ib += 1
        if ca != "-":
            out[ia] = ib if cb != "-" else None
    return out


THREE_TO_ONE = {
    "ALA": "A", "ARG": "R", "ASN": "N", "ASP": "D", "CYS": "C", "GLN": "Q",
    "GLU": "E", "GLY": "G", "HIS": "H", "ILE": "I", "LEU": "L", "LYS": "K",
    "MET": "M", "PHE": "F", "PRO": "P", "SER": "S", "THR": "T", "TRP": "W",
    "TYR": "Y", "VAL": "V", "MSE": "M",
}


def main() -> str:
    lines: list[str] = []
    out = lines.append

    # ---- A. ligand survey -------------------------------------------------
    pdb_ids = sorted(set(rcsb_entries_for(HUMAN_ACTR10)) | set(rcsb_entries_for(PIG_ARP10)))
    if not pdb_ids:
        raise SystemExit(
            "missing input: RCSB returned no structures for ACTR10; check network access"
        )
    entries = [load_entry(p) for p in pdb_ids]

    out("## A. Is a nucleotide modelled in Arp11, and in its neighbours?")
    out("")
    out(
        f"All {len(pdb_ids)} PDB entries whose UniProt mapping contains human ACTR10 "
        f"({HUMAN_ACTR10}) or pig ACTR10 ({PIG_ARP10}). Within each entry the Arp1 and "
        "beta-actin chains are the internal control: they are the polymerising "
        "actin-fold subunits of the same filament, imaged in the same experiment."
    )
    out("")
    out("| PDB | res. (A) | PubMed | Arp11 chain: ligands | Arp1 chains: ligands | beta-actin chain: ligands |")
    out("|---|---|---|---|---|---|")
    informative = []
    for e in entries:
        by_role: dict[str, list[str]] = {}
        for ch, acc in e.chain_acc.items():
            role = actin_fold_role(acc, e.chain_desc.get(ch, ""))
            if role:
                ligs = sorted(e.chain_ligands.get(ch, set()))
                by_role.setdefault(role, []).append(f"{ch}: {','.join(ligs) if ligs else '-'}")
        cells = [
            "; ".join(by_role.get(r, ["(chain absent)"]))
            for r in ("Arp11 (ACTR10)", "Arp1 (ACTR1A)", "beta-actin")
        ]
        res = f"{e.resolution:.2f}" if e.resolution else "?"
        out(f"| {e.pdb_id} | {res} | {e.pubmed or '-'} | " + " | ".join(cells) + " |")
        arp11_ligs = {
            lig
            for ch, acc in e.chain_acc.items()
            if actin_fold_role(acc, e.chain_desc.get(ch, "")) == "Arp11 (ACTR10)"
            for lig in e.chain_ligands.get(ch, set())
        }
        if arp11_ligs & NUCLEOTIDES:
            informative.append((e.pdb_id, sorted(arp11_ligs & NUCLEOTIDES)))
    out("")
    out(
        f"Entries in which a nucleotide is modelled in the Arp11 chain: "
        + (", ".join(f"{p} ({'/'.join(l)})" for p, l in informative) if informative else "none")
    )
    out("")
    # Which nucleotide was modelled matters for term choice downstream, so the split is
    # tallied rather than left for a reader to count off the list above.
    tally: dict[str, int] = {}
    for _, ligs in informative:
        for lig in ligs:
            tally[lig] = tally.get(lig, 0) + 1
    out(
        "Split by ligand modelled in the Arp11 chain: "
        + ("; ".join(f"{k} in {v} entries" for k, v in sorted(tally.items())) if tally else "none")
        + f" (of {len(entries)} entries surveyed, "
        + f"{len(entries) - len(informative)} model no nucleotide in that chain)."
    )
    out("")

    # ---- B. atomic contacts ----------------------------------------------
    cif = download_cif(CONTACT_PDB)
    parser = MMCIFParser(QUIET=True)
    structure = parser.get_structure(CONTACT_PDB, io.StringIO(cif))
    contacts = nucleotide_contacts(structure, CONTACT_CUTOFF)
    ce = next(e for e in entries if e.pdb_id == CONTACT_PDB)

    out(f"## B. Nucleotide contacts computed from {CONTACT_PDB} coordinates")
    out("")
    out(
        f"Every residue with a heavy atom within {CONTACT_CUTOFF} A of a nucleotide in "
        "the same chain, computed from the deposited model."
    )
    out("")
    out("| chain | subunit | ligand | n contacts | contacting residues |")
    out("|---|---|---|---|---|")
    actin_contact_positions: list[int] = []
    arp11_contact_positions: list[int] = []
    for c in sorted(contacts, key=lambda x: x.chain):
        role = actin_fold_role(ce.chain_acc.get(c.chain, ""), ce.chain_desc.get(c.chain, ""))
        subunit = role or ce.chain_desc.get(c.chain, "?")
        listing = ", ".join(
            f"{THREE_TO_ONE.get(rn, rn)}{ri}" for ri, rn in c.residues
        )
        out(f"| {c.chain} | {subunit} | {c.ligand} | {len(c.residues)} | {listing} |")
        if role == "beta-actin":
            actin_contact_positions += [ri for ri, _ in c.residues]
        if role == "Arp11 (ACTR10)":
            arp11_contact_positions += [ri for ri, _ in c.residues]
    out("")

    # ---- C. conservation in human ACTR10 ---------------------------------
    seq_human = fetch_fasta(HUMAN_ACTR10)
    seq_pig = fetch_fasta(PIG_ARP10)
    seq_actb = fetch_fasta(HUMAN_ACTB)

    pig_aln, hum_aln = align(seq_pig, seq_human)
    pig_to_human = position_map(pig_aln, hum_aln)
    pid_pig = sum(1 for x, y in zip(pig_aln, hum_aln) if x == y and x != "-")

    out("## C. Are the contacts conserved in human ACTR10?")
    out("")
    out(
        f"Pig ARP10 ({PIG_ARP10}, {len(seq_pig)} aa) vs human ACTR10 ({HUMAN_ACTR10}, "
        f"{len(seq_human)} aa): {pid_pig} identical aligned positions "
        f"({100 * pid_pig / min(len(seq_pig), len(seq_human)):.1f}% of the shorter sequence). "
        "The structure is pig, so every contact is transferred through this alignment."
    )
    out("")
    out("| pig ARP10 contact | aligned human ACTR10 position | identical? |")
    out("|---|---|---|")
    same = 0
    for pos in sorted(set(arp11_contact_positions)):
        hp = pig_to_human.get(pos)
        pig_res = seq_pig[pos - 1] if pos <= len(seq_pig) else "?"
        hum_res = seq_human[hp - 1] if hp else "-"
        ok = hp is not None and pig_res == hum_res
        same += ok
        out(f"| {pig_res}{pos} | {hum_res}{hp if hp else ''} | {'yes' if ok else 'NO'} |")
    n_arp11 = len(set(arp11_contact_positions))
    out("")
    out(
        f"{same}/{n_arp11} of the pig Arp11 ATP-contacting residues are identical in "
        "human ACTR10."
        if n_arp11
        else "No Arp11 nucleotide contacts were found, so nothing to transfer."
    )
    out("")

    actb_aln, hum2_aln = align(seq_actb, seq_human)
    actb_to_human = position_map(actb_aln, hum2_aln)
    pid_actb = sum(1 for x, y in zip(actb_aln, hum2_aln) if x == y and x != "-")
    out(
        f"Human beta-actin ({HUMAN_ACTB}, {len(seq_actb)} aa) vs human ACTR10: "
        f"{pid_actb} identical aligned positions "
        f"({100 * pid_actb / len(seq_actb):.1f}% of actin). ACTR10 is the most divergent "
        "member of the family, so this alignment is included to locate actin's own "
        "nucleotide site, not to claim close homology."
    )
    out("")
    out("| beta-actin ADP contact | aligned human ACTR10 position | identical? |")
    out("|---|---|---|")
    a_same = a_gap = 0
    for pos in sorted(set(actin_contact_positions)):
        hp = actb_to_human.get(pos)
        a_res = seq_actb[pos - 1] if pos <= len(seq_actb) else "?"
        hum_res = seq_human[hp - 1] if hp else "-"
        if hp is None:
            a_gap += 1
        ok = hp is not None and a_res == hum_res
        a_same += ok
        out(f"| {a_res}{pos} | {hum_res}{hp if hp else '(gap)'} | {'yes' if ok else 'no'} |")
    n_actin = len(set(actin_contact_positions))
    out("")
    if n_actin:
        out(
            f"{a_same}/{n_actin} of beta-actin's own ADP-contacting residues are identical "
            f"in human ACTR10; {a_gap}/{n_actin} fall in an alignment gap."
        )
    out("")

    # Eckley 1999's specific claim: actin 38-57 deleted in Arp11.
    loop = range(38, 58)
    mapped = {p: actb_to_human.get(p) for p in loop}
    n_gapped = sum(1 for v in mapped.values() if v is None)
    out("### Test of the subdomain-2 loop deletion (Eckley et al. 1999)")
    out("")
    out(
        "Eckley et al. 1999 predicted that Arp11 lacks actin residues 38-57, the "
        "subdomain-2 surface loop on the pointed-end face, and that this is why Arp11 "
        "cannot be polymerised past. In the alignment above, "
        f"{n_gapped}/{len(list(loop))} of actin positions 38-57 align to a gap in human "
        "ACTR10."
    )
    out("")
    out("```")
    i = actb_aln.replace("-", "")
    # show the aligned block spanning actin 38-57
    col_start = col_end = None
    ia = 0
    for col, ca in enumerate(actb_aln):
        if ca != "-":
            ia += 1
            if ia == 30 and col_start is None:
                col_start = col
            if ia == 66:
                col_end = col
                break
    out(f"ACTB   {actb_aln[col_start:col_end + 1]}")
    out(f"ACTR10 {hum2_aln[col_start:col_end + 1]}")
    out("```")
    out("")
    return "\n".join(lines)


if __name__ == "__main__":
    sys.stdout.write(main())
