#!/usr/bin/env python3
"""Quantitative phylogenetic distance analysis for single-organism IBAs across ai-gene-review.

Computes four complementary distance metrics for every positive GOA IBA annotation
supported by experimental evidence from a single distinct non-self donor organism:

1. Taxonomic LCA Clade Depth (d_LCA) & Branch Steps (s_up + s_down):
   Distance along the NCBI/UniProt `OC` species tree between donor and target taxa,
   grouped into 7 phylogenetic distance tiers (from Tier 1 Close Clade to
   Tier 7 Cross-Domain LUCA).
2. Excess PAINT Node Depth (Delta_depth = d_LCA - d_PTN):
   How many taxonomic ranks deeper in the PANTHER tree the PAINT curator placed
   the IBD ancestral assertion (PTN node) than the donor-target LCA actually requires
   (calibrated to vertebrate target lineages where d_LCA >= 6).
3. PANTHER Subfamily Dilution (SAME_SF vs CROSS_SF):
   Whether the target protein and the single donor protein belong to the same
   PANTHER subfamily or cross a subfamily duplication/divergence boundary.
4. Exact PANTHER Tree Edge Steps (steps_from_ibd) & Duplications (duplication_on_path):
   Exact tree-edge distance and intervening gene-duplication events from the
   TreeGrafter path table (`projects/TREEGRAFTER/graft_paths_all.tsv`).
5. Donor-Support Topology Regimes (d_MRCA vs d_LCA across all non-self GOA IBAs):
   Compares single-gene single-taxon (R1), multi-paralog single-taxon (R2),
   multi-species single-clade jump (R3: d_MRCA > d_LCA), and phylogenetically
   bracketed multi-species (R4: d_MRCA <= d_LCA) transfers.

Usage:
    uv run python projects/IBA_REVIEW/single_organism_distance.py --summary
    uv run python projects/IBA_REVIEW/single_organism_distance.py --regimes
    uv run python projects/IBA_REVIEW/single_organism_distance.py --tier 7
    uv run python projects/IBA_REVIEW/single_organism_distance.py --candidates
    uv run python projects/IBA_REVIEW/single_organism_distance.py --tsv reports/single_org_iba.tsv
    uv run pytest --doctest-modules projects/IBA_REVIEW/single_organism_distance.py
"""

from __future__ import annotations

import argparse
import csv
import glob
import json
import os
import re
from collections import defaultdict
from typing import Any, Dict, List, NamedTuple, Set, Tuple

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

# Only donor taxa without a local `genes/<ORG>/*/*-uniprot.txt` file need fallback OC lineages.
FALLBACK_TAXON_LINEAGES: Dict[str, List[str]] = {
    "402676": [
        "Eukaryota",
        "Fungi",
        "Dikarya",
        "Ascomycota",
        "Taphrinomycotina",
        "Schizosaccharomycetes",
        "Schizosaccharomycetales",
        "Schizosaccharomycetaceae",
        "Schizosaccharomyces",
    ],
    "8355": [
        "Eukaryota",
        "Metazoa",
        "Chordata",
        "Craniata",
        "Vertebrata",
        "Euteleostomi",
        "Amphibia",
        "Batrachia",
        "Anura",
        "Pipidae",
        "Xenopus",
    ],
}

PAINT_TAXON_NAMES: Dict[str, str] = {
    "": "Unrecorded PAINT taxon",
    "taxon:": "Unrecorded PAINT taxon",
    "taxon:131567": "cellular organisms",
    "taxon:2": "Bacteria",
    "taxon:2157": "Archaea",
    "taxon:2759": "Eukaryota",
    "taxon:33154": "Opisthokonta",
    "taxon:4751": "Fungi",
    "taxon:451864": "Dikarya",
    "taxon:4890": "Ascomycota",
    "taxon:147538": "Pezizomycotina",
    "taxon:4892": "Saccharomycetales",
    "taxon:2952368": "Saccharomyceta",
    "taxon:4893": "Saccharomycetaceae",
    "taxon:4895": "Schizosaccharomycetaceae",
    "taxon:554915": "Amoebozoa",
    "taxon:5782": "Dictyostelia",
    "taxon:2698737": "Sar",
    "taxon:4734": "Peronosporales",
    "taxon:5654": "Trypanosomatidae",
    "taxon:33208": "Metazoa",
    "taxon:6072": "Eumetazoa",
    "taxon:33213": "Bilateria",
    "taxon:33317": "Protostomia",
    "taxon:1206794": "Ecdysozoa",
    "taxon:6237": "Caenorhabditis",
    "taxon:6656": "Arthropoda",
    "taxon:33392": "Endopterygota",
    "taxon:7147": "Diptera",
    "taxon:33511": "Deuterostomia",
    "taxon:7711": "Chordata",
    "taxon:7742": "Vertebrata",
    "taxon:7776": "Gnathostomata",
    "taxon:117570": "Teleostomi",
    "taxon:117571": "Euteleostomi",
    "taxon:32443": "Teleostei",
    "taxon:41665": "Clupeocephala",
    "taxon:8287": "Sarcopterygii",
    "taxon:32523": "Tetrapoda",
    "taxon:32524": "Amniota",
    "taxon:40674": "Mammalia",
    "taxon:32525": "Theria",
    "taxon:9347": "Eutheria",
    "taxon:1437010": "Boreoeutheria",
    "taxon:314146": "Euarchontoglires",
    "taxon:9526": "Catarrhini",
    "taxon:207598": "Homininae",
    "taxon:314147": "Glires",
    "taxon:9989": "Rodentia",
    "taxon:39107": "Murinae",
    "taxon:33090": "Viridiplantae",
    "taxon:35493": "Streptophyta",
    "taxon:3193": "Embryophyta",
    "taxon:58023": "Tracheophyta",
    "taxon:3398": "Magnoliopsida",
    "taxon:1437183": "Mesangiospermae",
    "taxon:71240": "eudicotyledons",
    "taxon:1437201": "Pentapetalae",
    "taxon:71275": "rosids",
    "taxon:91836": "malvids",
    "taxon:3700": "Brassicaceae",
    "taxon:4447": "Liliopsida",
    "taxon:147369": "BOP clade",
    "taxon:4479": "Poaceae",
    "taxon:1224": "Pseudomonadota",
    "taxon:1236": "Gammaproteobacteria",
    "taxon:543": "Enterobacteriaceae",
    "taxon:1783272": "Terrabacteria group",
    "taxon:1239": "Bacillota",
    "taxon:1385": "Bacillales",
    "taxon:2037": "Actinomycetales",
    "taxon:1117": "Cyanobacteriota",
    "taxon:28890": "Methanobacteriota",
}

# Approximate clade depth on the vertebrate-calibrated UniProt OC scale.
# Every explicit `taxon:<id>` key in PAINT_TAXON_NAMES has a corresponding entry here;
# blank `""` / `"taxon:"` strings (where no taxon constraint was recorded in the PAINT GAF)
# are intentionally omitted so they fall into the unrecorded/unmapped bucket.
PAINT_TAXON_DEPTH: Dict[str, int] = {
    "taxon:131567": 0,
    "taxon:2": 1,
    "taxon:2157": 1,
    "taxon:2759": 1,
    "taxon:33154": 1,
    "taxon:33090": 2,
    "taxon:4751": 2,
    "taxon:554915": 2,
    "taxon:2698737": 2,
    "taxon:33208": 2,
    "taxon:1224": 2,
    "taxon:1783272": 2,
    "taxon:1239": 2,
    "taxon:1117": 2,
    "taxon:28890": 2,
    "taxon:451864": 3,
    "taxon:4890": 3,
    "taxon:5782": 3,
    "taxon:6072": 3,
    "taxon:33213": 3,
    "taxon:35493": 3,
    "taxon:1236": 3,
    "taxon:2037": 3,
    "taxon:147538": 4,
    "taxon:4892": 4,
    "taxon:2952368": 4,
    "taxon:4895": 4,
    "taxon:4734": 4,
    "taxon:5654": 4,
    "taxon:33511": 4,
    "taxon:33317": 4,
    "taxon:1206794": 4,
    "taxon:3193": 4,
    "taxon:1385": 4,
    "taxon:4893": 5,
    "taxon:6656": 5,
    "taxon:7711": 5,
    "taxon:58023": 5,
    "taxon:543": 5,
    "taxon:6237": 6,
    "taxon:33392": 6,
    "taxon:7147": 6,
    "taxon:3398": 6,
    "taxon:1437183": 6,
    "taxon:71240": 6,
    "taxon:1437201": 6,
    "taxon:71275": 6,
    "taxon:91836": 6,
    "taxon:4447": 6,
    "taxon:147369": 6,
    "taxon:7742": 6,
    "taxon:7776": 6,
    "taxon:117570": 6,
    "taxon:117571": 6,
    "taxon:8287": 6,
    "taxon:32443": 7,
    "taxon:41665": 7,
    "taxon:3700": 7,
    "taxon:4479": 7,
    "taxon:32523": 7,
    "taxon:32524": 8,
    "taxon:40674": 9,
    "taxon:32525": 9,
    "taxon:9347": 9,
    "taxon:1437010": 9,
    "taxon:314146": 9,
    "taxon:9526": 10,
    "taxon:207598": 10,
    "taxon:314147": 10,
    "taxon:9989": 10,
    "taxon:39107": 10,
}

