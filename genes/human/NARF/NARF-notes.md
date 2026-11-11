# NARF (J3KS48): evidence and exact-input prediction review

The ProtNLM function paragraph transfers the established function of NARFL/IOP1 to NARF/IOP2. Direct knockdown experiments distinguish these paralogs: NARF depletion did not decrease aconitase activity. The separate 4Fe–4S-binding claim remains uncertain, especially for the extensively truncated selected product.

## Input identity and functional boundary

J3KS48 and Q9UHQ1 share HGNC:29916. The first 128 selected residues match reference 1–128, and selected 129–213 match reference 174–258. Most of the reference C-terminal region is absent. This same-gene bridge must not be confused with NARFL/CIAO3, a different gene.

## Biological evidence

- [PMID:10514485 — Prenylated prelamin A interacts with Narf, a novel nuclear protein.](https://pubmed.ncbi.nlm.nih.gov/10514485/): Human NARF constructs localize to nuclei and bind prenylated prelamin A; the paper does not establish activity of the selected 217-residue product.

> When a FLAG epitope-tagged Narf is expressed
> in HeLa cells, it is exclusively nuclear and partially co-localizes with the
> nuclear lamina.

- [PMID:18270200 — A role for IOP1 in mammalian cytosolic iron-sulfur protein biogenesis.](https://pubmed.ncbi.nlm.nih.gov/18270200/): Compared with IOP1 depletion, IOP2/NARF depletion did not impair cytosolic or mitochondrial aconitase activity, distinguishing the paralogs in this tested CIA phenotype.

> Knockdown of IOP2, in contrast, had no
> effect on either.

## Exact non-GO claims

The complete emitted record is preserved in [NARF-protnlm-source.json](NARF-protnlm-source.json). Assessments below address the selected protein product; evidence on longer products is identified explicitly.

### Protein name

> Uncharacterized protein

The emitted name “Uncharacterized protein” makes no specific biochemical assertion. It omits the verifiable NARF gene identity and hydrogenase-family relationship.

### Function

> Component of the cytosolic iron-sulfur (Fe/S) protein assembly machinery. Required for maturation of extramitochondrial Fe/S proteins

PLI (CS 0; PARALOG_OVERANNOTATION) for the claimed required CIA-machinery role. In the direct IOP1/IOP2 comparison, IOP1 knockdown impaired cytosolic aconitase while IOP2/NARF knockdown did not. This is a tested functional boundary, not an argument from a missing annotation. The experiments do not exclude every possible iron-related role for NARF. [PMID:18270200](https://pubmed.ncbi.nlm.nih.gov/18270200/).

### Location

> Nucleus

UNC (CS 1) for this exact product. The donor Q9UHQ1 is the same gene, and the original NARF paper supports nuclear localization, but the large deletions in J3KS48 leave product-specific localization unresolved. [PMID:10514485](https://pubmed.ncbi.nlm.nih.gov/10514485/); [sequence mapping](NARF-bioinformatics/RESULTS.md).

## Emitted GO claims

All 1 emitted GO claims are individually assessed in [NARF-protnlm-predictions-review.yaml](NARF-protnlm-predictions-review.yaml).

## Family integration

PTHR11615 groups hydrogenase-related proteins with divergent cellular roles. Human NARF/IOP2 and NARFL/IOP1 cannot be treated as isofunctional because of their fold. The direct paralog comparison supplies a biological transfer boundary; no ancestral node placement or cluster occupancy is inferred.

## Evidence limits

The two primary references are abstract-only in the standard publication cache. Their abstracts explicitly report the nuclear localization and comparative knockdown results used here. Neither resolves function of J3KS48. A full molecular function is therefore not assigned to this short product.

Exact sequence mapping: [NARF-bioinformatics/RESULTS.md](NARF-bioinformatics/RESULTS.md). Global alignments can place nonhomologous alternative tails opposite gaps or distant residues; only conserved segments and explicitly retained feature intervals support functional transfer.

## Research integration

The genuine Falcon report is retained. Its gene-level synthesis is interpreted through the exact product sequence and the primary sources above; the truncation boundary and paralog distinctions are assessed independently.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

This section does not use ProtNLM2 output. Sources: the UniProt records J3KS48 and Q9UHQ1, QuickGO, the PANTHER geneinfo API, the InterPro API, cached primary papers, and a new local sequence mapping.

### Product identity

- J3KS48 (TrEMBL, 217 aa) is the product of the Ensembl alternative gene model ENST00000581202 / ENSP00000462305 at the NARF locus (HGNC:29916). The reviewed canonical product is Q9UHQ1 (456 aa, isoform 1; UniProt lists 4 isoforms, and J3KS48 is not one of them).
- My independent mapping (`NARF-bioinformatics/compare_sequences_rereview.py` → `RESULTS-rereview.md`, `results-rereview.json`, with sequences fetched live) reproduces the earlier blocks. J3KS48 1-128 = Q9UHQ1 1-128 and J3KS48 129-213 = Q9UHQ1 174-258, followed by a 4-residue tail. It lacks Q9UHQ1 129-173 and 259-455.
- Domain consequences: it keeps 121 of 289 residues of PF02906 (Fe-only hydrogenase large-subunit C-terminal domain, Q9UHQ1 93-381) and none of PF02256 (Fe hydrogenase small subunit, 393-444). Of the 15 Q9UHQ1 cysteines it keeps 12, and loses Cys172 plus the C-terminal Cys374/Cys378 pair. The N-terminal cysteine-rich region (Cys3/6/11/53/56/59) is intact. So this is a truncated alternative gene-model product, not a fragment of a full-length protein. It is unlikely to fold into the full hydrogenase-like domain.
- PE level 1 rests on the Ser29 phosphopeptide (PMID:23186163). That residue is in the shared N-terminus, so it does not show that J3KS48 specifically is expressed.

### Evolutionary placement

- PANTHER geneinfo puts NARF (Q9UHQ1) in PTHR11615:SF124 "NUCLEAR PRELAMIN A RECOGNITION FACTOR". NARFL/IOP1 is a separate paralogous lineage in the same family (NARF/Nar1-like). UniProt cross-references only list the family PTHR11615 for both accessions.
- PAINT: Q9UHQ1 gets IBA lamin binding (GO:0005521) and is_active_in lamin filament (GO:0005638) from node PTN002614243, which is seeded by Q9UHQ1's own IPI/IDA (PMID:10514485). PAINT did not propagate any Fe-S assembly term to the NARF clade. I read that as a deliberate decision, and it is consistent with PMID:18270200 ("Knockdown of IOP2, in contrast, had no effect on either" for cytosolic and mitochondrial aconitase). J3KS48 receives no IBA.
- The family review `interpro/panther/PTHR11615/PTHR11615-review.yaml` says "No arbitrary PANTHER subfamily ... is assigned" and lists J3KS48 as the only "Human NARF" representative. It does not disagree with the placement, but it leaves it out: PANTHER does define SF124 for NARF. The family-review subfamily entry would better use Q9UHQ1 as representative and cite SF124. I did not edit it, since it is outside my gene folder.

### Literature (gene-level, canonical product)

- PMID:10514485: nuclear, partly at the lamina; binds the farnesylated prelamin A tail, and binding needs farnesylation and the CaaX motif.
- PMID:36490339 (full text): HIF-1 target in breast cancer cells; acts as a coactivator recruiting KDM6A to OCT4-bound NANOG/KLF4/SOX2 genes. The work is knockdown-based and does not specify an isoform. I did not propose any GO term from it, because it is not product-specific and the NEW bar is not met for J3KS48.
- No study tests J3KS48 itself.

### Decisions

- GO:0005634 nucleus (IEA, GO_REF:0000044): stays UNDECIDED. It is true for canonical NARF, but on J3KS48 the SubCell statement is ARBA-derived. NARF localization determinants are unmapped, and the product lacks about 55% of the canonical sequence.
- core_functions are left empty on purpose. No molecular function can be assigned to this truncated product with evidence. The gene-level functions (prelamin A binding, lamin binding, OCT4 coactivation) belong in a review of canonical Q9UHQ1.
- The description was rewritten to state gene-level biology and the product-specific deletions. I added PMID:36490339 and the falcon report as references, and marked the ProtNLM source file as provenance only (relevance NONE).
- Next relative: canonical Q9UHQ1 (same_gene_canonical). It has no review in the repo; the planned folder is `genes/human/NARF__Q9UHQ1`.
- No modules in `modules/` include NARF. `modules/dmel_iron_sulfur_cluster_assembly.yaml` covers the NARFL/Nar1 CIA lineage, not NARF.
