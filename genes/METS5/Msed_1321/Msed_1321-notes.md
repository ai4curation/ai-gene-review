# Msed_1321 (A4YGC7) notes

Automated deep research was unavailable for this review. These notes come from my own
reading of the cached full texts (PMID:24532060, PMID:21169482, PMID:32218776), the
UniProt record, the GO term definitions in OLS, and web searches on the clostridial
4-hydroxybutyryl-CoA dehydratase (AbfD). No `-deep-research-*.md` file was created.

## Identity

- 507 aa, unreviewed TrEMBL entry. The submitter named it "Vinylacetyl-CoA
  Delta-isomerase" (EC 5.3.3.3). BRENDA cross-references it under EC 4.2.1.120
  (4-hydroxybutanoyl-CoA dehydratase), and MetaCyc has MONOMER-13736.
- Domains: Pfam HpaB_N (PF11794) and HpaB (PF03241), InterPro IPR004925
  HpaB/PvcC/4-BUDH. This is the 4-hydroxyphenylacetate 3-monooxygenase /
  4-hydroxybutyryl-CoA dehydratase family, which has the acyl-CoA dehydrogenase-like
  fold. PANTHER PTHR36117:SF3.
- UniProt keywords FAD and Flavoprotein (ARBA). No cofactor line.
- Sequence observation from the UniProt file: a CxxxC motif (Cys101, Cys105) and
  His293/Cys299. This fits the kind of cysteine/histidine ligand set expected for the
  [4Fe-4S] cluster of the clostridial enzyme. I did not align it to AbfD here, so treat
  this as unverified.
- Paralog Msed_1220 lacks catalytic residues [PMID:21169482 "one of which (Msed_1220)
  lacks catalytically essential amino acids"].

## Biochemistry (Hawkins et al. 2014, PMID:24532060)

- Recombinant Msed_1321 was produced anaerobically in E. coli and was active
  [PMID:24532060 "This approach resulted in the production of soluble, active enzyme
  that was purified to electrophoretic homogeneity after metal affinity
  chromatography."]
- Homotetramer [PMID:24532060 "this suggests that the enzyme associates as a
  homotetramer"].
- Much less oxygen-sensitive than the clostridial enzyme [PMID:24532060 "With a
  half-life of roughly 4 days, 4-hydroxybutyryl-CoA dehydratase from M. sedula proved
  to be surprisingly robust in the presence of oxygen"].
- Activity assay: a coupled assay. Msed_0406 makes 4HB-CoA, and Msed_0399 (crotonyl-CoA
  hydratase/(S)-3-hydroxybutyryl-CoA dehydrogenase) turns the crotonyl-CoA product
  over with NAD+ [PMID:24532060 "the reaction was initiated by the addition of purified
  4-hydroxybutyryl-CoA dehydratase"]. The readout therefore depends on crotonyl-CoA
  being formed from 4-hydroxybutyryl-CoA, which is the GO:0043721 reaction.
- Kinetics: Km 0.15 mM for 4-hydroxybutyryl-CoA [PMID:24532060 "Msed_1321 on
  4-hydroxybutyryl-CoA, 0.15 mM"], and the rate is low [PMID:24532060 "the dehydration by
  4-hydroxybutyryl-CoA dehydratase, is also low (2.2 μmol min −1 mg −1 )"].
- The four recombinant enzymes (Msed_0406, Msed_1321, Msed_0399, Msed_0656) together
  convert 4HB to acetyl-CoA in vitro [PMID:24532060 "were produced recombinantly in
  Escherichia coli , combined in vitro , and shown to convert 4HB to acetyl-CoA"].
- Strongly induced in autotrophy [PMID:24532060 "4-hydroxybutyryl-CoA dehydratase
  (Msed_1321; 27-fold)"].
- The vinylacetyl-CoA isomerase activity was NOT assayed for Msed_1321 in the cached
  paper.

## Context (Ramos-Vera et al. 2011, PMID:21169482; Liu et al. 2020, PMID:32218776)

- The dehydratase is the key, well-conserved enzyme of the 4HB part of both crenarchaeal
  cycles [PMID:21169482 "4-Hydroxybutyryl-CoA dehydratase, which catalyzes a
  mechanistically intriguing elimination of water, is well conserved and rightly can be
  considered the key enzyme of these two cycles."]
- Msed_1321 was named as the gene behind the high dehydratase activity of autotrophic
  extracts [PMID:21169482 "their genomes contained the corresponding gene (Msed_1321,
  Tneu_0422, and Igni_0595, respectively)"].
- The protein is abundant and slow [PMID:32218776 "Whereas 4-hydroxybutyryl-CoA
  dehydratase appears to constitute a large fraction of cellular protein as well, it
  slowly catalyzes a mechanistically difficult radical reaction"].

## Clostridial paradigm (AbfD)

- Scherf & Buckel 1993, Eur J Biochem 215:421-429. The IUBMB EC 4.2.1.120 entry lists it
  as PMID 8344309. It describes the C. aminobutyricum enzyme as an iron-sulfur and
  FAD-containing 4-hydroxybutyryl-CoA dehydratase/vinylacetyl-CoA delta3-delta2-isomerase.
  NCBI E-utilities were down during this session ("address table is empty"), so I could
  not cache this PMID. It is not cited as a reference in the review.
- Rhea and IUBMB say the clostridial enzyme has an intrinsic vinylacetyl-CoA isomerase
  activity, and that its mechanism probably runs through vinylacetyl-CoA or a shared
  dienoxy intermediate. This comes from web search (IUBMB EC 4.2.1.120, Rhea), not from
  a cached paper.

## Assessment

- GO:0043721 (4-hydroxybutanoyl-CoA = (2E)-butenoyl-CoA + H2O; OLS-verified, under
  hydro-lyase activity) is the core MF. It is supported by experiment on recombinant
  enzyme (PMID:24532060) and missing from GOA, so it is added as NEW (IDA).
- GO:0050393 vinylacetyl-CoA delta-isomerase: this IEA comes from the submitter's EC
  5.3.3.3 name. The activity is plausible because the clostridial homolog has it, but
  it has not been tested for Msed_1321 and it is not the physiological step of the cycle.
  The row is kept as non-core.
- GO:0016627 oxidoreductase acting on CH-CH: an InterPro mapping from the acyl-CoA
  dehydrogenase-like fold superfamilies. The net reaction is a dehydration (lyase), not
  a redox reaction. FAD acts only transiently in the radical mechanism. The row is
  removed.
- Process: NEW GO:0015977 carbon fixation, with the 3HP/4HB cycle proposed term reused
  from Msed_0709.
