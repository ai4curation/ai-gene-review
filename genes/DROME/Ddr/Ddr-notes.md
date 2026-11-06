# Ddr (Drosophila melanogaster, Q59DZ7, FBgn0053531) curation notes

## 2026-11-06 literature search

No deep-research provider was available (no API keys); `just deep-research` was not run.
FlyBase has no hand-written gene description for Ddr, so no `-deep-research-flybase.md`
was produced. Searches done by hand:

- PubMed `Drosophila discoidin domain receptor Ddr` -> 1 hit (PMID:36355066).
- PubMed `(Drosophila OR fly OR insect) AND (discoidin domain receptor OR CG33531)` -> 10
  hits; apart from PMID:36355066 and PMID:37919278, all are about mammalian DDR1/DDR2
  (some expressed in insect cells) or unrelated.
- PubMed `"Ddr"[tiab] AND Drosophila[tiab]` -> 39 hits; all others use "DDR" for the DNA
  damage response.
- PubMed `Ddr Drosophila (olfactory OR axon OR wound OR basement membrane OR collagen)
  receptor tyrosine kinase discoidin` -> only PMID:36355066.
- Web searches for Ddr in olfactory axon targeting, fasciculation, wound healing and
  basement membrane: only the Corty et al. paper, its bioRxiv preprint and the
  InteractiveFly/FlyBase pages that summarise it.

**Leads given to me that I could not verify:** a role of fly Ddr in olfactory receptor
neuron axon targeting or fasciculation, and wound or basement-membrane roles. I found no
publication for either. They are not used in the review.

## What is known

### Glial Ddr in axon ensheathment (Corty et al. 2022, PMID:36355066, full text cached)