MOD_XREFS: Dict[str, Tuple[str, int]] = {
    "MGI": ("MGI", 0),
    "RGD": ("RGD", 0),
    "SGD": ("SGD", 0),
    "FlyBase": ("FB", 0),
    "WormBase": ("WB", 2),
    "ZFIN": ("ZFIN", 0),
    "Xenbase": ("Xenbase", 0),
    "TAIR": ("TAIR", 0),
    "Araport": ("AGI_LocusCode", 0),
    "dictyBase": ("dictyBase", 0),
    "PomBase": ("PomBase", 0),
    "CGD": ("CGD", 0),
}

TIER_NAMES: Dict[int, str] = {
    0: "Tier 0: Unknown / Unresolved Donor Lineage",
    1: "Tier 1: Close Clade (e.g. Rodent <-> Primate, Murinae, Caenorhabditis)",
    2: "Tier 2: Intermediate / Unenumerated Clade (e.g. Saccharomycotina, Magnoliopsida, Residual)",
    3: "Tier 3: Phylum / Subphylum Split (e.g. Euteleostomi, Ascomycota, Ecdysozoa)",
    4: "Tier 4: Deep Metazoa / Bilateria Split (Protostomia <-> Deuterostomia)",
    5: "Tier 5: Cross-Kingdom Opisthokonta / Amorphea / Deep Bacterial Split",
    6: "Tier 6: Cross-Supergroup (Eukaryota root: Plant/Algae <-> Opisthokont/Protist)",
    7: "Tier 7: Cross-Domain (LUCA: Bacteria/Archaea <-> Eukaryota)",
}

FAILURE_ACTIONS = {"REMOVE", "MARK_AS_OVER_ANNOTATED"}
REFINEMENT_ACTIONS = {"MODIFY", "TOO_GENERAL"}
DOWNGRADE_ACTIONS = FAILURE_ACTIONS | REFINEMENT_ACTIONS
RETAIN_ACTIONS = {"ACCEPT", "KEEP_AS_NON_CORE"}


def classify_evolutionary_span(
    donor_org: str, target_os: str, lca: str
) -> Tuple[int, str]:
    """Assign an ordered evolutionary distance tier (1..7, higher = more distant; 0 = Unknown).

    >>> classify_evolutionary_span("Escherichia coli", "Homo sapiens", "Cellular organisms (LUCA)")
    (7, 'Tier 7: Cross-Domain (LUCA: Bacteria/Archaea <-> Eukaryota)')
    >>> classify_evolutionary_span("Arabidopsis thaliana", "Homo sapiens", "Eukaryota")
    (6, 'Tier 6: Cross-Supergroup (Eukaryota root: Plant/Algae <-> Opisthokont/Protist)')
    >>> classify_evolutionary_span("Saccharomyces cerevisiae", "Homo sapiens", "Eukaryota")
    (5, 'Tier 5: Cross-Kingdom Opisthokonta (Fungi <-> Metazoa / Choanoflagellata)')
    >>> classify_evolutionary_span("Drosophila melanogaster", "Homo sapiens", "Metazoa")
    (4, 'Tier 4: Deep Metazoa / Bilateria Split (Protostomia [Worm/Fly] <-> Deuterostomia [Vertebrate])')
    >>> classify_evolutionary_span("Danio rerio", "Homo sapiens", "Euteleostomi")
    (3, 'Tier 3: Vertebrate Split (Euteleostomi: Teleost/Amphibian <-> Mammal/Bird)')
    >>> classify_evolutionary_span("Mus musculus", "Homo sapiens", "Euarchontoglires")
    (1, 'Tier 1: Close Clade (Euarchontoglires, e.g. Rodent <-> Primate)')
    >>> classify_evolutionary_span("Unknown", "Homo sapiens", "Unknown")
    (0, 'Tier 0: Unknown / Unresolved Donor Lineage')
    """
    if lca == "Unknown":
        return (0, "Tier 0: Unknown / Unresolved Donor Lineage")
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
        "Archaea",
        "Bacillati",
        "Gammaproteobacteria",
        "Enterobacteriaceae",
        "Actinomycetes",
    ):
        if lca in ("Bacteria", "Archaea"):
            return (5, f"Tier 5: Deep Prokaryotic Split ({lca})")
        return (3, f"Tier 3: Intra-Phylum Bacteria ({lca})")
    if lca == "Metazoa":
        return (
            4,
            "Tier 4: Deep Metazoa / Bilateria Split (Protostomia [Worm/Fly] <-> Deuterostomia [Vertebrate])",
        )
    if lca in ("Ecdysozoa", "Arthropoda"):
        return (3, f"Tier 3: Intra-Protostomia ({lca}: Worm <-> Fly / Insect)")
    if lca in ("Dikarya", "Ascomycota", "Saccharomycotina", "Pezizomycotina"):
        is_tier3 = lca in ("Dikarya", "Ascomycota")
        return (
            3 if is_tier3 else 2,
            f"Tier {'3' if is_tier3 else '2'}: Fungal Split ({lca})",
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
        "Boreoeutheria",
        "Euarchontoglires",
        "Primates",
        "Haplorrhini",
        "Simiiformes",
        "Catarrhini",
        "Hominidae",
        "Homininae",
        "Homo",
        "Glires",
        "Rodentia",
        "Muroidea",
        "Muridae",
        "Murinae",
        "Mus",
        "Rattus",
        "Caenorhabditis",
        "Drosophila",
        "Saccharomyces",
        "Schizosaccharomyces",
        "Candida",
        "Aspergillus",
        "Arabidopsis",
        "Oryza",
        "Bacillus",
        "Mycobacterium",
        "Escherichia",
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
    tok: str,
    acc_info: Dict[str, Tuple[str, str, str, str, str, str]],
    mod_to_acc: Dict[str, str] | None = None,
) -> Tuple[str, str, str, str, str, str]:
    if ":" not in tok:
        return ("", "", tok, "", "", "")
    prefix, rest = tok.split(":", 1)
    if prefix == "PANTHER":
        return ("PTN", "PTN", tok, "", "", "")
    if mod_to_acc and tok in mod_to_acc:
        mapped_acc = mod_to_acc[tok]
        if mapped_acc in acc_info:
            tax, org, fam, sf, _sf_name, sym = acc_info[mapped_acc]
            if tax and org:
                return (tax, org, tok, fam, sf, sym)
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
            tax, org, fam, sf, _sf_name, sym = acc_info[rest]
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
    tax_lineage: Dict[str, List[str]] = dict(FALLBACK_TAXON_LINEAGES)
    for org_dir in sorted(os.listdir("genes")):
        org_path = os.path.join("genes", org_dir)
        if not os.path.isdir(org_path):
            continue
        for gene_dir in sorted(os.listdir(org_path)):
            up_path = os.path.join(org_path, gene_dir, f"{gene_dir}-uniprot.txt")
            if os.path.exists(up_path):
                taxid, _, oc_list, _, _ = read_uniprot_lineage(up_path)
                if taxid and oc_list and taxid not in tax_lineage:
                    tax_lineage[taxid] = oc_list
    return tax_lineage


