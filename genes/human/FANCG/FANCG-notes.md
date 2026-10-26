# FANCG (O15287, XRCC9) — review notes

## Identity / overview
- Human Fanconi anemia group G protein; 622 aa; gene = FANCG, synonym XRCC9; chr 9p13.
- TPR-repeat protein (UniProt lists TPR 1–4 at 246–279, 344–377, 453–486, 514–547; InterPro FANCG + FANCG_N; Gene3D TPR domain). No catalytic domain; α-helical solenoid scaffold. Cryo-EM structures of the human FA core complex include FANCG (PDB 7KZP/7KZQ/… chains G/H).
- Subunit of the multisubunit FA core complex (FANCA, FANCB, FANCC, FANCE, FANCF, FANCG, FANCL/PHF9, FANCM + FAAP20/FAAP100/FAAP24). The core complex is an E3 ubiquitin ligase (FANCL = catalytic RING) that monoubiquitinates the FANCD2–FANCI (ID2) heterodimer during S-phase interstrand crosslink (ICL) repair.

## Key functional evidence (with provenance)

- XRCC9 = complementing gene for MMC-hypersensitive CHO UV40; corrects chromosomal instability and mutagen sensitivity. [PMID:9256465 "We cloned and sequenced a human cDNA, designated XRCC9 , that partially corrected the hypersensitivity of UV40 to mitomycin C, cisplatin, ethyl methanesulfonate, UV, and γ-radiation"] and [PMID:9256465 "XRCC9 is a candidate tumor suppressor gene that might operate in a postreplication repair or a cell cycle checkpoint function"]. Note: 1997 paper could not assign a pathway ("no similarity with known proteins").

- FANCG is the FA complementation group G gene, identical to XRCC9. [PMID:9806548 "we report the identification of the gene mutated in group G, FANCG ... We identified the gene as human XRCC9"].

- FANCG is a component of a functional nuclear FA complex with FANCA and FANCC (Garcia-Higuera 1999, PMID:10373536, cited in UniProt). FANCG binds FANCA directly and strongly by Y2H. [PMID:10627486 "Using the yeast 2-hybrid system and full-length cDNA, the authors found a strong interaction between FANCA and FANCG proteins"].

- FANCF forms a nuclear complex with FANCA, FANCC and FANCG; each FA protein (except FANCD) required for complex formation → multiprotein nuclear FA complex maintains genomic integrity. [PMID:11063725 "FANCF was found predominantly in the nucleus, where it complexes with FANCA, FANCC and FANCG"] and [PMID:11063725 "a model in which a multi-protein FA complex serves a nuclear function to maintain genomic integrity"].

- FA core complex is required for DNA damage recognition at a stalled fork and monoubiquitinates FANCD2/FANCI; FANCG is one of the eight core subunits. [PMID:22266823 "Eight of the FA proteins comprise the FA core complex, a multisubunit complex required for DNA damage recognition at a stalled replication fork ... the complex, an E3 ligase, monoubiquitinates the FANCD2/FANCI heterodimer"]. FANCG specifically required for error-prone TLS/point mutagenesis: [PMID:22266823 "FANCA-deficient and FANCG-deficient cells exhibited a decrease in spontaneous and DNA damage-inducible point mutagenesis"].

- FA pathway (ubiquitinated FANCI–FANCD2) required for replication-coupled ICL repair in S phase. [PMID:19965384 "FANCI-FANCD2 is required for replication-coupled ICL repair in S phase"] (used to support ICL-repair BP; FANCG is upstream core-complex subunit needed for that monoubiquitination).

- FA core complex membership / chromatin loading (FAAP20 papers, FANCM-MHF, Rev1): [PMID:22343915 "FAAP20 is an integral component of the FA nuclear core complex ... required for DNA-damage-induced chromatin loading of FANCA and the functional integrity of the FA pathway"]. FANCM-MHF associates with the FA core complex and promotes FANCD2 monoubiquitination [PMID:20347428 "FANCM-MHF associates with the Fanconi anemia (FA) core complex, promotes FANCD2 monoubiquitination in response to DNA damage"]. FAAP20 links RNF8 ubiquitin signaling to the FA core complex [PMID:22705371 "a ubiquitin signaling cascade initiated by RNF8 ... and mediated by FAAP20, a component of the FA core complex"].

