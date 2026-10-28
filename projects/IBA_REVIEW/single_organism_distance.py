#!/usr/bin/env python3
"""Quantitative phylogenetic distance analysis for single-organism IBAs across ai-gene-review.

Computes four complementary distance metrics for every positive GOA IBA annotation
supported by experimental evidence from a single distinct non-self donor organism:

1. Taxonomic LCA Clade Depth (d_LCA) & Branch Steps (s_up + s_down):
   Distance along the NCBI/UniProt `OC` species tree between donor and target taxa,
   grouped into 7 phylogenetic distance tiers (from Tier 1 Genus/Intraspecies to
   Tier 7 Cross-Domain LUCA).
2. Excess PAINT Node Depth (Delta_depth = d_LCA - d_PTN):
   How many taxonomic ranks deeper in the PANTHER tree the PAINT curator placed
   the IBD ancestral assertion (PTN node) than the donor-target LCA actually requires.
3. PANTHER Subfamily Dilution (SAME_SF vs CROSS_SF):
   Whether the target protein and the single donor protein belong to the same
   PANTHER subfamily or cross a subfamily duplication/divergence boundary.
4. Exact PANTHER Tree Edge Steps (steps_from_ibd) & Duplications (duplication_on_path):
   Exact tree-edge distance and intervening gene-duplication events from the
   TreeGrafter path table (`projects/TREEGRAFTER/graft_paths_all.tsv`) where available.

Usage:
    python3 projects/IBA_REVIEW/single_organism_distance.py --summary
    python3 projects/IBA_REVIEW/single_organism_distance.py --tier 7
    python3 projects/IBA_REVIEW/single_organism_distance.py --candidates
    python3 projects/IBA_REVIEW/single_organism_distance.py --tsv reports/single_org_iba.tsv
"""

from __future__ import annotations

import argparse
import csv
import glob
import json
import os
import re
from collections import defaultdict
from typing import Any, Dict, List, Optional, Set, Tuple

import yaml

MOD_TO_TAXON: Dict[str, Tuple[str, str]] = {
    "MGI": ("10090", "Mus musculus"),
    "RGD": ("10116", "Rattus norvegicus"),
    "SGD": ("559292", "Saccharomyces cerevisiae"),
    "sgd": ("559292", "Saccharomyces cerevisiae"),
    "PomBase": ("284812", "Schizosaccharomyces pombe"),
    "JaponicusDB": ("402676", "Schizosaccharomyces japonicus"),
    "FB": ("7227", "Drosophila melanogaster"),
    "WB": ("6239", "Caenorhabditis elegans"),
    "ZFIN": ("7955", "Danio rerio"),
    "Xenbase": ("8355", "Xenopus laevis"),
    "TAIR": ("3702", "Arabidopsis thaliana"),
    "AGI_LocusCode": ("3702", "Arabidopsis thaliana"),
    "araport11": ("3702", "Arabidopsis thaliana"),
    "dictyBase": ("44689", "Dictyostelium discoideum"),
    "CGD": ("237561", "Candida albicans"),
    "EcoliWiki": ("83333", "Escherichia coli"),
    "RAP2022-09-01": ("39947", "Oryza sativa"),
}

PAINT_TAXON_NAMES: Dict[str, str] = {
    "": "LUCA / Root",
    "taxon:131567": "cellular organisms",
    "taxon:2": "Bacteria",
    "taxon:2157": "Archaea",
    "taxon:2759": "Eukaryota",
    "taxon:33154": "Opisthokonta",
    "taxon:4751": "Fungi",
    "taxon:4890": "Ascomycota",
    "taxon:33208": "Metazoa",
    "taxon:6072": "Eumetazoa",
    "taxon:33213": "Bilateria",
    "taxon:33317": "Protostomia",
    "taxon:1206794": "Ecdysozoa",
    "taxon:33511": "Deuterostomia",
    "taxon:7711": "Chordata",
    "taxon:7742": "Vertebrata",
    "taxon:7776": "Gnathostomata",
    "taxon:117570": "Teleostomi",
    "taxon:117571": "Euteleostomi",
    "taxon:8287": "Sarcopterygii",
    "taxon:32523": "Tetrapoda",
    "taxon:32524": "Amniota",
    "taxon:40674": "Mammalia",
    "taxon:32525": "Theria",
    "taxon:9347": "Eutheria",
    "taxon:1437010": "Boreoeutheria",
    "taxon:314146": "Euarchontoglires",
    "taxon:314147": "Glires",
    "taxon:9989": "Rodentia",
    "taxon:33090": "Viridiplantae",
    "taxon:35493": "Streptophyta",
    "taxon:3193": "Embryophyta",
    "taxon:58023": "Tracheophyta",
    "taxon:3398": "Magnoliopsida",
    "taxon:1224": "Pseudomonadota",
    "taxon:1236": "Gammaproteobacteria",
}

