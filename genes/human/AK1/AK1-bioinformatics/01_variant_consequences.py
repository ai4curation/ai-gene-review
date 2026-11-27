"""Recompute the protein consequence of every reported AK1 cDNA change.

Checks (i) that the NM_000476 CDS translates to the UniProt P00568 canonical
sequence, so cDNA and protein numbering agree, (ii) that the reference base(s)
named in each variant are really at that position, and (iii) what the protein
consequence is, including the new reading frame and stop for frameshifts and a
nonsense-mediated-decay call from the exon structure (Ensembl).
"""
from __future__ import annotations

import json
import re

import yaml
from Bio.Seq import Seq

from ak1_common import HERE, THREE, dump, fetch, uniprot_sequence


def load_cds(transcript: str) -> str:
    url = ("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore"
           f"&id={transcript}&rettype=fasta_cds_na&retmode=text")
    text = fetch(url, f"{transcript}.cds.fasta").read_text()
    return "".join(l.strip() for l in text.splitlines() if not l.startswith(">")).upper()


def load_mrna_and_cds_start(transcript: str) -> tuple[str, int, int]:
    """Return mRNA sequence and 0-based CDS start/end from the GenBank record."""
    url = ("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore"
           f"&id={transcript}&rettype=gb&retmode=text")
    text = fetch(url, f"{transcript}.gb").read_text()
    m = re.search(r"^\s+CDS\s+(\d+)\.\.(\d+)", text, re.M)
    origin = text.split("ORIGIN", 1)[1]
    seq = re.sub(r"[^acgtn]", "", origin.lower()).upper()
    exons = [(int(a), int(b)) for a, b in re.findall(r"^\s+exon\s+(\d+)\.\.(\d+)", text, re.M)]
    return seq, int(m.group(1)) - 1, int(m.group(2)), exons


def apply(cds: str, hgvs: str) -> tuple[str, dict]:
    """Apply a simple HGVS c. change (substitution, del, dup) to the CDS."""
    info: dict = {}
    m = re.fullmatch(r"c\.(\d+)([ACGT])>([ACGT])", hgvs)
    if m:
        pos, ref, alt = int(m.group(1)), m.group(2), m.group(3)
        info["ref_base_observed"] = cds[pos - 1]
        info["ref_matches"] = cds[pos - 1] == ref
        return cds[:pos - 1] + alt + cds[pos:], info
    m = re.fullmatch(r"c\.(\d+)(?:_(\d+))?del", hgvs)
    if m:
        a = int(m.group(1)); b = int(m.group(2) or a)
        info["deleted"] = cds[a - 1:b]
        return cds[:a - 1] + cds[b:], info
    m = re.fullmatch(r"c\.(\d+)(?:_(\d+))?dup", hgvs)
    if m:
        a = int(m.group(1)); b = int(m.group(2) or a)
        info["duplicated"] = cds[a - 1:b]
        return cds[:b] + cds[a - 1:b] + cds[b:], info
    raise ValueError(f"unsupported HGVS: {hgvs}")


