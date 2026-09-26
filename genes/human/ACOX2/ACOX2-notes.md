# ACOX2 (human) — gene review notes

Current judgments are in the 2026-09-26 full annotation audit below. Earlier entries are a historical journal and include superseded mechanistic interpretations and provider-access outcomes.

UniProtKB: Q99424; HGNC:120; gene ACOX2 (chromosome 3p14.3). 681 aa; C-terminal SKL
peroxisomal targeting signal (PTS1). EC 1.3.3.6. FAD flavoprotein. Homodimer (by similarity).

Deep research note: falcon deep-research provider is out of credits (HTTP 402), so no
`-deep-research-falcon.md` was generated. This review is grounded in the UniProt record,
the seeded GOA, and cached publications only.

## Function

ACOX2 is the human **peroxisomal branched-chain acyl-CoA oxidase** (originally "hBRCACox";
homolog of rat trihydroxycoprostanoyl-CoA / THCC oxidase). It is a FAD-dependent oxidase
that catalyses the **first, oxygen-dependent, rate-limiting dehydrogenation** step of
peroxisomal beta-oxidation, removing two hydrogens and introducing a trans-2,3 double bond
into the acyl-CoA, producing H2O2 as a byproduct (UniProt FUNCTION; EC 1.3.3.6).

Two physiological substrate classes:
1. **C27 bile-acid intermediates** — (25S)-THCA-CoA and DHCA-CoA. ACOX2 initiates the
   side-chain shortening that converts C27 cholestanoic acids to the mature C24 bile acids
   (cholic / chenodeoxycholic). [PMID:27884763 "Acyl-CoA oxidase (ACOX2) is involved in the
   shortening of C27 cholesterol derivatives to generate C24 bile acids"]
2. **2-methyl-branched-chain fatty acyl-CoAs** — e.g. (2S)-pristanoyl-CoA; stereospecific
   for (2S)-methyl isomers. Redundant with ACOX3 for pristanoyl-CoA (PMID:29287774, per
   UniProt). Also mono-methyl branched-chain FAs (mmBCFA) in brown adipose tissue (by
   similarity to mouse Q9QXD1). Low-efficiency straight-chain activity (C10, C16).

The 1990 human-liver enzymology paper [PMID:2079609] established that human liver contains a
**separate trihydroxycoprostanoyl-CoA oxidase** distinct from palmitoyl-CoA oxidase (ACOX1),
explaining why bile-acid metabolism is normal in ACOX1 deficiency — this separate THCC
oxidase is ACOX2.

## Localization

Peroxisome / peroxisomal matrix. Direct protein evidence in human liver
[PMID:8943006] (immunocytochemistry; SKL PTS1; absent in Zellweger livers) and
[PMID:2079609]. IMP peroxisomal localization confirmed for both WT and R225W mutant in
HepG2 [PMID:27884763 "similar protein size and peroxisomal localization for both normal and
mutated variants"]. The Reactome TAS `cytosol` annotations refer to the peroxisomal-import
transit state (PEX5 cargo in cytosol before matrix translocation), not the site of
catalytic activity.

## Disease

**ACOX2 deficiency / Congenital bile acid synthesis defect 6 (CBAS6; MIM:617308)** —
autosomal recessive inborn error of bile-acid synthesis. Accumulation of toxic C27
intermediates (THCA, DHCA), negligible C24 bile acids, persistent hypertransaminasemia /
liver fibrosis; variable neurological features (ataxia, cognitive impairment). Known
variants: R225W [PMID:27884763] and a large N-terminal deletion (69-682 del) [PMID:27647924,
via UniProt]. Phytanic/pristanic acids remain normal (redundancy with ACOX3 for BCFA).

## Molecular function GO landscape

- GO:0003997 acyl-CoA oxidase activity — parent MF; core (EC 1.3.3.6). Best single MF.
- GO:0033791 THCA-CoA 24-hydroxylase activity — the bile-acid-specific reaction, IDA in
  [PMID:27884763]; also directly matches Rhea:46728 in UniProt. Core bile-acid MF.
- GO:0016402 pristanoyl-CoA oxidase activity — BCFA reaction; UniProt Rhea:40459
  (PubMed:29287774). Valid but redundant with ACOX3.
- GO:0120523 / GO:0120524 medium-/long-chain fatty acyl-CoA oxidase activity — RHEA IEA
  (decanoyl/hexadecanoyl-CoA). UniProt calls straight-chain activity "low efficiency", so
  these are minor/over-annotations relative to the branched-chain and bile-acid core.
- GO:0005504 fatty acid binding (IBA) — substrate binding is implied by catalysis but a bare
  "fatty acid binding" MF is uninformative for this enzyme; over-annotation.
- GO:0050660 FAD binding / GO:0071949 FAD binding — cofactor binding; supported (COFACTOR FAD).
- GO:0042803 protein homodimerization activity (ISS from P07872/ACOX1) — UniProt SUBUNIT
  "Homodimer (By similarity)"; accept as by-similarity.
- GO:0005515 protein binding (IPI, STRN3 / DYNLT1) — bare "protein binding" from high-throughput
  interactome screens; uninformative, over-annotated.

## Biological process

- GO:0006699 bile acid biosynthetic process (IDA, PMID:27884763) — core BP.
- GO:0033540 fatty acid beta-oxidation using acyl-CoA oxidase — the precise BP; IDA/IMP core.
- GO:0006635 fatty acid beta-oxidation — parent BP; accept.
- GO:0000038 very long-chain fatty acid metabolic process (IBA) — ACOX2 handles
  branched-chain and C27 bile-acid substrates, not straight VLCFA (that is ACOX1). Likely
  IBA over-propagation; mark over-annotated.
- GO:0006631 fatty acid metabolic process — broad InterPro IEA; accept as broad-but-correct.
</content>

## 2026-09-20 full-gene re-review

Read every source annotation and relevant evidence, including primary full texts for disputed reactions and the exact PAINT target path. See [ACOX2-primary-source-checks.md](ACOX2-primary-source-checks.md) for assay context, access limits, short exact excerpts, and pending focused adjudication. All original source fields are preserved; no NEW annotation is added. Broad true chemistry and localization are retained separately from exact substrate/reaction conflicts.

## 2026-09-26 — full 40-annotation source audit

This section supersedes conflicting assertions in the earlier journal and the September 20 primary-source notes. Those historical files are retained; no generated source was rewritten. In particular, GO:0033791 is not equivalent to the UniProt oxidase reaction, homodimerization is unresolved, weak straight-chain oxidation is not disproved, and generic protein-binding annotations are removed as uninformative. The current synthesis does not assign mouse brown-fat physiology as an established human function.

### Baseline, identity and research access

Approved human symbol ACOX2, HGNC:120, NCBI Gene 8309 and UniProt Q99424 were checked against primary nomenclature records; aliases include BRCACOX, BRCOX and THCCox. The parent verified main `9e34ed516aaa199a283a5042f6adf3b60ae45d54` and no overlapping open PR. The review baseline was INITIALIZED with 40 source rows and 20 references. Local YAML blob `1811ae9458b2b1ab4d27b670ae414dd3a05d4063` and notes blob `7b94ca1fd30c55d359a3a2c68c83445bad63a7bd` matched main. Local HTML was an older derived rendering; the publication base is remote blob `d6264f4213cfd4c447528aa5f58435322d996f9a`.

The required genuine Falcon request with a 1200-second timeout and automatic perplexity-lite fallback was attempted using writable temporary UV tool/cache directories. Both failed before reaching a provider because PyPI could not resolve `deep-research-client` (three retries, 6.4 and 9.8 seconds). The earlier HTTP 402 note describes a different session. No provider output was produced or authored manually. Concurrent normal publication fetching found all seven existing PMID caches. Normal additional fetches of 8654595, 8026493, 9218493 and 8387517 also failed DNS and produced no files. The last two are required new review references, so the publication must remain draft until they are cached normally. The first two are unresolved donor leads only. These notes are manual research, not provider output.

### Oxidase chemistry and the hydroxylase term

Live [GO:0033791](https://amigo.geneontology.org/amigo/term/GO:0033791) specifies 25R-THCA-CoA hydroxylation using water and an acceptor, while the ACOX2 UniProt RHEA:46728 reaction consumes oxygen and produces a 24E-enoyl product from 25S substrate. Historical oxidase synonyms therefore do not settle the formal reaction mismatch. The human [PMID:27884763](https://pubmed.ncbi.nlm.nih.gov/27884763/) publisher methods/results describe 10 micromolar THCA supplied to HepG2 cells over 48 hours, with cholic-acid production measured by HPLC-MS. This supports pathway participation, but does not isolate the elementary hydroxylation specified by GO. Its IDA and the exact IBA chemistry remain UNDECIDED; no self-evidence circularity is alleged.

The ISS donor [O02767](https://www.ncbi.nlm.nih.gov/gene?LinkName=protein_gene&from_uid=2117287) is **rabbit ACOX2**, not rat. Full [PMID:9218493](https://pdfs.semanticscholar.org/25a0/7b6451608e1ad668bdbeb8c04fe2dc8ae4e7.pdf?skipShowableCheck=true) verifies the enoyl product by chromatography and mass spectrometry. Its small hydroxylated product is attributed probabilistically to endogenous COS-cell hydratase. Accordingly the donor-supported ISS is MODIFY to GO:0003997, with the nomenclature problem retained as a question. This does not assert universal impossibility of coupled hydroxylation. The annotation-reviewer peer independently checked the product analysis and endorsed this bounded refinement.

### Substrate range and assembly

Full [PMID:29287774](https://www.researchgate.net/publication/322072163_A_novel_case_of_ACOX2_deficiency_leads_to_recognition_of_a_third_human_peroxisomal_acyl-CoA_oxidase) was read through methods, results and discussion. The human recombinant assays use a yeast fox1 deletion background, 100 micromolar substrate, and HPLC measurement of enoyl plus hydroxylated products. The panel includes C10, C16, pristanoyl and THC-CoA, not C24/C26. It supports weak straight-chain capacity as NON_CORE and shared ACOX2/ACOX3 pristanoyl activity; only ACOX2 handled THC-CoA in that tested comparison. Assay substrate breadth is kept separate from predominant physiological flux.

The primary human purification study [PMID:8387517](https://www.researchgate.net/publication/14810824_The_CoA_esters_of_2-methyl-branched_chain_fatty_acids_and_of_the_bile_acid_intermediates_Di-_and_trihydroxycoprostanic_acids_are_oxidized_by_one_single_peroxisomal_branched_chain_Acyl-CoA_oxidase_in_h) supplies two additional qualifications. Table III uses partially purified preparations chromatographically separated from palmitoyl-CoA oxidase; its lignoceroyl-CoA rate is 0.14 versus 59.4 nmol H2O2/min/ml for 2-methylpalmitoyl-CoA (0.2%). This supports retaining limited VLCFA capacity as NON_CORE, not a claim of in-vivo flux. The paper also contrasts roughly 67–70 kDa preparations with an earlier 138 kDa estimate and explicitly leaves native assembly unresolved, including possible purification-induced dissociation. Homodimer ISS from rat ACOX1 therefore remains UNDECIDED. The short external-text excerpts are identified as such in the YAML; no uncached body text is impersonated as a repository cache.

Live GO:0000038 describes an aliphatic tail longer than 22 carbons; the total carbon count of a C27 steroid does not itself meet that criterion. Normal patient VLCFA levels do not prove absent side activity. The earlier generalization that every ACOX2-deficient patient lacks C24 bile acids is also narrowed to the measured family and assay.

### Propagation, localization and interaction audit

All seven PAINT rows were assessed using the cached ancestral path rather than donor counting; the source_entities use actual PTN nodes. The fatty-acid-binding IBD draws on rat Acox2/Acox3. NCBI source tracing leads to PMID:8654595 and PMID:8026493, but the accessible abstracts do not settle free-acid recognition, so that exact binding annotation remains UNDECIDED. Acyl-CoA preference alone cannot disprove free-acid binding. The rat ligand-bound structure called ACO-II in PMID:16672280 belongs to ACOX1/P07872, not ACOX2, and is not repurposed as direct ACOX2 evidence.

Electronic mappings retain actual Rhea, InterPro and ARBA source identities. Unread rule predicates remain UNRESOLVED while the annotation judgment follows independent biology. The oxidoreductase and broad metabolic terms are refined to their demonstrated oxidase chemistry or pathway. Live GO:0071949 specifically denotes oxidized FAD and is a child of the broader GO:0050660; the two are not synonyms. The cofactor transfer is consistent with the flavoprotein reaction, while FAD supplementation is not presented as an independent affinity measurement.

The P07872 ISS donor is rat ACOX1, a paralog: cofactor and location can transfer with human corroboration, while assembly needs separate assessment. PMID:8943006 is abstract-only for this session and its original localization is retained with later human PMP70 colocalization. PMID:2079609 is pre-cloning human-liver enzymology, not sequence identification. Five cached Reactome records were read: matrix locations describe the catalytic compartment, and the two cytosolic rows describe PEX5 cargo before import. No import-machinery process is invented for that cargo.

The BioPlex 2.0 and HuRI full cached texts support study context; the BioPlex 3.0 cache is truncated despite metadata claiming full text, so its review flag records unavailable full text. GOA/UniProt identify STRN3 and DYNLT1 partners. All three generic binding rows are REMOVE because no informative ACOX2 molecular function is established, without denying interaction or pretending the pair-level supplements were revalidated.

All 40 source assertions, alternative products, UniProt/GOA files, PAINT evidence and historical primary-source notes are preserved. One core function integrates matrix oxidase chemistry, bile-acid synthesis and oxidase-dependent beta-oxidation. No NEW annotation is added. Validation and independent-review outcomes follow below.

Independent focused consultation by the annotation-reviewer peer confirmed the rabbit product-analysis refinement and separately read PMID:8387517 Table III and Discussion. The peer agreed that the small C24 rate supports only preparation-level in-vitro capacity and that the native-mass discrepancy warrants UNDECIDED. Its 0.2% figure is a substrate-rate comparison within that preparation, not an organ-level physiological contribution.

Final local checks: `just validate human ACOX2`, `just validate-history` and `just render human ACOX2` pass. Gene validation has two warnings: the required uncached PMID:9218493/PMID:8387517 references and the deliberate source-specific GO:0033791 split (rabbit ISS MODIFY; unresolved human IDA/IBA UNDECIDED). Final actions are 23 ACCEPT, 6 KEEP_AS_NON_CORE, 4 MODIFY, 4 UNDECIDED and 3 REMOVE. All 40 source assertions and alternative products were compared against the baseline; immutable source hashes match. Trailing spaces were removed with parsed-YAML equality. Exact four-file handoff: `/tmp/ACOX2-local-manifest.json`. No Git or remote writes were made; the parent independently reviews and publishes the draft.

Coordinator review found no further biological blocker after inspecting all 40 decisions, the core and reference assessments. The reference-level full-text flags for PMID:27884763 and PMID:29287774 now record their abstract-only local caches; PMID:9218493 and PMID:8387517 likewise remain unavailable locally despite successful external primary reading. This flag describes the cache, not the truth or verification of a citation.

The citation audit also includes notes and historical journal entries. The full missing-cache list is PMID:16672280, PMID:27647924, PMID:8026493, PMID:8387517, PMID:8654595 and PMID:9218493. Two support new decisions; the remainder document donor leads, an excluded paralog source or historical disease context. Keep the PR draft until these required records are retrieved normally. No missing source or provider report was fabricated.

## 2026-09-26 — PR #3161 follow-up at dda08a47

Read the [full review and formal changes-requested summary](https://github.com/ai4curation/ai-gene-review/pull/3161) against published head `dda08a47bbe1ebb4a788a579d5a410f2456afd55`. The coordinator independently confirmed the three starting blobs: YAML `ff99313a1f911d286e931dc861d8b1bb89d4afc3`, notes `080e8b821db260aa1b782bc9f40c8d39b8d13825`, and HTML `616fbc609bc946e729d69e2907c4c0f8a8a34d69`. This section supersedes the prior C24 retention, mixed hydroxylase decisions, and one-core synthesis. Source annotations, alternative products, and machine caches remain unchanged.

The C24 rate in PMID:8387517 is a real reported preparation-level result, independently read by two reviewers, but it is not securely attributable to ACOX2 itself. Table III's 0.14 versus 59.4 nmol H2O2/min/ml (0.2%) compares substrates within a partially purified preparation. The experiment does not by itself discriminate a small intrinsic side activity from residual activity of another oxidase. Residual contamination is a possibility, not an observed explanation. The VLCFA-process IBA is therefore UNDECIDED. The generic acyl-CoA reaction quote was removed from that row because it does not establish C24 activity. The purified/recombinant human panel in PMID:29287774 did not test C24/C26, so it cannot close this question. Neither normal patient VLCFA concentrations nor the total carbon count of steroid substrates is negative evidence for intrinsic VLCFA activity.

The [current GO:0033791 definition](https://amigo.geneontology.org/amigo/term/GO:0033791) was rechecked: its formal reaction and RHEA:15733/EC:1.17.99.3 cross-references specify hydroxylation, while its synonyms include oxidase names. The chemistry attributed to ACOX2 by the human recombinant study and UniProt RHEA:46728 is enoyl formation with oxygen and peroxide. The three rows now consistently use MODIFY to the verified oxidase term GO:0003997. This is a target-level reaction-term adjudication supported independently of the unresolved rat IBD assay; it is not a conclusion that all evidence codes must always have matching actions. Their primary-source limits remain distinct: human PMID:27884763 is a whole-cell bile-acid endpoint; the rat IBD chemistry is uninspected; rabbit PMID:9218493 directly identifies the enoyl product and offers endogenous hydratase as a probable explanation of the minor hydroxylated product. The human target's contribution to IBD is legitimate, not circular.

The loss of substrate precision in the broad replacement is explicitly recorded as an ontology question. GO:0003997 already occurs in the review; the replacement repairs the chemical assertion rather than adding functional coverage. No fabricated THCA-CoA-specific term is introduced, and no exact hydroxylation assertion is retained solely to preserve an informative label. The THCA-CoA substrate scope remains explicit in evidence and core prose.

The core now separates two substrate scopes: C27 bile-acid side-chain oxidation under the verified generic oxidase MF, and [pristanoyl-CoA oxidation GO:0016402](https://amigo.geneontology.org/amigo/term/GO:0016402). The first core is specifically scoped to the bile-acid reaction, not an extra umbrella duplicating the pristanoyl core. The branched-chain core retains the precise oxidase-dependent beta-oxidation process GO:0033540. The broader GO:0006635 annotation remains ACCEPT in the original set and is covered by this more specific core process; a redundant core-process parent was not added solely for repetition.

All YAML aliases were expanded to literal evidence entries without changing their content. The rabbit reference title now correctly joins cholestanoyl without an inserted space. The IMP row again includes the measured family C27/C24 phenotype alongside the mutant/WT cellular comparison, and the bile-acid row includes the source's pathway statement. Mutation-versus-WT cellular experiments were not reclassified as inherently incapable of supporting IMP. Core prose now describes biology rather than curation scope; EC 1.3.3.6 and the UniProt-supported heart/liver/kidney expression summary were restored to the standalone description.

The reference reviews were updated to match these judgments, especially the preparation-level C24 evidence. Local full-text flags remain true for unavailable/abstract-only caches even when an external full paper was read. All six notes-inclusive missing PMIDs remain a hard draft gate: 16672280, 27647924, 8026493, 8387517, 8654595, and 9218493. The PR must remain draft and must not merge until normal source recovery. The reference requirement is not waived by manual primary reading, and no cache/provider artifact was fabricated. The review reply is prepared for coordinator publication, not sent by this author.
