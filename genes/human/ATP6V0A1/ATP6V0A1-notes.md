# ATP6V0A1 notes

## 2026-06-03 - Proteostasis PN review

Deep research status: Falcon deep research has now completed successfully
(`ATP6V0A1-deep-research-falcon.md`, 27 citations); see the synthesis section at
the end of this file. The original PN-batch attempt timed out before the
`deep_research_unified` tool bugs were fixed. This review uses that report
together with fetched UniProt, GOA, cached publications, Reactome records,
Panther family data, and the PN projection reports.

Core biology: ATP6V0A1 encodes the a1 subunit of the V0 membrane sector of
V-ATPase. UniProt describes it as a "Subunit of the V0 complex of
vacuolar(H+)-ATPase" and says V-ATPase acidifies "lysosomes, endosomes, the
trans-Golgi network, and secretory granules, including synaptic vesicles"
[file:human/ATP6V0A1/ATP6V0A1-uniprot.txt, "Subunit of the V0 complex of
vacuolar(H+)-ATPase"; file:human/ATP6V0A1/ATP6V0A1-uniprot.txt,
"acidification of various organelles, such as lysosomes, endosomes"]. The human
V-ATPase structure paper frames V-ATPases as "ATP hydrolysis-driven proton
pumps" and says organellar V-ATPases maintain "pH homeostasis of endosomes and
lysosomes" [PMID:33065002, "ATP hydrolysis-driven proton pumps that acidify
intracellular vesicles"; PMID:33065002, "pH homeostasis of endosomes and
lysosomes"].

ATP6V0A1-specific disease/function papers support the same function. Aoto et
al. show that ATP6V0A1 missense variants impair lysosomal acidification in cell
lines and that mutant mice have lysosomal dysfunction, autophagy defects,
reduced mTORC1 signaling, synaptic connectivity defects, and lowered
neurotransmitter content of synaptic vesicles [PMID:33833240, "These data
suggested that all ATP6V0A1 missense variants impaired lysosomal acidification
in cell lines."; PMID:33833240, "the neurotransmitter content of synaptic
vesicles was indeed lowered"]. Bott et al. similarly link ATP6V0A1 variants to
"direct impairment of endolysosome acidification and failure of lysosomal
functions" [PMID:34909687, "direct impairment of endolysosome acidification and
failure of lysosomal functions."].

PN projection: ATP6V0A1 appears in the PN projection under
`Autophagy-Lysosome Pathway > Pre-initiation autophagy signaling > mTORC1
pathway, upstream > Nutrient sensing > V0 lysosomal v-ATPase proton pump
component`, projecting `GO:0046610 lysosomal proton-transporting V-type ATPase,
V0 domain` as `more_specific_than_existing_goa`
[file:projects/PROTEOSTASIS/reports/pn_projection/pn_projected_candidate_additions.tsv,
"ATP6V0A1		GO:0046610	lysosomal proton-transporting V-type ATPase, V0 domain"].
This projection was accepted conservatively as a NEW candidate only because it
is independently supported by ATP6V0A1/V-ATPase evidence. The PN resource was
not used to add broader mTORC1 or nutrient-sensing process annotations.

Curation decisions:

- Accept V-ATPase complex/V0-domain membership, contributes-to rotary
  proton-transporting ATPase activity, proton transmembrane transport, lysosomal
  and endosomal acidification, and synaptic vesicle acidification.
- Add `GO:0046610 lysosomal proton-transporting V-type ATPase, V0 domain` as a
  conservative PN-supported NEW annotation.
- Keep plasma membrane, secretory granule, ficolin-1-rich granule, phagocytic
  vesicle, clathrin-coated vesicle, perinuclear cytoplasm, melanosome, and
  ATPase-binding rows as non-core where supported.
- Mark generic cytoplasm, membrane, and extracellular exosome rows as
  over-annotated relative to the more informative organelle membrane and complex
  terms.
- Remove the PMID:7896830 `protein binding` row because the paper supports
  papillomavirus E5 binding to the 16 kDa V-ATPase proteolipid subunit, not to
  ATP6V0A1 [PMID:7896830, "The 16K subunit of the vacuolar H(+)-ATPase binds
  specifically"].
- Mark the PFK-1 `protein binding` row as over-annotated. The a1 interaction is
  real, but generic `protein binding` is not an informative ATP6V0A1 molecular
  function [PMID:12649290, "An in vitro bead-bound PFK-1 pull-down assay showed
  that this interaction was also true for the ubiquitously expressed a1
  subunit."].

## Falcon deep research synthesis (2026-06-21)

The Falcon report (`file:human/ATP6V0A1/ATP6V0A1-deep-research-falcon.md`)
corroborates the core a1-subunit / lysosomal-acidification biology above and adds
mechanistic and pathway detail.

**Mechanistic MF detail — a1 is the proton-conducting subunit, not just a
structural component.** Unlike the ATP6AP1/ATP6AP2 accessory subunits, ATP6V0A1
directly builds the proton pathway: its C-terminal membrane domain (aCT, 8 TM
helices, two near-horizontal) forms the **cytoplasmic and luminal hemichannels**,
and the **essential arginine R740/R741** deprotonates the c-ring glutamates
(E139 on c / E98 on c'') as the rotor turns, releasing H+ to the lumen (~10 H+
per 3 ATP). R741Q is a recurrent loss-of-acidification disease variant
(embryonic-lethal when homozygous in mouse), which pins the proton-translocation
activity to this residue (Indrawinata 2023; Aoto 2021 PMID:33833240; Bott 2021
PMID:34909687). This supports annotating ATP6V0A1 with the proton-transmembrane-
transporter / V0 proton-pore activity rather than only "complex component".

**N-terminal cytosolic domain (aNT) as the V1-V0 coupling/regulatory hub.** The
dumbbell-shaped aNT bridges V1 (subunits E, G, C, H) and V0, couples ATP
hydrolysis to rotation, and carries isoform-specific trafficking sequences
(Tuli 2023) — the structural basis for a1-isoform-specific organelle targeting.

**New non-core role — cholesterol absorption / immune evasion (Huang 2024).** In
colorectal cancer, ATP6V0A1 drives RABGEF1-dependent endosome maturation and
exogenous cholesterol absorption → ER cholesterol → 24-hydroxycholesterol → LXR
→ TGF-β1 → suppression of memory CD8+ T cells. A genuine but disease/context-
specific downstream consequence of endosomal acidification; keep **non-core**.

**Corroborated (no change to calls):** acidification of lysosomes/endosomes/TGN/
secretory & synaptic vesicles; powering H+-coupled neurotransmitter loading
(VGLUT/VMAT/VGAT) and secondary active transport; mTORC1 nutrient sensing;
autophagy/PQC; and the neurological disease spectrum (DEE, progressive myoclonus
epilepsy, neurodevelopmental phenotypes). Net: core call unchanged (V0 a1 subunit
mediating organellar/lysosomal acidification), with sharper mechanistic support.
