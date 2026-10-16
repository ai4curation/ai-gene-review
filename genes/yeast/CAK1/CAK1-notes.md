# CAK1 (YFL029C, CIV1; UniProt P43568) - curation notes

Working journal for the GO annotation review of *S. cerevisiae* CAK1. Inline citations
quote the cached text in `publications/PMID_*.md` verbatim; statements attributed to
papers that are not cached are marked as such and come from the Falcon deep-research
report (`CAK1-deep-research-falcon.md`).

## 2026-09-26 - initial review session

### Inputs used

- `CAK1-uniprot.txt`: EC 2.7.11.22, "CMGC Ser/Thr protein kinase family, CDC2/CDKX
  subfamily", single 368-aa kinase domain, catalytic Asp156; IntAct interaction with
  CDC28 (P00546, NbExp=3). Note the UniProt PANTHER cross-reference is PTHR44167:SF24
  (a CHK2-like family), whereas the IBA rows in GOA come from PTN008391902 (with human
  CDK10) and the deep CDK node PTN000623091; `modules/g2_m_transition.yaml` follows the
  local PANTHER 19.0 classification (PTHR24056:SF508). No PANTHER id is asserted in this
  review, so nothing hinges on which is right.
- `CAK1-goa.tsv`: 25 rows (3 IBA, 4 IEA, 3 IPI, 8 IDA/IMP to GO:0097472, 2 IMP to
  GO:0000086, 1 IDA cytoplasm, 1 IMP meiotic cell cycle, 2 IGI GO:0060633).
- `CAK1-deep-research-falcon.md` (Edison, 31 citations): agrees with the primary
  literature on every point I could check against cached abstracts; used for the Bur1
  Thr240 (Yao & Prelich 2002, doi:10.1128/MCB.22.19.6750-6758.2002), Ctk1 Thr338
  (Ostapenko & Solomon 2005, doi:10.1128/MCB.25.10.3906-3913.2005) and Kin28-in-vivo
  (Espinoza et al. 1998, doi:10.1128/MCB.18.11.6365) statements, whose primary papers
  are not in the cache. I did not fetch them because the task scope was limited to
  `genes/yeast/CAK1/`.
- Cached publications read: PMID:8752210, PMID:8752211, PMID:8781234, PMID:9819350
  (abstract only); PMID:10373527, PMID:11739722, PMID:19269370 (full text);
  PMID:10688190, PMID:14690591, PMID:20489023 (abstract only, high-throughput);
  PMID:9857180 (abstract; fission-yeast Csk1, mentions Cak1/Civ1 as the budding-yeast
  CAK).

### What Cak1 is

