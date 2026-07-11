# GNS (N-acetylglucosamine-6-sulfatase) — review notes

UniProtKB: P15586 (GNS_HUMAN). HGNC:4422. Gene on chromosome 12. EC=3.1.6.14.
552 aa precursor; signal peptide 1-36; mature chain 37-552.

## Core biology (verified)

- **Molecular function.** Lysosomal exo-sulfatase that **hydrolytically removes the
  6-O-sulfate group from terminal N-acetyl-D-glucosamine-6-sulfate (GlcNAc-6-S) residues**
  of heparan sulfate and keratan sulfate. UniProt FUNCTION: "Hydrolyzes 6-sulfate groups
  in N-acetyl-d-glucosaminide units of heparin sulfate and keratan sulfate"
  [file:human/GNS/GNS-uniprot.txt]. EC 3.1.6.14, catalytic activity established
  [PMID:1463457]. GO:0008449 N-acetylglucosamine-6-sulfatase activity is the exact,
  current MF term carried by GOA (EXP/IDA/IBA/IEA/TAS) and its GO definition matches this
  reaction verbatim.
- **Catalytic mechanism / PTM.** Sulfatase-family member; requires the C-alpha-formylglycine
  (3-oxoalanine, "FGly") residue generated from the active-site cysteine (Cys91 in the
  precursor numbering) by SUMF1 (formylglycine-generating enzyme). UniProt: "The conversion
  to 3-oxoalanine ... is critical for catalytic activity" [file:human/GNS/GNS-uniprot.txt].
  Binds 1 Ca2+ per subunit. SUMF1/SUMF2 regulate GNS activity [PMID:15962010].
- **Catalytic properties.** Human liver enzyme is a highly specific **exo-enzyme** for
  glucosamine-6-sulfate / glucose-6-sulfate residues; forms A and B desulfate keratan-
  sulfate- and heparin-derived substrates; no activity toward internal sulfate ester bonds
  [PMID:3689315, "Both forms A and B are exo-enzymes, since activity towards internal
  sulphate ester bonds was not observed."].
- **Biological process.** Acts in the stepwise exolytic lysosomal **catabolism of heparan
  sulfate and keratan sulfate** (glycosaminoglycan catabolism). PMID:1463457:
  "Glucosamine-6-sulphatase is an exo-hydrolase required for the lysosomal degradation of
  heparan sulphate and keratan sulphate."
- **Localization.** Lysosome / lysosomal lumen (UniProt SUBCELLULAR LOCATION: Lysosome).
  Also detected biochemically in neutrophil primary (azurophil) granules [PMID:15595925]
  and in secreted/exosome fractions (large-scale proteomics) [PMID:23533145] — these are
  secondary/context locations, not the core catabolic compartment.

## Disease

Deficiency causes **mucopolysaccharidosis type IIID (MPS IIID; Sanfilippo syndrome D;
MIM 252940)**, an autosomal-recessive lysosomal storage disorder with heparan-sulfate
accumulation and progressive CNS degeneration [PMID:12573255; PMID:20232353;
file:human/GNS/GNS-uniprot.txt DISEASE].

## Annotation review decisions

- GO:0008449 (MF, N-acetylglucosamine-6-sulfatase activity) — CORE. All 5 lines (EXP
  PMID:1463457; IDA PMID:15595925; IBA; IEA GO_REF:0000120; TAS Reactome + PMID:3689315)
  ACCEPT.
- GO:0008484 (MF, sulfuric ester hydrolase activity, IDA PMID:15962010) — parent of the
  specific sulfatase activity; MODIFY -> GO:0008449 (paper tested GNS among sulphatases
  whose activity is FGly/SUMF1-dependent).
- GO:0005515 (MF, protein binding, IPI PMID:17474147, NCK1/SH3 peptide array) — bare
  "protein binding", high-throughput; MARK_AS_OVER_ANNOTATED.
- GO:0005539 glycosaminoglycan binding, GO:0043199 sulfate binding (IEA ortholog) —
  substrate-related binding inherent to catalysis; KEEP_AS_NON_CORE (not separately
  informative beyond the enzyme activity).
- GO:0030200 heparan sulfate proteoglycan catabolic process (IBA + IDA + IEA) — CORE BP,
  ACCEPT. GO:0006027 glycosaminoglycan catabolic process (TAS) ACCEPT (parent-level, valid).
  GO:0042340 keratan sulfate proteoglycan catabolic process (IEA) ACCEPT (UniProt/EC name
  both substrates). GO:0030203 glycosaminoglycan metabolic process (IEA InterPro) — broad
  metabolic parent; KEEP_AS_NON_CORE.
- CC lysosome (IBA is_active_in, IEA) + lysosomal lumen (TAS) — CORE, ACCEPT.
- CC azurophil granule / azurophil granule lumen / ficolin-1-rich granule lumen /
  extracellular region / extracellular exosome — secondary neutrophil-granule/secreted
  locations; KEEP_AS_NON_CORE.

## Core MF term used in core_functions
GO:0008449 "N-acetylglucosamine-6-sulfatase activity" (exact current GOA term).
