# Bacterial assimilatory nitrate reduction: audit31 foundation

## Scope and preservation, 2026-10-27

This foundation establishes identities and normally fetched inputs for subsequent gene and module review. It does not adjudicate the seeded annotations. The original module YAML is unchanged. All 14 original accessions are retained; seven partners complete native reduction systems without adding unrelated candidate nitrate reductases. E. coli remains a physiological comparison whose respiratory upstream context must be represented explicitly.

The clean worktree began at `46d71eb5cd1b628c3edd69c37d776bb9c6768d4b`; `uv sync` completed. Existing PSEPK records were snapshotted before acquisition and never refreshed. New records were created by the normal `ai-gene-review fetch-gene` command with explicit accessions. The ignored `.cache/module-audit-logs/nitrate-foundation/` directory contains original identity responses, fetch logs, `existing-before.json`, `original14-seeded-baseline.json`, and the consolidated `panel21-seeded-baseline.json`. Baselines retain full seeded documents and raw-file SHA256 values. The consolidated panel has 170 initial annotation rows and 42 immutable UniProt/GOA files.

| Organism | Product | Accession | Role to review | Original exemplar |
|---|---|---|---|---|
| ECOLI | nirB | P08201 | NADH-dependent nitrite reductase large subunit | yes |
| ECOLI | nirD | P0A9I8 | Nitrite reductase small subunit | yes |
| ECOLI | narU | P37758 | Nitrate/nitrite transport, respiratory context | yes |
| SYNE7 | nrtA | P38043 | ABC uptake substrate-binding component | yes |
| SYNE7 | nrtB | P38044 | ABC uptake membrane component | yes |
| SYNE7 | nrtC | P38045 | ABC uptake ATPase component | yes |
| SYNE7 | nrtD | P38046 | ABC uptake ATPase component | yes |
| SYNE7 | narB | P39458 | Ferredoxin-dependent nitrate reductase | yes |
| SYNE7 | nirA | P39661 | Ferredoxin-dependent nitrite reductase | added |
| BACSU | nasA | P42432 | Nitrate uptake porter | added |
| BACSU | nasB | P42433 | Nitrate reductase electron-transfer subunit | yes |
| BACSU | nasC | P42434 | Nitrate reductase catalytic subunit | yes |
| BACSU | nasD | P42435 | Nitrite reductase large subunit | added |
| BACSU | nasE | P42436 | Nitrite reductase small subunit | added |
| PSEPK | nasA | Q88L43 | Nitrate/nitrite porter PP_2092 | yes |
| PSEPK | PP_1703 | Q88M71 | Fused nitrate reductase candidate | yes |
| PSEPK | nirB | Q88M69 | Nitrite reductase large subunit | yes |
| PSEPK | nirD | Q88M68 | Nitrite reductase small subunit | yes |
| MYCS2 | nasN | A4ZHT3 | Experimentally identified fused nitrate reductase | added |
| MYCS2 | nirB | A0QPK2 | Nitrite reductase large subunit, MSMEG_0427 | added |
| MYCS2 | MSMEG_0428 | A0QPK3 | Nitrite reductase small-subunit homolog | added |

UniProt species identities are ECOLI taxon 83333 (K-12), SYNE7 1140 (PCC 7942), BACSU 224308 (168), PSEPK 160488 (KT2440), and MYCS2 246196 (mc2 155). No `nirD` gene symbol was invented for A0QPK3: its current record supplies an ordered locus only. The MYCS2 panel starts at intracellular nitrate until a native uptake route is established. The original P42433/P42434 proteins are Bacillus NasB/NasC, not Klebsiella proteins.

## NasN accession reconciliation

The experimentally studied MYCS2 `MSMEG_4206` is annotated as a pseudogene in CP000480.1. Searching that name alone therefore misses the intact protein. PMID:32111737 reports a missing guanine at position 1850 in the old sequence. PMID:33471823 independently maps the newer `MSMEI_4108` name to `MSMEG_4206` and the corrected accession DQ866862, and confirms the error by Sanger sequencing in its experimental strain. Its full text states: “A BLAST search revealed that MSMEI_4108 corresponds to MSMEG_4206” and “based on the accession number (DQ866862), it has been shown that this annotation is due to a sequencing error”.

The reproducible script in `bacterial_assimilatory_nitrate_reduction-source-analysis/check_nasN_identity.py` compares the downloaded reference CDS with DQ866862.1 and translates the latter. The only nucleotide difference is insertion of G at corrected position 1850; the corrected 4056-nucleotide sequence encodes 1351 amino acids that exactly match UniProt A4ZHT3. DQ866862 uses the older locus `MSMEG4211` and protein accession ABJ96323.1. The adjacent JSON records input URLs and sequence hashes. The large downloaded genome remains in the ignored acquisition cache.

