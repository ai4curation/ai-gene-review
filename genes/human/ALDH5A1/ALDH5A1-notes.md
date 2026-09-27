# ALDH5A1 (SSADH) review notes

The historical decision summary below is superseded by the 2026-09-27 audit appended
at the end, particularly the NAD(P)+ parent-term, glutamate-pathway, homotetramer and
clinical-source assessments.

UniProtKB: P51649 (SSDH_HUMAN). HGNC:408. EC 1.2.1.24. 535 aa precursor with an
N-terminal mitochondrial transit peptide (1..47); mature chain 48..535.

## Core biology
ALDH5A1 encodes **succinate-semialdehyde dehydrogenase, mitochondrial (SSADH)**, the
NAD+-dependent enzyme catalysing the **final step of GABA degradation** (the GABA shunt):
oxidation of **succinate semialdehyde -> succinate**, which then enters the TCA cycle,
routing GABA carbon into central energy metabolism.

- Catalytic activity (UniProt/Rhea RHEA:13217): succinate semialdehyde + NAD(+) + H2O =
  succinate + NADH + 2 H(+); EC 1.2.1.24 [file:human/ALDH5A1/ALDH5A1-uniprot.txt].
- "Mitochondrial NAD(+)-dependent succinic semialdehyde dehydrogenase (ALDH5A1, SSADH)
  represents the last enzyme in the GABA catabolism and irreversibly oxidizes SSA to
  succinate" [PMID:12208142].
- "Succinic semialdehyde dehydrogenase (SSADH) is involved in the final degradation step
  of the inhibitory neurotransmitter gamma-aminobutyric acid by converting succinic
  semialdehyde to succinic acid in the mitochondrial matrix" [PMID:19300440].
- Homotetramer of identical subunits [PMID:16199352; UniProt SUBUNIT].
- Km(SSA) 6.3 uM, Km(NAD+) 125 uM; recombinant enzyme characterised [PMID:16199352].
- Redox-regulated via a reversible Cys340-Cys342 disulfide on a dynamic catalytic loop;
  inhibited under oxidizing conditions / by H2O2 [PMID:19300440].
- Member of the aldehyde dehydrogenase superfamily [PMID:7814412].

## Localization
Mitochondrion / mitochondrial matrix. TransitPeptide 1..47. UniProt subcellular location:
Mitochondrion. Reactome places the reaction in the mitochondrial matrix (R-HSA-888548).
Confirmed by IDA (HPA), HDA/HTP proteomics (PMID:20833797 muscle mito phosphoproteome;
PMID:34800366 MitoCoP high-confidence mito proteome), and IBA.

## Disease
SSADH deficiency (SSADHD; MIM:271980) = 4-hydroxybutyric (gamma-hydroxybutyric, GHB)
aciduria. Autosomal recessive; accumulation of GABA and GHB; developmental delay,
hypotonia, intellectual disability, ataxia, seizures, behavioural disturbance
[PMID:9683595, PMID:12208142, PMID:14635103, PMID:15037717].

## Annotation review decisions (summary)
- MF GO:0004777 succinate-semialdehyde dehydrogenase (NAD+) activity: CORE. Multiple EXP
  (12208142, 14635103, 19300440), IDA (16199352, 9683595), ISS, IEA, IBA all converge.
  All ACCEPT.
- MF GO:0009013 succinate-semialdehyde dehydrogenase [NAD(P)+] activity (IEA/InterPro):
  human enzyme is NAD+-specific (name, EC 1.2.1.24, kinetics). NAD(P)+ term is broader/
  the bacterial (EC 1.2.1.16) flavour. MARK_AS_OVER_ANNOTATED (not wrong at family level
  but less precise than the NAD+-specific term).
- MF GO:0016491 oxidoreductase activity (IEA): correct but generic parent of GO:0004777.
  MARK_AS_OVER_ANNOTATED.
- MF GO:0042802 identical protein binding (IPI, 16199352): supported (homotetramer) but
  bare binding term; per policy do not REMOVE experimental IPI -> KEEP_AS_NON_CORE.
- BP GO:0009450 GABA catabolic process: CORE. IBA + IDA (9683595). ACCEPT.
- BP GO:0006540 GABA shunt (IMP, 15037717): correct process; ACCEPT (arguably the more
  informative pathway term). 15037717 is a case report of SSADHD showing GABA/GHB
  accumulation, supporting the pathway role.
- BP GO:0006105 succinate metabolic process (ISS): product is succinate; correct but
  broad/generic vs the GABA catabolic framing. KEEP_AS_NON_CORE.
