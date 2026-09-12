# ADCK1 (Q86TW2) — review notes

Human AarF domain-containing protein kinase 1, 530 aa, chromosome 14, HGNC:19038.
PANTHER family `PTHR43173` (ABC1 family protein), subfamily `PTHR43173:SF19`
(AARF DOMAIN-CONTAINING PROTEIN KINASE 1). Reviewed for the PAINT campaign,
deep research provider **affinage** (`gates_passed: True`, 5 citations, all
numeric PMIDs, no `PMID:bio_*` preprint ids).

## 0. GOA / stub reconciliation (done before reviewing anything)

```
ADCK1-goa.tsv               9 lines  =  8 data rows + 1 header
distinct data rows          8
stub `- term:` entries      8
```

Exact match. No collapsed `GO:0005515` partner rows and no same-term/different-assigner
collapse, because the gene has **zero** `GO:0005515` rows and its three `GO:0005739`
rows differ in evidence code and reference (so the seeding key
`(GO ID, evidence_type, reference, negated, qualifier)` separates them).
QuickGO independently returns `numberOfHits: 8` for `UniProtKB:Q86TW2`, matching the
TSV exactly, so nothing has been dropped between GOA and the local snapshot.

## 1. The headline: the kinase-activity annotations are NOT in GOA — they are in UniProt

The campaign hypothesis was that `GO:0004672`/`GO:0006468` would be present on ADCK1
as fold-name-propagated errors. **They are not.** GOA carries no molecular-function
term of any kind for ADCK1 — the eight rows are three IBA (one CC, two BP), three
`GO:0005739` localisation rows, and two IMP BP rows. PAINT gave the ADCK1 node no MF
term at all (see §4). *Hypothesis not confirmed in GOA.*

The error is one layer upstream. UniProt still carries, from the generic protein-kinase
ProRule rather than from data:

```
[file:human/ADCK1/ADCK1-uniprot.txt "EC=2.7.-.- {ECO:0000255|PROSITE-ProRule:PRU00159};"]
[file:human/ADCK1/ADCK1-uniprot.txt "KW   Alternative splicing; ATP-binding; Kinase; Mitochondrion;"]
[file:human/ADCK1/ADCK1-uniprot.txt "KW   Serine/threonine-protein kinase; Transferase; Transit peptide."]
[file:human/ADCK1/ADCK1-uniprot.txt "DR   GO; GO:0004674; F:protein serine/threonine kinase activity; IEA:UniProtKB-KW."]
[file:human/ADCK1/ADCK1-uniprot.txt "DR   GO; GO:0005524; F:ATP binding; IEA:UniProtKB-KW."]
```

and in the same entry says the opposite:

> [file:human/ADCK1/ADCK1-uniprot.txt "not yet clear (Probable). It is not known if it has protein kinase"]
> [file:human/ADCK1/ADCK1-uniprot.txt "activity and what type of substrate it would phosphorylate (Ser, Thr or"]

Those two `IEA:UniProtKB-KW` GO cross-references are absent from the current GOA TSV
and from QuickGO, consistent with the GOA-wide withdrawal of `GO_REF:0000043`
Swiss-Prot-keyword annotations. So the defect currently reaches users through the
UniProt entry (keywords, EC number, protein name) rather than through GO. It is
recorded here and in `suggested_questions` as a UniProt correction to report, not as
an `existing_annotations` action, because there is no annotation to act on.

**Careful about the mirror error.** "No canonical protein kinase activity" is *not*
the same as "no catalytic activity", and the measurement below refuses the stronger
claim (§3).

## 2. What COQ8A/COQ8B were actually shown to do (primary sources, not family prose)

- Stefely et al. 2015, ADCK3/COQ8A crystal structure
  [PMID:25498144 "We find that multiple UbiB-specific features are poised to inhibit protein kinase activity, including an N-terminal domain that occupies the typical substrate binding pocket and a unique A-rich loop that limits ATP binding by establishing an unusual selectivity for ADP."]
  and
  [PMID:25498144 "A single alanine-to-glycine mutation of this loop flips this coenzyme selectivity and enables autophosphorylation but inhibits coenzyme Q biosynthesis in vivo"].
  That single mutation is **ADCK3 A339G**.
