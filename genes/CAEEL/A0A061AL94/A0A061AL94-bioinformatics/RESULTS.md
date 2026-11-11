# A0A061AL94 (mcm-4, Y39G10AR.14b): relation to canonical MCM-4 (Q95XQ8)

Script: `compare_to_canonical.py` (run with `uv run compare_to_canonical.py`); raw output in
`compare_to_canonical.out`. Inputs are fetched live from UniProt REST (A0A061AL94, Q95XQ8 FASTA and
Q95XQ8 JSON features) and Ensembl REST (gene WBGene00003156 with transcripts). A copy of the Q95XQ8
UniProt flat file retrieved on 2026-10-21 is kept as `Q95XQ8-uniprot.txt` for quotation.

## Results

- A0A061AL94 is 74 aa; canonical MCM-4 Q95XQ8 (Swiss-Prot, Y39G10AR.14a) is 823 aa.
- The fragment is an exact substring of the canonical protein: canonical residues 750-823, 100% identity,
  covering 9.0% of the canonical length. Its initiator Met corresponds to canonical Met750.
- Ensembl gene models: Y39G10AR.14a.1 has 7 exons and encodes the 823-aa protein; Y39G10AR.14b.1 is a
  single-exon model (chromosome I 2318427-2318651, minus strand) lying inside the 3' end of the
  locus and encoding the 74-aa product. The b model therefore represents translation from an internal
  start codon within the last coding exon, giving an N-terminally truncated product.
- Canonical features absent from the fragment: the C4-type zinc finger (269-294), the MCM C-terminal
  AAA+ ATPase domain (400-735) with Walker A (469-476) and Walker B (533-536) motifs, all eight annotated
  ATP-binding residues (430, 456, 475, 476, 577, 602, 692, 695) and the arginine finger (602).
- What the fragment retains is only the C-terminal winged-helix region (Pfam PF21128 WHD_MCM4 on the
  A0A061AL94 record).

## Interpretation

The fragment cannot form either half of an MCM ATPase site (it has neither the Walker A/B cis half nor
the arginine-finger trans half), so it cannot carry or contribute the ATPase/helicase activity of MCM-4
as a standalone chain. Whether the b product is translated in vivo, and whether it binds the MCM2-7 ring
or DNA, is untested; PeptideAtlas peptides mapping to this region cannot distinguish it from the
canonical protein because the sequence is identical to canonical 750-823.
