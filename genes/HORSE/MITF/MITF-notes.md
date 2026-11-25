# MITF (horse, Equus caballus; UniProt F6ZKQ4) — notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

No prior review existed; folder created with `just fetch-gene HORSE F6ZKQ4 --alias MITF` (stub id confirmed F6ZKQ4).
ProtNLM2 output was not opened or used.

### Deep research
`just deep-research-falcon HORSE MITF --fallback perplexity-lite` failed: falcon "Failed to authenticate" and
perplexity-lite HTTP 401 (quota exceeded). No deep-research file was produced. The review uses the cached literature
below and the curated human UniProt record (saved to `MITF-bioinformatics/human-O75030-uniprot.txt`).

### Identity of the benchmark accession
- F6ZKQ4 is an unreviewed Ensembl-derived model (413 aa, PE 3). No Swiss-Prot horse MITF exists; UniProt has 8 horse MITF TrEMBL entries.
- `MITF-bioinformatics/RESULTS.md`: F6ZKQ4 aligns gaplessly to human isoform M2 (O75030-10, 413 aa, 97.8% identity). It is the
  melanocyte-type MITF-M product in its (-) splice form (no 6-aa ACIFPT segment). It lacks the 107-residue isoform-A N terminus of the
  human canonical O75030 (526 aa). K4FCY0 (419 aa) is the horse MITF-M(+) form; longer models carry the A/H/C-type N termini.
- The horse cDNA fragment Q95MD1 used for the horse EMSA (PMID:22511888) is identical in the overlapping region and also lacks ACIFPT.
- Consequence: bHLH-Zip, dimerization and C-terminal transactivation regions are intact; the Rag-binding N terminus is absent.
  [PMID:9647758 "MITF-M mRNA is exclusively expressed in melanocytes and melanoma cells"]
  [PMID:23401004 "MITF isoform 4 (also known as MITF-M) is expressed exclusively in melanocytes and melanoma cells"]
  [PMID:23401004 "In contrast, no homology was observed between the N terminus of TFEB and MITF isoforms 4, 5, and 6 or TFEC."]
  So lysosomal-membrane recruitment by Rag GTPases (PMID:23401004) and the isoform-A Ser-5 mTORC1 phospho-degron (PMID:36608670) are not transferred to this product.

### Evolutionary grounding
- PANTHER PTHR45776 (MiT/TFE transcription factor), subfamily PTHR45776:SF4 (MICROPHTHALMIA-ASSOCIATED TRANSCRIPTION FACTOR), the MITF
  ortholog subfamily that contains human MITF O75030 and mouse Mitf (MGI:104554).
- PAINT (interpro/panther/PTHR45776/PTHR45776-paint.tsv): PTN005248237 (taxon 33154, Opisthokonta; whole MiT/TFE + yeast/fly/worm members)
  carries GO:0005634, GO:0000978, GO:0000981, GO:0006357. PTN000000820 (taxon 32523, Tetrapoda; seeded only by mouse Mitf) carries
  GO:0030318 melanocyte differentiation. Horse sits inside both clades. No FamilyReview (`PTHR45776-review.yaml`) exists, so no
  subfamily-placement disagreement to report.
- PAINT did not propagate lysosome, osteoclast, mast-cell or RPE terms from the MITF/TFE members; treated as deliberate.

### Horse-specific evidence
- [PMID:22511888 "We therefore sequenced the MITF gene and found a 10 bp insertion in the melanocyte-specific promoter."]
  Splashed white (SW1) is a MITF-M promoter variant; SW3 is a frameshift (p.C280Sfs*20); macchiato is p.N310S in the basic region.
- EMSA with recombinant horse MITF bHLH-Zip (Q95MD1 residues 112-207) on an M-box oligonucleotide: wild type binds, N310S reduced ~80%.
  [PMID:22511888 "We analyzed the DNA binding properties of the mutant MITF in an electrophoretic mobility shift assay and found that DNA binding activity was reduced by about 80%"]
  This is direct horse evidence for sequence-specific DNA binding of the bHLH-Zip domain shared by F6ZKQ4.
- The white-spotting phenotypes are organismal outcomes; they are consistent with, but not used as, evidence of process participation.

### Annotation decisions (9 rows)
- ACCEPT: GO:0000978 (IBA), GO:0000981 (IBA), GO:0005634 (IBA, IEA), GO:0030318 (IBA).
- MODIFY: GO:0006357 (IBA) -> GO:0045944 positive regulation of transcription by RNA polymerase II (node term true but family-general; MITF evidence is activation).
- KEEP_AS_NON_CORE: GO:0005737 cytoplasm (regulated inactive pool; 14-3-3 retention via MARK3 site, conserved in the M isoform).
- TOO_GENERAL: GO:0006355 (entailed by GO:0006357).
- MODIFY: GO:0046983 protein dimerization activity -> GO:0042803 homodimerization + GO:0046982 heterodimerization (TFE3/TFEB/TFEC).

### Relative
Closest characterised relative by PANTHER subfamily SF4 and PAINT node PTN000000820: human MITF (O75030). No human MITF or mouse Mitf review exists
in the repo (only zebrafish mitfa/mitfb and donkey EQUAS/MITF), so human MITF needs a review.
