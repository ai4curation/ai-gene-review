# VTI1A notes

## Local evidence reviewed

- `just fetch-gene human VTI1A` created the review stub, UniProt record, GOA table, cached publications, Reactome entries, and PANTHER family data. GOA seeded 53 annotations covering SNARE activity/complex membership, endosome-to-Golgi/TGN retrograde traffic, Golgi/TGN and endosomal locations, autophagy, neuronal/synaptic context, broad membrane/cytosol locations, and a movement phenotype.
- `just deep-research-falcon human VTI1A` timed out after 600 seconds on 2026-06-02 and did not produce a Falcon report.
- UniProt identifies VTI1A as a VTI1-family SNARE. Its function comment says it mediates vesicle transport through interactions with target-membrane SNAREs and promotes lipid-bilayer fusion [UniProt:Q96AJ9, "mediates vesicle transport pathways through interactions with t-SNAREs on the target membrane"; UniProt:Q96AJ9, "to promote fusion of the lipid bilayers"]. This supports SNAP receptor/SNARE-complex activity as the core molecular function, not generic protein binding.
- Direct endosome-to-TGN evidence is strong. The syntaxin-10 SNARE-complex paper reports that a complex of STX10, STX16, Vti1a, and VAMP3 is required for mannose 6-phosphate receptor transport from endosomes to Golgi/TGN [PMID:18195106, "STX10, STX16, Vti1a, and VAMP3 is required for this MPR transport"]. Soluble Vti1a inhibited MPR transport, and the authors concluded that this complex transports MPRs from late endosomes to the Golgi [PMID:18195106, "implicate a SNARE complex comprised of STX10, STX16, Vti1a, and VAMP3"].
- A second trafficking route is supported by the VAMP7/Vti1a paper. KChIP1 vesicles colocalized with Vti1a and VAMP7, Vti1a knockdown inhibited Kv4/KChIP1 traffic to the plasma membrane, and the authors conclude that VAMP7/Vti1a defines a novel cell-surface traffic pathway [PMID:19138172, "KChIP1-expressing vesicles co-localized with the SNARE proteins Vti1a and VAMP7"; PMID:19138172, "inhibited Kv4/KChIP1traffic to the plasma membrane"].
- Autophagy evidence comes from the STX13/Vti1a paper. The abstract reports that knockdown of syntaxin 13 or Vti1a caused LC3-positive puncta accumulation and blocked autophagic flux [PMID:24095276, "Knockdown of syntaxin 13 (STX13) or its binding partner Vti1a in mammalian cells caused LC3-positive puncta to accumulate"]. This supports VTI1A in autophagy/macroautophagy and autophagosome context, but the direct text available does not justify ESCRT-III complex membership.
- The Golgi ribbon/endocytic recycling paper supports Vti1a as a VAMP4 cognate SNARE partner in early-endosome-to-TGN retrograde traffic and Golgi organization [PMID:23677696, "syntaxin 6, syntaxin 16, and Vti1a also disrupted the Golgi ribbon structure"; PMID:23677696, "normal retrograde trafficking from the early endosome to the TGN"]. The `endocytic recycling` row should be interpreted through this retrograde trafficking evidence.
- `PMID:15215310` is problematic for VTI1A. The accessible cached abstract is about syntaxin 5/Ykt6/GS28/GS15 and does not mention VTI1A [PMID:15215310, "syntaxin 5, GS28, Ykt6, and GS15 exist as a unique SNARE complex"]. Rows using this PMID are accepted for the term only because independent VTI1A evidence supports the same SNARE and endosome-to-Golgi conclusions; the cited PMID itself should be treated as a likely source/reference mismatch.
- `PMID:22958904` is a VAMP1 disease paper. The cache contains no VTI1A mention, and the abstract identifies VAMP1 as the responsible gene for hereditary spastic ataxia [PMID:22958904, "This report identifies vesicle-associated membrane protein 1 (VAMP1)... as the responsible gene"]. The VTI1A `voluntary musculoskeletal movement` annotation should be removed.
- The PN projection to `GO:0000815 ESCRT III complex` should not be added for VTI1A. VTI1A is a SNARE that intersects with ESCRT/CHMP2B autophagy phenotypes through STX13/Vti1a trafficking, but it is not an ESCRT-III complex subunit.

## Curation synthesis

The core role of VTI1A is SNARE-mediated vesicle docking/fusion in membrane trafficking, especially endosome/late-endosome to trans-Golgi network retrograde transport and related Golgi/TGN vesicle fusion. Core locations are Golgi/TGN membrane, late endosome/endosome, cytoplasmic vesicle, and ER-to-Golgi or alternative trafficking vesicles.

Autophagy/macroautophagy rows should be retained because Vti1a knockdown blocks autophagic flux in the STX13/CHMP2B context. The evidence supports autophagy and autophagosome context but does not establish ESCRT-III complex membership.

Rows from `PMID:15215310` are likely mis-referenced or at least not confirmable from accessible text. The affected terms are still biologically supported by independent VTI1A evidence, but the PMID should not be treated as direct evidence for VTI1A. The movement phenotype from `PMID:22958904` should be removed because it is attributable to VAMP1, not VTI1A.

## Description cleanup note

The YAML `description` field was revised to keep it as a standalone biological summary. Project-specific curation framing moved here instead.

- Moved out of the YAML description: the prior wording described the autophagy/autophagosome context as PN-relevant and noted that VTI1A should not be annotated as an ESCRT-III complex component.
