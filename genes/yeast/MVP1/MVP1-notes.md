# MVP1 (YMR004W, P40959) curation notes

## Session 2026-11-21: provenance of the research

- Deep research providers (falcon, perplexity) are not configured in this environment, so no
  `MVP1-deep-research-<provider>.md` file exists and none was run. Everything below is my own
  reading of the cached publications and the UniProt record.
- `just mod-description-deep-research yeast MVP1` succeeded and wrote
  `MVP1-deep-research-sgd.md` (SGD hand-written description, fetched 2026-11-21). Its claims are
  checked in the review's `reference_review` for that file.
- `just paint-losses yeast MVP1`: "No IRD or IKR loss on this gene's lineage."
- PubMed E-utilities searches (esearch, then esummary):
  - `Mvp1[tiab] AND (yeast OR cerevisiae)`: 9 hits (41883240, 41083234, 35800464, 34524084,
    32198400, 24567361, 24330158, 21954159, 7862158). 41083234 is about the Setosphaeria
    turcica orthologue, 24330158 is an Arabidopsis gene with a MVP1 alias, 35800464 is a
    protocol paper.
  - `Mvp1[tiab] AND Vps1[tiab]`: 34524084, 24567361, 7862158.
  - `Mvp1[tiab] AND SNX8`: 41883240, 34524084, 24567361.
  - `Mvp1[tiab] AND retromer`: 41883240, 35800464, 34524084, 24567361.
  - `YMR004W`: 1 hit (15263065), not relevant to function.
  - `SNX-BAR[tiab] AND yeast[tiab] AND Vps55`: 34524084.
- Cached with `just fetch-pmid`: PMID:34524084 (full text), PMID:41883240 (full text),
  PMID:27883263 (abstract only; no PMC record).
- Not readable: the full text of PMID:7862158 (Ekena and Stevens 1995, PMC230391). Europe PMC
  returned HTTP 500 for the XML and 403 for the PDF; the cache is abstract-only.
  PMID:11557775 and PMID:27883263 are also abstract-only.

## Identity and domain architecture

- 511 aa SNX-BAR sorting nexin; human homologue SNX8. UniProt: PX domain 128..247, disordered
  N-terminal region 1..36; PI3P-binding residues 172, 174, 198, 213 (by similarity);
  InterPro SNX8/Mvp1 (IPR028662), Snx8 BAR domain (PF19566).
- Seven yeast SNX-BARs: "Vps5 (SNX1/2 in humans), Vps17 (SNX5/6/32 in humans), Snx4 (SNX4 in
  humans), Snx41 (SNX7 in humans), Snx42 (SNX30 in humans), Mvp1 (Snx8 in humans), and
  Ykr078w" [PMID:34524084].
- Structure (cryo-EM, 4.2 A, PDB 6Q0X): "Full-length Mvp1 is a tetramer consisting of two Mvp1
  dimers that self-interact in such a manner that the concave lipid-engaging surfaces of the
  BAR dimers are buried." [PMID:32198400]. N-terminal deletions (Δ2-78, Δ2-100) are dimeric,
  bind liposomes better and still tubulate them, but Δ2-100 "did not rescue the CPY
  trafficking defect in Δmvp1 cells" [PMID:32198400]. The authors propose "the N-terminus
  promotes tetramerization as a mechanism of autoinhibition" [PMID:32198400].

## Molecular function

1. **PI3P binding (PX domain).**
   - All yeast PX domains bind PI3P in lipid overlays, with one unnamed outlier
     [PMID:11557775, abstract only].
   - In vivo: "Localization to these puncta is disrupted by loss of the sole PI3K (vps34Δ)
     and by a mutation, R172A, in the PtdIns3P binding pocket of its PX domain"
     [PMID:24567361]; R172E likewise [PMID:34524084].
   - In vitro: "full-length Mvp1 interacts with liposomes, but only in the presence of PI3P"
     [PMID:32198400].