- BP GO:0006536 glutamate metabolic process (ISS): weaker — glutamate is upstream of GABA
  (glutamate -> GABA via GAD), not a direct substrate/product of SSADH. The ISS is a
  transfer from mouse ortholog. MARK_AS_OVER_ANNOTATED (indirect at best).
- BP GO:0007417 central nervous system development (IMP, 9683595): 9683595 identifies
  splicing mutations causing SSADHD; the neurological disease phenotype is a downstream
  consequence of loss of GABA catabolism, not evidence that SSADH drives CNS development.
  This is a pleiotropic/disease-derived process. KEEP_AS_NON_CORE (do not REMOVE an
  experimental IMP whose full text we cannot read).
- CC GO:0005739 mitochondrion (IBA, IEA, IDA/HPA, HDA, HTP) and GO:0005759 mitochondrial
  matrix (TAS Reactome): all ACCEPT; matrix is the more precise, correct location.

## 2026-09-27 full substantive audit

Approved HGNC:408 symbol ALDH5A1, UniProt P51649, aliases SSADH/SSDH were checked.
The five canonical files matched main `ba3ff58d7d2de76dbe3c24b16e05e12369f463fc`;
canonical and alias PR searches and alias-directory checks found no overlap. The
25 original annotation source objects, two alternative products, 16 original
reference identities, GOA and UniProt are preserved. The completed decisions are
22 ACCEPT, two MODIFY and one KEEP_AS_NON_CORE, with no NEW annotation. Four donor
references were added and all 20 references manually assessed.

### Catalysis, assembly and pathway scope

- Human brain cDNA yields active recombinant SSADH in bacteria, with NAD+ and SSA
  kinetic measurements and an apparent homotetramer [PMID:16199352]. The specific
  catalytic function remains GO:0004777. Identical-protein binding is ACCEPT as
  enzyme assembly integrated into the one catalytic core, not a separate generic
  interaction function.
