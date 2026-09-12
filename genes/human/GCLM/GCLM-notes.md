# GCLM (glutamate-cysteine ligase modifier/regulatory subunit) — review notes

UniProt: P48507 (GSH0_HUMAN). HGNC:4312. Gene synonym GLCLR. Taxon: Homo sapiens (9606).

## Summary of function

GCLM is the **modifier (regulatory / light) subunit of glutamate-cysteine ligase (GCL)**, also
called gamma-glutamylcysteine synthetase (γ-GCS). GCL catalyzes the **first and rate-limiting
step of glutathione (GSH) biosynthesis**: the ATP-dependent ligation of L-glutamate and
L-cysteine to form L-γ-glutamyl-L-cysteine (γ-glutamylcysteine).

- UniProt RecName: "Glutamate--cysteine ligase regulatory subunit"; AltNames include "GCS light
  chain", "Gamma-ECS regulatory subunit", "Glutamate--cysteine ligase modifier subunit"
  [file:human/GCLM/GCLM-uniprot.txt "RecName: Full=Glutamate--cysteine ligase regulatory subunit"].
- PATHWAY: "Sulfur metabolism; glutathione biosynthesis; glutathione from L-cysteine and
  L-glutamate: step 1/2." [file:human/GCLM/GCLM-uniprot.txt].
- SUBUNIT: "Heterodimer of a catalytic heavy chain and a regulatory light chain."
  [file:human/GCLM/GCLM-uniprot.txt]. The catalytic heavy chain is GCLC (P48506).
- INTERACTION: GCLM (P48507) binds GCLC (P48506; NbExp=5) and OSGIN1 (Q9UJX0; NbExp=3)
  [file:human/GCLM/GCLM-uniprot.txt].
- SIMILARITY: "Belongs to the aldo/keto reductase family. Glutamate--cysteine ligase light
  chain subfamily." — GCLM has an aldo/keto-reductase-like fold (Pfam PF00248 Aldo_ket_red) but
  is **not itself catalytic**; catalysis resides in GCLC [file:human/GCLM/GCLM-uniprot.txt].

## Modifier-subunit role (the core biology)

GCLM has **no glutamate-cysteine ligase activity on its own**; it acts by binding the catalytic
subunit GCLC. Heterodimer formation with GCLM markedly optimizes GCLC catalysis: it lowers the
Km for glutamate and ATP and raises the Ki for feedback inhibition by GSH, thereby greatly
increasing GSH-synthesis efficiency under physiological conditions.