Current A4ZHT3 calls this protein assimilatory sulfite reductase (NADPH), with an ARBA-supported reaction and EC 1.8.1.2. This label must be reviewed against the direct NasN experiments, not accepted from the protein name. Its PANTHER cross-reference is PTHR43105:SF9; the official name is NADPH-FE(3+) OXIDOREDUCTASE SUBUNIT ALPHA. That surprising label neither establishes sulfite chemistry nor licenses relabeling the family. Family/member verification remains part of module review.

## Reviewed literature and native boundaries

PMID:32111737, full article recovered through the normal PMC URL fetch, supplies direct native genetics and purified NasN biochemistry. Deleting nasN prevents aerobic growth with nitrate as the nitrogen source while leaving nitrite/ammonium utilization intact; complementation restores nitrate use. The protein joins a molybdenum/iron-sulfur catalytic region to a diflavin electron-transfer region and is monomeric in the reported preparation. NADPH is preferred, but NADH supports measurable turnover. Oxygen tolerance is relative to the comparator NasAC preparation: the protein remains oxygen sensitive, and biochemical assays were generally anaerobic. Do not turn aerobic physiological use into oxygen-insensitive catalysis. GlnR promoter binding and regulation describe the regulator, not a transcription-factor activity of NasN. Comparative rescue by Amycolatopsis NasAC does not establish KT2440 enzyme specificity or kinetics.

PMID:33471823, full text, independently supports MSMEG_4206 as the nitrate reductase used under its aerobic nitrate-assimilation conditions. Other candidate loci, including narB and narGHJI, are not interchangeable with this demonstrated function. The body clarifies that an individual MSMEG_2237 deletion was not obtained, although a combined deletion was tested; the abstract's compressed wording should not be expanded into an assertion that every single knockout succeeded. The tested anaerobic regime did not show nitrate utilization or nitrate-dependent survival benefits. This is a condition-bounded result, not proof of universal inactivity of all alternative enzymes.

PMID:10542156, the 1999 review, was read in the recovered full PMC page, especially its assimilatory-enzyme, gene-organization, transport, and physiological distinction sections. It distinguishes cyanobacterial ferredoxin enzymes from heterotrophic NADH systems, explicitly identifies Bacillus NasB as diaphorase and NasC as catalytic, and describes NasDE use downstream of respiratory Nar under anaerobic conditions. The historical summary table foregrounds E. coli NirBD redox balance and detoxification. It must not be used to deny newer native E. coli assimilation evidence: the ECOLI reviewer has identified PMID:34323689 experiments using nitrate as both sole electron acceptor and sole nitrogen source. Respiratory nitrate reduction can therefore feed biosynthesis. Neither that result nor a general review makes NarU/NirBD an autonomous assimilatory nitrate-reductase pathway.

PMID:24467397, the broad molybdenum-enzyme review, was read specifically in section 5.5.3 on assimilatory Nas. Its cross-taxon nomenclature and enzyme architecture provide a useful map; unrelated sections of this very large review were not assessed. Its discussion of ferredoxin interactions and artificial viologen assays helps distinguish physiological donor specificity from an assay bypass. Primary corroboration is supplied by NasN studies above and by native cyanobacterial sources assigned to the SYNE7 reviewer. Review-level architecture should not be the only evidence on a specific module leaf.

PMID:7868621 is presently abstract-level evidence for Bacillus nasABCDEF and nitrate/nitrite use as sole nitrogen sources. The PMC page exposes a scanned-PDF link rather than full article text. A normal publisher PDF retrieval was attempted separately; its outcome is in `bacillus-pdf-attempt.log`. Detailed assignments from the review should be checked against the primary paper when accessible.

PMID:25962912, full text, was read for Anabaena maturation biology. Bacterial two-hybrid assays support interaction of NirA with its maturation-associated NirB and of NarB with NarM. This cyanobacterial **NirB is not the heterotrophic NADH nitrite-reductase large subunit**. The authors propose scaffolding/maturation roles; they do not demonstrate that this NirB independently reduces nitrite. Regulation also differs between Anabaena PCC 7120 and SYNE7 PCC 7942. No Anabaena proteins were added to the panel.

PMID:17295914 provides full-text background on corrected interrupted coding sequences in M. smegmatis. Its accessible body explains the resequencing approach, but the specific NasN accession link is supported more directly by PMID:33471823 and the sequence reconciliation above. It is not being used as an independent direct NasN catalytic assay.

The 2026 P. putida Y-9 article titled “The nirB and nirD genes are essential for both assimilatory and dissimilatory reduction of nitrite in Pseudomonas putida Y-9 under aerobic conditions” was located by the coordinator. Normal retrieval of its ScienceDirect URL returned HTTP 403. No mechanistic inference is asserted from its title. Even if recovered, Y-9 must be distinguished from KT2440.

## Acquisition and remaining review work

