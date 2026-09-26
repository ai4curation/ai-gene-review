# ACSL4 annotation audit

## 2026-09-26: identity, baseline and access

This is a substantive audit of the existing COMPLETE human ACSL4 review, performed under the review, annotation-reviewer and core-function-synthesizer instructions. All 51 seeded annotation rows and all 37 references/findings were inspected. The machine-sourced annotation fields remain unchanged. No NEW annotations were added.

ACSL4 is the approved human symbol (HGNC:3571; NCBI Gene 2182; UniProt O60488). Historical symbols include ACS4, FACL4, LACS4, MRX63 and MRX68. The [NCBI gene record](https://www.ncbi.nlm.nih.gov/gene/2182) supplies the HGNC identity; the ClinGen campaign lists the association as Definitive. Alias and symbol searches found no overlapping open ACSL4 review PR. The coordinator's attempted exhaustive open-PR path query timed out with HTTP 504, so an exhaustive repository-wide overlap check is not claimed.

The seven gene files matched authoritative GitHub main at `e0d565bddebefd72f7c1c32562b588f75a893f69` before editing. The review blob was `d2e60977b646187ae1b17058c0a636ddf61ccc15`; the HTML blob was `5236844b28c3c723f5a53e2bb35b84b9ca33e8e9`. Local snapshots and the publication manifest record the remaining source blobs. There was no pre-existing notes file.

The required default Falcon research launch (1200-second observation allowance, with perplexity-lite fallback) ran alongside publication caching. The first attempt failed when uvx tried to create its tool environment in a protected default directory. A supported per-process retry used `UV_TOOL_DIR=/tmp/aigr-uv-tools`, `UV_TOOL_BIN_DIR=/tmp/aigr-uv-bin`, and `UV_CACHE_DIR=/tmp/aigr-uv-cache`. Both provider invocations then failed before research because their dependency installation could not resolve PyPI. No fresh report was produced and no provider process remained live. The existing genuine Falcon, Cyberian and Perplexity reports remain unedited; they are research leads, not substitutes for primary evidence. `just fetch-gene-pmids human ACSL4` reported all 26 PMIDs already cached; no publication or Reactome cache was changed.

The local cache is full text for PMID:29450800, PMID:34800366 and PMID:38720107. The other 23 PMID caches are abstract-only, including files with duplicated abstract material under a full-text-looking heading. Their `full_text_unavailable: true` flags reflect local cache availability even where a separate external full-text route was successfully read. External access is documented below rather than misrepresented as a cache update.

## Biochemical scope and ontology checks

The human cDNA study [PMID:9598324](https://pubmed.ncbi.nlm.nih.gov/9598324/) directly establishes a functional arachidonate-preferring fatty acid-CoA ligase. The rat enzyme in [PMID:9096315](https://pubmed.ncbi.nlm.nih.gov/9096315/) was expressed in bacteria and purified; it preferred arachidonate/EPA and retained lower-affinity palmitate activity. That study must not be described as a purified-human experiment.

The full publisher article for [PMID:31061331](https://www.jstage.jst.go.jp/article/bpb/42/5/42_b19-00085/_html/-char/en) was read, including Methods, Fig. 2/product assays and Results. Human ACSL4 variants cloned from Caco-2 cells were expressed in Sf9 cells and partially purified. Both produced acyl-CoAs from AA/EPA (C20) and DHA/adrenate (C22). The cellular expression host does not change the species of the human enzyme. The same paper explicitly leaves membrane topology unresolved after detecting both variants in pellet and supernatant. It does not justify a universal integral-membrane/type-III claim.

Live GO definitions were checked rather than inferred from common lipid terminology:

- [GO:0004467](https://amigo.geneontology.org/amigo/term/GO:0004467): “A long-chain fatty acid has an aliphatic tail containing 13 to 22 carbons.” C22 activity therefore fits the long-chain enzyme core.
- [GO:0031957](https://amigo.geneontology.org/amigo/term/GO:0031957): “A very long-chain fatty acid has an aliphatic tail containing more than 22 carbons.” Its parent is fatty acid-CoA ligase activity, GO:0120515. C22 substrates do not establish the >22-carbon activity.
- [GO:0035338](https://amigo.geneontology.org/amigo/term/GO:0035338) describes production of long-chain CoA thioesters in the same 13–22-carbon range.
- [GO:0006633](https://amigo.geneontology.org/amigo/term/GO:0006633) includes fatty-acid elongation (GO:0030497). A participating activation catalyst need not itself perform the carbon-condensation step.
- [GO:0005737](https://amigo.geneontology.org/amigo/term/GO:0005737): “The contents of a cell excluding the plasma membrane and nucleus, but including other subcellular structures.” Cytoplasm is compatible with ER/mitochondrial association; it is not synonymous with soluble cytosol.
- [GO:0160020](https://amigo.geneontology.org/amigo/term/GO:0160020) covers positive regulation of ferroptosis. ACSL4-dependent production of peroxidation-sensitive lipid substrates supports this existing regulatory term without requiring universal indispensability.

The original full patient study [PMID:11889465](https://pubmed.ncbi.nlm.nih.gov/11889465/) was not recovered. The [Siena repository](https://usiena-air.unisi.it/handle/11365/33459) lists restricted full text. Its accessible abstract reports reduced enzyme activity in patient lymphoblastoid cells but does not identify a >22-carbon substrate. The GO:0031957 IMP row is therefore UNDECIDED. Neither rejecting that activity nor accepting it from C22 assays would be justified. The independent broad enzyme activity and broad cytoplasm assignment remain compatible with positive human evidence and curator judgment.

The two previous core entries described overlapping broad/specific versions of one ligase activity. They are now one core, using GO:0004467 to cover the actual HUFA substrate range, linked to long-chain acyl-CoA production and positive regulation of ferroptosis. Existing arachidonate-specific annotations remain accepted. Broad keyword mappings for nucleotide binding and ligase activity are refined to ATP binding and long-chain fatty acid-CoA ligase; two broad lipid-metabolism rows are refined to long-chain fatty acid metabolism. Broad fatty-acid metabolism itself remains acceptable pathway coverage.

## Participation in fatty-acid biosynthesis

The IEA donor is mouse Acsl4 (UniProt Q9QUJ7; ENSMUSP00000033634), not an assumed paralog. The precise original donor experiment for the biosynthesis assertion was not recovered, and the corresponding propagation source status remains UNRESOLVED.

The target assertion nevertheless has positive human pathway support. Cached [R-HSA-548843](https://reactome.org/content/detail/R-HSA-548843) explicitly names ACSL4 as the catalyst that activates arachidonate at the ER. Its parent [R-HSA-75876](https://reactome.org/content/detail/R-HSA-75876) explicitly places ACSL activation before ELOVL condensation and includes the arachidonate activation step. ACSL4 is doing reaction chemistry within this pathway, not simply being an input or being consumed. Retain the existing GO:0006633 annotation, with a bounded activation-in-elongation rationale. Do not describe ACSL4 as a carbon-condensing fatty-acid synthase or create a NEW process annotation. The coordinator independently read both cached Reactome records and agreed with this distinction.

The pathway's prose uses a >20-carbon convention for “very long-chain,” unlike GO:0031957's >22 definition. Its name or membership cannot establish ligation of a >22-carbon free fatty acid. The direct C20 arachidonate activation event still supports the existing long-chain acyl-CoA biosynthesis annotation.

## Localization: assay-specific resolution

For [PMID:24269233](https://eprints.lib.hokudai.ac.jp/dspace/bitstream/2115/54775/1/WoS_64262_Kihara.pdf), the Hokkaido University author manuscript was read. Results 3.1 identifies human ACSL4 among constructs restoring deficient sphingolipid-to-glycerophospholipid metabolism in yeast. Results 3.2 distinguishes human variant 1 mainly at the plasma membrane, with an ER pool, from variant 2 predominantly at the ER in HeLa cells. The manuscript also identifies the ACSL4 enzyme tested in the preceding PMID:22633490 work. The latter's ALDH3A2-focused title is not evidence of an ACSL4 misattribution. ACSL3-specific droplet imaging in this manuscript is not reassigned to ACSL4.

The cached full [PMID:29450800](https://pmc.ncbi.nlm.nih.gov/articles/PMC6182735/) distinguishes endogenous ACSL4's calnexin-associated ER distribution from ACSL3 trafficking compartments using HT1080/MCF-7 fractionation and confocal microscopy. This is stronger ER-specific evidence than the original general cloning quote or provider location summary.

The full [PMID:23455425 primary Nature article](https://doczz.net/doc/8162647/autophagosomes-form-at-er-mitochondria-contact-sites) was recovered as an external transcription, matched by title/authors/DOI. Fig. 1c and adjacent Results identify HEK293 MAM fractions using FACL4 and calnexin. This is the direct FACL4/ACSL4 basis for retaining ER–mitochondria contact-site localization. The local abstract alone does not contain the result. No autophagy-process annotation is inferred from use as a fraction marker.

In cached full [PMID:38720107](https://pubmed.ncbi.nlm.nih.gov/38720107/), mitochondrial subfractionation/immunoelectron microscopy and imaging support outer-membrane ACSL4 with additional intermembrane-space signal. The review quotes the actual ACSL4 localization result instead of a generic statement about PCK2. The same study directly measures AA-d8-CoA formation by purified human-cell ACSL4 and tests activity-dependent ferroptosis susceptibility. PCK2 is the kinase; ACSL4 is its ligase substrate.

The MitoCoP HTP row retains **mitochondrion** resolution. Although full PMID:34800366 is cached, the ACSL4-specific supplementary identification was not independently extracted. Independent human-cell localization supports the compatible curated assignment, but does not turn the HTP source into an outer-membrane experiment. Likewise, the YTS membrane proteome (PMID:19946888) remains **membrane**, without arbitrary ER refinement or integral-topology inference.

The original HuH7 droplet proteome (PMID:14741744) is abstract-only and prominently describes ACSL3. The [same authors' later primary JLR article](https://www.jlr.org/article/S0022-2275%2820%2942556-8/fulltext), as exposed in indexed Discussion text, explicitly compares greater droplet ACSL3 abundance with ACSL4 and cites the original study. This corroborates the compatible curated ACSL4 IDA location; it does not mean the original full identification was recovered. Retain the droplet rows with explicit curator deference rather than declaring an ACSL3 name-confusion error.

For urinary-exosome PMID:19056867 and B-cell-exosome PMID:20458337, neither full ACSL4 entry was recovered. General abstract descriptions of 1132 and 539 protein surveys do not establish the target-specific detection. Both rows are UNDECIDED. There is also no basis for the old contamination/incidental-cargo assertions.

## Contextual processes and citation integrity

Human wild-type ACSL4 rescues Drosophila neural/glial and wiring defects in the original abstract of PMID:19617635; patient variants fail rescue. The IBA neuronal-differentiation row remains non-core because it is a developmental consequence in a conserved context, not because the only evidence is disease association. PMID:27656110 provides additional fly lipid/synapse context. PAINT source reviews use ancestral PTN nodes and do not mistake target self-evidence or a short donor list for circularity or weak ancestry.

The insulin-secretion ISS donor O35547 is **rat** Acsl4. The [original rat insulinoma-cell study](https://pmc.ncbi.nlm.nih.gov/articles/PMC3724621/) and [PubMed figure captions](https://pubmed.ncbi.nlm.nih.gov/23766516/) identify knockdown-dependent changes in stimulated insulin secretion (Fig. 2). These were web-only source checks; no machine cache was created. The cached human UniProt record explicitly assigns this effect by similarity to O35547. Retain the contextual non-core annotation without converting it into a direct secretory mechanism.

PMID:10669417 genuinely resolves to the PLC/PI3K chemoattractant-signaling study in the cached PubMed metadata. Its abstract concerns mouse experiments, but its full ACSL4-linked experiment could not be inspected. The citation-support question remains UNVERIFIED, not MISCITED or WRONG_IDENTIFIER. The original IDA/reference fields are unchanged, and the clearly established human enzyme activity is accepted using independent human experiments.

PMID:12525535 now has a result-bearing P375L/activity quote instead of its title. Primary references retain species and assay scope. The review of ACSL4 (PMID:31306767) is labeled background synthesis. PMID:31504388 is a mouse steroidogenic tissue knockout affecting ester stores, not evidence to create a direct steroid-synthesis core. Recent neuronal, wound and fibroblast disease studies are contextual; the internally difficult direction-of-effect wording in the PMID:39892437 abstract is left unverified and is not used to establish the core regulatory direction.

Provider-only findings and supporting quotes were removed from the curated evidence. In particular, the Cyberian catalytic-triad/residue and blanket localization claims were not accepted simply because a report stated them. Its original file remains immutable and listed as low-relevance, unverified research provenance. Primary observations now support the core and annotation reasons.

## Outcome and verification

Final actions across all 51 original rows: **41 ACCEPT, 4 MODIFY, 3 KEEP_AS_NON_CORE, 3 UNDECIDED**. No rows are removed or newly asserted. All 37 references have manual source assessments. The three unresolved rows are the >22-carbon activity and two exosome localizations. The review status remains COMPLETE because all rows have decisions; COMPLETE does not mean every underlying experiment was accessible.

Source-field equality was checked against the original parsed review for every row, excluding only the editable `review` section. Every primary supporting quote and finding quote was checked as a normalized verbatim substring of its unchanged cache. YAML trailing whitespace was stripped with parsed-YAML equality asserted. Gene validation, history validation and rendering results are recorded in the matching append-only history and the publication manifest.

Final checks passed: `just validate human ACSL4`, `just validate-history history/genes/human/ACSL4/2026-09-26T224730Z-codex-142634.yaml`, and `just render human ACSL4`. The only gene warning recommends citing available deep-research reports; primary evidence was intentionally used instead. There are no validation errors. The four-file publication manifest is `/tmp/ACSL4-audit-manifest.json`.

### Coordinator review and publication gate

The coordinator independently inspected all 51 annotation judgments, the catalytic core, all reference assessments and this source-access record. The biological audit passed. A citation-wide check found that PMID:23766516, cited above for the rat insulin-secretion donor, is not in the local publication cache even though every PMID in the review YAML is cached. A normal `ai-gene-review fetch-pmid 23766516` retry on 2026-09-26 returned a DNS resolution failure and cached 0/1 records. No cache was fabricated. This citation remains explicit and the PR must stay **draft** until its required cache is recovered; gene validation alone does not inspect every citation in notes.
