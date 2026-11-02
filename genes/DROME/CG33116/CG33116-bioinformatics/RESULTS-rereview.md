# CG33116 (Q9VIU4) re-review: subfamily placement and CAPT motif

Date: 2026-10-20. Scripts: `tree_rereview.py` (output `tree_rereview_output.txt`,
`rereview_consensus.nwk`, `rereview_aln.fasta`) and `capt_motif_rereview.py`
(output `capt_motif_rereview_output.txt`). Run with
`uv run --with biopython --with requests python tree_rereview.py`.

## PANTHER subfamily composition (UniProt stream, 2026-10-20)

- PTHR10414:SF71 (CG33116's subfamily): 692 UniProt entries, 0 vertebrate,
  405 arthropod, 130 nematode entries; includes C. elegans ept-1 (O44732),
  molluscs, flatworms, rotifers and cnidarians. It is the invertebrate EPT1-type
  subfamily.
- PTHR10414:SF47 (human SELENOI/EPT1 Q9C0D9, mouse Selenoi): 718 entries,
  717 vertebrate.
- The fly paralogs fall elsewhere: bbc/CG6016 (dCCS2) in SF37 (with yeast
  CPT1/EPT1, Arabidopsis AAPT1), cpt/CG7149 (dCCS3) in SF36. Cpes/CG4585
  (dCCS4) carries no PTHR10414 assignment.

## Tree (MAFFT + NJ, identity distance, 100 bootstraps; 13 sequences)

Identity to CG33116: CG7149 51.3%, mollusc SF71 49.3%, human/zebrafish SELENOI
48.1%, worm ept-1 43.5%, cnidarian SF71 41.7%, versus bbc 32.6%, CHPT1 29.0%,
CEPT1 25.4%, yeast EPT1/CPT1 ~29%.

The NJ tree places CG33116 with CG7149 (bootstrap 66) inside a clade containing
SELENOI (SELENOI pair 84), the mollusc, worm and cnidarian SF71 members, apart
from the CHPT1+CEPT1 pair (58) and fly bbc. Deep nodes are not resolved by
bootstrap at this sampling, so the tree alone is weak; the conclusion that
CG33116 is an invertebrate member of the EPT1/SELENOI lineage rests jointly on
(i) PANTHER subfamily composition (SF71 invertebrate vs SF47 vertebrate),
(ii) the identity pattern, and (iii) the primary paper's own statement that
CG33116 and CG7149 share a single human orthologue from a fly-lineage
duplication (PMID:23449981).

## CAPT motif

All EPT1-lineage sequences (CG33116, CG7149, SELENOI, mollusc, cnidarian) carry
`...PLGELFDHGLD`, whereas CEPT1, CHPT1, bbc and AAPT1 carry `...DHGCD`. CG33116
retains every conserved motif residue, including the two terminal aspartates
reported as catalytic in CEPT1 (D-H-G-L-D at 134-138). The worm ept-1 sequence
did not match the strict regex (a motif variant); this is not interpreted
further. The L/C difference correlates with the clades but is not, by itself,
evidence of donor specificity.

## Limitations

No CG33116 enzyme assay exists; donor (CDP-ethanolamine vs CDP-choline) and
acceptor (DAG vs alkylacylglycerol) preference are inferred from lineage.
