# Brief: review one human gene in ai-gene-review (vision-disorder campaign)

You are one of several workers running in parallel in the repository
`/home/user/ai-gene-review`. Each worker owns exactly one gene folder. A coordinator
commits the results; you never touch git.

The campaign: Mendelian non-syndromic vision disorders curated in the sister
knowledge base `dismech` are being checked against the normal function of their causal
genes as reviewed here. Your gene is causal for one or more of those disorders. Your job
is a complete, defensible GO annotation review of that gene, following this repository's
own rules.

## Hard rules

- Write only inside `genes/human/<GENE>/`: the review YAML `<GENE>-ai-review.yaml` and
  `<GENE>-notes.md`. Nothing else in the folder is yours to edit (`*-goa.tsv`,
  `*-uniprot.txt` are machine inputs).
- You may cache additional publications with `just fetch-pmid <PMID>` (it writes
  `publications/PMID_<n>.md`). Never hand-edit anything under `publications/`,
  `reactome/`, `cache/`, `interpro/`, `src/`, or another gene's folder.
- No git commands that change state (no add, commit, checkout, stash, reset, restore).
  No `uv sync`, no package installs, no ontology downloads beyond what `just validate`
  does itself.
- Deep research is run by the coordinator, not by you. Do not run any
  `deep-research-*` recipe and never create or edit a `*-deep-research-*.md` file. If
  `genes/human/<GENE>/<GENE>-deep-research-openscientist.md` exists when you start (or
  appears while you work; check once more before you write `core_functions`), read it
  as a literature lead: it is a provider report with a citation list, useful for finding
  the primary papers, not an authority. Fetch and read a paper before you cite it; a
  PMID in that report that you have not opened is not evidence, and its claims are not
  quotable. Add the report to `references:` as
  `file:human/<GENE>/<GENE>-deep-research-openscientist.md` with a `reference_review`.
  If no report exists, grounding comes from the UniProt record, the cached GOA-cited
  publications, Reactome cache entries, and papers you fetch yourself. Record what you
  read in `<GENE>-notes.md`.
- Save your work as you go. Write the notes file early and fill review rows in batches,
  saving the YAML after each batch, so that an interruption loses little. The session
  can be cut off by a usage limit at any time.
- Be economical with reading. Read each cached paper once; for long full-text papers
  search for the gene name and read the relevant passages instead of the whole file.
- Never write an identifier (GO, PMID, UniProt, PANTHER, Reactome) from memory. Look it
  up in the same step you write it.
- Never quote text you have not read in the cited file. Every `supporting_text` must be a
  verbatim substring of the cached source (`publications/PMID_<n>.md`,
  `reactome/R-HSA-<n>.md`, or the gene's `-uniprot.txt` cited as
  `file:human/<GENE>/<GENE>-uniprot.txt`). If you cannot find a real quote, give
  `reference_id` alone with no `supporting_text`.
- Disk is tight. Do not create large files or scratch copies of the repository.

## Read before you start

1. `/home/user/ai-gene-review/CLAUDE.md` — all of it. The sections that most often
   decide a row: the ActionEnum; "Correct but general terms are MODIFY"; "ND
   annotations"; "Root organelle terms"; "Do not overrule curators from incomplete
   evidence"; "Do not add what curators deliberately declined to add"; "What an IBA
   asserts"; "Term-id validation"; "Reviewing references" (including the rules on
   quoting UniProt and never citing a GOA file); "A curation gap is not a knowledge gap";
   "Isoform and Negation Tracking".
2. `.claude/skills/annotation-reviewer/SKILL.md`,
   `.claude/skills/core-function-synthesizer/SKILL.md`,
   `.claude/skills/reference-findings-summarizer/SKILL.md`.
3. One finished example for format: `genes/human/CNGA1/CNGA1-ai-review.yaml`.
4. Only when a row needs it: `projects/ORGANELLES.md`, `projects/NO_DATA.md`,
   `docs/action_consistency.md`, `projects/IBA_REVIEW.md`,
   `src/ai_gene_review/validation/protein_binding_policy.py`,
   `docs/source_defects.md`, `docs/reference_curation.md`.

## Procedure

1. Read `genes/human/<GENE>/<GENE>-uniprot.txt`: function, catalytic activity, cofactor,
   subunit, subcellular location, PTM, disease, features, and the evidence tags on each
   statement (which ones trace to a publication, which are rule-based).
2. Open the review YAML. Every row under `existing_annotations` was seeded from GOA with
   `action: PENDING`. For each row read its source: `publications/PMID_<n>.md` (check
   `full_text_available:`; many are abstract-only), `reactome/R-HSA-<n>.md`, or the
   GO_REF method. For rows that share a paper, read the paper once.
