# epg-6 (Q86MP3) review notes

Deep research: `just deep-research-falcon worm epg-6` was attempted (2026-10-08) but the
falcon provider timed out and perplexity was unavailable, so no deep-research file was
produced. The review is based on cached publications, the UniProt record and PubMed searches.

## Key facts
- WD40 PROPPIN of the WIPI3/WIPI4 (yeast Hsv2) group [PMID:30871075 "Caenorhabditis elegans EPG-6 belongs to the other PROPPIN group together with yeast HSV2 and human WIPI3 and WIPI4"].
- Binds PI3P and binds ATG-2 directly; with ATG-2 drives omegasome-to-autophagosome progression [PMID:21802374 "EPG-6 directly interacts with ATG-2. epg-6 and atg-2 regulate progression of omegasomes to autophagosomes"].
- In vitro also binds PI5P (strongly), PI4P and PI(3,5)P2 (weakly) [file:worm/epg-6/epg-6-uniprot.txt].
- Human counterpart: WIPI4 binds one tip of ATG2A [PMID:30185561 "WIPI4 binds to one of the tips, enabling the ATG2A-WIPI4 complex to tether a PI3P-containing vesicle to another PI3P-free vesicle"].
- epg-6 mutants are long-lived despite an autophagy block, suggesting an autophagy-independent role [PMID:30871075 "lifespan was significantly increased in epg-6 mutant animals"].

## Decisions
- PI3P binding and adaptor activity are core MFs; other phosphoinositide binding rows kept as non-core.
- GO:0034045 (obsolete) rows modified to GO:7770114 phagophore membrane (matching human ATG2A review).
- protein binding (IPI with ATG-2) modified to protein-macromolecule adaptor activity.
- NEW: GO:0062079 ATG2-ATG18 complex (direct binding, IPI).
