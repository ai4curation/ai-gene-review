# Vps50 (CG4996, Vps54L, syndetin ortholog) notes

- Identified as a Rab4/Rab14 interactor that co-purifies with Vps51-53; distantly related to Vps54; named Vps54L/GARPII [PMID:25453831 "These results suggest that the GARP complex exists in a second version in which Vps54 is replaced by CG4996"; "GFP-tagged CG4996 colocalized with Rab4 in S2 cells and interacted with GARP subunits by coprecipitation"].
- Mammalian ortholog syndetin defines EARP [PMID:25799061 "EARP contains an uncharacterized protein, syndetin, in place of the Vps54 subunit of GARP"]; EARP binds syntaxin 6 and functions in Tf recycling [PMID:25799061 "Depletion of syndetin or syntaxin 6 delays recycling of internalized transferrin to the cell surface."].
- Syndetin is NOT needed for retrograde endosome-to-TGN transport [PMID:25799061 "These experiments thus demonstrated that, unlike GARP, the Syndetin-containing complex is not involved in retrograde transport from endosomes to the TGN."].

Decisions: GARP complex rows (IDA/NAS from PMID:25453831, which called it GARPII) MODIFY -> EARP complex; retrograde endosome-to-Golgi MARK_AS_OVER_ANNOTATED; endocytic recycling ACCEPT.

Deep research: falcon completed (genes/DROME/Vps50/Vps50-deep-research-falcon.md) after the review was first committed; checked for consistency.
- Deep research (falcon) adds fly in vivo data: CRISPR Vps50 nulls are viable and male fertile but reduce adult c4da dendrite regrowth after pruning, milder than Vps54 loss and without TGN sterol accumulation [file:DROME/Vps50/Vps50-deep-research-falcon.md "Vps50-mutant neurons did **not** show the corresponding filipin-detected sterol accumulation, and mutant males remained fertile, unlike Vps54-mutant males"] (O'Brien et al. 2022, doi:10.1083/jcb.202112108; not in GOA). Worm EARP sorts dense-core vesicle cargo.
