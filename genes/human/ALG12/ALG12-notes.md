# ALG12 (human, Q9BV10) review notes

## Summary of function

ALG12 is an ER membrane, ER-lumenal-facing alpha-1,6-mannosyltransferase (glycosyltransferase
family GT22; CAZy GT22, Pfam PF03901 Glyco_transf_22) of the dolichol-linked oligosaccharide
(LLO) assembly pathway for protein N-glycosylation. It transfers the **eighth mannose** from
**dolichyl-phosphate-mannose (Dol-P-Man)** in an alpha-1,6 linkage onto Man7GlcNAc2-PP-dolichol
to give Man8GlcNAc2-PP-dolichol (EC 2.4.1.260; RHEA:29535). The lumenal mannose additions of LLO
assembly use Dol-P-Man as donor, not GDP-Man.

- [UniProt Q9BV10 FUNCTION, "In the lumen of the endoplasmic reticulum, adds the eighth mannose residue in an alpha-1,6 linkage onto Man(7)GlcNAc(2)-PP-dolichol to produce Man(8)GlcNAc(2)-PP-dolichol."]
- [UniProt Q9BV10 SUBCELLULAR LOCATION "Endoplasmic reticulum membrane"; "Multi-pass membrane protein" — 12 predicted TM helices]
- [UniProt Q9BV10 SIMILARITY "Belongs to the glycosyltransferase 22 family."]

## Disease

Loss of ALG12 mannosyltransferase activity causes **ALG12-CDG / congenital disorder of
glycosylation type Ig (CDG-Ig, MIM:607143)**, a multisystem disorder with under-glycosylated
serum glycoproteins, psychomotor/developmental retardation, hypotonia, dysmorphism,
immunodeficiency.

## Key references (all abstract-only in cache; quotes verbatim from abstracts)

- **PMID:11983712** (Chantret et al 2002, J Biol Chem) — identified human ALG12 as ortholog of
  yeast ALG12 encoding the dolichyl-P-Man:Man7GlcNAc2-PP-dolichyl alpha6-mannosyltransferase;
  CDG-Ig patient fibroblasts "deficient in their capacity to add the eighth mannose residue onto
  the lipid-linked oligosaccharide precursor"; homozygous F142V; WT rescue. Establishes MF, BP,
  and disease. Basis of the EXP/IMP/IDA annotations.
- **PMID:12093361** (Thiel et al 2002, Biochem J) — "Deficiency of the endoplasmic reticulum
  enzyme dolichyl-phosphate mannose (Dol-P-Man):Man(7)GlcNAc(2)-PP-dolichyl mannosyltransferase";
  reduced activity, Man7GlcNAc2-PP-Dol accumulation; L158P + C-terminal truncation; WT rescue.
- **PMID:12217961** (Grubenmann et al 2002, Hum Mol Genet) — "a deficiency in the ALG12 ER
  alpha1,6-mannosyltransferase"; ER/lumenal localization inference; yeast alg12 complementation;
  T67M and R146Q. Basis of the IC (lumenal side of ER membrane) and NAS (ER; protein folding)
  annotations.
- **PMID:19946888** (Ghosh et al 2010, J Mass Spectrom) — NK-cell membrane proteome MS study
  (1843 proteins); basis of HDA "membrane" annotation. Generic membrane localization only.

## Annotation decisions (high level)

- Core MF: GO:0052917 (dol-P-Man:Man(7)GlcNAc(2)-PP-Dol alpha-1,6-mannosyltransferase activity) —
  EXP/IMP ACCEPT (core). Exact GOA current term (EC 2.4.1.260).
- GO:0000009 (alpha-1,6-mannosyltransferase activity, IBA) ACCEPT — correct but less specific
  than GO:0052917.
- GO:0000030 (mannosyltransferase activity, TAS Reactome x2) MODIFY -> GO:0052917 (too general).
- GO:0016757 (glycosyltransferase activity, IEA InterPro) ACCEPT as correct-but-broad parent.
- Core BP: GO:0006488 (dolichol-linked oligosaccharide biosynthetic process) IMP/IDA/TAS and
  GO:0006487 (protein N-linked glycosylation) IBA/IMP — ACCEPT (core).
- Core CC: GO:0005789 (ER membrane) IBA/IEA/TAS — ACCEPT. GO:0098553 (lumenal side of ER
  membrane, IC) ACCEPT (more specific, correct topology). GO:0005783 (ER, NAS) ACCEPT as broader.
