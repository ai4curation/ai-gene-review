# Map2k4 (mouse, P47809) - manual literature synthesis

No deep-research API was available in this session; this synthesis was written by hand from the
cached publications in `publications/` and the UniProt record. Provenance is inline.

## Identity

- Mouse Map2k4 (MKK4, SEK1, JNKK1, MEK4), UniProt P47809 (Swiss-Prot, 397 aa), MGI:1346869.
- STE-group protein kinase, MAP kinase kinase subfamily
  [file:mouse/Map2k4/Map2k4-uniprot.txt "Belongs to the protein kinase superfamily. STE Ser/Thr protein kinase family. MAP kinase kinase subfamily."].
- Kinase domain 100-366; N-terminal D domain (35-50) docks MAPK substrates; C-terminal DVD domain (362-385)
  docks upstream MAP3Ks; activation-loop Ser255/Thr259 phosphorylated by MAP3Ks (UniProt record).

## Molecular function

- Dual-specificity MAP2K that phosphorylates the Thr-Pro-Tyr activation motif of JNK1-3, preferring the
  tyrosine, and also activates p38 MAPKs
  [file:mouse/Map2k4/Map2k4-uniprot.txt "MAP2K4 shows preference for phosphorylation of the Tyr residue and MAP2K7/MKK7 for the Thr residue."].
- Founding biochemistry (human orthologs): [PMID:7716521 "A dual-specificity kinase that activates JNK, named JNKK, was identified that functions between MEKK and JNK."];
  [PMID:7839144 "Two human MAP kinase kinases (MKK3 and MKK4) were cloned that phosphorylate and activate p38 MAP kinase."].
  MKK4 does not activate ERK [PMID:7839144 "These MKK isoforms did not activate the ERK subgroup of MAP kinases, but MKK4 did activate JNK."].
- In rat heart, MKK4 immunoprecipitated kinase activity (GST-JNK/c-Jun coupled assay) is activated by
  osmotic shock but not by ischaemia, and MKK4 is not the p38 activator in ischaemic heart
  [PMID:20550965 "rule out a role for MKK4 in the activation of p38 during cardiac ischaemia"]. This shows the
  p38-directed activity is stimulus dependent.
- MKK4 and MKK7 are non-redundant JNK activators [PMID:9891090 "Genetic studies demonstrate that MKK4 and MKK7 serve nonredundant functions as activators of JNK in vivo."].

## Upstream activators and scaffolds

- Upstream MAP3Ks: MEKK1, ASK1, TAK1, MLKs, DLK, LZK, TPL2 (UniProt ACTIVITY REGULATION; Reactome R-MMU-209329,
  R-NUL-3299417, R-NUL-451681).
- TAK1 binds MKK4; PP2Cepsilon attenuates TAK1-MKK4 binding and IL-1-induced MKK4-JNK signalling
  [PMID:12556533 "Co-immunoprecipitation experiments indicated that PP2Cepsilon associates stably with TAK1 and attenuates the binding of TAK1 to MKK4 or MKK6."].
- MEKK1 binds MKK4 through MEKK1 kinase subdomain VIII [PMID:14500727 "Once activated, MEKK1 phosphorylates the MAP2K MKK4, which in turn phosphorylates JNK."].
- JSAP1/JIP3 (Mapk8ip3) scaffold binds activated SEK1 (mouse SEK1 cloned from brain) and MEKK1; JSAP1 enhances
  MEKK1-SEK1-JNK3 activation [PMID:10523642 "only the activated form of SEK1 associated with JSAP1 in cotransfected COS-7 cells"].

## Cellular location

- Cytoplasm and nucleus (UniProt, ECO:0000269 PubMed:9891090). Rat neurons: cytoplasm, dendrites and axons
  (see rat review, PMID:9714150).

## Physiology (mouse genetics)

- Neural deletion: severe brain developmental defects; decreased JNK activity
  [PMID:17875933 "Decreased JNK activity in the absence of MKK4 correlated with impaired phosphorylation of a subset of physiologically relevant JNK substrates and with altered gene expression."].
- Cardiomyocyte deletion: exacerbated pathological hypertrophy, normal physiological growth
  [PMID:19265040 "upregulated NFAT (nuclear factor of activated T-cell) transcriptional activity associated with exacerbated cardiac hypertrophy and the appearance of apoptotic cardiomyocytes were observed in MKK4(cko) mice"].
  NOTE: the UniProt DISRUPTION PHENOTYPE line states that cardiac deletion "prevents pathological cardiac
  hypertrophy", which is the opposite of what its cited paper (PMID:19265040) reports.
- Neonatal facial motoneurons lacking MKK4 or DLK are resistant to axotomy-induced death
  [PMID:25100604 "the facial motoneurons in those mutant mice are completely resistant to axotomy-induced death"].
  MKK4 thus promotes, not inhibits, motoneuron death.
- VSMC (mouse aortic cells): MKK4 overexpression sensitizes to H2O2-induced apoptosis
  [PMID:24705900 "overexpression of MKK4 significantly increased the number of TUNEL(+) VSMC compared to GFP control"].
- C2C12 myotubes: DN MKK4 blocks neuregulin-induced JNK activation and AChR epsilon promoter activity
  [PMID:10493750 "Blockade of JNK activation by overexpressing dominant-negative MKK4 inhibited epsilon-promoter activation."].
- Zebrafish map2k4 morphants are ventralized; Axin/JNK dorsalization pathway [PMID:17681137 "JNK-MO and MKK4-MO can ventralize embryos"].

## Questionable source annotations

- PMID:10521398 (erbB2 rescue) never mentions MKK4; the MGI with/from allele MGI:1929071 is Erbb2<tm1Cbm>
  (checked at informatics.jax.org). The Map2k4 NMJ development IMP appears to be on the wrong gene.
- PMID:8702681 (ARIA/AChR induction) abstract discusses Raf/MEK/ERK only; full text not available.
