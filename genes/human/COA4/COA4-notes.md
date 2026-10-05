# COA4 (Q9NYJ1) — research notes

Human cytochrome c oxidase assembly factor 4 homolog, mitochondrial.
Synonyms: CHCHD8, E2IG2. HGNC:24604. 87 aa. Chromosome 11.

## Why this gene, now

COA4 was one of the ~100 "orphan" mitochondrial proteins in MitoCarta3.0. UniProt still
carries only `FUNCTION: Putative COX assembly factor. {ECO:0000250}` — i.e. by similarity,
with no experimental function statement. The 2026 MitoMatch paper
([doi:10.1038/s41467-026-77112-z](https://doi.org/10.1038/s41467-026-77112-z)) supplies the
missing direct physical interaction (COA4–COX11) and the first human loss-of-function
characterization, converting a long-standing genetic inference into experimentally grounded
human data. See `projects/MITO_INTERACTOME.md`.

## Structure and import

- Twin CX9C protein: CHCH domain at 31–72, Cx9C motif 1 at 34–44, Cx9C motif 2 at 54–64,
  disulfides 34↔64 and 44↔54 (UniProt Q9NYJ1, `ECO:0000305|PubMed:23676665`).
- Twin CX9C proteins are imported into the intermembrane space by the MIA40/CHCHD4–ALR
  disulfide relay [PMID:19703468 "which we demonstrated to be dependent for import"]. Yeast Coa4 is Cmc3 in that nomenclature.
- Localization in yeast: IMS, associated with the inner membrane [PMID:20624914 "Coa4 is a twin
  CX 9 C motif mitochondrial protein localized in the intermembrane space and associated with
  the inner membrane"].
- **Not a copper metallochaperone.** COA4 lacks the copper-binding cysteine motif of COX17, and
  its loss gives a far milder phenotype than deletion of the bona fide chaperones
  [PMID:35666203 "Importantly, Coa4 lacks the copper-binding cysteine motif that is found in
  Cox17, further negating its metallochaperone role"]. This matters: do **not** annotate
  `copper chaperone activity` (GO:0016531) or copper binding.

## Yeast Coa4 — the prior evidence chain

**Discovery (2009, as Cmc3).** Systematic survey of the 14 yeast twin Cx9C proteins; most
deletions impair respiratory chain assembly or stability [PMID:19703468 — abstract only in cache].

**Renaming and first characterization (2010).** Isolated as an allele-specific suppressor of a
Shy1 Leigh-syndrome mutant; renamed Coa4. Key phenotypes [PMID:20624914]:
- "Cells lacking Coa4 are depressed in CcO activity but show no impairment in Cox1 maturation or
  formation of the Shy1-stabilized Cox1 assembly intermediate" — so Coa4 acts *downstream* of
  Cox1 synthesis and hemylation.
- "Cells lacking Coa4 resemble shy1 Δ cells in exhibiting a reduced mitochondrial copper content."
- "Coa4 may likewise be part of the Cu(I) routing pathway."
- Respiratory function restored by CYC1 (cytochrome c) overexpression.

**ROS confound (2013).** coa4Δ respiratory growth is rescued by DTT/GSH/ascorbate *without*
restoring CcO assembly — the growth defect is largely H₂O₂ from partially assembled CcO
intermediates, not the assembly defect itself [PMID:23198688 "Interestingly, the presence of the
reductants does not suppress these assembly defects and the levels of cytochrome c oxidase remain
reduced"]. Important caveat when reading respiratory-growth rescue as evidence of restored assembly.

**Genetic placement in the copper pathway (2022).** Targeted suppressor screen [PMID:35666203]:
- COX11 overexpression restores Cox1 abundance, CcO assembly and respiration in coa4Δ.
- The rescue requires the copper-coordinating cysteines of Cox11 — so it is restored copper
  delivery, not ROS suppression: "cysteine mutants of Cox11 that are incapable of binding copper,
  failed to rescue the respiratory defect".
- Coa4 and Cox11 abundance are reciprocally regulated in mitochondria.
- coa4Δ cells have reduced cellular copper; copper supplementation partially rescues.
- **Human COA4 complements yeast coa4Δ** — "we demonstrate that human COA4 can replace the
  function of yeast Coa4 indicating its evolutionarily conserved role". This is what licenses
  transferring the yeast mechanism to the human protein.
- Directionality: "only Cox11 can rescue coa4Δ and not the other way around ... suggests that
  Coa4 acts upstream of Cox11 in the copper delivery pathway".
- **Explicit negative result:** "Our initial attempts to detect protein:protein interaction
  between Cox11 and Coa4 via coimmunoprecipitation/mass spectrometry experiments were not
  successful (data not shown)." The 2026 paper closes exactly this gap.

## MitoMatch (2026) — what is new

Swaminathan et al., *The predicted interactome of the human mitochondrial proteome*,
Nat Commun 2026 (in press), [doi:10.1038/s41467-026-77112-z](https://doi.org/10.1038/s41467-026-77112-z).
No PMID assigned yet, so it is cited and cached by DOI as
`publications/DOI_10.1038_s41467-026-77112-z.md` (full text retrieved via OpenAlex under
CC-BY), which means its supporting quotes are machine-verifiable like any PMID reference.

Prediction: AlphaFold-Multimer predicts an evolutionarily conserved COA4–COX11 interaction, with
IMS-localized COA4 contacting the IMS-facing domain of COX11 — topologically coherent.

Experimental validation and human phenotyping:

| Experiment | Result |
|---|---|
| Yeast Coa4-V5 co-IP/MS, DSSO-crosslinked mitochondria (n=3) | Cox11 recovered; also IMS phosphatase Ptc5 |
| COX11-FLAG IP from 293T mitochondria (n=3) | Recovers COA4-V5, plus COX1 and COX2 |
| Reciprocal COA4-V5 IP (n=3) | Recovers COX11-FLAG; **not** COX1 or COX2 |
| CRISPR COA4-KO, MCH58 fibroblasts, 2 clones | COA4 absent |
| COX11 immunoblot in KO (n=3) | Striking reduction in COX11 abundance |
| ICP-MS of KO mitochondria (n=3) | Reduced Cu; Fe, Zn, Mn unaffected |
| BCS copper-chelator titration (n=3) | COX1 loss more pronounced in KO than WT |
| BN-PAGE/western (n=2) | Drastic, specific loss of complex IV–containing supercomplexes |
| Seahorse OCR (n=3) | Reduced respiration |

The crosslinking step is plausibly why 2026 succeeded where 2022 failed — consistent with a
transient or low-affinity contact.

## Independent support for COA4–COX11 that predates the 2026 paper

UniProt Q9NYJ1 records `INTERACTION: Q9NYJ1; Q9Y6N1: COX11; NbExp=2; IntAct=EBI-22303661,
EBI-2963275`, sourced from BioPlex [PMID:33961781]. This is also the origin of the GOA
`IPI GO:0005515 protein binding` row with `WITH/FROM UniProtKB:Q9Y6N1`. So the human COA4–COX11
interaction had affinity-purification support before MitoMatch; the 2026 work adds reciprocal
targeted co-IP, cross-species conservation, and functional consequence.

## Annotation assessment

**Well supported and core**
- `GO:0033617 mitochondrial respiratory chain complex IV assembly` — previously IBA/IEA only.
  Now backed by human KO data (complex IV supercomplex loss, reduced OCR, COX1 sensitized to
  copper limitation) plus two decades of yeast genetics. This is the core BP.
- `GO:0005758 mitochondrial intermembrane space` — twin CX9C/MIA substrate, yeast localization
  data, InterPro IPR039870. Core CC.

**Uninformative but not wrong**
- `GO:0005515 protein binding` (IPI, PMID:33961781, with COX11). Per repository guidelines this
  term is uninformative regardless of evidence quality. The real content — a specific,
  conserved, functionally consequential contact with COX11 — is carried by the complex IV
  assembly annotation and by `core_functions`. Mark over-annotated, keep the partner recorded in
  `supporting_entities`.

**Redundant generalization**
- `GO:0005739 mitochondrion` (×3: IEA, HTP, IDA). Correct but subsumed by the IMS annotation.

**Candidate not currently annotated**
- `GO:0006878 intracellular copper ion homeostasis`. Reduced mitochondrial/cellular copper is
  reproducible across yeast coa4Δ [PMID:20624914, PMID:35666203] and human COA4-KO (2026, with
  Fe/Zn/Mn controls). **But** it may be a downstream consequence of failed CcO metallation
  rather than a separate role — the 2022 authors themselves frame it as one of "2 distinct but
  closely related roles", and comparable copper deficiency is seen in SCO1/SCO2/COX10/COX15
  patient fibroblasts, where it is attributed to CTR1 turnover/mislocalization. Left out of
  `core_functions`; raised in `suggested_questions` instead.

**Molecular function: still unknown.** No catalytic activity is established, and metallochaperone
activity is positively excluded. The best current statement is an accessory/regulatory role
supporting COX11-mediated CuB metallation of COX1 — which the ontology does not currently express
well for this case. Asserting a specific MF term here would over-reach; `core_functions` therefore
carries the BP + CC with a mechanistic description rather than an invented MF.

## Open questions

- Is COA4's molecular role stabilizing COX11, loading COX11 with copper, or gating handoff to
  COX1? The reciprocal abundance regulation and the KO's COX11 loss are consistent with a
  stabilizing/chaperone-like role, but do not distinguish these.
- Is the copper-homeostasis phenotype direct, or secondary to CcO failure? A CTR1
  turnover/localization experiment in COA4-KO cells would separate them.
- Does Ptc5-mediated dephosphorylation regulate Coa4? Only co-IP enrichment supports this so far.
- Isoform 2 (Q9NYJ1-2, VSP_030428) extends the N-terminus (M → MFYRLPIPRM). All functional work
  is on isoform 1; no isoform-specific data exist.
- COA4 is estrogen-inducible [UniProt `INDUCTION`, PMID:11085516] — biological significance unknown.
