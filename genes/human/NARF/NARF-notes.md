# NARF (J3KS48) review notes

Full re-review, 2026-10-20. This review was written without reference to any ProtNLM output.

## Product identity

- J3KS48 is an unreviewed TrEMBL entry with 217 aa, encoded by Ensembl ENST00000581202 (ENSP00000462305) at the NARF locus (HGNC:29916). The reviewed canonical product is Q9UHQ1, with 456 aa.
- J3KS48 is not one of UniProt's four named Q9UHQ1 isoforms (isoform 2: insertion after 256; isoform 3: Δ38-85; isoform 4: Δ1-59). It is a separate gene-model product.
- Alignment (`NARF-bioinformatics/RESULTS.md`, script reads the sequence from `NARF-uniprot.txt`):
  - J3KS48 1-128 = Q9UHQ1 1-128 (identical).
  - J3KS48 129-213 = Q9UHQ1 174-258 (identical). Reference residues 129-173 are skipped.
  - J3KS48 214-217 is a short alternative tail and is not homologous to the reference. The aligner scatters it opposite reference 383-385 and 456, which is an alignment artefact.
  - Reference residues 259-456 are absent. They contain the C-terminal half of the Pfam PF02906 large-subunit-like domain (93-381 in Q9UHQ1, truncated to 129-217 in J3KS48) and all of the PF02256 small-subunit-like domain (393-444).
  - Cysteines in the hydrogenase-like H-cluster-motif region: C172 (TSACP motif) is lost to the internal deletion, and C374 and C378 are lost to the C-terminal truncation. The N-terminal cysteines (3, 6, 11, 53, 56, 59), C192, C228 (APCYDK) and C252 are kept.
- Conclusion: J3KS48 is a severely truncated alternative product. Peptides from it have been seen in MS (PeptideAtlas/ProteomicsDB), but they could come from the regions it shares with the canonical protein, so expression of J3KS48 as such is unproven.

## Evolutionary placement

- PANTHER PTHR11615 (NITRATE, FORMATE, IRON DEHYDROGENASE). Q9UHQ1 is in subfamily SF124 (NUCLEAR PRELAMIN A RECOGNITION FACTOR), per the PANTHER 19 geneinfo API. The paralog NARFL/CIAO3 (Q9H6Q4) is in SF322 (CYTOSOLIC IRON-SULFUR ASSEMBLY COMPONENT 3). J3KS48 is not a PANTHER reference protein; it maps to the same gene (ENSG00000141562) and is therefore SF124.
- PAINT node PTN002614243 propagates GO:0005521 lamin binding (enables) and GO:0005638 lamin filament (is_active_in) from Q9UHQ1 to mouse Narf (Q9CYQ7) and Q9UHQ1 itself. No PAINT node gives NARF any Fe-S assembly or CIA term. I read that omission as deliberate: the CIA function stays on the NARFL/Nar1 side.
- The paralog boundary has been tested directly. Knockdown of IOP1/NARFL lowers cytosolic aconitase activity, while knockdown of IOP2/NARF has no effect [PMID:18270200 "Knockdown of IOP2, in contrast, had no effect on either."].

## Biology (gene level, full-length protein)

- Nuclear; partly at the lamina; binds the farnesylated prelamin A tail [PMID:10514485 "When a FLAG epitope-tagged Narf is expressed in HeLa cells, it is exclusively nuclear and partially co-localizes with the nuclear lamina."]. Its similarity to hydrogenases is limited [PMID:10514485 "Narf has limited homology to iron-only bacterial hydrogenases and eukaryotic proteins of unknown function."].
- Acts as a hypoxia-induced OCT4 coactivator that recruits KDM6A [PMID:36490339 "NARF recruits histone lysine demethylase 6A (KDM6A) to OCT4 binding sites, thereby licensing OCT4-mediated transcriptional activation of the NANOG, SOX2, and KLF4 genes."]. This comes from breast cancer cell lines in a single study.
- The deep research (falcon) also reports an MS iron-deposition association (Ding 2020) and an Alu-exonization editing study (Lev-Maor 2007). Neither defines a molecular function, so neither is used for annotation.

## Decisions

- GO:0005634 nucleus (IEA, SubCell): ACCEPT. The location is experimentally established for the gene product, nothing in the J3KS48 sequence argues against it, and the term is broad enough not to depend on the deleted regions. The earlier review had this as UNDECIDED; I changed it because the claim holds at gene level and is conservative enough to apply to this product.
- No NEW annotations. Lamin binding and transcription coactivator activity are supported for the full-length protein, but the binding regions have not been mapped and J3KS48 lacks 239 reference residues, so neither activity is transferred to this product.

## Relatives and family

- Closest experimentally characterised relative: Q9UHQ1, the canonical NARF product of the same gene (SF124, PAINT donor at PTN002614243). The repo has no review keyed to Q9UHQ1; this folder is keyed to J3KS48. No NARF ortholog in another model organism has been characterised experimentally.
- NARFL/CIAO3 (Q9H6Q4, SF322) is a different subfamily. Its CIA functions must not be transferred.
- Family review `interpro/panther/PTHR11615/PTHR11615-review.yaml` agrees on keeping NARF and NARFL separate and on nucleus being unresolved family-wide. It assigns no PANTHER subfamily id: its "Human NARF" subfamily has no term. PANTHER itself places NARF in SF124 and NARFL in SF322. This is not a disagreement, but the family review could record those ids.
- Modules: no NARF-containing module. `modules/dmel_iron_sulfur_cluster_assembly.yaml` covers the CIA pathway with fly CIAO3 (CG17683), the NARFL-type paralog, and NARF does not belong there.
