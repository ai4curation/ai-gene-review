#!/usr/bin/env python3
"""Build a pathway/module worklist for the PSEPK curation project."""

from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

import yaml


DEFAULT_PROJECT_DIR = Path("projects/P_PUTIDA")
_PSEPK_REVIEW_INDEX: tuple[dict[str, Path], dict[str, Path]] | None = None
MODULE_MAP = {
    "module:cell_envelope_division": {
        "module": "",
        "module_file": "",
        "scope_note": (
            "Partitioned functional bucket: PSEPK cell-envelope/division contains "
            "98 primary genes from UniProt name/keyword assignment. The set mixes "
            "Lpt/LPS outer-membrane assembly, LPS-core and lipid-A biosynthesis "
            "context, peptidoglycan turnover/remodeling, cell-division regulatory "
            "spillovers, VacJ/MlaA phospholipid-asymmetry context, ApbE-like "
            "envelope flavinylation, outer-membrane barrels/channels/autotransporters, "
            "named outer-membrane lipoprotein families, domain-resolved lipoprotein "
            "spillovers, and generic lipoprotein/signal-peptide spillovers. LptD/LptE "
            "are already curated in modules/lpt_lps_transport_boundary.yaml; "
            "PP_3016 and PP_3134 are first-pass curated and represented in "
            "modules/lipopolysaccharide_biosynthesis.yaml, while maa is first-pass "
            "curated and routed out as a maltose O-acetyltransferase lipid-A-keyword "
            "spillover. The sulA/PP_2199/PP_2352 cell-division regulatory "
            "spillover split is first-pass curated and represented in "
            "modules/divisome_z_ring_septation_boundary.yaml. The vacJ "
            "phospholipid-asymmetry singleton is first-pass curated and represented "
            "in modules/mla_phospholipid_transport_boundary.yaml. The PP_2150 "
            "ApbE/FMNylylation singleton is first-pass curated and represented in "
            "modules/ccm_heme_export_cytochrome_c_maturation_boundary.yaml as "
            "related envelope flavoprotein maturation context. The 11-gene "
            "peptidoglycan turnover/remodeling split is first-pass curated and "
            "represented in modules/peptidoglycan_biosynthesis.yaml. The 8-gene "
            "outer-membrane barrel/channel/autotransporter split is first-pass "
            "curated and represented in "
            "modules/transport_envelope_spillover_boundary.yaml. The 9-gene "
            "named outer-membrane lipoprotein-family split is also first-pass "
            "curated and represented in "
            "modules/transport_envelope_spillover_boundary.yaml. The 30-gene "
            "domain-resolved lipoprotein split is now first-pass curated and "
            "represented in modules/transport_envelope_spillover_boundary.yaml "
            "as mostly broad membrane/envelope context, with sharper "
            "desiccation-response, peptidase, peptidase-inhibitor, and "
            "heme-binding candidates retained where supported. The 30-gene "
            "generic lipoprotein/signal-peptide split is also first-pass "
            "curated and represented in modules/transport_envelope_spillover_boundary.yaml "
            "as low-information broad membrane/envelope context only. Use "
            "projects/P_PUTIDA/batches/module_cell_envelope_division_partition.tsv "
            "for the complete partition ledger."
        ),
        "priority_phase": "9",
        "batch_status": "PARTITIONED",
    },
    "module:stress_detoxification": {
        "module": "",
        "module_file": "",
        "scope_note": (
            "Partitioned functional bucket: PSEPK stress/detoxification contains "
            "52 primary genes from UniProt name/keyword assignment. The set mixes "
            "peroxide/peroxiredoxin detoxification enzymes, glutathione/thiol "
            "detoxification candidates, arsenic/copper resistance proteins, "
            "universal-stress-protein candidates, cold/heat-shock proteins, "
            "ThiJ/DJ-1/PfpI candidates, and miscellaneous regulatory or "
            "low-information stress-induced proteins. The 10-gene "
            "peroxide/peroxiredoxin split is first-pass curated and represented "
            "in modules/oxidative_stress_peroxide_detoxification_boundary.yaml. "
            "The 7-gene glutathione/thiol detoxification split is first-pass "
            "curated and represented as side context in "
            "modules/glutathione_metabolism_boundary.yaml. The 8-gene "
            "arsenic/copper metal-resistance split is first-pass curated and "
            "represented in modules/metal_resistance_detoxification_boundary.yaml. "
            "The 11-gene universal-stress-protein split is first-pass curated "
            "and represented in modules/universal_stress_protein_boundary.yaml. "
            "The 5-gene cold/heat-shock spillover split is first-pass curated "
            "and represented as bacterial cold-shock and HSP20 holdase side "
            "context in modules/integrated_stress_response_boundary.yaml. "
            "The 3-gene ThiJ/DJ-1/PfpI split is first-pass curated and "
            "represented in modules/stress_detoxification_spillover_boundary.yaml "
            "as HSP31-like glyoxalase III/methylglyoxal-detoxification context. "
            "The final 8-gene stress-regulatory/miscellaneous spillover split is "
            "first-pass curated and represented in "
            "modules/stress_detoxification_spillover_boundary.yaml as SrkA/OxyR "
            "regulatory context, Dps DNA/ferroxidase context, PaaY phenylacetate-route "
            "thioesterase context, PP_3509 bleomycin-response context, and three "
            "low-information KGG-repeat unknowns. "
            "Use projects/P_PUTIDA/batches/module_stress_detoxification_partition.tsv "
            "for the complete partition ledger."
        ),
        "priority_phase": "9",
        "batch_status": "PARTITIONED",
    },
    "module:transport_membrane_efflux": {
        "module": "",
        "module_file": "",
        "scope_note": (
            "Partitioned functional bucket: PSEPK transport/membrane/efflux contains "
            "779 primary genes from UniProt name/keyword assignment. The set mixes "
            "transport systems, TonB-dependent uptake, outer-membrane receptors and "
            "porins, secretion/export components, RND/MFS/DMT/ABC transporters, ion "
            "homeostasis proteins, redox membrane proteins, envelope-polysaccharide "
            "context, signaling channels, and low-information membrane proteins. The "
            "bucket is not one satisfiable module. The partition currently splits it "
            "into 26 curation-scale rows. LptA/LptC are already curated and represented "
            "in modules/lpt_lps_transport_boundary.yaml. The 7-gene "
            "TonB-ExbB-ExbD energy-transduction split is first-pass curated and "
            "represented in modules/tonb_dependent_transport_boundary.yaml, preserving "
            "exbB and tonB anchors, adding Asta provenance, fetching and curating "
            "PP_0696, PP_1512, PP_1898, PP_1899, and exbD. The 30-gene "
            "TonB-dependent receptor panel is also first-pass curated in the same "
            "module, preserving fpvA as the ferripyoverdine anchor and separating "
            "ferric-siderophore, CntO pseudopaline-metal, heme, B12-family, OprC "
            "copper-receptor, and generic ligand-unresolved receptors. TonB/receptor "
            "pairing remains unresolved. The 15-gene protein export, secretion, and "
            "outer-membrane assembly split is first-pass curated and represented in "
            "modules/protein_export_secretion_outer_membrane_assembly_boundary.yaml, "
            "separating Bam, Lol, Type-II/Type-V/Sec/prepilin side components, and "
            "HlyD-family MFP candidates with unresolved partners and substrates. "
            "The 42-gene RND tripartite efflux and MFP/OMF split is first-pass "
            "curated and represented in modules/rnd_multidrug_efflux_boundary.yaml, "
            "separating Czc metal-efflux loci, Mex/Opr and generic RND systems, "
            "MFS/Emr/EamA side contexts, type-I secretion and TolC-like components, "
            "PvdR pyoverdine export, and FieF CDF metal efflux. The 80-gene MFS "
            "drug/metabolite transporter split is first-pass curated and represented "
            "in modules/mfs_drug_metabolite_transport_boundary.yaml, preserving pcaK "
            "and nicT anchors, separating named aromatic/carboxylate carriers, "
            "alpha-ketoglutarate/symporter/compatible-solute candidates, "
            "Bcr/CmlA/EmrB/QacA/fosmidomycin/xenobiotic-efflux MFS carriers, "
            "sugar/cyanate candidates, low-resolution MFS proteins, and PP_1700 "
            "acyltransferase side context. The 21-gene DMT/EamA small "
            "drug/metabolite transporter split is first-pass curated and represented "
            "in modules/dmt_eama_transport_boundary.yaml, separating SugE/EmrE "
            "SMR-family efflux candidates, RarD-like EamA permeases, amino-acid/"
            "vitamin-associated EamA candidates, diverse-substrate candidates, and "
            "generic EamA/DMT membrane permeases. The 38-gene outer-membrane "
            "porin/channel/autotransporter split is first-pass curated and extends "
            "modules/transport_envelope_spillover_boundary.yaml with OprD/Opd "
            "substrate-selective porins, OprB carbohydrate porins, GlpF/AqpZ "
            "channels, FadL fatty-acid porin context, EstP autotransporter "
            "esterase, TamA assembly context, and low-resolution porin or "
            "outer-membrane candidates. The 15-gene amino-acid/peptide/polyamine "
            "ABC importer split is first-pass curated in modules/"
            "amino_acid_peptide_polyamine_abc_transport_boundary.yaml, separating "
            "Glt/Gln-like, arginine/amino-acid, Ehu ectoine-family, branched-chain, "
            "and PP_4748-PP_4751 importer components. The 11-gene metal/"
            "siderophore/anion ABC transporter split is first-pass curated in "
            "modules/metal_siderophore_anion_abc_transport_boundary.yaml, separating "
            "iron, ferric-siderophore, generic metal/phosphate, and heme/hemin "
            "importer contexts. The singleton sugar/nucleoside ABC transporter split "
            "is first-pass curated in modules/sugar_nucleoside_abc_transport_boundary.yaml "
            "as low-resolution PP_1030 sugar ABC ATPase context. The 33-gene generic "
            "ABC residual split is first-pass curated in modules/"
            "generic_abc_transport_boundary.yaml, separating MacB/ABC-3-like, fused "
            "ABCB/type-I-exporter-like, binding-protein-dependent, sulfonate, amino-acid, "
            "cobalamin, heme/hemin, and non-ABC outlier contexts. The 102-gene "
            "ion/metal transporter parent split has been subpartitioned because it "
            "mixes true cation-homeostasis systems with redox, metalloenzyme, and "
            "envelope side nodes; the 26-gene monovalent cation/potassium-system "
            "sub-split is first-pass curated in modules/"
            "monovalent_cation_antiporter_boundary.yaml, separating Trk/Kup, NhaA/"
            "NhaB/NhaP, Kef, Mrp, K/Na/Ca exchanger, potassium-channel, NhaC-like, "
            "and DASS-related side contexts. The five-gene P-type metal ATPase "
            "sub-split is first-pass curated in modules/"
            "p_type_metal_atpase_transport_boundary.yaml, separating zinc/cadmium "
            "CadA-family ATPases, copper ATPase context, MgtA magnesium import, "
            "and an unresolved type-IB cation ATPase candidate. The three-gene "
            "chromate/fluoride/inorganic-channel sub-split is first-pass curated "
            "in modules/inorganic_ion_channel_resistance_boundary.yaml, separating "
            "CHR-family chromate transport, reviewed FluC fluoride detoxification, "
            "and an HlyIII-family pore-forming candidate. The 15-gene transition-"
            "metal/Mg/Co transporter sub-split is first-pass curated in modules/"
            "transition_metal_magnesium_cobalt_transport_boundary.yaml, separating "
            "CDF/ZIP zinc and mixed-metal transporters, CbiM/CbtA cobalt components, "
            "CorA/MgtE magnesium-cobalt transporters, NiCoT/Rcn nickel-cobalt efflux/"
            "response context, and CorC/CNNM-UPF0053 low-resolution metal-transporter "
            "candidates. The 14-gene sodium-solute/MATE sub-split is first-pass "
            "curated in modules/sodium_solute_symporter_mate_boundary.yaml, "
            "separating AGCS amino-acid:sodium symporters, GltS, ArcD, ActP, "
            "PutP, TcyP, MATE xenobiotic efflux, broad SSF candidates, and PP_0670 "
            "ACR3 arsenical-resistance context. The 14-gene membrane metalloenzyme/"
            "envelope side-node sub-split is first-pass curated in modules/"
            "transport_membrane_enzyme_spillover_boundary.yaml, keeping proteases, "
            "glycosylation/lipid side nodes, TamB, CopD, and CycZ-like context out "
            "of ion-transport assertions. The 25-gene membrane redox/electron-transfer "
            "spillover sub-split is first-pass curated in modules/"
            "membrane_redox_electron_transfer_boundary.yaml, separating cytochromes, "
            "ferredoxins/iron-sulfur proteins, Ccm proteins, Hmp/MsrQ detoxification "
            "or repair nodes, CumA/azurin, and the OFeT/FTR1-like iron transporter. "
            "All ion/metal sub-splits are now first-pass curated. The 55-gene "
            "non-ABC amino-acid/quaternary-amine/nucleobase transporter split is "
            "first-pass curated in modules/"
            "amino_acid_amine_nucleobase_transport_boundary.yaml, separating "
            "GltP/YveA acidic-amino-acid symporters, APC/GabP permeases, "
            "LysE/Rht exporters, BCCT compatible-solute transporters, NCS "
            "nucleobase/purine/xanthine/uracil permeases, Amt/Rh ammonium/urea "
            "channels, BrnQ/AzlC branched-chain transporters, and enzyme or "
            "low-confidence side nodes. The 14-gene carbohydrate/nucleoside "
            "transport split is first-pass curated in modules/"
            "carbohydrate_nucleoside_transport_boundary.yaml, separating GntP "
            "gluconate transporters, CodB/NCS1 nucleobase or cytosine permeases, "
            "PnuC nicotinamide-riboside transport, beta-glucanase and "
            "sugar-transferase side nodes, prophage structural context, and an "
            "unresolved SpmB/Gate-domain membrane protein. The seven-gene "
            "organic-acid/aromatic-anion transport split is first-pass curated in "
            "modules/organic_acid_aromatic_anion_transport_boundary.yaml, separating "
            "CitMHS citrate transport, BenE benzoate transport, BhbP broad "
            "monocarboxylate context, unresolved bile-acid/Na+-symporter-family "
            "context, and LldP lactate/proton symport. The 13-gene inorganic "
            "nutrient transport split is first-pass curated in modules/"
            "inorganic_nutrient_transport_boundary.yaml, separating SulP/CysZ "
            "sulfate or organosulfate transporters, YjbB/PiT phosphate transport, "
            "ModR molybdate-responsive transcription regulation, NasS nitrate-binding "
            "side context, PhoU phosphate-transport accessory/regulatory context, "
            "and unresolved PP_5475 nitrite-transporter-name-only context. The "
            "3-gene lipoprotein/envelope accessory spillover split is first-pass "
            "curated in modules/transport_envelope_spillover_boundary.yaml, with "
            "PP_1501 left as unresolved lipoprotein context, PP_2304 treated as "
            "PpiD PPIase/folding-chaperone context, and csgG treated as CsgG curli "
            "assembly/transport context. The 13-gene envelope-polysaccharide export "
            "and flippase-context split is first-pass curated in modules/"
            "envelope_polysaccharide_export_boundary.yaml, separating ArnT/GtrA "
            "and bactoprenol-linked glycan transfer context, Wzz/Wzy/O-antigen "
            "and polysaccharide export context, Wzy O-antigen polymerase, and "
            "peptidoglycan or unresolved transglycosylase side nodes. The 20-gene "
            "stress-resistance membrane spillover split is first-pass curated by "
            "extending modules/stress_detoxification_spillover_boundary.yaml with "
            "Pqi paraquat-response proteins, PP_1264 xenobiotic-efflux context, "
            "TerB toxic-stress context, holin/phage release side nodes, CidA/CidB "
            "holin-regulator context, and unresolved VasX/CptA/ToxA toxin-domain "
            "membrane side nodes. The 24-gene transport-bucket membrane redox/"
            "electron-transfer split is first-pass curated by extending modules/"
            "membrane_redox_electron_transfer_boundary.yaml with DsbB/DsbD, "
            "thioredoxin/glutaredoxin, Rnf/Nqr, ETF, cytochrome bd, qhnDH, Ccm/Cco, "
            "DsbE/Lgt, and low-information membrane redox/enzyme side contexts. "
            "The 39-gene membrane signaling/channels/c-di-GMP spillover split is "
            "first-pass curated by extending modules/c_di_gmp_turnover_boundary.yaml "
            "with GGDEF diguanylate cyclases, EAL cyclic-guanylate phosphodiesterases, "
            "low-confidence CSS/PsiE/GGDEF-EAL c-di-GMP candidates, MscS/MscL "
            "mechanosensitive channels, chloride/bestrophin channels, FecR/ECF-sigma "
            "regulatory sensors, and low-information membrane signaling side nodes. "
            "The 42-gene membrane-associated enzyme side-node split is first-pass "
            "curated by extending modules/transport_membrane_enzyme_spillover_boundary.yaml "
            "with membrane peptidases/proteases, lipid oxidoreductases, acyltransferase/"
            "lipid-transfer proteins, cell-envelope glycosyltransferases, kinase/"
            "phosphatase signaling proteins, sulfatase/hydrolase candidates, "
            "detoxification/sulfurtransferase side nodes, toxin-associated nuclease/"
            "transferase context, HflK/HflC protease modulators, and low-information "
            "membrane enzyme candidates. The 83-gene other domain-resolved membrane "
            "protein split is first-pass curated in modules/"
            "transport_membrane_domain_spillover_boundary.yaml, separating TauE/TSUP, "
            "AI-2E/PerM, DctM/TRAP, CstA, MMPL, FUSC, and other broad transporter "
            "candidates from isolated ABC permease/binding-protein side nodes, "
            "metal/TerC/GDT1/MgtC homeostasis proteins, envelope/cell-shape/curli/"
            "biofilm side nodes, cytosolic nucleic-acid/tRNA/transcription spillovers, "
            "NRPS/RHS/toxin side nodes, and low-information DoxX/SURF1/DedA/PAP2/"
            "MAPEG membrane-domain proteins. The 67-gene low-information membrane "
            "protein split is first-pass curated in modules/"
            "low_information_membrane_protein_boundary.yaml, separating clear "
            "low-information transporter candidates, ArsB arsenical pumps, YfdC "
            "formate/nitrite transporter context, a TonB-domain energy-transducer "
            "singleton, envelope/outer-membrane/biofilm/toxin side nodes, and "
            "domain-only membrane proteins left unresolved. All transport/membrane/"
            "efflux sub-splits are now first-pass curated. "
            "Use projects/P_PUTIDA/batches/module_transport_membrane_efflux_partition.tsv "
            "for the complete partition ledger."
        ),
        "priority_phase": "10",
        "batch_status": "PARTITIONED",
    },
    "module:regulation_signal_transduction": {
        "module": "",
        "module_file": "",
        "scope_note": (
            "Partitioned functional bucket: PSEPK regulation/signal transduction contains "
            "387 primary genes from UniProt name/domain assignment. The set is dominated "
            "by transcription-factor family expansions plus two-component proteins, sigma "
            "factors, phage/toxin-antitoxin regulators, and low-information DNA-binding "
            "spillovers. The bucket is not one satisfiable pathway. The partition splits "
            "it into LysR, AraC/XylS, GntR, TetR/AcrR, small-family metabolic regulators, "
            "MerR/ArsR/MarR metal-redox-stress regulators, two-component sensors/response "
            "regulators, XRE/Cro/phage/toxin-antitoxin regulators, sigma-54 enhancer-binding "
            "regulators, ECF/sigma/anti-sigma factors, and low-information/named transcriptional "
            "regulators. The 21-gene small-family metabolic-regulator split is first-pass "
            "curated and represented in modules/metabolic_transcriptional_regulator_boundary.yaml. "
            "The 16-gene sigma/anti-sigma split is first-pass curated and represented "
            "in modules/sigma_anti_sigma_regulation_boundary.yaml. "
            "The 16-gene sigma-54/LuxR split is first-pass curated and represented "
            "in modules/sigma54_enhancer_binding_regulator_boundary.yaml. "
            "The 25-gene TetR/AcrR split is first-pass curated and represented "
            "in modules/tetr_acrr_transcriptional_regulator_boundary.yaml, preserving "
            "ttgR and PP_2144 as stronger named/curator-supported cases while keeping "
            "generic TetR paralog regulons unresolved and PP_2597 no-core unresolved. "
            "The 25-gene MerR/ArsR/MarR metal-redox-stress split is first-pass curated "
            "and represented in modules/metal_redox_stress_transcription_regulator_boundary.yaml, "
            "preserving arsR1/arsR2 as named arsenite-responsive regulators, keeping soxR "
            "as redox-sensitive SoxR-like context, and leaving five weak no-GOA product-name-only "
            "records no-core unresolved. "
            "The 28-gene XRE/Cro/phage/toxin-antitoxin split is first-pass curated "
            "and represented in modules/phage_regulation_toxin_antitoxin_boundary.yaml, "
            "with MqsRA/HigA, LexA-like, Cro/C1-cupin, simple Cro/C1, and non-phage "
            "spillover groups separated and PP_5680 retained as no-core unresolved. "
            "The 29-gene GntR-family split is first-pass curated and represented "
            "in modules/gntr_transcriptional_regulator_boundary.yaml, separating "
            "FadR/GntR C-terminal, UTRA/HutC-like, and PLP/aminotransferase-domain "
            "regulator candidates while leaving regulons, effectors, regulatory "
            "direction, and PLP-domain substrate chemistry unresolved. "
            "The 40-gene AraC/XylS-family split is first-pass curated and represented "
            "in modules/arac_xyls_transcriptional_regulator_boundary.yaml, preserving "
            "existing ada and BenR anchor reviews, separating named, DJ-1/PfpI or "
            "INH-QAR, RmlC/cupin, arabinose-binding-domain, and other sensor-domain "
            "regulator candidates, and leaving regulons, effectors, regulatory "
            "direction, and PP_4602 kinase side context unresolved unless "
            "gene-specific evidence supports them. "
            "The 32-gene low-information/named transcription-regulator split is "
            "first-pass curated and represented in "
            "modules/transcriptional_regulator_spillover_boundary.yaml, preserving "
            "HexR as a curated anchor, adding conservative missing transcription-regulator "
            "molecular-function rows only where product/domain evidence supports them, "
            "and retaining PP_1762, PP_2738, PP_4528, PP_5232, and PP_5343 as no-core "
            "unresolved records. "
            "The 48-gene two-component sensor/response-regulator split is first-pass "
            "curated and represented as an extension to "
            "modules/orphan_two_component_regulators_boundary.yaml, preserving colR "
            "as a curated ColRS anchor while grouping generic histidine kinases, "
            "DNA-binding response regulators, and receiver-only/noncanonical response "
            "regulators without inferring cues, regulons, transporter outputs, or "
            "HD-GYP/cyclic-di-GMP activities beyond supported side context. "
            "The 107-gene LysR-family split is first-pass curated and represented "
            "in modules/lysr_transcriptional_regulator_boundary.yaml, preserving "
            "pcaQ, galR, and catR as stronger curated anchor reviews, adding "
            "Asta provenance to those anchors, curating 104 newly fetched reviews "
            "to family-level DNA-binding transcription-regulator functions, and "
            "treating direct pathway-process annotations on regulator genes as "
            "pathway-association over-annotation unless gene-specific activator "
            "evidence supports positive transcription regulation. "
            "Use projects/P_PUTIDA/batches/module_regulation_signal_transduction_partition.tsv "
            "for the complete partition ledger; all regulation/signal-transduction "
            "split rows are now first-pass curated."
        ),
        "priority_phase": "9",
        "batch_status": "PARTITIONED",
    },
    "module:chromosome_partition_cell_cycle": {
        "module": "",
        "module_file": "",
        "scope_note": (
            "Partitioned functional bucket: PSEPK chromosome/cell-cycle contains "
            "37 primary genes from UniProt name/keyword assignment. The set mixes "
            "chromosome partition/condensation proteins, Xer/FtsK chromosome "
            "dimer resolution and DNA translocation, divisome/Z-ring/septation "
            "components, MinCDE septum-site selection, Tol-Pal envelope/division "
            "coordination, and broad keyword spillovers PP_1105 and tig. The "
            "MinCDE septum-site-selection sub-batch is first-pass curated and "
            "represented by modules/min_system_septum_site_selection_boundary.yaml; "
            "the divisome/Z-ring/septation sub-batch is first-pass curated and "
            "represented by modules/divisome_z_ring_septation_boundary.yaml; "
            "the Xer/FtsK chromosome dimer resolution and DNA translocation "
            "sub-batch is first-pass curated and represented by "
            "modules/chromosome_dimer_resolution_dna_translocation_boundary.yaml; "
            "the Tol-Pal envelope/division coordination sub-batch is first-pass "
            "curated, includes promoted TolA hole filling from the broad "
            "transport/membrane bucket, and is represented by "
            "modules/tol_pal_cell_division_envelope_coordination_boundary.yaml; "
            "the chromosome partition/condensation sub-batch is first-pass "
            "curated, includes promoted PP_0002 hole filling from the unknown "
            "bucket, and is represented by "
            "modules/chromosome_partition_condensation_boundary.yaml; "
            "the two broad keyword spillovers are first-pass curated and routed "
            "out, with PP_1105 assigned to DNA ligase/repair context and tig "
            "assigned to trigger-factor chaperone/protein-folding context; "
            "use projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_partition.tsv "
            "for the complete partition ledger."
        ),
        "priority_phase": "8",
        "batch_status": "PARTITIONED",
    },
    "module:dna_replication_repair_recombination": {
        "module": "",
        "module_file": "",
        "scope_note": (
            "Partitioned functional bucket: PSEPK DNA replication/repair/recombination "
            "contains 93 primary genes from UniProt name/keyword assignment. The set "
            "mixes DNA topology/topoisomerase proteins, replication accessory and "
            "polymerase candidates, SOS/translesion/alkylation repair proteins, repair "
            "helicase/recombination candidates, nuclease/DNase/toxin side nodes, "
            "reverse-transcriptase candidates, mobile-element integrases/recombinases/"
            "transposases, and architectural/RNA/protein-folding spillovers. Reuse "
            "existing KEGG-derived modules for canonical bacterial DNA replication, "
            "base excision repair, nucleotide excision repair, mismatch repair, "
            "homologous recombination, and non-homologous end joining. The compact "
            "DNA-topology/topoisomerase, SOS/translesion/alkylation, and "
            "nuclease/DNase/toxin splits are complete as boundary modules; the "
            "repair-helicase/recombination split extends the homologous-"
            "recombination module; and the replication-accessory/polymerase "
            "split extends bacterial DNA replication. The architectural/RNA/"
            "protein-folding spillover split is complete as a boundary module. Route "
            "mobile-element and reverse-transcriptase genes to the mobile-genetic-"
            "elements queue unless direct chromosomal repair evidence is found. Use "
            "projects/P_PUTIDA/batches/module_dna_replication_repair_recombination_partition.tsv "
            "for the complete partition ledger."
        ),
        "priority_phase": "8",
        "batch_status": "PARTITIONED",
    },
    "module:mobile_genetic_elements": {
        "module": "",
        "module_file": "",
        "scope_note": (
            "Partitioned functional bucket: PSEPK mobile genetic elements contains "
            "89 primary genes from UniProt name/keyword assignment. The set mixes "
            "GOA-supported transposases and insertion-sequence integration proteins, "
            "domain-only or fragmentary transposase candidates, integrases, prophage "
            "structural and packaging proteins, phage DNA replication/processing "
            "proteins, lysis/host-interaction proteins, regulatory/toxin-antitoxin "
            "candidates, and low-information prophage proteins. The 18-gene "
            "transposase_goa_supported split is first-pass curated with Asta coverage "
            "and represented by modules/mobile_genetic_elements_boundary.yaml, which "
            "also contains the completed DNA-bucket mobile-element boundary genes. "
            "The 22-gene transposase_domain_or_fragment split is first-pass curated "
            "there as a lower-confidence split: six full IS66 multi-domain proteins "
            "are retained as domain-supported transposase/DNA-transposition calls, "
            "while isolated Orf2/TnpB, IS66-C-only, DUF, TniB/TniQ, mixed-domain, "
            "and product-only records remain no-core unresolved context. "
            "The 3-gene integrase_mobile_element_context split is also first-pass "
            "curated there, with PP_2825 retained as the supported phage-integrase "
            "DNA-binding/integration protein and PP_1963/PP_3677 retained as "
            "unresolved product-name-only candidates. "
            "The 21-gene prophage_structural_packaging split is first-pass curated "
            "in modules/phage_structural_packaging_boundary.yaml, with terminase "
            "large subunits retained as endonuclease/virion-assembly context, "
            "domain-supported portal/tail/capsid/head components retained as "
            "structural molecule activity in virion assembly, and six ambiguous "
            "small-terminase, assembly, internal-core, or product-only entries "
            "left no-core unresolved. "
            "The 2-gene phage_lysis_host_interaction split is first-pass curated in "
            "modules/phage_lysis_host_interaction_boundary.yaml, and the 3-gene "
            "phage_regulatory_toxin_antitoxin split is first-pass curated in "
            "modules/phage_regulation_toxin_antitoxin_boundary.yaml. The 6-gene "
            "phage_dna_replication_processing split is first-pass curated in "
            "modules/phage_dna_replication_processing_boundary.yaml, separating "
            "phage O-family origin-binding replication proteins, a P-loop/ISTB "
            "ATP-binding replication candidate, a T7-like SSB protein, a phage "
            "endodeoxyribonuclease/integration context, and one unresolved "
            "DNA-circulation candidate. "
            "The 14-gene low_information_prophage_proteins split is first-pass "
            "curated with Asta coverage; PP_1571, PP_3860, and PP_3871 are added "
            "to the structural/packaging module as domain-supported structural "
            "exceptions, PP_2285 keeps non-core genome-ejection process context, "
            "and the remaining name-only or ambiguous records stay no-core "
            "unresolved. All eight sub-batches are now complete. Use "
            "projects/P_PUTIDA/batches/module_mobile_genetic_elements_partition.tsv "
            "for the complete partition ledger."
        ),
        "priority_phase": "8",
        "batch_status": "PARTITIONED",
    },
    "module:protein_folding_targeting_turnover": {
        "module": "",
        "module_file": "",
        "scope_note": (
            "Partitioned functional bucket: PSEPK protein folding/targeting/turnover "
            "contains 91 primary genes from UniProt name/keyword assignment. The set "
            "mixes bacterial chaperones, holdases, foldases, co-chaperones, "
            "ATP-dependent proteases, cofactor and metal-protein maturation "
            "chaperones, cell-wall/envelope peptidase and inhibitor proteins, "
            "aminopeptidases, periplasmic/membrane/secreted protease quality-control "
            "candidates, DNA-damage/repair spillover proteases, phage/mobile-element "
            "proteases, and low-information peptidase spillovers. The 13-gene "
            "chaperone_folding_holdase_foldase split is first-pass curated with "
            "Asta coverage and represented in "
            "modules/bacterial_chaperone_protein_folding_boundary.yaml, separating "
            "Hsp33/HslO, SurA, ClpB, SlyD, HscA/HscB, GroES, GrpE, CbpA/CbpM, "
            "ClpA/B-like ATPase, cold-shock nucleic-acid chaperone, and unresolved "
            "DjlA_N/TerB-like side context. The 13-gene "
            "atp_dependent_protease_turnover split is also first-pass curated with "
            "Asta coverage and represented in "
            "modules/bacterial_atp_dependent_protein_turnover_boundary.yaml, separating "
            "Lon-family proteases, ClpP proteolytic subunits, ClpA/ClpX ATPase "
            "unfoldases, ClpS/SspB substrate adaptors, the HslUV protease, one "
            "ClpP/TepA-domain peptidase candidate, and one no-core Lon N-terminal "
            "domain fragment. The 12-gene cofactor_metal_maturation_chaperones "
            "split is first-pass curated with Asta coverage and represented in "
            "modules/cofactor_metal_maturation_chaperone_boundary.yaml, separating "
            "HMA/PCuAC copper and metal chaperones, SdhE FAD assembly, "
            "UreD/UreE/UreF/UreG urease nickel metallocenter assembly, "
            "ZNG1/CobW-family zinc chaperones, and HemW heme/Fe-S chaperone "
            "context; cobW cobalamin biosynthesis was removed as unsupported "
            "name/family transfer and yggW coproporphyrinogen oxidase was marked "
            "over-annotated. The 16-gene "
            "cell_wall_envelope_peptidase_inhibitor split is first-pass curated "
            "with Asta coverage and represented in "
            "modules/envelope_cell_wall_peptidase_inhibitor_boundary.yaml, "
            "separating M23/M37 envelope metalloendopeptidases, NlpC/P60 "
            "cysteine peptidases, Prc/CtpA S41A serine peptidases, M14/S66 "
            "carboxypeptidases, alpha-2-macroglobulin/chagasin/ecotin "
            "protease inhibitors, and two no-core low-information candidates "
            "PP_2108 and PP_5729. The 13-gene "
            "peptide_processing_aminopeptidases split is first-pass curated "
            "with Asta coverage and represented in "
            "modules/protein_turnover_peptide_processing_boundary.yaml, "
            "separating Map/MetAP and Xaa-Pro aminopeptidases, M18/M42/M90 "
            "aminopeptidases, PrlC oligopeptidase, U32 and DJ-1/PfpI generic "
            "peptidase candidates, M20A/M20 deacetylase or dipeptidase side "
            "nodes, and TldD/PmbA metallopeptidase context; obsolete "
            "GO:0019877 from UniProt was not authored as a core process. The "
            "12-gene periplasmic_membrane_secreted_protease_qc split is "
            "first-pass curated with Asta coverage and represented in "
            "modules/envelope_protease_quality_control_boundary.yaml, separating "
            "M48/BepA envelope metalloendopeptidases, PmbA/U62 and QEGLA/MATCAP "
            "metallopeptidase candidates, S8/subtilase serine proteases, M16 "
            "metallopeptidases, and no-core unresolved qmcA and PP_5455 context; "
            "obsolete GO:0051603 was not authored as a core process. The 3-gene "
            "dna_damage_or_repair_spillover_proteases split is first-pass curated "
            "with Asta coverage and represented as an extension to "
            "modules/dna_bucket_architectural_rna_protein_spillover_boundary.yaml: "
            "PP_0758 and PP_2941 are SRAP/HMCES-like protein-DNA covalent "
            "cross-link repair boundary proteins, while PP_2493 is retained "
            "conservatively as a RadC/JAB/MPN metalloprotease-like candidate "
            "without asserting a direct DNA-repair process. The 2-gene "
            "phage_mobile_protease_spillovers split is first-pass curated with "
            "Asta coverage and represented as an extension to "
            "modules/phage_structural_packaging_boundary.yaml, routing PP_1566 "
            "and PP_3878 to prophage structural maturation protease context "
            "rather than host protein turnover. The final 7-gene "
            "low_information_peptidase_spillovers split is first-pass curated "
            "with Asta coverage and represented in "
            "modules/protein_turnover_peptidase_spillover_boundary.yaml, "
            "separating class-specific S1/S9A serine and clan AA aspartic "
            "endopeptidase candidates, generic PfpI/C39 peptidase candidates, "
            "and no-core unresolved PP_2447/PP_2685 context. Use "
            "projects/P_PUTIDA/batches/module_protein_folding_targeting_turnover_partition.tsv "
            "for the complete partition ledger."
        ),
        "priority_phase": "8",
        "batch_status": "PARTITIONED",
    },
    "module:translation_rna_processing": {
        "module": "",
        "module_file": "",
        "scope_note": (
            "Partitioned functional bucket: PSEPK translation/RNA processing "
            "contains 128 primary genes from UniProt name/keyword assignment. "
            "The set mixes rRNA modification methyltransferases and "
            "pseudouridine synthases, ribosome assembly/maturation and "
            "hibernation factors, tRNA modification and processing enzymes, "
            "ribonucleases/RNA decay and RNA helicases, aminoacyl-tRNA "
            "charging/editing/quality-control enzymes, translation factors and "
            "ribosome-rescue proteins, transcription/RNA-polymerase spillovers, "
            "pyoverdine/ferribactin NRPS spillovers, and two low-information "
            "RNA-binding/enzyme spillovers. The 4-gene "
            "nonribosomal_peptide_synthetase_spillovers split is first-pass "
            "curated with Asta coverage and represented as an extension to "
            "modules/siderophore_biosynthesis_boundary.yaml, routing pvdD, "
            "pvdJ, pvdI, and pvdL to pyoverdine/ferribactin NRPS assembly "
            "rather than translation. The 2-gene "
            "low_information_rna_binding_or_enzyme_spillovers split is also "
            "first-pass curated with Asta coverage and represented in "
            "modules/translation_rna_processing_spillover_boundary.yaml, "
            "retaining PP_2182 as a ProQ/FinO RNA-chaperone candidate and "
            "routing PP_2953 out as a NADPH quinone-reductase-like "
            "oxidoreductase rather than RNA processing. The 6-gene "
            "transcription_rna_polymerase_spillovers split is first-pass "
            "curated with Asta coverage and represented in "
            "modules/transcription_rna_polymerase_spillover_boundary.yaml, "
            "routing NusA/NusB, RapA, DksA, PP_2266, and PP_4553 to "
            "transcription and RNA-polymerase boundary context rather than "
            "translation/RNA processing. The 10-gene "
            "translation_factors_ribosome_rescue split is first-pass curated "
            "with Asta coverage and represented in "
            "modules/translation_factor_ribosome_rescue_boundary.yaml, "
            "separating IF-1, SelB, EF-4/LepA, EttA, Frr, Pth, ArfB, SmpB, "
            "HslR, and YchF as translation-factor, ribosome-recycling, "
            "stalled-ribosome-rescue, and ribosome-associated NTPase context. The "
            "11-gene aminoacyl_trna_charging_editing_quality_control split is "
            "first-pass curated with Asta coverage and represented in "
            "modules/aminoacyl_trna_quality_control_boundary.yaml, separating "
            "YbaK/Dtd/YcfH deacylase or editing context, Aat N-end-rule "
            "L/F-transferase chemistry, Glu-Q tRNA(Asp) modification, and "
            "unresolved GAD/T6SS or short-fragment side nodes from canonical "
            "aminoacyl-tRNA synthetases. The 12-gene "
            "ribonuclease_rna_decay_processing_helicases split is first-pass "
            "curated with Asta coverage and represented in "
            "modules/rna_decay_processing_boundary.yaml, separating RNase "
            "P/G/T/Z/D/PH tRNA or rRNA processing activities, SrmB/DbpA "
            "DEAD-box helicase context, and RraA/RraB/YhbY-like side nodes. The "
            "29-gene rrna_modification_methyltransferase_pseudouridine split is "
            "first-pass curated with Asta coverage and represented in "
            "modules/rrna_modification_ribosome_maturation_boundary.yaml, separating "
            "site-specific Rsm/Rlm/Rlu/Rsu-family rRNA methyltransferases and "
            "pseudouridine synthases, dual RlmN/RluF side chemistry, RsmE paralogs, "
            "and unresolved PP_4306/RlmI target-site side nodes. The 24-gene "
            "ribosome_assembly_maturation_hibernation split is first-pass curated "
            "with Asta coverage and represented in "
            "modules/bacterial_ribosome_maturation_regulation_boundary.yaml, separating "
            "ribosome biogenesis GTPases, 30S/50S maturation factors, hibernation "
            "and silencing factors, ribosomal-protein modification enzymes, and "
            "low-information ribosomal-interface side nodes. The 30-gene "
            "trna_modification_processing split is first-pass curated with Asta "
            "coverage and represented in "
            "modules/trna_modification_processing_boundary.yaml, separating "
            "wobble-uridine side-chain chemistry, t6A37 biosynthesis, tRNA "
            "methylation, pseudouridylation, deamination, lysidine formation, "
            "thiolation, dihydrouridine synthesis, aminocarboxypropylation, "
            "prenylation, and CCA-end processing. All nine translation/RNA "
            "processing splits are now first-pass complete. Use "
            "projects/P_PUTIDA/batches/module_translation_rna_processing_partition.tsv "
            "for the complete partition ledger."
        ),
        "priority_phase": "8",
        "batch_status": "PARTITIONED",
    },
    "module:motility_chemotaxis_biofilm": {
        "module": "",
        "module_file": "",
        "scope_note": (
            "Partitioned functional bucket: PSEPK motility/chemotaxis/biofilm "
            "contains 35 primary genes from UniProt name/keyword assignment. "
            "The set mixes type IV pilus biogenesis and assembly, fimbrial/"
            "type-I-pilus surface-adhesion extension candidates, an Hcp/T6SS "
            "product-name spillover, alginate envelope/export and lyase "
            "context, orphan MCP chemotaxis receptor candidates, a sensory "
            "c-di-GMP phosphodiesterase spillover, a DNA-binding response-regulator "
            "spillover, CheY-like/membrane accessory spillovers, an outer-membrane "
            "flagellation-name spillover, flagellar export/localization/accessory "
            "spillovers, and c-di-GMP flagellar brake context. "
            "The 12-gene type IV pilus "
            "biogenesis set is first-pass curated in "
            "modules/type_iv_pilus_biogenesis_boundary.yaml, with pilD and "
            "pilT retained as explicit hole-filling gaps. The PP_1888/fimI fimbrial "
            "extension is first-pass curated and represented by the existing "
            "modules/pili_surface_adhesion_boundary.yaml; PP_0655 is "
            "first-pass curated and routed to "
            "modules/bacterial_secretion_system_boundary.yaml because its "
            "Hcp/T6SS domains supersede the generic fimbrial product name. "
            "The glmP/PP_1754/PP_3350/PP_3464/PP_3774 alginate context is "
            "first-pass curated and represented by the existing "
            "modules/alginate_biosynthesis_boundary.yaml. "
            "The PP_2310/PP_3950/PP_4888 orphan MCP set is first-pass "
            "curated and represented by "
            "modules/orphan_mcp_aerotaxis_receptors_boundary.yaml; PP_2599 "
            "is first-pass curated and routed to "
            "modules/c_di_gmp_turnover_boundary.yaml because HD-GYP/HD-PDEase "
            "and cyclic-di-GMP phosphodiesterase-family evidence supersede "
            "the generic chemotaxis sensory-transducer product name. "
            "PP_2403 is first-pass curated and routed to "
            "modules/orphan_two_component_regulators_boundary.yaml because "
            "OmpR/PhoB DNA-binding response-regulator evidence supersedes the "
            "CheY-like product name; PP_3757/PP_3771/PP_4331 are first-pass "
            "curated and represented by "
            "modules/chemotaxis_adaptation_accessory_boundary.yaml as one "
            "compact CheY-like response-regulator candidate and two conservative "
            "membrane accessory candidates. ycfJ is first-pass curated and routed "
            "to modules/transport_envelope_spillover_boundary.yaml as an "
            "outer-membrane lipoprotein/surface-antigen-family spillover; "
            "PP_4328/PP_4329/PP_4342/flhF/PP_4377 are first-pass curated and "
            "represented by modules/flagellar_export_assembly_boundary.yaml as "
            "hook-control, export, localization/number-control, and FlaG accessory "
            "context; ycgR is first-pass curated and routed to "
            "modules/flagellar_motor_switch_stator_boundary.yaml as a PilZ-domain "
            "c-di-GMP-dependent motor brake. "
            "Reuse completed pili/surface-adhesion, chemotaxis, flagellar, "
            "alginate, secretion, and c-di-GMP modules where appropriate; use "
            "projects/P_PUTIDA/batches/module_motility_chemotaxis_biofilm_partition.tsv "
            "for the complete partition ledger."
        ),
        "priority_phase": "8",
        "batch_status": "PARTITIONED",
    },
    # KEGG ppu00400 is broader than this module; keep this as a seeded submodule.
    "kegg:ppu00400": {
        "module": "tryptophan_biosynthesis",
        "module_file": "modules/tryptophan_biosynthesis.yaml",
        "scope_note": "Seeded submodule; KEGG bucket also includes phenylalanine, tyrosine, and chorismate genes.",
        "priority_phase": "3",
        "pr_status": "MERGED",
        "pr_url": "https://github.com/ai4curation/ai-gene-review/pull/1874",
    },
    "kegg:ppu00270": {
        "module": "methionine_biosynthesis",
        "module_file": "modules/methionine_biosynthesis.yaml",
        "scope_note": "Seeded submodule; KEGG bucket includes cysteine and methionine metabolism.",
        "priority_phase": "3",
    },
    "kegg:ppu00220": {
        "module": "arginine_biosynthesis",
        "module_file": "modules/arginine_biosynthesis.yaml",
        "scope_note": "Seeded bacterial acetylated arginine-biosynthesis module; KEGG ppu00220 also includes arginine-deiminase/carbamate, urease, glutamine-synthetase, nitrogen-assimilation, and polyamine side nodes, while ArgD is UniPathway-supported but assigned to ppu00330 in the partition.",
        "priority_phase": "3",
    },
    "kegg:ppu00230": {
        "module": "purine_metabolism",
        "module_file": "modules/purine_metabolism.yaml",
        "scope_note": "Seeded broad purine-metabolism boundary module; KEGG ppu00230 combines de novo IMP/AMP/GMP biosynthesis, salvage, purine catabolism, nucleotide housekeeping, alarmone metabolism, cyclic-nucleotide turnover, and several cross-bucket side nodes.",
        "priority_phase": "6",
    },
    "kegg:ppu00240": {
        "module": "pyrimidine_metabolism",
        "module_file": "modules/pyrimidine_metabolism.yaml",
        "scope_note": "Seeded broad pyrimidine-metabolism boundary module; KEGG ppu00240 combines de novo UMP synthesis, CTP and dTMP branches, salvage, reductive pyrimidine catabolism, nucleoside phosphorylase/nucleotidase side nodes, ribonucleotide reduction, and generic nucleotide-pool housekeeping.",
        "priority_phase": "6",
    },
    "kegg:ppu00250": {
        "module": "alanine_aspartate_glutamate_metabolism",
        "module_file": "modules/alanine_aspartate_glutamate_metabolism.yaml",
        "scope_note": "Seeded broad alanine/aspartate/glutamate boundary module; KEGG ppu00250 combines alanine transamination, aspartate/asparagine reactions, glutamate/glutamine nitrogen assimilation, proline and polyamine side routes, and nucleotide/arginine/pyrimidine/NAD/amino-sugar spillovers.",
        "priority_phase": "6",
    },
    "kegg:ppu00260": {
        "module": "glycine_serine_threonine_metabolism",
        "module_file": "modules/glycine_serine_threonine_metabolism.yaml",
        "scope_note": "Seeded broad glycine/serine/threonine boundary module; KEGG ppu00260 combines serine and threonine biosynthesis, glycine cleavage, methylated-glycine/betaine catabolism, one-carbon chemistry, and tryptophan/cysteine/methionine/glyoxylate/lipid/pyoverdine spillovers.",
        "priority_phase": "6",
    },
    "kegg:ppu00261": {
        "module": "monobactam_biosynthesis_boundary",
        "module_file": "modules/monobactam_biosynthesis_boundary.yaml",
        "scope_note": "Seeded boundary/absence module; KEGG ppu00261 is mostly aspartate-family lysine/diaminopimelate precursor enzymes, sulfate activation, and an MbtH-like secondary-metabolite accessory protein rather than evidence for a complete PSEPK monobactam route.",
        "priority_phase": "6",
    },
    "kegg:ppu00280": {
        "module": "branched_chain_amino_acid_degradation",
        "module_file": "modules/branched_chain_amino_acid_degradation.yaml",
        "scope_note": "Seeded broad branched-chain amino acid degradation boundary module; KEGG ppu00280 combines leucine, valine, and isoleucine catabolic steps with fatty-acid beta-oxidation, propanoate/butanoate, lipoamide, thiolase, and CoA-transferase spillovers.",
        "priority_phase": "6",
    },
    "kegg:ppu00290": {
        "module": "branched_chain_amino_acid_biosynthesis",
        "module_file": "modules/branched_chain_amino_acid_biosynthesis.yaml",
        "scope_note": "Seeded broad branched-chain amino acid biosynthesis boundary module; KEGG ppu00290 combines strict valine, leucine, and isoleucine biosynthetic enzymes with threonine-deaminase paralogs, alanine aminotransferase, leucine dehydrogenase, and C5-branched dibasic acid spillovers.",
        "priority_phase": "6",
    },
    "kegg:ppu00300": {
        "module": "lysine_biosynthesis",
        "module_file": "modules/lysine_biosynthesis.yaml",
        "scope_note": "Seeded bacterial L-lysine biosynthesis via diaminopimelate module; KEGG ppu00300 combines strict DapA/DapB/DapD/DapC/DapE/DapF/LysA route enzymes with shared aspartate-family precursors, homoserine branch nodes, peptidoglycan DAP ligases, and ornithine/acetylornithine aminotransferase side context.",
        "priority_phase": "6",
    },
    "kegg:ppu00310": {
        "module": "lysine_degradation",
        "module_file": "modules/lysine_degradation.yaml",
        "scope_note": "Seeded broad lysine degradation boundary module; KEGG ppu00310 combines the DavB/DavA/DavT/DavD L-lysine-to-glutarate route with D-lysine/pipecolate, aminoadipate, glutarate/hydroxyglutarate, beta-oxidation, thiolase, lipoamide, and aldehyde-dehydrogenase spillovers.",
        "priority_phase": "6",
    },
    "kegg:ppu00330": {
        "module": "arginine_proline_metabolism",
        "module_file": "modules/arginine_proline_metabolism.yaml",
        "scope_note": "Seeded broad arginine/proline boundary module; KEGG ppu00330 combines proline biosynthesis/catabolism, succinylated arginine catabolism, agmatine/polyamine/putrescine routes, opine/2-ketoarginine side chemistry, and 5-oxoproline/creatinine side nodes.",
        "priority_phase": "6",
    },
    "kegg:ppu00332": {
        "module": "carbapenem_biosynthesis_boundary",
        "module_file": "modules/carbapenem_biosynthesis_boundary.yaml",
        "scope_note": "Boundary/absence module; KEGG ppu00332 contains only ProB/ProA shared proline-precursor chemistry in PSEPK and should not be interpreted as a complete carbapenem biosynthesis pathway.",
        "priority_phase": "6",
    },
    "kegg:ppu00350": {
        "module": "tyrosine_catabolism",
        "module_file": "modules/tyrosine_catabolism.yaml",
        "scope_note": "Mapped to the homogentisate L-tyrosine catabolism module; KEGG ppu00350 also includes aldehyde dehydrogenases, decarboxylases, and aromatic side-node spillovers that require boundary review.",
        "priority_phase": "6",
    },
    "kegg:ppu00360": {
        "module": "phenylalanine_metabolism",
        "module_file": "modules/phenylalanine_metabolism.yaml",
        "scope_note": "Seeded broad phenylalanine-metabolism boundary module; KEGG ppu00360 combines PhhA/homogentisate phenylalanine-to-tyrosine chemistry, the Paa phenylacetate catabolic operon, D-amino-acid dehydrogenases, decarboxylase/aldehyde side nodes, and fatty-acid-like spillovers.",
        "priority_phase": "6",
    },
    "kegg:ppu00361": {
        "module": "chlorocyclohexane_chlorobenzene_degradation_boundary",
        "module_file": "modules/chlorocyclohexane_chlorobenzene_degradation_boundary.yaml",
        "scope_note": "Boundary module; KEGG ppu00361 contains only CatA paralogs and CatB in PSEPK, supporting catechol ortho-cleavage/beta-ketoadipate lower-pathway chemistry but not a complete chlorocyclohexane or chlorobenzene upper degradation route.",
        "priority_phase": "2",
    },
    "kegg:ppu00380": {
        "module": "tryptophan_metabolism_boundary",
        "module_file": "modules/tryptophan_metabolism_boundary.yaml",
        "scope_note": "Boundary module; KEGG ppu00380 is broad in PSEPK and primary partition genes are gcdH and katG, supporting glutaryl-CoA dehydrogenase and catalase-peroxidase/peroxide-detoxification side nodes rather than a complete dedicated tryptophan-catabolic route.",
        "priority_phase": "6",
    },
    "kegg:ppu00401": {
        "module": "novobiocin_biosynthesis_boundary",
        "module_file": "modules/novobiocin_biosynthesis_boundary.yaml",
        "scope_note": "Boundary/absence module; KEGG ppu00401 contains only HisC, AroA, TyrB, and AmaC shared amino-acid/aromatic-precursor enzymes in PSEPK, not a novobiocin aminocoumarin antibiotic biosynthesis gene cluster.",
        "priority_phase": "6",
    },
    "kegg:ppu00410": {
        "module": "beta_alanine_metabolism_boundary",
        "module_file": "modules/beta_alanine_metabolism_boundary.yaml",
        "scope_note": "Seeded broad beta-alanine metabolism boundary module; KEGG ppu00410 combines reductive pyrimidine catabolism to beta-alanine, beta-alanine transamination, pantothenate ligation, methylmalonate-semialdehyde dehydrogenases, aldehyde dehydrogenases, and acyl-CoA/fatty-acid side nodes.",
        "priority_phase": "6",
    },
    "kegg:ppu00430": {
        "module": "taurine_hypotaurine_metabolism_boundary",
        "module_file": "modules/taurine_hypotaurine_metabolism_boundary.yaml",
        "scope_note": "Boundary module; KEGG ppu00430 contains TauD taurine dioxygenase plus acetate, glutamate, and glutathione metabolism side nodes rather than a full dedicated taurine/hypotaurine route.",
        "priority_phase": "6",
    },
    "kegg:ppu00440": {
        "module": "phosphonate_phosphinate_metabolism",
        "module_file": "modules/phosphonate_phosphinate_metabolism.yaml",
        "scope_note": "Seeded PhnWX 2-aminoethylphosphonate catabolism module, now extended with the PP_0824-PP_0827 phosphonate ABC import sub-batch from ppu02010 and the PP_1722-PP_1726 AEP/phosphonate ABC import candidate from ppu02024. KEGG ppu00440 in PSEPK contains PhnW AEP transaminase and PhnX phosphonoacetaldehyde hydrolase; the combined module remains a compact phosphonate uptake/catabolism context rather than a broad C-P lyase or phosphinate system.",
        "priority_phase": "6",
    },
    "kegg:ppu00450": {
        "module": "selenocompound_metabolism_boundary",
        "module_file": "modules/selenocompound_metabolism_boundary.yaml",
        "scope_note": "Boundary module; KEGG ppu00450 contains the selenium-specific SelD/SelA Sec-tRNA biosynthesis spine plus methionine, cysteine, sulfate-assimilation, and aminoacyl-tRNA side nodes rather than a broad dedicated selenocompound route.",
        "priority_phase": "6",
    },
    "kegg:ppu00460": {
        "module": "cyanoamino_acid_metabolism_boundary",
        "module_file": "modules/cyanoamino_acid_metabolism_boundary.yaml",
        "scope_note": "Boundary module; KEGG ppu00460 in PSEPK contains AnsA/PP_1160 asparaginase-family genes plus SHMT, periplasmic beta-glucosidase, and glutathione hydrolase side nodes rather than a proven cyanogenic-glycoside or cyanoamino-acid detoxification route.",
        "priority_phase": "6",
    },
    "kegg:ppu00470": {
        "module": "d_amino_acid_metabolism_boundary",
        "module_file": "modules/d_amino_acid_metabolism_boundary.yaml",
        "scope_note": "Boundary module; KEGG ppu00470 combines peptidoglycan D-Glu/D-Ala chemistry, D-amino-acid racemases/dehydrogenases, hydroxyproline/dioxovalerate side-route enzymes, diaminopimelate/lysine biosynthesis side nodes, and asparaginase context rather than one strict D-amino-acid catabolic pathway.",
        "priority_phase": "6",
    },
    "kegg:ppu00480": {
        "module": "glutathione_metabolism_boundary",
        "module_file": "modules/glutathione_metabolism_boundary.yaml",
        "scope_note": "Boundary module; KEGG ppu00480 combines glutathione biosynthesis, glutathione reductase/peroxidase/GST detoxification, glutathione hydrolase and 5-oxoproline turnover, NADPH-generating central-carbon enzymes, aminopeptidase side nodes, and unrelated SpeC/PtxD spillovers rather than one strict glutathione pathway.",
        "priority_phase": "6",
    },
    "kegg:ppu00500": {
        "module": "starch_sucrose_metabolism_boundary",
        "module_file": "modules/starch_sucrose_metabolism_boundary.yaml",
        "scope_note": "Boundary module; KEGG ppu00500 in PSEPK combines bacterial glycogen/alpha-glucan metabolism, TreY/TreZ/TreS trehalose and GlgE-route chemistry, BcsA cellulose synthesis, shared sugar-phosphate/UDP-glucose precursor enzymes, and beta-glucosidase side context rather than a plant-like starch/sucrose pathway.",
        "priority_phase": "6",
    },
    "kegg:ppu00520": {
        "module": "amino_sugar_nucleotide_sugar_metabolism_boundary",
        "module_file": "modules/amino_sugar_nucleotide_sugar_metabolism_boundary.yaml",
        "scope_note": "Boundary module; KEGG ppu00520 in PSEPK combines UDP-GlcNAc biosynthesis, de novo UDP-MurNAc/peptidoglycan precursor chemistry, MurNAc recycling/salvage, nucleotide-sugar side branches, alginate/GDP-mannose context, and shared sugar-phosphate enzymes rather than one linear pathway.",
        "priority_phase": "6",
    },
    "kegg:ppu00523": {
        "module": "polyketide_sugar_unit_biosynthesis_boundary",
        "module_file": "modules/polyketide_sugar_unit_biosynthesis_boundary.yaml",
        "scope_note": "Boundary/absence module; KEGG ppu00523 in PSEPK contains a dTDP-deoxy-sugar/dTDP-L-rhamnose enzyme set, not evidence for a complete polyketide sugar-unit biosynthesis or natural-product glycosylation pathway.",
        "priority_phase": "6",
    },
    "kegg:ppu00525": {
        "module": "acarbose_validamycin_biosynthesis_boundary",
        "module_file": "modules/acarbose_validamycin_biosynthesis_boundary.yaml",
        "scope_note": "Boundary/absence module; KEGG ppu00525 in PSEPK contains only shared dTDP-glucose and dTDP-deoxy-sugar precursor enzymes, not evidence for a complete acarbose, validamycin, or aminocyclitol antibiotic biosynthesis pathway.",
        "priority_phase": "6",
    },
    "kegg:ppu00540": {
        "module": "lipopolysaccharide_biosynthesis",
        "module_file": "modules/lipopolysaccharide_biosynthesis.yaml",
        "scope_note": "LPS module; KEGG ppu00540 in PSEPK combines lipid IVA/lipid A biosynthesis, Kdo2-lipid A formation, LPS core oligosaccharide assembly, and lipid A/LPS remodeling candidates. Broad membrane/cofactor/generic transferase terms should remain non-core or over-annotation context.",
        "priority_phase": "6",
    },
    "kegg:ppu00541": {
        "module": "nucleotide_sugar_biosynthesis_boundary",
        "module_file": "modules/nucleotide_sugar_biosynthesis_boundary.yaml",
        "scope_note": "Boundary module; KEGG ppu00541 in PSEPK combines ADP-heptose, Kdo/CMP-Kdo, dTDP-rhamnose, GDP-mannose/GDP-D-rhamnose, UDP-glucose/UDP-glucuronate, UDP-GlcNAc, and unresolved polysaccharide/redox side nodes rather than one linear nucleotide-sugar pathway.",
        "priority_phase": "6",
    },
    "kegg:ppu00543": {
        "module": "exopolysaccharide_biosynthesis_boundary",
        "module_file": "modules/exopolysaccharide_biosynthesis_boundary.yaml",
        "scope_note": "Boundary module; KEGG ppu00543 in PSEPK is centered on alginate/exopolysaccharide production but also contains serine O-acetyltransferase cysteine-biosynthesis spillovers and an unresolved glycosyltransferase side candidate.",
        "priority_phase": "6",
    },
    "kegg:ppu00550": {
        "module": "peptidoglycan_biosynthesis",
        "module_file": "modules/peptidoglycan_biosynthesis.yaml",
        "scope_note": "Peptidoglycan module; KEGG ppu00550 in PSEPK combines cytosolic UDP-MurNAc-peptide assembly, lipid-linked precursor assembly/recycling, SEDS-family polymerases, PBPs/transpeptidases, and carboxypeptidase/remodeling side nodes. MurJ should be promoted from UniPathway context because it is expected for lipid II flipping but absent from KEGG ppu00550; the linked UniPathway UPA00544 recycling/salvage arm is represented inside the same module.",
        "priority_phase": "6",
    },
    "kegg:ppu00552": {
        "module": "teichoic_acid_biosynthesis_boundary",
        "module_file": "modules/teichoic_acid_biosynthesis_boundary.yaml",
        "scope_note": "Boundary/absence module; KEGG ppu00552 in PSEPK contains only wbpM and uppP, supporting unresolved envelope polysaccharide context and shared undecaprenyl carrier recycling rather than a complete Gram-positive teichoic-acid biosynthesis route.",
        "priority_phase": "6",
    },
    "kegg:ppu00561": {
        "module": "glycerolipid_metabolism_boundary",
        "module_file": "modules/glycerolipid_metabolism_boundary.yaml",
        "scope_note": "Boundary module; KEGG ppu00561 in PSEPK combines bacterial phosphatidic-acid/glycerophospholipid precursor enzymes, DgkA diacylglycerol recycling, glycerol entry, and side nodes from glycerate/hydroxypyruvate, aromatic alcohol, and generic lipase metabolism.",
        "priority_phase": "6",
    },
    "kegg:ppu00562": {
        "module": "inositol_phosphate_metabolism_boundary",
        "module_file": "modules/inositol_phosphate_metabolism_boundary.yaml",
        "scope_note": "Boundary/absence module; KEGG ppu00562 in PSEPK contains SuhB inositol-monophosphatase/rrnTAC context plus TpiA and MmsA paralog side nodes, not a complete inositol-phosphate or phosphatidylinositol signalling route.",
        "priority_phase": "6",
    },
    "kegg:ppu00564": {
        "module": "glycerophospholipid_metabolism",
        "module_file": "modules/glycerophospholipid_metabolism.yaml",
        "scope_note": "Broad bacterial glycerophospholipid module; KEGG ppu00564 in PSEPK combines phosphatidic-acid/CDP-DAG precursor chemistry, phosphatidylglycerol/cardiolipin/PE/PC synthesis, glycerol-3-phosphate supply, phospholipase/glycerophosphodiester turnover, and ethanolamine side nodes.",
        "priority_phase": "6",
    },
    "kegg:ppu00566": {
        "module": "sulfoquinovose_metabolism_boundary",
        "module_file": "modules/sulfoquinovose_metabolism_boundary.yaml",
        "scope_note": "Boundary/absence module; KEGG ppu00566 in PSEPK contains only yihS as a KEGG K18479 sulfoquinovose-isomerase candidate and mdh as central-carbon malate-dehydrogenase spillover, not a complete sulfoquinovose degradation pathway.",
        "priority_phase": "6",
    },
    "kegg:ppu00592": {
        "module": "alpha_linolenic_acid_metabolism_boundary",
        "module_file": "modules/alpha_linolenic_acid_metabolism_boundary.yaml",
        "scope_note": "Boundary/absence module; KEGG ppu00592 in PSEPK contains only two FadA-like thiolases, supporting generic fatty-acid beta-oxidation side context rather than a complete alpha-linolenic-acid-specific pathway.",
        "priority_phase": "6",
    },
    "kegg:ppu00620": {
        "module": "pyruvate_metabolism_boundary",
        "module_file": "modules/pyruvate_metabolism_boundary.yaml",
        "scope_note": "Boundary module; KEGG ppu00620 in PSEPK mixes pyruvate-forming/consuming central-carbon nodes, pyruvate dehydrogenase/lipoate complexes, acetate/acetyl-CoA routes, lactate and methylglyoxal side routes, malate/oxaloacetate/TCA overlap, amino-acid precursor spillovers, and alcohol/aldehyde dehydrogenase side nodes rather than one satisfiable pyruvate pathway.",
        "priority_phase": "6",
    },
    "kegg:ppu00621": {
        "module": "dioxin_degradation_boundary",
        "module_file": "modules/dioxin_degradation_boundary.yaml",
        "scope_note": "Boundary/absence module; KEGG ppu00621 in PSEPK contains only PP_1791 unresolved aldolase/synthase and PP_2504 2-hydroxymuconate/4-oxalocrotonate tautomerase side context, not a complete dioxin degradation route.",
        "priority_phase": "2",
    },
    "kegg:ppu00625": {
        "module": "chloroalkane_chloroalkene_degradation_boundary",
        "module_file": "modules/chloroalkane_chloroalkene_degradation_boundary.yaml",
        "scope_note": "Boundary/absence module; KEGG ppu00625 in PSEPK contains formaldehyde dehydrogenase and alcohol dehydrogenase side nodes, not a complete chloroalkane/chloroalkene degradation route with dehalogenation chemistry.",
        "priority_phase": "2",
    },
    "kegg:ppu00626": {
        "module": "naphthalene_degradation_boundary",
        "module_file": "modules/naphthalene_degradation_boundary.yaml",
        "scope_note": "Boundary/absence module; KEGG ppu00626 in PSEPK contains only FrmA formaldehyde detoxification and AdhP alcohol dehydrogenase side context, not a complete naphthalene degradation route.",
        "priority_phase": "2",
    },
    "kegg:ppu00627": {
        "module": "aminobenzoate_degradation_boundary",
        "module_file": "modules/aminobenzoate_degradation_boundary.yaml",
        "scope_note": "Boundary module; KEGG ppu00627 in PSEPK mixes gallate, ferulate/vanillate, nitroaromatic redox, UbiX/prenyl-FMN, Baeyer-Villiger monooxygenase, CoA-hydratase, and unresolved amidase side nodes rather than one complete aminobenzoate degradation route.",
        "priority_phase": "2",
    },
    "kegg:ppu00630": {
        "module": "glyoxylate_dicarboxylate_metabolism_boundary",
        "module_file": "modules/glyoxylate_dicarboxylate_metabolism_boundary.yaml",
        "scope_note": "Boundary module; KEGG ppu00630 in PSEPK mixes glycolate/glyoxylate conversion, phosphoglycolate repair, formate oxidation, one-carbon/TCA/glyoxylate-shunt overlap, and respiratory redox side nodes rather than one linear glyoxylate/dicarboxylate pathway.",
        "priority_phase": "6",
    },
    "kegg:ppu00633": {
        "module": "nitrotoluene_degradation_boundary",
        "module_file": "modules/nitrotoluene_degradation_boundary.yaml",
        "scope_note": "Boundary/absence module; KEGG ppu00633 in PSEPK contains only nfnB nitroreductase-family context plus PP_2486 and nemA OYE/NADH-flavin oxidoreductase side nodes, not a complete nitrotoluene degradation route.",
        "priority_phase": "2",
    },
    "kegg:ppu00640": {
        "module": "propanoate_metabolism_boundary",
        "module_file": "modules/propanoate_metabolism_boundary.yaml",
        "scope_note": "Boundary module; KEGG ppu00640 in PSEPK combines Prp/methylcitrate propionyl-CoA assimilation, AcnB/PrpD/AcnA-II dehydratase/aconitase context, methylmalonate-semialdehyde and valine/thymine side routes, acetate/acyl-CoA activation, fatty-acid beta-oxidation, ACC, TCA/glyoxylate, and BCKDH/lipoamide overlap nodes rather than one linear propanoate pathway.",
        "priority_phase": "6",
    },
    "kegg:ppu00643": {
        "module": "styrene_degradation_boundary",
        "module_file": "modules/styrene_degradation_boundary.yaml",
        "scope_note": "Boundary/absence module; KEGG ppu00643 in PSEPK contains peaE phenylacetaldehyde dehydrogenase, hmgABC homogentisate/aromatic-amino-acid catabolism, and unresolved PP_2932 amidase-family context, but lacks the route-defining styrene monooxygenase and styrene oxide isomerase steps needed for complete styrene degradation.",
        "priority_phase": "2",
    },
    "kegg:ppu00650": {
        "module": "butanoate_metabolism_boundary",
        "module_file": "modules/butanoate_metabolism_boundary.yaml",
        "scope_note": "Boundary module; KEGG ppu00650 in PSEPK combines butanediol/4-hydroxybutyrate/3-hydroxybutyrate dehydrogenases, class II PHA synthases, succinate-semialdehyde/GABA side nodes, acetoacetate/acyl-CoA activation, thiolase/beta-oxidation, BCAA/acetolactate, phenylacetate/caprolactam, and TCA spillovers rather than one linear butanoate pathway.",
        "priority_phase": "6",
    },
    "kegg:ppu00660": {
        "module": "c5_branched_dibasic_acid_metabolism_boundary",
        "module_file": "modules/c5_branched_dibasic_acid_metabolism_boundary.yaml",
        "scope_note": "Boundary module; KEGG ppu00660 in PSEPK combines acetolactate/acetohydroxybutanoate and leucine-biosynthesis enzymes, GalC gallate/4-carboxy-4-hydroxy-2-oxoadipate aldolase context, and SucCD TCA succinyl-CoA synthetase rather than one dedicated C5-branched dibasic acid pathway.",
        "priority_phase": "6",
    },
    "kegg:ppu00680": {
        "module": "methane_metabolism_boundary",
        "module_file": "modules/methane_metabolism_boundary.yaml",
        "scope_note": "Boundary/absence module; KEGG ppu00680 in PSEPK contains formaldehyde/formate detoxification and oxidation, folate/serine and central-carbon side nodes, respiratory redox context, and PeaA amine dehydrogenase context, but not a complete methane oxidation or methanogenesis pathway.",
        "priority_phase": "6",
    },
    "kegg:ppu00710": {
        "module": "carbon_fixation_calvin_cycle_boundary",
        "module_file": "modules/carbon_fixation_calvin_cycle_boundary.yaml",
        "scope_note": "Boundary/absence module; KEGG ppu00710 in PSEPK contains non-oxidative PPP, lower EMP/gluconeogenesis, PEPC anaplerotic carbon fixation, malic enzyme, and Mdh side nodes, but lacks Rubisco and phosphoribulokinase support for a complete Calvin-Benson-Bassham cycle.",
        "priority_phase": "6",
    },
    "kegg:ppu00340": {
        "module": "histidine_biosynthesis",
        "module_file": "modules/histidine_biosynthesis.yaml",
        "scope_note": "Seeded submodule; KEGG histidine metabolism also includes histidine catabolism and shared glutathione/nucleotide side nodes.",
        "priority_phase": "3",
    },
    "kegg:ppu00020": {
        "module": "tca_cycle",
        "module_file": "modules/tca_cycle.yaml",
        "scope_note": "TCA module seeded; PSEPK batch distinguishes strict cyclic steps from pyruvate dehydrogenase, pyruvate carboxylase, and methylcitrate side-branch nodes.",
        "priority_phase": "1",
    },
    "kegg:ppu00030": {
        "module": "pentose_phosphate_pathway",
        "module_file": "modules/pentose_phosphate_pathway.yaml",
        "scope_note": "PPP module seeded; PSEPK batch distinguishes strict oxidative/non-oxidative PPP enzymes from ED, gluconate, ribose/PRPP, and sugar-phosphate side nodes.",
        "priority_phase": "1",
    },
    "kegg:ppu00040": {
        "module": "pentose_glucuronate_interconversions",
        "module_file": "modules/pentose_glucuronate_interconversions.yaml",
        "scope_note": "Boundary module for KEGG pentose/glucuronate map; distinguishes PPP rpe, UDP-sugar branch nodes, and candidate sugar-acid degradation enzymes.",
        "priority_phase": "1",
    },
    "kegg:ppu00052": {
        "module": "galactose_leloir_pathway",
        "module_file": "modules/galactose_leloir_pathway.yaml",
        "scope_note": "Seeded Leloir submodule; KEGG galactose metabolism also includes phosphomutases, UDP-glucose generation, and cell-envelope/nucleotide-sugar side nodes.",
        "priority_phase": "1",
    },
    "kegg:ppu00053": {
        "module": "hexuronate_aldarate_catabolism",
        "module_file": "modules/hexuronate_aldarate_catabolism.yaml",
        "scope_note": "Seeded free-hexuronate/aldarate catabolism submodule; KEGG ascorbate/aldarate also includes nucleotide-sugar side nodes and overlapping KGSADH candidates.",
        "priority_phase": "1",
    },
    "kegg:ppu00051": {
        "module": "fructose_mannose_metabolism",
        "module_file": "modules/fructose_mannose_metabolism.yaml",
        "scope_note": "Boundary module for fructose PTS entry, GDP-mannose/alginate precursor biosynthesis, alginate polymer handling, and LPS/O-antigen GDP-D-rhamnose side nodes; KEGG also includes shared lower-carbon enzymes covered by central-carbon modules.",
        "priority_phase": "1",
    },
    "kegg:ppu00061": {
        "module": "fatty_acid_biosynthesis",
        "module_file": "modules/fatty_acid_biosynthesis.yaml",
        "scope_note": "Type-II fatty acid biosynthesis module centered on acetyl-CoA carboxylase, malonyl-ACP formation, acyl-ACP elongation, reduction/dehydration, and unsaturated-fatty-acid branch enzymes; KEGG also includes acyl-CoA ligases and weak SDR spillover candidates.",
        "priority_phase": "1",
    },
    "kegg:ppu00071": {
        "module": "bacterial_fatty_acid_beta_oxidation",
        "module_file": "modules/bacterial_fatty_acid_beta_oxidation.yaml",
        "scope_note": "Seeded bacterial beta-oxidation/degradation module distinguishing acyl-CoA activation, beta-oxidation spiral enzymes, unresolved acyl-CoA dehydrogenase paralogs, alkane/rubredoxin side nodes, and unrelated KEGG spillovers.",
        "priority_phase": "1",
    },
    "kegg:ppu00074": {
        "module": "mycolic_acid_biosynthesis",
        "module_file": "modules/mycolic_acid_biosynthesis.yaml",
        "taxon_research_path": "projects/P_PUTIDA/deep-research/PSEPK__mycolic-acid-biosynthesis__ppu00074-deep-research-falcon.md",
        "scope_note": "Boundary/absence module: PSEPK ppu00074 contains only PP_1183 and fabD, which support siderophore carrier-protein activation and FAS-II malonyl-ACP supply rather than a satisfiable mycolic-acid pathway.",
        "priority_phase": "1",
    },
    "kegg:ppu00130": {
        "module": "ubiquinone_biosynthesis",
        "module_file": "modules/ubiquinone_biosynthesis.yaml",
        "scope_note": "Seeded ubiquinone biosynthesis module; KEGG ppu00130 also includes other terpenoid-quinone, generic quinone reductase, homogentisate, and acyl-CoA thioesterase side nodes.",
        "priority_phase": "4",
    },
    "kegg:ppu00900": {
        "module": "terpenoid_backbone_biosynthesis",
        "module_file": "modules/terpenoid_backbone_biosynthesis.yaml",
        "scope_note": "Seeded bacterial MEP/DOXP terpenoid-backbone module; KEGG ppu00900 also includes UbiX cofactor chemistry and thiolase/mevalonate-route spillovers.",
        "priority_phase": "4",
    },
    "kegg:ppu00906": {
        "module": "carotenoid_biosynthesis_boundary",
        "module_file": "modules/carotenoid_biosynthesis_boundary.yaml",
        "scope_note": "Boundary/partial module: PSEPK ppu00906 contains only crtZ/PP_3246, supporting a predicted beta-carotene hydroxylase/xanthophyll-tailoring step rather than a complete carotenoid biosynthesis pathway.",
        "priority_phase": "4",
    },
    "kegg:ppu00907": {
        "module": "pinene_camphor_geraniol_degradation_boundary",
        "module_file": "modules/pinene_camphor_geraniol_degradation_boundary.yaml",
        "scope_note": "Boundary/absence module: PSEPK ppu00907 contains HMG-CoA lyase paralogs and broadly reused CoA-thioester beta-oxidation/hydration enzymes, but no route-defining pinene, camphor, or geraniol upper-pathway enzymes.",
        "priority_phase": "4",
    },
    "kegg:ppu00730": {
        "module": "thiamine_biosynthesis",
        "module_file": "modules/thiamine_biosynthesis.yaml",
        "scope_note": "Seeded thiamine diphosphate biosynthesis module; KEGG ppu00730 also includes DXP supply, sulfur-transfer context, thiamine salvage hydrolases, and broad nucleotide/ribosome side nodes.",
        "priority_phase": "4",
    },
    "kegg:ppu00740": {
        "module": "riboflavin_biosynthesis",
        "module_file": "modules/riboflavin_biosynthesis.yaml",
        "scope_note": "Seeded riboflavin/FMN/FAD biosynthesis module; KEGG ppu00740 also includes FMN reductases, cobalamin dimethylbenzimidazole synthesis, nucleotide hydrolase, haloacid dehalogenase, and UbiX prenyl-FMN side nodes.",
        "priority_phase": "4",
    },
    "kegg:ppu00750": {
        "module": "vitamin_b6_metabolism",
        "module_file": "modules/vitamin_b6_metabolism.yaml",
        "scope_note": "Seeded vitamin B6/PLP metabolism module; KEGG ppu00750 includes de novo PNP/PLP formation, salvage phosphorylation, and shared threonine/serine/erythrose precursor-side nodes.",
        "priority_phase": "4",
    },
    "kegg:ppu00760": {
        "module": "nad_biosynthesis_and_nicotinate_metabolism",
        "module_file": "modules/nad_biosynthesis_and_nicotinate_metabolism.yaml",
        "scope_note": "Seeded NAD biosynthesis/salvage and nicotinate metabolism module; KEGG ppu00760 combines de novo NAD formation, nicotinate salvage, NADP/transhydrogenase redox interconversion, nicotinate catabolism, and nucleotide/central-metabolism side nodes.",
        "priority_phase": "4",
    },
    "kegg:ppu00770": {
        "module": "pantothenate_and_coa_biosynthesis",
        "module_file": "modules/pantothenate_and_coa_biosynthesis.yaml",
        "scope_note": "Seeded pantothenate and CoA biosynthesis module; KEGG ppu00770 combines the strict pantothenate/CoA route with branched-chain amino-acid precursor supply, beta-alanine side routes, nucleotide hydrolases, and acyl-carrier protein/cofactor side nodes.",
        "priority_phase": "4",
    },
    "kegg:ppu00780": {
        "module": "biotin_metabolism_boundary",
        "module_file": "modules/biotin_metabolism_boundary.yaml",
        "scope_note": "Seeded biotin metabolism boundary module; KEGG ppu00780 combines the BioC/BioH/BioF/BioA/BioD/BioB biotin biosynthesis route and BirA biotin ligase/repressor context with fatty-acid/SDR side nodes drawn in through acyl-ACP pimelate precursor chemistry.",
        "priority_phase": "4",
    },
    "kegg:ppu00785": {
        "module": "lipoic_acid_metabolism_boundary",
        "module_file": "modules/lipoic_acid_metabolism_boundary.yaml",
        "scope_note": "Seeded lipoic acid metabolism boundary module; KEGG ppu00785 combines LipB/LipA endogenous protein lipoylation with lipoate-dependent pyruvate, 2-oxoglutarate, branched-chain 2-oxoacid, glycine-cleavage, acetoin-cleavage, and Lpd redox context.",
        "priority_phase": "4",
    },
    "kegg:ppu00860": {
        "module": "porphyrin_metabolism_boundary",
        "module_file": "modules/porphyrin_metabolism_boundary.yaml",
        "scope_note": "Seeded porphyrin/tetrapyrrole boundary module; KEGG ppu00860 combines the heme/protoporphyrin biosynthetic spine, heme O/heme A maturation, cobalamin/corrinoid biosynthesis, siroheme biosynthesis, heme oxygenase/utilization, bacterioferritin/iron-storage, and unresolved HemX-family side nodes.",
        "priority_phase": "4",
    },
    "kegg:ppu00790": {
        "module": "folate_biosynthesis",
        "module_file": "modules/folate_biosynthesis.yaml",
        "scope_note": "Seeded folate biosynthesis module; KEGG ppu00790 combines strict pterin/pABA-to-THF formation with queuosine, molybdenum cofactor, tetrahydrobiopterin/phenylalanine hydroxylase, riboflavin, and MobA-like side nodes.",
        "priority_phase": "4",
    },
    "kegg:ppu00670": {
        "module": "one_carbon_by_folate",
        "module_file": "modules/one_carbon_by_folate.yaml",
        "scope_note": "Seeded one-carbon-by-folate module; KEGG ppu00670 combines folate one-carbon carrier interconversion and folate-dependent nucleotide/methyl reactions with glycine-cleavage, methionine-cycle, betaine, and lipoamide side nodes.",
        "priority_phase": "4",
    },
    "kegg:ppu00190": {
        "module": "oxphos",
        "module_file": "modules/oxphos.yaml",
        "scope_note": "Seeded oxidative phosphorylation module; KEGG ppu00190 combines respiratory electron-entry complexes, terminal oxidases, ATP synthase, and phosphate/polyphosphate side nodes that need strict boundary review in PSEPK.",
        "priority_phase": "5",
    },
    "kegg:ppu00910": {
        "module": "nitrogen_cycle",
        "module_file": "modules/nitrogen_cycle.yaml",
        "scope_note": "Seeded nitrogen-cycle/nitrogen-metabolism module; KEGG ppu00910 combines assimilatory nitrate/nitrite reduction, denitrification and nitric-oxide response nodes, cyanate/nitrile side chemistry, glutamine synthetase assimilation, and carbonic-anhydrase spillovers.",
        "priority_phase": "5",
    },
    "kegg:ppu00920": {
        "module": "sulfur_metabolism_boundary",
        "module_file": "modules/sulfur_metabolism_boundary.yaml",
        "scope_note": "Boundary module: PSEPK ppu00920 combines sulfate/thiosulfate import and assimilatory sulfate reduction, taurine and alkanesulfonate import/desulfonation, sulfide and cytochrome-linked sulfur redox side nodes, sulfurtransferase chemistry, methionine/cysteine side reactions, and organosulfur CoA/AMP candidates; it is now extended with the PP_0225-PP_0227 cystine/sulfur-compound ABC import sub-batch from ppu02010.",
        "priority_phase": "5",
    },
    "kegg:ppu00930": {
        "module": "caprolactam_degradation_boundary",
        "module_file": "modules/caprolactam_degradation_boundary.yaml",
        "scope_note": "Boundary/absence module: PSEPK ppu00930 contains only fadB, PP_2217, and paaF shared CoA-thioester hydratase/beta-oxidation side enzymes, not route-defining caprolactam upper-pathway enzymes.",
        "priority_phase": "7",
    },
    "kegg:ppu00946": {
        "module": "flavonoid_degradation_boundary",
        "module_file": "modules/flavonoid_degradation_boundary.yaml",
        "scope_note": "Boundary/uncertain module: PSEPK ppu00946 contains bglX plus a sparse PP_3195-PP_3206 hydrolase/redox/cupin/dehydratase cluster, but no resolved flavonoid-degradation route.",
        "priority_phase": "7",
    },
    "kegg:ppu00970": {
        "module": "aminoacyl_trna_biosynthesis",
        "module_file": "modules/aminoacyl_trna_biosynthesis.yaml",
        "scope_note": "Seeded aminoacyl-tRNA biosynthesis module covering canonical aminoacyl-tRNA synthetases, GatCAB indirect Asn/Gln-tRNA transamidation, fmt initiator Met-tRNA formylation, selenocysteine-tRNA side chemistry, and unresolved PP_0613 amidase-family side context.",
        "priority_phase": "7",
    },
    "kegg:ppu00975": {
        "module": "siderophore_biosynthesis_boundary",
        "module_file": "modules/siderophore_biosynthesis_boundary.yaml",
        "scope_note": "Boundary/partial module: PSEPK ppu00975 contains pvdH, PP_2800, and pvdY precursor/tailoring genes associated with siderophore biosynthesis, but not the complete pyoverdine NRPS assembly or siderophore export pathway.",
        "priority_phase": "7",
    },
    "kegg:ppu00996": {
        "module": "alkaloid_biosynthesis_boundary",
        "module_file": "modules/alkaloid_biosynthesis_boundary.yaml",
        "scope_note": "Boundary/absence module: PSEPK ppu00996 contains only PP_3358 hydroxycinnamoyl-CoA hydratase-lyase, supporting hydroxycinnamate/vanillin side metabolism rather than complete alkaloid biosynthesis.",
        "priority_phase": "7",
    },
    "kegg:ppu00999": {
        "module": "plant_secondary_metabolite_biosynthesis_boundary",
        "module_file": "modules/plant_secondary_metabolite_biosynthesis_boundary.yaml",
        "scope_note": "Boundary/absence module: PSEPK ppu00999 contains shikimate dehydrogenase paralogs, bglX beta-glucosidase, and metK SAM synthesis, supporting broad precursor/side-node chemistry rather than plant secondary metabolite biosynthesis.",
        "priority_phase": "7",
    },
    "kegg:ppu01040": {
        "module": "unsaturated_fatty_acid_biosynthesis_boundary",
        "module_file": "modules/unsaturated_fatty_acid_biosynthesis_boundary.yaml",
        "scope_note": "Boundary/side-node module: PSEPK ppu01040 contains tesA, tesB, and PP_5331 lipid ester/acyl-thioester hydrolases, not the FabA/FabB unsaturated-acyl-ACP biosynthesis branch already covered by fatty_acid_biosynthesis.",
        "priority_phase": "7",
    },
    "kegg:ppu01053": {
        "module": "siderophore_biosynthesis_boundary",
        "module_file": "modules/siderophore_biosynthesis_boundary.yaml",
        "scope_note": "Boundary/partial module extension: PSEPK ppu01053 contains PP_1183 EntD-family carrier-protein phosphopantetheinyltransferase and PP_2170 chorismate mutase precursor context, not a complete siderophore-group NRPS pathway.",
        "priority_phase": "7",
    },
    "kegg:ppu01320": {
        "module": "sulfur_metabolism_boundary",
        "module_file": "modules/sulfur_metabolism_boundary.yaml",
        "scope_note": "Boundary module reuse: PSEPK ppu01320 sulfur-cycle membership is covered by sulfur_metabolism_boundary, combining sulfate activation/reduction, sulfite reductase components, SoxYZ/cytochrome sulfur-redox boundary nodes, and cysteine synthesis rather than a complete standalone sulfur cycle.",
        "priority_phase": "7",
    },
    "kegg:ppu01501": {
        "module": "beta_lactam_resistance_boundary",
        "module_file": "modules/beta_lactam_resistance_boundary.yaml",
        "scope_note": "Boundary resistance module: PSEPK ppu01501 combines AmpC beta-lactam hydrolysis, AmpG/NagZ cell-wall recycling, PBP beta-lactam targets, RND/MFP/OMF efflux systems, and OprD/opmQ permeability/export context rather than a single linear pathway.",
        "priority_phase": "7",
    },
    "kegg:ppu01502": {
        "module": "vancomycin_resistance_boundary",
        "module_file": "modules/vancomycin_resistance_boundary.yaml",
        "scope_note": "Boundary/absence resistance module: PSEPK ppu01502 contains DadX, DdlA/DdlB, MurF, MraY, and MurG peptidoglycan precursor enzymes, not a VanHAX D-Ala-D-Lac vancomycin-resistance pathway.",
        "priority_phase": "7",
    },
    "kegg:ppu01503": {
        "module": "cationic_antimicrobial_peptide_resistance_boundary",
        "module_file": "modules/cationic_antimicrobial_peptide_resistance_boundary.yaml",
        "scope_note": "Boundary resistance module: PSEPK ppu01503 combines phosphatidylglycerol lysylation, LPS/lipid A context, PhoPQ/Cpx-like regulation, RND efflux, periplasmic folding/proteolysis, and peptidoglycan remodeling rather than a single CAMP-resistance pathway.",
        "priority_phase": "7",
    },
    "kegg:ppu03008": {
        "module": "ribosome_biogenesis_eukaryotes_boundary",
        "module_file": "modules/ribosome_biogenesis_eukaryotes_boundary.yaml",
        "scope_note": "Boundary/absence module: PSEPK ppu03008 contains rnc RNase III/rRNA processing, orn oligoribonuclease/RNA turnover, and PP_2912 RIO-type kinase-like context, not evidence for a eukaryotic ribosome-biogenesis pathway in KT2440.",
        "priority_phase": "8",
    },
    "kegg:ppu03018": {
        "module": "bacterial_rna_degradation",
        "module_file": "modules/bacterial_rna_degradation.yaml",
        "scope_note": "Boundary module: PSEPK ppu03018 has a strict RppH/RNase E/PcnB/PNPase/RNase R RNA-turnover core plus DEAD-box RNA helicase remodeling, with Hfq/Rho regulatory context and enolase/chaperone/polyphosphate/RecQ side or spillover nodes.",
        "priority_phase": "8",
        "batch_status": "PARTITIONED",
    },
    "kegg:ppu03020": {
        "module": "bacterial_rna_polymerase_core",
        "module_file": "modules/bacterial_rna_polymerase_core.yaml",
        "scope_note": "Compact bacterial DNA-directed RNA polymerase core module; KEGG ppu03020 contains rpoA, rpoB, rpoC, and rpoZ core subunits, while sigma factors and pathway-specific transcription regulators remain separate regulatory contexts.",
        "priority_phase": "8",
    },
    "kegg:ppu03030": {
        "module": "bacterial_dna_replication",
        "module_file": "modules/bacterial_dna_replication.yaml",
        "scope_note": "Boundary module: PSEPK ppu03030 has a strict DnaB/DnaG primosome, SSB, Pol III core/clamp-loader/proofreading, RNase H/PolA RNA-primer processing, and LigA nick-sealing core, plus PP_3893, DnaQ-like exonuclease candidates, and LigB as unresolved boundary side nodes.",
        "priority_phase": "8",
        "batch_status": "PARTITIONED",
    },
    "kegg:ppu03060": {
        "module": "bacterial_protein_export",
        "module_file": "modules/bacterial_protein_export.yaml",
        "scope_note": "Boundary module: PSEPK ppu03060 combines SecA/SecYEG/SecDF-YajC/SecB Sec export, Ffh/FtsY SRP targeting, YidC membrane insertion, LepB/LspA signal-peptide processing, and two TatABC-like loci; type I secretion and LolCDE are neighboring modules.",
        "priority_phase": "8",
        "batch_status": "PARTITIONED",
    },
    "kegg:ppu03070": {
        "module": "bacterial_secretion_system_boundary",
        "module_file": "modules/bacterial_secretion_system_boundary.yaml",
        "scope_note": "Boundary module: PSEPK ppu03070 combines Xcp/Gsp type-II secretion components, a PP_1449/PP_1450 two-partner/type Vb secretion pair, multiple VgrG/Hcp/DotU/TssJ/TssM/ClpV type-VI secretion loci, and a PP_4926/CyaB type-I secretion tail; Sec/Tat/SRP/YidC inner-membrane export remains in ppu03060.",
        "priority_phase": "8",
        "batch_status": "PARTITIONED",
    },
    "kegg:ppu03250": {
        "module": "viral_life_cycle_hiv1_boundary",
        "module_file": "modules/viral_life_cycle_hiv1_boundary.yaml",
        "scope_note": "Boundary/absence module: PSEPK ppu03250 contains only ppiA, a cyclophilin-family peptidyl-prolyl cis-trans isomerase/protein-folding enzyme, not evidence for an HIV-1 or viral life-cycle pathway in KT2440.",
        "priority_phase": "8",
    },
    "kegg:ppu03410": {
        "module": "bacterial_base_excision_repair",
        "module_file": "modules/bacterial_base_excision_repair.yaml",
        "scope_note": "Boundary module: PSEPK ppu03410 includes damage-specific DNA glycosylases, AP-site/ExoIII-like processing nucleases, and shared PolA/LigA/LigB repair-synthesis and nick-sealing machinery; RecJ is retained as a shared repair exonuclease side node.",
        "priority_phase": "8",
    },
    "kegg:ppu03420": {
        "module": "bacterial_nucleotide_excision_repair",
        "module_file": "modules/bacterial_nucleotide_excision_repair.yaml",
        "scope_note": "Boundary module: PSEPK ppu03420 has a strict UvrABC nucleotide-excision repair core with Mfd transcription-coupled input, plus UvrD, PolA, NAD-dependent ligase, PP_2839 helicase, and PP_3087 UvrA-like ATPase side nodes.",
        "priority_phase": "8",
    },
    "kegg:ppu03430": {
        "module": "bacterial_mismatch_repair",
        "module_file": "modules/bacterial_mismatch_repair.yaml",
        "scope_note": "Boundary module: PSEPK ppu03430 has a strict MutS/MutL mismatch-repair core plus UvrD, exonuclease, SSB, Pol III/clamp-loader/proofreading, and ligase side nodes shared with replication and other DNA-repair pathways.",
        "priority_phase": "8",
    },
    "kegg:ppu03440": {
        "module": "bacterial_homologous_recombination",
        "module_file": "modules/bacterial_homologous_recombination.yaml",
        "scope_note": "Boundary module: PSEPK ppu03440 has a strict RecA/RecFOR, RecBCD, RuvABC, RecG, and PriA homologous-recombination core plus SSB, RecJ, PolA, DnaQ-like exonucleases, and Pol III replication-restart side nodes shared with DNA replication and excision-repair pathways.",
        "priority_phase": "8",
    },
    "kegg:ppu03450": {
        "module": "bacterial_non_homologous_end_joining",
        "module_file": "modules/bacterial_non_homologous_end_joining.yaml",
        "scope_note": "Compact bacterial Ku/LigD non-homologous end-joining module; KEGG ppu03450 contains ku and ligD, supporting double-strand-break repair by NHEJ rather than a broad DNA repair bucket.",
        "priority_phase": "8",
    },
    "kegg:ppu04146": {
        "module": "peroxisome_boundary",
        "module_file": "modules/peroxisome_boundary.yaml",
        "scope_note": "Boundary/absence module: PSEPK ppu04146 contains cytoplasmic ROS detoxification, fatty-acid activation, isocitrate dehydrogenase, HMG-CoA lyase, and NudC side nodes, not evidence for a bacterial peroxisome organelle or peroxisome-biogenesis pathway.",
        "priority_phase": "8",
    },
    "kegg:ppu04148": {
        "module": "efferocytosis_boundary",
        "module_file": "modules/efferocytosis_boundary.yaml",
        "scope_note": "Boundary/absence module: PSEPK ppu04148 contains only speC ornithine decarboxylase/polyamine context and petA respiratory complex III context, not evidence for eukaryotic efferocytosis in KT2440.",
        "priority_phase": "8",
    },
    "kegg:ppu04141": {
        "module": "protein_processing_er_boundary",
        "module_file": "modules/protein_processing_er_boundary.yaml",
        "scope_note": "Boundary/absence module: PSEPK ppu04141 contains PP_3234 and PP_3312 HSP20-family small heat shock proteins plus htpG bacterial Hsp90-family chaperone context, not evidence for endoplasmic-reticulum protein processing in KT2440.",
        "priority_phase": "8",
    },
    "kegg:ppu04156": {
        "module": "integrated_stress_response_boundary",
        "module_file": "modules/integrated_stress_response_boundary.yaml",
        "scope_note": "Boundary/absence module: PSEPK ppu04156 contains GroEL/DnaK/HtpG bacterial heat-shock chaperone context plus PP_5211 glutathione gamma-glutamylcyclotransferase context, not evidence for eukaryotic integrated stress response signaling in KT2440.",
        "priority_phase": "8",
    },
    "kegg:ppu04980": {
        "module": "cobalamin_transport_metabolism_boundary",
        "module_file": "modules/cobalamin_transport_metabolism_boundary.yaml",
        "scope_note": "Boundary module: PSEPK ppu04980 contains pduO corrinoid/cobalamin adenosyltransferase context and metH cobalamin-dependent methionine synthase context, not evidence for a complete cobalamin transport pathway.",
        "priority_phase": "8",
    },
    "kegg:ppu04981": {
        "module": "folate_transport_metabolism_boundary",
        "module_file": "modules/folate_transport_metabolism_boundary.yaml",
        "scope_note": "Boundary module: PSEPK ppu04981 contains folate/one-carbon-dependent enzymes (glyA1/glyA2, metH, folA, thyA, fau) but no folate transporter, so the transport label is absent while metabolism overlaps folate biosynthesis, one-carbon-by-folate, cobalamin, methionine, and nucleotide contexts.",
        "priority_phase": "8",
    },
    "kegg:ppu02060": {
        "module": "phosphotransferase_system_boundary",
        "module_file": "modules/phosphotransferase_system_boundary.yaml",
        "scope_note": "Boundary module: PSEPK ppu02060 contains the fruBKA fructose PTS uptake/catabolic-entry branch plus ptsH/ptsP/ptsN HPr/Ntr regulatory phosphorelay context, not a generic all-sugar PTS transport system.",
        "priority_phase": "8",
    },
    "kegg:ppu02020": {
        "module": "",
        "module_file": "",
        "scope_note": (
            "Partitioned umbrella map: PSEPK ppu02020 contains 99 primary "
            "two-component-system genes but mixes true His-Asp two-component "
            "pairs, ECF sigma/anti-sigma systems, dicarboxylate/tricarboxylate "
            "transport regulation, metal/copper/iron response, nutrient "
            "homeostasis, pili/biofilm context, efflux systems, and side "
            "spillovers dnaA and etp, which are now curated as DNA-replication "
            "and protein-phosphatase side context. Use "
            "projects/P_PUTIDA/batches/ppu02020_two_component_system_partition.tsv "
            "to select submodule batches; do not curate ppu02020 as one "
            "satisfiable module."
        ),
        "priority_phase": "8",
        "batch_status": "PARTITIONED",
    },
    "kegg:ppu02024": {
        "module": "",
        "module_file": "",
        "scope_note": (
            "Partitioned umbrella map: PSEPK ppu02024 contains 60 primary "
            "genes and 84 total KEGG members but does not define a single "
            "LuxI/LuxR quorum-sensing module. The primary set is mostly "
            "branched-chain amino-acid ABC import, polyamine import, "
            "peptide/opine/glutathione import, QseBC-like two-component "
            "regulation, RND efflux, phosphonate import, surface adhesion, and "
            "small side-context spillovers. The RND multidrug efflux side "
            "bucket, QseBC-like two-component regulation bucket, "
            "phosphonate/AEP ABC import bucket, peptide/opine/glutathione "
            "ABC import bucket, polyamine ABC import bucket, and the three "
            "singleton side-context buckets are first-pass curated; use "
            "projects/P_PUTIDA/batches/ppu02024_quorum_sensing_partition.tsv "
            "to inspect the nine boundary buckets, and do not curate ppu02024 "
            "as one satisfiable module."
        ),
        "priority_phase": "8",
        "batch_status": "PARTITIONED",
    },
    "kegg:ppu02025": {
        "module": "",
        "module_file": "",
        "scope_note": (
            "Partitioned umbrella map: PSEPK ppu02025 contains 43 primary "
            "genes and 62 total KEGG members from the Pseudomonas aeruginosa "
            "biofilm-formation map. The primary set mixes global Gac/Csr/Crp "
            "regulation, Wsp-like chemotaxis/c-di-GMP signaling, c-di-GMP "
            "turnover, T6SS/biofilm context, orphan regulatory sensors, and "
            "Pil/Chp twitching regulation. The Wsp-like surface-sensing/c-di-GMP, "
            "c-di-GMP turnover, Pil/Chp twitching-regulation, Gac/Csr/Crp "
            "global-regulation, T6SS secretion-boundary context, and orphan "
            "regulatory-sensor sub-buckets are first-pass curated. Use "
            "projects/P_PUTIDA/batches/ppu02025_biofilm_formation_pseudomonas_partition.tsv "
            "to select submodule batches; do not curate ppu02025 as one "
            "satisfiable module."
        ),
        "priority_phase": "8",
        "batch_status": "PARTITIONED",
    },
    "kegg:ppu02030": {
        "module": "",
        "module_file": "",
        "scope_note": (
            "Partitioned umbrella map: PSEPK ppu02030 contains 41 primary "
            "genes and 48 total KEGG members from the bacterial chemotaxis "
            "map. The primary set mixes named/known MCP receptors, orphan "
            "MCP and aerotaxis receptors, core Che signal-transduction "
            "components, adaptation/accessory proteins, and periplasmic "
            "binding-protein transport spillovers. First-pass chemotaxis "
            "sub-batches are curated for core Che signaling, adaptation/"
            "accessory proteins, named receptors, and orphan MCP/aerotaxis "
            "receptors; transport-binding spillovers remain assigned to "
            "transport modules. Do not curate ppu02030 as one satisfiable "
            "module."
        ),
        "priority_phase": "8",
        "batch_status": "PARTITIONED",
    },
    "kegg:ppu02040": {
        "module": "",
        "module_file": "",
        "scope_note": (
            "Partitioned flagellar-assembly map: PSEPK ppu02040 contains 47 "
            "primary genes. The set is biologically coherent but too broad for "
            "one first-pass curation batch, mixing flagellar export/assembly "
            "proteins, basal-body/hook/filament components, motor/switch/stator "
            "proteins, sigma/master regulators, and nonflagellar "
            "transport/envelope spillovers such as fliY and PP_5157. The "
            "flagellar_motor_switch_stator, "
            "flagellar_export_assembly_chaperones, "
            "flagellar_basal_body_hook_filament, and "
            "flagellar_regulation_sigma_master_control sub-batches, plus the "
            "nonflagellar_transport_envelope_spillovers boundary bucket, are complete as "
            "modules/flagellar_motor_switch_stator_boundary.yaml, "
            "modules/flagellar_export_assembly_boundary.yaml, "
            "modules/flagellar_basal_body_hook_filament_boundary.yaml, and "
            "modules/flagellar_regulation_boundary.yaml, with "
            "modules/transport_envelope_spillover_boundary.yaml documenting "
            "out-of-apparatus spillovers."
        ),
        "priority_phase": "8",
        "batch_status": "PARTITIONED",
    },
    "kegg:ppu03010": {
        "module": "",
        "module_file": "",
        "scope_note": (
            "Partitioned ribosome map: PSEPK ppu03010 contains 54 primary "
            "genes, all ribosomal proteins. There is no unknown/spillover "
            "bucket, but the first-pass curation unit should be smaller than "
            "the full ribosome. The 30S and 50S protein sub-batches are "
            "complete as modules/bacterial_30s_ribosomal_subunit_boundary.yaml "
            "and modules/bacterial_50s_ribosomal_subunit_boundary.yaml; use "
            "projects/P_PUTIDA/batches/ppu03010_bacterial_ribosome_partition.tsv "
            "as the reproducible split record."
        ),
        "priority_phase": "8",
        "batch_status": "PARTITIONED",
    },
    "kegg:ppu04122": {
        "module": "",
        "module_file": "",
        "scope_note": (
            "Partitioned sulfur-relay map: PSEPK ppu04122 contains 19 primary "
            "genes and 22 total KEGG members. The primary set mixes "
            "molybdopterin/MoCo sulfur-carrier chemistry, Tus/MnmA tRNA "
            "thiolation, ThiS thiamine sulfur-carrier context, and general "
            "rhodanese/mercaptopyruvate sulfurtransferase side nodes. Use "
            "projects/P_PUTIDA/batches/ppu04122_sulfur_relay_system_partition.tsv "
            "to select submodule batches; do not curate ppu04122 as one "
            "generic sulfur-relay module."
        ),
        "priority_phase": "8",
        "batch_status": "PARTITIONED",
    },
    "kegg:ppu02010": {
        "module": "",
        "module_file": "",
        "scope_note": (
            "Partitioned umbrella map: PSEPK ppu02010 contains 207 ABC-transporter "
            "genes across many substrate systems and should not be curated as one "
            "satisfiable pathway. Completed sub-batches: PP_0112-PP_0114 MetNIQ "
            "methionine import plus PP_0219-PP_0221 MetNIQ-like methionine import "
            "in methionine_import_boundary, PP_0117-PP_0120 ZnuABC zinc import in "
            "zinc_import_boundary, PP_3801-PP_3803 Znu-like cation/zinc import in "
            "zinc_import_boundary, PP_0824-PP_0827 phosphonate import in "
            "phosphonate_phosphinate_metabolism, PP_0225-PP_0227 "
            "cystine/sulfur-compound import in sulfur_metabolism_boundary, "
            "PP_0280-PP_0283 arginine/ornithine import in "
            "arginine_ornithine_abc_import_boundary, PP_4483-PP_4486 "
            "His/ArgT basic-amino-acid import in "
            "arginine_ornithine_abc_import_boundary, PP_1297-PP_1300 "
            "YhdWXYZ unresolved amino-acid ABC import in "
            "yhdwxyz_amino_acid_abc_import_boundary, PP_0294-PP_0296 plus "
            "PP_0304, PP_0076, betX/PP_1741, PP_0868-PP_0871, opuA-PP_2775, "
            "and PP_3558-PP_3559 compatible-solute import/binding in "
            "osmoprotectant_compatible_solute_transport_boundary, PP_0873/potF-I "
            "plus PP_2195, potF-II, PP_3719, potF-III, and potF-IV "
            "PotF-like putrescine/polyamine binding in polyamine_transport_boundary, "
            "PP_5177-PP_5181 Spu/Pot spermidine/putrescine ABC import in "
            "polyamine_transport_boundary, "
            "PP_0878-PP_0885 Dpp dipeptide import in "
            "dipeptide_abc_import_boundary, PP_3076-PP_3078, "
            "PP_4146-PP_4150, and dppA-IV Yej/Dpp-like peptide ABC "
            "import candidates in yej_dpp_like_peptide_abc_import_boundary, "
            "PP_1068-PP_1071 GltIJKL "
            "glutamate/aspartate import in glutamate_aspartate_abc_import_boundary, "
            "PP_0615-PP_0619 branched-chain amino-acid import in "
            "branched_chain_amino_acid_abc_import_boundary, "
            "PP_2748-PP_2753 branched-chain amino-acid import in "
            "branched_chain_amino_acid_abc_import_boundary, "
            "PP_2767-PP_2770 branched-chain amino-acid import in "
            "branched_chain_amino_acid_abc_import_boundary, "
            "PP_1137-PP_1141 LivFGMHK branched-chain amino-acid import in "
            "branched_chain_amino_acid_abc_import_boundary, PP_4863-PP_4867 "
            "Bra/Liv branched-chain amino-acid import in "
            "branched_chain_amino_acid_abc_import_boundary, "
            "PP_2656-PP_2659 PstSACB plus "
            "PP_5326-PP_5329 Pst-like phosphate import in phosphate_import_boundary, "
            "PP_3828-PP_3830 ModABC molybdate import in "
            "molybdate_abc_import_boundary, "
            "PP_4841-PP_4845 UrtABCDE urea import in "
            "urea_abc_import_boundary, "
            "PP_2154-PP_2156 LolCDE lipoprotein localization in "
            "lipoprotein_lolcde_localization_boundary, "
            "PP_4324-PP_4327 CcmABCD heme export/cytochrome c maturation in "
            "ccm_heme_export_cytochrome_c_maturation_boundary, "
            "pvdT/pvdE pyoverdine export and precursor-export context, "
            "PP_0958-PP_0962 Mla/Ttg2 phospholipid transport/lipid asymmetry in "
            "mla_phospholipid_transport_boundary, "
            "PP_0140-PP_0142 Mce/MlaD-MlaE-like phospholipid transport candidate "
            "in mce_mlad_mlae_like_phospholipid_transport_boundary, "
            "lptB plus PP_0982/PP_0983 LptF/LptG and msbA with LptA/C/D/E "
            "context in lpt_lps_transport_boundary, "
            "PP_1778-PP_1779 unresolved LPS/polysaccharide ABC export candidate "
            "as a separate lpt_lps_transport_boundary part, "
            "ftsX/ftsE FtsEX cell-division ABC-like complex in "
            "ftsex_cell_division_boundary, "
            "plpB/PP_5165 NlpA-family lipoprotein curated as an unresolved "
            "adjacent envelope lipoprotein rather than added to sulfate import, "
            "PP_1015-PP_1018 Gts glucose import in glucose_import_boundary, "
            "PP_2260-PP_2264 unresolved sugar/glycerol-phosphate-like import in "
            "sugar_glycerol_phosphate_import_boundary, PP_2454-PP_2459 Rbs "
            "ribose import/accessory utilization plus PP_2757-PP_2761 second "
            "ribose-like RbsABC comparison in ribose_import_boundary, and "
            "PP_3342-PP_3346 NikABCDE nickel import in nickel_import_boundary, "
            "and PP_4881-PP_4882, PP_5135-PP_5137, and PP_5195-fbpA "
            "ferric/iron ABC import candidates in ferric_iron_abc_import_boundary. "
            "Remaining clusters should be handled by substrate class with an "
            "unknown/general ABC bucket retained."
        ),
        "priority_phase": "7",
        "batch_status": "PARTITIONED",
    },
    "unipathway:UPA00028": {
        "module": "pantothenate_and_coa_biosynthesis",
        "module_file": "modules/pantothenate_and_coa_biosynthesis.yaml",
        "taxon_research_path": "projects/P_PUTIDA/deep-research/PSEPK__pantothenate_and_coa_biosynthesis__ppu00770-deep-research-falcon.md",
        "scope_note": "UniPathway pantothenate biosynthesis cross-references the PanB/PanC route and four 2-dehydropantoate reductase candidates, including PP_4452 which is not in the KEGG ppu00770 bucket.",
        "priority_phase": "4",
    },
    "unipathway:UPA00060": {
        "module": "thiamine_biosynthesis",
        "module_file": "modules/thiamine_biosynthesis.yaml",
        "taxon_research_path": "projects/P_PUTIDA/deep-research/PSEPK__thiamine_biosynthesis__ppu00730-deep-research-falcon.md",
        "scope_note": "UniPathway thiamine biosynthesis support bucket. Most UPA00060 members are already in KEGG ppu00730; the UniPathway-primary `pet`/PP_3185 aminopyrimidine aminohydrolase is retained as thiamine-salvage context within the existing thiamine module.",
        "priority_phase": "4",
    },
    "unipathway:UPA00094": {
        "module": "fatty_acid_biosynthesis",
        "module_file": "modules/fatty_acid_biosynthesis.yaml",
        "taxon_research_path": "projects/P_PUTIDA/deep-research/PSEPK__fatty_acid_biosynthesis__upa00094-deep-research-falcon.md",
        "scope_note": "UniPathway ACP-linked fatty-acid-biosynthesis support bucket: acpP is the phosphopantetheinylated acyl carrier protein, with accB and Fab enzymes already covered by the completed type-II fatty-acid-biosynthesis module. This maps UPA00094 to the existing FAS-II module rather than a separate pathway.",
        "priority_phase": "1",
    },
    "unipathway:UPA00098": {
        "module": "arginine_proline_metabolism",
        "module_file": "modules/arginine_proline_metabolism.yaml",
        "taxon_research_path": "projects/P_PUTIDA/deep-research/PSEPK__arginine_proline_metabolism__upa00098-deep-research-falcon.md",
        "scope_note": "UniPathway proline biosynthesis/interconversion support bucket: proB/proA/proC/proI cover glutamate-to-proline chemistry and ocd supplies the ornithine cyclodeaminase route. This is handled as a subroute within the existing broad arginine/proline metabolism module.",
        "priority_phase": "3",
    },
    "unipathway:UPA00117": {
        "module": "l_carnitine_dehydrogenation",
        "module_file": "modules/l_carnitine_dehydrogenation.yaml",
        "taxon_research_path": "projects/P_PUTIDA/deep-research/PSEPK__l_carnitine_dehydrogenation__upa00117-deep-research-falcon.md",
        "scope_note": "Compact UniPathway L-carnitine dehydrogenation module: lcdH catalyzes the cytoplasmic NAD+-dependent oxidation of L-carnitine to 3-dehydrocarnitine. Carnitine uptake and downstream 3-dehydrocarnitine utilization remain adjacent context until directly supported.",
        "priority_phase": "6",
    },
    "unipathway:UPA00191": {
        "module": "bacterial_fatty_acid_beta_oxidation",
        "module_file": "modules/bacterial_fatty_acid_beta_oxidation.yaml",
        "taxon_research_path": "projects/P_PUTIDA/deep-research/PSEPK__bacterial_fatty_acid_beta_oxidation__upa00191-deep-research-falcon.md",
        "scope_note": "UniPathway rubredoxin/electron-transfer support bucket: rubA is curated as a cytoplasmic rubredoxin electron-transfer protein in hydrocarbon/alkane oxidation context. This extends the existing alkane/rubredoxin boundary node of the bacterial fatty-acid beta-oxidation module and should not be interpreted as a core beta-oxidation spiral enzyme.",
        "priority_phase": "1",
    },
    "unipathway:UPA00659": {
        "module": "bacterial_fatty_acid_beta_oxidation",
        "module_file": "modules/bacterial_fatty_acid_beta_oxidation.yaml",
        "taxon_research_path": "projects/P_PUTIDA/deep-research/PSEPK__bacterial_fatty_acid_beta_oxidation__upa00659-deep-research-falcon.md",
        "scope_note": "UniPathway fatty-acid beta-oxidation support bucket: fadE, fadB, and fadA are already-curated beta-oxidation core enzymes, while PP_4030 is curated as a cytoplasmic enoyl-CoA hydratase/isomerase-family auxiliary candidate with a PANTHER-supported dienoyl-CoA isomerase role. This extends the existing bacterial beta-oxidation module rather than creating a separate pathway.",
        "priority_phase": "1",
    },
    "unipathway:UPA00392": {
        "module": "queuosine_biosynthesis_boundary",
        "module_file": "modules/queuosine_biosynthesis_boundary.yaml",
        "taxon_research_path": "projects/P_PUTIDA/deep-research/PSEPK__queuosine_biosynthesis_boundary__upa00392-deep-research-falcon.md",
        "scope_note": "Compact UniPathway tRNA-queuosine biosynthesis route: queF preQ1 supply plus tgt, queA, and queG tRNA-modification steps. queF is side context from the KEGG ppu00790 primary partition.",
        "priority_phase": "4",
    },
    "unipathway:UPA00212": {
        "module": "mcl_pha_monomer_supply_from_fas",
        "module_file": "modules/mcl_pha_monomer_supply_from_fas.yaml",
        "taxon_research_path": "projects/P_PUTIDA/deep-research/PSEPK__mcl_pha_monomer_supply_from_fas__upa00212-deep-research-falcon.md",
        "scope_note": "Compact UniPathway PhaG module: phaG bridges de novo fatty-acid synthesis to medium-chain-length PHA monomer supply. PhaC polymerization and beta-oxidation/PhaJ routes are adjacent PHA biology but outside the single-gene UPA00212 member set.",
        "priority_phase": "9",
    },
    "unipathway:UPA00219": {
        "module": "peptidoglycan_biosynthesis",
        "module_file": "modules/peptidoglycan_biosynthesis.yaml",
        "taxon_research_path": "projects/P_PUTIDA/deep-research/PSEPK__peptidoglycan_biosynthesis__upa00219-deep-research-falcon.md",
        "scope_note": "Broad UniPathway peptidoglycan-biosynthesis support bucket: MurA/B/C/D/E/F, Ddl paralogs, MraY/MurG, MurJ, SEDS polymerases, PBPs, and L,D-transpeptidase-like remodeling candidates belong in the existing peptidoglycan module. This is the main UniPathway route view, while UPA00544 is the separate recycling/salvage arm.",
        "priority_phase": "6",
    },
    "unipathway:UPA00232": {
        "module": "ubiquinone_biosynthesis",
        "module_file": "modules/ubiquinone_biosynthesis.yaml",
        "taxon_research_path": "projects/P_PUTIDA/deep-research/PSEPK__ubiquinone_biosynthesis__ppu00130-deep-research-falcon.md",
        "scope_note": "UniPathway ubiquinone biosynthesis support bucket. This is the strict UbiC/UbiA/UbiD/UbiX/VisC-UbiI/UbiH/Coq7/UbiE/UbiG route plus UbiB/UbiJ/UbiK accessory context already handled in the ppu00130 ubiquinone module.",
        "priority_phase": "4",
    },
    "unipathway:UPA00252": {
        "module": "porphyrin_metabolism_boundary",
        "module_file": "modules/porphyrin_metabolism_boundary.yaml",
        "taxon_research_path": "projects/P_PUTIDA/deep-research/PSEPK__porphyrin_metabolism_boundary__upa00252-deep-research-falcon.md",
        "scope_note": "UniPathway protoheme/heme support bucket: PP_0189 is a HemY_N/TPR-associated inner-membrane late protoheme-biosynthesis support protein and hemH is the ferrochelatase completing protoheme formation. This support view extends the existing porphyrin/tetrapyrrole boundary module rather than a separate pathway.",
        "priority_phase": "4",
    },
    "unipathway:UPA00544": {
        "module": "peptidoglycan_biosynthesis",
        "module_file": "modules/peptidoglycan_biosynthesis.yaml",
        "taxon_research_path": "projects/P_PUTIDA/deep-research/PSEPK__peptidoglycan_biosynthesis__upa00544-deep-research-falcon.md",
        "scope_note": "UniPathway peptidoglycan recycling/support bucket: NagZ, AnmK, MupP, AmgK, MurU, and Mpl form the MurNAc/anhMurNAc and muropeptide salvage route that returns cell-wall turnover products to UDP-MurNAc-peptide precursor supply. This is a recycling/salvage support view inside the peptidoglycan module, distinct from de novo MurA/MurB/MurC-F biosynthesis.",
        "priority_phase": "6",
    },
    "unipathway:UPA00286": {
        "module": "alginate_biosynthesis_boundary",
        "module_file": "modules/alginate_biosynthesis_boundary.yaml",
        "taxon_research_path": "projects/P_PUTIDA/deep-research/PSEPK__alginate_biosynthesis_boundary__upa00286-deep-research-falcon.md",
        "scope_note": "UniPathway alginate biosynthesis boundary bucket: AlgD precursor formation, Alg8/Alg44 polymerization/activation, AlgF/AlgJ/AlgI/AlgX/AlgG modification and maturation, AlgE/AlgK export/scaffold context, and AlgB regulation. This consolidates members split across ppu00051, ppu00543, and ppu02020 without treating them as a single enzyme-only route.",
        "priority_phase": "7",
    },
    "unipathway:UPA00345": {
        "module": "efp_translation_stall_rescue",
        "module_file": "modules/efp_translation_stall_rescue.yaml",
        "taxon_research_path": "projects/P_PUTIDA/deep-research/PSEPK__efp_translation_stall_rescue__upa00345-deep-research-falcon.md",
        "scope_note": "Compact UniPathway EF-P translation module: efp encodes cytoplasmic elongation factor P for peptide-bond synthesis and rescue of stalled/polyproline ribosomes. EarP-dependent Arg32 rhamnosylation and dTDP-rhamnose supply are activation context, not part of the single-gene UPA00345 member set.",
        "priority_phase": "8",
    },
    "unipathway:UPA00529": {
        "module": "glycine_betaine_biosynthesis_boundary",
        "module_file": "modules/glycine_betaine_biosynthesis_boundary.yaml",
        "taxon_research_path": "projects/P_PUTIDA/deep-research/PSEPK__glycine_betaine_biosynthesis_boundary__upa00529-deep-research-falcon.md",
        "scope_note": "Compact UniPathway choline-derived glycine betaine pathway with BetA/BetB catalytic biosynthesis and BetI regulatory boundary context. Transporters and unassigned choline dehydrogenase paralogs are excluded unless later evidence assigns them to this route.",
        "priority_phase": "6",
    },
    "unipathway:UPA00539": {
        "module": "pqq_biosynthesis",
        "module_file": "modules/pqq_biosynthesis.yaml",
        "taxon_research_path": "projects/P_PUTIDA/deep-research/PSEPK__pqq_biosynthesis__upa00539-deep-research-falcon.md",
        "scope_note": "Compact UniPathway PQQ biosynthesis route: pqqA precursor peptide, pqqD1/pqqD2 PqqA-binding chaperones, pqqE radical-SAM peptide cyclase, pqqF processing protease, pqqB maturation oxygenase/hydroxylase, and pqqC terminal synthase. Quinoprotein utilization and ambiguous pqqG context are excluded.",
        "priority_phase": "4",
    },
    "unipathway:UPA01010": {
        "module": "nad_biosynthesis_and_nicotinate_metabolism",
        "module_file": "modules/nad_biosynthesis_and_nicotinate_metabolism.yaml",
        "taxon_research_path": "projects/P_PUTIDA/deep-research/PSEPK__nad_biosynthesis_and_nicotinate_metabolism__ppu00760-deep-research-falcon.md",
        "scope_note": "UniPathway nicotinate catabolism support bucket. The NicA/NicB/NicC/NicX/NicD/NicF/MaiA catalytic route and NicR/NicS regulator context are already handled in the completed ppu00760 NAD/nicotinate metabolism module.",
        "priority_phase": "4",
    },
    "unipathway:UPA00637": {
        "module": "osmoregulated_periplasmic_glucan_biosynthesis",
        "module_file": "modules/osmoregulated_periplasmic_glucan_biosynthesis.yaml",
        "taxon_research_path": "projects/P_PUTIDA/deep-research/PSEPK__osmoregulated_periplasmic_glucan_biosynthesis__upa00637-deep-research-falcon.md",
        "scope_note": "Compact UniPathway OPG biosynthesis module: opgH inner-membrane GT2 glucosyltransferase plus opgG periplasmic OpgG-family glucan biosynthesis/accessory protein. Keep distinct from alginate, LPS, peptidoglycan, cellulose, and broad exopolysaccharide modules.",
        "priority_phase": "6",
    },
    "unipathway:UPA00664": {
        "module": "bacterial_lipoprotein_maturation",
        "module_file": "modules/bacterial_lipoprotein_maturation.yaml",
        "taxon_research_path": "projects/P_PUTIDA/deep-research/PSEPK__bacterial_lipoprotein_maturation__upa00664-deep-research-falcon.md",
        "scope_note": "Compact bacterial lipoprotein maturation module: lgt catalyzes the diacylglyceryl-transfer first step; lspA is the already-curated signal peptidase II middle step; lnt catalyzes the final N-acyl-transfer step. Keep separate from broad protein export and Lol lipoprotein trafficking.",
        "priority_phase": "6",
    },
    "unipathway:UPA00665": {
        "module": "bacterial_lipoprotein_maturation",
        "module_file": "modules/bacterial_lipoprotein_maturation.yaml",
        "taxon_research_path": "projects/P_PUTIDA/deep-research/PSEPK__bacterial_lipoprotein_maturation__upa00665-deep-research-falcon.md",
        "scope_note": "LspA signal peptidase II middle step in bacterial lipoprotein maturation. lspA remains primarily owned by the KEGG ppu03060 bacterial protein export partition, but its UniPathway UPA00665 cross-reference belongs in the Lgt-LspA-Lnt maturation module.",
        "priority_phase": "6",
    },
    "unipathway:UPA00666": {
        "module": "bacterial_lipoprotein_maturation",
        "module_file": "modules/bacterial_lipoprotein_maturation.yaml",
        "taxon_research_path": "projects/P_PUTIDA/deep-research/PSEPK__bacterial_lipoprotein_maturation__upa00666-deep-research-falcon.md",
        "scope_note": "Compact bacterial lipoprotein maturation module: lnt catalyzes the final apolipoprotein N-acyl-transfer step; lgt and lspA provide the upstream diacylglyceryl-transfer and signal-peptide-cleavage context. Keep separate from broad protein export and Lol lipoprotein trafficking.",
        "priority_phase": "6",
    },
    "unipathway:UPA00694": {
        "module": "bacterial_cellulose_biosynthesis",
        "module_file": "modules/bacterial_cellulose_biosynthesis.yaml",
        "taxon_research_path": "projects/P_PUTIDA/deep-research/PSEPK__bacterial_cellulose_biosynthesis__upa00694-deep-research-falcon.md",
        "scope_note": "Compact UniPathway bacterial cellulose biosynthesis bucket: bcsA is the UDP-forming cellulose synthase catalytic subunit, bcsB is the c-di-GMP-binding regulatory subunit, and PP_2638 is a BcsC/operon-C-like outer-membrane accessory protein. Keep this module distinct from the existing plant cellulose module, alginate, OPG, LPS, peptidoglycan, and broad exopolysaccharide boundary modules.",
        "priority_phase": "6",
    },
    "unipathway:UPA00729": {
        "module": "trna_ms2io6a37_hydroxylation",
        "module_file": "modules/trna_ms2io6a37_hydroxylation.yaml",
        "taxon_research_path": "projects/P_PUTIDA/deep-research/PSEPK__trna_ms2io6a37_hydroxylation__upa00729-deep-research-falcon.md",
        "scope_note": "Compact UniPathway tRNA-modification module: miaE terminal non-heme diiron monooxygenase hydroxylates ms2i6A37 in selected tRNAs to ms2io6A37. Upstream MiaA/MiaB A37 hypermodification chemistry is substrate-supply context outside the single-gene UPA00729 member set.",
        "priority_phase": "6",
    },
    "unipathway:UPA00989": {
        "module": "trna_m7g46_methylation",
        "module_file": "modules/trna_m7g46_methylation.yaml",
        "taxon_research_path": "projects/P_PUTIDA/deep-research/PSEPK__trna_m7g46_methylation__upa00989-deep-research-falcon.md",
        "scope_note": "Compact UniPathway tRNA-modification module: trmB catalyzes SAM-dependent guanine-N7 methylation at tRNA position 46 to form m7G46. Broader RNA methylation and tRNA methyltransferase-complex annotations are context only pending more specific evidence.",
        "priority_phase": "6",
    },
    "kegg:ppu00010": {
        "module": "entner_doudoroff_and_gluconeogenesis",
        "module_file": "modules/entner_doudoroff_and_gluconeogenesis.yaml",
        "scope_note": "P. putida lacks canonical EMP glycolysis; needs careful split from generic glycolysis/gluconeogenesis.",
        "priority_phase": "1",
    },
    "kegg:ppu00362": {
        "module": "benzoate_degradation",
        "module_file": "modules/benzoate_degradation.yaml",
        "scope_note": "Benzoate/beta-ketoadipate aromatic-catabolism bucket; KEGG membership also includes gallate, phenylacetate, fatty-acid-like, and side-route nodes.",
        "priority_phase": "2",
    },
    "kegg:ppu01220": {
        "module": "aromatic_compound_degradation",
        "module_file": "modules/aromatic_compound_degradation.yaml",
        "scope_note": "Broad aromatic-compound umbrella; split candidate genes into route-specific catabolic funnels and side-node/cofactor context.",
        "priority_phase": "2",
    },
    "kegg:ppu00622": {
        "module": "benzoate_upper_pathway",
        "module_file": "modules/benzoate_upper_pathway.yaml",
        "scope_note": "Benzoate upper-pathway bucket inside a broader xylene map; KT2440 support is BenABCD-to-catechol plus side-route context.",
        "priority_phase": "2",
    },
}


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            delimiter="\t",
            fieldnames=fieldnames,
            extrasaction="ignore",
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def psepk_review_index() -> tuple[dict[str, Path], dict[str, Path]]:
    global _PSEPK_REVIEW_INDEX
    if _PSEPK_REVIEW_INDEX is not None:
        return _PSEPK_REVIEW_INDEX

    by_accession: dict[str, Path] = {}
    by_symbol: dict[str, Path] = {}
    for review in Path("genes/PSEPK").glob("*/*-ai-review.yaml"):
        try:
            data = yaml.safe_load(review.read_text(encoding="utf-8")) or {}
        except Exception:
            continue
        accession = data.get("id", "")
        symbol = data.get("gene_symbol", "")
        if accession:
            by_accession.setdefault(str(accession), review)
        if symbol:
            by_symbol.setdefault(str(symbol), review)
        for alias in data.get("aliases") or []:
            by_symbol.setdefault(str(alias), review)

    _PSEPK_REVIEW_INDEX = (by_accession, by_symbol)
    return _PSEPK_REVIEW_INDEX


