# DHODH (human, UniProtKB:Q02127) — review notes

Reviewed GO annotations for human **DHODH** — dihydroorotate dehydrogenase (quinone),
mitochondrial (EC 1.3.5.2; PYRD_HUMAN). Grounded in the cached UniProt record
(`DHODH-uniprot.txt`), the seeded GOA (`DHODH-goa.tsv`), cached `publications/PMID_*.md`,
cached Reactome entries, and the pre-existing `DHODH-deep-research-falcon.md` (generated
2025-12-27; falcon is currently out of credits so no new deep-research run was made).

## Verified biology
- Class 2 (type 2) flavoenzyme; catalyses the **4th and only mitochondrial step** of de
  novo pyrimidine biosynthesis: FMN-dependent oxidation of **(S)-dihydroorotate → orotate**,
  passing electrons to **ubiquinone** [file:human/DHODH/DHODH-uniprot.txt "Reaction=(S)-dihydroorotate + a quinone = orotate + a quinol"; EC=1.3.5.2].
- Cofactor **FMN**, 1 per subunit [file:... "Name=FMN; Xref=ChEBI:CHEBI:58210"; PMID:10673429].
- Kinetics of recombinant human enzyme: Km 4 µM (DHO), 9.9 µM (ubiquinone-50)
  [PMID:8925840 "Km values for dihydroorotate and ubiquinone-50 were found to be 4 microM and 9.9 microM"].
- **Mitochondrion inner membrane**, single-pass; catalytic TIM-barrel domain faces the
  intermembrane space; N-terminal helices form the lipophilic ubiquinone/inhibitor tunnel
  [file:... "Mitochondrion inner membrane"; PMID:10673429 "an alpha-helical domain that forms the opening of a tunnel"].
- Disease: **Postaxial acrofacial dysostosis / Miller syndrome** (MIM:263750), biallelic
  loss-of-function [PMID:19915526 via UniProt DISEASE].
- Drug target: leflunomide/teriflunomide (A77 1726, IC50 ~1 µM), brequinar
  [PMID:8925840 "An IC50 value of 1 microM was determined for A77 1726"].
- Ferroptosis: DHODH reduces ubiquinone to ubiquinol in the IMM as a parallel
  (GPX4/FSP1-independent) radical-trapping antioxidant defence [PMID:33981038].

## Curation decisions of note
- **GO:0004151 dihydroorotase activity (IEA, GO_REF:0000107 Ensembl Compara)** → **REMOVE**.
  This is a *different* enzyme (EC 3.5.2.3, the DHO domain of trifunctional CAD, step 3 of
  the pathway). DHODH is EC 1.3.5.2 (step 4). Clearly-wrong orthology-transfer IEA (mouse
  ortholog O35435 mis-mapped). Endorsed by task brief.
- **GO:0005737 cytoplasm (IEA, InterPro IPR005720)** → **REMOVE**. Domain-based electronic
  inference mislocalising a strictly IMM-anchored protein whose catalytic domain faces the
  intermembrane space. (HPA reports a cytosol IDA in the UniProt DR block, but that is not
  in the GOA TSV under review.)
- **GO:0005515 protein binding (IPI ×2, PMID:32296183 HuRI)** → both **MARK_AS_OVER_ANNOTATED**
  (NOT removed, per curation policy for bare protein-binding IPIs). WITH/FROM P49638 (TTPA)
  and Q6ZMZ0 (RNF19B); both are single high-throughput Y2H interactions, uninformative and
  unvalidated. The seeded review only had one GO:0005515 entry; added the second GOA row.
- Generic parents (GO:0016020 membrane, GO:0016491 oxidoreductase activity, GO:0016627
  oxidoreductase acting on CH-CH) → **MARK_AS_OVER_ANNOTATED** (more specific terms present).
- **NEW** annotations added (not in GOA): GO:0010181 FMN binding (structural + fluorimetric
  evidence), GO:0048038 quinone binding (ubiquinone tunnel), GO:0110076 negative regulation
  of ferroptosis (Mao et al. 2021 Nature).

## Reference-format housekeeping
- Converted all UniProt supporting_text from `reference_id: UniProt:Q02127` to the
  `file:human/DHODH/DHODH-uniprot.txt` convention and added a matching top-level references
  entry. Trimmed four UniProt quotes that had combined non-adjacent `CC` lines so each is
  now a genuine verbatim substring of the record.
