# nce101 (SPAC12G12.17) — S. pombe — research notes

Journal / provenance log for the AI GO-annotation review. This is an
**understudied ("dark") gene**: the fission yeast protein itself has **no direct
experimental functional characterization**. All conclusions below are grounded in
the UniProt record, the GOA annotation set, PomBase curation, family/orthology
data, and the single foundational budding-yeast paper that defines the family.

## 1. Identity and sequence facts (from UniProt C6Y4B6; do not edit that file)

- UniProt: **C6Y4B6** (NCE1_SCHPO), Reviewed/Swiss-Prot, **58 aa**, MW ~6998 Da.
- Gene: `nce101`; systematic/ORF name `SPAC12G12.17`; chromosome I.
- **PE 2: Evidence at transcript level** — i.e., the protein's existence is inferred
  from transcript evidence; there is **no protein-level experimental evidence** for
  this specific ORF beyond transcript detection.
- Only two primary references on the UniProt entry, and neither characterizes function:
  - PMID:11859360 — the S. pombe genome sequence (Wood et al., 2002) [genomic DNA].
  - PMID:18488015 — transcriptome at single-nucleotide resolution (Wilhelm et al.,
    2008) [IDENTIFICATION; confirms the transcript exists].
- Domain / topology (UniProt):
  - `TRANSMEM 10..27 /note="Helical" /evidence=ECO:0000255` — a single predicted TM
    helix (sequence-analysis prediction, not experimentally determined topology).
  - `SUBCELLULAR LOCATION: Membrane {ECO:0000305}; Single-pass membrane protein
    {ECO:0000305}` — inferred (ECO:0000305 = curator inference), not experimentally shown.
  - Keywords: Membrane, Protein transport, Transmembrane, Transmembrane helix, Transport.
- `FUNCTION: Involved in a novel pathway of export of proteins that lack a cleavable
  signal sequence. May be part of the export machinery or may also be a substrate for
  non-classical export (By similarity). {ECO:0000250}` — **ECO:0000250 = inferred from
  sequence/structural similarity ("By similarity")**, i.e. transferred from the
  S. cerevisiae ortholog, NOT measured in S. pombe. Note the explicit hedge:
  machinery **OR** substrate.
- `SIMILARITY: Belongs to the NCE101 family {ECO:0000305}.`
- Family/domain databases: InterPro **IPR024242** (NCE101), Pfam **PF11654** (NCE101),
  PANTHER **PTHR28011 / PTHR28011:SF1** ("NON-CLASSICAL EXPORT PROTEIN 1").
- No AlphaFold-derived functional annotation beyond a model in AlphaFoldDB; SMR entry.

Sequence:
`MSQPYLISKW MDPLFGIFVG TYGYYLYEKE HRPRGRSLRE LALRKWNKQA VSQQSMKN` (58 aa)
The TM helix (res 10–27) is the single obvious feature; the C-terminal tail is
short and enriched in basic/charged residues (…RPRGRSLRELALRKWNKQ…), consistent with a
tail-anchored / single-pass membrane microprotein but with no diagnostic catalytic motif.

## 2. Family / orthology (from InterPro + PANTHER; interpro/panther/PTHR28011/)

- **InterPro IPR024242 (NCE101)** description (fetched from InterPro API):
  "This entry represents the non classical export protein 1 family. Family members
  are involved in a novel pathway of export of proteins that lack a cleavable signal
  sequence."
- PANTHER PTHR28011 "NON-CLASSICAL EXPORT PROTEIN 1": 275 proteins, 1 subfamily
  (PTHR28011:SF1), 729 taxa, 236 AlphaFold models, 0 experimental structures,
  0 associated pathways. Reviewed members captured: only **2**:
  - C6Y4B6 (S. pombe nce101, 58 aa) — this gene.
  - **Q02820 (S. cerevisiae NCE101, 53 aa)** — the reference ortholog.
- So the family is small microproteins, essentially unstudied outside the founding paper.

## 3. The founding paper: PMID:8655575 (Cleves, Cooper, Barondes, Kelly, 1996)
"A new pathway for protein export in Saccharomyces cerevisiae", J Cell Biol.
(Full text read via Europe PMC / PMC2120850.)

- Screen design: a mammalian non-classically-secreted reporter (**galectin-1**) was
  expressed in yeast; a **multicopy cDNA library** screen looked for clones whose
  overexpression modulated non-classical export of galectin-1.
- NCE1 = "clone07"; NCE2 = "clone17":
  [PMID:8655575 "We have named the clone07 and clone17 genes NCE1 and NCE2 (nonclassical
  _export), respectively."]
- NCE1 encodes a small protein: [PMID:8655575 "The NCE1 cDNA encodes a 53-amino"] (53 aa
  in S. cerevisiae). It was "one of four novel proteins smaller than 100 amino acids
  identified in this screen."
- **Crucial ambiguity of function** — the paper explicitly does NOT resolve whether NCE1
  is machinery or cargo: [PMID:8655575 "The small NCE1 gene product may be part of the
  export machinery, or, along with the other low molecular weight proteins identified in
  the screen, may also be a substrate for nonclassical export."]
  This is the exact hedge preserved in the UniProt FUNCTION line.
- The paper's **mechanistic/genetic characterization (transmembrane topology model, null
  allele, essentiality, suppression of ste6Δ) is done on NCE2, not NCE1.** NCE2 is the
  4-TM candidate machinery component; NCE1 was left essentially uncharacterized beyond
  the overexpression phenotype.