- GO:0016020 (membrane, HDA PMID:19946888) MARK_AS_OVER_ANNOTATED — uninformative generic
  membrane from a proteome survey; ER membrane is the specific term.
- GO:0006457 (protein folding, NAS PMID:12217961) — MARK_AS_OVER_ANNOTATED. ALG12 does not fold
  proteins; N-glycosylation is upstream of/supports folding but "protein folding" mis-describes
  the molecular role. Downstream/indirect.

## 2026-09-27 full annotation audit

This dated section supersedes the earlier decision summary above. All 23 seeded
annotations and 12 original reference identities were reviewed; the final file
contains 18 ACCEPT, four MODIFY and one UNDECIDED decisions, no NEW rows, 13
reference assessments and one integrated catalytic core. The previous two cores
represented the same reaction in related processes and are consolidated. All
source term/evidence/reference/qualifier fields are preserved. No new process term
is asserted: both LLO biosynthesis and protein N-linked glycosylation were already
seeded and represented in the prior cores.

### Identity, baseline and research provenance

Human ALG12 is HGNC:19358 / UniProtKB:Q9BV10; CDG1G and ECM39 are aliases. The root
preflight verified all five canonical files against main
`ba3ff58d7d2de76dbe3c24b16e05e12369f463fc`, with no canonical/alias directory or open-PR
conflict (three separate open-PR searches, 2026-09-27 05:18 UTC). The baseline was
INITIALIZED despite prior author decisions. The original GOA, UniProt record,
reference identities and annotation source objects remain unchanged.

The default Falcon research launch with `--fallback perplexity-lite --timeout 1200`
ran concurrently with `fetch-gene-pmids`. The first launch incorrectly inherited
offline dependency mode; an online retry using the supported `/tmp` UV tool/cache
directories failed DNS while resolving `deep-research-client` from PyPI. Both
providers failed before research execution. Logs: `/tmp/ALG12-deep-research.log`
and `/tmp/ALG12-deep-research-online.log`. No generated provider report exists and
none was authored manually. Publication caching succeeded for all four seeded
PMIDs (`/tmp/ALG12-fetch-goa.log`). The normal new-source fetch of PMID:41807832
failed DNS, cached 0/1 and exited 1 (`/tmp/ALG12-fetch-new.log`); this is the sole
missing required PMID in the YAML/notes census. It is reserved for future recovery,
not added to an already frozen recovery batch. The review stays DRAFT.

### Primary evidence and access limits

