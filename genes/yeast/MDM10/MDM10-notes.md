# MDM10 notes (S. cerevisiae, P18409, YAL010C)

## Gene-specific findings
- OM beta-barrel protein: [PMID:8089171 "MDM10 encodes a protein of 56.2 kD located in the mitochondrial outer membrane."]; widespread in OM, not only ERMES foci [PMID:19556461 "with the exception of Mdm10, which displayed a more widespread localization throughout the mitochondrial network"]
- SAM subunit: [PMID:15239954 "We have identified an unexpected subunit of the SAM complex, Mdm10, which is involved in maintenance of mitochondrial morphology."]; [PMID:15239954 "Mitochondria lacking Mdm10 are selectively impaired in the final steps of the assembly pathway of Tom40, including the association of Tom40 with the receptor Tom22 and small Tom proteins, while the biogenesis of porin is not affected."]
- Tom22 integration: [PMID:20026336 "The second large SAM complex, SAM-Mdm10 (mitochondrial distribution and morphology protein), binds the alpha-helical precursor of Tom22 and promotes its membrane integration."]
- Two pools: [PMID:20111053 "Mdm10 is distributed in the TOB complex for beta-barrel protein assembly and in the MMM1 complex for tethering of the endoplasmic reticulum and mitochondria."]; timing of Tom40 release [PMID:20111053 "These results show that Mdm10 regulates the timing of release of unassembled Tom40 from the TOB complex, to facilitate its coordinated assembly into the TOM40 complex."]
- Not detected by CsFiND at contacts: [PMID:37366411 "Among ERMES core components, we could not detect Mdm10 by the LC-MSMS analysis."] (Mdm10 has no MAM IDA row anyway).
- ND molecular_function row REMOVED as superseded by the tether activity IDA row.
- Mitochore model (actin linkage) superseded: [PMID:13679517 "Rather, our interpretation of these observations is that Mmm1p, Mdm10p, and Mdm12p form a complex that is required to link mitochondria to actin cables, the tracks that direct mitochondrial movement from mother cells to developing daughter cells."] -> establishment of mitochondrion
  localization kept as non-core.
- Peroxisome number phenotype: [PMID:30908556 "Finally, we present evidence that the contribution of ERMES subunits Mdm10 and Mdm12 to peroxisome number involves two different mechanisms."] -> non-core.

## Deep research status (2026-10-09)

A first `just deep-research-falcon yeast MDM10 --fallback perplexity-lite` run completed and produced
`MDM10-deep-research-falcon.md` (tool-generated, not edited). A second, duplicate run timed out and its
fallback reported "Provider 'perplexity' not available"; that did not affect the first output. The falcon
report is consistent with this review. Its statements were cross-checked against primary sources:
it describes the 2024 Covill-Cooke bioRxiv preprint (mitochondria-anchored Mmm1 rescues even the quadruple
ERMES deletion); the published version (PMID:42095818) confirms this in its full text, and the abstract's
"provided that Mdm10 is present" refers to native ER-anchored Mmm1 acting with the ChiMERA tether. It also
cites Nguyen et al. 2012 (PMID:22409400, now cached), whose claim that ERMES has no direct role in PS
transport is outweighed by later in vitro and in vivo METALIC data, and whose finding that inheritance
defects are secondary to morphology supports the non-core calls. All quotes used were checked verbatim
against `publications/PMID_*.md`.

## ERMES complex (shared context for MMM1, MDM10, MDM12, MDM34)

