# recD (E. coli K-12, P04993) curation notes

Author: Claude (AI-assisted). Deep research providers were not run for this gene
(no provider API keys in this environment). The notes below summarize the cached
publications (all abstract-only except PMID:20195537) and the curated UniProt
record, with inline provenance.

## Identity and complex

- RecD is the 608-residue third subunit of the RecBCD heterotrimer (Exonuclease V)
  [file:ECOLI/recD/recD-uniprot.txt "Heterotrimer of RecB, RecC and RecD. All subunits contribute to DNA-binding."].
- The purified subunits reassemble into a fully active holoenzyme, but RecD alone
  has none of the holoenzyme activities at the concentrations tested
  [PMID:1618858 "The RecB, RecC, and RecD subunits can associate in vitro to give nuclease, helicase, ATPase, and Chi-specific endonuclease activities which are indistinguishable from those of the RecBCD holoenzyme"].
- Crystal structure: the DNA duplex is split across RecC and the strands run to the
  two motor subunits, then to the RecB nuclease domain
  [PMID:15538360 "the DNA duplex has been split across the RecC subunit to create a fork with the separated strands each heading towards different helicase motor subunits"].
  The nuclease active site is in RecB, not RecD
  [file:ECOLI/recD/recD-uniprot.txt "RecB has a slow 3'-5' helicase, an exonuclease activity and loads RecA onto ssDNA, RecD has a fast 5'-3' helicase activity"].

## Molecular function

- Purified RecD is a 5'->3' DNA helicase [PMID:12815438 "purified RecD protein is also a DNA helicase, but one that possesses a 5' --> 3' polarity"].
- In the holoenzyme RecD is the fast motor on the 5'-ended strand
  [PMID:12815437 "RecD is a fast helicase acting on the 5'-ended strand and RecB is a slow helicase acting on the 3'-ended strand"].
- RecD is an ssDNA-dependent ATPase, and the ATPase is intrinsic (K-to-Q Walker A mutant inactive)
  [PMID:9092551 "This mutant protein has no ATPase activity, indicating that the observed ATP hydrolysis activity is intrinsic to the RecD protein itself."].
- RecD binds ATP (photoaffinity labeling) [PMID:3298248 "The recB and recD subunits of the recBCD enzyme (exonuclease V) from Escherichia coli were covalently photolabeled with the ATP photoaffinity analogue"].
- RecD stimulates the RecB nuclease and processivity rather than cutting DNA itself
  [file:ECOLI/recD/recD-uniprot.txt "When added to pre-assembled RecBC greatly stimulates nuclease activity and augments holoenzyme processivity."].
  So exodeoxyribonuclease V activity (GO:0008854) is a complex activity to which RecD
  contributes; `enables` on RecD overstates it.

## Biological process

- RecBCD initiates DSB repair by homologous recombination
  [PMID:19052323 "The RecBCD enzyme of Escherichia coli is a helicase-nuclease that initiates the repair of double-stranded DNA breaks by homologous recombination."].
- In vitro joint-molecule formation with RecA and SSB depends on RecBCD unwinding
  [PMID:2014257 "RecBCD enzyme initiates the process by unwinding the linear double-stranded DNA to produce single-stranded DNA, which is trapped by SSB and RecA."].
- E. coli recD null mutants are recombination- and repair-proficient (RecBC loads RecA
  constitutively), so RecD is not necessary in E. coli; it nevertheless performs the
  5' strand motor step of wild-type end processing
  [file:ECOLI/recD/recD-uniprot.txt "Loss of RecBCD enzyme exonuclease activity, no effect on recombination proficiency or resistance to DNA-damaging agents"].
- Contrast: in Pseudomonas syringae RecD is required for repair
  [PMID:20195537 "However, RecD is not essential for DNA repair, nor does its deletion cause any growth defects in E. coli."].

## PAINT (PTHR43788) nodes reaching P04993

Tree analysis of `.cache/panther_trees/PTHR43788.json.gz` (271 leaves):

- PTN002465241: family root (all 271 leaves; SF6 RecD/RecD2/HELB, SF8 IGHMBP2,
  SF16 HELZ2, others). Carries GO:0043139 (seeds include P04993, P38935 IGHMBP2,
  Q9RT63 RecD2, O34481 YrrC, Q8NG08 HELB) and GO:0006974.
- PTN008452915: SF6-only node (51 leaves: RecD, RecD2, archaeal and eukaryotic HELB;
  Q8NG08 is human HELB, MGI:2152895 mouse Helb). Carries GO:0017116 (seeds P04993,
  Q8NG08) plus HELB-only seeded GO:0006261, GO:1903775, GO:2000042.
- PTN000095219: bacterial node, 26 SF6 leaves incl. RecD and standalone RecD2
  (Q9RT63, O34481). Carries GO:0009338 and GO:0006310, seeded by P04993 only.

Judgements: GO:0006261/GO:1903775/GO:2000042 are HELB (end-resection limiting,
replication) roles placed too deep; GO:2000042 is the opposite of RecD's role.
GO:0009338 is too deep (reaches RecD2, which is not a RecBCD subunit) but true for
RecD. `just paint-losses ECOLI recD` reports no IRD/IKR on this lineage.