def build_mod_to_acc() -> Dict[str, str]:
    mod_to_acc: Dict[str, str] = {}
    mod_species_dirs = [
        "mouse",
        "rat",
        "yeast",
        "DROME",
        "worm",
        "DANRE",
        "XENTR",
        "ARATH",
        "DICDI",
        "SCHPO",
        "CANAL",
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
    """Compute LCA name, shared depth, steps up, steps down, and total steps between two OC lineages.

    >>> compute_lineage_distance(
    ...     ["Eukaryota", "Metazoa", "Chordata", "Mammalia", "Euarchontoglires", "Rodentia"],
    ...     ["Eukaryota", "Metazoa", "Chordata", "Mammalia", "Euarchontoglires", "Primates"],
    ... )
    ('Euarchontoglires', 5, 1, 1, 2)
    >>> compute_lineage_distance(
    ...     ["Bacteria", "Pseudomonadota", "Gammaproteobacteria"],
    ...     ["Eukaryota", "Metazoa", "Chordata"],
    ... )
    ('Cellular organisms (LUCA)', 0, 3, 3, 6)
    >>> compute_lineage_distance([], ["Eukaryota", "Metazoa"])
    ('Unknown', -1, -1, -1, -1)
    """
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


def compute_mrca_lineage(lineages: List[List[str]]) -> Tuple[str, int]:
    """Compute the Most Recent Common Ancestor (MRCA) clade and depth across donor OC lineages.

    >>> compute_mrca_lineage([
    ...     ["Eukaryota", "Metazoa", "Chordata", "Mammalia", "Euarchontoglires", "Rodentia"],
    ...     ["Eukaryota", "Metazoa", "Chordata", "Mammalia", "Euarchontoglires", "Primates"],
    ... ])
    ('Euarchontoglires', 5)
    >>> compute_mrca_lineage([
    ...     ["Bacteria", "Pseudomonadota"],
    ...     ["Eukaryota", "Metazoa"],
    ... ])
    ('Cellular organisms (LUCA)', 0)
    >>> compute_mrca_lineage([["Eukaryota"], []])
    ('Unknown', -1)
    """
    if not lineages or any(not lin for lin in lineages):
        return ("Unknown", -1)
    prefix = list(lineages[0])
    for lin in lineages[1:]:
        common: List[str] = []
        for a, b in zip(prefix, lin):
            if a == b:
                common.append(a)
            else:
                break
        prefix = common
        if not prefix:
            break
    if not prefix:
        return ("Cellular organisms (LUCA)", 0)
    return (prefix[-1], len(prefix))


def canonical_seed_gene(tok: str, mod_to_acc: Dict[str, str] | None = None) -> str:
    """Return a canonical gene identifier for a WITH/FROM seed token to deduplicate dual-namespace seeds.

    >>> canonical_seed_gene("SGD:S000000001", {"SGD:S000000001": "P12345"})
    'UniProtKB:P12345'
    >>> canonical_seed_gene("UniProtKB:P12345", {"SGD:S000000001": "P12345"})
    'UniProtKB:P12345'
    """
    if mod_to_acc and tok in mod_to_acc:
        return f"UniProtKB:{mod_to_acc[tok]}"
    return tok


def classify_donor_regime(
    n_donor_taxa: int, n_distinct_donors: int, d_mrca: int, d_lca_max: int
) -> str:
    """Classify a non-self IBA row into one of the four donor-support topology regimes.

    >>> classify_donor_regime(1, 1, -1, 5)
    'R1_SINGLE_GENE'
    >>> classify_donor_regime(1, 3, -1, 5)
    'R2_MULTI_PARALOG_SINGLE_TAXON'
    >>> classify_donor_regime(2, 2, 5, 1)
    'R3_SINGLE_CLADE_JUMP'
    >>> classify_donor_regime(2, 2, 1, 5)
    'R4_BRACKETED_MULTI_SPECIES'
    >>> classify_donor_regime(2, 2, -1, 5)
    'R0_UNKNOWN_LINEAGE'
    >>> classify_donor_regime(1, 1, -1, -1)
    'R0_UNKNOWN_LINEAGE'
    """
    if d_lca_max < 0 or (n_donor_taxa >= 2 and d_mrca < 0):
        return "R0_UNKNOWN_LINEAGE"
    if n_donor_taxa == 1:
        return "R1_SINGLE_GENE" if n_distinct_donors == 1 else "R2_MULTI_PARALOG_SINGLE_TAXON"
    if d_mrca > d_lca_max:
        return "R3_SINGLE_CLADE_JUMP"
    return "R4_BRACKETED_MULTI_SPECIES"


def wilson_ci(k: int, n: int, z: float = 1.959963984540054) -> Tuple[float, float]:
    """Return 95% Wilson score confidence interval (in percentage points, 0..100) for k/n.

    >>> tuple(round(x, 1) for x in wilson_ci(50, 261))
    (14.8, 24.4)
    >>> tuple(round(x, 1) for x in wilson_ci(124, 938))
    (11.2, 15.5)
    >>> tuple(round(x, 1) for x in wilson_ci(12, 25))
    (30.0, 66.5)
    >>> tuple(round(x, 1) for x in wilson_ci(7, 34))
    (10.3, 36.8)
    >>> tuple(round(x, 1) for x in wilson_ci(17, 218))
    (4.9, 12.1)
    """
    if n <= 0:
        return (0.0, 0.0)
    p = k / n
    z2 = z * z
    denom = 1.0 + z2 / n
    center = (p + z2 / (2.0 * n)) / denom
    half = (z * ((p * (1.0 - p) / n + z2 / (4.0 * n * n)) ** 0.5)) / denom
    return (100.0 * max(0.0, center - half), 100.0 * min(1.0, center + half))


REGIME_LABELS: Dict[str, str] = {
    "R1_SINGLE_GENE": "R1: Single donor gene (1 taxon, 1 distinct seed)",
    "R2_MULTI_PARALOG_SINGLE_TAXON": "R2: Multi-paralog single taxon (1 taxon, >=2 distinct seeds)",
    "R3_SINGLE_CLADE_JUMP": "R3: Multi-species single-clade jump (>=2 taxa, d_MRCA > d_LCA)",
    "R4_BRACKETED_MULTI_SPECIES": "R4: Bracketed multi-species (>=2 taxa, d_MRCA <= d_LCA)",
    "R0_UNKNOWN_LINEAGE": "Excluded: Tier 0 / Unknown donor lineage",
}


def scan_corpus() -> Tuple[
    int,
    int,
    int,
    int,
    int,
    int,
    List[Dict[str, Any]],
    List[Dict[str, Any]],
    List[Dict[str, Any]],
    Dict[str, int],
]:
    acc_info, taxon_names = load_panther_entries()
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
                resolved = [resolve_seed(s, acc_info, mod_to_acc) for s in seeds]
                orgs = {
                    r[0]
                    for r in resolved
                    if r[0] and not r[0].startswith(("PTN", "UNRESOLVED", "OTHER"))
                }
                if len(orgs) == 1 and all(
                    r[0] and not r[0].startswith(("UNRESOLVED", "OTHER")) for r in resolved
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
                    g_res = [resolve_seed(s, acc_info, mod_to_acc) for s in g_seeds]
                    g_orgs = {
                        r[0] for r in g_res if r[0] and not r[0].startswith(("PTN", "UNRESOLVED", "OTHER"))
                    }
                    if len(g_orgs) == 1 and all(
                        r[0] and not r[0].startswith(("UNRESOLVED", "OTHER")) for r in g_res
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
    n_excluded_unresolved_1_seed = 0
    n_excluded_unresolved_multi_seed = 0
    iba_genes: Set[Tuple[str, str]] = set()
    reviewed_iba_genes: Set[Tuple[str, str]] = set()
    candidate_by_gene: Dict[Tuple[str, str], List[Dict[str, Any]]] = defaultdict(list)
    multi_donor_by_gene: Dict[Tuple[str, str], List[Dict[str, Any]]] = defaultdict(list)

    for goa_path in sorted(glob.glob("genes/*/*/*-goa.tsv")):
        parts = goa_path.split(os.sep)
        org_dir, gene_dir = parts[1], parts[2]
        has_rev = os.path.exists(
            os.path.join("genes", org_dir, gene_dir, f"{gene_dir}-ai-review.yaml")
        )
        with open(goa_path, encoding="utf-8", errors="replace") as fh:
            for line in fh:
                if "\tIBA\t" not in line:
                    continue
                c = line.rstrip("\n").split("\t")
                if len(c) < 13 or c[8] != "IBA" or "NOT" in c[3]:
                    continue
                n_iba_rows += 1
                iba_genes.add((org_dir, gene_dir))
                if has_rev:
                    reviewed_iba_genes.add((org_dir, gene_dir))
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
                n_distinct_donors = len({canonical_seed_gene(s, mod_to_acc) for s in seed_toks})
                resolved = [resolve_seed(s, acc_info, mod_to_acc) for s in seed_toks]
                donor_taxa = {
                    r[0]
                    for r in resolved
                    if r[0] and not r[0].startswith(("PTN", "UNRESOLVED", "OTHER"))
                }
                has_unresolved = any(
                    not r[0] or r[0].startswith(("UNRESOLVED", "OTHER")) for r in resolved
                )
                if has_unresolved and target_taxid not in donor_taxa:
                    if n_distinct_donors <= 1:
                        n_excluded_unresolved_1_seed += 1
                    else:
                        n_excluded_unresolved_multi_seed += 1
                if len(donor_taxa) == 1 and not has_unresolved:
                    n_single_org_leaf += 1
                    donor_tax = next(iter(donor_taxa))
                    if donor_tax != target_taxid:
                        donor_org = next(
                            (r[1] for r in resolved if r[0] == donor_tax and r[1]),
                            taxon_names.get(donor_tax, donor_tax),
                        )
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
                        paint_tax = paint_rec["taxon"] if paint_rec else None
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
                                "n_distinct_donors": n_distinct_donors,
                                "n_donor_taxa": 1,
                                "seed_toks": "|".join(seed_toks),
                                "all_with_from_toks": "|".join(tokens),
                                "donor_taxid": donor_tax,
                                "donor_org": donor_org,
                                "target_fam": target_fam,
                                "target_sf": target_sf,
                                "donor_sfs": "|".join(sorted(donor_sfs_set)),
                                "paint_taxon": paint_tax,
                                "paint_taxon_name": (
                                    PAINT_TAXON_NAMES.get(paint_tax, paint_tax)
                                    if paint_tax is not None
                                    else ""
                                ),
                            }
                        )
                elif len(donor_taxa) >= 2 and not has_unresolved and target_taxid not in donor_taxa:
                    donor_taxa_sorted = sorted(donor_taxa)
                    dt_to_org = {
                        dt: next(
                            (r[1] for r in resolved if r[0] == dt and r[1]),
                            taxon_names.get(dt, dt),
                        )
                        for dt in donor_taxa_sorted
                    }
                    donor_orgs = sorted(set(dt_to_org.values()))
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
                    donor_sfs_set = {r[4] for r in resolved if r[4]}
                    if not donor_sfs_set:
                        for tok in seed_toks:
                            acc = mod_to_acc.get(tok)
                            if acc and acc in acc_info and acc_info[acc][3]:
                                donor_sfs_set.add(acc_info[acc][3])
                    paint_tax = paint_rec["taxon"] if paint_rec else None
                    multi_donor_by_gene[(org_dir, gene_dir)].append(
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
                            "n_distinct_donors": n_distinct_donors,
                            "n_donor_taxa": len(donor_taxa_sorted),
                            "donor_taxid": "|".join(donor_taxa_sorted),
                            "donor_taxa": "|".join(donor_taxa_sorted),
                            "donor_org": "|".join(donor_orgs),
                            "donor_org_by_tax": dt_to_org,
                            "seed_toks": "|".join(seed_toks),
                            "all_with_from_toks": "|".join(tokens),
                            "target_fam": target_fam,
                            "target_sf": target_sf,
                            "donor_sfs": "|".join(sorted(donor_sfs_set)),
                            "paint_taxon": paint_tax,
                            "paint_taxon_name": (
                                PAINT_TAXON_NAMES.get(paint_tax, paint_tax)
                                if paint_tax is not None
                                else ""
                            ),
                        }
                    )

    loader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
    records: List[Dict[str, Any]] = []
    multi_donor_records: List[Dict[str, Any]] = []
    all_genes = sorted(set(candidate_by_gene.keys()) | set(multi_donor_by_gene.keys()))
    for org_dir, gene_dir in all_genes:
        rows = candidate_by_gene.get((org_dir, gene_dir), [])
        m_rows = multi_donor_by_gene.get((org_dir, gene_dir), [])
        up_path = os.path.join("genes", org_dir, gene_dir, f"{gene_dir}-uniprot.txt")
        taxid, _, oc_list, up_fam, up_sf = read_uniprot_lineage(up_path)
        if taxid and oc_list and taxid not in tax_lineage:
            tax_lineage[taxid] = oc_list

        rev_path = os.path.join("genes", org_dir, gene_dir, f"{gene_dir}-ai-review.yaml")
        rev_by_exact: Dict[Tuple[str, frozenset[str]], Dict[str, Any]] = {}
        rev_by_term: Dict[str, Dict[str, Any]] = {}
        if os.path.exists(rev_path):
            with open(rev_path, encoding="utf-8", errors="replace") as rfh:
                rdoc = yaml.load(rfh, Loader=loader) or {}
            for ann in rdoc.get("existing_annotations") or []:
                if not isinstance(ann, dict) or ann.get("retired"):
                    continue
                if ann.get("evidence_type") == "IBA":
                    tid = (ann.get("term") or {}).get("id", "")
                    supp_ents = frozenset(ann.get("supporting_entities") or [])
                    rev = ann.get("review") or {}
                    prop = ann.get("propagation_review") or rev.get("propagation_review") or {}
                    entry = {
                        "action": rev.get("action", ""),
                        "reason": (rev.get("reason") or "").replace("\n", " ").strip(),
                        "root_cause": prop.get("root_cause", ""),
                    }
                    rev_by_exact[(tid, supp_ents)] = entry
                    rev_by_term[tid] = entry

        t_lin = oc_list or tax_lineage.get(taxid, [])
        for r in rows:
            d_lin = tax_lineage.get(r["donor_taxid"], [])
            r_t_lin = t_lin or tax_lineage.get(r["target_taxid"], [])
            lca, lca_depth, steps_up, steps_down, total_steps = compute_lineage_distance(
                d_lin, r_t_lin
            )
            r["lca_clade"] = lca
            r["lca_depth"] = lca_depth
            r["steps_up"] = steps_up
            r["steps_down"] = steps_down
            r["total_tax_steps"] = total_steps
            tier, tier_label = classify_evolutionary_span(r["donor_org"], r["target_os"], lca)
            r["tier"] = tier
            r["tier_label"] = tier_label
            r["mrca_clade"] = "single_taxon"
            r["mrca_depth"] = -1
            r["regime"] = classify_donor_regime(1, r["n_distinct_donors"], -1, lca_depth)
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

            wf_key = frozenset(t for t in r["all_with_from_toks"].split("|") if t)
            if (r["go_id"], wf_key) in rev_by_exact:
                rev_info = rev_by_exact[(r["go_id"], wf_key)]
                r["match_type"] = "EXACT"
            elif r["go_id"] in rev_by_term:
                rev_info = rev_by_term[r["go_id"]]
                r["match_type"] = "TERM_FALLBACK"
            else:
                rev_info = {}
                r["match_type"] = "UNMATCHED"
            r["action"] = rev_info.get("action") or "UNREVIEWED"
            r["reason"] = rev_info.get("reason", "")
            r["root_cause"] = rev_info.get("root_cause", "")
            records.append(r)

        for mr in m_rows:
            r_t_lin = t_lin or tax_lineage.get(mr["target_taxid"], [])
            dtaxa = [dt for dt in mr["donor_taxa"].split("|") if dt]
            d_lins = [tax_lineage.get(dt, []) for dt in dtaxa]
            mrca_clade, mrca_depth = compute_mrca_lineage(d_lins)
            best_lca_depth = -1
            best_lca = "Unknown"
            best_tier = 0
            best_tier_label = "Tier 0: Unknown donor lineage"
            best_steps_up = -1
            best_steps_down = -1
            best_total_steps = -1
            dt_org_map = mr.pop("donor_org_by_tax", {})
            if r_t_lin and all(d_lins):
                best_tier = 99
                for dt, dl in zip(dtaxa, d_lins):
                    d_org = dt_org_map.get(dt, taxon_names.get(dt, dt))
                    lca, lca_depth, s_up, s_down, tot_steps = compute_lineage_distance(dl, r_t_lin)
                    tier, tier_lbl = classify_evolutionary_span(d_org, mr["target_os"], lca)
                    if lca_depth > best_lca_depth or (
                        lca_depth == best_lca_depth and tier < best_tier
                    ):
                        best_lca_depth = lca_depth
                        best_lca = lca
                        best_tier = tier
                        best_tier_label = tier_lbl
                        best_steps_up = s_up
                        best_steps_down = s_down
                        best_total_steps = tot_steps
            mr["lca_clade"] = best_lca
            mr["lca_depth"] = best_lca_depth
            mr["steps_up"] = best_steps_up
            mr["steps_down"] = best_steps_down
            mr["total_tax_steps"] = best_total_steps
            mr["tier"] = best_tier
            mr["tier_label"] = best_tier_label
            mr["mrca_clade"] = mrca_clade
            mr["mrca_depth"] = mrca_depth
            mr["regime"] = classify_donor_regime(
                mr["n_donor_taxa"], mr["n_distinct_donors"], mrca_depth, best_lca_depth
            )
            if not mr["target_fam"] and up_fam:
                mr["target_fam"] = up_fam
            if not mr["target_sf"] and up_sf:
                mr["target_sf"] = up_sf
            donor_sfs_list = [s for s in mr["donor_sfs"].split("|") if s]
            if not mr["target_sf"] or not donor_sfs_list:
                mr["sf_status"] = "UNKNOWN_SF"
            elif mr["target_sf"] in donor_sfs_list:
                mr["sf_status"] = "SAME_SF"
            else:
                mr["sf_status"] = "CROSS_SF"
            grow = graft_index.get((org_dir, gene_dir, mr["go_id"]), {})
            if grow.get("status") == "ok" and grow.get("steps_from_ibd", "").isdigit():
                mr["graft_steps_from_ibd"] = int(grow["steps_from_ibd"])
                mr["graft_dup_on_path"] = grow.get("duplication_on_path", "").lower() == "true"
            else:
                mr["graft_steps_from_ibd"] = None
                mr["graft_dup_on_path"] = None
            wf_key = frozenset(t for t in mr["all_with_from_toks"].split("|") if t)
            if (mr["go_id"], wf_key) in rev_by_exact:
                rev_info = rev_by_exact[(mr["go_id"], wf_key)]
                mr["match_type"] = "EXACT"
            elif mr["go_id"] in rev_by_term:
                rev_info = rev_by_term[mr["go_id"]]
                mr["match_type"] = "TERM_FALLBACK"
            else:
                rev_info = {}
                mr["match_type"] = "UNMATCHED"
            mr["action"] = rev_info.get("action") or "UNREVIEWED"
            mr["reason"] = rev_info.get("reason", "")
            mr["root_cause"] = rev_info.get("root_cause", "")
            multi_donor_records.append(mr)

    n_reclassified_r2_to_r1_all = sum(
        1 for r in records if r["n_seed_tokens"] > 1 and r["n_distinct_donors"] == 1
    )
    n_reclassified_r2_to_r1_rated_resolved = sum(
        1
        for r in records
        if r["n_seed_tokens"] > 1
        and r["n_distinct_donors"] == 1
        and r["action"] in (DOWNGRADE_ACTIONS | RETAIN_ACTIONS)
        and r["regime"] != "R0_UNKNOWN_LINEAGE"
    )
    diagnostics = {
        "excluded_unresolved_1_seed": n_excluded_unresolved_1_seed,
        "excluded_unresolved_multi_seed": n_excluded_unresolved_multi_seed,
        "reclassified_r2_to_r1_by_dedup_all": n_reclassified_r2_to_r1_all,
        "reclassified_r2_to_r1_by_dedup_rated_resolved": n_reclassified_r2_to_r1_rated_resolved,
    }
    return (
        n_iba_rows,
        len(iba_genes),
        len(reviewed_iba_genes),
        n_single_org_leaf,
        n_paint_rows,
        single_org_ibd,
        records,
        graft_single_org_rows,
        multi_donor_records,
        diagnostics,
    )


