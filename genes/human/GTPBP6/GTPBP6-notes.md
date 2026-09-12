# GTPBP6 (Putative GTP-binding protein 6, PGPL) — research notes

UniProt O43824. TRAFAC-class OBG-HflX-like GTPase. Pseudoautosomal gene (Xp/Yp telomere), escapes X-inactivation, Y homologue [PMID:9466997].

## Function — mitochondrial ribosome biogenesis & recycling
Despite being annotated by some IBA pipelines (from bacterial ObgE/CgtA ortholog P25519) as cytoplasmic ribosome-binding, the experimentally characterized human function is in MITOCHONDRIA:
- [PMID:34135319 "the GTPases GTPBP5, GTPBP6, GTPBP7, and GTPBP10 mediate mtLSU maturation"]
- [PMID:34135319 "Addition of recombinant GTPBP6 reconstitutes late mtLSU biogenesis in vitro and shows that GTPBP6 triggers a molecular switch and progression to a near-mature PTC state"]
- [PMID:34135319 "cryo-EM analysis of GTPBP6-treated mature mitochondrial ribosomes reveals the structural basis for the dual-role of GTPBP6 in ribosome biogenesis and recycling"]
- [PMID:34800366] mito proteome — GTPBP6 localizes to mitochondrion (HTP).

So: localization = mitochondrion (mitochondrial matrix/mitoribosome), NOT cytoplasm. MF = GTP binding + ribosomal large subunit binding (the mtLSU). BP = mitochondrial large ribosomal subunit assembly + (mitochondrial) ribosome recycling.

## Decisions
- ribosome binding (IBA, from bacterial ortholog) — the real binding is to the mtLSU; MODIFY/keep general or KEEP_AS_NON_CORE; the specific ribosomal large subunit binding (IDA 34135319) is core.
- cytoplasm (IBA is_active_in, from bacterial ortholog P25519) — the human protein acts in the mitochondrion; this IBA mislocalizes; MARK_AS_OVER_ANNOTATED / flag. Mitochondrion (HTP 34800366) is correct.
- GTP binding (IEA InterPro, TAS 9466997) — ACCEPT (G-domain motifs; core MF support).
- ribosomal large subunit binding (IDA 34135319) — ACCEPT core (binds mtLSU).
- mitochondrial large ribosomal subunit assembly (IDA 34135319) — ACCEPT core BP.
- mitochondrion (HTP 34800366) — ACCEPT.
