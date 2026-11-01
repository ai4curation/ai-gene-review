# FANCL (Q9NW38) review notes

Human Fanconi anemia complementation group L. HGNC:20748. Synonym PHF9. 375 aa.

## Core biology (synthesis)

FANCL is the catalytic RING-type E3 ubiquitin ligase subunit of the multiprotein
Fanconi anemia (FA) core complex. Working with the dedicated E2 conjugating enzyme
UBE2T, FANCL monoubiquitinates FANCD2 (on Lys561) and FANCI (on Lys523), the key
activating step of the FA/interstrand-crosslink (ICL) repair pathway. The
monoubiquitinated FANCD2–FANCI (ID2) complex is recruited to chromatin at stalled
replication forks / ICLs and coordinates nucleolytic incision, translesion synthesis
and homologous recombination.

Domain architecture (UniProt Q9NW38): N-terminal E2-like/ELF (UBC-like) domain,
central "DRWD"/RWD-like domain, and a C-terminal RING-type zinc finger (residues
307–363, degenerate, binds 2 Zn). The UBC-RWD region (URD, ~104–294) mediates
interaction with FANCI and FANCD2; the RING binds the E2 (UBE2T). Cys307 is essential
for ligase activity (C307A abolishes activity). Trp341 is required for UBE2T binding.

Note the UniProt CAUTION: originally reported as a PHD-type zinc finger (PubMed:12724401)
but it is actually a RING-type zinc finger; PHD fingers have no ubiquitin ligase activity.

## Key evidence / provenance

- E3 ubiquitin ligase activity; essential for FANCD2 monoubiquitination:
  [PMID:12973351 "Here we report a new component of a Fanconi anemia protein complex, called PHF9, which possesses E3 ubiquitin ligase activity in vitro and is essential for FANCD2 monoubiquitination in vivo"]. Also defines involvement in FA (disease), catalytic activity, and C307/C310 mutagenesis abolishing activity.

- UBE2T is the cognate E2 that binds FANCL (E2/E3 pair):
  [PMID:16916645 "UBE2T binds to FANCL, the ubiquitin ligase subunit of the Fanconi anemia core complex, and is required for the monoubiquitination of FANCD2 in vivo"]. W341G abolishes UBE2T binding and ligase activity.

- E3 activity determined by chromatin localization, forms active E2/E3 holoenzyme on chromatin:
  [PMID:17938197 "the actual E3 ligase activity is not determined by the assembly of the FA core complex but rather by its DNA damage-induced localization to chromatin"];
  [PMID:17938197 "FANCD2 monoubiquitination is therefore not regulated by multiprotein complex assembly but by the formation of an active E2/E3 holoenzyme on chromatin"].

- Minimal reconstitution: Ube2t + FANCL monoubiquitinate FANCD2, stimulated by RWD-like domain; FANCI restricts site-specificity:
  [PMID:19111657 "we minimally reconstitute this monoubiquitination reaction with Ube2t and the FANCL protein, revealing that monoubiquitination is stimulated by a conserved RWD-like domain in FANCL"];
  [PMID:19111657 "addition of the FANCI protein enhances monoubiquitination and also restricts it to the in vivo substrate lysine residue on FANCD2"].

- FANCL also monoubiquitinates FANCI (Lys523):
  [PMID:19589784 "We also demonstrate that FANCI can be ubiquitinated on Lys-523 by the UBE2T-FANCL pair in vitro"].

- Structure of FANCL RING–Ube2T; specific E3–E2 selection:
  [PMID:24389026 "Using the Fanconi Anemia pathway exclusive E3-E2 pair, FANCL-Ube2T, we report the atomic structure of the FANCL RING-Ube2T complex"];
  [PMID:24389026 "these specific interactions are required for selection of Ube2T over other E2s by FANCL"].

- FA nuclear core complex membership / chromatin:
  [PMID:22343915 "Fanconi anemia (FA) nuclear core complex is a multiprotein complex required for the functional integrity of the FA-BRCA pathway regulating DNA repair"].
  [PMID:20347428 "FANCM-MHF associates with the Fanconi anemia (FA) core complex, promotes FANCD2 monoubiquitination in response to DNA damage"].
  UniProt SUBUNIT: FA complex composed of FANCA, FANCB, FANCC, FANCE, FANCF, FANCG, FANCL/PHF9 and FANCM.

- ICL repair pathway (downstream of FANCD2/FANCI monoubiquitination):
  [PMID:19965384 "FANCI-FANCD2 is required for replication-coupled ICL repair in S phase"].

## Curation decisions

