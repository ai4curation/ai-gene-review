# FANCA (FANCA) — AIGR vs Affinage

**Affinage record:** run 2026-06-09 · 29 discoveries · self-eval **win** · gates **passed**.

## Agreement (brief)
- Both place FANCA as a non-catalytic scaffold/organizer of the FA core complex whose
  functional pool is nuclear, required for assembly, stability, nuclear accumulation and
  chromatin loading of the complex that monoubiquitinates FANCD2–FANCI.
- Both anchor the same partner network (FANCG, FANCF, FANCC, FAAP20) and the same core
  process (interstrand cross-link repair / the FA–BRCA pathway), citing an overlapping set
  of foundational PMIDs (9398857, 11063725, 22266823, 22343915).
- Both agree the cytoplasmic pool is a minor/pre-assembly location, not the functional site.

## Disagreements
| Topic | Affinage says | AIGR review says | Verdict (who is right + why) |
|---|---|---|---|
| Molecular activity grounding | `mechanism_profile` lists coarse MF parents: DNA binding, RNA binding, `catalytic activity, acting on DNA` (GO:0140097), `molecular adaptor activity` (GO:0060090), `structural molecule activity` (GO:0005198) | Specific curated core MF: `protein-macromolecule adaptor activity` (GO:0030674) with the scaffold role in `core_functions` | **AIGR** for the primary function. GO:0030674 is a precise child of the adaptor parent Affinage emits; `structural molecule activity` and the bare `catalytic activity, acting on DNA` are lossy/misleading down-casts. But Affinage's DNA/RNA-binding terms flagged a genuine gap (see below). |
| Intrinsic nucleic-acid binding | FANCA binds nucleic acids (RNA > ssDNA > dsDNA) via its C-terminal domain (PMID:22194614) | Not annotated anywhere in the review | **Affinage surfaces a real gap.** Verified in full text: purified FANCA, EMSA, patient truncation Q772X deficient. Incorporated as NEW `single-stranded DNA binding` (GO:0003697), non-core. |
| Single-strand annealing / strand exchange (RAD52-like) | FANCA directly catalyzes SA and SE comparable to RAD52 and acts in the SSA sub-pathway of DSB repair independently of the canonical FA pathway (PMID:30057198) | Not annotated; review covers only ICL repair / DNA repair | **Real but bounded.** Mol Cell 2018, purified protein + homodimer requirement + six deficient patient mutants + CRISPR/siRNA cell assays. Genuine and disease-relevant, yet single-lab (Zhang group) and not adopted by GO curators. Incorporated as NEW `double-strand break repair via single-strand annealing` (GO:0045002), explicitly non-core — not elevated to a core function. |
| RNA binding (GO:0003723) | Emitted as an MF term; narrative notes RNA affinity > DNA | Absent | **Neither annotated.** Kept out deliberately: even the source paper concedes "there is currently limited information to explain how the RNA-binding activity of FANCA could be linked to its functions." Documented in the reference notes, not annotated — a correct conservative call. |
| Centrosome / mitotic-spindle role | Narrative asserts FANCA localizes to centrosomes/PCM and maintains spindle-assembly-checkpoint function (PMID:23806870, PMID:26366677) | Not in the review | **Left out (defensible).** These are real papers but a peripheral, pleiotropic activity not in the curated GOA; consistent with AIGR's scope discipline. Not incorporated (conservative). |
| ATR-S1449 / NEK2-T351 phosphoregulation | Narrative highlights DNA-damage-induced ATR phosphorylation and NEK2 centrosomal phosphorylation | Not annotated | **Regulation of FANCA, not a function of FANCA.** Correctly excluded by AIGR — these describe upstream regulation, not a GO function/process/component for FANCA itself. |
| `protein binding` (GO:0005515) IPI annotations | Would collapse the whole hub into generic binding / adaptor | 18 GO:0005515 IPI calls MARK_AS_OVER_ANNOTATED; hub role captured once as GO:0030674 | **AIGR** — the curated treatment (informative adaptor MF + over-annotation flags) is strictly better than a generic-binding collapse. |

## Papers incorporated into the review
| PMID | Supports | How used (supporting_text / reference / NEW annotation) |
|---|---|---|
| PMID:22194614 | Intrinsic ssDNA/nucleic-acid binding | Added to `references` (reference_review MEDIUM/VERIFIED) + NEW annotation `single-stranded DNA binding` (GO:0003697, IDA, non-core) with two verbatim `supported_by` quotes |
| PMID:30057198 | SA/SE (RAD52-like) role in SSA DSB repair | Added to `references` (reference_review MEDIUM/VERIFIED) + NEW annotation `double-strand break repair via single-strand annealing` (GO:0045002, IMP, non-core) with two verbatim `supported_by` quotes |

Not incorporated (deliberately): PMID:23806870, PMID:26366677 (centrosome/spindle), PMID:19109555
(ATR-S1449), PMID:24799500 (SHM/CSR), PMID:25015289 (CXCR5 neddylation), PMID:20864535 (NPMc) —
peripheral/pleiotropic or regulatory activities not in the curated GOA; excluding them is the
conservative, scope-appropriate call. Most of Affinage's remaining PMIDs are already cited by the
review.

## Net assessment
The review is **modestly better** after reconciliation. AIGR was already stronger than Affinage on
the primary function (a precise adaptor MF and disciplined over-annotation handling versus Affinage's
coarse, sometimes wrong-branch `mechanism_profile`). Affinage's real value here was its dense
narrative, which surfaced one genuine gap the curated review had missed: FANCA's intrinsic
nucleic-acid binding and RAD52-like SA/SE activity in the SSA branch of DSB repair. These are
well-controlled (purified protein, disease-mutant correlation, cell assays) but single-lab and not
yet adopted by GO curators, so they were added as two NEW **non-core** annotations rather than
promoted to core functions — capturing the finding without overstating FANCA's canonical scaffold
identity.
