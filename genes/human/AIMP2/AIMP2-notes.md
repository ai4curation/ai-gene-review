# AIMP2 curation notes

## 2026-09-27 substantive campaign audit

AIMP2 is the approved human symbol, **HGNC:20609**, for **UniProt Q13155**.
The archived HGNC primary subset records JTV1, JTV-1, p38 and PRO0992 as aliases.
The canonical UniProt protein is 320 residues. The historical JTV1 paper's
312-residue prediction is a historical sequence statement, not a replacement
for the current sequence [PMID:8666379]. No alias directory was present.
The coordinator searched open AIMP2/JTV1/JTV-1 PRs and found no overlap. All eight
canonical files matched main `d2d8c9043b082a62378eff620ec0122d4118173b` before
editing; the coordinator subsequently confirmed AIMP2 unchanged at main
`23787fa952f4d41c0b92795752e367b2d9a207b1`.

The old COMPLETE review had **51 machine-seeded assertions and two authored
NEW proposals**, not 53 independently seeded assertions. Every seeded object
outside its review is preserved. Both authored NEW proposals were reassessed
and withdrawn for specific reasons below. The final list has 51 entries:
19 ACCEPT, 7 MODIFY, 22 REMOVE, 2 KEEP_AS_NON_CORE and 1 UNDECIDED. All 62
pre-existing reference identifier/title pairs are preserved; five independently
verified primary sources are added with explicit cache gates.

### Research execution and access limits

Four existing provider reports were read as literature leads and preserved
byte-for-byte. A fresh required Falcon attempt with a 1200-second timeout and
perplexity-lite fallback ran in an isolated temporary research directory to
avoid replacing the historical report. Both clients failed while resolving
`deep-research-client` from PyPI: three DNS retries, provider-client exit 2,
wrapper exit 1. Neither provider received a research request. No provider text
was fabricated or renamed as a report. The attempt ran concurrently with normal
publication caching, which found all 45 previously declared PMID records cached.

Five further normal fetches ended in DNS failures with no cache files produced:
**PMID:34523057, PMID:35133502, PMID:35546148, PMID:39542129 and PMID:42719951**.
These remain draft/publication gates even where independent primary web text
was accessible. Local cache metadata determines `full_text_unavailable`;
external full-source access is documented separately. A true local full-text
flag also does not guarantee that every Results or supplementary table was
extracted. The original supporting sources and machine files remain unchanged.

### MSC structural function and process participation

Human complex purification and stable knockdown support a structural role for
AIMP2/p38: “with p38 connecting two subcomplexes that may form in the absence of
p38” [PMID:19131329]. The same abstract says loss of the auxiliary components
was not lethal in the tested human cells, although growth was slightly reduced.
This differs from the mouse p38-null neonatal phenotype and complete complex
disintegration [PMID:12060739]; neither context should be universalized.

