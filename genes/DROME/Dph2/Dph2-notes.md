# Dph2 review notes

Module context: dmel_diphthamide_dph1_dph2_complex (Dph2 with Dph1).

Deep research: the first falcon run (perplexity-lite fallback) failed (falcon killed /
timed out; perplexity provider unavailable). There is no Drosophila-specific
experimental literature on Dph2 in the cached publications; annotations rest on
orthology (yeast/mouse/human DPH1-DPH2) and on Drosophila interactome screens.

- Drosophila interactome evidence for the Dph2-Dph1 pair: [PMID:37061542 "We apply state-of-the-art methods to identify binary protein-protein interactions (PPIs) for Drosophila melanogaster"]; also DPIM (PMID:14605208) and DPIM2 (PMID:38944040).
- Human heterodimer model: [PMID:30877278 "We have built a homology model of the human DPH1-DPH2 heterodimer"]
- UniProt pathway: "Protein modification; peptidyl-diphthamide biosynthesis".

Decisions: ND root MF removed (superseded by ISS activity); three protein binding rows
removed as uninformative (captured by GO:0120513 complex membership); catalytic complex
(NAS) modified to GO:0120513. Activity and process accepted. Core function uses
contributes_to GO:0090560 since the ACP-histidine synthase is the DPH1-DPH2 heterodimer.
