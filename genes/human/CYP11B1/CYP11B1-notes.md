# CYP11B1 (P15538) review notes

## Gene identity
- Human steroid 11-beta-hydroxylase, cytochrome P450c11 / P-450(11)beta / CYPXIB1.
- Mitochondrial inner-membrane cytochrome P450 (heme-thiolate), 503 aa, N-terminal
  mitochondrial transit peptide (residues 1-24), heme axial Cys ligand at position 450.
- EC 1.14.15.4. HGNC:2591, gene on chromosome 8q22 adjacent to paralog CYP11B2.

## Core catalytic function
- Catalyses the FINAL step of cortisol (glucocorticoid) synthesis: 11beta-hydroxylation of
  11-deoxycortisol -> cortisol, and 11-deoxycorticosterone (21-hydroxyprogesterone) ->
  corticosterone. [file:human/CYP11B1/CYP11B1-uniprot.txt "11beta position, yielding cortisol or corticosterone, respectively"]
- Uses the mitochondrial adrenodoxin electron-transfer system: NADPH -> FDXR
  (adrenodoxin/ferredoxin reductase, FAD) -> FDX1/FDX2 ([2Fe-2S] adrenodoxin/ferredoxin)
  -> CYP11B1. [PMID:18215163 abstract; UniProt FUNCTION]
- Reaction (RHEA:46100): 11-deoxycortisol + 2 reduced [adrenodoxin] + O2 + 2 H+ =
  cortisol + 2 oxidized [adrenodoxin] + H2O.
- Km ~338 uM for 11-deoxycortisol, ~180 uM for 21-hydroxyprogesterone; kcat 1.67 / 0.85 s-1
  (recombinant enzyme, PMID:18215163).
- Also 11beta-hydroxylates adrenal androgens (androstenedione -> 11OH-androstenedione;
  testosterone -> 11beta,17beta-diOH-androstenedione) — secondary androgen-pathway role.

## Relationship to CYP11B2 (aldosterone synthase)
- CYP11B1 and CYP11B2 are >93% identical at the protein level. [PMID:15026188 "their primary structure is 93% identical"; PMID:2256920 "93% identical"]
- CYP11B1 is the GLUCOCORTICOID-branch enzyme; CYP11B2 is the MINERALOCORTICOID/aldosterone-branch enzyme.
- CYP11B1 has only weak 18-hydroxylase and NO 18-oxidase activity, so it CANNOT make aldosterone.
  [file quote "Due to its lack of 18-oxidation activity, it is incapable of generating" aldosterone;
   PMID:2256920 "P-450(11)beta substantially fails to catalyze the reaction to form aldosterone"]
- Consequence for review: "aldosterone biosynthetic process" annotations on CYP11B1 are
  over-annotations (belongs to CYP11B2 / bovine CYP11B1 which is bifunctional). The IBA MF
  term "corticosterone 18-monooxygenase activity" reflects a weak residual activity; keep
  non-core.

## Localization
- Mitochondrion inner membrane, peripheral membrane protein. [file "Mitochondrion inner membrane"]
- HTP mitochondrial proteome (PMID:34800366) supports mitochondrial localization.
- IC (PMID:8506298) and TAS (PMID:15026188, Reactome) support inner-membrane.

## Tissue / regulation
- Expressed in zona fasciculata/reticularis of the adrenal cortex.
  [file "Expressed in the zona fasciculata/reticularis of"]
- ACTH (peptide hormone) is the primary trophic/transcriptional stimulus -> supports
  "cellular response to peptide hormone stimulus".
- NRSF/NRSE regulates CYP11B1 and CYP11B2 transcription; K+ and angiotensin II augment
  transcription (PMID:19342457, H295R adrenocortical cells). K+ response is more central
  to CYP11B2/aldosterone; keep CYP11B1 K+ annotation non-core.

## Disease
- 11beta-hydroxylase deficiency congenital adrenal hyperplasia = Adrenal hyperplasia 4
  (AH4, MIM:202010); second commonest form of CAH; hypertensive form from
  11-deoxycorticosterone (DOC) excess plus androgen excess/virilization.
  [PMID:8506298 "second most common cause of congenital adrenal hyperplasia and results in a hypertensive form"]
