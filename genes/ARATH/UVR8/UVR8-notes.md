# UVR8 (UV RESISTANCE LOCUS 8) — Arabidopsis thaliana — Research Notes

UniProt: Q9FN03 | TAIR/Araport: AT5G63860 | NCBI Taxon: 3702

## Summary of gene function

UVR8 is the plant UV-B photoreceptor. It is a seven-bladed beta-propeller protein
of the RCC1 structural family. In the absence of UV-B it exists as a homodimer.
Specific intrinsic tryptophan residues (principally Trp-285 and Trp-233) act as the
UV-B chromophore; UV-B absorption disrupts the cation-pi/salt-bridge network at the
dimer interface and triggers instantaneous monomerization. The monomer accumulates
in the nucleus, where it binds the E3 ubiquitin ligase COP1 (via the C-terminal C27
region), leading to stabilization of the bZIP transcription factor HY5 and induction
of UV-B photomorphogenesis, acclimation, and UV-protective gene expression
(flavonoid/sinapate biosynthesis, DNA repair, antioxidant genes). The negative
regulators RUP1 and RUP2 (UV-B-induced) bind UVR8 and drive its redimerization,
inactivating signaling. UVR8 also associates with chromatin via histone H2B in the
HY5 promoter region.

## Key structural / functional points

- Seven-bladed beta-propeller; RCC1 sequence/structural homology
  [UniProt Q9FN03: "AltName: Full=RCC1 domain-containing protein UVR8"; 8x RCC1 REPEAT features].
- HOMODIMER in dark/ground state; UV-B drives monomerization
  [PMID:22388820 "UVR8 undergoes an immediate switch from homodimer to monomer, which triggers a signalling pathway for ultraviolet protection"].
- Trp-285 and Trp-233 are the UV-B chromophore
  [PMID:22388820 "Two of these tryptophans, Trp 285 and Trp 233, collectively serve as the ultraviolet-B chromophore"].
- No external cofactor chromophore (tryptophan-based)
  [PMID:22388820 "a symmetric homodimer of seven-bladed β-propeller that is devoid of any external cofactor as the chromophore"].

## RCC1 homology but NOT a functional RanGEF (important caveat)

UVR8 has sequence similarity to human RCC1, a guanine-nucleotide exchange factor
(GEF) for the small GTPase Ran. However, experimentally UVR8 has essentially no Ran
GEF activity and does not function as a RanGEF:
- [PMID:16330762 "UVR8 has sequence similarity to the eukaryotic guanine nucleotide exchange factor RCC1, but we found that it has little exchange activity"].
- [PMID:16330762 "we found that UVR8 had ≈7% of the GEF activity of RCC1 with human Ran as substrate"].
- [PMID:16330762 "UVR8 did not interact with Arabidopsis Ran1 and Ran2 in yeast two-hybrid assays and did not complement the yeast prp20 mutant lacking yeast RCC1"].
- [PMID:16330762 "Together, these observations indicate that UVR8 is unlikely to be a functional homologue of RCC1, and Ran GEF activity is unlikely to be the basis of UVR8 activity"].
- [PMID:19165148 "seems not to interact with Arabidopsis Ran proteins in directed yeast two-hybrid assays nor does it have substantial GEF activity"].

=> The GOA annotation GO:0005085 "guanyl-nucleotide exchange factor activity" (ISS
from PMID:12226503, based purely on RCC1 sequence similarity) is an over-propagated
homology inference that is directly contradicted by experimental data in the SAME
gene's literature. This should be REMOVED.

## Subcellular localization

- Nucleus AND cytosol; UV-B promotes rapid nuclear accumulation
  [PMID:17720867 "UV-B stimulates the nuclear accumulation of both a green fluorescent protein (GFP)-UVR8 fusion and native UVR8"].
- [PMID:17720867 "Nuclear accumulation of UVR8 is specific to UV-B, occurs at low fluence rates, and is observed within 5 min of UV-B exposure"].
- [PMID:16330762 "GFP-UVR8 fluorescence was present in the nucleus but also detectable in the cytosol"].
- UniProt subcellular location: Nucleus; Cytoplasm, cytosol [Q9FN03 SUBCELLULAR LOCATION].
- Nuclear localization necessary but not sufficient for function; UV-B additionally required
  [PMID:17720867 "nuclear localization, although necessary for UVR8 function, is insufficient to cause expression of target genes; UV-B is additionally required to stimulate UVR8 function in the nucleus"].

