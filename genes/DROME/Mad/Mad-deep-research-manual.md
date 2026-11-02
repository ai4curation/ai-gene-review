# Mad (Mothers against dpp; CG12399; P42003): manual literature synthesis

No deep-research API provider was available in this session. This file was written by hand by the
reviewing agent from the UniProt record (`Mad-uniprot.txt`) and cached publications under
`publications/`. Most cached papers are abstract-only; full-text papers are flagged below.

## Identity and family

- Mad is the founding member of the SMAD family: the Drosophila BMP-pathway receptor-regulated
  Smad (R-Smad), ortholog of vertebrate SMAD1/5/9 [PMID:11703946 "binds the Smad1/5 ortholog MAD"].
- Cloned as a dominant enhancer of weak dpp alleles; "MAD is a member of a novel, highly conserved
  protein family" [PMID:7768443].
- Domain architecture: N-terminal MH1 (DNA binding via a beta-hairpin), proline-rich linker,
  C-terminal MH2 (protein interaction, trimerisation) ending in the receptor-phosphorylated SSXS
  motif (Ser453/Ser455) [UniProt P42003 FT/CC].

## Signal transduction mechanism

- Mad acts in responding cells, cell-autonomously, downstream of Dpp receptors
  [PMID:8681796 "Mad is an essential component of the signal transduction pathway downstream of the
  Dpp receptors in responding cells"; PMID:8681791 "MAD is required specifically in cells responding to
  DPP"].
- Phosphorylation by Tkv induces homo-oligomerisation and hetero-complex formation with Medea
  (Smad4) [PMID:9693372 "Mad forms a heteromeric complex with Drosophila Smad4 (Medea) upon
  phosphorylation by Thick veins (Tkv)"; "Mad exists as a monomer in the absence of Tkv stimulation"].
- Mad drives nuclear translocation of Medea [PMID:9502733 "Mad is required to actively translocate
  Medea into the nucleus"; PMID:9502724 "MEDEA ... requires physical association with MAD for nuclear
  translocation"].
- Besides Tkv/Sax, the activin receptor Baboon can phosphorylate Mad directly, held in check by
  dSmad2 competition [PMID:22563507, full text; PMID:18820452].
- Cytoplasmic in unstimulated cells [PMID:8681791 "Immunohistochemical studies localize MAD to the
  cytoplasm in all tissues examined"]; with endogenous tagging only a minor fraction becomes nuclear
  [PMID:39494616, full text].

## Transcription factor activity

- MH1 domain has sequence-specific DNA binding, revealed when the C-terminus is removed; Mad binds and
  is required for the vestigial quadrant enhancer [PMID:9230443].
- Activation elements (AE) recruit Mad/Medea; Brinker competes for binding [PMID:20010841;
  PMID:11306550 full text "Brinker efficiently competes with Mad in vitro"].
- Silencer elements (SE): a trimeric Mad/Medea complex (two Mad, one Med) recruits the zinc-finger
  protein Schnurri to repress brinker, bam and other genes [PMID:12705870; PMID:17008448; PMID:16109720
  per UniProt]. This is the main mechanism of Dpp gradient read-out in the wing.
- Shn binds Mad directly and they act synergistically [PMID:11071761].
- In motor neurons, both AE- and SE-type motifs mediate direct activation by pMad/Med, independent of
  Shn and Brk [PMID:36029115, full text].
- Negative feedback on dpp transcription via BMP-SE motifs [PMID:40955849, full text].

## Regulation of Mad

- E3 ligase Smurf binds and degrades phosphorylated Mad [PMID:11703946; PMID:12754252].
- eIF4A promotes activation-dependent Mad/Medea degradation [PMID:17115029].
- PDP phosphatase dephosphorylates the SSXS motif [PMID:16510868].
- Linker phosphorylation by CDK8 and Shaggy/GSK3 limits signal intensity and range [PMID:25377173,
  full text]; Yorkie binds linker-phosphorylated Mad [PMID:19914168, full text].
- Nemo phosphorylates Ser25 and promotes nuclear export [PMID:17507407; PMID:19451277 at the NMJ].
- Lis1 binds and stabilises Mad in germline stem cells [PMID:21041636].
- Nuclear accumulation requires nucleoporin Nup154 [PMID:21696798].
- The Ski/Sno-family protein Fussel binds Medea, not Mad, and impairs Mad/Medea complex function
  without blocking pMad nuclear translocation [PMID:22879948, full text: "we could not verify an
  interaction of Fuss with Mad on an in vitro level"; "Fuss does not inhibit the nuclear translocation
  of pMad"].

## Biological contexts (all downstream of BMP signalling)

Embryonic dorsal-ventral patterning, midgut/visceral mesoderm induction, wing and other imaginal disc
patterning and growth, eye morphogenetic furrow initiation, pupal retina patterning, R7/R8 subtype
pairing (with dSmad2) [PMID:28853393], ovarian germline and somatic stem cell maintenance
[PMID:9695953; PMID:16256740; PMID:21041636], intestinal stem cell regulation [PMID:20056890;
PMID:23733344], retrograde BMP signalling for NMJ growth [PMID:15046722; PMID:22959350; PMID:19451277],
Ap4/FMRFa neuron specification [PMID:26092715], histoblast spreading [PMID:20226662].
These are contexts in which Mad acts as the BMP transcriptional effector; they are pleiotropic outcomes
rather than distinct molecular functions.
