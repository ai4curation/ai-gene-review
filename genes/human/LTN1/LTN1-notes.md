# LTN1 (Listerin) research notes

UniProt: O94822 (LTN1_HUMAN). Gene synonyms: RNF160, ZNF294, C21orf10. 1766 aa.
EC 2.3.2.27 (RING-type E3 ubiquitin transferase). HGNC:13082.

## Core function
LTN1/Listerin is the RING-type E3 ubiquitin ligase of the ribosome-associated quality
control (RQC) complex. It poly-ubiquitinates nascent polypeptides that remain housed in
the 60S large ribosomal subunit after a stalled 80S ribosome is split, marking them for
proteasomal degradation (via VCP/p97 extraction).

- [PMID:25578875 "the 60S-housed nascent polypeptides are poly-ubiquitinated by Listerin"]
- [PMID:25578875 "its mammalian homolog Listerin was both necessary and sufficient for ubiquitination of stalled translation products"]
- UniProt FUNCTION: "E3 ubiquitin-protein ligase component of the ribosome quality control complex (RQC) ... mediates ubiquitination and extraction of incompletely synthesized nascent chains for proteasomal degradation"
- CATALYTIC ACTIVITY EC=2.3.2.27.

## Mechanism / NEMF dependence
Listerin's specificity for nascent-chain–60S complexes depends on NEMF. The 3.6 Å cryo-EM
structure of a nascent chain–60S–Listerin–NEMF complex shows NEMF contacts 60S and
peptidyl-tRNA to sense nascent-chain occupancy; ribosome-bound NEMF recruits and stabilizes
Listerin's N-terminal domain, and Listerin's C-terminal RWD domain contacts the ribosome to
position the ligase (RING) domain near the nascent polypeptide exit tunnel.
- [PMID:25578875 "Listerin specificity for nascent chain-60S complexes depends on nuclear export mediator factor (NEMF)"]
- [PMID:25578875 "ribosome-bound NEMF recruits and stabilizes Listerin's N-terminal domain, while Listerin's C-terminal RWD domain directly contacts the ribosome to position the adjacent ligase domain near the nascent polypeptide exit tunnel"]

## Domain architecture
N-terminal HEAT/ARM repeats (16 HEAT repeats) form a ring that wraps the 60S; C-terminal
RING-CH / RING-type zinc finger (residues 1715–1762) is the catalytic ligase domain. The
RING coordinates zinc (zinc ion binding is a structural feature of the RING).

## Subunit / complex
Component of the RQC complex (LTN1 + NEMF + TCF25), associated with the 60S ribosomal
subunit; the complex probably also contains VCP/p97.
- UniProt SUBUNIT: "Component of the ribosome quality control complex (RQC), composed of the E3 ubiquitin ligase LTN1, TCF25 and NEMF associated with the 60S ribosomal subunit"
- GO term GO:1990112 RQC complex (IDA, PMID:25578875).

## Localization
Cytoplasm/cytosol; associated with cytosolic ribosomes (60S). [PMID:28757607] used for
cytosol IDA in GOA.

## PMID:28757607 caveat
This paper (Matsuo et al. 2017) is about Hel2/RQT1 ubiquitination of 40S uS10 (the ZNF598
ortholog branch), not Listerin catalysis per se. It is cited in LTN1 GOA only for cytosol
localization (located_in GO:0005829). Relevance to LTN1 = LOW/contextual.

## PMID:21903422 caveat
Li et al. 2011 Immunity — innate immunity interactome (IRF7, STING1/TMEM173, TIRAP). These
are the IntAct "protein binding" partners (Q92985 IRF7, Q86WV6 STING1, P58753 TIRAP). High-
throughput innate-immunity interactome; not part of LTN1's core RQC ligase function.

## Autoubiquitination
LTN1 is autoubiquitinated (UniProt PTM, by similarity to mouse Q6A009). Supports
GO:0051865 protein autoubiquitination (Ensembl IEA).

## Actions summary
- Core MF: GO:0061630 ubiquitin protein ligase activity (IDA PMID:25578875) -> ACCEPT (core).
- GO:0072344 rescue of stalled cytosolic ribosome, GO:1990116 ribosome-associated ubiquitin-
  dependent protein catabolic process, GO:1990112 RQC complex -> ACCEPT.
- GO:0043023 ribosomal large subunit binding -> ACCEPT (binds 60S).
- GO:0008270 zinc ion binding -> ACCEPT (RING structural, non-core).
- GO:0005515 protein binding (IPI innate-immunity partners) -> KEEP_AS_NON_CORE.
- cytosol/cytosolic ribosome terms -> ACCEPT.
- GO:0004842, GO:0016567, GO:0051865 -> ACCEPT/KEEP_AS_NON_CORE (ubiquitination process/parent).
