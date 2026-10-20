# BBIP1 (BBIP10 / BBS18; UniProt A8MTZ0) — curation notes

## Identity
- Human gene, HGNC:28093, gene symbol BBIP1. Synonyms: BBIP10, BBS18, NCRNA00081.
- 92 aa, ~10.5 kDa; smallest of the eight BBSome core subunits. Was historically misannotated
  as a non-coding RNA ("non-protein coding RNA 81") before being recognized as a protein
  [UniProt A8MTZ0 CAUTION: "Was previously thought to be non-coding and described as 'non-protein coding RNA 81'"].
- Member of the BBIP10 family (Pfam PF14777, InterPro IPR028233). Present exclusively in ciliated organisms.
- N-terminal region 1–22 is disordered/polar; 4 splice isoforms annotated.

## Core biology — key primary paper
PMID:19081074 (Loktev et al., Dev Cell 2008; abstract-only in cache, full_text_available: false;
corresponds to UniProt "Ref.4" Loktev et al. supplying FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/HDAC6 interaction):
- Discovered BBIP10 as the eighth BBSome subunit. "We have now discovered a BBSome subunit that
  we named BBIP10. Similar to other BBSome subunits, BBIP10 localizes to the primary cilium,
  BBIP10 is present exclusively in ciliated organisms"
  [PMID:19081074 "BBIP10 localizes to the primary cilium, BBIP10 is present exclusively in ciliated organisms"].
- Depletion produces canonical BBS phenotypes in zebrafish
  [PMID:19081074 "depletion of BBIP10 yields characteristic BBS phenotypes in zebrafish"].
