# mlaF (P63386, E. coli K-12) review notes

## Deep research

- 2026-10-23: `just deep-research ECOLI mlaF --provider perplexity` was run once and
  failed ("Provider 'perplexity' not available. Available: falcon, openscientist").
  No deep-research file was generated; this review is based on the cached
  publications listed below (full text unless noted) and the UniProt record.

## Identity and architecture

- MlaF (YrbF, b3195) is the 269-residue ABC nucleotide-binding domain (NBD) subunit of
  the inner-membrane MlaFEDB complex of the Mla (maintenance of lipid asymmetry)
  pathway. UniProt: "Belongs to the ABC transporter superfamily. MlaF family."
- Complex stoichiometry MlaF2 E2 D6 B2 [UniProt SUBUNIT, ECO:0000269 PMID:27529189,
  PMID:28388411]. MlaF is peripheral on the cytoplasmic face of the IM: MlaFB is "the
  cytoplasmic portion of the larger MlaFEDB ABC transporter complex" [PMID:32602838].
- Each MlaF binds one MlaB (STAS domain) on the helical subdomain of the NBD, ~30 A from
  the ATP site [PMID:32602838 "The MlaB binding site on MlaF is centered on the helical
  subdomain of the core NBD in MlaF, distant from the MlaF2 dimer interface and the ATP
  binding sites"].
- A unique C-terminal extension (CTE) of MlaF reaches over to the neighbouring MlaFB
  module ("handshake") and is required for function; forced dimerization largely rescues
  the CTE deletion [PMID:32602838].
- MlaF is unstable without MlaB: "we were unable to express and purify significant
  amounts of MlaF alone" and over-expression of MlaF suppresses the mlaB knockout
  [PMID:32602838].

## ATP hydrolysis (verification of the IMP row, PMID:27529189, full text)

- Purified MlaFEB in DDM: kcat 1.8 umol ATP/s/umol complex; MlaD association lowers it ~3x
  [PMID:27529189].
- "Remarkably, no activity is detected with the MlaFEBT52A complex, similar to a variant
  of the complex containing a predicted non-functional mutation in the MlaF Walker A
  motif (MlaFK47REB)" and "the mlaBT52A or mlaFK47R alleles do not complement SDS-EDTA
  sensitivity" [PMID:27529189]. So the IMP rests on the K47R Walker A mutant abolishing
  complex ATPase activity: sound support for MlaF as the catalytic ATPase.
- ATP drives the retrograde direction: "ATP hydrolysis drives overall transport in the
  retrograde direction" and anterograde transfer "is abolished by ATP hydrolysis"
  [PMID:34873038]. Transport direction is still debated in the field; the module
  deliberately stays direction-neutral.

## Process and complex terms

- Mla pathway prevents PL accumulation in the outer leaflet of the OM [PMID:19383799,
  abstract only]; mla mutants are SDS-EDTA sensitive [UniProt DISRUPTION PHENOTYPE].
- Proteoliposome transport system with MlaFEDB, MlaC and MlaA-OmpF [PMID:33199922,
  abstract only] - basis for EcoCyc IDA rows (GO:0120010, GO:0120014).
- GO:1990531 "phospholipid-translocating ATPase complex" is defined as "A protein complex
  that functions as a phospholipid-translocating P-Type ATPase" (synonyms P4-ATPase
  complex, DRS2-CDC50 complex) and is_a transporter complex only; MlaFEDB is an ABC
  transporter, so GO:0043190 ATP-binding cassette (ABC) transporter complex is the
  correct complex term (checked with runoak against sqlite:obo:go).
- GO:0120014 phospholipid transfer activity is defined as carrying a PL through the
  aqueous phase in a hydrophobic pocket; for MlaFEDB it is the complex-level activity
  used in the Mla module. MlaF itself contacts no lipid; it contributes the ATPase
  that drives the transfer, so the honest framing is MlaF enables GO:0016887 and
  contributes_to GO:0120014.

## Reference issues

- PMID:29358647 (TatA-type Tat translocase components) is cited by ComplexPortal for
  "membrane" (NAS). Full text contains no mention of Mla/MlaF/yrb genes (grep), so it is
  miscited; the location itself (IM, cytoplasmic face) is correct.
- PMID:15690043, PMID:16606699 (high-throughput pull-downs; GroEL interactor) are
  abstract-only; GroEL binding is a generic folding interaction, rows REMOVEd under the
  protein-binding policy.

## PAINT

- PTN000655692 (PTHR43023): IBD GO:0016887 seeded by AT1G65410 (TGD3) and P63386;
  GO:0120014 seeded by P63386.
- PTN000655704 (taxon Bacteria): GO:1990531, GO:0120010 seeded by P63386.
  (interpro/panther/PTHR43023/PTHR43023-paint.tsv)
