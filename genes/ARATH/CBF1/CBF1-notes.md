# CBF1 / DREB1B (At4g25490, UniProt P93835) — curation notes

## Identity
- Arabidopsis thaliana CBF1, a.k.a. DREB1B, ERF029; AP2/ERF transcription factor family, ERF subfamily.
- 213 aa; single AP2/ERF DNA-binding domain (residues 47–104), predicted NLS (32–44), acidic C-terminal activation domain.
- Member of the CBF/DREB1 cold-induced subfamily: CBF1/DREB1B, CBF2/DREB1C, CBF3/DREB1A, arrayed in tandem on chromosome 4 [PMID:9735350 "isolated DREB1A and 2 related genes, DREB1B (= CBF1) and DREB1C. These were arrayed in the order B, A, C in an 8.7 kb region of Arabidopsis chromosome 4"].

## Molecular function
- Sequence-specific DNA-binding transcriptional activator. Binds the C-repeat/DRE element (5'-[AG]CCGAC-3', CRT/DRE) in COR-gene promoters.
- DNA binding shown directly by gel-shift with recombinant CBF1; binds CRT/DRE but not mutant element [PMID:9023378 "Binding of CBF1 to the C-repeat/DRE was demonstrated in gel shift assays using recombinant CBF1 protein expressed in Escherichia coli"].
- Transactivation shown in yeast: CBF1 activates reporters driven by CRT/DRE but not mutated element [PMID:9023378 "expression of CBF1 in yeast was found to activate transcription of reporter genes containing the C-repeat/DRE as an upstream activator sequence but not mutant versions of the DNA element"].
- DNA-binding is via the AP2 domain [PMID:9023378 "the function of the AP2 domain is DNA binding"; "Presumably, the binding of CBF1 to the C-repeat/DRE involves the AP2 domain"].
- A related DREB1/DREB2 study confirms specific DRE binding and transactivation in plant cells (protoplasts) for the DREB1 family [PMID:9707537 "Both the DREB1A and DREB2A proteins specifically bound to the DRE sequence in vitro and activated the transcription of the b-glucuronidase reporter gene driven by the DRE sequence in Arabidopsis leaf protoplasts"].

## Biological process
- Master regulator of the CBF cold-response regulon; drives COR (cold-regulated) gene expression.
- CBF1 overexpression induces COR genes and increases freezing tolerance of non-acclimated plants [PMID:9525853 "Increased expression of Arabidopsis CBF1 ... induced COR gene expression and increased the freezing tolerance of nonacclimated Arabidopsis plants. We conclude that CBF1 is a likely regulator of the cold acclimation response"].
- Loss-of-function (RNAi/antisense): CBF1 (with CBF3) is a positive regulator of cold acclimation; CBF1/CBF3 RNAi lines are defective in cold acclimation [PMID:18093929 "CBF1 and CBF3 ... positively regulate cold acclimation by activating the same subset of CBF-target genes"; "CBF1 and CBF3 RNAi lines are defective in cold acclimation but are not affected in their constitutive freezing tolerance"].
- CBF1/DREB1 genes are induced mainly by cold, not osmotic stress, in leaves/roots/stems [PMID:9735350 "the 3 DREB1 genes are induced mainly by cold stress but not by osmotic stress in leaves, roots, and stems"].
- The CRT/DRE element stimulates transcription in response to both low temperature and water deficit [PMID:9023378 title/abstract; "likely to have a role in cold- and dehydration-regulated gene expression in Arabidopsis"].
- DREB1 (cold) vs DREB2 (drought) pathways are largely separated; DREB1/CBF is the cold/low-temperature arm [PMID:9707537 "two independent families of DREB proteins, DREB1 and DREB2, function as trans-acting factors in two separate signal transduction pathways under low-temperature and dehydration conditions, respectively"].

## Localization
- Nuclear (consistent with TF function, predicted NLS). UniProt: Nucleus (PROSITE-ProRule). 14-3-3 interaction occurs "in the nucleus upon freezing" [UniProt SUBUNIT]. No direct experimental sub-cellular localization assay found in cached refs; nucleus is well-supported by function + sequence.

## Protein interactions / regulation
- 14-3-3 (GRF) proteins: CBF proteins interact with phosphorylated 14-3-3 in the nucleus, which destabilizes CBFs to fine-tune cold signaling [PMID:28344081 "they interact with and destabilize the key cold-responsive C-repeat-binding factor (CBF) proteins"]. GOA lists IPI to GRF1/3/5/6/7/9/10 (P42643/P42644/P42645/P48347/P48349/Q96299/Q96300).
- ADA2/GCN5 SAGA-like coactivator: the DNA-binding domain of CBF1 binds Arabidopsis ADA2 proteins directly; implicates SAGA-like coactivator in CBF1-driven COR expression [PMID:16603259 "the DNA-binding domain of CBF1 ... can bind directly to the Arabidopsis ADA2 proteins"]. GOA lists IPI to Q9ATB4 (ADA2b).
- Regulated by 26S proteasome degradation under freezing [UniProt INDUCTION; PMID:28344081].

