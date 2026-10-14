# FLCN (donkey, A0A8C4MM62) notes

DONKEY40 cohort review. Evidence base: donkey UniProt TrEMBL record (unreviewed, PE 3), the donkey GOA file
(12 IEA rows, no experimental rows), the human Swiss-Prot ortholog Q8NFG4 and mouse Q8QZS3 records fetched
into `FLCN-bioinformatics/`, a donkey-human pairwise alignment (`FLCN-bioinformatics/RESULTS.md`), and the
cached full text of PMID:34381247. No deep-research provider call was made.

## Sequence

- Donkey A0A8C4MM62 (578 aa) aligns to human Q8NFG4 (579 aa) at 94.64% identity over 578 paired residues,
  covering 99.83% of human and 100% of donkey [file:EQUAS/FLCN/FLCN-bioinformatics/RESULTS.md "The donkey
  sequence A0A8C4MM62 (578 residues) aligns to human Q8NFG4 (579 residues) with 94.64% identity across 578
  paired residues."]. Differences cluster in the disordered N-terminal segment (donkey 31-82).
- The GAP catalytic arginine is conserved [file:EQUAS/FLCN/FLCN-bioinformatics/RESULTS.md "SITE (Essential
  for GTPase activation (GAP) activity): human [164] R -> donkey [164] R."].
- Domain architecture: full-length uDENN FLCN/SMCR8-type domain (86-557), longin and DENN Pfam domains;
  PANTHER PTHR31441:SF2 FOLLICULIN [file:EQUAS/FLCN/FLCN-uniprot.txt "PANTHER; PTHR31441:SF2; FOLLICULIN; 1."].

## Function (from human/mouse experimental evidence, transferred)

- GAP for RagC/RagD, activating mTORC1 toward TFEB/TFE3 [file:EQUAS/FLCN/FLCN-bioinformatics/human_Q8NFG4-uniprot.txt
  "Activates mTORC1 by acting as a GTPase-activating protein: specifically stimulates GTP hydrolysis by
  RagC/RRAGC or RagD/RRAGD"].
- Non-canonical mTORC1 substrate selectivity: controls TFEB/TFE3, not S6K1/4E-BP1 [human UniProt "Acts as a key
  component for non-canonical mTORC1-dependent control of the MiT/TFE factors TFEB and TFE3"].
- In low amino acids the lysosomal folliculin complex (LFC) forms and FLCN GAP activity is inhibited; this
  maximizes TFEB/TFE3 nuclear translocation, so FLCN effects on transcription are indirect [human UniProt "In
  low-amino acid conditions, the lysosomal folliculin complex (LFC) is formed on the membrane of lysosomes"].
- Complex: FLCN-FNIP1/2 heterodimer (GO:1990877 FNIP-folliculin RagC/D GAP, human IDA) [human UniProt
  "GO:1990877; C:FNIP-folliculin RagC/D GAP; IDA:UniProtKB."].
- Additional roles: LDHA uncompetitive inhibition [PMID:34381247 "we identify the human tumor suppressor
  folliculin (FLCN) as a binding partner and uncompetitive inhibitor of LDHA"]; autophagy via GABARAP;
  lysosome positioning via RILP/RAB34; primary cilia/LKB1.
- Localization: lysosome membrane (starvation) and cytosol (fed); also cilia, centrosome, mitotic spindle,
  nucleus [human UniProt "Also localizes to motile and non-motile cilia, centrosomes and the mitotic spindle"].
- Mouse knockout: embryonic lethal at 5.5-6.5 dpc [file:EQUAS/FLCN/FLCN-bioinformatics/mouse_Q8QZS3-uniprot.txt
  "Embryonic lethality at 5.5-6.5 dpc"]. Mouse IMP annotations to positive regulation of TGF-beta receptor
  signaling and cell-cell junction assembly exist (DR lines) but the papers are not cached.

## Annotation decisions (summary)

- ACCEPT: GTPase activator activity, positive regulation of TORC1 signaling (TreeGrafter), lysosomal membrane,
  cytosol, positive regulation of TOR signaling (ARBA; broader parent, still accurate).
- KEEP_AS_NON_CORE: nucleus, centrosome, spindle, cilium; negative regulation of transcription by RNA pol II
  (indirect, via TFE3/TFEB cytoplasmic retention); positive regulation of TGF-beta receptor signaling
  (TreeGrafter; indirect, mouse IMP).
- MARK_AS_OVER_ANNOTATED: negative regulation of signal transduction (ARBA; vague, FLCN's main signalling role
  is positive regulation of TORC1).
- NEW: FNIP-folliculin RagC/D GAP complex (GO:1990877).

## ProtNLM2 GO predictions

- GO:0007179 TGF-beta receptor signaling pathway: UNC (regulator, not shown to be a pathway component).
- GO:0004857 enzyme inhibitor activity: COR (LDHA inhibition, human IDA; not in donkey GOA).
- GO:0001934 positive regulation of protein phosphorylation: UNC (indirect/generic).
- GO:0001701 in utero embryonic development: COR (mouse knockout lethality; not in donkey GOA).
- GO:0007043 cell-cell junction assembly: UNC (mouse IMP exists, but primary evidence not available here).
