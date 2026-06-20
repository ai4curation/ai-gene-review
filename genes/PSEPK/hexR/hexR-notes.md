# hexR (Q88P32) — Pseudomonas putida KT2440 (PSEPK) — Research Notes

## Identity
- UniProt: Q88P32 (HEXR_PSEPK), 287 aa, reviewed (Swiss-Prot).
- Gene: hexR; locus PP_1021.
- Name: HTH-type transcriptional regulator HexR [UniProt "RecName: Full=HTH-type transcriptional regulator HexR"].
- Family/domains: RpiR-family regulator with an N-terminal winged-helix HTH DNA-binding domain and a C-terminal sugar isomerase (SIS) domain.
  - [UniProt "DOMAIN          2..78 /note=\"HTH rpiR-type\""]
  - [UniProt "DOMAIN          122..261 /note=\"SIS\""]
  - [UniProt "DNA_BIND        38..57 /note=\"H-T-H motif\""]

## Molecular function & mechanism
- HexR is a DNA-binding transcriptional repressor of glucose metabolism genes.
  - [UniProt "FUNCTION: Involved in regulation of glucose metabolism. Transcriptional repressor of the gap-1 gene and of the edd-glk-gltR-2 and zwf-pgl-eda operons. Acts by binding directly to an inverted pseudopalindromic sequence in the promoter region."]
- Binds the P(edd), P(zwf), and P(gap-1) promoters with nanomolar affinity; two monomers bind a pseudopalindrome consensus 5'-TTGTN(7-8)ACAA-3'.
  - [PMID:19506074 "HexR recognizes the P(edd), P(zwf), and P(gap-1) promoters with affinity in the nanomolar range"]
  - [PMID:19506074 "two monomers of HexR bind to a pseudopalindrome with a consensus sequence of 5'-TTGTN(7-8)ACAA-3'"]
- DNA-binding HTH domain belongs to the RpiR family.
  - [PMID:19506074 "the helix-turn-helix DNA binding domain of HexR exhibits high similarity to proteins of the RpiR family of regulators"]

## Effector / activity regulation
- The Entner-Doudoroff intermediate 2-keto-3-deoxy-6-phosphogluconate (KDPG) binds HexR and releases it from operator DNA (induction). Glucose, glucose-6-phosphate, and 6-phosphogluconate do NOT cause dissociation.
  - [UniProt "ACTIVITY REGULATION: Binding of 2-keto-3-deoxy-6-phosphogluconate (KDPG) to HexR releases the repressor from its target sequences."]
  - [PMID:19506074 "Binding of the Entner-Doudoroff pathway intermediate 2-keto-3-deoxy-6-phosphogluconate to HexR released the repressor from its target operators, whereas other chemicals such as glucose, glucose 6-phosphate, and 6-phosphogluconate did not induce complex dissociation"]
- The phosphorylated effector is recognized by the C-terminal SIS (sugar isomerase) domain.
  - [PMID:19506074 "The phosphorylated effector is likely to be recognized by a sugar isomerase domain located at the C-terminal end of HexR"]

## Subunit / quaternary structure
- Monomer in solution, binds DNA as a dimer.
  - [UniProt "SUBUNIT: Monomer in solution. Binds DNA as a dimer."]
  - [PMID:19506074 "we purified HexR and showed that it is a monomer in solution"]

## Biological role / regulon
- In P. putida KT2440, glucose is channeled to the central Entner-Doudoroff intermediate 6-phosphogluconate via convergent peripheral pathways, regulated by HexR, GnuR, PtxS (repressors) and GltR-2 (activator).
  - [PMID:18245293 "Expression of the three pathways is mediated by three transcriptional repressors, HexR, GnuR, and PtxS, and by a positive transcriptional regulator, GltR-2."]
- HexR controls glucokinase/glucose-6-phosphate dehydrogenase genes, Entner-Doudoroff enzyme genes, and gap-1 (glyceraldehyde-3-phosphate dehydrogenase).
  - [PMID:18245293 "HexR controls the genes that encode glucokinase/glucose 6-phosphate dehydrogenase that yield 6-phosphogluconate; the genes for the Entner-Doudoroff enzymes that yield glyceraldehyde-3-phosphate and pyruvate; and gap-1, which encodes glyceraldehyde-3-phosphate dehydrogenase."]

## Localization
- As a transcriptional repressor acting at promoter operators, HexR functions in the cytoplasm bound to chromosomal DNA (forms a protein-DNA complex). GOA includes GO:0032993 protein-DNA complex (IPI, CollecTF).

## Annotation assessment summary
- Core MF: GO:0001217 DNA-binding transcription repressor activity (IPI, PMID:19506074) — ACCEPT, core.
- Core MF: GO:0000976 transcription cis-regulatory region binding (IPI, PMID:19506074) — ACCEPT, core.
- Core BP: GO:0045892 negative regulation of DNA-templated transcription — ACCEPT, core.
- GO:0006355 regulation of DNA-templated transcription — broad parent of the negative-regulation term; KEEP_AS_NON_CORE (less informative).
- GO:0003700 DNA-binding transcription factor activity — repressor activity (GO:0001217) is the more specific/accurate child; MODIFY/over-annotated relative to repressor term. Keep as non-core (parent).
- GO:0003677 DNA binding — generic; more specific GO:0000976 present; MARK_AS_OVER_ANNOTATED.
- GO:0097367 carbohydrate derivative binding — captures the SIS-domain effector (KDPG) binding; broad but supported by the effector-sensing mechanism. KEEP_AS_NON_CORE.
- GO:1901135 carbohydrate derivative metabolic process — HexR regulates metabolism but is not itself a metabolic enzyme; this BP is an InterPro over-call. MARK_AS_OVER_ANNOTATED.
- GO:0032993 protein-DNA complex — supported (binds DNA as dimer at operators). ACCEPT/KEEP_AS_NON_CORE.
