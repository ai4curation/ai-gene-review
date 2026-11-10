# Mhc (Drosophila melanogaster) - manual literature review

No deep-research API provider was available for this review. This file summarises
literature read directly from the cached publications in `publications/` (full text where
noted) and the UniProt record P05661 (MYSA_DROME).

## Gene and protein

- Mhc is the single-copy muscle myosin II heavy chain gene of *D. melanogaster*. UniProt
  P05661 is a 1962-aa class II myosin with an N-terminal SH3-like domain, a myosin motor
  domain (86..777) with a P-loop ATP-binding site (179..186), an IQ motif and a long
  coiled-coil rod (802..1927) [file:DROME/Mhc/Mhc-uniprot.txt "Belongs to the TRAFAC class
  myosin-kinesin ATPase superfamily. Myosin family."].
- Muscle myosin is a hexamer of two heavy chains plus two essential and two regulatory light
  chains [file:DROME/Mhc/Mhc-uniprot.txt "Muscle myosin is a hexameric protein that consists
  of 2 heavy chain subunits (MHC), 2 alkali light chain subunits (MLC) and 2 regulatory light
  chain subunits (MLC-2)."].
- Isoform diversity arises from mutually exclusive exons (3, 7, 9, 11, 15) and exon 18
  inclusion; these map to the ATP pocket, relay, actin interface, S2 hinge and tail
  [file:DROME/Mhc/Mhc-uniprot.txt "Exon 3 encodes the hydrophobic pocket adjacent to the
  ATP-binding site"].
- An internal promoter produces myosin rod protein (MRP), which has the MHC rod but 77
  unique N-terminal residues instead of the motor [PMID:8995523 "Myosin rod protein (MRP), a
  155 kDa protein encoded by a gene internal to the Drosophila muscle myosin heavy chain (Mhc)
  gene"].

## Molecular function: actin-based motor (ATPase)

- MHC is the motor of muscle thick filaments [PMID:8887536 "Myosin heavy chain (MHC) is the
  motor protein of muscle thick filaments."; PMID:15051736 "The Myosin heavy chain (Mhc) locus
  encodes the muscle-specific motor mediating contraction in Drosophila."].
- Purified IFM myosin from transgenic flies shows actin-activated MgATPase and drives actin
  sliding in motility assays; variable exons tune the kinetics [PMID:16154586 "in vitro
  experiments show the exon 7 domain modulates myosin ATPase activity but has no effect on
  actin filament velocity"; PMID:18462751 relay-domain chimeras: "a 50% reduction in
  actin-activated ATPase activity, a significant increase in actin affinity, abolition of
  actin sliding"].
- IBM-3 E701K (human E706K) depresses ATPase, actin affinity and motility [PMID:22496423
  "These results confirm that the IBM-3 mutation induces poor ATPase activity, weak actin
  affinity, and significant reduction in catalytic efficiency in a fast skeletal myosin
  isoform."].
- Transducer mutants (A261T, G200D) have opposite effects on S1 ATPase and ADP/actin
  affinities and cause dilated vs restrictive cardiomyopathy-like phenotypes (full text)
  [PMID:21680742 "the two point mutations have an opposite effect on the enzymatic activity
  of S1"].
- Dominant Samba alleles with point mutations in the ATP binding/hydrolysis region cause
  hypercontraction myopathy (full text) [PMID:15051736 "These mutants are caused by single
  point mutations in the ATP binding/hydrolysis domain of Mhc and lead to degeneration of
  the flight muscles."].

## Structure: thick filament backbone

- MHC/MRP rods polymerise into thick filaments in the A band; MRP is a homodimer that
  co-integrates with MHC [PMID:8995523 "co-localize the protein with MHC to the sarcomeric
  A-band in immunostained muscles"; "indicate that native MRP is a homodimer"].
- Rod (LMM) mutations from myosin storage myopathy reduce filament assembly in vitro
  (full text) [PMID:28973424 "In vitro assembly assays demonstrated a decreased ability of
  mutant myosin to polymerize, with L1793P filaments exhibiting shorter lengths."].
- Thick filaments formed from MRP alone in Mhc-null embryos still assemble into sarcomeres
  [PMID:12927543 "Embryos that express MRP in the absence of MHC form thick filaments that
  participate in the assembly of sarcomeres"].

## Myofibril assembly and maintenance

- Myosin is not required for myoblast fusion or fibre morphogenesis, but is for
  myofibrillogenesis [PMID:15075240 "neither sarcomeric myosin nor actin are required for
  myoblast fusion or the subsequent morphogenesis of muscle fibres"].
- MHC isoform identity does not dictate myofibril architecture but is required for function
  and stability [PMID:8887536 "Our data show that the proper MHC isoform is critical for
  specialized muscle function and myofibril stability."].
- Adult knockdown (RNAi) lengthens sarcomeres and thin filaments without destroying
  architecture (full text) [PMID:24915196 "The abnormal thin filament lengths we observed in
  the Mhc knockdown flies suggest that the role of myosin in determining thin filament length
  is as important during muscle maintenance as it is in muscle development."].

## Non-muscle roles

- MARCM clones of Mhc3 are defective in tracheal air-sac cell migration; border-cell
  migration is also impaired in Mhc3 (full text) [PMID:17603108 "These results suggest that
  Mhc is indeed required for tracheal cell migration in the air sac primordium."; "Moreover,
  border cell migration is impaired in the Mhc 3 allele"].
- Slbo-dependent induction of "muscle-specific" genes in border cells [PMID:16580994
  "Actin cytoskeleton regulators were also induced, including, surprisingly, a large cluster
  of \"muscle-specific\" genes."].

## Not supported / uncertain

- Polytene chromosome puff (PMID:10471711): abstract-only; abstract concerns an EMS screen and
  states that mutants near Mhc are in other loci. No basis visible for a puff localization.
- Muscle cell differentiation (PMID:16297904): Mhc expression is reduced in CanB2 mutants;
  Mhc is an output of differentiation, not a driver.
