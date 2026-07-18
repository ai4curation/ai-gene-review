# NADSYN1 (Q6IA69) — review notes

Gene: NADSYN1 (HGNC:29832), human, chromosome 11. UniProt: Q6IA69, `NADE_HUMAN`,
706 aa. Recommended name: **Glutamine-dependent NAD(+) synthetase**;
EC 6.3.5.1; alias NAD(+) synthase [glutamine-hydrolyzing]. Evidence at protein
level (PE 1). MANE-Select transcript NM_018161.5 / NP_060631.2.

## Core molecular function

NADSYN1 catalyzes the **final, committed step of NAD+ de novo synthesis**: the
ATP-dependent amidation of deamido-NAD+ (nicotinate adenine dinucleotide, NaAD)
to NAD+, using **L-glutamine** as the physiological nitrogen (amide) donor
(hydrolysed to L-glutamate).

- [file:human/NADSYN1/NADSYN1-uniprot.txt FUNCTION, "Catalyzes the final step of the nicotinamide adenine dinucleotide (NAD) de novo synthesis pathway, the ATP-dependent amidation of deamido-NAD using L-glutamine as a nitrogen source."]
- Reaction (Rhea:24384; EC 6.3.5.1): deamido-NAD(+) + L-glutamine + ATP + H2O = L-glutamate + AMP + diphosphate + NAD(+) + H(+) [file:human/NADSYN1/NADSYN1-uniprot.txt CATALYTIC ACTIVITY].
- PATHWAY: "Cofactor biosynthesis; NAD(+) biosynthesis; NAD(+) from deamido-NAD(+) (L-Gln route): step 1/1." [file:human/NADSYN1/NADSYN1-uniprot.txt PATHWAY]. This same reaction is the last step of BOTH the de novo (tryptophan/kynurenine) route and the Preiss–Handler route, which converge at deamido-NAD+ (NaAD).

### Domain architecture / mechanism (glutaminase + ligase)

Two-domain, bifunctional enzyme:
- N-terminal **carbon–nitrogen (CN) hydrolase / nitrilase-family glutaminase
  domain** (residues ~5–275) hydrolyses glutamine → glutamate + NH3, supplying
  ammonia in situ. Catalytic triad-like active sites at positions 45 (proton
  acceptor), 114, and 175 (nucleophile Cys) [file:human/NADSYN1/NADSYN1-uniprot.txt DOMAIN / ACT_SITE].
- C-terminal **NAD synthetase (ligase) domain** (region ~325–706) performs the
  ATP-dependent amidation of NaAD; ATP-binding P-loop at 355–362 [file:human/NADSYN1/NADSYN1-uniprot.txt REGION / BINDING].
- Hara et al. 2003 (PMID:12547821) showed the CN-hydrolase domain confers
  glutamine dependency; mutating the catalytic Cys-175→Ser abolishes
  glutamine-dependent activity while leaving ammonia-dependent activity intact.
  [PMID:12547821, "mutant NADsyn1 in which Cys-175 corresponding to the catalytic cysteine residue in nitrilases was replaced with Ser does not use glutamine"]
  MUTAGEN annotation confirms this: [file:human/NADSYN1/NADSYN1-uniprot.txt MUTAGEN 175, "C->S: Eliminates glutamine-dependent NAD synthetase activity with the ammonia-dependent activity intact."]
- The intrinsic glutaminase (CN-hydrolase) partial reaction justifies the
  IEA glutaminase-activity annotation (GO:0004359) as a supporting/contributing
  activity, and ATP binding (GO:0005524) as a supporting activity.

Human also has a distinct **NADSYN2** that is ammonia-dependent only (lacks the
CN-hydrolase domain); NADSYN1 uniquely uses glutamine [PMID:12547821, "both NADsyn1 and NADsyn2 have NAD synthetase activity", "NADsyn1 uses glutamine as well as ammonia as an amide donor, whereas NADsyn2 catalyzes only ammonia-dependent NAD synthesis"].

### Kinetics (PMID:12547821, via UniProt)
KM 0.49 mM deamido-NAD+, 0.089 mM ATP, 1.44 mM glutamine, 13.1 mM ammonium —
i.e. much lower KM for glutamine than ammonium, supporting glutamine as the
physiological donor [file:human/NADSYN1/NADSYN1-uniprot.txt BIOPHYSICOCHEMICAL PROPERTIES].

