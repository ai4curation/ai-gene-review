# SNRPGP15 (A8MWD9) bioinformatics: does the product exist, and is the SmG fold intact?

Reproduce: `uv run --with biopython --with requests python analyze.py > analysis_output.txt`.
All data are fetched live (UniProt, Ensembl REST, ENA, RCSB PDB 4PJO, EBI Proteins API);
raw output is in `analysis_output.txt`. Nothing below is hardcoded in the script.

## 1. Sequence relationship to SNRPG (P62308)

The UniProt A8MWD9 sequence is 76 aa, gap-free against SNRPG, 72/76 identical (94.7%).
Four substitutions: M13T, L17F, N55K, V61E (SNRPG numbering = SNRPGP15 numbering).

## 2. Reading frame at the locus

- Ensembl ENSG00000224543 is annotated `processed_pseudogene` (single exon,
  chr19:14489388-14489609, GRCh38, + strand); HGNC locus_type is `pseudogene`.
- Translating the GRCh38 locus gives MSKAHPPELK...MLEALE then `TGA` at codon 75
  (chr19:14489610-14489612) where SNRPG has Arg75: `MLEALE*V*`. The GRCh38 ORF therefore
  encodes 74 residues, not the 76-residue UniProt sequence; the Ensembl pseudogene model
  ends exactly at codon 74.
- The EMBL clone cited by UniProt (AC012318.7) also has `TGA` at codon 75, so the UniProt
  sequence (ending ...ERV) is not the translation of either genomic source.
- Ensembl variation: rs1249850259 (T/C at 14489610) would restore CGA (Arg); gnomAD exome
  allele frequency 2.06e-06, i.e. the stop is the near-universal allele.
- No frameshifts or other in-frame stops in codons 1-74.
- EST CK005235 (5' read, frontal cortex IMAGE clone, cited by UniProt) translates to
  MSKAHPP...EAKERV*, carrying all four SNRPGP15-specific substitutions plus three further
  differences (T50I, I68F, L73K) and Arg at 75. It is a single-pass read; whether it
  derives from this locus (with read errors) or from another SNRPG copy is unresolved.

## 3. Structural context (human minimal U1 snRNP, PDB 4PJO, 4.0 A cutoff, SmG chain G)

- SmG residues contacting U1 snRNA: K3, P36, F37, M38, N39, R63, G64, N65. All retained
  in SNRPGP15, as are the U127 pocket residues F34, N39 and R63 named in PMID:25555158.
- Residues contacting other protein chains in the particle: 44 positions; 42 are retained. The two changed are:
  - **M13T**: side chain contacts SmE Met14 (N-terminal helix packing against SmE).
  - **V61E**: in the β4 strand (Sm2 motif); side chain contacts SmE Pro17 and Leu20 at the
    SmG-SmE ring interface. Introduces a charged residue into a hydrophobic contact.
- L17F and N55K: no partner within 4 A.
- The C-terminal R75 and V76, both protein contacts in SNRPG, are absent from the
  GRCh38-encoded 74-residue ORF.

Interpretation: the Sm fold and the RNA-binding pocket residues are intact in sequence;
the substitutions fall at the SmE interface rather than at the RNA site. Whether V61E
abolishes heptamer incorporation is untested; it is a plausible but unproven defect.

## 4. Proteomics

- EBI Proteins API lists 16 observed peptides (PeptideAtlas, ProteomicsDB) mapped to A8MWD9.
  **All 16 are exact substrings of SNRPG**, and none spans one of the four
  SNRPGP15-specific residues. (One, IRGNSIIMLEALERV, carries an API `unique` flag, but its
  sequence is identical to SNRPG 62-76, so it does not discriminate.)
- The two in-silico tryptic peptides that would discriminate SNRPGP15 from SNRPG,
  GFDPFMNLVIDECVEMATSGQQK and NIGMVEIR, have not been observed, although the shared SNRPG
  peptide GNSIIMLEALER has more than 25,000 PeptideAtlas observations.
- Conclusion: no proteomic evidence for the SNRPGP15 product. The UniProt
  "Proteomics identification" keyword reflects shared SNRPG peptides.

## Overall

Processed pseudogene; reference-genome ORF truncated by a stop at codon 75; no
discriminating peptide; transcription evidence limited to one ambiguous EST. The protein
sequence is inside the SmG clade (recent retrocopy) and keeps the RNA-contact residues,
so the IBA node placement is phylogenetically correct, but there is no evidence that a
product exists to carry the inherited functions.
