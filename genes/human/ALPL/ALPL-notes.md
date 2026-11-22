# ALPL (human) — review notes

UniProt: P05186 · HGNC:438 · TNAP / TNSALP / AP-TNAP · EC 3.1.3.1 (and EC 3.9.1.1 by
similarity to mouse P09242).

## What the protein is

GPI-anchored (Ser501, `LIPID 501 /note="GPI-anchor amidated serine"` in the UniProt
record), N-glycosylated, obligate-homodimeric alkaline phosphomonoesterase on the outer
leaflet of the plasma membrane. Belongs to the alkaline phosphatase family (IPR001952,
PF00245).

Ecto-orientation was settled experimentally in human fibroblasts by three independent
arguments [PMID:2220817, "Normal fibroblast ALP is linked to the outside of the plasma
membrane, since in intact cell monolayers (1) dephosphorylation rates of the
membrane-impermeable substrates PEA and PLP in the medium at physiologic pH were similar
to those observed with disrupted cell monolayers, (2) brief exposure to acidic medium
resulted in greater than 90% inactivation of the total ALP activity, and (3) digestion
with phosphatidylinositol-specific phospholipase C (PI-PLC) released about 80% of the ALP
activity."]. This is the fact that GOA does not record — every location row says "plasma
membrane" and none says which face — hence the proposed GO:0009897 annotation.

Metal centre: two Zn(2+) plus one Mg(2+) in the catalytic site, and a separate
mammalian-specific structural Ca(2+) site. Now directly observed in human TNAP structures
[PMID:41145834, "The same divalent cations were identified, including the three essential
cations in the catalytic site (two zinc ions and one magnesium ion), along with a calcium
ion at the CA cluster, as seen in the apo structure of the enzyme (PDB codes 7YIV or
7YIW)."]. GOA has calcium ion binding but no zinc or magnesium term — a clear gap, hence
two more proposed NEW rows.

The calcium site is structural, not catalytic; the UniProt DOMAIN comment says
"Calcium-binding is structural and does not influence the [activity]". That is why the
existing GO:0005509 IDA is marked KEEP_AS_NON_CORE rather than ACCEPT.

Dimerisation is a functional requirement, not incidental oligomerisation. N417S is
glycosylated and surface-delivered yet monomeric and dead [PMID:23688511, "Importantly,
this mutant failed to assemble into a dimer structure, which is needed for the catalytic
function of TNSALP, as evidenced by newly developed SDS-PAGE as well as
sucrose-density-gradient centrifugation."], and P108L behaves the same way independently
[PMID:25982064, "Importantly, TNSALP (WT) largely formed a functional dimeric structure,
while TNSALP (P108L) was found to be present as a monomer in the cell."]. This is what
makes dominant hypophosphatasia possible, e.g. G82R [PMID:33821301, "TNSALP with the novel
ALPL mutation (c.244G > A p.Gly82Arg) completely lost its enzymatic activity and suppressed
that of wild-type TNSALP, corroborating its dominant negative effect."]. Normally I would
avoid a protein-binding term, but GO:0042803 here is the only annotation that explains the
dominant inheritance, so it was added.

## Substrate hierarchy

Broad specificity, but the physiologically important substrates are few, and the mutant
panel in PMID:12162492 shows the branches are genetically separable — some alleles keep
PPiase and lose PLPase activity ["Three mutations ( E174G, E174K, and E281K) were found to
retain normal or slightly subnormal catalytic efficiency toward pNPP and PPi but not
against PLP."], which maps onto the skeletal versus seizure arms of the disease.

- **PPi** — core. Removing the hydroxyapatite-propagation inhibitor is the reaction that
  explains hypophosphatasia. In matrix vesicles TNAP is the responsible enzyme
  [PMID:19874193, "We conclude that TNAP is the enzyme that hydrolyzes both ATP and PP(i)
  in the MV compartment."].
- **PLP** — core. Gates cellular vitamin B6 uptake; basis of B6-responsive seizures.
- **Phosphoethanolamine / phosphocholine** — promoted to core on the strength of the 2025
  paper [PMID:41145834, "Recombinant TNAP hydrolyzes phosphocholine and phosphoethanolamine
  with similar efficiency than PPi."] plus its physiological readout ["In summary, TNAP is
  the phosphatase enabling cellular choline uptake during fasting, participating in hepatic
  lipid metabolism."]. PEA has been known as a TNAP substrate since 1990 and is a
  diagnostic marker; what is new is the choline/VLDL link and the kinetic parity with PPi.
- **ATP / ADP / AMP** — real but ancillary; shared with ENPP/CD39/CD73. Kept non-core.
- **N-phosphocreatine** — mouse only (futile creatine cycle in thermogenic fat). Kept
  non-core across all five related rows (GO:0005758, GO:0031966, GO:0050187, GO:0140651,
  GO:0120162), since every human annotation for these is ISS or IEA from mouse P09242.

## The one REMOVE: GO:0140928

`GO:0140928 inhibition of non-skeletal tissue mineralization` (IEA, GO_REF:0000107,
involved_in) is directionally inverted. Tracing the propagation: the human IEA comes from
Ensembl Compara transfer; the seed is a mouse Alpl IDA from PMID:21490328. I pulled that
abstract — it says "Overexpression of TNAP increased calcification of cultured aortas" and
"Hydrolysis of PP(i) was reduced 25% by β,γ-methylene-ATP and 50% by inhibition of TNAP".
So TNAP promotes ectopic calcification by destroying PPi; the paper's *inhibitory* arm is
about NPP1 and ANK, which appear on the same term legitimately.

Independent human-relevant confirmation of the direction [PMID:28592560, "A selective and
orally bioavailable TNAP inhibitor prevented calcification in ABCC6 mutant cells in vitro
and attenuated both the development and progression of calcification in Abcc6-/- mice in
vivo, without the deleterious effects on bone associated with other proposed treatment
strategies."]. An inhibitor that blocks the process cannot be blocking a protein that
performs it.

Checked GO for a term in the opposite direction — searched "mineralization" via QuickGO;
there is no "promotion of non-skeletal tissue mineralization" and no ectopic-calcification
term other than GO:0140928 itself. Hence a `proposed_new_terms` entry rather than a MODIFY.

## Other non-obvious calls

- **GO:0001649 osteoblast differentiation (HDA, PMID:16210410)** →
  MARK_AS_OVER_ANNOTATED. The paper measures a 27-fold rise in ALP abundance during
  induced differentiation. That makes ALPL a differentiation marker; it does not show
  participation. In Alpl-null models osteoblasts differentiate and deposit osteoid — what
  fails is mineralisation of it.
- **GO:0016462 pyrophosphatase activity** (three rows) → MODIFY to GO:0004427. Confirmed
  via QuickGO that GO:0004427 is a descendant of GO:0016462. The experiments measured
  inorganic PPi specifically, and the broad parent also covers nucleoside triphosphatases,
  which is a different physiological story.
- **GO:0001501 skeletal system development (TAS)** → MODIFY to GO:0030282. HPP is a
  mineralisation disorder, not a patterning disorder.
- **GO:0016791 phosphatase activity** (InterPro2GO) and **GO:0016020 membrane** (HDA) →
  MODIFY to the specific terms both are parents of.
- **GO:0071529 cementum mineralization** → ACCEPT, not non-core. Premature loss of primary
  teeth is a major HPP diagnostic criterion and acellular cementum is the tissue that
  fails, so this specific term has direct human clinical support.
- **GO:0065010 extracellular membrane-bounded organelle, is_active_in** → ACCEPT. This is
  the matrix vesicle, a genuine second site of action, distinct from the two GO:0070062
  extracellular-exosome rows which are untargeted proteomic inventory hits and were kept
  non-core.
- **GO:0016887 ATP hydrolysis activity** → KEEP_AS_NON_CORE rather than REMOVE. TNAP does
  hydrolyse ATP, but the term normally connotes energy-coupled ATPases; flagging non-core
  records the chemistry without implying TNAP is an ATPase.
- The six `response to X` rows (LPS, insulin, vitamin B6, M-CSF, glucocorticoid, sodium
  phosphate) all describe regulation *of* ALPL, not function *of* ALPL. Kept non-core;
  none has evidence against it.

## The other three isozymes

ALPI, ALPP and ALPG were reviewed in the same pass; see their own notes files. Decisions
taken consistently across all four:

- `GO:0016791 phosphatase activity` (InterPro2GO) → MODIFY to `GO:0004035` in every gene.
  The signature that generates it is the alkaline phosphatase domain itself, so the parent
  term throws away what the signature actually says.
- `GO:0009897 external side of plasma membrane` proposed as NEW in all four. Every gene has
  plasma-membrane rows and none records which face, although ecto-orientation is what makes
  these enzymes act on extracellular substrates. Evidence differs per gene: PMID:2220817
  (ALPL, PI-PLC + membrane-impermeable substrates), PMID:29567797 (ALPI, flow cytometry of
  a GPI-signal truncation), PMID:2153284 (ALPP, the saturation mutagenesis that worked out
  GPI attachment at Asp-484), PMID:2162249 (ALPG, PI-PLC release of the Nagao isozyme).
- `GO:0042803 protein homodimerization activity` proposed as NEW in all four. Normally a
  binding term would not earn a place, but the dimer is functionally load-bearing family-wide:
  ALPL monomeric mutants are dead and dominant-negative, the ALPP structure credits the
  interface with mammalian-specific allostery, and ALPI disease alleles act partly by
  impairing dimerization.
- Metal terms: ALPL was missing zinc and magnesium; ALPP and ALPI have them but not calcium;
  ALPG had no metal term at all. Proposed the missing ones in each, with IDA where a human
  structure resolves the metal (ALPL, ALPP) and ISS where it was resolved in a paralogue
  (ALPG).
- Interactome-derived `GO:0005515 protein binding` rows on ALPI and ALPP →
  MARK_AS_OVER_ANNOTATED. All are binary Y2H maps and the partner lists are dominated by
  keratin-associated proteins.

The contrast in what can be *asserted* is the main finding of doing all four together. ALPL
supports three core functions with named substrates and processes. ALPI supports one, with
LPS and TLR4 attached, on Mendelian evidence GOA has not yet cited. ALPP and ALPG support
only chemistry and topology — no physiological substrate is known for either — so their core
functions carry a `knowledge_gaps` entry and no `directly_involved_in`, which is the honest
representation rather than an omission.

## Process notes

- `just deep-research-falcon` failed twice before working: first a uv HTTP timeout
  (fixed with `UV_HTTP_TIMEOUT=300 uv sync`), then `uvx` resolving Python 3.11 while
  deep-research-client requires >=3.12. Worked around with
  `DEEP_RESEARCH_CLIENT_CMD="uvx --python 3.13 --from deep-research-client[cyberian]==0.2.7rc1 deep-research-client"`.
  Worth fixing in `scripts/deep_research_wrapper.py` so the uvx invocation pins a Python.
- No OLS MCP was available in this session; GO term definitions, ancestry and the
  GO:0140928 annotation provenance were checked against the QuickGO REST API instead.
- All 14 cited PMIDs are cached. Ten are abstract-only; PMID:19874193, PMID:28592560,
  PMID:41145834 and PMID:23533145 have full text. No experimental annotation was
  overruled on the basis of an abstract-only cache.

## 2026-09-27: independent full annotation audit

The preceding entries are the earlier review journal. This audit rechecked all 71 machine-seeded assertions and four prior authored proposals against actual source material and term definitions. It supersedes the earlier judgments about mouse-only phosphocreatine chemistry, calcium-binding core status, ATP-hydrolysis terminology, broad skeletal development and the redundant external-membrane NEW. The raw UniProt/GOA, genuine Falcon report and its artifact remain unchanged. A fresh normal Falcon attempt with configured perplexity-lite fallback ran in parallel with ordinary publication caching; the provider failed on DNS before producing a report, while normal seeded-publication caching completed. Manual primary research is recorded here, not under a fabricated provider filename.

### Catalytic and compartment evidence

[PMID:12162492] directly assays affinity-purified human TNAP variants expressed as soluble tagged proteins in COS-1 cells. Its abstract exposes pNPP assays at pH 9.8 and PPi/PLP measurements at physiological pH. The substrate-selective mutant results distinguish chemical activities; they do not alone assign the clinical phenotype of each allele. The abstract-only local status is retained.

The full [PMID:19874193] separately measures soluble **human** TNAP kinetics and **mouse** osteoblast matrix-vesicle function. Human ATP, ADP and PPi hydrolysis at pH 7.4 are direct target assays. Mouse matrix-vesicle AMP-to-adenosine/nucleotide turnover and genotype effects are not relabeled as purified human kinetics. PPi removal and nucleotide-derived Pi belong to one mineralization mechanism. Broad alkaline-phosphatase and ADP/AMP activity rows can therefore remain core at their respective resolution without generating separate redundant core entries.

The live [GO:0016887 page](https://amigo.geneontology.org/amigo/term/GO:0016887) carries an ATP-powered-reaction usage comment and a part_of relation to ATP-dependent activity. TNAP consumes ATP as a phosphatase substrate; these experiments do not show coupling its energy to another operation. The two existing ATP-hydrolysis rows are refined to the immediate reaction parent [GO:0017111](https://amigo.geneontology.org/amigo/term/GO:0017111), with ATP retained explicitly as the assayed substrate. This preserves the positive chemistry and raises the ontology convention as a question. The reaction-specific phosphoamidase term [GO:0050187](https://amigo.geneontology.org/amigo/term/GO:0050187) is exactly phosphocreatine-to-creatine/Pi despite its broad label.

The full [PMID:33981039] explicitly assays recombinant **human** TNAP (R&D 2909-AP) on phosphocreatine at pH 7.8 and 37 degrees C. Thus the earlier blanket “mouse only” classification of this molecular activity is incorrect. Its detailed mitochondrial fractionation, knockout-controlled microscopy, protease protection, APEX2 and thermogenic flux experiments use mouse TNAP, mouse adipocytes and mice. Human catalytic activity is now an MF-only core; transferred mouse mitochondrial locations and thermogenic processes remain positive contextual annotations. No human mitochondrial localization or thermogenic-flux NEW is proposed. The current [PMID:42020733] abstract adds glycerol-dependent allosteric regulation and variant/association context, but its complete Methods/Results were not recovered; no new glycerol-binding assertion is inferred.

The full [PMID:41145834] directly establishes human PC/PEA chemistry: human residues 18–500 expressed in Expi293F, purified-enzyme kinetics at pH 9.0, human serum from six donors at pH 7.4 and HuH-6 surface hydrolysis. The mouse enzyme preparation is separately commercial. Seven-day cell growth/DNA rescue by choline versus phosphocholine supports substrate availability but is not direct labeled uptake. Whole-animal fasting, hepatic lipid and metabolite findings are mouse; liver/blood ethanolamine was below detection while kidney changes were measured. TNAP performs dephosphorylation, not membrane transport or direct lipoprotein secretion.

This 2025 paper's actual structural observations support the two Zn ions, Mg, separate Ca site and dimer. The [human 9SH5 deposition](https://www.rcsb.org/structure/9SH5) is associated with that study; 7YIV/7YIW are earlier models. PC/PEA orientations are docking predictions, phosphate occurs in the crystallization condition and inhibitor cryo-EM supplies actual ligand density. The older [PMID:11395499] is a TNAP homology model built from placental AP plus metal analysis, not an atomic TNAP structure. Structural Ca binding is retained as core, since a functional structural site need not itself cleave the substrate.

### Annotation-specific calibration

The [PMID:2220817] human fibroblast evidence directly resolves external orientation using membrane-impermeable substrates, acid inactivation and PI-PLC release. Its existing plasma-membrane row is refined to external side of plasma membrane; the prior authored NEW for that same location is withdrawn under the ancestor/descendant redundancy rule. Other genuine broad membrane assertions stay at their justified source resolution. Ordinary source qualifiers remain unchanged and are not treated as separate evidence.

[PMID:16210410] full Methods/Results were recovered from the [original author upload](https://www.researchgate.net/publication/7556010_Differential_Expression_Profiling_of_Membrane_Proteins_by_Quantitative_Proteomics_in_a_Human_Mesenchymal_Stem_Cell_Line_Undergoing_Osteoblast_Differentiation) after both publisher HTML and PDF routes failed. Human hMSC-TERT cells received 10 nM calcitriol and were analyzed at day 4. ALPL has 9% sequence coverage and greater than 27-fold induction in postnuclear/postmitochondrial membrane material, with catalytic histochemical confirmation. This is real target evidence. The complete main Methods/Results inspected do not perturb ALPL or establish it as performing a step in acquisition of osteoblast identity. The differentiation HDA remains over-annotated on that source-specific basis; the membrane HDA remains ACCEPT at its actual broad fractionation resolution. Neither conclusion says that ALPL can never affect differentiation. The paper discusses early lineage commitment and heterogeneity rather than fully mature mineralizing osteoblasts. The local cache remains abstract-only despite this external read.

The full [PMID:28592560] and the available abstract/Discussion of [PMID:21490328] support a directional challenge to inhibition of non-skeletal mineralization: TNAP overexpression increases aortic calcification, while TNAP inhibition reduces calcification in the human ABCC6-mutant fibroblast/mouse models. The PPi-generating inhibitory arm belongs to NPP1/ANK. This positive counterevidence supports REMOVE for the transferred inhibition term. It is not a general claim that inhibitor effects always settle sign or that no indirect protective ALPL effect is possible. No unverified opposite-direction GO term is invented.

The broad skeletal-system-development TAS from [PMID:9781036] remains ACCEPT: skeletal development includes mineralization and is not confined to pattern formation. The dental cementum transfer has a traced rat source [PMID:17043865], whose primary abstract measures histochemical spatial/activity relationships; independent human mineralization chemistry and clinical dental context support the curated biological inference. The rat paper is not described as an ALPL perturbation or a newly read human experiment.

The primary urinary-exosome Table 1 in indexed full PMC2637050/[PMID:19056867] names ALPL with three unique peptides and four identifications. This positive hit supports NON_CORE localization. The ALPL-specific supplementary row in [PMID:23533145] remains unrecovered despite a local body extraction, so that distinct source row is UNDECIDED. Neither row is rejected as contamination or from the paper title. The Reactome GPLD1 model makes GPLD1 the GPI-cleaving enzyme; ALPL is an anchored substrate, with independent human evidence for membrane and soluble extracellular TNAP.

### Donor and proposal checks

The actual PAINT IBD rows in PTHR11596 were inspected: PTN000174527 for alkaline phosphatase, PTN000904735 for plasma membrane and PTN002613308 for bone mineralization. Human target inclusion among experimental descendants is legitimate for the first assertion. The bone node's listed experimental descendants are mouse and zebrafish, not human; independent human evidence corroborates it without claiming a new phylogenetic reconstruction.

The [MGI comparative Alpl graph](https://www.informatics.jax.org/homology/GOGraph/Alpl) resolves response-source chains to rat [PMID:11810315] (LPS/surfactant activity without TNAP mRNA induction), [PMID:20818503] (diabetes/insulin reversal), [PMID:7669437] (CSF-1 correction of osteoblast ALP expression in toothless rats) and [PMID:2039500] (dexamethasone-responsive alternative promoters). Mouse [PMID:7550313] supplies B6-related physiology; full [PMID:23523568] supplies vascular-cell phosphate culture context. These are positive contextual response assertions. They do not make ALPL the hormone receptor, transcription factor or every downstream protective effector.

Three prior authored NEW MF proposals remain: zinc binding, magnesium binding and homodimerization. Human structural metal/dimer observations and the source-specific human N417S/P108L experiments [PMID:23688511], [PMID:25982064] provide positive support; the latter papers are not claimed to be independent laboratories. Existing ALPI/ALPP metal annotations provide same-family context, not the primary proof. The current ALPL seeded rows contain no ancestor/descendant metal-binding assertion that makes Zn or Mg redundant; calcium is a distinct ion. No seeded dimer assertion duplicates the retained proposal. The local GO-CAM index has no P05186 model to contradict this synthesis. No NEW biological process is added: TNAP's catalytic participation, rather than disease necessity alone, supports the existing mineralization and metabolite-process rows.

### Complete source inventory and remaining cache gates

The preserved provider and artifact contain eight distinct DOI publications. These resolve to [PMID:33919113], [PMID:33477631], [PMID:39728440], [PMID:31413732], [PMID:37982855], [PMID:40100438], [PMID:36699639] and [PMID:39872235]. The actual 39728440 review is already cached. Reviews/consensus/clinical-management papers are assessed as secondary context; the AAV8-TNAP-D10 paper is a mouse therapy study, with construct species not guessed from the host. The raw UniProt citation strings replayed in the provider's input prompt (23039266, 3532105, 8406453) are inherited template metadata, not additional scientific assertions or authored bibliography reliance. The original ALPI/ALPP/ALPG comparison citations in these notes are retained and explicitly assessed as paralog comparisons.

The finite required missing list is **13 PMIDs**: 2039500, 7669437, 11810315, 17043865, 20818503, 31413732, 33477631, 33919113, 36699639, 37982855, 39872235, 40100438 and 42020733. Their primary identities/DOIs and available abstract scope were independently verified. One normal 13-ID cache attempt ended with exit 1, cached 0/13, because of DNS failure; no local record was fabricated. The exact terminal receipt and raw-log hash are in `tmp/ALPL-full-audit/additional-normal-fetch-receipt.json`. These source gates keep the review DRAFT even when primary web abstracts or external bodies are readable. The pending recovery inventory must remain fixed until a separate reviewed revision.

The resulting 74 rows comprise all 71 immutable seeded assertions plus the three retained prior NEW MFs. The compact synthesis has four units: PPi/nucleotide mineralization, PLP dephosphorylation, PC/PEA metabolism and the directly measured human phosphocreatine activity. It contains no separate transport or human thermogenic-core assertion. Final schema/reference/quote, source/isoform, history and render checks are recorded with the handoff after independent review.

Full validation completed successfully with four warning groups: the 13 required cache gaps, source-specific plasma-membrane refinement, differing exosome source access and no citation to the preserved provider report. The latter is intentionally retained as independently assessed background rather than cited merely to silence an advisory. All 90 ordinary supporting excerpts match their actual caches; all 71 machine-sourced objects and three alternative products remain unchanged. Rendering and scaffolded history validation also passed. The root independent biological read accepted all 74 decisions, 44 reference assessments and four core units; cache closure and any later scientific changes remain separately reviewable.

## 2026-09-27: source24 closure after exact normal-record recovery

This entry closes the 13 cache gates listed in the preceding audit. The normal hosted fetch recovered all 13 records, and the coordinator imported their exact bytes after archive, identity, actual-access and no-overwrite checks. The original failed local attempt remains historical provenance; it is not the current access state. The earlier frozen review, source/provider bytes and history are preserved. The current recursive census includes the authored YAML, all prior notes and both genuine Falcon outputs, with decoded DOI/PMCID matching to the actual caches. No identified required PMID or Reactome cache remains missing.

Five donor studies remain **abstract-only**: [PMID:2039500], [PMID:7669437], [PMID:11810315], [PMID:17043865] and [PMID:20818503]. Their exact normal abstracts now directly support the respective contextual response or spatial/activity statements. All are rat experiments. Dexamethasone, CSF-1 and insulin regulate measured ALP expression or activity; that does not assign hormone-receptor or transcription-factor activity to ALPL. The LPS study distinguishes heavy-surfactant TNAP activity from TNAP mRNA, which was not induced, and does not isolate direct TNAP-catalyzed LPS dephosphorylation. The cementum study supplies histochemical activity/localization, not an ALPL perturbation experiment. The retained human transfer and mineralization synthesis remain explicitly distinguished from those rat observations.

The new [PMID:42020733] cache also remains **abstract-only**. Its report of glycerol-dependent allostery and human variant associations is retained without guessing the species/construct of every assay or claiming the complete Methods were recovered. No glycerol-binding NEW or direct human thermogenic-flux claim is added.

Seven records contain actual article-body extractions. Five are narrative reviews: [PMID:31413732] (HPP management and extracellular PPi/PLP chemistry), [PMID:33477631] (inflammatory/metabolic and neuronal literature), [PMID:33919113] (HPP genetics, mineralization and clinical consequences), [PMID:39872235] (dental manifestations and mixed treatment outcomes) and [PMID:40100438] (engineered asfotase alfa and clinical data). These provide secondary synthesis rather than new purified human enzyme assays. [PMID:37982855] contains systematic-review/meta-analysis and consensus Methods covering 93 included pediatric/adolescent studies; those are evidence-synthesis methods, not a new patient intervention or biochemical assay, and prospective-validation limits remain explicit.

The original full [PMID:36699639] resolves the earlier construct uncertainty. Its Methods explicitly identify **human TNAP-D10 cDNA**, packaged in AAV8 using HEK293 cells, with AAV8-GFP controls. The hosts are mouse Alpl conditional-knockout and Phospho1-null cohorts. Serum activity/PPi and skeletal improvement support the mineralization mechanism of an engineered mineral-targeted human enzyme; this does not establish native human localization. Dentoalveolar changes were limited. The absence of promoted/increased ectopic calcification during the tested 60-day interval, including the CKD challenge, is a bounded treatment-safety observation. It does not demonstrate active inhibition of non-skeletal mineralization and therefore does not reverse the source-specific GO:0140928 REMOVE. An independent actual-body consultation confirmed this distinction.

All 74 annotation actions and the four compact core units are unchanged. The 13 reference assessments now state their actual source scope; seven full-text-unavailable flags are cleared, six are retained, and fetched titles replace the pre-cache title spellings where needed. Exact rat-donor excerpts and a direct human-construct Methods excerpt are attached to their original PMID records. The biological review can proceed to normal external review with the required citation caches closed. The YAML DRAFT status is retained for the existing source-specific membrane/exosome and provider-citation advisories; those are distinct from missing required source records. Final validation, exact-quote, source/isoform-preservation, recursive-census, history and render results are recorded in the closure handoff.

# 2026-09-27 — PR 3320 chemistry-specific core follow-up

The current-head review correctly identified a machine-readable mismatch: phosphocholine phosphatase activity was paired with both choline and ethanolamine metabolism. The core now separates the two substrate reactions. GO:0052731 remains paired only with GO:0019695, and a fifth core pairs the already accepted GO:0052732 phosphoethanolamine phosphatase activity with GO:0006580. The same actual human biochemical evidence supports both reactions [PMID:41145834]; human fibroblast ectophosphatase evidence also supports phosphoethanolamine hydrolysis [PMID:2220817]. Locations retain the existing extracellular/cell-surface scope. No new annotation is proposed and all 74 annotation decisions are preserved.

For the ATP-term suggestion, the independently read AmiGO usage comment states exactly: “Note that this term is meant to specifically represent the ATPase activity of proteins using ATP as a source of energy to drive a reaction.” [Official GO:0016887 page](https://amigo.geneontology.org/amigo/term/GO%3A0016887?relation=regulates). The saved primary ontology response is `tmp/ALPL-full-audit/continued-primary-7.json`; a fresh direct request during this follow-up timed out, so the quote is attributed to that successful earlier read, not to the failed request. The current term also has a part-of relation to ATP-dependent activity. Human TNAP ATP hydrolysis remains positively supported; the replacement with the immediate NTP-phosphatase parent reflects this usage restriction rather than denial of the measured ATP reaction. The term-convention question remains available for expert resolution.

The two retained calcium-homeostasis rows concern participation in calcium/phosphate balance and remain non-core in the pathological model context. Homeostasis still means maintenance of an internal steady state; pathological calcification is not itself relabeled as healthy homeostasis. The broad annotation does not specify that TNAP inhibits deposition, whereas GO:0140928 explicitly does. Positive removal of inhibitory pyrophosphate supports the opposite direction for that inhibition assertion. This explains the different term-level decisions without claiming that all disease-associated changes establish homeostasis.

The unresolved prostate-secretion exosome identification now explicitly cross-references the independently recovered ALPL Table 1 hit in the urinary-exosome study [PMID:19056867]. That resolves the general location in another sample but does not recover the missing target row from [PMID:23533145]; its source-specific UNDECIDED action remains. Skeletal-system development stays ACCEPT: a valid broader representation of core mineralization does not become non-core merely because the compact core names its narrower process.

Reference assessments now describe the cached publication and then its actual available sections, replacing internal batch terminology. Seven recovered bodies and six abstract-only records are still distinguished individually; no blanket full-article claim is introduced. The prior published histories and all source/provider bytes remain unchanged.
