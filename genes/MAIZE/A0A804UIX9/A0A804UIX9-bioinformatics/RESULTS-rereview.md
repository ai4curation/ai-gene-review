# A0A804UIX9 re-review: gene model, family placement and nearest relatives

Date: 2026-10-21. Script: `gene_model_rereview.py`; raw output: `gene_model_rereview_output.txt`.
Family composition figures come from UniProt REST queries run the same day (commands recorded in
`A0A804UIX9-notes.md`).

## 1. Gene model

Gene Zm00001eb381380 (B73 chromosome 9) has two annotated transcripts in Ensembl Plants:

| transcript | UniProt | canonical | protein length | exons |
|---|---|---|---|---|
| Zm00001eb381380_T001 | A0A804UIX9 | yes | 375 | 2 (CDS entirely within exon 1) |
| Zm00001eb381380_T002 | A0A804R394 | no | 316 | 4 |

T001 keeps as exon sequence two short segments that T002 splices out (46089268-46089349, 82 bp, and
46089594-46089672, 79 bp). Because neither segment is a multiple of three, the two products use
different reading frames downstream of each splice site.

## 2. Comparison with the tandem paralog

A0A804R017 (Zm00001eb380900, also on chromosome 9) is the nearest maize sequence. Identities over
target segments (identical / aligned target residues) are:

| target segment | A0A804R394 (same gene, T002) | A0A804R017 (paralog) |
|---|---|---|
| 1-44 (disordered N-terminus) | 44/44 | 22/24 |
| 45-200 (PGG domain 1, TM1-TM4) | 156/156 | 153/156 |
| 201-297 (PGG domain 2, TM5-TM6) | 41/70 | 95/97 |
| 298-375 (C-terminal tail) | 6/24 | 29/78 |

Interpretation:

- Residues 1-297 of A0A804UIX9 are almost identical to the paralog (about 98% identity over the
  aligned columns), so this part of the T001 model is well supported.
- The 78-residue C-terminal tail (298-375; RFVAHGAPGPHGGLRRWELQGGPRKHL...) does not match the paralog.
  At this point the paralog continues with the conserved PGG/transmembrane segment
  `LYGLTITALLGLMGAYAAGSCREVHESTYVICLNAGVLAYIFLQ`. The alternative transcript T002 of the same gene
  encodes the matching segment (`SWLTALLGLMGAYAAGSCREVHESTYVICLNAGVLAYIFLQE`) in a different
  reading frame. The A0A804UIX9 tail therefore looks like a frame-shifted read-through. It is not a
  conserved protein region, and the second PGG domain of A0A804UIX9 probably lacks its final
  membrane-spanning segment.
- T002 is not a better model either. It splices out residues ~228-260, which are part of the
  conserved second PGG motif (`YVAGLNPPGGFWGD`), and it encodes a frame-shifted Ser/Pro-rich segment
  in their place.
- Neither annotated product matches the paralog's architecture across the whole length. The
  benchmark accession is the canonical gene model of this locus, but its last ~78 residues are
  probably a gene-model artifact. The genomic sequence could not be retrieved (the Ensembl REST
  sequence endpoint returned 503 errors), so a three-frame translation check was not possible.

## 3. PANTHER family placement

- PTHR24177 ("CASKIN") has 12,734 UniProt members. All 12,734 are Viridiplantae
  (taxonomy_id:33090) and 0 are Metazoa (taxonomy_id:33208). Human CASKIN1 (Q8WXD9) is classified
  in PTHR24174, not PTHR24177. The family name is a PANTHER label and does not reflect animal
  members. This is a family of plant PGG proteins with or without ankyrin repeats (in a 500-member
  sample, Pfam PF13962 alone: 203; PF12796+PF13962: 195).
- No member of PTHR24177 is a reviewed (Swiss-Prot) entry, and no member has experimentally
  characterised function in UniProt.
- SF432 ("OS06G0286146 PROTEIN") contains 296 entries, all grass/monocot sequences (maize, rice,
  wheat, Panicum, Eragrostis, Carex, ...). None is reviewed.
- All five reviewed PGG-domain proteins (ACD6 Q8LPS2, ITN1 Q9C7A2, At2g01680 Q9ZU96, At5g02620
  Q6AWW5, rice NPR4 A2CIR5) are in a different PANTHER family, PTHR24186. Identity of A0A804UIX9 to
  ACD6 is low (31/123 identical in the PGG-domain-1 segment). Shared Pfam PGG domains establish only
  a domain-level relationship. They do not establish orthology or membership of the same subfamily.

## Conclusion

A0A804UIX9 is the canonical product of Zm00001eb381380. It is a grass-specific PGG-only multi-pass
membrane protein (PTHR24177:SF432). Its C-terminal ~78 residues are probably a model artifact. No
characterised protein exists in its PANTHER family, so no specific molecular function or process
can be transferred by phylogeny.
