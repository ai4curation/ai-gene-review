# GCK (glucokinase / hexokinase-4, P35557) — review notes

## Summary of gene function

GCK encodes glucokinase (hexokinase-4 / hexokinase type IV / hexokinase-D), the
high-Km hexose-phosphorylating enzyme (EC 2.7.1.1) expressed mainly in pancreatic
beta cells and hepatocytes. It catalyzes the first, committed step of glucose
utilization: phosphorylation of D-glucose to D-glucose 6-phosphate using ATP
(RHEA:17825). It also phosphorylates D-mannose and D-fructose (and, weakly,
2-deoxyglucose, glucosamine), but these are of minor physiological relevance
[UniProt P35557 CATALYTIC ACTIVITY; PMID:7742312].

The defining property that distinguishes GCK from HK1-3 is its weak affinity for
glucose (KM ~6 mM, sigmoidal/cooperative kinetics, Hill coefficient ~1.7) and lack
of product inhibition by G6P. This makes it a physiological glucose sensor: its
activity varies steeply across the physiological blood-glucose range, so it sets the
threshold for glucose-stimulated insulin secretion in the beta cell and controls
hepatic glucose uptake/glycogen synthesis in the liver
[PMID:7742312 "KM=6.03 mM for glucose"; UniProt "GCK acts as a glucose sensor in the pancreatic beta cell"].

## Regulation and localization

- **Cytosolic** in both beta cells and hepatocytes; the HPA IDA and Reactome/IBA
  place it in cytosol (GO:0005829) [GOA rows 7, 33, 39, 63, 67-72].
- In **hepatocytes**, GCK is regulated by the glucokinase regulatory protein GCKR:
  at low glucose (and high fructose-6-phosphate) GCK binds GCKR and the inactive
  complex is sequestered in the nucleus; at high glucose GCK is released back to the
  cytosol [PMID:10456334; UniProt ACTIVITY REGULATION/SUBUNIT]. This is the basis of
  the nucleus (GO:0005634) and nucleoplasm (GO:0005654) annotations and the Reactome
  GCK1:GCKR transport reactions.
- Interacts with **MIDN** (midnolin ubiquitin-like domain), preferentially at low
  glucose, inhibiting activity [PMID:24187134]; with **PFKFB1/PFK-2/FBPase-2**
  [PMID:11522786]; with **GCKR** [PMID:16173921 Y2H, PMID:32296183 HuRI].

## Disease

- **MODY2 / GCK-MODY** (MIM:125851): heterozygous inactivating mutations → mild,
  stable fasting hyperglycemia (compensated by the WT allele).
- **PNDM1** (MIM:606176): homozygous/biallelic loss → permanent neonatal diabetes;
  protein instability is a major severity determinant [PMID:25015100].
- **HHF3 / GCK-hyperinsulinism** (MIM:602485): heterozygous activating (gain-of-function)
  mutations, often in the allosteric activator site → hyperinsulinemic hypoglycemia
  [PMID:12941786, PMID:15277402, PMID:11916951, PMID:17082186, PMID:19146401].
- T2D susceptibility variants (GWAS, e.g. rs1799884) affect fasting glucose /
  insulin secretion [PMID:20668700].

## Annotation review decisions (high level)

- **Core MF**: glucokinase activity (GO:0004340) — strongly supported by many EXP/IDA
  annotations and the whole disease literature. ACCEPT the experimental instances.
- **Hexokinase activity (GO:0004396)**, **ATP binding (GO:0005524)**, **D-glucose
  binding (GO:0005536)** — correct and experimentally supported; ACCEPT.
- **Fructokinase (GO:0008865) / mannokinase (GO:0019158)** — genuine in-vitro
  activities (PMID:7742312), but of minor/uncertain physiological relevance; the EXP
  instances are real so ACCEPT/KEEP_AS_NON_CORE; the RHEA/IBA electronic ones are the
  same broad substrate promiscuity.
- **Glucose/G6P metabolic process, glycolysis, glucose homeostasis, regulation of
  insulin secretion, glucose sensor activity** — all well supported; core BP/MF.
- **protein binding (GO:0005515) IPI** — uninformative MF; MARK_AS_OVER_ANNOTATED
  (per policy, do not REMOVE IPIs). The real interactions (GCKR, MIDN, PFKFB1) are
  captured in notes/description.
- **calcium ion import (GO:0070509)** — Ensembl-projected IEA from mouse ortholog;
  not a GCK molecular function; over-propagated electronic inference → MARK_AS_OVER_ANNOTATED.
- **cytoplasmic side of mitochondrial outer membrane (GO:0032473) / mitochondrion
  (GO:0005739)** — these come from the hexokinase family IBA/ISS (HK1-3 are OMM-bound
  via their N-terminal hydrophobic anchor; GCK lacks this anchor and is cytosolic).
  Over-annotation by family inheritance → MARK_AS_OVER_ANNOTATED.
- **purine nucleotide metabolic process (GO:0006163)**, **nicotinamide nucleotide
  metabolic process (GO:0046496)** — ARBA electronic mappings; too indirect / not the
  gene's role (ATP is a co-substrate, not evidence of purine metabolism) →
  MARK_AS_OVER_ANNOTATED.
</content>
</invoke>

## 2026-10-10 review pass (INITIALIZED -> COMPLETE)

