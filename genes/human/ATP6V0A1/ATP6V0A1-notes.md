# ATP6V0A1 notes

## 2026-06-03 - Proteostasis PN review

Deep research status: `just deep-research-falcon human ATP6V0A1 --fallback perplexity-lite`
was run for this review. Falcon timed out after 600 seconds, and the configured
`perplexity-lite` fallback failed with a Perplexity API quota 401. No provider
deep-research file was created. I proceeded from fetched UniProt, GOA, cached
publications, Reactome records, Panther family data, and the PN projection
reports.

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