## Secondary / likely non-core roles
- Phospho-Ser7-dependent complex with BRCA2(FANCD1), FANCD2, XRCC3 (distinct from core complex). UniProt: "When phosphorylated at Ser-7, forms a complex with BRCA2, FANCD2 and XRCC3" (PMID:18212739). Ser7Ala abolishes BRCA2/FANCD2/XRCC3 binding but not FANCA/FANCF core-complex binding. Links FANCG to homologous-recombination machinery; not the canonical core-complex activity → treat as non-core.
- Mitochondrial/oxidative-stress role: FANCG interacts with mitochondrial peroxiredoxin-3 (PRDX3) and a fraction localizes to mitochondria; FA-G cells show distorted mitochondria and reduced mitochondrial peroxidase activity. [PMID:17060495 "the FA group G (FANCG) protein is found in mitochondria. Wild-type but not G546R mutant FANCG physically interacts with the mitochondrial peroxidase peroxiredoxin-3 (PRDX3)"] and [PMID:17060495 "FA-G cells demonstrate distorted mitochondrial structures"]. Real, experimentally supported, but a minor moonlighting/secondary role secondary to the nuclear ICL-repair function → KEEP_AS_NON_CORE (mitochondrion, mitochondrion organization, PRDX3 binding).
- αII-spectrin (SPTAN1) SH3-domain interaction via an SH3-binding motif in FANCG [PMID:19102630 "FANCG interacted with ... the SH3 domain ... The site of interaction in FANCG was mapped to a motif that binds to SH3 domains"] — specific but non-core scaffold interaction.

## Historical molecular-function interpretation — superseded

The following two blocks retain the starting review for provenance. Their absolute DNA-binding statement, screen-over-annotation policy and old action summary are superseded by the dated source reassessments, integrated review and follow-up below.
- FANCG has NO known enzymatic/DNA-binding activity of its own. Within the FA core complex, DNA/branched-structure binding is via FANCM-MHF and the E3 catalysis via FANCL. FANCG is a TPR α-solenoid that acts as a protein-protein adaptor/scaffold: it binds FANCA directly and is required for assembly, stability and nuclear accumulation of the core complex.
- Therefore the GOA MF "damaged DNA binding" (TAS, PMID:9806548, source PINC/ProtInc — an old low-quality mapping; the 9806548 abstract makes no DNA-binding claim) is best read as a complex-level property mis-attributed to the FANCG subunit → over-annotation.
- "protein binding" (GO:0005515) IPI rows: the FANCA/FANCF rows are biologically central but the term is uninformative → keep as non-core. Rows from large binary-interactome / neurodegeneration-aggregation / host-pathogen screens (VIM, GFAP, CYP3A4, RAB5A, SUOX, tax, etc.) are non-specific → over-annotated.

## Historical action-summary rationale — superseded
- Core: FA nuclear complex (CC), interstrand cross-link repair (BP), DNA damage response (BP), DNA repair (BP), chromatin/nucleoplasm/nucleus locations. 
- Non-core: cytoplasm/cytosol (minor form), nuclear speck, mitochondrion + mitochondrion organization + PRDX3 binding, spectrin/other specific PPIs.
- Over-annotated: damaged DNA binding (MF), high-throughput/aggregation/host-pathogen protein-binding rows.


## Historical scoped assessments retained below

The next two dated entries describe the separately sealed source assessments before integration; their counts and preserved-field statements are historical. The integrated disposition follows them.


## 2026-10-25 — FANCG direct-source reassessment

See the [FANCG source guide](FANCG-source-guide.md) for current biological interpretation and public source locators. The 55 current direct contexts have individual recommendations (8 ACCEPT, 31 MODIFY, 15 KEEP_AS_NON_CORE, 1 UNDECIDED). They map to 28 inherited imported rows. The two old grouped screen assertions retain non-core binding as a whole while the identified current partners have separate, evidence-specific refinements; machine-source adoption is a later explicit step, not an automatic reset.

