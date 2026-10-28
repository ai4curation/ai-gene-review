# hutH (PA5098, Q9HU85) notes

## Identity

- UniProt Q9HU85 (HUTH_PSEAE), 509 aa, Swiss-Prot reviewed, PE 3. The functional
  annotation is from HAMAP MF_00229
  [file:PSEAE/hutH/hutH-uniprot.txt "Reaction=L-histidine = trans-urocanate + NH4(+)"].
- PAL/histidase (aromatic amino acid ammonia-lyase) family, PANTHER PTHR10362, TIGR01225
  hutH, PROSITE PS00488 (PAL_HISTIDASE active-site signature).
- The MIO cofactor-forming Ala-Ser-Gly is at 142-144 (UniProt CROSSLNK 142..144; MOD_RES
  Ser143 2,3-didehydroalanine).
- In the PAO1 hut cluster, between the histidine transporter HutTh (PA5097) and the
  urocanate transporter HutTu (PA5099) [PMID:41641996 "aeruginosa strains possess transporters specific for both histidine (HutTh, PA5097) and urocanate (HutTu, PA5099)"].

## Paralog PA5093 (Q9HU90)

- The PAO1 hut locus also encodes a second HutH-like protein, PA5093 (Q9HU90, unreviewed,
  "Probable histidine/phenylalanine ammonia-lyase"). It is the counterpart of the
  P. fluorescens SBW25 HutH1, which lacks the active-site residues and is not a
  functional histidase
  [PMID:17717196 "Analysis of the deduced amino acid sequences of hutH 1 and hutH 2 showed that HutH 1 lacks the conserved Ala–Ser–Gly active site residues"];
  [PMID:17717196 "deletion of hutH 1 had no effect; however, deletion of hutH 2 resulted in a strain unable to grow on histidine."].
- My check (file:PSEAE/hutH/hutH-bioinformatics/RESULTS.md) found that PA5098 has
  Ala-Ser-Gly at 142-144 and is 82% identical to the structurally characterised P. putida
  HutH (P21310). PA5093 has no ASG tripeptide and is about 40% identical to either
  histidase. So PA5098 is the PAO1 histidase (the HutH2 type), and PA5093 is the
  MIO-less HutH1 type.
- PANTHER places PA5093 and PA5098 as a PAO1-specific duplication (PTN002233699) under
  PTN000796665. PA5093 therefore inherits IBAs for histidine ammonia-lyase activity and
  L-histidine catabolic process (UniProt Q9HU90 DR GO lines show both as IBA:GO_Central),
  almost certainly wrongly. This is a candidate for a NOT annotation at the PA5093 leaf
  (PTN002233700).

## Biology (literature)

- Histidase eliminates ammonia from L-histidine to give trans-urocanate, step I of the hut
  pathway. The MIO electrophile is formed autocatalytically from Ala-Ser-Gly
  [PMID:10220322 "the reactive electrophile is a 4-methylidene-imidazole-5-one, which is formed autocatalytically by cyclization and dehydration of residues 142-144 with the sequence Ala-Ser-Gly"].
- P. aeruginosa histidase is induced by urocanate and subject to catabolite and nitrogen
  control [PMID:4290562 "The results imply that urocanate is the physiological inducer of the histidine-degrading enzymes in P. aeruginosa."];
  [PMID:4990767 "Urocanate but not histidine was able to induce formation of histidine-degrading enzymes in a histidine ammonia-lyase-deficient mutant of Pseudomonas aeruginosa."].
- The first three steps of the pathway are catalysed by HutH, HutU and HutI
  [PMID:16475788 "The first three steps for the degradation of histidine include the action of HutH, HutU, and HutI to convert L-histidine to N-formimino-L-glutamate."].

## PMID:4290562 (Lessie & Neidhardt 1967), the PseudoCAP seed reference

- Abstract only. The scanned PMC276695 full text could not be retrieved: the MCP returned
  empty and the PDF is behind a browser challenge.
- The paper measures histidase directly. It partially purifies the P. aeruginosa enzyme,
  estimates its molecular weight and Km, and describes sigmoid kinetics
  [PMID:4290562 "The molecular weight of partially purified histidase was estimated at 210,000 by sucrose gradient centrifugation."];
  [PMID:4290562 "Its K(m) for histidine was 2 x 10(-3)m in tris(hydroxymethyl)aminomethane chloride buffer."].
  210 kDa matches a homotetramer of the 53.8 kDa PA5098 subunit (about 215 kDa); HAL is
  tetrameric (PMID:10220322).
- The paper predates genes, so the link from this activity to PA5098 is an inference.
  The inference is secure: PA5098 is the only MIO-containing PAL/histidase-family protein
  in PAO1, and PA5093 lacks the motif. The activity claim is therefore sound. The
  evidence is a direct assay of the wild-type enzyme, so IDA would fit better than
  IMP. The mutants in the paper are urocanase-deficient and regulatory mutants,
  not hutH mutants.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN000796617 | GO:0016841 ammonia-lyase activity | 9 | 269 (42 taxa) | GO:0004397 histidine ammonia-lyase activity, IMP, PMID:4290562 (PseudoCAP) | SOUND | Histidase activity of the P. aeruginosa enzyme was directly assayed (partially purified; Km, MW). The generic ammonia-lyase term at the MIO-lyase superfamily root is appropriate. The other 8 seeds (plant PAL, mammalian HAL) support it independently. The evidence code should be IDA, not IMP; that does not affect the IBD. |
| PTN000796665 | GO:0004397 histidine ammonia-lyase activity | 1 (sole seed) | 21 (16 taxa) | GO:0004397 histidine ammonia-lyase activity, IMP, PMID:4290562 (PseudoCAP) | SOUND | The seed is sound for PA5098 (direct assay; PA5098 is the only MIO-motif HAL in PAO1). The node term suits a bacterial histidase clade. One problem: the node includes PA5093, a PAO1 in-paralog that lacks the Ala-Ser-Gly MIO motif (the HutH1 type, shown non-functional in P. fluorescens SBW25), so PA5093's IBA is an over-propagation. PAINT should add a NOT at PTN002233700. |
| PTN000796665 | GO:0006548 L-histidine catabolic process | 1 (sole seed) | 21 (16 taxa) | GO:0006548 L-histidine catabolic process, IMP, PMID:4290562 (PseudoCAP) | SOUND | Histidase catalyses step I of histidine degradation, and the paper treats it as the first enzyme of the inducible pathway. Genetic confirmation of HutH-type genes is in SBW25 (PMID:17717196). The same PA5093 caveat applies. |

## Decisions summary

- ACCEPT: histidine ammonia-lyase activity (IBA, IEA, IMP), L-histidine catabolic process
  (IBA, IEA, IMP), cytoplasm (IEA).
- MODIFY to GO:0004397: catalytic activity (IEA), ammonia-lyase activity (IEA).
- Source defects: PSEUDOCAP WRONG_EVIDENCE_CODE (IMP should be IDA; CHECK, PROBABLE) on the
  MF IMP row. GO_CENTRAL MISSING_NEGATION for PA5093 at PTN002233700 (PROBABLE), recorded
  on the IBA MF row because PA5093 has no review in this repository.
