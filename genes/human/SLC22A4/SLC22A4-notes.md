# SLC22A4 (OCTN1 / ETT) — curation notes

UniProt: Q9H015 (S22A4_HUMAN); HGNC:10968; 551 aa; MANE NM_003059.3 / NP_003050.2.
Family: SLC22 / major facilitator superfamily organic cation transporter (TC 2.A.1.19), PANTHER PTHR24064. 12 predicted TM helices (UniProt FT, 12 TMs; the original 1997 report called 11).

## Summary of function

OCTN1 is a polyspecific, pH-sensitive plasma-membrane solute carrier whose
**physiologically defining, highest-affinity substrate is ergothioneine (ERGO)**, a
diet-derived sulfur-containing betaine antioxidant. It is a **mixed-mechanism
transporter**: it moves different substrates by different mechanisms (Na+-coupled
symport for ergothioneine/carnitine/glycine betaine; Na+-independent, pH-dependent
antiport/facilitated transport for the prototypical organic cation
tetraethylammonium (TEA) and other xenobiotic cations; bidirectional, principally
efflux transport of acetylcholine). So one cannot simply assert "organic cation
facilitated transport" for all substrates.

### Ergothioneine (defining function)
- Named the "ergothioneine transporter" (ETT/ETTh) by Gründemann et al.
  [PMID:15795384 "Discovery of the ergothioneine transporter"]. UniProt records
  ergothioneine as the high-affinity substrate: [Q9H015 UniProt CC:FUNCTION
  "Na(+)-dependent and pH-dependent high affinity microbial symporter of"
  "potent food-derived antioxidant ergothioeine" (sic)]. KM = 21 µM
  [Q9H015 CC:BIOPHYSICOCHEMICAL PROPERTIES "KM=21 uM for ergothioneine (at pH 7.4)"].
- Catalytic reaction is Na+-coupled: [Q9H015 CC:CATALYTIC ACTIVITY
  "Reaction=ergothioneine(out) + Na(+)(out) = ergothioneine(in) +" ... RHEA:75843;
  CHEBI:134344 ergothioneine].