The inherited IPI scaffold proposal is refined from GO:0030674 to GO:0140378 using the current ontology's explicit distinction and human assembly evidence. The inherited HR ISS proposal remains uncertain while retaining positive chicken recombination/rescue, human/hamster complex association and the original quotations. Failed human rescue in chicken is not evidence of human functional loss. A retained ISS interpretation remains a reasoned alternative. The prior characterization of both HR papers as chicken-only is superseded by the actual human/hamster experiments in PMID:18212739.

Actual PMID:17060495 Figures 2–4 support a mitochondrial pool, PRDX3 association, protection against calpain cleavage and partial morphology rescue, without assigning FANCG peroxidase activity or direct calpain inhibition. The damaged-DNA-binding TAS remains unresolved because the operative PMID:9806548 experiment was inaccessible; the historical absolute assertion that FANCG has no DNA-binding activity is not adopted as a current conclusion. Existing description/core are intentionally retained for separate synthesis, including their obsolete adaptor/fixed-core wording; their presence is historical rather than new scientific endorsement.

All 49 inherited source positions, 57 exact quotation/path/reference associations, 42 original reference identities/findings/availability-field presence, products, and 19 unassigned database reviews remain unchanged. Twenty-six whole manual reference assessments retain their previous notes verbatim and append current reading boundaries; genuine PMID:15262960 is added without quotation. Its normal source is protected FANCF intake reuse. No normal cache was edited or fetched in this task. All 26 original PMID availability flags were absent and remain absent, independently of normal metadata or external access.

Original reading, current ontology responses, literal table/IntAct records, raw failures and the exact legacy/current mapping are pinned in the private evidence packet. No new annotation row, core function, status, source adoption or canonical history was created here. The old source groups, all original quotes and prior notes remain available for the subsequent combined synthesis.


## 2026-10-25 — Database-source evidence reassessment

The database-derived contexts were reassessed against actual phylogeny, donor experiments, target-specific Reactome routes, HPA images and current rule mappings. See the [authored source-access guide](FANCG-source-guide.md) for public original locators and exact limits. The nineteen decisions retain sixteen core assertions and three contextual locations (cytoplasm, modeled PKR-associated cytosol, and HPA nuclear speckles). They do not alter the separately reviewed direct contexts or inherited authored proposals.

PANTHER v19 places the exact 622-residue target beneath both relevant IBDs. Mouse Q9EQR6/MGI:1926471 is traced to PMID:11719385 and PMID:11823446. Selected original 2001 Methods/Results/Figure 5 support crosslink and bounded radiation responses; the 2002 abstract reports no X-ray response in its MEFs. These preparation-specific results preserve broad DNA-damage-response scope rather than collapsing all evidence to ICL repair. The self-WITH human complex assertion is legitimate.

Human PMID:11063725 fractionation and immunoprecipitation, plus PMID:22343915 nuclear purification and FANCG chromatin Results, support a nuclear assembly pool. Broad nucleus is retained alongside specific compartments. Cytoplasm is not reduced universally to cytosol, and tagged mitochondrial experiments are not treated as natural-product equivalence. Each Reactome location is traced to FANCG's own entity/compartment, with FANCL/UBE2T, nuclease, polymerase, deubiquitinase and kinase roles kept distinct.

HPA006695's antigen exactly matches residues 123–260; actual selected HeLa/U2OS images show nuclear puncta. The source-supported nuclear-speck location remains positive and non-core without implying that repair occurs at the puncta. InterPro provides a FANCG-specific family mapping. Current ARBA output was verified, but the exact historical condition match remains unresolved; independent biology supports the retained term.

All inherited quotation paths, text and reference associations remain unchanged under the standing instruction to add no new publication quotations. Two missing donor publications were acquired through genuine fetches with preimages protected. Cache metadata, external original access and actual selected reading are explicitly distinguished. The old description/core/status and unowned reviews are preserved pending their separate synthesis or integration.


## 2026-10-25 — Integrated FANCG sources and core synthesis

