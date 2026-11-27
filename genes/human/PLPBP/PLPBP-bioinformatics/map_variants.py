"""Place literature, ClinVar and gnomAD variants on the protein.

Every variant's c. change is applied to the RefSeq CDS and translated; the
resulting protein consequence is compared with the reported p. change and with
the UniProt canonical sequence (numbering check). Missense variants are then
annotated with the per-residue features from structure_features.py and with
contacts computed in the AlphaFold model. Truncating variants are described by
what part of the fold and which ligand-contact residues they remove.

Thresholds (--site-cutoff, --buried-rsa) only assign descriptive labels;
interpretation belongs in RESULTS.md.
"""
import argparse
import csv
import json
import re
from pathlib import Path

import numpy as np
import yaml
from Bio import SeqIO
from Bio.PDB import NeighborSearch, PDBParser
from Bio.Seq import Seq
from Bio.SeqUtils import seq1, seq3

VOLUME = dict(G=60.1, A=88.6, S=89.0, C=108.5, D=111.1, P=112.7, N=114.1, T=116.1, E=138.4, V=140.0,
              Q=143.8, H=153.2, M=162.9, I=166.7, L=166.7, K=168.6, R=173.4, F=189.9, Y=193.6, W=227.8)
CHARGE = dict(D=-1, E=-1, K=1, R=1)
KD = dict(A=1.8, R=-4.5, N=-3.5, D=-3.5, C=2.5, Q=-3.5, E=-3.5, G=-0.4, H=-3.2, I=4.5, L=3.8, K=-3.9,
          M=1.9, F=2.8, P=-1.6, S=-0.8, T=-0.7, W=-0.9, Y=-1.3, V=4.2)


def apply_c(cds: str, c: str):
    """Return (kind, mutated_cds or None). Handles coding SNV, del, dup; flags intronic."""
    c = c.replace(" ", "")
    if re.search(r"\d[+-]\d", c):
        return "splice/intronic", None
    m = re.fullmatch(r"c\.(\d+)([ACGT])>([ACGT])", c)
    if m:
        i = int(m[1]) - 1
        if cds[i] != m[2]:
            return f"REF_MISMATCH(cds has {cds[i]})", None
        return "snv", cds[:i] + m[3] + cds[i + 1:]
    m = re.fullmatch(r"c\.(\d+)(?:_(\d+))?del[ACGT]*", c)
    if m:
        s, e = int(m[1]) - 1, int(m[2] or m[1])
        return "del", cds[:s] + cds[e:]
    m = re.fullmatch(r"c\.(\d+)(?:_(\d+))?dup[ACGT]*", c)
    if m:
        s, e = int(m[1]) - 1, int(m[2] or m[1])
        return "dup", cds[:e] + cds[s:e] + cds[e:]
    return "unparsed", None


