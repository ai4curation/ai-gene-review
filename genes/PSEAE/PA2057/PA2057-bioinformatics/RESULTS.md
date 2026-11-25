# PA2057 upstream reading-frame analysis

Script: `upstream_frame.py` (run `python upstream_frame.py`; needs NCBI E-utilities and UniProt REST).
Raw output: `results_output.txt`.

## Question

The UniProt/EMBL model of PA2057 (Q9I258, AAG05445.1, NP_250747.1, NC_002516.2:2251275..2253815, + strand,
846 aa) has no predicted signal peptide, which an outer-membrane TonB-dependent receptor needs. Its
UniRef90 cluster (UniRef90_Q9I258, 336 members) is dominated by 985-aa P. aeruginosa sequences (98 members),
for example UniParc UPI000EB53B2E. Is the PAO1 start site wrong?

## Method

Fetch 600 nt upstream of the annotated start plus the first 20 codons from NC_002516.2, translate in the
PA2057 frame, find the last upstream stop codon, and compare the open extension with the N-terminus of
UPI000EB53B2E that precedes the annotated start motif.

## Results

- The annotated start codon translates as V in the motif VVTGSRIPRA (an internal GTG).
- In the PAO1 genome the PA2057 reading frame continues 185 codons upstream of the annotated start without
  a stop. The ATG that aligns with the start of the longer orthologous models (the second in-frame ATG; a first one lies 26 codons further upstream) gives the extension MPHHAPSTRLPSSLALAALLAAAYAAPPEARAE..., a
  139-residue N-terminus that starts with a hydrophobic signal-peptide-like segment.
- That extension is 137/139 identical to the 139 residues preceding the annotated start motif in
  UPI000EB53B2E (985 aa).

## Conclusion

the PAO1 genome continues the PA2057 reading frame 185 codons upstream of the annotated start without a stop,
and the 139-residue extension from the ATG aligned with the orthologous start matches the longer orthologous models. The PAO1 gene model
starts too late. The full-length protein is about 985 residues with a signal peptide. Which start codon is
used in vivo has not been shown experimentally.
