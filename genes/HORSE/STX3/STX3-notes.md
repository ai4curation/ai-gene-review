# STX3 (horse, A0A3Q2H352) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not opened or used. Deep research could not be generated:
`just deep-research-falcon HORSE STX3 --fallback perplexity-lite` failed (falcon
"Failed to authenticate"; perplexity HTTP 401 insufficient quota). The review rests on
the cached literature below, the UniProt records and the PANTHER/PAINT data.

### Identity of the benchmark accession

- A0A3Q2H352 is an unreviewed TrEMBL entry (PE 3), Ensembl ENSECAT00000043417.3,
  289 aa, VGNC:23730 STX3. There is no Swiss-Prot horse STX3 entry. Horse has four
  more STX3 TrEMBL gene models (F7BC79, A0A3Q2H370, A0A5F5PZR6, F6ZUC9). All four diverge
  after about residue 226 and lack a recognisable anchor, so A0A3Q2H352 is the only horse
  model with a complete SNARE motif plus transmembrane anchor
  [file:HORSE/STX3/STX3-bioinformatics/RESULTS.md].
- PANTHER: PTHR19957:SF34 SYNTAXIN-3. Human Q13277, mouse Q64704 and rat Q08849
  belong to the same subfamily (interpro/panther/PTHR19957/PTHR19957-entries.csv). So
  STX3 is the orthologous subfamily, not a paralogous syntaxin.
- Exon structure: residues 1-226 match mouse 3A/3B and human isoform A at 99% identity. Residues 227-262
  (C-terminal half of the SNARE motif) are 100% identical to the mouse 3B-specific segment
  (exon 9B, the retinal STX3B exon). Residues 263-289 (the membrane anchor) are the exon-10A
  (STX3A-type) anchor. Human retina RNA-seq describes STX3A as exons 9A/10A and STX3B as
  9B/10B [PMID:33974130 "RNA-sequencing data sets from normal human retina samples were analyzed for the presence of matching reads corresponding to STX3A (exons 8/9A, 9A/10A) and STX3B (exons 8/9B, 9B/10B)"].
  This model is therefore an unusual 9B/10A combination. It may be a minor transcript or an
  Ensembl gene-model artefact. It is full-length and keeps every functional
  module (N-peptide, Habc, Qa-SNARE motif with 0-layer Q, TMD), so gene-level function
  transfer is unaffected. Isoform-specific (3A versus 3B) claims are not transferred.

### Literature (orthologs, same PANTHER subfamily SF34)

- Apical exocytosis in epithelia (human): [PMID:26553929 "Apical exocytosis of NHE3, CFTR (cystic fibrosis transmembrane conductance regulator), and GLUT5 required an interaction cascade of Rab11, Myo5B, Slp4a, Munc18-2, and Vamp7 with Stx3"]. Loss-of-function variants cause variant MVID [PMID:24726755 "STX3 is an apical receptor involved in membrane fusion of apical vesicles in enterocytes."].
- Postsynaptic AMPAR exocytosis during LTP (rodent): [PMID:23395379 "the Q-SNARE proteins syntaxin-3 and SNAP-47 are required for regulated AMPAR exocytosis during LTP but not for constitutive basal AMPAR exocytosis"].
- Photoreceptor OS protein trafficking (mouse): [PMID:32778589 "STX3 is an essential part of the trafficking pathway for both disc (rhodopsin) and rim (PRPH2/ROM1) components of the OS."].
- Retinal STX3B: [PMID:33974130 "STX3B is highly expressed in human retina and that the protein is enriched in the inner and outer segments of photoreceptors and in ribbon synapses of the human retina"].
- Isoforms: [PMID:7598732 "Syntaxin 3B contained a different sequence in the carboxyl terminal region from that of syntaxin 3A."]. A soluble nuclear isoform (Stx3S) acts as a transcriptional regulator [PMID:29475951]. That isoform lacks the anchor, so it does not apply to this TMD-bearing model.

### PAINT

- PTN000461349 (root syntaxin node): SNARE binding, SNAP receptor activity, SNARE complex,
  vesicle fusion, intracellular protein transport, endomembrane system. Human STX3 Q13277 is among the
  endomembrane-system seeds.
- PTN000461524: plasma membrane, exocytosis (GO:0006887, IBD dated 20260828; not yet in
  this horse GOA set, so it is proposed as NEW).
- PTN002717040 (Euteleostomi, taxon:117571): postsynapse and exocytic insertion of
  neurotransmitter receptor to postsynaptic membrane, seeded by mouse Stx3 (MGI:103077,
  SynGO IDA). Horse is inside this clade.
- No FamilyReview yaml exists for PTHR19957 (only entries/metadata/paint), so there is no subfamily
  disagreement to report.

### Relative

No reviewed horse canonical entry exists, so the same_gene_canonical rule does not apply.
The closest characterised ortholog in SF34 is human STX3 (Q13277). It has no review in the repo
(no genes/human/STX3), so it needs review. The donkey STX3 (EQUAS, A0A9L0J901) is a
cohort partner reviewed by another agent.