- MF `ubiquitin protein ligase activity` (GO:0061630): core, ACCEPT (IBA/IEA/EXP/IDA).
- MF `ubiquitin-protein transferase activity` (GO:0004842): parent of 0061630; correct but more
  general; ACCEPT (IEA/IDA/ISS).
- BP `protein monoubiquitination` (GO:0006513): core, ACCEPT.
- BP `interstrand cross-link repair` (GO:0036297): core pathway, ACCEPT.
- CC `Fanconi anaemia nuclear complex` (GO:0043240): core location/complex, ACCEPT.
- CC `chromatin` (GO:0000785): site of active E3 holoenzyme, ACCEPT.
- CC nucleus/nucleoplasm/cytosol/cytoplasm: ACCEPT nucleus/nucleoplasm; cytoplasm/cytosol
  KEEP_AS_NON_CORE (FANCL acts in nucleus/chromatin; cytoplasmic pool by similarity/ISS).
- MF `protein binding` (GO:0005515): uninformative; MARK_AS_OVER_ANNOTATED. Most are
  high-throughput Y2H (HuRI PMID:25416956/32296183; neo-PPI PMID:35512704). The
  functionally meaningful one (PMID:24389026, partner UBE2T Q9NPD8) is better captured by
  the E2-binding term.
- MF `ubiquitin protein ligase binding` (GO:0031625, IPI with UBE2T/UBE2W which are E2s):
  the partners UBE2T (Q9NPD8) and UBE2W (Q96B02) are E2 conjugating enzymes, not E3 ligases;
  MODIFY to GO:0031624 `ubiquitin conjugating enzyme binding` (verified QuickGO/AmiGO:
  "Binding to a ubiquitin conjugating enzyme, any of the E2 proteins").
- BP `DNA repair` (GO:0006281), `DNA damage response` (GO:0006974), `protein ubiquitination`
  (GO:0016567): correct general terms, ACCEPT.