- Three groups independently purified/cloned the budding-yeast CAK in 1996. It is a
  monomer, active without a cyclin, active in E. coli, and not part of TFIIH
  [PMID:8752210 "Unlike CAKs from other organisms, Cak1p is active as a monomer, has
  full activity when expressed in E. coli, and is not a component of the basal
  transcription factor, TFIIH."]; it is "most similar in sequence to the Cdks, but
  unlike them is active as a monomer" [PMID:8752211]; and it is "an unusual
  44-kilodalton protein kinase, Cak1, that is only distantly related to CDKs"
  [PMID:8781234].
- Essential: "The CIV1 gene is essential for yeast cell viability" [PMID:8752211];
  "The CAK1 gene was essential for cell viability." [PMID:8781234].
- Activity is not cell-cycle regulated: "Cak1 accounted for most CAK activity in yeast
  cell lysates, and its activity was constant throughout the cell cycle." [PMID:8781234].
  So Cak1 is a constitutive CDK-maturation step, not a timed switch; the timing of
  Cdc28 activity comes from cyclins, Swe1/Mih1, Sic1 etc.
- Localisation: "Cak1p is dispersed throughout the cell as shown by
  immunofluorescence; biochemical subcellular fractionation confirmed that most of the
  Cak1p is found in the cytoplasm." [PMID:9819350]. Stable in exponential growth,
  drops in stationary phase, oscillates in meiosis [PMID:9819350].
- Substrate preference (deep research, from Kaldis et al. 1998 MBoC, not cached):
  "yeast Cak1 preferentially phosphorylated monomeric CDKs, whereas human
  Cdk7-containing CAK favored cyclin-bound complexes" - consistent with a cytoplasmic
  pool acting on Cdc28 before cyclin binding and nuclear import.

### Substrates (all activation-loop threonines)

| Substrate | Site | Evidence | Source |
|---|---|---|---|
| Cdc28 (Cdk1) | Thr169 | in vitro + loss in cak1-ts; sole essential mitotic role | PMID:8752210, PMID:8752211, PMID:9819350, PMID:11739722 |
| Kin28 (TFIIH, Cdk7 ortholog) | Thr162 | in vitro + loss in vivo; stimulates CTD kinase | PMID:10373527 |
| Bur1 | Thr240 | in vitro; T240A ~ cak1 mutant | Yao & Prelich 2002 (not cached; deep research) |
| Ctk1 (CTDK-I) | Thr338 | in vitro + in vivo; T338A inactive | Ostapenko & Solomon 2005 (not cached; deep research; cited in PMID:19269370) |
| Smk1 / Ime2 | - | NOT direct substrates in vitro | PMID:11739722 "Neither Ime2-GSTp or Smk1-HAp was phosphorylated under conditions in which CDK2 was phosphorylated in a robust fashion" |

- Kin28: "Kin28p is no longer phosphorylated on Thr-162 following inactivation of Cak1p
  in vivo, that Cak1p can phosphorylate Kin28p on Thr-162 in vitro, and that this
  phosphorylation stimulates the CTD kinase activity of Kin28p" [PMID:10373527]. But
  Thr162 phosphorylation is not essential: kin28-T162A rescues a KIN28 disruption; it
  becomes severe only in a tfb3-ts (MAT1) background [PMID:10373527, results].
- Selectivity: Pho85 and Srb10 do not depend on Cak1 (deep research, Espinoza 1998).
- Cak1's sole essential mitotic role is Cdc28 Thr169 [PMID:11739722 "CAK1 encodes a
  protein kinase in Saccharomyces cerevisiae whose sole essential mitotic role is to
  activate the Cdc28p cyclin-dependent kinase by phosphorylation of threonine-169 in
  its activation loop."]; CDC28-43244 (T169E + hyperactivating substitutions) lets
  cak1-null cells grow [PMID:11739722, results].

### Cell-cycle phenotype

- "A temperature-sensitive mutation in CAK1 confers a G2 delay accompanied by low
  Cdc28p protein kinase activity and shows genetic interactions with altered expression
  of the gene for the major mitotic cyclin, CLB2." [PMID:8752210].
- "Cdc28 phosphorylation and activity are conditionally inhibited in a civ1-4
  temperature-sensitive mutant." [PMID:8752211]. The arrest morphology is in the full
  text (not cached); the SGD IMP to G2/M is taken on trust, and is consistent with
  PMID:8752210. Deep research adds that null microcolonies are heterogeneous (~21%
  unbudded, 33% large-budded), i.e. Cak1 loss affects G1 as well as G2/M, as expected
  for the activator of all Cdc28 complexes.

### Meiosis and sporulation (PMID:11739722, full text)

- cak1-null CDC28-43244 diploids: premeiotic S delayed from ~4 h to >12 h; IME1 induced
  slowly and to low level; middle genes (NDT80, SMK1, CLB1, SPR3) essentially absent
  through 12 h; only 13% complete MI+MII; no spores. Kinase-dead cak1-D169R phenocopies
  the null: "These results indicate that the catalytic activity of Cak1p is required
  for its functions in meiosis and spore formation."
- Smk1 (MAPK for spore wall) T207 phosphorylation requires Cak1 ("Smk1p is not
  activated in a cak1 missense mutant") but Cak1 does not phosphorylate Smk1 or Ime2 in
  vitro, so an intermediary kinase is inferred. High-copy IME1 restores IME1/HOP1 mRNA
  but not meiotic divisions, so the early defect is not just an IME1 deficit.
- Summary: "The data indicate that Cak1p activates multiple steps in meiotic
  development through multiple protein kinase targets." Direct meiotic targets unknown.

### Transcription / chromatin (PMID:19269370, full text)

- Signalling E-MAP: positive genetic interactions CAK1-SET2, CAK1-EAF3 (confirmed by
  tetrads: "eaf3Δ and set2Δ suppressed the slow growth phenotype observed in a
  cak1-DAmP background"), CAK1-CTK1 epistatic with overlapping expression profiles.
- Phenotype: "the cak1-DAmP strain, as well as other previously characterized CAK1
  mutants (cak1-22, cak1-23, cak1-95) (Espinoza et al., 1998), showed a significant
  increase of transcription initiation from a cryptic internal TATA site within FLO8".
- Mechanism offered by the authors: Cak1 -> Ctk1 (T338) -> CTD Ser2-P -> Set2 H3K36me ->
  Eaf3/Rpd3C(S) deacetylation -> suppression of cryptic initiation; Bur1 is a parallel
  Cak1-dependent branch ("Cak1 acts as a key regulator controlling two kinases cascades
  involved in regulating intergenic chromatin integrity").
- The SGD IGI rows (with SET2 = SGD:S000003704 and EAF3 = SGD:S000006227) to
  GO:0060633 are therefore mechanistically explained but two to three steps removed
  from Cak1's own activity - kept as non-core.

### GO term issues found

1. **GO:0019912 "cyclin-dependent protein kinase activating kinase activity" is
   obsolete (2025-05-30)**, with `consider GO:0004672` and `consider GO:0097472`
   (QuickGO history). This explains why the eight SGD IDA/IMP rows sit on GO:0097472
   "cyclin-dependent protein kinase activity". That term is defined as
   "Cyclin-dependent catalysis of the phosphorylation of an amino acid residue in a
   protein", which the cited papers explicitly contradict for Cak1 (active as a
   monomer; full activity in E. coli). Decision: MODIFY all eight rows to GO:0004674
   protein serine/threonine kinase activity (has_input Cdc28 / Kin28), with the CAK
   role expressed at the process level (GO:0045737). Comparator: PomBase annotates the
   analogous monomeric fission-yeast CAK **csk1** (SPAC1D4.06c) to GO:0004674 with
   `has_input cdc2` and `part_of GO:0010971 positive regulation of G2/M transition`,
   not to a CDK-activity term - so the proposed representation matches an existing MOD
   convention. By contrast PomBase does annotate **mcs6** (SPBC19F8.07, the genuinely
   cyclin-dependent Cdk7 ortholog in the Mcs6-Mcs2 complex) to GO:0097472 and
   GO:0004693, which is exactly the distinction that matters: those terms are for the
   cyclin-bound CDK, not for a monomeric CAK.
2. **GO:0004693 IEA from EC:2.7.11.22** and **GO:0106310 protein serine kinase
   activity IEA from RHEA:17989** are mechanical consequences of UniProt's EC
   assignment; the first asserts cyclin dependence (contradicted), the second asserts
   serine specificity (no serine site known; every characterised site is a threonine;
   GO has no protein threonine kinase term). Both MODIFY -> GO:0004674.
3. **GO:0005515 protein binding IPI x3 (Cdc28)**: REMOVE per project policy; the
   interaction is real and is an enzyme-substrate relationship ("Civ1 binds tightly to
   and phosphorylates Cdc28" [PMID:8752211]) that belongs as has_input on the kinase
   activity row.
4. **GO:1902749 regulation of cell cycle G2/M phase transition (IBA, node seeded by
   human CDK10)**: accepted; definition ("signaling pathway that modulates the activity
   of a cell cycle cyclin-dependent protein kinase to modulate the switch from G2 to
   M") fits literally, though Cak1 is a constitutive primer rather than a timed
   regulator and GO:0000086 is the more direct term.
5. **No NEW annotations.** The obvious candidate, GO:0045737 positive regulation of
   cyclin-dependent protein serine/threonine kinase activity, fails the comparator
   check: human CDK7 (P50613), mouse Cdk7 (Q03147) and pombe csk1 carry none of
   GO:0045737 / GO:1904031 / GO:0000079 / GO:0032147 (QuickGO, 2026-09-26); they carry
   cell-cycle-transition and transcription terms instead. I read this as a convention
   (CAKs are annotated to the transition they enable, with the CDK as has_input on the
   kinase activity) rather than a gap, and left it as a suggested question. GO:0045737
   is still used in `core_functions.directly_involved_in` because it is the most
   accurate statement of what Cak1 does; the validator warns about this twice.
6. Ascospore formation (GO:0030437) for the Smk1/spore-wall role would be more specific
   than "meiotic cell cycle" but is not in GOA; noted in the GO:0051321 review reason
   rather than proposed.

### Actions summary (25 rows)

- ACCEPT 9: GO:0000086 (IBA, IMP x2), GO:0004672 IEA, GO:0004674 IBA, GO:0005524 IEA,
  GO:0005634 IBA, GO:0005737 IDA, GO:1902749 IBA.
- MODIFY 10 (-> GO:0004674): GO:0097472 x8, GO:0004693 IEA, GO:0106310 IEA.
- REMOVE 3: GO:0005515 IPI x3.
- KEEP_AS_NON_CORE 3: GO:0051321 IMP, GO:0060633 IGI x2.

### Validation

`just validate yeast CAK1`: valid, 2 warnings (GO:0045737 in core_functions not in
existing_annotations - deliberate, see item 5). `just render yeast CAK1` done.

### Open questions

- Which kinase does Cak1 phosphorylate to drive premeiotic S and Smk1 activation?
- How does the mostly cytoplasmic Cak1 pool service the nuclear CDKs Kin28, Bur1, Ctk1?
- Is the phosphorylation-independent suppression of Cdc28 C-terminal mutants by
  catalytically weak Cak1 (Kim et al. 2009 Gene, not cached; deep research) a genuine
  chaperone-like role?
