# AGXT (P21549) review notes

Human alanine--glyoxylate aminotransferase (AGT), HGNC:341. Liver-specific,
peroxisomal, PLP-dependent aminotransferase (class-V PLP family). Deficiency
causes primary hyperoxaluria type 1 (PH1, MIM:259900).

## Core biochemistry / function
- Peroxisomal aminotransferase that transaminates glyoxylate to glycine
  (glyoxylate + L-alanine -> glycine + pyruvate; EC 2.6.1.44) and thereby
  detoxifies glyoxylate, preventing its oxidation to oxalate
  [UniProt P21549 FUNCTION; PMID:23229545 "Failure to transaminate glyoxylate
  to glycine within the peroxisomes, allows glyoxylate to diffuse into the
  cytosol where it is oxidized to the metabolic end product oxalate"].
- Also catalyses serine:pyruvate transamination (EC 2.6.1.51; L-serine +
  pyruvate = 3-hydroxypyruvate + L-alanine) contributing to serine metabolism /
  gluconeogenesis [PMID:10347152].
- Kinetic study concludes the enzyme is "highly specific for catalysing
  glyoxylate to glycine processing, thereby playing a key role in glyoxylate
  detoxification" [PMID:17696873].
- Can also perform beta-elimination of beta-chloro-L-alanine and
  half-transamination of L-cysteine (side reactions) [PMID:18492492].

## Cofactor / structure
- PLP-dependent; PLP covalently bound to Lys209 (Schiff base) [PMID:12899834;
  UniProt MOD_RES 209]. PLP-binding affinity reduced by G82E, minor-allele I340M
  [PMID:17696873, PMID:15802217].
- Active enzyme is a homodimer; N-terminal extension wraps over neighbouring
  subunit and is essential for the active dimer [PMID:22198249, PMID:12899834,
  PMID:10960483, PMID:16971151, PMID:20133649].

## Localization
- Peroxisome / peroxisomal matrix in human liver, randomly dispersed through
  the matrix [PMID:3418107, PMID:9053548, PMID:3709805, PMID:1703535,
  PMID:7813517]. Imported via Pex5p recognising an atypical C-terminal KKL PTS1
  plus ancillary C-terminal targeting info [PMID:22529745, PMID:15911627].
- Species-dependent compartmentalization (peroxisomal in human/rabbit;
  peroxisomal+mitochondrial in rodents; mostly mitochondrial in cat) [UniProt
  CAUTION; PMID:7813517]. Human lost the ancestral N-terminal mitochondrial
  targeting signal by an initiation-codon point mutation [PMID:2363689].
- Disease mistargeting: the minor allele P11L creates a cryptic N-terminal MTS;
  in combination with G170R (and I244T/F152I/G41R) AGT is rerouted to
  mitochondria where it cannot detoxify peroxisomal glyoxylate [PMID:1703535,
  PMID:23229545, PMID:24055001, PMID:26149463].

## Disease
- PH1: calcium-oxalate nephrolithiasis/nephrocalcinosis, oxalosis, ESRD
  [UniProt DISEASE; many variant refs].

## Annotation review decisions (summary)
- Core MF used in core_functions: GO:0008453 L-alanine:glyoxylate transaminase
  activity (exact term in GOA, current OLS label matches).
- L-serine:pyruvate transaminase activity (GO:0004760) kept as accepted
  secondary MF (EC 2.6.1.51, experimentally shown PMID:10347152).
- PLP binding GO:0030170 accepted (secondary). Homodimerization GO:0042803
  accepted (non-core, quaternary structure requirement).
- protein binding GO:0005515 IPIs (IntAct/HuRI Y2H) -> MARK_AS_OVER_ANNOTATED
  (uninformative; mostly keratin/keratin-associated Y2H hits + PEX5 which is the
  real biology but captured as bare protein binding). identical protein binding
  GO:0042802 -> ACCEPT (reflects the biologically real homodimer).
- amino acid binding GO:0016597 (IDA, PMID:18492492) ACCEPT (substrate binding
  demonstrated). transaminase activity GO:0008483 -> MODIFY to GO:0008453
  (parent, too general).
- L-cysteine catabolic process GO:0019448 (IDA PMID:18492492) -> in vitro side
  reaction; KEEP_AS_NON_CORE. L-serine catabolic process GO:0006565 (IDA
  PMID:10347152) KEEP_AS_NON_CORE. L-alanine catabolic process GO:0042853 ->
  L-alanine is the amino donor of the physiological reaction; KEEP_AS_NON_CORE.
- glyoxylate catabolic/metabolic + glycine biosynthetic processes: ACCEPT (core
  BP).
- cytoplasm/cytosol IEA/TAS: AGT is peroxisomal in human; cytosol/cytoplasm
  reflect the pre-import stage / Reactome import reaction. IEA cytoplasm
  (ARBA) is a default-localization over-annotation -> MARK_AS_OVER_ANNOTATED;
  Reactome cytosol TAS KEEP_AS_NON_CORE (import-pathway context).
</content>

## 2026-09-27 substantive evidence audit

This entry supersedes the earlier decision summary where it treats cytoplasm as a
false default, treats alanine catabolism as merely a by-product, assigns generic
protein binding `MARK_AS_OVER_ANNOTATED`, narrows all transamination to one substrate
pair, or groups all disease variants under mitochondrial mistargeting. It also
qualifies the earlier serine/gluconeogenesis statement by species and assay context.

### Identity, baseline and access

The approved human symbol is AGXT (HGNC:341; NCBI Gene 189; UniProt P21549), verified
against [NCBI Gene](https://www.ncbi.nlm.nih.gov/gene/189/) and
[ClinGen](https://search.clinicalgenome.org/kb/genes/HGNC:341). Historical SPAT and
aliases AGXT1, PH1, AGT, SPT, AGT1, TLH6 and Ser-PyrAT were checked for overlap.
AGT is also the symbol of the separate angiotensinogen gene and is not used as a
source identity here. Parent verified the five canonical files against main
`a18dacfd84f4b1a18c864a145a88772e475091bd` and checked open canonical/alias PRs;
the two unrelated SPT search hits do not touch AGXT.

The baseline contains 62 annotations, 30 references and 22 PMIDs. All original
annotation fields outside `review`, reference identifiers/titles, UniProt and GOA
bytes are preserved. No NEW assertion is added. The genuine Falcon research
attempt and configured perplexity-lite fallback each failed while installing
`deep-research-client` because PyPI DNS resolution failed (provider exit 2;
wrapper exit 1). Neither provider ran research or produced an artifact. Concurrent
standard publication caching succeeded for all 22 already-cached PMIDs. This is a
manual evidence audit, not provider output. Logs: `/tmp/AGXT-fresh-research.log`
and `/tmp/AGXT-fetch-pmids.log`.

Every cached abstract was read. Locally available full sections were read for
PMID:12777626, PMID:22529745, PMID:23229545 and PMID:32296183. The first includes
Methods and Results, and the PEX5 paper includes direct structural, biochemical
and localization experiments. The PMID:23229545 extraction has Introduction and
Discussion but omits Methods/Results; its positive full-text metadata does not
authorize claims about uninspected images. Reference `full_text_unavailable`
flags follow the local cache metadata. Other caches remain abstract-only,
including the two publications recovered externally below. Existing experimental
annotations are retained when independent positive evidence agrees; incomplete
abstracts are not used to claim wrong genes or absent experiments.

### Catalytic participation and substrate scope

AGXT directly converts both substrates of its principal reaction: glyoxylate to
glycine and L-alanine to pyruvate [PMID:17696873, "the enzyme is highly specific
for catalysing glyoxylate to glycine processing"; cached UniProt RHEA:24248]. Thus
glycine synthesis, glyoxylate catabolism and alanine catabolism are three views of
one catalytic event, consolidated into one PLP-dependent, homodimeric matrix core.
No assertion that AGXT dominates total hepatic alanine disposal is needed.
The N-terminal deletion retains a dimeric state but lowers activity and promotes
aggregation; it does not prove the extension is required for all dimer formation
[PMID:22198249]. Cofactor experiments distinguish wild-type from G82E and other
variants [PMID:17696873, PMID:15802217, PMID:20133649].

The second core captures serine:pyruvate transamination, not another copy of the
glyoxylate reaction. PMID:10347152 explicitly tests human liver in vitro and finds
substantial SPT/AGT flux. The independent reviewer recovered the primary author
article, and the owner read the returned Methods and Results at the
[author-hosted full text](https://www.researchgate.net/publication/12952025_Flux_of_the_L-serine_metabolism_in_rabbit_human_and_dog_livers_-_Substantial_contributions_of_both_mitochondrial_and_peroxisomal_serine_pyruvatealanine_glyoxylate_aminotransferase).
The preparation contains mitochondria and peroxisomes; flux is assigned from
hydroxypyruvate accumulation plus pyruvate-dependent labelled carbon dioxide.
Human evidence is ex vivo; the infusion experiment testing gluconeogenesis is in
rabbits. Retaining human serine catabolism is therefore positive catalytic
participation, while human in-vivo flux remains an explicit question.

PMID:18492492 reports real cysteine beta-elimination and half-transamination,
with coenzyme/product analyses and subsequent pyruvate transamination. Its
half-transamination turnover is 200-fold below alanine and 60-fold below serine,
despite stronger binding. Cysteine catabolism remains NON_CORE because a major
physiological contribution is unresolved, not because the reaction is false.
The generic transaminase row from this source is also retained at that non-core
substrate scope: narrowing it to alanine/glyoxylate alone would lose experimental
meaning. Amino-acid binding is grounded in measured relative affinities, not just
the paper's docking calculation. Beta-chloroalanine elimination is positive
artificial-substrate chemistry; no new physiological function is inferred.

By contrast, primary [PMID:20133649 Results](https://pmc.ncbi.nlm.nih.gov/articles/PMC2840350/)
explicitly identify alanine/glyoxylate kinetics in the normal and G41 proteins,
supporting refinement of that source's broad transaminase MF. The same externally
recovered Results support PLP binding and size-exclusion/cross-linking analysis,
with apo/holo distinctions. The local cache is unchanged and remains abstract-only.
GO:0047635 was checked against its live
[GO definition](https://amigo.geneontology.org/amigo/term/GO:0047635): the generic
alanine/oxo-acid reaction is not assumed to be a formal parent of GO:0008453.
Its ARBA annotation is refined to the experimentally characterized glyoxylate
reaction, while the reverse serine pair is covered by the specific serine MF.

### Localization, complexes and propagation

Direct normal-human-liver immunogold microscopy supports matrix localization
[PMID:3418107, "randomly dispersed throughout the peroxisomal matrix"]. Broad
peroxisome annotations remain valid at their source resolution. Cytoplasm
includes organelles and is not synonymous with cytosol, so the ARBA cytoplasm
annotation is accepted without inventing a default-localization mechanism.
Reactome:R-HSA-9033235 and Reactome:R-HSA-9033236 place AGXT in cytosol as PEX5
cargo before import; these locations remain NON_CORE. Reactome:R-HSA-389684
captures the mature peroxisomal catalytic reaction. Its wording about
irreversibility does not negate experimentally measured reverse kinetics.

The human AGXT-PEX5 structure resolves an AGXT homodimer and direct recognition
through the C-terminal domain [PMID:22529745]. It makes an obligatory additional
adaptor unlikely in the purified system, superseding an unqualified search for
the hypothesized adaptor from PMID:15911627. Generic PEX5-binding annotations
are removed as functionally uninformative without denying the interactions;
AGXT is cargo, and PEX5/import machinery performs translocation. Structural
self-binding rows can be refined to homodimerization. HuRI self-binding retains
its binary-interaction scope, because the screen itself does not resolve
stoichiometry [PMID:32296183]. The full pair supplement was not reconstructed;
no claim that keratin partners are contaminants or false interactions is made.

The cached PTHR21152 PAINT file contains the term-specific IBD assertions at
PTN000475663 (both catalytic activities, glycine synthesis and glyoxylate
catabolism) and PTN000475539 (peroxisome). Each IBA propagation block records
its ancestral node and direct human corroboration. Human self-inclusion is
valid descendant evidence; donor count is not a quality proxy. The complete
alignment/tree reconstruction was not repeated. The RHEA/EC and UniProt location
mappings are traceable in WITH/FROM. The two ARBA identifiers are recovered,
but rule predicates remain UNRESOLVED, separate from the annotation judgments.
No AGXT/P21549 entry was found in `gocams/index.tsv`; this absence is not used
to propose a new pathway term.

Disease-source distinctions are preserved: PMID:12777626 reports P11L/I244T
peroxisomal aggregation in its expression context, whereas PMID:23229545 reports
different partitioning in stable CHO cells and discusses system differences.
The 2003 abstract reverses the P11L notation, but its full construct description
specifies P11L; the machine title/source is unchanged. PMID:24055001 concerns
Gly161 cytosolic apo-protein aggregation. PMID:26149463 distinguishes intact
peroxisomal G47R-Mi from nicked mitochondrial protein. PMID:1703535 also describes
a small mitochondrial pool in a minor-allele control, so localization is not
stated as absolutely exclusive for every allele.

### Independent review and checks

The annotation-reviewer peer independently assessed PMID:18492492 and recovered
the PMID:10347152 author article. It confirmed the real cysteine chemistry,
non-core physiological scope, and direct human ex-vivo serine contribution with
rabbit-only in-vivo evidence. Parent independently read all 62 decisions, all 30 reference assessments, both
cores and these notes, and checked the primary serine and G41 sources; no
biological blocker remained. Its minor row-47 quote suggestion was adopted to
include the explicit human-liver AGXT methods context. All 22 PMIDs cited across YAML and these notes are cached;
no additional publication identifier or missing-cache gate has been introduced.
Targeted gene validation, history validation and rendering passed. One intentional
warning remains for source-specific GO:0008483 actions: cysteine/pyruvate side
chemistry is NON_CORE, whereas the resolved alanine/glyoxylate assay is MODIFY.
Status is DRAFT because that validation warning remains. Source-object and
reference-identity preservation, unchanged UniProt/GOA bytes, alias-free YAML
and trailing-whitespace checks also passed. The final four-file manifest records
exact SHA256 and byte-derived Git blob hashes.

## 2026-09-27 — PR #3212 specificity and citation-scope follow-up

This follow-up addresses review comment 5851742948 at published head
`b365022100517b5bd89492314f912dd1d92b1bb1`. The three curated files and published
history exactly matched `/tmp/AGXT-local-manifest.json` before edits. All 62
source assertion objects, 30 reference identifier/title pairs, machine UniProt/GOA
files and existing history remain unchanged. The earlier journal entries and
published history are preserved; the decisions below supersede their generic
transaminase and DRAFT-warning statements.

The two GO:0008483 rows now consistently propose GO:0008453. The change to the
PMID:18492492 row is an ontology-specificity correction, not a denial of the paper's
additional chemistry. Its cached abstract explicitly compares side reactions with
physiological L-alanine transamination; the same source already has a specific
alanine:glyoxylate annotation. The cached PMID:17696873 kinetic study independently
establishes that substrate pair. GO:0008483 identifies amino-group transfer without
encoding cysteine identity or beta-elimination, so it is not a useful placeholder
for those findings. The separate cysteine catabolic process remains NON_CORE, and
the unresolved coupled reaction and human physiological flux remain in the question.

Live AmiGO definitions were checked on 2026-09-27. GO:0008453 specifies the alanine,
glyoxylate, pyruvate and glycine reaction. Its `is_a` lineage reaches GO:0008483
through GO:0047635 and GO:0140385; the reviewer called the broad term a direct
parent, but the current hierarchy instead makes it an ancestor. This distinction
does not change the specificity judgment. This live result also supplements the
earlier note that did not assume GO:0047635 parentage. GO:0019448 covers reactions
that break down L-cysteine, so measured direct beta-elimination/half-transamination
is positive participation evidence even with much lower turnover and unresolved
hepatic flux. The non-core annotation does not imply a major physiological pathway.

For PMID:20133649, the reason now rests on the actual cached abstract's variant
catalytic-efficiency result and explicitly separate substrate-pair evidence from
cached PMID:17696873, with its relevant exact snippet attached. It does not ask the
reader to treat a missing cached Results section as present. The earlier external
PMC2840350 access record is retained as provenance; no full-text workaround or
cache modification is introduced. Likewise, the cached PMID:10347152 abstract
alone establishes human in-vitro flux and the human/rabbit peroxisomal context,
while the in-vivo tracer experiment is rabbit only. The second core quote now
includes that explicit species/localization context.

GO:0016597 amino acid binding remains ACCEPT. Measured substrate recognition is
part of catalysis, and absence of a separate binding-only entry in `core_functions`
is not evidence that it is non-core. The first catalytic core now explicitly says
that amino-acid binding supplies substrate recognition and cites the measured
affinities. No redundant core or NEW annotation is added.

All 22 PMIDs cited across YAML and notes remain cached; no reference was added.
The source-scoped differences concern the explanations, not machine annotation
fields or paper identities. Normal targeted validation, rendering, append-only
history and exact file-hash checks are recorded in the follow-up manifest. No Git,
remote comments, shared project edits or cache writes were performed by this author.

Follow-up checks completed: `just validate human AGXT` passed with **zero warnings**;
rendering and the scaffolded history validation passed. The obsolete action-consistency
warning is resolved, so the review status is COMPLETE. Final actions are 51 ACCEPT,
5 MODIFY, 3 KEEP_AS_NON_CORE and 3 REMOVE. All 62 assertions and 30 reference
identities are preserved; all 22 notes-inclusive PMIDs and three cited Reactome
entries are cached. The prior published history remains byte-identical.
