# ACADS (human) review notes

UniProt: P16219 (ACADS_HUMAN). Short-chain specific acyl-CoA dehydrogenase, mitochondrial; SCAD; Butyryl-CoA dehydrogenase; EC 1.3.8.1. 412 aa precursor, mitochondrial transit peptide 1-24, mature chain 25-412. HGNC:90, gene on chr 12. NCBITaxon:9606.

## Core function

ACADS catalyzes the first, FAD-dependent step of mitochondrial fatty acid beta-oxidation for short-chain substrates: the alpha,beta-dehydrogenation of short-chain (C4-C6) acyl-CoA thioesters to the corresponding trans-2-enoyl-CoA, with electrons passed to electron-transfer flavoprotein (ETF). Optimum substrate butyryl-CoA (C4).

- UniProt FUNCTION: "Short-chain specific acyl-CoA dehydrogenase is one of the acyl-CoA dehydrogenases that catalyze the first step of mitochondrial fatty acid beta-oxidation... short-chain specific acyl-CoA dehydrogenase acts specifically on acyl-CoAs with saturated 4 to 6 carbons long primary chains (PubMed:11134486, PubMed:21237683)." [P16219 UniProt CC FUNCTION, ECO:0000269|PubMed:11134486, ECO:0000269|PubMed:21237683]
- EC 1.3.8.1 with ECO:0000269|PubMed:21237683. Catalytic activity entries (Rhea) for short-chain 2,3-saturated fatty acyl-CoA, butanoyl-CoA, pentanoyl-CoA, hexanoyl-CoA, all left-to-right.

[PMID:3597357 "Short chain acyl-CoA (SCA), medium chain acyl-CoA (MCA), and isovaleryl-CoA (IV) dehydrogenases were purified to homogeneity from human liver"] — original purification of human SCAD. Establishes homotetramer, FAD per subunit, ETF electron acceptor, butyryl-CoA -> crotonyl-CoA product.
[PMID:3597357 "The products of SCA dehydrogenase/butyryl-CoA, MCA dehydrogenase/octanoyl-CoA, and IV dehydrogenase/isovaleryl-CoA reactions were identified as crotonyl-CoA, 2-octenoyl-CoA, and 3-methylcrotonyl-CoA"] — direct evidence SCAD dehydrogenates butyryl-CoA to crotonyl-CoA.
[PMID:3597357 "indicating a homotetrameric structure"] and [PMID:3597357 "each contains 1 mol of FAD per subunit"] and [PMID:3597357 "They all utilized electron transfer flavoprotein (ETF) or phenazine methosulfate (PMS) as an electron acceptor"].

## Structure / cofactor / quaternary

- Homotetramer (UniProt SUBUNIT, ECO:0000269|Ref.10 = SGC crystal structure PDB 2VIG). Binds 1 FAD per subunit (UniProt COFACTOR Ref.10). FAD shared between dimeric partners. Active site proton acceptor Glu392 (ACT_SITE, by similarity to P15651).
- PDB structures: 2VIG (1.9 A, with FAD and substrate analog), 7Y0A, 7Y0B, 8SGS (EM).
- Belongs to acyl-CoA dehydrogenase family (InterPro IPR006089 etc.). CDD cd01158 SCAD_SBCAD.

## Localization