def protein_consequence(ref: str, cds: str, mut: str) -> dict:
    new = str(Seq(mut[: len(mut) // 3 * 3]).translate())
    new_to_stop = new.split("*")[0]
    if new_to_stop == ref:
        return {"type": "synonymous", "hgvs_p": "p.="}
    i = next(k for k in range(min(len(ref), len(new_to_stop)) + 1)
             if k >= len(ref) or k >= len(new_to_stop) or ref[k] != new_to_stop[k])
    if len(mut) == len(cds):
        if len(new_to_stop) < len(ref):
            return {"type": "nonsense", "pos": i + 1, "hgvs_p": f"p.{seq3(ref[i])}{i + 1}Ter", "last_native_residue": i}
        return {"type": "missense", "pos": i + 1, "ref": ref[i], "alt": new_to_stop[i],
                "hgvs_p": f"p.{seq3(ref[i])}{i + 1}{seq3(new_to_stop[i])}"}
    if (len(mut) - len(cds)) % 3:
        n = len(new_to_stop) - i + 1
        alt = new_to_stop[i] if i < len(new_to_stop) else "Ter"
        return {"type": "frameshift", "pos": i + 1,
                "hgvs_p": f"p.{seq3(ref[i])}{i + 1}{seq3(alt) if alt != 'Ter' else 'Ter'}fs*{n}",
                "last_native_residue": i, "novel_tail_length": len(new_to_stop) - i}
    return {"type": "inframe_indel", "pos": i + 1, "hgvs_p": f"p.{seq3(ref[i])}{i + 1}(inframe)"}


def norm_p(p: str | None) -> str | None:
    if not p:
        return None
    return p.replace("(", "").replace(")", "").replace("*", "*").replace("X", "*").strip()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--query-fasta", required=True)
    ap.add_argument("--cds-fasta", required=True)
    ap.add_argument("--model", required=True)
    ap.add_argument("--features", required=True)
    ap.add_argument("--literature", required=True)
    ap.add_argument("--clinvar", required=True)
    ap.add_argument("--gnomad", required=True)
    ap.add_argument("--gene", required=True)
    ap.add_argument("--ligand-columns", nargs="+", required=True, help="feature columns holding ligand distances")
    ap.add_argument("--site-cutoff", type=float, default=4.5)
    ap.add_argument("--buried-rsa", type=float, default=0.20)
    ap.add_argument("--outdir", default="results")
    a = ap.parse_args()
    out = Path(a.outdir)
    out.mkdir(exist_ok=True)

    ref = str(next(SeqIO.parse(a.query_fasta, "fasta")).seq)
    cds = str(next(SeqIO.parse(a.cds_fasta, "fasta")).seq).upper()
    cds_prot = str(Seq(cds).translate()).rstrip("*")
    checks = {"cds_translation_equals_uniprot_canonical": cds_prot == ref, "protein_length": len(ref),
              "cds_length_nt": len(cds)}
    feats = {int(r["pos"]): r for r in csv.DictReader(open(a.features), delimiter="\t")}
    lig = lambda pos: min(float(feats[pos][c]) for c in a.ligand_columns)  # noqa: E731
    site_res = sorted(p for p in feats if lig(p) <= a.site_cutoff)
    checks["ligand_site_residues"] = [f"{ref[p - 1]}{p}" for p in site_res]

    model = PDBParser(QUIET=True).get_structure("af", a.model)[0]
    atoms = [at for at in model.get_atoms() if at.element != "H"]
    ns = NeighborSearch(atoms)
    residues = {r.id[1]: r for r in model.get_residues()}

    def contacts(pos: int) -> list[str]:
        r = residues[pos]
        side = [at for at in r if at.get_id() not in ("N", "C", "O", "CA")] or [r["CA"]]
        near = set()
        for at in side:
            for other in ns.search(at.coord, 4.0):
                rr = other.get_parent()
                if abs(rr.id[1] - pos) > 1:
                    near.add(rr.id[1])
        return [f"{ref[p - 1]}{p}" for p in sorted(near)]

    def polar_partners(pos: int) -> list[str]:
        r = residues[pos]
        res = set()
        for at in r:
            if at.element in ("N", "O") and at.get_id() not in ("N", "O"):
                for other in ns.search(at.coord, 3.5):
                    rr = other.get_parent()
                    if rr.id[1] != pos and other.element in ("N", "O"):
                        res.add(f"{ref[rr.id[1] - 1]}{rr.id[1]}:{other.get_id()}")
        return sorted(res)

    def describe_missense(pos: int, r: str, alt: str) -> dict:
        f = feats[pos]
        d = lig(pos)
        rsa = float(f["rsa"])
        label = ("ligand_site" if d <= a.site_cutoff else
                 "low_confidence_region" if float(f["plddt"]) < 70 else
                 "buried" if rsa < a.buried_rsa else "surface_or_partly_exposed")
        ss = sorted({f[c] for c in f if c.endswith("_ss")} - {"-"})
        return {"structural_label": label, "plddt": float(f["plddt"]), "rsa": rsa,
                "min_ligand_distance": round(d, 1), "template_ss": "/".join(ss) or "-",
                "family_identity": float(f["family_identity"]), "family_entropy": float(f["family_entropy"]),
                "delta_volume": round(VOLUME[alt] - VOLUME[r], 1),
                "delta_charge": CHARGE.get(alt, 0) - CHARGE.get(r, 0),
                "delta_hydropathy": round(KD[alt] - KD[r], 1),
                "to_or_from_proline_or_glycine": bool({r, alt} & {"P", "G"}),
                "sidechain_contacts_4A": contacts(pos), "sidechain_polar_partners_3.5A": polar_partners(pos)}

    def describe_trunc(last_native: int) -> dict:
        lost = [f"{ref[p - 1]}{p}" for p in site_res if p > last_native]
        return {"native_residues_retained": last_native, "fraction_retained": round(last_native / len(ref), 2),
                "ligand_site_residues_lost": lost,
                "schiff_lysine_retained": any(ref[p - 1] == "K" and p <= last_native and lig(p) <= 2.0 for p in site_res)}

    # ---- literature
    lit = yaml.safe_load(open(a.literature))
    lit_rows = []
    for v in lit["variants"]:
        kind, mut = apply_c(cds, v["c"])
        row = {"c": v["c"], "reported_p": v.get("p"), "sources": v["sources"],
               "zygosity_reported": v.get("zygosity_reported"), "c_parse": kind}
        if mut:
            cons = protein_consequence(ref, cds, mut)
            row["computed"] = cons
            rp, cp = norm_p(v.get("p")), cons["hgvs_p"]
            row["p_consistent_with_cds"] = (rp == cp) if rp else None
            if cons["type"] == "missense":
                row["structure"] = describe_missense(cons["pos"], cons["ref"], cons["alt"])
            elif cons["type"] in ("nonsense", "frameshift"):
                row["structure"] = describe_trunc(cons["last_native_residue"])
        lit_rows.append(row)

    # ---- ClinVar (this gene only, single-gene records)
    cv = json.load(open(a.clinvar))
    cv_rows = []
    for k, r in cv.items():
        if r["genes"] != [a.gene]:
            continue
        row = {"accession": r["accession"], "title": r["title"], "classification": r["classification"],
               "review_status": r["review_status"], "traits": r["traits"], "c": r["cdna_change"]}
        if r["cdna_change"]:
            kind, mut = apply_c(cds, r["cdna_change"])
            row["c_parse"] = kind
            if mut:
                cons = protein_consequence(ref, cds, mut)
                row["computed"] = cons
                if cons["type"] == "missense":
                    row["structure"] = describe_missense(cons["pos"], cons["ref"], cons["alt"])
                elif cons["type"] in ("nonsense", "frameshift"):
                    row["structure"] = describe_trunc(cons["last_native_residue"])
        cv_rows.append(row)

    # ---- gnomAD
    g = json.load(open(a.gnomad))["data"]["gene"]
    canon = g["canonical_transcript_id"]
    gn_rows = []
    for v in g["variants"]:
        if v["transcript_id"] != canon:
            continue
        ac = sum((v[k] or {}).get("ac", 0) for k in ("exome", "genome"))
        an = max((v[k] or {}).get("an", 0) for k in ("exome", "genome"))
        hom = sum((v[k] or {}).get("homozygote_count", 0) for k in ("exome", "genome"))
        row = {"variant_id": v["variant_id"], "hgvsc": v["hgvsc"], "hgvsp": v["hgvsp"],
               "consequence": v["consequence"], "lof": v["lof"], "ac": ac, "an_max": an, "hom": hom}
        m = re.fullmatch(r"p\.([A-Z][a-z]{2})(\d+)([A-Z][a-z]{2})", v["hgvsp"] or "")
        if m and v["consequence"] == "missense_variant":
            r1, pos, a1 = seq1(m[1]), int(m[2]), seq1(m[3])
            row["ref_matches_canonical"] = pos <= len(ref) and ref[pos - 1] == r1
            if row["ref_matches_canonical"]:
                row["structure"] = describe_missense(pos, r1, a1)
        gn_rows.append(row)

    # ---- summaries
    def tally(rows, key):
        t = {}
        for r in rows:
            s = r.get("structure", {}).get("structural_label")
            if s:
                t.setdefault(key(r), {}).setdefault(s, 0)
                t[key(r)][s] += 1
        return t

    gn_mis = [r for r in gn_rows if r.get("structure", {}).get("structural_label")]
    lit_mis = [r for r in lit_rows if r.get("computed", {}).get("type") == "missense"]
    plof = [r for r in gn_rows if r["lof"] == "HC"]
    summary = {
        "checks": checks,
        "literature": {"n": len(lit_rows),
                       "n_p_consistent": sum(1 for r in lit_rows if r.get("p_consistent_with_cds")),
                       "inconsistent": [(r["c"], r["reported_p"], r.get("computed", {}).get("hgvs_p"))
                                        for r in lit_rows if r.get("p_consistent_with_cds") is False],
                       "missense_labels": tally(lit_mis, lambda r: "patient_missense"),
                       "mean_family_identity_patient_missense": float(np.mean(
                           [r["structure"]["family_identity"] for r in lit_mis])),
                       "mean_rsa_patient_missense": float(np.mean([r["structure"]["rsa"] for r in lit_mis]))},
        "gnomad": {"canonical_transcript": canon, "constraint": g["gnomad_constraint"],
                   "n_missense": len(gn_mis),
                   "missense_labels": tally(gn_mis, lambda r: "all_missense"),
                   "homozygous_missense": [(r["hgvsp"], r["ac"], r["hom"], r["structure"]["structural_label"])
                                           for r in gn_mis if r["hom"] > 0],
                   "mean_family_identity_all_missense": float(np.mean(
                       [r["structure"]["family_identity"] for r in gn_mis])),
                   "mean_rsa_all_missense": float(np.mean([r["structure"]["rsa"] for r in gn_mis])),
                   "n_high_confidence_plof": len(plof), "plof_total_ac": sum(r["ac"] for r in plof),
                   "plof_homozygotes": sum(r["hom"] for r in plof),
                   "most_frequent_plof": sorted(((r["hgvsc"], r["hgvsp"], r["ac"], r["hom"]) for r in plof),
                                                key=lambda x: -x[2])[:8],
                   "ref_mismatch": [r["hgvsp"] for r in gn_rows if r.get("ref_matches_canonical") is False]},
        "clinvar": {"n_single_gene_records": len(cv_rows),
                    "missense_labels_by_classification": tally(
                        [r for r in cv_rows if r.get("computed", {}).get("type") == "missense"],
                        lambda r: r["classification"]),
                    "types_by_classification": {}},
    }
    for r in cv_rows:
        t = r.get("computed", {}).get("type") or r.get("c_parse") or "other"
        d = summary["clinvar"]["types_by_classification"].setdefault(r["classification"] or "none", {})
        d[t] = d.get(t, 0) + 1

    (out / "literature_variants_annotated.json").write_text(json.dumps(lit_rows, indent=1))
    (out / "clinvar_annotated.json").write_text(json.dumps(cv_rows, indent=1))
    (out / "gnomad_annotated.json").write_text(json.dumps(gn_rows, indent=1))
    (out / "variant_summary.json").write_text(json.dumps(summary, indent=1))

    with open(out / "literature_variants.tsv", "w") as fh:
        cols = ["c", "reported_p", "computed_p", "consistent", "type", "label", "plddt", "rsa", "dist_ligand",
                "ss", "fam_identity", "dVol", "dCharge", "contacts_4A", "polar_partners", "truncation", "sources"]
        fh.write("\t".join(cols) + "\n")
        for r in lit_rows:
            c, s = r.get("computed", {}), r.get("structure", {})
            trunc = (f"retains {s['native_residues_retained']} aa; loses {','.join(s['ligand_site_residues_lost'])}"
                     if "native_residues_retained" in s else "")
            fh.write("\t".join(str(x) for x in [
                r["c"], r["reported_p"], c.get("hgvs_p", ""), r.get("p_consistent_with_cds", ""),
                c.get("type", r["c_parse"]), s.get("structural_label", ""), s.get("plddt", ""), s.get("rsa", ""),
                s.get("min_ligand_distance", ""), s.get("template_ss", ""), s.get("family_identity", ""),
                s.get("delta_volume", ""), s.get("delta_charge", ""), ",".join(s.get("sidechain_contacts_4A", [])),
                ",".join(s.get("sidechain_polar_partners_3.5A", [])), trunc, ",".join(r["sources"])]) + "\n")
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()
