# GPC3 (donkey A0A9L0J2B1): N-terminal gene-model check (re-review, 2026-10-21)

## Question

The original comparison (`RESULTS.md`) reported 92.61% identity to human GPC3 (P51654) over
555 paired residues, with unaligned segments at the N-terminus. This re-review asks whether the
donkey model carries the human signal peptide (P51654 FT SIGNAL 1..24), which is needed for
entry into the secretory pathway, GPI anchoring and heparan sulfate addition.

## Method

`compare_nterm_rereview.py` (PEP 723 script; Biopython) finds the first exact 10-mer shared by
the donkey and human sequences, then aligns the segments before and after that anchor separately
(BLOSUM62, gap open -10, extend -0.5). Run from this folder:

```
uv run --script compare_nterm_rereview.py ../GPC3-uniprot.txt human-GPC3-P51654.fasta
```

Separately, the donkey and horse GPC3 TrEMBL entries were listed from the UniProt REST API
(query `gene_exact:GPC3 AND organism_id:9793/9796`, 2026-10-21), the Ensembl REST lookup was
used for transcript parentage, and the UniProt reference proteome one-protein-per-gene FASTA
(`UP000694387_9793.fasta.gz`, current release, downloaded 2026-10-21) was searched for the gene-centric
representative of donkey GPC3.

## Output (nterm_rereview_output.txt)

```
Donkey length 565; human length 580
First shared 10-mer: donkey 44, human 59 (GSDLQVCLPK)
Donkey N-terminal segment 1..43: MSFQFAPGGCYGHARVFDCQMVMMMEARMFIFWPRFWKGTPNK
Human N-terminal segment 1..58: MAGTVRTACLVVAMLLSLDFPGQAQPPPPPPDATCHQVRSFFQRLQPGLKWVPETPVP
N-terminal segments, global alignment: 12/33 identical paired residues
N-terminal segments, best local alignment score: 18.0
Downstream of anchor: 502/522 identical paired residues (96.17%)
Human signal peptide (FT SIGNAL 1..24): MAGTVRTACLVVAMLLSLDFPGQA
Human signal peptide present verbatim in donkey: False
```

## Other observations (from the UniProt and Ensembl queries; not computed by the script)

- A0A9L0J2B1 is encoded by Ensembl transcript ENSEAST00005057340 of gene ENSEASG00005018489,
  whose start (79332981) lies downstream of the start of the other GPC3 transcripts (79317588 /
  79317642): it uses an alternative first exon.
- The same gene also encodes A0A9L0JGR2 (580 aa, ENSEAST00005069329), whose N-terminus
  begins MAGTVHTACLVVAMLLSLDCPGQAQPPPPPPDATCHQVRSFFQRLQPGLKWVPETPVPGSDLQVCLPK, i.e. it carries
  a human-like signal peptide and is colinear with human P51654. A0A9L0JGR2 is the entry listed
  for GPC3 in the UniProt one-protein-per-gene reference proteome FASTA. The Ensembl canonical
  transcript (ENSEAST00005080949, A0A9L0J383, 611 aa) carries the same signal peptide plus a
  31-residue net insertion (611 vs 580 aa) next to human position G59.
- Horse A0A3Q2GY79 (565 aa) has the same divergent N-terminus as A0A9L0J2B1, consistent with a
  shared Ensembl equid annotation pattern.

## Interpretation

Downstream of donkey residue 44 the A0A9L0J2B1 product is 96% identical to human GPC3 and
retains the processing, glycosaminoglycan-attachment and GPI-anchor sites (see `RESULTS.md`).
Its first 43 residues are not homologous to the human signal peptide/N-terminal region (12/33
identities in a forced alignment of short segments is at background level), and the human signal
peptide is absent. A0A9L0J2B1 is therefore an alternative-first-exon gene model of donkey GPC3,
not the canonical product; whether this transcript exists and whether its product could reach the
secretory pathway is not established. The canonical donkey GPC3 product is A0A9L0JGR2.
