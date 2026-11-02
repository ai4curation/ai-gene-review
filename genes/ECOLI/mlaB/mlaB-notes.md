# mlaB (P64602, E. coli K-12) review notes

## Deep research

- 2026-10-23: `just deep-research ECOLI mlaB --provider perplexity` was run once and
  failed ("Provider 'perplexity' not available. Available: falcon, openscientist").
  No deep-research file was generated; this review is based on the cached
  publications listed below (full text unless noted) and the UniProt record.

## Identity

- MlaB (YrbB, b3191), 97 aa, a single STAS domain (PROSITE PS50801, Pfam PF13466);
  last gene of the mlaFEDCB operon. Cytoplasmic; no TM helix or signal peptide.
- Binds the side of each MlaF NBD: "MlaB, a STAS domain protein, binds the ABC
  nucleotide binding domain, MlaF, and is required for its stability" [PMID:32602838,
  full text]. The MlaB binding site is ~30 A from the ATP site; MlaB subunits do not
  contact each other and have "presumed minimal contacts" with other transporter
  subunits [PMID:32602838].
- MlaFEDB cryo-EM: "On the cytoplasmic side, each of the MlaF ATPase subunits is bound
  to MlaB" [PMID:33236984]. MlaB does not line the lipid pathway, which runs through
  MlaE and MlaD [PMID:33236984].

## Role in the complex

- Thong et al. 2016 [PMID:27529189, full text]: "MlaB is necessary for both the assembly
  and activity of the ABC transporter, likely by modulating MlaF structure and
  stability". Without MlaB, MlaFE could not be isolated. MlaB T52A does not affect
  MlaFEB assembly but abolishes ATPase activity, and mlaB T52A does not complement
  SDS-EDTA sensitivity.
- Kolich et al. 2020 [PMID:32602838]: MlaF cannot be expressed/purified alone, but
  MlaFB co-expression gives good yield; "These data suggest that MlaB stabilizes MlaF".
  MlaF over-expression fully suppresses the mlaB knockout: "MlaB may have no essential
  function in Mla lipid transport apart from its role in promoting MlaF stability
  and/or association with the MlaFEDB complex". Thr52 lies at the MlaF-MlaB interface
  and is the conserved Ser/Thr phosphorylation site of STAS domains; phosphoregulation
  is hypothesized, not shown.
- Interpretation: MlaB is a stoichiometric, non-catalytic accessory subunit. Its
  documented activity is binding and stabilizing MlaF (GO:0050821 protein
  stabilization, process), enabling MlaFB to assemble with MlaED. It does not contact
  phospholipid, so "enables phospholipid transfer activity" overstates it; at most it
  contributes to the complex activity. GO lacks a specific MF term for "ABC ATPase
  subunit stabilizer"; no MF is asserted with `enables` in core_functions.

## Stress phenotypes (PMID:20128927, full text)

- Tn5 screen for hyperlethality to nalidixic acid; yrbB::Tn5 was among 14 hits, also
  more readily killed by mitomycin C, UV and H2O2; complementation was observed for
  tested mutants including yrbB. The authors note the yrbB mutation does not change
  bacteriostatic susceptibility or permeability to most compounds. These are indirect,
  envelope-related phenotypes; nothing places MlaB in a DNA-damage response pathway.
- PAINT PTN002185077 (PTHR35849, taxon Gammaproteobacteria) propagates
  GO:0006974 DNA damage response, GO:0120014, GO:0120010 and GO:1990531, all seeded
  solely by P64602 itself (interpro/panther/PTHR35849/PTHR35849-paint.tsv).

## Location

- UniProt: "Cytoplasm" (ECO:0000305 PMID:19383799). EcoCyc IDA cytosol from proteomics
  PMID:18304323 (full text; MlaB not found in cached text, presumably in supplementary
  tables) and PMID:17309111 (abstract only). Functional location is the cytoplasmic face
  of the IM, bound to MlaF in MlaFEDB.

## Reference issues

- PMID:29358647 (TatA-type Tat translocase paper) is the ComplexPortal NAS reference for
  "membrane"; full text has no mention of Mla genes - miscited.
- GO:1990531 is defined as a P-type ATPase (P4 flippase) complex; MlaFEDB is an ABC
  transporter: GO:0043190 is the correct complex term.
