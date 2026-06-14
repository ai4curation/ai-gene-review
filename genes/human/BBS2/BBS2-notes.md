# BBS2 (Q9BXC9) curation notes

(See BBS2-ai-review.yaml for the structured review.)

## Identity and structure
- Human BBS2, "BBSome complex member BBS2" / Bardet-Biedl syndrome 2 protein. 721 aa. UniProt Q9BXC9, HGNC:967.
- Domain architecture (InterPro/Pfam): N-terminal β-propeller (WD40/YVTN repeat-like, Gene3D 2.130.10.10), middle domain, GAE (γ-adaptin ear) domain, hairpin, platform, and C-terminal helical (CtH) domain. A coiled-coil region (residues 325–369) mediates interaction with MKKS/BBS6. Architecture is coatomer/adaptin-like, consistent with the BBSome being a coat-like complex [UniProt Q9BXC9 FT/DR].
- BBS2 together with BBS7 and BBS9 forms the β-propeller/GAE/platform scaffold core of the BBSome.

## Core complex membership (BBSome)
- BBSome is a stable octameric complex of BBS1, BBS2, BBS4, BBS5, BBS7, BBS8/TTC8, BBS9, and BBIP1/BBIP10 [PMID:17574030 "seven highly conserved BBS proteins form a stable complex, the BBSome"; PMID:19081074 BBIP10 added as eighth subunit].
- ComplexPortal CPX-1908 (BBSome complex). TCDB 3.A.33.1.1 "the bbsome complex (bbsome) family".
- BBS2 interacts directly via its C-terminus with BBS7, and via its coiled coil with MKKS/BBS6 [UniProt SUBUNIT]. IntAct: strong BBS2–BBS7 (NbExp=17), BBS2–BBS9 (NbExp=14), BBS2–BBS1 (NbExp=10).
- BBSome assembly is chaperonin-assisted: BBS6/MKKS, BBS10, BBS12 form a complex with CCT/TRiC chaperonins that mediates BBSome assembly; BBS7 is delivered by the chaperonin to nucleate assembly [PMID:20080638; PMID:22500027].

## Function — ciliary membrane protein trafficking
- BBSome functions as a coat complex for sorting specific membrane proteins to/from primary cilia. It cooperates with the GTPase Rab8 (via Rabin8/RAB3IP GEF) to promote ciliary membrane biogenesis [PMID:17574030 "A core complex of BBS proteins cooperates with the GTPase Rab8 to promote ciliary membrane biogenesis"; UniProt FUNCTION].
- ARL6/BBS3-GTP recruits the BBSome to the membrane to form a coat that sorts ciliary cargo (Reactome R-HSA-5624126/5624127). LZTFL1 binds the BBSome and regulates its ciliary trafficking and Smoothened/Hedgehog signaling [PMID:22072986; Reactome R-HSA-5624129].
- BBSome with LZTFL1 controls SMO ciliary trafficking and contributes to SHH (sonic hedgehog) pathway regulation [UniProt FUNCTION].
- Required for ciliogenesis but dispensable for centriolar satellite function [UniProt FUNCTION].
- Localizes to cilium membrane, basal body, and cytoplasm; also reported at centriolar satellites and ciliary transition zone [UniProt SUBCELLULAR LOCATION; HPA IDA GO:0035869].

## Function — receptor signaling / obesity (cargo trafficking)
- BBS proteins are required for leptin receptor (LepR) signaling in the hypothalamus. Bbs2-/-, Bbs4-/-, Bbs6-/- mice are leptin-resistant; leptin-induced STAT3 phosphorylation reduced; Pomc expression reduced [PMID:19150989]. BBS1 is the direct LepRb interactor, but BBS2 depletion also mistraffics LepRb (large perinuclear vesicles), so BBS2 is functionally required for LepRb trafficking [PMID:19150989 Fig 6 "We found similar mistrafficking of LepRb when BBS2 protein was depleted"]. This supports involvement in leptin-mediated appetite regulation and fat-cell/obesity phenotypes, mechanistically via membrane-receptor trafficking.

## Disease
- Bardet–Biedl syndrome 2 (BBS2; MIM 615981): pigmentary retinopathy, obesity, polydactyly, hypogenitalism, renal malformation, intellectual disability; autosomal recessive (occasional triallelism) [UniProt DISEASE; PMID:11285252 positional cloning].
- Retinitis pigmentosa 74 (RP74; MIM 616562): nonsyndromic RP caused by BBS2 missense mutations (p.A33D, p.P134R, p.D104A, p.R632P) [PMID:25541840]. Basis for the IMP "visual perception" annotation — supports photoreceptor cilium/role in vision.