- In vivo RNAi screen in peripheral wrapping glia identified Ddr [PMID:36355066 "In an in
  vivo RNA interference screen to identify glial genes required for axon ensheathment, we
  identified the conserved receptor tyrosine kinase Discoidin domain receptor (Ddr)."]
- CRISPR null alleles (frameshifts giving ~150-aa peptides) are viable [PMID:36355066 "Both
  mutant alleles were homozygous viable and viable when placed in trans to large
  deficiencies that uncover the Ddr locus."]
- Two isoforms: a short secreted-like 380-aa form and the 1054-aa full-length receptor
  [PMID:36355066 "Ddr encodes two potential isoforms: a short isoform (380 amino acids) that
  lacks transmembrane and kinase domains, and a full-length isoform that encodes a 1054
  amino acid protein."] Q59DZ7 is the 1054-aa form.
- Loss reduces larval axon ensheathment, rescued by Ddr in wrapping glia [PMID:36355066
  "Similar phenotypes were observed in Ddr loss-of-function animals and could be rescued by
  resupplying Ddr specifically in wrapping glia, confirming the specificity of our RNAi
  results."]
- Adult wing nerve: ensheathment normal, but axon caliber reduced and long-term neuron
  survival reduced [PMID:36355066 "In adult nerves, loss of Ddr decreased long-term
  survival of sensory neurons and significantly reduced axon caliber without overtly
  affecting ensheathment."]; caliber reduction in both mutant and glial RNAi
  [PMID:36355066 "We found that in both glial-specific Ddr knockdown and Ddr whole animal
  mutant nerves the caliber of the dTSM axon was significantly reduced compared with
  controls"]
- Genetic interaction with Multiplexin (type XV/XVIII collagen): dominant, double
  heterozygotes [PMID:36355066 "Although animals that were heterozygous for either gene
  alone did not show defects in wrapping glia morphology, we found that the
  double-heterozygous animals exhibited moderate to severe defects in glial morphology"].
  Authors interpret Mp as a candidate ligand only [PMID:36355066 "the strong genetic
  interaction we observed between Ddr and Mp is consistent with a model in which Mp acts as
  a collagen ligand for Ddr during axonal ensheathment."] No binding or activation assay
  was done; kinase activity of fly Ddr was not tested.
- Ddr acts alongside EGFR and FGFR (Heartless) in ensheathment [PMID:36355066 "Ddr joins
  two other receptor tyrosine kinases – EGFR and FGFR – as important and conserved
  regulators of axon ensheathment"].

### Tau modifier screen (PMID:37919278, full text cached)

Human DDR2 was prioritised in progressive supranuclear palsy, and RNAi of fly orthologues
modified tau neurotoxicity in a fly eye model (GMR-Gal4). This is a disease-model modifier
result; it says nothing about the normal function of Ddr and is not used for annotation.

## Bioinformatics (Ddr-bioinformatics/RESULTS.md)

- Kinase domain: fly Ddr lacks the beta3 lysine (Ala789), catalytic-loop Asn (Ser897) and
  DFG Asp (Ser910); same three losses in D. virilis and Anopheles. Tribolium DDR and
  C. elegans ddr-2 retain all three; the Apis predicted model (A0A7M7MKP6) keeps the catalytic-loop
  Asn and DFG Asp but has Pro674 at the beta3 lysine, and C. elegans ddr-1 keeps only the catalytic-loop Asn (and lacks the HRD Asp). Dipteran Ddr is predicted to be a pseudokinase. This is the
  main finding of the review and drives the kinase-activity decisions.
- DS domain: Trp52/Asp69 of the DDR2 collagen pocket are not conserved in any invertebrate
  DDR (fly His128, Gly146). Insects have no fibrillar collagen; the module already records
  that Drosophila has only Col4a1, viking and Multiplexin.
- UniProt CAUTION for the FA58C ProRule (PRU00081) also flags missing conserved residues
  in the discoidin domain.

## Annotation decisions (summary)

- Plasma membrane (IBA, IEA): ACCEPT. Signal peptide + single TM (Phobius 501-525).
- GO:0038062 PTK collagen receptor activity (IBA, PTN002400507): MODIFY to GO:0004888
  transmembrane signaling receptor activity. The PAINT node is sound for vertebrate DDRs,
  but fly Ddr shows lineage-specific loss of catalytic residues and no collagen-pocket
  conservation; receptor function is supported by architecture plus glial genetics.
- GO:0004672 protein kinase activity (IEA): MARK_AS_OVER_ANNOTATED (pseudokinase
  prediction, untested).
- GO:0005524 ATP binding (IEA): UNDECIDED (glycine loop kept; Lys and DFG Asp lost;
  pseudokinases vary in nucleotide binding).
- GO:0005518 collagen binding (IBA): MARK_AS_OVER_ANNOTATED (no binding data; pocket not
  conserved; Mp interaction genetic only).
- GO:0038063 collagen-activated RTK pathway (IEA from MF): MARK_AS_OVER_ANNOTATED.
- GO:0007169 cell surface RTK signaling pathway (IBA): UNDECIDED.
- GO:0043235 signaling receptor complex (IBA): KEEP_AS_NON_CORE.
- GO:0051897 positive regulation of PI3K/AKT (IBA): MARK_AS_OVER_ANNOTATED.
- NEW: GO:0032285 non-myelinated axon ensheathment (IMP, PMID:36355066) - core.
  Participation: Ddr acts in the wrapping glia that perform the ensheathment (rescue in
  wrapping glia). FlyBase uses GO:0008366 for other glial ensheathment genes (bdl,
  wrapper, fray, Nrg; QuickGO 2026-11-06); GO:0032285 is its more specific child and fits
  non-myelinating wrapping glia. GO:0032294 was avoided because its definition names
  Schwann cells.
- NEW: GO:0031133 regulation of axon diameter (IMP) - non-core, non-cell-autonomous.

## Open questions

- Is fly Ddr catalytically dead? Does it signal through a kinase-active partner (EGFR,
  Htl) as ErbB3-type pseudokinase receptors do?
- Does Multiplexin (or collagen IV) bind the Ddr DS domain? Which surface?
- What does the short 380-aa extracellular isoform do?
