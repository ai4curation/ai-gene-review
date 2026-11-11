# bir-1 (T27F2.3, UniProt G5EFA2): manual literature synthesis

No deep-research provider was available for this session; this summary was written by hand
from the cached publications in `publications/` and the UniProt record. Quotes are verbatim.

## Identity and domain architecture

- 155-residue protein with a single baculoviral IAP repeat (BIR, residues 20-87), the
  zinc-binding fold shared with human Survivin (BIRC5); no RING or CARD domain. UniProt:
  "Belongs to the IAP family."
- One of only two BIR proteins in C. elegans (BIR-1 and BIR-2) [PMID:10209096 "these proteins
  are the only BIRPs in C. elegans"].
- bir-1 lies in an operon with skp-1 (SKIP) [PMID:12682297 "is organized in an operon with the
  transcription cofactor C. elegans SKIP (skp-1)"].

## Chromosomal passenger complex (CPC) subunit

- Four-subunit complex AIR-2 (Aurora B) / ICP-1 (INCENP) / CSC-1 (Borealin-like) / BIR-1
  [PMID:12707312 "These preparations contained approximately equal levels of CSC-1, BIR-1, and
  ICP-1 and slightly more AIR-2"].
- Direct, zinc-dependent binding to CSC-1 [PMID:12707312 "We conclude that the interaction
  between CSC-1 and BIR-1 requires a native, Zn2+-bound BIR domain."]; C83A abolishes binding.
- CSC-1/BIR-1 subcomplex binds ICP-1; AIR-2 binding is indirect via ICP-1
  [PMID:12707312 "Thus, AIR-2 can associate with the CSC-1/BIR-1 subcomplex, but this
  interaction is likely indirect via ICP-1."].
- BIR-1 does not stimulate AIR-2 kinase activity; it is a targeting subunit
  [PMID:12707312 "This activity is not stimulated by CSC-1/BIR-1, suggesting that these two
  subunits function as targeting subunits for AIR-2 kinase."].
- Localization interdependence: "CSC-1, BIR-1, and ICP-1 are interdependent for their
  localization, and all are required for AIR-2 localization." [PMID:12707312];
  "AIR-2 was not present on chromosomes in the absence of BIR-1." [PMID:10983970, abstract].

## Localization

- Chromosomes and spindle midzone [PMID:10983970 "The C. elegans BIRP BIR-1 was localized to
  chromosomes and to the spindle midzone."]. UniProt (from PMID:10983970): on chromosomes in
  prometaphase/metaphase, chromosomes plus midzone in anaphase, midzone only in telophase,
  persists at the cytokinetic remnant; also on polar-body chromosomes.

## Loss-of-function phenotypes (cell division)

- Cytokinesis failure, multinucleate embryos [PMID:10209096 "embryos lacking bir-1 were unable to
  complete cytokinesis and they became multinucleate"].
- Chromosome behaviour, spindle midzone formation and cytokinesis defects, identical to air-2
  [PMID:10983970 abstract]; reduced H3 phosphorylation and HCP-1 (kinetochore) staining.
- Identical phenotypes for CSC-1, AIR-2, ICP-1 and BIR-1 depletion [PMID:12707312].
- Partial rescue by human Survivin [PMID:10209096; PMID:10983970].

## Apoptosis: not supported in C. elegans

- [PMID:10209096 "Overexpression of bir-1 was unable to inhibit developmentally occurring cell
  death in C. elegans and inhibition of bir-1 expression did not increase cell death."] and
  "BIR-1, a C. elegans BIRP, is probably not involved in the general regulation of apoptosis but
  is required for embryonic cytokinesis."

## Post-embryonic phenotypes and transcription (Kostrouchova lab)

- Larval RNAi: egg-laying defect (vulva and egg-laying muscles normal; neuronal cause
  suggested), Dpy, Unc, distal tip cell migration defect, Pvul [PMID:12682297].
- Reduced expression of gfp reporters and endogenous dpy-7 and hlh-1; reduced phosphoacetylated
  histone H3 [PMID:12682297].
- In MCF-7 cells, transfected bir-1 increased basal and T3/THR-induced reporter transcription by
  ~20-50% [PMID:12682297 "The basal transcription increase was ≈20–50%."].
- Collagen genes reduced after bir-1 RNAi and increased on heat-shock overexpression
  [PMID:17116281, abstract only].
- Interpretation: these effects are indirect readouts (heterologous reporter, RNAi phenotypes);
  no DNA-binding or transcription-factor activity has been shown. The link may run through
  CPC-dependent histone H3 S10 phosphorylation, which the authors themselves propose.

## Open questions

- Does BIR-1's BIR domain read histone H3 phospho-Thr3 as human Survivin does, and is that
  how the C. elegans CPC is targeted (holocentric chromosomes; cup-like/ring domains)?
- Is the transcriptional effect a direct function of BIR-1 or an indirect consequence of
  altered H3 phosphorylation / CPC activity in non-dividing cells?
