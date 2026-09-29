# CRTISO (At1g06820, CCR2; UniProt Q9M9Y8) — research notes

Journal for the de-novo review of Arabidopsis thaliana prolycopene isomerase /
carotenoid isomerase. Append, do not rewrite.

## 1. Identity check

- UniProt Q9M9Y8, `CRTSO_ARATH`, "Prolycopene isomerase, chloroplastic", EC 5.2.1.13,
  synonyms CCR2 (Carotenoid and chloroplast regulation protein 2), CRTISO; locus
  At1g06820, ORF F4H5.10; 595 aa precursor with a 56-residue chloroplast transit
  peptide [file:ARATH/CRTISO/CRTISO-uniprot.txt "TRANSIT 1..56 /note=\"Chloroplast\"
  /evidence=\"ECO:0007744|PubMed:22223895\""].
- Family: carotenoid/retinoid oxidoreductase family, CrtISO subfamily; PANTHER
  PTHR46313:SF3 "PROLYCOPENE ISOMERASE, CHLOROPLASTIC" (verified in
  `interpro/panther/panther.obo`; Q9M9Y8 is a listed member of PTHR46313:SF3 in
  `interpro/panther/panther-members.tsv`). InterPro IPR014101 (CrtISO), IPR045892
  (CrtISO-like), IPR002937 (amine oxidase domain), IPR036188 (FAD/NAD-binding
  superfamily); NCBIfam TIGR02730 carot_isom.
- The GOA rows, the UniProt record and the deep-research report all agree on the
  same locus. There is a distinct Arabidopsis paralog (At1g57770, "CRTISO2") that is
  NOT this gene; nothing in this review should be transferred to or from it.

## 2. What the cached publications actually contain

| PMID | Paper | Cache | Use |
|---|---|---|---|
| 11884677 | Park et al. 2002 Plant Cell — identification of Arabidopsis CRTISO (ccr2) | abstract only (`full_text_available: false`) | GOA IMP/TAS source; all quotes from the abstract |
| 11884678 | Isaacson et al. 2002 Plant Cell — tomato *tangerine* = CRTISO | abstract only | GOA TAS source; tomato ortholog |
| 15557094 | Isaacson et al. 2004 Plant Physiol — in vitro CRTISO assay (tomato enzyme) | full text | substrate specificity, redox/membrane requirement |
| 21209101 | Yu et al. 2011 J Biol Chem — CRTISO is an FAD(red)-dependent non-redox flavoprotein (tomato enzyme) | full text | cofactor, mechanism, regiospecificity |
| 32003746 | Cazzonelli et al. 2020 eLife — cis-carotene-derived apocarotenoid regulates etioplast/chloroplast development | full text | ccr2 PLB phenotype and its mechanism |
| 19174535 | Cazzonelli et al. 2009 Plant Cell — SDG8/CCR1 controls CRTISO transcription | full text | regulation; CRTISO complementation of ccr2 |
| 22223895 | Bienvenut et al. 2012 MCP — N-terminal acetylome | full text (CRTISO data are in supplementary tables, not in the body text) | UniProt transit-peptide cleavage site source |
| 22582030 | Ruiz-Sola & Rodríguez-Concepción 2012 Arabidopsis Book — pathway review | abstract only | background |
| 19969518 | Joyard et al. 2009 Mol Plant — chloroplast proteomics review | abstract only; CRTISO not named in the abstract | not quotable for CRTISO localization; noted as a knowledge gap only |

PMIDs for the non-GOA papers were resolved by exact-title PubMed esearch and title
confirmed by esummary before fetching with `uv run ai-gene-review fetch-pmid`.

## 3. Molecular function