- MF `ubiquitin binding` (GO:0043130): NEW (not in GOA). ELF (E2-like fold) domain binds
  free ubiquitin non-covalently via the Ile44 patch; dispensable in vitro but required for
  efficient DNA-damage-induced FANCD2 monoubiquitination in vivo. Regulatory/non-core.
  [PMID:26149689 "the ELF domain of FANCL is required to mediate a non-covalent interaction
  between FANCL and ubiquitin"]; [PMID:26149689 "the ELF domain is required to promote
  efficient DNA damage-induced FANCD2 monoubiquitination in vertebrate cells, suggesting an
  important function of ubiquitin binding by FANCL in vivo"]. Verified GO:0043130 is a
  molecular_function via QuickGO (not obsolete). Added during Affinage reconciliation.

## Affinage reconciliation (2026-07)

Affinage record (run 2026-06-09, 22 discoveries, self-eval win) is a PMID-dense narrative
fully consistent with AIGR on the core biology. Its `mechanism_profile` GO layer is coarse
(GO:0016874 ligase activity, GO:0140096 catalytic activity acting on protein, GO:0031386
protein tag activity; nucleus/nuclear chromosome/mitochondrion) — do not import directly;
AIGR's GO:0061630 + GO:0031624 + specific locations are more precise. Incorporated
PMID:26149689 (ELF ubiquitin binding, above) as the one genuine MF the review lacked.
Affinage's moonlighting claims — K11-linked β-catenin/Wnt (PMID:22653977), ligase-independent
Parkin mitophagy (PMID:35644338), germ-cell/reproduction phenotypes (PMID:12417526,
PMID:20661450) — are single-study and/or non-human organism/tissue phenotypes; AIGR correctly
scopes them out of the human GO core-function set. Not added as annotations.


## Historical scoped assessments retained below

The following entries record the separately completed target-study and database assessments before integration. Their preserved-status and source-adoption boundaries are historical; the integrated disposition follows.



## Direct evidence review, 2026-10-26

Reassessed 65 current direct contexts and their 22 historical imported reviews, plus inherited NEW47. The 44 positive Y2H screen edges are retained non-core with explicit partners. Human FANCL–UBE2T interaction supports E2 binding; generic protein binding and E3-binding labels are refined where the partner evidence is verified. The contextual SMAD4 interaction is refined to co-SMAD binding using the actual supplementary target table and pulldown image; no constitutive core role is inferred.

Current0 human FANCL chromatin/PMID:22343915 and current77 UBE2W/PMID:19111657 remain UNDECIDED at target/source level. The former paper directly supports human core membership but its inspected chromatin panel names other proteins. The latter original main could not be recovered; UBE2T has independent human structural corroboration, which must not be transferred to UBE2W. The historical collapsed old44 object records both distinct current outcomes.

The inherited ubiquitin-binding proposal remains ISS with explicit Drosophila, Xenopus and chicken evidence, without a direct human binding claim. Human E3 chemistry, chicken mutant/chromatin experiments and Xenopus functional reconstitution are kept separate. The existing core-functions/status/products remain unchanged in this lane and are for later integration. See FANCL-source-guide.md and the private packet for bounded reading, exact source identities, whole reference successors and quote-preservation checks.


## Database-source evidence reassessment — 2026-10-25

The [FANCL source guide](FANCL-source-guide.md) records exact original-paper, official rule, PAINT, HPA and Reactome locators. These assessments retain the inherited quotation text and reference associations without adding publication quotations.

The 26 current database contexts yield 18 ACCEPT, four MODIFY, three KEEP_AS_NON_CORE and one UNDECIDED. Twenty-five map to the existing review positions; the new nuclear-envelope electronic source remains a separate reviewable proposal pending deliberate source integration. Direct annotations and the inherited authored proposal remain untouched. The historical description, two core units, status and two natural products are preserved for later integrated synthesis.

The broad transferase mappings are refined to the directly demonstrated FANCL E3 activity, and broad ubiquitination to monoubiquitination. The repair refinement is supported by the performed E3 step and target/donor crosslink experiments, not partner nuclease or polymerase chemistry. Actual human FANCL assays are distinguished from mouse UBE2W and Xenopus/chicken preparations. In-vitro polyubiquitin observations are not erased by the physiological monoubiquitination emphasis.

Fresh official PANTHER v19 tree and alignment responses now verify the displayed 375-residue target and its four inherited IBDs. Earlier failed requests remain historical provenance. The additional Arabidopsis donor in the later DNA-repair IBD is a source-version difference, not a circularity argument. Conditional mouse POG–GGN1 perinuclear redistribution remains positive evidence, but the precise human nuclear-envelope inference is unresolved at the accessed original scope. Nuclear bodies and additional HPA vesicles support real compartment breadth; non-core cytoplasmic decisions do not imply inactivity.

All 11 Reactome reviews cite their originating event directly and distinguish FANCL's own compartment from the work of other participants. Their modeled 1–375 sequence does not establish equivalent activity or distribution of the natural 380-residue product. Source and product records remain unchanged.

Acquisition narrative erratum: the historical partner expansion associated with PMID:19111657 was mislabeled PMID:22343915 in one intake narrative. The actual source objects and mapping were always PMID:19111657 and are preserved. This corrects the narrative without rewriting the sealed acquisition record.


## 2026-10-26 — Integrated FANCL review and core synthesis

The [source guide](FANCL-source-guide.md) combines all 91 current imported contexts and the inherited NEW 47 ELF ubiquitin-binding proposal. There are 92 active records: 30 ACCEPT, 48 KEEP_AS_NON_CORE, 11 MODIFY, two UNDECIDED and one NEW. All 48 historical positions and 34 quotation/path/reference associations remain intact. Expanded screen contexts append; old 44 retains UBE2W UNDECIDED and the UBE2T refinement appends separately. Human chromatin current 0 remains UNDECIDED without alleging curator error. The positive conditional mouse nuclear-envelope follow-up supports current 54 KEEP_AS_NON_CORE, with tagged/coexpression/species/topology limits explicit.

The standalone description and two complementary E3-transfer/E2-recognition core facets now use human UBC–RWD/RING architecture and nuclear location. Old core quote positions remain fixed. Positive human chemistry is separated from Xenopus, chicken and mouse experiments; ELF ubiquitin recognition remains conserved ISS rather than human direct binding. The two literal natural products remain unchanged, with matched product comparisons proposed rather than assumed equivalence.

Six whole-reference unions retain both actual current read scopes and one historical note. PMID:16916645 and PMID:19111657 remain UNVERIFIED for their uninspected operative evidence, independently of verified identity and positive abstract content. Current54's two reference successors explicitly supersede prior access and U limits. All 31 historical reference identities/findings remain; eight additional references give 39. Only the three approved record_section properties from the bounded PR5481 comparison are reconciled; no other content from that PR is adopted.

The complete 41-source normal union is preserved byte-exact, with 34 selected sources and 7 private context records. Genuine current GOA91 is adopted while inherited UniProt bytes remain unchanged; the complete old source snapshot is retained in lineage evidence. No new quotation or normal publication fetch occurred during integration. Status is DRAFT pending canonical validation, ownership and publication; unresolved source contexts remain explicit.

The DNA-repair IBA precision refinement now includes structured TERM_SCOPING_PROBLEM / GRANULARITY_MISMATCH metadata. Its source entities explicitly SUPPORT_TRANSFER: the broad parent is true, the positive ancestral placement is preserved, and human self-WITH is legitimate. No residue loss, false donor or circular propagation is alleged.

## 2026-10-26 — Canonical validation

All six canonical checks pass, including GOA matching, ontology/component validation and rendering of 191 narratives. Computed status is DRAFT with 47 advisories: 44 supported generic-binding decisions and two intentional source-specific action differences. One additional advisory records the unused inherited research file. Review all 91 current imported contexts plus the inherited ubiquitin-binding proposal: 30 ACCEPT, 48 KEEP_AS_NON_CORE, 11 MODIFY, two UNDECIDED and one NEW. Retain two complementary core facets and both natural products without assuming functional equivalence. The source-specific human chromatin and UBE2W contexts remain UNDECIDED. Adopt genuine current GOA while preserving all 48 historical positions and 34 quotation/path/reference associations; append 44 partner contexts and keep UBE2W at old position 44. Preserve 31 original reference identities/findings and add eight references, yielding 39. Add UniProt section locators to three unchanged quotations. Existing UniProt, publication/Reactome/family caches, provider outputs, prior history and unrelated work remain unchanged. Four missing publication files are genuine additive fetches. No new quotation is authored; generated HTML is checked without changing the inherited file.


## 2026-10-26 — PR feedback follow-up and public evidence locators

The current source for each decision is the [FANCL biological evidence guide](FANCL-source-guide.md) and the cited publication or database record. Earlier references to a “private packet,” “current0/current54/current77,” and “old44/NEW47” are historical working labels, not external evidence identifiers. Human chromatin means GO:0000785 / PMID:22343915; conditional nuclear envelope means GO:0005635 / GO_REF:0000107, tracing to mouse Q9CR14 and PMID:12574169; unresolved UBE2W means the Q96B02 interaction in PMID:19111657. The historical combined partner annotation is the same PMID:19111657 source, and the inherited ubiquitin-binding proposal is GO:0043130 / PMID:26149689. The public guide records the operative paper sections, assay species, construct boundaries and source-specific limits without requiring access to working files. Earlier numerical labels and disposition counts remain journal history.

The experimental DNA-repair and DNA-damage-response rows now use the same GO:0036297 interstrand cross-link repair refinement as the IBA DNA-repair row. All three broad parents remain true; the refinement selects the directly supported repair process. Human PHF9/FANCL depletion, MMC chromosome damage, patient-cell complementation and purified human FANCL/UBE2T chemistry supply target evidence independently of the uninspected PMID:16916645 main. Its abstract's UBE2T phenotype is not relabelled as a FANCL experiment.

The original PMID:12574169 Methods, Results and Figure 6 caption establish tagged mouse POG/FANCL redistribution with coexpressed GGN1 in HeLa cells. Their perinuclear pattern and inferred GGN1 topology do not resolve the nuclear envelope from nearby structures. The exact human envelope inference therefore becomes UNDECIDED, while the positive mouse observation and orthology provenance remain. Full operative text was read; figure pixels remain uninspected. This supersedes the earlier KEEP_AS_NON_CORE decision on precision grounds, not on an abstract-only reading or a claim that localization is absent.

All 44 screen partner contexts remain KEEP_AS_NON_CORE. Their reasons now identify the partner and source-specific accession limit; common methods, validation limits and physiological boundaries appear once in the guide's “Screen evidence boundaries” section. UBE2W remains independently UNDECIDED, and UBE2T retains its human structural support. The ten nucleoplasm TAS rows remain ACCEPT: repeated Reactome events are shared model evidence, not independent experiments, but FANCL's own nuclear-compartment placement is consistent with its independently supported nuclear repair core. No partner nuclease, polymerase or kinase activity is transferred.

This follow-up adds no publication quotations and preserves all inherited source, quote and annotation positions, reference identities/findings, description, two core functions, two natural products and DRAFT status. Empty inherited findings remain unchanged; the reference assessments and public source guide already hold the bounded source summaries. No new biological-process or localization annotation is added.

Canonical follow-up validation: All six canonical checks pass and all 191 narratives render. Computed status remains DRAFT with 46 advisories: 44 supported generic-binding records under the explicit project instruction, one source-specific UBE2W/UBE2T action difference and one unused-research-file advisory. Current actions across 92 active objects are 28 ACCEPT, 47 KEEP_AS_NON_CORE, 13 MODIFY, three UNDECIDED and one inherited NEW. The 91 imported source contexts, 34 quotation associations, 39 references, two core functions and two natural products are preserved. The new curation history records this superseding assessment.
