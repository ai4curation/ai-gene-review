# Curation Notes: Human `AKAP13` (`UniProtKB:Q12802`, `HGNC:371`)

## 1. Gene Identity, Isoform Architecture & Family Context
- **HGNC symbol / ID**: `AKAP13` (*A-kinase anchoring protein 13*; `HGNC:371`).
- **Historical aliases reflecting partial cDNA discoveries**:
  - **Ht31** (*human thyroid RII-anchoring protein*, N-terminal fragment cloned in `PMID:1618839`; RIIalpha-binding amphipathic helix solved by NMR in `PMID:11285229`).
  - **Lbc** (*lymphoid blast crisis* oncogene, C-terminally truncated hyperactive DH/PH RhoA GEF isolated from acute-phase CML in `PMID:8290273`; purified RhoA specificity established in `PMID:8910315`; proto-Lbc C-terminal regulatory tail characterized in `PMID:9891067`).
  - **Brx** (*breast cancer nuclear receptor-binding auxiliary protein*, alternative splice isoform interacting with estrogen and nuclear hormone receptors in `PMID:9627117`).
  - **AKAP-Lbc** (full-length 2,813-aa chimeric AKAP + RhoA GEF polypeptide unified in `PMID:11546812`).
- **UniProtKB canonical entry**: `UniProtKB:Q12802` (`AKA13_HUMAN`, sequence version `2`, 2,813 aa; `PANTHER:PTHR13944:SF18`).
- **Domain & Catalytic Site Architecture (`Q12802`, `sv=2`)**:
  - **PKA RII-anchoring amphipathic alpha-helix (Ht31 peptide)**: residues `1246-1267` (`DLIEEAASRIVDAVIEQVKAAG`; `PMID:1618839`, `PMID:11285229`, `PMID:11546812`).
  - **PKA-phosphorylated 14-3-3 inhibitory motif**: `Ser1565` (`1562-RRHSWG-1567`; anchored PKA phosphorylates `Ser1565`, recruiting 14-3-3 dimers in a C-terminal leucine-zipper homo-oligomer-dependent manner to autoinhibit basal RhoGEF activity; `PMID:15229649`, `PMID:15691829`).
  - **C1-like zinc finger**: residues `1791-1839` (`Cys1805` in `1805-CSQC-1808`; `site_ref: PANTHER:PTHR13944#c1_zn_finger_cys53`).
  - **DH catalytic domain**: residues `1994-2191`, retaining `Glu2001` (`E2001A` decreases RhoA exchange; `site_ref: PANTHER:PTHR13944#dh_cr1_catalytic_glu`, `PMID:24993829`) and `Tyr2153` (`Y2153F` abolishes RhoA exchange; `site_ref: PANTHER:PTHR13944#dh_cr3_catalytic_tyr`, `PMID:11546812`). Solved in complex with `RhoA-GDP` at 2.1 Å (`PDB:4D0N`, `PMID:25186459`).
  - **PH domain**: residues `2231-2333`, dispensable for basal intrinsic GDP release in vitro (`PMID:25186459`) but binds activated `RhoA-GTPgammaS` at 2.0 Å (`PDB:6BCA`, `PMID:29876405`, `PMID:23493395`, `PMID:24993829`) as a positive-feedback module, and contains `Trp2324` involved in `IKBKB` anchoring (`PMID:23090968`).
  - **C-terminal Galpha12-binding, PKD1-anchoring, and leucine-zipper oligomerization region** (`PMID:15383279`, `PMID:15691829`, `PMID:18951085`, `PMID:31051012`).

## 2. PAINT Anomaly at `PTN002677811` (`PTHR13944-paint.tsv`)
- In `PTHR13944-paint.tsv`, node `PTN002677811` (the euteleostome `SF18` `AKAP13` clade root) carries an erroneous **`IRD` loss row (`20250516`) on `GO:0005085`**, which is why `human/AKAP13` (`Q12802`) has **no `IBA` row for `GO:0005085`** in GOA even though `Q12802` is itself listed among the experimental seeds for `GO:0005085` at the root `PTHR13944` node `PTN002677784` and carries a positive `IBD` for `GO:0035025` at `PTN002677811`! This is flagged as `LOSS_CONTRADICTED` (`REMOVE_LOSS`) in `PTHR13944-review.yaml`.

## 3. Evaluation of `AKAP13-deep-research-affinage.md`
- **Trust gates**: Passed blocking gates (`uniprot_accession: Q12802`, human, `self_evaluation_pairwise: win`, `faith_pct: 100.0`, `31` citations).
- **Strengths**: High precision across 31 primary human/mouse/rat `AKAP13` papers; accurately synthesizes dual PKA-anchoring and Galpha12-selective RhoA GEF activity (`PMID:11546812`, `PMID:31051012`), `Ser1565`/14-3-3 + C-terminal leucine-zipper autoinhibition (`PMID:15229649`, `PMID:15691829`), PKCeta-PKD1-HDAC5 hypertrophic signaling (`PMID:15383279`, `PMID:18951085`), PKNalpha-MLTK-MKK3-p38alpha (`PMID:21224381`) and KSR1-RAF-MEK-ERK (`PMID:21102438`) MAPK scaffolding, the 2.1 Å DH-PH/RhoA-GDP structure (`PMID:25186459`), embryonic cardiac development (`PMID:20139090`), and osteogenesis (`PMID:25892096`).
- **Weaknesses & Source Defects**:
  1. **Coarse `goslim_generic` `molecular_activity` grounding omits all three specific molecular functions**: Emits only `GO:0060090 molecular adaptor activity, GO:0098772 molecular function regulator activity`, failing to capture `GO:0005085` (`guanyl-nucleotide exchange factor activity`), `GO:0051018` (`protein kinase A binding`), or `GO:0005078` (`MAP-kinase scaffold activity`).
  2. **Misses PH-domain positive-feedback RhoA-GTP binding (`PMID:23493395`, `PMID:24993829`, `PMID:29876405` PDB `6BCA`)**: By relying solely on `PMID:25186459` (`with the PH domain dispensable for nucleotide exchange`), Affinage misses the 2.0 Å `PDB:6BCA` crystal structure and biochemical proof that the AKAP-Lbc PH domain binds activated `RhoA-GTP` to drive positive feedback.
  3. **Historical/mechanistic recall gaps**: Omits founding Ht31 cloning/NMR papers (`PMID:1618839`, `PMID:11285229`), founding Lbc oncogene & RhoA specificity papers (`PMID:8290273`, `PMID:8910315`, `PMID:9891067`), Brx characterization (`PMID:9627117`), and IKKbeta/NF-kappaB cardiomyocyte scaffolding (`PMID:23090968`), and lists `Akap13`-null embryonic lethality (`PMID:20139090`) alongside viable `ΔGEF`/`ΔPKD` gene-trap mice (`PMID:23658642`) without explaining the allele-architecture discrepancy.
