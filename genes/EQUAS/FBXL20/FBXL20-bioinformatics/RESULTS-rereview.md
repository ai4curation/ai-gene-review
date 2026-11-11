# FBXL20 (donkey A0A9L0IQA3): N-terminal exon comparison (re-review, 2026-10-21)

Reproduce: `uv run --script genes/EQUAS/FBXL20/FBXL20-bioinformatics/nterm_exon_rereview.py > genes/EQUAS/FBXL20/FBXL20-bioinformatics/nterm_exon_rereview_output.txt`

Method: sequences fetched from UniProt REST; for each FBXL20 gene product the
script locates the conserved motif MFSNSDEAV (which starts the region shared by all
full-length forms, about 7 residues before the F-box) and reports the sequence
upstream of it, the length downstream of it, and whether the C-terminus ends in the
CAAX-type tail CCIIL. This supersedes the "12-residue insertion" reading in
RESULTS.md (that file is kept unchanged); the global aligner there paired five
N-terminal residues by chance.

## Output

```
A0A9L0IQA3	len=448	motif_start=27	prefix=MRSVLVPQLPSMQAVIFKATAHLGIG	caax_tail=yes	after_motif_len=422
Q96IG2	len=436	motif_start=15	prefix=MRRDVNGVTKSRFE	caax_tail=yes	after_motif_len=422
Q9CZV8	len=436	motif_start=15	prefix=MRRDVNGVTKSRFE	caax_tail=yes	after_motif_len=422
Q58DG6	len=436	motif_start=15	prefix=MRRDVNGVTKSRFE	caax_tail=yes	after_motif_len=422
F6YIL4	len=437	motif_start=16	prefix=MQAVIFKATAHLGIG	caax_tail=yes	after_motif_len=422
A0A5F5PIX0	len=463	motif_start=15	prefix=MRRDVNGVTKSRFE	caax_tail=yes	after_motif_len=449
A0A9L0IZC9	len=438	motif_start=17	prefix=MAPSRDRLLHFGFKAT	caax_tail=yes	after_motif_len=422
A0A9L0JDR0	len=447	motif_start=26	prefix=MSERPMKTHDGGQRGWSTPQRKWNG	caax_tail=yes	after_motif_len=422
A0A9L0J589	len=397	motif_start=NA	prefix=(motif absent)	caax_tail=yes	after_motif_len=NA
A2A536	len=210	motif_start=17	prefix=MAPSRDRLLHFGFKAT	caax_tail=no	after_motif_len=194
```

## Interpretation

- A0A9L0IQA3 carries a 26-residue N-terminal segment (MRSVLVPQLPSMQAVIFKATAHLGIG)
  in place of the 14-residue N-terminus of the reviewed human, mouse and bovine
  canonical products (MRRDVNGVTKSRFE). The two segments are not homologous, so this
  is an alternative first exon (alternative gene model), not an insertion.
- Downstream of the motif, A0A9L0IQA3 has the same 422-residue length as the
  canonical human, mouse and bovine products, so the F-box, the full LRR domain and
  the C-terminal CAAX tail are all present.
- The same alternative N-terminal segment (MQAVIFKATAHLGIG) begins the horse gene
  product F6YIL4, and other donkey models (A0A9L0IZC9, A0A9L0JDR0) and a mouse
  model (A2A536) carry yet other first exons, so FBXL20 uses several alternative
  first exons. No donkey model in this set has the canonical MRRDVNGVTKSRFE start
  together with an intact F-box (A0A9L0J589 lacks the motif region).
- The functionally characterised parts of FBXL20 (F-box for SKP1 binding, LRR
  domain for substrate binding, CAAX motif for membrane targeting) all lie
  downstream of the variable N-terminal segment.