The [live GO:0030674 definition and comment](https://amigo.geneontology.org/amigo/term/GO:0030674)
explicitly direct integral protein-complex scaffolds to
[GO:0140378 protein complex scaffold activity](https://amigo.geneontology.org/amigo/term/GO:0140378).
That term describes a structural component holding the complex together. It is
therefore the precise replacement for the human MSC adaptor IDA and the broad
Compara adaptor inference. It also captures the source-specific KARS1-binding
rows in which the physical anchoring mechanism is established. The principal
core is one integrated MSC scaffold unit, with complex assembly and tRNA
aminoacylation, rather than repeated generic interaction cores.

The translation IEA is retained. The live
[GO:0006418 relations](https://amigo.geneontology.org/amigo/term/GO%3A0006418?relation=isa_partof)
place tRNA aminoacylation for protein translation **part_of GO:0006412**.
AIMP2 performs structural work in this machinery; the synthetases perform the
amino acid activation and tRNA esterification. A lack of AIMP2 catalytic
activity does not exclude structural process participation. This reasoning
supports the existing process assertions, rather than manufacturing a new one.

Important structural distinctions:

- PMID:21536907 uses solution scattering and hydrogen-deuterium exchange on a
  LysRS–p38 subcomplex. Its dimeric p38/LysRS geometry is not a universal
  whole-MSC stoichiometry determination.
- PMID:23159739 establishes the AIMP2 N-terminal KARS1 anchor. KARS1 Ser207
  phosphorylation, nuclear mobilization and Ap4A production belong to KARS1.
- PMID:26472928 describes an MRS–AIMP3:EPRS–AIMP2 GST-domain subcomplex. The fold
  supports assembly, not glutathione-transferase catalysis by AIMP2.
- Full cached Methods in PMID:31576228 specify a truncated **DX2-derived S34
  construct** retaining Ser34–Gln45 and Asp115–Lys320, with truncated DRS and an
  EPRS GST domain. Its retained interfaces inform the scaffold, but it is not
  an intact canonical AIMP2 structure. Both S156A and S156D/E perturb DRS
  association; substitution effects do not alone prove phosphorylation effects.
- PMID:32644155 uses cross-linking mass spectrometry and integrative modeling,
  **not cryo-EM**. The paper discusses uncertain native stoichiometry and
  proposed tRNA channeling. Neither becomes a directly measured universal claim.
- PMID:24312579 identifies MSC-associated isoform peptides and potential TARSL2
  association by affinity purification. Presence in a preparation does not
  resolve every individual contact or its physiological role.

The indexed full primary [PMC11072160](https://pmc.ncbi.nlm.nih.gov/articles/PMC11072160/)
was read through primary search results for PMID:35133502, including Methods
and Figures 6–8. Human AIMP2 N-terminal constructs support phosphomimetic LysRS
in biochemical/yeast assays. HEK293 AIMP2 knockout releases LysRS from the MSC;
full-length and short N-terminal rescues improve nutrient-stressed growth.
Complete-medium growth was not significantly different. These results support
structural stabilization without assigning AIMP2 synthetase chemistry.

The primary [2024 PubMed abstract](https://pubmed.ncbi.nlm.nih.gov/39542129/)
and [publisher highlights](https://www.sciencedirect.com/science/article/pii/S0022283624004959)
for PMID:39542129 clarify RARS1/AIMP1/AIMP2 leucine-zipper assembly. Partner
binding changes the homodimerization options; free subunits and assembled
subcomplexes need not share an oligomeric state. The full paper was not
recovered, and its broader proposed topology is not treated as a universally
measured native stoichiometry. This source was coordinated with the independent
AIMP1 reviewer to avoid duplicate normal fetch attempts.

### Stress functions, signaling direction and isoforms

The p53-binding IPI is refined to specific **GO:0002039 p53 binding**.
PMID:18695251 explicitly reports direct AIMP2–p53 contact and protection from
MDM2-mediated degradation. Competitive protection is not a bridge to MDM2.
The cached Discussion leaves direct JNK phosphorylation of AIMP2 unresolved;
it must not be presented as established. This source supports positive p53
activity, so the prior **negative p53 signaling NEW GO:0043518 is withdrawn**.
Positive regulation of apoptosis remains a supported refinement of the broad
apoptosis keyword assertion.

A different mechanism is supported by PMID:21285945. The cached abstract and
externally indexed full [PMC3049210](https://pmc.ncbi.nlm.nih.gov/articles/PMC3049210/)
Results/Figure 1 and ChIP methods show JTV1/AIMP2 coactivation with FBP at the
USP29 promoter in human-cell expression/stress experiments. The source-specific
binding row is refined to **GO:0003713 transcription coactivator activity**.
USP29, not AIMP2, performs the ensuing p53 deubiquitination. FUBP1 degradation
is not the mechanism of this particular paper.

For TGF-beta signaling, the cached PMID:27197155 abstract was supplemented by
indexed original [AACR Methods/Results](https://aacrjournals.org/cancerres/article/76/11/3422/607891/Oncogenic-Mutation-of-AIMP2-p38-Inhibits-Its-Tumor),
DOI 10.1158/0008-5472.CAN-15-3255. Figure 2C/D and S2D support AIMP2-dependent
SMURF2–FUBP1 association, a genuine contextual adaptor mechanism. The p38 MAPK
kinase tests used immunoprecipitated TGF-beta-activated kinase and recombinant
AIMP2/MSC substrates with S156 controls. This distinct mechanism does not
resolve the JNK question in the earlier p53 source. The independent reviewer
confirmed the association, transcription-coactivation and kinase passages.

The broad differentiation annotation is retained as non-core, with the mouse
lung phenotype [PMID:12819782] distinguished from human signaling assays.
The prior **type II pneumocyte differentiation NEW GO:0060510 is withdrawn**:
it is a descendant of already seeded GO:0030154, violating the explicit
NEW nonredundancy rule. This does not deny the reported mouse phenotype.
No replacement NEW process is proposed. The cached GO-CAM index had no Q13155
entry; absence from that index is not treated as evidence of a curation gap.

Other contextual sources were kept bounded. PMID:19584093 reports facilitation
of TRAF2–c-IAP1 association, not ubiquitin-ligase catalysis by AIMP2.
PMID:27262173 reports AXIN/DVL1 competition and mouse intestinal phenotypes,
not a ternary bridge. Full cached PMID:23974709 directly tests PARP1 interaction
and stimulation, with neurotoxicity in AIMP2-overexpression models; these data
do not establish AIMP2 as the cause of all Parkinson disease. The parkin source
PMID:12783850 distinguishes truncations from the Lys161Asn point mutant rather
than showing all parkin variants fail to degrade AIMP2.

Full external primary [PMC9095880](https://pmc.ncbi.nlm.nih.gov/articles/PMC9095880/)
Results for PMID:35546148 establish a DX2-specific KRAS mechanism in the tested
comparisons; full-length AIMP2 did not cause the same KRAS increase. This is
isoform context, not a new function assigned to canonical AIMP2. The four
historical provider reports remain immutable even where their synthesis was
more categorical.

### Inherited disease and source attribution

PMID:29215095 is the clinical Tyr35Ter report in four children from two
consanguineous families. It does not contain the later Golgi/caspase-2 cellular
finding. That finding was independently verified in the primary indexed
[PMID:34523057 abstract](https://pubmed.ncbi.nlm.nih.gov/34523057/): expressed
mutant AIMP2 in mouse FBD-102b cells, with differentiation effects ameliorated
by CASP2 knockdown. This does not establish normal human AIMP2 as a Golgi
protein, and the old clinical-paper finding was corrected.

The newly published [PMID:42719951 abstract](https://pubmed.ncbi.nlm.nih.gov/42719951/)
(2026-09-10; DOI 10.1111/febs.70716) reports patient fibroblast AIMP2/protein-
synthesis changes and zebrafish loss phenotypes. Only the primary abstract
was accessible; the publisher full text failed. It supplies current disease
context without new mechanistic GO assertions or inferred treatment efficacy.

### Propagation, broad compartments and generic binding

The cached `interpro/panther/PTHR13438/PTHR13438-paint.tsv` records the MSC IBD at
**PTN001412300**, with human, mouse and rat evidence. The member table includes
human Q13155. Human evidence among the descendant seeds is legitimate, not
circular. The full phylogenetic tree and alignment were not reconstructed;
no target-specific loss argues against complex membership. The source entity
block records the ancestral node rather than repeated extant donors.

Mouse Q8R010/ENSMUSP00000031613 and rat Q32PX2/ENSRNOP00000001379 were traced
as the relevant orthology records. The exact underlying experimental chains
were not recovered; the human judgments have independent primary support.
The combined MSC source's ARBA internals remain unresolved. Keyword,
subcellular-vocabulary and domain mappings were checked at their stated scope.

Broad cytoplasm/cytosol assertions remain ACCEPT at source resolution.
Cytosolic Reactome reactions do not assign AIMP2 the synthetases' chemistry.
The KARS phosphorylation event refers to KARS as substrate, not AIMP2 kinase
activity. Two legacy Reactome wording inconsistencies were noted locally in
reference assessments without rewriting cached records.

The membrane HDA [PMID:19946888] is UNDECIDED: the exact AIMP2 supplementary
peptide record, fraction controls and target validation were not recovered.
The source includes possible transient membrane associations. Cytosolic
abundance alone does not establish contamination or exclude a membrane pool.

Twenty-two generic-binding rows are removed as uninformative under the stated
curation policy, with source-specific study context. This does not claim that
the interactions are false. Screen-level association does not automatically
specify a molecular activity, and unrecovered pair tables remain acknowledged.
The interspecies screen [PMID:27107014] includes yeast partners; the
neurodegeneration screen [PMID:32814053] is not a parkin/PARP1 mechanistic assay.
Specific human p53, transcription-coactivation and KARS1 scaffold evidence
justify the four informative binding refinements instead.

### Validation and handoff

The review is DRAFT because five newly cited primary records still require
normal cache recovery. All source objects, machine/provider files and existing
reference identities were checked for preservation. Targeted schema/ontology/
reference validation, rendered output, history validation and the final
notes-inclusive PMID inventory are recorded in the frozen handoff manifest.

Final check outcome: targeted validation passed with two warnings (five missing
PMID caches and unused-provider advice). History validation and rendering passed.
The independent coordinator accepted all 51 decisions and the core/source
synthesis. Twenty-two supporting quotations match their cached sources. The
notes/YAML/provider PMID scan has the same five missing records listed above.
The frozen manifest records exact hashes and the unchanged source objects.

## Source4 cache closure and post-merge review follow-up, 2026-09-27

PR #3256 merged at 2026-09-27 07:13:28 UTC with head
`30620a9c78b3ae701817d2cfc48aa92bcb5e6e2d`. A fresh API read confirmed that state.
All nine local gene-directory files matched its exact blobs before editing and
also match their counterparts on imported main
`d35dcc30b44924f79c0510b281ae824aa536848a`. This follow-up uses a separate branch,
`cmungall/clingen-aimp2-source4`; the parent owns Git and publication.

The normal source4 fetch recovered PMID:34523057, PMID:35133502,
PMID:35546148, PMID:39542129 and PMID:42719951. Their exact bytes match the
canonical import receipt `tmp/source4-canonical-import-receipt.json`
(SHA256 `3c32b81b66e9234a64b687be4203965fb8d960bcffdbcfd2f6dc9b335428698b`).
No record was reconstructed or rewritten. All five exact fetched titles agree
with the existing reference titles. Only PMID:35546148 has recovered full text;
the other four are abstract-only, so their full-text-unavailable flags stay true.
The prior external primary reads remain separately documented above. Different
network paths explain why those page reads succeeded while normal local CLI
fetches failed; the successful recovery used the standard fetcher in an Actions
runner rather than manufacturing caches from browser excerpts.

The four recovered abstracts confirm their previously bounded findings: mouse
FBD-102b mutant Golgi phenotypes (PMID:34523057), human LysRS stabilization under
stress (PMID:35133502), structurally characterized leucine-zipper assembly
(PMID:39542129), and patient fibroblast findings distinct from zebrafish disruption
(PMID:42719951). Each now has an exact cached supporting excerpt. Abstract
availability does not establish access to missing full-paper details.

Full PMID:35546148 Results/Figure 1d and Supplementary Figure 1c distinguish DX2
from full-length AIMP2 in the CCD18CO cellular KRAS-abundance comparison. The
same Results/Figure 2 and Supplementary Figure 4d report similar purified-protein
KRAS4B binding by full-length AIMP2 and DX2; Supplementary Figure 4e places AIMP2
mainly with the MSC/KARS1 pool and DX2 in later free-protein fractions. The review
therefore keeps the isoform boundary on **cellular stabilization in that assay**,
not on an alleged inability of AIMP2 to bind KRAS. Independent reviewer
`annotation_a4galt` read these recovered Results and both new quotes and agreed
with this distinction. No source assertion, decision or core function changed.

The six nonblocking suggestions in
[the published review](https://github.com/ai4curation/ai-gene-review/pull/3256#issuecomment-5853250123)
were assessed individually:

- Register all four genuine provider artifacts as provenance. The three added
  assessments identify concrete overstatements already resolved by primary
  evidence, including the direct-JNK claim and the classification of AIMP2/AIMP3
  as synthetases. The files remain unchanged and are not experimental support.
- Explain why KARS1 partner identity alone does not establish the scaffold
  mechanism in the variant-specific PMID:31116475 experiment. Its generic-binding
  REMOVE remains unchanged; the interaction is not denied.
- Remove the curatorial closing clause from the biological description.
- Confirm the five identifiers and exact titles against recovered normal records,
  with source-access flags reflecting their actual contents.
- Retain membrane HDA UNDECIDED: the target peptide/fraction controls remain
  unresolved, and cytosolic abundance does not prove contamination or exclude a
  membrane-associated pool. No new evidence settles that source.
- Make the PARP1 question acknowledge positive direct biochemical stimulation;
  declining an additional NEW assertion here is a scope/term-assessment choice,
  not a denial of the measured effect or an inference from phenotype alone.

Full targeted validation completed with exit 0. All missing-reference warnings
are resolved. Its one remaining advisory says no annotation cites a provider
report; a top-level provenance reference does not satisfy that annotation-level
rule. Generated text with documented scope errors is not added to annotation
support merely to silence the advisory. Under the literal zero-warning status
convention, the YAML remains DRAFT even though the source-cache closure is
complete. The recursive YAML/notes/four-provider census finds 53 PMIDs and ten
Reactome IDs, all cached. Final preservation, quote, history and rendering checks
are recorded in the frozen manifest.

Final integrity checks preserve all 51 source objects and actions, every core
function and alternative product, and all 67 prior reference id/title pairs.
The three provider provenance entries bring the reference count to 70. All 32
supporting-text occurrences match their cached sources after whitespace
normalization. All six immutable machine/provider files remain byte-identical
to the published baseline. Every citation cache matches the exact current-main
blob except the five source4 additions, whose hashes match the import receipt.
History validation and HTML rendering passed. This closure makes no source
mutation, annotation action change or new biological assertion.


## 2026-09-27 DOI-inclusive provider citation census correction

The preceding all-cached census counted explicit PMID citations but missed references expressed only as DOIs in the immutable provider reports. That completeness claim is superseded by this DOI-inclusive audit. All provider DOI strings were decoded and normalized, compared with normal publication-cache metadata, and mapped to primary PubMed title/DOI records. The following cited sources are still missing:

| PMID and primary record | Normalized DOI | Provider location |
|---|---|---|
| [PMID:38945214], *AIMP2 restricts EV71 replication by recruiting SMURF2 to promote the degradation of 3D polymerase* | 10.1016/j.virs.2024.06.009 | AIMP2-deep-research-falcon.md, line 171 |
| [PMID:37933844], *Human lysyl-tRNA synthetase phosphorylation promotes HIV-1 proviral DNA transcription* | 10.1093/nar/gkad941 | AIMP2-deep-research-falcon.md, line 170 |
| [PMID:25320310], *Interaction of NS2 with AIMP2 facilitates the switch from ubiquitination to SUMOylation of M1 in influenza A virus-infected cells* | 10.1128/jvi.02170-14 | AIMP2-deep-research-perplexity.md, line 299 |
| [PMID:38172953], *Bi-directional regulation of AIMP2 and its splice variant on PARP-1-dependent neuronal cell death; Therapeutic implication for Parkinson's disease* | 10.1186/s40478-023-01697-5 | AIMP2-deep-research-falcon.md, line 162 |
| [PMID:26325028], *Stepping Out of the Cytosol: AIMp1/p43 Potentiates the Link Between Innate and Adaptive Immunity* | 10.3109/08830185.2015.1077829 | AIMP2-deep-research-falcon.md, line 197 |
| [PMID:38835119], *Identification and structure of AIMP2-DX2 for therapeutic perspectives* | 10.5483/bmbrep.2024-0053 | AIMP2-deep-research-perplexity.md, line 282 |

The percent-encoded BMB Reports DOI in Perplexity bibliography item 21 is cited repeatedly in the narrative and maps to PMID:38835119. The JVI URL query tail maps to PMID:25320310, which is genuinely absent; the Cancer Research PDF suffix instead maps to already-cached PMID:27197155. DOI 10.1111/febs.16557 resolves to an unrelated Methanococcus enzyme study, appears only as unused URL item 46, and has no narrative [46] citation. It is recorded as an excluded stray URL rather than a required biological source. The Cyberian DOI 10.1006/geno.1995.9997 belongs to already-cached PMID:8666379; the report's accompanying PMID:8666380 is an identifier mismatch. Those generated reports remain unchanged. The AIMP1-centered review PMID:26325028 is retained because the Falcon narrative cites it for family/scaffold context; it is not treated as a newly demonstrated AIMP2 mechanism.

One ordinary 13-record fetch ended naturally with exit 1 and cached 0/13 because DNS resolution failed. The newly decoded BMB source received a separate first attempt, also exit 1 and cached 0/1. No cache was created or edited. Exact DOI strings, titles, primary URLs, provider file/line context, protected hashes and terminal logs are recorded in `tmp/AGO2-AIMP2-doi-audit/`; the fixed source11 proposal reserves the missing records without changing earlier dispatched batches.

The review YAML, all original annotation assertions and decisions, reference assessments, core functions, alternative products, raw source files and generated provider reports are byte-identical to published head `a4838425ca616cbb37fe3a1771e28d5fc7458626`. This follow-up changes only append-only notes and session provenance and regenerates the derived HTML. The PR remains draft until the 6 required DOI-derived caches are recovered through the normal fetcher; prior validation advisories remain separate from this source gate.

## 2026-09-27 source11 recovery and PR #3289 evidence follow-up

All nine canonical gene files matched PR #3289 head `d5a7f3eae54c35adff562230ea4a4ce03466ad20` before editing. Formal review 5329790811 and comment 5854714854 were read in full. The six DOI-derived source gates above are now closed by exact normal-fetch records from source11 run `36304820186`, head `8159c7bdcb9c06c003a704f37d839a46a27c392f`, artifact `10928541969`. Their unchanged bytes match `tmp/source11-canonical-import-receipt.json`. Five contain full-text sections; PMID:26325028 is abstract-only. Access does not turn a review article into primary evidence or establish every claim in a retained provider report.

- [PMID:25320310] Full Methods/Results establish AIMP2 interactions with NS2, including endogenous recovery in infected A549 cells, and altered M1 stability/modification and vRNP export in the tested influenza system. The NS2-binding deletion, depletion and modification-site experiments support a context-specific regulatory role. The measured M1 modification switch does not make AIMP2 a ubiquitin ligase, SUMO ligase or viral RNA polymerase. The provider uses the paper's introductory TGF-beta/FUBP1 background separately from these new results.
- [PMID:26325028] The available abstract primarily reviews AIMP1/p43 immune functions and mentions AIMP2/p38 as family/MSC context. That is sufficient to identify the provider background citation, but not to transfer AIMP1 cytokine secretion or immune-cell activity to AIMP2. The unseen full article is not declared devoid of AIMP2 experiments.
- [PMID:37933844] Full Methods/Results Figures 3-4 test a tagged AIMP2-N36 peptide in human HEK293T/SupT1 cells. The peptide restricts LysRS nuclear relocation and HIV-1 transcription/infectivity. LysRS supplies the catalytic Ap4A arm; the peptide supplies retention/interaction. This supports the existing KARS1-binding model without asserting an equivalent endogenous full-length antiviral role or transferring LysRS catalysis to AIMP2.
- [PMID:38172953] Full Methods/Results distinguish AIMP2 from exon-2-skipped DX2 in oxidative-stress experiments. Human neuroblastoma interaction, PARylation and AIF-localization results support opposite regulatory effects on PARP1. Co-immunoprecipitation recovery is not an equilibrium dissociation constant. Rat primary hippocampal neurons and mouse toxin/AAV experiments supply distinct neuronal outcome contexts. PARP1 performs PAR synthesis; DX2 protection is not assigned to canonical AIMP2, and synaptic loss does not alone make AIMP2 a synaptic vesicle machine.
- [PMID:38835119] The full review summarizes canonical AIMP2 and DX2 structure/signaling. Its introductory TNF-beta/TGF-beta wording and JAK/JNK nomenclature are internally imprecise and are not adopted. Existing primary studies govern the FUBP1, TRAF2, p53 and KRAS judgments; the review adds no new experiment.
- [PMID:38945214] Full Methods explicitly clone human AIMP2 and SMURF2. Tagged and endogenous co-immunoprecipitation, inhibitor/turnover experiments and reciprocal knockdowns support recruitment of SMURF2 for EV71 3D-polymerase degradation in human-cell contexts. The paper reports K63-linked ubiquitination, not K48. SMURF2 is the ligase and the proteasome performs degradation; AIMP2 supplies the recruiting interaction. Its antiviral effect here and pro-viral influenza effect are context-specific, not a universal directional viral-response function. Vero expression assays are separately identified as monkey-cell experiments.

These source assessments are registered in `references`; no extra process assertion or core function is added during this bounded closure. All 51 existing annotation source objects, qualifiers, decisions and reasons remain unchanged. The core retains the same scaffold/assembly/aminoacylation/location/complex terms, with two exact existing cached abstract excerpts added from PMID:39542129 and PMID:35133502. The PMID:42719951 finding now attaches the actual zebrafish sentence as well as the human-fibroblast result, preserving the species distinction. The final suggested question retains its biological interrogative; its former curation procedure is already documented here and in the earlier notes.

The recursive audit covers YAML, these notes, all four unchanged provider reports, DOI/PubMed links and PDF URLs. All 59 explicit PMID identities and ten Reactome references are cached. Of 27 normalized DOI identities, 26 match normal cache metadata; the sole unmatched DOI remains the independently identified, unused and unrelated FEBS URL described above. Its presence in this exclusion explanation is not adoption as biological evidence. The Cyberian PMID mismatch remains explicitly corrected in notes without editing the provider. No nested PDF or additional auxiliary source artifact is present. All six new records are absent from both the PR base and current main `44097c7ba93eb8d1f5c171389c364dcba91dead6`, so this follow-up includes their exact normal bytes explicitly.

The previously published history session `2026-09-27T072710Z-codex-ff775a` links the original PR #3256, while this source-closure follow-up belongs to PR #3289. That historical record is preserved unchanged; the new scaffolded session records the current PR. The source-cache gate is resolved, but DRAFT remains appropriate while the unused-provider validation advisory persists. A retained provider provenance reference is not added to annotation support merely to silence that advisory. No raw publication, raw gene source or provider report has been edited.

Final targeted validation passed with that single existing provider-use advisory and no missing-cache warning. All 34 case-sensitive, whitespace-normalized attached quotes match their canonical records. Preservation checks confirm all 51 annotation objects and actions, unchanged core terms and isoforms, all 70 prior reference identities, and all six protected raw/provider files. The six added assessments bring the reference count to 76. Literal YAML DRAFT records the remaining advisory; it does not require keeping PR #3289 draft once the parent independently accepts the closed source gates and completed evidence review.