- A unique (non-BBSome-shared) function: required for cytoplasmic microtubule polymerization and
  acetylation [PMID:19081074 "BBIP10 is required for cytoplasmic microtubule polymerization and
  acetylation, two functions not shared with any other BBSome subunits"].
- Mechanism links to the tubulin deacetylase HDAC6: "inhibition of the tubulin deacetylase HDAC6
  restores microtubule acetylation in BBIP10-depleted cells, and BBIP10 physically interacts with HDAC6"
  [PMID:19081074]. HDAC6 = UniProt Q9UBN7 (the WITH/FROM in the GOA IPI row).
- Model: "BBSome-bound BBIP10 may therefore function to couple acetylation of axonemal microtubules
  and ciliary membrane growth" [PMID:19081074].

UniProt FUNCTION (from Ref.4): "Required for primary cilia assembly and BBSome stability. Regulates
cytoplasmic microtubule stability and acetylation." SUBUNIT: "Part of BBSome complex, that contains
BBS1, BBS2, BBS4, BBS5, BBS7, BBS8, BBS9 and BBIP10. Interacts with HDAC6." SUBCELLULAR LOCATION:
"Cell projection, cilium. Cytoplasm. Note=Localizes inside the primary cilium but not at centriolar satellites."

## BBSome architecture / assembly
PMID:22500027 (Zhang et al., JBC 2012; full text available):
- BBIP10 is "an integral BBSome protein that binds to the complex through BBS4"
  [PMID:22500027 "BBIP10, an integral BBSome protein that binds to the complex through BBS4"].
- PCM1 can interact with BBIP10 only when BBS4 is present [PMID:22500027].
- Establishes ordered BBSome assembly (core BBS7-BBS2-BBS9; then BBS1, BBS5, BBS8, BBS4).
- The GOA IPI row from this paper uses WITH/FROM UniProtKB:Q96RK4 (= BBS4), consistent with the
  BBIP10–BBS4 binding shown here. Supports a BBSome part_of / structural-binding annotation.

## Interaction mapping (high-throughput)
PMID:29039417 (Woodsmith et al., Nat Methods 2017; abstract-only):
- Yeast two-hybrid "off-switch" perturbation profiling across "eight subunits of the BBSome"; defined
  >1,000 interaction-disrupting mutations [PMID:29039417]. BBIP1 included as one of the eight subunits.
- GOA IPI row also uses WITH/FROM Q96RK4 (BBS4). Supports BBIP1 participating in BBSome via PPIs;
  generic "protein binding" (GO:0005515) is uninformative.

## Disease
PMID:24026985 (Scheidecker et al., J Med Genet 2014; not cached, cited in UniProt Ref.5):
- A null mutation in BBIP1 causes Bardet-Biedl syndrome 18 (BBS18) [MIM:615995]. Confirms BBIP1 as a
  bona fide BBSome subunit whose loss causes BBS (severe retinopathy, obesity, polydactyly, renal,
  intellectual disability).

## Structure
- Cryo-EM structure of the human BBSome includes BBIP1 (PDB 6XT9, chain J, residues 1-92; EMD-10617).
- ComplexPortal CPX-1908 = BBSome complex.

## Localization summary (for CC annotation review)
- BBSome (GO:0034464): strongly supported, multiple lines (IDA PMID:19081074, IPI, IBA, IEA). Core CC.
- Cilium / ciliary membrane (GO:0005929 / GO:0060170): BBIP10 localizes inside primary cilium; ciliary
  membrane is where the BBSome acts as a coat. Supported.
- Cytoplasm (GO:0005737): UniProt SUBCELLULAR LOCATION lists Cytoplasm; consistent with cytoplasmic
  microtubule role. Supported.
- Ciliary basal body (GO:0036064): IDA from HPA. The BBSome traffics via the basal body; plausible.
- Cytosol (GO:0005829): HPA IDA + multiple Reactome TAS. Generic; BBSome subunits cycle through
  cytosol before ciliary entry. Acceptable but less specific than BBSome / ciliary CCs.

## Process annotations
- cilium assembly (GO:0060271): supported by IMP (zebrafish/cell depletion phenotypes), NAS, IEA. Core BP.
- receptor localization to non-motile cilium (GO:0097500): IBA from GO_Central, based on the well-
  established BBSome role in trafficking signaling receptors (e.g. GPCRs like SSTR3, MCHR1) into/out
  of the primary cilium. Def: "A process in which a receptor is transported to, or maintained in, a
  location within a non-motile cilium." Strongly fits BBSome core function. Core BP.

## Notable functions NOT yet well captured by GO annotations
- Microtubule stabilization / cytoplasmic microtubule acetylation coupled via HDAC6 (PMID:19081074).
  This BBIP1-specific (non-BBSome-shared) activity is a candidate for additional BP/MF terms
  (e.g. regulation of microtubule polymerization/stability; negative regulation of tubulin deacetylation
  via HDAC6 binding). HDAC6 binding itself is more informative than generic protein binding.
- BBSome structural stability ("Required for ... BBSome stability") — supports a structural/scaffold role.


## 2026-09-30 — prospective primary-evidence amendment

This entry supersedes the earlier mechanistic proposals while preserving the prior journal. All 22 machine-source tuples and four alternative products are retained. The three supported generic binding assertions are non-core under the supplied ActionEnum; genericity alone does not make an interaction incorrect or exaggerated. The resulting source decisions are 11 ACCEPT and 11 KEEP_AS_NON_CORE.

The prior authored microtubule-polymerization and molecular-adaptor NEW proposals are withdrawn. The available depletion, HDAC6 association and rescue evidence establishes a phenotype but does not identify a tubulin-incorporation step performed by BBIP1 or a coordinated HDAC6/BBS4 bridge. No substitute NEW process is proposed, so no comparator-based gap claim is made. The tubulin observations remain in the biological description and questions.

The structural NEW proposal is narrowed to GO:0140378 protein complex scaffold activity and represented by one BBSome core. Its integral BBS4/BBS8 contacts are supported by selected original human structural Results and purification Methods [PMID:31951201](https://elifesciences.org/articles/53910). The official term is a descendant of structural molecule activity; the broad ancestor is not retained as a second proposal. After that single failed local fetch, a read-only current-main check found the existing normal record for this PMID. Its exact signed-main bytes were restored with exclusive create and verified by blob and SHA256. The fetched title (including final period) and one short structural Results anchor are now bound in the candidate. This source binding does not claim that full focused validation, history creation or rendering has run.

The 2017 publisher supplementary Figure 6 caption independently supports the BBS4–BBS18 pair [PMID:29039417](https://www.nature.com/articles/nmeth.4464). Its 104-residue construct is not assigned to a current UniProt isoform without provenance. The exact mutation matrix and image pixels remain unread. Selected local PMID22500027 Results distinguish BBS4 association from BBS4-dependent PCM1 co-association. Complete PMID19081074 abstract and original Figure 2 caption support discovery/localization and ciliogenesis, while full biochemical Results remain inaccessible. HPA antibody text, rather than a generated axoneme quotation, supports basal-body localization; ciliary-membrane IDA is retained with curator deference and the original localization experiment's access limitation.

Short primary anchors replace the prior repeated or punctuation-altered snippets. Existing notes remain historical and no scientific snippets are repeated in this appendix. The generated Falcon file, raw UniProt/GOA, source records and products are unchanged. The separate current-main/open-PR ownership check is read-only; this proposal does not perform canonical application, history creation, validation, rendering or publication.


### Focused validation of the completed amendment

`just validate human BBIP1` passed (actual ae727d), with four advisories. Three concern supported generic protein-binding rows retained as non-core under the supplied ActionEnum: the interaction observations are not shown incorrect, and no unsupported replacement activity is invented. The fourth concerns the available Falcon report not being cited by an annotation; the report remains unchanged, while decisions use directly read primary evidence. These advisories do not justify removing supported interactions or citing provider prose in place of primary evidence. Rendering passed (774e6b); the new history record records the actual checks. No global validation claim.


## 2026-09-30 — first review follow-up: partner-specific binding and localization evidence

The discovery-paper binding tuple combines two original GOA observations, with BBS4/Q96RK4 and HDAC6/Q9UBN7. The HDAC6 component supports MODIFY to [GO:0042826 histone deacetylase binding](https://amigo.geneontology.org/amigo/term/GO%3A0042826), a child of enzyme binding. The cached abstract explicitly identifies the association [PMID:19081074]; [NCBI HDAC6](https://www.ncbi.nlm.nih.gov/gene/10013/) corroborates the partner identity. This refinement applies to HDAC6, not to BBS4. Both original partner records remain preserved, and the reason retains the supported BBS4 observation. Full original biochemical Results remain inaccessible, so this does not establish purified binary binding, direct enzyme inhibition, or a coordinated three-protein bridge. The two other BBS4 source rows remain KEEP_AS_NON_CORE under the supplied ActionEnum; a supported interaction is not removed solely because its GO term is generic.

The [official HPA antibody record](https://www.proteinatlas.org/ENSG00000214413-BBIP1/summary/antibody) names basal-body and cytosolic staining in RPTEC/TERT1 and serum-starved hTERT-RPE1 cells. The revised reasons link that record directly and make the read boundary explicit: antibody text and the existing HPA IDA were assessed; image pixels and antibody specificity were not independently re-scored. The basal-body ACCEPT is retained, and no isoform attribution is added.

Additional references now follow the claim: discovery and human structural evidence support complex membership; the human structure and existing Reactome cargo events support structural participation in receptor trafficking; the discovery paper supports the assembly phenotype. PMID:31951201 is linked wherever the reason invokes the later structure. A row's original reference is not repeated as an additional reference. The scaffold NEW row already identifies PMID:31951201 as its original reference and uses the existing single core anchor. No scientific quotation is added or repeated here.

Positive cytosol reasons now describe the corresponding complex-localization context, and the core prose states how scaffold activity contributes to receptor localization. The accepted scaffold term, all core ontology terms, the withdrawn process/adaptor proposals, four alternative products and all 22 machine-source objects remain unchanged. The resulting source decisions are 11 ACCEPT, 10 KEEP_AS_NON_CORE and 1 MODIFY, plus the single previously accepted scaffold NEW assertion. This supersedes the earlier all-three-generic-binding NC summary for the HDAC6 component only.


### Focused checks for the first follow-up

`just validate human BBIP1` passed (actual 2ddbd2) with three advisories: the two remaining supported generic-binding rows stay non-core under the supplied ActionEnum, and the immutable Falcon report remains uncited while directly read primary sources support the decisions. No interaction is removed solely for genericity. Rendering passed (faeb27); the generated Codex EDIT history records this session. No global validation claim.

## Second review follow-up: scope of the merged interaction entry — 2026-09-30

The GOA source contains separate BBS4/Q96RK4 and HDAC6/Q9UBN7 interaction records for PMID:19081074. The generated review combines them under one term/evidence/reference key. This inherited entry does not retain separate partner scopes, and Review has no partner-scoped replacement field. ExistingAnnotation supports supporting_entities, but none were retained in this inherited entry. The previous prose qualification did not constrain the machine-readable replacement, so that replacement is withdrawn and the combined entry is retained as non-core. Duplicating indistinguishable entries with different actions would leave the partner assignment ambiguous. All original source files and all 22 inherited source annotation objects are preserved.

Histone deacetylase binding accurately describes the HDAC6 observation; it does not describe the BBS4 partner. That supported observation remains in the reference finding and these notes, while the established BBS4/BBS8 structural contribution remains represented by the scaffold core. No additional MF is manufactured to compensate for the source aggregation. A future partner-resolved source model could represent the two interactions independently. [PMID:19081074](https://pubmed.ncbi.nlm.nih.gov/19081074/)

The three generic-binding entries are deliberately retained as supported non-core context under the user's supplied action definitions, which reserve REMOVE for annotations unlikely to be correct on the combined evidence. This instruction takes precedence over the general recommendation to remove uninformative protein-binding terms. It does not promote those interactions to additional core functions. The notes record this decision explicitly; no repository-wide policy change is part of the gene review.


### 2026-09-30: correction of the inherited interaction-source projection

The previous explanation that the two PMID:19081074 interactions could not be
represented separately was incorrect. Although Review has no partner-specific
replacement slot, ExistingAnnotation.supporting_entities supplies the source
partner scope, and the GOA validator includes that field in annotation identity.
Two annotations with distinct support lists can therefore carry different
review actions without ambiguity. This corrects the earlier statement that
splitting the inherited entry would leave indistinguishable annotations.

The unchanged GOA file contains 23 distinct source tuples. The normal local
seeder, run without title fetching and with output confined to a temporary
file, restores nine missing support lists and adds the separately sourced
HDAC6/Q9UBN7 interaction; these are recovered source annotations, not NEW
biological assertions. Its BBS4/Q96RK4 counterpart remains separate and
non-core. The HDAC6 source is refined to GO:0042826 histone deacetylase binding
because the PMID:19081074 abstract explicitly identifies that interaction.
The term names the enzyme class of the binding partner; it does not claim
that BBIP1 binds histones, independently inhibits HDAC6, or bridges HDAC6 to
BBS4. The normal cache is abstract-only, and no new full-text assay claim is made.

The three supported BBS4-specific interactions remain KEEP_AS_NON_CORE under
the supplied ActionEnum: they are supported interactions, and the existing
scaffold core carries their principal structural interpretation. This source
repair does not change that separate instruction-precedence decision or any
other annotation judgment. There are now 23 source annotations plus the one
existing scaffold NEW proposal: 11 ACCEPT, 11 KEEP_AS_NON_CORE, 1 MODIFY, and
1 NEW. All four alternative products, the scaffold core, and all reference
records remain unchanged.