3. Run `just paint-losses human <GENE>` before judging IBA rows and act on what it lists.
4. Where the function is established by papers that GOA does not cite, find them
   (PubMed E-utilities: `curl -s "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmode=json&retmax=20&term=<query>"`,
   then `esummary` to confirm title/authors), cache them with `just fetch-pmid`, and read
   them. Prefer primary papers and structure papers over reviews. Check the PMID resolves
   to the paper you mean before you cite it.
5. Write `<GENE>-notes.md` as a journal with inline provenance:
   `[PMID:12345 "exact supporting text"]`. Say what you could not verify.
6. Fill every row: `review.summary`, `review.action`, `review.reason`,
   `review.supported_by`, and `proposed_replacement_terms` for MODIFY. No row may stay
   PENDING. Use UNDECIDED only where the evidence genuinely cannot be reached or
   adjudicated, and say why.
7. Write the top-level `description` (a project-independent biological summary: what the
   product is, where it acts, its main roles; no curation or project commentary), then
   `core_functions`, `suggested_questions`, `suggested_experiments`, and `knowledge_gaps`
   only for genuine biological unknowns. Keep the machine-seeded `references:` entries;
   add `reference_review` to the ones you actually checked and `findings` for the papers
   that matter. Add any reference you cite that is not yet listed.
8. Record defects that live in the source record (annotation on the wrong gene, a
   mis-keyed PMID, a wrong evidence code) as `review.source_defects` on the row, as
   `docs/source_defects.md` describes — only when the cached text shows it. A title that
   foregrounds another gene is not enough (see CLAUDE.md); if you cannot see what the
   curator saw, use UNDECIDED.
9. Validate until there are no errors:
   `just validate human <GENE>`
   Fix every ERROR. Read each WARNING and fix the ones that point at a real problem;
   list the ones you leave and why. Then run
   `just backfill-record-sections genes/human/<GENE>` if you quoted the UniProt file,
   and validate once more.
10. Set `status: COMPLETE` only when no row is PENDING, validation reports no errors, and
    you would defend each action. Otherwise set `status: DRAFT` and say what is missing.

## Looking up GO terms

- One term: `curl -s "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0008020"`
  (label, definition, `isObsolete`).
- Search: `curl -s "https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=<words>&limit=15"`
- Ancestors: `curl -s "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0008020/ancestors?relations=is_a,part_of"`
- Who else carries a term (the comparator check before any NEW process term):
  `curl -s "https://www.ebi.ac.uk/QuickGO/services/annotation/search?goId=GO:0007601&taxonId=9606&limit=50"`
- Read the definition before you use a term. Labels you write must be the exact current
  label. `core_functions` ids are hard-validated by branch: `molecular_function` and
  `contributes_to_molecular_function` take molecular-function terms, `locations` take
  cellular anatomical entities, `in_complex` takes a protein-containing complex,
  `directly_involved_in` takes biological processes.

## Things that go wrong on these genes

- Phototransduction proteins are over-annotated with whole-pathway and whole-organ
  process terms (`visual perception`, `phototransduction`, `response to light stimulus`)
  from several evidence codes at once. Rows that share a term must get consistent
  actions; judge the claim, not the evidence code. A true but broad term is not REMOVE.
- Much of the experimental literature is on the bovine, mouse or frog protein. An ISS
  or IBA row to the human gene can be sound on that basis; say which species the
  experiment was in rather than implying a human assay.
- Reactome TAS rows for trafficking steps (Golgi membrane, vesicle membrane, ciliary
  membrane) describe transit of a cargo protein. Apply the organelle and transit rules
  in CLAUDE.md and `projects/ORGANELLES.md` rather than accepting or removing them
  as a block.
- Ensembl Compara IEA transfers from mouse can carry tissue-specific locations (sperm,
  junctions). Check what the mouse annotation rests on before deciding.
- Bare `GO:0005515 protein binding` rows follow the protein-binding policy: MODIFY when
  the cited paper supports a specific molecular function, otherwise REMOVE as
  uninformative (not as false). Do not invent a function from an interaction screen.
- Subunits of a complex whose activity belongs to the complex use
  `contributes_to_molecular_function`, not `molecular_function`.
- Regulatory and inhibitory subunits get the regulator/inhibitor activity term that GO
  actually has; look it up.

## What to send back

A short plain-text report, at most about 250 words, no file dumps:

- final `status`, and the count of rows by action;
- the core functions as `GO id — label` lists (molecular function, process, location,
  complex);
- anything that looks wrong in the source record (wrong gene, mis-keyed reference,
  wrong evidence code), with the row it is on;
- what you could not verify, and warnings you left in place;
- PMIDs you added to the cache.
