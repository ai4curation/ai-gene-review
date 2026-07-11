# PGAP2 (Post-GPI Attachment to Proteins Factor 2) — curation notes

UniProt: Q9UHJ9 (PGAP2_HUMAN), aka FRAG1 (FGF receptor-activating protein 1).
HGNC:17893. 254 aa (canonical isoform 2, Q9UHJ9-1). Multi-pass Golgi membrane protein.

Deep research: falcon provider was out of credits (HTTP 402) at the time of review, so
no `-deep-research-falcon.md` was generated. Grounding is UniProt (Q9UHJ9), the seeded
GOA (`PGAP2-goa.tsv`), and cached publications in `publications/`.

## Function

PGAP2 carries out the **second step of GPI fatty-acid remodeling** in the Golgi. GPI
anchors are synthesized in the ER, attached to nascent proteins, then remodeled during
transport to the plasma membrane. In the Golgi, PGAP3 first removes the sn-2 unsaturated
fatty acid to give a lyso-GPI intermediate; PGAP2 is then required to **reacylate the
lyso-GPI with a saturated (stearic) fatty acid at sn-2**. This fatty-acid remodeling
generates the mature, detergent-resistant-membrane (DRM/lipid-raft)-associating GPI anchor
and is required for stable cell-surface expression of GPI-anchored proteins (GPI-APs).

Key verbatim quote (PMID:29374258, full text available):
> "In the Golgi, GPI-APs undergo fatty acid remodeling where PGAP3 removes an sn-2-linked
> unsaturated fatty acid and PGAP2 is involved in reacylation with stearic acid, a
> saturated fatty acid"

UniProt CC FUNCTION (file:human/PGAP2/PGAP2-uniprot.txt):
> "Involved in the fatty acid remodeling steps of GPI-anchor maturation where the
> unsaturated acyl chain at sn-2 of inositol phosphate is replaced by a saturated stearoyl
> chain. May catalyze the second step of the fatty acid remodeling, by reacylating a
> lyso-GPI intermediate at sn-2 of inositol phosphate by a saturated chain (By similarity).
> The fatty acid remodeling steps is critical for the integration of GPI-APs into lipid
> rafts (PubMed:23561846)."

Catalytic role is debated: UniProt names it "Acyltransferase PGAP2" with EC=2.3.-.- and a
CATALYTIC ACTIVITY (Rhea:RHEA:83851, octadecanoyl-CoA + lysoGPI -> acyl-GPI + CoA) but
both are annotated **By similarity (ECO:0000250|UniProtKB:Q2ABP2)** — i.e., inferred, not
demonstrated for the human protein. PGAP2 may be the acyltransferase itself, or required
for the reacylation (accessory). The GOA carries **no catalytic MF** (only `protein
binding` IPI and a KW-derived `transferase activity` on the UniProt side that is NOT in
the GOA TSV), so no specific acyltransferase MF is asserted in `core_functions`.

## Localization

Golgi apparatus membrane, multi-pass (5 predicted TM helices per UniProt topology).
UniProt SUBCELLULAR LOCATION: "Golgi apparatus membrane" (ECO:0000269|PubMed:10585768).
GOA also carries ER-membrane (ISS/IBA) — consistent with GPI-anchor pathway spanning
ER->Golgi, though the mature remodeling function is Golgi-localized.

## Disease

Biallelic hypomorphic PGAP2 variants cause **hyperphosphatasia with mental retardation
syndrome 3 / hyperphosphatasia with impaired intellectual development syndrome 3
(HPMRS3; MIM:614207)** — intellectual disability, hypotonia, poor speech, elevated serum
alkaline phosphatase (a hallmark of GPI-anchor / inherited GPI deficiency, IGD).
[PMID:23561846; PMID:23561847]

PMID:23561846 (Hansen et al. 2013, IDA for GPI anchor biosynthetic process): rescue
experiments in PGAP2-deficient CHO cells with mutant (p.Tyr99Cys, p.Arg177Pro) vs WT
PGAP2 showed "less expression of cell-surface GPI-anchored proteins DAF and CD59 than of
the wild-type protein" — functional demonstration that PGAP2 is required for surface
GPI-AP expression.

## Annotation decisions summary

- GPI anchor biosynthetic process (GO:0006506): core BP. ACCEPT IBA/IDA. IMP
  (PMID:29374258) is a PGAP4 paper whose full text explicitly assays/uses PGAP2 context;
  ACCEPT (defer to curator, experimental).
- GPI anchor remodelling (GO:0120574, ISS): core BP, more specific/accurate; ACCEPT.
- Golgi membrane (GO:0000139) EXP/ISS/IEA: core location; ACCEPT (EXP), the ISS/IEA
  duplicates ACCEPT/KEEP_AS_NON_CORE.
- endoplasmic reticulum membrane (GO:0005789) IBA/ISS: KEEP_AS_NON_CORE — plausible
  (pathway spans ER->Golgi) but mature remodeling is Golgi; not the core location.
- membrane (GO:0016020) TAS: MODIFY -> Golgi membrane (too general).
- protein binding (GO:0005515) IPI x3 refs: all from large-scale binary interactome /
  splicing PPI screens (HuRI, alt-splicing PPI, human interactome map). Uninformative;
  MARK_AS_OVER_ANNOTATED per curation policy (do not REMOVE experimental IPIs).

## References (relevance)
- PMID:29374258 — HIGH (best verbatim mechanistic description of PGAP2 reacylation step)
- PMID:23561846 — HIGH (function + disease; IDA)
- PMID:10585768 — MEDIUM (original cloning as FRAG1; membrane protein; Golgi from full text)
- PMID:25416956 / 26871637 / 32296183 — LOW (high-throughput PPI, uninformative for MF)
