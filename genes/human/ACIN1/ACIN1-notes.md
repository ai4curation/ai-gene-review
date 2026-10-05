# ACIN1 notes

ACIN1 is reviewed in the PN "specific function in autophagosome maturation and lysosome fusion unknown" bucket. That PN row is no-mapping/context-only and its autophagy citations are Drosophila Acinus studies, so it was used as search context rather than as direct human ACIN1 evidence.

The strongest human ACIN1 function is nuclear RNA processing/splicing through EJC/ASAP-associated complexes. UniProt describes ACIN1 as an "Auxiliary component of the splicing-dependent multiprotein exon junction complex (EJC)" and as a "Component of the ASAP complexes which bind RNA" [file:human/ACIN1/ACIN1-uniprot.txt, "Auxiliary component of the splicing-dependent multiprotein exon junction complex"; file:human/ACIN1/ACIN1-uniprot.txt, "Component of the ASAP complexes which bind RNA"]. The EJC biochemical paper identified "two novel EJC components, Acinus and SAP18" and showed that "Acinus binds directly to another EJC component, RNPS1" [PMID:16314458, "identified two novel EJC components, Acinus and SAP18"; PMID:16314458, "Acinus binds directly to another EJC component, RNPS1"]. The ASAP structural paper states that ASAP subunits Acinus, RNPS1, and SAP18 are implicated in "transcriptional regulation, pre-mRNA splicing and mRNA quality control" and that the Acinus-RNPS1-SAP18 ternary complex has "both RNA- and protein-binding properties" [PMID:22388736, "transcriptional regulation, pre-mRNA splicing and mRNA quality control"; PMID:22388736, "both RNA- and protein-binding properties"].

ASAP complex and nuclear-speckle localization are well supported. Schwerk et al. isolated ASAP complexes from HeLa extract and found they were "composed of the polypeptides SAP18 and RNPS1 and different isoforms of the Acinus protein" [PMID:12665594, "composed of the polypeptides SAP18 and RNPS1 and different isoforms of the Acinus protein"]. Singh et al. later summarized that "RNPS1, Acinus, and SAP18 form the apoptosis- and splicing-associated protein (ASAP) complex" and demonstrated that SAP18 assembles a "nuclear speckle-localized splicing regulatory multiprotein complex including RNPS1 and Acinus" [PMID:20966198, "RNPS1, Acinus, and SAP18 form the apoptosis- and splicing-associated protein (ASAP) complex"; PMID:20966198, "nuclear speckle-localized splicing regulatory multiprotein complex including RNPS1 and Acinus"].

ACIN1's apoptosis annotation is also supported, but it is separate from the PN autophagy question. The original Acinus paper identified a nuclear factor that "induces apoptotic chromatin condensation after cleavage by caspase-3" and found Acinus "essential for apoptotic chromatin condensation in vitro" [PMID:10490026, "induces apoptotic chromatin condensation after cleavage by caspase-3"; PMID:10490026, "essential for apoptotic chromatin condensation in vitro"]. The ASAP paper also reports that microinjected ASAP complexes accelerated cell death and that the complex disassembles after apoptosis induction [PMID:12665594, "microinjection of ASAP complexes into mammalian cells resulted in acceleration of cell death"; PMID:12665594, "after induction of apoptosis the ASAP complex disassembles"].

Hematopoietic differentiation rows are real caspase/substrate contexts but not central ACIN1 core functions. During erythroid differentiation, acinus is cleaved as part of caspase-dependent nuclear changes [PMID:11208865, "cleave proteins involved in nucleus integrity (lamin B) and chromatin condensation (acinus)without inducing cell death"; PMID:11208865, "normal erythroid differentiation requires the transient activation of several caspases"]. During monocyte-to-macrophage differentiation, the abstract reports that differentiation-associated caspase activation "leads to the cleavage of the protein acinus" [PMID:12393560, "leads to the cleavage of the protein acinus"].

Curation decisions:
- Accept RNA splicing, RNA binding, ASAP complex, nucleus/nucleoplasm/nuclear speck, apoptotic chromatin condensation, and positive regulation of apoptotic process.
- Modify broad nucleic acid binding to RNA binding.
- Modify regulation of mRNA processing to negative regulation of mRNA splicing via spliceosome, based on UniProt/ASAP-complex evidence that the complex can inhibit in vitro splicing reactions.
- Keep erythrocyte and monocyte differentiation as non-core hematopoietic/caspase contexts.
- Remove ATP hydrolysis activity; ACIN1 is an RRM/SAP-domain RNA-processing factor, and neither UniProt function nor cached primary evidence supports an ACIN1 ATPase activity.
- Remove generic protein binding and enzyme binding rows; specific interactions are better represented by ASAP complex membership, EJC context, RNA-binding/splicing functions, or regulatory evidence, and being a CASP3 substrate does not establish a separate enzyme-binding activity.
- Keep the Drosophila Acinus basal-autophagy PN signal as a suggested question/experiment for human ACIN1 rather than a new human annotation.

## Description cleanup note

The YAML `description` field was revised to keep it as a standalone biological summary. Project-specific curation framing moved here instead.

- Moved out of the YAML description: the prior wording said the human GOA evidence reviewed here supports RNA processing and apoptosis rather than a direct human ACIN1 autophagy annotation. That is a curation observation, not part of the standalone gene description.

