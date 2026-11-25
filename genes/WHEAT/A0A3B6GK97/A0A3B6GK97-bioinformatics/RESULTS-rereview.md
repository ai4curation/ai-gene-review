# Re-review analysis (2026-10-20): gene model, homoeologs and phylogenetic placement of A0A3B6GK97

This supplements `RESULTS.md` (which is unchanged). It asks whether the missing N-terminal
catalytic region of the 302-aa TraesCS3D02G033600 model is a gene-model artifact that hides an
intact patatin active site, or whether the locus genuinely lacks the catalytic serine.

## Reproduce

```
uv run python scripts/gene_model_rereview.py --query A0A3B6GK97 \
  --comparators A0A3B6E9X0,A0A9R1KF31,A0A3B6FIU7,A0A1D5WV83,A0A453DST9,A0A453DST0,Q6ZG46,O48723 \
  --gene TraesCS3D02G033600 --upstream 8000 --outdir results_rereview
uv run python scripts/sf103_motif_scan_rereview.py --subfamily PTHR32176:SF103 \
  --taxon 147389 --out results_rereview/sf103_triticeae_motifs.tsv
```

Inputs are fetched live from UniProt REST and Ensembl REST (IWGSC RefSeq v1.1 assembly). Outputs:
`results_rereview/summary_rereview.json`, `results_rereview/upstream_frames.fasta`,
`results_rereview/sf103_triticeae_motifs.tsv`. The PANTHER tree was retrieved from the PANTHER
API (`treeinfo?family=PTHR32176`, PANTHER 19, filtered to Arabidopsis, rice, wheat and potato).

## 1. PANTHER tree placement

- A0A3B6GK97 is in PTHR32176:SF103, a grass (BEP-clade) subfamily. Its speciation node
  PTN002083020 (BEP clade) contains rice Os08g0476900 (Q6ZG46), Os08g0477100 (Q6ZG42),
  Os08g0376500 and Os08g0376550 and many wheat copies; no Arabidopsis or other dicot member
  of the filtered tree falls inside it.
- The sister of the SF103 clade (at duplication node PTN008645074) is rice PLP2 (Q6ZJD3,
  SF26), a reviewed entry whose function is "By similarity" only (no experimental data).
- The SF103 + rice PLP2 clade joins the clade holding the Arabidopsis pPLAII proteins
  (PLP1/O23179, PLP4/Q9FIY1, PLP5/O23180 in SF89; PLP2/O48723 in SF109) and rice PLP1
  (Q84QY3, SF5) only at the deeper duplication node PTN009133995. A0A3B6GK97 is therefore
  not an ortholog of any Arabidopsis pPLAII protein. The nearest experimentally characterised
  relatives are those Arabidopsis pPLAII proteins (out-paralogs across a pre-monocot/dicot
  duplication), of which PLP2/pPLAIIalpha (At2g26560, O48723) is the best studied.
- "pPLAII" in `RESULTS.md` is therefore correct only in the broad sense (the pPLAII-type
  soluble patatin clade), not as orthology to the Arabidopsis pPLAII genes.

## 2. Homoeologs and paralogs

Local alignment of the query to its relatives (`summary_rereview.json`):

| Accession | Locus | Length | G-x-S-x-G | DGGG | Identity to query (aligned span) |
|---|---|---|---|---|---|
| A0A3B6GK97 (query) | TraesCS3D02G033600 | 302 | none | none | - |
| A0A3B6FIU7 | TraesCS3B02G036500 | 444 | none | none | 93.3% (query 17-302) |
| A0A9R1KF31 | TraesCS3B02G036800 | 434 | GTSTG 97 | 58 | 89.2% |
| A0A3B6E9X0 | TraesCS3A02G046500 | 433 | GTSTG 96 | 57 | 88.5% |
| A0A1D5WV83 | TraesCS3D02G033200/033500 | 433 | GTSTG 96 | 57 | 88.8% |
| Q6ZG46 | rice Os08g0476900 | 430 | GTSTG 92 | 53 | 74.6% |
| O48723 | Arabidopsis PLP2 | 407 | GTSTG 64 | 25 | 54.0% |

The closest relative is A0A3B6FIU7 (3B, 93.3% identity), which is a full-length (444 aa) model
and **also lacks both the catalytic-serine elbow and the DGGG oxyanion block**. The other
chromosome-3 SF103 copies (3A 046500, 3B 036800, 3D 033200/033500) are intact.

## 3. Genomic sequence upstream of the 3D locus

The 8 kb upstream of TraesCS3D02G033600 (3D:12377036-12385035, + strand) was translated in the
three forward frames. In frame 0, about 1.5 kb upstream of the annotated start, a segment aligns
to residues 1-150 of the 3B homoeolog A0A3B6FIU7 at 87.3% identity, beginning with the
homoeolog's start (MPSMQQAEAGAEQRS...). The intervening stretch carries stop codons and is
absent from FIU7, consistent with an intron. This indicates that TraesCS3D02G033600 is an
**incomplete gene model**: its true product probably resembles the 444-aa 3B homoeolog, with
about 140 N-terminal residues encoded upstream of the annotated start.

The reconstructed N-terminal region, however, does **not** restore the active site:

- The oxyanion block reads `SIDGGDVRG` (genomic 3D) and `SIDGGSVCG` (3B protein) where the
  intact paralogs read `SIDGGGVRG`.
- At the position where the intact paralogs carry `...DYFDVIAGTSTGGLV...`, both the 3D
  genomic translation and the 3B protein carry an unrelated segment
  (`...RRRQRRCYETNANPPEDTFPP...` in FIU7). No G-x-S-x-G motif homologous to the nucleophile
  elbow is encoded in any forward frame of the 8 kb upstream region; the few G-x-S-x-G matches
  in frames 1 and 2 have no homology to the patatin N-terminus.

## 4. Catalytic motifs across Triticeae SF103 members

`sf103_triticeae_motifs.tsv` lists 38 Triticeae SF103 entries. Many, mostly short fragments,
lack the motifs; among models of 300 aa or more, A0A3B6FIU7 (444), Aegilops tauschii
A0A453DST9 (386) and A0A453DST0 (390), and durum wheat A0A9R1RW72 (303) and A0A9R1Q5T7 (309)
lack both motifs. This is a motif census only; orthology of these entries to the query was not
established (the two Aegilops entries share 86.8% identity with the query over 182 residues but
have unrelated N-termini).

## Conclusions

1. The 302-aa model is an incomplete gene model (the missing N-terminal exons are present in
   the genomic sequence upstream).
2. Even the reconstructed full-length product, and the full-length 3B homoeolog, lack the
   catalytic serine nucleophile and the canonical oxyanion glycines. The 3B/3D homoeolog pair
   is therefore predicted to encode a **non-catalytic patatin-like protein** (a pseudo-patatin
   that keeps the C-terminal two-thirds of the fold and the catalytic Asp but has lost the Ser).
3. Lipid acyl hydrolase activity, and the IBA lipase terms propagated from node PTN001282408,
   should not be transferred to this product.

## Caveats

- No RNA-seq or transcript evidence was examined; whether the locus is expressed, and which
  exons are used, is untested.
- The exon/intron structure was inferred from protein-to-genome alignment of one homoeolog,
  not from a spliced-alignment tool.
- Loss of the catalytic serine strongly predicts loss of patatin-type ester hydrolysis but
  says nothing about possible non-catalytic roles (for example lipid binding).
