# MNN14 (YJR061W, P40355) — curation notes

Journal for the AI GO-annotation review of *Saccharomyces cerevisiae* MNN14.
Understudied ("dark") gene. Primary deliverable is a rigorous knowledge_gaps section.
Every assertion below carries inline provenance.

## Identity (verified)

- UniProt: **P40355** (MNN14_YEAST), 935 aa, MW 108,427.
- SGD: S000003822; systematic/ordered-locus name **YJR061W**; ORF name J1736.
- RefSeq NP_012595.1.
- Protein name in UniProt: "Mannosyltransferase regulator 14"
  [ECO:0000303|PubMed:28101612]. The *name* was coined in the 2017 glyco-engineering
  paper; it does NOT itself establish a mannosyltransferase catalytic activity.

## Family / domains — IMPORTANT attribution point

The task brief anticipated a GT15/MNN1 alpha-1,3-mannosyltransferase. **This is not what
the record shows.** MNN14 is NOT in the MNN1/GT15 family.

- UniProt SIMILARITY: "Belongs to the **MNN4 family**." [UniProt P40355, "SIMILARITY: Belongs to the MNN4 family."]
- InterPro: **IPR009644** (FKTN/MNN-like).
  [UniProt P40355, "InterPro; IPR009644; FKTN/MNN-like."].
- PANTHER: PTHR15407 (FUKUTIN-RELATED)
  [UniProt P40355, "PANTHER; PTHR15407; FUKUTIN-RELATED; 1."].

So MNN14 sits in the fukutin-related/MNN-like family shared by MNN4 and the metazoan
fukutin (FKTN)/FKRP ribitol-phosphate transferases, distinct from the
KRE2/MNT1/GT15 mannosyltransferases.

### Topology (type II Golgi membrane protein)
- TOPO_DOM 1..21 Cytoplasmic; TRANSMEM 22..42 (signal-anchor, type II); TOPO_DOM 43..935 Lumenal.
  [UniProt P40355 FT lines]. Consistent with a Golgi-lumen-acting glycan-modifying protein.
- KW: Golgi apparatus; Membrane; Signal-anchor; Transmembrane.

### DXD motif (catalytic-motif reasoning)
- MOTIF 498..500 "DXD" [ECO:0000250|UniProtKB:P36044] — inferred by similarity to MNN4 (P36044).
- UniProt DOMAIN comment: "The conserved DXD motif is essential for the function, which could
  be an indication that MNN14 has transferase activity." [UniProt P40355,
  "The conserved DXD motif is essential for the function, which could be an indication that MNN14 has transferase activity."]
- DXD motifs coordinate a divalent cation and the nucleotide-sugar in many GT-A / phosphotransferase
  enzymes. Its presence is *consistent with*, but does NOT prove, a catalytic transferase role for
  MNN14 — see knowledge gap. The same wording is used for MNN4, whose curated MF is *regulator*,
  not transferase (below).

## Function — KNOWN vs NOT known

