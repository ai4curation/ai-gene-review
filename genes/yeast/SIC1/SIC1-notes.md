# SIC1 (P38634) curation notes

## Identity

- *Saccharomyces cerevisiae* S288c, YLR079W, synonyms SDB25, "CDK inhibitor p40". 284 aa, ~32 kDa.
- Domain: SIC1_C (IPR062579 / PF29958), matching the experimentally mapped C-terminal kinase-inhibitory
  region (~residues 215-284). The N-terminal half (residues 1-89 in UniProt) is disordered and carries the
  CDK phosphosites (Thr5, Thr33, Ser76 annotated in UniProt; Thr2/Thr5/Thr33/Thr45/Ser69/Ser76/Ser80 studied
  by NMR). Thr173 is the Hog1 site, Ser201 the CK2 site.
- Not related in sequence to metazoan Cip/Kip (p27/p21) or *S. pombe* Rum1; functional analogue only.
  [PMID:20417603 "p27, a mammalian CDK2-cyclin E inhibitor, has similar functions with the yeast CDK inhibitor Sic1, such as a role in orchestrating the G1/S transition, although they do not share significant sequence similarity"]
- UniProt FUNCTION: "Substrate and inhibitor of the cyclin-dependent protein kinase CDC28"; interacts with
  HOG1; IntAct interactions with CDC14, CDC4, HOG1.

## Core biology

- Discovery: p40 was purified as a Cdc28 substrate that bound tightly to Cdc28 and inhibited it
  [PMID:8421781 "The p40 protein bound tightly to p34CDC28 and inhibited the activity of the kinase"].
- Cyclin specificity and cell-cycle role: [PMID:7954792 "cdc34 mutants cannot enter S phase because they fail to destroy p40SIC1, which is a potent inhibitor of Clb but not Cln forms of the Cdc28 kinase"];
  [PMID:7954792 "In wild-type cells, p40SIC1 protein appears at the end of mitosis and disappears shortly before S phase"];
  [PMID:7954792 "Proteolysis of a cyclin-specific inhibitor of Cdc28 is therefore an essential aspect of the G1 to S phase transition"].
  IGI partners on the GO:0000082 rows: CDC4 (S000001885), CDC53 (S000002290), CDC34 (S000002461),
  CLB5 (S000006324) — i.e. the SCF(Cdc4)-Cdc34 destruction machinery and the S-phase cyclin target.
- Degradation mechanism: Cln1/2-Cdc28 (plus Pho85-Pcl1) multisite phosphorylation of the N-terminus creates
  Cdc4 phosphodegrons; SCF(Cdc4) with Cdc34 ubiquitinates Sic1; proteasome degrades it.
  [PMID:19008353 "Phosphorylation by G 1 CDK activity (Cln1/2–Cdc28) targets Sic1 to the SCF Cdc4 ubiquitin ligase, resulting in Sic1 ubiquitination and degradation by the proteasome"]
  [PMID:19008353 "The disordered cyclin-dependent kinase (CDK) inhibitor Sic1 interacts with a single site on its receptor Cdc4 only upon phosphorylation of its multiple dispersed CDK sites."]
  [PMID:19008353 "we measured an apparent overall K d value of ≈0.6 μM between the pSic1 preparation and Skp1–Cdc4, whereas no binding was detected for Sic1"]
  [PMID:18787112 "Such phosphorylation enables Sic1-Cdc4 interaction required for ubiquitination of Sic1."]
  Ultrasensitivity: [PMID:19008353 "A requirement for multiple phosphorylation events in Sic1 in principle sets a high threshold for the level of active G 1 CDK required to initiate transition to S phase"].
- Transcription: Swi5-dependent SIC1 transcription in late M/early G1; SCF(Cdc4) degradation of Swi5
  terminates SIC1 transcription so Sic1 can be cleared at late G1
  [PMID:18787112 "Degradation of Sic1 is strictly required for S-phase entry ( 3 ), whereas that of Swi5 ensures efficient entry into S phase."].
- Mitotic exit / licensing (deep research, Philip et al. 2022 eLife, Venta et al. 2020):
  [file:yeast/SIC1/SIC1-deep-research-falcon.md "Newly synthesized Sic1 contributes to the decline of mitotic Clb–Cdk1 activity and helps establish the low-CDK state required for mitotic exit and the next G1 phase."]
  [file:yeast/SIC1/SIC1-deep-research-falcon.md "Sic1 releases **Clb2–Cdk1–Cks1 from Cdc6**, allowing Mcm2–7 loading onto chromatin after mitotic exit."]
