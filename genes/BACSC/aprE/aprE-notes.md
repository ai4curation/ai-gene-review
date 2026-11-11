# aprE (UniProtKB:F1DKR8) notes - Bacillus spizizenii ATCC 6633 = JCM 2499

## Entry identity

- F1DKR8_BACSC is an unreviewed TrEMBL entry (PE 3, inferred from homology) of
  228 residues, flagged `Fragment` with NON_TER at both residue 1 and residue 228.
- The sequence comes from a PCR amplicon, not from a genome or protein study. The
  only reference is a multiplex-PCR detection assay for rope-forming bacilli in
  bread dough, which chose aprE as the B. subtilis ATCC 6633 target and deposited
  the amplicon sequence [PMID:22555872 "lpaL and aprE genes (497 and 744 bp target
  sequences) respectively were chosen"; "The results were registered with GenBank
  under accession numbers HQ877873 and HQ871154."]. EMBL HQ871154 / ADX87424.1 is
  the source of F1DKR8.
- No full-length aprE entry for this strain (taxon 703612) or for any
  "spizizenii" taxon was returned by a UniProt query `gene:aprE AND
  taxonomy_name:spizizenii` (run 2026-10-28; F1DKR8 was the only hit).

## Sequence analysis (my own, not committed as a script)

- An ungapped comparison of F1DKR8 with B. subtilis 168 subtilisin E
  (UniProtKB:P04189, 381 aa) puts F1DKR8 residue 1 at P04189 residue 36, with
  212/228 identical residues (93%). F1DKR8 therefore spans most of the propeptide
  (P04189 30-106) and the N-terminal two-thirds of the mature protease, ending at
  the P04189 residue 263 equivalent.
- The fragment carries the catalytic Asp (F1DKR8 D103 = P04189 D138) and His
  (H135 = H170) as UniProt ACT_SITE features. It lacks the signal peptide
  (P04189 1-29) and the catalytic Ser (P04189 S327), which lies beyond the
  fragment's C-terminus. That is why UniProt adds a CAUTION that the entry
  "Lacks conserved residue(s) required for the propagation of feature annotation".
  The missing residues reflect the amplicon boundaries, not a lost function: the
  gene is a subtilisin E ortholog.

## Function (literature)

- B. subtilis ATCC 6633 (now classified as B. spizizenii) is the subtilin
  producer. In this strain, AprE is one of the extracellular serine proteases
  that cleave the leader from subtilin precursors [PMID:12705882 "Two
  extracellular B. subtilis proteases were able to activate subtilin precursors,
  the commercially available serine protease prototype subtilisin (AprE) and
  WprA."]. An aprE wprA double mutant of ATCC 6633 still made active subtilin
  [PMID:12705882 "Surprisingly, the aprE wprA double mutant of the ATCC 6633
  strain was still able to produce active subtilin, however, with a reduced
  production rate."], so AprE is one of several redundant processing proteases.
  The abstract does not say whether the "subtilisin (AprE)" used in vitro was
  the strain's own enzyme or a commercial prototype.
- The PAINT IBD for serine-type endopeptidase activity and proteolysis in
  PTHR43806 (node PTN002459139) is seeded by B. subtilis subtilisin E (P04189)
  among others (interpro/panther/PTHR43806/PTHR43806-paint.tsv).
- Subtilisin E is the reviewed reference for this ortholog
  (genes/BACSU/aprE): a secreted, Ca(2+)-stabilised alkaline serine
  endopeptidase with an Asp-His-Ser triad, made as a pre-pro-enzyme whose
  propeptide acts as an intramolecular chaperone.

## Annotation calls

- GO:0004252 serine-type endopeptidase activity (IEA): ACCEPT. The gene encodes a
  subtilisin E ortholog. Annotation applies to the gene product, not to the
  truncated sequence record.
- GO:0005576 extracellular region (IEA, from an ARBA-derived "Secreted" line):
  ACCEPT, on the basis of the ATCC 6633 extracellular-protease literature and
  subtilisin E, not on the ARBA rule. The fragment itself lacks the signal
  peptide.
- GO:0006508 proteolysis (IEA): ACCEPT, the process counterpart of the activity.
- GO:0008236 serine-type peptidase activity (IEA): MODIFY to GO:0004252, which the
  gene already carries.

## CMMMech claim check (data/records/waste-x-ray-films.yaml)

CMMMech grounds the `bacterial_stripping_then_smelting` mechanism and the
`bacillus_atcc6633_protease_extract` node to F1DKR8. Its `functional_role`
states: "Extracellular alkaline serine protease subtilisin (AprE) secreted by
Bacillus spizizenii ATCC 6633, catalyzing proteolytic hydrolysis of gelatin
emulsion proteins on waste radiographic films."

- The strain match and gene identity hold: F1DKR8 is aprE from ATCC 6633.
- The claim that AprE itself hydrolyses film gelatin is stronger than the
  evidence. Nakiboglu et al. (2001), the source CMMMech cites, used a crude
  cell-free extract and did not identify which protease(s) did the work.
  CMMMech's own evidence entry says so ("without isolating aprE or testing aprE
  deletion mutants"). B. subtilis-group strains secrete several extracellular
  proteases: ATCC 6633 has at least AprE, WprA and Vpr [PMID:12705882], and
  laboratory strains lacking six or eight extracellular proteases are standard
  hosts. The neutral metalloprotease NprE is a likely contributor to gelatin
  hydrolysis at pH 8. AprE is a plausible contributor, not a demonstrated one.
- F1DKR8 is a 228-residue PCR fragment that lacks the catalytic Ser and the signal
  peptide. It identifies the gene but is not a complete protein sequence, and
  the grounding should say so.
- "Alkaline" describes the subtilisin class (high pH optimum). The stripping run
  was done at pH 8 and 50 degrees C, which says nothing specific about AprE.
