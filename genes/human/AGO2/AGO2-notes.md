# AGO2 source and annotation audit

## 2026-09-27 — substantive review

The starting review contained 267 assertions, 173 references and two core functions. Its COMPLETE label did not establish that every assertion had been substantively reviewed: one Falcon target-cleavage sentence was reused for cap binding, localization, developmental processes and generic interaction decisions. This session preserves every original assertion field outside `review`, both alternative products, and every original reference identifier/title. It adds no NEW annotations. The canonical symbol is AGO2, HGNC:3263, UniProtKB:Q9UKV8; the archived official HGNC subset records EIF2C2 and CASC7 as previous symbols and hAGO2, Q10 and LINC00980 as aliases. No separate historical-symbol directories were found. Parent-coordinated canonical and separate alias searches found no overlapping open PRs.

The baseline was compared byte-for-byte with main `795b693f5711c625401d03a755fe937260ae0ac0`; parent confirmed subsequent main changes through `43b6ab10` did not change human gene files. Baseline Git blobs were YAML `db369079be7432d1708a54fc4b0daddb61d9d042` and HTML `64fceb013f830b93ca93a4dc24ca120784316a06`. There was no notes file. UniProt, GOA and the existing genuine Falcon report remain unchanged.

### Research and access provenance

The default Falcon invocation (1200-second timeout, perplexity-lite fallback) and publication caching ran concurrently. Both provider-client launches failed before provider execution because PyPI dependency retrieval could not resolve its host; no new provider report was produced. The existing Falcon report is retained as secondary background, not treated as primary proof. The normal publication command confirmed all 82 originally cited PMIDs were already cached. Each abstract and available relevant primary body was read, with incomplete extracted bodies distinguished from complete papers. All original Reactome summaries were read except R-HSA-203862, whose cache was missing; its supported retrieval failed DNS.

Normal additional publication retrievals failed DNS for PMID:19159466, PMID:21475248, PMID:33199684, PMID:20473314 and PMID:40930611. None was fabricated. Their identities and relevant contents were independently read through PubMed, primary publisher, PMC or author/institutional primary copies. They remain missing-cache publication gates even where reference correctness is VERIFIED. A successful web read is not represented as a successful repository cache fetch. Abstract-only local records retain `full_text_unavailable: true` even when additional primary sections were read externally; partial extracted body records retain the cache-derived false flag with explicit limitations.

### RNA binding, silencing and maturation

Guide miRNA, guide siRNA, target mRNA, duplex loading and single-guide states are distinct aspects of AGO2 biology. Broad RNA-binding assertions are retained at their source resolution instead of being called over-annotations simply because miRNA binding is also present. Human AGO2 slicing is directly supported by PMID:15260970; the abstract explicitly distinguishes AGO2 endonucleolysis from the other human Argonautes assayed. This does not imply that every endogenous miRNA target is sliced.

The full PMID:19838187 uses human AGO constructs in mouse NIH3T3 tethering/transcriptional pulse-chase experiments. AGO–TNRC6 recruitment promotes biphasic deadenylation and subsequent decay. The measured activity is recruitment/regulation by AGO2; PAN2–PAN3 and CCR4–CAF1 perform poly(A) hydrolysis. Thus the four inferred positive-deadenylation/deadenylation-dependent-decay annotations are core, not merely downstream consequences. PMID:19324964 and PMID:19383768 independently distinguish AGO recruitment from TNRC6 effector domains.

PMID:18178619 reconstitutes a human Dicer–TRBP–AGO2 trimer with guide processing, loading and slicing activities. PMID:19820710 adds structural evidence; PMID:23661684 examines both TRBP- and PACT-containing preparations. AGO2 is a participating component, not the Dicer RNaseIII enzyme. Full PMID:19966796 separates duplex-bound pre-RISC from single-guide mature RISC and explicitly warns that these intermediates are not identical to the historically named Dicer/TRBP/AGO2 loading complex. Its assembly evidence is therefore not used alone to assert that exact composition.