- All PMID/DOI supporting_text verified verbatim (whitespace-normalized) against cached
  publications. Reactome titles left exactly as fetched.

Final: `just validate human DHODH` → ✓ Valid.


## 2026-10-17 evidence-based augmentation

This dated entry supersedes the interpretation of the older decisions above; the earlier journal text is retained verbatim. All 23 imported annotation dictionaries and all three historical proposal identities remain unchanged. Current QuickGO has 21 target rows: three historical keys are absent and one newer process key is present. This comparison does not reseed or silently replace the historical review. The current official human product is Q02127, 395 residues, with no listed alternative product; its targeting segment is not cleaved.

The review now has 12 ACCEPT, 10 MODIFY, 1 KEEP_AS_NON_CORE, 2 UNDECIDED and 1 inherited NEW action. The remaining NEW is the old FMN-binding proposal, not an additional annotation. FMN binding and quinone binding are integrated with catalysis in one GO:0106430 core at the inner mitochondrial membrane, directly participating in de novo UMP biosynthesis.

The old cytoplasm removal was incorrect: GO:0005737 includes mitochondria and differs from cytosol. The actual typed ancestry supports a MODIFY to inner mitochondrial membrane, as for broad membrane. Broad oxidoreductase and pathway descriptions are refined with supported specific replacements. The PAINT target is beneath the actual activity/process node PTN000234184 and location node PTN000234186; target experimental evidence among descendants is legitimate. No donor-count or circularity objection is made.

The two HuRI pairs are verified associations with exact human sequence records. TTPA remains non-core because a more informative supported binding class was not established. RNF19B association is refined to ubiquitin protein ligase binding using independently established E3 partner activity; the HuRI record specifies an RNF19B sufficient-binding fragment at residues 185–732. The dataset's quadruplicate retesting and sequence confirmation do not establish native colocalization, stoichiometry, DHODH ubiquitination or pair-specific orthogonal validation. The earlier blanket description of both interactions as unvalidated is superseded. Supported generic binding follows the [explicit project instruction](https://github.com/ai4curation/ai-gene-review/blob/d77f71b566bd5ee0e87e410083f71e5b6f27036b/projects/CLINGEN_MENDELIAN.md#curation-instructions), not the contrary generic-removal default in the annotation skill.

The historical dihydroorotase transfer is UNDECIDED. Its hydrolytic reaction differs from the established quinone-dependent oxidation, but the original donor experiment behind mouse O35435's historical assertion could not be recovered and the assertion is absent from the complete current donor record. The prior confident attribution to name confusion is withdrawn. Conversely, the UDP process is retained: DHODH executes an upstream chemical step of the pathway, and upstream participation is not synonymous with an indirect effect. The inspected mouse knockout/rescue study measures UMP synthesis, not a terminal UDP-forming kinase reaction (PMID:30449682).

Primary-source limits matter. The 1996 enzyme paper remains abstract-only but contains direct positive human kinetics. Genuine originals for PMID:10673429 and PMID:10727948 were read separately without changing their abstract-only caches. The crystal construct has historical Met30–Arg396 numbering with a ten-His tag, whereas official human sequence length remains 395. The structures contain FMN, orotate and inhibitors; quinone positioning is modeled. Rat protease/deletion experiments establish rat topology, while the human construct imported into yeast mitochondria has an incomplete extreme N terminus. No natural cleavage product is inferred. The historical quinone proposal is refined to ubiquinone binding using substrate kinetics plus structural context.

The ferroptosis proposal is now UNDECIDED and non-core. The 2021 abstract and accessible captions include genetic experiments, so the issue is not absence of genetic evidence. The published 2023 Matters Arising original shows high-dose brequinar inhibition of FSP1 and context-dependent, modest DHODH genetic effects; the full 2021 main paper and full reply argument were unavailable. Both the comment and reply are cited, and the original reference's broad interpretation is marked DISPUTED (PMIDs:33981038,37407687,37407682). The 2021 correction concerns funding only (PMID:34341547). This follows the prior [human review in issue 821](https://github.com/ai4curation/ai-gene-review/issues/821), without treating a disputed general mechanism as a retraction or denying contextual protection.

