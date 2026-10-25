# CYP11B2 (P19099) review notes

## Identity / core biology
CYP11B2 = aldosterone synthase (cytochrome P450 11B2, mitochondrial; P450c11AS / P450aldo / P450C18).
Mitochondrial inner-membrane heme-thiolate cytochrome P450 of the adrenal cortex zona glomerulosa.
Catalyses the final three steps of mineralocorticoid (aldosterone) synthesis on a single active site:
11beta-hydroxylation (11-deoxycorticosterone -> corticosterone), 18-hydroxylation (corticosterone ->
18-hydroxycorticosterone), and 18-oxidation (-> aldosterone). Uses the adrenodoxin/adrenodoxin-reductase
(FDX1/FDX2 + FDXR) electron-transfer system with O2 and NADPH-derived electrons.

- UniProt FUNCTION: "A cytochrome P450 monooxygenase that catalyzes the biosynthesis of aldosterone...
  Catalyzes three sequential oxidative reactions of 11-deoxycorticosterone... 11-beta hydroxylation,
  followed by two successive oxidations at C18 yielding 18-hydroxy and then 18-oxo intermediates...
  ending with the formation of aldosterone." Electron system: "flavoprotein FDXR (adrenodoxin/ferredoxin
  reductase) and nonheme iron-sulfur protein FDX1 or FDX2 (adrenodoxin/ferredoxin)."
- >93% identical to CYP11B1; the distinguishing capability is 18-oxidase activity, required to make
  aldosterone (CYP11B1 lacks it) [PMID:1741400; PMID:2256920].
- EC 1.14.15.4 (steroid 11beta-monooxygenase) and EC 1.14.15.5 (corticosterone 18-monooxygenase /
  aldosterone synthase).

## Localization
Mitochondrion inner membrane (peripheral membrane protein), UniProt SUBCELLULAR LOCATION
(ECO:0000250|UniProtKB:P14137). Reactome reactions place CYP11B2 "associated with the inner
mitochondrial membrane". HTP mito-proteome (PMID:34800366) supports mitochondrion. Core CC =
GO:0005743 mitochondrial inner membrane.

## Disease
- Aldosterone synthase deficiency = corticosterone methyloxidase (CMO) deficiency type I (CMO-1,
  MIM:203400) and type II (CMO-2, MIM:610600); autosomal recessive salt-wasting.
- CYP11B1/CYP11B2 chimera (unequal crossover) -> glucocorticoid-remediable aldosteronism / familial
  hyperaldosteronism type I [PMID:1518866].

## Curation decisions summary
Core:
- GO:0047783 corticosterone 18-monooxygenase activity (18-oxidase = aldosterone synthase; distinguishes
  from CYP11B1) — ACCEPT (IBA + IEA present)
- GO:0004507 steroid 11-beta-monooxygenase activity — ACCEPT (IDA PMID:23322723, PMID:1741400,
  PMID:2256920; IBA; TAS; IEA)
- GO:0032342 aldosterone biosynthetic process — ACCEPT (IDA PMID:23322723, PMID:1741400, PMID:2256920;
  IBA; IMP; IEA)
- GO:0005743 mitochondrial inner membrane — ACCEPT (IBA/IC/ISS/TAS/IEA)
- GO:0020037 heme binding — ACCEPT (IDA PMID:23322723; secondary/cofactor)

Non-core / accept:
- GO:0006705 mineralocorticoid biosynthetic process (Reactome TAS) — ACCEPT (parent BP)
- GO:0005506 iron ion binding, GO:0004497 monooxygenase activity, GO:0016705 oxidoreductase... —
  ACCEPT (correct, general P450 IEAs)
- GO:0008395 steroid hydroxylase activity (Reactome TAS) — ACCEPT (correct grouping term)
- GO:0005739 mitochondrion — ACCEPT (correct, less specific than inner membrane)
- Downstream physiology (blood volume, water/Na/K homeostasis, response to K+/hormone) —
  KEEP_AS_NON_CORE (real but pleiotropic downstream consequences of aldosterone, not molecular core)

Notable judgement calls:
- Cortisol/glucocorticoid: CYP11B2 is NOT the physiological cortisol producer (that is CYP11B1). It can
  make cortisol / 18-hydroxycortisol / 18-oxocortisol in vitro and in primary aldosteronism.
  - GO:0034651 cortisol biosynthetic process NOT|involved_in (IMP PMID:9703385) — ACCEPT the negation.
  - GO:0034651 cortisol biosynthetic process involved_in (IMP PMID:19342457) — MARK_AS_OVER_ANNOTATED
    (in vitro / non-physiological; contradicted by the NOT annotation and by the CYP11B1/CYP11B2 division
    of labour).
  - GO:0006704 glucocorticoid biosynthetic process (IBA) — MARK_AS_OVER_ANNOTATED (CYP11B1's role;
    IBA over-broadens across the CYP11B clade).
  - GO:0034650 cortisol metabolic process (IBA) — MARK_AS_OVER_ANNOTATED (same reasoning; metabolic parent).