The primary [PMID:28781232 article](https://pmc.ncbi.nlm.nih.gov/articles/PMC5915679/) Results were read through the indexed PMC primary text despite intermittent challenge pages. Its experiments mainly establish mature AGO/GW182 recruitment, including up to three AGO molecules per GW182, rather than precursor cleavage. Its NAS miRNA-processing annotation is retained on the combined independent loading/maturation evidence, with that citation scope explicit. Live definitions checked at AmiGO/ZFIN distinguish generation of functional miRNA (GO:0035196) from pre-miRNA conversion (GO:0031054); these do not require AGO2 to perform every precursor-cleavage reaction. The PAINT pre-miRNA node is not justified solely by an AGO2-specific miRNA pathway.

### Direct cap recognition remains unresolved

PMID:17524464 proposed an eIF4E-like AGO2 MID-domain cap motif. Its repression and catalytic observations are not collectively discarded. The primary [PMID:19159466 article](https://pmc.ncbi.nlm.nih.gov/articles/PMC2636766/) challenges the structural homology and accessibility of the proposed aromatic residues; that is a structural critique, not an independent biochemical null experiment. The primary [PMID:21475248 article](https://pmc.ncbi.nlm.nih.gov/articles/PMC3090017/) tests isolated MID domains and catalytically active recombinant AGO2 beginning at S34. Low, nonspecific cap-resin recovery did not establish selective recognition; that construct omits the N-terminal proline-rich segment and cannot exclude cofactor-dependent cellular behavior.

Full cached PMID:23409027 reports cap-specific photocrosslinking in cellular AGO2 complexes, strengthened by eIF4GI. Its wording allows direct interaction or very close proximity. eIF4GI/AGO2 association can involve additional partners; these experiments do not settle selective binding by isolated AGO2. Five cap-binding assertions therefore remain UNDECIDED. The same F470/F505 substitutions affect TNRC6 recruitment in PMID:19838187, so a mutant repression defect is not uniquely diagnostic of cap recognition. Translation repression remains core independently of this controversy.

### Recombinant inhibition of Dicer

For PMID:14749716 the local extraction includes Introduction, Methods and Discussion but omits Results. The [author-uploaded full original](https://www.researchgate.net/publication/8897039_Characterization_of_the_interactions_between_mammalian_PAZ_PIWI_domain_proteins_and_Dicer) was read on 2026-09-27. Figures 3–4 report purified insect-cell Dicer, COS1-produced GST–AGO2, nuclease-resistant association, PIWI-box/RNaseIII-A interaction in yeast and a dose-dependent reduction of 130-bp RNA cleavage relative to GST. Similar pre-let-7 and preincubation results are described as data not shown. No explicit substrate-sequestration separation-of-function control was found. The generic binding annotation is replaced by GO:0060698 endoribonuclease inhibitor activity at that bounded recombinant in-vitro scope, excluded from core. The live AmiGO definition requires binding and reduced endoribonuclease activity; the physiological direction of regulation remains an open question.

### Compartments, target-specific outputs and disputed mechanisms

- The [PMID:29735530 primary Methods](https://pmc.ncbi.nlm.nih.gov/articles/PMC6005451/) identify human GFP–AGO2 WT/S387A/S387D constructs expressed in rat hippocampal neurons. Spine/PSD95 experiments support the contextual synapse annotations; the rat cell background does not make them human-protein misattributions.
- The [PMID:17382880 primary Results](https://pmc.ncbi.nlm.nih.gov/articles/PMC3430382/), Figures 3–6, use formaldehyde crosslinking, ARE-specific RNA purification, co-IP and translation assays. AGO2/FXR1 association and translation activation are serum-starvation dependent. The ARE binding judgment is retained with curator deference at the RNP-association scope, without claiming purified guide-independent AU-motif recognition.
- Full PMID:25336585 shows AGO2/AGO1 association with PolII/TBP, promoter ChIP and guide/promoter sequence-dependent activation. Nuclear and positive transcriptional roles remain non-core. The exact AGO2 core-promoter sequence-specific DNA-binding MF remains UNDECIDED: the assays do not identify which component contacts DNA rather than associated RNA or proteins.
- The [PMID:31400113 primary Results](https://pmc.ncbi.nlm.nih.gov/articles/PMC6755100/), Figures 3–5 and 8, distinguish AGO2 occupancy from GW182/DDX6-dependent P-body formation. AGO2 depletion did not reduce visible P-bodies in the reported models, but lack of necessity does not prove nonparticipation. Cached GO-CAM `653b0ce600001283` explicitly asserts AGO2 participation in P-body assembly using this source. The executing assembly contribution remains unresolved; no unsupported scaffold function is substituted.
- PMID:14749716 Figure 6 independently supports endogenous AGO2 in soluble and membrane-associated HEK293T fractions with calnexin/HSP90 controls. PMID:19946888 YTS proteomics is retained at its broad membrane-associated resolution with curator deference; the AGO2 supplementary peptide assignment was not independently reanalyzed. No integral membrane topology or contamination conclusion is inferred.
- Full PMID:28159509 identifies AGO2 in human pericardial-fluid exosome preparations and AGO2-associated miRNAs. Figure S3 reports resistance to proteinase K/RNase before membrane disruption, with loss after sonication. This strengthens encapsulation in that preparation, not universal secretion or a demonstrated activity of transferred AGO2 protein in every recipient phenotype.
- The ISS APP donor is rat Ago2 Q9QZ81. Independent [PMID:20473314 Figure 6](https://pmc.ncbi.nlm.nih.gov/articles/PMC2908492/) supports AGO2-associated APP RNA and FMRP-dependent repression in human BE2-M17 cells. The complete rat donor chain remains unresolved; human corroboration is not mislabeled as its recovery.
- PMID:10534406 remains abstract-only after primary search attempts. Its abstract explicitly concerns human EIF2C1 cloning and rabbit homology; it does not settle which historical protein/construct or initiation step underlies the AGO2 NAS annotations. Those two rows and their electronic process propagation remain UNDECIDED rather than REMOVE based on name history alone.

### Reference integrity and pathway provenance

PubMed explicitly links PMID:25446899 to the 2025 Expression of Concern PMID:40930611, DOI 10.1016/j.ccell.2025.07.022. Its [full institutional primary notice](https://mdanderson.elsevierpure.com/en/publications/erratum-cancer-exosomes-perform-cell-independent-microrna-biogene-2/) was read on 2026-09-27. It reports duplicated/relabelled figure panels, an institutional recommendation for retraction, author disagreement and ongoing journal assessment. The original is marked DISPUTED, not retracted or `is_invalid`. The generic binding row is removed for lack of functional information, without declaring a particular AGO2 interaction disproven. The independent pericardial-fluid source is judged separately.

PMID:19701182 has a [2025 Author Correction](https://www.nature.com/articles/s41586-024-08559-7), read in full via the indexed publisher notice. It corrects duplicated beta-actin/Dicer images and an MCF7 lane label in Figure 5b. AGO2-associated RMRP small-RNA evidence used here is Figure 5c; the correction is not a retraction. The TERT–RMRP polymerase activity is not assigned to AGO2.

All 78 cytosol/Reactome assertions retain their original compartment and citations. Event summaries are distinguished from direct localization measurements. Upstream p53/FOXO3-dependent miRNA transcription does not make AGO2 a transcriptional enzyme, and lowered target mRNA abundance does not establish target slicing. Internal cached summary discrepancies are documented for R-HSA-8948651 (CNOT6L/CNOT5L), R-HSA-9012203 (CHD11/CHD1), R-HSA-9925087 (miR-138/miR-429) and R-HSA-9925159 (miR-140/miR-34); original machine titles are unchanged.

Nine PAINT source reviews use only the actual PTN nodes, checked against term-specific cached PTHR22891 IBD rows. AGO2 appearing among experimental descendant evidence is legitimate grounding, not circularity. Mouse Q8CJG0 and ENSMUSP00000042207 were cross-checked against NCBI Gene 239528. ARBA/UniRule identifiers are preserved, with unrecovered rule internals explicitly UNRESOLVED even when direct target evidence supports the biological assertion.

### Draft completion and validation

The initial authored pass assigns 175 ACCEPT, 24 KEEP_AS_NON_CORE, 10 UNDECIDED, 57 REMOVE and one MODIFY across the unchanged 267 assertions. Generic GO:0005515 removals enforce the repository policy and do not allege that unresolved physical interactions are absent. All 173 original references and five added primary records have source-specific assessments; no original PMID finding existed to silently preserve or contradict. Three cores separate slicing, recruitment-mediated repression/decay, and guide loading/maturation.

Targeted validation passed with two warning groups: the five unavailable PMID caches and an advisory that no annotation quotes the existing Falcon report. A separate validation with ontology-term checking also passed; reference checks were skipped only in that additional term-check invocation. Primary excerpts are used for annotation evidence, so the advisory is retained without adding a provider quote merely to silence it. The notes-inclusive audit finds 87 cited PMIDs, 82 cached and exactly the five documented missing records. Reactome R-HSA-203862 remains an additional source gate.

The parent independently read all 267 biological judgments and the three cores, and independently checked the full PMID:14749716 Figures 3–4/Methods and the live inhibitor-term definition. The parent accepted the bounded in-vitro inhibitor replacement and the cap, P-body, ARE, APP and promoter decisions. A subsequent independent pass through all PMID and GO_REF assessments and grouped Reactome notes found no blocker. All source assertions and machine-file hashes match the baseline. Final standard validation, history validation and rendering passed; the publication manifest records exact file hashes and source preservation. The review status is DRAFT, with no PENDING decisions, because publication must remain draft while the five added PMID caches and Reactome R-HSA-203862 remain unavailable.

## 2026-09-27 — PR #3210 precursor-processing and core-function follow-up

This follow-up addresses review 5328442214 at published head `f8d4f2db443c15f349167eae8bb51e6d85db8121`. All three curated baseline files matched that published tree byte-for-byte. It preserves all 267 source assertions, both alternative products and all 178 reference identifier/title pairs from that head. No machine evidence file, existing publication cache or published history record is edited. The following source-specific judgments supersede the earlier common precursor-maturation rationale; the earlier session record is retained as provenance.

There are **six**, rather than five, GO:0031054 source rows. The live AmiGO definition concerns conversion of a precursor transcript into a mature miRNA. Guide loading alone is not that conversion. The six rows now distinguish their actual evidence:

- IBA at PANTHER:PTN000527278: target ACCEPT, with the exact ancestral mechanism UNRESOLVED and curator-deferred. The cached PAINT table really contains the term-specific IBD, with AGO2 among legitimate experimental descendants. Human target processing has primary support, but AGO2-specific precursor slicing is not proof of that mechanism in every descendant. Neither donor count nor target self-evidence is a reason to reject the IBA.
- Combined IEA: ACCEPT based on independently observed human and mouse precursor processing. The original ARBA/UniRule internal conditions remain unresolved; conserved target biology does not retroactively validate every rule condition.
- PMID:16424907: UNDECIDED for the precise source-specific AGO2 contribution. The abstract identifies the PACT/Dicer/AGO2/TRBP complex and PACT-depletion effects. Full PMC1383527 and publisher retrieval remained blocked. This is not an assertion that the curator chose the wrong gene, and independent short-hairpin cleavage does not identify the experiment in this source.
- PMID:19966796: MODIFY to existing GO:0070922 RISC complex assembly. Full cached Results explicitly distinguish dicing from guide loading; recombinant AGO2 lacking dicing on pre-miR-luc can use an undiced hairpin as a long guide. Direct duplex contact and maturation of pre-RISC provide the positive replacement evidence.
- PMID:18178619: MODIFY to existing GO:0070922. The full original author PDF was read at <https://doudnalab.org/Publications/pnas-105-512.pdf>. Figure 2B assigns pre-let-7 dicing to Dicer; Figures 3–4 establish AGO2 guide selection/loading and release. Its generic RLC abstract quote is not treated as proof that AGO2 itself cleaves that precursor.
- PMID:17671087: ACCEPT at the original process/assay scope. Full Results and Figure 1 were recovered at <https://pmc.ncbi.nlm.nih.gov/articles/PMC1935024/>. In human HEK293F extracts, AGO2 overexpression increases synthetic pre-let-7 conversion to the mature product. This is stronger than the earlier abstract-only account, although it does not isolate AGO2 catalysis or separate processing rate from product stabilization. The paper also mentions an AGO1 effect without showing those data; that is not represented as a purified-protein assay.

### Direct precursor cleavage and its scope

Three suggested primary identifiers were independently resolved on PubMed and normal fetching was attempted together. PMID:20448148, *A novel miRNA processing pathway independent of Dicer requires Argonaute2 catalytic activity*, was read in the original author PDF at <https://www.giraldezlab.org/docs/1694.full.pdf> (DOI 10.1126/science.1190809). Figure 2B and its Results directly assay recombinant human AGO2 cleavage of the short pre-miR-451 hairpin to a 30-nucleotide intermediate. The organismal experiments use zebrafish; mouse Ago2 constructs supply rescue. Subsequent trimming is a separate step, not an AGO2 exonuclease assignment. This directly supports the human precursor-cleavage core without borrowing Dicer chemistry.

PMID:20424607, *A dicer-independent miRNA biogenesis pathway that requires Ago catalysis* (DOI 10.1038/nature09092), was verified through its PubMed abstract and displayed Figure 5 caption and the Nature record. It provides mouse catalytic-mutant and precursor-processing evidence; full PMC body access was blocked. PMID:18083100, *Dual role for argonautes in microRNA processing and posttranscriptional regulation of microRNA expression* (DOI 10.1016/j.cell.2007.10.032), was verified through the PubMed and Cell abstracts. Its ac-pre-miRNA claim corroborates the processing distinction, but the unread full experimental body is not used to infer construct/species details or as sole evidence for a core. These identifiers are VERIFIED on actual primary access, independently of local cache availability.

Normal `just fetch-pmid 18083100 20448148 20424607` returned exit 1 and cached 0/3 because DNS resolution failed (`/tmp/AGO2-followup-fetch.log`). No cache was fabricated. References to externally inspected bodies are explicit about the route, date and figure; reference-only support objects do not pretend that a missing body quote passed cache validation. The open-access full-text bodies for the two older sources remain absent from their abstract-only local caches. `full_text_unavailable: true` therefore remains paired with explicit external access notes. No `supporting_text_fulltext` bypass is used for these openly available papers.

### Core specificity and remaining review points

The target-cleavage function is separated into exact GO:0090624 miRNA-paired and GO:0070551 siRNA-paired mRNA activities. Live AmiGO pages checked on 2026-09-27 give those exact labels and an `is_a` parent of GO:0016891 for each; GO:0090624 also has a `part_of` relation to GO:0035279. The current formal definition of GO:0035279 still specifies endonucleolytic cleavage, despite its broader name and deadenylation synonyms, so it remains with miRNA target slicing. It is not used as a synonym for all miRNA-driven decay. No independently enabled activity is placed in `contributes_to_molecular_function`.

Five cores distinguish the two mRNA substrates, effector recruitment, duplex guide loading and short-precursor cleavage. The precursor core uses GO:0004521 only for the hairpin substrate, which the mRNA-specific terms do not cover; it is not a second umbrella claim for the same target-cleavage activity. Loading retains GO:0070922 and no longer carries precursor conversion merely by adjacency. Broad cytoplasm is used at the experimentally supported source resolution. P-body association remains explicit for the recruitment function without making visible granules obligatory for every silencing event. No NEW annotation is added and the proposed RISC-assembly replacements duplicate established coverage deliberately rather than manufacturing another source assertion.

The GO:0033962 P-body assembly row remains UNDECIDED with an explicit deferral to GO-CAM 653b0ce600001283 and its original PMID:31400113 IDA. Lack of reduced P-body counts after AGO2 depletion is evidence about necessity for that measured endpoint. It does not demonstrate universal nonparticipation. Conversely, granule occupancy does not establish an executing assembly step. The earlier hypothetical redundancy explanation is withdrawn; the model-specific question remains open.

The bounded recombinant Dicer-inhibitor replacement is retained: the earlier full primary inspection established AGO2 contact and dose-dependent suppression, with substrate competition and endogenous relevance unresolved. The PPD-family abstract language is not its sole mechanistic evidence. The historical NAS translation-initiation assertions remain UNDECIDED; current publisher access still did not recover the full source. Negative regulation of initiation does not logically contradict every possible initiation-factor mechanism, and an old EIF2C name is not proof of a wrong-gene annotation.

### Follow-up validation and release gates

The normal `just validate human AGO2` completed successfully with three warning groups: eight missing PMID caches, intentionally different source-specific actions for GO:0031054, and no annotation directly citing the preserved Falcon report. The processing-action advisory is retained deliberately: the reviewed papers assay different steps, and a correct target-level function does not make every original experiment a precursor-conversion assay. The current counts are 172 ACCEPT, 24 KEEP_AS_NON_CORE, 11 UNDECIDED, 3 MODIFY and 57 REMOVE, with no NEW entries. Five cores and 181 reference assessments remain.

Rendering and the scaffolded history validation passed. Exact comparisons confirmed all 267 assertion source objects, both alternative products, all 178 baseline reference identifier/title pairs, the three machine-generated gene artifacts and the published history unchanged. Trailing whitespace introduced by YAML serialization was removed only after asserting parsed-YAML equality; the HTML was rendered from the resulting file.

The notes-inclusive cache audit finds 90 cited PMIDs, 82 cached and eight missing: PMID:18083100, PMID:19159466, PMID:20424607, PMID:20448148, PMID:20473314, PMID:21475248, PMID:33199684 and PMID:40930611. Reactome:R-HSA-203862 is also still missing. DRAFT remains required. The follow-up manifest records exact bytes and baseline blobs; no Git, remote comment or publication operation was performed by the author.

## 2026-09-27 post-merge verified cache closure

The coordinator observed PR #3210 merged at 03:59:52 UTC with reviewed head
`4171bbc8aad68ab8a734881ca3af70d61174b377` and imported the exact signed main
snapshot `3e4b386077392a633b451112065243c8577d132b`. Every canonical AGO2
file was independently matched byte-for-byte to that snapshot before this
follow-up. A fresh author API read failed connection; this preflight relies
on the coordinator's live observation and the exact imported objects, not
an invented later remote-state observation.

Eight normally fetched PMID records and Reactome:R-HSA-203862 now match the
verified recovery receipts by SHA-256. PMID:19159466, PMID:21475248,
PMID:20424607, PMID:20448148, PMID:20473314 and PMID:33199684 contain
extracted full bodies. PMID:18083100 remains abstract-only;
PMID:40930611 contains the Expression of Concern bibliographic linkage,
not the body of the notice. These recoveries supersede earlier statements
that the nine repository records were missing. The distinction between
external primary access and local body availability remains explicit.

The recovered human precursor-cleavage Results [PMID:20448148] reproduce
Figure 2B's hAgo2/pre-miR-451 30-nt product and Figure 4D's recombinant
human engineered-hairpin assay. The existing processing rows and hairpin
core now carry the exact cached Results sentence. Zebrafish organismal
experiments, mouse rescue constructs and separate downstream trimming
remain distinguished. The mouse paper [PMID:20424607] now supplies its full
Results and Methods Summary, confirming the endogenous catalytic mutant
and biochemical cleavage; the isolated 293T-complex transgene species is
not independently resolved from that extraction. This does not change the
existing comparator or any annotation action. The 2007 ac-pre-miRNA paper
[PMID:18083100] still supplies only its corroborating abstract.

The two recovered cap papers preserve the assay limits: the structural
study [PMID:19159466] places one proposed aromatic side chain in the
hydrophobic core and the other on the surface, whereas the biochemical
study [PMID:21475248] tests the isolated MID domain and active S34-to-C-
terminus AGO2 with cap and nonspecific resin controls. Cellular cofactors
are not excluded. The latter reference's title now exactly matches the
machine-fetched ASCII apostrophe; its PMID and scientific identity are
unchanged. Human BE2-M17 Results [PMID:20473314] confirm AGO2-associated
APP RNA and contextual FMRP-dependent repression without recovering the
rat donor chain. The human variant study [PMID:33199684] confirms
mutation-dependent defects, including a distinct severe p.G733R pattern;
its simulated unwinding mechanism remains qualified. The notice metadata
[PMID:40930611] establishes the Expression of Concern linkage; detailed
image-integrity concerns remain based on the previously documented full
external notice, not a nonexistent local notice abstract. It is not a
completed retraction.

The recovered Reactome summary explicitly lists DICER1, AGO2 and TARBP2
in the loading complex and assigns canonical precursor cleavage to
DICER1. It confirms AGO2 participation in the event but does not export
compartment metadata. The original cytosol assertion therefore retains
curator deference and independent human localization support; the summary
is not represented as a direct localization assay.

All 267 machine-seeded assertions, all review actions and the five core
biological descriptions/terms are preserved. Existing histories, machine
files and the provider report are unchanged. All 90 previously cited biological-source PMIDs in the
review YAML/notes and every cited Reactome identifier now have canonical
records. The notes-inclusive count becomes 92 after the two artifact-only
gaps below are explicitly documented. A separate scan of the immutable Falcon report identifies two
additional artifact-only missing records, PMID:15105377 and PMID:23746446;
these are disclosed separately rather than counted as recovered. DRAFT
remains appropriate for unresolved validation advisories and those
artifact citations. Source receipts are
`tmp/verified-reference-records/local-import-receipt.json` and
`tmp/verified-reference-records2/local-import-receipt.json`; source2 artifact
SHA-256 is `0876942c72b2e537e858e8af7cd3c79d34b97c2169490e3d883c6f00884e2965`.
Only the nine exact required recovered records accompany this gene's
manifest. No cache, Git state or remote state was edited.

## 2026-09-27 remaining provider references after PR 3264 merge

The merged review at main `d35dcc30b44924f79c0510b281ae824aa536848a`
was rechecked against every local gene file before this follow-up. The two
provider-only citations, PMID:15105377 and PMID:23746446, now have verified,
unchanged normal-fetch caches from source4 run 36294925088, artifact 10925791130
(ZIP SHA256 `26ba088d1d78146c81fd744fc68aa532f4a9eb2c3dfc4b96cd647fd74624ac81`).
Both include full text; their abstracts and relevant experimental passages
were read. The 2004 paper characterizes cleavage chemistry in affinity-purified
minimal RISC from human HeLa extract, without identifying a purified AGO2
polypeptide as the sole catalytic component in that experiment. The 2013 paper
studies engineered human AGO1/AGO3, with AGO2 structural and domain comparators.
These source scopes are preserved; neither cache creates a new AGO2 assertion.

The prior DNS and missing-record statements above are historical. A fresh
recursive census now finds all 92 cited PMIDs and all cited Reactome records.
The full review YAML, all 267 seeded assertions, actions, five cores, reference
identities, quotations, alternative products and raw/provider files remain
unchanged. This follow-up adds only the two exact caches, provenance notes,
their rendering and a scaffolded history record. Intentional validation
advisories remain separate from the now-closed source gaps.