- Mitochondrion matrix (UniProt SUBCELLULAR LOCATION, ECO:0000250|UniProtKB:Q3ZBF6, soluble matrix protein). N-terminal mitochondrial transit peptide cleaved.
- GOA has mitochondrion (IDA MGI PMID:16729965; IDA HPA; HTP PMID:34800366), mitochondrial matrix (ISS, TAS Reactome), and a spurious nucleus (HDA PMID:21630459, sperm-nucleus proteomics — almost certainly contaminant; soluble matrix enzyme).
- Note: PMID:16729965 is the OCTN1-to-mitochondria paper (abstract is about OCTN1/SLC22A4, a carnitine transporter). The ACADS mitochondrion IDA from MGI cites this PMID; the curator (MGI) likely used ACADS as a mitochondrial marker/co-stain in that work — abstract-only here, so do not overrule; mitochondrial localization for ACADS is in any case strongly supported by all other evidence. Treat as ACCEPT (location is correct).
- PMID:34800366 (Morgenstern MitoCoP) high-confidence human mitochondrial proteome: [PMID:34800366 "We classified >8,000 proteins in mitochondrial preparations of human cells and defined a"] (abstract truncated at cache; mitochondrial classification). HTP mitochondrion = correct.
- Nucleus HDA from PMID:21630459 sperm nucleus proteome: [PMID:21630459 "403 different proteins have been identified from the isolated sperm nuclei. ... More than half (52.6%) of the proteins had not been detected in the previous human whole sperm cell proteome reports."] This is a large-scale dataset; ACADS as a mitochondrial matrix enzyme appearing in a sperm-nucleus prep is best explained as mitochondrial/cytoplasmic carryover. Mark over-annotated (HDA, no functional support for nuclear role).

## Disease

- Acyl-CoA dehydrogenase short-chain deficiency (ACADSD, MIM 201470): inborn error of mito FAO; acute acidosis and muscle weakness in infants, lipid-storage myopathy in adults; ethylmalonic aciduria. ECO:0000269|PubMed:11134486, PubMed:1692038, PubMed:9499414.
- Common susceptibility variants c.625G>A (R171W? actually 625G>A is a non-rare variant) and c.511C>T confer susceptibility to ethylmalonic aciduria. [PMID:11134486 "functional SCAD deficiency due to the presence of susceptibility SCAD gene variations, i.e. 625G>A and 511C>T"]
- PMID:11134486 characterized variants and the pathway: GOA uses it for IMP GO:0003995 (R171W has 69% WT activity, G209S 86%; several missense cause loss of acyl-CoA dehydrogenase activity per UniProt VARIANT notes, e.g. G90S, A192V, R325W, S353L, R380W "loss of acyl-CoA dehydrogenase activity"). And IC GO:0006635 fatty acid beta-oxidation (from MF GO:0003995).

## Annotation-by-annotation reasoning

MF terms:
- GO:0016937 short-chain fatty acyl-CoA dehydrogenase activity — CORE. Supported by EXP PMID:21237683 (EC characterization), ISS, IBA, IEA. This is the precise MF term. ACCEPT (EXP/IBA), the IEA/ISS duplicates ACCEPT/KEEP.
- GO:0003995 acyl-CoA dehydrogenase activity — parent term, correct but less specific than GO:0016937. IDA PMID:3597357 (purified human SCAD), IMP PMID:11134486, ISS, IEA, TAS PMID:2565344. ACCEPT the IDA/IMP (experimental, correct), the broad parent is fine but non-core given the more specific child.
- GO:0016627 oxidoreductase activity, acting on CH-CH group of donors — InterPro IEA, correct parent, KEEP_AS_NON_CORE (too general).
- GO:0050660 flavin adenine dinucleotide binding — IEA InterPro, correct (FAD cofactor, 1 per subunit). ACCEPT.
- GO:0070991 medium-chain fatty acyl-CoA dehydrogenase activity — IEA from RHEA:43464 (hexanoyl-CoA, C6). C6/hexanoyl is at the boundary; SCAD does act on C4-C6 (UniProt lists hexanoyl-CoA Rhea reaction with ECO:0000269|PubMed:21237683). Hexanoyl-CoA (C6) is conventionally "medium chain". This term is defensible as a minor/boundary activity but is not the core specificity (which is short-chain, optimum C4). KEEP_AS_NON_CORE — the C6 activity is real (UniProt catalytic activity hexanoyl-CoA, PubMed:21237683) but the enzyme is the short-chain ACAD; medium-chain is the boundary of its range, not its identity. Do not REMOVE (mechanically derived from a real UniProt-curated Rhea reaction).
- GO:0005515 protein binding (x2, IPI from BioPlex PMID:28514442 and PMID:33961781; WITH P16444 DPEP1) — high-throughput AP-MS interactome; DPEP1 is a membrane dipeptidase, not an obvious functional partner. Uninformative term; per guidelines do not endorse bare protein binding. MARK_AS_OVER_ANNOTATED (real HT interaction but uninformative; not core).

