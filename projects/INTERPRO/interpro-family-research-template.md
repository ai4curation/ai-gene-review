---
title: "InterPro family deep-research template"
---

# InterPro family deep-research template

This is the InterPro analogue of the PANTHER family workflow. For PANTHER, `just
fetch-gene` already auto-caches the family (because UniProt carries a PANTHER xref)
into `interpro/panther/<FAM>/`. There is **no equivalent auto-fetch for the InterPro
entries** that drive `GO_REF:0000002` (InterPro2GO) annotations, so they have to be
fetched and researched explicitly. This template fills that gap.

Copy this file to `interpro/interpro/<IPRxxxxxx>/<IPRxxxxxx>-notes.md` and fill it in,
keeping inline provenance (`[PMID:12345 "<verbatim supporting text>"]`).

## 0. Fetch the cached metadata

The existing fetcher already supports the `interpro` database, not just `panther`:

```bash
# Metadata only (InterPro entry: type, hierarchy, member DBs, InterPro2GO terms, literature)
uv run python src/ai_gene_review/tools/fetch_interpro_family_simple.py interpro IPR000719 --output-dir .

# With the reviewed (Swiss-Prot) member list as a CSV (use for taxonomic / paralog scoping)
uv run python src/ai_gene_review/tools/fetch_interpro_family_simple.py interpro IPR000719 --include-proteins --output-dir .
```

This writes `interpro/interpro/<IPRxxxxxx>/<IPRxxxxxx>-metadata.yaml` (+ `-entries.csv`).
The metadata already contains most of what is needed: the InterPro `type`
(family/domain/homologous_superfamily/...), the `go_terms` (the InterPro2GO mappings
under review), the `hierarchy` (parents/children), the `member_databases` (Pfam, PROSITE,
SMART, PRINTS, CATH-Gene3D, PANTHER signatures), and curated `literature` with PMIDs.

## 1. Family definition

- **Accession / name / short name:**
- **InterPro type:** family · domain · repeat · homologous_superfamily · active_site · binding_site · conserved_site · PTM
  - *Type matters for GO scope.* A **domain** or **homologous_superfamily** signature
    identifies a fold/module, not a whole-protein function — InterPro2GO terms attached
    to it are systematically prone to over-annotation when the same module appears in
    proteins with different overall functions.
- **Member databases / signatures integrated:** (Pfam PFxxxxx, PROSITE, SMART, PRINTS, CATH-Gene3D)
- **Parent / child entries (hierarchy):** which more-specific child entries exist; is the
  matched entry the broad parent or a specific child?

## 2. InterPro2GO mappings under review

List each GO term currently mapped from this entry (from `metadata.go_terms`) and judge
whether it is appropriate **for everything the signature matches**:

| GO term | Aspect | Appropriate for all members? | Risk |
|---------|--------|------------------------------|------|
| GO:xxxxxxx label | F/P/C | yes / no | e.g. too broad; only true for a subfamily; fold ≠ function |

Guidance:
- A mapping is sound when the GO term is true for **every** protein the signature can
  match (InterPro2GO is a blanket rule with no subfamily resolution).
- Flag terms that are only true for a **subfamily**, that describe a **whole-protein
  function** attached to a **domain** signature, or that are so generic (`ATP binding`,
  `metal ion binding`, `membrane`) they add little.

## 3. Biological summary of the family

What the family/domain does mechanistically; conserved catalytic/binding residues;
known functional divergence across subfamilies; pseudo-enzyme members. Cite primary
literature (`[PMID:... "<quote>"]`), the InterPro entry `description`/`literature`, and
relevant Pfam/structural references.

## 4. Taxonomic scope

From `-entries.csv` (reviewed members): which clades carry this signature, and does the
InterPro2GO process/component term hold across them (e.g. a "photosynthesis" process term
on a domain present in non-photosynthetic taxa)?

## 5. Over-annotation verdict and recommendation

- **Overall InterPro2GO quality for this entry:** sound · partially over-broad · over-annotating
- **Recommended GO action pattern** for genes matching this entry (ACCEPT / MODIFY-to-specific /
  KEEP_AS_NON_CORE / MARK_AS_OVER_ANNOTATED / REMOVE), with the more specific replacement
  term(s) where applicable.
- **Recommendation to InterPro (if any):** e.g. demote a whole-protein term on a domain
  entry, or move it to a child entry.

## 6. References

- `file:interpro/interpro/<IPRxxxxxx>/<IPRxxxxxx>-metadata.yaml`
- `file:interpro/interpro/<IPRxxxxxx>/<IPRxxxxxx>-entries.csv` (if fetched)
- Primary literature PMIDs (cache under `publications/` where used as supporting text)
