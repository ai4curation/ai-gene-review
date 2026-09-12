# LHY (LATE ELONGATED HYPOCOTYL) — Arabidopsis thaliana — Research Notes

UniProt: Q6R0H1 | Locus: AT1G01060 | 645 aa | single MYB (SANT/SHAQKYF-type) DNA-binding domain.

## Summary of gene function

LHY is a single-MYB (MYB-related, SHAQKYF-class) transcription factor that, together with
its paralog CCA1, forms the morning-expressed arm of the Arabidopsis circadian oscillator.
LHY mRNA and protein peak ~1 h after dawn; the protein binds the Evening Element (EE,
AAATATCT) and related/CCA1-binding-site motifs in target promoters and acts predominantly
as a transcriptional repressor of evening-phased clock genes (notably TOC1/APRR1), of
TCP21/CHE, and of CCA1 and LHY itself (autorepression), thereby generating the negative
feedback loops at the core of the clock.

### MYB DNA-binding transcription factor

- UniProt: "AltName: Full=MYB-related transcription factor LHY"; DOMAIN 19..73 "HTH myb-type";
  DNA_BIND 46..69 "H-T-H motif". InterPro IPR006447 (plant Myb domain), IPR001005 (SANT/Myb),
  PROSITE PS51294 HTH_MYB. So LHY is a bona fide sequence-specific DNA-binding TF.
- [PMID:9657154 "LHY was shown to encode a MYB DNA-binding protein."]
- [PMID:19286557 "CCA1 and LHY are DNA binding proteins that repress TOC1 expression through direct binding to its promoter region"]

### Core clock / circadian function

- [PMID:9657154 "The dominant late elongated hypocotyl (lhy) mutation of Arabidopsis disrupted circadian clock regulation of gene expression and leaf movements and caused flowering to occur independently of photoperiod."]
- [PMID:9657154 "suggesting that LHY was part of a feedback circuit that regulated its own expression"] — autorepression.
- [PMID:12007421 "We have obtained plants lacking CCA1 and with LHY function strongly reduced, cca1-1 lhy-R, and show that these plants are unable to maintain sustained oscillations in both constant light and constant darkness."]
- [PMID:19218364 "CIRCADIAN CLOCK ASSOCIATED1 (CCA1) and LATE ELONGATED HYPOCOTYL (LHY) are Myb-related proteins that function in or close to the central oscillator in Arabidopsis"]
- UniProt FUNCTION: "Binds to the promoter region of APRR1/TOC1 and TCP21/CHE to repress their transcription. Represses both CCA1 and itself."

### DNA binding / cis-regulatory region binding (direct, experimental)

- [PMID:19286557 "electrophoretic mobility shift assays indicate that CCA1 and LHY specifically bind to the CCA1-binding site in CHE promoter"] — basis for IDA GO:0003700 and GO:0000976 on CHE/CCA1 promoter.
- [PMID:19286557 "CHE is a clock component partially redundant with LHY in the repression of CCA1"] and "LHY inhibits CCA1 expression (17) probably through direct binding to a CCA1-binding site (18) (AGATTTTT) located 479 nucleotides upstream of the TCP-binding site."
- [PMID:19218364 "LHY and CCA1 bind to the same region of the promoter of a Light-harvesting chlorophyll a/b protein (Lhcb, also known as CAB)"] — DNA binding demonstrated; this paper is the EXP support for nuclear localization.
- [PMID:21471455 "this circadian regulation is caused by the direct action of CCA1 and LHY binding at the CBF1-3 locus—presumably at the EE, CBS, and related motifs"] — ChIP-supported promoter binding at CBF locus.

### Subcellular location: nucleus

- [PMID:19218364 "they also colocalize in the nucleus and heterodimerize in vitro and in vivo"] — EXP nuclear localization (GOA EXP from this paper).
- UniProt SUBCELLULAR LOCATION: Nucleus (ECO:0000269|PubMed:19218364 and PROSITE ProRule for Myb).

### Homo/heterodimerization (subunit)

- [PMID:19218364 "CCA1 and LHY can form homodimers, and they also colocalize in the nucleus and heterodimerize in vitro and in vivo"]; "CCA1 and LHY are present in the same large complex in plants" (>400 kD by gel filtration).
- Note: this is "protein binding"-type interaction info; informative biology but the bare GO:0005515 term is discouraged as a *core function*. No GO:0005515 annotation is present in the GOA anyway.

### Response to cold / CBF pathway (output process)

