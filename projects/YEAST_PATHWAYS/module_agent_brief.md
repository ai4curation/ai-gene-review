# Brief for module-curation agents (YeastPathways module project)

Repo: ai-gene-review. You are creating or revising `modules/<slug>.yaml`
documents that generalise YeastPathways (SGD YeastCyc) pathways into reusable
biological modules. This is NOT a rote translation of YeastCyc.

## Read first
- `CLAUDE.md` (identifier discipline; the NEW-annotation and IBA rules apply to
  module claims too).
- `.claude/skills/module-curation/SKILL.md` and its `references/*.md`.
- `modules/README.md`.
- Your group(s) in `projects/YEAST_PATHWAYS/crosswalk.yaml` — the action
  (NEW / ALIGN / GENERALIZE), the chosen scope and the rationale. You may
  disagree with the rationale after reading the literature; if so, explain in
  your final answer and in the module `notes`, but keep the slug.
- The source pathway(s) in `projects/YEAST_PATHWAYS/data/yeastpathways_summary.yaml`
  (reactions, EC numbers, catalysts with UniProt ids, YeastCyc citations, comment).
- The GO-CAMs listed for the group under `gocams/<id>/<id>-src.yaml`
  (YeastPathways_* = SGD conversion; hex ids = PomBase S. pombe models).
  Use the `gocam-curation` skill conventions for reading them.
- For ALIGN/GENERALIZE: the existing module in full, plus 1-2 sibling modules of
  similar quality (e.g. `modules/histidine_biosynthesis.yaml`,
  `modules/coenzyme_a_biosynthesis.yaml`).

## What to produce
1. **Critical pathway assessment.** For each YeastCyc reaction decide whether it
   belongs in the module, which enzyme really catalyses it (YeastCyc gene lists
   are incomplete or stale in places: e.g. missing ARO10, SOL3/SOL4, GND1/2, THI4,
   MEU1/MRI1/MDE1/UTR4/ADI1, GLG1/2, DUG1-3), and the compartment. Find the
   primary literature: use WebSearch / the article tools, then cache each cited
   paper with `just fetch-pmid <PMID>` so `publications/PMID_<n>.md` exists
   before you cite it. Only cite PMIDs whose cached file you have read.
2. **Generalisation.** Model at the scope in the crosswalk: species-neutral
   label/description, parts in pathway order, `variant_sets` for real
   alternatives (architecture fusions, route variants, lineage-specific steps),
   `connections` with `PRECEDES` (+ `chaining_status/chaining_note` when the
   CoA check would mis-fire). MF terms on leaf annotons only. Module-level
   concepts: the most specific GO BP term(s).
3. **Exemplar grounding.** Every leaf role gets `representative_members` (or a
   concrete GENE_PRODUCT participant) that include the S. cerevisiae S288C
   protein(s) (UniProtKB accession from the summary YAML or the gene's UniProt
   file) and, when the group lists a PomBase GO-CAM, the S. pombe ortholog(s)
   (accessions from the PomBase GO-CAM / UniProt). Keep existing non-fungal
   representatives. Use a FAMILY selector with a PANTHER family id only if you
   have verified it (`grep -A1 "^id: PANTHER:PTHRxxxxx$" interpro/panther/panther.obo`
   and membership); otherwise omit `term` and keep `preferred_term` (see CLAUDE.md
   "PANTHER ids"). Never guess PTN ids.
4. **GO-CAM grounding.** Add `gocam_associations` on the module node for each
   listed model (with `title`), and on leaf annotons where a specific
   activity id clearly corresponds (format `gomodel:<model>/<activity>`; for
   YeastPathways models the activity ids look like `gomodel:HISTCYCLOHYD-RXN`
   -- copy them exactly from the src file). Where the GO-CAM disagrees with your
   module (wrong MF, missing step, extra gene), say so in `notes`.
5. **Evidence**: top-level `evidence` must cite `YeastPathways:<frame id>` for each
   source frame (url `https://pathway.yeastgenome.org/YEAST/NEW-IMAGE?object=<id>`),
   GO terms used as concepts, and the PMIDs.
6. **Exemplar gene list.** Append (or create) a section for each of your modules
   in `projects/YEAST_PATHWAYS/module_members/<slug>.yaml`:
   ```yaml
   module: <slug>
   scerevisiae:   # every S. cerevisiae gene product used anywhere in the module
     - {symbol: HIS1, uniprot: P00498}
   spombe:        # every S. pombe gene product used (only if a PomBase GO-CAM is linked)
     - {symbol: his1, uniprot: ...}   # PomBase symbol as used for genes/SCHPO/<symbol>
   panther_families: [PTHR...]   # verified family ids used as role families
   ```
   This file drives which genes and families get reviewed, so include every
   exemplar gene product, including ones you added beyond YeastCyc.

## Validate
```
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/<slug>.yaml
uv run python -m ai_gene_review.validation.module_validator modules/<slug>.yaml
just render-module modules/<slug>.yaml
```
Errors must be fixed. Warnings about missing gene/family reviews are expected
(those reviews are being produced in parallel) -- do not create gene reviews.
Do not commit, push, or edit files outside `modules/<your slugs>.yaml`,
`pages/modules/<your slugs>.html`, `projects/YEAST_PATHWAYS/module_members/`,
and `publications/` (via fetch-pmid). Revert incidental `cache/` changes
(`git checkout -- cache/`).

Also create a history record per module:
`just new-history --kind module --slug <slug> --event CREATE|EDIT --outcome changed --summary "..." --agent-tool claude-code --details "..."`
and `just validate-history <path>`.

## Final answer
Per module: action taken, boundary/generalisation decision, parts and
variant sets, YeastCyc corrections (missing/wrong enzymes, compartments),
GO-CAM disagreements, validation status, and counts of S. cerevisiae /
S. pombe exemplars.

Note: the scratchpad is shared by parallel agents; use a uniquely named
subfolder for any helper scripts.
