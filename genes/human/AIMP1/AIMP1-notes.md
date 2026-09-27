# AIMP1 review notes

## 2026-09-27: full source audit

The starting review contains 50 machine-seeded annotations, no prior NEW rows, and 32 references. AIMP1 is the approved human symbol (HGNC:10648; UniProt Q12904); SCYE1 is a previous symbol, with p43, EMAPII and EMAP-2 among the aliases. The coordinator checked canonical/alias open-PR searches and exact current-main file blobs at `d2d8c9043b082a62378eff620ec0122d4118173b`. The starting YAML blob is `a845fc10e198e1f735ed6678a5fb1acc9aa1b075`. All original annotation fields, including evidence, references and any molecular-form flags, and all 32 original reference identifier/title pairs are preserved. There are no IBA rows and no AIMP1/Q12904 match in the local GO-CAM index.

I applied the review, annotation-reviewer and core-function-synthesizer skills. This is a substantive audit of the previous COMPLETE review, rather than an acceptance of its status. The genuine existing Falcon report is preserved unchanged. A fresh standard Falcon attempt, with a 1,200-second timeout and perplexity-lite fallback, used supported temporary UV tool/cache directories and a temporary output location to protect that existing report. Both providers failed while resolving dependencies because of DNS; neither produced a new report. Parallel normal publication caching skipped the 14 already present seeded PMID caches. Normal fetches of six additional papers also failed DNS. No publication, UniProt, GOA, Reactome or generated research source was hand-written or edited.

The final action counts are 24 ACCEPT, 17 KEEP_AS_NON_CORE, 5 REMOVE, 2 MODIFY and 2 UNDECIDED, with no NEW annotations. Two core entries distinguish tRNA binding from structural assembly of the same synthetase complex. Broader true RNA-binding, translation and compartment assertions remain valid; they do not need artificial refinement just because the integrated core uses a narrower term.

### RNA binding, oligomerization and complex assembly

