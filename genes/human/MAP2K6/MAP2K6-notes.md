# MAP2K6 (MKK6, MEK6, SKK3; UniProt P52564) curation notes

## Sources used
- UniProt P52564 (`MAP2K6-uniprot.txt`)
- Falcon deep research (`MAP2K6-deep-research-falcon.md`, completed during this review and used as a source)
- Cached GOA publications in `publications/` (most are abstract-only; full text available for PMID:10848581, 17255949, 19141286, 29021624, 32296183, 32707033, 32911434, 35857590)
- Reactome entries in `reactome/`
- Paralog review `genes/human/MAP2K3/MAP2K3-ai-review.yaml` for consistent term choices

## Identity and family
- STE-group dual-specificity kinase, MAP2K subfamily [file:human/MAP2K6/MAP2K6-uniprot.txt "protein kinase family. MAP kinase kinase subfamily."]
- Cloned in 1996 as a close MKK3 relative that selectively phosphorylates p38 [PMID:8621675 "MKK6, like MKK3, selectively phosphorylates p38"]; 79% identical to MKK3 [PMID:8663074 "79% identical to MKK3"].
- Two splice isoforms (334 aa MKK6b = canonical; 278 aa) with distinct tissue expression [PMID:8621675 "MKK6 exists in a variety of alternatively spliced isoforms with distinct patterns of tissue expression"].
- Domains: N-terminal D domain (KIM, residues 4-19) docks MAPK substrates; C-terminal DVD domain (311-334) docks MAP3Ks [file:human/MAP2K6/MAP2K6-uniprot.txt "(MAP3Ks) and are essential for activation."].

## Molecular function
- MAP kinase kinase activity: dual phosphorylation of Thr and Tyr in the TGY motif of all four p38 isoforms [file:human/MAP2K6/MAP2K6-uniprot.txt "and a tyrosine residue in the MAP kinases p38 MAPK11, MAPK12, MAPK13"]; Reactome: "All are activated by phosphorylation on a canonical TxY motif by the dual-specificity kinase MKK6, which displays minimal substrate selectivity amongst the p38 isoforms" [Reactome:R-HSA-1247960].
- p38beta preferentially activated by MKK6 [PMID:8663524 "the preferred activation of p38beta by MAP kinase kinase 6 (MKK6)"]; SAPK4/p38delta activated by SKK3/MKK6 [PMID:9218798 "SAPK4 was activated in vitro by SKK3 (also called MKK6)"]; p38gamma in DNA-damage G2 checkpoint [PMID:10848581].
- Selective: does not act on ERK or JNK [Reactome:R-HSA-450346 "both phosphorylate and activate p38 MAP kinase at its activation site Thr-Gly-Tyr but do not phosphorylate or activate Erk1/2 or SAPK/JNK"].
- Mechanism: 2019 kinetics show random, partially processive dual phosphorylation favouring Tyr182; 2023 cryo-EM of MKK6-p38alpha shows face-to-face complex via KIM + alphaG/C-lobe interface [file:human/MAP2K6/MAP2K6-deep-research-falcon.md "Initial phosphorylation was **random but favored Tyr182**"].
- Non-p38 substrates reported: PIP4K2B Ser326 under oxidative stress [Reactome:R-HSA-8877691 "MAP2K6 (MKK6), and possibly other kinases of the p38 MAPK family, phosphorylates PIP4K2B at serine residue S326"]; PAK6 [file:human/MAP2K6/MAP2K6-uniprot.txt "phosphorylates and activates PAK6."]. These justify keeping a (non-core) Ser/Thr kinase activity, unlike MAP2K3.
- Dimer: MEK6 kinase domain forms an autoinhibitory dimer, also seen for full-length unphosphorylated WT in solution [PMID:19141286 "The structure reveals an autoinhibited elongated ellipsoidal dimer."].

## Activation / upstream
- Activated by phosphorylation of Ser207/Thr211 [file:human/MAP2K6/MAP2K6-uniprot.txt "Activated by dual phosphorylation on Ser-207 and"], by many MAP3Ks: ASK1 (Reactome:R-HSA-3228469), TAK1 [PMID:8663074 "demonstrated to be phosphorylated and activated in vitro by TAK1"; PMID:11460167 "the activity of TAK1 to phosphorylate MKK6, which activates the JNK-p38 kinase pathway, is directly regulated by K63-linked polyubiquitination"], TAO2 [PMID:11279118 "endogenous TAO2 specifically associates with MEK3 and MEK6"], PKR in response to dsRNA [PMID:15229216 "MKK6 was efficiently phosphorylated by PKR"], LRRK2 [PMID:20067578 "LRRK2 is able to phosphorylate MKK3, 6 and 7"], ZAKalpha in ribotoxic stress.
- Inactivated by anthrax lethal factor cleavage (Reactome:R-HSA-5211405) and Yersinia YopJ acetylation of S207/T211 (UniProt PTM).

## Localization
- Nucleus and cytoplasm [PMID:9768359 "The p38 activators MKK3 and MKK6 were present in both the nucleus and the cytoplasm, consistent with a role in activating p38 in the nucleus."]; UniProt also notes microtubule binding (cytoskeleton). HPA IDA: cytosol, nucleoplasm.

## Biological processes
- Core: p38MAPK cascade (GO:0038066), the MAP2K tier; stress-activated MAPK cascade.
- Downstream/contextual (non-core): gamma-irradiation G2 checkpoint via MKK6-p38gamma [PMID:10848581 "Activation of the MKK6-p38γ cascade is sufficient to induce G 2 arrest in cells"]; senescence (Reactome); NOD1/2 signalling via TAK1 (Reactome:R-HSA-727819); mouse Mkk6 KO increases WAT browning/UCP1 [PMID:29021624 "Lack of MKK6 increases the basal expression of UCP1 and promotes T3-mediated induction of UCP1 expression in WAT."]; bone/osteoblast (mouse IEA; UniProt function text mentions endochondral ossification).
- Reactome "Regulation of TP53 activity through acetylation" membership is indirect (via PIP4K2B phosphorylation → PI5P/ING2) and is treated as over-annotation.

## Protein-binding (GO:0005515) rows - decisions (consistent with MAP2K3 review)
- MAPK14 partner (PMID:11035004, 17255949, 32707033) → MODIFY to GO:0051019 mitogen-activated protein kinase binding (substrate docking via D domain).
- EIF2AK2/PKR (PMID:15229216) and LRRK2 (PMID:20067578) → MODIFY to GO:0019901 protein kinase binding (kinases that phosphorylate MKK6 but are not canonical MAP3Ks; MAP2K3 review used GO:0019901 for LRRK2).
- PICK1 (HuRI Y2H), WFS1 (neurodegeneration Y2H), NFE2L2 (weak DULIP binder) → REMOVE (uninformative; removal does not imply interaction is false).
- Identical protein binding (PMID:19141286) → MODIFY to GO:0042803 protein homodimerization activity.

## Deep research status
- The falcon deep research file (`MAP2K6-deep-research-falcon.md`) became available during the review and was used as a supporting source.
