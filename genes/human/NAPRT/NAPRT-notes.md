# NAPRT (human) review notes

UniProt: Q6XQN6 (PNCB_HUMAN), gene symbol NAPRT (synonyms FHIP, NAPRT1). 538 aa. Chromosome 8.

## Identity and core function

NAPRT is **nicotinate phosphoribosyltransferase** (NAPRTase). It is the first, committed
enzyme of the **Preiss–Handler pathway** of NAD+ biosynthesis from dietary nicotinic acid
(niacin/Na). It condenses nicotinate with 5-phospho-alpha-D-ribose 1-diphosphate (PRPP) to
form nicotinate mononucleotide (NaMN, = nicotinate beta-D-ribonucleotide), coupled to ATP
hydrolysis.

- UniProt FUNCTION: "Catalyzes the first step in the biosynthesis of NAD from nicotinic
  acid, the ATP-dependent synthesis of beta-nicotinate D-ribonucleotide from nicotinate and
  5-phospho-D-ribose 1-phosphate ... Helps prevent cellular oxidative stress via its role in
  NAD biosynthesis" [file:human/NAPRT/NAPRT-uniprot.txt].
- CATALYTIC ACTIVITY (Rhea:RHEA:36163, EC=6.3.4.21): 5-phospho-alpha-D-ribose 1-diphosphate +
  nicotinate + ATP + H2O = nicotinate beta-D-ribonucleotide + ADP + phosphate + diphosphate
  [file:human/NAPRT/NAPRT-uniprot.txt].
- PATHWAY: "Cofactor biosynthesis; NAD(+) biosynthesis; nicotinate D-ribonucleotide from
  nicotinate: step 1/1" [file:human/NAPRT/NAPRT-uniprot.txt]. UniPathway UPA00253, UER00457.
- SUBCELLULAR LOCATION: "Cytoplasm, cytosol" [file:human/NAPRT/NAPRT-uniprot.txt].
- SUBUNIT: "Homodimer" [file:human/NAPRT/NAPRT-uniprot.txt]. Confirmed by crystal structure
  (PDB 4YUB) [PMID:26042198].

Note on EC: UniProt/GO now assign EC **6.3.4.21** (a ligase, because the physiological
reaction is ATP-coupled). Older literature (PMID:21742010, PMID:26042198 abstracts) cite the
transferase number **EC 2.4.2.11**; both refer to the same enzyme. The ATP-independent
phosphoribosyltransfer is the base chemistry; ATP hydrolysis raises efficiency/affinity.

## Key experimental evidence

- **PMID:17604275** (Hara et al. 2007, JBC; abstract-only): first identification of human
  NAPRT; "identified NA phosphoribosyltransferase (NAPRT) in humans and provided direct
  evidence of tight link between NAPRT and the increase in cellular NAD levels"; NAPRT
  "mediated [(14)C]NAD synthesis from [(14)C]NA in human cells"; NA "almost doubled cellular
  NAD contents and decreased cytotoxicity by H(2)O(2). Both effects were reversed by knockdown
  of NAPRT expression ... NAPRT is essential for NA to increase cellular NAD levels and, thus,
  to prevent oxidative stress of the cells" [PMID:17604275]. Basis for IDA MF (GO:0004516),
  IDA cytosol, IMP NAD+ salvage biosynthesis (GO:0034355), and IMP response to oxidative
  stress (GO:0006979).
- **PMID:21742010** (Galassi et al. 2012, Biochimie; abstract-only): recombinant human NAPRT
  kinetic characterization; "Nicotinate phosphoribosyltransferase (NaPRT, EC 2.4.2.11)
  catalyzes the conversion of nicotinate (Na) to nicotinate mononucleotide, the first reaction
  of the Preiss-Handler pathway for the biosynthesis of NAD(+)"; site-directed mutagenesis of
  conserved residues (D19, Y21, H213, D288, R318, G379, etc.) validated their importance for
  activity [PMID:21742010]. Cofactor Mg2+/Mn2+ (highest with Mn2+); ATP shows dual
  stimulation/inhibition; Pi is an activator [file:human/NAPRT/NAPRT-uniprot.txt kinetics].
  Basis for EXP MF (GO:0004516).
