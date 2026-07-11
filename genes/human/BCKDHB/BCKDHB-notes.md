# BCKDHB (P21953) review notes

## Identity
- 2-oxoisovalerate dehydrogenase subunit beta, mitochondrial (ODBB_HUMAN); BCKDE1B / BCKDH E1-beta.
- EC 1.2.4.4. HGNC:987. NCBITaxon:9606.
- Precursor: transit peptide 1..50 (mitochondrial); mature chain 51..392.
- ComplexPortal CPX-2216 "Mitochondrial 2-oxoisovalerate dehydrogenase complex".

## Core biology (from UniProt P21953, verified quotes)
- FUNCTION: "Together with BCKDHA forms the heterotetrameric E1 subunit of the mitochondrial branched-chain
  alpha-ketoacid dehydrogenase (BCKD) complex. The BCKD complex catalyzes the multi-step oxidative
  decarboxylation of alpha-ketoacids derived from the branched-chain amino-acids valine, leucine and
  isoleucine producing CO2 and acyl-CoA..." "The E1 subunit catalyzes the first step with the
  decarboxylation of the alpha-ketoacid forming an enzyme-product intermediate. A reductive acylation
  mediated by the lipoylamide cofactor of E2 extracts the acyl group from the E1 active site..."
- SUBUNIT: "Heterotetramer of 2 alpha/BCKDHA and 2 beta chains/BCKDHB that forms the branched-chain
  alpha-keto acid decarboxylase (E1) component of the BCKD complex." Complex organized around E2
  (24-meric DBT core) + 6-12 E1 + ~6 E3 (DLD dimer).
- COFACTOR: thiamine diphosphate (ThDP/TPP). BINDING 152 = ThDP (shared with alpha). Multiple K+ structural
  binding sites (178,180,181,228,231,233).
- SUBCELLULAR LOCATION: Mitochondrion matrix.
- INTERACTION: P21953 - P12694 (BCKDHA), NbExp=15 (IntAct EBI-1029067/EBI-1029053). This is the direct
  E1 heterotetramer partner. All 5 IPI GO:0005515 rows have WITH/FROM UniProtKB:P12694 = BCKDHA.

## Catalysis (UniProt CATALYTIC ACTIVITY, RHEA)
- RHEA:13457 (EC 1.2.4.4): lipoyl-lysyl-[protein] + 3-methyl-2-oxobutanoate (= alpha-ketoisovalerate, KIV
  from valine) + H+ = S(8)-2-methylpropanoyldihydrolipoyl-lysyl-[protein] + CO2. Evidence PubMed:10745006, 9582350.
- RHEA:84639: with 4-methyl-2-oxopentanoate (KIC from leucine).
- RHEA:84643: with (S)-3-methyl-2-oxopentanoate (KMV from isoleucine).
- So E1 handles all three BCKAs (KIV, KIC, KMV) -> the three separate leucine/isoleucine/valine
  catabolic BP terms are all legitimate for BCKDHB.

## Key literature (all cached abstract-only unless noted)
- PMID:10745006 (Aevarsson 2000, Structure): crystal structure of human E1b, "the 170 kDa
  alpha(2)beta(2) heterotetrameric E1b component"; K+ ion sites; MSUD mutations explained. Full_text: false.
- PMID:9582350 (Wynn 1998, JBC): "The E1 decarboxylase component of the human branched-chain ketoacid
  dehydrogenase complex comprises two E1alpha (45.5 kDa) and two E1beta (37.5 kDa) subunits forming an
  alpha2 beta2 tetramer." Assembly of E1 in type IA MSUD. Full_text: false.
- PMID:3593587 (Ono 1987): Purification/characterization of human liver BCKADH complex; "The BCKADH
  effectively oxidized all of KIV, KIC, and KMV". Full_text: false.
- PMID:2022752 (Nobukuni 1991, JCI): Complete E1beta defect from 11-bp deletion in mito targeting leader
  peptide; "BCKDH activity in the proband ... approximately 6% of the normal control level"; "The absence
  of the E1 beta subunit results in instability of the E1 alpha subunit." IMP support for complex,
  process, mitochondrion. Full_text: abstract only.
- PMID:12902323 (Wynn 2003): His146-beta' essential catalytic residue in reductive acylation. His-alpha/beta
  active-site mechanism. (IPI to BCKDHA.)
- PMID:15166214 (Li 2004): ThDP binding / phosphorylation-loop cross-talk in E1b. (IPI to BCKDHA.)
- PMID:15576032 (Wynn 2004): Regulation of BCKDC by phosphorylation of Ser292-alpha; disorder of
  phosphorylation loop shuts off reductive acylation. (IPI to BCKDHA.)
- PMID:28514442 (Huttlin 2017 BioPlex/Nature) & PMID:33961781 (Huttlin 2021 Cell): large-scale
  interactome; IPI GO:0005515 with BCKDHA. Full text available.
- PMID:34800366 (Morgenstern 2021 Cell Metab): high-confidence human mito proteome (HTP), mitochondrion.

## Disease
- MSUD 1B (MIM:620698), autosomal recessive; E1-beta subunit deficiency (Type IB). BCAA (Leu/Ile/Val) and
  their BCKAs accumulate -> encephalopathy, neurodegeneration. (dismech Maple_Syrup_Urine_Disease.yaml.)

## Curation plan
- Core MF: GO:0003863 branched-chain 2-oxo acid dehydrogenase activity (contributes_to; heterotetrameric
  E1 catalytic activity — BCKDHB contributes to shared active site with BCKDHA). Label per GOA/UniProt.
- Core BP: GO:0009083 branched-chain amino acid catabolic process (directly_involved_in).
- Core CC: GO:0005759 mitochondrial matrix; in_complex GO:0160157 BCKDH complex.
- IEA/IBA process terms (Leu/Ile/Val catabolism, response to nutrient) accept as non-core/accept-broader.
- 5x protein binding IPI (all vs BCKDHA): MARK_AS_OVER_ANNOTATED per policy (bare protein binding,
  real but uninformative; the informative capture is the E1 heterotetramer complex + MF).
- protein-containing complex GO:0032991 IEA: MODIFY -> too general vs GO:0160157.
- Reactome/HPA/HTP location terms: accept.

## Deep research
- falcon deep research file polled; see final report for whether it landed within the 8-min window.