[PMID:11306575](https://pubmed.ncbi.nlm.nih.gov/11306575/) was checked against the cached abstract and the [author-uploaded original article](https://www.researchgate.net/publication/12027128_The_EMAPII_Cytokine_Is_Released_from_the_Mammalian_Multisynthetase_Complex_after_Cleavage_of_Its_p43proEMAPII_Component). Figures 6–7 distinguish intact human p43 from its separated domains: full-length protein is dimeric, whereas the isolated C-terminal EMAP-II domain is monomeric. The N-terminal region supplies self-association. Intact p43 binds tested tRNAs at approximately 0.2 micromolar Kd, versus 7.5 and 40 micromolar for the separated N- and C-terminal regions. Thus cleavage loses the strong cooperative activity, not every measurable RNA interaction. The previous review incorrectly assigned homodimerization to the C-terminal cytokine and overstated loss of binding. The caspase-7 release experiment used murine synthetase complex and assayed migration of human mononuclear phagocytes. Those species and preparation boundaries are retained.

[PMID:10358004](https://pubmed.ncbi.nlm.nih.gov/10358004/) was verified through its primary PubMed abstract. It identifies human RARS, interaction with the pro-EMAPII N-terminal region, and stimulation of aminoacylation by intact protein. The kinetic result is reduced apparent tRNA Km with unchanged kcat. I did not recover its full body or infer additional assay details. This is positive substrate-recruitment evidence; AIMP1 does not become an aminoacyl-tRNA ligase.

The [full original PMID:25288775](https://pmc.ncbi.nlm.nih.gov/articles/PMC4210331/) was read through PMC and indexed primary Results when later direct opens were challenged. The human RARS–QARS–AIMP1 structure and assembly-disrupting mutants establish structural work by AIMP1. Its N-terminal helix organizes the subcomplex, and AIMP2-binding experiments connect it to the larger assembly. Isolated-subcomplex 2:2:2 versus dynamic 1:1:1 arrangements do not establish a universal native MSC stoichiometry. This evidence supports refinement of the existing functional MSC protein-binding row to **GO:0140378 protein complex scaffold activity**, rather than inventing a new annotation.

The [live GO:0140378 definition](https://amigo.geneontology.org/amigo/term/GO:0140378) explicitly concerns an integral complex component that holds the complex together. GO:0030674 molecular adaptor activity directs integral complex scaffolds to this term. AIMP1 meets that distinction through structural contacts and interface mutants, not merely AP-MS association.

The original source of that generic row, cached full PMID:24312579, used AIMP1/AIMP2/KARS baits in human HEK293T and HCT8 cells, repeated AP-MS and SAINT scoring. It recovered the MSC and detected AIMP1 isoform 2 peptides in KARS precipitates. This does not establish an isoform-exclusive function. PMID:19131329's cached abstract independently describes human tandem-affinity purification after auxiliary-protein silencing; its specific p38 bridging statement is not reassigned to p43. Cached full PMID:32644155 adds HEK293T cross-linking and docking evidence for the integrated structure. Its delivery geometry and stoichiometric model remain model interpretations, rather than proof of an AIMP1 catalytic mechanism.

A late primary-source check, coordinated with the AIMP2 reviewer, verified [PMID:39542129](https://pubmed.ncbi.nlm.nih.gov/39542129/) and [PDB 8J9S](https://www.rcsb.org/structure/8J9S). The AIMP1–AIMP2 leucine-zipper structure and RARS1-containing assembly corroborate the scaffold interpretation. Assembly-specific coiled-coil contacts do not negate the purified free-p43 dimer result. The full article body was not recovered, and the larger fourteen-protein arrangement remains a model rather than a universally fixed stoichiometry. The AIMP2 lane ran the one normal fetch attempt; it failed DNS and wrote no cache. This corroboration does not change any annotation decision or core.

### Compartments and the membrane-proteomics limit

The [full Results of PMID:14500886](https://pmc.ncbi.nlm.nih.gov/articles/PMC2366922/) report human nuclear and cytosolic complex purification and p43 immunoblots of gel-filtered extracts from both compartments. AIMP1 was predominantly complex-associated in those extracts. The [full original PMID:19289464](https://pmc.ncbi.nlm.nih.gov/articles/PMC2679476/) compares full-length human GFP-p43 with an N-terminal truncation in HeLa cells and examines mobility, complex association and polysome fractions. These data support cytosolic localization without excluding the nuclear pool. Both local publication caches remain abstract-only despite the external full-primary reads. Indexed queries using each PMCID plus `p43` recovered the relevant Results.

Cached full PMID:10791971 directly detects p43 in high-molecular-weight synthetase fractions. Its main MARS1 nucleolar/rRNA result is a separate claim and is not assigned to AIMP1. The HPA-derived cytosol IDA is corroborated by the independent p43 experiments; the original antibody-image details were not reconstructed.

[PMID:17525271](https://pmc.ncbi.nlm.nih.gov/articles/PMC1899434/) was verified through indexed original Methods/Results and Figure 2. HeLa endogenous AIMP1 fractionation and imaging show predominantly calnexin-associated ER and a smaller GM130-associated Golgi pool. The study links AIMP1 to gp96 dimerization and KDELR1 association. These findings support the broad ER and Golgi annotations as contextual locations; they do not settle which side of a membrane contains AIMP1. Successful query: `"PMC1899434" "Figure 2" "HeLa" "ER"`. A separate attempted laboratory PDF download did not yield usable article text and is not the evidence route.

The YTS membrane HDA from PMID:19946888 remains **UNDECIDED**. The cached abstract and [original publisher record](https://analyticalsciencejournals.onlinelibrary.wiley.com/doi/10.1002/jms.1696) establish the membrane-preparation/MS methods, but I did not recover AIMP1's target-level identification/peptide entry. Solubility or abundance is not evidence of contamination. Surface-bound extracellular EMAP-II in PMID:11741979 is a distinct, positively supported population and does not resolve this proteomics hit.

All ten cached Reactome records were read. Nine locate AIMP1 through cytosolic MSC membership in cognate tRNA-charging events; their ligase chemistry belongs to the synthetases. R-HSA-9825759 concerns MAPK-dependent KARS phosphorylation and release, while the AIMP1 assertion remains location only. The historical IARS amino-acid wording inconsistency in R-HSA-379893 and old QARS compartment wording in R-HSA-379982 are not propagated as AIMP1 biology; source files are unchanged.

### Extracellular effects and ortholog transfers

[PMID:11741979](https://pubmed.ncbi.nlm.nih.gov/11741979/) explicitly states human p43 secretion and studies the C-terminal EMAP-II ligand. The primary abstract reports ATP-synthase alpha binding by ELISA/pull-down, recipient-cell surface binding, and endothelial growth inhibition relieved by soluble alpha subunit. I did not recover the full assay body. These observations support the existing surface, proliferation and signaling annotations; they do not establish ATPase-inhibitor activity or integral membrane topology. Generic protein binding is removed as uninformative, without denying the measured interaction.

[PMID:12237313](https://pubmed.ncbi.nlm.nih.gov/12237313/) and its [author-uploaded full original](https://www.researchgate.net/publication/11154033_Dose-dependent_Biphasic_Activity_of_tRNA_Synthetase-associating_Factor_p43_in_Angiogenesis) distinguish low-dose endothelial migration from higher-dose apoptosis using recombinant full-length p43, bovine aortic endothelial cells, and chick CAM/mouse Matrigel tests. Thus extracellular activity is not exclusive to cleaved EMAP-II. The broad apoptosis IEA is refined to **GO:2000353 positive regulation of endothelial cell apoptotic process**, supported by the effector assay rather than p43 merely being a caspase substrate. The [live GO definition and parentage](https://amigo.geneontology.org/amigo/term/GO%3A2000353) were checked. This is refinement of an existing assertion, not a NEW process. Dose alone does not establish nonphysiological irrelevance.

The [full original PMID:17001013](https://pmc.ncbi.nlm.nih.gov/articles/PMC1595450/) supports mouse Aimp1 secretion under glucose starvation and glucagon stimulation in alphaTC1 cells, with rodent in vivo responses. The human plasma observations do not establish equivalent glucose-responsive secretion. Existing mouse P31230 transfers are retained as bounded extracellular biology; normal human endocrine physiology is not asserted. Indexed PMCID/`AIMP1`/`human`/`Recombinant` searches recovered Methods and Results.

The Ensembl IEA donors Q4G079 and ENSRNOP00000077517 were traced to rat Aimp1; [NCBI Gene 114632](https://www.ncbi.nlm.nih.gov/gene/114632) corroborates the identity. Exact original donor experiments were not recovered. Independent p43 vascular experiments support the contextual vessel-morphogenesis judgment despite that unresolved link. The virus-defense row remains **UNDECIDED**: [PMID:29379495 full primary PMC5775236](https://pmc.ncbi.nlm.nih.gov/articles/PMC5775236/) examines knockout **mice**, dendritic-cell/TH1 biology and influenza challenge. It supplies pertinent context but is not a recovered rat donor experiment. No rat source review was changed and no new antiviral assertion was manufactured.

### Binding-source recovery and generic terms

The [original PMID:24337748](https://pubmed.ncbi.nlm.nih.gov/24337748/) was additionally read as full original article text through the [full-article text mirror](https://paperzz.com/doc/8646917/signaling-with-the-cytoskeleton-interaction-of-t-cell-ant...), using the title/DOI `10.4049/jimmunol.1300377` and `p43` to locate the target discussion. Figure 3D/Methods compare repeated tagged-GBP1 Jurkat preparations with untransduced controls. The Discussion explicitly names multisynthetase auxiliary component p43. Thus the GTPase-binding row is retained as non-core; GBP1 is a large GTPase, and a term naming GTPase binding does not imply a small-GTPase-specific regulator. The evidence is co-association, not a purified binary assay or GAP/GEF activity. The machine cache remains abstract-only.

The other four generic IPI rows come from PMID:22190034 (HIV–human AP-MS), PMID:25416956 (binary interactome), PMID:28514442 (BioPlex 2.0), and PMID:33961781 (cell-specific BioPlex networks). Their assay context and cached material were read. Generic binding is removed under the annotation-reviewer information-content policy, not called overannotation or a false interaction. Where the cached full-text extraction is partial, `full_text_unavailable` remains false according to the genuine metadata, with the limitation recorded in reference notes.

### Access, cache gates and validation

All 14 original PMID caches and all ten cited Reactome caches are present. The six additional required PMID caches are missing after the normal fetch attempt: **10358004, 12237313, 17001013, 17525271, 25288775 and 29379495**. The late corroborating PMID:39542129 adds a seventh required cache, whose single normal fetch coordinated by the AIMP2 lane also failed DNS. They remain cited because they supply real evidence or document the inspected scope. The review is **DRAFT** pending these normal cache files. Primary identifier/content verification is independent of machine-cache availability; VERIFIED does not mean the download succeeded or that every target assay was resolved.

Evidence quotes are ordinary `supporting_text` from the actual cached text or short externally verified primary abstracts. No full-text-only field is used to evade a missing cache, and generated research headers are not substituted for experimental evidence. Reference identity/title pairs from the original review are unchanged. The review is validated and rendered with the repository tools; the final handoff manifest records check results, source preservation, exact byte hashes and all cache gates.

Final local checks: schema validation, strict ontology term/label validation, history validation and rendering passed. The local best-practice/GOA check passed with one intentional advisory: no annotation cites the generated research file, because primary evidence is used instead. The case-sensitive whitespace-normalized audit matched all 56 ordinary quote occurrences whose caches are present; five unique externally verified abstract snippets account for 12 further occurrences awaiting normal caches. The complete `just validate human AIMP1` run remains separately tracked in the handoff manifest until its reference phase finishes.

## 2026-09-27 PR #3262 feedback: primary release evidence and binding scope

The current-head [review](https://github.com/ai4curation/ai-gene-review/pull/3262#issuecomment-5853340658)
was read in full against published head `a7342d4d932748d0687fb56eaec20e8ef1a7de09`.
All six canonical file blobs matched that head before editing. The 50 machine
source objects, molecular-form fields, qualifiers, two cores and action counts
remain unchanged. The one corrected reference title is the later added
PMID:29379495: its normal CI fetch returned `T(H)1`, whereas the primary web
heading displays a subscript H. The review now uses the machine plain-text
rendering. This corrects the observed CI error; it does not claim that a local
DNS-limited validation can re-fetch that record.

The earlier extracellular section is superseded on one source attribution:
PMID:11741979's intact-p43 secretion sentence is introductory background. Its
own reported assays concern the C-terminal EMAP-II ligand, recipient-cell
surface binding and endothelial growth inhibition. The affected reviews now
cite those actual results, rather than calling the sentence a release assay.

The independent primary [PMID:10850427](https://pubmed.ncbi.nlm.nih.gov/10850427/)
and its [author-uploaded original](https://www.researchgate.net/publication/12468958_Prostate_adenocarcinoma_cells_release_the_novel_proinflammatory_polypeptide_EMAP-II_in_response_to_stress)
were read. Human prostate-cancer cells release precursor and processed forms
under stress. Figure 6 separately tests the recombinant 34- and 22-kDa forms.
These results support extracellular localization and form-dependent cytokine
activity, without establishing constitutive secretion or a unique release route.
The normal fetch failed DNS (0/1; `/tmp/AIMP1-10850427-fetch.log`); external
primary reading is not a fabricated local cache. The new record is a future
recovery gate, separate from the seven earlier source4-owned records.

The [original GBP1 paper](https://www.researchgate.net/publication/259322294_Guanylate_Binding_Protein_1-Mediated_Interaction_of_T_Cell_Antigen_Receptor_Signaling_with_the_Cytoskeleton)
was reread. Figure 3D reports four control-subtracted runs and the Discussion
names p43. The [GO:0051020 definition](https://amigo.geneontology.org/amigo/term/GO:0051020)
identifies the GTPase partner class; it does not assert GAP/GEF chemistry.
NON_CORE retains the curator's contextual physical-interaction interpretation,
with direct binary contact unresolved. Generic GO:0005515 removals follow the
information-content policy, rather than a rule rejecting all AP-MS evidence.
A short external snippet now identifies the target-level evidence; the ordinary
local record remains abstract-only.

The externally available PMID:11306575 Results/Figure 6 was independently
reread and supplies the short solution-dimer quote. Exact immutable UniProt
text corroborates it as a database statement. The annotation reason now also
distinguishes the later AIMP1-AIMP2 assembly state in PMID:39542129; neither
experiment establishes a universal native MSC stoichiometry. The cached
PMID:10791971 complex-membership row now quotes the actual p43 immunoblot and
co-elution result. The endothelial-apoptosis reason explicitly retains the
bovine recipient-cell, recombinant full-length ligand and high-dose arm of a
biphasic response. These assay limits already supported the accepted refinement.

Extracellular cytokine activity remains positively supported but non-core because
its deployment depends on release, processing and responding-cell context. The
two integrated cores retain intracellular tRNA recruitment and MSC assembly.
No missing-cached-source count is used to rank one biological function above
another. The contradictory PMID:22190034 availability prose now matches its
actual abstract-only normal metadata and unchanged true-unavailable flag.

The earlier final-check paragraph recorded a then-pending reference phase.
The new follow-up manifest separately records the terminal current validation,
source integrity, exact quotes, history and rendering; the prior CI failure is
not represented as a pass. The complete recursive review/notes/provider census
now has eight missing PMID records: **10358004, 10850427, 12237313, 17001013,
17525271, 25288775, 29379495 and 39542129**. DRAFT remains required until normal
cache retrieval permits every source-specific title/quote check.

The parent independently checked the full biological delta and the original human
release, GBP1-association and solution-dimer sources, finding no blocker. Final
full targeted validation exited 0 with all validations passed. Its two warnings
are the eight known missing publication records (reported repeatedly where cited)
and the intentional unused historical research-report advisory. History validation,
rendering, source preservation and all 50 cached quote occurrences passed. The
two external full-text snippets remain explicitly distinguished from local caches.

## 2026-09-27 source4 cache closure

This bounded follow-up starts from PR #3262 head `d942abff69f34812fb01426830a1dfb77384e34e`, confirmed by the live PR API and byte-for-byte comparison of all six gene files. The prior release-evidence and title corrections are retained. All 50 annotation objects, actions and evidence/qualifier fields, the two cores, and all 40 reference identifiers/titles are unchanged. Only seven reference assessments and two local full-text availability flags change. No NEW annotation or new functional assertion is added.

The coordinator imported seven exact normal source4 `fetch-pmid` records after verifying the run/head, artifact hash, raw outputs and source identities. Run `36294925088` and import receipt `tmp/source4-canonical-import-receipt.json` document the recovery; no publication bytes were edited. These seven paths are absent at the exact PR baseline and are included with this follow-up:

| PMID | Recovered local scope | Check and interpretation |
| --- | --- | --- |
| 10358004 | Abstract only | Human RARS interaction and reduced apparent tRNA Km with unchanged kcat corroborate substrate recruitment; no aminoacyl-transfer chemistry is assigned to AIMP1. |
| 12237313 | Abstract only | The normal abstract confirms dose-dependent migration versus apoptosis. Earlier external full Methods/Results supply the bovine recipient, chick CAM and mouse Matrigel boundaries. |
| 17001013 | Abstract only | The record confirms the hormonal study; earlier external reading establishes the mouse/rodent experimental scope. The PMC link does not mean full text was cached. |
| 17525271 | Abstract only | The gp96/KDELR1 interaction and retention study is recovered. Earlier external HeLa Figure 2 evidence remains the source for ER/Golgi fractionation and imaging; membrane topology remains unresolved. |
| 25288775 | Full text | Human subcomplex structure, AIMP1 M1 deletion/M2 helix-swap Results and AIMP2 linkage corroborate scaffold work. The main article directs detailed procedures to supplementary Methods; not every supplementary panel is claimed recovered. |
| 29379495 | Full text | Mouse BMDC and influenza experiments are now directly readable locally. The Methods specify mouse backgrounds and H3N2 challenge; human TCGA survival associations are a distinct evidence type. The existing rat-source uncertainty remains unresolved. |
| 39542129 | Abstract only | Human AIMP1/AIMP2/RARS1 leucine-zipper assembly corroborates the scaffold mechanism. Complex-state contacts do not negate free full-length p43 dimerization or impose fixed stoichiometry on every MSC. |

The two full-text records now have `full_text_unavailable: false`; the five abstract-only flags remain true. The prior exact `T(H)1` title correction for 29379495 matches the newly imported normal cache. Existing externally read full-text excerpts remain separately identified; source4 does not convert those other records into full local articles. No recovered evidence contradicts the existing annotation decisions or cores.

The explicit PMID/URL census has 22 records, with PMID:10850427 still pending source9 after the prior terminal failure in `/tmp/AIMP1-10850427-fetch.log`. No duplicate request for that source was launched. A deeper check of the immutable Falcon bibliography found three DOI-only citations that the earlier PMID-only scan missed:

| Provider DOI | Independently verified primary identifier | Scope of this check |
| --- | --- | --- |
| 10.1038/s41467-024-50730-1 | [PMID:39075051](https://pubmed.ncbi.nlm.nih.gov/39075051/), *Structural basis of tRNA recognition by the widespread OB fold* | Identity verified; the original publisher Results describe bacterial Trbp111 and yeast Arc1p. The provider's human-AIMP1 framing is not used as direct human structural evidence. |
| 10.3389/fimmu.2024.1423510 | [PMID:38975338](https://pubmed.ncbi.nlm.nih.gov/38975338/), *The mARS complex: a critical mediator of immune regulation and homeostasis* | Identity verified as a review, rather than a new direct AIMP1 experiment. |
| 10.7150/ijbs.101127 | [PMID:39494335](https://pubmed.ncbi.nlm.nih.gov/39494335/), *AIMP1-Derived Peptide Secreted from Hair Follicle Stem Cells Promotes Hair Growth by Activating Dermal Papilla Cells* | Identity verified; no new peptide/hair-growth annotation is manufactured during this cache closure. |

Those three normal caches remain absent after one ordinary fetch attempt terminated with DNS failures, cached 0/3 and exit 1 (`/tmp/AIMP1-provider-doi-fetch.log`). The remaining four gates are **10850427, 38975338, 39075051 and 39494335**. Only 10850427 is already owned by source9; the other three require future recovery, without changing an active dispatched request set. The full provider-inclusive census therefore has **25 distinct PMIDs**, not 22. This corrects the earlier census claim without editing the genuine generated report or treating its citations as automatically verified biological assertions. All ten cited Reactome records are present. The review remains DRAFT, with the remaining source gates and final validation, quote, history, rendering and immutable/hash checks recorded in the source4 follow-up manifest.

Full targeted validation exited 0 with all validations passed. Its two warning categories are the unavailable PMID:10850427 cited by the YAML and the intentionally unused genuine Falcon report. The validator scans the curated YAML and pathway Markdown; the separate recursive citation census also includes notes and DOI-only provider citations, so the four-source gate above is broader than the validator warning. The 62 ordinary cached PMID quotation occurrences pass case-sensitive whitespace-normalized substring checks; the three remaining ordinary PMID quotations all cite 10850427 and await its normal cache. The existing two external full-text snippets and the immutable UniProt quote remain unchanged.

## 2026-09-27 source9/source11 closure and current review response

The live PR API confirmed PR #3262 at `252e9e6309623069a394c7c12f8696ad07dc87b3`; all six canonical gene files matched the published blobs before editing. This follow-up addresses [formal review 5329762935](https://github.com/ai4curation/ai-gene-review/pull/3262#pullrequestreview-5329762935) and its [full comment](https://github.com/ai4curation/ai-gene-review/pull/3262#issuecomment-5854658975). All 50 machine-supplied annotation objects, actions, qualifier/isoform fields, existing reference identities and both integrated cores are retained. Three manually assessed provider-source references are added; no NEW annotation is proposed.

The coordinator imported exact normal records from source9 and source11, with byte-level provenance in `tmp/source9-canonical-import-receipt.json` and `tmp/source11-canonical-import-receipt.json`. No source file or genuine Falcon report was edited. These records supersede the four missing-cache gates in the preceding dated entry:

| PMID | Actual recovered scope | Evidence assessment |
| --- | --- | --- |
| 10850427 | Abstract only | Human prostate-cell stress-associated release and processing are checkable locally. The three existing ordinary excerpts now match the cache. The local-full-text-unavailable flag stays true. |
| 38975338 | Full review text, PMC11224427 | This mARS/immune-regulation synthesis is useful context, not a new direct human AIMP1 assay. |
| 39075051 | Full primary text, PMC11286949 | Results and Methods study bacterial Trbp111 and yeast Arc1p. Their terminal-base recognition mechanism is not a direct human AIMP1 structural result; the human binding judgments retain the original p43 evidence. |
| 39494335 | Full primary text, PMC11528461 | Human AIMP1 cDNA is expressed in inducible mice, with separate cultured human dermal-papilla and ex vivo hair-follicle experiments. The active N-terminal TN41 fragment (residues 6–46) differs from C-terminal EMAP-II. Additional procedures are referred to supplementary material; complete recovery of every supplement is not asserted. |

The current inflammatory-response concern was checked against the [author-uploaded original PMID:10850427](https://www.researchgate.net/publication/12468958_Prostate_adenocarcinoma_cells_release_the_novel_proinflammatory_polypeptide_EMAP-II_in_response_to_stress), accessed on 2026-09-27. Its Methods and Figures 5–6 test endothelial coagulation using conditioned medium and recombinant precursor/mature forms. The response is specifically TNF-dependent potentiation; hypoxic medium alone did not significantly increase coagulation. The short Figure 6 caption excerpt, “Potentiation of TNF-induced endothelial coagulation,” is preserved as an explicitly identified notes-file receipt in the YAML. It is not attributed to the abstract-only cache, and no intrinsic coagulation chemistry is assigned to AIMP1.

The three nonblocking suggestions are addressed without changing annotation actions. The signal-transduction row now attaches the actual PMID:11741979 surface-binding observation. The antiviral UNDECIDED row now quotes the PMID:29379495 mouse influenza Results; these mouse data corroborate context but do not resolve the distinct rat donor experiment. The cytokine rationale states that extracellular availability, molecular processing/form and recipient-cell context explain its non-core treatment; it does not deny measured cytokine activity or require cleavage for every extracellular effect.

The recursive census covers the review, all gene Markdown and the immutable genuine provider report, with decoded DOI/URL normalization and exact cache-metadata matching. It contains 25 distinct PMIDs and ten Reactome records, all now present; the three provider DOI mappings in the preceding table remain unchanged and now have their actual source records. The provider's bacterial/yeast-to-human extrapolation is not adopted. No new ordinary fetch was needed for records already recovered normally. Final validation, exact quotation checks, preserved-source assertions, append-only history and rendering are recorded in the frozen manifest. DRAFT is retained if the intentional unused-provider advisory remains; absence of a missing source gate is distinct from an independent PR approval.


### External primary excerpts and schema scope

The three short externally read receipts below are author notes, not normal publication caches or independent experimental evidence. The primary PMID and source remain explicit in each annotation's original source or additional references. Their annotation support points to this notes file. The schema's `supporting_text_fulltext` field requires inability to commit/share full text publicly; that condition has not been established here, so no such field or licensing assertion is used.

- **PMID:10850427**, original Figure 6 caption: “Potentiation of TNF-induced endothelial coagulation.” [Author-uploaded original](https://www.researchgate.net/publication/12468958_Prostate_adenocarcinoma_cells_release_the_novel_proinflammatory_polypeptide_EMAP-II_in_response_to_stress), read 2026-09-27. The TNF-dependent assay limits are described above; the punctuation outside the short excerpt is editorial.
- **PMID:11306575**, original Results/Figure 6: “we concluded that p43 is a dimer in solution.” [Author-uploaded original](https://www.researchgate.net/publication/12027128_The_EMAPII_Cytokine_Is_Released_from_the_Mammalian_Multisynthetase_Complex_after_Cleavage_of_Its_p43proEMAPII_Component), prior independently checked receipt retained. The measured recombinant full-length human protein is distinguished from its isolated monomeric C-terminal fragment and from complex-associated states.
- **PMID:24337748**, original Discussion: “identiﬁed by us by mass spectrometry (multisynthetase complex auxiliary component p43”. [Author-uploaded original](https://www.researchgate.net/publication/259322294_Guanylate_Binding_Protein_1-Mediated_Interaction_of_T_Cell_Antigen_Receptor_Signaling_with_the_Cytoskeleton), prior independently checked receipt retained, including the extracted ﬁ ligature. Figure 3D and Methods concern tagged-GBP1 Jurkat preparations and controls; direct binary interaction is not inferred.

The coordinator independently accepted the biological delta and identified this narrower schema boundary. This source-shape correction preserves all actions and cores while making the provenance and cache limits explicit.
