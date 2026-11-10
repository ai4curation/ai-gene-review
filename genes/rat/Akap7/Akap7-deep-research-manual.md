# Akap7 (rat, Q6JP77) - manual literature synthesis

No deep-research provider was available for this review, so this summary was
compiled by hand from the cached publications in `publications/` and PubMed
searches ("AKAP18delta OR AKAP18gamma OR AKAP7gamma"). Every statement carries
inline provenance.

## Gene and isoforms

- Rat Akap7 (RGD:1303071, GeneID 361458) encodes several splice forms.
  The Swiss-Prot entry Q6JP77 contains only the two long forms, AKAP18delta
  (displayed, 353 aa) and AKAP18gamma (Q6JP77-2, missing residues 56-60).
- The short membrane-anchored isoform AKAP18alpha/AKAP15 is not in Q6JP77.
  In rat it exists as the unreviewed 81-aa entry A0ABK0LH41 (RefSeq
  XP_038937088.1), whose sequence begins MGQLCC and shares its last 57 residues
  with Q6JP77. In human the two forms are separate Swiss-Prot entries
  (O43687 alpha/beta; Q9P0M2 gamma).
  [PMID:27911261 "Only the short α isoform contains N-terminal myristoylation and palmitoylation sites, facilitating plasma membrane association"]
  [PMID:27911261 "Only the final exon, containing the PKA-binding domain characteristic of AKAPs, is shared by all AKAP7 isoforms."]
- Evolution: rat appears to make AKAP7delta but not a native AKAP7gamma.
  [PMID:22834419 "Multi-species AKAP7 gene alignments, show the recent formation of AKAP7δ occurs with the loss of native AKAP7γ in rats and basal primates."]

## Domains

- C-terminal amphipathic RII-binding helix (FT 301-314; L308P reduces RIIalpha
  binding, PMID:15037626 via UniProt). It binds with high affinity.
  [PMID:16483255 "Amongst the AKAPs that bind RIIalpha subunits with high affinity is AKAP7delta [AKAP18delta; K(d) (equilibrium dissociation constant) value of 31 nM]."]
- An RI-binding region overlaps the RII site (shown for mouse AKAP7gamma).
  [PMID:12804576 "Yeast two-hybrid analysis and co-immunoprecipitation studies showed that AKAP7gamma bound the type I PKA regulatory subunit (RI)"]
- Central 2H phosphoesterase domain (residues 88-292, crystal structures 2VFK,
  2VFL and 2VFY of the rat protein) binds 5'AMP and 5'CMP. No phosphoesterase
  activity has been found.
  [PMID:18082768 "It may act as a phosphoesterase, although we did not identify a substrate, or as an AMP sensor with the potential to couple intracellular AMP levels to PKA signalling events."]
- Polybasic nuclear localization signal (Pfam PF10469 AKAP7_NLS), masked when
  PKA is bound.
  [PMID:30455320 "Targeting proceeds via a mechanism whereby association with the PKA holoenzyme masks a polybasic nuclear localization signal on the anchoring protein."]

## Functions

### PKA anchoring (core)
- AKAP18delta binds RII in vitro and in vivo.
  [PMID:15037626 "AKAP18delta functions as an AKAP in vitro and in vivo."]
- PMID:21177871 (full text read) used full-length AKAP18delta binding to RIIalpha as its
  screening assay for small-molecule disruptors.
  [PMID:21177871 "where full-length AKAP18δ was added to RIIα subunits of PKA bound to 384-well microtiter plates"]
  [PMID:21177871 "This peptide inhibited the AKAP18δ-RIIα subunit interaction with an IC50 value of 10 nm"]
  In cardiomyocyte lysates FMP-API-1 reduced the amount of AKAP18delta pulled
  down on cAMP-agarose with RII, and the authors read the AKAP18delta-PKA complex
  as the one that sets PKA beside PLN.
  [PMID:21177871 "FMP-API-1 displaces PKA from AKAP18δ (Fig. 2), which tethers PKA to PLN (22)"]
  [PMID:21177871 "The PKA-mediated PLN phosphorylation depends on the interaction of PLN with AKAP18δ (22)."]
- Phosphorylation of RII at S96 changes AKAP15/18 binding in neonatal rat
  cardiomyocytes.
  [PMID:18550536 "Coimmunoprecipitation showed that more AKAP15/18 was pulled down by the phosphomimic, RIIS96D, than RIIS96A."]
- EM structures of type II PKA bound to AKAP18gamma.
  [PMID:24192038 "Electron microscopy and three-dimensional reconstructions of type-II PKA-AKAP18γ complexes reveal hetero-pentameric assemblies that adopt a range of flexible tripartite configurations."]

### SERCA2/PLN complex in heart (core context in rat)
- [PMID:17901878 "We show that AKAP18delta acts as a scaffold that coordinates PKA phosphorylation of PLN and the adrenergic effect on Ca(2+) re-uptake."]
- [PMID:26027516 "Here, we further these findings by showing that phosphorylation of PLB requires interaction with AKAP7δ/γ and that this interaction occurs only when PLB is unphosphorylated."]
- [PMID:22834419 "AKAP7 immunostaining is prominent in the sarcoplasmic reticulum in both rat (expressing AKAP7δ only) and mouse (predominantly AKAP7γ but also AKAP7δ)."]
- Contrary in vivo result in mouse: deleting every AKAP7 isoform does not impair
  adrenergic Ca2+ handling.
  [PMID:23035250 "KO cardiomyocytes responded normally to adrenergic stimulation, as measured by whole-cell patch clamp or a fluorescent intracellular Ca(2+) indicator."]
  [PMID:23035250 "Immunoblot and RT-PCR revealed that only the long isoforms of AKAP7 were detectable in ventricular cardiomyocytes."]

### Renal AQP2 shuttle
- [PMID:15037626 "Within the particulate fraction, AKAP18delta was identified on the same intracellular vesicles as AQP2 and PKA."]
- [PMID:15037626 "AVP not only recruited AQP2, but also AKAP18delta to the plasma membrane."]
- [PMID:15037626 "The elevation of cAMP caused the dissociation of AKAP18delta and PKA."]
- [PMID:17135396 "AKAP18delta, which is located on AQP2-bearing vesicles, directly interacts with PDE4D and PKA."]

### Other partners
- PKC: [PMID:22670899 "These data demonstrate a direct interaction between PKC and both isoforms of AKAP7."]
- CaV1.2 in T-tubules is reported for AKAP15, the short alpha form.
  [PMID:14569017 "A kinase-anchoring protein 15 (AKAP15) coimmunoprecipitates with CaV1.2 channels isolated from rat heart membrane extracts and transfected cells, and it colocalizes with CaV1.2 channels and PKA in the transverse tubules of isolated ventricular myocytes."]

### Neuronal role (mouse; mainly the alpha isoform)
- [PMID:27911261 "Genetic ablation of AKAP7 specifically from dentate granule cells results in disruption of MF-CA3 LTP directly initiated by cAMP"]
- [PMID:27911261 "Western immunoblotting demonstrated that the α isoform is much more abundant than γ/δ in the hippocampus"]

### Localization of the long forms
- [PMID:27911261 "Long isoforms, γ/δ, are predominantly cytosolic, although they contain a potential nuclear localization sequence."]
- [PMID:12804576 "endogenous AKAP7gamma protein was found in both the nucleus and cytoplasm of oocytes."]