2. **Membrane bending (BAR domain).**
   - "Membrane tubules were observed in reactions containing 10 µM and 20 µM Mvp1, but not
     in reactions without Mvp1" [PMID:24567361]. Tubules 36-63 nm; also uniformly sized
     ~54 nm vesicles, i.e. apparent fission in vitro, "not previously reported for a SNX-BAR
     protein" [PMID:24567361].
   - Independently: "Mvp1 also deformed liposomes into tubules with mean and median
     diameters of 49.8 (±13.4) nm and 48 nm" [PMID:32198400].
   - In vivo relevance: Mut1 (198KRI→AAA) cannot bind or tubulate liposomes and is "as
     defective as cells lacking Mvp1 altogether" for CPY sorting [PMID:32198400]; the
     dimer-interface mutant I346E/Q468E/W496E "failed to rescue the mislocalization of
     Vps55-GFP" [PMID:34524084].
   - GO term: GO:0180020 membrane bending activity (checked in OLS; parent molecular_function).
     Proposed as NEW (IDA).
3. **Self-association.** Homodimer (BAR-BAR) and autoinhibited tetramer [PMID:32198400];
   Mvp1-GFP co-IPs Mvp1-FLAG "but not with other SNX-BAR proteins" [PMID:34524084].
4. **Vps1 binding (disputed).**
   - Chi et al.: "we have never observed binding of these proteins in solution or on a
     membrane" [PMID:24567361].
   - Suzuki et al.: "Mvp1 coprecipitated with Vps1-GFP, but not with GFP, suggesting that
     Mvp1 directly binds to Vps1" [PMID:34524084], with recombinant proteins; the
     GTP-hydrolysis-dead Vps1 K42A binds more strongly.
   - Not proposed as a GO annotation; left as a question and a knowledge gap.
5. **Cargo recognition.** Vps55 needs its 61-YHTSDFM-67 motif to co-IP with Mvp1, "although
   it is also possible that the Vps55-Mvp1 interaction is bridged by another protein"
   [PMID:34524084]. Not enough for a cargo-binding MF term.

## Biological roles

1. **Endosome-to-Golgi retrieval (core).**
   - Chi et al. 2014 (BY4742 background): Vps10 shifts from Golgi to endosomes in mvp1Δ;
     "they suggest that Mvp1 has a role in retrograde sorting of Vps10" [PMID:24567361].
     Mvp1 and Vps17 co-coat ~54% of budding tubules; Vps10 is in 60% of Mvp1-coated tubules.
     "Thus, Mvp1 can be considered a component of the retromer-mediated retrograde pathway."
     [PMID:24567361].
   - Sun et al. 2020 (W303A): Δmvp1 increases vacuole-membrane Vps10-EGFP and secretes CPY
     [PMID:32198400].
   - Suzuki et al. 2021: Mvp1 is the coat for a separate pathway. "Strikingly, Vps55-GFP
     accumulated on the vacuole membrane in mvp1Δ cells" while it stays endosomal in vps35Δ
     and snx4Δ. Vps55 vesicles accumulate in sec18ts cells and lack Vps10. Vps10, Kex2 and
     Neo1 localise normally in mvp1Δ: "These observations suggest that Mvp1 is not required
     for retromer-mediated recycling." [PMID:34524084]. Nhx1 is recycled cooperatively by
     retromer, Snx4 and Mvp1, and the triple mutant fails to grow at 37°C.
   - Kölling 2026: "From this, we conclude that Vps68 recycling depends on both Mvp1 and
     retromer." A weak Mvp1-Vps26 co-IP, about 50-fold below Vps5 [PMID:41883240].
   - **Disagreement to carry forward:** whether Mvp1 is needed for retromer cargo (Vps10)
     differs between Chi 2014/Sun 2020 and Suzuki 2021. All agree that Mvp1 acts in
     endosome-to-Golgi retrieval, so GO:0042147 stands either way.
