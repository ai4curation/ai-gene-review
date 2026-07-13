#!/usr/bin/env python3
"""Partition the PSEPK transport/membrane/efflux functional bucket."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PARTITION_TSV = ROOT / "projects/P_PUTIDA/data/psepk_pathway_partition.tsv"
BATCH_DIR = ROOT / "projects/P_PUTIDA/batches"
OUT_TSV = BATCH_DIR / "module_transport_membrane_efflux_partition.tsv"
OUT_MD = BATCH_DIR / "module_transport_membrane_efflux_partition.md"
GENE_ROOT = ROOT / "genes/PSEPK"
SOURCE_BUCKET = "module:transport_membrane_efflux"


BUCKETS = {
    "already_promoted_or_reused_transport_context": {
        "label": "Already promoted or reused transport context",
        "module": "",
        "action": "EXISTING_OR_REUSE",
        "status": "CURATED_OR_ROUTED",
        "note": (
            "Genes already promoted into stronger non-umbrella modules during earlier "
            "curation passes, such as pilD in type-IV pilus biogenesis and tolA in "
            "the Tol-Pal envelope/division module."
        ),
    },
    "lpt_lps_transport_context": {
        "label": "Lpt/LPS envelope transport context",
        "module": "lpt_lps_transport_boundary",
        "action": "EXISTING_OR_REUSE",
        "status": "CURATED",
        "note": (
            "LptA and LptC were already fetched, Asta-backed, curated, and represented "
            "in the existing Lpt/LPS transport boundary module; keep them with that "
            "module rather than generic membrane-protein spillovers."
        ),
    },
    "tonb_exbb_exbd_energy_transduction": {
        "label": "TonB-ExbB-ExbD energy transduction",
        "module": "tonb_dependent_transport_boundary",
        "action": "COMPLETED_SUBMODULE",
        "status": "CURATED",
        "note": (
            "First-pass curation is complete for all seven TonB/ExbB/ExbD-family "
            "energy-transduction components. Existing exbB and tonB curated anchors "
            "were preserved and given Asta provenance, five missing review folders "
            "were fetched and Asta-backed, and the new TonB-dependent transport "
            "boundary module separates the canonical exbB-exbD-tonB locus from "
            "orphan TonB and ExbB/ExbD-like paralog candidates."
        ),
    },
    "tonb_dependent_outer_membrane_receptors": {
        "label": "TonB-dependent outer-membrane receptors",
        "module": "tonb_dependent_transport_boundary",
        "action": "COMPLETED_SUBMODULE",
        "status": "CURATED",
        "note": (
            "First-pass curation is complete for all 30 TonB-dependent outer-membrane "
            "receptors. The existing fpvA anchor was preserved and given Asta provenance, "
            "29 missing or initialized reviews were Asta-backed and curated, and the "
            "TonB-dependent transport boundary module now separates ferric-siderophore, "
            "CntO pseudopaline-metal, heme, B12-family, OprC copper-receptor, and "
            "generic ligand-unresolved receptor context."
        ),
    },
    "protein_export_secretion_outer_membrane_assembly": {
        "label": "Protein export, secretion, and outer-membrane assembly",
        "module": "protein_export_secretion_outer_membrane_assembly_boundary",
        "action": "COMPLETED_SUBMODULE",
        "status": "CURATED",
        "note": (
            "First-pass curation is complete for all 15 protein export, secretion, "
            "and outer-membrane assembly genes. BamA/B/D/E and the BamE-domain "
            "candidate were separated from LolA/LolB lipoprotein localization, "
            "Type-II/Type-V secretion side components, a SecYEG accessory candidate, "
            "a prepilin peptidase candidate, and HlyD-family membrane-fusion "
            "candidates whose partners and substrates remain unresolved."
        ),
    },
    "rnd_tripartite_efflux_and_mfp_omf_systems": {
        "label": "RND tripartite efflux and MFP/OMF systems",
        "module": "rnd_multidrug_efflux_boundary",
        "action": "COMPLETED_SUBMODULE",
        "status": "CURATED",
        "note": (
            "First-pass curation is complete for all 42 RND/MFP/OMF and adjacent "
            "efflux-system genes. The existing RND multidrug-efflux boundary module "
            "was extended with Czc metal-efflux loci, Mex/Opr and generic RND "
            "systems, MFS/Emr/EamA side contexts, type-I secretion and TolC-like "
            "outer-membrane components, PvdR pyoverdine export, and FieF CDF metal "
            "efflux. MFP/OMF components are modeled as component-level contributors "
            "unless substrate or partner evidence is stronger."
        ),
    },
    "mfs_drug_metabolite_transporters": {
        "label": "MFS drug/metabolite transporters",
        "module": "mfs_drug_metabolite_transport_boundary",
        "action": "COMPLETED_SUBMODULE",
        "status": "CURATED",
        "note": (
            "First-pass curation is complete for all 80 MFS drug/metabolite "
            "transport and adjacent membrane genes. Seventy-eight missing review "
            "folders were fetched and Asta-backed, pcaK and nicT curated anchors "
            "were preserved with Asta provenance, and the new MFS drug/metabolite "
            "transport boundary module separates named aromatic/carboxylate "
            "transporters, alpha-ketoglutarate/symporter/compatible-solute context, "
            "drug/xenobiotic efflux candidates, sugar/cyanate candidates, "
            "low-resolution MFS proteins, and a PP_1700 membrane-acyltransferase "
            "side node. Substrate, direction, and coupling calls stay conservative "
            "unless product, family, or prior evidence supports them."
        ),
    },
    "dmt_eama_small_drug_metabolite_transporters": {
        "label": "DMT/EamA small drug-metabolite transporters",
        "module": "dmt_eama_transport_boundary",
        "action": "COMPLETED_SUBMODULE",
        "status": "CURATED",
        "note": (
            "First-pass curation is complete for all 21 DMT/EamA/RarD/SMR-family "
            "small drug/metabolite transporter genes. All missing review folders "
            "were fetched, Asta-backed, curated, and represented in the new DMT/EamA "
            "transport boundary module, which separates SugE/EmrE SMR-family efflux "
            "candidates, RarD-like EamA permeases, amino-acid/vitamin-associated "
            "EamA candidates, diverse-substrate candidates, and generic EamA/DMT "
            "membrane permeases. emrE choline/betaine TreeGrafter rows were modified "
            "toward broader SMR-family efflux context."
        ),
    },
    "outer_membrane_porins_channels_autotransporters": {
        "label": "Outer-membrane porins, channels, and autotransporters",
        "module": "transport_envelope_spillover_boundary",
        "action": "COMPLETED_SUBMODULE",
        "status": "CURATED",
        "note": (
            "First-pass curation is complete for all 38 outer-membrane porin, "
            "channel, autotransporter, and envelope-protein genes. Thirty-three "
            "missing review folders were fetched, Asta was generated for all 38, "
            "and five curated anchors (oprE, oprF, galP, nicP, aqpZ) were preserved "
            "with added Asta provenance. The existing transport/envelope spillover "
            "module was extended with OprD/Opd substrate-selective porins, OprB "
            "carbohydrate porins, GlpF/AqpZ channels, FadL fatty-acid porin "
            "context, EstP autotransporter esterase, TamA assembly context, and "
            "low-resolution porin/outer-membrane candidates. pcaP sphingoid "
            "catabolism and oprG host-outer-membrane annotations were corrected."
        ),
    },
    "amino_acid_peptide_polyamine_abc_importers": {
        "label": "Amino-acid, peptide, and polyamine ABC importers",
        "module": "amino_acid_peptide_polyamine_abc_transport_boundary",
        "action": "COMPLETED_SUBMODULE",
        "status": "CURATED",
        "note": (
            "First-pass curation is complete for all 15 amino-acid, ectoine/"
            "osmoprotectant, and related ABC importer components. The new boundary "
            "module separates Glt/Gln-like permease/binding-protein pairs, "
            "arginine/amino-acid permeases, EhuB/EhuC/EhuD ectoine-family components, "
            "a branched-chain amino-acid membrane component, and a PP_4748-PP_4751 "
            "binding/permease/ATPase importer. PP_5024 ion-channel rows were modified "
            "toward ABC amino-acid importer context."
        ),
    },
    "metal_siderophore_anion_abc_transporters": {
        "label": "Metal, siderophore, and anion ABC transporters",
        "module": "metal_siderophore_anion_abc_transport_boundary",
        "action": "COMPLETED_SUBMODULE",
        "status": "CURATED",
        "note": (
            "First-pass curation is complete for all 11 metal, siderophore, heme, "
            "phosphate, and generic metal ABC importer components. The new module "
            "separates PP_2416/PP_2417 iron-import context, PP_2592/PP_2593/fatD "
            "ferric-siderophore import, low-resolution metal/phosphate substrate "
            "binding and ATPase context, and PP_4688/PP_4689 heme/hemin import. "
            "Siderophore-iron rows on non-siderophore-labeled permeases were "
            "broadened where appropriate."
        ),
    },
    "sugar_nucleoside_abc_transporters": {
        "label": "Sugar and nucleoside ABC transporters",
        "module": "sugar_nucleoside_abc_transport_boundary",
        "action": "COMPLETED_SUBMODULE",
        "status": "CURATED",
        "note": (
            "Singleton first-pass curation is complete for PP_1030, a low-resolution "
            "predicted sugar ABC transporter ATPase. The new boundary module keeps "
            "ATP hydrolysis as the conservative function and leaves the transported "
            "sugar, partner permease/substrate-binding proteins, and localization "
            "unresolved."
        ),
    },
    "generic_abc_transporters": {
        "label": "Generic ABC transporters",
        "module": "generic_abc_transport_boundary",
        "action": "COMPLETED_SUBMODULE",
        "status": "CURATED",
        "note": (
            "First-pass curation is complete for all 33 residual ABC-family or "
            "ABC-like transport-bucket genes. The new boundary module separates "
            "MacB/ABC-3-like efflux components, fused ABCB/type-I-exporter-like "
            "proteins, binding-protein-dependent importer pieces, sulfonate, "
            "amino-acid, cobalamin, and heme/hemin spillovers, and non-ABC outliers "
            "including PP_0386 c-di-GMP phosphodiesterase, PP_1737 MlaA-family "
            "phospholipid transfer, PP_3213 THI5-like thiamine-biosynthesis context, "
            "and rbbA ribosome-associated ATPase."
        ),
    },
    "ion_metal_transporters_and_antiporters": {
        "label": "Ion, metal, and antiporter systems",
        "module": "ion_metal_transport_boundary",
        "action": "SUBPARTITIONED",
        "status": "CURATED",
        "note": (
            "Deeper partition created in projects/P_PUTIDA/batches/"
            "module_transport_membrane_efflux_ion_metal_partition.tsv because the "
            "102-gene parent bucket mixes true cation transporters with redox, "
            "metalloenzyme, and envelope side nodes. Completed sub-splits include "
            "the 26-gene monovalent cation/potassium split in "
            "modules/monovalent_cation_antiporter_boundary.yaml, the five-gene "
            "P-type metal ATPase split in "
            "modules/p_type_metal_atpase_transport_boundary.yaml, and the "
            "three-gene chromate/fluoride/inorganic-channel split in "
            "modules/inorganic_ion_channel_resistance_boundary.yaml, and the "
            "15-gene transition-metal/Mg/Co transporter split in "
            "modules/transition_metal_magnesium_cobalt_transport_boundary.yaml. "
            "The 14-gene sodium-solute/MATE split is first-pass curated in "
            "modules/sodium_solute_symporter_mate_boundary.yaml. The 14-gene "
            "membrane metalloenzyme/envelope side-node split is first-pass curated "
            "in modules/transport_membrane_enzyme_spillover_boundary.yaml. "
            "The 25-gene membrane redox/electron-transfer spillover split is "
            "first-pass curated in modules/membrane_redox_electron_transfer_boundary.yaml. "
            "All ion/metal sub-splits are now first-pass curated."
        ),
    },
    "amino_acid_quaternary_amine_nucleobase_transporters": {
        "label": "Amino-acid, quaternary-amine, and nucleobase transporters",
        "module": "amino_acid_amine_nucleobase_transport_boundary",
        "action": "COMPLETED_SUBMODULE",
        "status": "CURATED",
        "note": (
            "First-pass curation is complete for all 55 non-ABC amino-acid, "
            "quaternary-amine, compatible-solute, nucleobase, ammonium, and urea "
            "transporter or side-node genes. The new boundary module separates "
            "GltP/YveA acidic-amino-acid symporters, APC/GabP amino-acid and "
            "amine permeases, LysE/Rht exporters, BCCT choline/betaine/carnitine "
            "transporters, NCS nucleobase/purine/xanthine/uracil permeases, "
            "Amt/Rh ammonium and urea channels, BrnQ/AzlC branched-chain "
            "transporters, PP_1060 glutamate synthase, PP_4226 Tre1-like side "
            "context, and PP_2721 low-confidence unresolved context."
        ),
    },
    "carbohydrate_nucleoside_transporters": {
        "label": "Carbohydrate and nucleoside transporters",
        "module": "carbohydrate_nucleoside_transport_boundary",
        "action": "COMPLETED_SUBMODULE",
        "status": "CURATED",
        "note": (
            "First-pass curation is complete for all 14 carbohydrate/nucleoside "
            "transport-bucket genes. The new boundary module separates GntP-family "
            "gluconate transporters, CodB/cytosine and NCS1 nucleobase permeases, "
            "PnuC nicotinamide-riboside transport, PP_1740 beta-glucanase side "
            "context, PP_3142 membrane sugar-transferase side context, PP_3048 "
            "prophage structural context, and unresolved PP_0138 SpmB/Gate-domain "
            "membrane context."
        ),
    },
    "organic_acid_aromatic_anion_transporters": {
        "label": "Organic-acid and aromatic-anion transporters",
        "module": "organic_acid_aromatic_anion_transport_boundary",
        "action": "COMPLETED_SUBMODULE",
        "status": "CURATED",
        "note": (
            "First-pass curation is complete for all seven organic-acid and "
            "aromatic-anion transporter genes. The new boundary module separates "
            "CitMHS citrate transport, BenE benzoate transporters, BhbP "
            "hydroxybutyrate/monocarboxylate context with unsupported gluconate "
            "specificity broadened, PP_3247 unresolved bile-acid/Na+ symporter-family "
            "transport context, and LldP lactate/proton symport."
        ),
    },
    "inorganic_nutrient_transporters": {
        "label": "Inorganic nutrient transporters",
        "module": "inorganic_nutrient_transport_boundary",
        "action": "COMPLETED_SUBMODULE",
        "status": "CURATED",
        "note": (
            "First-pass curation is complete for all 13 inorganic nutrient "
            "transport-bucket genes. The new boundary module separates SulP/CysZ "
            "sulfate or organosulfate transporters, YjbB/PiT phosphate transport, "
            "ModR molybdate-responsive transcription regulation, NasS nitrate-binding "
            "side context, PhoU phosphate-transport accessory/regulatory context, "
            "and unresolved PP_5475 nitrite-transporter-name-only context."
        ),
    },
    "membrane_redox_electron_transfer_proteins": {
        "label": "Membrane redox and electron-transfer proteins",
        "module": "membrane_redox_electron_transfer_boundary",
        "action": "COMPLETED_SUBMODULE",
        "status": "CURATED",
        "note": (
            "First-pass curation is complete for all 24 transport-bucket membrane "
            "redox/electron-transfer genes. The reused/extended boundary module "
            "separates DsbB/DsbD disulfide-redox proteins, thioredoxin/glutaredoxin "
            "redox proteins, Rnf/Nqr ion-translocating oxidoreductase subunits, ETF "
            "electron carriers, cytochrome bd oxidase context, qhnDH QH-AmDH context, "
            "Ccm/Cco cytochrome maturation/heme-handling context, PP_4236 DsbE/Lgt "
            "redox-lipoprotein context, and low-information membrane redox/enzyme "
            "side nodes."
        ),
    },
    "membrane_signaling_channels_c_di_gmp_spillovers": {
        "label": "Membrane signaling, channels, and c-di-GMP spillovers",
        "module": "c_di_gmp_turnover_boundary",
        "action": "COMPLETED_SUBMODULE",
        "status": "CURATED",
        "note": (
            "First-pass curation is complete for all 39 membrane signaling, channel, "
            "and c-di-GMP spillover genes. The reused/extended c-di-GMP boundary "
            "module separates EC/product/GOA-supported GGDEF diguanylate cyclases, "
            "EAL cyclic-guanylate phosphodiesterases, low-confidence CSS/PsiE/"
            "GGDEF-EAL c-di-GMP signaling candidates, MscS/MscL mechanosensitive "
            "channels, chloride/bestrophin channel candidates, FecR/ECF-sigma "
            "regulatory sensors, and low-information membrane signaling side nodes."
        ),
    },
    "envelope_polysaccharide_export_and_flippase_context": {
        "label": "Envelope polysaccharide export and flippase context",
        "module": "envelope_polysaccharide_export_boundary",
        "action": "COMPLETED_SUBMODULE",
        "status": "CURATED",
        "note": (
            "First-pass curation is complete for all 13 envelope polysaccharide "
            "export/flippase-context genes. The new boundary module separates "
            "ArnT/GtrA and bactoprenol-linked glycan transfer context, Wzz/Wzy/"
            "O-antigen and polysaccharide export context, Wzy O-antigen polymerase, "
            "and peptidoglycan or unresolved transglycosylase side nodes."
        ),
    },
    "lipoprotein_envelope_accessory_spillovers": {
        "label": "Lipoprotein and envelope accessory spillovers",
        "module": "transport_envelope_spillover_boundary",
        "action": "COMPLETED_SUBMODULE",
        "status": "CURATED",
        "note": (
            "First-pass curation is complete for all three lipoprotein/envelope "
            "accessory spillover genes. The existing transport/envelope spillover "
            "module was extended with PP_1501 as unresolved product-name-only "
            "lipoprotein context, PP_2304 as PpiD PPIase/folding-chaperone context, "
            "and csgG as CsgG curli assembly/transport component context."
        ),
    },
    "stress_resistance_membrane_spillovers": {
        "label": "Stress-resistance membrane spillovers",
        "module": "stress_detoxification_spillover_boundary",
        "action": "COMPLETED_SUBMODULE",
        "status": "CURATED",
        "note": (
            "First-pass curation is complete for all 20 stress-resistance membrane "
            "spillover genes. The existing stress/detoxification spillover module "
            "was extended with Pqi paraquat-response proteins, PP_1264 xenobiotic "
            "efflux context, TerB toxic-stress context, holin/phage release side "
            "nodes, CidA/CidB holin-regulator context, and unresolved VasX/CptA/ToxA "
            "toxin-domain membrane side nodes."
        ),
    },
    "membrane_associated_enzymes_and_side_nodes": {
        "label": "Membrane-associated enzymes and side nodes",
        "module": "transport_membrane_enzyme_spillover_boundary",
        "action": "COMPLETED_SUBMODULE",
        "status": "CURATED",
        "note": (
            "First-pass curation is complete for all 42 membrane-associated enzyme "
            "and side-node genes. The reused/extended boundary module separates "
            "membrane peptidase/protease side nodes, lipid oxidoreductase and "
            "hydroxylase candidates, acyltransferase/lipid-transfer proteins, "
            "peptidoglycan and cell-envelope glycosyltransferase side nodes, "
            "kinase/phosphatase signaling proteins, sulfatase/broad hydrolase "
            "candidates, detoxification and sulfurtransferase side nodes, "
            "secreted/toxin-associated transferase or nuclease candidates, HflK/"
            "HflC FtsH-modulator context, and low-information membrane enzyme "
            "candidates."
        ),
    },
    "other_domain_resolved_membrane_proteins": {
        "label": "Other domain-resolved membrane proteins",
        "module": "transport_membrane_domain_spillover_boundary",
        "action": "COMPLETED_SUBMODULE",
        "status": "CURATED",
        "note": (
            "First-pass curation is complete for all 83 other domain-resolved "
            "membrane proteins. The new boundary module separates TauE/TSUP "
            "transporter candidates, AI-2E/PerM and other broad permease candidates, "
            "isolated ABC permease and binding-protein side nodes, metal/TerC/GDT1/"
            "MgtC homeostasis proteins, envelope/cell-shape/curli/biofilm side "
            "nodes, cytosolic nucleic-acid/tRNA/transcription spillovers, NRPS/RHS/"
            "toxin side nodes, and DoxX/SURF1/DedA/PAP2/MAPEG or other low-information "
            "membrane-domain proteins."
        ),
    },
    "low_information_membrane_proteins": {
        "label": "Low-information membrane proteins",
        "module": "low_information_membrane_protein_boundary",
        "action": "COMPLETED_SUBMODULE",
        "status": "CURATED",
        "note": (
            "First-pass curation is complete for all 67 low-information membrane "
            "proteins. The new boundary module separates clear low-information "
            "transporter candidates, ArsB arsenical pumps, the YfdC formate/nitrite "
            "transporter-family candidate, a TonB-domain energy-transducer singleton, "
            "envelope/outer-membrane/biofilm/toxin side nodes, and domain-only "
            "membrane proteins kept unresolved."
        ),
    },
}

BUCKET_ORDER = list(BUCKETS)

FIELDS = [
    "gene",
    "ordered_locus",
    "uniprot_accession",
    "protein_name",
    "ec_numbers",
    "go_ids",
    "interpro_ids",
    "pfam_ids",
    "keywords",
    "partition_bucket",
    "partition_label",
    "proposed_module",
    "recommended_action",
    "bucket_status",
    "notes",
    "review_status",
    "curation_status",
    "asta_research_status",
]


def norm(value: str) -> str:
    return (value or "").casefold()


def ids(row: dict[str, str], field: str) -> set[str]:
    return {part.strip() for part in row.get(field, "").split(";") if part.strip()}


def has_any(text: str, terms: tuple[str, ...]) -> bool:
    lowered = norm(text)
    return any(term in lowered for term in terms)


def row_text(row: dict[str, str]) -> str:
    return " ".join(
        [
            row.get("protein_name", ""),
            row.get("keywords", ""),
            row.get("go_ids", ""),
            row.get("interpro_ids", ""),
            row.get("pfam_ids", ""),
        ]
    )


def review_status(gene: str) -> str:
    return "PRESENT" if (GENE_ROOT / gene / f"{gene}-ai-review.yaml").exists() else "MISSING"


def curation_status(gene: str) -> str:
    path = GENE_ROOT / gene / f"{gene}-ai-review.yaml"
    if not path.exists():
        return "MISSING"
    text = path.read_text(encoding="utf-8")
    if "action: PENDING" in text or "TODO: Review" in text or "TODO: Add description" in text:
        return "PENDING"
    return "CURATED"


def asta_research_status(gene: str) -> str:
    return "PRESENT" if (GENE_ROOT / gene / f"{gene}-deep-research-asta.md").exists() else "MISSING"


def assign_bucket(row: dict[str, str]) -> str:
    gene = row["suggested_review_name"]
    text = row_text(row)
    go = ids(row, "go_ids")
    interpro = ids(row, "interpro_ids")
    pfam = ids(row, "pfam_ids")
    keywords = row.get("keywords", "")

    if gene in {"pilD", "tolA"}:
        return "already_promoted_or_reused_transport_context"

    if gene in {"lptA", "lptC", "lptD", "lptE"} or has_any(text, ("lpt", "lipopolysaccharide export")):
        return "lpt_lps_transport_context"

    if gene in {"exbB", "exbD", "tonB", "PP_0696", "PP_1898", "PP_1899"} or has_any(
        text,
        ("exbb", "exbd", "protein tonb", "energy transducer tonb", "motA/tolq/exbb", "exbd/tolr"),
    ):
        return "tonb_exbb_exbd_energy_transduction"

    if (
        has_any(
            text,
            (
                "tonb-dependent",
                "tonb dependent",
                "tonb box",
                "siderophore receptor",
                "ferric siderophore receptor",
                "heme receptor",
                "b12 family",
            ),
        )
        or ({"PF07715", "PF00593"} <= pfam)
        or ({"IPR000531", "IPR012910"} <= interpro)
    ):
        return "tonb_dependent_outer_membrane_receptors"

    if (
        has_any(
            text,
            (
                "type ii secretion",
                "type i secretion",
                "secretion system",
                "general secretion",
                "secretin",
                "shlb",
                "fhac",
                "hecb",
                "twin-arginine",
                "tat ",
                " sec",
                "protein export",
                "lipoprotein-releasing",
                "outer membrane protein assembly factor",
                "prepilin",
            ),
        )
        or gene in {"bamA__Q88HI4", "bamA__Q88MH2", "bamB", "bamD", "lolB", "lolA", "yidC", "ftsY"}
        or pfam & {"PF01478", "PF12019", "PF03865", "PF08479", "PF13525", "PF13525"}
    ):
        return "protein_export_secretion_outer_membrane_assembly"

    if (
        has_any(
            text,
            (
                "resistance-nodulation",
                "rnd",
                "membrane fusion protein",
                "outer membrane efflux",
                "efflux pump",
                "multidrug efflux",
                "hlyd family secretion",
                "mex",
                "ttg",
                "tolc",
                "cobalt-zinc-cadmium resistance",
            ),
        )
        or pfam
        & {
            "PF00873",
            "PF02321",
            "PF25917",
            "PF25963",
            "PF26002",
            "PF25954",
            "PF25973",
            "PF25975",
            "PF25893",
        }
    ):
        return "rnd_tripartite_efflux_and_mfp_omf_systems"

    if (
        has_any(
            text,
            (
                "mfs",
                "major facilitator",
                "fosmidomycin efflux",
                "bcr/cfla",
                "drug resistance transporter",
            ),
        )
        or pfam & {"PF07690", "PF00083"}
        or interpro & {"IPR011701", "IPR020846"}
    ):
        return "mfs_drug_metabolite_transporters"

    if (
        has_any(text, ("porin", "outer membrane protein opr", "outer-membrane porin", "ompa", "autotransporter", "beta barrel"))
        or pfam & {"PF03573", "PF00593", "PF07396", "PF03922", "PF00691", "PF03797"}
        or go & {"GO:0015288", "GO:0009279"}
    ):
        return "outer_membrane_porins_channels_autotransporters"

    if (
        has_any(
            text,
            (
                "abc",
                "atp-binding cassette",
                "periplasmic binding protein",
                "substrate-binding",
                "transport system permease",
                "transport system atp-binding",
                "binding protein component",
                "permease component",
            ),
        )
        or pfam & {"PF00005", "PF00528", "PF00497", "PF02687", "PF12704"}
    ):
        if (
            has_any(text, ("amino acid", "peptide", "oligopeptide", "dipeptide", "polyamine", "putrescine", "spermidine", "glutathione", "opine", "branched-chain"))
            or go & {"GO:0006865", "GO:0015171", "GO:0015179", "GO:0015197"}
        ):
            return "amino_acid_peptide_polyamine_abc_importers"
        if has_any(text, ("iron", "ferric", "siderophore", "heme", "cobalt", "zinc", "molybdate", "metal", "nickel", "manganese", "phosphate", "sulfate", "phosphonate")):
            return "metal_siderophore_anion_abc_transporters"
        if has_any(text, ("sugar", "ribose", "xylose", "arabinose", "galactose", "maltose", "glucose", "carbohydrate", "nucleoside")):
            return "sugar_nucleoside_abc_transporters"
        return "generic_abc_transporters"

    if (
        pfam & {"PF00892", "PF00893"}
        or interpro & {"IPR000620", "IPR037185", "IPR000390"}
        or has_any(text, ("drug/metabolite transporter", "eamA", "rard", "suge", "guanidinium exporter"))
    ):
        return "dmt_eama_small_drug_metabolite_transporters"

    if (
        has_any(
            text,
            (
                "cobalt",
                "cadmium",
                "zinc",
                "copper",
                "cation",
                "metal",
                "magnesium",
                "potassium",
                "sodium",
                "na+/h+",
                "antiporter",
                "proton antiporter",
                "p-type",
                "ferrous",
                "manganese",
                "nickel",
                "calcium",
                "chromate transporter",
            ),
        )
        or pfam & {"PF00122", "PF01545", "PF00999", "PF01699", "PF02417"}
        or go & {"GO:0005385", "GO:0008324", "GO:0015079", "GO:0015297", "GO:0055070", "GO:0060003"}
    ):
        return "ion_metal_transporters_and_antiporters"

    if (
        has_any(
            text,
            (
                "amino acid",
                "glutamate",
                "aspartate",
                "gaba",
                "gamma-aminobutyrate",
                "choline/carnitine/betaine",
                "betaine transporter",
                "lysine",
                "arginine",
                "uracil permease",
                "ethanolamine transporter",
                "serine/threonine transporter",
                "threonine and homoserine exporter",
                "ammonium transporter",
                "urea transporter",
            ),
        )
        or pfam & {"PF00324", "PF01235", "PF02028", "PF01810", "PF00860", "PF00909", "PF03253"}
    ):
        return "amino_acid_quaternary_amine_nucleobase_transporters"

    if (
        has_any(
            text,
            (
                "sugar",
                "gluconate",
                "glucarate",
                "glycerol",
                "fructose",
                "mannose",
                "ribose",
                "xylose",
                "arabinose",
                "galactose",
                "carbohydrate",
                "nucleoside transporter",
                "nicotinamide riboside transporter",
            ),
        )
        or pfam & {"PF02447", "PF02133", "PF13520", "PF04973"}
    ):
        return "carbohydrate_nucleoside_transporters"

    if (
        has_any(
            text,
            (
                "citrate",
                "dicarboxylate",
                "tricarboxylate",
                "succinate",
                "malate",
                "lactate",
                "formate",
                "oxalate",
                "organic acid",
                "benzoate",
                "aromatic acid",
                "bile acid",
                "carboxylate",
                "acetate transporter",
            ),
        )
        or go & {"GO:0015137", "GO:0005280", "GO:0015128", "GO:0015104"}
    ):
        return "organic_acid_aromatic_anion_transporters"

    if (
        has_any(text, ("phosphate", "sulfate", "sulfonate", "taurine", "molybdate", "nitrate", "nitrite", "cyanate"))
        or pfam & {"PF00916", "PF01740", "PF02690", "PF07264"}
    ):
        return "inorganic_nutrient_transporters"

    if (
        has_any(
            text,
            (
                "cytochrome",
                "electron transport",
                "disulfide",
                "dsb",
                "thioredoxin",
                "ferredoxin",
                "oxidase",
                "respiratory",
                "quinol",
                "rnf",
                "sco1",
                "senc",
                "surF1",
                "fixh",
            ),
        )
        or go & {"GO:0009055", "GO:0020037", "GO:0015035", "GO:0017004"}
    ):
        return "membrane_redox_electron_transfer_proteins"

    if (
        has_any(text, ("diguanylate", "cyclic-guanylate", "ggdef", "eal domain", "hd-gyp", "transmembrane sensor", "signal transduction", "mechanosensitive channel", "chloride channel", "bestrophin"))
        or pfam & {"PF00563", "PF00990", "PF08447", "PF13426", "PF00924", "PF00654"}
        or go & {"GO:0071111", "GO:0043709", "GO:0052621", "GO:0008381"}
    ):
        return "membrane_signaling_channels_c_di_gmp_spillovers"

    if (
        has_any(
            text,
            (
                "wzy",
                "o-antigen",
                "exopolysaccharide",
                "polysaccharide transporter",
                "bactoprenol",
                "undecaprenyl",
                "glycosyl transferase",
                "glycosyl-transferase",
                "transglycosylase",
                "cellulose",
            ),
        )
        or pfam & {"PF02366", "PF00535", "PF04138", "PF04932", "PF02706", "PF13440", "PF04226"}
        or go & {"GO:0000030", "GO:0006493", "GO:0009103", "GO:0016757", "GO:0016763"}
    ):
        return "envelope_polysaccharide_export_and_flippase_context"

    if has_any(text, ("lipoprotein", "outer-membrane lipoprotein", "palmitate", "periplasmic folding chaperone", "ppid")) or "Lipoprotein" in keywords:
        return "lipoprotein_envelope_accessory_spillovers"

    if (
        has_any(
            text,
            (
                "paraquat",
                "tellurite",
                "terb",
                "holin",
                "immunity protein",
                "toxin",
                "phage",
                "chromate transporter",
                "acid resistance",
                "bleomycin",
            ),
        )
        or pfam & {"PF04403", "PF02470", "PF04391", "PF05106", "PF16085", "PF02417", "PF07254"}
    ):
        return "stress_resistance_membrane_spillovers"

    if (
        has_any(
            text,
            (
                "transferase",
                "protease",
                "peptidase",
                "hydrolase",
                "esterase",
                "acyltransferase",
                "desaturase",
                "phosphatase",
                "enzyme",
                "sulfatase",
                "lipase",
                "ribonuclease",
                "monooxygenase",
                "oxidoreductase",
            ),
        )
        or go & {"GO:0016787", "GO:0006508"}
    ):
        return "membrane_associated_enzymes_and_side_nodes"

    if has_any(text, ("uncharacterized", "domain-containing protein", "membrane protein", "putative membrane protein", "transmembrane-like", "duf")) or not (go or pfam or interpro):
        return "low_information_membrane_proteins"

    return "other_domain_resolved_membrane_proteins"


def make_row(source: dict[str, str], bucket_id: str) -> dict[str, str]:
    info = BUCKETS[bucket_id]
    gene = source["suggested_review_name"]
    return {
        "gene": gene,
        "ordered_locus": source["ordered_locus"],
        "uniprot_accession": source["uniprot_accession"],
        "protein_name": source["protein_name"],
        "ec_numbers": source["ec_numbers"],
        "go_ids": source["go_ids"],
        "interpro_ids": source["interpro_ids"],
        "pfam_ids": source["pfam_ids"],
        "keywords": source["keywords"],
        "partition_bucket": bucket_id,
        "partition_label": info["label"],
        "proposed_module": info["module"],
        "recommended_action": info["action"],
        "bucket_status": info["status"],
        "notes": info["note"],
        "review_status": review_status(gene),
        "curation_status": curation_status(gene),
        "asta_research_status": asta_research_status(gene),
    }


def write_rows(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def write_batch_md(path: Path, title: str, rows: list[dict[str, str]], note: str) -> None:
    lines = [
        "---",
        f'title: "{title}"',
        "maturity: DRAFT",
        "tags: [BIOLOGY_DOMAIN, PIPELINE]",
        "species: [PSEPK]",
        "autolink_gene_symbols: false",
        "---",
        "",
        f"# {title}",
        "",
        note,
        "",
        "| Gene | Ordered locus | UniProt | Protein | Review | Asta |",
        "|---|---|---|---|---|---|",
    ]
    for row in rows:
        lines.append(
            f"| `{row['gene']}` | `{row['ordered_locus']}` | `{row['uniprot_accession']}` | "
            f"{row['protein_name']} | {row['curation_status']} | {row['asta_research_status']} |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    source_rows = [
        row
        for row in csv.DictReader(PARTITION_TSV.open(encoding="utf-8"), delimiter="\t")
        if row["primary_bucket_id"] == SOURCE_BUCKET
    ]
    if not source_rows:
        raise SystemExit(f"No rows found for {SOURCE_BUCKET}")

    rows = [make_row(source, assign_bucket(source)) for source in source_rows]
    if len({row["gene"] for row in rows}) != len(rows):
        raise SystemExit("Duplicate gene rows in partition output")

    write_rows(OUT_TSV, rows)

    by_bucket: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_bucket[row["partition_bucket"]].append(row)

    counts = Counter(row["partition_bucket"] for row in rows)
    examples: dict[str, list[str]] = defaultdict(list)
    for row in rows:
        if len(examples[row["partition_bucket"]]) < 8:
            examples[row["partition_bucket"]].append(row["gene"])

    lines = [
        "---",
        'title: "PSEPK transport/membrane/efflux functional-bucket partition"',
        "maturity: DRAFT",
        "tags: [BIOLOGY_DOMAIN, PIPELINE]",
        "species: [PSEPK]",
        "autolink_gene_symbols: false",
        "---",
        "",
        "# PSEPK transport/membrane/efflux functional-bucket partition",
        "",
        "The `module:transport_membrane_efflux` bucket is a large UniProt",
        "name/keyword umbrella. It mixes transport systems, outer-membrane",
        "receptors and porins, secretion/export components, efflux pumps, ion",
        "homeostasis proteins, redox membrane proteins, envelope-polysaccharide",
        "context, signaling channels, and low-information membrane proteins. It",
        "is not satisfiable as one biological module.",
        "",
        "## Outputs",
        "",
        f"- Source table: `{PARTITION_TSV.relative_to(ROOT)}`",
        f"- Full partition table: `{OUT_TSV.relative_to(ROOT)}`",
        "",
        "## Partition Summary",
        "",
        "| Bucket | Genes | Proposed module | Action | Status | Example genes |",
        "|---|---:|---|---|---|---|",
    ]
    for bucket_id in BUCKET_ORDER:
        info = BUCKETS[bucket_id]
        module = info["module"] or "(none)"
        example_text = ", ".join(f"`{gene}`" for gene in examples[bucket_id])
        lines.append(
            f"| `{bucket_id}` | {counts[bucket_id]} | `{module}` | "
            f"{info['action']} | {info['status']} | {example_text} |"
        )

    lines.extend(
        [
            "",
            "## Working Decisions",
            "",
            "- Do not curate the 779-gene transport/membrane/efflux bucket as one module.",
            "- Prioritize system-resolved transport families first: TonB-dependent uptake,",
            "  RND tripartite efflux, ABC import/export components, MFS/DMT transporters,",
            "  and ion/metal antiporters.",
            "- Reuse existing modules when a row is clearly a missing member of a prior",
            "  pathway boundary, such as Lpt/LPS transport, protein export/secretion,",
            "  c-di-GMP turnover, stress/detoxification, or transport-envelope spillovers.",
            "- Keep substrate claims conservative for generic permeases; product names and",
            "  domain families are often sufficient for a transport-family core function",
            "  but not for a specific solute.",
            "- Treat low-information membrane proteins as a last-pass unresolved bucket.",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")

    for bucket_id in BUCKET_ORDER:
        info = BUCKETS[bucket_id]
        bucket_rows = by_bucket[bucket_id]
        stem = f"module_transport_membrane_efflux_{bucket_id}"
        write_rows(BATCH_DIR / f"{stem}.tsv", bucket_rows)
        write_batch_md(
            BATCH_DIR / f"{stem}.md",
            f"PSEPK transport/membrane/efflux: {info['label']}",
            bucket_rows,
            info["note"],
        )

    print(f"Wrote {OUT_TSV.relative_to(ROOT)} with {len(rows)} rows")
    for bucket_id in BUCKET_ORDER:
        print(f"{bucket_id}: {counts[bucket_id]}")


if __name__ == "__main__":
    main()
