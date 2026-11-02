# Nedd4 (rat, UniProt Q62940) - manual literature synthesis

No deep-research provider was available for this review. This file was compiled by hand
from the cached publications in `publications/`, PubMed searches, and the UniProt record
(`Nedd4-uniprot.txt`). Each claim carries its provenance.

## Identity and domain architecture

- Rat Nedd4 (Nedd4-1; RGD:3157; GeneID 25489) is an 887-aa HECT-type E3 ubiquitin ligase.
  The UniProt record annotates a C2 domain (54-180), three WW domains (246-279, 402-435,
  459-492) and a C-terminal HECT domain (551-887) [UniProtKB:Q62940 FT DOMAIN].
- Rat Nedd4 was cloned as the binding partner of the ENaC PY motifs: "rNedd4 contains a
  Ca2+ lipid binding (CaLB or C2) domain, three WW domains and a ubiquitin ligase (Hect)
  domain" [PMID:8665844].
- Catalysis: HECT E3s accept ubiquitin from an E2 as a thioester on a catalytic cysteine and
  transfer it to substrate lysines. UniProt: "E3 ubiquitin-protein ligase which accepts
  ubiquitin from an E2 ubiquitin-conjugating enzyme in the form of a thioester and then
  directly transfers the ubiquitin to targeted substrates" (by similarity to human P46934)
  [UniProtKB:Q62940 CC FUNCTION].

## Substrate recognition by WW domains (rat experimental)

- "the rNedd4-WW domains mediate this association by binding to the P2 regions, which
  include the PY motifs (XPPXY) of either betarENaC (PPPNY) or gammarENaC (PPPRY)"
  [PMID:8665844].
- NMR structure of the rat Nedd4 WW3 domain with the betaENaC PY peptide: "Here we report
  the solution structure of the third WW domain of Nedd4 complexed to the PY motif-containing
  region of betaENaC" [PMID:11323714].
- ENaC is ubiquitinated in vivo and ubiquitination limits surface channel number:
  "Our results suggest that ENaC function is regulated by ubiquitination" [PMID:9351815]
  (abstract only). In vivo the dominant renal ENaC regulator is the paralog Nedd4-2
  (NEDD4L); Nedd4-1's role in ENaC control is mainly from overexpression/binding studies.
- Immunolocalization in rat kidney and lung epithelia expressing ENaC; "microvillar borders
  of proximal convoluted tubules expressed variable amounts of rNedd4" [PMID:9227416]
  (abstract only).

## Neuronal functions

- Dendrite development via Rap2A: "Nedd4-1, the serine/threonine kinase TNIK, and Rap2A form
  a complex that controls Nedd4-1-mediated ubiquitination of Rap2A" and "Nedd4-1 KO leads to
  the development of shorter and less complex dendrites" [PMID:20159449]. Ubiquitination
  requires catalytic activity: "The ubiquitination of Rap2A was abolished when catalytically
  inactive instead of WT Nedd4-1 was used" [PMID:20159449]. Ubiquitination is mainly mono-,
  with "a minor fraction of Rap2A is modified by Nedd4-1 via K63-linked di-ubiquitination"
  [PMID:20159449]. Note the genetics are in mouse; rat brain synaptosome extracts were the
  source for the WW-domain affinity screen.
- AMPA receptor trafficking: Nedd4-1 ubiquitinates GluA1 and is "necessary for this process"
  of AMPA-induced endocytosis and lysosomal sorting in rat hippocampal neurons [PMID:21148011]
  (abstract only in cache). Independently, in rat cortical/hippocampal neurons "Nedd4 is
  enriched in synapses, co-distributes and physically associates with AMPAR subunits" and
  "knockdown of Nedd4 by specific siRNAs abolishes AMPAR ubiquitination" [PMID:21338354].
- Neuromuscular junction: Nedd4-null mice have abnormal NMJs; "Nedd4 is involved in
  regulating the formation and function of the NMJs through non-cell autonomous mechanisms"
  [PMID:19345204].

## Muscle

- Denervation atrophy in rat gastrocnemius increases Nedd4 protein: "MTMR4 decreases approx.
  90% with a 2-fold increase in Nedd4 expression" [PMID:19125695]. The ubiquitination and
  binding experiments in that paper used human NEDD4 and human MTMR4 in HEK293/HeLa cells;
  "Ubiquitinated MTMR4 (seen as a high-molecular-mass smear) was detected in
  immunoprecipitates only when wild-type MTMR4 was transfected, but not in immunoprecipitates
  from the PY-mutant-transfected or untransfected lysate" [PMID:19125695]. The rat-specific
  datum is therefore an expression response to denervation.

## Development and immunity (mouse ortholog)

- "disruption of Nedd4-1 in mice (leaving Nedd4-2 intact) caused embryonic lethality at mid
  gestation, with pronounced heart defects (double-outlet right ventricle and
  atrioventricular cushion defects) and vasculature abnormalities" [PMID:20026598].
- T cells: "Nedd4 was required for polyubiquitination of Cbl-b induced by CD28
  costimulation" and "Nedd4 promotes the conversion of naive T cells into activated T cells"
  [PMID:18931680].
- Mast-cell signalling (rat RBL cells): Nedd4 and Cbl "become associated with lipid rafts
  after activation of IgE signaling" [PMID:11248052]; this is a relocalization observation,
  not a demonstrated role in an immune response.

## Nuclear / DNA damage (human ortholog)

- "we identified Nedd4 as an E3 that associates with and ubiquitylates RNAPII in response to
  UV-induced DNA damage in human cells" [PMID:17996703].

## Synthesis

Nedd4 is a HECT E3 whose molecular function is ubiquitin transfer to PY-motif substrates
recognized by its WW domains. Its best-supported cellular outcomes are monoubiquitination /
K63-linked ubiquitination of membrane proteins (ENaC, receptor tyrosine kinases, AMPA
receptor GluA1) that drives endocytosis and lysosomal degradation, and mono-ubiquitination
of the small GTPase Rap2A that promotes dendrite growth. Many organismal phenotypes
(heart/vascular development, NMJ, T-cell activation) are downstream consequences established
by mouse knockouts.
