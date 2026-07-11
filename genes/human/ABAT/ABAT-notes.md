# ABAT (GABT_HUMAN, UniProtKB:P80404) review notes

Human 4-aminobutyrate aminotransferase (GABA transaminase / GABA-T). No falcon deep
research file (falcon out of credits, HTTP 402). Grounded in the UniProt entry, GOA TSV,
and cached publications.

## Core biology (verified)

- **Enzyme**: 4-aminobutyrate aminotransferase, mitochondrial (EC 2.6.1.19), a
  pyridoxal-5'-phosphate (PLP)-dependent, class-III aminotransferase. It catalyses the
  first step of GABA degradation (the GABA shunt): transamination of GABA
  (4-aminobutanoate) with 2-oxoglutarate to succinate semialdehyde + L-glutamate
  [UniProt P80404 CATALYTIC ACTIVITY, Rhea:RHEA:23352, EC 2.6.1.19; Reactome R-HSA-916855].
- **Second activity**: also acts as (S)-3-amino-2-methylpropionate:2-oxoglutarate
  transaminase (EC 2.6.1.22; L-beta-aminoisobutyrate -> methylmalonate semialdehyde),
  linking to pyrimidine/thymine catabolism. In human this is by-similarity/ISS
  (ECO:0000250|UniProtKB:P50554), not directly assayed in the cached human papers.
  UniProt FUNCTION: "Catalyzes the conversion of gamma-aminobutyrate and
  L-beta-aminoisobutyrate to succinate semialdehyde and methylmalonate semialdehyde,
  respectively." Can also convert delta-aminovalerate and beta-alanine (By similarity).
- **Cofactor**: PLP covalently bound at Lys357 (Schiff base); also binds a [2Fe-2S]
  cluster per homodimer (UniProt COFACTOR; BINDING 163/166; metal-binding & iron-sulfur
  keywords).
- **Subunit**: homodimer, disulfide-linked via Cys321 [PMID:15528998].
- **Localisation**: mitochondrion / mitochondrial matrix (UniProt SUBCELLULAR LOCATION;
  Reactome R-HSA-916855 "The reaction takes place in the mitochondrial matrix").
- **Tissue**: liver > pancreas > brain > kidney > heart > placenta [PMID:7851425].
- **Disease**: GABA-transaminase deficiency (GABATD, MIM:613163), autosomal recessive
  epileptic encephalopathy: psychomotor retardation, hypotonia, hyperreflexia, lethargy,
  refractory seizures, EEG abnormalities; elevated GABA. Variant R220K reduces Vmax to
  ~25% of WT [PMID:10407778].

## Evidence per cited publication

- **PMID:10407778** (Medina-Kauwe 1999, review) — IDA GO:0034386 (transaminase activity)
  + GABATD R220K variant. Abstract: "an inborn error of GABA degradation"; recombinant
  R220K enzyme "Vmax was reduced to 25% of wild-type activity." Supports MF (transaminase
  activity) and disease.
- **PMID:15528998** (Yoon 2004) — IDA. Cys321 disulfide crosslink; WT active, mutants
  inactive. Abstract: "converts the major inhibitory neurotransmitter GABA to succinic
  semialdehyde"; homodimer disulfide-linked. Supports MF (contributes_to transaminase
  activity, dimer), GABA shunt (GO:0006540), and the 4-aminobutyrate transaminase complex
  (GO:0032144, part_of).
- **PMID:15650327** (Kim 2004) — IDA GO:0030170 (PLP binding). Lys357 essential for
  catalysis and PLP binding; mutants lacked 330/415 nm PLP absorption bands. Supports PLP
  binding.
- **PMID:34800366** (Morgen/MitoCoP 2021) — HTP GO:0005739 (mitochondrion). High-confidence
  human mitochondrial proteome; ABAT is one of the MitoCoP proteins (supplementary tables;
  not named in body text). Supports mitochondrial localisation.
- **Reactome:R-HSA-916855** — TAS GO:0005759 (mitochondrial matrix). "GABA and
  2-oxoglutarate (2OG) are converted to succinate semialdehyde (SUCCSA) and L-glutamate
  (L-Glu) by 4 aminobutyrate aminotransferase (ABAT). The reaction takes place in the
  mitochondrial matrix."

## GOA review disposition summary

Core: MF transaminase activity (GO:0034386, IDA x2 + IEA), PLP binding (GO:0030170, IDA +
IEA + IBA), GABA catabolic process (GO:0009450 IBA) / GABA shunt (GO:0006540 IDA),
mitochondrion/matrix localisation (multiple), 4-aminobutyrate transaminase complex
(GO:0032144, part_of, IDA). Secondary MF (S)-3-amino-2-methylpropionate transaminase
(GO:0047298) kept (real EC 2.6.1.22 activity), not core in human.

Over-annotation / non-core: the large Ensembl-Compara (GO_REF:0000107, ECO:0000265) block
of rodent-ortholog phenotype/behaviour BP terms (response to hypoxia/iron/nicotine/
cocaine/ethanol/xenobiotic, copulation, locomotory/exploration behaviour, cerebellum
development, regulation of insulin/dopamine/prolactin/aspartate secretion, blood pressure,
uterine contraction, heat generation, inhibitory postsynaptic potential, dopamine
metabolic process, nervous system process). These are downstream physiological/behavioural
consequences of GABA metabolism transferred from mouse/rat orthologs, not molecular
functions of the human protein — MARK_AS_OVER_ANNOTATED (kept, not removed, per policy on
IEA orthology transfer that is biologically plausible but too indirect). "nervous system
process" (GO:0050877) ISS + IEA is the least indirect but still a high-level BP consequence
-> KEEP_AS_NON_CORE.

GO:0032145 succinate-semialdehyde dehydrogenase binding (ISS) — GABA-T and SSADH act
sequentially in the GABA shunt and are reported to interact; keep as non-core supporting
MF (bare-binding-avoidance does not apply: this is a specific named binding partner, not
generic "protein binding").
