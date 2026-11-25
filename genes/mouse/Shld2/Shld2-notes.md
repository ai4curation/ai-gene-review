# Shld2 (mouse, Q3UEN2) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

The review is new, made because Q3UEN2 is the closest experimentally characterised relative of the
ProtNLM2 benchmark gene human SHLD2 (Q86V20). No ProtNLM2 output was opened or used.

### Deep research

`just deep-research-falcon mouse Shld2 --fallback perplexity-lite` failed. Falcon (Edison API) returned
`403 Forbidden` at `/auth/login`. The perplexity-lite fallback returned `401 insufficient_quota`. No
deep-research file exists. The review is built from cached primary literature found by a PubMed search
for Shld2/Fam35a/shieldin, cached with `just fetch-pmid`.

### Evolutionary grounding

- PANTHER: Q3UEN2 is in PTHR14495:SF2, the family's only subfamily
  (`interpro/panther/PTHR14495/PTHR14495-entries.csv`). PAINT node PTN001025652 (taxon 6072, Eumetazoa)
  is seeded by human SHLD2. It carries nucleus, site of DSB and regulation of DSB repair via HR. It does
  not carry NHEJ, isotype switching or ssDNA binding. CSR is vertebrate-specific, so leaving it off a
  Eumetazoa node is reasonable. Human ssDNA binding is not in GOA, so its absence from the node is an
  absence of a donor term, not a declined transfer.
- Sequence (`Shld2-bioinformatics/RESULTS.md`): 67% identity to the human 904-aa long form. The
  N-terminal SHLD3/REV7 segment is 68% identical and the OB-fold region 79%. Mouse carries the 69-aa OB
  fold B exon, 56/69 identical, which the human 835-aa short form lacks.

### Mouse-experimental findings

- Shld2-/- mice (Ling 2020) [PMID:32558186 "All together, these data show a critical function of SHLD2 in CSR in mice, supporting previous findings in the CH12 B‐cell line (Noordermeer et al , 2018 )."].
  Lymphocyte development and V(D)J recombination are normal
  [PMID:32558186 "Hence, SHLD2 deficiency does not impact V(D)J recombination, consistent with what was observed in the Mb1 cre/+ Rev7 fl/fl mice (Ghezraoui et al , 2018 )."].
  Shld2 loss suppresses Brca1 Δ11 embryonic lethality.
- CH12-F3 (Ghezraoui 2018): REV7 co-purifies SHLD1-SHLD2. Shld2-/- CSR is rescued by the mouse transgene
  [PMID:30046110 "CSR was restored in Shld3-/- and Shld2-/- cells by integration of Shld3 and Shld2 transgenes, respectively"].
  RPA-ssDNA is enriched at switch regions in Shld2-/- cells.
- MEFs (Mirman 2018): Shld2 limits resection at deprotected telomeres
  [PMID:30022158 "Similarly, the 5′ end resection was increased by Rev7- or Shld2-deficiency"].
- Mouse TRF2ts cells (Dev 2018): Fam35a depletion reduces telomere fusions
  [PMID:30022119 "we found that such chromosome fusions were diminished by FAM35A or C20orf196 depletion like that elicited by MAD2L2 depletion"].
- Brca1-deficient MEFs (Mirman 2022): Shld2 is needed for fill-in at PARPi-induced DSBs
  [PMID:35027730 "BrdU-γH2AX metaPLA foci did not form in cells lacking REV7 or SHLD2 or when Polα was inhibited"].
- Caveat (King 2025): Shld2 loss does not rescue Brca1-null embryos
  [PMID:39227718 "By contrast, no Brca1−/−Shld2−/− double-knockout pups were born to intercrosses between Brca1+/−Shld2−/− mice (Table 2)."].
  In mouse, HR suppression by 53BP1 is only partly shieldin-dependent.

### Inferred, not shown in mouse

- ssDNA binding (GO:0003697) and the scaffold/adaptor role (GO:0030674) come from the human biochemistry
  (PMID:30022168). Both are proposed by MODIFY of the ND MF row as ortholog inferences.
- All CC rows (nucleus, nucleoplasm, DSB site) are ortholog or PAINT transfers. No mouse imaging exists.
  Actin cytoskeleton (ISO, from a secondary HPA signal) is marked over-annotated.

### Decisions

- GO:0002208 MODIFY to GO:0045190 isotype switching, on mouse knockout evidence.
- GO:0010569 IBA MODIFY to GO:2000042, signed. Chromosome rows MODIFY to GO:0035861.
- GO:0043247 and GO:0045830 KEEP_AS_NON_CORE. NHEJ, HR, nucleus and DSB-site rows ACCEPT.
