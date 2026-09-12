# CYP19A1 (Aromatase / Estrogen synthase, P11511) — review notes

## Summary of gene function

CYP19A1 encodes **aromatase** (cytochrome P450 19A1, P-450AROM, estrogen synthase; EC 1.14.14.14),
a **microsomal, endoplasmic-reticulum-membrane heme-thiolate cytochrome P450 monooxygenase**. It
catalyzes the **rate-limiting, committed step of estrogen biosynthesis**: the aromatization of C19
androgens to C18 estrogens. In three sequential oxidative steps (each requiring 1 O2 and 1 NADPH via
cytochrome P450 reductase, POR) it removes the C19 angular methyl group and aromatizes the steroid
A-ring, converting androstenedione -> estrone and testosterone -> 17beta-estradiol. The first two
steps are C19 methyl hydroxylations (19-hydroxy, 19-oxo/aldehyde); the third, unique step is
A-ring aromatization with C1-beta hydrogen abstraction, C10-C19 bond cleavage, and release of formic
acid [PMID:19129847; UniProt P11511 FUNCTION].

- Aromatase is "the only enzyme in vertebrates known to catalyse the biosynthesis of all oestrogens
  from androgens" [PMID:19129847].
- Crystal structure (Ghosh 2009, PDB 3EQM) is the first mammalian full-length microsomal P450 to be
  crystallized; androstenedione binds in an androgen-specific cleft with C19 ~4 A from the heme Fe;
  heme Fe axially coordinated via Cys437 (thiolate) [PMID:19129847; UniProt FT BINDING 437].
- Electron donor: cytochrome P450 reductase (POR); aromatase itself is the terminal oxygenase, NOT an
  electron carrier.
- Secondary/minor activities: 2-hydroxylation of estrone (estrogen 2-hydroxylase, GO:0101021) and
  oxidation of dihydrotestosterone to 19-nor products [PMID:22773874].

## Localization
Endoplasmic reticulum membrane / microsome membrane; multi-pass membrane protein (N-terminal TM
anchor ~19-42) [PMID:2973313; UniProt SUBCELLULAR LOCATION]. Membrane anchoring is required to give
lipophilic steroids access to the active site [PMID:19129847].

## Expression
Widely expressed via tissue-specific alternative promoters: placenta, adipose, gonads (ovary,
testis), brain, skin fibroblasts, bone [UniProt TISSUE SPECIFICITY; PMID:2040633, PMID:7690033,
PMID:8117272]. In the ovary, FSH + oocyte-secreted factors (GDF9/BMP15) induce CYP19A1 in granulosa/
cumulus cells to drive estradiol production (follicle development) [PMID:30541132]. In adipose,
osteopontin/MMP-cleaved OPN induces aromatase and estradiol (relevant to obesity-linked,
estrogen-dependent breast cancer) [PMID:26482249].

## Disease / pharmacology
- Aromatase deficiency (AROD, MIM:613546): loss of function; maternal virilization in pregnancy,
  46,XX pseudohermaphroditism/virilization at birth, delayed puberty, tall stature (unfused
  epiphyses), osteoporosis [UniProt DISEASE; PMID:1371509 first molecular defect; PMID:8265607,
  PMID:8530621, PMID:9211678, PMID:24705274].
- Aromatase excess syndrome (AEXS, MIM:139300): gain/overexpression; heterosexual precocity in males
  (gynecomastia), isosexual precocity in females [UniProt DISEASE].
- Validated drug target: aromatase inhibitors (letrozole, anastrozole, exemestane) are frontline
  therapy for estrogen-dependent breast cancer [PMID:19129847; UniProt DrugBank].

## Curation decisions (high level)
- Core MF: aromatase activity (GO:0070330) — accept all copies (IBA, IEA, EXP, IDA).
- Core BP: estrogen biosynthetic process (GO:0006703) — accept.
- Core CC: endoplasmic reticulum membrane (GO:0005789) — accept; ER (GO:0005783) accept; bare
  membrane (GO:0016020) over-annotated.
- Secondary: heme binding (GO:0020037), iron ion binding (GO:0005506) — accept (cofactor).
- Over-general parents to demote: monooxygenase activity (GO:0004497), oxidoreductase
  GO:0016705 / GO:0016712, steroid hydroxylase activity (GO:0008395).
- estrogen 2-hydroxylase (GO:0101021) and DHT oxidation / androgen catabolism — keep as non-core
  (minor/secondary activities).
- response to estradiol (GO:0032355) — over-annotation (aromatase synthesizes estradiol; the IBA
  "response to" is a phylogenetic artifact from paralogs, not aromatase's function).
- sterol metabolic process (GO:0016125) — over-annotation (estrogens are steroids, not sterols;
  aromatase does not metabolize sterols).
- electron transfer activity (GO:0009055) — remove: aromatase is the terminal oxygenase, it
  RECEIVES electrons from POR; it is not an electron carrier/shuttle (wrong MF for a P450).
- oxygen binding (GO:0019825) — over-annotated (O2 is a co-substrate activated by the heme, but
  GO:0019825 is for O2-carrier proteins).