- **Mitochondrion corrected.** The earlier notes treated GO:0005739 as hexokinase-family
  over-propagation. That was wrong for the ISS row: its source UniProtKB:P17712 is HXK4_RAT
  (rat glucokinase itself), whose mitochondrion location rests on rat liver fractionation
  [PMID:16542652 "We confirmed association of glucokinase immunoreactivity with rat liver mitochondria using Percoll gradient centrifugation"]
  (following Danial et al. 2003, BAD-glucokinase mitochondrial complex). Both mitochondrion
  rows (ISS, IEA) are now KEEP_AS_NON_CORE: a minor pool, not the main compartment.
  The IBA "cytoplasmic side of mitochondrial outer membrane" stays MARK_AS_OVER_ANNOTATED
  (sources P52789 = human HK2 and M4FD55 = Brassica hexokinase, both anchor-bearing);
  the source comments were corrected (P52789 had been mislabelled as rat HK1).
- **protein binding (GO:0005515) IPI x3** changed MARK_AS_OVER_ANNOTATED -> REMOVE per
  the repo policy for this term; the GCKR, PFKFB1 and MIDN interactions stay in notes/description.
- Core function 2 (beta-cell glucose sensing) now also lists positive regulation of insulin
  secretion (GO:0032024, accepted IMP PMID:8132752) and cytosol.
- dismech alignment: Congenital_Isolated_Hyperinsulinism binds GO:0004340 glucokinase activity
  INCREASED on the GCK node, matching the AIGR core MF. Hyperinsulinemic_Hypoglycemia's
  "Lowered Beta-Cell Glucose Set-Point" node binds only GO:0050796 (DYSREGULATED) and no MF.


## 2026-11-04 biological reassessment

Human GCK directly phosphorylates glucose and contributes to its concentration-dependent coupling with insulin secretion. Human mutation studies distinguish a shifted secretory response from complete absence of insulin release, and reduced hepatic glycogen accumulation from glycogen-synthase activity (PMID:7742312; PMID:8132752; PMID:8878425). The three earlier repeated catalytic cores are consolidated into one activity with distinct glycolytic, secretory-regulatory and systemic homeostasis facets.

Mannose and fructose phosphorylation are genuine enzymatic observations, but GCK-specific physiological alternative-sugar flux remains uncertain (PMID:7742312). The three natural products differ at the amino terminus; reported liver-mRNA translation differences do not prove that either liver protein is catalytically inactive (PMID:1871135; PMID:1354840).

The mitochondrial assessment now incorporates the actual ancestral PAINT placement. It does not infer a target-specific loss from the short donor list or from comparison with other hexokinase anchors. Rat mitochondrial association remains positive but bounded localization evidence (PMID:16542652). Nuclear sequestration and cytosolic return remain distinct from active nuclear catalysis (PMID:10456334; PMID:24187134).

Interaction refinements follow the partner's demonstrated molecular role, while generic screen positives remain real interactions even when their uninformative GO term is removed (PMID:11522786; PMID:32296183). The leptin response remains claim-specific uncertainty because the relevant donor experiment is not resolved by the available text (PMID:17470517). Gck-dependent calcium elevation places the enzyme upstream of stimulus–secretion coupling, not in the calcium-import machinery (PMID:18477811).

Source access, construct distinctions and the earlier review's preserved evidence are documented in [GCK-source-guide.md](GCK-source-guide.md) and [GCK-evidence.json](GCK-evidence.json). Earlier journal entries above remain unchanged.

### Structural and variant assay scope

The regulator complex combines human pancreatic GCK with rat GKRP; fructose 6-phosphate binds GKRP and favors the inhibited complex. Nearby GCK substitutions can produce opposite biochemical and glycemic effects, but modeled secretion thresholds do not fully explain clinical severity. These studies strengthen regulator and catalytic mechanisms without assigning every construct to a natural product. [PMID:23957911](https://pubmed.ncbi.nlm.nih.gov/23957911/); [PMID:19884385](https://pubmed.ncbi.nlm.nih.gov/19884385/).

## 2026-11-05 sugar kinetics and functional scope

The curated UniProt kinetics explicitly attributed to PMID:7742312 confirm efficient mannose turnover alongside glucose, and lower fructose catalytic efficiency under the reported conditions. The original kinetic tables remain unaccessed, but the numerical record is available and used; physiological GCK-dependent alternative-sugar flux remains a separate uncertainty. The values and conditions are centralized in [GCK-source-guide.md](GCK-source-guide.md).

Glucose sensing remains a defining core property of the same concentration-responsive catalytic mechanism. The real Gck-dependent calcium phenotype supports upstream coupling, while assigning calcium import itself exceeds the demonstrated role (PMID:18477811). Broad hexokinase activity remains true through its accepted glucokinase child; this does not assert activity on every hexose or deny the measured alternative reactions. Earlier journal text remains historical.

The mitochondrial-side term permits peripheral association rather than requiring the HK1/HK2 amino-terminal binding mechanism. The actual ancestral placement and mouse BAD-associated GCK complex remain compatible with a minor mitochondrial pool; neither establishes direct human membrane topology or GCK–VDAC binding (PMID:12931191; PMID:16542652). The newly assessed study is abstract-only in the normal cache, and its original full text was not recovered.