## Annotation review decisions (summary)
- MF: DNA binding (IEA, IDA) and DNA-binding transcription factor activity (IEA, ISS) — ACCEPT (well supported). Propose more specific MF terms: GO:0000977 (RNA Pol II transcription regulatory region sequence-specific DNA binding) and/or GO:0043565 (sequence-specific DNA binding) as proposed_new_terms; kept GO:0003677 DNA binding as accepted parent.
- `protein binding` GO:0005515 (IPI, two refs) — uninformative per guidelines; KEEP_AS_NON_CORE (real interactions: 14-3-3 / ADA2), but note these are regulatory, not core MF. Avoid as core.
- BP: positive regulation of DNA-templated transcription (IDA) — ACCEPT (core). response to cold / cold acclimation (multiple IMP/IEP/TAS) — ACCEPT core for cold acclimation; response to cold accepted. response to water deprivation (IEP) — KEEP_AS_NON_CORE (CRT/DRE is dehydration-responsive and CBF1 OE confers some drought tolerance via the regulon, but CBF1 itself is cold-induced not osmotic-induced; peripheral).
- CC: nucleus (IEA, ISM) — ACCEPT.

## Open questions
- Direct experimental demonstration of CBF1 nuclear localization in planta (vs prediction).
- Extent to which CBF1 directly contributes to drought/water-deprivation responses vs. cross-talk through the shared CRT/DRE element.

## Deep research synthesis (Falcon / Edison Scientific, 2026-06-06)
Source: `file:ARATH/CBF1/CBF1-deep-research-falcon.md`. The Falcon report corroborates and strengthens the existing review without overturning any decision:
- MF (DNA-binding TF activity / activator): corroborates the activator-not-just-binder distinction [falcon "CBF1 encodes an AP2-domain transcriptional activator that binds CRT/DRE motifs and can activate CRT/DRE-containing reporters in heterologous assays (yeast), supporting that it acts as a bona fide transcriptional activator rather than merely binding DNA."]. Used as supported_by on GO:0003700 (IEA, ISS), GO:0045893 (IDA), GO:0006355, and core_function 1.
- DNA binding (GO:0003677): [falcon "recombinant CBF1 binds the CRT/DRE sequence by gel-shift assays"]. Added to the IEA and IDA DNA-binding annotations.
- Nucleus (GO:0005634): report confirms localization rests on a predicted NLS + TF function, not direct imaging [falcon "multiple primary sources identify a **putative nuclear localization sequence** in the protein sequence, consistent with its function as a transcription factor acting on nuclear DNA."]; report's Limitations section explicitly notes no CBF1-GFP imaging was retrieved, so the open question on direct localization stands.
- Cold acclimation / response to cold: kinetics [falcon "CBF-family transcripts rise rapidly following cold shift (minutes), and COR gene expression follows within hours"] and quantitative loss-of-function effect [falcon "antisense downregulation of **CBF1 and CBF3** reduces cold-induced freezing tolerance by about **60%**"] and the core-regulator framing [falcon "CBF1 is a core regulator of **cold acclimation**."].
- Water deprivation (kept NON_CORE): report reinforces that the cold/drought link is via the shared cis-element [falcon "The CRT/DRE element is a shared regulatory node for cold- and dehydration-responsive gene expression, and CBF/DREB-type factors are widely used to connect these stress responses."], consistent with KEEP_AS_NON_CORE (CBF1 transcript is cold-induced, not osmotic-induced).
- ADA2/GCN5 (protein binding, NON_CORE): report adds the SAGA-like coactivator mechanism [falcon "Stockinger et al. (2001) report physical interaction (in vitro pull-down) between CBF1 and Arabidopsis homologs of **Ada/SAGA-like complex** components **ADA2a/ADA2b** and **GCN5** (a histone acetyltransferase)."]. Still uninformative as bare `protein binding`; retained NON_CORE per guidelines.
- New mechanistic context not annotatable to existing GOA/UniProt IDs (recorded for reference, no NEW GO term added): SVALKA (SVK) lncRNA cis-antisense fine-tuning of CBF1 mRNA stability/termination; upstream ICE1-CBF-COR cascade, CAMTA activation, MYB15 repression, circadian control. These concern regulation OF CBF1 rather than CBF1's own activity, so no new MF/BP annotation is warranted.
- No `action: UNDECIDED` entries existed; none required resolution.

## PR #1417 review fix (2026-06-06)
Reviewer (ai4c-agent) flagged that `proposed_new_terms` listed GO:0000977 and GO:0043565, which are EXISTING GO terms (not terms requiring creation). Verified via QuickGO REST API:
- GO:0000977 "RNA polymerase II transcription regulatory region sequence-specific DNA binding" — molecular_function, not obsolete.
- GO:0043565 "sequence-specific DNA binding" — molecular_function, not obsolete.

Action taken:
- Removed the entire `proposed_new_terms` block (both GO:0000977 and GO:0043565).
- Added GO:0000977 as a `NEW` entry under `existing_annotations` with `evidence_type: IDA`, `original_reference_id: PMID:9023378`, qualifier `enables`. This is the single most informative MF term: CBF1 binds the C-repeat/DRE (a Pol II promoter regulatory region) sequence-specifically. Supported by verbatim gel-shift/EMSA quote ["Binding of CBF1 to the C-repeat/DRE was demonstrated in gel shift assays using recombinant CBF1 protein expressed in Escherichia coli."] plus the specificity-vs-mutant-element quote ["expression of CBF1 in yeast was found to activate transcription of reporter genes containing the C-repeat/DRE as an upstream activator sequence but not mutant versions of the DNA element."], both exact substrings of PMID:9023378.
- Did not separately add GO:0043565 (sequence-specific DNA binding); GO:0000977 is its more specific child and already captures the Pol II promoter context, so a single NEW annotation suffices.
- Also fixed two `directly_involved_in:` fields in `core_functions` that were single mappings instead of YAML lists (added `- ` list-item syntax for GO:0045893 and GO:0009631).
- Validation: `uv run ai-gene-review validate genes/ARATH/CBF1/CBF1-ai-review.yaml` → ✓ Valid.
