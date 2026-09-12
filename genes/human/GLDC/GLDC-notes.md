# GLDC (P23378) — review notes

Glycine dehydrogenase (decarboxylating), mitochondrial / Glycine cleavage system P protein
/ Glycine decarboxylase. HGNC:4313. EC 1.4.4.2.

Deep research: falcon out of credits (HTTP 402); no `-deep-research-falcon.md`. Review grounded
in `GLDC-uniprot.txt`, seeded GOA, and cached `publications/PMID_*.md`.

## Core biology (verified)

- P-protein of the mitochondrial **glycine cleavage system (GCS)**: P=GLDC, H=GCSH, T=AMT/GCST,
  L=DLD. Catalyses the first, committed step of glycine catabolism.
- PLP-dependent (pyridoxal-5'-phosphate) enzyme; PLP is covalently bound as
  N6-(pyridoxal phosphate)lysine at Lys754 (FT MOD_RES 754; ISS from P15505).
  [file:human/GLDC/GLDC-uniprot.txt "N6-(pyridoxal phosphate)lysine"]
- Reaction: decarboxylates glycine (releases CO2) and transfers the residual aminomethyl
  moiety to the lipoyl (lipoamide) arm of the H-protein (GCSH).
  UniProt FUNCTION: [file:human/GLDC/GLDC-uniprot.txt "The P protein (GLDC) binds the alpha-amino group of glycine"]
  and "CO(2) is released"; "remaining methylamine moiety is then transferred to the lipoamide".
- Mechanism paper PMID:24467211 (Go et al 2014, Biochemistry, abstract only): GLDC is an
  "unusual PLP-containing alpha-amino acid decarboxylase" that removes CO2 without releasing free
  methylamine; "aminomethyl moiety is instead transferred to an accessory H-protein"; the GCS
  "couples the decarboxylation of glycine to the biosynthesis of serine". Also frames GLDC as a
  metabolic oncogene, but that is tumour context, not the core catalytic function.
- Homodimer; interacts with GCSH (By similarity). [file: "Homodimer (By similarity)"]
- Localisation: mitochondrion / mitochondrial matrix. UniProt SUBCELLULAR LOCATION: Mitochondrion
  (ECO:0000269|PubMed:28244183). Reactome places reaction in mitochondrial matrix. HPA IDA
  (GO_REF:0000052) and HTP mito-proteome (PMID:34800366) both localise to mitochondrion.
- Structure: PDB 6I33/6I34/6I35 (human, res 45-1020), PLP-dependent transferase fold.

## Disease

- Deficiency is the most common cause (~80%) of **nonketotic hyperglycinemia (NKH) / glycine
  encephalopathy** (MIM:605899): neonatal seizures, encephalopathy, raised CSF:plasma glycine.
  Many NKH missense variants lose glycine catabolic activity (PMID:28244183; PMID:1996985 Phe756del
  abolishes activity in COS7).

## Annotation-specific notes

- MF GO:0004375 glycine dehydrogenase (decarboxylating) activity — core; supported by EXP
  (PMID:1993704), IDA (PMID:28244183), TAS (PMID:1996985), IBA, IEA(EC 1.4.4.2 / RHEA:24304). ACCEPT.
- BP GO:0019464 glycine decarboxylation via glycine cleavage system — most specific catabolic
  process; core. ACCEPT (IBA and NAS).
- BP GO:0006546 glycine catabolic process — parent of the GCS decarboxylation; correct but less
  specific. ACCEPT (IDA/TAS/IEA); GO:0019464 is the preferred specific core term.
- GO:0009055 electron transfer activity (TAS, PMID:2268343) — this reference is a genomic-copy
  deletion paper (abstract does not describe electron transfer). GLDC is a PLP decarboxylase, NOT
  an electron carrier (the L-protein/DLD is the one with FAD/redox activity). Very likely a
  mis-mapping / over-annotation. It is a TAS (author statement), not experimental; the abstract
  gives no support. MARK_AS_OVER_ANNOTATED (do not REMOVE a non-IEA cited annotation outright; but
  flag strongly — arguably wrong branch). Considered: the "aminomethyl-transferring" alt name and
  the oxidoreductase KW do not imply electron transfer activity in the GO sense.
- GO:0005960 glycine cleavage complex (NAS, ComplexPortal PMID:28244183) part_of — correct, GLDC is
  a subunit of GCS. ACCEPT.
- GO:0042803 protein homodimerization activity (ISS from P15505) — supported by UniProt SUBUNIT
  Homodimer. ACCEPT (KEEP; adapter/dimerization real). Kept as non-core supporting.
- GO:0070280 pyridoxal binding (ISS) — PLP cofactor binding; real. Prefer GO:0030170 pyridoxal
  phosphate binding (the actual cofactor is PLP, covalently bound as Schiff base at Lys754).
  MODIFY -> GO:0030170. (UniProt DR itself carries GO:0030170 IBA.)
- GO:0036255 response to methylamine (ISS from P15505) — from rat activity-regulation (inhibited by
  methylamine). Peripheral regulatory response, not core. KEEP_AS_NON_CORE.
- GO:1903442 response to lipoic acid (ISS from P15505) — from rat activity-regulation (stimulated by
  lipoic acid). Peripheral, not core. KEEP_AS_NON_CORE.
- GO:0006520 amino acid metabolic process (IEA InterPro) — correct but very general parent. ACCEPT
  (broad IEA); GO:0019464 is the informative term.
- GO:0006544 glycine metabolic process (IEA InterPro) — correct broad parent. ACCEPT.
- GO:0016829 lyase activity (IEA InterPro, IPR001597) — GLDC is classified EC 1.4.4.2 oxidoreductase,
  not a lyase; IPR001597 (ArAA beta-elim lyase / Thr aldolase) is a broad PLP-fold signature. The
  lyase MF is a wrong-branch electronic mapping for this enzyme (its MF is glycine dehydrogenase
  (decarboxylating), an oxidoreductase). REMOVE (clearly wrong IEA inference — permitted).
- Mitochondrion/mitochondrial matrix (multiple IBA/IEA/IDA/HTP/TAS) — all correct. ACCEPT.
- GO:0004375 IEA (GO_REF:0000120, EC/RHEA) — correct electronic MF. ACCEPT.

## core_functions
- MF GO:0004375 glycine dehydrogenase (decarboxylating) activity (with GO:0030170 PLP binding as
  supporting MF).
- BP directly_involved_in GO:0019464 glycine decarboxylation via glycine cleavage system.
- CC located_in GO:0005759 mitochondrial matrix.
