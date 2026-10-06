# Brief for batch gene-review agents (YeastPathways module project)

You are reviewing yeast metabolic genes for the ai-gene-review repo
(/home/user/ai-gene-review). Read `CLAUDE.md` first and follow it strictly —
especially "Do not overrule curators from incomplete evidence", "Do not add what
curators deliberately declined to add", the IBA section, and the `protein binding`
policy. Look at one or two complete existing yeast reviews for format
(e.g. `genes/yeast/CAT2/CAT2-ai-review.yaml`).

For EACH gene in your batch:

1. `just fetch-gene <org> <SYMBOL>` (org = `yeast` for S. cerevisiae, `SCHPO`
   for S. pombe; use the symbol exactly as given). If the directory already
   exists and the review has no `PENDING` actions, skip the gene and say so.
   Then `just fetch-gene-pmids <org> <SYMBOL>` to cache cited publications.
2. Do NOT run paid deep-research providers. Instead write
   `genes/<org>/<SYMBOL>/<SYMBOL>-notes.md`: a short evidence journal built
   from the UniProt record, cached `publications/PMID_*.md`, and (if useful)
   WebSearch. Every claim carries provenance `[PMID:nnn "quote"]` or
   `[UniProt:ACC]`.
3. Fill `<SYMBOL>-ai-review.yaml`: `description` (project-independent biology),
   a review for EVERY existing annotation (no `PENDING` left), `core_functions`
   (MF with GO id + `directly_involved_in` BP + `locations`, `supported_by`),
   references with titles. Use exact verbatim `supporting_text` quotes from the
   cached publication files (or the uniprot txt via `file:` refs as other
   reviews do). Use `UNDECIDED` only when evidence genuinely cannot be assessed.
   Never guess GO ids: verify with the OLS MCP / QuickGO / `uv run runoak -i
   sqlite:obo:go info GO:xxxxxxx` before using any id you author.
   Be especially careful with the pathway context given below: the gene's core
   function should be the enzymatic step it catalyses in that pathway
   (reaction/EC given), unless evidence says otherwise.
4. `just validate <org> <SYMBOL>` must pass (warnings OK, errors not).
5. Create a history record:
   `just new-history --kind gene --organism <org> --slug <SYMBOL> --event CREATE --outcome changed --summary "Create review: <SYMBOL>" --agent-tool claude-code --sections existing_annotations,core_functions --details "<one paragraph>"`
   then `just validate-history <path>`.

Rules:
- Only touch files for the genes in your batch, `publications/` (via the fetch
  commands), and `history/genes/...`. Do NOT edit modules, projects, schema,
  other genes, or `cache/` files deliberately. Do NOT commit or push; the
  coordinator commits.
- Do not fabricate. If a publication is abstract-only and you cannot verify a
  curator's experimental annotation, defer to the curator (ACCEPT or UNDECIDED,
  per CLAUDE.md), never REMOVE on that basis.
- Final answer: a compact table per gene: symbol, UniProt acc, #annotations,
  action counts, core MF term(s), validation status, and any family-level or
  pathway-level observations useful to the module curator (e.g. paralog
  specialisation, mis-annotated EC, compartment, moonlighting).