def describe(ref_prot: str, mut_cds_with_utr: str, mut_cds_len_change: int) -> dict:
    """Compare the reference protein with the translation of the mutant mRNA ORF."""
    mut_prot = str(Seq(mut_cds_with_utr[: len(mut_cds_with_utr) // 3 * 3]).translate())
    stop = mut_prot.find("*")
    mut_prot_to_stop = mut_prot if stop < 0 else mut_prot[:stop]
    first = next((i for i, (a, b) in enumerate(zip(ref_prot + "*", mut_prot)) if a != b), None)
    out: dict = {"mutant_protein_length": len(mut_prot_to_stop), "stop_found": stop >= 0}
    if first is None:
        out["consequence"] = "synonymous / no change"
        return out
    pos = first + 1
    ref_aa = (ref_prot + "*")[first]
    alt_aa = mut_prot[first]
    if mut_cds_len_change % 3 != 0:
        new_len = len(mut_prot_to_stop) - first  # residues from first changed one to stop
        out["class"] = "frameshift"
        out["hgvs_p"] = f"p.{THREE[ref_aa]}{pos}{THREE[alt_aa]}fsTer{new_len + 1}" if stop >= 0 else \
            f"p.{THREE[ref_aa]}{pos}{THREE[alt_aa]}fs (no stop in available mRNA)"
        out["first_changed_residue"] = pos
        out["stop_codon_number"] = len(mut_prot_to_stop) + 1 if stop >= 0 else None
        out["novel_tail"] = mut_prot_to_stop[first:]
    elif mut_cds_len_change != 0:
        out["class"] = "in-frame deletion" if mut_cds_len_change < 0 else "in-frame insertion"
        n = abs(mut_cds_len_change) // 3
        out["hgvs_p"] = f"p.{THREE[ref_aa]}{pos}del" if n == 1 else f"p.{pos}_{pos + n - 1}del"
        out["first_changed_residue"] = pos
        # an in-frame deletion inside a run of identical residues is position-ambiguous
        run_start = pos
        while run_start > 1 and ref_prot[run_start - 2] == ref_aa:
            run_start -= 1
        run_end = pos
        while run_end < len(ref_prot) and ref_prot[run_end] == ref_aa:
            run_end += 1
        out["equivalent_positions"] = list(range(run_start, run_end + 1))
    elif alt_aa == "*":
        out["class"] = "nonsense"
        out["hgvs_p"] = f"p.{THREE[ref_aa]}{pos}Ter"
        out["first_changed_residue"] = pos
        out["stop_codon_number"] = pos
    else:
        out["class"] = "missense"
        out["hgvs_p"] = f"p.{THREE[ref_aa]}{pos}{THREE[alt_aa]}"
        out["first_changed_residue"] = pos
        out["ref_aa"], out["alt_aa"] = ref_aa, alt_aa
    return out


def main() -> None:
    spec = yaml.safe_load((HERE / "reported_variants.yaml").read_text())
    tx = spec["transcript"]
    cds = load_cds(tx)
    mrna, cds_start, cds_end, exons = load_mrna_and_cds_start(tx)
    protein = uniprot_sequence()
    translated = str(Seq(cds).translate()).rstrip("*")
    checks = {
        "transcript": tx,
        "cds_length_nt": len(cds),
        "cds_translation_equals_uniprot_P00568": translated == protein,
        "uniprot_length": len(protein),
        "cds_matches_mrna_slice": mrna[cds_start:cds_end] == cds,
        "mrna_exons_1based": exons,
    }
    # last exon-exon junction in CDS coordinates (1-based position of the last base
    # of the penultimate exon), for the 50-55 nt nonsense-mediated-decay rule
    last_junction_cds = exons[-2][1] - cds_start if len(exons) >= 2 else None
    checks["last_exon_junction_cds_position"] = last_junction_cds
    utr3 = mrna[cds_end:]
    rows = []
    for v in spec["variants"]:
        mut_cds, info = apply(cds, v["cdna"])
        d = describe(protein, mut_cds + utr3, len(mut_cds) - len(cds))
        row = {**v, **info, **d}
        if d.get("class") in {"frameshift", "nonsense"} and d.get("stop_codon_number") and last_junction_cds:
            # position of the premature stop codon's first base in mutant CDS coordinates,
            # converted back to reference coordinates for comparison with the junction
            ptc_nt = (d["stop_codon_number"] - 1) * 3 + 1
            shift = len(mut_cds) - len(cds)
            ptc_ref = ptc_nt - shift if ptc_nt > int(re.search(r"\d+", v["cdna"]).group()) else ptc_nt
            dist = last_junction_cds - ptc_ref
            row["ptc_cds_position_ref_coords"] = ptc_ref
            row["nt_upstream_of_last_junction"] = dist
            row["nmd_predicted"] = dist > 55
            row["residues_of_native_sequence_retained"] = d["first_changed_residue"] - 1
        rows.append(row)
    out = {"checks": checks, "variants": rows}
    dump(out, "variant_consequences.json")
    print(json.dumps(checks, indent=1))
    for r in rows:
        print(f"{r['cdna']:14s} reported={r['reported_protein']!s:45.45s} computed={r.get('hgvs_p')}"
              f"  {('ref_ok=' + str(r['ref_matches'])) if 'ref_matches' in r else ''}"
              f"{(' NMD=' + str(r['nmd_predicted'])) if 'nmd_predicted' in r else ''}")


if __name__ == "__main__":
    main()