PAINT_TAXON_DEPTH: Dict[str, int] = {
    "": 0,
    "taxon:131567": 0,
    "taxon:2": 1,
    "taxon:2157": 1,
    "taxon:2759": 1,
    "taxon:33090": 2,
    "taxon:33154": 1,
    "taxon:4751": 2,
    "taxon:33208": 2,
    "taxon:6072": 3,
    "taxon:33213": 3,
    "taxon:33511": 4,
    "taxon:33317": 4,
    "taxon:1206794": 4,
    "taxon:7711": 5,
    "taxon:7742": 6,
    "taxon:117571": 6,
    "taxon:32523": 7,
    "taxon:32524": 8,
    "taxon:40674": 9,
    "taxon:32525": 9,
    "taxon:9347": 9,
    "taxon:314146": 9,
}

MOD_XREFS: Dict[str, Tuple[str, int]] = {
    "MGI": ("MGI", 0),
    "RGD": ("RGD", 0),
    "SGD": ("SGD", 0),
    "FlyBase": ("FB", 0),
    "WormBase": ("WB", 2),
    "ZFIN": ("ZFIN", 0),
    "TAIR": ("TAIR", 0),
    "Araport": ("AGI_LocusCode", 0),
    "dictyBase": ("dictyBase", 0),
    "PomBase": ("PomBase", 0),
    "CGD": ("CGD", 0),
}

TIER_NAMES: Dict[int, str] = {
    1: "Tier 1: Close Clade (e.g. Rodent <-> Primate, Murinae, Caenorhabditis)",
    2: "Tier 2: Order / Subphylum Split (e.g. Saccharomycotina, Magnoliopsida)",
    3: "Tier 3: Phylum / Subphylum Split (e.g. Euteleostomi, Ascomycota, Ecdysozoa)",
    4: "Tier 4: Deep Metazoa / Bilateria Split (Protostomia <-> Deuterostomia)",
    5: "Tier 5: Cross-Kingdom Opisthokonta / Amorphea / Deep Bacterial Split",
    6: "Tier 6: Cross-Supergroup (Eukaryota root: Plant/Algae <-> Opisthokont/Protist)",
    7: "Tier 7: Cross-Domain (LUCA: Bacteria/Archaea <-> Eukaryota)",
}

DOWNGRADE_ACTIONS = {"REMOVE", "MARK_AS_OVER_ANNOTATED", "MODIFY", "TOO_GENERAL"}
RETAIN_ACTIONS = {"ACCEPT", "KEEP_AS_NON_CORE"}


def classify_evolutionary_span(
    donor_org: str, target_os: str, lca: str
) -> Tuple[int, str]:
    """Assign an ordered evolutionary distance tier (1..7, higher = more distant) and label."""
    if lca == "Cellular organisms (LUCA)":
        return (7, "Tier 7: Cross-Domain (LUCA: Bacteria/Archaea <-> Eukaryota)")
    if lca == "Eukaryota":
        plant_orgs = {"Arabidopsis thaliana", "Oryza sativa"}
        amoebo_orgs = {"Dictyostelium discoideum"}
        d_is_plant = any(p in donor_org for p in plant_orgs)
        d_is_amoebo = any(a in donor_org for a in amoebo_orgs)
        if (
            d_is_plant
            or "Viridiplantae" in target_os
            or "Arabidopsis" in target_os
            or "Oryza" in target_os
            or "Triticum" in target_os
            or "Chlamydomonas" in target_os
        ):
            return (
                6,
                "Tier 6: Cross-Supergroup (Eukaryota root: Plant/Algae <-> Opisthokont/Protist)",
            )
        if d_is_amoebo:
            return (5, "Tier 5: Amorphea Split (Amoebozoa <-> Opisthokonta)")
        return (
            5,
            "Tier 5: Cross-Kingdom Opisthokonta (Fungi <-> Metazoa / Choanoflagellata)",
        )
    if lca in (
        "Bacteria",
        "Bacillati",
        "Gammaproteobacteria",
        "Enterobacteriaceae",
        "Actinomycetes",
    ):
        if lca == "Bacteria":
            return (5, "Tier 5: Deep Bacterial Split (Cross-Phylum Bacteria)")
        return (3, f"Tier 3: Intra-Phylum Bacteria ({lca})")
    if lca == "Metazoa":
        return (
            4,
            "Tier 4: Deep Metazoa / Bilateria Split (Protostomia [Worm/Fly] <-> Deuterostomia [Vertebrate])",
        )
    if lca in ("Ecdysozoa", "Arthropoda"):
        return (3, f"Tier 3: Intra-Protostomia ({lca}: Worm <-> Fly / Insect)")
    if lca in ("Ascomycota", "Saccharomycotina", "Pezizomycotina"):
        return (
            3 if lca == "Ascomycota" else 2,
            f"Tier {'3' if lca == 'Ascomycota' else '2'}: Fungal Split ({lca})",
        )
    if lca in (
        "Viridiplantae",
        "Embryophyta",
        "Magnoliopsida",
        "Pentapetalae",
        "rosids",
    ):
        return (
            3 if lca in ("Viridiplantae", "Embryophyta") else 2,
            f"Tier {'3' if lca in ('Viridiplantae', 'Embryophyta') else '2'}: Plant Split ({lca})",
        )
    if lca == "Euteleostomi":
        return (
            3,
            "Tier 3: Vertebrate Split (Euteleostomi: Teleost/Amphibian <-> Mammal/Bird)",
        )
    if lca in (
        "Eutheria",
        "Euarchontoglires",
        "Murinae",
        "Hominidae",
        "Caenorhabditis",
        "Aspergillus",
    ):
        return (1, f"Tier 1: Close Clade ({lca}, e.g. Rodent <-> Primate)")
    return (2, f"Tier 2: Other ({lca})")


