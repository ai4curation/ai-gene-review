# CHEK1 (Chk1, O14757) — curation notes

## Identity and architecture
Human CHEK1 encodes checkpoint kinase 1, a 476-aa serine/threonine-protein kinase (EC 2.7.11.1)
of the CAMK group with an N-terminal catalytic domain (~res 1–265) and a C-terminal autoinhibitory
regulatory region (AIR). The isolated kinase domain is ~20-fold more active than full-length CHK1,
consistent with C-terminal autoinhibition [CHEK1-deep-research-falcon.md, chen2000; UniProt DOMAIN
"The autoinhibitory region (AIR) inhibits the activity of the kinase domain"]. Not to be confused
with CHEK2/Chk2 or the unrelated Csk-homologous tyrosine kinase (MATK/"CHK").

## Core function
Principal effector kinase of the ATR-dependent DNA replication-stress and DNA-damage checkpoints.
Activated by ATR phosphorylation at Ser317/Ser345 (with CLSPN/Claspin as mediator, and BRCA1, FEM1B
as modulators), followed by Ser296 autophosphorylation
[PMID:9278511 "Human Chk1 protein was modified in response to DNA damage"; PMID:20639859 "Ser296
phosphorylation is catalysed by Chk1 itself after Chk1 phosphorylation by ATR"; PMID:19330022
"attenuates the induction of CHK1 Ser345 phosphorylation upon replication interference"].

Restrains CDK activity to enforce checkpoints:
- Phosphorylates CDC25A (promoting its degradation and inhibiting CDK2/CDK1) and CDC25C on Ser216
  (creating a 14-3-3 docking site) [PMID:9278511 "Chk1 bound to and phosphorylated the dual-specificity
  protein phosphatases Cdc25A, Cdc25B, and Cdc25C ... Chk1 phosphorylates Cdc25C on serine-216";
  PMID:14559997 "Chk1 phosphorylation targets Cdc25A for destruction"].
- Regulates WEE1 stability indirectly: CHK1 phosphorylates PABIR1/FAM122A (Ser37) → releases PP2A-B55α
  → dephosphorylates and stabilizes WEE1, sustaining inhibitory CDK phosphorylation and the G2/M
  checkpoint [PMID:33108758 "CHK1 directly phosphorylated FAM122A on a highly conserved site, Ser37";
  "CHK1 is known to directly phosphorylate WEE1 thereby activating a G2/M checkpoint"].
