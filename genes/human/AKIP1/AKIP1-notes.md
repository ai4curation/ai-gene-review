# AKIP1 / BCA3 (Q9NQ31) — review notes

2026-10-03. PAINT no-IBA backlog. Provider: affinage (gates clear, good recall).

## Shape

27 rows over 4 distinct terms; 23 are `GO:0005515` IPI. Unlike AIRIM, the partners split three
informative ways:

| Source | Partners | Action |
|---|---|---|
| PMID:15630084 (discovery) | PRKACA | **MODIFY → `GO:0034236`** PKA catalytic subunit binding |
| PMID:36115835 (PDZ–PBM fragmentomics) | 18 PDZ proteins (DLG1–4, SCRIB, MAGI1/2, PATJ…) | **MODIFY → `GO:0030165`** PDZ domain binding |
| HuRI, ND Y2H interactome | FHL2, FGFR3, GSN, GW128 | REMOVE |

**AKIP1 is not an AKAP despite its name.** It binds the PKA *catalytic* subunit's N-terminal A helix,
not the RII regulatory subunit:
[PMID:15630084 "The interaction was localized to the A helix (residues 14-39) of the C subunit and to the carboxyl terminus of AKIP1."]

**The PDZ rows have a sequence basis.** AKIP1 ends **…F-P-V**, a class II PDZ-binding motif
(Φ-x-Φ-COOH). Caveat recorded: the fragmentomics paper never names AKIP1 in its text (data are
supplementary), and these are peptide–domain affinities, not cellular interactions.

An unanswered question worth flagging: the **same C-terminus** binds both the PKA catalytic subunit
and PDZ domains. Competitive?

## The InterPro mapping chose the wrong NF-κB branch

`GO:1901222` regulation of **non-canonical** NF-κB (IEA, InterPro IPR033214). But the mechanism is
PKA phosphorylation of **p65 Ser-276** — the canonical subunit:
[PMID:20562110 "attenuated PKA-dependent phosphorylation of p65 on Ser-276"]

Non-canonical NF-κB runs through NIK, p100 processing and RelB. InterPro's own description of
IPR033214 talks about p65 colocalization and never mentions the non-canonical pathway, so the
branch isn't supported even by the mapping's source. **MODIFY → `GO:0043122`** regulation of
canonical NF-κB signal transduction — deliberately direction-neutral, since InterPro notes splice
variants that repress or enhance.

## Recorded, not added

Mitochondrial localization: [PMID:23319652 "AKIP1 is preferentially localized to interfibrillary mitochondria and up-regulated in this cardiac mitochondrial subpopulation on ischemic injury."]
— shown in **rat** myocytes, curated for **no** species (mouse Akip1 has only nuclear terms), and the
paper itself notes [PMID:23319652 "Because there is only 70% homology between the mouse and human AKIP1a"].
Transfer isn't safe → knowledge gap, not NEW.

Rac1 (PMID:17227220) and β-catenin (PMID:30936461) binding: single studies each → questions.

## Process

- Four papers (20562110, 23319652, 17227220) were sitting in this worktree as untracked
  **old-format** files (`reference_id:` header) from an earlier session. Re-fetched with
  `force=True` rather than committing stale-format records.
- Quotes checked whitespace-collapsed and otherwise character-exact: 14 distinct, 0 failures.

## Round 2 (review feedback)

1. **The NF-κB MODIFY rested on uncited InterPro paraphrases.** It now quotes PMID:23319652, which
   states the isoform dependence directly: AKIP1b recruits SIRT1 and represses; AKIP1a enhances.
   (The reviewer pointed to line 101; the statement is a few sentences on — I checked rather than
   quoting the line number.)
2. **So `GO:0043123` positive regulation, not the neutral `GO:0043122`.** UniProt's canonical isoform
   (Q9NQ31-1) is AKIP1a, which enhances. The repression belongs to AKIP1b, a different product.
3. **PMID:18178962 was missing** — the paper UniProt cites with ECO:0000269 for exactly this function,
   cited by no GO annotation. AKIP1 binds **p65 directly**, PKAc is in the AKIP1·p65 complex, knockdown
   abolishes the response.

That third point changed the core function. AKIP1 binds **both** the kinase and its substrate, so it
gets `GO:0035591` signaling adaptor activity as NEW and as the core MF — the same treatment as AKAP7's
PKA-to-channel bridge — with `GO:0034236` kept as a second core function. No IPI partner accession,
because the abstract doesn't say which species the co-IP used.

Not added: a nuclear-retention process term. Both results behind it are overexpression, and whether
AKIP1 anchors or blocks export isn't shown. Recorded as a question.