def load_panther_entries() -> Tuple[Dict[str, Tuple[str, str, str, str, str, str]], Dict[str, str]]:
    acc_info: Dict[str, Tuple[str, str, str, str, str, str]] = {}
    taxon_names: Dict[str, str] = {}
    for path in sorted(glob.glob("interpro/panther/*/*-entries.csv")):
        fam = os.path.basename(os.path.dirname(path))
        with open(path, encoding="utf-8", errors="replace") as fh:
            reader = csv.DictReader(fh)
            for row in reader:
                acc = (row.get("id") or "").strip()
                tax = (row.get("source_tax_id") or "").strip()
                org = (row.get("source_tax_name") or "").strip()
                sf = (row.get("subfamily") or "").strip()
                sf_name = (row.get("subfamily_name") or "").strip()
                sym = (row.get("gene") or "").strip()
                if acc:
                    acc_info[acc] = (tax, org, fam, sf, sf_name, sym)
                if tax and org:
                    taxon_names[tax] = org
    return acc_info, taxon_names


def resolve_seed(
    tok: str, acc_info: Dict[str, Tuple[str, str, str, str, str, str]]
) -> Tuple[str, str, str, str, str, str]:
    if ":" not in tok:
        return ("", "", tok, "", "", "")
    prefix, rest = tok.split(":", 1)
    if prefix == "PANTHER":
        return ("PTN", "PTN", tok, "", "", "")
    if prefix in MOD_TO_TAXON:
        taxid, org = MOD_TO_TAXON[prefix]
        return (taxid, org, tok, "", "", "")
    if prefix == "ensembl":
        if rest.startswith("ENSMUSP"):
            return ("10090", "Mus musculus", tok, "", "", "")
        if rest.startswith("ENSRNOP"):
            return ("10116", "Rattus norvegicus", tok, "", "", "")
    if prefix == "ENSEMBL_GeneID" and rest.startswith("ENSG"):
        return ("9606", "Homo sapiens", tok, "", "", "")
    if prefix == "UniProtKB":
        if rest in acc_info:
            tax, org, fam, sf, sf_name, sym = acc_info[rest]
            return (tax, org, tok, fam, sf, sym)
        return ("UNRESOLVED_UP", rest, tok, "", "", "")
    return (f"OTHER:{prefix}", rest, tok, "", "", "")


