# pax6a notes (DANRE, P26630)

## 2026-09-27 session log

- Deep research FAILED for this gene (Edison: 402 Payment Required; OpenAI key invalid). Not retried.
  Literature research done manually via Europe PMC REST searches
  (`pax6a AND pax6b`, `pax6b AND zebrafish`, `pax6 AND (teleost OR medaka OR gar) AND duplicat*`).
- Newly cached PMIDs: 18485195, 24951566, 23359656, 37094695, 27387288, 12917294, 8900176, 7946344.

## Key facts with provenance

- Naming: pax6a = old pax6.1 / pax[zf-a]
  [PMID:18282108 "Overlapping divergent expression patterns have been reported for pax6a and pax6b (previously named pax6.1 and pax6.2 respectively) [43,49]."]
- Protein function equal to pax6b:
  [PMID:18282108 "Activation by the two wild type co-orthologues through the P3 homeodomain target [45] (Figure 1D), or the CD19 paired domain target [46] (Figure 1E), was not significantly different, in contrast to the original observations by Nornes et al [43]."]
- Expression: broad neural, not pancreas
  [PMID:18282108 "pax6a is expressed in the lens and retina, as well as more widely in the developing telencephalon, diencephalon, hind brain, and spinal cord, although not in developing pancreas [49]."]
  [PMID:18485195 "In constrast, regions A and C of the zebrafish pax6a gene are not active in the pancreas, this difference being attributable to sequence divergences within two cis-elements binding the pancreatic homeoprotein PDX1."]
- Copy-specific habenula role:
  [PMID:27387288 "Somewhat surprisingly, on the other hand, morpholino knock-down of pax6a alone abrogated the expression of both markers (Fig 2C and 2G); pax6a morphant/pax6bsa86 mutant embryos behaved the same as pax6a morphants alone with respect to these markers (Fig 2D and 2H)."]
- CRISPR allele (exons 8-12 deleted, PTC) and dose-dependent anterior segment / neural crest phenotypes:
  [PMID:32555736 "In contrast to the pax6b/sunrise allele used here, the pax6a mutant allele harbours a premature termination codon, lacking the homeobox DNA binding domain and the PST-rich transactivation domain."]
  [PMID:32555736 "Taken together, our data are consistent with a gene number dependent effect of pax6a/b on the migration of the two distinct waves of NC cells."]
- Retinal regeneration: [PMID:20152834 "In contrast, the paralogous Pax6a protein was required for later neuronal progenitor cell divisions, which maximized the number of neuronal progenitors."]
  Rods not affected: [PMID:20152834 "The reduced number of INL neuronal progenitor cells in both Pax6 knockdown retinas resulted in a corresponding loss of regenerated cones, but not rods."]

## GOA accession artefact (important)

QuickGO shows that ZFIN's experimental annotations to pax6a (IDA GO:0000981 PMID:18282108 and PMID:9831649,
IDA GO:0045944, IMP GO:0021986 habenula development PMID:27387288, IGI GO:0001755 PMID:32555736,
IGI GO:0021538/GO:0010468 PMID:24528677, IMP GO:0009952/GO:0030902 PMID:17010333, IGI GO:0030900
PMID:12917294, IDA GO:0043565 PMID:8900176, IDA GO:0005634 PMID:7946344) are attached to RefSeq-derived
TrEMBL accessions (A0A8M3AP00, A0A8M3AZJ7, A0A8M3B718, ...) and not to Swiss-Prot P26630. The fetched GOA
file therefore makes pax6a look experimentally unstudied relative to pax6b. I added three of these as NEW
(habenula development, epithalamus development, neural crest cell migration) where I read the evidence;
the MF IDAs are already covered by accepted IBA/IEA rows. PMID:12917294, 8900176 and 7946344 are
abstract-only and their abstracts do not clearly show the pax6a claim, so they were not added.

## Decisions

- REMOVE IBA GO:0003309 (beta-cell differentiation): pax6a not expressed in pancreas (expression partition).
- REMOVE IMP GO:0060221 (rod differentiation): contradicted by the source paper.
- MARK_AS_OVER_ANNOTATED IMP GO:0042670 (cone differentiation): effect on pax6a not significant, secondary.
- MODIFY IMP GO:0008284 -> GO:2000179 positive regulation of neural precursor cell proliferation.