- Stefely et al. 2016
  [PMID:27499294 "Although COQ8 was predicted to be a protein kinase, we demonstrate that it lacks canonical protein kinase activity in trans. Instead, COQ8 has ATPase activity and interacts with lipid CoQ intermediates"].

The GO record matches: COQ8A (Q8NI60) and COQ8B (Q96D53) each carry
`GO:0004672 NOT|enables` **and** `GO:0006468 NOT|involved_in`, both IDA from
PMID:27499294 — while COQ8A simultaneously carries `GO:0016301 kinase activity` (IDA,
two references) and `GO:0043531 ADP binding` (IDA, PMID:25498144). So the curated
consensus is precise: *not a protein kinase; still a nucleotide-using enzyme.*
**The one exception, and it is a real one.** A 2024 paper does demonstrate protein-kinase
activity for a UbiB protein:
[PMID:38425362 "Intact protein MS validated this idea: COQ3, but not COQ6, is phosphorylated by COQ8B at multiple sites"].
It is the source of COQ8B's non-negated `GO:0004672` IDA, which now sits alongside that
gene's own `NOT|enables GO:0004672` row. Two caveats bound how far it reaches:

1. The enzyme is an **ancestral reconstruction**, not the extant human protein —
   [PMID:38425362 "Ancestral COQ8A and COQ8B were purified as membrane-bound recombinant proteins; however, COQ8A produced very low yields compared with COQ8B."]
   — and the paper never states that it switched to extant COQ8B for the phosphorylation
   experiment.
2. The **residue class was not determined** ("at multiple sites"), so this does not
   establish Ser/Thr specificity for any UbiB protein.

The same paper also rules out small-molecule kinase activity:
[PMID:38425362 "Critically, GC/MS analyses did not detect any phosphorylated CoQ intermediates, suggesting that the enzyme is not a small-molecule kinase."]

*I initially wrote, twice, that no UbiB protein had been shown to phosphorylate a protein
substrate in trans. That was false, and the refuting paper was already in my cache — the
same failure shape as the ACBD3 acyl-CoA reversal. Corrected at every site; the UniProt
recommendation survives on the narrower and still-sound grounds above.*

## 3. Which motifs ADCK1 actually retains — measured, not asserted

`ADCK1-bioinformatics/ubib_motif_scan.py` (see `RESULTS.md`). Every motif column is
anchored on a residue that **PKA's own UniProt feature table annotates**, and the run
aborts unless the alignment reproduces published/curated positions (ADCK1 K183/D315;
COQ8A K358/D488/N493/D507; COQ8A A339 in the P-loop column). It does.

**Retained — the phosphotransfer active site is intact.** ADCK1 keeps the β3 lysine
(K183), the catalytic aspartate (D315), the catalytic-loop asparagine (N320) and the
Mg-binding aspartate (D338). All four are conserved in **8/8** of the UbiB proteins
examined (ADCK1, ADCK2, ADCK5, COQ8A, COQ8B, yeast Cqd1, Cqd2, Coq8).

**Divergent — the two UbiB diagnostics.**

| | P-loop (curated ATP BINDING site) | GxGxxG glycines | catalytic loop |
|---|---|---|---|
| PKA-Cα | `LGTGSFGRV` (50..58) | 3/3 | `YRD` |
| **ADCK1** | `LGTASLAQV` (161..169) | **1/3** (G162, **A164**, A167) | **`HCD`** |
| ADCK2 | `VGSGCVAQV` (206..214) | 2/3 | `HAD` |
| COQ8A | (not curated; aligned) | 1/3 (A337, **A339**, G342) | `QTD` |
| Cqd2/Mcp2 | (not curated; aligned) | 1/3 | `HCD` |

Two things follow, and they are the load-bearing facts of this review:

1. **ADCK1's A164 sits in the same P-loop column as COQ8A's A339** — the residue whose
   Ala→Gly substitution flips COQ8A from ADP- to ATP-selectivity. The script asserts
   this correspondence rather than assuming it. So the ATP-ligand assignment on
   ADCK1's `BINDING 161..169` / `BINDING 183`, which comes from
   `[file:human/ADCK1/ADCK1-uniprot.txt "/evidence=\"ECO:0000255|PROSITE-ProRule:PRU00159\""]`,
   is a rule transfer that the one characterised relative with the same loop
   **contradicts in ligand identity**.
