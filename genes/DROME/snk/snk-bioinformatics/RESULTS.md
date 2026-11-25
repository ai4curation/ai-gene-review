# snk (P05049) — PANTHER placement and catalytic-site check

Script: `panther_placement.py` (stdlib Python; run from repo root). Raw output: `panther_placement_output.txt`.
Inputs: the PANTHER 19.0 fruit-fly HMM classification file (PTHR19.0_fruit_fly, downloaded by the repo's PANTHER member-index build), the snk GOA file (WITH/FROM column of the two IBA rows only) and the snk UniProt record.

## PANTHER subfamily

The PANTHER 19.0 classification assigns snk (FBgn0003450) to PTHR24260:SF147 (EG:BACR7A4.3 PROTEIN-RELATED), a Drosophila-only subfamily of 27 fruit-fly proteins in the reference set, including CG43124, CG43125, CG43742 and CG10764. No member of SF147 other than snk has published biochemical characterisation that we found.

## IBA donors sit in other subfamilies

Every FlyBase donor listed in the WITH/FROM of the two IBA rows (extracellular region; innate immune response; PAINT node PTN000667087) falls in a PTHR24260 subfamily other than SF147 (SF134, SF135, SF136, SF140, SF144, SF145). snk itself is not among the donors of either IBA row. The innate immune response IBA therefore reaches snk only through descent from a deep ancestral node whose experimental seeds are the immune clip-domain proteases (psh, MP1, spirit, SPE, grass, modSP, sphinx1/2).

## Catalytic triad and activation site

The UniProt-annotated charge-relay positions are H235 (TAAHC motif), D283 and S381 (GDSGGP motif): the His-Asp-Ser triad is intact. Residues 180-192 read VPSVPLIVGGTPT, consistent with the Leu185-Ile186 zymogen activation bond (Reactome R-DME-214953) and with P184 (mutated to L in PMID:20605458 to block cleavage by Gd) immediately upstream.

## Limitations

This is a classification lookup, not a phylogeny; it does not resolve where within PTHR24260 the PAINT node PTN000667087 sits relative to SF147 in the PAINT tree version used for the IBA.