- Nuclear CHK1 activity is essential to establish the G2/M checkpoint [PMID:20932473 "nuclear Chk1
  activity is essential to establish a G(2)/M checkpoint"].

## Additional direct substrates / roles
- RAD51 Thr309 — promotes homologous recombination repair [PMID:15665856 "RAD51 is phosphorylated
  on Thr 309 in a Chk1-dependent manner"; "Chk1 is a key regulator of genome maintenance by the
  homologous recombination repair (HRR) system"]. Also regulates BRCA2–RAD51 associations
  [PMID:18317453].
- p53 — phosphorylates N- and C-terminal sites (e.g. S20, S366/T387) [PMID:10673501 "recombinant hCHK1
  ... can phosphorylate p53 in vitro at S20"; PMID:15659650 "six additional CHK1 and CHK2 sites
  residing in the final 100 amino acids of p53"]. MDMX Ser367 → 14-3-3γ binding → p53 activation
  [PMID:16511572 "Chk1 phosphorylated MDMX at serine 367"].
- TLK1 Ser695 — DNA-damage checkpoint control of chromatin assembly [PMID:12660173 "Chk1 phosphorylates
  Tlk1 on serine 695 (S695) in vitro"].
- FANCE Thr346/Ser374 — Fanconi anemia/BRCA cross-link repair [PMID:17296736 "Chk1 directly
  phosphorylates the FANCE subunit ... on two conserved sites (threonine 346 and serine 374)"].
- Aurora B Ser331 — required for full Aurora B activation and spindle-checkpoint fidelity
  [PMID:22024163 "phosphorylation at Ser331 is an essential mechanism for Aurora B activation";
  "Chk1 in vitro kinase assay"].
- NEK6 [PMID:18728393 "Nek6 is also directly phosphorylated by the checkpoint kinases Chk1 and Chk2
  in vitro"], NEK11 S273 [Reactome R-HSA-9943662], RB1 Ser612 [PMID:17380128 "phosphorylation of pRB
  at Ser612 was conducted by Chk1/2 after DNA damage"], E2F6 S12 (replication-stress transcription)
  [Reactome R-HSA-9007539], Mig-6/ERRFI1 Ser251 (EGF signalling) [PMID:22505024 "S251 and S302 ...
  were phosphorylated by Chk1 in vitro"], Smurf1 (RhoB abundance/apoptosis) [PMID:25249323
  "phosphorylation of Smurf1"], SPRTN (recruitment to chromatin) and a SPRTN–CHK1 cross-activation
  loop [PMID:31316063 "SPRTN cleaves, evicts and activates CHK1 from replicative chromatin"],
  histone H3 Thr11 [PMID:18243098 "Chk1 is a histone H3 threonine 11 kinase"].

## Localization
Predominantly nuclear; shuttles to cytoplasm (CRM1/XPO1-dependent export) and associates with
chromatin and replication forks; localizes to interphase centrosomes where it shields centrosomal
CDK1 from premature activation by CDC25B [PMID:15311285 "human Chk1 kinase localizes to interphase,
but not mitotic, centrosomes ... centrosome-associated Chk1 shields centrosomal Cdk1 from unscheduled
activation by cytoplasmic Cdc25B"; PMID:12676962 "Chk1 is associated with chromatin in cycling
cells"]. Present along meiotic chromosomes in spermatocytes [PMID:9382850].

## Regulation / turnover
Hsp90/Cdc37 client (destabilized by Hsp90 inhibition) [PMID:16330544 "Chk1 ... is destabilized when
heat shock protein 90 (Hsp90) is inhibited, suggesting that Chk1 is an Hsp90 client"; PMID:22939624].
Activated CHK1 is degraded by SCF(Fbx6/FBXO6) to terminate the checkpoint [PMID:19716789 "an
Fbx6-containing SCF ... mediates the ubiquitination and degradation of Chk1 and, in turn, terminates
the checkpoint"]. Basal turnover controlled by hHR23A/RAD23A [PMID:26296656 "hHR23A associates with
Chk1 through its UBA domains"]. AKT phosphorylates Ser280 to promote cytoplasmic sequestration
[PMID:15710331]. Essential gene: loss causes peri-implantation lethality [Reactome R-HSA-176116].

## Curation decisions of note
- GO:0005829 cytosol TAS from Reactome R-HSA-205328 → REMOVE: that pathway ("Interaction of other
  tyrosine kinases with p-KIT") explicitly concerns "CHK1 (Csk homologous kinase or MATK)", a
  cytoplasmic *tyrosine* kinase, NOT CHEK1/Chk1 checkpoint kinase — a gene-name collision.
- GO:0005576 extracellular region HDA from PMID:23580065 → REMOVE: high-throughput shotgun proteomics
  of glaucoma tears; a nuclear checkpoint kinase is not an extracellular protein (biofluid detection,
  not a site of function).
- Generic GO:0005515 protein binding IPI rows: substrate/regulator interactions resolved to REMOVE
  (uninformative; not asserting the interaction is false), except Hsp90 rows → MODIFY to GO:0051879
  Hsp90 protein binding, and 14-3-3 (YWHAB/YWHAG) rows → MODIFY to GO:0071889 14-3-3 protein binding
  (both are genuine, functionally distinct, literature-supported interactions).
- GO:0006260 DNA replication TAS → MODIFY to GO:0006275 regulation of DNA replication: CHK1 regulates
  origin firing / fork progression but does not perform replication.
- GO:0045787 positive regulation of cell cycle (PMID:26296656) → MARK_AS_OVER_ANNOTATED: CHK1 is a
  checkpoint/negative regulator; the paper concerns hHR23A control of Chk1 turnover.
- GO:0071260 cellular response to mechanical stimulus (IEP, PMID:19593445) → MARK_AS_OVER_ANNOTATED:
  weak IEP; the BAD/prostate-cancer paper does not establish a mechanical-stimulus role for CHK1.
