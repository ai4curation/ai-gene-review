# SLC52A3 (RFVT3) — gene review notes

## Identity and nomenclature (IMPORTANT — tangled naming)

- UniProt: Q9NQ40, `S52A3_HUMAN`, 469 aa, chromosome 20, gene `SLC52A3`
  (synonyms `C20orf54`, `RFT2`, `RFVT3`).
- UniProt RecName: "Solute carrier family 52, riboflavin transporter, member 3";
  AltName "Riboflavin transporter 2; Short=hRFT2"
  [file:human/SLC52A3/SLC52A3-uniprot.txt].
- **Local names used by different labs all refer to this same protein (SLC52A3 / RFVT3 / C20orf54):**
  - The **Said/Subramanian lab** (PMID:21854757, PMID:22273710) calls it **"hRFT-2"**.
    Their "hRFT-2" is the 469-aa C20orf54 product, apical, intestinal — i.e. SLC52A3.
  - The **Inui/Yao lab** (PMID:20463145) calls it **"hRFT3"** / "hRFT-3".
  - Later papers (PMID:24264046, PMID:27702554, PMID:29428966, PMID:30892938) use the
    standardized **RFVT3 / hRFVT-3 / SLC52A3**.
  - Beware: SLC52A2 is separately "RFVT2"/"hRFVT-2"/brain transporter — do not conflate.
- The modern consensus (Reactome R-HSA-3165230; UniProt) is: SLC52A1=RFVT1,
  SLC52A2=RFVT2, **SLC52A3=RFVT3**. GOA attributes all of the above papers' RFVT3/hRFT-2/hRFT3
  data to Q9NQ40.

## Core biology

- **Molecular function:** riboflavin (vitamin B2) transmembrane transporter; mediates
  cellular **uptake** of riboflavin. UniProt: "Plasma membrane transporter mediating the
  uptake by cells of the water soluble vitamin B2/riboflavin"
  [file:human/SLC52A3/SLC52A3-uniprot.txt]. Rhea reaction riboflavin(in) = riboflavin(out)
  (CHEBI:57986) [file:human/SLC52A3/SLC52A3-uniprot.txt "riboflavin(in) = riboflavin(out)"].
  KM ≈ 0.98 µM for riboflavin [file:human/SLC52A3/SLC52A3-uniprot.txt "KM=0.98 uM for riboflavin"].
- **Biological process:** riboflavin transport (GO:0032218); a key player in
  **intestinal (apical brush-border) riboflavin absorption** (GO:0050892).
  Na+-independent at low pH; inhibited by riboflavin analogs (lumiflavin, FMN, FAD),
  methylene blue, and (weakly) amiloride
  [file:human/SLC52A3/SLC52A3-uniprot.txt "ACTIVITY REGULATION"].
- **Location:** apical (brush-border) plasma membrane of polarized epithelia
  (GO:0016324); plasma/cell membrane (GO:0005886); multi-pass membrane protein
  (11 predicted TM helices; cryo-EM structure PDB 8XSN)
  [file:human/SLC52A3/SLC52A3-uniprot.txt "Apical cell membrane"].
- **Tissue specificity:** "Predominantly expressed in testis. Highly expressed in small
  intestine and prostate" [file:human/SLC52A3/SLC52A3-uniprot.txt]; HPA "Tissue enhanced
  (intestine, testis)".
- Humans cannot synthesize riboflavin and must acquire it via diet/intestinal absorption
  [file:human/SLC52A3/SLC52A3-uniprot.txt "must obtain it via intestinal absorption"].

## Disease

- **Biallelic (autosomal-recessive) loss-of-function mutations cause riboflavin
  transporter deficiency: Brown-Vialetto-Van Laere syndrome type 1 (BVVLS1; MIM 211530)
  and Fazio-Londe disease (FALOND; MIM 211500)** — infantile/childhood progressive
  bulbar palsy with sensorimotor (axonal) neuronopathy and sensorineural deafness;
  respiratory compromise is a leading cause of death. **Treatable with high-dose oral
  riboflavin** [file:human/SLC52A3/SLC52A3-uniprot.txt "DISEASE"; PMID:20206331;
  PMID:22273710; PMID:27702554].
- Original disease-gene discovery: mutations in C20orf54 cause BVVLS
  [PMID:20206331 "mutations in this gene were the cause of disease"].
- Many pathogenic missense variants act by mislocalization (ER retention → loss of
  cell-surface expression), some (e.g. W17R) by loss of transport activity with normal
  membrane targeting [PMID:22273710
  "significant (P < 0.01) inhibition in riboflavin uptake in Caco-2 cells expressing W17R";
  PMID:27702554 "drastic inhibition in RF uptake and impairment in membrane expression"].

