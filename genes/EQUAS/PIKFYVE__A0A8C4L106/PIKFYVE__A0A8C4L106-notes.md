# PIKFYVE (donkey, A0A8C4L106) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: closest characterised relative of the ProtNLM2 benchmark entry EQUAS/PIKFYVE (A0A9L0JQ61, the short
460-residue splice product, reviewed in genes/EQUAS/PIKFYVE). Same Ensembl gene ENSEASG00005003072; A0A8C4L106 is the
product of the Ensembl canonical transcript ENSEAST00005004444. Folder created with
`just fetch-gene EQUAS A0A8C4L106 --alias PIKFYVE__A0A8C4L106` (stub id A0A8C4L106 confirmed). ProtNLM2 output was not
opened or used.

Deep research: `just deep-research-falcon EQUAS PIKFYVE__A0A8C4L106 --fallback perplexity-lite` failed (falcon
"Failed to authenticate"; perplexity-lite 401 insufficient quota). No deep-research file exists. Literature was read
from the cached publications already in publications/ (the same mammalian PIKfyve papers used for the horse ortholog
review, genes/HORSE/PIKFYVE).

### Identity and evolutionary basis for transfer
- TrEMBL, PE 4 (predicted), 2108 aa; full-length gene model, not a fragment.
- UniProt PANTHER xref PTHR46715:SF1, the single PIKfyve subfamily, shared with human Q9Y2I7, mouse Q9Z1T6 and horse
  A0A3Q2HE51. This subfamily membership, not similarity, is the basis for transfer.
- Donkey is not a PAINT reference proteome: there are no IBA rows. The combined IEA rows (GO_REF:0000120) cite
  PANTHER:PTN001347166 (a TreeGrafter placement in the family) and the human ortholog ENSP00000264380 (Q9Y2I7-1).
  For which terms PAINT chose to propagate, the horse ortholog's IBA rows (node PTN002928511/PTN002928512) were used as
  the reference: PtdIns3P 5-kinase, PtdIns 5-kinase, PtdIns(3,5)P2 metabolic process, phagocytic vesicle membrane,
  phagosome-lysosome fusion, melanosome organization, neutrophil chemotaxis and ROS regulation. PAINT did not propagate
  PI4P 5-kinase or protein serine kinase activity.
- Own sequence comparison (PIKFYVE__A0A8C4L106-bioinformatics/RESULTS.md, compare_orthologs.py): 92.94% identity to
  human over 2095 paired residues (99.86% of human covered), 91.36% to mouse, 99.72% to horse; all eight FYVE Zn-ligand
  Cys conserved (offset +10); human catalytic K1877 (K1877E kinase-dead, PMID:33098764) = donkey K1887; human S2053
  activation-loop autophosphorylation site = donkey S2063.

### What is experimental where
- Donkey: nothing. Every function below is inferred.
- Mouse: PtdIns3P and PtdIns 5-kinase activity [PMID:10419465 "displays a strong in vitro activity for PtdIns 5-P and
  PtdIns 3,5-P(2) generation"]; FYVE-dependent late endosome targeting [PMID:11706043 "PIKfyve localization to
  membranes of the late endocytic pathway was found to be absolutely dependent on the presence of an intact FYVE
  finger."]; ternary complex with VAC14 and FIG4 [PMID:17556371]; melanosome biogenesis (melanocyte knockout,
  PMID:29584722).
- Human: reconstituted PIKfyve-VAC14-FIG4 structure/biochemistry, autophosphorylation [PMID:33098764 "PIKfyve
  autophosphorylation represses its lipid kinase activity and stimulates Fig4 lipid phosphatase activity."]; MHC-II
  (PMID:30612035), STING (PMID:41639454), EGFR nuclear transit (PMID:17909029), coronavirus entry (PMID:32221306), all
  inhibitor/knockdown necessity evidence.

### Decisions (36 rows, all IEA)
- ACCEPT: PtdIns3P 5-kinase, PtdIns 5-kinase, early and late endosome membrane, PAS complex.
- MODIFY: kinase/transferase/PI kinase/nucleotide binding/metal ion binding (-> zinc ion binding)/ser-thr kinase
  (-> protein serine kinase); endosome membrane, vesicle membrane, cytoplasmic vesicle -> early/late endosome
  membrane; PI metabolic and PI(3,5)P2 metabolic -> GO:1903102 / GO:1904563.
- KEEP_AS_NON_CORE: PAINT-placed cell-type processes (neutrophil chemotaxis, ROS regulation, melanosome organization,
  phagosome-lysosome fusion, phagocytic vesicle membrane), Ensembl projections (MHC-II, phagosome maturation,
  retrograde endosome-to-Golgi transport, STING, autophagosome assembly, membrane raft), ATP binding, cytosol,
  protein serine kinase.
- MARK_AS_OVER_ANNOTATED: Golgi membrane, intracellular protein localization, PI4P 5-kinase (not propagated by PAINT;
  treated as deliberate), virus endocytosis (host requirement), protein localization to nucleus, DEP -> intracellular
  signal transduction.
- No NEW terms.

### Follow-up
Human PIKFYVE (Q9Y2I7, PTHR46715:SF1) is the characterised ortholog and source of the experimental data; it has no
review in the repo (no genes/human/PIKFYVE). Reviewing it would put the donor-side evidence on a firmer footing.
