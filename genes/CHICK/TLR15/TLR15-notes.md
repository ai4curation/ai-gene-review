# TLR15 (chicken, UniProt A0A8V0Z0H8) — curation notes

No `TLR15-deep-research-*.md` file was produced by the batch harness before this
review was written; these notes rest on the UniProt record, the GOA rows and the
cached publications.

## Entry identity (TrEMBL, unreviewed)

`A0A8V0Z0H8_CHICK` is an unreviewed Ensembl-derived entry, 924 aa, named
"Toll-like receptor 15" with gene name TLR15, cross-referenced to
Ensembl ENSGALG00010016958, RefSeq NP_001385167 and GeneID 421219. Ensembl gives
that gene as "TLR15 toll like receptor 15 [Source:NCBI gene; Acc:421219]" on
chromosome 3, so this entry is the right gene. This matters because the project's
candidate table listed a different accession, Q2XQ10, whose submitter name is
"Toll-like receptor 2"; the entry fetched here carries the matching name and the
NCBI/Ensembl cross-references.

Architecture is canonical for a TLR: leucine-rich repeats (Pfam LRR_1, LRR_8), two
predicted transmembrane segments (59..80, 709..732) and a TIR domain (761..902),
PANTHER family PTHR24365 (subfamily SF17, named after TLR2 — consistent with the
family placement below rather than with orthology).

## Established biology

- TLR15 is restricted to birds and reptiles and is not the orthologue of any
  mammalian TLR: [PMID:23066147 "TLR15 can only be identified in avian"] and
  reptilian genomes, which places its origin after the bird/reptile–mammal split.
  Phylogenetically it falls near, but not inside, the TLR1/2/6/10 group:
  [PMID:16495540 "TLR15 groups with high bootstrap support with the recognized TLR1/TLR2/TLR6/TLR10 clade but displays no close relationship to any particular clade member"].
- It is a cell-surface receptor:
  [PMID:21383168 "In contrast to TLR9, TLR15 is expressed at the cell surface"].
- Its activation mechanism is unique among TLRs: it is not activated by binding a
  microbial molecular pattern but by proteolytic cleavage of its own ectodomain by
  secreted microbial proteases —
  [PMID:21383168 "Activation of TLR15 involves proteolytic cleavage of the receptor ectodomain"]
  and stimulation of NF-kappa-B-dependent transcription; removing the whole
  ectodomain makes the receptor constitutively active. The paper's own controls
  exclude the classical ligands: a panel including
  [PMID:21383168 "various types of TLR ligands (LPS, di- and triacylated lipopeptides, zymosan, flagellin, TLR7/8 ligand, CpG DNA, and profilin-like protein) were tested for their ability to activate TLR15"]
  with and without candidate chicken heterodimerisation partners, and
  [PMID:21383168 "a high dose of purified microbial TLR ligands did not activate TLR15"].
- An independent study found activation by yeast lysates:
  [PMID:23066147 "TLR15 mediated NF-κB induction in response to lysates from yeast, but not those"]
  [PMID:23066147 "derived from viral or bacterial pathogens, or a panel of well-characterized TLR"]
  agonists; the activity was abolished by heat or by the serine-protease inhibitor
  PMSF, which is consistent with the protease-activation mechanism rather than with
  recognition of a yeast cell-wall carbohydrate (zymosan preparations did not
  activate).
- Transcript induction after Salmonella infection was the finding that first
  described the receptor (PMID:16495540); that is expression data, not evidence of
  ligand recognition.

## Annotation decisions (summary)

The interesting rows are the two IBA annotations transferred from human TLR2
(via PANTHER:PTN002808136).

- GO:0042497 triacyl lipopeptide binding (IBA from UniProtKB:O60603/TLR2) —
  **REMOVE**. This is exactly the ligand-specificity transfer the project set out to
  check. TLR15 is not a TLR2 orthologue but a lineage-specific receptor, and the
  cleanest experimental test available reports that di- and triacylated lipopeptides
  do not activate it, with or without candidate chicken co-receptors.
- GO:0043235 signaling receptor complex (IBA, part_of, same donor) — kept as
  non-core. The donor basis is the TLR2/TLR1 heterodimer, which TLR15 does not form
  as far as anyone has shown, but TLRs signal as dimers and the truncated receptor's
  autoactivation was interpreted as self-dimerisation, so complex membership is
  defensible at this generic level while the identity of the complex is unknown.
- GO:0002224 (IBA) modified to GO:0035681 toll-like receptor 15 signaling pathway.
  The receptor-specific term exists, it names this receptor, and two independent
  studies show NF-kappa-B activation initiated at this receptor.
- GO:0038023 signaling receptor activity (IBA) — **accepted deliberately, and not
  upgraded to GO:0038187 pattern recognition receptor activity**. GO:0038187 requires
  combining with a pathogen-associated molecular pattern; TLR15 is activated by
  cleavage of its ectodomain, and the proteases that cleave it are enzymes rather
  than patterns bound by the receptor. The generic receptor term is the accurate one
  here, which is worth recording explicitly because every other reviewed TLR in this
  batch takes the GO:0038187 upgrade.
- GO:0005886 plasma membrane (IBA) accepted: unusually for an IBA location call in
  this family, it is confirmed experimentally for this receptor by surface
  biotinylation and confocal microscopy.
- GO:0007165 and GO:0016020 kept as non-core.
