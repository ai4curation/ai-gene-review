# DSF2 (YBR007C / P38213) — curation notes

Journal-style notes for the AI GO review of *Saccharomyces cerevisiae* DSF2. Provenance is
recorded inline as `[PMID:xxxx "verbatim supporting text"]` or `[SGD]`/`[UniProt P38213]`.

## Identity

- **Standard name:** DSF2 = "**D**eletion **S**uppressor of mpt**F**ive" (MPT5 = PUF5). The
  UniProt alt name is "Deletion suppressor of MPT5 mutation protein 2" [UniProt P38213].
- **Systematic name:** YBR007C (chromosome II). UniProt AC **P38213**; SGD **S000000211**.
- 736 aa, ~82.3 kDa, PE 1 (protein-level evidence: detected by mass spectrometry).
- **Verified ORF** in SGD, but SGD lists **molecular function = Unknown** and **biological
  process = Unknown** [SGD]. This is a genuinely understudied ("dark") gene.

## CRITICAL attribution: DSF2 vs DSF1 are NOT homologs

The names DSF1 and DSF2 come from the **same phenotypic screen**, not from sequence homology.
Both `dsf1` (YEL070W) and `dsf2` (YBR007C) were recovered as deletion suppressors that rescue
the temperature-sensitivity of an mpt5Δ (puf5Δ) strain
[PMID:16328373 "we screened deletion suppressors to rescue the temperature sensitivity of Deltampt5, and identified dsf1 (YEL070W), dsf2 (YBR007C), sir2, sir3, sir4 and swe1"].

- **DSF1 (YEL070W)** is a **mannitol dehydrogenase** (alias MAN1), an oxidoreductase enzyme
  with a paralog MAN2 [SGD].
- **DSF2 (YBR007C)** is a **Sel1-like / TPR-repeat protein** with no known catalytic activity.

So DSF1 and DSF2 are functionally and structurally **unrelated**; the shared "Dsf" prefix is a
phenotype label. DSF2-specific evidence must not be conflated with DSF1 enzymology. DSF2's
closest characterized family member is instead the fission-yeast **Nif1** (see Orthology).

## Domain architecture (inline analysis of DSF2-uniprot.txt)

Reading `DSF2-uniprot.txt` (P38213):

- **N-terminal ~1–461: extensively disordered / low-complexity.** UniProt/MobiDB-lite marks
  disordered REGIONs at 1–46, 178–208, 229–410, 440–461, with many polar / low-complexity /
  basic-and-acidic COMPBIAS stretches [UniProt P38213]. This half of the protein is a large
  intrinsically-disordered region with no recognizable folded domain.
- **C-terminal ~560–736: Sel1-like TPR/α-solenoid.** UniProt records SMART **SM00671 SEL1**
  (Sel1-like repeat), InterPro **IPR006597 (Sel1-like)**, **IPR011990 (TPR-like helical domain
  superfamily)**, Gene3D **1.25.40.10 (TPR domain)**, and SUPFAM **SSF81901 (HCP-like)**
  [UniProt P38213]. Sel1/TPR repeats form α-helical solenoids that are generic
  **protein–protein interaction / scaffolding** modules — they do NOT specify a catalytic
  activity or a particular partner.
- **Phosphoprotein.** UniProt cites two large-scale phosphoproteomics/Cdk1-substrate studies
  (PMID:18407956, PMID:19779198) as evidence at protein level. DSF2 is not named in the cached
  text of either (the hits are in supplementary tables), so specific phosphosites are not
  extracted here; the safe statement is that DSF2 is a detected phosphoprotein.

Interpretation: a disordered N-terminal region plus a C-terminal Sel1/TPR solenoid is the
architecture of a **scaffold / adaptor**, but the architecture alone does not tell us *which*
complex or *which* partners, and there is no experimental interactor that pins down a molecular
function. Domain content is therefore consistent with, but not proof of, an adaptor role.

## Orthology / family context (PANTHER PTHR43628)

- UniProt assigns DSF2 to **PANTHER PTHR43628** (family), subfamily **PTHR43628:SF11 "PROTEIN
  DSF2"** [UniProt P38213].
