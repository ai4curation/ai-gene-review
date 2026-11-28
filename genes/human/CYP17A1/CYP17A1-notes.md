# CYP17A1 (P450c17) review notes

UniProtKB: P05093 (CP17A_HUMAN). HGNC:2593. Human, NCBITaxon:9606.
Name: Steroid 17-alpha-hydroxylase/17,20 lyase; Cytochrome P450c17; Cytochrome P450 17A1.
EC 1.14.14.19 (17alpha-hydroxylase) and EC 1.14.14.32 (17,20-lyase / 17-alpha-hydroxyprogesterone aldolase).

## Core biology (grounded in UniProt P05093 + cached literature)

CYP17A1 is a **microsomal (ER-membrane) heme-thiolate cytochrome P450 monooxygenase** that
sits at the **branch point of steroidogenesis**, determining whether pregnane precursors are
routed toward glucocorticoids (cortisol) or toward androgens/estrogens. It is a **single,
bifunctional enzyme** carrying two catalytic activities on one polypeptide:

1. **17-alpha-hydroxylase (EC 1.14.14.19):** hydroxylates C21 steroids —
   pregnenolone -> 17alpha-hydroxypregnenolone, progesterone -> 17alpha-hydroxyprogesterone.
   These 17-OH intermediates are precursors of cortisol (adrenal glucocorticoid pathway).
   [PMID:9452426 "P450c17 is the single enzyme that catalyzes both the 17alpha-hydroxylation of 21-carbon steroids and the 17,20-lyase activity that cleaves the C17-C20 bond to produce C19 sex steroids"]

2. **17,20-lyase (EC 1.14.14.32):** cleaves the C17-C20 bond of the 17-OH intermediates ->
   DHEA (from 17OH-pregnenolone) and androstenedione (from 17OH-progesterone), the committed
   step toward androgens/estrogens.
   [PMID:9452426 "the 17,20-lyase activity that cleaves the C17-C20 bond to produce C19 sex steroids"]

The lyase reaction is **cytochrome b5- and POR-dependent**: cytochrome b5 acts as an
allosteric effector that raises the Vmax of the lyase (not the hydroxylase) reaction, without
direct electron transfer. [PMID:9452426 "coexpression of human b5 with P450c17 also increases the Vmax of the 17,20-lyase reactions but not of the 17alpha-hydroxylase reactions"]
[file quote P05093 "The 17,20-lyase activity is stimulated by cytochrome b5, which acts as an allosteric effector increasing the Vmax of the lyase activity"]

Mechanism: monooxygenase using molecular O2, one atom inserted into substrate, second reduced
to water; two electrons from NADPH via cytochrome P450 reductase (POR).
[file quote P05093 "two electrons provided by NADPH via cytochrome P450 reductase"]

Minor/additional activities (UniProt): 16-alpha-hydroxylase activity relevant to estriol
synthesis (PMID:25301938, PMID:27339894); mouse ortholog characterized similarly (PMID:36640554).

## Localization

ER membrane / microsome membrane. [file quote P05093 "Endoplasmic reticulum membrane"]
NAS/TAS legacy annotations (GO:0005783 endoplasmic reticulum; GO:0005789 ER membrane) all
consistent. UniProt SUBCELLULAR LOCATION cites PubMed:2808364.

## Disease

Combined 17alpha-hydroxylase/17,20-lyase deficiency = Adrenal hyperplasia 5 (AH5, MIM:202110),
a form of congenital adrenal hyperplasia: hypertension + sexual-development defects.
[PMID:24140098 "characterized by hypertension and sexual infantilism and caused by loss-of-function mutations in CYP17A1"]
Isolated 17,20-lyase deficiency also occurs (46,XY DSD); true isolated lyase deficiency can
also be caused by CYB5A mutation. [PMID:9326943; PMID:22170710]

## Structure

Multiple X-ray structures (DeVore & Scott 2012 PMID:22266943 with abiraterone/TOK-001;
Petrunak 2014 PMID:25301938 with substrates). Heme-iron axial Cys442; substrate binding
via Asn202. Abiraterone (prostate cancer drug) is a CYP17A1 inhibitor.

## Curation decisions summary

