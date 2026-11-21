# SLC6A1 (GAT-1 / GABA transporter 1) — curation notes

UniProt: P30531 (SC6A1_HUMAN). HGNC:11042. Gene synonyms GAT1, GABATR, GABT1.
Taxon: Homo sapiens (NCBITaxon:9606). 599 aa, 12 TM helices, PDZ-binding C-terminus.
Review batch: canonical-surfaceome backfill, batch 9.

## Identity and family

- First cloned from human brain by Nelson et al. 1990 [PMID:2387399 "A cDNA clone encoding a
  transporter for the neurotransmitter gamma-aminobutyric acid in human brain was cloned and
  sequenced"], encoding a "hydrophobic protein of 599 amino acids" whose
  "Hydropathy analysis revealed twelve potential transmembrane segments" [PMID:2387399].
- SLC6/NSS family. UniProt: [file:human/SLC6A1/SLC6A1-uniprot.txt "Belongs to the
  sodium:neurotransmitter symporter (SNF)" ... "(TC 2.A.22) family. SLC6A1 subfamily"].
  TCDB 2.A.22.3.2 (neurotransmitter:sodium symporter, NSS). Pfam PF00209 (SNF), InterPro
  IPR002980 (Na/ntran_symport_GABA_GAT1), PANTHER PTHR11616:SF138. This is a secondary-active
  symporter, NOT an antiporter, NOT a facilitative uniporter, and NOT a heteromeric transporter
  (no SLC3 heavy chain; the only functionally relevant partner is the scaffold PALS1, below).

## Core molecular function: GABA:Na+:Cl- symport

- UniProt CC:FUNCTION: [file:human/SLC6A1/SLC6A1-uniprot.txt "Mediates transport of
  gamma-aminobutyric acid (GABA) together" with sodium and chloride and is responsible for the
  reuptake of GABA from the synapse (PubMed:30132828)]. Transport is electrogenic and reversible;
  direction set by membrane potential and the Na+/Cl-/GABA gradients.
- Curated catalytic reaction (Rhea RHEA:70687), left-to-right = uptake:
  [file:human/SLC6A1/SLC6A1-uniprot.txt "4-aminobutanoate(out) + chloride(out) + 2 Na(+)(out)"
  = 4-aminobutanoate(in) + chloride(in) + 2 Na(+)(in)]. ChEBI xrefs: 4-aminobutanoate
  (GABA) = CHEBI:59888, chloride = CHEBI:17996, Na+ = CHEBI:29101. A minor hypotaurine
  reaction (RHEA:71243) is recorded By similarity only.
- Stoichiometry directly measured in oocytes by Loo et al. 2000: [PMID:10973981 "the GAT1
  stoichiometry was 2Na(+):1GABA"], and [PMID:10973981 "Cl(-) was transported by GAT1"] with
  [PMID:10973981 "suggesting unidirectional influx of 2Na(+):1Cl(-):1GABA per transport cycle"].
  So the GAT1 cycle moves 2 Na+ : 1 Cl- : 1 GABA, net +2 charge inward — electrogenic. This IDA
  grounds GO:0005332 (GABA:Na:Cl symporter activity) directly on the human protein.
- Disease/functional confirmation: Mattison et al. 2018 screened epilepsy patients; [PMID:30132828
  "the seven identified exonic variants were found to reduce GABA transport activity"] and
  [PMID:30132828 "reduced GAT-1 function is a common consequence of epilepsy-causing SLC6A1
  variants"]. Loss-of-function → myoclonic-atonic epilepsy (MAE, MIM:616421), confirming the
  GABA-reuptake function is the disease-relevant activity (IMP grounding of GO:0005332).

### GO term granularity (MF)

OLS-verified: GO:0005332 (gamma-aminobutyric acid:sodium:chloride symporter activity) has as
is_a ANCESTORS all of: GO:0015185 (GABA transmembrane transporter activity), GO:0005283 (amino
acid:sodium symporter activity), GO:0015370 (solute:sodium symporter activity), GO:0015378
(sodium:chloride symporter activity). Therefore GO:0005332 is the single strictly-asserted, most
specific MF; the four ancestors are TOO_GENERAL once GO:0005332 is ACCEPTed (judging the term,
not the evidence code — this applies even to the IDA on GO:0015378). GO:0015370 additionally
rests only on an ARBA rule.

## Biological process / transport steps

- Physiological role = GABA reuptake from the synaptic cleft into presynaptic terminals (and
  astrocytes), terminating GABAergic signalling. GAT1 performs the transport steps itself, so the
  transport-process terms are participation, not mere necessity.
- GABA reuptake (GO:0051936) and GABA import (GO:0051939) are the specific accepted processes.
  OLS: GO:0051936 is_a GO:0051933 (amino acid neurotransmitter reuptake) is_a GO:0098810
  (neurotransmitter reuptake) is_a ... is_a GO:0006836 (neurotransmitter transport); and
  GO:0051936/GO:0051939 are both is_a descendants of GO:0006865 (amino acid transport). So
  GO:0098810, GO:0006836 and GO:0006865 are TOO_GENERAL (specific GABA terms entail them).
- GO:0003333 (amino acid transmembrane transport): OLS shows GABA import/reuptake are NOT in its
  is_a subtree (they sit under amino acid transport, not under amino acid *transmembrane*
  transport). It is correct but non-specific; refined (MODIFY) to the GABA-specific process the
  gene already carries (GO:0051939), a substrate-narrowing lateral correction.
- Co-transported ions (Na+, Cl-) are genuinely translocated as part of the symport cycle (Loo
  et al., above), so the ion rows are not wrong, but they are ancillary coupling steps, not the
  gene's purpose → KEEP_AS_NON_CORE: GO:0098719 (Na+ import across PM, IDA), GO:0098658 (inorganic
  anion import across PM, IDA = Cl-), GO:1902476 (chloride transmembrane transport, IDA),
  GO:0035725 (Na+ transmembrane transport, IBA).

## Localization

- Plasma membrane is the molecular location (multi-pass, 12 TM). UniProt CC:SUBCELLULAR
  LOCATION: Cell membrane; [file:human/SLC6A1/SLC6A1-uniprot.txt "Note=Localized at the
  presynaptic"] terminals of interneurons (Presynapse). IDA plasma-membrane localization on the
  human protein in Loo et al. (is_active_in). → GO:0005886 ACCEPT (core); GO:0016020 membrane
  MODIFY→GO:0005886.
- Synaptic/neuronal context terms: GO:0098793 presynapse and GO:0098982 GABA-ergic synapse are
  the functional sites of reuptake → ACCEPT. GO:0030424 axon, GO:0043025 neuronal cell body are
  real but peripheral subcellular locations → KEEP_AS_NON_CORE. GO:0009986 cell surface (IBA) is
  a weaker synonym for the plasma-membrane location → KEEP_AS_NON_CORE.

## Interactions

- The functionally meaningful partner is the MPP5/PALS1 scaffold: [file:human/SLC6A1/SLC6A1-uniprot.txt
  "Interacts (via PDZ domain-binding motif) with PALS1"]; [file:human/SLC6A1/SLC6A1-uniprot.txt
  "interaction increases SLC6A1-mediated GABA uptake"] (By similarity; PDZ-binding motif at aa
  597-599). The single bare protein-binding GOA row is instead an IntAct high-throughput hit with
  HSF2BP (O75031) from the binary-interactome screen [PMID:32296183] — uninformative; REMOVE per
  the protein-binding policy. PALS1 is noted here, not asserted as a GOA row.

## Rows requiring the participation test (CLAUDE.md "do not add / do not over-keep")

GAT1 performs GABA reuptake. It does not itself execute memory, learning, or synapse assembly;
those are distal organismal consequences of altered GABAergic tone, transferred by ISS from mouse
(P31648) with the acts_upstream_of qualifier. The gene product performs no step of these
processes → MARK_AS_OVER_ANNOTATED: GO:0007613 memory, GO:0008306 associative learning,
GO:0050808 synapse organization. Chemical synaptic transmission (GO:0007268, TAS) is different:
reuptake is a bona fide part of the GABAergic transmission cycle (it terminates signalling), so
that one is defensible as KEEP_AS_NON_CORE (involved_in), though its provenance is a
chromosome-mapping paper (PMID:8530094).

## Blood-brain barrier row (scrutinized)

GO:0150104 transport across blood-brain barrier (NAS, PMID:30280653) cites a general BBB review
(Sweeney et al. 2019), not any GAT1-specific datum. The BBB permeability barrier is formed by
brain endothelial cells; GAT1/SLC6A1 is a neuronal/astrocytic presynaptic GABA transporter and is
not an established BBB-endothelial GABA carrier. The NAS over-reaches from a review that does not
demonstrate GAT1 performing transport across the BBB → MARK_AS_OVER_ANNOTATED.

## Summary of decisions

- Core MF: GO:0005332 (GABA:Na+:Cl- symporter activity); core processes GABA reuptake / GABA
  import across the presynaptic plasma membrane; core locations plasma membrane + presynapse.
- No proposed_new_terms (existing ontology covers the function well).
- No source_defects identified (UniProt and GOA are internally consistent for this entry).
