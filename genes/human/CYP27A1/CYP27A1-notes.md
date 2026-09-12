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