- Localisation: nuclear (functional Sic1-GFP), degraded by nuclear Cdc4
  [PMID:11080155 "Consistent with this notion, a functional Sic1–GFP fusion protein was localized in the nucleus (Figure 8 E)."];
  both compartments [PMID:11792824 "A substrate of Cln2, Sic1, was also in both compartments."];
  bipartite NLS and carbon-source modulation, Clb5 accumulates in cytoplasm when SIC1 is shut off
  [PMID:16294029 "We identify a bipartite nuclear localization sequence responsible for nuclear localization of Sic1 and for correct cell cycle progression in a carbon-source dependent manner"].
- Stress control: Hog1 binds and phosphorylates Sic1 (Thr173) to stabilise it and arrest G1 under osmostress
  [PMID:15448699 "Hog1 interacts physically with Sic1 in vivo and in vitro, and phosphorylates a single residue at the carboxyl terminus of Sic1"];
  T173A impairs arrest (UniProt MUTAGEN).
- Cdc14 dephosphorylates Sic1 (in vitro substrate) [PMID:11274204 "five different substrates including the physiologic targets Swi5 and Sic1"];
  Cdc14-Sic1 also in AP-MS network [PMID:20489023 abstract only, no Sic1 text].
- Autophagy: [PMID:20417603 "Sic1 is a negative regulator of autophagy, based on the observations that overexpression of Sic1 or Sic1-Δ3P, a degradation-resistant mutant, significantly inhibited autophagy, and that loss of Sic1 dramatically upregulated autophagy"];
  Rim15 downstream [PMID:20417603 "deletion of RIM15 completely suppressed the upregulation of autophagy in sic1Δ cells"];
  mechanism open [PMID:20417603 "However, only a weak interaction was detected in co-immunoprecipitation experiments (data not shown)."];
  Pho85 cyclins Clg1/Pcl1/Pho80 destabilise Sic1 to promote autophagy.

## Curation decisions

| Term | Evidence | Action | Note |
|---|---|---|---|
| GO:0000082 G1/S transition (x4 IGI) | PMID:7954792 | ACCEPT | Sic1 is the CKI that gates the switch; it performs the inhibition (participation test met). GO:2000134 used in core_functions for direction. |
| GO:0004861 CKI activity (x2 IDA) | PMID:7954792, PMID:8421781 | ACCEPT | Core MF. |
| GO:0005515 with CDC14 (PMID:11274204, PMID:20489023) | IPI | REMOVE | Enzyme-substrate; uninformative bare term; interaction not disputed. |
| GO:0005515 with HOG1 | IPI | REMOVE | Kinase-substrate; uninformative; biology recorded here. |
| GO:0005515 with CDC4 (x3) | IPI | MODIFY -> GO:1905761 | Phosphodegron recognition by SCF substrate receptor; specific term already on gene. |
| GO:0005634 nucleus (3 IDA + IEA) | | ACCEPT | Site of core function. |
| GO:0005737 cytoplasm (IDA + IEA) | | ACCEPT | Real cytoplasmic pool, carbon-source modulated. |
| GO:0016242 neg. reg. macroautophagy | IMP | KEEP_AS_NON_CORE | Solid genetics, but secondary/lineage-specific, mechanism open. |
| GO:1905761 SCF binding (EXP + IDA) | PMID:19008353 | KEEP_AS_NON_CORE | Direct and correct, but substrate-side (how Sic1 is regulated); mirrors p27 GO:0031625 handling. |

Participation test applied: Sic1 does the inhibiting (activity), but for its own ubiquitination it is the
substrate, so no process term for its degradation is proposed and the SCF-binding MF is kept non-core.
Comparator: human CDKN1B carries GO:0031625 ubiquitin protein ligase binding (KEEP_AS_NON_CORE in that
review), and neither p27 nor Sic1 carries a ubiquitin-dependent catabolic process term as actor.

## Not annotated / open

- Cip/Kip-like escort of Clb5 into the nucleus (PMID:16294029) — single abstract-only report; raised in
  suggested_questions rather than as a NEW cyclin binding / adaptor annotation.
- Mitotic-exit role (GO:0010458) is used in core_functions on the strength of the deep-research
  summary of Philip 2022 / Venta 2020 and the Schwob 1994 timing data; not proposed as NEW because the
  primary papers are not in the publication cache.
- CK2 Ser201, TORC1/Mpk1 stabilisation, Cks1 docking at pThr173 — from deep research only; notes only.
