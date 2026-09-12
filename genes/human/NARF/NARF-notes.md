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
