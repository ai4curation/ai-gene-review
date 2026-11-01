# Adcy8 (rat, P40146) - manual literature synthesis

No deep-research API was available for this session; this synthesis was compiled by hand from the
cached publications in `publications/` and the UniProt record (`Adcy8-uniprot.txt`). Each claim is
followed by its provenance.

## Identity and architecture

- Rat type VIII adenylyl cyclase (AC8), 1248 aa, cloned from rat brain; two cassettes of six TM
  helices each followed by a cytosolic nucleotide cyclase domain (C1, C2), the canonical
  transmembrane AC topology [PMID:8163524 "The open reading frame encodes a 1248-amino acid protein
  predicted to have two sets of six transmembrane spans and two putative nucleotide binding domains
  as is characteristic of other mammalian adenylyl cyclases"].
- Family: adenylyl cyclase class-4/guanylyl cyclase family; PANTHER PTHR45627:SF1 (adenylate
  cyclase type 8) within PTHR45627 (UniProt DR lines).
- Splice variants VIII-A/B/C differ in an extracellular glycosylated loop and a cytoplasmic segment;
  all are Ca2+/CaM stimulated [PMID:8557635 "Adenylyl cyclase activity of each of the variants is
  stimulated by Ca2+/calmodulin and the EC50 for activation of type VIII-C is one fourth of that for
  either type VIII-A or -B"].

## Catalytic activity and regulation

- Ca2+/calmodulin-stimulated adenylate cyclase (ATP -> cAMP + PPi; EC 4.6.1.1) [PMID:8163524
  "Adenylyl cyclase activity in membranes prepared from type VIII-transformed cells is stimulated up
  to 40-fold by the addition of Ca2+/calmodulin (EC50 = 53 nM calmodulin)"]. Gs-alpha synergises in
  membranes [PMID:8163524 "The addition of activated recombinant alpha subunit of Gs synergistically
  increases the Ca2+/calmodulin-stimulated activity"], but in intact neurons AC8 behaves as a "pure"
  Ca2+ sensor [PMID:18448650 "In contrast, AC8 is a pure Ca sensor. It is neither stimulated by G(s)
  nor inhibited by G(i)."].
- Two CaM-binding sites: an N-terminal 1-5-8-14 motif and a C-terminal IQ-like motif; the IQlm
  confers CaM binding and autoinhibition; Ca2+-CaM disrupts an N/C-terminal autoinhibitory
  interaction [PMID:19305019 "we propose that the IQlm alone, and not the majority of the C2b, imparts
  CaM binding and autoinhibitory functions"; "We additionally find that the N and C termini of AC8
  interact, which is an association specifically abrogated by fully Ca(2+)-bound, but not
  Ca(2+)-free, CaM"].
- Selectively stimulated by capacitative (store-operated) Ca2+ entry in non-excitable cells; needs
  lipid-raft/caveolar residence [PMID:11744699 "residence of Ca(2+)-sensitive adenylyl cyclases in
  caveolae is essential but not sufficient for regulation by CCE"]; Orai1/STIM1 reconstitute this
  [PMID:19171672 "we expressed Orai1 and STIM1 in HEK293 cells and saw a robust increment in CCE, and
  a proportional increase in CCE-stimulated AC8 activity"]; direct N-terminal Orai1 binding
  [PMID:22494970 "we have identified a direct interaction between the amino termini of
  Ca(2+)-stimulated AC8 and Orai1, the pore component of SOC channels"].
- In excitable cells, activated by Ca2+ entry through L-type channels [PMID:24086669 "In these cells,
  AC8 was activated by Ca(2+) entry through L-type voltage-gated channels following depolarisation"].
- Negative feedback: AKAP79/150 binds AC8 and recruits PKA, which phosphorylates Ser-112
  [PMID:20410303; PMID:22976297 "By site-directed mutagenesis we identify Ser-112 as an essential
  residue for direct PKA phosphorylation of AC8"]. PP2A (catalytic + scaffold subunits) binds the
  AC8 N-terminus, antagonised by Ca2+/CaM [PMID:16258073].
- Acute Gi/o-coupled mu-opioid receptor activation inhibits and chronic activation superactivates
  AC8 via Gbetagamma [PMID:16186630].
- Forms homodimers/oligomers through the TM domains [PMID:11856299; PMID:19158400].
- Associates with cortical actin through its N-terminus [PMID:22399809].

## Localisation

- Plasma membrane, lipid rafts/caveolae [PMID:11744699; PMID:19158400; PMID:19171672; PMID:16258073].
- Neurons: puncta in dendrites and axons, colocalising with synaptic markers [PMID:14585998];
  enriched in presynaptic active zone and extrasynaptic fractions, only slight PSD signal
  [PMID:17335981]. Not nuclear [PMID:11457491].

## Physiology

- Beta cells: coincidence detector for glucose/Ca2+ and GLP-1/glucagon [PMID:13680124]; required for
  GLP-1-induced cAMP, Ca2+ signalling and exocytosis amplification; downregulated by chronic high
  glucose [PMID:21046358]; Ca2+-influx-activated AC8 drives PKA activation and vesicle pool
  replenishment [PMID:25381556]; Adcy8 KO mice are glucose intolerant [PMID:25403481].
- Brain (mouse KOs): AC1/AC8 double KO lacks L-LTP and long-term memory [PMID:10482244]; AC8 KO lacks
  mossy fiber LTP [PMID:14585998], CA1 LTD and stress-induced anxiety [PMID:10864938]; memory
  acquisition deficits [PMID:18448650]; attenuated opiate withdrawal [PMID:18222416].
- Other: cholangiocyte secretin/ACh-stimulated secretion [PMID:19444869]; IL-1beta-induced
  expression switches EP3 signalling in vascular smooth muscle [PMID:16741924].