- GO:0008203 cholesterol metabolic process (IBA) and GO:0016125 sterol metabolic process (IEA/TAS):
  CYP11B2 acts on C21 steroids (deoxycorticosterone), well downstream of cholesterol; it does not
  metabolize cholesterol or free sterols. MARK_AS_OVER_ANNOTATED (over-broad clade/Reactome grouping).
- GO:0006700 C21-steroid hormone biosynthetic process (IDA PMID:2256920) — ACCEPT (aldosterone is a
  C21 steroid; correct broader BP).
</content>


## Reassessment, 15 October 2026

This reassessment preserves the earlier notes above as provenance. Several earlier exclusions were too categorical. The experimentally established major function is the conversion of deoxycorticosterone to aldosterone through 11-beta hydroxylation, corticosterone 18-hydroxylation and a subsequent 18-oxidation. GO:0047783 names the middle reaction; it should not be described as though its definition alone covered the final oxidation. Heme and iron binding belong to this catalytic machinery rather than separate biological core units.

The current official P19099 record has one 503-residue precursor, a 1–24 targeting segment and a 25–503 processed chain. Fresh official sequence sources agree exactly with the preserved record. Processing does not create an alternative splice product. Clinical variants, experimental CYP11B1/CYP11B2 hybrids and N-terminally engineered recombinant proteins remain distinct from the official product.

