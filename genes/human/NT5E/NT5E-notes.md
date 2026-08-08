# NT5E (ecto-5'-nucleotidase / CD73) — review notes

UniProt: P21589 (5NTD_HUMAN). HGNC:8021. 574 aa precursor; mature chain 27–549;
signal peptide 1–26; C-terminal propeptide 550–574 removed and replaced by GPI anchor.

## Identity and core function

- Ecto-5'-nucleotidase, EC 3.1.3.5 (plus 3.1.3.35, 3.1.3.89, 3.1.3.91, 3.1.3.99);
  CD antigen CD73; also called 5'-NT, IMP-specific 5'-nucleotidase, thymidylate
  5'-phosphatase [file:human/NT5E/NT5E-uniprot.txt DE lines].
- FUNCTION: "Catalyzes the hydrolysis of nucleotide monophosphates, releasing
  inorganic phosphate and the corresponding nucleoside, with AMP being the preferred
  substrate" [file:human/NT5E/NT5E-uniprot.txt FUNCTION]. Prefers ribonucleotide
  monophosphates over deoxyribose forms; other substrates: IMP, UMP, GMP, CMP, dAMP,
  dCMP, dTMP, NAD and NMN.
- Human e5NT "catalyzes the hydrolysis of extracellular AMP to adenosine and
  represents the major control point for extracellular adenosine levels"
  [PMID:23142347 abstract]. "CD73 hydrolyses AMP and is the major control point for
  the levels of extracellular adenosine" [PMID:34403084 abstract].
- Cofactor: binuclear Zn(2+) site [file:human/NT5E/NT5E-uniprot.txt COFACTOR;
  BINDING residues 36/38/85/117/220/243]. Zinc-binding resolved in crystal
  structures [PMID:22997138, PMID:23142347, PMID:34403084].
- SUBUNIT: Homodimer [file:human/NT5E/NT5E-uniprot.txt SUBUNIT]; "The dimerization
  interface is formed by the C-terminal domains" [PMID:23142347 abstract].
- Activity regulation: inhibited by AMPCP (adenosine 5'-(alpha,beta-methylene)-
  diphosphate) [file:human/NT5E/NT5E-uniprot.txt ACTIVITY REGULATION]. ADP and ATP
  are competitive inhibitors [PMID:34403084 abstract].

## Localization

- SUBCELLULAR LOCATION: "Cell membrane ... Lipid-anchor, GPI-anchor"
  [file:human/NT5E/NT5E-uniprot.txt]. GPI-anchor amidated serine at position 549
  (LIPID feature). Primary evidence: "the glycophospholipid functioning as the
  membrane anchor of 5'-nucleotidase" [PMID:2129526 abstract].
- GPI-anchored ectoenzyme on the external side of the plasma membrane; UniProt GO
  cross-refs include GO:0009897 external side of plasma membrane (IEA:Ensembl) and
  GO:0009986 cell surface (HDA). Frequently recovered in extracellular exosome
  proteomics (secondary localization).

## Disease

- CALJA — calcification of joints and arteries (MIM:211800), adult-onset
  calcification of lower-extremity arteries and hand/foot joints
  [file:human/NT5E/NT5E-uniprot.txt DISEASE]. Caused by NT5E loss-of-function
  variants including C358Y [PMID:21288095 (St Hilaire 2011, not cached);
  PMID:24887587].
- Mechanism of disease mutants: "All 3 mutations resulted in absent NT5E enzymatic
  activity at the cell surface" and showed "significantly reduced trafficking to the
  plasma membrane" — a trafficking-opathy [PMID:24887587 abstract, full text in
  cache].

## Adhesion moonlighting function

- CD73 = L-VAP-2; "it also has a function in mediating lymphocyte adhesion to the
  endothelium"; a CD73 mAb could "partially inhibit the ecto-5'-nucleotidase
  activity of peripheral blood lymphocytes" [PMID:7595232 abstract/full text].

## Mineralization / purinergic signaling context

- In calcific aortic valve disease, "Expression of NPP1 and 5'-nucleotidase by VICs
  promotes the mineralization of the aortic valve through A2aR"; "mineralization
  induced by adenosine triphosphate was decreased by silencing NPP1 and
  5'-nucleotidase" [PMID:25644539 abstract]. Basis for GO:0031214 biomineral tissue
  development, GO:0033198 response to ATP, GO:0046034 ATP metabolic process IDAs
  (via MGI).

## Protein interactions

- IPI "protein binding" (GO:0005515) annotations from the human binary interactome
  map [PMID:32296183, Luck et al. 2020] to ZNRF4 (Q8WWF5) and RNF24 (Q9Y225-2), both
  listed in the UniProt INTERACTION block
  [file:human/NT5E/NT5E-uniprot.txt INTERACTION].

## Curation decisions (summary)

- Core MF (core_functions): GO:0008253 5'-nucleotidase activity (primary; with
  directly_involved_in GO:0006196 AMP catabolic process + GO:0046086 adenosine
  biosynthetic process); GO:0002953 5'-deoxynucleotidase activity; GO:0008270 zinc
  ion binding. Core locations: GO:0005886 plasma membrane, GO:0009897 external side
  of plasma membrane.
- ACCEPT: all experimental/curated 5'-nucleotidase activity, 5'-deoxynucleotidase
  activity, zinc ion binding, plasma membrane, cell surface annotations, plus the
  redundant IEA/IBA versions of the correct core terms.
- KEEP_AS_NON_CORE: leukocyte cell-cell adhesion (GO:0007159), identical protein
  binding / homodimer (GO:0042802), biomineral tissue development (GO:0031214),
  response to ATP (GO:0033198), nucleotide catabolic process (GO:0009166 generic
  parent), extracellular exosome (GO:0070062, secondary localization).
- MARK_AS_OVER_ANNOTATED: generic IEA parents (GO:0000166 nucleotide binding,
  GO:0016787 hydrolase activity, GO:0016788 hydrolase acting on ester bonds,
  GO:0046872 metal ion binding, GO:0016020 membrane) and bare protein binding
  (GO:0005515 IPI, per policy not removed). Also GO:0046034 ATP metabolic process:
  CD73 acts on AMP, not ATP directly, so the ATP metabolic-process IDA overstates
  substrate scope.
- No REMOVE actions: no clearly-wrong IEA identified; all experimental annotations
  retained.

## Ontology checks

- GO:0031225 "anchored component of membrane" is now OBSOLETE (checked via
  ols:go). Did NOT use it in core_functions; used GO:0005886 plasma membrane and
  GO:0009897 external side of plasma membrane instead (both non-obsolete and
  well-supported).
- Verified labels via oaklib ols:go adapter: GO:0008253 5'-nucleotidase activity,
  GO:0002953 5'-deoxynucleotidase activity, GO:0008270 zinc ion binding, GO:0046086
  adenosine biosynthetic process, GO:0006196 AMP catabolic process, GO:0009897
  external side of plasma membrane.
