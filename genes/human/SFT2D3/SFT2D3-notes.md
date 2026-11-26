# SFT2D3 Reference Enhancement Notes

## Status: ENHANCED ✅

### Initial State
- **Literature references**: 0 PMIDs/PMCs
- **Total references**: 6 (mostly GO_REF annotations)
- **Findings**: 13 from deep research file

### Enhancements Made (2025-09-13)

#### Added Literature References
1. **PMID:25464851** - "Genome-wide RNAi screen reveals a role for multipass membrane proteins in endosome-to-golgi retrieval"
   - Key findings on SFT2D2 (human paralog) function
   - Demonstrates endosome-to-Golgi retrieval role
   - Shows specific SNARE protein interactions (syntaxin 6)
   - 6 specific findings extracted with supporting text

2. **PMID:10406798** - "Got1p and Sft2p: membrane proteins involved in traffic to the Golgi complex"
   - Yeast homolog functional studies
   - Establishes evolutionary conservation
   - Vesicle fusion requirements
   - 6 specific findings extracted with supporting text

#### Impact
- **Literature references**: 0 → 2 PMIDs
- **Total references**: 6 → 8
- **Total findings**: 13 → 25 findings with proper supporting text
- **Functional validation**: Now has direct experimental evidence through paralog studies

### Research Strategy Used

1. **Targeted paralog search**: Focused on SFT2D2 since SFT2D3 itself is understudied
2. **Evolutionary approach**: Used yeast Sft2p/Got1p studies for mechanistic insights
3. **Functional context**: Emphasized vesicle transport and SNARE interactions
4. **Quality control**: Used `just fetch-pmid` commands to properly cache publications

### Key Scientific Insights Added

- **Mechanistic detail**: SNARE protein interaction patterns (syntaxin 6 specificity)
- **Subcellular localization**: Retromer complex association, endosomal/Golgi trafficking
- **Functional requirements**: Vesicle fusion dependencies in yeast models
- **Evolutionary conservation**: Membrane topology and trafficking function preserved

### Next Steps for SFT2D3
- Consider searching for additional SFT2D1 studies
- Look for AlphaFold structural predictions
- Check for any disease association studies
- Review for any tissue-specific expression patterns

### Lessons Learned
- Paralog studies are extremely valuable for understudied genes
- Yeast homolog research provides strong mechanistic foundations
- Focus on functional context rather than generic gene expression studies
## 2026-11-19 ORGANELLES Golgi batch 4 (Golgi apparatus rows)

- The review's GO:0005794 row is a NEW proposal. GO:0005794 has never been in SFT2D3-goa.tsv
  (`git log -S` on the GOA file finds no such row), so this is not GOA drift. The second GO:0005794
  in the file is the core_functions location.
- The NEW row was ISS citing PMID:25464851, a paper about the paralog SFT2D2, plus a deep-research
  sentence about a 2024 preprint. It is re-based as IC on the peer-reviewed version, Sumya,
  Aragon-Ramirez and Lupashin 2025 Mol Biol Cell [PMID:40397568 "The most notable increase was
  observed for QPCTL (39-fold), SFT2D3 (12-fold), and BSG (12-fold)"]. That paper uses RPE1 cells
  and GS15-positive Golgi-derived vesicles after acute COG4 depletion. Full text cached. The preprint
  is PMID:39484492 (cached, not cited).
- Second, independent line: family conservation. Yeast Sft2p is "found mostly in the late Golgi"
  (PMID:10406798), and human SFT2D2 colocalizes with syntaxin 6 (PMID:25464851).
- Caveat: the SFT2D3 value is a fold change after perturbation. Control-vesicle enrichment is in
  Supplemental Table S4, not read. BSG (plasma membrane) rose equally. No sub-compartment row.

### Review follow-up (2026-11-19)

- The Golgi row's summary now matches the reason's hedge. PMID:40397568 reports a finite 12-fold change for SFT2D3, unlike enzymes it says were detected only after COG4 depletion, so SFT2D3 was quantified in control vesicles too. Family conservation corroborates but does not establish the location. GO:0042147 in core_functions still rests on paralog and ortholog papers: left for a later pass.
