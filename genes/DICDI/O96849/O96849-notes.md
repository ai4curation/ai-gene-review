# O96849 (DIRS-1 ORF2, RT-RNase H) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

### Identity

- UniProt O96849 (TrEMBL, PE 4, 608 aa, no gene name; AmoebaDB DDB_G0267206 / DDB_G0267304).
  Q23898 is a second cloned copy (EMBL AAA70202, same length, 9 differences, none at
  catalytic positions: `O96849-bioinformatics/RESULTS.md`).
- Encoded by the Dictyostelium DIRS-1 retrotransposon, the founding member of the DIRS
  (tyrosine recombinase, YR) retroelement order. DIRS-1 is the most abundant D. discoideum
  retrotransposon (~40 intact and 200-300 fragmented copies), clustered at centromeres
  [PMID:32170321].
- ORF numbering differs between papers. Cappello et al. 1985 call the RT-bearing ORF
  "ORF3" [PMID:2416457 "The conserved reading frame (ORF3) contains a 200 amino acid region
  that bears significant homology to retrovirus reverse transcriptase"]; Hammann/Winckler
  papers call it ORF2 (RT, RH, MT) with the YR in ORF3 [PMID:29051748 "ORF2 overlaps with ORF3
  and encodes RT, RH and methyl transferase (MT) domains, while ORF3 contains the YR"], or
  ORF III [PMID:24369430]. The protein is the same: RT + RNase H + C-terminal MT-like region.

### Domains and family (UniProt/InterPro, checked with HMMER)

- RT (PF00078, 51-215; CDD cd03714 RT_DIRS1). Catalytic Asp D99, D165, D166 (YLDD) retained.
- RNase H (PF17917 323-403; CDD cd09275 RNase_HI_RT_DIRS1 327-449). Acidic cluster D331,
  E334, E368, D393 (D443 tentative) retained.
- C-terminal region 455-561 matches Pfam PF05869 (phage Dam N6-adenine MTase) at E=7.8e-15,
  but motif IV (NPPY in reviewed phage Dam enzymes P51715, Q38156) is FPPP (519-522) here:
  both the catalytic Asn and the base-stacking Tyr are lost. Degenerate MTase-like domain;
  catalytic activity doubtful. Literature calls it "a methylase with unknown function"
  [PMID:32170321].
- PANTHER PTHR33050:SF7 (family PTHR33050 "reverse transcriptase domain-containing protein";
  subfamily includes hepadnavirus P proteins and other DIRS RT-RNase H proteins). No
  PAINT/IBA node available for this subfamily, so no IBA annotations exist.
- No YR domain in this protein: integration is done by the separately encoded YR (O96848 /
  Q23897, "Core-binding (CB) domain-containing protein", 1007 aa).

### What is experimentally established (element-level only)

PMID:32170321 (full text) used genetically tagged DIRS-1 reporter elements:
- DIRS-1 retrotransposition is detectable only in rrpC- and agnA- RNAi mutants.
- The ICR is essential for complete retrotransposition.
- The extrachromosomal cDNA is single-stranded, mostly linear, and is a genuine intermediate.
- A truncated reporter lacking most of the RT-RNase H coding region still produced cDNA in
  rrpC- cells, "suggested that the DIRS-1 encoded reverse transcriptase ... can act in trans".
  So RT function is inferred from trans-complementation by endogenous copies; the protein
  itself was never expressed, purified, mutated individually or assayed.
- No biochemical RT, RNase H or MTase assay exists for this protein.

Therefore: RNA-directed DNA polymerase activity and RNase H activity are domain-based
(intact catalytic residues) plus consistent with element genetics; participation in
retrotransposition is a curator inference from that activity plus element-level genetics.
DNA-directed DNA polymerase activity (second-strand synthesis) is plausible for RT-RNase H
proteins but unexplored; the DIRS-1 cDNA intermediate detected is single-stranded and the
enzyme for conversion to dsDNA is not identified.

### Annotation decisions (summary)

- ACCEPT: GO:0003964 RNA-directed DNA polymerase activity; GO:0006278 RNA-templated DNA biosynthetic process.
- MODIFY: transferase activity, nucleotidyltransferase activity -> GO:0003964; DNA biosynthetic
  process -> GO:0006278; nucleic acid binding (from RNase H superfamily) -> GO:0004523.
- KEEP_AS_NON_CORE: GO:0003887 DNA-directed DNA polymerase activity (plausible, untested).
- MARK_AS_OVER_ANNOTATED: GO:0009007 adenine-specific DNA MTase (degenerate motif IV);
  GO:0003677 DNA binding (rests on the degenerate MTase domain).
- REMOVE: GO:0009307 DNA restriction-modification system (prokaryotic defence system; no basis
  in a eukaryotic retroelement protein).
- NEW: GO:0004523 RNA-DNA hybrid ribonuclease activity (ISM); GO:0032197 retrotransposition (IC).
- Not proposed: DNA integration / DNA recombination (YR function, separate protein),
  transposon silencing (that is done to the element by RrpC/AgnA, not by this protein).

### Deep research

`just deep-research-falcon DICDI O96849 --fallback perplexity-lite` failed on 2026-10-21:
falcon "Failed to authenticate"; perplexity fallback HTTP 401 insufficient_quota. No
deep-research file was produced; review based on cached literature (PMID:32170321,
29051748, 24369430, 2416457, 6095047, 6096693, 25352599) and the HMMER analysis.