Core MF: GO:0004508 steroid 17-alpha-monooxygenase activity (no dedicated 17,20-lyase MF term
exists in GO; GO:0004508 is the canonical CYP17A1 MF, well supported by IDA/EXP/IMP + IBA).
Core BP: androgen biosynthesis (GO:0006702), glucocorticoid/cortisol biosynthesis
(GO:0006704 / GO:0034651). Core CC: GO:0005789 ER membrane. Secondary MF: heme binding
(GO:0020037), iron ion binding (GO:0005506).

Over-annotated / generic IEA MF terms (monooxygenase, steroid hydroxylase, oxidoreductase
16705/16712) are not wrong but are ancestors of the specific GO:0004508; keep as non-core.
GO:0019825 oxygen binding (legacy TAS from PINC/ProtInc, cited to PMID:2808364 which does not
mention oxygen binding) is an over-annotation for a P450 — mark as over-annotated.
Generic ARBA IEA BP terms (primary alcohol metabolic, olefinic compound metabolic) are
mechanistically-derived over-general terms — keep as non-core / over-annotated.


## 2026-10-25 complete annotation and taxon audit
All seeded annotation fields outside review were preserved exactly. Every row was reassessed; broad true claims were refined and cofactor activities retained. No NEW process annotations were added. `just deep-research-falcon human CYP17A1 --fallback perplexity-lite` ran concurrently with publication caching. Falcon authentication failed, then Perplexity returned HTTP401 insufficient quota. Manual primary research substitutes for unavailable provider output; no provider-labelled report was fabricated.

PMID25301938 structural/biochemical evidence supports human Delta5 lyase preference:17OH-pregnenolone→DHEA is efficient, while17OH-progesterone→androstenedione is poor rather than absent. PMID40340376(full text) directly measures second-electron transfer and product formation using b5 or POR. The dominant b5 effect on multiple-turnover kinetics is increased coupling; older9452426 yeast-microsome results cannot justify a universal allosteric-only/no-electron-transfer assertion.

QuickGO definition GO0004508 is only17alpha hydroxylation(RHEA65760). Queries for17,20-lyase, hydroxyprogesterone deacetylase andEC1.14.14.32 found no specific matching GO term. Proposed steroid17,20-lyase MF therefore covers oxidative C17-C20 cleavage, C19 steroid+acetate products; EC1.14.14.32 and RHEA50244/14753 are in the curated UniProt reactions. The oxidative reaction is not assigned to a nonoxidative lyase class just from its common name.

PMID19403566 supports tissue-specific rat adrenal repression versus testes; PMID7588219 demonstrates fetal mouse adrenal expression/activity(E12.5–14.5), lost by late gestation/adulthood. The boundary is normal adult adrenal output, not absence of the gene or gonadal activity. Mouse-focused36640554 includes human comparison and is not rejected from its title.

GO-CAM67b1629100003765 gives CYP17A1 hydroxylase/cortisol roles; it does not supply lyase evidence. Cached Reactome193070/193099 describe lyase despite GO4508 attachment and name acetaldehyde instead of the acetate supported by primary chemistry/Rhea. These limitations are assessed explicitly. Reactome194002 incorrectly attributes pregnenolone→17OH-progesterone entirely to HSD3B; the CYP17 step is required.

## PR #5543 gene-level follow-up (2026-10-25)

Verified GO ancestry live on 2026-10-25 via https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0034651/paths/GO:0034308?relations=is_a,part_of . The response contains two paths, both entirely is_a: GO:0034651 → GO:0034650 → GO:0034308, and GO:0034651 → GO:0034309 → GO:0034308. Thus cortisol biosynthesis is a descendant of primary alcohol metabolism; the existing MODIFY is a specialization, not a lateral replacement. Added the explicit chains to the reason and shortened the summary to distinguish the claim from its justification. No actions or replacement terms changed.

## Root-organelle correction, 2026-10-26

The supported root endoplasmic reticulum annotations are retained as ACCEPT, separately from unchanged subcompartment claims. This supersedes earlier journal wording that refined the root location or treated its breadth as non-core. Original annotation payloads, unrelated review decisions and core functions are preserved. Source-specific rationales distinguish curated location/inference, original experimental annotations and source access limits; no new assay or target-table inspection is claimed.

## CYP17A1 variant enzymology preprint (2026-11-01)

