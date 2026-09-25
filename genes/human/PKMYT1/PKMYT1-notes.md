# PKMYT1 (human, Q99640) — curation notes

Working journal for the GO annotation review of human PKMYT1 (Myt1 kinase).
Sources: `PKMYT1-uniprot.txt`, `PKMYT1-goa.tsv`, `PKMYT1-deep-research-falcon.md`,
cached publications under `publications/`, and QuickGO term lookups.

## 1. Identity and gestalt

- UniProt Q99640, `PMYT1_HUMAN`, 499 aa. RecName: "Membrane-associated tyrosine- and
  threonine-specific cdc2-inhibitory kinase"; EC 2.7.11.1. Family: protein kinase
  superfamily, Ser/Thr protein kinase family, **WEE1 subfamily**.
- Domain architecture from the UniProt feature table: protein kinase domain 110–359;
  active site (proton acceptor) Asp233; ATP binding 116–124 and 139; Mg(2+) binding
  238/251/253; **membrane-association motif 382–398**; **interaction with CDC2-CCNB1
  437–499**; interaction with PIN1 398–499; Ser426 phosphorylated **by PLK1**
  (UniProt cites Nakajima et al. 2003, PubMed 12738781).
- Not to be confused with the lncRNA *PKMYT1AR*, which the deep-research report
  explicitly separates from this gene.

The picture that all three evidence streams agree on: PKMYT1 is the **membrane-anchored**
WEE1-family brake on mitotic entry, acting on **cyclin-bound CDK1 at Thr14**, with a
second, non-catalytic arm — **docking/sequestration of cyclin B1–CDK1** — that WEE1 does
not have.

## 2. Primary literature

### PMID:9001210 (Liu, Stanton, Wu, Piwnica-Worms, Mol Cell Biol 1997) — abstract only in cache

- Dual specificity + Thr14 preference + cyclin dependence:
  [PMID:9001210 "report the isolation of a novel human cDNA encoding a dual-specificity protein kinase (designated Myt1Hu) that preferentially phosphorylates Cdc2 on threonine 14 in a cyclin-dependent manner"]
- Site logic: [PMID:9001210 "phosphorylation of threonine 14 and tyrosine 15 is inhibitory"]
  (versus Thr161, which is activating).
- Localisation: [PMID:9001210 "Myt1Hu localizes to the endoplasmic reticulum and Golgi complex in HeLa cells"]
- Membrane anchor, and the origin of every "nucleus" annotation in this record:
  [PMID:9001210 "A stretch of hydrophobic and uncharged amino acids located outside the catalytic domain of Myt1Hu is the likely membrane-targeting domain, as its deletion results in the localization of Myt1Hu primarily to the nucleus"]
  — note this is the **mutant**; wild-type protein is not nuclear.

### PMID:9268380 (Booher, Holman, Fattaey, JBC 1997) — abstract only in cache

- Substrate restriction (the basis of the IDA rows for GO:0004674 and GO:0010972):
  [PMID:9268380 "We find that human Myt1 phosphorylates and inactivates Cdc2-containing cyclin complexes but not complexes containing Cdk2 or Cdk4"]
- Membrane residence throughout the cycle — decisive against nuclear annotations:
  [PMID:9268380 "Analysis of endogenous Myt1 demonstrates that it remains membrane-bound throughout the cell cycle"]
- Mitotic downregulation: [PMID:9268380 "its kinase activity decreased during M phase arrest, when Myt1 became hyperphosphorylated"]
- Conclusion: [PMID:9268380 "Myt1 inhibits mitosis due to its specificity for Cdc2.cyclin complexes"]

### PMID:10373560 (Liu, Rothblum-Oviatt, Ryan, Piwnica-Worms, Mol Cell Biol 1999) — full text in cache

This is the only full-text primary paper available, and it is also the IntAct source for
the CDK1 (P06493) and CCNB1 (P14635) interaction rows. It does far more than record a
binary interaction:

- [PMID:10373560 "The COOH-terminal 63 amino acids of Myt1 were identified as a Cdc2-cyclin B1 interaction domain"]
- Residue-level mapping of an RXL motif:
  [PMID:10373560 "cyclin B1 coimmunoprecipitated with wild-type Myt1 (lane 2) but not the mutant form of Myt1 (lane 3), indicating that residues R, N, and L at positions 486, 487, and 488, respectively, are important for cyclin B1 binding"]