- Reconstitution: adding recombinant GCLM (GCSl) to HeLa extracts increased GCS activity 2–3-fold;
  transient GCSl transfection increased GCS activity ~2-fold and modestly raised GSH; a stable
  GCSl-overexpressing line had ~2-fold higher GCS activity and regenerated GSH faster after
  depletion [PMID:9895302 "Addition of recombinant GCSl to HeLa cell extracts in vitro was found
  to result in an increase in GCS activity of between 2- and 3-fold"].
- Heterodimer assembly increases holoenzyme activity: incubating wild-type GCLC with GCLR
  increased GCL activity by 110% [PMID:9841880 "increased by 110% after wild-type hGLCLC was
  incubated with hGLCLR for 10 min"]; the study also localizes GCLC Cys-553 to the GCLC–GCLR
  heterodimer interface [PMID:9841880 "cysteine-553 in hGLCLC is involved in heterodimer formation
  between hGLCLC and hGLCLR"].
- Recombinant human holoenzyme (GCLC+GCLM co-expressed) is fully active and behaves like native
  enzyme (feedback-inhibited by GSH, inhibited by BSO) [PMID:9675072 "coexpression in Escherichia
  coli ... of the human gamma-GCS catalytic (heavy) subunit and regulatory (light) subunit";
  "is feedback inhibited by glutathione and is potently inhibited by buthionine sulfoximine"].

This is exactly what GO models with GO:1990609 "glutamate-cysteine ligase regulator activity"
(MF, "Binds to and modulates the activity of glutamate-cysteine ligase") and GO:0035226
"glutamate-cysteine ligase catalytic subunit binding" (binds GCLC). GO:0004357
"glutamate-cysteine ligase activity" is a property of the holoenzyme and is annotated to GCLM
only with `contributes_to` (PMID:16183645, IMP), which is appropriate.

## Physiological / phenotype evidence

- Both subunits are essential for neuron survival: shRNA knockdown of either GCLC or GCLM in
  primary cortical neurons disrupted GCL (activity + GSH) and caused apoptotic death rescued by
  γ-glutamylcysteine/GSH ethyl ester [PMID:16183645 "both catalytic and modulatory subunits are
  essential for the survival of primary neurons"; "Independent targeting of the catalytic and
  modulatory subunits by shRNA caused disruption of GCL as assessed by ... enzyme activity, and
  glutathione concentrations"]. Note: overexpressing the catalytic (but not modulatory) subunit
  alone raised activity/GSH — GCLM is rate-optimizing but GCLC carries catalysis.
- Transcriptional regulation: GCLM (GLCLR) promoter is oxidant-inducible; sodium nitroprusside
  raised GSH ~2-fold, GCS activity ~6-fold, and GLCLR transcription ~2.5-fold in HepG2/HT29
  [PMID:10395918 "increase glutathione levels by 2-fold, as well as GCS activity by 6-fold";
  "transcriptional activity of the GLCLR gene was increased by approximately 2.5-fold"]. GCLM is
  an NFE2L2 (NRF2)/ARE target (Reactome R-HSA-9760125).
- Human genetics: the GCLM promoter -588C/T polymorphism (T = lower oxidant-inducible promoter
  activity, lower plasma GSH) is a risk factor for myocardial infarction [PMID:12081989 "the T
  allele showed lower promoter activity ... in response to oxidants"; "genetic risk factor for
  MI"] and is associated with impaired NO-mediated coronary vasomotor function [PMID:12975258
  "causes a decrease in endothelial NO bioactivity, leading to impairment of endothelium-dependent
  vasomotor function"]. These support downstream physiology (oxidative-stress defense; vascular NO
  tone) but are genetic-association/promoter data, not direct molecular function.

## Localization

Cytosol. Reactome TAS annotations to GO:0005829 (cytosol) via R-HSA-174367, R-HSA-5602892,
R-HSA-9760125; also a NAS from PMID:9895302 [file:human/GCLM/GCLM-uniprot.txt: "DR GO; GO:0005829;
C:cytosol; TAS:Reactome"].

## Protein-interaction (IPI GO:0005515) annotations

Five bare "protein binding" IPI annotations (IntAct). WITH/FROM in GCLM-goa.tsv:
- PMID:9675072 → UniProtKB:P48506 (GCLC) — co-expression/holoenzyme purification.
- PMID:28514442 (BioPlex 2.0) → UniProtKB:P48506 (GCLC).
- PMID:33961781 (BioPlex 3.0) → UniProtKB:P48506 (GCLC).
- PMID:40205054 (multimodal cell maps) → UniProtKB:P48506 (GCLC).
- PMID:32296183 (HuRI) → UniProtKB:Q9UJX0 (OSGIN1), NOT GCLC. This is a high-throughput binary
  screen; OSGIN1 (oxidative stress-induced growth inhibitor 1) also appears in the UniProt
  INTERACTION block.
All are uninformative bare "protein binding" → MARK_AS_OVER_ANNOTATED (never REMOVE an IPI);
the specific, informative version of the GCLC interaction is captured by GO:0035226.

## Disease

Reduced GCLM/GSH is linked to hemolytic anemia/GSH deficiency phenotypes (the HAGGSD disease is
classically GCLC-linked; Reactome R-HSA-5602892). MIM 601176 (GCLM gene+phenotype).

## Core function decisions

1. **GO:1990609 glutamate-cysteine ligase regulator activity** (MF) — the defining molecular
   function: binds and modulates GCL (raises efficiency; lowers Km glutamate/ATP; raises Ki for GSH
   feedback). Supported by PMID:9895302, PMID:9841880.
2. **GO:0004357 glutamate-cysteine ligase activity** as **contributes_to** — GCLM contributes to
   the holoenzyme catalytic activity but does not catalyze alone (PMID:16183645 IMP contributes_to).
   Modeled with contributes_to, not enables.
3. **GO:0017109 glutamate-cysteine ligase complex** (`in_complex` / part_of) — GCLM is a subunit
   of the GCL heterodimer (ComplexPortal CPX-2865; PMID:9675072, PMID:9841880 IDA).
4. **GO:0006750 glutathione biosynthetic process** (BP) — step 1 of GSH biosynthesis.
5. Location: **GO:0005829 cytosol**.

Do NOT assign a standalone catalytic MF (enables GO:0004357) to GCLM.