## Falcon deep research findings (2026-06-07)

Synthesis of the Falcon (Edison) report, emphasizing what is NEW relative to the existing review. PMIDs verified against PubMed via DOI conversion.

- NEW primary mechanistic evidence (Rodor 2016): genome-wide iCLIP shows human Acinus binds both pre-mRNAs (enriched at a subset of "suboptimal" introns, near splice sites) and spliced mRNAs, confirming it as a peripheral EJC factor; siRNA depletion + RNA-seq shows Acinus is required for inclusion of specific alternative cassette exons and faithful splicing of certain introns, supporting a direct role in exon/intron definition [PMID:27365209 "Acinus is preferentially required for the inclusion of specific alternative cassette exons"]. This strengthens the existing IBA RNA-splicing ACCEPT with direct human experimental data, which the review previously lacked.
- NEW specific splicing target with apoptosis relevance: Acinus regulates splicing of the DFFA/ICAD transcript, a major regulator of apoptotic DNA fragmentation; depletion can drive ICAD intron retention/short nonfunctional isoform and impair CAD-mediated DNA fragmentation [PMID:27365209 "Acinus regulates the splicing of DFFA/ICAD transcript, a major regulator of DNA fragmentation"]. This mechanistically links ACIN1's splicing function to its apoptosis function — a connection not captured in the current review.
- NEW interaction/regulatory node (review-level): API5/AAC-11 binds Acinus and protects it from caspase-3 cleavage, preventing Acinus-mediated p17 generation and apoptotic DNA fragmentation [PMID:38275765 (Abbas 2024 review) "API5...protects it from caspase-3 cleavage"]. Review-derived; not used to change annotations. Falcon also restates Akt phosphorylation inhibiting Acinus proteolysis and SRPK2 phosphorylation links (review-level, consistent with existing SRPK2/API5 mention in protein-binding reasons).
- NEW complex context (review-level, Deka & Singh 2017): structural description of ASAP as an RNPS1(RRM)–SAP18(UBL)–Acinus(RSB motif) heterotrimer, and an alternative PSAP complex where RNPS1/SAP18 pair with Pinin (PNN); SAP18 links the complex to Sin3/HDAC, and the Acinus-L SAP motif targets AT-rich SAR/MAR chromatin [PMID:28539829 "RNPS1, Acinus and SAP18...ASAP complex"; the PSAP/Pinin alternative is also described]. Consistent with, and enriching, the existing ASAP-complex annotation; PSAP/PNN is a genuinely new partner relationship noted here for context.
- NEW disease/association context (provisional, association-grade — NOT used to change annotations): ACIN1/Acin1 is reported upregulated in hepatocellular carcinoma with a spliceosome/EJC PPI neighborhood and predicted miR-674-5p/ceRNA regulation [PMID:39128105 (Tang 2024)], and positioned downstream of a METTL3→IGF2BP3 m6A axis stabilizing ACIN1 mRNA in cervical cancer [PMID:35255776 (Su 2022)]. These are network/expression-association studies, not causal mechanism, so they remain notes-only.
- A 2025 "Acinus in plant programmed cell death" item (doi:10.1007/s44372-025-00406-x, 0 citations) and a 2024 A549/strophanthidin proteomics item (doi:10.3390/molecules29040877) appear in the Falcon corpus but are tangential/provisional for human ACIN1 function and are not incorporated.

## APOPTOSIS refresh (2026-09-30)

Fresh GOA added five partner-specific `GO:0005515 protein binding` rows: RNPS1
from a spliceosome Y2H/co-IP matrix, RNPS1 and PNN from BioPlex AP-MS, and
RNPS1 and PNN from the U2OS multimodal cell map. All five were removed as
generic interaction rows. RNPS1 is already represented by accepted ASAP complex
membership, PNN is PSAP/EJC-neighborhood context, and the high-throughput
network sources do not establish a more specific ACIN1 molecular function.

The pre-existing generic protein-binding rows were migrated from the legacy
`MARK_AS_OVER_ANNOTATED` action to `REMOVE` under the current policy for
uninformative `protein binding`. SF3A2, PCBD1, SRPK2, PNN, and RBM5 edges were
not treated as false; they just do not add to ACIN1's reviewed RNA-binding,
ASAP/EJC splicing, and apoptotic chromosome-condensation activities. The
`GO:0019899 enzyme binding` NAS row was also changed to `REMOVE`: the Acinus
paper supports CASP3 cleavage and downstream apoptotic chromatin condensation,
but being a caspase substrate is not an enzyme-binding function.

The ACIN1 review now covers all 46 refreshed GOA rows. Core biology remains
unchanged: ACIN1 acts as a nuclear RNA-binding ASAP/EJC-associated splicing
factor and as a caspase-activated apoptotic chromatin-condensation factor, while
Drosophila Acinus autophagy evidence remains a human follow-up question rather
than a new human GO annotation.

## Completion status (2026-09-30)

Marked the refreshed APOPTOSIS review `COMPLETE`. The remaining validation
warning is advisory-only: `ACIN1-deep-research-falcon.md` is available and was
summarized in these notes, but the curated YAML intentionally cites the primary
papers and UniProt snippets that directly support each retained annotation.