- The reviewed members of PTHR43628 (`interpro/panther/PTHR43628/PTHR43628-entries.csv`) are
  DSF2 (yeast), **S. pombe Nif1 (P87159, "Mitosis inhibitor nif1", SPBC23G7.04c)**, and several
  bacterial/viral Sel1-repeat proteins (E. coli YjcO/YbeT, mimivirus L18). The family is united
  by **Sel1-like repeats**, i.e. it is a *structural* family, not a family with a single shared
  biochemistry.
- The PANTHER family name "Mitotic Progression Regulator" and its description are
  **LLM-generated and unreviewed** (`llm: true, checked: false` in the metadata YAML) — treat
  as a hypothesis, not evidence.
- **S. pombe Nif1** negatively regulates mitotic entry by binding and inhibiting the Nim1/Cdr1
  kinase (Nim1 normally inhibits Wee1, so Nif1 keeps Wee1 active → Cdc2/Cdk1 stays inhibited)
  [Wu & Russell 1997 EMBO J 16:1342, PMID:9135149 (Nif1 novel mitotic inhibitor); via WebSearch].
  This is the biological source of the DSF2 **IBA** annotations (GOA `with` field =
  `PomBase:SPBC23G7.04c`).

**Caveat on the IBA propagation:** the inference DSF2 → "negative regulation of G2/M transition"
+ "cell division site" is a **phylogenetic (IBA) transfer from a distant fungal ortholog that
shares only Sel1/TPR repeats**. There is **no S. cerevisiae experimental evidence** that DSF2
acts on Swe1 (the budding-yeast Wee1), Cdc28/Cdk1, or a Nim1-family kinase. The IBA is a
reasonable placeholder but is not independently corroborated for DSF2.

## What is experimentally KNOWN about DSF2 (budding yeast)

1. **Genetic:** dsf2 deletion suppresses (rescues) the temperature-sensitivity of mpt5Δ/puf5Δ,
   and partially suppresses its hydroxyurea sensitivity
   [PMID:16328373 "identified dsf1 (YEL070W), dsf2 (YBR007C), sir2, sir3, sir4 and swe1"];
   [UniProt P38213 DISRUPTION PHENOTYPE "Rescues temperature-sensitivity of MPT5 deletion. Partially suppresses the hydroxyurea (HU) sensitivity of MPT5 deletion."].
   Note this is a **suppressor genetic interaction**, i.e. loss of DSF2 compensates for loss of
   the Puf5 RNA-binding protein; it does not define DSF2's own molecular function.
2. **Localization:** Dsf2-GFP localizes to the **bud tip / bud neck** in unperturbed cells and
   **relocalizes to the cytoplasm upon DNA-replication stress (HU/MMS)** in a genome-wide GFP
   screen [SGD; PMID:22842922]. This is the basis of the HDA "cellular bud tip" (GO:0005934)
   annotation. DSF2 is not discussed individually in the PMID:22842922 text (it is one of the
   254 relocalizing proteins scored in the supplementary tables), so the localization is a
   high-throughput imaging call, not a dedicated study of DSF2.
3. **Expression:** low-abundance protein (~377 molecules/cell log phase per UniProt
   [UniProt P38213 MISCELLANEOUS]; ~1,600/cell per SGD).
4. **Post-translational:** detected as a phosphoprotein in Cdk1-substrate / phosphoproteome
   screens (PMID:19779198, PMID:18407956) — DSF2 in the supplementary hit lists.
5. **Deletion phenotypes (SGD systematic data):** increased replicative lifespan; decreased
   competitive fitness; sensitivity to the calcium chelator BAPTA [SGD]. These are pleiotropic
   fitness readouts, not a mechanistic function.

## What is NOT known (candidate knowledge gaps)

- **Molecular function is unknown.** No catalytic activity is expected (Sel1/TPR = binding
  module). No specific binding partner has been shown to define an adaptor/scaffold role.
  → MF_DARK.
- **Biological process is unknown.** The only BP annotation is the distant-ortholog IBA
  (negative regulation of G2/M). There is no direct evidence DSF2 regulates the budding-yeast
  cell cycle, and the suppressor and lifespan phenotypes could reflect an unrelated process.