class RateStats(NamedTuple):
    keep: int
    fail: int
    ref: int
    rem: int
    p_fail: float
    p_ref: float
    p_down: float
    p_rem: float


def _format_rate_cols(sub: List[Dict[str, Any]]) -> RateStats:
    n = len(sub)
    if n == 0:
        return RateStats(0, 0, 0, 0, 0.0, 0.0, 0.0, 0.0)
    keep = sum(1 for r in sub if r["action"] in RETAIN_ACTIONS)
    fail = sum(1 for r in sub if r["action"] in FAILURE_ACTIONS)
    ref = sum(1 for r in sub if r["action"] in REFINEMENT_ACTIONS)
    rem = sum(1 for r in sub if r["action"] == "REMOVE")
    down = fail + ref
    return RateStats(
        keep=keep,
        fail=fail,
        ref=ref,
        rem=rem,
        p_fail=100.0 * fail / n,
        p_ref=100.0 * ref / n,
        p_down=100.0 * down / n,
        p_rem=100.0 * rem / n,
    )


def print_donor_regimes(
    records: List[Dict[str, Any]],
    multi_donor_records: List[Dict[str, Any]],
    diagnostics: Dict[str, int] | None = None,
) -> None:
    all_non_self = records + multi_donor_records
    rated_all = [r for r in all_non_self if r["action"] in (DOWNGRADE_ACTIONS | RETAIN_ACTIONS)]
    resolved_all = [r for r in rated_all if r["regime"] != "R0_UNKNOWN_LINEAGE"]
    print(
        f"\n5A. DONOR-SUPPORT TOPOLOGY REGIMES ACROSS ALL NON-SELF RESOLVED IBAs "
        f"(d_MRCA vs d_LCA, rated n={len(resolved_all):,}; total non-self={len(all_non_self):,})"
    )
    print("-" * 116)
    print(
        f"{'Donor-Support Topology Regime':<66} | {'Rated':>5} | {'Keep':>5} | {'Fail':>4} | "
        f"{'%Fail':>6} | {'Refn':>4} | {'%Refn':>6} | {'%Down':>6} | {'%REM':>5}"
    )
    print("-" * 116)
    for reg_key in (
        "R1_SINGLE_GENE",
        "R2_MULTI_PARALOG_SINGLE_TAXON",
        "R3_SINGLE_CLADE_JUMP",
        "R4_BRACKETED_MULTI_SPECIES",
    ):
        sub = [r for r in rated_all if r["regime"] == reg_key]
        keep, fail, ref, _rem, p_fail, p_ref, p_down, p_rem = _format_rate_cols(sub)
        print(
            f"{REGIME_LABELS[reg_key]:<66} | {len(sub):>5} | {keep:>5} | {fail:>4} | "
            f"{p_fail:>5.1f}% | {ref:>4} | {p_ref:>5.1f}% | {p_down:>5.1f}% | {p_rem:>4.1f}%"
        )
    unk_reg = [r for r in rated_all if r["regime"] == "R0_UNKNOWN_LINEAGE"]
    if unk_reg:
        keep, fail, ref, _rem, p_fail, p_ref, p_down, p_rem = _format_rate_cols(unk_reg)
        print(
            f"{REGIME_LABELS['R0_UNKNOWN_LINEAGE']:<66} | {len(unk_reg):>5} | {keep:>5} | "
            f"{fail:>4} | {p_fail:>5.1f}% | {ref:>4} | {p_ref:>5.1f}% | {p_down:>5.1f}% | {p_rem:>4.1f}%"
        )

    print("\n5B. DONOR-SUPPORT REGIMES BY PHYLOGENETIC DISTANCE BAND (d_LCA TIERS)")
    print("-" * 116)
    for band_label, band_tiers in [
        ("Close / Intermediate Clade (Tiers 1-2)", (1, 2)),
        ("Phylum / Bilateria Split (Tiers 3-4)", (3, 4)),
        ("Cross-Kingdom / Supergroup / LUCA (Tiers 5-7)", (5, 6, 7)),
    ]:
        print(f"  [{band_label}]")
        for reg_key in (
            "R1_SINGLE_GENE",
            "R2_MULTI_PARALOG_SINGLE_TAXON",
            "R3_SINGLE_CLADE_JUMP",
            "R4_BRACKETED_MULTI_SPECIES",
        ):
            sub = [
                r
                for r in rated_all
                if r["regime"] == reg_key and r.get("tier") in band_tiers
            ]
            if not sub:
                continue
            _keep, fail, ref, rem, p_fail, p_ref, p_down, p_rem = _format_rate_cols(sub)
            print(
                f"    {REGIME_LABELS[reg_key]:<62} | n={len(sub):>4} | Fail: {fail:>3} ({p_fail:>5.1f}%) | "
                f"Refn: {ref:>3} ({p_ref:>5.1f}%) | Down: {p_down:>5.1f}% | REM: {rem:>3} ({p_rem:>4.1f}%)"
            )

    print("\n5C. DONOR-SUPPORT REGIMES BY INDIVIDUAL PHYLOGENETIC TIER (TIERS 1-7)")
    print("-" * 116)
    for tier in range(1, 8):
        print(f"  [{TIER_NAMES[tier]}]")
        for reg_key in (
            "R1_SINGLE_GENE",
            "R2_MULTI_PARALOG_SINGLE_TAXON",
            "R3_SINGLE_CLADE_JUMP",
            "R4_BRACKETED_MULTI_SPECIES",
        ):
            sub = [
                r for r in rated_all if r["regime"] == reg_key and r.get("tier") == tier
            ]
            if not sub:
                continue
            _keep, fail, ref, rem, p_fail, p_ref, p_down, p_rem = _format_rate_cols(sub)
            print(
                f"    {REGIME_LABELS[reg_key]:<62} | n={len(sub):>4} | Fail: {fail:>3} ({p_fail:>5.1f}%) | "
                f"Refn: {ref:>3} ({p_ref:>5.1f}%) | Down: {p_down:>5.1f}% | REM: {rem:>3} ({p_rem:>4.1f}%)"
            )

    print("\n5D. DONOR-SUPPORT REGIMES CROSS-TABULATED WITH PANTHER SUBFAMILY STATUS (SAME_SF vs CROSS_SF)")
    print("-" * 116)
    for reg_key in (
        "R1_SINGLE_GENE",
        "R2_MULTI_PARALOG_SINGLE_TAXON",
        "R3_SINGLE_CLADE_JUMP",
        "R4_BRACKETED_MULTI_SPECIES",
    ):
        reg_rows = [r for r in rated_all if r["regime"] == reg_key]
        res_sf_rows = [r for r in reg_rows if r.get("sf_status") in ("SAME_SF", "CROSS_SF")]
        cov_pct = 100.0 * len(res_sf_rows) / max(1, len(reg_rows))
        print(
            f"  [{REGIME_LABELS[reg_key]} — resolved SF coverage: {len(res_sf_rows)}/{len(reg_rows)} ({cov_pct:.1f}%)]"
        )
        for sf in ("SAME_SF", "CROSS_SF", "UNKNOWN_SF"):
            sub = [r for r in reg_rows if r.get("sf_status") == sf]
            if not sub:
                continue
            _keep, fail, ref, rem, p_fail, p_ref, p_down, p_rem = _format_rate_cols(sub)
            label = f"{REGIME_LABELS[reg_key]} + {sf}"
            print(
                f"    {label:<66} | n={len(sub):>4} | Fail: {fail:>3} ({p_fail:>5.1f}%) | "
                f"Refn: {ref:>3} ({p_ref:>5.1f}%) | Down: {p_down:>5.1f}% | REM: {rem:>3} ({p_rem:>4.1f}%)"
            )
            if sf == "SAME_SF" and reg_key != "R1_SINGLE_GENE":
                same_all = [
                    r for r in sub if len([s for s in r.get("donor_sfs", "").split("|") if s]) == 1
                ]
                mixed_sf = [
                    r for r in sub if len([s for s in r.get("donor_sfs", "").split("|") if s]) > 1
                ]
                for sub_lbl, sub_rows in (
                    ("-> all resolved donors in target SF", same_all),
                    ("-> mixed donor SFs (>=1 in target SF)", mixed_sf),
                ):
                    if not sub_rows:
                        continue
                    _k, fl, rf, rm, pf, pr, pd, prm = _format_rate_cols(sub_rows)
                    ci_lo, ci_hi = wilson_ci(fl, len(sub_rows))
                    print(
                        f"      {sub_lbl:<64} | n={len(sub_rows):>4} | Fail: {fl:>3} ({pf:>5.1f}%, 95% CI {ci_lo:.1f}-{ci_hi:.1f}%) | "
                        f"Refn: {rf:>3} ({pr:>5.1f}%) | Down: {pd:>5.1f}% | REM: {rm:>3} ({prm:>4.1f}%)"
                    )

    diag = diagnostics or {}
    excl_1 = diag.get("excluded_unresolved_1_seed", 0)
    excl_m = diag.get("excluded_unresolved_multi_seed", 0)
    reclass_all = diag.get("reclassified_r2_to_r1_by_dedup_all", 0)
    reclass_rated = diag.get("reclassified_r2_to_r1_by_dedup_rated_resolved", 0)
    print("\n5E. INCLUSION & ACTION-MATCHING DIAGNOSTICS")
    print("-" * 116)
    print(
        f"  Non-self GOA IBA rows excluded due to >=1 unresolved WITH/FROM seed: "
        f"1-distinct-seed={excl_1:,}, >=2-distinct-seeds={excl_m:,} (total={excl_1 + excl_m:,})"
    )
    print(
        f"  Single-taxon rows reclassified R2 -> R1 by canonical_seed_gene deduplication: "
        f"all_non_self={reclass_all:,}, rated_resolved_lineage={reclass_rated:,}"
    )
    for reg_key in (
        "R1_SINGLE_GENE",
        "R2_MULTI_PARALOG_SINGLE_TAXON",
        "R3_SINGLE_CLADE_JUMP",
        "R4_BRACKETED_MULTI_SPECIES",
    ):
        sub = [r for r in rated_all if r["regime"] == reg_key]
        n_exact = sum(1 for r in sub if r.get("match_type") == "EXACT")
        n_fb = sum(1 for r in sub if r.get("match_type") == "TERM_FALLBACK")
        p_ex = 100.0 * n_exact / max(1, len(sub))
        print(
            f"  {REGIME_LABELS[reg_key]:<66} | Rated={len(sub):>4} | "
            f"EXACT={n_exact:>4} ({p_ex:>5.1f}%) | TERM_FALLBACK={n_fb:>4}"
        )


