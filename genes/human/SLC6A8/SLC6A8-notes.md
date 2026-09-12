# SLC6A8 (CRT/CT1) — gene review notes

UniProt P48029 (SC6A8_HUMAN). HGNC:11055. Gene at Xq28. 635 aa, 12-TM, SLC6 (SNF/NSS;
TC 2.A.22) family, SLC6A8 subfamily. Disease: X-linked cerebral creatine deficiency
syndrome 1 (CCDS1 / creatine transporter deficiency, CTD).

## Core molecular function: creatine:Na+:Cl- symport

- UniProt CATALYTIC ACTIVITY (Rhea RHEA:71831):
  `creatine(out) + chloride(out) + 2 Na(+)(out) = creatine(in) + chloride(in) + 2 Na(+)(in)`
  i.e. 2 Na+ : 1 Cl- : 1 creatine stoichiometry, electrogenic symport.
- Intestinal study confirms stoichiometry directly: [PMID:12433955 "This
  accumulation was electrogenic, Na(+)- and Cl(-)-dependent, with a probable stoichiometry
  of 2 Na(+): 1 Cl(-): 1 creatine"].
- Heart cDNA in Xenopus oocytes: Na+- and Cl--dependent creatine uptake, Km ~20 uM
  [PMID:9882430 "Expression of this human heart cDNA clone in Xenopus laevis oocytes
  induced a Na+- and Cl--dependent creatine uptake activity that saturated with a Km of
  approximately 20 microM for creatine"]. Km(Na+) 59 mM, Km(Cl-) 5 mM (UniProt
  BIOPHYSICOCHEMICAL).
- Kidney cDNA: high-affinity creatine uptake Km = 77 uM, NO choline transport
  [PMID:7953292 "mediated high affinity (Km = 77 +/- 6 microM) creatine uptake, which was
  blocked by creatine analogs with high affinity. There was no specific transport of
  choline"].
- Brainstem/spinal cord cDNA: sodium-dependent creatine uptake Km 14.9 uM
  [PMID:7945388 "Transient expression of the hCRT-BS2M in COS-7 cells demonstrates sodium
  dependent [14C]creatine uptake with a KM value of 14.9 +/- 3.0 microM"].
- Electrogenic activity demonstrated electrophysiologically; all CTD mutants lose both
  transport and electrogenic activity [PMID:22644605 "Mutations led to the complete loss
  of both electrogenic and transport activities in X. laevis and Cr uptake in patients'
  fibroblasts"]. guanidinopropionate is a substrate analog; phosphocreatine derivative
  gives partial activity.

## Substrate specificity

- High specificity for creatine. Distant analogues (GABA, choline, glycine, beta-alanine,
  taurine, betaine) do NOT inhibit creatine uptake [PMID:12433955 "More distant structural
  analogues of creatine, such as GABA, choline, glycine, beta-alanine, taurine and betaine,
  had no effect on intestinal creatine uptake, indicating a high substrate specificity of
  the creatine transporter"]. Close guanidino analogues (guanidinopropionic acid,
  cyclocreatine) compete. So despite being in the GABA/monoamine transporter (SLC6) family,
  it does NOT efficiently transport GABA — it is a creatine transporter. Guanidinoacetate
  (the GAMT substrate precursor) is a poor substrate relative to creatine.

## Localization

- Plasma membrane / cell membrane; multi-pass. UniProt SUBCELLULAR LOCATION: Cell membrane
  (PMID:22644605); Apical cell membrane (PMID:12433955).
- All CTD mutants tested were correctly trafficked to plasma membrane [PMID:22644605 "All
  mutants were properly targeted to the plasma membrane in both systems"] — so for these
  the defect is in transport function, not localization.
- In polarized epithelia (intestine, kidney) it is apical: [PMID:12433955 "CRT protein was
  mainly associated with the apical membrane of the enterocytes"].

## Tissue expression / physiology

- Highest in skeletal muscle, kidney, heart; lower in brain and other tissues
  [PMID:7953292 "Northern analysis demonstrated highest levels of mRNA expression in human
  skeletal muscle, kidney, and heart, with lower levels in brain and other tissues"];
  [PMID:7945388 "mRNAs most prominently in the skeletal muscle, heart and kidney"].
- UniProt TISSUE SPECIFICITY: "Predominantly expressed in skeletal muscle and kidney. Also
  found in brain, heart, colon, testis and prostate."
- Supplies creatine to the brain via the blood-brain barrier (UniProt FUNCTION, By
  similarity to mouse Q8VBW1). Creatine/phosphocreatine is the cellular ATP buffer in
  tissues with fluctuating energy demand [PMID:8661037 "Creatine and creatine phosphate act
  as a buffer system for the regeneration of ATP in tissues with fluctuating energy
  demands"].

## SLC6 family relationship

- Member of Na+/Cl--dependent neurotransmitter symporter (SNF/NSS) family; closely related
  to taurine, GABA and betaine transporters [PMID:7953292 "the human creatine transporter
  is strongly related to a subfamily of sequences which includes the transporters for
  taurine, GABA, and betaine"]. This relationship is the basis of the IBA GABA-symporter
  annotation — but the experimentally established substrate is creatine, not GABA.

## Disease — CCDS1 / creatine transporter deficiency (CTD), X-linked

- X-linked intellectual disability with severe speech delay, behavioral problems and
  seizures; carrier females may have milder impairment. ~50% of carrier females affected
  [PMID:25861866 "Creatine transporter deficiency (CRTR-D) is an X-linked inherited disorder
  of creatine transport. All males and about 50% of females have intellectual disability or
  cognitive dysfunction"]. Many pathogenic missense/in-frame deletion variants reduce or
  abolish creatine transport in functional assays [PMID:17465020].

## Regulation (non-core)

- SPAK/OSR1 (WNK-controlled) kinases negatively regulate SLC6A8 activity in Xenopus oocytes
  [PMID:25531585]. Phosphorylated at Thr-42, Thr-617, Thr-620 (large-scale phosphoproteomics).

## Structure

- Cryo-EM structures of human SLC6A8 (PDB 9KR7, 9KRH, 9KRI), ~3.3-3.4 A.

## Annotation review summary

CORE: GO:0005309 creatine:sodium symporter activity (MF; strong IDA/IMP),
GO:0015881 creatine transmembrane transport (BP), GO:0005886 plasma membrane (CC).
GO:0005308 creatine transmembrane transporter activity (parent MF, NAS) is correct but
less precise than 0005309 → KEEP_AS_NON_CORE/ACCEPT.

OVER-ANNOTATIONS / family-electronic leakage:
- GO:0005332 gamma-aminobutyric acid:sodium:chloride symporter activity (IBA): wrong
  substrate — SLC6A8 does not transport GABA; MARK_AS_OVER_ANNOTATED.
- GO:0006836 neurotransmitter transport (IEA InterPro): creatine is not a neurotransmitter;
  over-annotation from family signature → MARK_AS_OVER_ANNOTATED.
- GO:0015812 gamma-aminobutyric acid transport (IEA, inferred from GO:0005332):
  inherits the wrong-substrate error → MARK_AS_OVER_ANNOTATED.
- GO:0006865 amino acid transport (IBA): creatine is not an amino acid (it's a guanidino
  compound); too generic/imprecise → MARK_AS_OVER_ANNOTATED.
- GO:0006936 muscle contraction (TAS PMID:8661155, a genomic-organization paper): indirect
  physiological role, not a molecular function of the transporter → KEEP_AS_NON_CORE.
- GO:0035725 sodium ion transmembrane transport (IBA): true (it cotransports Na+) but
  generic; KEEP_AS_NON_CORE.
- GO:0016020 membrane (TAS), GO:0006600 creatine metabolic process (TAS Reactome): generic
  but acceptable; ACCEPT/KEEP_AS_NON_CORE.
- GO:0016324 apical plasma membrane (IDA PMID:12433955; IEA): correct in polarized epithelia
  (apical), ACCEPT but context-specific → KEEP_AS_NON_CORE for the gene as a whole.
