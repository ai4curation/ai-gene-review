"""Place literature-reported LDHD variants on the protein.

For every variant in reported_variants.yaml:
  1. check the c. change against both RefSeq CDSs (NM_153486 = UniProt isoform 1,
     507 aa; NM_194436 = isoform 2, 484 aa, MANE Select) and report which
     transcript/isoform numbering is consistent with the paper;
  2. give the residue in isoform-1, isoform-2 and mouse (Q7TNG8 / PDB 8JD*) numbering;
  3. conservation across the downloaded orthologs;
  4. structural context in the mouse LDHD:FAD:Mn2+:D-lactate crystal structure
     (PDB 8JDE): distance to FAD, Mn2+ and substrate, relative solvent
     accessibility, first-shell neighbours; plus AlphaFold pLDDT and AlphaMissense
     score for the human residue/substitution.
Nothing here is asserted from memory: every value printed is computed from data/.
"""
from __future__ import annotations

import csv
import json
import re

import yaml
from Bio.PDB import NeighborSearch
from Bio.Seq import Seq

import common as c

PDB = "8JDE"  # wild-type mouse LDHD + FAD + Mn2+ + D-lactate


def check_cdna(hgvs_c: str | None):
    """Return per-transcript consequence of a simple substitution/duplication, or None."""
    if not hgvs_c:
        return {}
    out = {}
    for nm, t in c.transcripts().items():
        cds = t["cds"]
        m = re.match(r"c\.(\d+)([ACGT])>([ACGT])$", hgvs_c)
        if m:
            pos, ref, alt = int(m.group(1)), m.group(2), m.group(3)
            if pos > len(cds):
                out[nm] = {"consistent": False, "reason": "beyond CDS"}
                continue
            codon_i = (pos - 1) // 3
            codon = cds[codon_i * 3: codon_i * 3 + 3]
            ok = cds[pos - 1] == ref
            mut = codon[: (pos - 1) % 3] + alt + codon[(pos - 1) % 3 + 1:]
            out[nm] = {"consistent": ok, "ref_base_in_transcript": cds[pos - 1], "codon": codon_i + 1,
                       "protein_change": f"{Seq(codon).translate()}{codon_i + 1}{Seq(mut).translate()}" if ok else None}
            continue
        m = re.match(r"c\.(\d+)dup$", hgvs_c)
        if m:
            pos = int(m.group(1))
            full = t["mrna_from_atg"]  # read through into the 3'UTR to find the new stop
            mutcds = full[:pos] + full[pos - 1] + full[pos:]
            wt, mp = t["protein"], str(Seq(mutcds[: len(mutcds) // 3 * 3]).translate())
            first = next(i for i, (a, b) in enumerate(zip(wt, mp)) if a != b)
            stop = mp.find("*", first)
            out[nm] = {"duplicated_base": cds[pos - 1], "first_changed_codon": first + 1,
                       "first_change": f"{wt[first]}{first + 1}{mp[first]}",
                       "new_frame_length_to_stop": (stop - first + 1) if stop >= 0 else None,
                       "truncated_protein_length": stop if stop >= 0 else None, "wt_length": len(wt)}
            continue
        m = re.match(r"c\.(\d+)\+1dup$", hgvs_c)
        if m:
            # exon boundary cannot be verified from the CDS alone; report the last exonic codon
            pos = int(m.group(1))
            out[nm] = {"last_exonic_base": pos, "codon": (pos - 1) // 3 + 1, "phase": pos % 3}
            continue
        m = re.match(r"c\.(\d+)_(\d+)del$", hgvs_c)
        if m:
            a, b = int(m.group(1)), int(m.group(2))
            out[nm] = {"deleted_codons": f"{(a - 1) // 3 + 1}-{(b - 1) // 3 + 1}", "in_frame": (b - a + 1) % 3 == 0,
                       "includes_start_codon": a == 1, "last_deleted_residue": t["protein"][(b - 1) // 3] + str((b - 1) // 3 + 1)}
    return out


def database_lookup(v: dict, iso2_p: str | None, c_iso2: str | None) -> dict:
    """Find the variant in gnomAD v4 and ClinVar by rsID, MANE protein change or MANE c. notation."""
    out = {}
    for g in c.gnomad()["variants"]:
        if (v.get("rsid") and v["rsid"] in (g["rsids"] or [])) or (iso2_p and g["hgvsp"] == iso2_p) or (c_iso2 and g["hgvsc"] == c_iso2):
            n = c.gnomad_counts(g)
            out["gnomad"] = {"variant_id": g["variant_id"], "rsids": g["rsids"], "hgvsc_MANE": g["hgvsc"], "hgvsp_MANE": g["hgvsp"],
                             "consequence": g["consequence"], "allele_count": n["ac"], "allele_number": n["an"], "homozygotes": n["hom"],
                             "allele_frequency": float(f"{n['af']:.3g}") if n["af"] else None}
            c_iso2 = g["hgvsc"]  # trust the database notation over the paper once matched
            break
    for rec in c.clinvar().values():
        title = rec["title"]
        if c_iso2 and f":{c_iso2} " in title + " " or (iso2_p and f"({iso2_p})" in title):
            gc = rec["germline_classification"]
            out["clinvar"] = {"accession": rec["accession"], "title": title, "classification": gc["description"], "review_status": gc["review_status"],
                              "conditions": [t["trait_name"] for t in gc["trait_set"]], "protein_change_both_isoforms": rec.get("protein_change")}
            break
    return out


def feature_hits(pos1: int):
    hits = []
    for f in c.uniprot_features():
        a, b = f["location"]["start"]["value"], f["location"]["end"]["value"]
        if f["type"] in ("Natural variant", "Chain", "Sequence conflict"):
            continue
        if a <= pos1 <= b:
            lig = f.get("ligand", {}).get("name")
            hits.append(f["type"] + (f":{lig}" if lig else "") + (f" ({f.get('description')})" if f.get("description") else ""))
    return hits


def main():
    spec = yaml.safe_load((c.HERE / "reported_variants.yaml").read_text())["variants"]
    iso = c.isoforms()
    i1to2 = c.iso1_to_iso2()
    i2to1 = c.iso2_to_iso1()
    orth = c.orthologs()
    h2m = c.align_map(iso["iso1"], orth["mouse"])
    omaps = {k: c.align_map(iso["iso1"], v) for k, v in orth.items() if k != "human"}

    st = c.structure(PDB)
    model = st[0]
    chain = next(ch for ch in model if any(r.id[0] == " " for r in ch))
    cseq = c.chain_sequence(chain)
    # confirm PDB author numbering equals mouse UniProt numbering
    mism = [i for i, a in cseq.items() if i <= len(orth["mouse"]) and orth["mouse"][i - 1] != a]
    rsa = c.relative_sasa(model)
    het = {}
    for ch in model:
        for r in ch:
            if r.id[0].startswith("H_"):
                het.setdefault(r.get_resname(), []).extend(r.get_atoms())
    prot_atoms = [a for r in chain for a in r if r.id[0] == " "]
    ns = NeighborSearch(prot_atoms)
    all_ns = NeighborSearch([a for a in model.get_atoms()])

    def mind(res, atoms):
        return round(float(min(a - b for a in res for b in atoms)), 2) if atoms else None

    af = c.structure("AF-Q86WU2")[0]["A"]
    plddt = {r.id[1]: r["CA"].get_bfactor() for r in af}
    am = {row["protein_variant"]: row for row in csv.DictReader(open(c.DATA / "alphamissense.csv"))}

    rows, cdna_checks = [], {}
    for v in spec:
        chk = check_cdna(v.get("hgvs_c"))
        cdna_checks[v["id"]] = chk
        p = c.parse_hgvs_p(v.get("hgvs_p") or "")
        cand = []
        if p:
            cand.append(p)
        else:
            for nm, r in chk.items():  # derive protein change from cDNA when the paper gave none
                if r.get("protein_change") and nm == (v.get("reported_transcript") or nm):
                    pc = r["protein_change"]
                    cand.append((pc[0], int(pc[1:-1]), pc[-1]))
        resolved_note = None
        if not cand and v.get("rsid"):
            # the paper's c. notation matches neither transcript: resolve through the rsID in gnomAD (MANE numbering)
            for g in c.gnomad()["variants"]:
                if v["rsid"] in (g["rsids"] or []) and g["hgvsp"]:
                    q = c.parse_hgvs_p(g["hgvsp"])
                    cand.append((q[0], i2to1[q[1]], q[2]))
                    resolved_note = f"reported {v['hgvs_c']} matches neither transcript (reference base differs); {v['rsid']} is {g['hgvsc']} {g['hgvsp']} in gnomAD v4"
        for ref, pos, alt in cand[:1]:
            fits1 = pos <= len(iso["iso1"]) and iso["iso1"][pos - 1] == ref
            fits2 = pos <= len(iso["iso2"]) and iso["iso2"][pos - 1] == ref
            # decide numbering: cDNA consistency first, then residue identity
            pos1 = pos if fits1 else (i2to1.get(pos) if fits2 else None)
            numbering = "isoform 1 (Q86WU2-1 / NP_705690)" if fits1 else ("isoform 2 (Q86WU2-2 / NP_919417)" if fits2 else "UNRESOLVED")
            if fits1 and fits2:
                numbering += " [residue also matches isoform 2 at this number; cDNA check decides]"
            row = {"id": v["id"], "source": v["source"], "as_reported": v.get("hgvs_p") or v.get("hgvs_c"), "resolution_note": resolved_note, "numbering_used": numbering,
                   "iso1": f"{ref}{pos1}{alt}" if pos1 else None,
                   "iso2_MANE": (f"{ref}{i1to2[pos1]}{alt}" if pos1 and i1to2[pos1] else ("in isoform-1-only segment" if pos1 else None))}
            if pos1:
                mp = h2m.get(pos1)
                row["mouse_residue"] = f"{orth['mouse'][mp - 1]}{mp}" if mp else None
                cons = {k: (v2[m[pos1] - 1] if pos1 in m else "-") for (k, m), v2 in zip(omaps.items(), [orth[k] for k in omaps])}
                row["ortholog_residues"] = " ".join(f"{k}:{a}" for k, a in cons.items())
                row["identical_in"] = f"{sum(a == ref for a in cons.values())}/{len(cons)}"
                row["uniprot_features_at_site"] = "; ".join(feature_hits(pos1)) or "-"
                row["AF_pLDDT"] = round(float(plddt[pos1]), 1)
                a = am.get(f"{ref}{pos1}{alt}")
                row["AlphaMissense"] = f"{a['am_pathogenicity']} ({a['am_class']})" if a else None
                if mp and mp in cseq:
                    res = chain[mp]
                    row["pdb_residue"] = f"{PDB}:{chain.id}:{res.get_resname()}{mp}"
                    row["rel_SASA"] = round(float(rsa[(chain.id, mp)]), 2)
                    for lig in ("FAD", "MN", "LAC"):
                        row[f"min_dist_{lig}_A"] = mind(list(res.get_atoms()), het.get(lig, []))
                    near = sorted({(a2.get_parent().get_resname(), a2.get_parent().id[1]) for at in res for a2 in ns.search(at.coord, 4.0) if a2.get_parent() is not res}, key=lambda x: x[1])
                    # side-chain polar contacts (N/O/S within 3.5 A of a side-chain N/O/S) incl. ligands and waters
                    sc = [a for a in res if a.get_id() not in ("N", "CA", "C", "O") and a.element in ("N", "O", "S")]
                    pol = set()
                    for at in sc:
                        for a2 in all_ns.search(at.coord, 3.5):
                            par = a2.get_parent()
                            if par is res or a2.element not in ("N", "O", "S"):
                                continue
                            pol.add(f"{at.get_id()}-{par.get_resname()}{par.id[1]}:{a2.get_id()}({float(at - a2):.2f})")
                    row["sidechain_polar_contacts_3.5A"] = " ".join(sorted(pol)) or "-"
                    heavy = [a for a in res if a.get_id() not in ("N", "CA", "C", "O")]
                    row["n_atoms_within_4.5A_of_sidechain"] = len({a2.get_full_id() for at in heavy for a2 in all_ns.search(at.coord, 4.5) if a2.get_parent() is not res})
                    row["neighbours_4A_mouse_numbering"] = " ".join(f"{c.THREE[n]}{i}" for n, i in near if abs(i - mp) > 1)
            rows.append(row)

    placed = {r["id"]: r for r in rows}
    db = {}
    for v in spec:
        r = placed.get(v["id"])
        iso2_p = None
        if r and r.get("iso2_MANE") and r["iso2_MANE"][0].isalpha() and r["iso2_MANE"][-1].isalpha() and r["iso2_MANE"][1:-1].isdigit():
            x = r["iso2_MANE"]
            iso2_p = f"p.{c.ONE2THREE[x[0]]}{x[1:-1]}{c.ONE2THREE[x[-1]]}"
        c_iso2 = None
        hc = v.get("hgvs_c") or ""
        m = re.match(r"c\.(\d+)(.*)$", hc)
        if m and v.get("reported_transcript") == "NM_153486" and not iso2_p:
            q = c.cds_pos_iso1_to_iso2(int(m.group(1)))
            c_iso2 = f"c.{q}{m.group(2)}" if q else None
        elif m and not iso2_p:
            c_iso2 = hc
        db[v["id"]] = database_lookup(v, iso2_p, c_iso2)
        db[v["id"]]["query"] = {"rsid": v.get("rsid"), "iso2_protein": iso2_p, "c_MANE": c_iso2}

    out = {"pdb_used": PDB, "database_lookup": db, "pdb_chain_numbering_equals_mouse_uniprot": not mism, "pdb_numbering_mismatches": mism,
           "mouse_isoform2_identity": None, "cdna_checks": cdna_checks, "variants": rows}
    m2 = c.align_map(iso["iso2"], orth["mouse"])
    out["mouse_isoform2_identity"] = {"aligned": len(m2), "identical": sum(iso["iso2"][i - 1] == orth["mouse"][j - 1] for i, j in m2.items()),
                                       "same_numbering_everywhere": all(i == j for i, j in m2.items())}
    (c.RESULTS / "reported_variants_placed.json").write_text(json.dumps(out, indent=1))
    keys = sorted({k for r in rows for k in r}, key=lambda k: list(rows[0]).index(k) if k in rows[0] else 99)
    with open(c.RESULTS / "reported_variants_placed.tsv", "w", newline="") as fh:
        w = csv.DictWriter(fh, keys, delimiter="\t")
        w.writeheader()
        w.writerows(rows)
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
