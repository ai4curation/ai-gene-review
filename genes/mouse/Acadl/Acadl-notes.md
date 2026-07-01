# Acadl (mouse LCAD) — curation notes

**Gene:** Acadl (long-chain specific acyl-CoA dehydrogenase, LCAD), *Mus musculus*
**UniProt:** P51174 · **EC:** 1.3.8.8 · **Family:** acyl-CoA dehydrogenase (ACAD), PANTHER PTHR48083

## Why this gene was curated

Mouse Acadl is the **home** for a cluster of annotations that were *mis-transferred*
onto human **ACADVL** by Ensembl Compara orthology and that we **removed** in the
human ACADVL review (8 `REMOVE` calls). Human and rodent long-chain FAO are wired
differently: in humans **VLCAD (ACADVL) dominates** long-chain β-oxidation and LCAD
(ACADL) is a minor/near-vestigial activity, whereas in **rodents LCAD is a
functionally important long-chain dehydrogenase**. So the whole-organism knockout
phenotypes belong to *mouse Acadl*, not human ACADVL.

## Function

LCAD catalyzes the first (FAD-dependent, α,β-dehydrogenation) step of each mitochondrial
FAO cycle, forming (2E)-enoyl-CoA and passing electrons to ETF. Its long-chain specific
activity **overlaps with ACADVL and ACAD9**, acting on saturated and unsaturated acyl-CoAs
of ~C6–C24 [file:mouse/Acadl/Acadl-uniprot.txt "long-chain specific / acyl-CoA dehydrogenase
activity overlaps with that of ACADV and ACAD9, acting on saturated and unsaturated acyl-CoAs
with 6 to 24 carbons"]. Mature enzyme is a **homotetramer** in the **mitochondrial matrix**,
one FAD per subunit. LCAD is notably the principal dehydrogenase for **unsaturated and
branched/methyl-branched** long-chain substrates and for some C22–C24 species.

## The LCAD-knockout phenotypes (the mis-transfer source)

The mouse *Acadl*-null has been extensively characterized, and its phenotypes are annotated
here with **experimental IMP** evidence — these are exactly the terms removed from human ACADVL:

| GO term | Evidence | Reference (lead) |
|---------|----------|------------------|
| temperature homeostasis (GO:0001659) | IMP | PMID:15639194 |
| positive regulation of cold-induced thermogenesis (GO:0120162) | IMP | PMID:9802886 |
| response to cold (GO:0009409) | IMP | PMID:21151927 |
| negative regulation of fatty acid oxidation (GO:0046322) | IMP | PMID:15639194 |
| negative regulation of fatty acid biosynthetic process (GO:0045717) | IMP | PMID:15639194 |
| regulation of cholesterol metabolic process (GO:0090181) | IMP | PMID:15639194 |

The classic LCAD-KO mouse (Kurtz/Guerra and successors) shows **cold intolerance / impaired
non-shivering thermogenesis**, gestational loss, hepatic and cardiac lipidosis, and altered
lipid homeostasis — the phenotypic basis of the thermoregulation and lipid-regulation terms
above. (PMIDs recorded as leads from GOA; not yet cached for verbatim `supporting_text`
verification — anchor quotes to the in-repo UniProt record, or fetch these publications before
citing them in `supported_by`.)

## Core molecular function

- **GO:0004466 long-chain fatty acyl-CoA dehydrogenase activity** — core MF, with **IDA**
  (PMID:9861014) plus IBA/IEA/ISO support. This is the correct chain-length-specific term.
- **GO:0050660 FAD binding** — cofactor, ACCEPT (flavoenzyme).
- **GO:0005759 mitochondrial matrix** — core location.

## Over-annotation watch

- **GO:0017099 very-long-chain acyl-CoA dehydrogenase activity** (ECO:0007322) and
  **GO:0070991 medium-chain acyl-CoA dehydrogenase activity** (IEA/ECO:0000501): LCAD has a
  broad substrate range that *overlaps* VLCAD (long/very-long) and MCAD (medium), but its
  defining specificity is **long-chain**. These broader/narrower chain-length MF terms are
  candidates for `MARK_AS_OVER_ANNOTATED` / `KEEP_AS_NON_CORE` (parallel to how ACAD9's
  `GO:0017099` was handled) rather than core.
- **GO:0042803 protein homodimerization activity** (ISO): LCAD is a homotetramer; the
  self-association MF term is non-core (cf. the ACADVL/ACADM `GO:0042802` treatment).

## Cross-reference

This review closes the loop on the human **ACADVL** cross-paralog cleanup: see the ACADVL
review's 8 `REMOVE` calls (mouse P50544→P51174 LCAD phenotype transfers) — those annotations
are correctly at home here on mouse Acadl.

## Status

Fetched (42 GOA annotations) with notes; full per-annotation review + core_functions to be
completed. Part of the cross-species FAO project (mouse arm).
