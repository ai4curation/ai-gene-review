# ABRAXAS1 review notes

## Evidence setup

- `just fetch-gene human ABRAXAS1` seeded the UniProt, GOA, Reactome, PANTHER family, and review stub files on 2026-06-03.
- Falcon deep research was attempted with `just deep-research-falcon human ABRAXAS1 --fallback perplexity-lite`. Falcon timed out after 600 seconds; the `perplexity-lite` fallback then failed with a Perplexity API 401 quota error. No provider deep-research file was produced, so this review uses cached publications, UniProt, Reactome, PANTHER, and PN projection files directly.

## Functional synthesis

ABRAXAS1/FAM175A/CCDC98 is a nuclear BRCA1-A complex scaffold and ubiquitin-recognition subunit. The primary literature identifies Abraxas as a BRCA1 BRCT-binding phosphoprotein and RAP80 partner: [PMID:17525340 "identified a protein, Abraxas, that directly binds the BRCA1 BRCT repeats through a phospho-Ser-X-X-Phe motif"] and [PMID:17525340 "Abraxas recruits the ubiquitin-interacting motif (UIM)-containing protein RAP80 to BRCA1"].

The supported biological role is DNA double-strand break response and checkpoint/repair signaling, not a standalone catalytic activity. The key experimental summary is that [PMID:17525340 "Abraxas and RAP80 were required for DNA damage resistance, G(2)-M checkpoint control, and DNA repair"]. A second study frames CCDC98 as the factor that mediates BRCA1-RAP80 association and BRCA1-dependent G2/M checkpoint activation [PMID:17643121 "CCDC98 controls both DNA damage-induced formation of BRCA1 foci and BRCA1-dependent G2/M checkpoint activation"].

ABRAXAS1 is also an organizer of the RAP80/BRCA1-A complex. Feng et al. describe CCDC98 as central to assembly: [PMID:19261748 "CCDC98 as the central component that facilitates the assembly of this protein complex"]. The BRCA1-A/RAP80 complex has BRCC36 K63-linked deubiquitinase activity, but the catalytic subunit is BRCC36, while Abraxas is required for that activity in the RAP80 complex context [PMID:20656689 "Abraxas and BRCC45 were essential for BRCC36 DUB activity within the RAP80 complex"].

## PN projection decision

The PN projection has three ABRAXAS1 rows:

- `GO:0070531 BRCA1-A complex`: already exact in GOA and accepted.
- `GO:0006281 DNA repair`: already entailed by GOA via `GO:0006302 double-strand break repair`, so no new annotation is needed.
- `GO:0000151 ubiquitin ligase complex`: new to GOA from the PN group `Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|idiosyncratic RING complex`. I did not add this as a proposed annotation. ABRAXAS1 is part of BRCA1-A, but the gene-level evidence supports scaffold/polyubiquitin-binding and BRCC36 DUB support rather than direct membership in a generic ubiquitin ligase complex. The PN mapping itself says this is a shared E3-complex bucket and warns against assigning catalytic activity to every subunit.

## Annotation cautions

- `protein binding` rows are real interaction evidence but too uninformative for core molecular function. Mechanistic papers should be interpreted as BRCA1-A complex assembly, RAP80/BRCA1/BRCC36 interaction, and polyubiquitin-dependent recruitment rather than retained as generic protein binding.
- The IBA microtubule/spindle annotations are projected through a PANTHER node supported by ABRAXAS2 (`WITH/FROM: UniProtKB:Q15018`) rather than ABRAXAS1-specific evidence. I marked `microtubule binding`, `attachment of spindle microtubules to kinetochore`, and `mitotic spindle assembly` for removal for ABRAXAS1.
