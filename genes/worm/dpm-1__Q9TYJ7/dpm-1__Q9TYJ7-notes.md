# dpm-1 (Q9TYJ7, Y66H1A.2a) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: the full-length C. elegans dpm-1 product Q9TYJ7 (239 aa, WormBase Y66H1A.2a, WBGene00022044).
The 51-residue U4PF58 (Y66H1A.2b) entry reviewed in `genes/worm/dpm-1/` is an exact C-terminal substring of
this protein (checked in `dpm-1__Q9TYJ7-bioinformatics/RESULTS.md`). No ProtNLM2 output was consulted.

### Deep research

`just deep-research-falcon worm dpm-1__Q9TYJ7 --fallback perplexity-lite` failed on 2026-10-21: falcon
raised "Failed to authenticate" (Edison client) and the perplexity-lite fallback returned HTTP 401
(insufficient quota). No deep-research file was produced for this folder. Literature was read directly from
the publication cache and via web search instead. The existing falcon report for the same gene
(`genes/worm/dpm-1/dpm-1-deep-research-falcon.md`, run for U4PF58) was read for orientation; it reports that
no worm-specific enzyme assay, localization or rescue study was retrieved.

### What is established, and where

- **Experimentally in C. elegans:** nothing functional. GOA has no experimental annotation for Q9TYJ7; the
  UniProt entry is unreviewed, its function comment is a UniRule (RuleBase RU365083) statement, and PE=1
  rests only on PeptideAtlas peptide detection. No worm biochemistry, localization, complementation or
  mutant glycan analysis was found.
- **Experimentally in relatives in the same PANTHER subfamily (PTHR43398:SF1):**
  - Yeast Dpm1 (P14020): the cloned gene confers Dol-P-Man synthase activity on E. coli
    [PMID:3053713 "DPM1 is the structural gene for yeast Dol-P-Man synthase since Escherichia coli transformants harboring this gene express Dol-P-Man synthase activity in vitro"];
    ts mutants block GPI anchoring, N-glycosylation and O-mannosylation in vivo [PMID:2146492].
  - Human DPM1 (O60762): catalytic subunit of a DPM1-DPM2-DPM3 complex
    [PMID:10835346 "mammalian DPM synthase contains catalytic DPM1 and regulatory DPM2 subunits, and that DPM1 requires DPM2 for its stable expression in the endoplasmic reticulum"];
    DPM3 tethers DPM1 to the ER membrane
    [PMID:16280320 "A coiled-coil domain near the C terminus of DPM3 was important for tethering DPM1, the catalytic subunit of the enzyme, to the endoplasmic reticulum membrane"].
  - Class structure: Colussi et al. split DPM synthases into an S. cerevisiae class with a C-terminal
    hydrophobic anchor and a human class without one; a Caenorhabditis (C. briggsae) synthase falls in the
    human class, and the two classes are functionally interchangeable in S. pombe [PMID:9223280].
- **Evolutionary grounding of transfer:** Q9TYJ7, human DPM1 and yeast Dpm1 are all PTHR43398:SF1. PAINT
  places GO:0004582 at PTN002459128 (seeds human, mouse, yeast, Leishmania and Mycobacterium proteins),
  GO:0005789 at PTN000092441 (eukaryotes; seeds Arabidopsis, yeast, human) and GO:0006488 at PTN000092440
  (seeds yeast, Candida). The local PAINT file (`interpro/panther/PTHR43398/PTHR43398-paint.tsv`) has no
  IBD for GPI-anchor biosynthesis (GO:0006506), O-mannosylation (GO:0035269) or the DPM synthase complex
  (GO:0033185), although human DPM1 has experimental annotations to all three. The UniProt record still
  shows legacy GO_Central IBA lines for GO:0006506 and GO:0035269 that are no longer in GOA. I treat these
  omissions as deliberate PAINT decisions and do not add them as NEW.
- **Own sequence analysis** (`dpm-1__Q9TYJ7-bioinformatics/RESULTS.md`): conserved VDDAS (41) and MDAD (95)
  motifs retained; no transmembrane-strength hydrophobic window (max KD19 = 0.89), unlike yeast Dpm1 (2.01);
  worm has a DPM3 orthologue (dpm-3, Q9XVV5) but no DPM2 (PF07297) protein was found by Pfam search.

### Decisions

- GO:0004582 (IBA, IEA): ACCEPT. Inferred, not measured in worm.
- GO:0005789 ER membrane (IBA): ACCEPT; human-class DPM1 is expected to be peripheral on the cytosolic face,
  tethered by DPM3, rather than membrane-spanning.
- GO:0005783 ER (IEA): MODIFY to GO:0005789.
- GO:0006488 DLO biosynthesis (IBA): KEEP_AS_NON_CORE; the enzyme supplies the mannosyl donor for the
  lumenal mannoses but does not itself extend the oligosaccharide.
- NEW GO:0180047 dolichol phosphate mannose biosynthetic process: this is the process the enzyme's own
  reaction constitutes (participation, not necessity). Comparators: human DPM1 IDA and DPM2 IDA (PMID:10835346),
  yeast DPM1 ISS. Not an ancestor/descendant of GO:0006488.
- Not added: complex membership (GO:0033185), GPI anchor biosynthesis, O-mannosylation; raised as questions.
- No organismal phenotypes (RNAi lethality etc.) were used as process evidence.