def print_summary(
    n_iba_rows: int,
    n_iba_genes: int,
    n_reviewed_iba_genes: int,
    n_single_org_leaf: int,
    n_paint_rows: int,
    single_org_ibd: int,
    records: List[Dict[str, Any]],
    graft_single_org_rows: List[Dict[str, Any]],
    multi_donor_records: List[Dict[str, Any]] | None = None,
    diagnostics: Dict[str, int] | None = None,
) -> None:
    rated = [r for r in records if r["action"] in (DOWNGRADE_ACTIONS | RETAIN_ACTIONS)]
    unique_genes = len({(r["org_dir"], r["gene"]) for r in records})
    n_single_seed = sum(1 for r in records if r["n_distinct_donors"] == 1)
    n_multi_seed = sum(1 for r in records if r["n_distinct_donors"] >= 2)

    print("=" * 116)
    print("SINGLE-ORGANISM IBA PHYLOGENETIC DISTANCE SUMMARY")
    print("=" * 116)
    print(
        f"Total positive GOA IBA rows scanned:                 {n_iba_rows:,} "
        f"(across {n_iba_genes:,} GOA genes; {n_reviewed_iba_genes:,} reviewed genes)"
    )
    print(
        f"Single-organism GOA IBA rows (incl. self-species):   {n_single_org_leaf:,} "
        f"({100.0 * n_single_org_leaf / max(1, n_iba_rows):.1f}%)"
    )
    print(
        f"Non-self single-organism IBA rows:                   {len(records):,} "
        f"({100.0 * len(records) / max(1, n_iba_rows):.1f}%) across {unique_genes:,} genes"
    )
    print(
        f"  - Strictly 1 distinct seed (n_distinct_donors==1): {n_single_seed:,} "
        f"({100.0 * n_single_seed / max(1, n_iba_rows):.1f}% of all IBAs)"
    )
    print(
        f"  - Multiple distinct seeds in 1 taxon (>= 2 seeds): {n_multi_seed:,} "
        f"({100.0 * n_multi_seed / max(1, n_iba_rows):.1f}% of all IBAs)"
    )
    print(f"Rated non-self single-organism IBA rows:             {len(rated):,}")
    print(
        f"Cached PAINT IBD assertions (single-taxon / total):  {single_org_ibd:,} / {n_paint_rows:,} "
        f"({100.0 * single_org_ibd / max(1, n_paint_rows):.1f}%)"
    )
    print()
    print(
        "Action groups: Keep = ACCEPT + KEEP_AS_NON_CORE | "
        "Fail (propagation failure) = REMOVE + MARK_AS_OVER_ANNOTATED | "
        "Refine (term granularity) = MODIFY + TOO_GENERAL"
    )
    print()

    print("1. REJECTION & REFINEMENT RATES BY PHYLOGENETIC DISTANCE TIER (d_LCA)")
    print("-" * 116)
    print(
        f"{'Tier':<66} | {'Rated':>5} | {'Keep':>5} | {'Fail':>4} | {'%Fail':>6} | "
        f"{'Refn':>4} | {'%Refn':>6} | {'%Down':>6} | {'%REM':>5}"
    )
    print("-" * 116)
    for tier in range(1, 8):
        sub = [r for r in rated if r["tier"] == tier]
        if not sub:
            continue
        keep, fail, ref, _rem, p_fail, p_ref, p_down, p_rem = _format_rate_cols(sub)
        print(
            f"{TIER_NAMES[tier]:<66} | {len(sub):>5} | {keep:>5} | {fail:>4} | {p_fail:>5.1f}% | "
            f"{ref:>4} | {p_ref:>5.1f}% | {p_down:>5.1f}% | {p_rem:>4.1f}%"
        )
    unk_tier = [r for r in rated if r["tier"] == 0]
    if unk_tier:
        keep, fail, ref, _rem, p_fail, p_ref, p_down, p_rem = _format_rate_cols(unk_tier)
        print(
            f"{'Excluded: Tier 0 (Unknown donor lineage)':<66} | {len(unk_tier):>5} | {keep:>5} | "
            f"{fail:>4} | {p_fail:>5.1f}% | {ref:>4} | {p_ref:>5.1f}% | {p_down:>5.1f}% | {p_rem:>4.1f}%"
        )

    print("\n1B. REJECTION & REFINEMENT RATES BY TOTAL TAXONOMIC BRANCH STEPS (steps_up + steps_down)")
    print("-" * 116)
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
        _keep, fail, ref, rem, p_fail, p_ref, p_down, p_rem = _format_rate_cols(sub)
        print(
            f"{label:<60} | n={len(sub):>4} | Fail: {fail:>3} ({p_fail:>5.1f}%) | "
            f"Refn: {ref:>3} ({p_ref:>5.1f}%) | Down: {p_down:>5.1f}% | REM: {rem:>3} ({p_rem:>4.1f}%)"
        )
    unk_steps = [r for r in rated if r["total_tax_steps"] < 0]
    if unk_steps:
        print(f"Excluded (unknown donor lineage, total_tax_steps < 0): n={len(unk_steps)}")

    close_pairs = [r for r in rated if r["lca_depth"] >= 6]
    print(
        f"\n2. EXCESS PAINT NODE DEPTH ON CLOSE TAXONOMIC PAIRS "
        f"(d_LCA >= 6, total n={len(close_pairs):,})"
    )
    print("-" * 116)
    for label, pred in [
        (
            "Scoped within clade / Vertebrata (d_PTN >= 6)",
            lambda r: r["lca_depth"] >= 6
            and r["paint_taxon"] is not None
            and PAINT_TAXON_DEPTH.get(r["paint_taxon"], -1) >= 6,
        ),
        (
            "Intermediate Metazoa / Bilateria / Chordata (2 <= d_PTN <= 5)",
            lambda r: r["lca_depth"] >= 6
            and r["paint_taxon"] is not None
            and 2 <= PAINT_TAXON_DEPTH.get(r["paint_taxon"], -1) <= 5,
        ),
        (
            "Over-deeply placed at LUCA / Eukaryota / Opisthokonta (d_PTN <= 1)",
            lambda r: r["lca_depth"] >= 6
            and r["paint_taxon"] is not None
            and 0 <= PAINT_TAXON_DEPTH.get(r["paint_taxon"], -1) <= 1,
        ),
        (
            "Unrecorded / unmapped PAINT taxon (blank 'taxon:' in *-paint.tsv)",
            lambda r: r["lca_depth"] >= 6
            and r["paint_taxon"] is not None
            and PAINT_TAXON_DEPTH.get(r["paint_taxon"], -1) < 0,
        ),
        (
            "Uncached PAINT family (no local *-paint.tsv record)",
            lambda r: r["lca_depth"] >= 6 and r["paint_taxon"] is None,
        ),
    ]:
        sub = [r for r in rated if pred(r)]
        if not sub:
            continue
        _keep, fail, ref, rem, p_fail, p_ref, p_down, p_rem = _format_rate_cols(sub)
        print(
            f"{label:<66} | n={len(sub):>4} | Fail: {fail:>3} ({p_fail:>5.1f}%) | "
            f"Refn: {ref:>3} ({p_ref:>5.1f}%) | Down: {p_down:>5.1f}% | REM: {rem:>3} ({p_rem:>4.1f}%)"
        )

    print("\n3. PANTHER SUBFAMILY CROSSING (SAME_SF vs CROSS_SF, known donor lineage)")
    print("-" * 116)
    for dist_label, dist_pred in [
        ("Close/moderate taxa (d_LCA >= 4)", lambda r: r["lca_depth"] >= 4),
        ("Distant taxa (0 <= d_LCA <= 3)", lambda r: 0 <= r["lca_depth"] <= 3),
    ]:
        for sf in ("SAME_SF", "CROSS_SF"):
            sub = [r for r in rated if dist_pred(r) and r["sf_status"] == sf]
            if not sub:
                continue
            _keep, fail, ref, rem, p_fail, p_ref, p_down, p_rem = _format_rate_cols(sub)
            label = f"{dist_label} + {sf}"
            print(
                f"{label:<60} | n={len(sub):>4} | Fail: {fail:>3} ({p_fail:>5.1f}%) | "
                f"Refn: {ref:>3} ({p_ref:>5.1f}%) | Down: {p_down:>5.1f}% | REM: {rem:>3} ({p_rem:>4.1f}%)"
            )
    unk_sf_count = sum(1 for r in rated if r["lca_depth"] >= 0 and r["sf_status"] == "UNKNOWN_SF")
    print(f"Unresolved PANTHER subfamily (UNKNOWN_SF, uncached family/seed): n={unk_sf_count}")

    print("\n4A. EXACT TREEGRAFTER TREE STEPS & DUPLICATIONS (all single-taxon IBD paths in graft_paths_all.tsv)")
    print("-" * 116)
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
        _keep, fail, ref, rem, p_fail, p_ref, p_down, p_rem = _format_rate_cols(sub)
        print(
            f"{label:<60} | n={len(sub):>4} | Fail: {fail:>3} ({p_fail:>5.1f}%) | "
            f"Refn: {ref:>3} ({p_ref:>5.1f}%) | Down: {p_down:>5.1f}% | REM: {rem:>3} ({p_rem:>4.1f}%)"
        )

    print("\n4B. EXACT TREEGRAFTER TREE STEPS & DUPLICATIONS (matched non-self GOA IBA subset)")
    print("-" * 116)
    matched_gp = [r for r in rated if r["graft_steps_from_ibd"] is not None]
    for label, pred in [
        (
            "< 10 tree steps, duplication_on_path=False",
            lambda r: r["graft_steps_from_ibd"] < 10 and not r["graft_dup_on_path"],
        ),
        (
            "< 10 tree steps, duplication_on_path=True",
            lambda r: r["graft_steps_from_ibd"] < 10 and bool(r["graft_dup_on_path"]),
        ),
        (
            ">= 10 tree steps, duplication_on_path=False",
            lambda r: r["graft_steps_from_ibd"] >= 10 and not r["graft_dup_on_path"],
        ),
        (
            ">= 10 tree steps, duplication_on_path=True",
            lambda r: r["graft_steps_from_ibd"] >= 10 and bool(r["graft_dup_on_path"]),
        ),
    ]:
        sub = [r for r in matched_gp if pred(r)]
        _keep, fail, ref, rem, p_fail, p_ref, p_down, p_rem = _format_rate_cols(sub)
        print(
            f"{label:<60} | n={len(sub):>4} | Fail: {fail:>3} ({p_fail:>5.1f}%) | "
            f"Refn: {ref:>3} ({p_ref:>5.1f}%) | Down: {p_down:>5.1f}% | REM: {rem:>3} ({p_rem:>4.1f}%)"
        )

    if multi_donor_records is not None:
        print_donor_regimes(records, multi_donor_records, diagnostics)


