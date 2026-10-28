# pilA (PA4525, P04739) notes

## Identity

- UniProt P04739 (PILA_PSEAE), reviewed, 149 aa, type IVa major pilin.
  6-residue leader cleaved by PilD and N-methylated on Phe7; N-terminal
  hydrophobic helix (residues 7-27, membrane-spanning before assembly);
  C-terminal globular domain with the 134-147 disulfide loop. Pfam PF00114
  Pilin, PF07963 N_methyl; PANTHER PTHR30093:SF34.

## Literature

- Fibre structure: cryo-EM of the native PAO1 pilus [PMID:39666767 "PilA
  subunits constituting the T4P exhibit a classical pilin fold featuring an
  extended N-terminal α-helix linked to a C-terminal globular β-sheet-containing
  domain, which are packed tightly along the pilus"]; the globular domain coats
  the fibre surface [PMID:39666767 "The α-helical core of the pilus is
  surrounded by the C-terminal globular domain of PilA that coats the outer
  surface of the pilus, mediating interactions with the surrounding
  environment."].
- Inner-membrane pool regulates its own transcription via PilS [PMID:27162347
  "We suggest that direct interactions between PilA and PilS in the inner
  membrane reduce pilA transcription when PilA levels are high."].
- pilA mutant (strain PAK) lacks pili and twitching; reduced association with
  and invasion of corneal epithelial cells [PMID:12933890 "The pilA mutant is
  twitching motility negative because it lacks pili and thus was used as a
  control to distinguish the contributions of pili and their twitching
  motility function."].
- Attachment: SPR shows pilA mutants are defective in attachment
  [PMID:16849183 "Both mutants lacking pili (pilA), and those possessing an
  overabundance of pili (pilT), showed reduced SPR measured attachment
  compared with the wild-type PAO1 strain."].
- Biofilm caps formed by pilus-driven migration [PMID:14507363 "The migrating
  bacteria form the mushroom caps by climbing the stalks and aggregating on the
  tops in a process which is driven by type-IV pili."].
- Host Ca2+ signalling via CAMLG: yeast two-hybrid and over-expression of pilA
  inside BEAS-2B cells [PMID:23266901 "Overexpression of the pilA gene in
  BEAS-2B cells resulted in a significant increase in cytoplasmic Ca(2+)"].
  Host ER membrane location (UniProt EXP) comes from this paper; it reflects
  heterologous expression of PilA inside host cells, not a demonstrated
  delivery route during infection.
- PMID:2985436 (Pasloske et al. 1985) cloned and sequenced the strain PAK
  pilin gene; abstract-only, says nothing about location assay. PAK pilin is a
  different-strain orthologue (both group II pilins). The location claim is
  nevertheless certain for PAO1 PilA (PMID:39666767).
- PMID:9224878 (Alm and Mattick 1997, Gene) is a review of type 4 fimbrial
  genes [PMID:9224878 "Thus far over 30 genes have been characterized"]; an
  IMP from it is an evidence-code error (TAS would be correct).
- PMID:25049409 (Chung et al. 2014, Tip phage protein inhibits PilB): CACAO
  rows for cell surface and cytosol. Full text not available via PMC tool
  (PMC4128137 returned no body). Surface PilA (sheared pili) is fine; the
  cytosol row is odd because unassembled pilin is an inner-membrane protein.

## PANTHER node PTN002013003

- IBDs of GO:0043107 and GO:0044096 (2019-08-22), WITH UniProtKB:P04739 only.
  Two sub-nodes (PTN004739243, PTN004739244) carry NOT IRDs for both terms
  (2026-03-04), so PAINT curators have already pruned divergent branches.
- Remaining leaves (10, 9 taxa): P. aeruginosa PilA, E. coli K-12 PpdD
  (P36647), H. influenzae PpdD homologue (P44623), Salmonella (Q7CR79),
  Yersinia (A0A5P8YC84), Coxiella (Q83EZ7), Shewanella PilA (Q8EJP5),
  Xanthomonas PilE and XCC3098, Vibrio VC_2423. All PTHR30093:SF34 major
  pilins. The location claim (major pilin of a type IV pilus) fits the clade.
  Motility is less certain for leaves from species without documented
  twitching (E. coli K-12 PpdD is cryptic; H. influenzae is non-motile, its
  pili mediate competence/adherence), but the seed itself is sound.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN002013003 | GO:0043107 type IV pilus-dependent motility | 1 (sole) | 10 (9 taxa) | GO:0043107, IDA, PMID:12933890; GO:0043107, IMP, PMID:9224878 (PseudoCAP) | SOUND | PilA is the fibre subunit whose extension/retraction drives twitching; pilA mutants are non-piliated and non-twitching. Evidence codes are off (12933890 is a mutant assay, so IMP; 9224878 is a review, so TAS), recorded as PSEUDOCAP defects; the claim stands. Motility at the node is a mild over-reach for PpdD of E. coli K-12 and H. influenzae, which do not twitch. |
| PTN002013003 | GO:0044096 type IV pilus | 1 (sole) | 10 (9 taxa) | GO:0044096, IDA, PMID:2985436 (PseudoCAP) | SOUND | PilA is the major structural subunit of the fibre (cryo-EM, PMID:39666767). The cited paper is a strain PAK gene-sequencing paper whose abstract shows no location assay, so the reference is weak, but the claim is correct and appropriate for a clade of major pilins. |

## Decisions summary

- ACCEPT: plasma membrane (EXP, IEA); cell adhesion (IEA); motility (IBA,
  IDA, IMP); type IV pilus (IBA, IDA).
- MODIFY to GO:0044096 type IV pilus: pilus (EXP, IDA, IEA); cell surface
  (IDA).
- KEEP_AS_NON_CORE: biofilm attachment (IMP 16849183), biofilm formation on
  inanimate substrate (IMP 14507363).
- MARK_AS_OVER_ANNOTATED: host cell ER membrane (EXP, IEA); regulation of
  calcium-mediated signaling (IMP).
- UNDECIDED: cytosol (IDA, CACAO, full text unavailable).