## Quaternary structure / localization

- **Homohexamer** [file:human/NADSYN1/NADSYN1-uniprot.txt SUBUNIT, "Homohexamer."];
  Reactome R-HSA-197271 "NADSYN1 hexamer amidates NAAD to NAD+" describes the
  cytosolic hexamer catalysing the final NAD+ step.
- Localization: **cytosol / cytoplasm** (Reactome TAS R-HSA-197271; IBA; IEA).
  Reactome describes the enzyme as "Cytosolic hexameric NAD synthase 1". Cytosol
  (GO:0005829) is the specific location; "cytoplasm" (GO:0005737) is the broader
  parent.

## Disease

Bi-allelic loss-of-function variants cause **Vertebral, cardiac, renal, and limb
defects syndrome 3 (VCRL3; MIM:618845)** — an autosomal recessive, often lethal
congenital NAD deficiency disorder.
- [file:human/NADSYN1/NADSYN1-uniprot.txt DISEASE, "An autosomal recessive, lethal disorder characterized by severe cardiac and renal anomalies"]
- Szot et al. 2020 (PMID:31883644): five individuals from four families with
  bi-allelic NADSYN1 variants; missense variants show impaired enzymatic activity
  and severely reduced NAD levels by yeast complementation + enzyme assays.
  [PMID:31883644, "Functional assessments of NADSYN1 missense variants, through a combination of yeast complementation and enzymatic assays, show impaired enzymatic activity and severely reduced NAD levels."]
  This is the IMP evidence for GO:0003952 (activity) and GO:0034354 (de novo
  NAD+ process). Congenital NAD deficiency embryopathies are niacin/nicotinamide
  responsive in animal models (part of the broader NAD-deficiency disorder class
  established for HAAO/KYNU).
- VCRL3 variants characterized: p.Cys49Arg (loss of expression), p.Trp132Leu
  (decreased expression + decreased activity), p.Ala573Thr (decreased activity),
  and truncations (245–706 del, 613–706 del) [file:human/NADSYN1/NADSYN1-uniprot.txt VARIANT].

## Protein–protein interactions (IPI) — over-annotations

Three IntAct IPI "protein binding" (GO:0005515) annotations come from
**high-throughput systematic interactome screens**, not NADSYN1-focused studies:
- PMID:25416956 — Rolland et al., "A proteome-scale map of the human interactome
  network" (systematic Y2H); partner Q9H614.
- PMID:31515488 — Fragoza et al., "Extensive disruption of protein interactions
  by genetic variants…" (large-scale interactome); partner Q9NTM9 (CUTC).
- PMID:32296183 — Luck et al., "A reference map of the human binary protein
  interactome" (HuRI); many partners (ANKS1A, COL8A1, CREB5, CUTC, FRS3, GPANK1,
  HGS, HOXC8, MYO15B, NOXA1, NTAQ1, TFG…), matching the UniProt INTERACTION list.

None of these interactions has an established functional role for NADSYN1; they
are uninformative bare "protein binding" and are marked MARK_AS_OVER_ANNOTATED
(policy: never REMOVE an IPI protein-binding annotation).

## Annotation-review summary

- Core MF: **GO:0003952 NAD+ synthase (glutamine-hydrolyzing) activity** —
  EXP (PMID:12547821) and IMP (PMID:31883644): ACCEPT. IBA and IEA duplicates
  ACCEPT / KEEP_AS_NON_CORE.
- Supporting MF: GO:0004359 glutaminase activity (IEA) and GO:0005524 ATP binding
  (IEA) — ACCEPT as supporting (real partial reactions of this enzyme).
- Core BP: GO:0034354 'de novo' NAD+ biosynthetic process from L-tryptophan
  (IMP PMID:31883644, IBA, IEA) — ACCEPT; GO:0009435 NAD+ biosynthetic process
  (IEA) — broader parent, KEEP_AS_NON_CORE.
- Location: GO:0005829 cytosol (TAS Reactome; IEA) — ACCEPT; GO:0005737 cytoplasm
  (IBA, IEA) — broader parent, MARK_AS_OVER_ANNOTATED relative to cytosol.
- GO:0005515 protein binding (3× IPI) — MARK_AS_OVER_ANNOTATED (HT interactome).
</content>
</invoke>