2. **No UbiB protein has the HRD arginine** — 0/8, versus the PKA control. Checked
   alignment-free (PASS 3 reads the two residues before each protein's own catalytic
   Asp straight from its sequence), because the first pass reported this as an
   alignment gap and a gap can be an artefact. It is not: ADCK1 reads `H313-C314-D315`.

Note ADCK1 and yeast Cqd2 share the identical `HCD` catalytic loop, which is a small
independent corroboration of the orthology PANTHER asserts.

## 4. PAINT: one node, three terms, one seed

`interpro/panther/PTHR43173/PTHR43173-paint.tsv`:

```
PTHR43173  PTN005148758  GO:0005743  C  IBD  SGD:S000004243  taxon:2759
PTHR43173  PTN005148758  GO:0007005  P  IBD  SGD:S000004243  taxon:2759
PTHR43173  PTN005148758  GO:0055088  P  IBD  SGD:S000004243  taxon:2759
```

- **One node, one seed.** `SGD:S000004243` resolves to `Q06567` / `MCP2_YEAST`,
  Swiss-Prot, 569 aa, "ABC1 family protein MCP2" (= Ylr253w = Cqd2). It is in the
  **same PANTHER subfamily SF19** as human ADCK1, i.e. an ortholog, not a paralog.
  Its own SF19 co-members are ADCK1 orthologs across metazoa plus *S. pombe*
  SPBC15C4.02 and *A. thaliana* At2g40090.
- **The donor carries its own experimental evidence for all three terms**, from
  PMID:23781023: `GO:0005743` IDA, `GO:0007005` IMP + IGI, `GO:0055088` IGI. So
  `SOURCE_WEAK_OR_INFERRED` / `SOURCE_EVIDENCE_WEAK` would be factually false here.
- **The node's reach is 97 entities**, identical for all three terms (QuickGO
  `withFrom=PANTHER:PTN005148758`), spanning metazoa, fungi, plants, algae and
  ciliates. Human ADCK5 (Q3MIX3), which sits in the *same family* PTHR43173 but in
  subfamily SF28, receives **none** of the three — it has only 4 GO annotations total
  and no IBA at all. So the node is SF19-scoped in practice, which is the right scope.
- **The IBA lands at the same term the donor holds**, not above it — the ACRV1-style
  "propagation landed three levels above its donor" defect is **absent here**. Checked
  and negative; no downward MODIFY warranted.
- **No MF term anywhere on the node.** PAINT modelled the family's uncertainty about
  catalysis correctly.

## 5. Does ADCK1 have a coenzyme Q role?

This is where the naive family story would over-reach, and where the yeast ortholog
turns out to matter.

- Human ADCK1 has **no** `GO:0006744` annotation, and none is warranted: there is no
  human or *Drosophila* CoQ measurement for ADCK1 anywhere I could find. COQ8A and
  COQ8B both carry `GO:0006744` by IMP/IDA/IBA, from a **different** PANTHER node
  (WITH/FROM `AGI_LocusCode:AT4G01660`, `FB:FBgn0052649`), so the CoQ-biosynthesis
  term has not leaked across into the ADCK1 clade.
- **But the yeast ortholog does have a CoQ phenotype.** Kemmerer et al. 2021 renamed
  Mcp2 to **Cqd2**:
  [PMID:34362905 "Beyond Coq8 and Cqd1, the S. cerevisiae genome encodes just one other member of the UbiB family"],
  and
  [PMID:34362905 "Loss of Cqd1 skews cellular CoQ distribution away from mitochondria, resulting in markedly enhanced resistance to oxidative stress caused by exogenous polyunsaturated fatty acids, whereas loss of Cqd2 promotes the opposite effects."].
  This is CoQ **distribution**, explicitly not biosynthesis:
  [PMID:34362905 "Total cellular CoQ levels remained unchanged (Supplementary Fig. 3b), again suggesting these CoQ-related phenotypes are unrelated to CoQ biosynthesis."].
