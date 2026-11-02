# NTPase (O76268) re-review: isoform identity and subfamily relatives

Script: `compare_isoforms_rereview.py` (run with `uv run compare_isoforms_rereview.py`);
raw output: `results-rereview.json`. Sequences are fetched live from UniProt REST.

## Isoform identity

The benchmark accession O76268 is NTPase-PA (461 aa), one of four UniProt products of the gene.
O76268 is a full-length isoform, not a fragment. NTPase-PE (Q9VQI8, 464 aa) differs only in the first
residues (alternative first exon). NTPase-PF (M9PBV2, 524 aa) carries the same N-terminus as PE and an
internal insertion of about 63 residues just after the transmembrane segment. NTPase-PC/PD (Q8IPZ6, 271 aa)
is an N-terminally truncated product identical to O76268 residues 191-461. It lacks the
transmembrane segment and the ACR1 motif DAGSTGS.

The residues named in the cloning paper (PMID:19467631; C42 in the transmembrane domain and C447 in the
exoplasmic domain) are both cysteine in O76268 numbering. In PE or PF numbering they would be offset by
3 or more residues. The characterised cDNA therefore uses PA (O76268) numbering. O76268 position 202 is
Glu, the PIRSR-predicted proton acceptor.

## Relatives

| Accession | Protein | PANTHER subfamily | Global identity to O76268 | Aligned columns |
|---|---|---|---|---|
| Q9XU84 | C. elegans uda-1 | PTHR11782:SF127 (same as fly) | 0.416 | 387 |
| O75356 | human ENTPD5 | PTHR11782:SF35 | 0.423 | 392 |
| O75354 | human ENTPD6 | PTHR11782:SF99 | 0.418 | 426 |

Pairwise identity is about 42% against all three, so it does not separate them. The phylogenetic
placement comes from PANTHER, which puts fly NTPase in the same subfamily (SF127) as C. elegans uda-1
and puts the vertebrate ENTPD5 and ENTPD6 in separate subfamilies. This means the fly "NTPDase6" name
indicates family-level similarity, not one-to-one orthology with human ENTPD6.
