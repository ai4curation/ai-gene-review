# SCAP (Q12770) review notes

## Session log

- 2026-10-18: Started review. `just deep-research human SCAP --provider falcon` attempted once;
  it failed at login ("Exception: Failed to authenticate"; the Edison/Falcon key is not
  authorised). Not retried. No `-deep-research-*.md` file exists; these notes, UniProt and
  cached publications are the evidence base.
- Fetched extra publications: PMID:8898195, 17428919, 12963821, 16399501, 15260976,
  33446483, 32054686, 27068746. Most are abstract-only in the cache.

## Identity and architecture

- SCAP = SREBP cleavage-activating protein, 1279 aa, polytopic ER membrane protein with an
  N-terminal eight-TM membrane domain (containing the sterol-sensing domain, SSD, TM2-6) and a
  C-terminal cytosolic WD40 beta-propeller domain that binds the regulatory domain of SREBPs.
  UniProt: "Belongs to the WD repeat SCAP family." PANTHER PTHR46378 (SF1).
- Cloned by expression cloning from sterol-resistant CHO cells [PMID:8898195 "Through expression
  cloning we have isolated a cDNA-encoding SREBP cleavage-activating protein (SCAP), which
  regulates cholesterol metabolism by stimulating cleavage of transcription factors SREBP-1 and -2"];
  D443N in the SSD gives sterol resistance [PMID:8898195 "The D443N mutation enhances the
  cleavage-stimulating ability of SCAP and renders it resistant to inhibition by sterols"].
- Topology: [PMID:23564452 "Scap has eight transmembrane helices (TM) joined by four small
  hydrophilic loops and three large loops. Two of the large loops (Loops 1 and 7) are in the ER
  lumen, and the other large loop (Loop 6) faces the cytosol where it binds COPII proteins that
  initiate transport to Golgi."]

## Molecular function

1. **Cholesterol binding / sterol sensing** (the defining activity).
   - Direct binding by purified membrane domain (hamster Scap): [PMID:15260976 "cholesterol acts by
     binding with high affinity and specificity to the 767 amino acid octahelical membrane region of
     SCAP"].
   - Conformational change: [PMID:12963821 "the conformation of SCAP is altered in vitro by addition
     of cholesterol to ER membranes"]; Loop1 binds Loop7 in the transport-competent state and
     cholesterol disrupts this [PMID:27068746 "When ER cholesterol rises, it binds to Loop1. We
     hypothesized that this causes dissociation from Loop7, abrogating COPII binding."].
   - Human Scap-Insig-2 cryo-EM: 25HC sits at the Scap SSD / Insig-2 TM3-4 interface
     [PMID:33446483 "A 25HC molecule is sandwiched between the S4 to S6 segments in Scap and TMs 3 and 4
     in Insig-2 in the luminal leaflet of the membrane."]. Oxysterols bind INSIG, cholesterol binds
     SCAP [PMID:17428920 "Cholesterol acts by binding to the SREBP-escort protein Scap, thereby causing
     Scap to bind to anchor proteins called Insigs."].
   - GO: GOA carries only `sterol binding` (GO:0032934; IEA InterPro and ISS from hamster). The more
     specific `cholesterol binding` (GO:0015485, is_a sterol binding) and `sterol sensor activity`
     (GO:0032935: "Binding to and responding, e.g. by conformational change, to changes in the
     cellular level of a sterol") both fit SCAP better. Comparator: GO:0032935 is used for SLC38A9
     and OSBPL1A (cholesterol sensors) but not SCAP in any species - an obvious gap for the
     archetypal sterol sensor. Proposed NEW.
2. **Escort / ER-export cargo receptor for SREBPs.** SCAP binds SREBP via its WD40 domain and, in
   sterol-depleted cells, binds Sec23/Sec24 through the cytosolic MELADL hexapeptide in Loop 6.
   - [PMID:15899885 "Sec23/24 binding to Scap requires the hexapeptide sequence MELADL located in a
     cytoplasmic loop of Scap. This hexapeptide acts as a sterol-regulated ER sorting signal."]
   - [PMID:17428919 "preventing the binding of COPII-coated proteins to a hexapeptide sorting signal
     (MELADL) in Scap, the SREBP-escort protein"].
   - [PMID:12242332 "In sterol-depleted cells, SCAP escorts SREBPs to the Golgi where the SREBPs are
     processed by two membrane-bound proteases"].
   - GO has no "SREBP escort" term. `cargo receptor activity` (GO:0038024: "Cargo receptors span
     membranes ... binding simultaneously to cargo molecules and coat adaptors, to efficiently
     recruit the cargo molecules to nascent vesicles") describes exactly this. Comparator:
     carried by other ER-exit COPII cargo receptors (CNIH1/2 IBA, LMAN1, MIA3 IEA). Proposed NEW,
     flagged as a question for experts.
   - Avoid `protein binding` (three IPI rows: INSIG2, RNF139/TRC8, SPRING1) - REMOVE as uninformative.

## Localisation

- ER membrane at steady state (sterol-replete) and Golgi in sterol-depleted cells, with
  COPI-dependent return [PMID:32111832 "In control cells grown in sterol-containing media SCAP-eGFP
  was predominantly located in the ER and localization markedly shifted towards the Golgi upon
  sterol-depletion"]; [PMID:26311497 "Scap was mainly co-localized with an ER marker calnexin in
  normal medium"; PAQR3 anchors Scap/SREBP in Golgi]. COPII vesicle membrane (hamster IDA
  PMID:27068746 in GOA; human IEA).

## Complexes

- SREBP-SCAP complex (GO:0032936) and SREBP-SCAP-Insig complex (GO:0032937): [PMID:12202038 "Sterols
  induce binding of SCAP to INSIG-1, as determined by blue native-PAGE"]; [PMID:16399501
  "Endoplasmic reticulum (ER) bound SREBPs form complexes with Scap, a polytopic ER protein."].
- Membrane domain is a tetramer [PMID:15260976 "the membrane domain of SCAP is a tetramer"].

## Processes

- Core: SREBP signaling pathway (GO:0032933), COPII-coated vesicle cargo loading (GO:0090110),
  positive regulation of cholesterol biosynthetic process (GO:0045542).
- `cholesterol metabolic process` (GO:0008203) rows: SCAP does no metabolic chemistry; it
  regulates synthesis/uptake through SREBP. MODIFY to GO:0045542.
- `regulation of transcription by RNA polymerase II` (GO:0006357; ComplexPortal-derived): the
  transcriptional output belongs to the SREBP subunit; SCAP acts upstream in ER/Golgi. Marked
  over-annotated (not removed: experimental row, ComplexPortal complex-level inference).
- `negative regulation of cholesterol biosynthetic process` (NAS, a review on oxysterols):
  sterol-bound SCAP-INSIG is the feedback-inhibition switch, so it is defensible; non-core.
- `response to vitamin B3` (rat Ensembl IEA): expression-level response; not a function. REMOVE.

## Regulators / partners (context, not annotated as SCAP MF)

- INSIG1/2 (ER anchors), PAQR3 (Golgi anchor; [PMID:26311497 "PAQR3 interacts with Scap/SREBP and
  tethers them to the Golgi complex, resulting in enhanced SREBP processing"]), RNF139/TRC8
  [PMID:19706601 "This complex formation hampers the interaction between SCAP and Sec24"], SPRING1
  (Golgi factor needed for SCAP return to ER, PMID:32111832), RNF5 (PMID:32054686, ubiquitination),
  PCK1 phosphorylation of INSIG releases SCAP-SREBP (PMID:32322062), lycorine induces lysosomal
  SCAP degradation (PMID:32432943).

## GO-CAM

- The curated human GO-CAM `gocams/6205c24300000880` ("Regulation of cholesterol biosynthesis by
  SREBP ... and retention by the SREBP-SCAP complex") has no SCAP (Q12770) activity node; the
  SREBP-SCAP complex appears only as a generic GO:0032936 molecule acted on by INSIG1/2
  (`protein sequestering activity`, `SREBP-SCAP complex retention in endoplasmic reticulum`).
  SCAP's own sterol-sensor / escort activity is therefore not modelled. Raised in
  suggested_questions. GO:0036316 (retention) is carried by INSIG1/2 (anchors), not SCAP
  (the retained entity), so not proposed as NEW for SCAP.
