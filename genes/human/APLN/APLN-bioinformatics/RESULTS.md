# APLN (Q9ULZ1) — bioinformatics support for the annotation review

Three things in the APLN GOA record can be settled from sequence and from the committed
PAINT slice rather than asserted. Every script fetches live from UniProt, InterPro,
RNAcentral and RNAcentral's species views (responses cached under `cache/`, which is
disposable) and from `interpro/panther/PTHR15953/PTHR15953-paint.tsv`. Nothing below is
hardcoded; delete `cache/` and re-run to regenerate every number.

```
uv run python cterm_conservation.py      # -> cterm_conservation.tsv
uv run python resolve_withfrom.py        # -> withfrom_resolved.tsv, source_entities.yaml
uv run python check_goa_reconciliation.py
```

---

## 1. Is the mature apelin peptide conserved, and is the rodent peptide the human peptide? (`cterm_conservation.py`)

**Question.** Almost every experiment behind this gene's annotations is synthetic-peptide
pharmacology — `K17F`, `pE13F`, `[Pyr1]apelin-13`, apelin-36 — much of it on rodent
receptors or in rodents. Two things follow only if the peptides are conserved: (a) that
those experiments are about the *human* gene product, and (b) that the PAINT node placed
at Tetrapoda is a safe home for the family's one IBD assertion.

**Method.** No multiple alignment is needed. Every bioactive apelin (apelin-36/-31/-28/
-17/-13) is released from the **C-terminus** of the precursor, so "the last *n* residues"
is an exact, alignment-free anchor; human apelin-13 is UniProt `PEPTIDE 65..77` of a
77-residue precursor, i.e. exactly the last 13. All 333 UniProtKB entries that PANTHER
classifies into PTHR15953 were fetched, and per-column identity to human was measured over
the C-terminal 13 residues and, as an internal negative control, over an equally sized
window at the N-terminus (which falls inside the signal peptide, `SIGNAL 1..22`). The
script asserts that the human precursor is 77 aa before doing anything else.

**Result.**

| window | mean % identity to human |
|---|---|
| apelin-13 (C-terminal 13, positions 65–77) | **93.7 %** |
| signal-peptide control (N-terminal 13, positions 1–13) | 47.2 % |

Per column, the apelin-13 window splits cleanly in two:

| position | human residue | % identical across 333 members |
|---|---|---|
| 65 | Q | **41.1 %** (modal residue P, 188/333) |
| 66–77 | R P R L S H K G P M P F | 97.0 – 98.5 % each |

So the invariant unit is not apelin-13 but the 12-mer **R66–F77**; position 65, the
glutamine that becomes the pyroglutamate of `[Pyr1]apelin-13`, is the one variable
position in the peptide (zebrafish carries Pro there).

Among the five Swiss-Prot members, all 77 aa:

| accession | organism | apelin-13 | apelin-17 | apelin-36 |
|---|---|---|---|---|
| Q9ULZ1 | *Homo sapiens* | — | — | — |
| Q9R0R3 | *Rattus norvegicus* | identical | identical | 4 diff |
| Q9R0R4 | *Mus musculus* | identical | identical | 4 diff |
| Q9TUI9 | *Bos taurus* | identical | identical | 2 diff |
| Q4TTN8 | *Danio rerio* | 1 diff | 3 diff | 22 diff |

**Interpretation.** Human, rat, mouse and bovine apelin-13 and apelin-17 are *identical*.
A "rat" or "bovine" apelin-17 in a pharmacology paper is, residue for residue, the human
gene product. Divergence is confined to apelin-36, i.e. to the part of the precursor that
is trimmed away. This is why the rodent-derived ISS rows and the peptide-pharmacology IDA
rows on this gene are on much firmer ground than a species caveat would suggest — and also
why they say nothing species-specific.

## 2. Does the human C-terminus carry the ACE2 substrate motif? (`cterm_conservation.py`)

**Question.** Apelin is inactivated by ACE2, which removes a single C-terminal residue.
Vickers et al. (PMID:11815627) derived a consensus from an alignment of ACE2 substrates:
*"Pro-X((1-3 residues))-Pro-Hydrophobic, where hydrolysis occurs between proline and the
hydrophobic amino acid"*. Does human apelin match it, and does the family?

**Result.** The human C-terminal hexapeptide is `KGPMPF`; `P74-M75-P76-F77` is
Pro-X(1)-Pro-Phe, so the motif is present and predicts removal of **Phe77** only —
which is what ACE2 is reported to do. Across the family the motif is present in
**328/333 (98.5 %)** members, and the terminal residue is Phe in the same **328/333
(98.5 %)**; the five exceptions terminate in E (2), P, Y and S.

**Interpretation.** The single residue that ACE2 removes to inactivate apelin is the same
residue UniProt flags as a determinant of G(i)-versus-β-arrestin balance (`SITE 77`,
ECO:0000269|PubMed:38428423), and it is invariant across the family. The catalytically
relevant claim in this review is therefore a *retention* claim, not a loss claim: human
apelin retains the C-terminal Phe its rodent and bovine orthologs carry, which is what
makes their pharmacology transferable and what makes ACE2 a regulator of the human
peptide too.

## 3. Provenance of the inferred rows (`resolve_withfrom.py`, `check_goa_reconciliation.py`)

`resolve_withfrom.py` reads the review YAML — never a retyped list — and resolves every
`supporting_entities` identifier against a live database, writing
`withfrom_resolved.tsv` and the `source_entities.yaml` scaffold that the
`propagation_review` blocks are built from.

- 18 of 41 rows carry `supporting_entities`.
- **16** of those require `propagation_review`: IEA ×10, ISS ×5, IBA ×1.
- The remaining 2 are `IGI` rows (GO:0010629, GO:0040037) whose `supporting_entities`
  are genetic-interaction partners, not propagation donors.
- 13 distinct identifiers, **0 unresolved**.

Resolutions that mattered to the review:

| identifier | resolves to |
|---|---|
| `PANTHER:PTN001041490` | PTHR15953 IBD node, GO:0005576, taxon:32523 (Tetrapoda), seeds `RGD:620672\|UniProtKB:Q9TUI9\|UniProtKB:Q9ULZ1` |
| `RGD:620672` | 1 hit — Q9R0R3 APEL_RAT (so this row has **three** gene-level donors, not four: `RGD:620672` and the rat Ensembl protein are the same entity as Q9R0R3) |
| `ensembl:ENSRNOP00000100018` | 1 hit — Q9R0R3 APEL_RAT |
| `ensembl:ENSMUSP00000046012` | 1 hit — Q9R0R4 APEL_MOUSE |
| `UniProtKB-SubCell:SL-0112` / `SL-0243` | 'Extracellular space' / 'Secreted' |
| `RNAcentral:URS00000F0F49_9606` | hsa-miR-424-5p |
| `RNAcentral:URS00000F6E49_9606` | hsa-miR-503-5p |
| `InterPro:IPR026155` | 'Apelin', type=family, 345 proteins |

The two RNAcentral ids only resolve informatively with their `_9606` suffix kept: the bare
URS accessions describe cross-species sequences ("ncRNA from 16 species") and hide which
human miRNA the row means. They are exactly the two miRNAs the cited paper is about.

`check_goa_reconciliation.py` re-derives the join key
`(GO id, evidence code, reference, normalized WITH/FROM)` from `APLN-goa.tsv` and from the
review YAML and requires a bijection. Current state: **41 GOA rows, 41 reviewed YAML
entries, reconciliation OK**, plus whatever `NEW` rows the review adds, which the script
lists and excludes from the join.