- Common CAH mutations cluster in exons 6-8 (e.g. R448H). [PMID:8506298; PMID:2022736]
- Hyperaldosteronism familial type 1 (HALD1, glucocorticoid-remediable) arises from a
  CYP11B1/CYP11B2 chimeric gene (ACTH-driven CYP11B1 promoter + CYP11B2 coding).

## Curation decisions summary
- Core MF: GO:0004507 steroid 11-beta-monooxygenase activity (ACCEPT).
- Core BP: GO:0034651 cortisol biosynthetic process + GO:0006704 glucocorticoid biosynthetic
  process (ACCEPT).
- Core CC: GO:0005743 mitochondrial inner membrane (ACCEPT).
- Cofactor: GO:0020037 heme binding + GO:0005506 iron ion binding (ACCEPT).
- Over-annotations: GO:0032342 aldosterone biosynthetic process (belongs to CYP11B2),
  GO:0008203 cholesterol metabolic process (CYP11A1 role, IBA over-propagation),
  GO:0006955 immune response (downstream glucocorticoid effect).
- Non-core physiology/regulation: blood pressure, glucose homeostasis, K+/hormone responses,
  peptide hormone response, sterol/cortisol metabolic (parent), mitochondrion (broad).
</content>
</invoke>


## Terminal steroidogenesis audit, 2026-10-25

Manual primary-literature reassessment followed the review and annotation-reviewer workflow. Falcon deep research failed authentication, and its Perplexity-lite fallback failed with insufficient quota (run log `/tmp/adrenal-CYP11B1-deep.log`); the established outage was not retried for each homolog. No provider-branded research file was manufactured. Supported fetch commands supplied UniProt, GOA and publication caches. Abstract-only caches were treated as such, and inaccessible experimental evidence was not rejected merely for being inaccessible. No NEW biological-process rows were added.

Evolutionary scope: PMID:32196091 reconstructs functional specialization after duplication in Old World primates. This is not a universal mammalian two-paralog architecture: some mammals retain a single multifunctional CYP11B, and other lineages have additional copies. PANTHER PTHR24279:SF1 has official label CYTOCHROME P450 11B2, MITOCHONDRIAL but also contains zebrafish cyp11c1; membership alone cannot establish aldosterone synthesis. Corticosterone 18-monooxygenase activity describes the hydroxylation step, not the final conversion of 18-hydroxycorticosterone to aldosterone.

All 46 source rows were assessed. PMID:18215163 directly characterizes purified human CYP11B1 11beta-hydroxylation. PMID:15356073 provides full-text evidence that both CYP11B enzymes hydroxylate cortisol at C18, whereas only CYP11B2 further forms 18-oxocortisol. These secondary reactions are distinguished from the principal cortisol/corticosterone biosynthetic activity. Specific corticosterone 18-hydroxylation is supported more cautiously by the review discussion and curated sequence record; cortisol turnover alone does not establish corticosterone turnover.

All four aldosterone-process assertions are UNDECIDED: failure to perform the terminal aldosterone reaction does not prove failure to contribute an upstream intermediate, but physiological CYP11B1-dependent aldosterone flux is not isolated by the available sources. The immune-response source is abstract-only and the clinical hypoglycemia source PMID:16114325 has no abstract; these remain UNDECIDED. Cholesterol/sterol pathway-context annotations are retained as non-core without claiming direct CYP11B1 cholesterol conversion. IBA assessments use the ancestral-node interpretation, not donor counts or self-inclusion. GO-CAM 67b1629100003765 independently represents CYP11B1 11beta-monooxygenase activity in cortisol biosynthesis at the mitochondrial inner membrane. The core is one heme-dependent monooxygenase activity, not separate heme-binding and iron-binding functions.

## 2026-10-25: review evidence follow-up

Expanded six ambiguous location quotations to include the SUBCELLULAR LOCATION heading, distinguishing the curated location statement from identical keyword text. No annotation actions or machine source fields changed.
