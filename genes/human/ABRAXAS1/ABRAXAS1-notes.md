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

## Falcon deep research findings (2026-06-07)

A Falcon deep-research report (`ABRAXAS1-deep-research-falcon.md`, Edison Scientific) was generated successfully on 2026-06-07, superseding the earlier failed run noted above. It is consistent with the existing review and adds the following, with NEW/CONFIRMS/PROVISIONAL labels. PMIDs could not be resolved via tooling for several of these primary papers (PubMed MCP unavailable); where only a DOI was available it is given, and these citations are kept in notes only rather than added as guessed PMIDs to the YAML.

- CONFIRMS (molecular function / mechanism): ABRAXAS1 is a non-catalytic scaffold/adaptor with an N-terminal MPN-/JAMM-like domain that is catalytically inactive (MPN-) and acts as a DEUBAD-like activator/positioner of the K63-specific DUB BRCC36; ABRAXAS1 itself does not deubiquitinate. This matches the existing `KEEP polyubiquitin-binding` / `not the catalytic DUB` framing [PMID:20656689 "Abraxas and BRCC45 were essential for BRCC36 DUB activity within the RAP80 complex"; Rabl 2020 review doi:10.3390/biom10111503; Kyrieleis 2016 doi:10.1016/j.celrep.2016.11.063].

- NEW (structural architecture): Negative-stain EM of a reconstituted human BRCA1-A core (Abraxas/BRCC36/BRCC45/MERIT40) supports a V-shaped "superdimer" (dimer of heterotetramers) with ABRAXAS1-BRCC36 at the base and BRCC45/MERIT40 in the arms; complexes prefer longer K63 chains (>=4 Ub), and RAP80 enhances targeting to mixed SUMO-K63 chains [Kyrieleis 2016 doi:10.1016/j.celrep.2016.11.063; Rabl 2019 Mol Cell doi:10.1016/j.molcel.2019.06.002]. Adds structural detail beyond current complex-membership annotations; no annotation change warranted.

- NEW (domain map / NLS, clinical): ABRAXAS1 has an NLS (~aa 358-361, incl. Arg361) required for nuclear import of BRCA1-A; the Finnish founder variant c.1082G>A p.Arg361Gln (R361Q) impairs nuclear localization and reduces BRCA1/CtIP foci [Bose 2019 Hum Mol Genet doi:10.1093/hmg/ddz252]. A 2024 motif-interactome study (already cited as PMID:39009827) quantified the R361Q effect: importin/karyopherin affinity weakened ~10-fold (WT KD 7.5 uM vs R361Q 75 uM) with increased cytoplasmic localization [PMID:39009827 "Proteome-scale characterisation of motif-based interactome rewiring by disease mutations"]. The C-terminal pSPxF/SPTF motif (~aa 406-409; S404 damage-inducible, S406 constitutive, F409 critical) mediates phospho-dependent BRCA1 BRCT binding.

- NEW (disease mechanism / pathway choice): Two truncating germline ABRAXAS1 variants from early-onset breast cancer patients - c.1106dup (p.Ser370Ilefs*2, loses the C-terminal BRCA1-binding SPTF motif) and c.577C>T (p.Arg193*, also lacks the BRCC36-interaction region) - act dominantly to shift BRCA1 partitioning from BRCA1-A toward BRCA1-C and derepress mutagenic DSB repair (SSA/MMEJ/NHEJ) without impairing HR; notably heterozygous carriers did NOT show HR deficiency or altered PARP-inhibitor sensitivity [Sachsenweger 2023 Cell Death Dis doi:10.1038/s41419-023-05845-6]. Reframes ABRAXAS1 as a "fine-tuner" of BRCA1 repair-pathway choice (restrains end resection / mutagenic pathways) rather than a simple HR-promoting factor. Supports the existing `positive regulation of DNA repair` / checkpoint framing; no existing annotation contradicted.

- PROVISIONAL / low-confidence (RNA association): A proteome-wide R-DeeP screen in A549 lung cancer cells identified ABRAXAS1 as RNA-dependent, with direct RNA interaction validated by iCLIP2 ("mitosis-related protein ABRAXAS1") [Rajagopal 2022 Cancers doi:10.3390/cancers14246109]. This is a single high-throughput study in one cell line; flagged provisional and NOT used to add any RNA-binding GO annotation. Worth a curator question only.

- CONFIRMS (paralog specialization): ABRAXAS1 (BRCA1-A, nuclear) vs paralog ABRO1/ABRAXAS2 (BRISC, largely non-nuclear) partition the shared BRCC36/BRE/MERIT40 core. This reinforces the existing REMOVE decisions on microtubule/spindle IBA terms traceable to ABRAXAS2 [Rabl 2020 doi:10.3390/biom10111503; Rabl 2019 doi:10.1016/j.molcel.2019.06.002].
