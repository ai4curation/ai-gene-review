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

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

This entry was written during a re-review that deliberately ignored the ProtNLM2 predictions; the earlier sections above, including the ProtNLM2 claim assessments, are retained unchanged.

Full re-review, 2026-10-20. This review was written without reference to any ProtNLM output.

### Product identity

- J3KS48 is an unreviewed TrEMBL entry with 217 aa, encoded by Ensembl ENST00000581202 (ENSP00000462305) at the NARF locus (HGNC:29916). The reviewed canonical product is Q9UHQ1, with 456 aa.
- J3KS48 is not one of UniProt's four named Q9UHQ1 isoforms (isoform 2: insertion after 256; isoform 3: Δ38-85; isoform 4: Δ1-59). It is a separate gene-model product.
- Alignment (`NARF-bioinformatics/RESULTS.md`, script reads the sequence from `NARF-uniprot.txt`):
  - J3KS48 1-128 = Q9UHQ1 1-128 (identical).
  - J3KS48 129-213 = Q9UHQ1 174-258 (identical). Reference residues 129-173 are skipped.
  - J3KS48 214-217 is a short alternative tail and is not homologous to the reference. The aligner scatters it opposite reference 383-385 and 456, which is an alignment artefact.
  - Reference residues 259-456 are absent. They contain the C-terminal half of the Pfam PF02906 large-subunit-like domain (93-381 in Q9UHQ1, truncated to 129-217 in J3KS48) and all of the PF02256 small-subunit-like domain (393-444).
  - Cysteines in the hydrogenase-like H-cluster-motif region: C172 (TSACP motif) is lost to the internal deletion, and C374 and C378 are lost to the C-terminal truncation. The N-terminal cysteines (3, 6, 11, 53, 56, 59), C192, C228 (APCYDK) and C252 are kept.
- Conclusion: J3KS48 is a severely truncated alternative product. Peptides from it have been seen in MS (PeptideAtlas/ProteomicsDB), but they could come from the regions it shares with the canonical protein, so expression of J3KS48 as such is unproven.

### Evolutionary placement

- PANTHER PTHR11615 (NITRATE, FORMATE, IRON DEHYDROGENASE). Q9UHQ1 is in subfamily SF124 (NUCLEAR PRELAMIN A RECOGNITION FACTOR), per the PANTHER 19 geneinfo API. The paralog NARFL/CIAO3 (Q9H6Q4) is in SF322 (CYTOSOLIC IRON-SULFUR ASSEMBLY COMPONENT 3). J3KS48 is not a PANTHER reference protein; it maps to the same gene (ENSG00000141562) and is therefore SF124.
- PAINT node PTN002614243 propagates GO:0005521 lamin binding (enables) and GO:0005638 lamin filament (is_active_in) from Q9UHQ1 to mouse Narf (Q9CYQ7) and Q9UHQ1 itself. No PAINT node gives NARF any Fe-S assembly or CIA term. I read that omission as deliberate: the CIA function stays on the NARFL/Nar1 side.
- The paralog boundary has been tested directly. Knockdown of IOP1/NARFL lowers cytosolic aconitase activity, while knockdown of IOP2/NARF has no effect [PMID:18270200 "Knockdown of IOP2, in contrast, had no effect on either."].

### Biology (gene level, full-length protein)

- Nuclear; partly at the lamina; binds the farnesylated prelamin A tail [PMID:10514485 "When a FLAG epitope-tagged Narf is expressed in HeLa cells, it is exclusively nuclear and partially co-localizes with the nuclear lamina."]. Its similarity to hydrogenases is limited [PMID:10514485 "Narf has limited homology to iron-only bacterial hydrogenases and eukaryotic proteins of unknown function."].
- Acts as a hypoxia-induced OCT4 coactivator that recruits KDM6A [PMID:36490339 "NARF recruits histone lysine demethylase 6A (KDM6A) to OCT4 binding sites, thereby licensing OCT4-mediated transcriptional activation of the NANOG, SOX2, and KLF4 genes."]. This comes from breast cancer cell lines in a single study.
- The deep research (falcon) also reports an MS iron-deposition association (Ding 2020) and an Alu-exonization editing study (Lev-Maor 2007). Neither defines a molecular function, so neither is used for annotation.

### Decisions

- GO:0005634 nucleus (IEA, SubCell): ACCEPT. The location is experimentally established for the gene product, nothing in the J3KS48 sequence argues against it, and the term is broad enough not to depend on the deleted regions. The earlier review had this as UNDECIDED; I changed it because the claim holds at gene level and is conservative enough to apply to this product.
- No NEW annotations. Lamin binding and transcription coactivator activity are supported for the full-length protein, but the binding regions have not been mapped and J3KS48 lacks 239 reference residues, so neither activity is transferred to this product.

### Relatives and family

- Closest experimentally characterised relative: Q9UHQ1, the canonical NARF product of the same gene (SF124, PAINT donor at PTN002614243). The repo has no review keyed to Q9UHQ1; this folder is keyed to J3KS48. No NARF ortholog in another model organism has been characterised experimentally.
- NARFL/CIAO3 (Q9H6Q4, SF322) is a different subfamily. Its CIA functions must not be transferred.
- Family review `interpro/panther/PTHR11615/PTHR11615-review.yaml` agrees on keeping NARF and NARFL separate and on nucleus being unresolved family-wide. It assigns no PANTHER subfamily id: its "Human NARF" subfamily has no term. PANTHER itself places NARF in SF124 and NARFL in SF322. This is not a disagreement, but the family review could record those ids.
- Modules: no NARF-containing module. `modules/dmel_iron_sulfur_cluster_assembly.yaml` covers the CIA pathway with fly CIAO3 (CG17683), the NARFL-type paralog, and NARF does not belong there.