- ERMES is an ER-mitochondria tether: [PMID:19556461 "Thus, one core molecular function of the Mmm1/Mdm10/Mdm12/Mdm34 complex is to connect ER and mitochondria, which can be bypassed by expressing a synthetic tether."]
- Composition and topology: [PMID:37366411 "Mmm1 is an ER-resident membrane protein, Mdm10 and Mdm34 are mitochondrial outer membrane (MOM) proteins, and Mdm12 is a soluble subunit"]; Gem1 is a fifth, regulatory subunit [PMID:21945531 "We identified the calcium-binding GTPase Gem1 as a new ERMES subunit, revealing that ERMES is composed of five genuine subunits."]
- Mmm1 is an ER protein, not an outer membrane protein: [PMID:19556461 "indicating that Mmm1 is N-glycosylated and therefore is an integral ER membrane protein that was misannotated as a mitochondrial protein"]
- SMP domains of Mmm1/Mdm12 bind phospholipids and Mdm12 bridges Mmm1 to Mdm34: [PMID:26056272 "Last, we show that the three SMP-containing ERMES subunits form a ternary complex in which Mdm12 bridges Mmm1 to Mdm34."]
- In situ architecture: [PMID:37165187 "Each bridge consists of three synaptotagmin-like mitochondrial lipid binding protein domains oriented in a zig-zag arrangement."]
- Lipid transfer by the Mmm1-Mdm12 unit in vitro: [PMID:29279306 "In contrast, Mdm12 in a complex with Mmm1 mediated efficient lipid transfer between liposomes."]; [PMID:29279306 "This indicates that the lipid transfer activity of the Mmm1s–Mdm12 complex between membranes arises from the cooperation of Mmm1s and Mdm12."]
- PS transport ER-to-mitochondria needs Mmm1, Mdm12, Mdm34: [PMID:27469264 "In the absence of Mmm1, Mdm12 or Mdm34 the PS transport from the ER to mitochondria was significantly impaired"]; PE export does not: [PMID:27469264 "It is thus likely that the PE transport is primarily mediated by uncharacterized factors other than ERMES."]
- In vivo lipid flux: [PMID:35654841 "we show that the ERMES and Vps13-Mcp1 complexes have transport activity in vivo"]
- Native ER-anchored Mmm1 can be the sole transporter (with an artificial tether) if Mdm10 is present; mitochondria-anchored Mmm1 even complements the quadruple deletion [PMID:42095818 "Indeed, Mmm1-mNG-Fis1C could functionally complement the quadruple ERMES deletion mutant"]: [PMID:42095818 "our results suggest that Mmm1 can act as the sole lipid transporter at the ER-mitochondrial contact sites, provided that Mdm10 is present, even in the absence of the other two subunits"]
- Many ERMES phenotypes are secondary: [PMID:26370498 "The fact that it suppresses ERMES mtDNA defects indicates that these are secondary to the loss of a primary ERMES function."]; morphology rescued by synthetic tether [PMID:19556461 "ChiMERA expression also restored the mitochondrial morphology of mdm12Δ and mdm34Δ strains"]
- Evolution (context only, computational): [PMID:42822426 "the endoplasmic reticulum (ER)-mitochondria encounter structure (ERMES) complex from LOCA mitochondria, but human mitochondria lost these pathways"]

## Complex-level curation calls applied consistently

- ERMES complex (GO:0032865), tether activity (GO:0140474), MAM contact site (GO:0044233): ACCEPT for all
  subunits that carry them.
- Phospholipid transport / aminophospholipid transport / intermembrane lipid transfer: ACCEPT. For Mdm10
  (no SMP domain) accepted on the scaffold argument (outer-membrane anchor required even for minimal
  Mmm1-only transfer), but not used as a core MF.
- Lipid transfer activity: core MF only for Mmm1 and Mdm12, as contributes_to phospholipid transfer
  activity (GO:0120014), because efficient transfer needs the Mmm1-Mdm12 complex. Mdm34 lipid binding is
  domain-inferred only; not asserted as core.
- Mitochondrion organization, mitochondrion inheritance, establishment of mitochondrion localization,
  peroxisome organization, phospholipid homeostasis: KEEP_AS_NON_CORE (real mutant phenotypes, largely
  secondary to loss of tethering/lipid supply; not participation).
- Beta-barrel/TOM assembly: ACCEPT for Mdm10 (bona fide SAM-Mdm10 subunit); KEEP_AS_NON_CORE for
  Mmm1/Mdm12 (necessity evidence, Meisinger 2007 abstract-only; possible indirect lipid effect).
- Generic protein binding (GO:0005515) IPI rows: REMOVE (interactions real, captured by complex terms).
- No NEW annotations proposed: candidate terms (e.g. phospholipid binding) are descendants of terms
  the genes already carry.
