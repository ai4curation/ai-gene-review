# ACADS (human) review notes

UniProt: P16219 (ACADS_HUMAN). Short-chain specific acyl-CoA dehydrogenase, mitochondrial; SCAD; Butyryl-CoA dehydrogenase; EC 1.3.8.1. 412 aa precursor, mitochondrial transit peptide 1-24, mature chain 25-412. HGNC:90, gene on chr 12. NCBITaxon:9606.

## Core function

ACADS catalyzes the first, FAD-dependent step of mitochondrial fatty acid beta-oxidation for short-chain substrates: the alpha,beta-dehydrogenation of short-chain (C4-C6) acyl-CoA thioesters to the corresponding trans-2-enoyl-CoA, with electrons passed to electron-transfer flavoprotein (ETF). Optimum substrate butyryl-CoA (C4).

- UniProt FUNCTION: "Short-chain specific acyl-CoA dehydrogenase is one of the acyl-CoA dehydrogenases that catalyze the first step of mitochondrial fatty acid beta-oxidation... short-chain specific acyl-CoA dehydrogenase acts specifically on acyl-CoAs with saturated 4 to 6 carbons long primary chains (PubMed:11134486, PubMed:21237683)." [P16219 UniProt CC FUNCTION, ECO:0000269|PubMed:11134486, ECO:0000269|PubMed:21237683]
- EC 1.3.8.1 with ECO:0000269|PubMed:21237683. Catalytic activity entries (Rhea) for short-chain 2,3-saturated fatty acyl-CoA, butanoyl-CoA, pentanoyl-CoA, hexanoyl-CoA, all left-to-right.

[PMID:3597357 "Short chain acyl-CoA (SCA), medium chain acyl-CoA (MCA), and isovaleryl-CoA (IV) dehydrogenases were purified to homogeneity from human liver"] — original purification of human SCAD. Establishes homotetramer, FAD per subunit, ETF electron acceptor, butyryl-CoA -> crotonyl-CoA product.
[PMID:3597357 "The products of SCA dehydrogenase/butyryl-CoA, MCA dehydrogenase/octanoyl-CoA, and IV dehydrogenase/isovaleryl-CoA reactions were identified as crotonyl-CoA, 2-octenoyl-CoA, and 3-methylcrotonyl-CoA"] — direct evidence SCAD dehydrogenates butyryl-CoA to crotonyl-CoA.
[PMID:3597357 "indicating a homotetrameric structure"] and [PMID:3597357 "each contains 1 mol of FAD per subunit"] and [PMID:3597357 "They all utilized electron transfer flavoprotein (ETF) or phenazine methosulfate (PMS) as an electron acceptor"].

## Structure / cofactor / quaternary

- Homotetramer (UniProt SUBUNIT, ECO:0000269|Ref.10 = SGC crystal structure PDB 2VIG). Binds 1 FAD per subunit (UniProt COFACTOR Ref.10). FAD shared between dimeric partners. Active site proton acceptor Glu392 (ACT_SITE, by similarity to P15651).
- PDB structures: 2VIG (1.9 A, with FAD and substrate analog), 7Y0A, 7Y0B, 8SGS (EM).
- Belongs to acyl-CoA dehydrogenase family (InterPro IPR006089 etc.). CDD cd01158 SCAD_SBCAD.

## Localization

- Mitochondrion matrix (UniProt SUBCELLULAR LOCATION, ECO:0000250|UniProtKB:Q3ZBF6, soluble matrix protein). N-terminal mitochondrial transit peptide cleaved.
- GOA has mitochondrion (IDA MGI PMID:16729965; IDA HPA; HTP PMID:34800366), mitochondrial matrix (ISS, TAS Reactome), and a spurious nucleus (HDA PMID:21630459, sperm-nucleus proteomics — almost certainly contaminant; soluble matrix enzyme).
- Note: PMID:16729965 is the OCTN1-to-mitochondria paper (abstract is about OCTN1/SLC22A4, a carnitine transporter). The ACADS mitochondrion IDA from MGI cites this PMID; the curator (MGI) likely used ACADS as a mitochondrial marker/co-stain in that work — abstract-only here, so do not overrule; mitochondrial localization for ACADS is in any case strongly supported by all other evidence. Treat as ACCEPT (location is correct).
- PMID:34800366 (Morgenstern MitoCoP) high-confidence human mitochondrial proteome: [PMID:34800366 "We classified >8,000 proteins in mitochondrial preparations of human cells and defined a"] (abstract truncated at cache; mitochondrial classification). HTP mitochondrion = correct.
- Nucleus HDA from PMID:21630459 sperm nucleus proteome: [PMID:21630459 "403 different proteins have been identified from the isolated sperm nuclei. ... More than half (52.6%) of the proteins had not been detected in the previous human whole sperm cell proteome reports."] This is a large-scale dataset; ACADS as a mitochondrial matrix enzyme appearing in a sperm-nucleus prep is best explained as mitochondrial/cytoplasmic carryover. Mark over-annotated (HDA, no functional support for nuclear role).

