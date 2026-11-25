# GALM (galactose mutarotase / aldose 1-epimerase) — review notes

UniProtKB: Q96C23; HGNC:24063; EC 5.1.3.3; 342 aa; PDB 1SNZ/1SO0.

## Core biology (verified from UniProt + cached pubs)

- GALM is the cytosolic **aldose 1-epimerase (mutarotase)** that catalyses the FIRST step of the
  **Leloir pathway** of galactose metabolism: interconversion of the β- and α-anomers of D-galactose,
  supplying the α-anomer that galactokinase (GALK1) requires.
  [UniProt FUNCTION: "Mutarotase that catalyzes the interconversion of beta-D-galactose and alpha-D-galactose during galactose metabolism (PubMed:12753898)... Involved in the maintenance of the equilibrium between the beta- and alpha-anomers of galactose, therefore ensuring a sufficient supply of the alpha-anomer for GALK1"]
- Leloir pathway enzymes: GALM, GALK1, GALT, GALE [UniProt FUNCTION, PMID:30451973].
- Also active on D-glucose (α-D-glucose ⇌ β-D-glucose) but prefers galactose over glucose
  [PMID:12753898 abstract: "the protein has aldose 1-epimerase activity and exhibits a preference for galactose over glucose"; UniProt KM=37 mM galactose vs 54 mM glucose; kcat 12000 vs 4900 s^-1].
- Catalytic residues: His-176 (proton donor / ACT_SITE), Glu-307 (proton acceptor / ACT_SITE), His-107.
  Mutagenesis: H176A -300x, E307A loss of activity, H107A -5x [UniProt FEATURES / PMID:12753898].
- **Monomer** (SUBUNIT: Monomer, PMID:12753898 + PMID:15026423). GOA carries a NOT protein
  homodimerization activity (GO:0042803) IDA — consistent with monomeric state; keep negated.
- Subcellular location: **Cytoplasm** (UniProt SL). Reactome places the reaction in **cytosol** (GO:0005829). Also detected in urinary exosomes by MS (GO:0070062, PMID:19056867) — MS-detected, non-core.

## Disease
- Biallelic GALM variants cause **Galactosemia type IV (GALAC4 / galactose mutarotase deficiency)**,
  MIM:618881, Orphanet:570422 — a form of galactosemia [PMID:30451973]. GALAC4 variants (82-342 del,
  R142, G267, 311-342 del) reduce protein stability/accumulation and epimerase activity [UniProt VARIANTs].
- Note: the dismech Galactosemia.yaml (classic/GALK/GALE subtypes) predates/omits the GALM (type IV) form;
  GALM deficiency is the fourth Leloir-pathway galactosemia.

## Annotation-review reasoning
- GO:0004034 aldose 1-epimerase activity — CORE MF; multiple EXP/IDA/IMP/IBA/TAS + IEA(RHEA/EC). ACCEPT all.
- GO:0033499 (galactose catabolic process via UDP-galactose, Leloir pathway) — core BP. IBA/TAS/IMP/IDA. ACCEPT.
  (Stub label "beta-D-galactose catabolic process..." matches GOA TSV; current ontology primary label
   is "galactose catabolic process via UDP-galactose, Leloir pathway" — keep GOA label to match best-practices check.)
- GO:0006012 galactose metabolic process — core BP (IDA PMID:12753898 + IEA UniPathway). ACCEPT.
- GO:0019318 hexose metabolic process, GO:0005975 carbohydrate metabolic process — true but general parents;
  KEEP_AS_NON_CORE (grouping terms).
- GO:0006006 glucose metabolic process — GALM mutarotates glucose (IDA PMID:12753898, IBA). Real but non-core
  (prefers galactose; glucose mutarotation is a side/secondary activity). KEEP_AS_NON_CORE.
- GO:0016853 isomerase activity (IEA/InterPro) — generic parent of aldose 1-epimerase; MODIFY -> GO:0004034.
- GO:0030246 carbohydrate binding (IEA/InterPro) — lectin-type binding term; GALM binds galactose only as a
  catalytic substrate, not as a lectin. Over-annotation from InterPro2GO. MARK_AS_OVER_ANNOTATED.
- GO:0005829 cytosol (TAS Reactome) — ACCEPT (core location).
- GO:0005737 cytoplasm (IEA SubCell) — ACCEPT (broader, consistent).
- GO:0070062 extracellular exosome (HDA PMID:19056867) — MS detection in urinary exosomes; KEEP_AS_NON_CORE.
- GO:0042803 protein homodimerization activity, negated=true (IDA PMID:12753898) — GALM is a monomer;
  the NOT annotation is correct. ACCEPT.

Cached pubs (PMID_12753898, PMID_30451973, PMID_19056867) are all abstract-only (full_text_available: false).
Do not REMOVE experimental annotations on the basis of abstract-only text.

## 2026-11-12 audit to COMPLETE

Several of the calls above were revised to follow the rule that a correct but general
term is MODIFY, not ACCEPT or KEEP_AS_NON_CORE. Descendancy was checked against the GO
sqlite ancestors: GO:0033499 is_a GO:0019388 / GO:0006012 / GO:0019318 / GO:0005975,
and GO:0005829 is part of GO:0005737.

- GO:0005975 carbohydrate metabolic process (IEA, IDA), GO:0019318 hexose metabolic
  process (IEA) and GO:0006012 galactose metabolic process (IEA, IDA): now MODIFY to
  GO:0033499 Leloir pathway. This matches the E. coli galE and galM reviews.
- GO:0005737 cytoplasm (IEA): now MODIFY to GO:0005829 cytosol, which the gene
  already carries through the Reactome TAS rows.
- core_functions: GO:0033499 label updated to the current "beta-D-galactose catabolic
  process via UDP-galactose, Leloir pathway". The redundant ancestor GO:0006012 was
  removed from directly_involved_in.
- Verbatim supported_by quotes were added to the rows that lacked them. The NOT
  homodimerization row is supported by the UniProt SUBUNIT line "Monomer"
  (PMID:12753898, PMID:15026423; the latter is not cached).
- glucose metabolic process (IBA, IDA) stays KEEP_AS_NON_CORE: a genuine secondary
  activity (kcat 4900 vs 12000 s-1 for galactose; PMID:12753898 via UniProt).
