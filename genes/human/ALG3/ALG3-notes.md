# ALG3 (Q92685) review notes

## Summary of function

ALG3 is the human Dol-P-Man:Man(5)GlcNAc(2)-PP-dolichol alpha-1,3-mannosyltransferase
(EC 2.4.1.258), the enzyme catalysing the **first ER-lumenal step** of dolichol-linked
oligosaccharide (LLO) assembly for protein N-glycosylation.

- Assembly of the LLO begins on the **cytosolic face** of the ER membrane and finishes
  in the **lumen**. After Man5GlcNAc2-PP-dolichol is flipped to the lumenal face, ALG3
  transfers the **sixth mannose** (the first mannose derived from **dolichyl-phosphate-mannose,
  Dol-P-Man**, rather than GDP-Man) in an **alpha-1,3 linkage** onto Man5GlcNAc2-PP-Dol to
  give **Man6GlcNAc2-PP-dolichol**. The product is the substrate for ALG9, the next enzyme
  in the pathway [UniProt Q92685 FUNCTION; PMID:10581255].
- ALG3 is a **polytopic ER membrane protein** (11 predicted TM helices; UniProt features),
  member of the glycosyltransferase ALG3 family / CAZy GT58, active on the lumenal side of
  the ER membrane.
- It is the structural and functional orthologue of *S. cerevisiae* ALG3
  [PMID:10581255 "The mannosyltransferase is the structural and functional orthologue of the
  Saccharomyces cerevisiae ALG3 gene."].

## Disease

Deficiency causes **ALG3-CDG (congenital disorder of glycosylation type Id / CDG1D;
MIM:601110)**, originally described as CDGS type IV. Characterised by microcephaly,
severe epilepsy, minimal psychomotor development, dysmorphism, and partial deficiency of
sialic acids in serum glycoproteins; the defect causes accumulation of the
Man5GlcNAc2-PP-Dol intermediate and transfer of truncated oligosaccharides
[PMID:10581255; PMID:15840742]. Pathogenic variants include G118D and R171Q.

## Key references
- PMID:10581255 (Körner et al. 1999, EMBO J): identified ALG3 as the deficient
  mannosyltransferase in CDGS type IV; defines catalytic activity, pathway, subcellular
  location, and disease. Abstract-only in cache (full_text_available: false) but abstract
  is rich. This is the primary experimental reference for MF/BP/CC IDA/IC annotations.
- PMID:15840742 (Sun et al. 2005): CDG1D variant R171Q; clinical presentation.
- PMID:29547901 (Hacker et al. 2018, Hum Mol Genet): Y2H interactome of hNOT/ALG3;
  homodimers, and interactions with OSBP, OSBPL9, LRP1, SYPL1, CREB3. Abstract-only.
  Provides functional context for the IntAct protein-binding annotations. 33% identity
  with yeast ALG3.

## Annotation review decisions

GOA MF term = **GO:0052925** (dol-P-Man:Man(5)GlcNAc(2)-PP-Dol alpha-1,3-mannosyltransferase
activity) — this is the specific, correct current MF; used in IBA, IEA(EC/RHEA), and IDA.

- Core MF: GO:0052925 (IDA PMID:10581255, plus IBA and EC/RHEA IEA) — ACCEPT.
- GO:0000030 mannosyltransferase activity (IEA InterPro) and GO:0000033
  alpha-1,3-mannosyltransferase activity (TAS Reactome): correct but **less specific**
  parents of GO:0052925 -> MODIFY to GO:0052925 (over-general MF).
- Core BP: GO:0006488 dolichol-linked oligosaccharide biosynthetic process (IDA + TAS) and
  GO:0006487 protein N-linked glycosylation (IDA + IEA) — ACCEPT.
- GO:0009101 glycoprotein biosynthetic process (IBA): correct but broad parent of
  GO:0006487 -> KEEP_AS_NON_CORE (acceptable broader IBA).
- Core CC: GO:0005789 endoplasmic reticulum membrane (IDA + IEA + TAS) — ACCEPT;
  GO:0098553 lumenal side of ER membrane (IC) — ACCEPT (precise topology).
  GO:0005783 endoplasmic reticulum (IBA) — KEEP_AS_NON_CORE (broader parent of ER membrane).
- GO:0005515 protein binding (IPI x11 across 5 interactome papers): bare, uninformative
  MF from high-throughput screens -> MARK_AS_OVER_ANNOTATED (per policy, not REMOVE).

## 2026-09-27 substantive review (supersedes the earlier action summary)

Baseline and scope: HGNC:23056 / Q92685 / ALG3, approved aliases CDGS4,
D16Ertd36e, NOT56L and Not56. The root coordinator verified all five canonical
files against main ba3ff58d7d2de76dbe3c24b16e05e12369f463fc and separately checked
all five open-PR searches and alias directories. A subsequent comparison to main
9a41b2b3b426ab112d2b3256540aed3d43307bc0 showed no scope changes. This review
preserves every source field of all **22 seeded annotations**, both alternative
products and all 15 original reference identities. There were **zero prior NEW
rows**, despite the earlier task estimate. The final review has 14 ACCEPT,
3 MODIFY and 5 REMOVE decisions, 20 assessed references and one integrated core.
The historical note's “IPI x11” counts source interactions, whereas the seeded
review has five collapsed source-paper binding rows.

Research provenance: the genuine default Falcon launch used the supported
writable UV tool/cache directories, --fallback perplexity-lite and a 1200-second
timeout. Both provider paths failed during dependency resolution because PyPI
DNS was unavailable, before a provider report was produced
(`/tmp/ALG3-deep-research.log`). No provider output has been authored. The parallel
normal GOA publication fetch found all six seeded PMIDs cached
(`/tmp/ALG3-fetch-goa.log`, exit 0). Manual primary-source research below supplies
the review; it does not replace missing machine caches.

### Original human enzyme evidence and the leaky disease allele

[PMID:10581255](https://pubmed.ncbi.nlm.nih.gov/10581255/), DOI
[10.1093/emboj/18.23.6816](https://doi.org/10.1093/emboj/18.23.6816), was verified
against PubMed/PMC1171744. The complete original seven-page article was read from
an [author-uploaded PDF](https://www.researchgate.net/profile/Christian-Koerner-3/publication/12720543_Carbohydrate_deficient_glycoprotein_syndrome_type_IV_deficiency_of_dolichyl-P-ManMan5_GlcNAc2-PP-dolichyl_mannosyltransferase/links/00b7d530367db2b608000000/Carbohydrate-deficient-glycoprotein-syndrome-type-IV-deficiency-of-dolichyl-P-ManMan5-GlcNAc2-PP-dolichyl-mannosyltransferase.pdf).
Figures 4-5 and Methods distinguish normal Dol-P-Man synthesis from impaired
mannose transfer onto supplied Man5GlcNAc2-PP-Dol in patient fibroblast microsomal
extracts. These are membrane enzyme assays with donor/acceptor controls, not a
purified-human-protein kinetic experiment. Figures 8-9 test normal and G118D
human cDNA complementation in yeast alg3 cells. Patient glycan profiles and the
mutant complementation retain some complete precursors: the Discussion on
page 6820 explicitly describes reduced rather than abolished activity. The old
review's complete-loss claim is corrected. The exact cached abstract also states
“due to its leaky nature, a residual formation of full-length LLOs.”

The original membrane assay and multipass sequence/ER retrieval discussion
support the ER context; no independent immunofluorescence experiment is claimed
from this paper. The lumenal face is the curator's biochemical inference and is
also positively recorded in the reaction pathway. The local publication remains
abstract-only; external access does not alter its protected metadata.

[PMID:15840742](https://pubmed.ncbi.nlm.nih.gov/15840742/) was already cited in the
historical notes. The primary abstract identifies the intended human ALG3-CDG
study and reports correction of patient-fibroblast biochemistry after wild-type
ALG3 lentiviral expression. Its endocrine presentation supplies clinical context,
not an additional ALG3 endocrine function. The normal cache fetch failed DNS
(`/tmp/ALG3-fetch-new.log`).

### Interactions, processing and their functional limits

The full original [PMID:29547901 article](https://academic.oup.com/hmg/article/27/11/1858/4935075)
was recovered through indexed publisher text and an
[author-uploaded full-text copy](https://www.researchgate.net/publication/323831280_Molecular_partners_of_hNOTALG3_the_human_counterpart_of_the_Drosophila_NOT_and_yeast_ALG3_gene_suggest_its_involvement_in_distinct_cellular_processes_relevant_to_congenital_disorders_of_glycosylation_).
Results/Figures 3-5 and Methods identify stable human HEK293 transfectants,
reciprocal co-IP of ALG3 with the CREB3 precursor, and partner-specific processed
ALG3 species in other human-cell assays. The Discussion presents a prerequisite
for CREB3 processing as an interpretation of precursor-selective binding. It
does not resolve ALG3 as a protease or demonstrate an adaptor bridge. Homodimer
and partner associations remain positive findings; the five generic binding rows
are REMOVE under the uninformative-term policy, not because the interactions
are disproven. No NEW signaling process or separate homodimer assertion is added.

A related original [PMID:30192950 study](https://pubmed.ncbi.nlm.nih.gov/30192950/)
was read through its [author-uploaded full text](https://www.researchgate.net/publication/327535556_Sequential_cleavage_of_the_proteins_encoded_by_HNOTALG3_the_human_counterpart_of_the_Drosophila_NOT_and_yeast_ALG3_gene_results_in_products_acting_in_distinct_cellular_compartments),
including Figure 2, Results, Discussion and Methods. HT-29/SKBR3 fractionation
and antibodies against different regions identify processed species in ER,
cytosolic and nuclear fractions. Individual cleavage sites and some topology
interpretations additionally rely on predictions. The work asks which species
are active and questions the catalytic assignment; it does not directly refute
mannose transfer. The controlled 1999 microsomal experiment and human-cDNA
complementation remain positive evidence. The separate processing observations
are retained as context and an expert question, without mapping the paper's
transcript nomenclature to UniProt isoforms by assumption or assigning an
unmeasured nuclear molecular activity. Normal fetch failed DNS
(`/tmp/ALG3-fetch-isoform.log`).

The four interaction-survey sources were also assessed individually:

- [PMID:21516116](https://pubmed.ncbi.nlm.nih.gov/21516116/): cached primary
  Methods/Results establish Stitch-seq followed by pairwise Y2H retesting from
  fresh transformants. This is positive validation, not a reason to dismiss a
  large-scale dataset.
- [PMID:25910212](https://pubmed.ncbi.nlm.nih.gov/25910212/): source identity and
  variant-interaction design verified; the local full-text extraction contains
  Introduction/Discussion but omits full Results/Methods and the precise ALG3
  experiment. Its metadata still says full text available, so the review flag
  remains false for full_text_unavailable and this extraction limit is recorded
  separately. No wrong-pair or absent-assay assertion is made.
- [PMID:31515488](https://pubmed.ncbi.nlm.nih.gov/31515488/): cached primary
  Results/Methods show Y2H variant profiles and orthogonal PCA validation of a
  subset; no assumption that the specific ALG3 pair underwent PCA.
- [PMID:32296183](https://pmc.ncbi.nlm.nih.gov/articles/PMC7169983/): cached primary
  Results/Methods describe repeated screens with three Y2H versions, pairwise
  retesting and sequence confirmation; orthogonal subset validation is not
  assigned indiscriminately to ALG3.

All five binding-row sources retain their IPI/source identity. Short assay or
finding snippets replace paper-title-only support. The annotation-reviewer peer
confirmed the bounded policy approach but did not independently recover the
2018 full source; the full-source recovery above was performed in this lane.

### Recent human and ortholog evidence

[PMID:38597022](https://pmc.ncbi.nlm.nih.gov/articles/PMC11251843/) was read in the
original PMC manuscript, Methods and Results. Plasma glycan profiles and one
homozygous R266C patient fibroblast line reveal abnormal glycan extension and
increased UPR/ERAD readouts. The source explicitly acknowledges the single
ALG3 cell line and uses ALG9-CDG as an additional comparator. These downstream
responses support the consequence of glycosylation failure; they do not establish
ALG3 as the IRE1 signaling or ERAD execution component. No new UPR or ERAD term
is asserted. Normal cache fetch failed DNS (`/tmp/ALG3-fetch-new.log`).

[PMID:40789468](https://pmc.ncbi.nlm.nih.gov/articles/PMC12451169/) is the final
peer-reviewed 2025 JBC paper, DOI 10.1016/j.jbc.2025.110582. Indexed original
Results/Discussion/limitations show AKT phosphorylation of ALG3 Ser11/Ser13,
including human MCF10A and breast cancer cell work, isolated ALG3/recombinant
AKT1 assays and site substitutions. Glycoprotein phenotypes are rescued
differentially by wild-type and phosphorylation-site-mutant ALG3. The authors
explicitly did not directly measure phosphorylation-dependent transferase
activation or protein folding. ALG3 is the kinase's substrate; no kinase or
signaling MF is assigned to ALG3. The question of purified enzyme kinetics
remains open. Normal fetch failed DNS (`/tmp/ALG3-fetch-2025.log`).

[PMID:41807832](https://www.nature.com/articles/s41589-026-02164-7), DOI
10.1038/s41589-026-02164-7, was inspected through indexed original Methods/Results
using queries combining the DOI with ScALG3, D71N, GgALG12 and Results. The study
selected **yeast ScALG3**, human HsALG9 and chicken GgALG12. Purified ScALG3
processes synthetic lipid-linked substrates, with the D71N mutant used for a
substrate-bound structural complex. This corroborates ortholog catalytic
mechanism but is not a human ALG3 structural assay or a direct measurement of
human transmembrane-helix count. The shared normal fetch already failed during
ALG12 review (`/tmp/ALG12-fetch-new.log`); it was not duplicated.

### Source propagation, ontology and core synthesis

The protected PTHR12646 PAINT table places the three relevant IBD assertions at
PTN000291297: ER, glycoprotein biosynthesis and the precise catalytic activity.
All three remain ACCEPT. Structured IBA source entities are PTN-only; target
experimental evidence is legitimate ancestral grounding, not circularity.
The InterPro IPR007873 generic MF is true but refined to the target's specific
chemistry. The ARBA00085866 output was verified in the local rule catalog; its
exact historical target-matching condition was not recovered, so that source
link remains explicitly unresolved without manufacturing a rule failure.
RHEA:29527, EC:2.4.1.258 and UniProtKB-SubCell:SL-0097 agree with the protected
human record.

Live [GO:0052925](https://amigo.geneontology.org/amigo/term/GO%3A0052925) resolves
the Dol-P-Man donor and Man5-to-Man6 acceptor reaction. Its alpha-1,3 parent
GO:0000033 is below GO:0000030 mannosyltransferase activity; the two Reactome MF
refinements and InterPro refinement preserve chemistry while improving
specificity. Broad valid ER and glycoprotein-biosynthesis assertions remain
ACCEPT at their original resolution. Cached Reactome R-HSA-446188 is the normal
sixth-mannose step; R-HSA-4720473 describes impaired variants in that normal
reaction context and does not show normal activity in all mutants.
R-HSA-446193 has an isolated wording error calling terminal glucoses GlcNAcs;
its pathway assignment is otherwise supported, and the cache is unchanged.

GO-CAM model `65c57c3400000687`, activity `65d7e4ac00000326`, already assigns
human Q92685 the exact activity, lumenal-side location and LLO biosynthesis using
the original human study. This is a second representation of the same evidence,
not an independent experiment. The two previous duplicate cores are consolidated
into one reaction core, retaining the two existing process assertions and using
the already seeded lumenal location. **Zero NEW rows; zero new core BP terms.**
ALG3 itself performs mannose transfer. Necessity-only stress, proliferation and
CREB3-processing observations are not used to add processes, and no pathway gap
is inferred from comparator absence.

### Access, cache gates and verification

DRAFT is retained pending five required normal caches: **PMID:15840742,
PMID:30192950, PMID:38597022, PMID:40789468 and PMID:41807832**. Identity/content
verification by primary web access is distinct from local cache availability;
VERIFIED reference assessments do not claim a missing cache exists. All other
PMID flags follow protected metadata. Missing records are neither fabricated nor
removed from the citation census to silence checks. Sources proposed for a later
recovery batch do not modify any already dispatched job.

Final local verification: `just validate human ALG3` passed with one warning
category listing exactly the five missing references above. History validation
and HTML rendering passed. The immutable-source comparison passed for all
22 annotations, all 15 original reference identities and both alternative
products; all 50 cached supporting-text occurrences matched case-sensitively
after whitespace normalization. No casefold-only quote passes, YAML anchors or
aliases, or trailing YAML whitespace remain. The final four-file manifest records
byte-based Git blob IDs and SHA256 hashes; no protected source, Git or remote
state was changed.