- The overall claim: yeast has a signal-sequence-independent ("non-classical") protein
  export pathway distinct from the classical ER/Golgi secretory route:
  [PMID:8655575 "These findings demonstrate a new pathway for protein export that is
  distinct from the classical secretory pathway in yeast."]

Nomenclature caution: the yeast "NCE" genes are a tangle. The well-studied
S. cerevisiae **NCE102** (an MCC/eisosome plasma-membrane microdomain protein) descends
from the NCE2 story, NOT from NCE1. **NCE101 (Q02820) is the small NCE1 clone**, and
remains poorly characterized. Do not conflate nce101 with the eisosomal Nce102 literature.

## 4. S. cerevisiae ortholog Q02820 (NCE101 / NCE1 / YJL205C) — source of the IBA

- FUNCTION identical hedged wording, but attributed **{ECO:0000269|PubMed:8655575}**
  (experimental, from the founding paper).
- GOA-relevant GO on Q02820:
  - GO:0009306 protein secretion — **IGI:SGD** (inferred from genetic interaction; the
    1996 overexpression screen).
  - GO:0016020 membrane — IEA (UniProtKB-SubCell).
  - GO:0005829 cytosol — HDA:SGD (high-throughput; note this contradicts a strict
    membrane-only view and reflects that localization is not firmly established).
- So the **entire "protein secretion" evidence chain for fission yeast nce101 is an IBA
  propagated from a budding-yeast gene whose own support is a single indirect
  overexpression/genetic screen with explicitly ambiguous interpretation** (machinery vs
  substrate). It is a legitimate phylogenetic inference but should be treated as
  low-confidence and non-core.

## 5. PomBase curation (PomBase API, dataset latest)

- product: "non-classical export protein family Nce101"
- **characterisation_status: `conserved unknown`** — PomBase's explicit flag that the
  biological role is not known (dark gene).
- Manual GO in MF / BP / CC aspects: **none** (empty) — consistent with no experimental
  functional data.
- 12 single-locus phenotype annotations, all on the **`nce101delta` (deletion) genotype**,
  all from large-scale chemical-genomics/drug-sensitivity profiling (no reference-specific,
  mechanistically diagnostic phenotype):
  - resistance to: amorolfine, egtazic acid (EGTA), lithium / LiCl+SDS,
    MgCl2+SDS, KCl+SDS, methyl methanesulfonate (MMS), tert-butyl hydroperoxide.
  - sensitive to: cadmium, diamide, valproic acid, vanadate.
  These are pleiotropic stress/drug phenotypes typical of genome-wide screens; they do
  **not** point to a specific molecular function and are not GO-BP annotated by PomBase.

## 6. KNOWN vs NOT-KNOWN (synthesis)

KNOWN / defensible:
- It is a **small (58 aa) membrane-associated microprotein** with **one predicted TM
  helix** (sequence prediction; ECO:0000255/0000305). Membrane association is a
  reasonable, if not experimentally proven, localization.
- It is the S. pombe member of the **NCE101 family** (IPR024242 / PF11654 / PTHR28011),
  orthologous to S. cerevisiae NCE101.
- The transcript is expressed (PMID:18488015).
- Deletion gives only broad, pleiotropic chemical-stress phenotypes; the gene is
  non-essential-behaving in screens (viable deletion collection member).

NOT known (genuine knowledge gaps):
- **Molecular function is unknown.** There is no biochemical activity, no ligand/substrate,
  no interaction partner, no catalytic motif. "protein transport"/"protein secretion" is a
  family-level inference from an indirect budding-yeast overexpression screen, and even
  there the founding authors could not distinguish whether the protein is part of the
  export **machinery** or is itself an export **substrate/cargo**.
- **Biological process is unknown** for the fission yeast gene specifically; the
  non-classical export pathway has not been demonstrated to operate through nce101 in
  S. pombe.
- **Precise localization is unknown** (membrane inferred; the S. cerevisiae ortholog is
  also annotated cytosol by HDA — conflicting).
- **Topology/orientation** (N-in vs N-out, tail-anchored vs signal-anchored) is not
  experimentally determined.
- No loss-of-function phenotype that isolates a specific pathway.

## 7. Annotation-review plan (for nce101-ai-review.yaml)

Six GOA annotations:
1. GO:0009306 protein secretion — IBA (GO_REF:0000033; from PANTHER PTN001997334 / SGD
   S000003742). Defensible as a family-level phylogenetic inference but weak and NOT the
   demonstrated core function → **KEEP_AS_NON_CORE** (do not elevate to core; it is an
   inference from an indirect screen). Keep per "don't overrule phylogenetic annotation
   without positive evidence against it."
2. GO:0009306 protein secretion — IEA (GO_REF:0000002; InterPro IPR024242). Same term
   from InterPro2GO mapping of the family signature; redundant with the IBA and equally
   family-level → **KEEP_AS_NON_CORE**.
3. GO:0016020 membrane — IEA (GO_REF:0000044; UniProtKB-SubCell). Supported by the single
   predicted TM helix and Membrane keyword; uninformative-but-not-wrong root-ish CC.
   → **KEEP_AS_NON_CORE** (accurate but low-information; membrane is only predicted).
4. GO:0003674 molecular_function (root) — ND (GO_REF:0000015). Correct use of ND: MF is
   genuinely unknown → **ACCEPT** (this honestly records the knowledge gap).
5. GO:0005575 cellular_component (root) — ND. → **ACCEPT** (but see #3; PomBase ND may
   predate/parallel the SubCell membrane call).
6. GO:0008150 biological_process (root) — ND. → **ACCEPT**.

core_functions: minimal — at most a single, low-confidence entry, or empty, because no MF
is established. Lean toward NOT asserting a molecular_function id we cannot support; the
honest position is that MF is unknown (captured by the ND annotation and knowledge_gaps).

knowledge_gaps (REQUIRED, primary deliverable): unknown MF, unknown BP role in S. pombe,
unproven localization/topology, machinery-vs-substrate ambiguity, no LOF phenotype
isolating a pathway.