The [whole-gene source guide](FANCG-source-guide.md) now combines the accepted target-study and database evidence. All 74 genuine current imported contexts are represented once, at the 47 original imported positions plus 27 appended partner contexts. Old grouped positions 9, 10, 18 and 19 retain representative contexts; position 19 now carries the FANCA interaction, and the other NeuroNet partners append. The complete prior grouped source/review objects and exact source mapping are preserved in the integration lineage proof. All 57 inherited quotation/path/reference associations stay at their original positions, including the four core quotations.

The authored scaffold assertion at position 23 is refined to GO:0140378/action NEW on scientific grounds. The separate authored HR assertion at position 48 remains UNDECIDED and is retired as curator withdrawal of our unresolved specific human proposal. Positive conserved evidence, human/hamster association, original ISS provenance and quotations remain visible; this is not biological negation, GO withdrawal or removal of an imported annotation. There are 76 records in total and 75 active records (74 imported plus one authored scaffold proposal).

One scaffold core replaces the old adaptor wording. Complex-only contribution to ubiquitin ligase activity is retained while explicitly assigning transfer to FANCL/UBE2T. ICL repair is the specific BP facet; broad DNA damage response remains supported in annotations and prose but is not a redundant core ancestor. Nuclear location encompasses both chromatin-associated and other nuclear pools. The new standalone description removes the absolute no-DNA-binding statement and fixed eight-subunit/FANCM–FAAP24 composition. Questions and experiments address direct DNA/positioning roles, human HR mechanism and PRDX3 protection without asserting new activities.

Six whole reference unions retain the historical note once and both exact new read scopes. PMID:22266823 is MEDIUM relevance for pathway context and its actual negative G-specific pairwise result. Explicit database availability flags fill prior unspecified fields only when they match selected immutable cache metadata; other absences remain. Original 42 identities/findings and all source quotations are preserved, with four genuine additional references and 46 final references. The 53-record normal union has no conflicting bytes and no new integration-stage fetches. Status is DRAFT; unresolved science and ordinary advisories are not hidden by a COMPLETE status.

## 2026-10-25 — Canonical validation

All six canonical checks pass, including current GOA matching, term/component validation and rendering of 160 narratives. Computed status is DRAFT with 14 advisories: 13 supported generic-binding advisories retained under the standing campaign instruction and one advisory for the unused inherited research file. Review all 74 current imported contexts and retain the inherited scaffold proposal with a more precise molecular function. Explicitly retire the earlier authored human homologous-recombination proposal while preserving positive nonhuman and complex-level evidence and its inherited quotations. One active annotation remains UNDECIDED. Adopt genuine current GOA while preserving all 49 inherited positions and 57 quotation associations. Keep 46 references and one scaffold core; no natural alternative product is inferred from transcript models or engineered constructs. Existing UniProt, publication/Reactome/family caches, provider outputs, prior history, generated HTML and unrelated work remain exact. New publication files are genuine additive fetches; no new quotation field is authored.

## 2026-10-26 — Review-feedback follow-up proposal

Thirteen screen-only partner-class replacements are withdrawn while their positive imported interactions remain KEEP_AS_NON_CORE under the project instruction. The Tax context retains its specific binding refinement because PMID:22458338 includes pairwise retesting plus human-cell reporter and knockdown follow-up; screen-wide validation rates are not assigned to individual pairs. Scaffold, mapped spectrin-SH3 and PRDX3 refinements remain supported by their separate evidence.

The inherited GO_REF:0000052 title quote is preserved as method provenance and is explicitly not treated as FANCG experimental evidence. Chromatin is restored alongside nucleus in the structural core, supported by PMID:22343915 Figure 5H and accompanying Results. The redundant authored scaffold proposal at position 23 is retired without deleting its source object or quotes; imported-row scaffold replacements remain active. Both authored positions 23 and 48 are retained as retired records, leaving all 74 imported contexts active. All 57 quotation paths/text/reference associations and machine-source fields remain unchanged.

Canonical validation of this follow-up: All six canonical checks pass and all 160 narratives render. Computed status is DRAFT with 27 advisories: 26 supported generic-binding records under the explicit project instruction and the unused inherited research file. All 74 imported contexts, 57 quotation/path/reference associations and 46 reference objects remain intact. The two retired authored rows remain historical records; normal sources, prior history and unrelated work remain unchanged.
