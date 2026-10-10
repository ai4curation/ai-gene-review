# atg-2 (Q21480) review notes

Deep research: falcon attempt timed out on 2026-10-08 and perplexity was unavailable; no
deep-research file. Review based on cached papers, UniProt and PubMed.

## Key facts
- ATG2-family bridge-like lipid transfer protein (2290 aa). Lipid transfer is shown for orthologs [PMID:30952800 "ATG2A can bind tens of glycerophospholipids at once and transfers lipids robustly in vitro"; PMID:30911189 "Atg2 acts as a lipid-transfer protein that supplies phospholipids for autophagosome formation"].
- Binds EPG-6 directly; the ATG-2/EPG-6 complex acts at omegasome-to-autophagosome progression [PMID:21802374 "EPG-6 directly interacts with ATG-2"].
- Acts upstream of MTM-3 and EPG-5 [PMID:25124690 "MTM-3 acts downstream of the ATG-2/EPG-6 complex"].
- Acts cell-autonomously in AIY neurons for presynaptic assembly [PMID:27396362].

## Decisions
- IMP positive regulation of autophagy (PMID:25124690) modified to autophagosome assembly: ATG-2 is core machinery, not a regulator.
- PMN IBA marked over-annotated (yeast-specific process).
- protein binding IPI removed (interaction real; captured as GO:0062079 complex membership, NEW).
- NEW: GO:0120013 lipid transfer activity (ISS from ATG2A/S. pombe Atg2), GO:0062079 ATG2-ATG18 complex.
