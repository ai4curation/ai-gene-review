# CYCLOPS (Lotus japonicus, A9XMT3) curation notes

Date: 2026-10-02. Sources: UniProt A9XMT3, GOA (14 rows), cached publications, Falcon deep research.

## Identity
- CYCLOPS = IPD3 orthologue (Medicago IPD3 = Interacting Protein of DMI3). 518 aa, plant-specific, no similarity to known proteins outside the CYCLOPS family (IPR040036; PANTHER PTHR36890).
- [PMID:19074278 "CYCLOPS carries a functional nuclear localization signal and a predicted coiled-coil domain."]

## Molecular function
- Interacts with kinase-active CCaMK; preassembled complex: [PMID:19074278 "We show that CYCLOPS specifically interacts with kinase-active CCaMK in planta and is phosphorylated by CCaMK in vitro"]
- DNA-binding transcriptional activator: [PMID:24528861 "We show that CYCLOPS, a direct phosphorylation substrate of CCaMK, is a DNA-binding transcriptional activator."]
- Phospho-activation: [PMID:24528861 "Two phosphorylated serine residues within the N-terminal negative regulatory domain of CYCLOPS are necessary for its activity."] (Ser50/Ser154 per deep research.)
- Targets: NIN [PMID:24528861 "transactivates the NODULE INCEPTION (NIN) gene"]; ERN1 [PMID:28503742 "CYCLOPS binds in a sequence-specific manner to a motif within the ERN1 promoter"]; RAM1 [PMID:27020747 "activates RAM1 expression via binding of CYCLOPS to a cis element in the RAM1 promoter"]; CBP1 shared element (Gong et al. 2022, from deep research only; not cached).
- Homodimerization by Y2H/BiFC [PMID:19074278 "CYCLOPS forms homodimers"]; functional relevance unknown.

## Biological role
- Infection (rhizobial ITs; AM outer cortex entry, arbuscules): [PMID:19074278 "These data indicate that CYCLOPS is required for fungal infection of the outer cortical cell layers and for arbuscule development."]
- Organogenesis: dispensable when CCaMK deregulated [PMID:19074278 "These results indicate that CYCLOPS is dispensable for nodule organogenesis"], yet phosphomimetic CYCLOPS is sufficient [PMID:24528861 "A phosphomimetic version of CYCLOPS was sufficient to trigger root nodule organogenesis in the absence of rhizobia and CCaMK."]
- Conservation: rice CYCLOPS required for AM and complements Lotus mutant [PMID:19074278].

## Curation decisions
- GO:0003700 -> MODIFY to GO:0001216 DNA-binding transcription activator activity (all targets activated; Pol II specificity not shown so not GO:0001228).
- protein binding (CCaMK, A0AAR7) -> MODIFY to GO:0019901 protein kinase binding.
- GO:0006355 -> MODIFY to GO:0045893 (already present from ERN1 paper).
- Homodimerization -> KEEP_AS_NON_CORE.
- nucleus, sequence-specific DNA binding, nodulation, AM association, positive regulation of transcription -> ACCEPT.
- Participation test for nodulation/AM: CYCLOPS is the transcription factor that directly activates NIN/ERN1/RAM1, so it performs a step (transcriptional induction) rather than only being necessary. No NEW terms added.

## Project observation (symbiosis vs defense)
- No defense/immunity terms on CYCLOPS; annotations are cleanly symbiosis-specific (nodulation, AM). Consistent with ORYSJ/CCAMK, where CYCLOPS is the downstream effector of CCaMK.
