# E2F1 (human, UniProt Q01094) — curation notes

Working notes for the GO annotation review in `E2F1-ai-review.yaml`. Sources: the
seeded GOA rows, `E2F1-uniprot.txt`, `E2F1-deep-research-falcon.md`, and the cached
publications in `publications/`. Quotes below are verbatim from the cited source.

## 1. Identity and architecture

Unambiguously human E2F transcription factor 1, the founding member of the activator
E2F class. The historical aliases RBAP-1 / RBBP3 record its discovery as a
retinoblastoma-protein-binding factor, which is why so much of its annotation set is
RB1-centric. UniProt features fix the domain layout: `DNA_BIND 110..194`, a
`REGION 67..108` "Cyclin A:CDK2 binding", `REGION 195..284` "Dimerization",
`REGION 368..437` "Transactivation", and `REGION 409..426` "RB1 binding".

The protein is an obligate heterodimer, which matters for grading nearly every MF row
[UniProt Q01094, "SUBUNIT: Component of the DRTF1/E2F transcription factor complex. Forms"].
TFDP3 is the exception that proves the rule — it binds E2F1 but the resulting dimer
cannot engage DNA [PMID:17062573 "Although TFDP3 retained the capacity to bind to E2F
proteins, the resulting heterodimers failed to interact with the E2F consensus sequence."].

## 2. Core molecular function

A sequence-specific Pol II transcriptional activator
[UniProt Q01094, "Transcription activator that binds DNA cooperatively with DP"], driving
the G1/S program [UniProt Q01094, "The DRTF1/E2F complex functions in the control of"].
E2F1 over-expression forces quiescent cells into S phase
[PMID:20224733 "Overexpression of E2F-1 is sufficient to induce S-phase in most quiescent
cells, as reported previously 30, 31."] and reduces the G1 fraction of cycling cells
[PMID:20224733 "It was found that the overexpression of E2F-1/wt and E2F-1/411
significantly decreased the cell number in G1 phase compared to the control (pX17) cells."].
The deep research reaches the same conclusion
[file:human/E2F1/E2F1-deep-research-falcon.md "The best-established physiological role is
activation of a coordinated proliferation program at the **G1/S transition**."].

It is not an enzyme
[file:human/E2F1/E2F1-deep-research-falcon.md "Its primary molecular function is to act in
the **nucleus as a sequence-specific, DP-dependent transcriptional activator**."].

## 3. The RB1 switch, and why repression was ACCEPTed

The Rb-E2F complex is structurally settled
[PMID:16360038 "The crystal structure of an RbC-E2F1-DP1 complex reveals an intertwined
heterodimer in which the marked box domains of both E2F1 and DP1 contact RbC."], with a
second, pocket-domain interface on E2F1 residues 409-426
[PMID:12598654 "The fragment of E2F used in our structural studies, residues 409–426 of
E2F-1, represents the core of the pRb-binding region of the transcription factor."].
Repression works by masking, not by an intrinsic E2F1 repressor activity
[PMID:9468140 "Rb, which is recruited to target promoters by E2F1, represses transcription
by masking the E2F1 transactivation domain and by inhibiting surrounding enhancer elements"].

**Decision point.** `GO:0000122` (negative regulation of transcription by Pol II, IMP,
PMID:20224733) was initially graded `KEEP_AS_NON_CORE` on the reasoning that RB1 does the
repressing. On review that was inconsistent: the same file treats the Rb-E2F corepressor
platform as `core_functions[1]`. E2F1 does part of the work — it supplies the
sequence-specific DNA binding that positions RB1 and its deacetylase activity on the
promoter, and repression fails when that interface is broken (the Y411C/411 mutant). This
is the *scaffold* shape of participation described in CLAUDE.md, so the row was upgraded to
`ACCEPT`. The paper is explicit that the direction depends on cell-cycle position
[PMID:20224733 "E2F-1 acts as part of the repression complex with pRB in the expression of
DHFR, b-myb, TK and cdc2 in asynchronously growing cells; on the other hand, E2F-1 acts as
an activator in the expression of the same genes in cells that are re-entering the cycle."].
Note this study used a murine fibroblast line carrying human E2F1 constructs.

## 4. Apoptotic arm

Stabilisation is the trigger
[PMID:12717439 "A Chk2 consensus phosphorylation site in E2F-1 is phosphorylated in
response to DNA damage, resulting in protein stabilization, increased half-life,
transcriptional activation and localization of phosphorylated E2F-1 to discrete nuclear
structures."], and the output is apoptosis
[PMID:12717439 "Expression of a dominant-negative Chk2 mutant blocks induction of E2F-1 and
prevents E2F-1-dependent apoptosis."]. Direct pro-apoptotic targets are well attested:
ASPP1/2 [PMID:15731768 "We show here that E2F-1 binds in vivo the promoters of ASPP1 and
ASPP2 genes, two activators of p53-mediated apoptosis, E2F-1, E2F-2 and E2F-3 all activate
the isolated ASPP1 and ASPP2 promoters."], p73 via MCPH1
[PMID:18660752 "MCPH1 interacts with E2F1 on the p73 promoter, and regulates p73 induction
and E2F1-induced apoptosis as a result of DNA damage."], and the p53-independent mediator
DIP [PMID:15565177 "Yet, inhibition of endogenous DIP function by small interfering RNA
rescued p53-negative cells from E2F1-induced apoptosis, indicating that DIP is an essential
mediator of the p53-independent E2F1 death pathway."].

`GO:0000077` (DNA damage checkpoint signaling, IMP) was graded `KEEP_AS_NON_CORE`: the
checkpoint signal is generated by ATM/ATR-CHK2, and E2F1 is the transcriptional output.
The authors themselves hedge [PMID:12717439 "These results suggest a role for E2F-1 in
checkpoint control and provide a plausible explanation for the tumour suppressor activity
of E2F-1."]. `GO:0008630` was `ACCEPT`ed as the accurate representation.

## 5. Transcription-independent role at DNA lesions — and why no BP term was asserted

Strong, direct evidence
[PMID:20972224 "Here we demonstrate that E2F1 associates with the GCN5 histone
acetyltransferase in response to UV radiation and recruits GCN5 to sites of damage."],
[PMID:20972224 "UV radiation induces the acetylation of histone H3 lysine 9 (H3K9) and this
requires both GCN5 and E2F1."], and E2F1 is an accessory factor, not an enzyme
[file:human/E2F1/E2F1-deep-research-falcon.md "E2F1 is consequently an **accessory
organizer**, not a nuclease, ligase, helicase, or repair enzyme."].

**Decision point.** I considered a `NEW` row for `GO:0006281` (DNA repair), and declined.
PMID:20972224 is already cited in GOA — for the KAT2A `protein binding` row — so a curator
read this paper and chose *not* to make a repair annotation. That is precisely the
"do not add what curators deliberately declined to add" case in CLAUDE.md. The recruitment
activity that E2F1 genuinely contributes is instead captured as MF `GO:0035035`
(histone acetyltransferase binding), which is where the KAT2A interaction rows were
retargeted, and `core_functions[3]` asserts no process term. The annotation gap is raised
in `suggested_questions` for expert adjudication rather than filled unilaterally.

## 6. GO:0005515 sweep (61 rows)

Per the repository policy, bare `protein binding` takes only `MODIFY` / `REMOVE` /
`UNDECIDED` (a validator enforces this). Every row was traced to its partner and split:

- **RB1 / pocket proteins (14 rows) → `MODIFY` to `GO:0001222`** transcription corepressor
  binding. Includes the structural papers and the AP-MS network studies.
- **DP partners TFDP1/2/3 (8 rows) → `MODIFY` to `GO:0046982`** protein heterodimerization
  activity, the obligate dimerization that licenses DNA binding.
- **Coactivators (9 rows) → `MODIFY` to `GO:0001223`**: TRRAP
  [PMID:11418595 "We conclude that E2F stimulates transcription by recruiting
  acetyltransferase activity and the essential cofactors GCN5 and TRRAP."], PARP1
  [PMID:14627987 "Protein-binding reactions and coimmunoprecipitation experiments with
  purified PARP-1 and E2F-1, however, revealed that PARP-1 binds to E2F-1 in vitro."],
  DDB2, HCFC1, PHF8, MCPH1, RRP1B, BIRC2/cIAP1
  [PMID:21653699 "Here, we show that the N-terminal part of cIAP1 directly interacts with
  the DNA binding domain of the E2F1 transcription factor."].
- **HATs KAT2A/GCN5 (3 rows) → `GO:0035035`**; **deacetylases HDAC1/SIRT1 (6 rows) →
  `GO:0042826`**, including KAP1-bridged HDAC1
  [PMID:17704056 "KAP1 stimulates formation of E2F1-HDAC1 complex and inhibits E2F1
  acetylation."]. The HDAC1 rows from PMID:9468139/9468140 are Rb-bridged rather than
  direct; `histone deacetylase binding` does not overstate this.
- **Corepressors TRIM28, NCOR2, L3MBTL3 → `GO:0001222`**; **CDK8 → `GO:0019901`**;
  **SP1, STAT1 → `GO:0140297`**.
- **12 rows → `REMOVE`** as uninformative with no better term available: four viral E7
  pairs (host-virus, not an E2F1 function); high-throughput pairs with no functional
  follow-up (APP, PARP1/PMID:20133863 whose mechanism runs through E2F4/p130); and
  regulatory inputs where E2F1 is the *substrate or target* rather than the actor —
  PRMT5 methylating E2F1, L3MBTL3 reading methyl-K185 for degradation, BTG3 and TOPBP1
  inhibiting E2F1, TRIM16 reducing E2F1 levels. Removal does not question any interaction.

## 7. Rodent-derived electronic annotations

Five Ensembl-Compara rows propagated from rat/mouse were graded
`MARK_AS_OVER_ANNOTATED` because they encode experimental *context* rather than function:
response to LPS (traceable to a microglial Reg3g GO-CAM, `gocams/6348a65d00001191`),
cellular response to fatty acid, hypoxia, and NGF. `GO:0070345` (negative regulation of fat
cell *proliferation*, IEA + ISS) is separately problematic: the underlying experiments
concern blocked adipocyte *differentiation* via C/EBPalpha
[UniProt Q01094, "Blocks adipocyte differentiation"], and E2F1 promotes rather than
restrains proliferation — so the term looks mis-scoped at the mouse source.
`GO:0045599` (negative regulation of fat cell differentiation) is properly supported
[PMID:20176812 "E2F represses the transactivation of C/EBPα target genes by disrupting the
binding of C/EBPα to its cis -regulatory sites."] and was kept as non-core. Spermatogenesis
and glial cell proliferation were kept as non-core tissue-level outputs of the generic
G1/S program.

`GO:0048255` (mRNA stabilization, IDA) was `MARK_AS_OVER_ANNOTATED`: E2F1 has no
RNA-binding domain, and the observation
[PMID:15766563 "Second, E2F1 induces stabilisation of axin2 mRNAs."] is a downstream
phenotype most simply explained by E2F1-dependent transcription of an RNA-binding
regulator. Not removed, since the result stands unchallenged.

## 8. IBA rows

Four IBA rows (`GO:0000978`, `GO:0000981`, `GO:0006357`, `GO:0035189`) were all
`ACCEPT`ed. Sequence-specific Pol II transcription regulation is the ancestral activity of
the E2F family, so the node placement is sound. `GO:0035189` and `GO:0006357` list
`UniProtKB:Q01094` in their own WITH/FROM — per CLAUDE.md this is expected and correct, a
marker that experimental grounding exists on the target itself, and was *not* treated as
circular.

## 9. Generalisation pattern

The largest single group of `MODIFY` calls (68 total) generalises or specialises to the
Pol II-specific branch: `GO:0003677` DNA binding → `GO:0000978`; `GO:0003700` /
`GO:0001216` → `GO:0000981` / `GO:0001228`; `GO:0045893` / `GO:0010628` / `GO:0006355` →
`GO:0045944` / `GO:0006357`; `GO:0006351` (DNA-templated transcription, IEA + ISS) →
`GO:0006357`, since a TF regulates transcription rather than performing it;
`GO:0032991` (root complex term) → `GO:0090575`.

## 10. Open questions carried into the review

1. Should the lesion-associated repair role be annotated on E2F1, or modelled as a causal
   GO-CAM edge to the acetyltransferase it recruits?
2. Should negative-regulation terms sit on E2F1 at all, given RB1 executes the repression?
3. Are single-context rodent response-to-stimulus terms appropriate for propagation?