def print_tier_rows(records: List[Dict[str, Any]], tier: int) -> None:
    sub = [r for r in records if r["tier"] == tier]
    print(f"Rows in {TIER_NAMES.get(tier, f'Tier {tier}')}: {len(sub)}")
    for r in sub:
        ptn_tax = f" ({r['paint_taxon_name']})" if r.get("paint_taxon_name") else ""
        rc = f" | root_cause={r['root_cause']}" if r.get("root_cause") else ""
        reg = f" | regime={r['regime']}" if r.get("regime") else ""
        print(
            f"  {r['org_dir']}/{r['gene']} | {r['go_id']} ({r['go_name']}){reg} | "
            f"donor={r['donor_org']} | PTN={r['ptn_id']}{ptn_tax} | "
            f"sf={r['sf_status']} | action={r['action']}{rc}"
        )


def print_candidates(records: List[Dict[str, Any]], all_regimes: bool = False) -> None:
    keywords = (
        "do not",
        "does not",
        "lacks",
        "absent",
        "plant",
        "yeast-specific",
        "only in",
        "artifact",
        "over-annotat",
        "mislead",
        "cytosolic",
        "not directly",
        "unlike",
    )
    scope_label = "NON-SELF IBAs (ALL REGIMES R1-R4)" if all_regimes else "SINGLE-ORGANISM IBAs"
    print(f"HIGH-DISTANCE (Tier 4-7) RETAINED {scope_label} WITH SKEPTICAL REVIEW REASONS:")
    print("-" * 116)
    for r in records:
        if r["tier"] >= 4 and r["action"] in RETAIN_ACTIONS:
            reason_lower = r["reason"].lower()
            if any(k in reason_lower for k in keywords):
                ptn_tax = f" ({r['paint_taxon_name']})" if r.get("paint_taxon_name") else ""
                reg = f" | {r['regime']}" if r.get("regime") else ""
                print(
                    f"[Tier {r['tier']}{reg}] {r['org_dir']}/{r['gene']} | {r['go_id']} ({r['go_name']}) | "
                    f"donor={r['donor_org']} ({r['seed_toks']}) | PTN={r['ptn_id']}{ptn_tax} | "
                    f"action={r['action']}"
                )
                print(f"    reason: {r['reason'][:220]}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--summary", action="store_true", help="Print summary tables")
    parser.add_argument(
        "--regimes",
        action="store_true",
        help="Print donor-support topology regime comparison (R1..R4 across d_MRCA vs d_LCA)",
    )
    parser.add_argument(
        "--all-regimes",
        action="store_true",
        help="Include multi-species R3/R4 rows when running --tier, --candidates, --tsv, or --json",
    )
    parser.add_argument(
        "--tier", type=int, choices=range(0, 8), help="List rows in a specific tier (0..7)"
    )
    parser.add_argument(
        "--candidates",
        action="store_true",
        help="List high-distance retained re-review candidates",
    )
    parser.add_argument("--tsv", type=str, help="Write full per-row metrics table to TSV")
    parser.add_argument("--json", type=str, help="Write full per-row metrics table to JSON")
    args = parser.parse_args()

    if not os.path.isdir("genes") or not os.path.isdir("interpro"):
        raise SystemExit(
            "Error: single_organism_distance.py must be run from the repository root "
            "(expected 'genes/' and 'interpro/' directories)."
        )

    (
        n_iba_rows,
        n_iba_genes,
        n_reviewed_iba_genes,
        n_single_org_leaf,
        n_paint_rows,
        single_org_ibd,
        records,
        graft_single_org_rows,
        multi_donor_records,
        diagnostics,
    ) = scan_corpus()

    if args.summary or not (
        args.regimes or args.tier is not None or args.candidates or args.tsv or args.json
    ):
        print_summary(
            n_iba_rows,
            n_iba_genes,
            n_reviewed_iba_genes,
            n_single_org_leaf,
            n_paint_rows,
            single_org_ibd,
            records,
            graft_single_org_rows,
            multi_donor_records,
            diagnostics,
        )
    elif args.regimes:
        print_donor_regimes(records, multi_donor_records, diagnostics)
    active_records = (records + multi_donor_records) if args.all_regimes else records
    if args.tier is not None:
        print_tier_rows(active_records, args.tier)
    if args.candidates:
        print_candidates(active_records, all_regimes=args.all_regimes)
    if args.tsv or args.json:
        export_records = list(active_records)
        if args.tsv:
            os.makedirs(os.path.dirname(os.path.abspath(args.tsv)), exist_ok=True)
            if export_records:
                fieldnames = list(dict.fromkeys(k for r in export_records for k in r.keys()))
                with open(args.tsv, "w", encoding="utf-8", newline="") as f:
                    writer = csv.DictWriter(
                        f, fieldnames=fieldnames, delimiter="\t", extrasaction="ignore"
                    )
                    writer.writeheader()
                    writer.writerows(export_records)
            print(f"Wrote {len(export_records)} rows to {args.tsv}")
        if args.json:
            os.makedirs(os.path.dirname(os.path.abspath(args.json)), exist_ok=True)
            with open(args.json, "w", encoding="utf-8") as f:
                json.dump(export_records, f, indent=2)
            print(f"Wrote {len(export_records)} rows to {args.json}")


if __name__ == "__main__":
    main()