def read_uniprot_lineage(uniprot_path: str) -> Tuple[str, str, List[str], str, str]:
    taxid, os_name, oc_list, fam, sf = "", "", [], "", ""
    if not os.path.exists(uniprot_path):
        return taxid, os_name, oc_list, fam, sf
    with open(uniprot_path, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            if line.startswith("OX   NCBI_TaxID="):
                m = re.search(r"NCBI_TaxID=(\d+)", line)
                if m:
                    taxid = m.group(1)
            elif line.startswith("OS   ") and not os_name:
                os_name = line[5:].strip().rstrip(".")
            elif line.startswith("OC   "):
                for tok in line[5:].strip().rstrip(".").split(";"):
                    tok = tok.strip()
                    if tok:
                        oc_list.append(tok)
            elif line.startswith("DR   PANTHER;"):
                m_sf = re.search(r"PANTHER;\s*(PTHR\d+):(SF\d+);", line)
                if m_sf:
                    fam, sf = m_sf.group(1), m_sf.group(2)
                else:
                    m_f = re.search(r"PANTHER;\s*(PTHR\d+);", line)
                    if m_f and not fam:
                        fam = m_f.group(1)
    return taxid, os_name, oc_list, fam, sf


def build_taxon_lineages() -> Dict[str, List[str]]:
    tax_lineage: Dict[str, List[str]] = {}
    for org_dir in sorted(os.listdir("genes")):
        org_path = os.path.join("genes", org_dir)
        if not os.path.isdir(org_path):
            continue
        for gene_dir in sorted(os.listdir(org_path))[:10]:
            up_path = os.path.join(org_path, gene_dir, f"{gene_dir}-uniprot.txt")
            if os.path.exists(up_path):
                taxid, _, oc_list, _, _ = read_uniprot_lineage(up_path)
                if taxid and oc_list:
                    tax_lineage[taxid] = oc_list
                    break
    return tax_lineage


def build_mod_to_acc() -> Dict[str, str]:
    mod_to_acc: Dict[str, str] = {}
    mod_species_dirs = [
        "mouse", "rat", "yeast", "DROME", "worm", "DANRE", "ARATH", "DICDI", "SCHPO", "CANAL"
    ]
    for sdir in mod_species_dirs:
        sdir_path = os.path.join("genes", sdir)
        if not os.path.isdir(sdir_path):
            continue
        for up_file in glob.glob(os.path.join(sdir_path, "*", "*-uniprot.txt")):
            with open(up_file, encoding="utf-8", errors="replace") as fh:
                txt = fh.read()
            ac_m = re.search(r"^AC\s+([A-Z0-9]+);", txt, re.M)
            if not ac_m:
                continue
            acc = ac_m.group(1)
            for dr_name, (id_prefix, field_idx) in MOD_XREFS.items():
                for m in re.finditer(rf"^DR   {re.escape(dr_name)}; (.+)$", txt, re.M):
                    fields = [x.strip().rstrip(".") for x in m.group(1).split(";")]
                    if field_idx < len(fields) and fields[field_idx]:
                        val = fields[field_idx]
                        mod_to_acc[f"{id_prefix}:{val}"] = acc
                        if dr_name == "TAIR" and not val.startswith("locus:"):
                            mod_to_acc[f"TAIR:locus:{val}"] = acc
                        if dr_name == "MGI" and val.startswith("MGI:"):
                            mod_to_acc[f"MGI:{val}"] = acc
    return mod_to_acc


def compute_lineage_distance(lin_a: List[str], lin_b: List[str]) -> Tuple[str, int, int, int, int]:
    if not lin_a or not lin_b:
        return ("Unknown", -1, -1, -1, -1)
    common = 0
    for x, y in zip(lin_a, lin_b):
        if x == y:
            common += 1
        else:
            break
    if common == 0:
        lca = "Cellular organisms (LUCA)"
    else:
        lca = lin_a[common - 1]
    steps_up = len(lin_a) - common
    steps_down = len(lin_b) - common
    return (lca, common, steps_up, steps_down, steps_up + steps_down)


def scan_corpus() -> Tuple[int, int, int, int, List[Dict[str, Any]]]:
    acc_info, _ = load_panther_entries()
    tax_lineage = build_taxon_lineages()
    mod_to_acc = build_mod_to_acc()

    paint_index: Dict[Tuple[str, str], Dict[str, Any]] = {}
    n_paint_rows = 0
    single_org_ibd = 0
    for path in sorted(glob.glob("interpro/panther/*/*-paint.tsv")):
        with open(path, encoding="utf-8", errors="replace") as fh:
            reader = csv.DictReader(fh, delimiter="\t")
            for row in reader:
                if row.get("evidence") != "IBD" or row.get("negated") == "true":
                    continue
                n_paint_rows += 1
                seeds = [
                    s for s in (row.get("seeds") or "").split("|") if s and not s.startswith("PANTHER:")
                ]
                resolved = [resolve_seed(s, acc_info) for s in seeds]
                orgs = {
                    r[0]
                    for r in resolved
                    if r[0] and not r[0].startswith(("PTN", "UNRESOLVED", "OTHER"))
                }
                if len(orgs) == 1 and all(
                    not r[0].startswith(("UNRESOLVED", "OTHER")) for r in resolved
                ):
                    single_org_ibd += 1
                paint_index[(row["node"], row["go_id"])] = {
                    "family": row["family"],
                    "node": row["node"],
                    "go_id": row["go_id"],
                    "aspect": row["aspect"],
                    "seeds": seeds,
                    "taxon": row.get("taxon", ""),
                }

    graft_index: Dict[Tuple[str, str, str], Dict[str, Any]] = {}
    graft_single_org_rows: List[Dict[str, Any]] = []
    graft_file = "projects/TREEGRAFTER/graft_paths_all.tsv"
    if os.path.exists(graft_file):
        with open(graft_file, encoding="utf-8", errors="replace") as fh:
            for row in csv.DictReader(fh, delimiter="\t"):
                f = row.get("file", "")
                parts = f.split("/")
                if len(parts) >= 3:
                    key = (parts[1], parts[2], row.get("term_id", ""))
                    graft_index[key] = row
                if row.get("status") == "ok" and (row.get("steps_from_ibd") or "").isdigit():
                    g_seeds = [
                        s for s in (row.get("seeds") or "").split("|") if s and not s.startswith("PANTHER:")
                    ]
                    g_res = [resolve_seed(s, acc_info) for s in g_seeds]
                    g_orgs = {
                        r[0] for r in g_res if r[0] and not r[0].startswith(("PTN", "UNRESOLVED", "OTHER"))
                    }
                    if len(g_orgs) == 1 and all(
                        not r[0].startswith(("UNRESOLVED", "OTHER")) for r in g_res
                    ):
                        graft_single_org_rows.append(
                            {
                                "action": row.get("action", ""),
                                "steps_from_ibd": int(row["steps_from_ibd"]),
                                "duplication_on_path": row.get("duplication_on_path", "").lower() == "true",
                            }
                        )

    n_iba_rows = 0
    n_single_org_leaf = 0
    candidate_by_gene: Dict[Tuple[str, str], List[Dict[str, Any]]] = defaultdict(list)

    for goa_path in sorted(glob.glob("genes/*/*/*-goa.tsv")):
        parts = goa_path.split(os.sep)
        org_dir, gene_dir = parts[1], parts[2]
        with open(goa_path, encoding="utf-8", errors="replace") as fh:
            for line in fh:
                if "\tIBA\t" not in line:
                    continue
                c = line.rstrip("\n").split("\t")
                if len(c) < 13 or c[8] != "IBA" or "NOT" in c[3]:
                    continue
                n_iba_rows += 1
                target_acc = c[1]
                go_id = c[4]
                go_name = c[5]
                aspect = c[6]
                with_from = c[10]
                target_taxid = c[11]
                target_os = c[12]

                tokens = [t.strip() for t in re.split(r"[|,]", with_from) if t.strip()]
                ptn_nodes = [t.split(":", 1)[1] for t in tokens if t.startswith("PANTHER:PTN")]
                seed_toks = [t for t in tokens if not t.startswith("PANTHER:")]
                resolved = [resolve_seed(s, acc_info) for s in seed_toks]
                donor_taxa = {
                    r[0]
                    for r in resolved
                    if r[0] and not r[0].startswith(("PTN", "UNRESOLVED", "OTHER"))
                }
                has_unresolved = any(r[0].startswith(("UNRESOLVED", "OTHER")) for r in resolved)
                if len(donor_taxa) == 1 and not has_unresolved:
                    n_single_org_leaf += 1
                    donor_tax = next(iter(donor_taxa))
                    if donor_tax != target_taxid:
                        donor_org = next(r[1] for r in resolved if r[0] == donor_tax)
                        paint_rec = None
                        for ptn in ptn_nodes:
                            if (ptn, go_id) in paint_index:
                                paint_rec = paint_index[(ptn, go_id)]
                                break
                        t_info = acc_info.get(target_acc)
                        target_fam = (
                            t_info[2] if t_info else (paint_rec["family"] if paint_rec else "")
                        )
                        target_sf = t_info[3] if t_info else ""
                        donor_sfs_set: Set[str] = {r[4] for r in resolved if r[4]}
                        if not donor_sfs_set:
                            for tok in seed_toks:
                                acc = mod_to_acc.get(tok)
                                if acc and acc in acc_info and acc_info[acc][3]:
                                    donor_sfs_set.add(acc_info[acc][3])
                        candidate_by_gene[(org_dir, gene_dir)].append(
                            {
                                "org_dir": org_dir,
                                "gene": gene_dir,
                                "target_acc": target_acc,
                                "target_taxid": target_taxid,
                                "target_os": target_os,
                                "go_id": go_id,
                                "go_name": go_name,
                                "aspect": aspect,
                                "ptn_id": ptn_nodes[0] if ptn_nodes else "",
                                "n_seed_tokens": len(seed_toks),
                                "seed_toks": "|".join(seed_toks),
                                "donor_taxid": donor_tax,
                                "donor_org": donor_org,
                                "target_fam": target_fam,
                                "target_sf": target_sf,
                                "donor_sfs": "|".join(sorted(donor_sfs_set)),
                                "paint_taxon": paint_rec["taxon"] if paint_rec else None,
                            }
                        )

    loader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
    records: List[Dict[str, Any]] = []
    for (org_dir, gene_dir), rows in sorted(candidate_by_gene.items()):
        up_path = os.path.join("genes", org_dir, gene_dir, f"{gene_dir}-uniprot.txt")
        taxid, _, oc_list, up_fam, up_sf = read_uniprot_lineage(up_path)
        if taxid and oc_list and taxid not in tax_lineage:
            tax_lineage[taxid] = oc_list

        rev_path = os.path.join("genes", org_dir, gene_dir, f"{gene_dir}-ai-review.yaml")
        rev_map: Dict[str, Dict[str, Any]] = {}
        if os.path.exists(rev_path):
            try:
                with open(rev_path, encoding="utf-8", errors="replace") as rfh:
                    rdoc = yaml.load(rfh, Loader=loader) or {}
                for ann in rdoc.get("existing_annotations") or []:
                    if not isinstance(ann, dict) or ann.get("retired"):
                        continue
                    if ann.get("evidence_type") == "IBA":
                        tid = (ann.get("term") or {}).get("id", "")
                        rev = ann.get("review") or {}
                        prop = ann.get("propagation_review") or rev.get("propagation_review") or {}
                        rev_map[tid] = {
                            "action": rev.get("action", ""),
                            "reason": (rev.get("reason") or "").replace("\n", " ").strip(),
                            "root_cause": prop.get("root_cause", ""),
                        }
            except Exception:
                pass

        for r in rows:
            d_lin = tax_lineage.get(r["donor_taxid"], [])
            t_lin = oc_list or tax_lineage.get(r["target_taxid"], [])
            lca, lca_depth, steps_up, steps_down, total_steps = compute_lineage_distance(
                d_lin, t_lin
            )
            r["lca_clade"] = lca
            r["lca_depth"] = lca_depth
            r["steps_up"] = steps_up
            r["steps_down"] = steps_down
            r["total_tax_steps"] = total_steps
            tier, tier_label = classify_evolutionary_span(r["donor_org"], r["target_os"], lca)
            r["tier"] = tier
            r["tier_label"] = tier_label
            if not r["target_fam"] and up_fam:
                r["target_fam"] = up_fam
            if not r["target_sf"] and up_sf:
                r["target_sf"] = up_sf

            donor_sfs_list = [s for s in r["donor_sfs"].split("|") if s]
            if not r["target_sf"] or not donor_sfs_list:
                r["sf_status"] = "UNKNOWN_SF"
            elif r["target_sf"] in donor_sfs_list:
                r["sf_status"] = "SAME_SF"
            else:
                r["sf_status"] = "CROSS_SF"

            grow = graft_index.get((org_dir, gene_dir, r["go_id"]), {})
            if grow.get("status") == "ok" and grow.get("steps_from_ibd", "").isdigit():
                r["graft_steps_from_ibd"] = int(grow["steps_from_ibd"])
                r["graft_dup_on_path"] = grow.get("duplication_on_path", "").lower() == "true"
            else:
                r["graft_steps_from_ibd"] = None
                r["graft_dup_on_path"] = None

            rev_info = rev_map.get(r["go_id"], {})
            r["action"] = rev_info.get("action") or "UNREVIEWED"
            r["reason"] = rev_info.get("reason", "")
            r["root_cause"] = rev_info.get("root_cause", "")
            records.append(r)

    return n_iba_rows, n_single_org_leaf, n_paint_rows, single_org_ibd, records, graft_single_org_rows


def print_summary(
    n_iba_rows: int,
    n_single_org_leaf: int,
    n_paint_rows: int,
    single_org_ibd: int,
    records: List[Dict[str, Any]],
    graft_single_org_rows: List[Dict[str, Any]],
) -> None:
    rated = [r for r in records if r["action"] in (DOWNGRADE_ACTIONS | RETAIN_ACTIONS)]
    unique_genes = len({(r["org_dir"], r["gene"]) for r in records})

    print("=" * 100)
    print("SINGLE-ORGANISM IBA PHYLOGENETIC DISTANCE SUMMARY")
    print("=" * 100)
    print(f"Total positive GOA IBA rows scanned:                 {n_iba_rows:,}")
    print(
        f"Single-organism GOA IBA rows (incl. self-species):   {n_single_org_leaf:,} "
        f"({100.0 * n_single_org_leaf / max(1, n_iba_rows):.1f}%)"
    )
    print(
        f"Non-self single-organism IBA rows:                   {len(records):,} "
        f"({100.0 * len(records) / max(1, n_iba_rows):.1f}%) across {unique_genes:,} genes"
    )
    print(f"Rated non-self single-organism IBA rows:             {len(rated):,}")
    print(
        f"Cached PAINT IBD assertions (single-taxon / total):  {single_org_ibd:,} / {n_paint_rows:,} "
        f"({100.0 * single_org_ibd / max(1, n_paint_rows):.1f}%)"
    )
    print()

    print("1. REJECTION RATE BY PHYLOGENETIC DISTANCE TIER (d_LCA)")
    print("-" * 100)
    print(
        f"{'Tier':<66} | {'Rated':>6} | {'Keep':>6} | {'Downgr':>6} | {'%Down':>6} | {'%REM':>6}"
    )
    print("-" * 100)
    for tier in sorted(TIER_NAMES.keys()):
        sub = [r for r in rated if r["tier"] == tier]
        if not sub:
            continue
        keep = sum(1 for r in sub if r["action"] in RETAIN_ACTIONS)
        down = sum(1 for r in sub if r["action"] in DOWNGRADE_ACTIONS)
        rem = sum(1 for r in sub if r["action"] == "REMOVE")
        print(
            f"{TIER_NAMES[tier]:<66} | {len(sub):>6} | {keep:>6} | {down:>6} | "
            f"{100.0 * down / len(sub):>5.1f}% | {100.0 * rem / len(sub):>5.1f}%"
        )

    print("\n1B. REJECTION RATE BY TOTAL TAXONOMIC BRANCH STEPS (steps_up + steps_down)")
    print("-" * 100)
    for label, pred in [
        ("02-06 steps (Close: Genus/Family)", lambda r: 0 <= r["total_tax_steps"] <= 6),
        ("07-12 steps (Order/Superorder, e.g. Rodent-Primate)", lambda r: 7 <= r["total_tax_steps"] <= 12),
        ("13-18 steps (Phylum/Subphylum, e.g. Fish-Mammal)", lambda r: 13 <= r["total_tax_steps"] <= 18),
        ("19-24 steps (Kingdom/Supergroup, e.g. Yeast-Human)", lambda r: 19 <= r["total_tax_steps"] <= 24),
        ("25+   steps (Deep Bilateria / Cross-Kingdom / Cross-Domain)", lambda r: r["total_tax_steps"] >= 25),
    ]:
        sub = [r for r in rated if pred(r)]
        if not sub:
            continue
        down = sum(1 for r in sub if r["action"] in DOWNGRADE_ACTIONS)
        rem = sum(1 for r in sub if r["action"] == "REMOVE")
        print(
            f"{label:<66} | n={len(sub):>4} | Downgraded: {down:>4} ({100.0 * down / len(sub):>5.1f}%) | "
            f"REMOVE: {rem:>4} ({100.0 * rem / len(sub):>5.1f}%)"
        )

    print("\n2. EXCESS PAINT NODE DEPTH ON CLOSE VERTEBRATE PAIRS (d_LCA >= 6)")
    print("-" * 100)
    for label, pred in [
        (
            "Scoped within Vertebrata (d_PTN >= 6)",
            lambda r: r["lca_depth"] >= 6
            and r["paint_taxon"] is not None
            and PAINT_TAXON_DEPTH.get(r["paint_taxon"], -1) >= 6,
        ),
        (
            "Over-deeply placed at LUCA / Eukaryota (d_PTN <= 1)",
            lambda r: r["lca_depth"] >= 6
            and r["paint_taxon"] is not None
            and 0 <= PAINT_TAXON_DEPTH.get(r["paint_taxon"], -1) <= 1,
        ),
    ]:
        sub = [r for r in rated if pred(r)]
        if not sub:
            continue
        down = sum(1 for r in sub if r["action"] in DOWNGRADE_ACTIONS)
        rem = sum(1 for r in sub if r["action"] == "REMOVE")
        print(
            f"{label:<66} | n={len(sub):>4} | Downgraded: {down:>4} ({100.0 * down / len(sub):>5.1f}%) | "
            f"REMOVE: {rem:>4} ({100.0 * rem / len(sub):>5.1f}%)"
        )

    print("\n3. PANTHER SUBFAMILY CROSSING (SAME_SF vs CROSS_SF)")
    print("-" * 100)
    for dist_label, dist_pred in [
        ("Close/moderate taxa (d_LCA >= 4)", lambda r: r["lca_depth"] >= 4),
        ("Distant taxa (d_LCA <= 3)", lambda r: r["lca_depth"] <= 3),
    ]:
        for sf in ("SAME_SF", "CROSS_SF"):
            sub = [r for r in rated if dist_pred(r) and r["sf_status"] == sf]
            if not sub:
                continue
            down = sum(1 for r in sub if r["action"] in DOWNGRADE_ACTIONS)
            rem = sum(1 for r in sub if r["action"] == "REMOVE")
            label = f"{dist_label} + {sf}"
            print(
                f"{label:<66} | n={len(sub):>4} | Downgraded: {down:>4} ({100.0 * down / len(sub):>5.1f}%) | "
                f"REMOVE: {rem:>4} ({100.0 * rem / len(sub):>5.1f}%)"
            )

    print("\n4. EXACT TREEGRAFTER TREE STEPS & DUPLICATIONS (single-organism IBD seeds)")
    print("-" * 100)
    gp_rows = [
        r for r in graft_single_org_rows if r["action"] in (DOWNGRADE_ACTIONS | RETAIN_ACTIONS)
    ]
    for label, pred in [
        (
            "< 10 tree steps, duplication_on_path=False",
            lambda r: r["steps_from_ibd"] < 10 and not r["duplication_on_path"],
        ),
        (
            "< 10 tree steps, duplication_on_path=True",
            lambda r: r["steps_from_ibd"] < 10 and r["duplication_on_path"],
        ),
        (
            ">= 10 tree steps, duplication_on_path=False",
            lambda r: r["steps_from_ibd"] >= 10 and not r["duplication_on_path"],
        ),
        (
            ">= 10 tree steps, duplication_on_path=True",
            lambda r: r["steps_from_ibd"] >= 10 and r["duplication_on_path"],
        ),
    ]:
        sub = [r for r in gp_rows if pred(r)]
        if not sub:
            continue
        down = sum(1 for r in sub if r["action"] in DOWNGRADE_ACTIONS)
        rem = sum(1 for r in sub if r["action"] == "REMOVE")
        print(
            f"{label:<66} | n={len(sub):>4} | Downgraded: {down:>4} ({100.0 * down / len(sub):>5.1f}%) | "
            f"REMOVE: {rem:>4} ({100.0 * rem / len(sub):>5.1f}%)"
        )


def print_tier_rows(records: List[Dict[str, Any]], tier: int) -> None:
    sub = [r for r in records if r["tier"] == tier]
    print(f"Rows in {TIER_NAMES.get(tier, f'Tier {tier}')}: {len(sub)}")
    for r in sub:
        print(
            f"  {r['org_dir']}/{r['gene']} | {r['go_id']} ({r['go_name']}) | "
            f"donor={r['donor_org']} | PTN={r['ptn_id']} | "
            f"sf={r['sf_status']} | action={r['action']}"
        )


def print_candidates(records: List[Dict[str, Any]]) -> None:
    keywords = (
        "do not", "does not", "lacks", "absent", "plant", "yeast-specific",
        "only in", "artifact", "over-annotat", "mislead", "cytosolic",
        "not directly", "unlike",
    )
    print("HIGH-DISTANCE (Tier 4-7) RETAINED SINGLE-ORGANISM IBAs WITH SKEPTICAL REVIEW REASONS:")
    print("-" * 100)
    for r in records:
        if r["tier"] >= 4 and r["action"] in RETAIN_ACTIONS:
            reason_lower = r["reason"].lower()
            if any(k in reason_lower for k in keywords):
                print(
                    f"[Tier {r['tier']}] {r['org_dir']}/{r['gene']} | {r['go_id']} ({r['go_name']}) | "
                    f"donor={r['donor_org']} ({r['seed_toks']}) | action={r['action']}"
                )
                print(f"    reason: {r['reason'][:220]}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--summary", action="store_true", help="Print summary tables")
    parser.add_argument("--tier", type=int, choices=range(1, 8), help="List rows in a specific tier (1..7)")
    parser.add_argument("--candidates", action="store_true", help="List high-distance retained re-review candidates")
    parser.add_argument("--tsv", type=str, help="Write full per-row metrics table to TSV")
    parser.add_argument("--json", type=str, help="Write full per-row metrics table to JSON")
    args = parser.parse_args()

    (
        n_iba_rows,
        n_single_org_leaf,
        n_paint_rows,
        single_org_ibd,
        records,
        graft_single_org_rows,
    ) = scan_corpus()

    if args.summary or not (args.tier or args.candidates or args.tsv or args.json):
        print_summary(
            n_iba_rows,
            n_single_org_leaf,
            n_paint_rows,
            single_org_ibd,
            records,
            graft_single_org_rows,
        )
    if args.tier:
        print_tier_rows(records, args.tier)
    if args.candidates:
        print_candidates(records)
    if args.tsv:
        os.makedirs(os.path.dirname(os.path.abspath(args.tsv)), exist_ok=True)
        if records:
            fieldnames = list(records[0].keys())
            with open(args.tsv, "w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter="\t")
                writer.writeheader()
                writer.writerows(records)
        print(f"Wrote {len(records)} rows to {args.tsv}")
    if args.json:
        os.makedirs(os.path.dirname(os.path.abspath(args.json)), exist_ok=True)
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(records, f, indent=2)
        print(f"Wrote {len(records)} rows to {args.json}")


if __name__ == "__main__":
    main()
