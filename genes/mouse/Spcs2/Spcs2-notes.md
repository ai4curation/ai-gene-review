# Spcs2 (mouse, A0A140LHW5) review notes

## 2026-10-20 full re-review

This re-review is independent of any machine-learning function predictions; none were used.

### Identity of the benchmark accession: a short splice product, not the canonical protein

- A0A140LHW5 (TrEMBL, 74 aa) = Ensembl ENSMUSP00000146574, from transcript ENSMUST00000208465
  (Spcs2-206, protein_coding, not Ensembl canonical). The canonical product is Q9CYN2
  (Swiss-Prot SPCS2_MOUSE, 226 aa; Ensembl ENSMUST00000036274, Spcs2-201). Both are MGI:1913874.
- Exon structure (Ensembl REST, see [RESULTS.md](Spcs2-bioinformatics/RESULTS.md)):
  Spcs2-206 keeps coding exons 1 and 2, skips exon 3 (161 nt, not a multiple of 3) and joins exon 2
  to an internal acceptor 75 nt into exon 4. Exons 1+2 encode exactly residues 1-66, so the product
  is identical to Q9CYN2 for 66 residues, then reads 8 frame-shifted residues (KRPHRNGS) before a
  TGA stop in exon 4. The stop is about 33 nt upstream of the last exon junction, so the transcript is
  not an obvious NMD target by the 50-nt rule (an inference, not tested).
- Missing relative to the canonical protein: the last 20 residues of the N-terminal cytoplasmic
  domain (67-86), both transmembrane helices (87-107, 112-132), the lumenal loop and the whole
  C-terminal cytoplasmic domain (133-226). The record has no InterPro/Pfam (PF06703 SPC25)/PANTHER
  match. MobiDB-lite calls all 74 residues disordered; the retained segment is the Gly-rich,
  low-complexity N-terminus that is disordered in the canonical protein too.
- PE 1 on the record is gene-level proteomics; nothing shows peptides from the unique tail.

### Evolutionary grounding

- Canonical mouse Spcs2 (Q9CYN2) and human SPCS2 (Q15005) are both in PANTHER PTHR13085:SF0
  (SIGNAL PEPTIDASE COMPLEX SUBUNIT 2); they are 1:1 orthologs. A0A140LHW5 itself has no PANTHER
  assignment because it lacks the family domain.
- PAINT node PTN000317824 (taxon Eukaryota) carries IBD for GO:0005787 signal peptidase complex,
  GO:0045047 protein targeting to ER and GO:0051604 protein maturation
  (`interpro/panther/PTHR13085/PTHR13085-paint.tsv`). None of these propagated to A0A140LHW5;
  GOA for this accession is empty. This is correct: complex membership depends on the membrane
  helices and the C-terminal domain that this product does not have.
- The family review `interpro/panther/PTHR13085/PTHR13085-review.yaml` already says the same thing
  (canonical Q9CYN2 in SF0; short product without an exact PANTHER assignment). No disagreement
  about subfamily placement.

### Literature

- Human SPC structures: SPCS2 is noncatalytic; catalysis is in SEC11A/SEC11C
  [PMID:42173868 "the catalytic SPC subunit (paralog Sec11A or Sec11C, respectively) is joined by SPCS1 (also known as SPC12), SPCS2 (SPC25), and SPCS3 (SPC22/23)."].
  SPCS2 sits next to Sec61beta [PMID:42173868 "proximal localization of SPCS2 to Sec61β would position the SPC close to the lateral gate of Sec61α"].
- The Falcon deep-research report (Spcs2-deep-research-falcon.md) describes the canonical protein
  and does not notice that A0A140LHW5 is truncated; its claims about two transmembrane helices and
  integral membrane topology do not apply to this accession.
- No paper studies the Spcs2-206 product.

### Decisions

- existing_annotations: none (GOA empty for this accession).
- core_functions: none asserted. The only plausible functions (complex membership, ER membrane
  location) belong to the canonical product and need regions this product lacks. Proposing NEW
  annotations here would transfer canonical-protein function to a product that cannot carry it.
- Closest characterised relative: human SPCS2 (Q15005), ortholog of canonical mouse Spcs2 in
  PTHR13085:SF0; complete review at `genes/human/SPCS2/SPCS2-ai-review.yaml`.
- Module: `modules/dmel_signal_peptidase_complex.yaml` (Drosophila SPC; Spase25 is the fly
  ortholog). No mammalian SPC module exists.
- Previous version of this review cited a ProtNLM source JSON and its sequence-mapping script read
  that file. Both dependencies removed: the script now reads the sequence from Spcs2-uniprot.txt.
