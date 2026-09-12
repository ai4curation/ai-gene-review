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
- Pfam: **PF04991 (LicD)** — a nucleotidyl-/phosphotransferase-type domain
  [UniProt P40355, "Pfam; PF04991; LicD; 1."].
- InterPro: **IPR007074** (LicD/FKTN/FKRP nucleotidyltransferase) and
  **IPR009644** (FKTN/MNN4/W02B3.4-1)
  [UniProt P40355, "InterPro; IPR007074; LicD/FKTN/FKRP_NTP_transf." and
  "InterPro; IPR009644; FKTN/MNN4/W02B3.4-1."].
- PANTHER: PTHR15407 (FUKUTIN-RELATED)
  [UniProt P40355, "PANTHER; PTHR15407; FUKUTIN-RELATED; 1."].

So the fold is the LicD/fukutin-related nucleotidyltransferase superfamily, shared by MNN4
and the metazoan fukutin (FKTN)/FKRP ribitol-phosphate transferases — a phosphotransferase-type
architecture, distinct from the KRE2/MNT1/GT15 mannosyltransferases.

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
- **Molecular function is undetermined.** MNN14 has NO curated MF term other than the ND root.
  The two live hypotheses, neither established for MNN14:
  1. **Enzyme regulator/activator** of the mannosylphosphate transferase — the role its paralog
     MNN4 is assigned. In yeast the actual catalytic **mannosylphosphate transferase is
     Mnn6/Ktr6** (KRE2/MNT1 family), and **MNN4 is its positive regulator** whose amount is
     rate-limiting [Odani et al. 1997, PMID:9459307 "Mannosylphosphate transfer to cell wall
     mannan is regulated by the transcriptional level of the MNN4 gene"; Wang et al., MNN6=KTR6
     is the mannosylphosphate transferase]. MNN4's curated MF is **enzyme activator activity
     (GO:0008047, IMP:SGD)**; UniProt (P36044) states "While MNN4 seems to have a regulatory role
     in N-glycan mannosylphosphorylation, a transferase activity of MNN4 cannot be ruled out."
  2. **Transferase activity** of its own — suggested only by the conserved DXD motif (by similarity).
- **Direct acceptor substrate / exact reaction of MNN14 is unknown** (which mannan/glycan position;
  whether it transfers mannose-1-phosphate at all vs. regulates the enzyme that does).
- **Basis of the MNN4/MNN14 redundancy** is unknown (paralog sub-/neo-functionalization;
  condition-, substrate-, or acceptor-position specificity).
- **Standalone loss-of-function phenotype** beyond the glyco-profile is uncharacterized; MNN14 is
  non-essential and there is no described growth/stress phenotype for mnn14Δ alone.

## GOA annotations to review (5)
1. GO:0009101 glycoprotein biosynthetic process — IBA (GO_REF:0000033); IBA panel includes
   SGD:S000001684 (MNN4). BP is correct (mannosylphosphorylation is glycoprotein biosynthesis);
   generic but defensible. Not the *most* specific but IBA-appropriate. -> KEEP_AS_NON_CORE / ACCEPT.
2. GO:0000139 Golgi membrane — IEA (SubCell). Supported by topology + SubCell. -> ACCEPT.
3. GO:0006491 N-glycan processing — IGI (PMID:28101612), with SGD:S000001684 (MNN4). This is the
   experimental genetic-interaction annotation matching the double-deletion result. -> ACCEPT (core BP).
4. GO:0003674 molecular_function — ND (root). MF genuinely unknown. -> KEEP_AS_NON_CORE.
5. GO:0005575 cellular_component — ND (root). Superseded by Golgi membrane; but ND placeholder. -> KEEP_AS_NON_CORE.

Note: GO:0006491 "N-glycan processing" is defined as conversion of N-linked glycan to mature form by
glycosidases/glycosyltransferases [OLS GO:0006491]. Mannosylphosphorylation is an N-glycan
outer-chain maturation/modification, so this is an appropriate (if slightly generic) BP.

## Candidate MF terms considered (NOT asserted as MNN14 core)
- GO:0000031 mannosylphosphate transferase activity — this is the *catalytic* activity of Mnn6/Ktr6;
  assigning it to MNN14 would be over-annotation because (a) MNN14's own catalytic activity is unproven
  and (b) its paralog MNN4 is curated as a *regulator*, not a transferase. Listed only in knowledge_gaps.
- GO:0008047 enzyme activator activity — the MF of the paralog MNN4 (IMP:SGD); a plausible-by-orthology
  hypothesis for MNN14 but not experimentally shown for MNN14. Listed only in knowledge_gaps.

## References gathered
- PMID:28101612 — Kim et al. 2017, Appl Microbiol Biotechnol. Primary experimental (abstract-only cache).
  The single functional paper directly on MNN14; source of IGI GO:0006491.
- PMID:12509465 — Lamb & Mitchell 2003 (RIM101 represses NRG1/SMP1). Source of the INDUCTION note;
  MNN14 mentioned as a Rim101-repressed target. Secondary/regulatory context.
- PMID:9459307 — Odani et al. 1997, FEBS Lett. MNN4 = positive regulator of mannosylphosphorylation;
  establishes the MNN4-family regulator paradigm (background for the MF gap).
- UniProt:P40355 — domain/family/topology/DXD evidence.
- UniProt:P36044 — MNN4 paralog record (regulator MF; DXD ambiguity) for attribution.

## Web verification log
- rest.uniprot.org P40355 (full record downloaded to MNN14-uniprot.txt): family=MNN4, Pfam LicD,
  DXD 498-500, type II Golgi, FUNCTION = "role in N-glycan mannosylphosphorylation... partially
  redundant with MNN4."
- rest.uniprot.org P36044 (MNN4): MF enzyme activator activity (IMP:SGD); "seems to have a
  regulatory role... transferase activity cannot be ruled out."
- WebSearch (Odani 1997 PMID:9459307; Wang MNN6=KTR6): MNN6/Ktr6 = the mannosylphosphate transferase;
  MNN4 = its positive regulator, Mnn4p amount rate-limiting.
- OLS: GO:0006491, GO:0009101, GO:0000031, GO:0008047 definitions confirmed.
