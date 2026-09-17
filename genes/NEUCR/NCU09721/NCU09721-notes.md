# NCU09721: biological evidence

NCU09721 is a large beta-adaptin assigned to the AP-1 cargo-adaptor complex by curated phylogenetic inference. It provides a noncatalytic scaffold for membrane-cargo sorting within the Golgi/endosomal trafficking system. Characterized filamentous-fungal AP-1 complexes support post-Golgi secretion, endosome recycling, and clathrin-associated carrier traffic. These conserved roles support Golgi and carrier-membrane recruitment in Neurospora crassa, while its individual cargoes and direct clathrin-binding mechanism remain uncharacterized.

- cytoplasm: Beta-adaptin is a cytoplasmic coat-adaptor subunit that is recruited to the cytoplasmic surfaces of intracellular membranes. The AP-family fold and characterized fungal AP1 assemblies support this broad location.
- trans-Golgi network: The target AP-1 membership IBA and beta-adaptin domain support transfer from experimentally localized filamentous-fungal AP1 beta subunits. Fusarium AP1 beta colocalizes with a trans-Golgi marker, supporting the TGN assignment.
- intracellular protein transport: Characterized filamentous-fungal AP1 supports secretory carrier sorting and endosome recycling. The curated AP1-family assignment grounds a conserved role in intracellular vesicle-mediated protein traffic.
- endocytosis: AP1 contributes to endosomal recycling and endocytic itineraries in filamentous fungi; Fusarium AP1 loss delays internalization of the endocytic dye FM4-64. This supports a process contribution without reassigning the beta subunit to AP2 or claiming a primary plasma-membrane uptake function.
- endomembrane system: The AP1-family placement and direct Golgi localization of the related Fusarium beta subunit support a more precise trans-Golgi-network compartment.
- protein transport: Characterized filamentous-fungal AP1 supports secretory carrier sorting and endosome recycling. The curated AP1-family assignment grounds a conserved role in intracellular vesicle-mediated protein traffic.
- vesicle-mediated transport: Characterized filamentous-fungal AP1 supports secretory carrier sorting and endosome recycling. The curated AP1-family assignment grounds a conserved role in intracellular vesicle-mediated protein traffic.
- membrane coat: AP1 beta forms part of a membrane-associated cargo-adaptor coat. Filamentous-fungal AP1 assembles with other AP1 subunits and supports clathrin-dependent traffic, consistent with membrane coat membership.
- AP-1 adaptor complex: The curated IBA at PTN000123672 assigns this beta-adaptin to AP1 with experimentally characterized fungal AP1 beta descendants. The AP-beta domain and fungal AP1 subunit-interaction experiments support that inherited complex role; it is not inferred from the generic beta1/2/4 domain alone.
- clathrin binding: Dikaryan beta-adaptins lack the canonical C-terminal clathrin-binding appendage, but Aspergillus AP1 beta uses alternative tail motifs. The target sequence contains LLDID at residues 629–633, matching one tested Aspergillus motif, and terminal LLGLF at 745–749; the stronger Aspergillus LLNGF motif is not identical. These observations support clathrin-association plausibility, but short motif similarity and complex traffic do not establish the exact intrinsic target-binding mechanism. Direct target binding remains unresolved.

Primary evidence excerpts

- [file:NEUCR/NCU09721/NCU09721-uniprot.txt] “DR   InterPro; IPR026739; AP_beta.”
- [PMID:36836259] “FgAP1β interacts with FgAP1σ, FgAP1γ, and FgAP1μ”
- [PMID:36836259] “FgAP1β-GFP, FgAP1γ-GFP, and FgAP1μ-GFP also localize to the Golgi apparatus.”
- [PMID:29925567] “its role in clathrin-dependent maintenance of polar traffic of
specific membrane cargoes toward the apex of growing hyphae. We provide evidence
that AP-1 is involved in both anterograde sorting of RabERab11-labeled SVs and
RabA/BRab5-dependent endosome recycling.”
- [PMID:36836259] “the loss of FgAP1σ blocks the transportation of the v-SNARE protein FgSnc1 from the Golgi to the plasma membrane and delays the internalization of FM4-64 dye into the vacuole.”
- [PMID:28220754] “clathrin binding domains are also missing from the AP-1 β subunit (β1) of all Dikarya”

Provenance: live API snapshot 2026-09-09T03:00:51.831347+00:00. Complete API prediction JSON and all emitted claim IDs, text, and original evidence are preserved in the source and provenance JSON files. Current sequence/annotation data are separate comparison snapshots. Annotation overlap records known biology, not demonstrated training membership. All seven gene-focused Falcon jobs completed; the provider reports were inspected and useful primary leads checked. Publication retrieval used Europe PMC metadata/XML when the canonical PubMed fetch returned HTTP 429.

The Falcon report does not account for the target AP1 IBA when calling complex identity unresolved. The curated AP1 assignment is retained; generic AP-beta domains alone would not distinguish AP1 from AP2. ProtNLM Golgi donor Q22498 is worm COPG-1, a coatomer subunit, so independent AP1 primary evidence is used for the location.

Direct inspection of the frozen Q7S2Q5 sequence gives LLDID at 629–633 and LLGLF at 745–749 (one-based positions after stripping sequence whitespace). PMID:29925567 full-text section “AP-1 associates with clathrin via specific C-terminal motifs” and Fig. 4E identify Aspergillus LLDID at630 and LLNGF at707; mutating these affects clathrin distribution, especially LLNGF. This strengthens family-transfer plausibility but does not equate motif detection with a target binding assay. Primary full text inspected at https://pmc.ncbi.nlm.nih.gov/articles/PMC6063236/.