- **And it is catalysis-dependent in yeast**:
  [PMID:34362905 "Similar to Cqd1 (Fig. 3g), Cqd2 function was dependent on intact canonical PKL and UbiB-specific residues"].

This is the direct counterweight to the *Drosophila*/human kinase-independence result
(§6) and the reason this review does **not** assert that ADCK1 is catalytically dead.
Two different readouts in two different organisms; the honest position is that they
are not yet reconciled. Filed as a `suggested_question` and a `suggested_experiment`.

Note also that the human ortholog of yeast **Cqd1** is **ADCK2**, not ADCK1 — the
2021 paper says so, and my alignment agrees (ADCK2 and Cqd1 share the `HAD` catalytic
loop and a 2/3 P-loop, against ADCK1/Cqd2's `HCD` and 1/3). Getting this pairing wrong
would have imported ADCK2's CoQ10-deficiency myopathy literature onto ADCK1.

## 6. What the human/fly evidence actually shows

Yoon et al. 2019 (PMID:31125351) is the only paper behind both IMP rows, and it has
genuine **human** experiments, not only fly ones:

- Human HeLa siRNA knockdown, TEM:
  [PMID:31125351 "As a result, the mitochondrial length was increased and the number of mitochondrial cristae was decreased by ADCK1 knockdown"].
  Increased length = increased fusion (supports `GO:0010637`), fewer cristae
  (supports `GO:1903852`). Both rows are IMP and both are correctly human-grounded.
- Epistasis places ADCK1 upstream of YME1L1:
  [PMID:31125351 "the flies over-expressing dADCK1 with simultaneous dYME1L1 knockdown successfully survived into adulthood"].
- OPA1 processing, HEK293T:
  [PMID:31125351 "The result demonstrated that the over-expression of both OPA1 and ADCK1 led to increased cleavage of L-OPA1"].
- Kinase-independence:
  [PMID:31125351 "In our experiment, we engineered kinase-dead mutant forms of ADCK1 with substitutions of the key amino acids related to the phosphotransferase activity of ADCK1, such as A164G, K183I, D315A, and D338N mutations"]
  and
  [PMID:31125351 "Over-expression of each mutant as well as the triple-mutation-containing form (K183I-D315A-D338N; 3KD) of ADCK1 still induced the same phenotypes similar to ADCK1 wild type, and thus we concluded that the phenotypes induced by ADCK1 are kinase-independent"],
  with the endogenous-kinase control
  [PMID:31125351 "we performed an experiment of over-expressing the kinase-dead form of ADCK1 in ADCK1 knocked down HeLa cells by expressing siRNA for ADCK1 and were able to obtain the identical conclusion"].

  **Read the scope of this correctly.** Every one of these assays is a *gain-of-function*
  readout: the mutants were scored for whether they still produce the **over-expression**
  phenotype. The paper says as much in its own section heading, "Phenotypes induced by
  ADCK1 over-expression are independent of its kinase activity". It shows the
  over-expression phenotype does not need the motifs. It does **not** show that ADCK1
  lacks catalytic activity, and the authors do not claim that — they state the prior
  honestly: [PMID:31125351 "Until now, ADCK1 was predicted to be a kinase, yet there were no available reports to confirm it."]
  No in vitro assay of purified ADCK1 has ever been published.

**Independent mammalian corroboration, 2025** (PMID:40884816, brain endothelial cells,
mouse):
[PMID:40884816 "We first confirmed that mouse ADCK1 was localized to the mitochondrial inner membrane in primary brain ECs"]
— a second, mammalian line of evidence for the inner-membrane localisation that human
ADCK1 currently holds only by IBA. Also
[PMID:40884816 "Co‐IP assay detecting interaction between ADCK1 and IMMT in primary brain ECs"],
ADCK1–OPA1 co-IP, and reciprocal ADCK1-HA / Adck1-shRNA control of L-OPA1 cleavage.
The paper reproduces Yoon's OPA1-processing result in a second organism and a second
lab, which is why `GO:0010954 positive regulation of protein processing` is proposed as
a NEW annotation rather than left as narrative.

## 7. Checks run, including the ones that came back negative

- **Retraction / erratum / expression-of-concern.** All eight PMIDs relied on
  (31125351, 33988507, 34800366, 31175694, 33824271, 36371387, 40884816, 23781023)
  were queried through `efetch` and read for `CommentsCorrections/RefType` on each
  record. **None carries any retraction, erratum, correction or expression of
  concern.** Negative result, reported.
- **Reference-projection check** (does a reference annotate a complex plus all its
  subunits with identical evidence?). `PMID:34800366` has **1235** annotations, all
  `GO:0005739` on the page sampled; it is a mitochondrial-proteome survey, so a large
  entity count is its design, and crucially **no functional or phenotype term spreads
  with it** — the second discriminator is negative, so this is not a projection defect.
  The result is paginated (100 of 1235 returned), so the exact entity count is
  **unavailable** and is not substituted with the annotation total. `PMID:33988507` is
  small and unambiguous: 6 annotations over 4 entities.
- **IntAct / partner promiscuity.** ADCK1 has 71 IntAct and 80 BioGRID interactions per
  the UniProt cross-references, yet **zero** `GO:0005515` rows in GOA. There is nothing
  to over-annotate and nothing to prune; the check is vacuous for this gene and is
  recorded as such rather than skipped.
- **Sibling/paralog consistency.** *Corrected after an initial wrong answer:* `COQ8A`
  and `COQ8B` **do** have merged reviews (both landed in PR #2108, the CoQ10 module;
  both `status: INITIALIZED` but with real verdicts). `ADCK2` and `ADCK5` have none.
  No row is shared between those reviews and this one, so there is no direct
  disagreement, but the framing lines up: COQ8A's review ACCEPTs both NOT rows,
  MODIFYs `GO:0016301 kinase activity` → `GO:0016887 ATP hydrolysis activity`, MODIFYs
  the `GO:0004672` ISS → `GO:0005524` + `GO:0016887`, and MARK_AS_OVER_ANNOTATEDs
  `GO:0016310 phosphorylation` — i.e. the same "not a protein kinase, still a
  nucleotide-using enzyme" reading this review takes. **One divergence worth flagging
  to whoever owns those files:** COQ8B's review ACCEPTs its non-negated `GO:0004672`
  IDA *and* ACCEPTs its `NOT|enables GO:0004672` IDA, which cannot both be right as
  they stand. If ADCK2 or ADCK5 is reviewed later, the `GO:0055088` IBA is the row to
  compare — ADCK5 is in the same PANTHER *family* but does **not** carry it.
- **`is_active_in` vs `located_in`.** The `GO:0005743` row uses `is_active_in`, which
  presupposes an activity exerted there. ADCK1's demonstrated role (regulating
  YME1L1-dependent OPA1/IMMT handling) is exerted at the inner membrane whether or not
  it is catalytic, so the qualifier stands. Considered and kept, not overlooked.