The previous PR 827 formal approval and PR 1990 human-authorized merge remain part of provenance; they do not convert every earlier claim into a permanent verdict. The new [evidence guide](DHODH-evidence-guide.md) records exact source access, assay species and product limits. Existing machine inputs, Falcon output and publication/Reactome caches are unchanged. Genuine missing citation caches were added separately. Status is DRAFT, reflecting unresolved claims and the retained generic association; status is not forced to COMPLETE.


### Historical-proposal state clarification

Ordinary validation exposed that changing an old NEW proposal to UNDECIDED or MODIFY makes the GOA checker treat it as an imported assertion unless its proposal state is recorded. The schema already defines `retired` for an annotation retired or replaced. The former active ferroptosis proposal and the broader quinone-binding proposal therefore receive `retired: true`, while retaining UNDECIDED and MODIFY respectively. This retires the prior proposed assertions, not a GOA record: all 23 imported source dictionaries and every historical term/evidence/reference/qualifier remain unchanged. The specific ubiquinone-binding recommendation and unresolved ferroptosis reasoning remain visible. No schema or validator code is changed, and the failed initial check is retained in provenance.

## 2026-10-17 review follow-up: chemistry, pathway scope and proposal state

This appended entry supersedes the earlier dihydroorotase uncertainty and the retirement of the live quinone recommendation. The electronic GO:0004151 assertion is now REMOVE: its ring-hydrolysis chemistry and zinc-dependent DHOase machinery differ from the class-2 DHODH domain and demonstrated human FMN/quinone reaction. Target InterPro matches and human structural/kinetic evidence support this biological judgment. The original donor event remains untraced; neither a name-confusion mechanism nor a wrong-paralog transfer is asserted.

GO:0006225 remains ACCEPT and is now included with GO:0044205 in the single catalytic core. Its definition includes pathways to UDP, and DHODH performs the upstream orotate-producing reaction. The mouse donor evidence includes knockout, mouse cDNA rescue and UMP tracer incorporation. That endpoint is explicitly UMP; no kinase activity is assigned. Neither process term is an ontology ancestor of the other. Including the existing UDP assertion resolves core coverage without misrepresenting UMP as a narrower UDP descendant or introducing a NEW process annotation.

The earlier phrase about current QuickGO refers to the independent complete Q02127 API snapshot obtained on 2026-10-17 at 12:25:19 UTC, containing 21 rows. The committed historical GOA TSV still contains its original 23 rows. At term/evidence/reference/qualifier-key scope, the separate snapshot lacks the historical GO:0004151, GO:0006221 and GO:0016491 keys and adds GO:0044210, de novo CTP biosynthesis. This is a timestamped presence comparison, not a claim that the historical file was refreshed or that all WITH/FROM fields match. The [evidence guide](DHODH-evidence-guide.md#2026-10-17-review-follow-up) supplies the endpoint and source distinctions. No GOA file is overwritten and no new CTP annotation is proposed.

Historical authored proposal row 25 originally asserted GO:0048038 quinone binding, IDA, PMID:10673429. It is now refined in place to active NEW GO:0048039 ubiquinone binding, IDA, PMID:8925840, qualifier enables. Direct positive human substrate kinetics support the specific binding claim; the older structure paper remains supporting context and is not described as a quinone co-crystal. The old proposal is recorded here and in preserved history, rather than hidden behind retired while retaining a live recommendation. No second parent/child binding row is added. Historical ferroptosis proposal row 23 remains retired UNDECIDED because that broad proposal is genuinely withdrawn pending unresolved, disputed evidence. The schema permits retirement or replacement; excluding this withdrawn claim from positive machine-readable function coverage is intentional. Its evidence, dispute and reasoning remain public.

All 23 imported source dictionaries, the other annotation actions, source-cache bytes and prior notes remain unchanged. The 26 positions now comprise 12 ACCEPT, 9 MODIFY, 1 KEEP_AS_NON_CORE, 1 REMOVE, 1 UNDECIDED and 2 historical NEW proposals. The single core integrates catalysis, FMN and ubiquinone engagement. No new verbatim quotation is added, including none from PMID:8925840, whose inherited notes excess is preserved. Product/construct distinctions remain in the evidence guide and row reasons; official-record wording was removed from the biological description.
