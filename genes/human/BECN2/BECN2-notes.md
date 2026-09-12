# BECN2 review notes

Review started from `just fetch-gene human BECN2`. The proteostasis network places BECN2 under `Autophagy-Lysosome Pathway > Autophagophore initiation and elongation > Class 3 PI3K complex 1, direct > Class 3 PI3K complex 1 component`.

Falcon deep research was requested with `just deep-research-falcon human BECN2`, but the provider timed out after 600 seconds and no `BECN2-deep-research-falcon.md` file was produced. I am completing the review using the cached primary literature, UniProt record, GOA seed, and notes below.

BECN2 is a mammalian Beclin-family protein with two supported lysosomal degradation roles: autophagy and G-protein-coupled receptor (GPCR) turnover. The primary Cell paper reports that Beclin 2 functions in autophagy, interacts with class III PI3K complex components and Bcl-2, and has an additional lysosomal degradation role not shared by BECN1 [PMID:23954414 "functions in autophagy and interacts with class III PI3K complex components and Bcl-2" and "functions in an additional lysosomal degradation pathway"].

BECN2's GPCR role is direct and should remain core. Beclin 2 is required for ligand-induced endolysosomal degradation of several GPCRs through interaction with GASP1/GPRASP1, and heterozygous knockout mice accumulate brain cannabinoid receptor 1 [PMID:23954414 "required for ligand-induced endolysosomal degradation of several G protein-coupled receptors (GPCRs) through its interaction with GASP1" and "increased levels of brain cannabinoid 1 receptor"].

The PI3KC3-C1/autophagy-initiation connection is supported by the Cell paper, UniProt, and the ATG14 structural abstract. UniProt lists BECN2 in class III PI3K type I/type II complexes and notes interactions with ATG14, AMBRA1, UVRAG, and PIK3C3/VPS34 [file:human/BECN2/BECN2-uniprot.txt "Interacts ... with ATG14" and "Interacts with AMBRA1, UVRAG and PIK3C3/VPS34"]. The structural paper reports that ATG14 binding to BECN/Beclin homologs is essential for autophagy and that BECN2:ATG14 forms a coiled-coil heterodimer [PMID:28218432 "ATG14 binding to BECN/Beclin homologs is essential for autophagy" and "the BECN2 CCD and ATG14 CCD form a parallel, curved heterodimer"].

Mitophagy is too specific for the accessible BECN2 evidence. BECN2 has general autophagy/autophagosome assembly support, but the cached human paper and UniProt summaries do not establish a BECN2-specific mitophagy role. I will modify the mitophagy row to autophagosome assembly rather than retaining cargo-specific mitophagy.

The vacuole transport row is a yeast-style transfer and should be converted to the directly supported human endosome-to-lysosome transport/GPCR degradation role. Generic protein binding rows are not useful as molecular-function annotations; the evidence should be captured as protein-macromolecule adaptor activity, phosphatidylinositol 3-kinase binding, complex membership, and GASP1-dependent GPCR catabolism.

Curation stance:
- Core: autophagy/autophagosome assembly, class III PI3K type I/type II complex context, phosphatidylinositol 3-kinase binding, protein-macromolecule adaptor activity, endosome-to-lysosome transport, GPCR catabolic process, cytoplasm.
- Modify: mitophagy to autophagosome assembly; late endosome-to-vacuole transport to endosome-to-lysosome transport; protein-containing complex binding to adaptor activity.
- Keep as non-core: cellular response to nitrogen starvation as autophagy context.
- Mark over-annotated: generic protein binding rows.

## Description cleanup note

The YAML `description` field was revised to keep it as a standalone biological summary. Project-specific curation framing moved here instead.

- Moved out of the YAML description: the prior wording tied the PI3KC3-C1 interpretation to a Proteostasis Network leaf and contrasted that shared role with the BECN2-specific GPCR catabolic branch.

## Falcon deep research findings (2026-06-07)

The Falcon report (`BECN2-deep-research-falcon.md`) was generated after the original review was completed (the earlier notes recorded a Falcon timeout). It is consistent with the existing review and adds a substantial body of post-2013 BECN2 literature that was NOT previously captured. PMIDs below were resolved from the report's DOIs via the PubMed ID converter. Synthesis of KEY findings:

- **NEW — Noncanonical degradation of inflammasome sensors (innate immunity).** BECN2 negatively regulates NLRP3, AIM2, NLRP1, and NLRC4 inflammasomes by mediating lysosomal degradation of the sensors through a ULK1- and ATG9A-dependent, but BECN1/WIPI2/ATG16L1/LC3-independent, non-canonical autophagic pathway; sensors are recruited onto ATG9A+ vesicles and SNAREs SEC22A/STX5/STX6 mediate fusion; Becn2 loss worsens alum-induced peritonitis [PMID:34152938 "loss of BECN2 enhanced the activities of NLRP3, AIM2, NLRP1, and NLRC4 inflammasomes" ; "ATG9A-Dependent but ATG16L1- and LC3-Independent Non-Canonical Autophagy"] (Deng et al. 2022, Autophagy, DOI:10.1080/15548627.2021.1934270). This is a distinct biological process not represented in existing_annotations.

