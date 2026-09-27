# ADGRV1 (Q8WXG9) annotation review notes

Gene: ADGRV1 / GPR98 / VLGR1 / MASS1 / USH2C. HGNC:17416. Human, NCBITaxon:9606.
Largest known GPCR / cell surface protein (full-length VLGR1b ~6,307 aa).

## Core biology (wild-type focus)

- Adhesion GPCR (family B / LNB-7TM). Huge ectodomain: 35 Calx-beta (Ca-exchanger beta)
  repeats, EAR/EPTP repeats, pentraxin-like domain; GAIN domain with GPS autoproteolysis
  site cleaving into extracellular alpha subunit + membrane 7TM beta subunit.
  [PMID:11606593 "The longest gene product, VLGR1b, is 6307 amino acids ... a much larger
  ectodomain containing 35 calcium exchanger beta repeats and a pentraxin homology domain."]
  [PMID:14740321 "All LNB 7TM members, including VLGR1, have a G-protein-coupled proteolysis
  site (GPS)"]

- Calx-beta repeats bind calcium in vitro (overlay assays with isolated repeats).
  [PMID:10976914 "Bacterial fusion proteins containing two or four repeats specifically bind
  45Ca in overlay experiments; binding is competed poorly by Mg2+ but competed well by
  neomycin, Al3+, and Gd3+."] -> supports GO:0005509 IDA.

- Cell-surface expression demonstrated by biotinylation of recombinant protein.
  [PMID:10976914 "the recombinant protein is expressed on the surface of transfected
  mammalian cells."] -> GO:0009986 cell surface IDA, GO:0005886 plasma membrane.

## USH2 complex / ankle links (hearing)

- ADGRV1 is the transmembrane core of the USH2 quaternary complex (USH2A + GPR98 + WHRN +
  PDZD7). WHRN & PDZD7 both required for complex; PDZD7 prefers GPR98, WHRN prefers USH2A;
  WHRN-PDZD7 heterodimer bridges USH2A-GPR98. [PMID:25406310 "both WHRN and PDZD7 are
  required for the complex formation with USH2A and GPR98. In this USH2 quaternary complex,
  WHRN prefers to bind to USH2A, whereas PDZD7 prefers to bind to GPR98."]
- Colocalize at ankle-link region of developing hair bundle. [PMID:25406310 "In hair cells,
  proteins encoded by the four genes are colocalized at the ankle link region of the
  mechanosensitive structure, the hair bundle, during development"]
- ADGRV1 ectodomain forms the ankle links themselves (transient in mammalian cochlea).
  -> GO:0002141 ankle link (part_of), GO:0002142 ankle link complex, GO:1990696 USH2 complex,
  GO:0032420 stereocilium, GO:0060171 stereocilium membrane, GO:0060122 stereocilium
  organization, GO:0050910 detection of mechanical stimulus (acts_upstream_of_or_within).

- Whirlin directly associates with VLGR1b (basis of IPI GO:0005515 PMID:16434480). Mediated
  by whirlin PDZ domains binding GPR98 C-terminal PDZ-binding motif -> MODIFY to GO:0030165
  PDZ domain binding. [PMID:16434480 "whirlin directly associates with USH2A isoform b and
  VLGR1b"]
- PDZD7 PDZ2 binds GPR98 PDZ-binding motif (IPI GO:0005515 PMID:20440071) -> MODIFY to
  GO:0030165. [PMID:20440071 "it is mediated by the PDZ2 domain of PDZD7 and the PDZ-binding
  motif of GPR98."]

## Photoreceptor periciliary complex (vision)

- ADGRV1, usherin, whirlin form periciliary membrane complex at apical inner segment around
  connecting cilium. Pdzd7 knockdown reduces Gpr98 at connecting cilium. [PMID:20440071
  "reduced Gpr98 localization in the region of the photoreceptor connecting cilium"]
  -> GO:0001917 photoreceptor inner segment, GO:1990075 periciliary membrane compartment.
- USH2C -> progressive RP = photoreceptor maintenance. [PMID:15671307 "USH2C and USH2A
  manifest photoreceptor disease with rod- and cone-mediated visual losses and thinning of
  the outer nuclear layer."] -> GO:0045494 photoreceptor cell maintenance (ACCEPT), and the
  GO:0048496 "maintenance of animal organ identity" IMP is a contorted mapping -> MODIFY to
  GO:0045494.

## Signaling

- UniProt (by similarity to mouse Q8VHN7): couples to Gai (GNAI1/2/3), Gaq (GNAQ), Gas
  (GNAS), inhibiting adenylate cyclase and cAMP. Cleaved beta subunit constitutively inhibits
  AC more strongly than full-length. -> GO:0004930 GPCR activity (ACCEPT, multiple evidences),
  GO:0001965 G-alpha-subunit binding (ACCEPT), GO:0007186 GPCR signaling pathway (ACCEPT).
- GO:0010855 adenylate cyclase INHIBITOR ACTIVITY is mechanistically wrong: inhibition is
  indirect via Gi, ADGRV1 does not bind AC. -> MODIFY to GO:0007193 (AC-inhibiting GPCR
  signaling pathway). Applies to both IBA and ISS copies.

## Pleiotropic / non-core

- Ca-dependent PKA/PKC activation regulating MAG ubiquitination / myelination (auditory
  pathway) -> GO:0071277 cellular response to calcium (KEEP_AS_NON_CORE), GO:0031647
  regulation of protein stability (KEEP_AS_NON_CORE). UniProt by-similarity.
- Bone metabolism -> GO:0030501 positive regulation of bone mineralization (KEEP_AS_NON_CORE),
  UniProt by-similarity, mouse.
- Seizures: mouse mass1/Frings audiogenic seizures; human MASS1 S2652X in one febrile/afebrile
  seizure family (incomplete penetrance). [PMID:12402266] -> GO:0050877 nervous system process
  IMP (KEEP_AS_NON_CORE).
- Developmental CNS expression (ventricular zone). [PMID:11606593 "Strong expression in the
  ventricular zone, home of neural progenitor cells ... suggests a fundamental role for VLGR1
  in the development of the central nervous system."] -> GO:0007399 nervous system development
  NAS (KEEP_AS_NON_CORE).

## Over-annotations flagged

- GO:0005737 cytoplasm (IBA is_active_in; IEA located_in) -> MARK_AS_OVER_ANNOTATED (plasma
  membrane / stereocilium receptor). The IDA cytoplasm (PMID:16434480) -> UNDECIDED (abstract
  only cache; full-text evidence not verifiable, membrane/ciliary localizations described).
- GO:0098609 cell-cell adhesion (NAS PMID:11606593) -> MARK_AS_OVER_ANNOTATED: based on 2002
  sponge-aggregation-factor sequence-similarity speculation. [PMID:11606593 "Similar repeats
  are found in the extracellular aggregation factor of marine sponges, which mediates
  species-specific cell aggregation."] ADGRV1's real adhesion is intracellular membrane links
  (ankle links between stereocilia of one cell; periciliary membrane links), not cell-cell.
- GO:0050793 regulation of developmental process (ARBA) -> MARK_AS_OVER_ANNOTATED (vague).
- Root/general terms MODIFY to specific: GO:0007154 cell communication -> GO:0007186;
  GO:0032991 complex -> GO:1990696 USH2 complex; GO:0048513 animal organ development ->
  GO:0048839 inner ear development.

## Notes on evidence access

- Full text cached (full_text_available: true): PMID:14740321, PMID:20440071, PMID:23382219,
  PMID:25406310.
- Abstract-only cache: 10976914, 11606593, 12402266, 15203201, 15671307, 16434480, 19056867.
  Did not REMOVE any experimental annotation on abstract-level doubt (per policy); used
  UNDECIDED for the one experimental (IDA) annotation whose specific evidence I could not
  verify (GO:0005737 cytoplasm, PMID:16434480).
- PMID:23382219 (SNX17/27/31 PX-FERM): cached text does not name GPR98/ADGRV1; the GO:0043235
  IDA rests on screen/SI data I cannot inspect -> KEEP_AS_NON_CORE, deferring to curator.

## 2026-09-26 — substantive re-review and source-scope corrections

This session re-examined all 64 seeded assertions, the existing structural-molecule NEW
proposal, all reference findings and all three core functions. The preceding notes are
historical: the signaling, cytoplasm, developmental-regulation, bone-mineralization and
source-access conclusions below supersede the corresponding earlier statements.

### Identity, baseline and protected source material

- Approved symbol: ADGRV1, HGNC:17416. The official HGNC download archived in
  `projects/CLINGEN_MENDELIAN/hgnc-symbols.json` records previous symbols USH2C, MASS1 and
  GPR98, and aliases DKFZp761P0710, KIAA0686, FEB4 and VLGR1. Its official source is
  <https://storage.googleapis.com/public-download-files/hgnc/tsv/tsv/hgnc_complete_set.txt>,
  retrieved 2026-09-25T21:55:10.520502+00:00, source SHA256
  `3e5da5b757afce6cae333d3e6c97a59ff3aadfb13da1c70f89d9a8f252b9e7ec`.
  The live HGNC page supplied no gene content through the text reader; the archived
  official record and HGNC-linked UniProt/NCBI records supply the nomenclature check.
- Only `genes/human/ADGRV1` exists among the canonical and four historical/alias names.
  The coordinator independently recovered GitHub path history: seed commit
  `c05a1506c8376d13b60800aab67bb9336f8ddbe9` created ADGRV1 data; the later review was
  developed through PR #2953. No directory migration is required or invented.
- Baseline main was `af7a6ea1c9a6dd7ceecc8b04b120577d1a4070cb`; the local YAML, HTML,
  notes, GOA, UniProt and existing Falcon report matched its blobs. GitHub open-PR
  searches for ADGRV1 and for GPR98/VLGR1/USH2C/MASS1 returned no overlap before edits.
- The review was selected from available cached Definitive genes under the coordinator's
  temporary source-access scheduling exception; no shared project files were edited.
  All 65 annotation source objects remain identical, including original reference,
  evidence, qualifier and isoform fields. The 65th object is a pre-existing NEW proposal.
  Inert seeded qualifiers were preserved and were not used to change the biological
  meaning of localization or process assertions.

### Genuine research and cache outcomes

The existing genuine Falcon report and its artifacts were preserved. A new default
Falcon attempt with a 1,200-second timeout and the configured perplexity-lite fallback
ran concurrently with `just fetch-gene-pmids human ADGRV1`. Both research routes failed
before provider execution because uvx could not resolve PyPI while obtaining
`deep-research-client[cyberian]==0.2.7rc1` (exit 2; approximately 9.6 and 8.2 seconds).
No replacement provider report was created. The cache sweep found all 12 existing PMIDs
already cached. A normal `just fetch-pmid` attempt for PMID:24962568, PMID:35630584,
PMID:36139365, PMID:24191038 and PMID:22419726 failed DNS for every item (0/5 cached,
exit 1). These primary sources were independently read through web routes as described
below, but no publication file was fabricated or modified. The gene remains DRAFT
pending these five caches. Logs are `/tmp/ADGRV1-research-attempt.log`,
`/tmp/ADGRV1-publication-cache.log` and `/tmp/ADGRV1-additional-cache.log` in this session.

### Receptor signaling and cleavage: distinguish the actual constructs

- [PMID:24962568](https://pmc.ncbi.nlm.nih.gov/articles/PMC4148852/), primary full text
  accessed on 2026-09-26, tests mouse Vgain (GAIN plus transmembrane region) and isolated
  beta-subunit constructs, with cleavage mutants, hydroxylamine, PTX and G protein
  chimeras. It supports GPS self-processing and Gi-dependent suppression of cAMP. The
  less active comparator is Vgain, not the entire approximately 6,300-residue VLGR1b.
  Retinal transfection and cochlear fragment detection supplement the recombinant work.
- [PMID:35630584](https://pmc.ncbi.nlm.nih.gov/articles/PMC9146371/), indexed primary
  full text and Figure 2 read on 2026-09-26, assays human VLGR1a and CTF constructs.
  VLGR1a raises cAMP with increasing expression; chimeras and IP assays support Gq/Gi
  coupling in the appropriate construct contexts. The CTF signaling construct uses the
  P2Y12 N terminus to ensure surface expression. The study's full-length comparison is
  the shorter VLGR1a isoform, not VLGR1b. Gs and Gq are not mechanisms for the Gi-linked
  suppression of cyclase. Large interaction-network GO enrichments were not transferred
  wholesale into ADGRV1 functions.
- [PMID:24191038](https://pmc.ncbi.nlm.nih.gov/articles/PMC3839775/), indexed primary
  full results and figure legends read, provides Gs/Gq intracellular-domain pull-downs
  and calcium-dependent MAG stability experiments. Its mini-MASS1 contains four
  Calx-beta repeats according to the original Methods/Results; the later 2022 summary
  describes the earlier construct differently, so the primary study governs that detail.
  Cycloheximide chase and ubiquitylation assays support protein stability regulation.
  Frings oligodendrocytes have reduced MAG protein without a corresponding reported
  Mag mRNA reduction; the differentiation-marker comparison does not establish a
  generalized failure of oligodendrocyte differentiation. The link to seizure causation
  remains proposed. Calcium response and MAG stability remain non-core.
- The live [GO:0010855 definition](https://amigo.geneontology.org/amigo/term/GO:0010855)
  requires binding to and decreasing cyclase activity. The two inhibitor-MF rows retain
  MODIFY to GO:0007193 because the measured mechanism is receptor/Gi pathway signaling.
  This does not assert that all physical receptor–cyclase contacts are impossible.
- A newly located primary preprint, [Structural insights into the inactive state of the
  adhesion GPCR ADGRV1](https://www.biorxiv.org/content/10.64898/2026.03.05.709805v1),
  DOI 10.64898/2026.03.05.709805, posted 2026-03-07, was read through the author full-text
  copy at ResearchGate. It reports weak selective Gi activation of beta-subunit constructs
  under its conditions, no detected Gs/Gq response in the stated assays, and a nanobody-bound
  inactive structure. The examined Stachel mutations did not abolish Gi activity. It is
  a preprint, not a reason to reject the earlier positive assays or assert a universal
  mechanism. It is retained here as a bounded research lead; the curated core relies on
  the peer-reviewed primary studies and explicitly leaves native activation unresolved.

### Cytoplasmic and sensory compartments

- The live [GO:0005737 definition](https://amigo.geneontology.org/amigo/term/GO:0005737)
  includes subcellular structures and excludes plasma membrane and nucleus. It does not
  require a soluble protein. All three cytoplasm rows are now KEEP_AS_NON_CORE.
- The complete [PMID:16434480 author PDF](https://www.ag-wolfrum.bio.uni-mainz.de/files/2019/01/VanWijk_et_al_2006_Whirlin_Usher_Network_HumMolGen.pdf)
  was recovered late in this audit. Methods p. 762 specify human constructs. Figure 4
  maps binding of the VLGR1b cytoplasmic tail to WHRN PDZ1 and tests deletion of the
  terminal motif. Figure 5 assays the 150-residue tail in COS-1 cells: alone it occupies
  nucleus and cytoplasm; whirlin retains it cytoplasmically, dependent on the motif.
  This directly resolves the source of the 2006 cytoplasm IDA, with a fragment/overexpression
  limitation. Rat/mouse tissue immunolocalization is a separate experiment. The locally
  cached abstract remains unchanged; `full_text_unavailable` records that cache limitation,
  while the reference review explicitly documents successful external full-text access.
- [PMID:36139365 full publisher PDF](https://mdpi-res.com/d_attachment/cells/cells-11-02790/article_deploy/cells-11-02790.pdf?version=1662544865),
  sections 3.3–3.6 and Figure 3, was read. Human CTF is transfected in HEK293T for
  fractionation and HeLa for localization. Enrichment in ER/MAM fractions and ER-associated
  imaging support intracellular membrane pools. Endogenous immunoelectron microscopy uses
  pig and zebrafish photoreceptor inner segments; architecture/calcium perturbations use
  mouse cells. These are not endogenous intact-human-retina experiments. The calcium
  transfer assay is also distinct from sensing extracellular calcium in the 2013 study.
- The 2022 affinity-proteomics paper also reports perinuclear cytoplasmic staining in mouse
  astrocytes. Neither a receptor's membrane topology nor its sensory-cell surface localization
  excludes intracellular pools. No soluble cytosolic receptor or broad nuclear function is
  asserted, and no additional localization NEW is needed for the present audit.

### Structural participation, developmental scope and evidence gaps

- Cached full PMID:17567809 provides more than a loss-of-function phenotype: ectodomain
  immunolocalization tracks the ankle links temporally and spatially, and BAPTA/subtilisin
  remove both links and receptor staining. Retain the existing structural-molecule NEW
  proposal on that direct physical role; another gene's unaccepted NEW is not evidence.
  At postnatal day 7, excitatory current amplitude is reduced in outer but not inner hair
  cells; both types show abnormal reverse-direction responses. The core describes cohesive
  structural support and does not assign the receptor the transduction-channel pore.
- The same full paper reports failure of peripheral microvilli to regress and their
  differentiation toward stereocilia in mutants. This supports retaining broad regulation
  of developmental process as non-core, rather than denying a regulatory role categorically.
  Physical receptor/scaffold interactions and loss of partners from the stereocilia base
  also support core establishment of protein localization, without assigning motor activity.
- Cached full PMID:25406310 reconstructs the USH2 quaternary complex using mouse-derived
  fragments. Human PDZ interactions and disease/localization evidence support conservation,
  but the fragment study is not a measurement of intact endogenous human stoichiometry.
  Both generic-binding rows retain informative PDZ-domain-binding replacements.
- The complete [PMID:11606593 original](https://www.researchgate.net/publication/11743200_Very_Large_G_Protein-coupled_Receptor-1_the_Largest_Known_Cell_Surface_Protein_Is_Highly_Expressed_in_the_Developing_Central_Nervous_System)
  was read. Its discussion pp. 790–792 explicitly speculates about protein interactions,
  adhesion and neural development. Mouse embryonic expression supports the broad NAS neural
  context; it does not establish a cell-fate mechanism. The cell-cell adhesion NAS remains
  over-annotated because its source is a sponge-domain analogy without an ADGRV1 intercellular
  adhesion experiment. This is a source-specific judgment, not a claim of permanent absence
  of any intercellular function. The original 6,307-residue sequence is historical; current
  UniProt VLGR1b is 6,306 residues.
- The live [GO:0048496 definition/parents](https://amigo.geneontology.org/amigo/term/GO:0048496)
  concern organ identity under negative regulation of cell differentiation. Clinical
  photoreceptor loss and dysfunction in PMID:15671307 support the more precise maintenance
  term GO:0045494, without asserting a fate-conversion mechanism.
- [PMID:22419726 primary publisher abstract](https://academic.oup.com/jcem/article/97/4/E565/2833844)
  supports human/mouse bone-density effects and increased osteoblast Rankl/osteoclastogenic
  activity after mouse loss. Full text remains purchase-gated. Net mineral density does
  not distinguish deposition from resorption, so positive regulation of bone mineralization
  is UNDECIDED pending the complete experiment, not a denial of bone biology.
- PMID:23382219 has a misleadingly complete cache flag: target-specific Results/SI for the
  PX-FERM screen are absent from the extracted text and were not recovered externally.
  Its receptor-complex IDA is UNDECIDED. PMID:19056867's abstract establishes the urinary
  exosome survey but not the ADGRV1 accession/peptides; that HDA is also UNDECIDED. No
  target misattribution, contamination or shedding mechanism is inferred from these gaps.
- Propagation reviews record actual GOA sources. PAINT entries record ancestral PTNs only;
  target self-evidence is legitimate. Every curator ISS uses mouse Q8VHN7, while the Compara
  stereocilium row uses the preserved rat identifiers A0A096MK89/ENSRNOP00000068422. Rule
  internals and the exact rat donor experiment remain unresolved where not recovered;
  independent primary biology is distinguished from validation of those source records.

### Verification checkpoint

Annotation source objects and existing reference identifiers/titles were preserved exactly.
The author is the assigned annotation-reviewer consultation; the coordinator will independently
read the stable draft before publication. Targeted schema, ontology, quotation, history and
render checks are recorded in the session history and publication manifest when complete.
The five missing caches remain an explicit draft gate regardless of validation warnings.

Independent coordinator review read all 65 decisions, three cores and reference judgments.
The signaling core uses the generic GPCR signaling BP to cover the demonstrated coupling
contexts; the Gi-specific pathway remains the explicit replacement on the two inhibitor-MF
rows. PMID:23382219 retains `full_text_unavailable: false` because substantial full-text
sections are available; missing target Results/SI are recorded separately and still require
UNDECIDED. The coordinator found no other biological blocker.

Final targeted validation passed with the five missing-cache warnings grouped together and
an advisory that no annotation directly cites the existing Falcon report. Standalone schema,
all cached title/quotation checks, annotation-source integrity, history validation and HTML
rendering passed. Final actions: 41 ACCEPT, 11 KEEP_AS_NON_CORE, 8 MODIFY, 3 UNDECIDED,
1 MARK_AS_OVER_ANNOTATED and the retained structural NEW. The five missing caches remain
the draft gate; final file hashes and validation logs are in `/tmp/ADGRV1-audit-manifest.json`.

### 2026-09-27 — CI reference-title metadata correction

The CI reference fetch for PMID:36139365 recovered the machine title with
`Ca(2+)`, whereas the visible PubMed/publisher title renders a superscript.
Matched the YAML title exactly to the machine-fetched title reported by
CI run 36282024981; this changes neither the identifier nor any biological
assessment. PubMed confirms the same article and DOI (10.3390/cells11182790).
Normal local fetching still fails DNS, so the five required cache gaps remain
draft gates. CI also reported publisher-PDF HTTP 403 responses; external PDF
reading recorded above is separate from successful normal cache creation.

### 2026-09-27 — PR #3192 evidence-verifiability follow-up

The complete [review comment](https://github.com/ai4curation/ai-gene-review/pull/3192#issuecomment-5851472562)
was read against published head `676504ebc6d7997336569b87b00642f26cb61230`.
Local YAML, HTML and notes byte hashes matched that publication receipt before
editing. All 65 assertion source objects, including the 64 original assertions
and retained structural NEW proposal, and all 26 current reference identifier/title
pairs are preserved. The earlier title-correction record is unchanged.

A fresh supported `just fetch-pmid` attempt for PMID:22419726, PMID:24191038,
PMID:24962568, PMID:35630584 and PMID:36139365 returned exit 1 and cached 0/5.
Every attempt failed with `nodename nor servname provided, or not known`.
The complete log is `/tmp/ADGRV1-followup-fetch.log`. CI's earlier success reaching
PubMed metadata justified this retry, but does not establish successful retrieval
from this local runtime. No publication file was authored or modified manually.

The four open-access sources account for 28 quotation instances: 10 each from
PMID:24962568 and PMID:35630584, five from PMID:24191038 and three from
PMID:36139365. These now use `supporting_text`; the nonpublic-PDF exemption is
not appropriate simply because a normal fetch fails. They are **not yet
cache-validated**. The missing caches remain a publication gate, and future
normal retrieval must check these excerpts against the resulting text. The
PMID:36139365 excerpt now states the observed ER/MAM fraction result rather than
only that cells were fractionated. The separately sourced, abstract-only cached
PMID:16434480 still uses the full-text field for its externally read author PDF.

Primary identity and content checks remain distinct from cache availability:

- [PMC3839775](https://pmc.ncbi.nlm.nih.gov/articles/PMC3839775/) was read again;
  its metadata explicitly links PMID:24191038 and DOI 10.1073/pnas.1318501110.
  Figures 3 and 5 retain the mini-MASS1 degradation, calcium-response and
  G-alpha interaction scope.
- [PMC9146371](https://pmc.ncbi.nlm.nih.gov/articles/PMC9146371/) explicitly links
  PMID:35630584. Its [publisher PDF](https://mdpi-res.com/d_attachment/molecules/molecules-27-03108/article_deploy/molecules-27-03108.pdf?version=1652352248)
  was read again, especially section 2.2 and Figure 2. It reports the shorter
  VLGR1a and engineered CTF, not signaling by intact native VLGR1b.
- Indexed primary [PMC4148852](https://pmc.ncbi.nlm.nih.gov/articles/PMC4148852/)
  again exposed the Vgain/autoproteolysis Results. The original primary read
  established the PMID:24962568 linkage; intermittent challenge responses are
  recorded as current access limits, not as a reason to erase that verification.
- The [Cells publisher PDF](https://mdpi-res.com/d_attachment/cells/cells-11-02790/article_deploy/cells-11-02790.pdf?version=1662544865)
  was read again, including sections 3.3–3.4 and Figure 3. DOI 10.3390/cells11182790
  is the previously PubMed-verified PMID:36139365 article. The YAML retains the
  exact machine title with `Ca(2+)`; the earlier superscript rendering difference
  did not identify another paper.
- The original [JCEM publisher abstract](https://academic.oup.com/jcem/article/97/4/E565/2833844)
  read established PMID:22419726's identity and the limited bone-density findings.
  The exact mineralization experiment remains inaccessible, and its annotation
  stays UNDECIDED. VERIFIED here is a citation judgment, not a claim that the
  full experiment or positive mineral deposition was verified.

The description now states the isoform/coupling boundary compactly. The
GO:0048513 developmental replacement is GO:0060122 stereocilium organization,
matching the demonstrated structural contribution and the integrated core;
the broader existing inner-ear-development assertion remains non-core context.
The PDZ-docking core omits redundant visual perception while retaining
photoreceptor maintenance. Establishment of protein localization remains in
that core because physical tail docking supplies an anchoring contribution,
in addition to the mouse partner-mislocalization phenotype. It does not assign
ADGRV1 the myosin transport step. The cached PMID:17567809 support is attached
to the core as well as the assertion. Broad cytoplasm assertions remain at
their source resolution; fragment ER/MAM evidence supports this compartment
without making the source assertion erroneous or requiring a new localization.

The review remains DRAFT. The action counts are unchanged; all five source-cache
gaps must be resolved before the evidence-verifiability request can be closed.

The coordinator independently read the complete follow-up delta, including the
description, stereocilium replacement, GPCR/PDZ cores and all five changed source
assessments, and accepted the changes. The coordinator separately confirmed
preservation of source objects, actions and reference identities. No cache was
recovered. The standard gene validation and the resulting publication manifest
record this remaining limitation rather than treating field conversion as a
successful source fetch.

Validation outcome (2026-09-27 UTC): the existing standard `just validate human ADGRV1` run completed successfully, with two warning groups: unavailable publication caches and unused Falcon evidence. The normal retry recovered no caches. All five missing PMID cache gates therefore remain open, and the review remains DRAFT. Rendering, history validation, source-object and reference-identity preservation checks passed. The coordinator independently accepted the complete biological delta.


## 2026-09-27 normal publication-cache recovery

All five required records are recovered. PMID:35630584 (PMC9146371) and
PMID:36139365 (PMC9496679) contain XML full text; their local
`full_text_unavailable` flags are now false. Relevant construct Methods and
signaling or fractionation Results agree with the previously inspected primary
articles. Human VLGR1a and engineered CTF remain distinct from intact VLGR1b;
transfected human CTF localization remains distinct from endogenous retinal
experiments in other species. Existing full-text quotations for these two papers
are present in the caches.

PMID:22419726, PMID:24191038 and PMID:24962568 are abstract-only locally,
so their flags remain true. The bone-density abstract does not newly resolve
positive mineral deposition. The two signaling papers had previously been
read in full externally, and that provenance remains explicit. Their ordinary
supporting_text snippets that came from external Results are now replaced by
exact cached abstract sentences supporting the same Gi coupling, Gs/Gq-linked
calcium response and MAG stability claims. The external construct/assay details
remain in the unchanged reasons with access provenance in the source assessments.
No full-text exception field or fabricated cache was used.

The exact cache records originate from normal fetch output in Actions run
36286975328, head 5946477c8ac79ade0709264c775ea1262b108438, artifact
10920674630. The verified ZIP SHA-256 is
`c0ffe4a66b80278af34b44aab6a3ae354ffd5699236b3a486ca95527be5e9713`;
`tmp/verified-reference-records/local-import-receipt.json` records per-file
hashes. Only these five gene-required caches enter the closure manifest.

All 65 original source assertions, annotation actions and reasons, core
functions and their biological descriptions, 26 reference identities,
machine/provider files and previous history are preserved. Only evidence
attachments, source-access notes and status metadata are updated. This entry
supersedes earlier missing-cache status. Targeted validation, rendering and
history checks determine the final status and are recorded in the manifest;
any remaining advisory is distinguished from the now-closed cache gate.
