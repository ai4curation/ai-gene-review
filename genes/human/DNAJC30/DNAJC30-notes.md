# DNAJC30 (WBSCR18) research notes

## Identity
- UniProt Q96LL9 (DJC30_HUMAN), 226 aa precursor. HGNC:16410. Synonym WBSCR18 (Williams-Beuren syndrome chromosomal region 18 protein). Located in 7q11.23 WBS critical region.
- Mitochondrial J-domain (HSP40/DnaJ subfamily C) protein. N-terminal mitochondrial transit peptide (1-38); J domain 49-114; single-pass transmembrane helix 208-225. Inner mitochondrial membrane.

## Function (well-supported)
- Mitochondrial inner-membrane protein; auxiliary component of the ATP synthase machinery; facilitates ATP synthesis.
  [PMID:30318146 "we identify DNAJC30 as an auxiliary component of ATP-synthase machinery"; "the 7q11.23 protein DNAJC30, which interacts with mitochondrial ATP-synthase machinery."]
  [UniProt FUNCTION "Associates with the ATP synthase complex and facilitates ATP synthesis (By similarity)."]
- Chaperone in complex I (NADH:ubiquinone oxidoreductase) "repair": facilitates the efficient exchange/turnover of complex I N-module subunits damaged by reactive oxygen species, integral to a complex I repair mechanism; contributes to complex I functional efficiency.
  [PMID:33465056 "DNAJC30 is a chaperone protein needed for the efficient exchange of complex I subunits exposed to reactive oxygen species and integral to a mitochondrial complex I repair mechanism"]
  [UniProt FUNCTION "May be a chaperone protein involved in the turnover of the subunits of mitochondrial complex I N-module. It facilitates the degradation of N-module subunits damaged by oxidative stress, and contributes to complex I functional efficiency (PubMed:33465056)."]

## Interactions
- Direct interaction with MT-ATP6 (P00846) and ATP5MC2 (Q06055); associates with ATP synthase complex (PMID:30318146).
- Large set of binary HuRI interactions (PMID:32296183) with mostly membrane proteins (AQP6, BEST2, EBP, MGST2, MRM1, etc.) — likely membrane-protein Y2H artifacts, uninformative bare protein binding.

## Localization
- Mitochondrion inner membrane (IDA, PMID:30318146); single-pass membrane protein.
- HTP mitochondrion (PMID:34800366, FlyBase high-throughput).
- Highly expressed in brain; enriched in pyramidal neurons.

## Disease
- Autosomal-recessive Leber hereditary optic neuropathy (LHONAR1/arLHON, MIM:619382): biallelic DNAJC30 mutations (e.g. Y51C, P78S, L101Q) recapitulate all hallmarks of mtDNA LHON (incomplete penetrance, male predominance, idebenone responsivity). Variants reduce turnover of complex I N-module subunits and impair complex I function.
  [PMID:33465056 "We describe biallelic mutations in a nuclear encoded gene, DNAJC30, in 33 unsolved patients from 29 families and establish an autosomal recessive mode of inheritance for LHON (arLHON)"]
- DNAJC30 deletion contributes to mitochondrial dysfunction in Williams-Beuren syndrome neurodevelopmental phenotypes (PMID:30318146).

## GO annotation review reasoning
- mitochondrial inner membrane (IDA, IEA) — ACCEPT (core localization, experimentally demonstrated).
- mitochondrion (HTP) — ACCEPT (consistent, less specific).
- regulation of mitochondrial ATP synthesis coupled proton transport (ISS/IEA from mouse P59041) — ACCEPT; supported by ATP synthase association and facilitation of ATP synthesis.
- brain development (ISS/IEA) — KEEP_AS_NON_CORE; reflects neurodevelopmental phenotype/high brain expression but is a downstream pleiotropic outcome, not the molecular core.
- protein binding (IPI) — the MT-ATP6/ATP5MC2 interactions (PMID:30318146) are biologically meaningful (ATP synthase) — could MODIFY toward a specific term; the HuRI set (PMID:32296183) is uninformative -> KEEP_AS_NON_CORE.
- Core MF: chaperone/co-chaperone activity in complex I subunit exchange + ATP synthase auxiliary subunit. Best MF terms: protein-folding chaperone binding / unfolded protein binding not directly shown; the gene acts as a holdase/chaperone facilitating subunit exchange. The clearest experimentally-grounded MF for the ATP-synthase role is enzyme/structural association; for complex I it's chaperone activity. Use GO:0051082 unfolded protein binding? Not demonstrated. Better core: biological processes (complex I repair / ATP synthesis regulation). For MF, GO:0140662? (ATP-dependent protein folding chaperone) is not apt (it's not ATP-dependent foldase). Will use a chaperone-binding/holdase framing carefully.

## GO:0051082 migration (2026-09-27)

The complex I repair core function carries no molecular-function term. GO:0051082 is obsolete, and whether DNAJC30 binds damaged N-module subunits directly or acts through HSP70 has not been established, so no holdase or carrier term is supported.


