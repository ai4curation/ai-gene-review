# icp-1 (Y39G10AR.13; UniProt G5EE37) - manual literature research

No deep-research API was available for this review. This summary was compiled by hand
from the cached publications in `publications/` and the UniProt record. Every claim
carries its source.

## Identity

- ICP-1 ("Incenp-like protein") is the *C. elegans* orthologue of INCENP, the scaffold
  subunit of the chromosomal passenger complex (CPC). The UniProt entry G5EE37 is an
  unreviewed TrEMBL entry, 622 aa, with a C-terminal Pfam INCENP_ARK-bind domain
  (PF03941, residues 530-587) and long disordered regions in the N-terminal two thirds
  [file:worm/icp-1/icp-1-uniprot.txt].
- ICP-1 and ICP-2 were identified by homology of their carboxyl termini to vertebrate
  Incenp [PMID:11050385 "We identified two Caenorhabditis elegans proteins, ICP-1 and
  ICP-2, with significant homology in their carboxyl termini to the corresponding region
  of vertebrate Incenp."].

## Complex membership and molecular function

- ICP-1 binds AIR-2 (Aurora B) in vitro [PMID:11050385 "ICP-1 bound C. elegans AIR-2
  in vitro"]. The C-terminal conserved domain is sufficient [PMID:12707312 "Our previous
  studies showed that the COOH-terminal conserved domain of ICP-1 is sufficient to bind
  to AIR-2 (Kaitna et al., 2000)."].
- ICP-1 bridges AIR-2 to the CSC-1/BIR-1 (Borealin/Survivin-like) targeting subcomplex
  [PMID:12707312 "Thus, AIR-2 can associate with the CSC-1/BIR-1 subcomplex, but this
  interaction is likely indirect via ICP-1."]; the four-subunit complex can be
  reconstituted in vitro [PMID:12707312].
- ICP-1 stimulates AIR-2 kinase activity [PMID:12707312 "ICP-1 dramatically stimulates
  AIR-2 kinase activity."; "ICP-1 is required for AIR-2 activity, and CSC-1 and BIR-1 do
  not enhance the MBP phosphorylation."]. This was confirmed with GST fusions, where
  ICP-1 is itself phosphorylated by AIR-2 [PMID:15548597 "When GST-ICP-1 was added to the
  AIR-2/BMK-1 kinase assay, GST-ICP-1 was phosphorylated, and GST-AIR-2
  autophosphorylation and GST-BMK-1 phosphorylation were increased"].
- TLK-1 stimulation of AIR-2 depends on ICP-1 [PMID:15916946 "Phosphorylated TLK-1
  increases AIR-2 kinase activity in a manner that is independent of TLK-1 kinase activity
  but depends on the presence of ICP-1/INCENP."] (abstract only).

## Localization

- Chromosomes in prophase nuclei, a stripe between the two kinetochore plates at
  prometaphase, and the interzonal (midzone) microtubules in anaphase [PMID:11402065
  "At prometaphase, CeINCENP is in a single stripe coincident with the chromosome between
  the two kinetochore plates"; "During anaphase and telophase, CeINCENP remains associated
  with the chromosomes, but is also present on the interzonal MTs"].
- Localization is interdependent with CSC-1 and BIR-1 and independent of AIR-2; AIR-2
  requires ICP-1 to localize [PMID:12707312 "Thus, CSC-1, BIR-1, and ICP-1 are mutually
  interdependent, but AIR-2 independent, for their localization to chromosomes."].
- Chromosomal targeting of ICP-1 is independent of kinetochore assembly (CENP-A)
  [PMID:11402065 "Thus, we conclude that kinetochore assembly and chromosomal targeting of
  CeINCENP are independent processes."].

## Loss-of-function phenotypes (RNAi)

- Female meiosis fails [PMID:11402065 "In CeINCENP-depleted embryos, meiotic divisions of
  the oocyte nucleus completely fail"].
- Mitotic chromosomes congress poorly and segregate with lagging chromatin
  [PMID:11402065 "However, they have difficulty congressing and fail to form a tight
  metaphase plate."; "This segregation is not normal and leading and lagging chromatin is
  always observed."]. Note that paternal chromosomes are still pulled apart into two
  masses, so sister separation per se occurs.
- Spindle assembly is normal until mid-anaphase; the spindle midzone fails to form
  [PMID:11402065 "Qualitatively, spindle assembly and structure appeared normal until
  midanaphase"; "Spindle midzone MTs that form between the separating chromosomes during
  anaphase and telophase are absent"].
- Cytokinesis initiates but fails [PMID:11402065 "Cytokinesis initiates normally in
  CeINCENP-depleted embryos, but it does not complete and the furrow regresses."].
- ICP-1 promotes stable ZEN-4 (centralspindlin) localization [PMID:11050385 "ICP-1
  promoted the stable localization of ZEN-4 (also known as CeMKLP1), a kinesin-like
  protein required for central spindle assembly."].
- ICP-1 is needed for BMK-1 (kinesin-5) spindle localization, via AIR-2 [PMID:15548597].

## Gaps

- No ICP-1-specific evidence for spindle assembly checkpoint function was found in the
  cached literature; the ComplexPortal NAS rows for that and for sister chromatid
  separation rest on generic CPC knowledge.
- The kinetochore IDA (PMID:15331665) could not be checked: only the abstract (about
  LIS-1) is cached.