- **PMID:26042198** (Marletta et al. 2015, FEBS Open Bio; full text available): crystal
  structure of human NaPRTase (PDB 4YUB, 2.9 Å); "the rate-limiting enzyme in the three-step
  Preiss-Handler pathway for the biosynthesis of NAD"; "catalyzes the conversion of nicotinic
  acid (Na) and 5-phosphoribosyl-1-pyrophosphate (PRPP) to nicotinic acid mononucleotide
  (NaMN) and pyrophosphate (PPi)"; "functions as a dimer with the active site located at the
  interface of the monomers"; type II phosphoribosyltransferase; lacks the FK866 tunnel of
  NAMPT [PMID:26042198]. Basis for EXP MF (GO:0004516).

## Localization annotations

- Cytosol is well supported: IDA (PMID:17604275), IDA (HPA GO_REF:0000052), IBA, IEA
  (SubCell), and Reactome TAS (R-HSA-197186). Core location = cytosol (GO:0005829).
- **Extracellular / granule / exosome** annotations are proteomics/pathway detections, not
  the site of catalytic function:
  - GO:0070062 extracellular exosome (HDA, PMID:23533145 prostatic-secretion exosomes;
    PMID:19056867 urinary exosomes) — high-throughput MS detection in exosome preps; keep as
    non-core.
  - GO:0005576 extracellular region + GO:0035578 azurophil granule lumen (TAS,
    Reactome:R-HSA-6798751 "Exocytosis of azurophil granule lumen proteins" / neutrophil
    degranulation) — NAPRT was detected in neutrophil granule proteomics and modeled in the
    degranulation pathway. This is a secondary/moonlighting localization, not the cytosolic
    NAD-synthesis function. Keep as non-core.
  These are consistent with NAPRT being a soluble cytosolic protein that is incidentally
  captured in secretory/vesicular proteomes; they do not indicate an extracellular catalytic
  role.

## Protein binding (GO:0005515, IPI, PMID:25416956)

Six IPI "protein binding" annotations from the Rolland et al. 2014 human interactome (Y2H)
map and IntAct (GRAMD2B/Q96HH9, RBPMS/Q93062, CCDC57/Q2TAC2, EHMT2/A2ABF9, KRT40/Q6A162).
These are bare "protein binding" with no specific downstream function established; not core.
Per policy, bare protein-binding IPI is not removed — mark as over-annotated (uninformative).
UniProt also lists an INTERACTION block with these partners [file:human/NAPRT/NAPRT-uniprot.txt].
The synonym "FHIP" (FHA-HIT-interacting protein) reflects a reported HIT-family interaction
(Ref.2, GenBank submission), but no specific functional MF term is warranted.

## Metal binding

GO:0046872 metal ion binding (IEA UniProtKB-KW) reflects the Mg2+/Mn2+ cofactor requirement
(COFACTOR block) [file:human/NAPRT/NAPRT-uniprot.txt]. Correct but generic; the catalytic MF
already captures the enzymatic function. This term is not in the GOA TSV rows seeded into the
review (the TSV lacks the KW-derived metal-ion-binding row), so it is not adjudicated here.

## Biomarker note (context, not a GO annotation)

NAPRT expression status is a biomarker: NAPRT-deficient tumors depend on NAMPT for NAD and are
sensitized to NAMPT inhibitors; NAPRT-proficient tumors can bypass NAMPT inhibition via the
Preiss–Handler route. Relevant to therapeutic context but not a molecular-function annotation.

## Summary of curation decisions

- Core MF: GO:0004516 nicotinate phosphoribosyltransferase activity (EXP/IDA — ACCEPT; IBA,
  IEA — ACCEPT).
- Core BP: GO:0034355 NAD+ biosynthetic process via the salvage pathway (IMP/IBA — ACCEPT);
  GO:0009435 NAD+ biosynthetic process (IEA parent) — ACCEPT (correct but less specific).
- Core CC: GO:0005829 cytosol (IDA/IBA/IEA/TAS — ACCEPT).
- response to oxidative stress (GO:0006979, IMP) — KEEP_AS_NON_CORE (downstream physiological
  consequence of NAD synthesis, per Hara 2007).
- extracellular exosome / extracellular region / azurophil granule lumen — KEEP_AS_NON_CORE
  (proteomics/degranulation detections, not catalytic site).
- protein binding IPI ×6 — MARK_AS_OVER_ANNOTATED (bare, uninformative; not removed).