The broad glucocorticoid and cortisol-metabolic annotations should not be rejected simply because CYP11B1 has the predominant physiological cortisol-producing role. Human CYP11B2 has a broader demonstrated biochemical range. Separately, CYP11B2-expressing V79 cells metabolized supplied cortisol to 18-hydroxycortisol and 18-oxo-cortisol [PMID:15356073](https://pmc.ncbi.nlm.nih.gov/articles/PMC1283128/). Those experiments support cortisol metabolism, not the formation of cortisol. The abstract of [PMID:9814482](https://pubmed.ncbi.nlm.nih.gov/9814482/) concerns engineered hybrids and substitutions and is not used as evidence that every such construct is wild-type CYP11B2.

The broad cholesterol and sterol pathway annotations are also retained as non-core. The current definitions include pathways, and [Reactome R-HSA-211976](https://reactome.org/content/detail/R-HSA-211976) expressly includes cholesterol-derived steroid-hormone synthesis. CYP11B2 performs downstream catalytic steps in that pathway. This does not assign cholesterol binding, cholesterol side-chain cleavage or control of cholesterol homeostasis to CYP11B2. The earlier propagation-failure diagnosis for this broad pathway term is withdrawn.

The complete current PTHR24279 tree contains 165 nodes. Its human leaf reconstructs the exact 503-residue sequence along a 14-node path, with all eight relevant IBDs on that path and no target-path loss record. The preserved seed donor sets and current GAF donor sets differ in some rows and are documented separately. Target self evidence is expected, not circular. Nineteen complete UniProt-keyed donor queries yielded 562 records and 134 same-term joins across nine rows; these are database reconstructions, not claims to have read all donor papers. The source P14137 is rat Cyp11a1, a paralog, correcting the earlier bovine-CYP11B-ortholog wording without changing the literal donor field.

All five current ARBA rules have matching branches against the official features and taxonomy: ARBA00026797 branch 1, ARBA00026962 branch 103, ARBA00029264 branch 0, ARBA00034378 branch 8 and ARBA00095220 branch 0 (zero-based). Four literal InterPro records and their GO mappings were inspected. Raw rule bodies and predicate evaluations remain in the review working record; the compact public guide records the conclusions and usable source locators.

The three normal Reactome reactions were traced through their catalysts to human P19099. The three disease FailedReaction models instead point to a seven-member CYP11B2 variant set and link back to those normal reactions. They are not successful catalytic assays of every mutant. Their inner-membrane compartment remains consistent with the independently established gene-level location; matrix-localized steroid metabolites do not make the enzyme a soluble matrix protein.

The NRSF study [PMID:19342457](https://pmc.ncbi.nlm.nih.gov/articles/PMC2703558/) supports expression responses to potassium and angiotensin II in human H295R cells. Its joint changes in CYP11B1, CYP11B2 and steroid output do not isolate a CYP11B2-specific cortisol-production step. The source-specific over-annotation judgment does not deny biochemical substrate range. Selected original Methods, Results and captions were read; the normal cache remains abstract-only, and no figure pixels or supplements are claimed.

The MitoCoP target was resolved in the authentic [Table S1 workbook](https://ars.els-cdn.com/content/image/1-s2.0-S1550413121005295-mmc2.xlsx) for [PMID:34800366](https://pmc.ncbi.nlm.nih.gov/articles/PMC8664129/): P19099/CYP11B2 is NotID_130, sheet A Excel row 284 and sheet B Excel row 257. It is in literature pool 4, with experimental identification fields empty. The correct mitochondrial membership is retained without claiming direct proteomic detection in that study. The original HTP source code remains unchanged.

The full abstracts of the G435S and codon-173 deletion reports were read; publisher attempts did not recover the full papers. [PMID:14614232](https://pubmed.ncbi.nlm.nih.gov/14614232/) directly supports reduced 18-hydroxylase/oxidase activity, while its specific blood-volume endpoint remains unverified. [PMID:9838244](https://pubmed.ncbi.nlm.nih.gov/9838244/) explicitly reports low sodium, elevated potassium and salt wasting. The physiological annotations remain contextual and do not attribute renal ion transport to CYP11B2.

The genuine default Falcon attempt failed authentication and the configured fallback returned an insufficient-quota error; no provider-generated research was fabricated. The isolated normal fetch preserved all 55 pre-existing assertions and backfilled 22 supporting-entity lists. The original machine fields, cached sources and prior notes prefix remain protected. Additional normal caches are distinguished from manually recovered original text. The compact source guide supplies scientific access limits and public locators; internal read ledgers preserve the exact consulted passages and attribution.

The independent chemistry consultation read the 1992 original page scans and the 2013 original assays, with selected original 2002 mutagenesis text. It supports direct wild-type cortisol-forming chemistry and leaves the patient-based NOT assertion unresolved: normal patient cortisol does not establish absolute catalytic incapacity. Full 1990 Methods and the complete 1998 patient original remain unrecovered. The two catalytic core units distinguish 11-beta and 18-hydroxylation; subsequent 18-oxidation is described separately with RHEA:50792. No new annotation is proposed. Consultation reports and exact read ledgers remain in the working provenance; the public guide retains scientific access and construct limits.


### Donor-method clarification

The literal inner-membrane donor UniProtKB:P14137 is rat Cyp11a1, with genuine experimental compartment annotations, but it is a paralog rather than a CYP11B2 ortholog. Row 22 retains ACCEPT for the independently supported human CYP11B2 location. Its propagation flags identify the mismatch with GO_REF:0000024's declared ortholog-transfer premise; they do not invalidate the rat source evidence or assert absence of human inner-membrane localization. The source fields, action, core units and quotations are unchanged.


## 2026-10-16: finite review follow-up

The published review was rechecked against the actual human CYP11B2 assays, current GO definitions, the literal PAINT node, full comparator annotation queries and official reaction identities. The 55 original source objects, including the cortisol NOT assertion, the two processed-product records and all existing source files remain unchanged. This appendix records a later judgment; earlier notes are retained verbatim.

All four broad mitochondrion assertions are now TOO_GENERAL relative to the independently supported inner-membrane location. This does not turn the MitoCoP literature-pool-4 membership into a direct proteomic detection or make the older mitochondrial-fraction assays resolve membrane topology.

Positive cortisol biosynthesis is retained as non-core biochemical activity. Original [PMID:1741400](https://pmc.ncbi.nlm.nih.gov/articles/PMC48470/) page 1461 Table 1 directly reports wild-type human CYP11B2 conversion of 11-deoxycortisol to cortisol in COS7 mitochondrial fractions; page 1460 describes the fractionation and product assays. [PMID:23322723](https://pmc.ncbi.nlm.nih.gov/articles/PMC5417327/) Table 1 and turnover Results independently establish this reaction using engineered, purified human CYP11B2 with human Adx/AdR. The NRSF study [PMID:19342457](https://pmc.ncbi.nlm.nih.gov/articles/PMC2703558/) perturbs CYP11B1 and CYP11B2 together and does not isolate the CYP11B2 contribution. That source limitation remains explicit. The patient-source NOT row remains UNDECIDED because physiological dispensability and incomplete patient-source access do not settle an unconditional absence of the demonstrated chemistry. Corticosterone formation also supports the broad glucocorticoid term; glucocorticoids are not restricted to cortisol.

The final aldosterone-forming oxidation is now a distinct core unit using a proposed molecular-function term, not an invented GO identifier. [RHEA:50792](https://www.rhea-db.org/rhea/50792) and the official P19099 reaction record distinguish 18-hydroxycorticosterone oxidation from the preceding corticosterone 18-hydroxylation, [GO:0047783](https://www.ebi.ac.uk/QuickGO/term/GO:0047783). Targeted current QuickGO and OLS searches found no exact final-reaction MF; the inspected Rhea page has no GO MF mapping. GO:0016705 is a suitable broad paired-donor redox parent. This gap proposal is not inferred merely from absence of an EC number. The prior core quote is relocated, and one two-word, cache-exact Reactome anchor supports the hydroxylation unit; per-source quote budgets remain below 25 words. No NEW annotation is added. Broad steroid-hydroxylase ACCEPT rows retain independently established enzyme biology, not an exact mapping of that term to the final oxidation. MODIFY refinements explicitly reuse specific functions already present in separate source tuples.

The cholesterol IBA remains non-core after an actual comparator and phylogenetic check. The 165-node family places human CYP11B2 on a 14-node path through the genuine PTN001547321 duplication, with the literal CYP11A1-descendant IBD and no target-path IRD/IKR loss. Complete current queries of CYP17A1/P05093, CYP21A2/P08686 and CYP19A1/P11511 confirm absence of GO:0008203; CYP11B1/P15538 has the same IBA. The aldosterone/mineralocorticoid GO closure also does not include cholesterol metabolism. These are real convention questions, not proof that the node is wrong or that every pathway participant must directly bind cholesterol. CYP11B2 performs downstream reactions in the cholesterol-derived steroid pathway represented by [Reactome R-HSA-211976](https://reactome.org/content/detail/R-HSA-211976). Conservative retention does not assign cholesterol side-chain cleavage, cholesterol binding or homeostatic control. This differs from row 22's actual ortholog-method mismatch: [UniProtKB:P14137](https://www.uniprot.org/uniprotkb/P14137/entry) explicitly identifies rat Cyp11a1, a supported mitochondrial paralog rather than a CYP11B2 ortholog.

The compact YAML source guide remains a reviewer-authored locator/access guide, not a second annotation authority. It now links the verified P14137 identity and reaction records. RHEA:46100 records cortisol formation; RHEA:76019 and RHEA:76023 in the official P19099 record distinguish the two cortisol-metabolism reactions measured in PMID:15356073. Old provider failures are preserved; no provider retry or fabricated provider report was needed. Original history remains append-only and publication/history/rendering remain ROOT's responsibility.


## Terminal steroidogenesis audit, 2026-10-25

Manual primary-literature reassessment followed the review and annotation-reviewer workflow. Falcon deep research failed authentication, and its Perplexity-lite fallback failed with insufficient quota (run log `/tmp/adrenal-CYP11B1-deep.log`); the established outage was not retried for each homolog. No provider-branded research file was manufactured. Supported fetch commands supplied UniProt, GOA and publication caches. Abstract-only caches were treated as such, and inaccessible experimental evidence was not rejected merely for being inaccessible. No NEW biological-process rows were added.

Evolutionary scope: PMID:32196091 reconstructs functional specialization after duplication in Old World primates. This is not a universal mammalian two-paralog architecture: some mammals retain a single multifunctional CYP11B, and other lineages have additional copies. PANTHER PTHR24279:SF1 has official label CYTOCHROME P450 11B2, MITOCHONDRIAL but also contains zebrafish cyp11c1; membership alone cannot establish aldosterone synthesis. Corticosterone 18-monooxygenase activity describes the hydroxylation step, not the final conversion of 18-hydroxycorticosterone to aldosterone.

All 55 source rows were reassessed while retaining the earlier detailed PAINT/source reconstruction and its evidence file. Broad steroid hydroxylase annotations consistently refine to 11beta- and 18-hydroxylation. The separate proposed 18-hydroxycorticosterone oxidase activity remains the final aldosterone-forming chemistry, supported by human biochemical studies including PMID:2256920 and PMID:23322723. Broad C21-steroid biosynthesis now retains both aldosterone and secondary glucocorticoid outputs.

The existing negated cortisol-biosynthesis row from PMID:9703385 remains UNDECIDED; normal cortisol in an aldosterone-deficient patient does not establish complete absence of CYP11B2 catalytic cortisol formation. Positive cortisol synthesis remains non-core based on independent human enzyme evidence (PMID:1741400 and PMID:23322723). The validator currently emits one term-action consistency warning because it groups opposite polarities together. This is an explicit biological distinction, not an unresolved positive-row inconsistency; neither the NOT qualifier nor the source uncertainty was erased to suppress the warning. No new experimental removal was made.