BP terms:
- GO:0006635 fatty acid beta-oxidation — IC PMID:11134486 and TAS PMID:8276399. CORE/ACCEPT. Mouse SCAD cloning paper (8276399) explicitly: [PMID:8276399 "Short-chain acyl-CoA dehydrogenase (SCAD) is one of five homologous dehydrogenases that catalyze the first reaction in the beta-oxidation of fatty acids."]
- GO:0033539 fatty acid beta-oxidation using acyl-CoA dehydrogenase — IBA + IEA. More specific BP capturing the ACAD-mediated step. ACCEPT (IBA).
- GO:0046359 butyrate catabolic process — IBA. ACADS optimum substrate is butyryl-CoA (C4). "Butyrate catabolic process" = breakdown of butyrate/butanoate. SCAD's dehydrogenation of butyryl-CoA is the committed step of butyryl-CoA/butanoyl-CoA catabolism. Defensible; KEEP_AS_NON_CORE (it is a substrate-specific framing of the same FAO step). ACCEPT/KEEP.

CC terms:
- GO:0005759 mitochondrial matrix — ISS (Q3ZBF6), TAS Reactome x2. CORE location. ACCEPT.
- GO:0005739 mitochondrion — IBA is_active_in, IEA, IDA HPA (GO_REF:0000052), IDA MGI PMID:16729965, HTP PMID:34800366. Correct but less specific than matrix. ACCEPT (parent of matrix).
- GO:0005634 nucleus — HDA PMID:21630459 (sperm nucleus proteome). MARK_AS_OVER_ANNOTATED (contaminant; matrix enzyme).

## References quality

- PMID:21237683 abstract foregrounds ACAD9/ACAD10/ACAD11 but UniProt cites it (ECO:0000269) for ACADS FUNCTION, catalytic activity and EC 1.3.8.1 — the full text characterized ACADS short-chain activity. Do NOT remove the EXP annotation. Abstract-only in cache (full_text_available: false).
- PMID:3597357 — purification of human liver SCAD/MCAD/IVD; directly supports SCAD enzymology. HIGH.
- PMID:11134486 — common ACADS variants, disease pathogenesis, function/catalytic activity/pathway. HIGH.
- PMID:2565344 — cDNA cloning of human SCAD; TAS GO:0003995. MEDIUM (sequence/identity, supports MF generically).
- PMID:8276399 — mouse SCAD cDNA; TAS GO:0006635. MEDIUM (ortholog; states SCAD catalyzes first beta-ox step).
- PMID:16729965 — OCTN1 mito paper; ACADS mito IDA by MGI. Abstract about OCTN1 (different gene); used as mito marker. LOW relevance to ACADS function, but location annotation is fine. full_text_unavailable.
- PMID:21630459 — sperm nucleus proteome; basis of nucleus HDA. LOW; likely contaminant.
- PMID:34800366 — MitoCoP; HTP mitochondrion. MEDIUM (confirms mito).
- PMID:28514442, PMID:33961781 — BioPlex interactome (protein binding, DPEP1). LOW; HT, uninformative term.

## Core functions to record

1. MF GO:0016937 short-chain fatty acyl-CoA dehydrogenase activity; directly_involved_in GO:0006635 fatty acid beta-oxidation (and GO:0033539); location GO:0005759 mitochondrial matrix. supported_by PMID:3597357, PMID:21237683/UniProt, PMID:11134486.