- **NEW — Negative regulation of innate immune signaling and tumor suppression.** BECN2 targets the upstream MAP3Ks MEKK3 (MAP3K3) and TAK1 (MAP3K7) for ATG9A-dependent (ATG16L/Beclin1/LC3-independent) autophagic degradation, restraining ERK1/2 and NF-kB signaling. Becn2-null mice develop splenomegaly, lymphadenopathy, increased proinflammatory cytokines, persistent STAT3 activation, and increased lymphoma incidence; myeloid Map3k3 ablation rescues these phenotypes, implicating BECN2 as a suppressor of inflammation-driven tumorigenesis [PMID:32865519 "Beclin 2 targeted the key signaling kinases MEKK3 and TAK1 for degradation" ; "markedly increased incidence of lymphoma development"] (Zhu et al. 2020, J Clin Invest, DOI:10.1172/JCI133283). New process/disease dimension.

- **CONFIRMS — Mitophagy is a BECN1, not BECN2, function.** In BECN1- vs BECN2-deficient HeLa cells and MEFs, selective mitophagy was compromised only by BECN1 loss (requiring ULK1 phosphorylation of Beclin-1 Ser15 and MAM localization); BECN2 contributed to general autophagosome formation but was not required for mitophagy [PMID:36719945 "Mitophagy was compromised only in Beclin1-deficient HeLa cells and mouse embryonic fibroblasts"] (Quiles et al. 2023, Sci Signal, DOI:10.1126/scisignal.abo4457). This independently supports the existing review's MODIFY decision converting the IBA mitophagy annotation to autophagosome assembly.

- **NEW (mechanistic refinement) — BECN2-ATG14 selectivity for GPCR cargo.** Crystal structures of the BECN2 coiled-coil and BECN2-ATG14 heterodimer show the potent BECN2-ATG14 interaction is selectively critical for endolysosomal degradation of GPRASP1/GASP1-associated GPCRs (notably DRD2/D2R), whereas EGFR degradation depends more on BECN1-UVRAG; stapled peptides that enhance BECN2-ATG14 selectively boost BECN2-dependent autophagy and DRD2 turnover [PMID:37409929 "potent BECN2-ATG14 coiled-coil interaction is selectively critical for endolysosomal degradation of GPRASP1/GASP1-associated GPCRs"] (Qiu et al. 2023, Autophagy, DOI:10.1080/15548627.2023.2233872). Note: this is a SEPARATE 2023 paper from PMID:28218432 (Su et al. 2017, Protein Science, DOI:10.1002/pro.3140), which is the structural reference already cited in the review (the converter confirms 28218432 = Su 2017, correctly titled in the existing references).

- **CONFIRMS / context — Beclin-ortholog review framing.** A highly cited review positions Beclin proteins as integrative hubs of cell signaling and membrane trafficking and highlights BECN2's unique GASP1-dependent GPCR degradation role not shared by other PI3KC3 members [PMID:26071895 "Beclin orthologs: integrative hubs of cell signaling, membrane trafficking, and physiology"] (Levine et al. 2015, Trends Cell Biol, DOI:10.1016/j.tcb.2015.05.004). Supports existing GPCR-catabolism and PI3KC3-context annotations.

- **PROVISIONAL / low-confidence — do NOT use for annotation.** The report cites a sesamin/lumbar-disc-degeneration disease-model paper (Zhang et al. 2024, Aging, DOI:10.18632/aging.205386) whose reported directionality (higher BECN2 with lower autophagy markers) conflicts with foundational BECN2 autophagy biology, and a 2025 preprint review (DOI:10.20944/preprints202507.2396.v1, not peer-reviewed). These are noted for completeness only and are NOT used to change any annotation.

### Curation impact

Conservative enrichment only — the review is COMPLETE and these findings augment rather than overturn it. The new immune/tumor-suppression functions (inflammasome sensor degradation; MAP3K7/MAP3K3 degradation; negative regulation of NF-kB/innate immune signaling) are real BECN2 functions but are NOT present in the existing GOA-seeded existing_annotations, so they belong in references/suggested follow-ups rather than as fabricated existing-annotation rows. I added the four primary PMIDs (34152938, 32865519, 36719945, 37409929) and the Levine 2015 review (26071895) to `references:` as statement-only entries, plus suggested questions/experiments. No existing annotation `action` was changed; Quiles 2023 reinforces (does not contradict) the existing mitophagy MODIFY.
