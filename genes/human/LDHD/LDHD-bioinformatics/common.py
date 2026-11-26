"""Shared helpers: sequences, isoform coordinate maps, alignments, structure access."""
from __future__ import annotations

import json
import pathlib
import re
from functools import lru_cache

from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices
from Bio.PDB import MMCIFParser, ShrakeRupley
from Bio.Seq import Seq

HERE = pathlib.Path(__file__).parent
DATA = HERE / "data"
RESULTS = HERE / "results"
RESULTS.mkdir(exist_ok=True)

THREE = {"ALA": "A", "ARG": "R", "ASN": "N", "ASP": "D", "CYS": "C", "GLN": "Q", "GLU": "E", "GLY": "G", "HIS": "H", "ILE": "I", "LEU": "L", "LYS": "K", "MET": "M", "PHE": "F", "PRO": "P", "SER": "S", "THR": "T", "TRP": "W", "TYR": "Y", "VAL": "V"}
ONE2THREE = {v: k.capitalize() for k, v in THREE.items()}
# Tien et al. 2013 theoretical maximum ASA (A^2) for relative solvent accessibility
MAX_ASA = {"A": 129, "R": 274, "N": 195, "D": 193, "C": 167, "Q": 225, "E": 223, "G": 104, "H": 224, "I": 197, "L": 201, "K": 236, "M": 224, "F": 240, "P": 159, "S": 155, "T": 172, "W": 285, "Y": 263, "V": 174}


@lru_cache
def isoforms() -> dict[str, str]:
    """Return {'iso1': 507-aa displayed sequence (Q86WU2-1, NP_705690), 'iso2': 484 aa (Q86WU2-2, NP_919417, MANE Select)}."""
    out = {}
    for rec in SeqIO.parse(DATA / "human_isoforms.fasta", "fasta"):
        acc = rec.id.split("|")[1]
        out["iso2" if acc.endswith("-2") else "iso1"] = str(rec.seq)
    return out


@lru_cache
def uniprot_features(acc: str = "Q86WU2") -> list[dict]:
    return json.loads((DATA / f"{acc}.json").read_text())["features"]


@lru_cache
def iso1_to_iso2() -> dict[int, int | None]:
    """Map isoform-1 positions to isoform-2 positions from the UniProt VAR_SEQ feature (not hard-coded)."""
    seg = [f for f in uniprot_features() if f["type"] == "Alternative sequence"]
    assert len(seg) == 1, seg
    a, b = seg[0]["location"]["start"]["value"], seg[0]["location"]["end"]["value"]
    s1, s2 = isoforms()["iso1"], isoforms()["iso2"]
    assert s1[: a - 1] + s1[b:] == s2, "isoform 2 is not isoform 1 minus the VAR_SEQ segment"
    m = {}
    for i in range(1, len(s1) + 1):
        m[i] = i if i < a else (None if i <= b else i - (b - a + 1))
    return m


def iso2_to_iso1() -> dict[int, int]:
    return {v: k for k, v in iso1_to_iso2().items() if v is not None}


@lru_cache
def transcripts() -> dict[str, dict]:
    """CDS of both RefSeq transcripts parsed from the GenBank records."""
    out = {}
    for nm in ("NM_153486", "NM_194436"):
        rec = SeqIO.read(DATA / f"{nm}.gb", "genbank")
        cds = [f for f in rec.features if f.type == "CDS"][0]
        seq = str(cds.extract(rec.seq))
        start = int(cds.location.start)
        out[nm] = {"version": rec.id, "cds": seq, "mrna_from_atg": str(rec.seq[start:]), "protein": str(Seq(seq).translate()).rstrip("*"), "protein_id": cds.qualifiers["protein_id"][0]}
    return out


@lru_cache
def orthologs() -> dict[str, str]:
    return {rec.id.split("|")[0]: str(rec.seq) for rec in SeqIO.parse(DATA / "orthologs.fasta", "fasta")}


def _aligner() -> PairwiseAligner:
    al = PairwiseAligner()
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score, al.extend_gap_score = -10, -0.5
    al.mode = "global"
    al.end_gap_score = 0  # free end gaps (semi-global)
    return al


@lru_cache
def align_map(query: str, target: str) -> dict[int, int]:
    """1-based residue map query position -> target position from a BLOSUM62 semi-global alignment."""
    aln = _aligner().align(query, target)[0]
    m = {}
    for (qs, qe), (ts, te) in zip(*aln.aligned):
        for k in range(qe - qs):
            m[qs + k + 1] = ts + k + 1
    return m


@lru_cache
def structure(pdb_id: str):
    return MMCIFParser(QUIET=True).get_structure(pdb_id, DATA / f"{pdb_id}.cif")


def chain_sequence(chain) -> dict[int, str]:
    return {r.id[1]: THREE[r.get_resname()] for r in chain if r.id[0] == " " and r.get_resname() in THREE}


def relative_sasa(model) -> dict[tuple[str, int], float]:
    sr = ShrakeRupley()
    sr.compute(model, level="R")
    out = {}
    for ch in model:
        for r in ch:
            if r.id[0] == " " and r.get_resname() in THREE:
                out[(ch.id, r.id[1])] = r.sasa / MAX_ASA[THREE[r.get_resname()]]
    return out


def parse_hgvs_p(p: str):
    m = re.match(r"p\.\(?([A-Z][a-z]{2})(\d+)([A-Z][a-z]{2})\)?$", p or "")
    if not m:
        return None
    a = {v: k for k, v in ONE2THREE.items()}
    return a[m.group(1)], int(m.group(2)), a[m.group(3)]


def cds_pos_iso1_to_iso2(pos: int) -> int | None:
    """Convert a CDS position in NM_153486 (isoform 1) to NM_194436 (isoform 2, MANE Select)."""
    m = iso1_to_iso2()
    codon = (pos - 1) // 3 + 1
    return None if m[codon] is None else (m[codon] - 1) * 3 + (pos - 1) % 3 + 1


@lru_cache
def gnomad() -> dict:
    return json.loads((DATA / "gnomad_r4.json").read_text())["data"]["gene"]


@lru_cache
def clinvar() -> dict:
    return json.loads((DATA / "clinvar_esummary.json").read_text())


def gnomad_counts(v: dict) -> dict:
    ac = an = hom = 0
    for k in ("exome", "genome"):
        if v.get(k):
            ac += v[k]["ac"] or 0
            an = max(an, 0) + (v[k]["an"] or 0)
            hom += v[k]["homozygote_count"] or 0
    return {"ac": ac, "an": an, "hom": hom, "af": ac / an if an else None}