- **PMID:11983712**, Chantret et al. Human F142V patient fibroblasts accumulate
  truncated lipid-linked glycans. The original Results/Figure 5 compares GFP-only
  with human wild-type ALG12 transduction in immortalized patient fibroblasts and
  shows restoration of mature LLO. Figure 6 separately follows transfer of truncated
  glycans to proteins and their reglucosylation; UGGT performs the reglucosylation.
  This is positive direct precursor-pathway evidence, not an ALG12 folding assay.
  [PubMed](https://pubmed.ncbi.nlm.nih.gov/11983712/) establishes the identifier.
  The original article's Results/Figures 1, 5 and 6 were recovered from the
  [author-uploaded full primary text](https://www.researchgate.net/publication/11385482_Congenital_Disorders_of_Glycosylation_Type_Ig_Is_Defined_by_a_Deficiency_in_Dolichyl-P-mannoseMan7GlcNAc2-PP-dolichyl_Mannosyltransferase),
  DOI 10.1074/jbc.M203285200. The repository cache is still abstract-only. Cached
  result-bearing evidence: “the pathological phenotype of the fibroblasts of the
  patient was largely normalized upon transduction with the wild type gene”.
- **PMID:12093361**, Thiel et al. The independently checked
  [primary PMC record](https://pmc.ncbi.nlm.nih.gov/articles/PMC1222867/) and abstract
  report reduced patient-fibroblast enzyme activity, Man7 precursor accumulation
  and wild-type cDNA normalization. The patient's serum transferrin loses complete
  N-glycan chains, but the rescue experiment measures fibroblast enzyme activity;
  it is not a claim of treatment correcting circulating transferrin. The full PDF
  body was not recovered for independent assay-detail inspection. The positive
  abstract findings and concordant human source support ACCEPT with curator
  deference. The local cache is abstract-only.
- **PMID:12217961**, Grubenmann et al. The human patient glycan profiles, normal
  human cDNA rescue of yeast alg12 and failure of the tested human mutant alleles
  support the enzyme identity. The [original HMG article](https://academic.oup.com/hmg/article/11/19/2331/2355556)
  and [Paperity preview](https://paperity.org/p/40175018/alg12-mannosyltransferase-defect-in-congenital-disorder-of-glycosylation-type-lg)
  expose abstract/early original text, but the preview explicitly truncates before
  full Results/Discussion. Original PDF access failed/redirected to an abstract.
  An independent peer reader confirmed these limits. Protein-folding NAS is
  therefore UNDECIDED, replacing the prior categorical indirect-effect judgment.
  The membrane-facing location remains a curator inference, not an imagined
  microscopy assay. The local cache remains abstract-only.
- **PMID:19946888**: the [primary PubMed record](https://pubmed.ncbi.nlm.nih.gov/19946888/)
  describes membrane isolation and mass spectrometry in YTS NK-like cells. No
  ALG12-specific peptide table was recovered. Retain membrane HDA with curator
  deference and independent positive ALG12 membrane biology; preserve its broad
  source resolution. A specific ER annotation elsewhere does not invalidate the
  broad membrane result, and the number of proteins identified does not establish
  contamination. The prior OVER decision is superseded by ACCEPT.

All four local publication flags remain `full_text_unavailable: true`. External
article access and local-cache availability are distinct. Ordinary YAML evidence
snippets are taken from the unchanged local abstracts or protected UniProt/Reactome
records; no external paraphrase is presented as a cached quote.

### New structural study: construct and species boundaries

**PMID:41807832**, *Structures of ALG3/9/12 reveal the assembly logic of the N-glycan
oligomannose core*, DOI 10.1038/s41589-026-02164-7. Identifier/title linkage was
independently established through the [RCSB 9S6T primary deposition](https://www.rcsb.org/structure/9S6T),
which explicitly links the citation to this PMID, and the
[publisher primary article](https://www.nature.com/articles/s41589-026-02164-7).
The PubMed page itself intermittently returned a browser challenge. Full indexed
publisher Results were recovered with the query
`"s41589-026-02164-7" "GgALG12" "Results"`; the read included biochemical
characterization, pseudo-Michaelis complex preparation, C-branch initiation,
Figures 1/3/4 and Extended Data 1. The study uses **chicken GgALG12**, human HsALG9
and yeast ScALG3, expressed in HEK293 cells. Human expression host does not make
GgALG12 a human protein. Purified wild-type GgALG12 processes shortened Dol25-linked
substrates; E35Q facilitates substrate-bound structural analysis and has strongly
reduced activity. The study supports conserved substrate recognition, with the
human clinical variants mapped onto homologous chicken residues. These results
are ortholog evidence and do not establish human ALG12 topology experimentally.
The older human prediction of 12 transmembrane helices in the historical notes is
not equated with the new 11-helix chicken structural topology. The captured
Fab-containing particle does not establish a physiological ALG12 complex.

The missing normal cache remains explicit even though primary external evidence
was read; no new activity or process annotation is manufactured from this paper.

### Ontology, PAINT and GO-CAM checks

- Live [GO:0006457](https://amigo.geneontology.org/amigo/term/GO:0006457) describes
  assistance in covalent/noncovalent polypeptide assembly into tertiary structure.
  It is not restricted to classical chaperone catalysis. Its protein-maturation
  context does not by itself resolve the original ALG12 NAS evidence.
- Live [GO:0006488](https://amigo.geneontology.org/amigo/term/GO:0006488) describes
  formation of dolichol-linked oligosaccharides and is `part_of` protein N-linked
  glycosylation (GO:0006487). ALG12 catalyzes a chemical step of that precursor
  process. Both terms already occur in the source review; their inclusion is
  synthesis of established participation, not a proposed missing process.
- Live [GO:0098553](https://amigo.geneontology.org/amigo/term/GO:0098553) includes
  proteins embedded in or attached to the ER membrane's lumen-facing leaflet and
  is `part_of` ER membrane. It fits the site of the lipid-linked reaction.
- GO:0052917 is the existing donor/acceptor-specific MF used in the source review
  and the GO-CAM. RHEA:29535 / EC:2.4.1.260 and the human studies identify the same
  reaction. Live AmiGO retrieval of the full MF definition repeatedly timed out;
  QuickGO returned only its JavaScript shell. No obsolescence or relabeling claim
  is made from these access failures. The authoritative seeded term identity is
  retained for validation. The installed OAK `sqlite:obo:go` snapshot was also read: GO:0052917
  resolves to the exact Man7-to-Man8/Dol-P-Man reaction and has alpha-1,6-mannosyltransferase
  activity as a parent; GO:0000009 in turn has mannosyltransferase activity as a parent.
  This is explicitly a local ontology check, not a successful live API response.
- `interpro/panther/PTHR22760/PTHR22760-paint.tsv` contains the ER-membrane IBD at
  **PTN000509188**, and alpha-1,6-mannosyltransferase/N-glycosylation IBDs at
  **PTN000509189**. Structured propagation blocks name the ancestral nodes only.
  Human ALG12 evidence among the descendants is legitimate target grounding; no
  donor-count or self-circularity argument is used. The InterPro and linkage-specific PAINT assertions are biologically true; target-level
  human substrate evidence nevertheless supports MODIFY to the exact MF. This
  granularity refinement neither disputes PAINT node placement nor assigns exact
  substrate specificity to every family descendant. The two reaction-specific
  Reactome MF rows are likewise refined to the chemistry those events resolve.
- `gocams/65c57c3400000687/65c57c3400000687-src.yaml`, activity
  `65d7e4ac00000341`, places Q9BV10 with MF GO:0052917, `occurs_in` GO:0098553
  (IC from the same original HMG source), and `part_of` GO:0006488 (patient-study
  evidence). This is explicit concordant curation, not independent replication.
- Cached Reactome R-HSA-446198 specifies the normal eighth-mannose transfer and ER
  lumen. Disease event R-HSA-4720497 describes the normal reaction before impaired
  variants; refining its generic MF does not assert normal mutant activity or
  alter the original reference. The parent R-HSA-446193 summary has a localized
  wording error about three terminal GlcNAcs: the mature precursor has **three
  glucoses**, as the human record and primary sources establish.

No new flat annotations, core biological processes, complex memberships or
speculative oligomerization functions are introduced. No custom bioinformatics
analysis was needed. Validation, history and exact source-preservation results
are recorded in the companion session history and publication manifest.

The coordinator independently read all 23 decisions, 13 reference assessments,
description, integrated core and questions. Its requested two target-specific MF
refinements were incorporated before final validation; all other biology was accepted.


## 2026-09-27 — source7 structural record and current-head review

PR #3281 was independently confirmed open at `9ecf454e6b7d57cc293e86d7baa37b5f6f493cb1`; all five canonical gene files matched that exact published tree before editing. Formal review 5329506875 and detailed [comment 5854097618](https://github.com/ai4curation/ai-gene-review/pull/3281#issuecomment-5854097618) were read completely. The coordinator imported the unchanged normal-fetch publication from source7 run `36299519155`, source head `583c2ac3b65ce1f7f9808c7b10c53e25f322129a`, artifact `10927941174` (ZIP SHA256 `a07af3765c6f8fa1aea780c1a6a4a6f71a561a75d1a29b6c9d334018618fa4b3`). The canonical PMID:41807832 record matches the source7 receipt: 217251 bytes, SHA256 `28fe1eafb0c6ae0b3040c3675f4fc47c0deffe1c7c65a5ad209120dc9faa0af8`. No publication text was edited or synthesized.

The complete cached Results, Methods and figure captions were now read. Methods specify GgALG12 accession F1P077, HsALG9 isoform 1 and ScALG3, codon-optimized and expressed in human 293 c18 cells; GgALG12 is still chicken protein. Wild-type GgALG12 catalyzes transfer on the synthetic Dol25-linked Man7 acceptor. The E35Q construct has strongly decreased activity and permits the pseudo-Michaelis complex; the structure uses Fab/nanobody aids. The chicken 11-transmembrane-helix topology is not substituted for an experimentally established human topology, and the imaging assembly is not a physiological complex annotation. The newly attached exact findings make species and construct scope inspectable in YAML. The primary metadata confirms the previous publisher/RCSB verification, so VERIFIED is retained. Local fetch DNS failure never demonstrated an invalid identifier; the earlier failed access history remains intact and this dated recovery supersedes its cache gate.

Both broad membrane and ER rows remain ACCEPT, with clearer positive core-location reasons. A multipass ER enzyme's membrane association and ER location are core compartments even when a source reports a broader resolution than the core summary. Omission of an ancestor location from the compact core list is not evidence for peripheral biology. The membrane-proteomics hit still relies on explicit curator deference plus independent positive membrane biology; the unrecovered target peptide table is not claimed to have been read.

All four optional reviewer points were assessed. (1) Protein-folding NAS remains UNDECIDED because the relevant original full Results/Discussion are not recovered; precursor assembly alone does not establish a separate folding step, but it also does not prove that the source could not support one. The new structural paper's pathway context does not resolve the old NAS source. (2) The two broad family/linkage MF refinements remain target-level MODIFYs using established human donor/acceptor chemistry. They do not rewrite an InterPro-wide map or the PAINT ancestral IBD; the explicit source comments retain that distinction. An older ALG9 decision does not override the rule to refine a general MF when target specificity is established. (3) The source-specific reason now anchors its rescue claim to the cached abstract; the independently read Figure 5 GFP-control detail remains in these notes with its original external access route. (4) The core process list is reduced to the precise GO:0006488 precursor-assembly process. The already seeded broader protein N-linked glycosylation rows remain valid: the established precursor pathway is part of that broader process. No NEW annotation or source-field change is involved.

All 23 source assertions, original reference identities and alternative products are preserved; all actions are unchanged. Prior provider attempts remain documented and no provider report was generated. The recursive authored PMID/decoded DOI/Reactome census, exact quotes, source preservation, history validation and rendering are checked. COMPLETE is used only if final validation has no warnings. This section records current source recovery without rewriting historical missing-cache statements.


## 2026-09-27 — membrane source resolution and folding context

Formal review 5330018783 and its complete [comment 5855216392](https://github.com/ai4curation/ai-gene-review/pull/3281#issuecomment-5855216392) were assessed against exact published head `ac323464585aeaf01ba4613a937cc65cae56d332`. Fresh remote checks matched all five canonical gene files before editing. All 23 source assertions, actions, qualifiers, original reference identities, alternative products and core terms remain unchanged.

The broad membrane HDA remains ACCEPT on positive biological grounds. Human ALG12 is an ER membrane enzyme acting on membrane-anchored donor and acceptor substrates. The [live membrane definition](https://amigo.geneontology.org/amigo/term/GO:0016020) covers the bilayer and its embedded or attached proteins; it does not denote a peripheral function. The proteomics screen reports membrane association and does not independently distinguish the ER or its lumenal face. Retaining that source resolution avoids claiming that the survey resolved a finer compartment. Its ALG12 peptide hit remains curator-reported, and the reference assessment now uses UNVERIFIED for that individual hit while explicitly retaining the verified bibliographic identity. Independent membrane evidence supports the existing annotation; no contamination or wrong-target claim is made. This reasoning supersedes any implication in the preceding sibling-review comparison that another gene's action label determines this gene's biology. Broad location accuracy and target-specific catalytic refinement are separate evidence judgments.

The protein-folding NAS remains UNDECIDED. The [live folding definition](https://amigo.geneontology.org/amigo/term/GO:0006457) concerns assistance in forming the correct polypeptide structure and is not restricted to classical chaperones. A new direct attempt to read the original [PMID:12217961 publisher PDF](https://academic.oup.com/hmg/article-pdf/11/19/2331/6947591/ddf229.pdf) failed at its redirected reader endpoint; the previously documented preview still does not provide the complete Results/Discussion. The actual cached [PMID:41807832] discussion names calnexin/calreticulin, glucosidases and UGGT in downstream quality control, whereas ALG12 builds the lipid-linked precursor. Its statement about complete B and C branches specifies **efficient** glucose removal/addition, not an absolute ban on processing a truncated glycan. This matters because [PMID:11983712] directly reports UGGT glucosylation of Man7 glycans in human ALG12-deficient fibroblasts. The added question and exact cached findings preserve that distinction without resolving an inaccessible original NAS statement by assumption.

Two additional exact findings attach the B-branch prerequisite and acceptor-cavity evidence from [PMID:41807832]. The measured and structurally characterized ALG12 is chicken GgALG12; human 293 c18 cells are the expression host. The ordering statement is pathway context, and the cavity is ortholog structural evidence. No new human structure, folding function, process annotation or complex membership is proposed. The InterPro and IBA molecular-function refinements remain specific to the human target supported by its own chemistry, not changes to all family members or the ancestral assertion.

The recursive authored-source census remains five PMIDs and three Reactome records with no provider artifact or new source gap. All cached source bytes and prior histories are unchanged. Targeted validation, the newly scaffolded history, exact quotes and rendering are checked before freezing this four-file follow-up.
