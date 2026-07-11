# ALDOB (P05062) review notes

Human fructose-bisphosphate aldolase B (liver-type aldolase). Deep research (falcon)
did not materialize within the 8-min poll window; review grounded in the UniProt record
(`ALDOB-uniprot.txt`), the seeded GOA (`ALDOB-goa.tsv`), cached `publications/PMID_*.md`,
and the HFI disorders KB (`~/repos/dismech/kb/disorders/Hereditary_Fructose_Intolerance.yaml`).

## Core biology

- Class I (Schiff-base) fructose-1,6-bisphosphate aldolase, EC 4.1.2.13; homotetramer;
  active-site Lys230 forms the Schiff-base intermediate, Asp188 is proton acceptor
  (UniProt FT ACT_SITE 188, 230).
- Two catalytic activities in one active site:
  - **Fructose-bisphosphate aldolase (GO:0004332)**: F1,6BP <-> DHAP + G3P (glycolysis/
    gluconeogenesis). Rhea:14729, EC 4.1.2.13.
  - **Fructose-1-phosphate aldolase (GO:0061609)**: F1P -> DHAP + D-glyceraldehyde
    (fructolysis). Rhea:30851. ALDOB has comparatively high F1P activity vs ALDOA/ALDOC.
  - UniProt kinetics: KM ~1 uM for F1,6BP, ~0.7-2.3 mM for F1P (PMID:10970798, PMID:20848650).
- Cytosolic (GO:0005829). Also reported at cytoskeleton/MTOC/centriolar satellite
  (PMID:18000879) and binds actin cytoskeleton (PMID:9244396) — moonlighting/peripheral.
- Tissue expression: liver, kidney, intestine (HPA "Group enriched (intestine, kidney, liver)").

## Disease

- **Hereditary fructose intolerance (HFI, MONDO:0009249, MIM:229600)** — autosomal
  recessive aldolase B deficiency. Fructose ingestion -> F1P accumulation, ATP/Pi
  depletion, hypoglycemia, hepatic/renal toxicity. Common alleles A150P, A175D, N335K
  (UniProt VARIANT). Many HFI variants characterized functionally in the cited papers
  (PMID:3383242, 10625657, 10970798, 12205126, 20848650).

## Moonlighting / non-canonical

- **Tumor suppressor scaffold (PMID:35122041, abstract-only)**: Aldob directly binds and
  inhibits G6PD, potentiating p53-mediated inhibition of G6PD in an Aldob-G6PD-p53
  ternary complex; scaffolding effect independent of enzymatic activity. Basis for GOA
  IDA molecular_adaptor_activity (GO:0060090), IMP negative regulation of PPP shunt
  (GO:1905856), and IPI protein binding to TP53/G6PD. Mutagenesis (K147A, R149A, K230A)
  impairs G6PD interaction (UniProt MUTAGEN).
- **V-ATPase assembly (PMID:17576770, abstract-only)**: aldolase physically associates
  with the B subunit of vacuolar H+-ATPase; binding (not catalysis) required for V-ATPase
  assembly/activity. Basis for GOA IMP GO:0070072 and IDA GO:0051117 ATPase binding.
  Note: the abstract describes "aldolase" generically; curator (BHF-UCL) attributed to ALDOB.
- **BBS protein interactions (PMID:18000879, abstract-only)**: Y2H + coIP + colocalization
  with BBS1/2/4/7; basis for centriolar satellite / MTOC localization and protein binding IPIs.
- Cytoskeleton binding (PMID:9244396): aldolase B binds liver cytoskeleton (actin);
  basis for GO:0008092 cytoskeletal protein binding IDA.

## Curation decisions summary

- Core MF: GO:0004332 and GO:0061609 (both heavily EXP/IDA supported) -> ACCEPT.
- Core BP: fructolysis/fructose catabolism (GO:0006001), glycolysis (GO:0006096),
  gluconeogenesis (GO:0006094), F1,6BP metabolic process (GO:0030388), fructose
  metabolic process (GO:0006000) -> ACCEPT/KEEP.
- Bare `protein binding` (GO:0005515) IPIs: uninformative -> MARK_AS_OVER_ANNOTATED
  (per policy, not REMOVE). The ALDOA IPIs (P04075) are large-scale interactome hits
  reflecting the homo/heterotetramer / co-purification.
- Moonlighting scaffold functions (G6PD/p53, V-ATPase, BBS, cytoskeleton, MTOC/centriolar
  satellite) -> KEEP_AS_NON_CORE; real but peripheral to the canonical aldolase function.
- extracellular exosome (GO:0070062, HDA prostatic-secretion exosome proteomics) ->
  KEEP_AS_NON_CORE (mass-spec bystander).
- Reactome cytosol TAS duplicates -> ACCEPT (cytosol) / KEEP_AS_NON_CORE where redundant.

## Verification note on PMID:6696436

GOA line 25: EXP GO:0004332 with original_reference_id PMID:6696436, assigned by Reactome.
The cached abstract (PMID:6696436) is "Human skeletal-muscle aldolase: N-terminal sequence
analysis..." — a sequencing paper on muscle (ALDOA) aldolase, not an activity assay on ALDOB.
Per policy (do not REMOVE experimental annotations whose full text I can't verify, and the
paper is clearly about the aldolase family EC 4.1.2.13), marked UNDECIDED: the EC 4.1.2.13
family activity is correct for aldolases but this specific reference does not appear to
establish ALDOB fructose-bisphosphate aldolase activity; other strong EXP/IDA lines already
support GO:0004332.