Source: Li K, Yakubu J, Jørgensen FS, Pandey AV. DOI:10.20944/preprints202610.2735.v1, posted
2026-10-28. **Not peer reviewed.** The cached record is abstract-only (`content_type:
abstract_only`, `is_preprint: true`, `full_text_declined: landing_page_only`), so only abstract
sentences are quotable as `supporting_text`; the PDF's tables and figures are not, and anything
below drawn from the PDF body is flagged as such rather than quoted.

Why it is relevant here: it is the first source in this review that measures the two CYP17A1
reactions **separately, on the same variant protein, each normalized to immunoreactive CYP17A1
abundance**. That bears directly on the `steroid 17,20-lyase activity` term proposed in this
review, and on the two catalytic `core_functions` entries.

### The two activities dissociate within one polypeptide

Seven missense variants (T131P, L209P, I296T, G303D, R340H, L361P, R449H) were expressed in
HEK293T cells and assayed with [4-14C]-progesterone (hydroxylase) and
[21-3H]-17alpha-hydroxypregnenolone (lyase).
[DOI:10.20944/preprints202610.2735.v1 "Residual 17α-hydroxylase activity ranged from approximately 1% of wild type for L209P to approximately 50% for R340H, and residual 17,20-lyase activity exceeded hydroxylase activity for every variant"]

Single substitutions therefore perturb the two reactions to *different* degrees. This is
independent support for treating oxidative C17-C20 cleavage as a molecular function distinct
from GO:0004508 (whose QuickGO definition covers only 17alpha hydroxylation, RHEA:65760), rather
than as a second output of one activity. It does not by itself establish a new GO term; it
strengthens the existing `proposed_new_terms` justification, which previously rested on
EC/RHEA reaction identity (PMID:40340376) plus structural substrate-preference work
(PMID:25301938).

Caveat, from the PDF body and not quotable from the cached abstract: the lyase assay supplies
17alpha-hydroxypregnenolone directly and so bypasses the upstream hydroxylation step. For the
severe alleles the authors argue the hydroxylase step is the in vivo bottleneck, so measurable
in vitro lyase capacity does not translate into sex-steroid output in patients. The dissociation
is a statement about the enzyme's two catalytic steps, not about pathway flux.

### The defect is catalytic, not loss of enzyme

[DOI:10.20944/preprints202610.2735.v1 "All seven variants retained substantial immunoreactive protein, but below wild type, and the set-level reduction was significant in all assays"]
[DOI:10.20944/preprints202610.2735.v1 "The pathogenicity of these CYP17A1 variants reflects specific catalytic and regulatory defects in a largely intact protein rather than loss of steady-state enzyme"]

Two further abstract-level results, recorded for completeness but not used to support any
annotation here: none of the seven variants altered splicing by SpliceAI or AlphaGenome
("confirming a purely protein-level mechanism"), and the cumulative gnomAD v4.1 burden of
pathogenic/likely pathogenic alleles implies "a carrier frequency of 1 in 1,023 globally and 1
in 523 in East Asian individuals". The population-genetic and variant-interpretation material is
disease-side content and was curated into the dismech `Congenital_Adrenal_Hyperplasia` entry
instead.

### Curation decisions

- **No annotation action changed, and no `NEW` annotation proposed.** The paper characterizes
  variant alleles; it does not identify a function of wild-type CYP17A1 that GOA does not
  already carry. Variant residual-activity measurements are not grounds for a new GO process or
  function term on the gene.
- The reference was added to `references:` with `reference_review` recording the preprint status
  explicitly, and cited as additional `supported_by` on (a) the 17,20-lyase `core_functions`
  entry and (b) the `steroid 17,20-lyase activity` `proposed_new_terms` entry. In both places it
  sits alongside, not in place of, the peer-reviewed PMID:40340376 and PMID:25301938 support.
- Also noted for a future pass: the abstract reports the authors' own measurement that R449H
  retains more lyase than hydroxylase activity, which is the opposite of what selective loss of
  cytochrome b5 stimulation would predict. If this survives peer review it is relevant to how
  this review describes b5-dependence of the lyase reaction, which currently rests on
  PMID:9452426 and PMID:40340376. Not acted on while the source is a preprint.