- The live [GO:0009013 definition and children](https://amigo.geneontology.org/amigo/term/GO:0009013)
  encompass NAD+ and NADP+ enzymes; the parent does not require both cofactors in
  one protein. MODIFY to the measured NAD+-dependent activity improves specificity
  without claiming an unread NADP+ negative assay. Generic GO:0016491 is refined
  by the same positive substrate/cofactor evidence. These replace the historical
  overannotation judgments.
- The live [GABA-shunt definition and parents](https://amigo.geneontology.org/amigo/term/GO:0006540)
  explicitly connect glutamate, GABA, SSA and succinate. GO:0006540 is an is_a child
  of both GO:0006536 and GO:0006105. SSADH executes a step in that pathway and
  directly produces succinate; both broader process annotations are therefore
  accepted as core. Immediate glutamate binding or catalysis is not required for
  this pathway membership.
- The patient MRS study [PMID:15037717] corroborates altered GABA/GHB metabolism;
  it does not itself measure purified SSADH chemistry. Human enzymology supplies
  that independent participation evidence [PMID:12208142; PMID:16199352].
- The 2003 variant abstract explicitly reports one exception to the below-5%
  activity statement for missense alleles considered disease-causing and describes
  other variants without strong activity effects [PMID:14635103]. That qualification
  is retained throughout. Transcript polyadenylation results [PMID:12208142] do not
  establish catalytic equivalence of all protein isoforms.

### Primary source resolution and limitations

The original [PMID:19300440 full Results/Methods](https://pmc.ncbi.nlm.nih.gov/articles/PMC2670868/)
were recovered through indexed primary PMC text although direct opens were challenged.
SSA is the substrate in the ligand complex; only the ADP portion of soaked NAD+ is
resolved. The structures are not a succinate-product complex or evidence of an ADP
cofactor. NADH-formation assays support catalysis. The oxidant/reductant work includes
recombinant protein and overexpressing HEK293 cells followed by lysate measurements;
quantitative control of endogenous neural GABA flux remains an open question. Crystal
assembly and the biochemical tetramer observation support oligomerization, while
disease-mutant assembly effects inferred from structure are not direct measurements.
The local publication remains abstract-only.

The full original [PMID:9683595 institutional PDF](https://art.torvergata.it/retrieve/e291c0d3-7a76-cddb-e053-3a05fe0aa144/Chambliss_AJHG_1998.pdf)
was independently read by the annotation-reviewer peer and this author. Human
recombinant GST-SSADH, patient/relative cell activity and splice-genotype segregation
support enzyme identity. Clinical developmental/speech delay grounds the existing
non-core developmental association; the paper does not assay a CNS morphogenetic or
differentiation step. Its discussion reports no established residual-activity/GHB-to-
clinical-severity correlation. Historical ALDH4A1 allele labels here denote SSADH,
not the modern ALDH4A1 protein. The short full-text quotation in row 22 was checked
against page 407 and is stored as `supporting_text_fulltext`; the cache stays unchanged.

PMID:7814412 experimentally validates rat cDNA through bacterial activity and purified
rat-brain sequence, alongside human partial cDNA and sequence comparisons. The ISS
donor is rat P51650. Later human expression studies independently establish the
conserved reaction; the rat expression experiment is not relabeled as human.

All nine original GOA PMID caches were read. Local full-text flags follow machine
cache availability: seven are abstract-only, while PMID:20833797 and PMID:34800366
have full-text metadata. The former extraction actually contains abstract/Discussion
and omits important experimental sections/tables. The latter main article was read,
but neither individual ALDH5A1 supplementary identification was re-extracted. Both
curated mitochondrial annotations are accepted with independent human localization
support, without inferring contamination or unmeasured submitochondrial resolution.
GO_REF:0000052 verifies the immunofluorescence curation method; its original antibody
images were not independently re-scored. Matrix localization in the integrated core
is independently supported by the human literature and cached Reactome R-HSA-888548.

### Propagation provenance

The cached PTHR43353 PAINT records identify PTN008681047 for SSADH activity/GABA
catabolism and PTN000192583 for mitochondrial localization. These are ancestral IBD
assertions, not a count of similar extant proteins. Human experimental descendants
are valid ancestral grounding; no circularity or function loss is inferred. The full
historical tree/MSA was not reconstructed. Twelve propagation blocks record all
proximate sources, with rule predicates left UNRESOLVED where not inspected.

Mouse Q8BWF0 is Aldh5a1 (MGI:MGI:2441982). The cached GO-CAM
`gocams/68d5ebd600002976/68d5ebd600002976-src.yaml` models SSADH catalysis and GABA-shunt
participation with IMP [PMID:11544478] and matrix context with IDA [PMID:14651853].
The model supplies a positive pathway role rather than a gap warranting NEW.

The [MGI donor graph](https://www.informatics.jax.org/marker/gograph/MGI:2441982)
is labeled generated 2023-03-10; it is a historical source snapshot, not a fresh GOA
export. [MouseMine](https://www.mousemine.org/mousemine/keywordSearchResults.do?searchTerm=Aldh5a1)
resolves its reference IDs: J:125589 is PMID:12065715 for succinate-process IMP,
J:128716 is PMID:17854388 for glutamate-process IMP, and J:86816 is PMID:14651853 for
mitochondrial evidence. J identifiers are not PMIDs.

- [PMID:12065715 primary abstract](https://pubmed.ncbi.nlm.nih.gov/12065715/) describes
  mouse treatment, survival and GABA/GHB responses. A donor succinate-flux assay was
  not resolved; direct human product formation independently grounds acceptance.
- [PMID:17854388 primary abstract](https://pubmed.ncbi.nlm.nih.gov/17854388/) describes
  mouse cortical isotope labeling and metabolite changes. These are system-level
  pathway observations, not direct glutamate catalysis. Its introductory NADP wording
  is not used to assign human cofactor specificity; direct human NAD+ kinetics are
  the relevant evidence.
- [PMID:11544478 primary Nature record](https://www.nature.com/articles/ng727z)
  and indexed original-paper excerpts verify the knockout/rescue citation used in
  the mouse model. The whole paper was not recovered.
- The cached PMID:14651853 abstract establishes mouse organelle-proteomics scope;
  the individual Aldh5a1 peptide record was not recovered. Human compartment evidence
  independently supports transfer.

### Research execution and cache gates

One genuine Falcon request with automatic perplexity-lite fallback was launched
concurrently with standard GOA-publication caching, using isolated writable temporary
UV directories. Both providers failed during dependency retrieval from PyPI due to
DNS errors before provider contact; no provider artifact was produced or authored.
Logs: `/tmp/ALDH5A1-fresh-research.log` and `/tmp/ALDH5A1-fetch-goa.log` (9/9 original
PMIDs already cached). This is a manual primary-source review.

The three newly traced donor PMIDs 11544478, 17854388 and 12065715 were submitted to
the normal fetcher; `/tmp/ALDH5A1-donor-fetch.log` records DNS failures and 0/3 cached.
They remain required cache gates for a future recovery batch. PMID:14651853 was already cached. No cache
was manually fabricated or edited. Status is DRAFT until the required sources and
validation warnings are resolved. The notes-inclusive authored PMID set is the nine
original publications plus these four donor papers; there are no provider-only PMIDs.

The parent independently reviewed every annotation, reference assessment, core and
question and found no biological blocker. Source preservation and all 43 cached
supporting snippets were independently checked with case-sensitive whitespace
normalization. The clinical full-text excerpt was checked against the institutional
PDF, page 407. No action was changed merely to eliminate a validation warning.
