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

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

This pass ignored all ProtNLM2 material. Deep research was attempted
(`just deep-research-falcon EQUAS FLCN --fallback perplexity-lite`) and failed: Edison/falcon returned
"Failed to authenticate" and the perplexity-lite fallback also failed. Literature used instead: newly cached
full texts of PMID:24095279 (Tsun 2013), PMID:31704029 (Shen 2019), PMID:31672913 (Lawrence 2019) and
PMID:32612235 (Napolitano 2020), plus the previously cached PMID:34381247.

### Identity

- A0A8C4MM62 is the full-length donkey folliculin, not a fragment, isoform or alternative gene model: 578 aa
  vs 579 aa for human Q8NFG4, 94.64% identity, no unpaired segments of 5 or more residues
  [file:EQUAS/FLCN/FLCN-bioinformatics/RESULTS.md "Human segments not paired with donkey (>=5 residues)"].
  The single-residue length difference is a 1-aa gap in the disordered 294-337 region (alignment.txt).
- uDENN, cDENN and dDENN regions are all present; Arg-164 (catalytic arginine finger) is conserved
  [PMID:31704029 "Biochemical analyses reveal a conserved arginine on FLCN as the catalytic arginine finger"].
- The human LDHA-binding region (210-220; UniProt ECO:0000269 PubMed:34381247) is identical in donkey. This
  answers the earlier suggested question, which wrongly placed the relevant loop in the divergent N-terminal
  disordered segment (31-82).

### Evolutionary grounding

- Donkey, human, mouse, rat, bovine, Xenopus, S. pombe Bhd1 and S. cerevisiae Lst7 all sit in
  PTHR31441:SF2 FOLLICULIN (`interpro/panther/PTHR31441/PTHR31441-entries.csv`); there is only one subfamily
  in PTHR31441 and no FamilyReview yet, so there is no subfamily-placement disagreement.
- TreeGrafter rows come from PANTHER node PTN009120754: GTPase activator activity, positive regulation of
  TORC1 signaling, cytosol, negative regulation of transcription by RNA pol II, positive regulation of
  TGF-beta receptor signaling. The node does not carry enzyme inhibitor activity (LDHA) or the
  cilium/centrosome/spindle locations; I treat those omissions as deliberate and add no NEW rows for them.

### Changes relative to the previous review

- GO:0032008 positive regulation of TOR signaling: ACCEPT -> MODIFY to GO:1904263 (correct but general; the
  child term is already annotated and FLCN acts on mTORC1).
- GO:0030511 positive regulation of TGF-beta receptor signaling: KEEP_AS_NON_CORE -> UNDECIDED. The only
  support was the mouse record's own DR GO line, which restates the annotation. The primary mouse IMP paper
  is not cached and I did not identify its PMID with confidence.
- Replaced DR-GO-line quotes, which only restate annotations, with quotes from primary papers (GAP, TORC1,
  lysosomal membrane, cytosol, complex) or curated UniProt subcellular-location text (nucleus).
- Added the four new primary references with findings and reference_review. Kept every existing reference.
- Unchanged: ACCEPT for GTPase activator activity, lysosomal membrane, cytosol and positive regulation of
  TORC1 signaling; KEEP_AS_NON_CORE for nucleus, centrosome, spindle, cilium and negative regulation of
  transcription by RNA pol II (indirect, via TFEB/TFE3 retention); MARK_AS_OVER_ANNOTATED for negative
  regulation of signal transduction; NEW for GO:1990877 FNIP-folliculin RagC/D GAP.

### Relative

- The closest experimentally characterised relative is human FLCN (Q8NFG4), in the same PANTHER subfamily
  (SF2) and the main experimental donor for the PTN009120754 node. No review of it exists in the repo
  (no genes/human/FLCN, and Q8NFG4 does not appear as an id in any review), so it needs review.
- Modules: none in `modules/` covers FLCN. The only hit is a deep-research artifact
  (`modules/nodal_signaling-deep-research-falcon_artifacts/artifact-02.md`), not a module.
