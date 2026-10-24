# CG33090 evidence notes

X2JE45 is native PC (799 aa) of [FBgn0028916](https://flybase.org/reports/FBgn0028916), distinct from PB/Q7KT91 (948 aa), PD/X2J9U5 (946 aa), and PE/X2JAF7 (923 aa). All two GOA rows attached to the exact accession are reviewed. The benchmark did not accidentally substitute a foreign sequence.

The [reproducible analysis](CG33090-bioinformatics/RESULTS.md) finds PC residues 29–799 identical to PB residues 178–948, with catalytic E362/D575 retained. Both independent MAFFT strategies recover those sites. The alteration overlaps the N-terminal GH116 domain, which is a specific reason to investigate native PC activity rather than simply accept or reject a family-derived name.

[PMID:25344605](https://doi.org/10.1074/jbc.M114.593376) experimentally establishes human E527/D677 as the catalytic pair. Its abstract is cached; the primary full-text search result supplies the precise residue designation. [PMID:33261081](https://pmc.ncbi.nlm.nih.gov/articles/PMC7761373/) is cached with full text and reports: “Thus, all human GBA2 isoforms were expressed but only isoform 1 clearly hydrolyzed the MUG substrate.” The tested N-terminal human alterations are not the same as PC. They demonstrate the importance of considering the whole isoform, not that PC must be inactive. The broad glycosyl-hydrolase prediction is UNC for this sequence.

The ancillary ProtNLM name points to non-lysosomal glucosylceramidase and its locations to ER/Golgi membranes. These are reasonable family-context leads for the longer protein, but their PC-specific relevance depends on protein folding and localization; mammalian bile-acid metabolism is not transferred to a fly protein. The original name, scores, locations and donors remain intact in CG33090-predictions-source.json.

Falcon completed in 343.06 seconds and was inspected. It independently identified the human isoform-activity study PMID:33261081 as relevant, but did not compare the exact 799-residue native PC sequence with the longer fly PB product. Its broad family-level glycosidase discussion is therefore supplemented by the explicit native-isoform analysis. The unresolved verdict concerns this target's altered N-terminal architecture, not an automatic demand for direct fly assays before accepting conserved functions.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not consulted. Earlier text in this file is left unchanged.

**Identity.** X2JE45 is the native CG33090-PC isoform (FBpp0310264, 799 aa) of FBgn0028916. The gene's other products are PB/Q7KT91 (948 aa, the reviewed Swiss-Prot entry), PD/X2J9U5 (946 aa) and PE/X2JAF7 (923 aa); FlyBase lists them in CG33090-flybase.txt. PC is an alternative N-terminal isoform, not a fragment and not a wrong gene model. PC residues 29-799 are identical to PB 178-948, and PB 1-177 is replaced by a distinct 28-residue N terminus.

**New mapping.** See [RESULTS-rereview.md](CG33090-bioinformatics/RESULTS-rereview.md) and `map_isoform_boundary_rereview.py`, which reuse the existing alignments. In both alignments PC position 29 corresponds to human GBA2 position 194, so PC has no counterpart for human residues 1-193. PC's own Pfam matches are GH116_N 51-296 and GH116 catalytic 356-787. Both catalytic residues are retained (PC E362 = human E527; PC D575 = human D677).

**Key literature point.** In PMID:33261081 a six-residue insertion in an N-terminal-domain beta-strand between human residues 189 and 190 (isoform X1) abolished activity: "indicating that the structural integrity of the N-terminal domain is also critical to the activity." That position lies inside the region PC lacks. This strengthens the case for leaving PC's activity unresolved, but it is not proof of inactivity.

**Evolutionary grounding.** X2JE45 and Q7KT91 both carry PANTHER PTHR12654:SF0, the same subfamily as human Q9HCG7, mouse Q69ZF3 and rat Q5M868 (interpro/panther/PTHR12654/PTHR12654-entries.csv). DIOPT gives 14/14 for human GBA2 (FlyBase). At gene level FlyBase shows an IBA for beta-glucosidase activity from PTN000291742, but no IBA for glucosylceramidase activity or glucosylceramide catabolic process. I treated that omission as a deliberate PAINT choice and did not propose either term. In GO, glucosylceramidase activity (GO:0004348) is not an is_a child of beta-glucosidase activity (GO:0008422): both sit under GO:0004553 (checked with runoak ancestors).

**Decisions.**
- GO:0004553: kept UNDECIDED, with the reason updated using the new boundary mapping. The family chemistry is right for the gene, but the exact PC isoform is unresolved.
- GO:0005975: UNDECIDED changed to MARK_AS_OVER_ANNOTATED. It is a generic six-hairpin-glycosidase superfamily mapping. Glucosylceramide catabolism falls under lipid and carbohydrate-derivative metabolism, not carbohydrate metabolic process.
- core_functions: added the gene-level expectation (beta-glucosidase activity, GO:0008422) with an explicit isoform caveat. No location was asserted: the human ER/Golgi localization comes from mouse data, and the PC N-terminal change could affect membrane association.
- No NEW annotations were added. A knowledge gap and experiments were added for isoform-resolved activity and in vivo lipid substrates.

**Relative.** The canonical product of the same gene is Q7KT91 (CG33090-PB, Swiss-Prot reviewed). The repo has no review for it, because genes/DROME/CG33090 is keyed to X2JE45. A review of the canonical product would go in genes/DROME/CG33090__Q7KT91. The human ortholog GBA2 (Q9HCG7) also has no review in the repo.

**Family/modules.** interpro/panther/PTHR12654/PTHR12654-review.yaml places X2JE45 in SF0, which agrees with UniProt; no placement disagreement. No module under modules/ includes GBA2 or CG33090. modules/glycosphingolipid_lysosomal_degradation.yaml is the related lysosomal (GBA1) pathway, but GBA2 is non-lysosomal and is not a member of it.
