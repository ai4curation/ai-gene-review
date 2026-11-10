# Map2k4 (rat) - manual literature synthesis

No deep-research API was available for this session. This file is a manual synthesis written
from the cached publications in `publications/` and the curated human ortholog record
(`genes/human/MAP2K4/MAP2K4-uniprot.txt`, P45985). Every statement carries its source.

## Identity

- Rat Map2k4 (RGD:1307040, GeneID 287398), UniProtKB A0ABK0L269 (unreviewed TrEMBL, 435 aa,
  Ensembl ENSRNOP00000102620). Synonyms: MKK4, SEK1, JNKK1, MEK4, XMEK2.
- The rat entry carries a single Protein kinase domain (residues 138-403; PROSITE PS50011),
  an ATP-binding site at Lys167 and a proton-acceptor Asp265 (PROSITE-ProRule PRU10027), and
  PANTHER subfamily PTHR48013:SF15 "DUAL SPECIFICITY MITOGEN-ACTIVATED PROTEIN KINASE KINASE 4"
  [file:rat/Map2k4/Map2k4-uniprot.txt]. Compared with human P45985 (399 aa) the rat model has
  a Gly-rich N-terminal extension; the D-site-like basic motif (KRKALKLNF) and the activation
  loop Ser/Thr pair (DSIAKT) are both present in the rat sequence (own inspection of the SQ block).

## Molecular function

- Human MKK4 (JNKK) is a dual-specificity kinase that activates JNKs and p38 but not ERK
  [PMID:7716521 "A dual-specificity kinase that activates JNK, named JNKK, was identified that
  functions between MEKK and JNK."; "JNKK also activated another MAPK, p38"]
  [PMID:7839144 "Two human MAP kinase kinases (MKK3 and MKK4) were cloned that phosphorylate and
  activate p38 MAP kinase."].
- In rat 3Y1 fibroblasts exposed to hyperosmolar media, a SAPK-alpha-activating activity was
  identified as MKK4, and activated MKK4 also phosphorylated p38 [PMID:7768885 "The adsorbed
  activity was identified as XMEK2/SEK1/MKK4 by using several anti-XMEK2 antibodies."; "whereas
  the activated XMEK2/SEK1/MKK4 could phosphorylate p38/MPK2 efficiently"]. Abstract only.
- Human UniProt (curated): MKK4 prefers the Tyr of the JNK Thr-Pro-Tyr motif, MKK7 the Thr;
  MKK4 docks substrates through its N-terminal D domain and MAP3Ks via the C-terminal DVD domain
  [file:human/MAP2K4/MAP2K4-uniprot.txt].

## Pathway context in rat systems

- Hyperosmotic stress: sorbitol perfusion of the isolated rat heart robustly activates MKK4 (and
  the other MKKs); in contrast, global ischaemia activates p38 via MKK3/MKK6 but not MKK4, and
  does not activate JNK [PMID:20550965 "In control experiments in which hearts were perfused with
  sorbitol, we saw robust activation of all MKK isoforms assayed"; "A lack of MKK4 activation
  indicates, at least in the ischaemic heart, that MKK4 is not a physiologically relevant
  activator of p38."]. Full text read. This argues that MKK4's contribution to p38 is
  stimulus-dependent and minor relative to MKK3/6.
- Global cerebral ischaemia/reperfusion in rat hippocampus activates MLK3-MKK4/7-JNK1/2,
  suppressed by estrogen via Akt1 [PMID:17064355]. Abstract only.
- Neuronal apoptosis: POSH scaffolds Rac1-MLK-MKK4/7-JNK; dominant-negative MKK4/7 suppresses
  POSH-induced death of neuronal cells [PMID:12514131 "POSH overexpression promotes apoptotic
  neuronal death and this is suppressed by dominant-negative forms of MLKs, MKK4/7 and c-Jun"].
  Full text read.
- TGF-beta1-induced apoptosis in FaO rat hepatoma cells is suppressed by DN SEK1 [PMID:12029621].
  Abstract only.
- Hepatocyte DNA synthesis in response to hyperosmotic glucose, TNF-alpha and HGF requires a
  Ras/Rac1/Cdc42/SEK/JNK/c-Jun pathway (DN SEK1 blocks it) [PMID:9487126]. Full text read; the
  readout is downstream proliferation, not regulation of the DNA replication machinery.
- Endothelin-1-induced cardiomyocyte hypertrophy requires SEK-1 (DN SEK-1(KR) blocks SAPK
  activation and protein synthesis) [PMID:9769323]. Abstract only.
- Neuronal localization: MEK4 is ubiquitous in adult rat CNS neurons, in cytoplasm, dendrites,
  axons and cell bodies [PMID:9714150 "All four kinases were present in the cytoplasm, dendrites,
  and axons of neurons."]. Abstract only.

## Mouse sources behind the RGD ISO rows

- PMID:25100604 (mouse; abstract only): MKK4-deficient neonatal mice have doubled facial
  motoneuron numbers and their motoneurons are completely resistant to axotomy-induced death -
  MKK4 promotes motoneuron death. The mouse/rat annotation "negative regulation of motor neuron
  apoptotic process" therefore looks sign-inverted.
- PMID:10521398 (mouse; full text cached): about ErbB2 mutants and Schwann cells; MKK4 is not
  mentioned, and the MGI with/from allele (MGI:1929071) is an Erbb2 allele. The mouse Map2k4
  "neuromuscular junction development" IMP, and the rat ISO copied from it, appear to be on the
  wrong gene.
- PMID:10493750 (mouse C2C12; abstract): DN MKK4 blocks neuregulin-induced JNK activation and
  AChR epsilon promoter activation (basis for MAPK cascade/ERBB signaling context).
- PMID:24705900 (mouse VSMC): MKK4-JNK1 mediates H2O2-induced VSMC apoptosis.
- PMID:8702681 (mouse C2C12; abstract): ARIA-induced AChR expression requires the ERK pathway
  (DN "MAP kinase kinase", i.e. MEK); MKK4 is not mentioned in the abstract.