- Docking is required for catalysis:
  [PMID:10373560 "deletion of the COOH-terminal 63 amino acids of Myt1 impaired the ability of Myt1 to phosphorylate Cdc2 in vitro"]
- Non-catalytic arm:
  [PMID:10373560 "overproduction of Myt1 perturbs cell cycle progression by sequestering Cdc2-cyclin B1 complexes in the cytoplasm"]
- Contrast with the paralogue, and the membrane motif boundaries:
  [PMID:10373560 "Furthermore, human Myt1 is localized to the endoplasmic reticulum and Golgi complex (40), whereas Wee1 localizes to the nucleus"];
  [PMID:10373560 "Membrane targeting requires 20 amino acid residues bordered by arginine 378 and histidine 399"]
- How the brake is released:
  [PMID:10373560 "We found that the mitotic form of Myt1 no longer interacts with Cdc2-cyclin B1 complexes"]
- Substrate restriction confirmed against Wee1:
  [PMID:10373560 "In contrast, Myt1 fails to recognize these complexes as substrates in vitro"]

**Caveat carried into the review:** the sequestration result was obtained on
*overproduced* Myt1. It is a real activity of the C terminus (kinase-inactive protein
still delays G2, and the RXL mutant does not), but its quantitative contribution at
endogenous levels is untested — hence a suggested experiment rather than a stronger claim.

### Secondary / contextual

- Schmidt et al. 2017 (doi:10.3390/molecules22122045), reviewed in the deep-research
  report: PKMYT1 vs WEE1 structural comparison (36.5% kinase-domain identity, 1.87 Å
  backbone RMSD), gatekeeper Thr178, and the division of labour whereby WEE1 is the
  nuclear Tyr15 kinase and PKMYT1 the membrane-associated Thr14 kinase.
- Oncology context (Gallo et al. 2022 doi:10.1038/s41586-022-04638-9; Wang et al. 2024
  doi:10.1038/s44321-024-00060-y; Xu et al. 2025 doi:10.1038/s41467-025-58183-w):
  CCNE1-amplification synthetic lethality and lunresertib/RP-6306. Relevant to the
  `description` as biology (why replication-stressed cells depend on PKMYT1), not used to
  justify any annotation.
- Deep research synthesis used for orientation:
  [file:human/PKMYT1/PKMYT1-deep-research-falcon.md "Human PKMYT1/Q99640 is a membrane-associated WEE-family kinase whose primary physiological role is inhibitory control of cyclin-B-bound CDK1."]

## 3. Annotation decisions and why

48 GOA rows. Actions: ACCEPT 15, REMOVE 14, MODIFY 11, KEEP_AS_NON_CORE 8.

### Molecular function

- **GO:0004674 protein serine/threonine kinase activity** (IDA, IEA, 2× Reactome TAS) —
  ACCEPT. This is the core activity; UniProt's threonine-kinase reaction (RHEA:46608) is
  the one carrying experimental evidence.
- **GO:0004672 protein kinase activity** (IBA, IEA, TAS) and **GO:0016301 kinase
  activity** (IDA) — MODIFY → GO:0004674. Pure granularity corrections; GO:0016301 does
  not even state that the substrate is a protein.
- **GO:0106310 protein serine kinase activity** (IEA, RHEA:17989) — MODIFY → GO:0004674.
  The term's own usage note restricts it to kinases that *specifically* phosphorylate
  serine and sends dual-specificity Ser/Thr enzymes to the Ser/Thr term. PKMYT1's
  characterised residue is Thr14; UniProt's serine reaction is an ECO:0000305 curator
  inference, and serine phosphorylation by PKMYT1 is reported as *auto*phosphorylation.