## Evidence audit — 2026-10-17

This addition supersedes the earlier statements that the HuRI interactions are likely artifacts, that inner-membrane immunogold was a human experiment, and that isolated DNAJC30 loss universally disrupts ATP-synthase dimers. The prior notes remain above as a historical record. The [source guide](DNAJC30-source-guide.md) gives public primary-source and measurement locators.

The two functional units remain distinct: transient participation in repair of assembled complex I, and binding to mitochondrial ATP synthase. The first has no assigned molecular-function term because the extraction, delivery or chaperone step has not been directly resolved. The second is refined to GO:0140260. No ATPase, protease or HSP70-stimulatory activity is inferred from the J-domain. The ATP-production phenotype is supported in mouse knockout conditions; the 2021 human-cell study did not reproduce complex-V defects. The earlier dimer/supercomplex claim arose from multigene Williams-Beuren samples and is not established as an isolated DNAJC30 effect. [PMID:30318146](https://pmc.ncbi.nlm.nih.gov/articles/PMC6459420/), [PMID:33465056](https://pmc.ncbi.nlm.nih.gov/articles/PMC7954600/).

The human MitoCoP identification is resolved to Q96LL9, Table S1A worksheet row 322. It supports mitochondrial membrane association; the inner-membrane refinement also uses independent localization. This replaces the unsupported historical attribution of that HTP observation to FlyBase. The 2018 immunogold specimen was macaque brain; human tissue association/fractionation and mouse functional experiments remain separately identified.

All 23 current HuRI partner products have positive validated two-hybrid records. Their diverse classes and construct limitations are recorded in the guide. A membrane-protein annotation alone is not evidence of an artifact. The grouped protein-binding assertion remains non-core; no common physiological mechanism or activity is assigned to the entire panel.

One official 226-residue precursor is represented. The predicted transit peptide (1–38), mature chain (39–226), J-domain (49–114) and membrane segment (208–225) are sequence features, not additional splice products. There is no demonstrated HSP70-activation assay in the sources used here.

The nine historical GOA assertion triples match the current 32 participant-resolved rows. Every historical source dictionary is retained, including the separately authored GO:0034367 proposal inherited from [PR #4809](https://github.com/ai4curation/ai-gene-review/pull/4809). The proposal is retained on physical participation and selective subunit-turnover evidence, not on absence of an annotation from other proteins. No additional NEW assertion or source retirement is introduced. The original GOA, UniProt, publication caches, generated PN notes and three history records remain unchanged; fresh machine exports are retained as provenance. The PN notes are a historical generated snapshot, not the updated functional assessment.

Ordinary deep research was attempted: Falcon authentication failed and the configured fallback returned an insufficient-quota error. No provider report was fabricated. Manual primary-source and official-record review supplies the evidence above. Duplicate YAML quotations were removed; this addition introduces no new publication quotation and preserves the earlier notes verbatim.

## Review follow-up — 2026-10-17

The two GO:1905706 assertions remain ACCEPT and the existing regulatory process is now explicit on the ATP-synthase-binding core. This preserves a positive biological role rather than treating context dependence as a reason to demote it. In the [2018 original](https://pmc.ncbi.nlm.nih.gov/articles/PMC6459420/), Figure 4F and the ATP-production Methods measure substrate-driven output from mouse cortical mitochondria with malate, pyruvate and ADP. These experiments do not isolate direct modulation of complex V from upstream respiratory-chain effects. Native human complex immunoprecipitation and subunit-binding experiments are complementary evidence, not proof that the association causes the ATP-output phenotype. The [2021 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC7954600/) found no complex-V defect in its tested human conditions. The causal connection remains open, and multigene Williams-Beuren sample effects are not attributed solely to DNAJC30.

Short exact anchors now mark the inherited remodeling proposal, both core units, one regulatory assertion, the HuRI assay and the UniProt curated-function finding. Each excerpt appears once; other support entries reuse the reference without repeating the quote. The new excerpts total 19 words from PMID:33465056, 13 from PMID:30318146, 8 from PMID:32296183 and 5 from UniProt. The earlier notes remain an unchanged historical prefix, including their longer quotations; these new-excerpt totals do not claim that the historical file aggregate was within 25 words per source. The curated UniProt FUNCTION interpretation is retained alongside its product-feature finding and remains distinct from a directly reconstituted repair mechanism.

The [MitoCoP extract](DNAJC30-bioinformatics/MitoCoP-DNAJC30.json), [source provenance](DNAJC30-bioinformatics/source-manifest.json) and [reproduction script](DNAJC30-bioinformatics/reproduce.py) expose the actual target measurements from the original Table S1 workbook. They provide data provenance, not independent support for the biological conclusions. No source workbook, machine cache, provider output, historical source assertion or product was changed. The inherited GO:0034367 NEW proposal is preserved; no further annotation is proposed. DRAFT remains the expected status while the project-authorized positive generic-binding assertion produces its advisory.
