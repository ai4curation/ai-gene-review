# ATOX1 manual notes

## GO-CAM 69ea894900001492

- GO-CAM activity `69ea894900001987` models ATOX1 as a cytosolic copper chaperone that participates in copper ion transport. This agrees with the core ATOX1 function: Cu(I) handoff from the cytosolic chaperone to Cu-ATPase metal-binding domains, with PMID:12029094 directly showing copper transfer from Atox1 to the N-terminal domain of ATP7B/WNDP and PMID:15670166 showing a Cu(I)-mediated adduct between human HAH1/ATOX1 and ATP7A metal-binding domains.
- GO-CAM activity `69ea894900002007` models the nuclear ATOX1 RNA polymerase II transcription-activator branch that indirectly up-regulates SOD3. The SOD3 regulation is biologically plausible and represented in GOA by both direct PMID:15761197 evidence and an orthology transfer, but it is peripheral to the conserved metallochaperone activity and remains a mouse-derived regulatory context rather than a direct human ATOX1 core function.
- The GO-CAM indirect edge from nuclear ATOX1 transcription factor activity to extracellular SOD3 activity is consistent with the gene-level evidence only as a summary relation: PMID:15761197 supports effects on SOD3 mRNA/protein and on copper-dependent SOD3 activity, while target-gene transcription, SOD3 secretion, ATP7A-mediated copper loading, and extracellular superoxide dismutation are intervening steps.

## Manual literature synthesis

- ATOX1 is a 68 aa HMA-domain Cu(I) metallochaperone. The CXXC motif binds Cu(I), and mutating either cysteine disrupts copper trafficking to the yeast secretory-pathway multicopper oxidase Fet3p [PMID:9430722].
- Human HAH1/ATOX1 interacts with metal-binding domains from the Wilson and Menkes Cu-ATPases in a copper-dependent manner [PMID:10497213], forms a Cu(I)-mediated complex with ATP7A metal-binding domains by NMR [PMID:15670166], and transfers copper to ATP7B/WNDP in vitro [PMID:12029094].
- The human CTR1/SLC31A1 cytosolic C-terminal peptide can bind Cu(I) and directly transfer it to ATOX1; this supports the CTR1-to-ATOX1 handoff but does not make every reported ATOX1 protein interaction a distinct molecular function [PMID:26745413].
- Platinum drugs can trap the ATOX1-Cu(I)-ATP7A-domain exchange complex, further supporting the centrality of the CXXC-mediated Cu(I) transfer surface [PMID:31283225].
- Generic interactome rows from broad yeast-two-hybrid screens were treated as uninformative protein-binding rows unless the cited paper itself established a copper-dependent handoff or other specific ATOX1 activity.

## Deep research

`just deep-research-falcon human ATOX1 --fallback perplexity-lite` was attempted on 2026-11-25. The local `deep-research-client` install only exposed the `claude_code` provider, and both Falcon and Perplexity-Lite failed provider availability checks, so no provider-authored `ATOX1-deep-research-*.md` file was written. This notes file records the manual synthesis used instead.
