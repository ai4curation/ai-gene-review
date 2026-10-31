# Tpm1 (rat, P04692) - manual literature synthesis

Reviewer-written synthesis. No deep-research provider was run (no API keys available in this
environment); this file summarizes cached publications in `publications/` and the curated
UniProt record `Tpm1-uniprot.txt`. Provenance is given inline.

## Gene and isoforms

- Rat Tpm1 encodes alpha-tropomyosin (Tropomyosin alpha-1 chain), a 284-residue parallel
  two-chained coiled-coil protein. [UniProtKB:P04692 "The molecule is in a coiled coil structure
  that is formed by 2 polypeptide chains."]
- The gene produces many isoforms by alternative promoters and alternative splicing: striated
  (skeletal) muscle (displayed isoform), smooth muscle, brain TMBr-1/2/3, and fibroblast TM-2,
  TM-3, TM-5a and TM-5b. [PMID:2022655 "All are derived from the alpha-tropomyosin gene via
  alternative RNA processing and the use of two alternate promoters."] The alternative exons
  change predicted actin affinity [PMID:2022655 "TM-5b is expected to bind actin with greater
  affinity than TM-5a"].

## Molecular function: actin filament binding

- Tropomyosin binds along the actin filament, one dimer spanning several actin subunits;
  deletion of internal periods of rat striated alpha-TM shows four or more periods are needed
  for actin binding [PMID:11329279 "four or more actin periods are required for Tm to bind to
  actin with reasonable affinity"].
- Alanine clusters locally destabilize the coiled coil and are required for normal actin
  affinity [PMID:14640678 "Changing three Ala residues to canonical interface residues,
  A74L-A78V-A81L, greatly stabilized tropomyosin"; "reduced actin affinity >10-fold"].
- Recombinant rat Tpm1 isoforms (smTM, TM2, TM5a, TM1b9a) bind F-actin in cosedimentation
  assays, and the actin C-terminus influences affinity and regulation [PMID:19041430 "The four
  tropomyosin isoforms selected for this study were products of the rat α-TM gene (TPM1)";
  "Tropomyosin binding to actin was studied by a cosedimentation assay"; abstract: "Actin
  proteolytically truncated by three C-terminal amino acids exhibited 1.2-1.5 fold reduced
  affinity for non-muscle and smooth muscle tropomyosin isoforms."]. This paper read in full
  text: all four rat Tpm1 isoforms tested bound actin and regulated actomyosin ATPase in the
  presence of S1; the long isoforms (smTM, TM2) were insensitive to actin C-terminal truncation
  for S1-induced binding, whereas short isoforms (TM5a, TM1b9a) were sensitive.
- UniProt curated function: [UniProtKB:P04692 "Binds to actin filaments in muscle and
  non-muscle cells"].

## Dimerization

- Alpha-Tm forms homodimers and alpha-beta heterodimers with Tpm2; dimer selectivity is
  encoded by alternatively spliced exons [PMID:7568216 "We demonstrate that the information for
  homo- versus heterodimerization is contained within the tropomyosin molecule itself"].
- Recombinant rat alpha2 and alpha-beta skeletal Tm dimers were made and compared
  [PMID:22812662 "associate in vivo to form homo- (α(2)) and heterodimers (α·β)"; "the α·β
  dimers differ in key properties (actin affinity, thermal stability)"].
- Fibroblast isoforms TM5a/5b homodimers: [PMID:16420482 "it has no influence on the
  alpha-helix content of Tm or on the end-to-end interaction between Tm dimers"].

## Striated muscle thin filament regulation

- With troponin, Tm regulates Ca2+-dependent actomyosin interaction [UniProtKB:P04692 "Plays a
  central role, in association with the troponin complex, in the calcium dependent regulation of
  vertebrate striated muscle contraction"].
- The HCM mutation V95A alters thin-filament Ca2+ sensitivity and sliding velocity in vitro
  [PMID:11136687 "The mutation caused a 40% to 50% increase in calcium affinity in regulated thin
  filament-myosin subfragment-1 (S1) MgATPase assays"; "a 5% decrease in unloaded shortening
  velocity in in vitro motility assays"].
- Tropomyosin is among the contractile proteins expressed in engineered neonatal rat cardiac
  constructs [PMID:14551059 "presence of contractile proteins (sarcomeric alpha-actin, troponin
  I, and tropomyosin)"] - this is expression evidence only.

## Pointed-end capping with tropomodulin

- Tmod1 binds the N-terminus of alpha-TM via a disordered N-terminal region and caps pointed
  ends in a Tm-dependent manner [PMID:15475586 "Tropomodulin binds to tropomyosin (TM) and to the
  pointed end of actin filaments"; "Tmod1(1-92) is mainly disordered with only one helical
  region"]; [PMID:15779917 "Tropomodulin together with tropomyosin can cap the pointed, slowly
  polymerizing, filament end"].

## Non-muscle cytoskeleton, stress fibers and motility

- High-molecular-weight Tpm1 isoforms are required for TGF-beta-induced stress fibers; forced
  TPM1 expression restores stress fibers and reduces migration [PMID:15897890 "Forced expression
  of TPM1 by using Tet-Off system increased stress fibers in MDA-MB-231 cells and reduced cell
  migration"]; [PMID:17721995 "Tropomyosin increased cell adhesion to matrix by enhancing actin
  fibers and focal adhesions"]. These are cell-level, largely indirect consequences of
  actin-filament stabilization.
- Alpha-tropomyosin 5b was found in an AQP2-associated actomyosin complex from rat kidney
  papilla [PMID:15823548 "alpha-tropomyosin 5b, annexin A2 and A6"].
- UniProt: [UniProtKB:P04692 "In non-muscle cells is implicated in stabilizing cytoskeleton
  actin filaments"]; [UniProtKB:P04692 "Associates with F-actin stress fibers"].

## Limitations

Most cached papers are abstract-only (only PMID:19041430 and PMID:22812662 have full text).
Mouse/human phenotype-derived ISO annotations (embryonic lethality, heart-rate response,
cardiomyopathy morphology) were not checked against their primary sources.
