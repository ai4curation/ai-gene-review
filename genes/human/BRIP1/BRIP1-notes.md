# BRIP1 (FANCJ / BACH1) review notes

UniProt: Q9BX63 (FANCJ_HUMAN). Gene: BRIP1 (HGNC:20473). Synonyms: BACH1, FANCJ.
1249 aa. EC 5.6.2.3. Family: DEAD/DEAH box helicase, Rad3/XPD (DinG) subfamily.

## Identity / disambiguation (IMPORTANT)
BRIP1's old alias **BACH1** ("BRCA1-associated C-terminal helicase 1") collides with a
completely different gene, **BACH1 = BTB and CNC homology 1** (bZIP/BTB transcription
factor, transcriptional repressor of heme oxygenase-1; UniProt O14867). These are
unrelated proteins.

- **PMID:14504288** ("Cadmium induces nuclear export of Bach1, a transcriptional repressor
  of heme oxygenase-1 gene") is about the **transcription factor BACH1 (O14867)**, NOT
  BRIP1/FANCJ. The abstract concerns Bach1/small Maf heterodimers, ho-1 repression, Nrf2
  competition, Crm1/Exportin-1-dependent nuclear export — zero helicase/DNA-repair content.
  [PMID:14504288 "ho-1 is repressed by Bach1/small Maf heterodimers, it is activated by
  Nrf2/small Maf heterodimers"]. The three GOA annotations sourced from this PMID
  (nucleus IDA, cytoplasm IDA, and **regulation of transcription by RNA polymerase II**
  GO:0006357 IDA, all MGI-assigned) are mis-mapped via the BACH1 alias.
  - GO:0006357 (regulation of transcription by RNA Pol II) is uniquely from this paper and is
    biologically wrong for the FANCJ helicase → **REMOVE**.
  - nucleus/cytoplasm are coincidentally correct for BRIP1 (supported by valid refs), so those
    terms are retained overall, but this particular evidence line is flagged as mis-attributed.

## Core molecular function
5'-3' ATP-dependent DNA helicase; DNA-dependent ATPase; requires a [4Fe-4S] cluster.
- [PMID:14983014 "we show that BACH1 is both a DNA-dependent ATPase and a 5′-to-3′ DNA helicase"]
- [PMID:14983014 "its activity was greatly stimulated by CT DNA and M13 single-stranded DNA ...
  Purified BACH1-K52R lacked ATPase activity"] (DNA-dependent ATPase; K52R catalytic-dead)
- [PMID:14983014 "BACH1 preferentially displaced the 38-mer fragment ... indicating translocation
  in the 5′-to-3′ direction"]
- Catalytic activity (UniProt): EC 5.6.2.3 "Couples ATP hydrolysis with the unwinding of duplex
  DNA at the replication fork by translocating in the 5'-3' direction."
- Cofactor [4Fe-4S] cluster required for helicase activity: [PMID:20639400 "Purified recombinant
  FANCJ-A349P protein had reduced iron and was defective in coupling adenosine triphosphate (ATP)
  hydrolysis and translocase activity to unwinding forked duplex or G-quadruplex DNA substrates"];
  UniProt DOMAIN "4Fe-4S iron-sulfur-binding is required for helicase activity"
  (PMID:16973432 "The DNA repair helicases XPD and FancJ have essential iron-sulfur domains").
- DNA substrate specificity: prefers forked duplex; needs a minimal 5' ssDNA tail of ~15 nt;
  can release D-loop third strand; fails on Holliday junctions.
  [PMID:15878853 "BACH1 helicase requires a minimal 5 ' ssDNA tail of 15 nucleotides for
  unwinding of conventional duplex DNA substrates ... BACH1 completely fails to unwind a
  synthetic Holliday junction structure"]

## G-quadruplex unwinding
- [PMID:18426915 "FANCJ unwound G4 DNA substrates in an ATPase-dependent manner"]
- [PMID:18426915 "Replication protein A stimulated FANCJ G4 unwinding, whereas the mismatch
  repair complex MSH2/MSH6 inhibited this activity"]
- [PMID:18426915 "FANCJ preserves genomic stability by directly unwinding DNA roadblocks such
  as G4 structures that destabilize or impede the replication fork"]

## DNA-protein crosslink (DPC) repair at replication forks
- [PMID:36608669 "we identify a role for the 5'-to-3' helicase FANCJ in DPC repair. In addition
  to supporting CMG bypass, FANCJ is essential for SPRTN activation. FANCJ binds ssDNA
  downstream of the DPC and uses its ATPase activity to unfold the protein adduct, which exposes
  the underlying DNA and enables cleavage of the adduct"]
- Acts at the replication fork (IDA, PMID:36608669).

## Homologous recombination / DSB repair / BRCA1
- [PMID:11301010 "BRCA1 interacts in vivo with a novel protein, BACH1, a member of the DEAH
  helicase family. BACH1 binds directly to the BRCT repeats of BRCA1"]
- [PMID:11301010 "A BACH1 derivative, bearing a mutation in a residue that was essential for
  catalytic function in other helicases, interfered with normal double-strand break repair in a
  manner that was dependent on its BRCA1 binding function"]
- BRCA1 binding requires phospho-Ser990: PMID:14576433 (BRCT is a phospho-peptide binding domain;
  UniProt: "Phosphorylation is necessary for interaction with BRCA1, and is cell-cycle regulated").
- Part of the BRCA1-B complex (ComplexPortal CPX-4426): GO:0070532, PMID:16391231.

## Interstrand crosslink (ICL) repair / MutLalpha (MLH1)
- [PMID:17581638 "FANCJ interacts with the mismatch repair complex MutLalpha, composed of PMS2
  and MLH1. Specifically, FANCJ directly interacts with MLH1 independent of BRCA1, through its
  helicase domain"]
- [PMID:17581638 "FANCJ helicase activity and MLH1 binding, but not BRCA1 binding, are essential
  to correct the FA-J cells' ICL-induced 4N DNA accumulation and sensitivity to ICLs"]
- FANCJ acts late in the FA pathway, after FANCD2 ubiquitination (UniProt, PMID:16153896/14983014).

## Other interactions
- BLM helicase: [PMID:21240188 "FANCJ and BLM were found to interact physically and functionally
  in human cells and co-localize to nuclear foci in response to replication stress"]
- RPA (RPA1/RPA70): [PMID:17596542 "FANCJ and RPA were shown to coimmunoprecipitate most likely
  through a direct interaction of FANCJ and the RPA70 subunit ... RPA stimulates FANCJ helicase
  to better unwind duplex DNA substrates"]
- CIA machinery (CIAO1, CIAO2B/FAM96B, MMS19) — cytosolic Fe-S cluster assembly / maturation of
  the FANCJ Fe-S cluster: PMID:23585563 (interaction with CIAO1, CIAO2B and MMS19; UniProt SUBUNIT).
- Acetylation at K1249 regulates DDR: PMID:22792074 (UniProt PTM "Acetylation at Lys-1249
  facilitates DNA end processing required for repair and checkpoint signaling").

## Protein-binding (GO:0005515) IPI annotations
All IntAct/UniProt IPI protein-binding lines (BRCA1 P38398, MLH1 P40692, BLM P54132,
MMS19 Q96T76, HSD17B14 Q9BPX1) are uninformative MF (GO:0005515). Per curation guidelines,
marked MARK_AS_OVER_ANNOTATED; the biologically meaningful partners (BRCA1, MLH1, BLM, MMS19/CIA)
are captured in core_functions and BP annotations.

## Localization
Nucleus (core; nucleoplasm), functions at replication fork. Also cytoplasm (CIA/Fe-S maturation,
PMID:23585563). Nuclear membrane (HPA IDA GO:0031965) is a single HPA-antibody localization not
corroborated functionally → over-annotated. Testis-high expression (UniProt tissue specificity).

## Disease
Biallelic loss → Fanconi anemia complementation group J (FANCJ, MIM:609054); monoallelic variants
→ breast/ovarian cancer susceptibility (BC MIM:114480). FANCJ variants A349P (Fe-S), K52R
(Walker A, catalytic-dead), P47A/M299I (breast cancer, helicase-defective).

## NER (GO:0006289) IBA
No FANCJ-specific evidence for classical nucleotide-excision repair; the IBA propagates the
Rad3/XPD family function (XPD does NER) onto FANCJ. FANCJ's characterized roles are ICL/HR/DPC/G4,
not NER → MARK_AS_OVER_ANNOTATED.

## NEW annotations added
- GO:0036297 interstrand cross-link repair (BP) — FANCJ's central biological role
  (PMID:17581638, PMID:18426915; UniProt DISEASE/FUNCTION).
- GO:0051539 4 iron, 4 sulfur cluster binding (MF) — experimentally required cofactor
  (PMID:20639400, PMID:16973432; UniProt COFACTOR/BINDING).
</content>
</invoke>


## 2026-10-03 complete annotation reassessment (TMP candidate)

All 92 machine-seeded annotation objects were assessed, preserving their exact source fields and all 99 joined GOA rows. The two older author-proposed NEW rows are omitted with the reasons below. The two UniProt products, Q9BX63-1 and Q9BX63-2, remain unchanged; no isoform-specific functional difference is inferred from the sequence notes alone. This candidate is pending independent science review and current ownership/source checks before application.

The decisions are 65 ACCEPT, 16 KEEP_AS_NON_CORE, 10 UNDECIDED and one REMOVE. DRAFT is the schema status because validation warnings remain; it does not mean any source row remains PENDING. Normal schema, ontology, GOA, reference-title and verbatim-snippet validation passed with 14 warnings: eleven generic-binding policy warnings, one cytoplasm action-consistency warning, one optional uncited-provider warning, and one ICL core-coverage warning. No validation check was disabled. The cytoplasm split reflects the distinct evidence being assessed, and the core warning does not justify a redundant NEW annotation.

The earlier notes above are preserved as a historical record. Their blanket protein-binding over-annotation policy, confident XPD-to-FANCJ NER story, unqualified breast-risk statement, claims of complete publication access, and IOP1-based localization rationale are superseded by this assessment. The immutable publication, UniProt, GOA and Affinage files were not altered.

### Motor activities and repair mechanisms

The complete cached abstract and actual Methods/Results of PMID:14983014 establish purified human BRIP1 DNA-stimulated ATPase activity, ATP-dependent strand separation and 5'-to-3' polarity. WT/K52R preparations, ATP removal, and two directionality substrates provide direct mechanistic evidence. No figure image or supplement image was independently inspected. PMID:15878853 is abstract-only but explicitly describes human forked-DNA binding, substrate-tail requirements, D-loop displacement and failure to unwind its synthetic Holliday-junction substrate. The complete PMID:18426915 abstract and selected Discussion support ATP-dependent G4 unwinding, RPA stimulation, MSH2/MSH6 inhibition and cellular telomestatin-response effects; the cache does not expose a complete Results/Methods record.

The three retained cores distinguish duplex-DNA motor activity in repair, G4 unwinding, and motor-dependent protein-adduct unfolding in DPC repair. They do not assign a new biochemical activity inferred from generic binding. PMID:17581638 reports direct MLH1 binding and helicase/MLH1-dependent correction of FA-J crosslink responses, while BRCA1 binding is dispensable in that assay. Its Discussion explicitly leaves alternative repair and checkpoint-recovery mechanisms open. The HR and ICL contexts therefore remain bounded by that mechanistic uncertainty; BRIP1 is not described as a BRCA2-like RAD51 mediator or a crosslink-cleaving nuclease.

For PMID:36608669, the complete abstract, source-relevant Results/captions and selected Discussion/Methods were read. Purified human FANCJ, HMCES and SPRTN establish the protein-adduct unfolding/proteolysis mechanism. Xenopus egg extract and addback experiments address replication-coupled events. Human K52R was aggregation-prone, and the corresponding frog K52R was used for those comparisons; human A349P is a different force-generation mutant. The source distinguishes human Pol-eta approach from yeast Pol-zeta/Rev1 bypass and FANCJ's backup role alongside RTEL1 in some CMG-bypass events. SPRTN cleaves the protein adduct; it does not proteolyze DNA. The former prose saying DNA was exposed for cleavage by SPRTN was wrong.

The production GO-CAM `65c57c3400000100` represents BRIP1's GO:0043139 activity in GO:0106300 at GO:0005657 and causally upstream of SPRTN metalloendopeptidase activity. This directly supports the division of labor. It does not provide an independent BRIP1 interstrand-crosslink activity node. No new DPC process annotation is needed because the process is already sourced.

### Source-specific decisions and access limits

The 17 generic-binding rows are now eleven non-core and six unresolved. The evidence was assessed against exact GOA partners, including both partners in collapsed rows. BRCA1 phosphopeptide recognition, MLH1 binding, BLM interaction and MMS19 binding are distinguished from screen-level associations. BRIP1 is the phosphorylated ligand of BRCA1 BRCT, not the phosphoprotein receptor. In the purified CIA assay, FANCJ binds MMS19 but not CIAO1; larger complex association must not be converted into binary binding to every member. The unresolved screen rows remain source-specific gaps even where a partner has independent targeted evidence. These actions follow the campaign's explicit supported-binding policy rather than treating a general MF term as evidence that the interaction is false.

For NER row 2, GOA and the cached PAINT IBD both identify `PANTHER:PTN000158307` with `WB:WBGene00001049` (dog-1). The XPD/P18074 assertion lies at a different node, `PTN000158239`. The old propagation_review was factually incorrect. Official indexed donor records retain experimental NER IGI/IMP annotations, but their precise publication provenance and full ancestral placement were not recovered. The row is UNDECIDED with an explicit unresolved node record. Neither a short donor list nor the absence of a direct human assay establishes bad propagation. The meiotic IBA uses the mouse donor MGI:2442836; the complete mouse PMID:26490168 abstract supports a specific crossover-control phenotype, with fertile mutants and mostly normal early meiotic events, rather than a blanket meiotic repair failure.

The HPA nuclear-membrane row is UNDECIDED because its images and antibody controls were not inspected. The earlier claim of an antibody artifact was unsupported. Nucleoplasmic and nuclear localization are independently supported. In PMID:23585563, ROOT recovered actual Results and the Figure2 caption describing predominantly nuclear FANCJ in WT and MMS19-depleted HeLa cells; the fractionation image itself was inaccessible. A minor cytoplasmic signal therefore cannot be verified or excluded. The IEA cytoplasm mapping is retained as non-core based on explicit UniProt curation, while the two experimental source rows retain their specific unresolved evidence boundaries. An IOP1 pathway statement is not a FANCJ localization assay.

The 34 Reactome TAS rows assert nucleoplasm, not performance of every named reaction. Their reaction summaries were read for compartment and repair context, including the explicit BRIP1 recruitment/resection entries R-HSA-5685985 and R-HSA-5685994. The long individual BRCA1/PALB2 variant enumerations in disease-reaction pages were not exhaustively inspected; they do not become evidence for a BRIP1 catalytic step. Independent nuclear-foci evidence supports the retained compartment assertions.

### Bach1 identity and transcription annotation

The PMID:14504288 cache is abstract-only. Additional actual [publisher-indexed Methods/Results and figure captions](https://www.sciencedirect.com/science/article/pii/S0021925820756991) describe FLAG Bach1 BTB/CLS/bZIP and leucine-zipper constructs, MafK, HO-1 reporters, and 293/293T and GM02063 cell systems. This positively identifies the separate transcription-factor Bach1 protein. The entire paper was not read, and the former global assertion that it contains no BRIP1 data is withdrawn.

GO:0006357 covers modulation of RNA-polymerase-II transcription; it does not require sequence-specific DNA binding. Row 84 retains REMOVE because the inspected constructs and transcription assays identify the other protein, not because of a blanket assertion that BRIP1 cannot affect transcription. The reference assessment is MISCITED, not WRONG_IDENTIFIER: the PMID and title themselves are correct. Row 82 retains the independently established nuclear term with a clear citation caveat, while row 83 is unresolved because the independent FANCJ cytoplasmic fraction also remains uninspected. These source distinctions require explicit independent peer attention.

### Prior NEW proposals and cofactor interpretation

Prior row 92, GO:0036297 interstrand cross-link repair, is omitted because its verified parent is the already-carried GO:0006281 DNA repair. The user rule prohibits a redundant ancestor/descendant NEW process proposal. The specific ICL context remains in core synthesis with the mechanistic limit described above. The omission is not a claim that BRIP1 has no ICL role. No complete three-product comparator study is claimed, and no replacement NEW process is proposed.

Prior row 93, GO:0051539 4 iron, 4 sulfur cluster binding, is also omitted. The immutable UniProt record curates a [4Fe-4S] cofactor, and that biological context is retained. The inspected human [primary Results](https://pmc.ncbi.nlm.nih.gov/articles/PMC2981534/) report atomic-absorption iron content of approximately three Fe per WT polypeptide versus one for A349P, together with motor uncoupling. These measurements establish iron association but do not directly measure intact four-iron/four-sulfur cluster composition. They also do not establish a stable three-iron cluster. The old NEW IDA's precise composition claim is stronger than the inspected experiment. No new cofactor annotation is manufactured to fill an apparent GOA omission. A targeted question records this gap.

### Disease association and evidence anchors

The unqualified hereditary breast-cancer susceptibility claim is removed from the biological description. The current official [ClinGen breast-carcinoma curation](https://search.clinicalgenome.org/kb/gene-validity/CGGV:assertion_87aa8181-721b-4583-98cf-0dead1827e27-2023-12-21T180000.000Z) is Refuted, dated 2023-12-21, and is distinct from dominant ovarian-cancer susceptibility and recessive Fanconi anemia. The consulted [Easton primary abstract](https://pubmed.ncbi.nlm.nih.gov/26921362/) reports no substantial association for truncating BRIP1 variants. The later BCAC/CARRIERS estimates were inspected through ClinGen's extraction, not independently reconstructed from their primary tables. This does not establish zero risk for every variant and context and does not change BRIP1's molecular functions.

The Affinage provider record was read as a secondary research aid, not imported as experimental authority. Its cluster-coordination and transcription/repair suggestions require their own primary checks; no adaptor MF or additional process term was inferred from its labels.

The old YAML contained 52 supporting-text occurrences. The candidate retains 36 focused occurrences with a per-source ledger of short verbatim excerpts; relevant anchors are preserved or shortened, overlapping excerpts consolidated, and misleading IOP1 snippets removed. It does not delete all quotations. Normal reference validation confirms their correspondence to the immutable caches. The older notes, including their historical quotations, remain an exact byte prefix. No new publication or research cache was fetched, created or edited.


### Final evidence-list correction

The final candidate removes PMID:14504288 from the positive supporting evidence for the accepted nuclear-localization annotation (source row 82). Its original reference identifier remains unchanged for provenance. Positive nuclear evidence now cites only PMID:17596542; the transcription-factor assay and citation problem remain documented in the reason and reference assessment. No annotation action, source field, quote, core function, or product changed in this correction.


### Canonical application

The completed 92-annotation review was applied after independent scientific review and verification of the current source files and task ownership. Earlier TMP-stage wording above records preparation history. The applied review retains 10 UNDECIDED annotations and DRAFT status, with the documented evidence limits and validation warnings. The application also regenerates the gene page and adds a curation history record.


### 2026-10-03 PR #3895 review follow-up

Resolve the three required consistency issues from review 5399956246. Retain the PMID:23585563 cytoplasm IDA on explicit deference to the curator who assessed the experiment, consistently with its UniProt-derived IEA; the fractionation image remains uninspected and the compartment is secondary. Apply the same independently supported localization judgment to the row originally citing PMID:14504288, preserving its original identifier and MISCITED assessment while removing that unrelated BACH1 paper from positive support.

Retain five screen-derived generic binding rows as non-core on independently established BRCA1/MLH1 interactions (PMID:11301010, PMID:15125843, PMID:17581638), without claiming that their individual screen measurements were checked. The mixed BioPlex row includes HSD17B14 as well as MLH1: only the independently established MLH1 edge supports retention here. The HSD17B14-only row remains UNDECIDED. Original source fields and references are preserved.

Remove GO:0036297 from the first core's structured directly_involved_in list. The narrative retains the experimentally supported helicase/MLH1-dependent crosslink response and its unresolved mechanistic step; no NEW process assertion is manufactured from correction of crosslink sensitivity alone. PMID:17581638 Discussion considers repair, checkpoint and protein-displacement explanations rather than settling the exact step. Homologous recombination remains in the first core, and the separately supported protein–DNA-adduct repair core is unchanged. This resolves the structural assertion mismatch without changing the standing redundancy rule.

Normalize prose PMID separators in the changed review. All 92 machine source objects, 68 reference identities, two products, existing exact quotations and the original notes prefix are preserved. Seven judgments move from UNDECIDED to KEEP_AS_NON_CORE; three remain UNDECIDED. No source cache or earlier history is edited. Normal validation, rendering and new history are still pending at this candidate stage.

### 2026-10-03 follow-up application

Applied the independently reviewed follow-up after checking the exact canonical preimages. Normal canonical validation passed with 17 warnings, recorded in the application receipt; these remain warnings rather than unresolved schema errors. The review stays DRAFT with 65 ACCEPT, 23 KEEP_AS_NON_CORE, 3 UNDECIDED and 1 REMOVE. A new standard codex/gpt-6 EDIT history for PR #3895 was scaffolded and validated. All 92 source objects, 68 reference objects, two products and existing quotations remain unchanged; raw sources, cached publications and earlier history records were preserved. The preceding candidate-stage note records the earlier stage and is superseded by this application entry.
