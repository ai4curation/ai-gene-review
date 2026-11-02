# CSN3 (Bos taurus, kappa-casein, P02668) - curation notes

## Identity and family
- Secreted, signal 1-21, mature 22-190; O-glycosylated C-terminal (caseinomacropeptide) region; chymosin
  cleavage site Phe105-Met106 (mature numbering) [file:BOVIN/CSN3/CSN3-uniprot.txt "Cleavage; by chymosin/rennin"].
- Disulfide-linked homomultimers [file:BOVIN/CSN3/CSN3-uniprot.txt "Monomer or homomultimer; disulfide-linked."].
- Ca-insensitive casein, descended from FDCSP-like SCPP ancestor [PMID:21245413 "the five exons of the Ca-insensitive casein gene are all reminiscent of FDCSP"].

## Core biology
- Micelle stabilization: [file:BOVIN/CSN3/CSN3-uniprot.txt "Kappa-casein stabilizes micelle formation, preventing casein precipitation in milk."]
  [PMID:21245413 "Ca-insensitive casein (κ-casein) does not usually interact with Ca but instead stabilizes the micelle"].
- Knockout: [PMID:16698927 "these females did not suckle
  their pups and failed to lactate because of destabilization of the micelles in
  the lumina of the mammary gland."] => kappa-casein essential for lactation.
- Binds t-PA in milk micelles [PMID:8186264 "multimeric forms of kappa-casein and dimeric alpha s2-casein were
  identified as t-PA binding components."].
- RCM-kappa-casein forms amyloid fibrils in vitro (PMID:19754881) - non-native chemically modified form.

## Annotation themes
- protein binding IPI with T. thermophilus ClpB (PMID:22348341): casein as model chaperone substrate -> REMOVE.
- Steroid response terms (PMID:3585228) -> MARK_AS_OVER_ANNOTATED (expression effect on total casein).
- protein stabilization IBA -> accept as closest process describing micelle stabilization.
- Bioactive peptides (casoxins, casoplatelin, glycomacropeptide) not annotated in GOA; not added (digestion products).

## Deep research
- OpenScientist deep research was not yet available when this review was completed; review based on primary literature, UniProt and cached publications.

## Deep research integration (OpenScientist, 2026-10-24)

The report's cited PMIDs were fetched into publications/ and the points used were checked
against the abstracts.

- No contradiction with the review. The report gives micelle surface (colloidal)
  stabilization as the primary function, matching the core GO:0140777 (family convention
  for kappa-casein), extracellular location and lactation.
- One error in the report, not adopted: its summary calls the alpha-s/beta-casein assembly
  "calcium-insensitive"; those caseins are calcium-sensitive (PMID:21245413), and it is
  kappa-casein that is calcium-insensitive.
- Added to GO:0140777 (NEW): PMID:41865247 (kappa-casein stabilizes micelles in milk but
  fibrillates under destabilizing conditions), PMID:22177076 (chymosin cleavage at
  Phe105-Met106 releases glycomacropeptide and leaves para-kappa-casein on the surface,
  backing the reason's statement), and a quote from the report.
- Not used: chymosin cleavage as a GO term for CSN3 (kappa-casein is the substrate; the
  activity belongs to chymosin), glycomacropeptide, casoxin and casoplatelin peptide
  activities, A/B variant cheese-making associations, JAK2-STAT5/mTOR expression control.
- No action changes.
- Also added PMID:41200845 (kappa-casein inhibits calcium-induced amorphous aggregation of beta-casein in vitro, found via the rat Csn3 report) to GO:0140777 and the IBA protein stabilization row, as direct biochemical support for the stabilizing activity.