- Genetic and enzymatic identification in Arabidopsis: "The Arabidopsis CRTISO locus
  was identified by the partial inhibition of lutein synthesis in light-grown tissue and
  the accumulation of poly-cis-carotene precursors in dark-grown tissue of crtISO
  mutants. After positional cloning, enzymatic analysis of CRTISO expressed in
  Escherichia coli confirmed that the enzyme catalyzes the isomerization of
  poly-cis-carotenoids to all-trans-carotenoids." [PMID:11884677]. This is exactly the
  GO:0046608 definition ("Catalysis of the isomerization of poly-cis-carotenoids to
  all-trans-carotenoids", QuickGO, verified 2026-09-26).
- Reaction: Rhea RHEA:30971 "7,7',9,9'-tetra-cis-lycopene = all-trans-lycopene",
  EC 5.2.1.13 (verified at rhea-db.org). UniProt CATALYTIC ACTIVITY cites
  PMID:11884677 for it [file:ARATH/CRTISO/CRTISO-uniprot.txt].
- Regiospecificity (tomato ortholog, in vitro): "CRTISO isomerizes adjacent cis-double
  bonds at C7 and C9 pairwise into the trans-configuration, but is incapable of
  isomerizing single cis-double bonds at C9 and C9′" and it converts
  "7,9,9′-tri-cis-neurosporene to 9′-cis-neurosporene and 7′9′-di-cis-lycopene into
  all-trans-lycopene" [PMID:15557094]. cis-zeta-carotenes are NOT substrates
  ("demonstrating that cis- ζ -carotenes are not substrates of CRTISO"
  [PMID:15557094]) — that step belongs to Z-ISO.
- Cofactor and mechanism (tomato ortholog, purified enzyme): "FAD is the cofactor
  required by CRTISO" and "it is the reduced form of FAD, partially replaceable by FMN
  red , which drives enzymatic activity of CRTISO" [PMID:21209101]. Crucially, the
  reaction is NOT a redox reaction: "The reduced form of this cofactor catalyzes a
  reaction not involving net redox changes" [PMID:21209101]. UniProt lists FAD, NAD(+)
  and NADP(+) as cofactors "by similarity" (ECO:0000250); only FAD is experimentally
  established, and only in the tomato ortholog.
- Membrane requirement: purified CRTISO "was enzymatically inactive with
  poly-cis-carotenes when present in Triton X-100 micelles or in liposomes prepared from
  E. coli lipids or DMPC" unless a membrane-containing lysate was present
  [PMID:15557094]; Yu et al. assayed it with substrate "embedded into phosphatidylcholine
  liposomal membranes" [PMID:21209101].

## 4. Pathway position

- Plant poly-cis desaturation route: PDS -> Z-ISO -> ZDS -> CRTISO, giving
  all-trans-lycopene for the cyclases. "CRTISO isomerizes all cis double bonds formed by
  the action of PDS and ZDS ( 14 ) yielding 7,9,9′,7′-tetra- cis -lycopene 3 (commonly
  referred to as prolycopene; 15 ) to finally form all- trans -lycopene. The latter is a
  substrate for the subsequent introduction of cyclic β- and/or ϵ-ionone end groups"
  [PMID:21209101]. Matches `modules/carotene_backbone_biosynthesis.yaml` (crtiso_step,
  concept GO:1901177 lycopene biosynthetic process; representative member Q9M9Y8).
- Light can substitute: "In the dark, the isomerisation of tri-cis-ζ-carotene to
  di-cis-ζ-carotene and tetra-cis-lycopene to all-trans-lycopene has a strict
  requirement for ZISO and CRTISO activity respectively" but "light-mediated
  photoisomerisation in the presence of a photosensitiser can substitute for a lack of
  isomerase activity" [PMID:32003746]. Hence ccr2 leaves are lutein-deficient but
  green, while etiolated tissue accumulates prolycopene.
- Tomato ortholog phenotype: "Fruit of tangerine are orange and accumulate prolycopene
  (7Z,9Z,7'Z,9'Z-tetra-cis-lycopene) instead of the all-trans-lycopene" [PMID:11884678].
- Ontology note (from the brief, verified by QuickGO ancestors 2026-09-26): GO:1901177
  is_a GO:0016120 carotene biosynthetic process, which is NOT a descendant of GO:0016117
  carotenoid biosynthetic process. This is an ontology structure issue, not something
  to fix in this review; both GO:0016117 (existing) and GO:1901177 (proposed) are
  therefore retained side by side.

## 5. Localization

- Transit peptide 1-56, cleavage after Ser-56 with N-acetyl-Val-57, from the
  large-scale N-terminal acetylome (PMID:22223895; reflected in UniProt FT lines). The
  body text of that paper does not name CRTISO; the datum is in its supplementary data.
- UniProt SUBCELLULAR LOCATION: "Plastid, chloroplast membrane {ECO:0000250};
  Peripheral membrane protein {ECO:0000250}" — inferred by similarity, not measured for
  Arabidopsis CRTISO. GO:0031969 "chloroplast membrane" is defined as either envelope
  bilayer. The deep-research report cites AT_CHLORO proteomics for an envelope
  assignment; the cached Joyard 2009 record is abstract-only and does not mention
  CRTISO, so I cannot quote it. Membrane association per se is well supported by the
  in vitro requirement for membranes (section 3), and plastid localization by the
  transit peptide and the etioplast phenotype.

## 6. The etioplast / prolamellar body phenotype (GO:0009662)

- "Etioplasts of dark-grown crtISO mutants accumulate acyclic poly-cis-carotenoids in
  place of cyclic all-trans-xanthophylls and also lack prolamellar bodies (PLBs)... This
  demonstrates a requirement for carotenoid biosynthesis to form the PLB."
  [PMID:11884677].
- Mechanism resolved later: "ccr2 is similar to cop1/det1 mutants in that it lacks a PLB
  in etioplasts, yet it is unique among PLB-deficient mutants in having normal PChlide
  and POR protein levels" and blocking upstream cis-carotene formation (ziso-155) or
  carotenoid cleavage dioxygenase activity "restored PLB formation in ccr2 etioplasts"
  [PMID:32003746]. So the PLB defect is caused by a cis-carotene-derived apocarotenoid
  signal produced when CRTISO is absent, not by CRTISO doing any of the work of
  etioplast assembly.
- Reasoning on the annotation: the phenotype is genuine, reproducible and mechanistically
  understood, and TAIR curated it with `acts_upstream_of_or_within`, which is the
  right relationship for an enzyme whose loss perturbs a downstream structure. CRTISO
  does not catalyse or scaffold any step of PLB assembly; it is upstream of it. I keep
  both the IMP and the PAINT IBA as KEEP_AS_NON_CORE (not REMOVE: the assertion is
  correct as an upstream requirement; not ACCEPT: it is not the enzyme's function).
  Comparator check (QuickGO 2026-09-26): among Arabidopsis proteins GO:0009662 is
  carried only by CRTISO, FLN2 and TOC75-4; the ~500 other rows are IBA/IEA
  propagations of the CRTISO clade to plant orthologs. That propagation is a considered
  PAINT judgement (PTN005296160) seeded by the Arabidopsis IMP, and Q9M9Y8 appearing in
  its own WITH/FROM is expected, not circular.

## 7. Review of the IEA rows

- IPR014101 (CrtISO family) -> GO:0046608 and GO:0016117: entry description is
  specifically the Arabidopsis prolycopene isomerase; both mappings correct. ACCEPT.
- IPR045892 (CrtISO-like family) -> GO:0016116 carotenoid metabolic process: the
  broader family also contains cyanobacterial CrtD (myxoxanthophyll C-3',4'
  desaturase), so InterPro chose the metabolic parent. For CRTISO itself the process is
  biosynthetic; MODIFY to GO:0016117 (already carried by the gene) — not wrong, just
  less specific than the evidence allows.
- IPR002937 (amine oxidase domain) -> GO:0016491 oxidoreductase activity: a fold-level
  mapping. CRTISO shares the FAD-binding amine-oxidase fold with CRTI-type desaturases
  and monoamine oxidases but catalyses a cis-trans isomerization with no net redox
  change [PMID:21209101 "catalyzing non-redox reactions"]; EC 5.2.1.13 is an isomerase
  class, and GO:0046608 sits under GO:0016859 cis-trans isomerase activity, not under
  GO:0016491. REMOVE as a paralog/fold activity the protein does not have (the brief's
  explicit rule for InterPro2GO rows). Note the older Isaacson 2004 model ("reversible
  redox reaction acting at specific double bonds") is a transient-hydride mechanism
  hypothesis, not evidence of an oxidoreductase activity; UniProt still echoes that
  sentence.
- SL-0053 -> GO:0031969 chloroplast membrane: consistent with UniProt (by similarity)
  and with membrane-dependent catalysis. ACCEPT, flagging that direct sub-plastid
  localization data for Arabidopsis CRTISO are not in the cached literature.

## 8. NEW proposal

- GO:1901177 lycopene biosynthetic process ("The chemical reactions and pathways
  resulting in the formation of lycopene"; not obsolete, QuickGO 2026-09-26).
  Participation test: CRTISO catalyses the terminal step (prolycopene ->
  all-trans-lycopene; RHEA:30971). Comparator check: Arabidopsis ZDS1 (Q38893) carries
  GO:1901177 by IDA (PMID:9914519) and the module uses GO:1901177 as the concept for the
  whole poly-cis desaturation/isomerization node. UniProt PATHWAY: "Carotenoid
  biosynthesis; lycopene biosynthesis." Not redundant with GO:0016117 because of the
  ontology structure noted in section 4. Evidence: IMP/IDA from PMID:11884677 (mutant
  accumulates poly-cis precursors; recombinant enzyme isomerizes them), corroborated by
  the tomato ortholog in vitro [PMID:15557094, PMID:21209101].
- Considered and NOT proposed: FAD binding (GO:0050660/GO:0071949) — experimentally
  shown only for the tomato enzyme [PMID:21209101]; UniProt lists it by similarity. Left
  as a suggested experiment rather than an annotation. GO:0016120 carotene biosynthetic
  process — ancestor of GO:1901177, redundant.

## 9. Regulation (context only, not annotated)

- SDG8/CCR1 histone methyltransferase is required for CRTISO transcription: "The level
  of CRTISO transcripts in ccr1-4 leaf tissue was only 10% that of wild-type leaves"
  and a CRTISO genomic fragment "completely restoring lutein levels by 96% in ccr2-1"
  [PMID:19174535]. Confirms At1g06820 is the ccr2 gene and that CRTISO can be
  rate-limiting for lutein.

## 10. Open questions carried into the review

- Physiological reductant that keeps CRTISO-bound FAD reduced in plastids (Yu et al.
  used dithionite/N2; Isaacson et al. used E. coli respiratory chain).
- Sub-plastid membrane (envelope vs thylakoid) for the Arabidopsis protein.
- Whether Arabidopsis CRTISO shares the tomato enzyme's strict 7,9-pair requirement and
  FAD dependence (all in vitro work used the tomato ortholog).
