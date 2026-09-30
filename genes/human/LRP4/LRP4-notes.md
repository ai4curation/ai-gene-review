# LRP4 literature and bioinformatics notes

## Reviewed product and sequence boundaries

Human LRP4 is reviewed UniProtKB O75096, a 1,905-aa type-I membrane receptor. The
record assigns a signal peptide at residues 1–20, extracellular region 21–1725,
transmembrane helix 1726–1746, and cytoplasmic tail 1747–1905
[file:human/LRP4/LRP4-uniprot.txt, "ID   LRP4_HUMAN              Reviewed;        1905 AA."]. Its
feature table contains eight LDL-receptor class-A domains, twenty class-B repeats,
and three explicitly annotated EGF-like domains. PANTHER PTHR22722:SF15 is the
checked LRP4 subfamily for human, mouse, and rat; the broader PTHR22722 LDL-receptor
family is not safe support for an LRP4-specific ligand, interface, or signaling
function [file:human/LRP4/LRP4-uniprot.txt, "DR   PANTHER; PTHR22722:SF15; LOW-DENSITY LIPOPROTEIN RECEPTOR-RELATED; 1."].

The reviewed record has one RefSeq protein, NP_002325.2, and no ALTERNATIVE PRODUCTS
block [file:human/LRP4/LRP4-uniprot.txt, "DR   RefSeq; NP_002325.2; NM_002334.4."]. There is thus no
curated human LRP4 isoform-specific biology to summarize. Alternative initiation in
an EMBL cross-reference is not equivalent to a reviewed UniProt isoform.

## AGRIN–LRP4–MuSK neuromuscular-junction function

The defining neuromuscular role is as the extracellular organizer/coreceptor that
binds AGRIN and assembles it with MuSK, enabling AGRIN-dependent MuSK activation and
postsynaptic differentiation. The foundational study states that Lrp4 “is a receptor
for Agrin, forms a complex with MuSK, and mediates MuSK activation”
[PMID:18848351, "is a receptor for Agrin, forms a complex with MuSK, and mediates MuSK activation"].
Because that cache is abstract-only and does not expose all construct and species
details, it should be described as direct mammalian Lrp4 evidence, not as a complete
human-specific assay record. The independent PMID:18957220 study used recombinant
domains, C2C12 cells, HEK293 reconstitution, and mouse muscle, concluding that
“These observations identify LRP4 as a key component of the receptor complex of agrin.”
[PMID:18957220, "These observations identify LRP4 as a key component of the receptor complex of agrin."].
Together the two 2008 studies establish the conserved mechanism, while the later
human structure and human genetics supply the human-specific evidence.

Human evidence comes from both structure and disease genetics. In congenital
myasthenia, p.Glu1233Lys and p.Arg1277His occur in the third beta-propeller and the
mutants “decrease binding affinity of LRP4 for both MuSK and agrin”
[PMID:24234652, "domain and decrease binding affinity of LRP4 for both MuSK and agrin."].
That paper further separates the third-propeller edge that regulates MuSK signaling
from the central cavity implicated in Wnt signaling. This is useful variant-to-function
evidence, but the disease phenotype should not be substituted for a generic claim that
all LRP4 variants disrupt both pathways.

## SOST/DKK1, Wnt signaling, and bone

The bone axis is distinct from the AGRIN/MuSK axis. A primary mouse study found that
Lrp4 is expressed in osteoblasts, “binds Dkk1 and sclerostin in vitro,” and that mutant
mice have altered bone growth, density, and turnover [PMID:19936252, "binds Dkk1 and sclerostin in vitro."].
This supports a conserved osteoblast pathway but is mouse in-vivo evidence, not direct
human physiology.

Targeted human/rodent work then established direct SOST binding and facilitator
activity: recombinant assays “confirmed that sclerostin LRP4 interaction is direct”
[PMID:21471202, "confirmed that sclerostin LRP4 interaction is direct."]. LRP4
overexpression and knockdown altered SOST inhibition of Wnt1/beta-catenin signaling,
and human bone-overgrowth variants R1170W and W1186S impaired both SOST interaction
and the facilitator effect. These biochemical and cell assays support coreceptor-like
facilitation; their in-vitro setting should remain explicit.

Recessive LRP4 variants were found in twelve Cenani-Lenz syndrome families
[PMID:20381006, "LRP4 mutations in 12 families with CLS."], and tested mutations lost
LRP4 antagonism of LRP6-mediated canonical Wnt activation. This is direct human genetic
and functional evidence for the developmental/Wnt arm. Limb and kidney malformations
are consequences of altered signaling, not molecular activities in themselves.

