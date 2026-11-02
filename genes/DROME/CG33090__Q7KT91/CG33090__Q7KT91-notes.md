# CG33090 (Q7KT91, CG33090-PB) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not consulted. No `*-protnlm-*` file or prediction-evidence folder was opened.

**Folder.** Q7KT91 is the reviewed Swiss-Prot canonical product (CG33090-PB, 948 aa) of FBgn0028916. The existing `genes/DROME/CG33090/` folder is keyed to the PC isoform X2JE45, so this review lives in `genes/DROME/CG33090__Q7KT91/` (fetched with `just fetch-gene DROME Q7KT91 --alias CG33090__Q7KT91`).

**Deep research.** `just deep-research-falcon DROME Q7KT91 --alias CG33090__Q7KT91 --fallback perplexity-lite` failed. Falcon returned "Failed to authenticate", and perplexity-lite returned HTTP 401 "insufficient_quota". No deep-research file was created. The literature below was read directly from the publication cache; the sibling falcon report (`genes/DROME/CG33090/CG33090-deep-research-falcon.md`, same gene) was consulted for background only. A web search found no primary Drosophila functional study of CG33090.

**Evolutionary grounding.**
- Q7KT91 is in PANTHER PTHR12654:SF0 (NON-LYSOSOMAL GLUCOSYLCERAMIDASE), as are human GBA2 Q9HCG7 and mouse Q69ZF3 (interpro/panther/PTHR12654/PTHR12654-entries.csv). FlyBase DIOPT scores human GBA2 at 14/14.
- QuickGO `withFrom=PTN000291742` gives 374 IBA rows, all GO:0008422 beta-glucosidase activity, across plants, bacteria and metazoa. The node is therefore the family root, and beta-glucosidase is the only MF PAINT asserted there.
- PTN000291746 is a narrower node covering deuterostomes plus a few other metazoa, not insects. PAINT added GO:0007417 CNS development there. Drosophila is outside that node, so CNS development is correctly not propagated.
- Human GBA2 and mouse Gba2 have IDA glucosylceramidase (GO:0004348) and glucosylceramide catabolism (GO:0006680), but PAINT asserted neither at any PTHR12654 node. I treated this omission as deliberate, so those two IEA rows are UNDECIDED, not ACCEPT.
- Catalytic residues: the sibling RESULTS.md (MAFFT G-INS-i/L-INS-i) maps human Glu527/Asp677 to PB Glu511/Asp724. PB keeps the full N-terminal GH116 domain. In human GBA2 only the full-length isoform is active (PMID:33261081).

**Location.** UniProt gives "Cell membrane; Single-pass" (ECO:0000305), with a predicted helix at 737-753 and residues 1-736 extracellular. This contradicts:
- mouse GBA2 data [PMID:23250757 "GBA2 is not an integral membrane protein but rather is membrane-associated at the ER and Golgi."];
- fly in vivo phosphosites Ser214/Ser667/Ser669 (PMID:18327897 via UniProt ECO:0000269), which lie in the predicted "extracellular" region.

FlyBase records the polypeptide in adult-head membrane-fraction proteomics (Aradska et al. 2015). Plasma membrane is MARK_AS_OVER_ANNOTATED. The general membrane term is accepted.

**Fly phenotypes (FlyBase).** GD12248/GD13484 RNAi with several drivers is viable, and insertion 5-HA-2418 is male-fertile. Neither is used as process evidence.

**Decisions.**

| Term | Evidence | Action |
|---|---|---|
| GO:0008422 beta-glucosidase activity | IBA, ISS | ACCEPT (core) |
| GO:0004553 hydrolase activity, hydrolyzing O-glycosyl compounds | IEA | MODIFY to GO:0008422 |
| GO:0004348 glucosylceramidase activity | IEA | UNDECIDED |
| GO:0006680 glucosylceramide catabolic process | IEA | UNDECIDED |
| GO:0005975 carbohydrate metabolic process | IEA | MARK_AS_OVER_ANNOTATED (consistent with the X2JE45 review) |
| GO:0008206 bile acid metabolic process | ISS | REMOVE |
| GO:0016139 glycoside catabolic process | ISS | MARK_AS_OVER_ANNOTATED |
| GO:0046527 glucosyltransferase activity | ISS | MARK_AS_OVER_ANNOTATED |
| GO:0005886 plasma membrane | IEA | MARK_AS_OVER_ANNOTATED |
| GO:0016020 membrane | IEA, ISS | ACCEPT |

- Bile acid metabolic process is removed because insects have no bile acid pathway, mouse KO bile acid metabolism is normal (mouse NOT IMP), and PAINT did not propagate it.
- Glucosyltransferase activity is mammalian in vitro transglucosylation only.
- No NEW terms.

**For transfer to the benchmark (X2JE45).** The only function supported by phylogeny for this gene is beta-glucosidase activity (IBA, PTN000291742). Nothing is experimentally established in Drosophila: no enzyme assay, no localization, no lipid phenotype. The glucosylceramide substrate, ER/Golgi localization and transglucosylation are vertebrate-only.