- [PMID:21471455 "the cca1-11/lhy-21 double mutation resulted in impaired freezing tolerance in both nonacclimated and cold-acclimated plants"]
- [PMID:21471455 "CCA1/LHY-mediated output from the circadian clock contributes to plant cold tolerance through regulation of the CBF cold-response pathway"]
- This is a clock-OUTPUT role (LHY regulates the CBF cold-response regulon), i.e. a downstream/non-core developmental-physiological process rather than the central oscillator function. GOA term GO:0009409 "response to cold" (IGI, acts_upstream_of_or_within).

### Flowering / photoperiodism (output process)

- [PMID:9657154 "caused flowering to occur independently of photoperiod"] — original mutant phenotype.
- [PMID:19011118 "the circadian clock proteins LATE ELONGATED HYPOCOTYL (LHY) and CIRCADIAN CLOCK-ASSOCIATED1 (CCA1) not only repressed the floral transition under short-day and long-day conditions but also accelerated flowering when the plants were grown under continuous light (LL)"] — basis for GO:0048574 "long-day photoperiodism, flowering" IGI (with SVP, AT2G46830).
- Flowering control is an output of the clock, not the central oscillator mechanism → non-core.

### Negative regulation of circadian rhythm / ELF4 repression

- [PMID:21499259 "the circadian-controlled CCA1 and LHY proteins directly suppress ELF4 expression periodically at dawn through physical interactions with these transcription-promoting factors"] — basis for GO:0042754 "negative regulation of circadian rhythm" IMP. LHY represses an oscillator component (ELF4); consistent with its repressor role.

### Annotations from network/Y1H papers (cis-regulatory region binding, IPI)

- PMID:30356219 (nitrogen TRN, abstract-only here): LHY appears as a TF binding a target promoter (WITH/FROM AT1G72330) in an enhanced yeast-one-hybrid network. GOA IPI GO:0000976. Supports DNA/cis-region binding capacity; the *nitrogen* process is not annotated as a process term for LHY.
- PMID:31806676 (PXY vascular TRN, full text here): large eY1H network of 690 TF-promoter interactions; LHY recovered binding a target promoter (WITH/FROM AT1G16530/LBD4). GOA IPI GO:0000976. [PMID:31806676 "we generated a transcriptional regulatory network (TRN) ... comprises 690 transcription factor-promoter interactions"]. Supports generic cis-region binding; no vascular process term annotated for LHY and this is a high-throughput Y1H screen.

## GO term definitions (verified knowledge)

- GO:0003700 DNA-binding transcription factor activity — sequence-specific TF that modulates transcription. Correct & core for LHY.
- GO:0000976 transcription cis-regulatory region binding — binding to a cis-regulatory region of DNA. Correct (EE/CCA1-binding-site promoter binding).
- GO:0003677 DNA binding — generic parent; IEA from InterPro Myb domain. True but less informative than the two terms above.
- GO:0005634 nucleus — correct, experimentally supported.
- GO:0042752 regulation of circadian rhythm; GO:0042754 negative regulation of circadian rhythm — core process terms; LHY is a central-oscillator repressor.
- GO:0007623 circadian rhythm — generic process; clock component, acceptable as parent.
- GO:0006355 regulation of DNA-templated transcription — generic; TAS from genome-wide TF survey (PMID:11118137), parent of more specific repressor activity.
- GO:0010468 regulation of gene expression — generic ARBA/IEA parent of transcription regulation.
- GO:0009409 response to cold; GO:0048574 long-day photoperiodism, flowering — clock-output physiological/developmental processes (non-core).

## Curation reasoning highlights

- LHY's *core* identity: sequence-specific MYB DNA-binding transcriptional repressor acting in the central circadian oscillator (autorepression + repression of TOC1/CHE/CCA1/ELF4). → ACCEPT for GO:0003700, GO:0000976 (IDA), GO:0042752, GO:0042754, GO:0005634(EXP).
- Generic parents (GO:0003677 DNA binding IEA, GO:0010468 regulation of gene expression IEA, GO:0006355 TAS, GO:0007623 circadian rhythm) are true but less informative → KEEP_AS_NON_CORE.
- Output/downstream processes (cold response, flowering photoperiodism) → KEEP_AS_NON_CORE.
- Redundant ISS DNA-binding-TF annotations (PMID:9657154, PMID:11118137) are superseded by the IDA from PMID:19286557 but still correct → KEEP_AS_NON_CORE (do not remove correct experimental/ISS support).
- No "protein binding" (GO:0005515) annotation present; nothing to demote.
- No annotation warrants REMOVE: even the high-throughput Y1H IPI terms (PMID:30356219, PMID:31806676) report a genuine, correct molecular capacity (cis-region binding) for a real DNA-binding TF; per project rules, do not REMOVE experimental annotations. They are kept (one IDA core; the two IPI as non-core given HT context).