### KNOWN (experimentally, PMID:28101612 — abstract-only in cache; IGI in GOA)
- MNN14 is an **MNN4 paralog** required for full **N-glycan mannosylphosphorylation** in
  *S. cerevisiae*. [PMID:28101612 "MNN14 gene, an MNN4 paralog with unknown function, is essential
  for N-glycan mannosylphosphorylation"]
- **Partial redundancy with MNN4:** single deletions leave residual mannosylphosphate; the
  **MNN4+MNN14 double deletion** abolishes N-glycan mannosylphosphorylation.
  [PMID:28101612 "Double disruption of MNN4 and MNN14 genes was enough to eliminate N-glycan
  mannosylphosphorylation."]
- Biotechnology relevance: eliminating mannosylphosphate (an och1Δmnn1Δmnn4Δmnn14Δ strain) is a
  step toward human-compatible glycoproteins in yeast. [PMID:28101612 abstract]
- INDUCTION: expression is repressed by RIM101 [UniProt P40355, "Expression is repressed by RIM101."],
  from PMID:12509465 (Lamb & Mitchell 2003; Rim101 represses NRG1/SMP1). This is a regulatory-network
  observation, not a molecular function.
- Localization: **Golgi apparatus membrane** (ECO:0000305; by SubCell + topology; IEA in GOA).
  [UniProt P40355, "SUBCELLULAR LOCATION: Golgi apparatus membrane"]

### NOT known (the real gaps)
- **In-vivo division of labour with MNN4 is unresolved.** MNN14 has intrinsic
  mannosylphosphate transferase activity in vitro [PMID:33144549], whereas the close paralog
  MNN4 is curated as an enzyme activator/positive regulator of the Mnn6/Ktr6
  mannosylphosphate transferase and is rate-limiting for mannosylphosphorylation
  [PMID:9459307 "Although two genes, MNN6 and MNN4, which encode a mannosylphosphate
  transferase and its putative positive regulator, respectively, are involved in this
  modification, the amount of Mnn4p has been found to be a limiting factor for
  mannosylphosphorylation."].
- **Direct acceptor positions for MNN14 in vivo are unknown.** Recombinant MNN14 transfers
  mannosyl-phosphate to high-mannose N-glycans in vitro, but which mannose residues/positions
  depend on MNN14 versus MNN4 in the cell remains unresolved.
- **Basis of the MNN4/MNN14 redundancy** is unknown (paralog sub-/neo-functionalization;
  condition-, substrate-, or acceptor-position specificity).
- **Standalone loss-of-function phenotype** beyond the glyco-profile is uncharacterized; MNN14 is
  non-essential and there is no described growth/stress phenotype for mnn14Δ alone.

## GOA annotations to review (5 live rows + 1 proposed molecular-function row)
1. GO:0009101 glycoprotein biosynthetic process — IBA (GO_REF:0000033); IBA panel includes
   SGD:S000001684 (MNN4). BP is correct (mannosylphosphorylation is glycoprotein biosynthesis);
   generic but defensible. Not the *most* specific but IBA-appropriate. -> KEEP_AS_NON_CORE / ACCEPT.
2. GO:0000139 Golgi membrane — IEA (SubCell). Supported by topology + SubCell. -> ACCEPT.
3. GO:0006491 N-glycan processing — IGI (PMID:28101612), with SGD:S000001684 (MNN4). This is the
   experimental genetic-interaction annotation matching the double-deletion result. -> ACCEPT (core BP).
4. GO:0003674 molecular_function — ND (root). Superseded by the separate NEW
   GO:0000031 row carrying the 2021 in-vitro catalytic evidence. -> REMOVE.
5. GO:0005575 cellular_component — ND (root). Superseded by Golgi membrane. -> REMOVE.
6. GO:0000031 mannosylphosphate transferase activity — NEW from the 2021 recombinant
   Mnn14 biochemical assay.

Note: GO:0006491 "N-glycan processing" is defined as conversion of N-linked glycan to mature form by
glycosidases/glycosyltransferases [OLS GO:0006491]. Mannosylphosphorylation is an N-glycan
outer-chain maturation/modification, so this is an appropriate (if slightly generic) BP.

## Molecular-function term triage

- GO:0000031 mannosylphosphate transferase activity — asserted as a NEW row because Kang
  et al. 2021 directly showed that recombinant soluble MNN14 can transfer mannosyl-phosphate
  from GDP-mannose to high-mannose N-glycan acceptors [PMID:33144549 "a strategy is
  established here for the in vitro mannosyl-phosphorylation of high-mannose type N-glycans
  that utilizes a recombinant Mnn14 protein"].
- GO:0008047 enzyme activator activity — the MF of the paralog MNN4 (IMP:SGD); still not
  asserted for MNN14 because MNN14 itself has intrinsic catalytic activity, and whether it
  also activates Mnn6/Ktr6 in vivo has not been tested.

## References gathered
- PMID:28101612 — Kim et al. 2017, Appl Microbiol Biotechnol. Primary experimental (abstract-only cache).
  Genetic evidence linking MNN14 to N-glycan mannosylphosphorylation; source of IGI
  GO:0006491.
- PMID:12509465 — Lamb & Mitchell 2003 (RIM101 represses NRG1/SMP1). Source of the INDUCTION note;
  MNN14 mentioned as a Rim101-repressed target. Secondary/regulatory context.
- PMID:9459307 — Odani et al. 1997, FEBS Lett. MNN4 = positive regulator of mannosylphosphorylation;
  establishes the MNN4-family regulator paradigm (background for the MF gap).
- UniProt:P40355 — domain/family/topology/DXD evidence.
- UniProt:P36044 — MNN4 paralog record (regulator MF; DXD ambiguity) for attribution.

## Web verification log
- rest.uniprot.org P40355 (full record downloaded to MNN14-uniprot.txt): family=MNN4,
  InterPro IPR009644, PANTHER PTHR15407, DXD 498-500, type II Golgi, FUNCTION =
  "role in N-glycan mannosylphosphorylation... partially redundant with MNN4."
- rest.uniprot.org P36044 (MNN4): MF enzyme activator activity (IMP:SGD); "seems to have a
  regulatory role... transferase activity cannot be ruled out."
- WebSearch (Odani 1997 PMID:9459307; Wang MNN6=KTR6): MNN6/Ktr6 = the mannosylphosphate transferase;
  MNN4 = its positive regulator, Mnn4p amount rate-limiting.
- OLS: GO:0006491, GO:0009101, GO:0000031, GO:0008047 definitions confirmed.

## 2026-09-28 — IBA re-review

The single IBA row derives from current PANTHER data:

```text
PTHR15407  PTN001034988  GO:0009101  P  IBD  CGD:CAL0000174110|CGD:CAL0000175223|MGI:MGI:2179507|SGD:S000001684|SGD:S000003822|UniProtKB:O75072  taxon:33154  20251219
```

This is not a stale or circular propagation. `PTN001034988` still exists, MNN14's own
`SGD:S000003822` evidence in the WITH/FROM list is an experimentally characterized
descendant used to place the ancestral IBD, and `GO:0009101 glycoprotein biosynthetic
process` is broad but valid for the mannosylphosphorylation activity defined by
PMID:28101612 and PMID:33144549.

Newer literature search turned up no post-2021 direct *S. cerevisiae* MNN14 papers that
change the GO calls. Pakhomova et al. 2026 is about *Ogataea polymorpha*
phosphomannosylation mutants and only mentions MNN14 as a *S. cerevisiae* MNN4 paralog;
2024-2026 reviews on heterologous protein glycosylation likewise use MNN14 as background
for mannosylphosphate removal or M6P glyco-engineering.

## 2026-10-01 current-GOA refresh

Forced a current GOA/UniProt refresh and re-fetched all cached PMIDs. Current GOA still has
the same five exact rows and no retired assertions are needed: one live IBA row, one live
SubCell row, one live SGD IGI row, and the two SGD ND placeholders all remain represented
in the review. The refresh backfilled current `supporting_entities` for the three non-ND
GOA rows.

Re-checked PANTHER PTHR15407 after the refresh. PTN001034988 is still the only ancestral
PAINT node that transfers to MNN14, and it carries only the deliberately broad
`GO:0009101` glycoprotein biosynthetic process assertion. The metazoan
`GO:0000139` Golgi membrane IBD at PTN000395622 does not propagate to MNN14. The 2026
literature search found newer glyco-engineering reviews and an orthologous
*Ogataea polymorpha* phosphomannosylation paper, but no post-2021 direct
*S. cerevisiae* MNN14 study that changed the MNN14 action set.