## Disease

- Acyl-CoA dehydrogenase short-chain deficiency (ACADSD, MIM 201470): inborn error of mito FAO; acute acidosis and muscle weakness in infants, lipid-storage myopathy in adults; ethylmalonic aciduria. ECO:0000269|PubMed:11134486, PubMed:1692038, PubMed:9499414.
- Common susceptibility variants c.625G>A (R171W? actually 625G>A is a non-rare variant) and c.511C>T confer susceptibility to ethylmalonic aciduria. [PMID:11134486 "functional SCAD deficiency due to the presence of susceptibility SCAD gene variations, i.e. 625G>A and 511C>T"]
- PMID:11134486 characterized variants and the pathway: GOA uses it for IMP GO:0003995 (R171W has 69% WT activity, G209S 86%; several missense cause loss of acyl-CoA dehydrogenase activity per UniProt VARIANT notes, e.g. G90S, A192V, R325W, S353L, R380W "loss of acyl-CoA dehydrogenase activity"). And IC GO:0006635 fatty acid beta-oxidation (from MF GO:0003995).

## Annotation-by-annotation reasoning

MF terms:
- GO:0016937 short-chain fatty acyl-CoA dehydrogenase activity — CORE. Supported by EXP PMID:21237683 (EC characterization), ISS, IBA, IEA. This is the precise MF term. ACCEPT (EXP/IBA), the IEA/ISS duplicates ACCEPT/KEEP.
- GO:0003995 acyl-CoA dehydrogenase activity — parent term, correct but less specific than GO:0016937. IDA PMID:3597357 (purified human SCAD), IMP PMID:11134486, ISS, IEA, TAS PMID:2565344. ACCEPT the IDA/IMP (experimental, correct), the broad parent is fine but non-core given the more specific child.
- GO:0016627 oxidoreductase activity, acting on CH-CH group of donors — InterPro IEA, correct parent, KEEP_AS_NON_CORE (too general).
- GO:0050660 flavin adenine dinucleotide binding — IEA InterPro, correct (FAD cofactor, 1 per subunit). ACCEPT.
- GO:0070991 medium-chain fatty acyl-CoA dehydrogenase activity — IEA from RHEA:43464 (hexanoyl-CoA, C6). C6/hexanoyl is at the boundary; SCAD does act on C4-C6 (UniProt lists hexanoyl-CoA Rhea reaction with ECO:0000269|PubMed:21237683). Hexanoyl-CoA (C6) is conventionally "medium chain". This term is defensible as a minor/boundary activity but is not the core specificity (which is short-chain, optimum C4). KEEP_AS_NON_CORE — the C6 activity is real (UniProt catalytic activity hexanoyl-CoA, PubMed:21237683) but the enzyme is the short-chain ACAD; medium-chain is the boundary of its range, not its identity. Do not REMOVE (mechanically derived from a real UniProt-curated Rhea reaction).
- GO:0005515 protein binding (x2, IPI from BioPlex PMID:28514442 and PMID:33961781; WITH P16444 DPEP1) — high-throughput AP-MS interactome; DPEP1 is a membrane dipeptidase, not an obvious functional partner. Uninformative term; per guidelines do not endorse bare protein binding. MARK_AS_OVER_ANNOTATED (real HT interaction but uninformative; not core).

