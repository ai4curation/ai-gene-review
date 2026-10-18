# DOCK2 source evidence

This guide identifies original sources, target records, assay limits and the reproducible interaction extract. It does not substitute an authored narrative for experimental evidence. The review preserves 77 source assertions and proposes no NEW annotations.

## Human exchange mechanism and products

- [PMID:32651375](https://pubmed.ncbi.nlm.nih.gov/32651375/): original Methods for human DOCK2/ELMO1 expression in High Five cells and nucleotide exchange; Results/Figure 6 for ELMO1 regulation. The fluorescence assay follows mant-GTP exchange after GDP injection. Purified and cellular deletion effects differ.
- [PMID:21613211](https://pubmed.ncbi.nlm.nih.gov/21613211/) and [2YIN](https://www.rcsb.org/structure/2YIN): abstract plus deposited human catalytic fragment, GECGD + DOCK2 residues 1192–1622. Full original Methods were unavailable. This fragment is not a natural short isoform.
- [PMID:26083206](https://pubmed.ncbi.nlm.nih.gov/26083206/): human patient Results for receptor-induced RAC1 activation, CXCL12 actin responses, T/B migration and fibroblast rescue. Supplemental Methods were inaccessible; no claim to have read them.
- [UniProt Q92608](https://www.uniprot.org/uniprotkb/Q92608/entry): independently reconstructed 1830- and 336-residue products. The short product lacks the canonical DHR2 region, without established functional inactivity. Human full-length structural entries [6TGC](https://www.rcsb.org/structure/6TGC) and [6TGB](https://www.rcsb.org/structure/6TGB) contain 524 UNK positions at 208–411, 610–658 and 691–961; all 1306 known residues agree. These missing positions are neither sequence substitutions nor complete sequence authentication.

The one core integrates exchange with positive RAC regulation. No separate core is manufactured for generic binding, a downstream phenotype or an unmeasured hydrolysis activity.

## Literal interaction records

The [portable extract](DOCK2-source-data/README.md) contains the exact selected record fields, public raw URLs/hashes and a standard-library reproduction command. It preserves 142 records for 46 source assertions; 139 are IntAct screening records and three are MINT RAC1 records. The primary publications remain the evidence sources. The extractor only projects database measurements and curated metadata.

For [HI-II-14](https://pmc.ncbi.nlm.nih.gov/articles/PMC4266588/), the separately recovered original Methods specify fresh-colony quadruplicate retesting, at least three positive tests and sequence confirmation. Orthogonal assays validate a sample, not every DOCK2 pair. For [HuRI](https://pubmed.ncbi.nlm.nih.gov/32296183/), original main Methods/Results describe quadruplicate verification, sequence confirmation and three assay configurations. Context-free binary assays do not establish native expression, stoichiometry or regulatory consequences.

Every screen partner and DOCK2 parent reference sequence was checked against its record checksum. This is separate from features specifying a sufficient binding region. GOLGA6L9 has a 159–432 feature and TENM4 a 663–2769 feature. The older MINT DOCK2–RAC1 record has DOCK2 1115–1680; the 2005 record explicitly leaves DOCK2 construct taxon unspecified. COS-7 and HEK293T are assay hosts, not automatic assignments of reagent species.

The literal MTUS2 Q5JR59-3 product is 348 residues and lacks canonical residues 1–1021, including mapped MAPRE1/KIF2C interaction regions. It is not assigned the full-length product's cytoskeletal-regulatory binding class. PCSK5 Q92824-2 retains its S8 domain and catalytic residues, while the screen does not measure maturation or native protease activity. HNRNPK P61978-2 is also independently sequence-matched.

Rows below are zero-based source-review indices; each remains a distinct literal partner/publication assertion.

| Row | Partner | PMID | Matching records | Disposition |
|---:|---|---|---:|---|
| 8 | P63000 | 12134158 | 1 | MODIFY → GO:0031267 |
| 9 | P63000 | 15723800 | 2 | MODIFY → GO:0031267 |
| 10 | O15162 | 25416956 | 3 | MODIFY → GO:0019899 |
| 11 | O95273 | 25416956 | 3 | KEEP_AS_NON_CORE |
| 12 | P26371 | 25416956 | 3 | KEEP_AS_NON_CORE |
| 13 | P36406 | 25416956 | 3 | MODIFY → GO:0031625 |
| 14 | P60410 | 25416956 | 3 | KEEP_AS_NON_CORE |
| 15 | P60411 | 25416956 | 3 | KEEP_AS_NON_CORE |
| 16 | P61978 | 25416956 | 6 | KEEP_AS_NON_CORE |
| 17 | Q13137 | 25416956 | 3 | KEEP_AS_NON_CORE |
| 18 | Q5JR59 | 25416956 | 3 | MODIFY → GO:0005519 |
| 19 | Q5VWX1 | 25416956 | 3 | KEEP_AS_NON_CORE |
| 20 | Q6A162 | 25416956 | 3 | MODIFY → GO:0008092 |
| 21 | Q7Z3S9 | 25416956 | 3 | KEEP_AS_NON_CORE |
| 22 | Q99750 | 25416956 | 3 | KEEP_AS_NON_CORE |
| 23 | Q9BYQ2 | 25416956 | 3 | KEEP_AS_NON_CORE |
| 24 | Q9BYQ4 | 25416956 | 3 | KEEP_AS_NON_CORE |
| 25 | Q9BYR5 | 25416956 | 3 | KEEP_AS_NON_CORE |
| 26 | A6NEM1 | 32296183 | 3 | KEEP_AS_NON_CORE |
| 27 | A8MQ03 | 32296183 | 3 | KEEP_AS_NON_CORE |
| 28 | O75525 | 32296183 | 3 | KEEP_AS_NON_CORE |
| 29 | O76011 | 32296183 | 3 | MODIFY → GO:0008092 |
| 30 | P0DPK4 | 32296183 | 3 | KEEP_AS_NON_CORE |
| 31 | P22735 | 32296183 | 3 | MODIFY → GO:0019899 |
| 32 | P26371 | 32296183 | 3 | KEEP_AS_NON_CORE |
| 33 | P49639 | 32296183 | 3 | MODIFY → GO:0140297 |
| 34 | P60328 | 32296183 | 3 | KEEP_AS_NON_CORE |
| 35 | P60409 | 32296183 | 5 | KEEP_AS_NON_CORE |
| 36 | P60410 | 32296183 | 3 | KEEP_AS_NON_CORE |
| 37 | P61978-2 | 32296183 | 3 | KEEP_AS_NON_CORE |
| 38 | Q07627 | 32296183 | 3 | KEEP_AS_NON_CORE |
| 39 | Q15323 | 32296183 | 3 | MODIFY → GO:0008092 |
| 40 | Q5JR59-3 | 32296183 | 3 | KEEP_AS_NON_CORE |
| 41 | Q5VWX1 | 32296183 | 3 | KEEP_AS_NON_CORE |
| 42 | Q6A162 | 32296183 | 3 | MODIFY → GO:0008092 |
| 43 | Q6L8G8 | 32296183 | 3 | KEEP_AS_NON_CORE |
| 44 | Q6N022 | 32296183 | 3 | KEEP_AS_NON_CORE |
| 45 | Q8IUG1 | 32296183 | 3 | KEEP_AS_NON_CORE |
| 46 | Q92824-2 | 32296183 | 3 | MODIFY → GO:0002020 |
| 47 | Q99750 | 32296183 | 5 | KEEP_AS_NON_CORE |
| 48 | Q9BWT7 | 32296183 | 3 | MODIFY → GO:0097110 |
| 49 | Q9BYP8 | 32296183 | 3 | KEEP_AS_NON_CORE |
| 50 | Q9BYQ3 | 32296183 | 3 | KEEP_AS_NON_CORE |
| 51 | Q9BYR6 | 32296183 | 3 | KEEP_AS_NON_CORE |
| 52 | Q9BYR8 | 32296183 | 3 | KEEP_AS_NON_CORE |
| 53 | Q9H8W4 | 32296183 | 3 | KEEP_AS_NON_CORE |

Partner classes come from the exact official UniProt records: enzymes PLSCR1/TGM1, E3 ligase TRIM23, transcription factor HOXA1, scaffold CARD10, cytoskeletal keratins and the sequence-appropriate MTUS2/PCSK5 products. Those activities are not assigned to DOCK2. Keratin binding does not establish assembled-intermediate-filament recognition. Positive pairs lacking a justified narrower class retain generic binding under the project's explicit policy.

## Reactome target paths

Each arrow below was checked in actual ContentService records, including reference accession, species, start/end and compartment. Database set membership is distinguished from a direct target assay.

| Claim | Exact path and scope |
|---|---|
| RAC2 exchange / cytosol | [9014296](https://reactome.org/content/detail/R-HSA-9014296) → catalystActivity 9014402 → physicalEntity CandidateSet 9014398 → **hasMember** 200938 → referenceEntity 89244, Q92608, human 1–1830, GO:0005829 |
| Cytosol in Nef reaction | [200952](https://reactome.org/content/detail/R-HSA-200952) → input 200938; output 200937 has the exact DOCK2 component |
| Cytosol in RHOG context | [9014449](https://reactome.org/content/detail/R-HSA-9014449) → input set 9014451 → hasMember 200938 |
| Broad RHO-cycle refinement | [9012999](https://reactome.org/content/detail/R-HSA-9012999) → RAC2 cycle 9013404 → 9014296 |
| Specific-granule lumen | [6798749](https://reactome.org/content/detail/R-HSA-6798749) → input set 6799354 → member 6799558, human Q92608 1–1830, GO:0035580 |
| Extracellular output | 6798749 → output set 6806312 → member 6806310, human Q92608 1–1830, GO:0005576 |

The [primary neutrophil survey](https://pubmed.ncbi.nlm.nih.gov/23650620/) abstract describes fractionation and mass spectrometry, but the DOCK2-specific table was not recovered. No independent membrane topology or lumen imaging is inferred. Likewise, the YTS membrane survey's target supplement remains unavailable. The distinct B-cell-exosome assertion is UNDECIDED because its target-specific measurement was not recovered.

## PAINT, orthologs and electronic mappings

PANTHER family PTHR45653 has target leaf PTN002511203. Its ancestor path includes PTN002902098, carrying exact IBD assertions for GO:0005085, GO:0031267, GO:0005737 and GO:0005886, and PTN000594048, carrying GO:0007520 and GO:0016477. The whole IBD snapshot is dated 2026-08-28 (PANTHER 19, GO 2026-08-05). Actual current donor annotations and tree descent were joined. Seeded donor fields remain unchanged even where the newer snapshot has a different list.

Human DOCK4 Q8N1I0/PMID:16464467 provides small-GTPase-binding descendant evidence. Zebrafish Dock1 A8E1V6 and Dock5 A8E1V7/PMID:17670792 and fly myoblast city supply myoblast-fusion grounding. Mouse Dock1 Q8BUR4/PMID:15728191 supplies migration context. These are not relabeled as direct human DOCK2 experiments. DOCK2 self-inclusion in exchange IBD evidence is legitimate experimental grounding, not circularity.

IPR026791 and IPR026799 map DOCK/DHR2 exchange and signaling functions. The latter also maps GO:0005096, whose current definition requires increased GTP hydrolysis. That electronic mapping contradicts the target's established exchange mechanism and is removed; the mouse experimental source is not rejected because full text was inaccessible. The specific RAC-regulation refinement is biological and uses a typed path that includes regulatory relations, not an asserted is_a-only descendant chain. Cytoplasm-to-cytosol refinement preserves the original source's broad resolution and the independent target-specific basis.

## Mouse uptake study and addendum

[PMID:21892172](https://pubmed.ncbi.nlm.nih.gov/21892172/), original Figure 6 and Methods on antigen uptake, BMDC culture and retroviral rescue, supports reduced soluble-antigen and particle uptake after mouse Dock2 loss. The normal cache omits Methods; a genuine original PMC HTML/XML was recovered separately. [PMID:22905357](https://pubmed.ncbi.nlm.nih.gov/22905357/) was read as a genuine publisher PDF including supplemental Methods. It limits low Dock2 expression to some ASC-null colonies and leaves the cause unresolved, while explicitly preserving DOCK2-dependent uptake/rescue. No particular passenger mutation or retraction is asserted. The normal addendum cache remains bibliographic-only.

## Cache and original-access inventory

Flags below describe the preserved normal cache; they do not replace the more specific access assessment. A cache marked full text may omit the relevant Methods. Conversely, independently recovered originals do not alter an abstract-only cache. Full text unavailable flags in the YAML refer to cached availability and are qualified by the reference assessment where separate access succeeded.

| PMID | Normal full-text flag / method | Actual use and access |
|---|---|---|
| [10559471](https://pubmed.ncbi.nlm.nih.gov/10559471/) | false; not recorded | Complete official abstract read: human DOCK2 Rac1 binding/activation and nonadherent expression. Full original Methods were not recovered. Independent human exchange assays support the activity without assigning an exact historical construct or natural isoform. |
| [12134158](https://pubmed.ncbi.nlm.nih.gov/12134158/) | false; not recorded | Complete abstract and exact MINT DOCK2–RAC1 record verified. The original foregrounds DOCK180; MINT separately annotates DOCK2 residues 1115–1680 and COS-7 host. Publisher PDF request resolved to subscription-preview HTML, not full Methods. Target association is retained without reconstructing inaccessible experiments. |
| [12176041](https://pubmed.ncbi.nlm.nih.gov/12176041/) | false; not recorded | Complete abstract explicitly reports human Jurkat DOCK2 association with CD3zeta, forced RAC2 activation in 293T cells and IL-2 reporter effects. Full Methods were not recovered; no purified interface or accession-matched isoform is inferred. |
| [15723800](https://pubmed.ncbi.nlm.nih.gov/15723800/) | false; not recorded | Complete abstract and two exact MINT DOCK2–RAC1 pull-down records at Figure 2b verified. MINT notes unspecified DOCK2 construct taxon; HEK293T is the host, not a species determination. The correct publisher PDF route returned 403, so full Methods remain unavailable. |
| [19946888](https://pubmed.ncbi.nlm.nih.gov/19946888/) | false; not recorded | Complete abstract describes a human YTS membrane-enriched proteome and transiently associated proteins. The DOCK2-specific supplementary row was not recovered. The curator-backed membrane annotation is retained with independent peripheral-membrane context; no integral topology is claimed. |
| [20458337](https://pubmed.ncbi.nlm.nih.gov/20458337/) | false; not recorded | Identifier and title verified; complete abstract describes purified B-cell exosomes, but the specific DOCK2 measurement remains unverified because the target supplementary table was not recovered. Source-specific exosome annotation remains UNDECIDED; this is not a contamination or misattribution claim. |
| [25416956](https://pubmed.ncbi.nlm.nih.gov/25416956/) | true; html | Literal DOCK2 binary pairs, methods, features and sequence checksums verified in IntAct. The protected cache omits Methods; a separately recovered genuine PMC original was read for three-of-four pairwise retesting, sequence confirmation and sampled orthogonal validation. No pair-specific native-cell validation is inferred. |
| [32296183](https://pubmed.ncbi.nlm.nih.gov/32296183/) | true; xml | Literal HuRI DOCK2 pairs and parent/isoform sequence checksums verified. Selected genuine original Methods/Results describe quadruplicate pairwise retesting, sequence confirmation and three assay configurations. Screening positivity is not proof of physiological stoichiometry, coexpression or a pathway role. |
| [32651375](https://pubmed.ncbi.nlm.nih.gov/32651375/) | true; xml | Selected full original Methods/Results read independently for human coding constructs, High Five expression and fluorescent nucleotide exchange. Purified ELMO1 N-terminal deletion increases activity while cellular signaling differs. Full-length 6TGC/6TGB sequences contain 524 unresolved UNK positions; all 1306 known residues match human DOCK2. UNK positions are not mutations or exact sequence verification. |
| [21613211](https://pubmed.ncbi.nlm.nih.gov/21613211/) | false; not recorded | Abstract and primary 2YIN deposition verified; full original could not be recovered. The deposited human DHR2 sequence is GECGD plus canonical DOCK2 residues 1192–1622, expressed in E. coli. This defines the tested fragment and does not establish all natural products as equivalent. |
| [26083206](https://pubmed.ncbi.nlm.nih.gov/26083206/) | true; xml | Selected full original Results show human receptor-triggered RAC1 defects, impaired CXCL12 actin responses and T/B-cell migration, plus fibroblast viral-rescue experiments. Supplemental Methods returned 403 and were not read. Human loss/rescue supports physiological signaling without proving every endpoint is a separate molecular activity. |
| [12393632](https://pubmed.ncbi.nlm.nih.gov/12393632/) | false; not recorded | Complete abstract reports DOCK2–CrkL interaction, Jurkat F-actin/CrkL colocalization, 293T RAC1 effects and a Jurkat Vav-associated complex. Full original retrieval failed; no exact reagent sequence or finer endomembrane organelle is assigned. |
| [12871644](https://pubmed.ncbi.nlm.nih.gov/12871644/) | false; not recorded | Complete abstract describes mouse T-cell-receptor/RAC activation and immunological-synapse phenotypes. Original full Methods were unavailable. Rac activation is not itself evidence of GTP hydrolysis acceleration; the electronic GAP mapping is assessed against the actual term and target exchange mechanism. |
| [21892172](https://pubmed.ncbi.nlm.nih.gov/21892172/) | true; xml | Original Figure 6 and uptake/rescue Methods were recovered and read separately from the incomplete normal cache. Mouse Dock2-null antigen and particle uptake defects are positive evidence. Addendum PMID:22905357 limits low Dock2 expression to some ASC-null mouse lines and leaves its cause unresolved, while explicitly retaining the DOCK2 loss/rescue findings. DISPUTED concerns the general upstream ASC interpretation, not every reported DOCK2 result. |
| [22905357](https://pubmed.ncbi.nlm.nih.gov/22905357/) | false; not recorded | Genuine publisher addendum PDF and supplemental Methods read; the normal cache is a bibliographic record without the full addendum. Strain-dependent Dock2 expression is not established as a specific passenger mutation. The addendum explicitly preserves DOCK2-dependent uptake/rescue and limits the general ASC connection; it is not a retraction. |
| [16464467](https://pubmed.ncbi.nlm.nih.gov/16464467/) | false; not recorded | Complete abstract and current donor annotation read. The DOCK4 isoform binds nucleotide-free RAC and is compared with DOCK2/DOCK4; this is descendant grounding for the PAINT small-GTPase-binding node. No exact DOCK2 assay construction is reconstructed from the abstract. |
| [17670792](https://pubmed.ncbi.nlm.nih.gov/17670792/) | false; not recorded | Complete abstract and current donor records read: zebrafish dock1/dock5 morpholino depletion impairs fast-twitch myoblast fusion. Used to document experimental descendants of the conserved PAINT node, not as a direct human DOCK2 fusion assay. |
| [15728191](https://pubmed.ncbi.nlm.nih.gov/15728191/) | true; xml | Complete abstract and selected original migration-rescue passage read: Ajuba-null mouse fibroblasts show a migration defect, with DOCK180 overexpression rescue. Current mouse Dock1 donor GOA grounds the PAINT migration node. The donor result is not relabeled as a human DOCK2 experiment. |
| [23650620](https://pubmed.ncbi.nlm.nih.gov/23650620/) | false; not recorded | Complete abstract describes fractionated human neutrophils and 1292 identified proteins. Reactome supplies exact DOCK2 membership in specific-granule lumen and extracellular output sets. The primary DOCK2 table/topology was not recovered, so independent lumen-topology validation is not claimed. |

## Reproduction and provenance limits

The finite publication contains genuine normal GOA, UniProt and missing publication/Reactome caches; preexisting main caches remain byte-identical. The interaction extractor can replay from saved raw files or request current public records, as documented in its README. Original paper retrieval failures are retained in the audit packet; access to a preview, challenge page, 403 payload or metadata response is not counted as full-text access. No figure pixels were inspected for the mouse addendum; the narrative and specified Methods were read.

Falcon authentication and the configured perplexity-lite fallback failed genuinely. No generated provider report exists and no manual content is mislabeled as one. The authored notes and review are based on the actual primary/database records listed above. Eight short exact source anchors appear once each in the YAML; other uses are reference-only. Quote count is not evidence count.
