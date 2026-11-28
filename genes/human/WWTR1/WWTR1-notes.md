# WWTR1 mechanobiology review notes

## Deep research

- `just deep-research-falcon human WWTR1` could not run in this worktree because the Falcon provider was not available; the local provider list contained only `claude_code`. These notes therefore record a manual pass through the cached primary publications and pathway records.

## Manual evidence synthesis

- WWTR1/TAZ is the YAP1 paralog in the Hippo output tier. Lei et al. connected TAZ to the MST/LATS Hippo kinase cascade by showing that LATS2 directly phosphorylates TAZ, that LATS/MST phosphorylation promotes TAZ binding to 14-3-3 epsilon, and that this shifts TAZ from the nucleus to the cytoplasm to inhibit its transcriptional coactivator output [PMID:18227151].
- Nuclear TAZ coactivates sequence-specific transcription factors rather than binding DNA itself. Focused papers show direct activation with PAX8/NKX2-1 [PMID:19010321], TEAD1-4 as the major Hippo transcription-factor partners for proliferation and EMT programs [PMID:19324877], and SMAD2/3-SMAD4 coupling in TGF-beta-stimulated human embryonic stem cells [PMID:18568018].
- The WW domain mediates PPxY/proline-rich-region binding to regulatory partners. Focused examples include WBP2, for which the PPXY-containing C terminus binds the TAZ WW domain [PMID:20972459], AMOT family proteins that sequester YAP/TAZ [PMID:21205866, PMID:23911299], and PRRG4 [PMID:23873930].
- The TAZ C-terminal PDZ-binding motif is a second regulatory binding module. Kanai et al. reported that it localizes TAZ to discrete nuclear foci and suggested that TAZ links plasma-membrane and cytoskeletal events to nuclear transcription [PMID:11118213]; UniProt separately curates cell membrane localization from that paper and a by-similarity PDZ-motif interaction at the plasma membrane with SLC9A3R2. Remue et al. showed that the first PDZ domains of ZO-1 and ZO-2 bind the TAZ C-terminal motif [PMID:20850437].
- Beta-catenin binding and SMAD-mediated TGF-beta signaling connect Hippo to Wnt and TGF-beta pathways, but these are treated as context-specific outputs rather than the core WWTR1 molecular role [PMID:20412773, PMID:22234184, PMID:18568018].
- Protein-interaction rows from BioPlex, fragmentomic, multimodal cell-map, and other proteome-scale screens were not upgraded on their own. They either remain useful only as bare interaction observations or duplicate more interpretable binding modes already supported by focused TAZ papers.
- The Human Protein Atlas WWTR1 subcellular page reported: "Mainly localized to the nucleoplasm and nuclear bodies. In addition localized to the cytosol." The page listed Nucleoplasm (supported), Nuclear bodies (supported), and Cytosol (supported) for antibody HPA007415.
- The local GO-CAM index has six UniProt-provided human Hippo models that already place WWTR1 as a nuclear `GO:0003712` transcription coregulator activity in `GO:0035329` hippo signaling. This gene-only PR reviews GOA rows and does not edit `modules/hippo_signaling.yaml` or the GO-CAM cache.