Canonical PMID caches were obtained with the normal publication pipeline. PMC URL caches were obtained with `ReferenceFetcher.fetch('url:' + url)` using `ReferenceValidationConfig(cache_dir=Path('publications'))`. This is the normal URL-fetch API; no publication text was hand-written. The canonical PMID:32111737 cache remains abstract-only; its real full text is `publications/url_https___pmc.ncbi.nlm.nih.gov_articles_PMC7152768__report_xml.md`. The useful full review is `publications/url_https___pmc.ncbi.nlm.nih.gov_articles_PMC94119_.md`. Some other PMC URL attempts produced browser-check pages; those are access failures, not scientific support. The canonical PMID:33471823 and PMID:24467397 caches contain the actual full articles.

Eleven fresh Falcon requests were attempted once across the owned PSEPK/BACSU/MYCS2 records. All failed authentication and created no reports. The existing genuine PSEPK nasA Falcon report was preserved without another request. `provider-decisions.json` and per-gene logs record commands and outcomes; no manually authored file masquerades as provider output. ECOLI and SYNE7 provider attempts are owned by their respective reviewers.

Remaining work includes holistic annotation review of every row, family/member checks, source findings and quotes, native assembly requirements, same-organism route logic, and module-specific validation. In particular, a nitrate-to-ammonium module does not itself model incorporation of ammonium into glutamine/glutamate; any linkage to ammonia assimilation must identify that boundary. Uptake requirements must match the represented extracellular or intracellular input. Mechanism conservation does not justify mixing cyanobacterial NarB with an arbitrary heterotrophic NirBD pair, universal nitrogen-regulatory claims, or identical donor preferences across fusion and multisubunit enzymes.


## Species-native module curation, 2026-10-29

The completed module preserves all 14 original accessions and grounds the full prepared panel of 21 products as exact `GENE_PRODUCT` selectors. Family metadata was read from each immutable UniProt PANTHER cross-reference and matched to the official `interpro/panther/panther.obo` name. The family names are metadata rather than wildcard participants or evidence that every member has the same substrate, electron donor or location. No unsupported PTN/ancestral assertion is retained. In particular, the NADPH-FE(3+) OXIDOREDUCTASE SUBUNIT ALPHA label does not determine the chemistry of NarB, PP_1703 or NasN, and the NirA family name does not imply a cyanobacterial chloroplast.

The required `native_nitrate_to_ammonium_routes` variant set selects one complete species-native implementation. Its route and terminal node identifiers are:

| Route | Uptake | Nitrate reduction | Nitrite reduction |
|---|---|---|---|
| `syne7_route` | `syne7_uptake`: NrtA P38043 + NrtB P38044 + NrtC P38045 + NrtD P38046 | `syne7_nitrate_reduction`: NarB P39458 | `syne7_nitrite_reduction`: NirA P39661 |
| `bacsu_route` | `bacsu_uptake`: NasA P42432 | `bacsu_nitrate_reduction`: NasB P42433 + NasC P42434 | `bacsu_nitrite_reduction`: NasD P42435 + NasE P42436 |
| `psepk_route` | `psepk_uptake`: NasA/PP_2092 Q88L43 | `psepk_nitrate_reduction`: PP_1703 Q88M71 | `psepk_nitrite_reduction`: NirB Q88M69 + NirD Q88M68 |
| `mycs2_route` | No uptake implementation | `mycs2_nitrate_reduction`: NasN A4ZHT3 | `mycs2_nitrite_reduction`: NirB A0QPK2 + MSMEG_0428 A0QPK3 |

All multicomponent steps use native `PROTEIN_COMPLEX` selectors with every role-bearing subunit in `active_units`. The absence of exact stoichiometry is deliberate. The reductions are required within each route. Uptake is optional only at an intracellular-nitrate input boundary; an extracellular-nitrate whole-cell realization must include its exact modeled native uptake node. This is a model requirement, not an assertion that no redundant transporter could exist. MYCS2 has only the intracellular realization and must fail an extracellular scenario. The module stops at ammonium, with no implied glutamine/glutamate incorporation.

`ecoli_respiratory_comparison` is a separate optional context part, not a member of the required complete-route variant set. It contains `ecoli_uptake_comparison` (NarU P37758) and `ecoli_nitrite_reduction_comparison` (NirB P08201 + NirD P0A9I8). There is deliberately no nitrate-to-nitrite continuity edge between them: the upstream respiratory nitrate reductase is known biology outside this panel. PMID:34323689 explicitly establishes nitrate as sole electron acceptor and nitrogen source; the older detoxification framing must not be used to deny assimilation. NarU transport coupling remains unresolved, and NirD's independently supported RelA inhibition is outside this module.

### Evidence and biochemical boundaries