BP terms:
- GO:0006635 fatty acid beta-oxidation — IC PMID:11134486 and TAS PMID:8276399. CORE/ACCEPT. Mouse SCAD cloning paper (8276399) explicitly: [PMID:8276399 "Short-chain acyl-CoA dehydrogenase (SCAD) is one of five homologous dehydrogenases that catalyze the first reaction in the beta-oxidation of fatty acids."]
- GO:0033539 fatty acid beta-oxidation using acyl-CoA dehydrogenase — IBA + IEA. More specific BP capturing the ACAD-mediated step. ACCEPT (IBA).
- GO:0046359 butyrate catabolic process — IBA. ACADS optimum substrate is butyryl-CoA (C4). "Butyrate catabolic process" = breakdown of butyrate/butanoate. SCAD's dehydrogenation of butyryl-CoA is the committed step of butyryl-CoA/butanoyl-CoA catabolism. Defensible; KEEP_AS_NON_CORE (it is a substrate-specific framing of the same FAO step). ACCEPT/KEEP.

CC terms:
- GO:0005759 mitochondrial matrix — ISS (Q3ZBF6), TAS Reactome x2. CORE location. ACCEPT.
- GO:0005739 mitochondrion — IBA is_active_in, IEA, IDA HPA (GO_REF:0000052), IDA MGI PMID:16729965, HTP PMID:34800366. Correct but less specific than matrix. ACCEPT (parent of matrix).
- GO:0005634 nucleus — HDA PMID:21630459 (sperm nucleus proteome). MARK_AS_OVER_ANNOTATED (contaminant; matrix enzyme).

## References quality

- PMID:21237683 abstract foregrounds ACAD9/ACAD10/ACAD11 but UniProt cites it (ECO:0000269) for ACADS FUNCTION, catalytic activity and EC 1.3.8.1 — the full text characterized ACADS short-chain activity. Do NOT remove the EXP annotation. Abstract-only in cache (full_text_available: false).
- PMID:3597357 — purification of human liver SCAD/MCAD/IVD; directly supports SCAD enzymology. HIGH.
- PMID:11134486 — common ACADS variants, disease pathogenesis, function/catalytic activity/pathway. HIGH.
- PMID:2565344 — cDNA cloning of human SCAD; TAS GO:0003995. MEDIUM (sequence/identity, supports MF generically).
- PMID:8276399 — mouse SCAD cDNA; TAS GO:0006635. MEDIUM (ortholog; states SCAD catalyzes first beta-ox step).
- PMID:16729965 — OCTN1 mito paper; ACADS mito IDA by MGI. Abstract about OCTN1 (different gene); used as mito marker. LOW relevance to ACADS function, but location annotation is fine. full_text_unavailable.
- PMID:21630459 — sperm nucleus proteome; basis of nucleus HDA. LOW; likely contaminant.
- PMID:34800366 — MitoCoP; HTP mitochondrion. MEDIUM (confirms mito).
- PMID:28514442, PMID:33961781 — BioPlex interactome (protein binding, DPEP1). LOW; HT, uninformative term.

## Core functions to record

1. MF GO:0016937 short-chain fatty acyl-CoA dehydrogenase activity; directly_involved_in GO:0006635 fatty acid beta-oxidation (and GO:0033539); location GO:0005759 mitochondrial matrix. supported_by PMID:3597357, PMID:21237683/UniProt, PMID:11134486.

## 2026-09-26 substantive audit — current decisions supersede the earlier notes

### Baseline, identity and scope

