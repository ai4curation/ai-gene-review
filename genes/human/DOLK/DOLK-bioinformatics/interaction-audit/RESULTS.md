# DOLK interaction audit results

The executed raw-input analysis finds 45 current GOA contexts, including 25 IPI partner/publication contexts. These join to 74 positive records among 112 incident IntAct records and represent 19 distinct partners. Both participant sequence checks match for every selected record (148 matches); the explicit assay features remain separate from those checks.

| Publication | Selected records | Partners | Validated two-hybrid records |
|---|---:|---:|---:|
| PMID:25416956 | 3 | 1 | 1 |
| PMID:26871637 | 3 | 1 | 1 |
| PMID:28514442 | 2 | 2 | 0 |
| PMID:32296183 | 63 | 19 | 19 |
| PMID:33961781 | 3 | 2 | 0 |

The historical review aggregates the IPI contexts into five publication-specific assertions. The EDA pair in the 2014 map and KCNA3 pair in the splicing study have homogeneous, independently characterized partner classes. Their binding refinements describe cytokine-partner and transporter-partner binding, respectively; neither implies receptor agonism or channel regulation. The KCNA3 assayed region is 53–575. Current canonical-sequence matching does not resolve the historical DOLK_1/DOLK_2 splice-clone sequences discussed in the original paper.

The other three historical assertions aggregate heterogeneous partners and remain contextual. EDA and KCNA3 also occur in HuRI; KCNA6 and LRRC4C recur in BioPlex and HuRI. Their different review actions reflect the scope of each historical aggregate, not contradictory judgments about the same pair. No evidence from one platform is used to turn another platform's association into a purified direct interaction. The BioPlex records identify the partners as tagged baits and DOLK as prey; that orientation is retained.

The secondary EDA run correctly reverses the target orientation and recovers six incident records with DOLK, across the 2014 and 2020 maps, with twelve matching participant checks. This checks the generic parser on a second protein within the saved query, without claiming an exhaustive EDA dataset.

- [x] Input files and target are parameters; results and biological conclusions are not hardcoded in the script.
- [x] The same script was executed with DOLK and EDA targets.
- [x] Both computed output sets were independently replayed with `--check`.
- [x] Direct machine outputs, exact source URLs and hashes are included.
- [x] Interpretation distinguishes source identity, assay coverage, repeated stages and native biological uncertainty.

The [source guide](../../DOLK-source-guide.md) gives the primary Methods and construct limits. The computational output is a source join and sequence check, not a new binding experiment.