## Specific annotations evaluated
- GO:0034464 BBSome (part_of): strongly supported by multiple experimental sources (IDA PMID:17574030, IDA PMID:24550735, IPI PMID:19081074 ComplexPortal, IMP PMID:19150989, plus IBA/IEA). CORE.
- GO:0060170 ciliary membrane (located_in): supported, ComplexPortal IDA PMID:19081074, UniProt SubCell. CORE localization.
- GO:0036064 ciliary basal body / GO:0035869 ciliary transition zone: experimentally supported localizations (IDA PMID:18299575; HPA IDA). Accept.
- GO:0005829 cytosol / GO:0005737 cytoplasm: BBSome assembles and exists in cytoplasm before ciliary entry; supported. Accept as non-core background localization.
- GO:0034451 centriolar satellite: UniProt SubCell SL-0485; also note UniProt FUNCTION explicitly states BBSome is "dispensable for centriolar satellite function" but BBS4 recruits BBSome there. Localization reported. Accept (located_in) but non-core.
- GO:0060271 cilium assembly (involved_in): BBSome required for ciliogenesis; well supported. CORE process.
- GO:0007601 visual perception (IMP PMID:25541840): supported by RP74 disease (photoreceptor cilium). Keep as non-core (downstream/organismal).
- GO:0043001 Golgi to plasma membrane protein transport (IMP PMID:19150989): the leptin paper shows LepRb mistrafficking between Golgi and plasma/ciliary membrane in BBS2-depleted cells. Reasonable; keep (non-core, related to receptor trafficking).
- GO:0038108 negative regulation of appetite by leptin-mediated signaling pathway (ISS/IEA from mouse Q9CWF6): supported by Bbs2-/- leptin resistance phenotype [PMID:19150989]. Keep as non-core.
- GO:0045444 fat cell differentiation (ISS/IEA): BBS proteins implicated in adipogenesis/obesity; transfer from mouse. Keep as non-core (organismal phenotype, plausible but indirect).
- GO:0061629 RNA polymerase II-specific DNA-binding transcription factor binding (IPI PMID:22302990, WITH UniProtKB:Q99496=RNF2/RING2): based on a paper foregrounding BBS7 interacting with PcG member RNF2; "our data supports a similar role for other BBS proteins." This is an interaction-based MF annotation. RNF2 (Q99496) is a transcriptional repressor (PRC1). The annotation captures a physical interaction; the broader "direct role in transcription" is contested/indirect. Mark as over-annotated / keep cautiously — interaction is real but functional significance for BBS2 specifically is weak. Use UNDECIDED-leaning; this is an experimental IPI so do not REMOVE — mark non-core / over-annotated.

## protein binding (GO:0005515) IPI annotations
- Numerous IntAct/IPI GO:0005515 protein binding annotations to BBSome partners (BBS1, BBS7, BBS9, BBS12, MKKS), assembly chaperonins, and to non-BBSome partners (ALDOB P05062, CCDC28B Q9BUN5, DLEC1 Q9Y238, IQCB1/NPHP5 Q15051, PCM1 Q9NRI5, and many high-throughput Y2H/AP-MS hits such as HNRNPF, LMO4, MDFI, NRF1, RBPMS, PSME3, FNDC3B, TUBA P68104, KRT8 Q15154, etc.).
- Per curation guidelines, GO:0005515 "protein binding" is uninformative and should be marked over-annotated; the informative MF is the structural/adaptor role within the BBSome (no good specific MF term beyond complex membership — BBS2 has no catalytic activity; it is a scaffolding subunit). Many HT-interactome hits (HNRNPF, NRF1, RBPMS, KRT8, TUBA) are likely non-specific.

## Mouse/ISS-transferred BP terms (GO_REF:0000024, from mouse Q9CWF6)
- Brain/CNS development terms (striatum, hippocampus, cerebral cortex development, brain morphogenesis, adult behavior), photoreceptor cell maintenance, negative regulation of multicellular organism growth, sperm axoneme assembly, melanosome transport, intracellular protein localization, regulation of cilium beat frequency.
- These are organismal/tissue phenotypes of Bbs2 loss in mouse, transferred by ISS. Most are downstream consequences of ciliary dysfunction rather than direct BBS2 molecular functions. Keep developmental/behavioral ones as non-core; melanosome transport and regulation of cilium beat frequency are weakly supported (motile-cilia term applies more to airway; BBS2 loss alters motile cilia morphology per PMID:18299575). sperm axoneme assembly relates to flagellar/cilium role.

## Key references verified
- PMID:17574030 — BBSome definition + Rab8/ciliary membrane biogenesis (HIGH).
- PMID:19081074 — BBIP10/eighth subunit; ciliogenesis, MT stability (HIGH for complex membership/localization).
- PMID:19150989 — leptin receptor signaling/trafficking, Bbs2-/- (HIGH).
- PMID:25541840 — BBS2 missense → nonsyndromic RP74 (HIGH for vision).
- PMID:22302990 — BBS7 (and "other BBS proteins") interaction with RNF2, transcriptional role (MEDIUM, BBS7-centric).
- PMID:18299575 — Bbs loss alters motile cilia in airway (MEDIUM; supports motile cilium localization/cilium beat).
- PMID:33144677 — DLEC1 interaction (spermatogenesis paper) (LOW-MEDIUM, interaction only).
