# Horse ALDH7A1 (A0A9L0R3Y5): evolutionary grounding and residue conservation

Script: `compare_sequences.py` (Biopython global alignment, BLOSUM62, gap open -10,
extend -0.5, free end gaps). Raw output: `results.json`. Run date 2026-10-20.

## 1. Evolutionary placement

- The horse UniProt record assigns A0A9L0R3Y5 to PANTHER PTHR43521:SF1 (alpha-aminoadipic
  semialdehyde dehydrogenase), with InterPro IPR044638 (ALDH7A1-like) and CDD cd07130
  (ALDH_F7_AASADH). It is the Ensembl canonical translation ENSECAP00000057580 of horse gene
  ENSECAG00000010547 (NCBI GeneID 100063766; CTD 501 = human ALDH7A1).
- A0A9L0R3Y5 is not itself in the PANTHER 19.0 member index used by this repository; the other
  horse translation of the same gene, A0A9L0RRL6, is indexed in PTHR43521:SF1.
- PAINT (interpro/panther/PTHR43521/PTHR43521-paint.tsv) places the following IBD assertions at
  node PTN000192435:
  - GO:0004043 L-aminoadipate-semialdehyde dehydrogenase [NAD(P)+] activity, seeded by mouse, human and zebrafish experiments
  - GO:0019477 L-lysine catabolic process, seeded by mouse, human and zebrafish experiments
  - GO:0008802 betaine-aldehyde dehydrogenase (NAD+) activity, seeded by human only
  - GO:0005739 mitochondrion, seeded by mouse and human
  - GO:0005829 cytosol, GO:0005634 nucleus, GO:0000139 Golgi membrane and GO:0005886 plasma membrane, seeded by human only
- Because the node's experimental seeds include zebrafish as well as human and mouse, the node is
  at least as deep as the bony-vertebrate ancestor. Horse ALDH7A1, a eutherian 1:1 ortholog of
  human and mouse ALDH7A1, therefore descends from PTN000192435 by taxonomic bracketing, and
  inherits the node's assertions unless there is horse-specific evidence of loss.
- PAINT placed no IBD for aldehyde metabolic process, medium-chain aldehyde dehydrogenase activity,
  choline catabolism, negative regulation of ferroptosis or sensory perception of sound at any node
  of PTHR43521. These are treated here as deliberate omissions and are not added to the horse review.
- Note that human P49419 is classified by the PANTHER 19.0 HMMs in PTHR43521:SF5 while the horse,
  mouse and zebrafish orthologs are in SF1. The shared PAINT node (human, mouse and zebrafish seeds
  together) and the 95.7% identity below indicate this is a subfamily classification artifact, not a
  functional split (also raised as a question in the human review).

## 2. Pairwise identity to the PAINT seed orthologs

| Comparison | Ortholog length | Aligned columns | Identical | Identity |
|---|---|---|---|---|
| horse A0A9L0R3Y5 vs human P49419 | 539 | 539 | 516 | 95.7% |
| horse A0A9L0R3Y5 vs mouse Q9DBF1 | 539 | 539 | 468 | 86.8% |
| horse A0A9L0R3Y5 vs horse A0A9L0RRL6 | 521 | 521 | 521 | 100.0% |

Every residue of human P49419 aligns with no internal gap; human residue 1 aligns to horse
residue 28. The other horse translation, A0A9L0RRL6, is identical to A0A9L0R3Y5 over all 521 of its
residues and lacks 18 residues that A0A9L0R3Y5 retains.

## 3. Catalytic and ligand-binding residues

All 14 single-residue ACT_SITE, BINDING and SITE positions annotated (with experimental evidence)
in human P49419 are conserved in horse A0A9L0R3Y5. Horse numbering = human + 27.

| Human position | Role (human UniProt) | Human | Horse position | Horse |
|---|---|---|---|---|
| 296 | Proton acceptor (active site) | E | 323 | E |
| 330 | Nucleophile (active site) | C | 357 | C |
| 195 | Transition state stabilizer | N | 222 | N |
| 192, 194, 218, 259, 275, 297, 427 | NAD(+) binding | T, F, K, T, S, L, E | 219, 221, 245, 286, 302, 324, 454 | T, F, K, T, S, L, E |
| 331, 489, 490 | (S)-2-amino-6-oxohexanoate (AASA) binding | T, G, A | 358, 516, 517 | T, G, A |

Result: all_sites_conserved = true. The horse protein retains the full catalytic machinery and
the substrate-binding residues for alpha-aminoadipic semialdehyde. Glu427 (human), described as the
hot-spot residue for pyridoxine-dependent epilepsy mutations (PMID:31652343), is Glu454 in horse.

## 4. N-terminus

A0A9L0R3Y5 begins with a 27-residue segment, MGCPGRGAGLYFRGSSGRRRVVRPGLS, before the residue
aligned to human Met1. Neither human P49419 nor mouse Q9DBF1 has it. The human 1..26 mitochondrial
transit peptide (ECO:0000255 prediction) aligns to horse 28..53
(MWRVGRQLCVQAAGGIRLSGLWNRPA vs human MWRLPRALCVHAAKTSKLSGPWSRPA). Whether horse translation starts
at the upstream Met1 or at the Met aligned to human Met1 is not established by any data here. Nor
is whether the arginine-rich extension alters mitochondrial import. Mitochondrial localization of
horse ALDH7A1 is therefore inferred, not observed.

## Limitations

- No horse ALDH7A1 protein has been assayed. A PubMed search on 2026-10-20 for
  (ALDH7A1 OR antiquitin) AND (horse OR equine OR Equus) returned no records.
- Residue conservation shows the catalytic machinery is intact. It does not measure activity,
  substrate preference or localization.