## 8. The colon-cancer TCF4 claim — recorded, not annotated

PMID:33824271 reports
[PMID:33824271 "the endogenous Co-IP experiment showed that endogenous ADCK1 and TCF4 formed a complex"]
and builds a β-catenin/TCF signalling role on it. This is topologically awkward: ADCK1
has a mitochondrial transit peptide and every localisation measurement on it — the
kinome atlas IDA, the mitochondrial-proteome HTP, mouse primary brain ECs — places it
in mitochondria; the paper reports no localisation experiment placing ADCK1 in the
nucleus or cytosol. Single lab, not replicated. It has produced **no** GO annotation,
so there is nothing to review; it is recorded here and raised as a question rather
than proposed as a term.

The osteosarcoma paper (PMID:36371387) is consistent with the mitochondrial story —
[PMID:36371387 "ADCK1 depletion disrupted mitochondrial functions in OS cells and induced mitochondrial membrane potential reduction, ATP depletion, reactive oxygen species production."]
— but adds no term beyond what is already annotated.

## 9. Bottom line

ADCK1 is a mitochondrial inner-membrane UbiB-family protein that sets mitochondrial
inner-membrane architecture by acting upstream of the YME1L1 protease, restraining
fusion and promoting cristae formation. Its catalytic status is genuinely open: the
phosphotransfer active site is intact and its yeast ortholog needs those residues,
while the mammalian over-expression phenotype does not. Its molecular function is
therefore left unannotated in GO, which is the correct state, and the actionable
defects are upstream in UniProt.