- **Mechanism of mpt5Δ suppression is unknown** — how loss of a bud-tip Sel1/TPR protein
  rescues loss of the Puf5 RNA-binding protein is not established.
- **Relationship to DNA-replication-stress relocalization is unexplained** — why a bud-tip
  protein moves to the cytoplasm under HU/MMS, and whether this matters functionally, is unknown.
- **Redundancy:** DSF2 has NO close sequence paralog in S. cerevisiae (it is NOT a paralog of
  DSF1); the only same-family protein is the distant fission-yeast Nif1. So genetic redundancy
  is unlikely to explain the mild phenotypes; the weak phenotypes more likely reflect a
  conditional / accessory role.

## GO annotation review plan

Five GOA annotations:

| term | ev | ref | plan |
|---|---|---|---|
| GO:0010972 neg reg G2/M transition (P, involved_in) | IBA | GO_REF:0000033 | KEEP_AS_NON_CORE — distant-ortholog (Nif1) inference; plausible but not corroborated in S. cerevisiae; not a core function |
| GO:0032153 cell division site (C, is_active_in) | IBA | GO_REF:0000033 | KEEP_AS_NON_CORE — same Nif1 IBA source; consistent with bud-tip/bud-neck localization but low-confidence for "is_active_in" |
| GO:0005934 cellular bud tip (C, located_in) | HDA | PMID:22842922 | ACCEPT — high-throughput GFP localization, direct experimental (HDA) for DSF2 |
| GO:0003674 molecular_function (root) | ND | GO_REF:0000015 | ACCEPT — correctly records MF unknown; honest root annotation |
| GO:0008150 biological_process (root) | ND | GO_REF:0000015 | ACCEPT — correctly records BP unknown |

Rationale for keeping the IBAs rather than removing: per CLAUDE.md we do not REMOVE on
paralog/ortholog grounds alone; the Nif1 IBA is a legitimate phylogenetic inference and the
bud-tip/bud-neck localization is loosely consistent with a cell-division-site association. But
neither is corroborated by DSF2 experiment, so they are marked non-core and the honest position
(MF/BP unknown) is retained in core_functions/knowledge_gaps.

## Falcon deep-research (DSF2-deep-research-falcon.md) — corroboration and cautions

The falcon report (2026-07-05, 16 citations) corroborates the core picture: Sel1-like/TPR
scaffold with no catalytic domain, bud-neck localization, relocalization to the cytoplasm under
DNA-replication stress, mpt5/puf5 deletion-suppressor origin, and Nif1 (S. pombe) as the
same-family mitotic inhibitor. It adds two *inferences* that I deliberately did NOT promote into
the review's supported claims because they are not verified from primary full text here:

- A proposed link to the **Cbk1 / RAM** signaling network (Dsf2 has Cbk1 phospho-consensus
  motifs but LACKS the canonical Cbk1 docking motif — a "non-docking putative substrate", per
  Gögl et al. 2015). This is an inference from motif presence, and even the report states the
  in-vivo phosphorylation evidence for Dsf2 specifically "remains indirect". Treated as a lead.
- Specific phosphosites (S391/S395) attributed to a 2025 GSK3 phosphoproteomics preprint.
  Unverified against cached full text; not cited in the review.

The falcon report's citations use internal keys (e.g. `gogl2015thestructureof`), not PMIDs, so
per project policy they are NOT used as `supported_by` in the review; the review is grounded only
on verified PMIDs (16328373, 22842922), UniProt P38213, and the PANTHER family file. The falcon
file is retained in the gene folder as the deep-research artifact.

## core_functions position

Given MF and BP are genuinely unknown, `core_functions` will be **minimal**: a single entry
capturing the best-supported, domain-grounded statement — that DSF2 is a Sel1-like/TPR-repeat
protein consistent with a protein-interaction/scaffold module localizing to the bud tip/neck —
using the MF root (GO:0003674) since no specific MF term is defensible, and locations
(GO:0005934). The real deliverable is `knowledge_gaps`.
