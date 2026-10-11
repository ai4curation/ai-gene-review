# AKAIN1 / C18orf42 (P0CW23) — review notes

2026-10-03. PAINT no-IBA backlog. Provider: affinage (gates clear).

## The gene

69 residues, neural-enriched, binds the **type II regulatory subunits of PKA** (RIIα/PRKAR2A,
RIIβ/PRKAR2B) through a predicted amphipathic helix — the AKAP binding mode — but with no targeting
domain. So it occupies the docking site AKAPs need, and expressed AKAIN1 **blocks AKAP-mediated PKA
localization**:

> [PMID:25653177 "Immunoprecipitation and pull-down assays showed that C18orf42 binds specifically to the type II regulatory subunits of PKA."]
> [PMID:25653177 "that of C18orf42 could block the AKAP-mediated subcellular localization of PKA."]

One paper, abstract only. The authors' "endogenous disruptor peptide" framing is a proposal: the
displacement result is from *expression*, and the endogenous-protein work used a FLAG knock-in in
**mouse** Neuro2a cells.

## Recall check

affinage's gates only certify precision, so I searched PubMed independently (AKAIN1, C18orf42).
Three other hits, none functional: PMID:36672701 lists AKAIN1 among ten Alzheimer's entorhinal-cortex
DEGs (cited, LOW); PMID:29275994 never mentions AKAIN1 in its full text; PMID:32799782 is **AKIP1**,
a different gene caught by name similarity. So affinage did not miss a decisive paper this time.

## Decisions (5 rows: 2 MODIFY, 2 ACCEPT, 1 REMOVE)

**`GO:0051018` PKA binding (IDA + IEA) → MODIFY to `GO:0034237` PKA regulatory subunit binding.**
The paper specifies RII. `GO:0034237` is a direct child of `GO:0051018` with no children (checked
via OLS ancestors/children, not inferred from labels). Comparator check: AKAP1, AKAP5 and AKAP11 —
RII-binding amphipathic-helix proteins — carry `GO:0034237`; AKAP7 carries only `GO:0051018`. So the
specific term is the established one, not universal. A refinement, not a dispute.

**`GO:0008104` intracellular protein localization (IDA) → ACCEPT, and the reason matters.** I
considered MODIFY to `GO:1903828` negative regulation of protein localization, since AKAIN1
*disrupts* PKA localization. But the mouse ortholog (G3UWD5), curated by MGI **from the same
paper**, keeps this very term *and separately* carries `GO:0031333` negative regulation of
protein-containing complex assembly (IDA). The full-text readers represent this as two statements.
Collapsing them would overrule a choice whose basis I cannot see. The human-side absence of
`GO:0031333` is recorded as a CURATION knowledge gap instead of being added as NEW — the
endogenous work was in a mouse line, which may be exactly why human was not given it.

**`GO:0005829` cytosol (IEA, Ensembl Compara) → ACCEPT.** Its source, mouse Akain1, carries cytosol
by IDA from the same paper.

**`GO:0005515` protein binding with ROPN1 (HuRI) → REMOVE** per policy — but flagged. ROPN1 carries
InterPro **IPR047844, "Ropporin, dimerization/docking domain"**, and ropporins are AKAP-associated
sperm proteins. An RII-binding amphipathic helix hitting a docking-domain protein is the shape of
interaction AKAIN1 is known for. Raised as a question, not asserted from a Y2H hit.

## Process notes

- **zsh word-splitting bit me again.** `set -- $pair` does not split in zsh, so `$1` held both
  tokens and the QuickGO URL contained a space; I briefly blamed the page size. Moved the loop to
  Python. (Already in memory; still happened.)
- **I typed GO_REF titles from memory, again.** `GO_REF:0000120` is "…Multiple **IEA Methods**",
  not "…Multiple Sources". The builder now copies GO_REF entries from the seeder. Auditing the five
  genes merged last week found two wrong GO_REF titles in **AK4P3** — fixed in a separate PR.
- **Quote checking is now stricter than the validator.** A reusable checker collapses whitespace
  but keeps every other character, so line-wrapped abstracts pass while a dash or prime
  substitution fails — the class that slipped through on AK4P3.