- **GO:0005524 ATP binding** (IEA) — ACCEPT; ATP site 116–124/139 plus Mg(2+) residues.
- **GO:0004713 protein tyrosine kinase activity deliberately NOT proposed.** The obvious
  temptation, given the protein's own RecName ("tyrosine- and threonine-specific") and
  the "dual-specificity" phrasing in PMID:9001210. But UniProt states the Tyr-15 activity
  "is unclear and may be indirect", GOA carries no such row, and the human data cannot
  separate direct PKMYT1 Tyr15 phosphorylation from WEE1 activity plus PKMYT1
  autophosphorylation. Raised as `suggested_questions[0]` and
  `suggested_experiments[0]` instead of asserted.

### The 13 bare `GO:0005515 protein binding` rows

Every partner is either **CDK1 (P06493)** or **cyclin B1 (P14635)** — i.e. the
physiological substrate complex. Policy (`annotation-reviewer` SKILL, "Quality
Standards"): MODIFY where the cited paper supports an informative MF, otherwise REMOVE as
uninformative, never asserting the interaction is false.

- The two rows anchored to PMID:10373560 (**the only mechanistic primary study**) → MODIFY, because that paper genuinely
  resolves the interaction:
  - P06493 → **GO:0019901 protein kinase binding** (co-IP + C-terminal deletion mapping;
    docking required for efficient Cdc2 phosphorylation).
  - P14635 → **GO:0030332 cyclin binding** (RXL motif R486/N487/L488 mapped by alanine
    substitution).
- The remaining 11 rows come from high-throughput surveys (PMID:23397142, PMID:23602568,
  PMID:25852190, PMID:26496610, PMID:28514442, PMID:32707033 ×2, PMID:33961781 ×2,
  PMID:35271311 ×2) → REMOVE as uninformative. The interactions themselves are the
  well-supported physiological ones; the informative molecular functions now live on the
  PMID:10373560 rows. PMID:32707033 is the only screen whose cached full text names
  PKMYT1: [PMID:32707033 "we could demonstrate that some of the poorly characterized kinases (NEK9 and PKMYT1) are required for cell shape control"].
- A protein-kinase-**inhibitor**-activity term (GO:0004860/GO:0030291) was considered for
  the CDK1 row and rejected: PKMYT1's inhibition of CDK1 is principally catalytic, and the
  binding-only component rests on overproduction experiments.

### Cellular component

- **ER membrane (GO:0005789)**, **Golgi membrane (GO:0000139)**, **ER (GO:0005783)**,
  **Golgi apparatus (GO:0005794)** — ACCEPT, all four. The parent/child pairs are
  simultaneously true of a peripheral membrane protein, and this mirrors how nucleus and
  nucleoplasm are both accepted on WEE1. The HPA `IDA` Golgi row (GO_REF:0000052) is an
  independent reproduction of the 1997 immunofluorescence; antibody imaging cannot resolve
  membrane from lumen, so the organelle-level term is right for that evidence.
- **membrane (GO:0016020)** ×3 (HDA, IEA, TAS) — KEEP_AS_NON_CORE. True and characteristic
  of PKMYT1, but the uninformative ancestor of the two specific membrane terms. The HDA row
  is from an NK-cell membrane-proteome survey that explicitly expected peripherally
  associated proteins: [PMID:19946888 "Isolated membranes were treated with reagents that have been reported to remove peripheral membrane proteins"].
- **cytoplasm (GO:0005737)** ×2 (IBA `is_active_in`, IEA) — KEEP_AS_NON_CORE. Correct in
  the broad sense (the catalytic and docking faces are cytosolic; the sequestered cyclin
  B1–CDK1 pool is cytoplasmic) but superseded by the membrane terms.
- **nucleus (GO:0005634)** ×2 and **nucleoplasm (GO:0005654)** — REMOVE, the most
  substantive negative calls in this review. Grounds:
  1. Endogenous Myt1 "remains membrane-bound throughout the cell cycle" (PMID:9268380).
  2. Nuclear accumulation is the phenotype of the **membrane-anchor deletion mutant**
     (PMID:9001210), not of the wild-type protein.
  3. UniProt records only ER membrane and Golgi apparatus membrane for Q99640.
  4. The functional contrast with WEE1 — "whereas Wee1 localizes to the nucleus"
     (PMID:10373560) — is the point of the gene.
  The IBA row is a `is_active_in nucleus` propagation from PTHR11042 node PTN000113601,
  whose characterised descendants include the nuclear WEE1-type kinases and the
  eIF2-alpha kinases; the argument recorded in `propagation_review` is about **node
  placement for the Myt1 sub-branch**, which acquired the C-terminal membrane anchor, not
  about donor count. The IEA row is an Ensembl Compara transfer from mouse Pkmyt1 with no
  human support. The nucleoplasm row is a Reactome compartment assignment on the
  "Inactivation of Myt1 kinase" reaction — the reaction is real, the compartment is not.
- **cytosol (GO:0005829)** ×2 (Reactome TAS) — MODIFY → GO:0005789 + GO:0000139. Cytosol
  denotes the aqueous compartment *excluding* membranes and organelles; PKMYT1 faces the
  cytosol but is attached to membranes.

### Biological process

- **GO:0010972 negative regulation of G2/M transition of mitotic cell cycle** (IBA + IDA)
  — ACCEPT; this is the central process claim, and both mechanistic arms feed it. Q99640
  appears in its own IBA `WITH/FROM` list, which is the expected marker of experimental
  grounding on the target, not circularity (`IBA_REVIEW` guidance).
- **GO:0000079 regulation of cyclin-dependent protein serine/threonine kinase activity**
  (TAS) — MODIFY → **GO:0045736** (negative regulation …). The direction is known and
  invariant.
- **GO:0007088 regulation of mitotic nuclear division** (TAS) — MODIFY → GO:0010972. The
  assays behind the reference are inhibitory Thr14/Tyr15 phosphorylation and a G2 delay;
  effects on nuclear division are downstream consequences of gating CDK1 activation.
- **GO:0000086 G2/M transition** (Reactome TAS) — ACCEPT (as on WEE1).
  **GO:0000278 mitotic cell cycle** (TAS) — KEEP_AS_NON_CORE (top-level parent).
- **GO:0051321 meiotic cell cycle** and **GO:0110031 negative regulation of G2/MI
  transition of meiotic cell cycle** (both IBA) — KEEP_AS_NON_CORE. Myt1 orthologues do
  hold oocytes in prophase arrest in Xenopus and mouse, and the mechanism is the same
  inhibitory phosphorylation, so the node placements are credible and the rows are kept.
  But there is no human oocyte experiment, and the roles are germline-restricted — so
  non-core rather than ACCEPT. Turned into `suggested_questions[2]`.

## 4. `NEW` annotations considered and declined

Per CLAUDE.md's "do not add what curators deliberately declined to add", nothing was added.
Candidates weighed:

- **GO:0004713 protein tyrosine kinase activity** — declined; see above. The comparator
  check is instructive: WEE1, the paralogue for which Tyr15 activity *is* established,
  carries GO:0004713 across many evidence codes, while PKMYT1 carries none in any species.
  That is a curation convention tracking a real evidential difference, not an oversight.
- **A protein-kinase-inhibitor MF for the sequestration arm** — declined; captured instead
  as the `cyclin binding` core function, where the evidence (RXL mapping) actually sits.
- **Anything about the CCNE1-amplification dependency** — declined. Synthetic lethality
  establishes that PKMYT1 is *necessary* in those cells, which is not participation in a
  process; the relevant GO content is already `negative regulation of G2/M transition`.

`proposed_new_terms: []` — no ontology gap identified.

## 5. Core functions

Two activity units, deliberately kept separate because they are separable by mutation:

1. **Catalytic**: GO:0004674 on cyclin-bound CDK1 (substrate UniProtKB:P06493), at
   GO:0005789 / GO:0000139, driving GO:0010972 and GO:0045736.
2. **Non-catalytic docking**: GO:0030332 cyclin binding via the RXL motif, at the same
   locations, contributing to GO:0010972. Kinase-dead Myt1 retains a partial G2 delay;
   the RXL mutant loses both binding and the delay.

All core-function term ids are either ACCEPTed rows or proposed replacement terms, so
nothing is asserted that the annotation review does not already sanction.

## 6. Validation

`just validate human PKMYT1` → ✓ Valid, 0 warnings.
`just validate-references` → all checks passed (every `supporting_text` verbatim).
`just validate-terms` → ✅ passed. Status set to `COMPLETE`.
