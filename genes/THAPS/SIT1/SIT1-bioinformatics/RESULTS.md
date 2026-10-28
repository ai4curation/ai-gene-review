# SIT1 / SIT2 gene-model comparison (Thalassiosira pseudonana)

Script: `compare_models.py` (fetches sequences live from the UniProt REST API; raw output in
`RESULTS-output.txt`). Run with `python3 -I compare_models.py > RESULTS-output.txt`.

## Question

The UniProtKB reference-proteome entries B8C2V9 (SIT1, 464 aa, from genome gene model EED92452)
and B5YNJ0 (SIT2, 475 aa, from ACI64637) are shorter than the TpSIT1/TpSIT2 proteins cloned and
studied by the Hildebrand laboratory (GenBank ABB81825, 517 aa, and ABB81826, 528 aa; UniProtKB
Q0QVM8 and Q0QVM7). Are the gene-model entries the same proteins, and what do they lack?

## Results

- B8C2V9 is an exact C-terminal suffix of Q0QVM8: True. N-terminal residues absent from B8C2V9: 53
  (`MSTAEIQSGADTAPVKHDDHADSHDVKLTPFNILRYIGSIGLLIFSIIIVGAL`).
- B5YNJ0 is an exact C-terminal suffix of Q0QVM7: True. N-terminal residues absent from B5YNJ0: 53
  (`MSSAEVDSTPTTTPVKHDDHADSHDVKLTPFNVLRYIGSIGLLIFSIIIVAAL`).
- Both gene models start at an internal methionine (`MFTGNTRVAKDA...`, residue 54 of the cDNA
  entries).
- The absent segment contains a strongly hydrophobic stretch (Kyte-Doolittle 19-residue window
  maximum 2.17 for SIT1 and 2.27 for SIT2, starting at residue 33), i.e. a probable N-terminal
  transmembrane helix that the gene-model entries lack. Phobius on B8C2V9/B5YNJ0 predicts only
  8 transmembrane segments.
- The anti-TpEL4 antigen peptide `PANERGTSFFGRKTC`, described as residues 318-332 of TpSIT1 in
  PMID:17172435, is at residues 318-332 of Q0QVM8 and residues 265-279 of B8C2V9, confirming that
  the published TpSIT1 numbering is on the 517-residue sequence.
- The translated N-terminal cloning primers of PMID:17172435 (`MSTAEIQ` for TpSIT1, `MSSAEV` for
  TpSIT2) match the start of Q0QVM8/Q0QVM7 but not B8C2V9/B5YNJ0; the C-terminal primers
  (`DALAEDA`, `EAVDAQA`) match the ends of all four entries.

## Interpretation

B8C2V9 and B5YNJ0 are the same genes as TpSIT1 and TpSIT2 (identity of the shared 464/475 residues
is exact), but their sequences derive from genome gene models with a downstream start codon and
lack the first 53 residues, including a probable transmembrane helix, present in the cDNA-derived
proteins that were expressed, tagged and knocked down experimentally. Residue numbers from the
literature must be shifted by 53 to map onto B8C2V9/B5YNJ0. This does not affect the GO
annotations reviewed here, which concern transport function and location rather than the
N-terminus.

Limitations: this is a sequence comparison only. Whether the genome-model start or the cDNA start
is used in vivo was not tested here; the experimental papers cloned and expressed the longer
cDNA-defined open reading frames.