- **PCC 7942:** PMID:9006953 and PMID:8437564 ground NrtABCD transport and its binding, membrane and ATP-binding components. PMID:9341163 and its full institutional PDF ground NrtC-dependent transport/regulation and identify the plasmid-cured PCC 7942 derivative. NarB ferredoxin input is directly supported by PMID:8624415/14871493; PMID:28520412 uses PCC 6803 ferredoxin with recombinant PCC 7942 NarB, not an exclusive native donor pair. NirA's ferredoxin enzyme class combines native sequence/active-site evidence (PMID:8490140) with curated target classification. Native-cell NR/NiR assays in PMID:9341163 used reduced methyl viologen, so they do not establish NirA donor preference against other physiological donors. Neither this NirA nor heterotrophic NirB should be confused with Anabaena's maturation-associated NirB.
- **Bacillus:** The source analysis of the PMID:7868621 publisher PDF records NasA nitrate-specific growth loss despite retained reductase, both NasB/NasC requirements after polarity controls, and artificial methyl-viologen nitrate assays. The canonical cache is abstract-only; the source-analysis findings are not fabricated full-text quotations under that PMID. The full PMID:9765565 body demonstrates that both NasD and NasE are needed, activity is cytosolic, and NADPH activity is less than 10% of NADH activity. Its abstract reverses the anabolic/catabolic ordering of NarGHI and NasBC; that sentence is not propagated. Assays are in JH642 derivatives of the 168 lineage. NasBC therefore uses donor-generic GO:0008940 with the review/domain NADH interpretation stated as inference; NasDE uses its measured primary NADH reaction, GO:0106316.
- **KT2440:** PMID:35285712 supports PP_2092 nitrate uptake by pooled-mutant fitness, not a clean knockout proving universal necessity or measured affinity. Nitrite transport is not asserted. The full PMID:10852866 source and reproducible ENA comparison connect the historical KT2442 724-residue catalytic fragment exactly to Q88M71 residues 1–724; this is not a purified full-fusion assay. GO:0050463 records the inferred NAD(P)H donor class from the fusion architecture without transferring MYCS2 NADPH preference or monomeric state. PMID:38000372 provides native nirBD expression/NirB protein/lysate activity, but the assay uses methyl viologen. The native NirB/NirD pair is a conserved assembly inference from these observations and target classifications, not direct KT2440 subunit-minus reconstitution. Y-9 deletion/isotope results are not substituted for KT2440 experiments.
- **mc2 155:** The source-sequence proof reconciles corrected DQ866862/MSMEG_4206 with all 1351 residues of A4ZHT3. PMID:32111737 full text directly supports NasN genetics, monomeric biochemistry, cytoplasmic activity and 26-fold NADPH-over-NADH preference. The main module reaction is GO:0050464. The protein remains oxygen-sensitive despite comparative tolerance. Native NirBD expression under GlnR control is supported by DOI:10.1186/1471-2164-14-301; its historical NarGHJI attribution is superseded by NasN studies and is not reused. Downstream activity, NAD(P)H class and NirB/MSMEG_0428 pairing are inferred from target-specific conserved classifications and expression, with no claimed purified native activity or direct small-subunit requirement experiment.

Every activity and connection has source evidence. The connections explicitly share nitrate or nitrite chemical entities, with location changes for uptake and matching donor/acceptor names for reductions. This continuity asserts no physical reductase supercomplex or substrate channeling. No new knowledge-gap entries were invented for missing panel members, source-access limitations or incomplete ontology coverage.

The module's source registry contains 45 entries with 63 manually selected findings: 21 immutable target UniProt records, 21 publication manifestations (including a full-text URL manifestation of PMID:9341163), and three source-analysis records. Quotes are extracted as literal cached spans. The module author checked all 21 selectors against their actual PANTHER DR IDs and official names, and checked the complete-route and comparison structure without running the coordinator-owned validators. The coordinator will independently audit the module, test native route requirements, validate and render it. Only this module, this appended journal and one helper-generated module history belong to this curation package; genes, raw sources, source-analysis outputs and git state were not edited.


### Integration verification, 2026-10-29

Independent final review clarified that the purified NasN preparation was heterologously expressed. Module findings now explicitly distinguish recombinant M. smegmatis protein biochemistry from native-strain genetics; no native purification is claimed. The production module validator and 80 native-route, incomplete-assembly and input-boundary cases passed. Subunit-role NO_FUNCTION_ID advisories are expected: the whole catalytic activity belongs to the complete assembly, while individual roles remain descriptive. The source-analysis README documents reproduction and the oracle limits. Full repository validation is recorded separately in the PR checks.

The audit YAML tables and generated results are stored under `analysis/module_audits/bacterial_assimilatory_nitrate_reduction/`. This keeps them out of recursive module discovery, which reserves YAML under `modules/` for ModuleReview records. Reproduction scripts and the accession proof remain in the module source-analysis directory.
