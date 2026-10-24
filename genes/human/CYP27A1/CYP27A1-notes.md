# CYP27A1 (human, Q02318) — review notes

Sterol 27-hydroxylase / sterol 26-hydroxylase, mitochondrial (EC 1.14.15.15).
Mitochondrial cytochrome P450 (CYP27A1). Deep research: falcon OUT OF CREDITS (HTTP 402);
no `-deep-research-*.md` generated. Grounded in UniProt (Q02318), seeded GOA, and cached
`publications/PMID_*.md`.

## Core biology (verified)

- Mitochondrial P450 that receives electrons from the adrenodoxin (ferredoxin) /
  ferredoxin reductase system. UniProt catalytic-activity blocks all use "reduced
  [adrenodoxin]" as electron donor.
- Catalyzes regio-/stereospecific hydroxylation of the sterol side chain at C27 (C26),
  and further oxidizes the C26/C27 alcohol to aldehyde and then to carboxylic acid
  (R-CH3 -> R-CH2OH -> R-CHO -> R-COOH) [PMID:1708392 "the expression of active enzyme
  capable of catalyzing multiple oxidation reactions (R-CH3----R-CH2OH----R-COOH) at
  carbon 27 of sterol intermediates of the bile acid synthesis pathway."].
- Bile-acid biosynthesis: initiates side-chain oxidation of 5-beta-cholestane
  intermediates (e.g. 5beta-cholestane-3a,7a,12a-triol -> THCA) — this is the
  EC 1.14.15.15 / RHEA:34631 reaction, captured in GOA as GO:0047748 (label
  "cholestanetetraol 26-dehydrogenase activity", but the definition IS the sterol
  26-hydroxylase reaction). [PMID:1708392 abstract; UniProt CATALYTIC ACTIVITY].
- Acidic (alternative) bile-acid pathway: converts cholesterol -> 27-hydroxycholesterol
  (first step), and can further oxidize it to 3beta-hydroxy-5-cholestenoic acid
  [PMID:9660774 "alternative pathways of bile acid synthesis which begin with
  27-hydroxylation of cholesterol catalyzed by P450c27"; "recombinant human P450c27 is
  also able to further oxidize 27-hydroxycholesterol giving first an aldehyde and then
  3beta-hydroxy-5-cholestenoic acid."]. GO:0031073 (cholesterol 26-hydroxylase activity)
  is this cholesterol->26/27-OH step.
- Regioselectivity determined by helix F residues (F215K/I211K mutants change product
  pattern, confer C-C cleavage) [PMID:11412116].
- Also 27-hydroxylates 7-ketocholesterol in retinal pigment epithelium (detox/elimination
  of a noxious oxysterol) [PMID:21411718]; the recombinant IDA GO:0016716 annotation is
  from this paper.
- Vitamin D: CYP27A1 can hydroxylate vitamin D3, but PMID:15465040 shows CYP27A1
  hydroxylates vitamin D2 at C-24 and C-27 (NOT C-25) and that CYP2R1 is the
  physiologically important 25-hydroxylase (CYP2R1 kcat/Km 26-fold higher than CYP27A1).
  So the vitamin D 25-hydroxylase MF and vitamin D3 biosynthetic-process annotations are
  minor/secondary at best; the primary IDA (PMID:15465040) is really a CYP2R1 paper.
  Treat vitamin D role as non-core (KEEP_AS_NON_CORE / MARK_AS_OVER_ANNOTATED).

## Localization

- Mitochondrion; UniProt: "Mitochondrion inner membrane ... Peripheral membrane protein
  ... Post-translationally targeted to mitochondria. After translocation into the matrix,
  associates with the inner membrane as a membrane extrinsic protein." So both
  mitochondrial inner membrane (GO:0005743) and mitochondrion (GO:0005739) are correct;
  Reactome's mitochondrial matrix (GO:0005759) reflects the matrix-facing extrinsic
  association and is acceptable as non-core.
- HTP MitoCoP proteomics (PMID:34800366) supports mitochondrial localization at large
  scale.

## Disease

- Cerebrotendinous xanthomatosis (CTX, MIM:213700): autosomal-recessive sterol storage
  disorder; cholestanol/bile-alcohol accumulation, tendon xanthomas, cataracts,
  progressive neurologic decline; treated with chenodeoxycholic acid.
  CTX-causing loss-of-function missense variants (R395C, R395S, R405Q, R362S, etc.)
  reduce sterol 27-hydroxylase activity [PMID:2019602, PMID:9186905, PMID:9790667].

## Cofactors

- Heme (axial Cys at position 476 binds heme Fe) — heme binding GO:0020037 (IDA
  PMID:9660774) and iron ion binding GO:0005506 (IEA) are both correct P450 cofactor
  functions.

## Smoothened signaling (GO:0045880)

- By-similarity/ISS/IEA from mouse (Q9DBG1 / MGI:88594): CYP27A1 makes
  7-keto,27-hydroxycholesterol, an oxysterol that can activate SMO. This is an indirect,
  downstream consequence of the oxysterol product, not a core molecular activity of
  CYP27A1. Keep as non-core.

## Action plan summary

- CORE MF: GO:0047748 (EC 1.14.15.15 sterol 26-hydroxylase / bile-acid intermediate
  side-chain hydroxylation), GO:0031073 (cholesterol 26/27-hydroxylase). ACCEPT the
  EXP/IDA instances.
- CORE BP: GO:0006699 (bile acid biosynthetic process), GO:0006707 (cholesterol
  catabolic process), GO:0008203 (cholesterol metabolic process).
- CORE CC: GO:0005743 (mito inner membrane), GO:0005739 (mitochondrion).
- CORE cofactor: GO:0020037 heme binding, GO:0005506 iron ion binding.
- GO:0008395 steroid hydroxylase (Reactome TAS): correct but general parent of the
  specific hydroxylase MFs; ACCEPT (or note as less specific). Many duplicate Reactome
  rows -> ACCEPT each.
- Vitamin D (GO:0030343, GO:1901755): KEEP_AS_NON_CORE / over-annotated per PMID:15465040.
- Smoothened (GO:0045880): KEEP_AS_NON_CORE (indirect oxysterol effect).
- Broad IEA MF parents (GO:0004497 monooxygenase, GO:0016705, GO:0016716): ACCEPT as
  correct-but-general.
</content>
</invoke>


## 2026-10-16 source-specific augmentation

This assessment preserves all 69 historical source objects and the preceding notes as an earlier record. It supersedes the earlier claims that vitamin D activity is nonphysiological, that MitoCoP newly measured CYP27A1, and that matrix placement should be peripheral merely because inner-membrane localization is also present. The current metadata query contains 67 exact matches; only the two historical ARBA steroid/lipid-process rows are absent. No source object is rewritten to mirror that later snapshot.

CYP27A1 performs two closely related core chemistries: oxidation of bile-acid-intermediate side chains and cholesterol side-chain hydroxylation/further oxidation. The 1991 human cDNA study and the 1998 human recombinant study distinguish direct enzyme activity from CTX variant phenotypes. Heme and the adrenodoxin/reductase electron-transfer system belong within these catalytic descriptions. The separate old heme-only core is integrated into the two catalytic units; its binding annotations remain accepted. The 2001 mutant study does not establish carbon–carbon cleavage by wild-type CYP27A1. The 2004 D3/D2 comparison supports secondary D3 C25 hydroxylation and must not be read as disproving a physiological contribution. GO:0036378 is obsolete and is not proposed. The original D3-process annotation is retained under the current GO part_of convention. See the source guide for DOI and section locators and the distinction between recovered original text and abstract-only sources.

The official precursor is 531 residues; the annotated mature processing product PRO_0000003618 comprises residues 34–531 (498 residues). No alternative splice products are enumerated in the inspected official record. The 1991 sequence analysis predicted the human targeting boundary; it did not directly sequence the mature human N terminus. The current precursor Cys476 corresponds to mature-chain Cys443 in that paper. Historical mutation and recombinant-construct numbering is not silently converted to current coordinates. The rat import study (PMID:19401463, Experimental Procedures and Results on digitonin/protease protection and carbonate extraction) supports a matrix-facing, membrane-extrinsic protein. Both matrix and inner-membrane placements are accepted, without implying an exclusively free-soluble matrix pool or direct human localization experiments in the rat paper.

The actual MitoCoP workbook is decisive about source scope: Q02318 is NotID_076 in literature pool 4, with experimental identification and validation fields blank (Table S1 workbook, (A) All protein groups row 287; (B) MitoCoP row 260, Excel rows). Its catalogue inclusion agrees with mitochondrial biology but is not a new proteomic detection of CYP27A1. The original HTP field remains untouched. Three historical Reactome IDs returned 404 twice; their exact source objects and unavailable-title placeholders remain, with independent enzyme/localization corroboration and no invented reaction names. Two other records are FailedReactions of defective variants with explicit normal-reaction links. Those are not NOT annotations for normal CYP27A1. Current Reactome NAD(P)H-acceptor metadata are not used to reverse the primary adrenodoxin-driven chemistry.

Actual PAINT reconstruction identifies the current target in PTHR24291, whose official broad family name is CYTOCHROME P450 FAMILY 4, and subfamily PTHR24291:SF6. The exact 531-residue MSA sequence and all four literal historical IBDs are on the 22-node target path; no path loss was found. The older PTHR24279 context lacking the target is preserved rather than overwritten. The full IBD file is the authenticated October 12 capture, not a new October 16 GAF download. Rat P17178/RGD:727915, mouse Q9DBG1/MGI:88594 and rabbit P17177 were distinguished by actual official records. All 916 saved rule branches were evaluated; rule provenance is not treated as independent proof of function.

The Smoothened annotations remain contextual positive biological-process inferences. In the original mouse Ptch1-null fibroblast experiments, CYP27A1 depletion and rescue with downstream oxysterols identify a performed catalytic contribution (PMID:30340023, Results and Figure 4H–J caption; selected Methods). This is stronger than an unspecified downstream association but does not establish direct receptor binding, ciliary localization or a human pathway assay. The GO-CAM contains CYP27A1 in that enzymatic role, while SMO and HSD11B2 have their own activities and locations. The full PMID:30340023 cache was selected byte-identically from the pending PR4615 source; it was not manufactured or modified.

Actions are 60 ACCEPT, five KEEP_AS_NON_CORE, three TOO_GENERAL and one MODIFY, with no NEW. The sole term refinement replaces the prior breadth-only lipid-biosynthesis overannotation judgment with directly performed bile-acid biosynthesis. Fifteen matrix annotations move from peripheral to accepted functional localization. Repeated inherited support is consolidated; the unrelated CYP7A1 excerpt on the CYP27A1 row, the nonspecific MitoCoP methods excerpt, and EC/name-only evidence are removed. The old notes remain intact so those prior observations and corrections are visible.

Genuine default Falcon research failed with HTTP403 authentication, and the configured Perplexity fallback failed with HTTP401 quota; these failures are preserved. Manual source work and the independent ROOT four-paper consultation supply this augmentation. The consultant read selected original 1708392/9660774 text; full 11412116/15465040 recovery remained unsuccessful. Owner reads include selected original 12077124/21411718/19401463/30340023 text, the MitoCoP workbook, complete cited abstracts, ontology definitions and actual raw source projections. Neither figure pixels nor whole supplementary articles are claimed. The compact source guide is navigation to this evidence, not an experimental supporting reference.

The broad mitochondrion annotations retain their positive biological and source assessment but are marked TOO_GENERAL because the accepted matrix and inner-membrane placements already resolve the catalytic compartment. This includes the valid inherited active-in assertion; it is not a rejection of its ancestral node or donor evidence. Concise primary findings reuse the existing chemistry and D3 excerpts within aggregate source budgets, with two short original localization/pathway excerpts added. The source guide is serialized as YAML without changing its scientific object.


## 2026-10-16: source summaries and ontology follow-up

The 69 annotation summaries are restored from the earlier review where they remain accurate and revised where the earlier wording conflicts with the inspected evidence. In particular, lower vitamin D3 catalytic efficiency does not demonstrate nonphysiological activity, MitoCoP includes CYP27A1 as a literature-pool 4 entry rather than a new experimental detection, matrix placement is compatible with membrane association, and an unavailable Reactome or original-paper method is not represented as recovered. All 69 imported source objects, products, core functions and existing quoted passages remain unchanged.

The only action change is lipid biosynthesis (row 9), from MODIFY to TOO_GENERAL, with its proposed bile-acid replacement removed. The retained vitamin D3 process GO:1901755 entails the broad GO:0008610 assertion. The six bile-acid-biosynthesis assertions remain valid independently; GO:0006699 is not a descendant of GO:0008610 in the current closure. Actions are now 60 ACCEPT, five KEEP_AS_NON_CORE and four TOO_GENERAL, with no NEW. Broad monooxygenase, paired-donor oxidoreductase and steroid hydroxylase assertions remain correct source-level catalytic classifications. Under the sparing TOO_GENERAL convention, retaining those classifications does not claim extra logical coverage or justify additional core functions.

A fresh official QuickGO response on 2026-10-16 still marks GO:0036378 obsolete and records that it was added in error. The guide gives the public endpoint, date and response hash; neither a local project entry nor a remaining issue checkbox overrides that ontology response. The D3 process keeps its existing current part_of interpretation. The authored guide is labeled as navigation and interpretation rather than independent verified evidence. It now includes a small extraction of the actual MitoCoP target cells, with workbook URL, hash, Excel coordinates and preserved null versus empty-string values. No missing value is converted into a measurement or a negative biological result.

The three unavailable Reactome identifiers retain their original fetched placeholder titles and UNVERIFIED assessments. Inventing titles would conceal the access limit. This follow-up changes the lipid-biosynthesis action and presentation of evidence; the earlier D3, matrix and inner-membrane decisions are retained. The prior notes remain intact as the record of the earlier curation stages.