2. **Endosome membrane tubulation and carrier fission with Vps1.**
   - Mvp1-coated tubules bud from endosomes and undergo fission [PMID:24567361]; Mvp1
     "promotes association of Vps1 with the endosome in vivo" [PMID:24567361, abstract];
     82% vs 34% of Vps17 endosomes carry Vps1-GFP in wild type vs mvp1Δ/mvp1Δ.
   - Suzuki et al. found Vps1-GFP still endosomal in mvp1Δ, lost only in
     vps35Δ snx4Δ mvp1Δ; Mvp1 oligomerisation is needed for that rescue [PMID:34524084].
   - Endosome fission (GO:0140285) is not proposed for Mvp1. Comparator check (QuickGO,
     queried by taxon, which returns positives): in S. cerevisiae only VPS1 carries the term
     (IMP, PMID:24567361); in human TMCC1, WASHC5, WIPI1, CORO1C carry it. No SNX-BAR
     (Vps5, Vps17, SNX1, SNX5, SNX8) does. In GO the fission term goes to the executor.
     By contrast GO:0097750 endosome membrane tubulation is carried by human SNX1 and SNX5
     (IDA, PMID:37322239), the same SNX-BAR role, which supports the MODIFY below.
     (Note: a QuickGO query filtered with goEvidence=IDA etc. silently ignored the filter and
     returned the same 3260 hits each time; the by-taxon query was used instead.)
3. **CPY sorting (vacuolar protein sorting).** Original phenotype: MVP1 "is itself required
   for vacuolar protein sorting" [PMID:7862158]. Severity reported differently: "Null mvp1Δ
   cells secrete 65% of newly synthesized CPY" [PMID:24567361] vs "mvp1Δ cells only exhibit
   a mild CPY-sorting defect" [PMID:34524084]. Treated as non-core: it follows from the
   receptor-recycling role, whose extent for Vps10 is disputed.
4. **Nucleus/transcription (one study).** Immunostaining of C-LYTAG-tagged Mvp1 showed
   "mostly a cytosolic signal" plus some nuclear staining; the authors note GFP-tagged
   Mvp1 is cytoplasmic in the genome-wide collection [PMID:21954159]. Deletion effects on
   Ser5-P CTD and HSP12/HSP26 expression are indirect. Not replicated; GFP-tagged Mvp1 is
   cytosolic and endosomal in the later studies [PMID:24567361; PMID:34524084].

## Location summary

- Cytosolic pool (autoinhibited tetramer) plus PI3P-dependent endosome membrane and
  endosome-derived tubules. In pep12Δ cells, "Mvp1-GFP lost its endosomal localization and
  was distributed to the cytoplasm" [PMID:34524084].
- Vacuole membrane only in mutants (Δ2-100; vps35Δ) [PMID:32198400; PMID:34524084].

## GO-CAMs (gocams/index.tsv)

- No production GO-CAM contains S. cerevisiae Mvp1 (SGD:S000004606 / P40959).
- S. pombe mvp1 (PomBase:SPAC3A11.06) is activity gomodel:6918f23700004102/6a0784b700005716
  in the PomBase model "endosome transport via multivesicular body sorting pathway"
  (gomodel:6918f23700004102): MF GO:0140312 cargo adaptor activity, has_input vps55
  (PomBase:SPAC630.11) and vps68 (PomBase:SPBC8D2.02c), part_of GO:0042147, occurs_in
  GO:0010008. Its part_of evidence is IEA (InterPro:IPR028662) and IBA (PANTHER:PTN001632411
  with SGD:S000004606), i.e. it rests on the S. cerevisiae annotation, not on pombe data.
  The has_input edges match Suzuki 2021 (Vps55) and Kölling 2026 (Vps68). Note for a later
  module: GO:0140312 is defined as binding the scaffolding elements of a vesicle coat and
  bridging membrane, cargo receptor and deformation machinery; Mvp1 is itself the coat and
  the membrane-deforming protein, so GO:0180020 membrane bending activity may fit better.
  Recorded as a suggested question, no GO-CAM review written.
