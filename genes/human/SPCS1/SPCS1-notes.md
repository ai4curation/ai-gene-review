# SPCS1 (Signal peptidase complex subunit 1) — review notes

UniProt: Q9Y6A9 (SPCS1_HUMAN); aka SPC12, "Microsomal signal peptidase 12 kDa subunit". 169 aa, multi-pass ER membrane protein (two TM helices, residues 94-114 and 116-136). HGNC:23401, gene on chr 3.

## Core identity and function
SPCS1 is one of the three **non-catalytic accessory subunits** (SPCS1, SPCS2, SPCS3) of the eukaryotic ER **signal peptidase complex (SPC)**. The catalytic subunits are SEC11A (SPC-A) or SEC11C (SPC-C). SPCS1 is **dispensable for SPC enzymatic (peptidase) activity**.

- UniProt FUNCTION: "Component of the signal peptidase complex (SPC) which catalyzes the cleavage of N-terminal signal sequences from nascent proteins as they are translocated into the lumen of the endoplasmic reticulum (PubMed:34388369). Dispensable for SPC enzymatic activity (By similarity)." [UniProt Q9Y6A9]
- UniProt SUBUNIT: "Component of the signal peptidase complex paralog A (SPC-A) composed of a catalytic subunit SEC11A and three accessory subunits SPCS1, SPCS2 and SPCS3 ... Within the complex, interacts with SPCS2 and SPCS3 (PubMed:34388369). The complex induces a local thinning of the ER membrane which is used to measure the length of the signal peptide (SP) h-region of protein substrates."
- Cryo-EM structure of human SPC: [PMID:34388369 "Structure of the human signal peptidase complex reveals the determinants for signal peptide cleavage"] establishes SPCS1 as a structural component of the complex and reports phosphorylation.
- Membrane topology established in [PMID:8632014 "Membrane topology of the 12- and the 25-kDa subunits of the mammalian signal peptidase complex"].

So core function = SPC complex membership (GO:0005787), signal peptide processing / protein processing involvement (GO:0006465 / GO:0016485), ER membrane localization (GO:0005789). NOT a catalytic MF.

## Secondary / non-core: viral (flavivirus + HCV) processing
SPCS1 was identified in CRISPR/host-factor screens as required for flavivirus and HCV propagation. This is a host-factor role hijacked by viruses; secondary, not the core cellular function.

- HCV: [PMID:24009510] "identified signal peptidase complex subunit 1 (SPCS1) ... Silencing of endogenous SPCS1 resulted in markedly reduced production of infectious HCV ... SPCS1 was found to interact with both NS2 and E2 ... SPCS1 plays a key role in the formation of the membrane-associated NS2-E2 complex." Note: in this paper, "Propagation of Japanese encephalitis virus was not affected by knockdown of SPCS1" — i.e. virion-assembly role here is HCV-specific via NS2/E2 interaction.
- Flaviviruses (CRISPR screen): [PMID:27383988 "A CRISPR screen defines a signal peptide processing pathway required by flaviviruses"] — SPCS1 required; "Plays a key role in the post-translational processing of flaviviral structural proteins prM, E, and NS1" (UniProt).
- JEV: [PMID:29593046] "The loss of SPCS1 function markedly reduced intracellular virion assembly and the production of infectious JEV particles but did not affect cell entry, RNA replication, or translation ... SPCS1 was found to interact with nonstructural protein 2B (NS2B) ... thereby influencing the posttranslational processing of JEV proteins and the assembly of virions." (Note: contradicts the HCV paper's statement that JEV is unaffected; later work supports a JEV role.)

## Annotation assessment summary
- GO:0005787 signal peptidase complex (IBA, IEA, IPI, TAS) — CORE, ACCEPT. Multiple lines.
- GO:0005789 ER membrane (IDA, IEA, ISS, TAS) — CORE localization, ACCEPT.
- GO:0016020 membrane (IEA, InterPro) — generic parent of ER membrane; KEEP_AS_NON_CORE (less informative).
- GO:0045047 protein targeting to ER (IBA) — SPC acts at the ER on translocated substrates; the IBA term is somewhat broad but defensible as involvement; KEEP_AS_NON_CORE (more accurate process is signal peptide processing).
- GO:0016485 protein processing (IDA, ComplexPortal) — ACCEPT; reflects SP cleavage. (GO:0006465 signal peptide processing is the more specific term; ComplexPortal also annotates GO:0006465 per UniProt DR line.)
- GO:0006508 proteolysis (TAS) — generic; the complex is a peptidase but SPCS1 itself is non-catalytic. KEEP_AS_NON_CORE / MARK_AS_OVER_ANNOTATED — it's a parent of signal peptide processing and SPCS1 is not catalytic. Keep as non-core.
- GO:0005515 protein binding (IPI x several) — KEEP_AS_NON_CORE (bare protein binding, uninformative). Interactions with SPCS2/SPCS3 (intra-complex) and with viral proteins.
- GO:0019068 virion assembly (IMP, PMID:24009510 HCV; PMID:29593046 JEV) — viral host-factor; KEEP_AS_NON_CORE.
- GO:0019082 viral protein processing (IMP, PMID:27383988) — viral host-factor; KEEP_AS_NON_CORE.
