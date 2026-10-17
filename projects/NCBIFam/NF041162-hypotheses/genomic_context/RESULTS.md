# NF041162 (family 2A encapsulin shell) — viral/prophage contamination check

**Question.** Aguilar et al. 2026 (Nat Commun 17:10571,
doi:10.1038/s41467-026-78136-1, "Small viruses reveal bidirectional evolution
between HK97-fold viruses and encapsulins via procapsids") show that the
SrpI-like (family 2) encapsulin domain is shared by encapsulins **and** by
HK97-fold major capsid proteins of phages infecting *Xanthomonas*,
*Janthinobacterium* and *Pseudomonas* (their structural group 1), and that
~19% of capsid proteins from small (5–11.6 kbp) metagenomic viral genomes
carry encapsulin Pfam domains. Does the proposed
`NCBIFAM:NF041162 skos:exactMatch GO:0140737 encapsulin nanocompartment`
(897 net-new UniProt entries) therefore reach viral capsids?

**Answer: no — NF041162 is clean.** The equivalog model separates the two
lineages that the Pfam domain does not.

## 1. Signature level (UniProtKB REST, queried 2026-10-17)

| query | UniProtKB entries |
|---|---|
| `xref:ncbifam-NF041162` | 933 (all Bacteria; 0 viral taxonomy) |
| `xref:pfam-PF19307` (SrpI-like) | 3,917 |
| `xref:pfam-PF19307 AND taxonomy_id:10239` (viruses) | **19** |
| `xref:pfam-PF04454` (Linocin_M18) `AND` viruses | 0 |
| `xref:ncbifam-NF045672` | 701 |
| `xref:ncbifam-NF045672 AND xref:ncbifam-NF041162` | **0** |

Of the 19 viral PF19307 proteins, 17 are major head/capsid proteins of
*Xanthomonas*, *Stenotrophomonas*, *Pseudomonas* and *Janthinobacterium*
phages — exactly the phage group the paper places with family II encapsulins.
NCBIFAM assigns all 17 to **NF045672** (`MCP_gp7_epsi_15`, "major capsid
protein", equivalog, no GO term), never to NF041162. The remaining two are
Tupanvirus (giant virus) proteins with no NCBIFAM assignment.

So a **Pfam/InterPro-level** rule (PF19307 / IPR045641 → GO:0140737) *would*
mis-annotate phage capsids; the NCBIFAM equivalog does not. InterPro currently
has no GO mapping on IPR045641 or IPR049822 (checked via the InterPro API).

## 2. Genomic context (`nf041162_context.py`)

For each NF041162 entry: EMBL protein id → NCBI `coded_by` CDS → ±8 kb of the
nucleotide record → neighbouring CDS products classified by regex. Per-entry
results: `nf041162_context.tsv`; counts: `nf041162_context_summary.yaml`.

- 932/933 neighbourhoods retrieved (1 entry has no EMBL protein id).
- **829/932 have a cysteine desulfurase (the family 2A cargo) within ±8 kb**,
  in the canonical layout: shell gene immediately upstream of, and usually
  overlapping, the cysteine desulfurase gene, often with serine
  O-acetyltransferase. The 103 without a match are a lower bound artefact of
  product-name matching (older annotations name the cargo e.g.
  "hypothetical protein"/"aminotransferase class V"), not evidence of
  absence.
- 6 neighbourhoods contain a phage-structural gene name. Inspected by hand:

| UniProt | organism | phage gene(s) in window | verdict |
|---|---|---|---|
| A0A285D2J8 | *Cereibacter ovatus* | portal, terminase GpA, prohead protease 1–7 kb upstream | shell + cysteine-desulfurase operon intact, **adjacent to** a prophage remnant |
| A0A4Q9VKP0 | *Siculibacillus lacustris* | terminase ~4 kb away | operon intact; not phage |
| A0ABU1IFV9 | *Paracidovorax wautersii* | "holin-like protein" + TIGR00659 murein hydrolase | LrgA/LrgB pair, not phage — false positive |
| A0ACG4YM36 | *Cupriavidus necator* | tail fibre ~7 kb away | operon intact (shell + annotated encapsulin cargo); not phage |
| G0ABQ1 | *Collimonas fungivorans* | tail sheath FI ~6 kb away | operon intact; not phage |
| H6SQ81 | *Pararhodospirillum photometricum* | "portal protein-like" ~7 kb away, transposase, plasmid stability protein | **only ambiguous case**: no adjacent cargo, mobile-element-rich region; 305 aa, typical shell length |

No NF041162 member is itself a phage gene; at most 1/932 sits in a context
where encapsulin identity is not corroborated by a neighbouring cargo.

## 3. Side observations

- 84 entries carry both NF041162 (2A) and NF041163 (2B); 71 of them have the
  cNMP-binding insertion (PF00027) typical of family 2B shells. Both models map
  to the same CC term, so this does not affect GO:0140737, but NF041162 is not
  strictly 2A-specific.
- `NF016349` (Linocin_M18 PfamEq) carries GO:0008233 peptidase activity and
  GO:0042742 defense response to bacterium in NCBI's `hmm_PGAP.tsv` — a
  holdover from the original misidentification of Linocin M18 as a bacteriocin.
  It must **not** be adopted into ncbifam2go.

## Conclusion

The NF041162 → GO:0140737 `exactMatch` stands. The paper's virus–encapsulin
mixing is real at the Pfam-domain level, and NCBIFAM already resolves it with a
separate phage capsid equivalog (NF045672). The caution to record is about
**domain-level** rules: any future PF19307/IPR045641 (or Linocin_M18) → GO:0140737
mapping would sweep in phage major capsid proteins and should be rejected.

Limitations: product-name regexes on heterogeneous GenBank annotations;
±8 kb window; only UniProtKB members (metagenome-only viral contigs of the kind
the paper studies are not in UniProtKB and were not tested).