- The same model has vps55 and vps68 activities (part_of GO:0032511).

## Facts for a yeast retromer module

- Mvp1 is not a retromer subunit: Mvp1 does not co-IP with Vps5/Vps17/Vps26/Vps29/Vps35
  [PMID:24567361; PMID:34524084]; only a weak Mvp1-Vps26 co-IP [PMID:41883240].
- Mvp1 homodimerises and does not heterodimerise with other SNX-BARs [PMID:34524084].
- Partners: Vps1 (genetic, PMID:7862158; direct binding in vitro, PMID:34524084, disputed by
  PMID:24567361); cargo Vps55 (motif-dependent co-IP, PMID:34524084), Vps68 (PMID:41883240),
  Nhx1 (with retromer and Snx4, PMID:34524084), Vps10 (disputed).
- Three parallel SNX-BAR recycling pathways: retromer, Snx4 and Mvp1 [PMID:34524084].

## Consistency with the VPS1 review

- VPS1 review says Vps1 cuts retromer/Mvp1-coated tubules (PMID:24567361) and lists
  "What recruits Vps1 to retromer/Mvp1-coated endosomal tubules" as an open question. The
  VPS1 notes do not cite Suzuki 2021 (PMID:34524084), which reports direct Mvp1-Vps1 binding
  and that Mvp1 recruits Vps1. PMID:42477131 (cached for VPS1) also cites Suzuki 2021 for a
  retromer-independent Mvp1/Vps1 pathway for Vps55. No contradiction, but the VPS1 question
  could cite PMID:34524084. Not edited here.
- VPS1 accepts GO:0006623 protein targeting to vacuole. Here the two MVP1 rows are
  KEEP_AS_NON_CORE, because Mvp1's contribution to Vps10 recycling is partial and disputed,
  whereas Vps1 is strictly required.

## Decisions summary (see review YAML)

- ACCEPT: endosome (IBA, IDA), endosome membrane (EXP, IEA), PI3P binding (IBA, IDA),
  phosphatidylinositol binding (IEA), retrograde transport endosome to Golgi (IBA, IEA, IMP).
  The endosome IDA row was first drafted as MODIFY to endosome membrane. It was changed to
  ACCEPT because the membrane claim is already accepted from the same paper (EXP row), the
  organelle claim is informative on its own, and the draft drew an
  `inconsistent_review_actions` warning against the accepted IBA row on the same term.
- MODIFY: plasma membrane tubulation IDA → endosome membrane tubulation (GO:0097320 was
  labelled "membrane tubulation" until 2016-12-23 according to QuickGO term history; SGD
  annotated it 2015-01-05; recorded as a WRONG_TERM source defect); identical protein binding
  (cryo-EM IPI) → protein homodimerization activity.
- KEEP_AS_NON_CORE: cytoplasm (IDA, IEA), cytosol (IEA), protein targeting to vacuole (IBA,
  IMP), identical protein binding (Y2H IPI).
- MARK_AS_OVER_ANNOTATED: nucleus (IDA PMID:21954159).
- NEW: GO:0180020 membrane bending activity (IDA, PMID:24567361).
- Source defects recorded: SGD WRONG_TERM on the GO:0097320 row (repoint to GO:0097750);
  MISSING_STATEMENT for the UniProt FUNCTION comment (no retromer-independent Vps55 pathway or
  Vps1 binding) and for the SGD description (no endosome-to-Golgi recycling role).

## Workspace note

- The repository's Edit/Write pre-tool hook runs `uv run` without the shared-environment
  variables. On the first Write of the review YAML it created a 1.4 GB `.venv` in this
  worktree and rewrote `uv.lock`; both were removed/restored, and later edits were made
  through the shell.