## Human AGRIN/LRP4/MuSK structure: fragment and completeness limits

PMID:37252960 reports a 3.8-A cryo-EM extracellular complex with 1:1:1
agrin:LRP4:MuSK stoichiometry; LRP4 simultaneously recruits both partners
[PMID:37252960, "reveals that arc-shaped LRP4 simultaneously recruits both agrin and MuSK to its"].
The experiment used human proteins, but the LRP4 construct was only residues 21–1350
[PMID:37252960, "The LRP4-ECD (21-1350aa) was subcloned into a pACEMam1 vector"].
Moreover, “The entire LDLa repeats of LRP4 were not resolved in the cryo-EM map”
[PMID:37252960, "The entire LDLa repeats of LRP4 were not resolved in the cryo-EM map."].

UniProt cross-references PDB 8S9P as chain B mapped to O75096 residues 1–1905
[file:human/LRP4/LRP4-uniprot.txt, "DR   PDB; 8S9P; EM; 3.80 A; B=1-1905."], but polymer mapping is
not the same as observed coordinates. The paper's truncated construct and unresolved
regions, together with the RCSB 8S9P chain-B report of 991 unobserved residues (about
52% of the canonical sequence), mean that 8S9P must be described as a partial observed
human extracellular-complex structure, not a complete resolved full-length receptor.

## Screens, family boundaries, and citation hazards

- PMID:12421765 is a large-protein yeast-two-hybrid screen in which “yeast two-hybrid screening”
  used cytoplasmic domains and random fragments [PMID:12421765, "yeast two-hybrid screening."].
  The abstract-only cache does not expose the LRP4-WHRN pair, so the specific pair remains
  curator-supported but not independently verifiable here.

- BioPlex records are human cell-line AP-MS co-associations. BioPlex 2.0 reports “more
  than 56,000 candidate interactions” [PMID:28514442, "more than 56,000 candidate interactions"],
  while BioPlex 3.0 was built “Through affinity-purification” mass spectrometry
  [PMID:33961781, "Through affinity-purification"]. Neither screen alone proves
  direct binding or general physiological complex formation; targeted SOST evidence in
  PMID:21471202 is stronger.

- PMID:36115835 measures PDZ-domain binding to short PDZ-binding motifs, including an
  LRP4-tail dataset record. Its scope is “domains and their target PDZ-binding motifs
  (PBM) within a human interactome” [PMID:36115835, "domains and their target PDZ-binding motifs (PBM) within a human interactome"].
  This supports motif-fragment affinity, not the claim that every tested PDZ protein forms
  an in-vivo full-length LRP4 complex.

- PMID:18289866 is not an LRP4-gene paper. It says that cells were transfected with
  “mLRP4, an LRP mini-receptor” [PMID:18289866, "cells were stably transfected with Pgp or mLRP4, an LRP mini-receptor."].
  This construct-name collision cannot support amyloid-beta clearance by O75096.

- PMID:20093106 studies the distinct current LRP10 protein: its abstract says that the
  “gene family, inhibits the canonical Wnt/beta-catenin signaling pathway” in reference
  to LRP10 [PMID:20093106, "gene family, inhibits the canonical Wnt/beta-catenin signaling pathway."].
  LRP10 also appears as a historical synonym in the O75096 record, which likely explains
  the hazard, but does not justify transferring the result to LRP4.

- PMID:41162706 directly supports a non-core pathogen-entry role: “Genetic ablation of
  LRP4 impaired YFV infection of cells” [PMID:41162706, "Genetic ablation of LRP4 impaired YFV infection of cells"].
  The same study identifies LRP1 and VLDLR as additional entry receptors. This does not
  establish a unique endogenous LRP4 pathway and must not be generalized to other LDLR
  paralogs or viruses.

## Bounded synthesis for later curation

The strongest direct molecular functions are (1) AGRIN/MuSK complex organization at
the neuromuscular junction and (2) SOST-binding facilitator/coreceptor activity in the
bone Wnt-inhibitory pathway. Human genetics and the human fragment structure reinforce
those two axes and show that different third-propeller positions can preferentially
disrupt them. Mouse ortholog evidence is valuable for in-vivo development and bone
physiology, but should remain labeled as transfer. Broad LDL-receptor architecture,
large-scale co-complex screens, and peptide-domain affinity maps are insufficient to
assign cargo uptake or partner-specific signaling without LRP4-directed evidence.