def locate_review(row: dict[str, str]) -> Path:
    gene = row.get("suggested_review_name", "")
    direct = Path("genes") / "PSEPK" / gene / f"{gene}-ai-review.yaml"
    if direct.exists():
        return direct
    by_accession, by_symbol = psepk_review_index()
    accession = row.get("uniprot_accession", "")
    return by_accession.get(accession) or by_symbol.get(gene) or direct


def count_existing_gene_reviews(rows: list[dict[str, str]]) -> tuple[int, int]:
    existing = 0
    asta = 0
    for row in rows:
        gene = row.get("suggested_review_name", "")
        if not gene:
            continue
        review = locate_review(row)
        gene_dir = review.parent
        review_stem = review.name.removesuffix("-ai-review.yaml")
        if review.exists():
            existing += 1
        asta_candidates = [gene_dir / f"{gene}-deep-research-asta.md"]
        if review_stem != gene:
            asta_candidates.append(gene_dir / f"{review_stem}-deep-research-asta.md")
        if any(candidate.exists() for candidate in asta_candidates):
            asta += 1
    return existing, asta


def build_worklist(project_dir: Path) -> list[dict[str, str]]:
    buckets = read_tsv(project_dir / "data" / "psepk_pathway_buckets.tsv")
    partition = read_tsv(project_dir / "data" / "psepk_pathway_partition.tsv")
    memberships = read_tsv(project_dir / "data" / "psepk_pathway_membership.tsv")

    primary_rows: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in partition:
        primary_rows[row.get("primary_bucket_id", "")].append(row)

    membership_counts = Counter(
        f"{row['membership_source'].casefold()}:{row['pathway_id']}"
        for row in memberships
        if row.get("pathway_scope") != "overview"
    )

    worklist: list[dict[str, str]] = []
    for bucket in buckets:
        bucket_id = bucket.get("bucket_id", "")
        mapping = MODULE_MAP.get(bucket_id, {})
        module_file = mapping.get("module_file", "")
        module_name = mapping.get("module", "")
        provider_slug = "falcon"
        module_research_path = ""
        if module_file:
            module_research_path = (
                Path(module_file)
                .with_name(Path(module_file).stem + f"-deep-research-{provider_slug}.md")
                .as_posix()
            )
        pathway_token = bucket_id.split(":", 1)[1] if ":" in bucket_id else bucket_id
        default_taxon_research_path = (
            project_dir
            / "deep-research"
            / f"PSEPK__{module_name or bucket_id.replace(':', '-')}__{pathway_token}-deep-research-falcon.md"
        )
        taxon_research_path = Path(
            mapping.get("taxon_research_path", default_taxon_research_path.as_posix())
        )

        rows = primary_rows.get(bucket_id, [])
        review_count, asta_count = count_existing_gene_reviews(rows)
        gene_count = int(bucket.get("gene_count", "0") or 0)
        missing_reviews = max(gene_count - review_count, 0)
        membership_key = bucket_id.replace("kegg:", "kegg:").replace(
            "unipathway:", "unipathway:"
        )
        scope_note = mapping.get("scope_note", "")
        if not scope_note:
            scope_note = "Pending module-scope decision."
        row = {
            "bucket_id": bucket_id,
            "bucket_label": bucket.get("bucket_label", ""),
            "bucket_type": bucket.get("bucket_type", ""),
            "module_area": bucket.get("module_area", ""),
            "gene_count": str(gene_count),
            "specific_membership_count": str(membership_counts.get(membership_key, gene_count)),
            "reviewed_gene_count": bucket.get("reviewed_count", ""),
            "existing_review_files": str(review_count),
            "missing_review_files": str(missing_reviews),
            "asta_research_files": str(asta_count),
            "module": module_name,
            "module_file": module_file,
            "module_file_exists": "true"
            if module_file and Path(module_file).exists()
            else "false",
            "module_research_falcon": "DONE"
            if module_research_path and Path(module_research_path).exists()
            else "TODO",
            "module_research_path": module_research_path,
            "taxon_research_falcon": "DONE" if taxon_research_path.exists() else "TODO",
            "taxon_research_path": taxon_research_path.as_posix(),
            "priority_phase": mapping.get("priority_phase", ""),
            "batch_status": mapping.get("batch_status", "SEEDED" if module_name else "UNMAPPED"),
            "pr_status": mapping.get("pr_status", "NOT_STARTED"),
            "pr_url": mapping.get("pr_url", ""),
            "scope_note": scope_note,
        }
        if (
            not module_name
            and bucket.get("bucket_type") == "kegg_pathway"
            and not mapping.get("batch_status")
        ):
            row["batch_status"] = "NEEDS_MODULE_MAPPING"
        elif bucket.get("bucket_type") in {"unknown", "orphan"}:
            row["batch_status"] = "ORPHAN_OR_UNKNOWN_QUEUE"
        worklist.append(row)

    def sort_key(row: dict[str, str]) -> tuple[int, int, str]:
        phase = int(row["priority_phase"]) if row["priority_phase"].isdigit() else 99
        mapped = 0 if row["module"] else 1
        return (phase, mapped, row["bucket_id"])

    return sorted(worklist, key=sort_key)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build PSEPK pathway worklist.")
    parser.add_argument("--project-dir", type=Path, default=DEFAULT_PROJECT_DIR)
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_PROJECT_DIR / "data" / "psepk_pathway_worklist.tsv",
    )
    args = parser.parse_args()

    rows = build_worklist(args.project_dir)
    fields = [
        "bucket_id",
        "bucket_label",
        "bucket_type",
        "module_area",
        "gene_count",
        "specific_membership_count",
        "reviewed_gene_count",
        "existing_review_files",
        "missing_review_files",
        "asta_research_files",
        "module",
        "module_file",
        "module_file_exists",
        "module_research_falcon",
        "module_research_path",
        "taxon_research_falcon",
        "taxon_research_path",
        "priority_phase",
        "batch_status",
        "pr_status",
        "pr_url",
        "scope_note",
    ]
    write_tsv(args.output, rows, fields)
    args.output.with_suffix(".manifest.txt").write_text(
        "\n".join(
            [
                f"generated_utc: {datetime.now(timezone.utc).isoformat()}",
                f"project_dir: {args.project_dir.as_posix()}",
                f"output: {args.output.as_posix()}",
                f"rows: {len(rows)}",
                "",
            ]
        ),
        encoding="utf-8",
    )
    print(f"Wrote {len(rows)} pathway buckets to {args.output}")


if __name__ == "__main__":
    main()
