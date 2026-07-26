# FANCB (FANCB) — AIGR vs Affinage

**Affinage record:** 2026-06-09 · 8 discoveries · self-eval faith 100% · gates passed.

## Agreement (brief)

Both sources agree on the central biology: FANCB (originally FAAP95) is an X-linked
(Xp22.31), non-catalytic subunit of the Fanconi anemia core complex that acts upstream to
enable FANCD2(-FANCI) monoubiquitination during replication-coupled interstrand-crosslink
(ICL) repair; loss abolishes DNA-damage-induced FANCD2 foci, causes crosslinker
hypersensitivity and chromosomal instability, and produces FA complementation group B
(frequently severe VACTERL-with-hydrocephalus). Both place FANCB in the FA nuclear core
complex, in the nucleus, and both flag the FANCD2-monoubiquitination requirement as the
defining functional output. Affinage's PMID-dense narrative (8 citations) is fully
consistent with the AIGR review's framing.

## Disagreements

| Topic | Affinage says | AIGR review says | Verdict (who is right + why) |
|---|---|---|---|
| FANCB molecular activity | `mechanism_profile` molecular_activity = **GO:0140096 catalytic activity, acting on a protein** | **GO:0030674 protein-macromolecule adaptor activity** (scaffold/dimerization of the BL100 module); explicitly non-catalytic | **AIGR right; Affinage GO wrong-branch.** FANCB carries no catalytic residues — the RING E3 is FANCL. AIGR's adaptor/scaffold call is the mechanistically correct MF; Affinage's coarse GO layer mis-assigns the module's catalysis to FANCB. Affinage's own narrative ("component…that functions upstream", "structural") actually agrees with AIGR, not with its GO tag. |
| Core mechanism granularity | Narrative: FANCB "functions upstream of FANCD2 monoubiquitination"; scaffold role implied but not articulated | **B-L-100 (FANCB-FANCL-FAAP100) catalytic module**: FANCB is the sole **dimerization element** forming the symmetric "dimer of trimers", stimulating FANCL ~6-fold (PMID:27986592, PMID:31666700) | **AIGR more specific and correct.** AIGR resolves the exact structural role (scaffold/dimerization templating core-complex assembly and positioning the two FANCL RINGs) that Affinage leaves at "upstream." AIGR's structural PMIDs are absent from the Affinage citation set. |
| Localization | `mechanism_profile`: GO:0005634 nucleus, **GO:0000228 nuclear chromosome** | Nucleus + **GO:0005654 nucleoplasm**, **GO:0000785 chromatin** (IDA), plus a **cytosolic BL100 assembly pool** (GO:0005829) pre-import | **AIGR more precise.** AIGR captures damage-induced chromatin loading (experimental IDA) and the cytosolic pre-import pool; Affinage's "nuclear chromosome" is a coarser parent and omits the cytosolic module. |
| Germline/meiosis + HSC roles | Narrative foregrounds meiotic sex-chromosome localization/H3K9 methylation (PMID:26123487) and HSC quiescence/repopulation (PMID:26658157) as "dedicated" FANCB roles | Not annotated; review scoped to the molecular scaffold function | **AIGR correctly conservative.** These are genuine *mouse* phenotypes but tissue/organism-level consequences of FA-pathway loss, not FANCB's direct molecular function; importing them as human GO core functions would over-reach. Legitimately excluded (documentable in notes, not as annotations). |
| SCE role | Narrative (via PMID:17903171) notes FANCB is **not** required for SCE (Mus81 route), yet PMID:21458466 shows **reduced** SCE on loss | Keeps SCE repair (GO:1990414) as **KEEP_AS_NON_CORE** | **AIGR right to hedge.** The FA/SCE relationship is species/cell-type specific and downstream; non-core status correctly reflects the ambiguity that Affinage's narrative itself surfaces. |

## Papers incorporated into the review

| PMID | Supports | How used |
|---|---|---|
| PMID:21458466 | FANCB required for HR (gene targeting/Rad51) and for spontaneous SCE; absent FancD2 foci | Added to `references` (reference_review HIGH/VERIFIED); verbatim `supported_by` on GO:1905168 (positive regulation of DSB repair via HR — previously unsupported) and GO:1990414 (SCE non-core). |
| PMID:32106311 | FANCB indispensable for enzymatic activation of FANCD2 monoubiquitination in ICL repair; variant residual activity tracks severity | Added to `references` (reference_review HIGH/VERIFIED); verbatim `supported_by` on GO:0036297 (interstrand cross-link repair). |

## Net assessment

The AIGR review is materially stronger and more specific than the Affinage record on FANCB's
core molecular function: it correctly identifies FANCB as the non-catalytic
scaffold/dimerization subunit of the B-L-100 catalytic module (GO:0030674 adaptor activity),
whereas Affinage's coarse `mechanism_profile` mis-tags it with catalytic activity (GO:0140096,
wrong branch) despite its own narrative describing a structural role. Affinage's PMID-dense
narrative was nonetheless useful as a sourcing layer: two of its experimental citations were
incorporated to backfill previously thin supporting evidence — PMID:21458466 (mouse FancB ES-cell
HR/SCE phenotypes) and PMID:32106311 (FANCD2-monoubiquitination requirement / genotype-phenotype).
Affinage's germline-meiosis and HSC-quiescence emphases are genuine mouse phenotypes that AIGR
correctly declines to promote to human GO core functions. **2 papers incorporated, 0 new
annotations, validation ✓ Valid.**
