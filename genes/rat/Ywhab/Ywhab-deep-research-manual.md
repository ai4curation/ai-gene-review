# Ywhab (rat 14-3-3 protein beta/alpha, P35213): manual literature synthesis

No deep-research API was available for this session; this summary was compiled manually
from the UniProt record and cached publications in `publications/`. Every claim carries
inline provenance.

## Identity and family

- Rat Ywhab (RGD:61998, GeneID 56011) encodes the 246-aa 14-3-3 protein beta/alpha, a
  member of the 14-3-3 family [file:rat/Ywhab/Ywhab-uniprot.txt "Belongs to the 14-3-3 family"].
  Two isoforms arise by alternative initiation (Long, Short) and the alpha form is the
  phosphorylated variant of beta [file:rat/Ywhab/Ywhab-uniprot.txt "The alpha, brain-specific form differs from the beta form in being
  phosphorylated"].
- Domain architecture: single 14-3-3 domain (Pfam PF00244, SMART SM00101, InterPro
  IPR023410); residues 58 and 129 annotated as phosphoserine-contacting sites (by similarity).

## Molecular function

- Canonical 14-3-3 activity: dimeric phosphoserine/phosphothreonine-motif reader
  [file:rat/Ywhab/Ywhab-uniprot.txt "Binds to a large number of partners, usually by recognition of a phosphoserine or
  phosphothreonine motif"]. Homodimers and heterodimers with SFN, YWHAG, YWHAQ (by similarity).
- Direct rat 14-3-3 beta binding to a phosphoserine client: GST-HCV core bound rat 14-3-3 beta
  directly, and the interaction depends on core Ser-53 [PMID:10644344 "14-3-3 protein bound to HCV core protein in a phosphoserine-dependent manner"].
- Inhibition of a client kinase: 14-3-3 beta binds TESK1 dependent on phospho-Ser-439
  and inhibits it [PMID:11555644 "Binding of 14-3-3beta inhibited the kinase activity of TESK1"].
- Sequestration of a kinase in rat brain: [PMID:12786973 "Apoptosis signal-regulating kinase 1 was sequestered in a complex that contained the molecular chaperone 14-3-3beta and protein phosphatase 5"];
  seizures trigger dissociation and ASK1 substrate phosphorylation.
- AANAT: PKA-phosphorylated AANAT forms a 14-3-3 complex that shields it and lowers its
  Km for serotonin [PMID:11427721 "Formation of this AANAT/14-3-3 complex enhances
  melatonin production"].
- AS160/TBC1D4 in rat adipocytes: beta binds phospho-AS160 but less well than gamma
  [PMID:21454690 "Both 14-3-3β and 14-3-3γ precipitated AS160, but the γ isoform was much more effective and precipitated higher amounts"];
  14-3-3 beta mRNA is the most abundant isoform in rat adipocytes but protein levels of gamma
  are higher [PMID:21454690 "14-3-3β was found to be the most abundant isoform"]. The
  insulin-enriched isoform on GLUT4 vesicles is gamma, not beta.

## Nuclear/transcriptional roles

- FBI1 (fourteen-three-three beta interactant 1) was found as a 14-3-3 beta partner in rat
  hepatoma K2 cells; the complex represses MKP-1 [PMID:18460465 "the FBI1-14-3-3beta complex could act as a transcriptional silencer"]
  and both proteins are on the MKP-1 promoter by ChIP.
- Human orthology sources: 14-3-3 retains HDAC4/5 in the cytoplasm
  [PMID:10869435 "The association of 14-3-3 with HDAC4 and HDAC5 results in the sequestration of these proteins in the cytoplasm."];
  UniProt (by similarity) notes blocking nuclear translocation of AKT1-phosphorylated SRPK2.

## Localization

- Cytoplasm/cytosol (UniProt, by similarity); nucleus (ChIP on MKP-1 promoter, PMID:18460465).
- Melanosome rests on organelle proteomics of the human protein (UniProt, by similarity).
- The human "vacuolar membrane" EXP annotation derives from recruitment of 14-3-3 beta to the
  Chlamydia trachomatis inclusion membrane via IncG [PMID:11260479 "14-3-3beta interacts with Chlamydia trachomatis inclusions"],
  a pathogen-specific context.

## Annotation-relevant caveats

- Human "protein phosphatase inhibitor activity" (PMID:17255105) rests on 14-3-3 binding
  shielding phospho-PDE3B from phosphatase action, i.e. substrate protection, not phosphatase
  inhibition [PMID:17255105 "the PKA-phosphorylated, 14-3-3 protein-bound, form
  of HSPDE3B is protected from phosphatase-dependent dephosphorylation and
  inactivation"].
- Human "positive regulation of transcription by RNA polymerase II" (PMID:10869435) is an
  indirect consequence of HDAC4/5 cytoplasmic sequestration.