Audited the existing COMPLETE review rather than reseeding its annotations. ACADS is the current HGNC:90 human symbol; SCAD and ACAD3 are aliases, NCBI Gene 35, UniProt P16219 ([NCBI](https://www.ncbi.nlm.nih.gov/gene/35), [HPA](https://www.proteinatlas.org/ENSG00000122971-ACADS)). The 30 seeded annotation objects are unchanged outside their `review` fields. No NEW annotations were added. Initial main comparison used commit `21121fc735d20bcb2dbf8328aa82d5da30185e5e`, YAML blob `6ddbc46d40388a92ed19c6e9cb00648c5ab9b2c2`; the local review matched it. Open PR searches for ACADS/SCAD/ACAD3 returned #2493 and #3105, but their complete file lists had no ACADS overlap. No Git state, shared project files, downloaded source files or publication caches were changed.

The original review had 14 ACCEPT, 13 KEEP_AS_NON_CORE and 3 MARK_AS_OVER_ANNOTATED. This audit has 18 ACCEPT, 8 MODIFY, 1 KEEP_AS_NON_CORE, 1 REMOVE and 2 UNDECIDED. The earlier statements here calling nucleus localization spurious or certainly contaminated, treating all broad terms as non-core, and labeling generic binding over-annotated are superseded.

### Research execution and source access

All ten cited PMIDs were already cached and were read for the scope relevant to each annotation. No publication refresh or cache rewriting was needed or performed. The required genuine research attempt was `just deep-research-falcon human ACADS --fallback perplexity-lite --timeout 1200`, using `UV_NO_SYNC=1`, `UV_CACHE_DIR=/tmp/aigr-uv-cache`, and `UV_TOOL_DIR=/tmp/aigr-uv-tools`. Both provider launches failed before invoking the provider: uvx could not resolve pypi.org to obtain deep-research-client. The Falcon dependency attempt exited 2 after three retries; the fallback also exited 2; the wrapper exited 1. No provider report was produced and no live provider process remained. An initial attempt without UV_TOOL_DIR first failed creating a temporary directory in the protected default tool directory; the corrected attempt used the writable /tmp runtime. There is no authored provider-named report.

Actual cache coverage matters more than its metadata. PMID:28514442 and PMID:34800366 contain full primary article text. PMID:33961781 is marked `full_text_available: true`, but the cached body has introductory/discussion material without complete methods/results or the ACADS-DPEP1 experimental record. The other seven PMID caches are abstract-only. Direct PMC opens for PMC3073726 and PMC8165030 returned browser challenges. Indexed primary PMC text did expose methods/results and SCAD comparison figure text for PMID:21237683; the publisher supplied only partial indexed sections for PMID:16729965. These are partial access routes, not claims to have recovered a complete paper or its supplements. Source caches remain intact.

### Enzymology, terms and core synthesis

[PMID:3597357](https://pubmed.ncbi.nlm.nih.gov/3597357/) reports purified human liver SCAD, measured butyryl-CoA conversion to crotonyl-CoA, ETF acceptance, homotetrameric structure and one FAD per subunit. These directly support the catalytic core; kinetic numbers not in the abstract were not reconstructed. The five broad GO:0003995 rows and the InterPro GO:0016627 row now MODIFY to GO:0016937, using human substrate evidence rather than claiming erroneous family membership or orthology.

The live [GO:0003995 entry](https://amigo.geneontology.org/amigo/term/GO%3A0003995) confirms that GO:0016937 is its child and that GO:0016627 is an ancestor. The [short-chain definition](https://zfin.org/GO:0016937) refers to the acyl chain and does not restrict the enzyme to straight-chain substrates. No branched-chain activity is rejected just from the term name. The [medium-chain entry](https://amigo.geneontology.org/amigo/term/GO%3A0070991) explicitly includes RHEA:43464, the hexanoyl-CoA reaction. This remains NON_CORE: it preserves the documented overlapping C6 activity without claiming the full ACADM substrate range. Reactome R-HSA-77327 and UniProt P16219 also record the ACADS hexanoyl-CoA reaction.

[PMID:21237683](https://pmc.ncbi.nlm.nih.gov/articles/PMC3073726/) concerns ACAD10/11 but includes SCAD comparison profiles and human liver matrix activity consistent with SCAD and MCAD. Indexed methods describe ETF reduction measurements; indexed Results section 3.6 and the activity figure text discuss the matrix comparison. Figure references differ between the indexed legend and text, so no unverified figure numbering or SCAD construct provenance is asserted. The EXP short-chain activity remains ACCEPT with independent human enzyme evidence; ACAD10/11 substrate measurements were not reassigned to ACADS.

GO:0033539 describes the beta-oxidation pathway that uses acyl-CoA dehydrogenase for its initial oxidation, not just a one-reaction process ([definition](https://zfin.org/GO:0033539)). ACADS performs that initial step within the pathway. The two broad GO:0006635 rows now MODIFY to this existing specific pathway term. GO:0046359 butyrate catabolism remains core because SCAD catalyzes a step on activated butyrate; it does not oxidize free butyrate. The cached `interpro/panther/PTHR43884/PTHR43884-paint.tsv` contains the relevant IBDs at PTN000097838 (activity and both processes) and PTN000856533 (mitochondrion). Neither the rat-only listed descendant for butyrate catabolism nor the presence of human ACADS among other IBA descendants constitutes weak support or circularity. Propagation reviews trace these actual nodes.

The core is one short-chain dehydrogenase activity, with matrix location, specific beta-oxidation and butyrate-catabolism participation. FAD binding remains an accepted annotation but is part of the same catalytic unit rather than a separate core function. The redundant general beta-oxidation ancestor was removed from the core list. The description no longer calls the oxidation the first committed pathway step, asserts a shared FAD geometry, or generalizes a historical selected patient series into universal clinical pathogenicity of common variants.

### Localization and interaction decisions

The five mitochondrial rows are ACCEPT at their original organelle-level resolution: PAINT IBA, ARBA IEA, HPA IDA, MitoCoP HTP and the PMID:16729965 IDA. Separate matrix annotations and the catalytic core preserve the more specific localization; that independent evidence is not used to upgrade these five source rows. HPA microscopy and the source studies do not by themselves resolve the matrix, and the PAINT node explicitly supports the organelle. [HPA ACADS](https://www.proteinatlas.org/ENSG00000122971-ACADS/subcellular) currently lists supported mitochondrial main localization, uncertain additional nucleoplasm/centrosome, and approved sperm-tail locations. None of the additional signals is manufactured into a NEW annotation. Matrix itself is a GO cellular compartment with fatty-acid oxidation enzymes in its definition ([GO:0005759](https://amigo.geneontology.org/amigo/term/GO%3A0005759?relation=isa_partof)).

[PMID:21630459](https://pubmed.ncbi.nlm.nih.gov/21630459/) reports nuclei isolated to over 99.9% purity and absence of mitochondria by light and electron microscopy. These stated controls do not justify the earlier contamination claim. The full study and ACADS-specific peptide data could not be inspected; the nuclear HDA is UNDECIDED. An uncertain HPA nucleoplasm signal does not independently settle sperm nuclear localization, and no nuclear biochemical function is inferred.

[PMID:16729965](https://www.sciencedirect.com/science/article/abs/pii/S0006291X06010254) foregrounds OCTN1. Its indexed abbreviation list explicitly includes SCAD, but the ACADS-specific experiment was not recovered. The earlier suggestion that SCAD was a mitochondrial marker is plausible but unverified, so it is no longer asserted as a fact. The mitochondrial annotation is ACCEPT at its original organelle-level resolution, with deference to the experimental curator and corroboration from independent localization evidence. The full cached MitoCoP study (PMID:34800366) describes a rigorous proteomics workflow, but the ACADS-specific supplemental record was not separately inspected; the article title is no longer used as a purported result-bearing quote.

For BioPlex 2.0 (PMID:28514442), the full cached primary methods describe tagged-bait AP-MS in HEK293T cells and co-complex associations. UniProt P16219 records DPEP1 as an interaction partner with two experiments, and the [reciprocal DPEP1 record](https://www.uniprot.org/uniprotkb/P16444-1/entry) lists ACADS. The generic binding annotation is REMOVE for lack of functional information, explicitly not because the association is false. The pair-specific supplement was not reanalyzed and no physiological interaction mechanism is inferred. For BioPlex 3.0 (PMID:33961781), the incomplete cache and unavailable partner record leave source-specific adjudication unresolved, so UNDECIDED replaces the invalid legacy over-annotation action.

### Other source-specific limits

PMID:11134486 reports a selected set of ten patients with ethylmalonic aciduria and variable or moderately reduced fibroblast SCAD activity. The IMP activity and IC pathway annotations are sound in substance and refined for specificity; the authors' historical common-variant risk interpretation is not universalized. PMID:2565344 is the human placental SCAD cDNA paper and supports gene/enzyme identity, not a newly claimed direct activity assay. PMID:8276399 explicitly studies mouse SCAD and supplies the pathway statement used by the TAS; it is not represented as a human experiment. Bovine ISS donor Q3ZBF6 was verified on the primary UniProt record as ACADS/SCAD. All machine-sourced annotation identifiers, labels, evidence types, references and flags were preserved.

### Validation outcome

`just validate human ACADS` passes with no curation warnings; `just render human ACADS` succeeds. Every source annotation field was compared with the saved baseline and is unchanged. YAML trailing whitespace was removed with parsed-YAML equality checked. The append-only history record was scaffolded with codex/gpt-6 metadata; parent independent review was requested before publication. Final publication scope is the review YAML, derived HTML, notes and this new history record only.

Parent independent review requested preserving the original evidence resolution of all five mitochondrial rows. This correction is incorporated above and in every affected row/reference assessment: these are ACCEPT, the two propagation assessments are NO_FAILURE_CORE, and the separate matrix annotations/core remain unchanged. Final action counts are 18 ACCEPT, 8 MODIFY, 1 KEEP_AS_NON_CORE, 1 REMOVE and 2 UNDECIDED.
