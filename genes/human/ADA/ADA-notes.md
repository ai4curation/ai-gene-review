# ADA (human) — curation notes

> Historical notes below are superseded where stated by the 2026-09-26 campaign audit at the end of this file.

UniProtKB:P00813 (ADA_HUMAN). 363 aa. EC 3.5.4.4. HGNC:186. Chr 20.

Deep research (falcon) was polled up to the time budget and was NOT present, so this
review is grounded in the UniProt record, the seeded GOA, and the 18 cached
`publications/PMID_*.md` entries (all 18 cited PMIDs are cached; only 3 have full text).

## Core biology
- Zinc metalloenzyme (metallo-dependent hydrolase superfamily; adenosine/AMP deaminase
  family). Catalyzes hydrolytic deamination:
  - adenosine + H2O + H+ -> inosine + NH4+ (RHEA:24408)
  - 2'-deoxyadenosine + H2O + H+ -> 2'-deoxyinosine + NH4+ (RHEA:28190)
  - also deaminates cordycepin (3'-deoxyadenosine) and the drug ribavirin (Reactome:R-HSA-9754964).
  [file:P00813 UniProt "Catalyzes the hydrolytic deamination of adenosine and 2-deoxyadenosine"]
- Binds 1 catalytic Zn2+ per subunit (His15, His17, His214, Asp295; active-site His217 proton donor).
  [file:P00813 UniProt "Binds 1 zinc ion per subunit"]
- Central to purine catabolism / adenosine homeostasis. Loss causes toxic accumulation of
  (deoxy)adenosine and dATP; disease = ADA-SCID (T-B-NK- SCID), OMIM 102700.
  [PMID:9361033 "directly with the accumulation of the toxic metabolites deoxyATP and deoxyadenosine"]

## Localization
- Predominantly cytosolic. Also lysosomal (~10% of activity in fibroblast lysosomes)
  [PMID:8452534 "adenosine deaminase (ADA) activity that accounts for approximately 10% of the total ADA activity"].
- Ecto-ADA: a genuine second localization/role at the cell surface, tethered by CD26/DPP4
  (peripheral membrane, extracellular side). Ecto-ADA/CD26 catabolizes extracellular adenosine
  (endothelium under hypoxia), acts as a T-cell costimulatory molecule, and regulates
  lymphocyte-epithelial adhesion. Keep these as NON-CORE (moonlighting/second site).
  [PMID:16670267], [PMID:8101391], [PMID:7594462], [PMID:11772392].

## Annotation decisions (summary)
- CORE (ACCEPT): GO:0004000 adenosine deaminase activity (IBA/IEA/ISS/IMP/IDA duplicates);
  GO:0046936 2'-deoxyadenosine deaminase activity; GO:0008270 zinc ion binding;
  GO:0006154 adenosine catabolic process; GO:0005829 cytosol; GO:0019239 deaminase activity
  (parent MF — ACCEPT, broader ok).
- NON-CORE (KEEP_AS_NON_CORE): ecto-ADA / CD26 axis and its downstream (T cell activation,
  cell surface, external side of plasma membrane, cell-cell adhesion via integrin, negative
  regulation of adenosine receptor signaling, response to hypoxia), lysosome, sleep regulation,
  ribavirin/xenobiotic metabolism.
- OVER-ANNOTATED: bare protein binding IPIs (POTEF and DPP4 IPIs -> MARK_AS_OVER_ANNOTATED,
  not REMOVE, per policy). High-throughput interactome IPIs (POTEF, A5A3E0) are not informative MF.
- REMOVE candidates (IEA over-propagations): GO:0009168 purine ribonucleoside monophosphate
  biosynthetic process (InterPro2GO; ADA is catabolic, not a monophosphate biosynthesis enzyme);
  GO:0032263 GMP salvage and GO:0044209 AMP salvage / GO:0006196 AMP catabolic /
  GO:0046059 dAMP catabolic (Ensembl-Compara ortholog transfers describing downstream pathway
  steps ADA itself does not carry out); GO:0070161 anchoring junction and GO:0060205 cytoplasmic
  vesicle lumen (SubCell keyword IEAs, weakly supported). These are electronic inferences argued
  against on biological grounds.
- The plasma-membrane / lysosome IEA CC terms are electronic but corroborated by IDA (keep).

## Sleep (GO:0045187)
IBA-only; ADA*2 (D8N) polymorphism modulates deep sleep [UniProt POLYMORPHISM; PMID:16221767,
not cited in GOA]. Real but non-core; KEEP_AS_NON_CORE.

## 2026-09-26 campaign audit

This section supersedes the action table above, which predates the current source audit. The 69 original annotation assertions remain unchanged. The final source-specific judgments, references and two catalytic cores were audited against the available evidence.

Identity: HGNC:186, human UniProtKB:P00813, approved symbol ADA, alias ADA1. The ADA*2 allozyme is an allele of ADA, not the separate ADA2 gene. NCBI Gene 100 and the ClinGen HGNC:186 entry were inspected. The baseline was checked by the coordinator against main af7a6ea1c9a6dd7ceecc8b04b120577d1a4070cb; no overlapping ADA PR was found.

Research access: the genuine Falcon wrapper was run with the Perplexity-lite fallback and 1200-second timeout, concurrently with publication caching. Both stopped before reaching a provider because PyPI could not resolve the deep-research-client dependency (three retries, 5.3 seconds for Falcon and 11.4 seconds for the fallback). No provider report was generated or authored. All 18 original PMID caches exist. A normal additional fetch for PMID:16221767 failed DNS, as did a normal batch for PMID:718989, PMID:8064675, PMID:10720488, PMID:16742956 and PMID:12499231. These remain missing cache records, not invented sources. Normal Reactome cache retrieval also failed for R-HSA-9734745, R-HSA-9748784 and R-HSA-9754964; their primary pages were read externally.

The cached PAINT PTHR11409 IBD data were inspected. Source entities are ancestral PTN nodes, not a donor vote. PTN000150817 carries the catalytic and purine-process assertions, including hypoxanthine salvage seeded by E. coli Add (P22333); PTN000150939 carries the human-supported surface/signaling assertions; PTN002605214 carries T-cell activation; PTN000150946 carries sleep with rat Ada as a seed. Human target evidence in an IBD is legitimate, not circular.

All seven cached mouse Ada GO-CAMs found through MGI:87916 were inspected, including the activity and part_of assertions. Important models: 5f46c3b700003884 (AMP breakdown), 5fa76ad400000265 (dAMP breakdown), 60ff660000000882 (GMP salvage) and 60ff660000001341 (AMP salvage). The latter routes explicitly place Ada before Pnp and Hprt1, then the relevant nucleotide synthesis enzymes. These curated pathways contradict the earlier assertion that ADA's lack of direct nucleotide substrates excludes pathway participation. The original experimental donor papers remain unread after access failures; no primary assay details are inferred from the models. Human reaction conservation and the human Reactome purine-salvage record corroborate transfer.

Live AmiGO definitions were read for GO:0004000, GO:0046936, GO:0043103, GO:0044209, GO:0009168 and GO:0019239. The two specific substrate MFs are siblings under deaminase activity. Hypoxanthine salvage includes generating hypoxanthine from derivatives. Purine monophosphate biosynthesis includes salvage. The two catalytic cores therefore distinguish adenosine from deoxyadenosine chemistry and integrate zinc as a cofactor, rather than adding an independent zinc-binding core. The ecto-ADA compartment carries the same catalytic activity, so its established surface location is retained as core; context-dependent T-cell costimulation, adhesion, sleep and receptor regulation remain non-core.

R-HSA-9754964 uses generic deaminase for ribavirin-to-carboxy-acid chemistry. Replacing that source with adenosine-specific GO:0004000 changes the substrate and is inappropriate. Its primary Reactome page, https://reactome.org/content/detail/R-HSA-9754964, was read directly; its local cache is still missing. R-HSA-9734745 is a cytosolic mutant loss-of-function event, which supports compartment provenance without proving loss of normal enzyme function. R-HSA-9748784 is Drug ADME.

All 18 cached primary abstracts and available sections were read. The accessible human endothelial study (PMID:16670267) distinguishes human ADA-CD26 surface activity from separate mouse vascular experiments; its discussion states murine ADA does not bind murine CD26. The cache omits Methods/Results despite its metadata. The BioPlex 3 cache (PMID:33961781) also stops in the Introduction. These extraction limits must remain explicit without asserting unseen assays. Generic protein-binding annotations are removed for lack of informative MF, without denying the observed DPP4 or POTEF associations.

The vesicle-lumen donor P03958 is mouse Ada, not rat. Its exact donor localization experiment was not recovered, and the human cell-junction paper's abstract establishes surface ADA and adhesion effects without resolving anchoring-junction structure. Those location judgments remain UNDECIDED. The valve-mineralization abstract (PMID:25644539) does not reveal its ADA-specific intervention, leaving response-to-purine participation unresolved; broad adenosine metabolism is independently established. Human lysosomal activity is retained without unsupported reassignment to a paralog. The lupus antibody study is not described as a purified human catalytic assay. The zinc-site mutation study uses a structural interpretation, not a direct mutant metal-occupancy measurement.

Primary access links: https://www.ncbi.nlm.nih.gov/gene/100 ; https://search.clinicalgenome.org/kb/genes/HGNC:186 ; https://amigo.geneontology.org/amigo/term/GO:0043103 ; https://amigo.geneontology.org/amigo/term/GO:0044209 ; https://amigo.geneontology.org/amigo/term/GO:0009168 . PMID:16221767 was checked through the indexed primary PMC abstract at https://pmc.ncbi.nlm.nih.gov/articles/PMC1266101/ ; full experimental sections were not obtained. The sleep association is also described in the immutable UniProt polymorphism record.

Final source pass: all summaries and reference reviews were checked for agreement with the judgments. The three human mutation papers support refinements from generic deaminase to the native adenosine reaction; each now has a source-specific reason and functional snippet, with assay limits explicit. The approximately 10% lysosomal activity estimate is scoped to the studied human fibroblasts, not all tissues. Full-text availability is false for full_text_unavailable when extracted full-text sections exist (including the incomplete endothelial and BioPlex 3 records); incomplete coverage remains explicit. The paper titles and machine sources are unchanged. Targeted validation, append-only history and rendering are recorded in the handoff manifest; publication must remain draft while the six additional PMID caches and three Reactome caches are missing.


## PR #3179 follow-up: exact quotations and substrate-specific core

This follow-up starts from published head
fcbb41460cdce1ffeada2b3108c1185d95dee8cc and addresses the
[review comment](https://github.com/ai4curation/ai-gene-review/pull/3179#issuecomment-5851466673).
All 69 annotation source objects, 32 reference id/title pairs and original
history are preserved. The action totals remain **45 ACCEPT, 11
KEEP_AS_NON_CORE, 5 MODIFY, 3 UNDECIDED and 5 REMOVE**, with no NEW rows.

**Exact source text.** Both copies of the deoxyadenosine reaction quotation now
match the immutable UniProt line verbatim, including operand order:
`Reaction=2'-deoxyadenosine + H2O + H(+) = 2'-deoxyinosine + NH4(+)`.
The chemistry was unchanged, but reordered operands were not an exact quotation.
All remaining UniProt support snippets were checked separately for literal
source matches after handling source line wrapping.

**Core process specificity.** The second core now uses
[GO:0006157 deoxyadenosine catabolic process](https://amigo.geneontology.org/amigo/term/GO:0006157).
Its definition concerns breakdown of deoxyadenosine; its parents include
2'-deoxyribonucleoside catabolic process and purine deoxyribonucleoside catabolic
process. This directly matches the substrate of GO:0046936. The core retains the
biological explanation that this step can also operate downstream of dAMP
dephosphorylation. The existing GO:0046059 ACCEPT is not reversed: doing an
internal reaction is genuine participation in a multistep pathway, even when
another enzyme first converts the starting nucleotide to a nucleoside.

Two previously inspected mouse models are now named explicitly for the core
pairing: cached `60418ffa00000414` contains MGI:MGI:87916 with GO:0004000,
part_of GO:0006154 and occurs_in cytosol; `60418ffa00001258`, activity
`60418ffa00001304`, contains Ada with GO:0046936, part_of GO:0006157 and
occurs_in cytosol. The latter model's deoxyadenosine-process assertion is IGI
(ECO:0000315), with MGI:MGI:1857117; it is not described as a purified human
experiment. The separate `5fa76ad400000265` still places the same Ada activity
in dAMP breakdown. Human reaction chemistry is independently explicit in the
UniProt catalytic record. The earlier donor-paper access limitations remain.
GO:0006157 already exists in GO, so it does not belong in `proposed_new_terms`,
which proposes missing ontology terms. Its use in the core summary does not
add a new GOA-like row in this follow-up.

**Checkable Reactome verification.** All three previously uncached primary
Reactome pages were successfully re-opened through the web tool. The following
page sections independently reproduce the claims, so `correctness: VERIFIED`
is retained while `full_text_unavailable: true` continues to mark the missing
normal local cache:

- [R-HSA-9734745](https://reactome.org/content/detail/R-HSA-9734745): Participants
  and Catalyst Activity identify ADA mutants in cytosol; Normal reaction links
  ordinary ADA deamination; Functional status explicitly records mutant loss
  of function. This supports the compartment context without assigning loss of
  function to wild-type ADA.
- [R-HSA-9748784](https://reactome.org/content/detail/R-HSA-9748784): the human
  Drug ADME overview lists Ribavirin ADME among its events, and Event Information
  gives xenobiotic metabolic process.
- [R-HSA-9754964](https://reactome.org/content/detail/R-HSA-9754964): the summary
  assigns ribavirin conversion to its carboxylic-acid derivative to ADA, while
  noting limited importance of this route in drug catabolism. Participants
  locates substrate and product in cytosol; Catalyst Activity explicitly assigns
  GO:0019239 to ADA. This remains a contextual drug reaction with a generic
  deaminase annotation, not an adenosine-substrate refinement.

**Vesicle source.** The short support quote was removed from the UNDECIDED
vesicle row because it adds no independent localization experiment. The review's
claim that the text existed only in a GO cross-reference was too strong:
UniProt's SUBCELLULAR LOCATION block itself contains the wrapped text
`Cytoplasmic vesicle` / `lumen {ECO:0000250|UniProtKB:P03958}`. That identifies
mouse-Ada similarity provenance, not proof of human luminal residence. The
underlying donor localization remains unresolved.

**Historical decisions explicitly superseded.** The initial notes' blanket
protein-binding OVER rule is withdrawn: all five generic protein-binding rows
are REMOVE under current annotation-reviewer policy, without denying their
reported interactions. The original removal candidates GO:0009168, GO:0006196,
GO:0032263, GO:0044209 and GO:0046059 are ACCEPT in the final review. ADA
performs a catalytic step in the explicitly modeled purine salvage/catabolic
routes; it need not catalyze the terminal phosphate-containing product.

The YAML status is now DRAFT, in accord with the schema's warning-bearing
review definition. The three UNDECIDED judgments remain visible. The six
notes-level PMID cache gaps and three Reactome cache gaps from the original
audit are unchanged, and publication must remain draft pending normal caching.
No new source identifier is introduced, no cache is hand-authored, and no
published history record is rewritten. Validation, rendering, source preservation
and the exact changed-file hashes are recorded in the follow-up manifest.
