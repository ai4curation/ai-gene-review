# A0A7P0T7Z1 (ACAD9-219) compared with canonical ACAD9 (Q9H845)

Script: `compare_gene_model.py`. Run it with `uv run --script compare_gene_model.py > results.txt`.
It fetches both UniProt sequences and both Ensembl transcript structures live. The raw output is in
`results.txt` (run 2026-10-21, Ensembl REST and UniProt REST).

## Sequence comparison

- A0A7P0T7Z1 has 626 aa and Q9H845 has 621 aa.
- Residues 1-521 are identical (521 aa). The sequences diverge from residue 522.
- Canonical 522-621: `TIMEEQLVLKRVANILINLYGMTAVLSRASRSIRIGLRNHDHEVLLANTFCVEAYLQNLFSLSQLDKYAPENLDEQIKKVSQQILEKRAYICAHPLDRTC`
- A0A7P0T7Z1 522-626: `ETKTGKDAAQGGTMWGTGLGSESPLGASVIPDHHGGAAGTEAGGQHPHQPVWHDGRAVAGQPLHPHWAPQPRPRGSLGQHLLRGSLLAESLQPLSAGQVCSRKPR`
- The two tails share no 6-mer. The alternative tail is Gly/Pro/His-rich (G+P+H fraction 0.35). UniProt
  marks residues 527-599 of A0A7P0T7Z1 as a MobiDB-lite disordered region. It is not a rearranged copy of
  the canonical C-terminus.

## Gene-model basis

Both transcripts have 18 exons and share every exon boundary except two.

- Exon 1 of ENST00000680636 starts 80 nt further upstream. This is 5' UTR only: the protein N-terminus
  is identical, so the script's frame label for exon 1 does not apply to the coding sequence.
- Exon 16 of ENST00000680636 uses an acceptor 94 nt upstream of the canonical acceptor
  (128909927 vs 128910021). 94 mod 3 = 1, so the extra exonic sequence shifts the reading frame for
  the rest of the CDS. This accounts for the unrelated 105-residue tail from residue 522 and for the
  different stop codon.
- The alternative stop codon (genomic 128912528) lies in the last exon (128912507-128913114). A simple
  premature-stop rule therefore does not predict nonsense-mediated decay. Whether this transcript
  makes a stable protein in cells has not been tested. Peptide-level proteomics support for the
  entry (PeptideAtlas/ProteomicsDB keywords) cannot tell it apart from the canonical product unless
  a peptide covers residues 522-626. No such peptide was examined here.

## Retention of canonical structural and functional regions

Region coordinates are taken from the canonical literature (PMID:33320993, PMID:38086790) and from the
Q9H845 UniProt record.

| Region (canonical numbering) | Status in A0A7P0T7Z1 |
|---|---|
| Mitochondrial transit peptide 1-37 | retained (identical) |
| ACAD N-terminal, middle and C-terminal Pfam domains (68-173, 177-277, 290-437) | retained (identical) |
| Catalytic proton acceptor Glu426 | retained (identical) |
| Solvent-exposed linker 445-482 | retained (identical) |
| ECSIT-contact loop 488-496 | retained (identical) |
| Vestigial dehydrogenase domain 493-587 (PMID:33320993; 487-587 in PMID:38086790) | partial: 493-521 retained, 522-587 lost |
| ECSIT-contact helix-turn-helix 554-560 | lost |
| Dimer-stabilising C-terminal helix 588-621 (helix-swapped residues 600-621, PMID:38086790) | lost |

The UniProt cross-references are consistent with this. A0A7P0T7Z1 carries Pfam PF02771, PF02770 and PF00441,
but not PF21343 (ACAD9-ACADV_C) or InterPro IPR049448 (ACAD9/ACADV-like_C), which Q9H845 carries.

## Interpretation

- The whole catalytic dehydrogenase module is identical to the canonical enzyme, including the transit
  peptide, the FAD-binding fold and Glu426. On sequence grounds, an acyl-CoA dehydrogenase activity and
  mitochondrial targeting are expected if the product folds.
- The product lacks most of the C-terminal vestigial domain, one of the two ECSIT-contact elements, and
  the domain-swapped C-terminal helix that stabilises the active dimer. PMID:25721401 places the
  missense variants that impair complex I assembly but preserve catalytic activity in this 176-residue
  C-terminal domain. It also links the equivalent VLCAD domain to inner-membrane association.
  The MCIA/complex I assembly role of canonical ACAD9 therefore cannot be transferred to this product
  without new evidence. Dimer stability, and with it the catalytic activity, is also untested.
- PANTHER places A0A7P0T7Z1 in PTHR43884:SF9 with Q9H845 (UniProt PANTHER cross-reference). This is
  expected, because classification is driven by the shared 521-residue module.
