# DPM2 (human) — review notes

UniProtKB: O94777. HGNC:3006. 84 aa, two predicted TM helices (11–31, 49–69),
ER membrane multi-pass protein. Pfam PF07297 (DPM2); InterPro IPR009914 (DPM2).
Pharos Tdark. Belongs to the DPM2 family.

Deep research: falcon provider is OUT OF CREDITS (HTTP 402); no
`-deep-research-falcon.md` was generated. Review grounded in the UniProt record,
the seeded GOA, and the cached abstract-only publications below.

## Core biology (verified)

DPM2 is the **regulatory/stabilizing subunit** of the dolichol-phosphate mannose
(Dol-P-Man) synthase complex (DPM1 catalytic / DPM2 / DPM3). It is **non-catalytic**.

- [PMID:9724629 "DPM2, an 84 amino acid membrane protein expressed in the endoplasmic reticulum (ER), makes a complex with DPM1 that is essential for the ER localization and stable expression of DPM1. Moreover, DPM2 enhances binding of dolichol phosphate, a substrate of DPM synthase."]
  Also: "Mammalian DPM1 is catalytic because a fusion protein of DPM1 that was stably expressed in the ER synthesized DPM without DPM2." → DPM1 is the catalytic subunit; DPM2 is regulatory.
- [PMID:10835346 "mammalian DPM synthase contains catalytic DPM1 and regulatory DPM2 subunits"] and DPM synthase is a 3-subunit complex (DPM1/DPM2/DPM3). DPM3 "associated with DPM1 via its C-terminal domain and with DPM2 via its N-terminal portion." "The stability of DPM3 was dependent upon DPM2." "DPM synthase activity was 10 times higher in the presence of DPM2, indicating that DPM2 also plays a role in the enzymatic reaction." Enzymatic ordering: "Therefore, DPM2 stabilizes DPM3 and DPM3 stabilizes DPM1" (quotable pieces: "Therefore, DPM2" and "stability of DPM3 was").
- Dol-P-Man synthase "generates mannosyl donors for glycosylphosphatidylinositols, N-glycan and protein O- and C-mannosylation" [PMID:10835346].

## Second complex: GPI-GnT (moonlighting membership)

DPM2 is also a component of the GPI-N-acetylglucosaminyltransferase (GPI-GnT)
complex and enhances GPI-GnT activity, but is NOT essential for it:
- [PMID:10944123 "DPM2, which regulates dolichol-phosphate-mannose synthase, also regulates GPI-GnT"]; DPM2 "associates with GPI-GnT through interactions with PIG-A, PIG-C and GPI1"; "indicating that DPM2 is not essential for GPI-GnT; however, the enzyme activity is enhanced 3-fold in the presence of DPM2."
- [PMID:16162815] GPI-GnT is the initial GPI-biosynthesis enzyme (transfers GlcNAc from UDP-GlcNAc to PI); DPM2 is one of its components (PIG-Y is the seventh). This paper's DPM2 annotations (GPI-GnT complex, ER membrane) are ComplexPortal/UniProt IDA.

## Disease

DPM2-CDG (congenital disorder of glycosylation type Iu / CDG1U, MIM:615042):
muscular dystrophy-dystroglycanopathy with severe epilepsy. Variant Y23C (CDG1U).
Ref PMID:23109149 (Barone et al. 2012) — NOT in GOA, not cached; cited only in
UniProt disease block, so not used as a supporting_text source here.

## Curation decisions (summary)

- ER / ER membrane localization (IBA GO:0005783; multiple GO:0005789 from IEA/NAS/IDA/TAS): ACCEPT the specific ER-membrane ones as core; keep the general "endoplasmic reticulum" (IBA) as ACCEPT (redundant-broader but correct).
- GO:0033185 dolichol-phosphate-mannose synthase complex (part_of; IBA + IDA): ACCEPT — core complex membership.
- GO:0030234 enzyme regulator activity (IBA, IEA) and GO:0008047 enzyme activator activity (IDA): ACCEPT — this is DPM2's actual MF (regulatory subunit that boosts DPM synthase activity 10x and DP binding). enzyme activator activity is the more precise/supported MF.
- BP terms GO:0180047 (dolichol phosphate mannose biosynthetic process), GO:0043048 (dolichyl monophosphate biosynthetic process), GO:0006488 (dolichol-linked oligosaccharide biosynthetic process, IBA): ACCEPT the direct Dol-P-Man ones as core. GO:0043048 "dolichyl monophosphate biosynthetic process" is a slightly odd term for this IDA (PMID:10835346 is about Dol-P-Man, not dolichyl-P synthesis) → MARK_AS_OVER_ANNOTATED (keep, likely mis-specific).
- GPI-GnT complex (GO:0000506; IPI/IDA/TAS) and GPI anchor biosynthetic process (GO:0006506; IDA): KEEP_AS_NON_CORE — real but a secondary/moonlighting role; DPM2 is not essential for GPI-GnT.
- protein binding (GO:0005515; several IPI): the interactions (DPM3, PIGA, PIGC, PIGQ) are informative for complex membership but the bare term is uninformative → MARK_AS_OVER_ANNOTATED per curation policy (do not REMOVE experimental IPIs).
- Reactome "Defective DPM2..." TAS ER-membrane entries: ACCEPT (localization is correct); leave titles as fetched.
