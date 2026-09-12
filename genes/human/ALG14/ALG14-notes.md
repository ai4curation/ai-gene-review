# ALG14 (Q96F25) review notes

Human ALG14 = UDP-N-acetylglucosamine transferase subunit ALG14 homolog. HGNC:28287.
216 aa, single-pass ER membrane protein (TM 4–24; short lumenal N-terminus 1–3;
large cytoplasmic domain 25–216 per UniProt Q96F25).

No deep-research file exists (falcon out of credits, HTTP 402). Review grounded in
UniProt Q96F25, GOA TSV, and cached publications PMID_16100110 (abstract-only) and
PMID_36200043 (full text), plus Reactome R-HSA-446207 / R-HSA-5633241.

## Core biology (verified)

ALG14 is the **membrane-anchoring, non-catalytic subunit** of the bipartite
ALG13/ALG14 UDP-GlcNAc transferase (GnTase) that catalyses the **second step of
dolichol-linked oligosaccharide (LLO / DLO) assembly**: transfer of the second
GlcNAc (β1,4-linked) from UDP-GlcNAc onto GlcNAc-PP-dolichol (Gn-PDol) to form
the chitobiose core GlcNAc2-PP-dolichol (Gn2-PDol), on the **cytoplasmic face of
the ER membrane**.

- ALG13 = soluble cytosolic catalytic subunit; ALG14 = membrane anchor that
  recruits ALG13 to the ER. Neither is active alone.
  [PMID:16100110 abstract: "Alg13 contains a predicted catalytic domain, but lacks
  any membrane-spanning domains. Alg14 spans the membrane but lacks any sequences
  predicted to play a direct role in sugar catalysis."; "as a membrane anchor that
  recruits Alg13 to the cytosolic face of the"; "Alg14 is both necessary and
  sufficient for the ER localization of Alg13".]
- Human ALG13+ALG14 co-expressed in yeast complement loss of either yeast gene
  ("when co-expressed in ... functionally complement the loss of either ALG13 or
  ALG14" — PMID:16100110), establishing functional conservation.
- In vitro human ALG13/14 heterodimer confirmed to catalyse β1,4 GlcNAc addition to
  Gn-PDol → Gn2-PDol [PMID:36200043 "complex catalyzes the addition of a β1,4-linked
  GlcNAc to Gn-PDol to produce Gn2-PDol in the DLO synthetic pathway"]. Only human
  ALG13 isoform 2 (short, Q9NP73-2), not isoform 1, forms the functional complex
  with ALG14 [PMID:36200043]. This is why the IPI (GO:0005515) WITH/FROM =
  UniProtKB:Q9NP73-2 (ALG13 isoform 2).
- CDG variants (ALG14 P65L/CMS15, D74N/R109Q/V141G/MEPCA) reduce GnTase activity
  in vitro [PMID:36200043 "all of the ALG13/ALG14-CDG mutants that were tested
  displayed reduced GnTase activity"; "confirmed the GnTase deficiency of these
  ALG13/ALG14-CDG variants"].

## Localization

ER membrane (GO:0005789), specifically the cytoplasmic side (GO:0098554); single-pass
membrane protein anchoring the otherwise-soluble ALG13. EXP annotation from
PMID:16100110; UniProt SubCell mapping (IEA); Reactome TAS.

## Disease

ALG14 deficiency → ALG14-CDG spectrum: congenital myasthenic syndrome 15 (CMS15,
MIM:616227); myopathy/epilepsy/progressive cerebral atrophy (MEPCA, MIM:619036);
intellectual developmental disorder with epilepsy/behavioral abnormalities/coarse
facies (IDDEBF, MIM:619031). Most variants show normal transferrin glycosylation yet
reduced GnTase activity in vitro (PMID:36200043).

## MF term note

GOA carries the MF as **GO:0043495 protein-membrane adaptor activity** (IBA + IGI),
NOT a catalytic UDP-GlcNAc transferase term. This is correct: ALG14 itself is the
non-catalytic membrane anchor. The catalytic MF (glycosyltransferase) belongs to
ALG13. So the core MF for ALG14 is the adaptor/anchor activity, with directly_involved_in
the LLO biosynthetic BP and part_of the ALG13/14 complex.

## Annotation actions (14 GOA rows)

1. GO:0043495 protein-membrane adaptor activity / IBA — ACCEPT (core; anchor)
2. GO:0006488 dolichol-linked oligosaccharide biosynthetic process / IBA — ACCEPT (core BP)
3. GO:0043541 UDP-N-acetylglucosamine transferase complex / IBA (part_of) — ACCEPT (core CC)
4. GO:0005789 ER membrane / IEA (SubCell) — ACCEPT
5. GO:0006488 DLO biosynthetic process / IEA (InterPro) — ACCEPT (dup of #2)
6. GO:0005515 protein binding / IPI (WITH Q9NP73-2) — MARK_AS_OVER_ANNOTATED (bare protein binding; real info is ALG13-anchoring, captured by adaptor MF + complex CC)
7. GO:0005789 ER membrane / EXP (PMID:16100110) — ACCEPT (core CC)
8. GO:0043495 protein-membrane adaptor activity / IGI (PMID:16100110) — ACCEPT (core; experimental)
9. GO:0098554 cytoplasmic side of ER membrane / IGI (PMID:16100110) — ACCEPT (more precise CC)
10. GO:0006487 protein N-linked glycosylation / IDA (acts_upstream_of_positive_effect, PMID:36200043) — ACCEPT
11. GO:0006488 DLO biosynthetic process / IDA (PMID:36200043) — ACCEPT (core BP; dup)
12. GO:0043541 UDP-GlcNAc transferase complex / IDA (part_of, PMID:36200043) — ACCEPT (core CC; dup)
13. GO:0005789 ER membrane / TAS Reactome R-HSA-5633241 — ACCEPT
14. GO:0005789 ER membrane / TAS Reactome R-HSA-446207 — ACCEPT
