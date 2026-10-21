# A0A8C9H4D2 (OLFML2A, Piliocolobus tephrosceles) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM2 file or prediction-evidence folder was opened for this review.

### Identity: short isoform, not the canonical product

- A0A8C9H4D2 is 439 aa (RefSeq XP_023072933.1, "isoform X2"; Ensembl ENSPTEP00000013988.1, gene ENSPTEG00000015637.1). PE 4, unreviewed.
- The same Ensembl gene also encodes A0A8C9H9A8 (655 aa, XP_023072932.1, "isoform X1", ENSPTEP00000013996.1). A0A8C9H9A8 is the full-length product, with a SignalP signal peptide (1..27) and the olfactomedin domain at 397..655 [file:9PRIM/A0A8C9H4D2/A0A8C9H4D2-bioinformatics/A0A8C9H9A8-uniprot.txt].
- Alignment (`A0A8C9H4D2-bioinformatics/RESULTS.md`): A0A8C9H4D2 9-439 matches A0A8C9H9A8 225-655 at 99.8% identity. A0A8C9H4D2 1-439 matches human isoform 3 (Q68BL7-3, residues 1-214 missing, 215-223 ATGTGSKAQ -> MSKRDKAGK) at 97.3% over its full length. A0A8C9H4D2 is therefore the counterpart of the human alternative-first-exon isoform 3.
- What is missing compared with the canonical product: the signal peptide; both tandem CXCXCX9C motifs (8 Cys, human positions 47-100); and the coiled coil (human 157-183). The olfactomedin domain (181..439 here) is complete. The UniProt CAUTION (PRU00446, "Lacks conserved residue(s) required for the propagation of feature annotation") also appears on the record.
- The photomedin paper [PMID:15836428 "characterized by the presence of tandem CXCXCX9C motifs in the N-terminal region, a coiled-coil domain and an olfactomedin domain in the C-terminal region"] describes the full-length protein as secreted as disulfide-bonded dimers. This short product lacks the N-terminal regions that define photomedins. There is no evidence in any species that the short isoform is translated, secreted, dimerised or binds GAGs.

### Evolutionary placement

- PANTHER PTHR23192:SF29 (OLFACTOMEDIN-LIKE PROTEIN 2A), the same subfamily as human Q68BL7 and the full-length Piliocolobus A0A8C9H9A8. It is a 1:1 ortholog of human OLFML2A (the same gene, a different isoform).
- The TreeGrafter signal-transduction IEA cites PTN000573914 in the GOA with/from column. The only GO:0007165 IBD in the family PAINT file (interpro/panther/PTHR23192/PTHR23192-paint.tsv) is at PTN000573635 (taxon 33213, Bilateria), seeded only by MYOC (Q99972) and two MGI genes. I did not check the node-to-node path between PTN000573914 and PTN000573635. PAINT placed GO:0005576 and GO:0007165 at this node. It did not propagate ECM binding or self-association. Human OLFML2A IBA signal transduction was left UNDECIDED in genes/human/OLFML2A.
- The family review interpro/panther/PTHR23192/PTHR23192-review.yaml lists A0A8C9H4D2 under SF29. I agree with that placement; there is no subfamily disagreement. That review does not, however, note that A0A8C9H4D2 is the short isoform without a signal peptide.

### Literature

- The only direct experimental study is on mouse photomedin-1 (PMID:15836428, abstract only): it is secreted, forms disulfide-linked dimers and binds chondroitin sulfate E and heparin.
- The cancer cell-line studies summarised in the falcon deep research (AP-1, integrin, HGF/NGF) are perturbation and correlation studies on human OLFML2A. They are not evidence of signal transduction participation. I did not use them for GO.

### Decisions

- GO:0005576 extracellular region (IEA, ARBA SubCell): MARK_AS_OVER_ANNOTATED. The term is correct for the gene's full-length product, but this accession has no signal peptide.
- GO:0007165 signal transduction (IEA TreeGrafter): UNDECIDED, consistent with the human IBA row. The PAINT node placement is a deliberate judgment that I do not have evidence to overturn. There is no OLFML2A-specific evidence for it, and this short product lacks the secretory entry needed for extracellular signalling.
- Previous core function GO:0005201 extracellular matrix structural constituent: dropped as unsupported. Even the full-length protein has only binding evidence.
- Relative to review next: A0A8C9H9A8, the full-length product of the same gene (same_gene_canonical; no review in the repo). The human OLFML2A review (Q68BL7) is already complete.