## Evidence per functional claim (for annotation review)

- **Riboflavin transporter activity / transport (GO:0032217, GO:0032218):**
  - PMID:20463145 (Inui/Yao, "hRFT3"): cloned, [3H]riboflavin uptake in HEK293,
    KM ≈ 0.33 µM (UniProt records 0.98 µM for this entry), Na+/Cl−-independent,
    inhibited by riboflavin analogs. IDA.
  - PMID:24264046 (RFVT3/SLC52A3): apical [3H]riboflavin uptake in T84 cells,
    pH-dependent, inhibited by methylene blue, reduced by RFVT3-siRNA. IDA/IMP.
  - PMID:22273710 (Said, "hRFT-2"=SLC52A3): WT vs BVVLS mutants RF uptake in Caco-2. IDA.
  - PMID:30892938 (RFVT-3): TMEM237 overexpression/knockdown modulates RF uptake. IMP.
- **Apical plasma membrane (GO:0016324):**
  - PMID:24264046: apical membranes of intestinal epithelial cells (T84, mouse jejunum/ileum). IDA.
  - PMID:20463145: brush-border/apical localization + function. EXP.
  - NB PMID:21854757 (Said lab): their **"hRFT-2" (=SLC52A3)** is "exclusively expressed
    at the apical membrane" — this is the annotation basis. (In that same paper the
    protein they call "hRFT-3" is a *different* SLC52 member, intracellular/BLM.)
    [PMID:21854757 "hRFT-2 is exclusively expressed at the apical membrane";
    "predominant role for the hRFT-2 in intestinal RF absorption"]. IDA.
- **Plasma membrane (GO:0005886):** PMID:20463145, PMID:22273710 (IDA/EXP);
  PMID:29428966 isoform 1 (EXP); Reactome TAS.
- **Intestinal absorption (GO:0050892):** PMID:24264046 (IDA), PMID:21854757 (IMP),
  PMID:30892938 (IMP). Well supported as a core physiological role.
- **Cytoplasm (GO:0005737) / nuclear membrane (GO:0031965):** PMID:29428966 (cancer
  study). Isoform-specific: **isoform 2 (SLC52A3b) is cytoplasmic** and non-functional
  for transport; isoform 1 (SLC52A3a) is cell membrane + also reported nucleus membrane +
  cytoplasm. [file:human/SLC52A3/SLC52A3-uniprot.txt "SUBCELLULAR LOCATION: [Isoform 2]:
  Cytoplasm"; "Nucleus membrane {ECO:0000269|PubMed:29428966}"]. These are non-core
  (isoform-2 / cancer-context localizations), not the canonical transporter function.
- **Sensory perception of sound (GO:0007605), IMP, PMID:20206331:** derived from the
  deafness phenotype of BVVLS patients. This is a downstream disease phenotype of
  systemic riboflavin deficiency, not a molecular role of the protein in hearing;
  over-annotation (phenotype→process). Marked over-annotated (experimental → not removed).
- **riboflavin metabolic process (GO:0006771), TAS, Reactome R-HSA-196843:** SLC52A3
  *transports* riboflavin; it does not chemically metabolize it. The broad metabolic-process
  term is a generalization; kept as non-core (transport contributes to riboflavin
  homeostasis but the specific act is transport).
- **protein binding (GO:0005515), IPI x4:**
  - PMID:30892938: TMEM237 — a genuine, functionally validated interactor (colocalizes,
    co-IP, modulates RFVT3 stability and RF uptake). Informative, but "protein binding"
    is uninformatively generic → over-annotated (not removed; experimental IPI).
  - PMID:32814053: high-throughput Y2H neurodegeneration interactome (ATXN3, DNM2-2,
    TOR1A). Screen-scale, generic protein binding → over-annotated.

## Non-canonical / context roles (not core)

- **Cancer:** SLC52A3 (esp. isoform SLC52A3a) is over-expressed in esophageal squamous
  cell carcinoma and other tumors; NF-κB (p65/Rel-B) drives its transcription; prognostic
  biomarker; SLC52A3a promotes proliferation [PMID:29428966]. Context-specific, non-core.

## Curation summary

- Core MF: GO:0032217 (riboflavin transmembrane transporter activity).
- Core BP: GO:0032218 (riboflavin transport), GO:0050892 (intestinal absorption).
- Core location: GO:0005886 (plasma membrane), GO:0016324 (apical plasma membrane).
- No better/more-specific GO term exists for the BP (no "riboflavin transmembrane
  transport" term as of this review; QuickGO checked), so GO:0032218 is retained as-is.
</content>
