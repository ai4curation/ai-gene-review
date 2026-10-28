# Q2U1U6 gene-model check (2026-10-21)

Script: `gene_model_check.py` (run with `uv run gene_model_check.py`); raw output in
`gene_model_check_output.txt`. Inputs are fetched live from UniProt REST and NCBI
E-utilities (AP007170.1, the RIB40 contig SC138 carrying AO090138000091).

## Question

Q2U1U6 (AO090138000091) is 134 aa, whereas other proteins with the chondroitin
AC/alginate lyase fold (IPR008929/SSF48230) are several hundred residues. Is the
134-aa product a real protein, or a truncated gene model?

## Results

1. **Q2U1U6 is the C-terminal end of a ~408-aa protein.** Q2U1U6 residues 6-134 align to
   residues 280-408 of the *A. flavus* NRRL 3357 protein A0A7U2MCM8 (408 aa) with 128/129
   identity, and of *A. minisclerotigenes* A0A5N6JAE3 (408 aa) with 128/129 identity. The
   *A. fumigatus* protein Q4WKU8 (399 aa) aligns over residues 272-398 with 97/127 identity.
   All of these full-length proteins end where Q2U1U6 ends. The *A. oryzae* var.
   *brunneus* entry A0ABQ6LHX9 (745 aa) carries Q2U1U6 as residues 612-745 (134/134
   identity), fused C-terminally to a beta-lactamase-related domain (IPR001466, residues
   6-345), which looks like a merged gene model in that assembly.
2. **The missing N-terminal 279 residues are encoded in the RIB40 genome.** Exact 8-mer
   peptides of A0A7U2MCM8 residues 1-280 (273 of 279 8-mers) map contiguously to the plus
   strand of AP007170.1 at ~186173-187010, in a different reading frame (+1) from the
   annotated CDS (frame 0, 187060-187464). Residues 280-408 map to the annotated CDS.
3. **A 65-nt GT...AG intron joins the two parts.** The exon-1 sequence ending
   `...GAAGCGGGGCGTGATCAAG` (E-A-G-R-D-Q + first base of Gly) is followed by a 65-nt
   intron (187011-187075, `GTACCG...CAGCATCAG`) whose removal reconstitutes the Gly
   codon (GGC) immediately before His-Thr-Met-Ser of exon 2. The annotated start codon
   (ATG at 187060) lies **inside** this intron, so the AO090138000091 model begins at an
   intronic ATG and omits exon 1.
4. Domain coverage: in the full-length *A. flavus* protein, InterPro places the
   IPR008929 / SSF48230 / Gene3D 1.50.10.100 domain at residues ~62-371. Q2U1U6 covers
   only residues 280-371 of that domain (its SSF48230 match is residues 6-97), i.e.
   roughly the last third of the alpha/alpha toroid.

## Interpretation

Q2U1U6 is a **truncated gene model**: the RIB40 locus very probably encodes a ~408-aa
protein (exon 1 of ~279 codons plus the annotated exon), orthologous to A0A7U2MCM8 of
*A. flavus*. The benchmark accession is not a plausible complete protein. Any functional
statement about this locus applies to the full-length product, not to the 134-aa
translation. The full-length protein has no PANTHER family or Pfam family assignment;
its only signature is the fold-level chondroitin AC/alginate lyase superfamily.

## Limitations

- The intron was located by exact-peptide mapping and splice-signal inspection, not by
  RNA-seq; transcript evidence was not checked.
- No signal-peptide or catalytic-residue analysis was run on the full-length product.
- Gene-model inference is based on the *A. flavus* ortholog's model; that model is also
  unreviewed (TrEMBL, PE 4).