- Physiological role: apical absorption of ERGO in small intestine and kidney and
  uptake into non-parenchymal liver cells; octn1(-/-) mice fail to absorb oral
  [3H]ERGO [PMID:20601551 "OCTN1 is responsible for small intestinal absorption of
  [(3)H]ERGO"; "OCTN1 is localized on the apical surface of small intestine in mice
  and humans"]. ERGO is linked to control of inflammation and oxidative stress.
- GO now has a specific MF term **GO:0170001 ergothioneine transmembrane
  transporter activity** (verified non-obsolete via QuickGO; no existing
  annotations yet). This is used as the primary core MF. Ergothioneine is also an
  amino-acid betaine, so the broad GOA rows GO:0015199 (amino-acid betaine
  transmembrane transporter activity) correctly but less specifically cover it.

### Acetylcholine (secondary physiological function)
- OCTN1 catalyses bidirectional ACh transport, **principally export**, implicating
  it in the non-neuronal cholinergic system [PMID:22569296 "physiological
  acetylcholine is principally exported by the" transporter; "Acetylcholine
  transport catalyzed by hOCTN1 revealed an asymmetric" regulation by Na+].
  KM ~0.8–1 mM (low affinity). UniProt: [Q9H015 CC:FUNCTION "acetycholine,
  although the exact transport mechanism has not been fully" identified]. This is
  bidirectional, not strictly Na+-coupled; transport is inhibited by external Na+.
  Term GO:0005277 acetylcholine transmembrane transporter activity.

### Organic cation / xenobiotic (TEA, drugs)
- Prototype: TEA, transported Na+-independently and pH-dependently (antiport)
  [PMID:9426230 "OCTN1 exhibited saturable and pH-dependent" [3H]TEA uptake;
  "active secretion of cationic compounds across the" renal brush border].
  UniProt MISCELLANEOUS: [Q9H015 "bidirectional transport of exogenous prototype
  organic cation" tetraethylammonium (TEA)]. Broad drug list (verapamil,
  quinidine, cimetidine, gabapentin, etc.; DrugBank cross-refs). Captured by
  GO:0015651 quaternary ammonium group transmembrane transporter activity /
  GO:0015697 quaternary ammonium group transport. The obsolete generic term
  GO:0015101 "organic cation transmembrane transporter activity" (QuickGO:
  obsolete) must NOT be used.

### Carnitine (genuine but secondary / low-affinity)
- OCTN2/SLC22A5 is the dedicated high-affinity, Na+-dependent carnitine
  transporter; OCTN1 transports L-carnitine with **low affinity** (KM ~422–1324 µM)
  [PMID:16729965 "demonstrated a K(m) of 422 microM"]. UniProt: [Q9H015 CC:FUNCTION
  "transporter of L-carnitine through the mitochondrial membrane, thereby"
  maintaining intracellular carnitine homeostasis]. Treated as KEEP_AS_NON_CORE
  (real secondary activity; a dedicated carnitine transporter exists).

### Glycine betaine / zwitterions
- OCTN1 transports glycine betaine (RHEA:72115) and a range of zwitterions; the
  SLC22A15 deorphaning study used OCTN1 as the known ergothioneine transporter
  comparator [PMID:33124720 "including ergothioneine, carnitine, carnosine,
  gabapentin"; "SLC22A15 transport of several substrates was sodium-dependent and";
  "higher Km for ergothioneine, carnitine, and carnosine compared to" previously
  identified transporters]. Covered by GO:0015199 (amino-acid betaine).

## Localization
- **Primary: plasma membrane** — apical in intestinal/renal epithelia
  [PMID:20601551; Q9H015 CC:SUBCELLULAR LOCATION "Localized to the apical membrane
  of small" intestines], basal in Sertoli cells of the blood–testis barrier
  [PMID:35307651 "OCTN) 1 primarily localized to the basal membrane of SCs";
  Q9H015 "Localized to the basal membrane of" Sertoli cells].
- **Mitochondrion (debated, secondary)** — Lamhonwah & Tein reported GFP/RFP-hOCTN1
  mitochondrial localization and L-carnitine uptake by isolated mitochondria
  [PMID:16729965 "report novel localization of the organic cation/carnitine
  transporter, OCTN1, to" mitochondria]; also HPA immunofluorescence (GO_REF:0000052)
  and a high-confidence mitochondrial proteome (PMID:34800366). Evidence partly
  rests on overexpressed fusion constructs; the field regards OCTN1 as primarily a
  plasma-membrane transporter. Mitochondrion / mitochondrial membrane rows are kept
  as KEEP_AS_NON_CORE (real but peripheral; outer-membrane specificity rests on a
  Reactome model).

## Genetics / disease (association, not a molecular function)
- SLC22A4 variants (notably the 1672C>T / slc2F2 haplotype and L503F) and an
  intronic RUNX1-site SNP are **risk/susceptibility** associations for rheumatoid
  arthritis (RA) [PMID:14608356] and Crohn disease / IBD5 locus [PMID:15107849].
  L503F reduces ACh and carnitine transport [UniProt VARIANT 503]. G462E abolishes
  TEA transport [UniProt VARIANT 462]. These are genetic risk associations, not
  processes OCTN1 performs; RA/IBD are not annotated as OCTN1 functions here.

## Activity regulation
- Allosterically activated by intracellular ATP [Q9H015 CC:ACTIVITY REGULATION
  "Allosterically activated by intracellular ATP."]; UniProt has an ATP BINDING
  feature (218–225) and Walker-type nucleotide-binding motif, so the GO:0005524
  ATP binding row is supported (not merely InterPro IEA).

## Interactions
- Interacts with the PDZ scaffold PDZK1 (and NHERF2), which targets apical
  transporters to the brush border [Q9H015 CC:SUBUNIT "Interacts with PDZK1.";
  PMID:15523054 "specific interaction of apical transporters OCTN1" and OCTN2 with
  PDZK1]. Captured by GO:0030165 PDZ domain binding. Bare GO:0005515 protein
  binding rows are removed per the protein-binding policy (informative content is
  in GO:0030165).

## Points of caution / source issues
- **Nucleoside transport retracted/disputed**: an earlier report of OCTN1-mediated
  nucleoside (cytarabine, 2'-deoxycytidine) transport was not reproducible
  [Q9H015 CC:CAUTION "another study was unable to verify these" findings;
  PMID:28209616, PMID:29530864]. Not annotated.
- **PMID:10966938 mis-citation**: Reactome's GO:0015199 (amino-acid betaine) EXP
  annotation on SLC22A4 cites PMID:10966938, which is the characterization of the
  **paralog hOCTN2/SLC22A5** (Wagner et al., Na+-carnitine cotransporter); the
  betaine/ergothioneine term is nonetheless correct for OCTN1. Recorded as a
  source_defect (mis-keyed reference, resource Reactome) and reference_review
  MISCITED.
- Several BP rows transferred electronically from the rat ortholog (Q9R141) are
  indirect physiology/expression responses (lactation, liver regeneration, response
  to LPS/dsRNA/vitamin D, sodium-independent organic *anion* transport) — these are
  marked MARK_AS_OVER_ANNOTATED (not functions OCTN1 performs; the organic-anion
  one also conflicts with OCTN1's cation/zwitterion selectivity).

## Core function decision
1. GO:0170001 ergothioneine transmembrane transporter activity (primary; plasma
   membrane, apical). Proposed as a NEW specific annotation (real GO term).
2. GO:0005277 acetylcholine transmembrane transporter activity (secondary; non-
   neuronal cholinergic export).
3. GO:0015651 quaternary ammonium group transmembrane transporter activity
   (organic cation / xenobiotic handling; TEA, drugs).
Carnitine transport (GO:0015226) is kept as non-core.