### Plastid annotation — likely artifact
GO:0009536 "plastid" (HDA, PMID:28887381) comes from a global membrane-associated
protein-oligomerization proteomics survey (protein correlation profiling of
>1350 proteins). This is a high-throughput dataset with known cross-compartment
mixing; UVR8 is consistently characterized as a nucleocytoplasmic protein, and there
is no functional evidence for a plastid role. [PMID:28887381 "Over 150 proteins had a
complicated localization pattern, and were clearly partitioned between cytosolic and
membrane-associated pools."] Treat as over-annotation (not a core/established location).

### Cytosol HDA (PMID:25293756)
GO:0005829 "cytosol" (HDA, PMID:25293756) is from a global cytosolic SEC/MS protein
complex survey of Arabidopsis leaves. Cytosolic localization of UVR8 is independently
well supported (PMID:16330762, PMID:17720867), so this is consistent/corroborating.

## Protein interactions / molecular function

- HOMODIMERIZATION: identical protein binding / homodimerization activity is central
  to the photoreceptor mechanism (ground-state dimer).
  [PMID:22388820 "a symmetric homodimer of seven-bladed β-propeller"];
  [PMID:23277547 "UVR8 monomerization is reversible in vivo, restoring the homodimeric ground state"].
- COP1 interaction (UV-B-dependent), via C-terminal C27 region; initiates signaling.
  [PMID:19165148 "the wild type but not the mutant UVR8 and COP1 proteins directly interact in a UV-B-dependent, rapid manner in planta"].
  [PMID:22988111 "a region of 27 amino acids from the C terminus of UVR8 (C27) mediates the interaction with COP1"];
  [PMID:22988111 "C27 is both necessary and sufficient for the interaction of UVR8 with the WD40 domain of COP1"].
- RUP1/RUP2 interaction (negative feedback, redimerization).
  [PMID:21041653 "REPRESSOR OF UV-B PHOTOMORPHOGENESIS 1 (RUP1) and RUP2, that interact directly with UVR8 as potent repressors of UV-B signaling"];
  [PMID:23277547 "the UVR8-interacting proteins ... RUP1 and RUP2 mediate UVR8 redimerization independently of COP1"].
- Histone H2B / chromatin binding.
  [PMID:16330762 "UVR8 expressed in E. coli bound strongly to a histone-agarose column"];
  [PMID:16330762 "GFP-UVR8 associated with a chromatin fragment containing the HY5 promoter ... but not with control ACTIN2 gene DNA"];
  [PMID:20031919 "UVR8 associates with histones in vivo and competition experiments indicate that the interaction is preferentially with histone H2B"].

Note on "protein binding" (GO:0005515): the IPI annotations from PMID:19165148 and
PMID:21041653 (with COP1 P43254, RUP2 Q9FFA7) and PMID:22988111 (COP1, RUP2, RUP1
Q9LTJ6) capture real, important interactions, but the bare GO:0005515 term is
uninformative per curation guidelines. These interactions are better represented by
the homodimerization MF term and the regulatory BP terms; the underlying COP1/RUP
interactions inform the photomorphogenesis/regulation functions rather than being
core MF in themselves.

## Biological process

- UV-B-specific signaling component orchestrating UV protection.
  [PMID:16330762 "Arabidopsis UV RESISTANCE LOCUS 8 (UVR8) is a UV-B-specific signaling component that orchestrates expression of a range of genes with vital UV-protective functions"].
- Regulates HY5 transcription.
  [PMID:16330762 "UVR8 regulates expression of the transcription factor HY5 specifically when the plant is exposed to UV-B"].
- UV-B photomorphogenesis / acclimation / tolerance.
  [PMID:19165148 "uvr8-null mutants are deficient in UV-B-induced photomorphogenesis and hypersensitive to UV-B stress"].
- uvr8-1 mutant: UV-B hypersensitive, reduced flavonoid/CHS induction.
  [PMID:12226503 "This mutation reduces the UV-B-mediated induction of flavonoids and blocks chalcone synthase mRNA and protein induction"].
- Entrainment of circadian clock by photomorphogenic UV-B requires UVR8.
  [PMID:21395889 "low-intensity UV-B radiation acts as entraining signal for the clock. UV RESISTANCE LOCUS 8 (UVR8) and CONSTITUTIVELY PHOTOMORPHOGENIC 1 (COP1) are required ... for this process"].

## GO term notes
- GO:0009881 "photoreceptor activity" (KW IEA) is the appropriate MF for UVR8; GO
  does not currently provide a dedicated "UV-B photoreceptor activity" MF term.
- GO:0010224 "response to UV-B" (BP) is a child of GO:0009411 "response to UV".
- GO:0042803 "protein homodimerization activity" / GO:0042802 "identical protein
  binding" both correctly capture the ground-state homodimer that is mechanistically
  central to photoreception.

## Action plan (summary)
- GO:0005085 GEF activity (ISS, PMID:12226503): REMOVE — homology-only, experimentally refuted.
- GO:0009536 plastid (HDA, PMID:28887381): MARK_AS_OVER_ANNOTATED — HT proteomics artifact.
- GO:0005515 protein binding x3 (IPI): MARK_AS_OVER_ANNOTATED — uninformative; real but better captured elsewhere.
- GO:0042802 / GO:0042803 (homodimer): ACCEPT (core, photoreceptor mechanism).
- GO:0005634 nucleus (IDA/EXP): ACCEPT; nucleus IEA: ACCEPT-equivalent.
- GO:0005829 cytosol (IDA): ACCEPT; cytosol IEA/HDA: KEEP_AS_NON_CORE.
- GO:0005737 cytoplasm (ISM): KEEP_AS_NON_CORE.
- GO:0000785 chromatin / GO:0003682 chromatin binding (IDA): ACCEPT (H2B-mediated).
- GO:0010224 response to UV-B (IEP) / GO:0009411 response to UV (IMP): ACCEPT/core.
- GO:0009649 entrainment of circadian clock (IMP): KEEP_AS_NON_CORE.
- Add photoreceptor activity (GO:0009881) and regulation of photomorphogenesis to core_functions / proposed.
