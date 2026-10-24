# ACAD9 (human, A0A7P0T7Z1) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: new review of benchmark accession A0A7P0T7Z1 (cohort MOD_EVOLUTION20). No ProtNLM2 file or
prediction-evidence folder was opened, and none of their output is used here. The folder
`genes/human/ACAD9/` is keyed to the canonical Swiss-Prot entry Q9H845, which has a complete review. This
accession therefore gets its own `ACAD9__A0A7P0T7Z1` folder, following the `SYMBOL__ACC` precedent.

### Setup

- `just fetch-gene human A0A7P0T7Z1 --alias ACAD9__A0A7P0T7Z1` gave 9 GOA rows. Eight are IEA (InterPro2GO,
  ARBA, SubCell, combined IEA). One is IDA from HPA immunofluorescence (GO_REF:0000052). There are no IBA rows.
- `just deep-research-falcon human ACAD9__A0A7P0T7Z1 --fallback perplexity-lite` FAILED. Falcon returned
  "Exception: Failed to authenticate", and perplexity-lite returned HTTP 401 insufficient_quota. No
  deep-research file was written. The literature base is the cached full-text primary papers on canonical
  ACAD9 (PMID:33320993, PMID:38086790, PMID:25721401, PMID:34646991; PMID:16020546 abstract only), plus the
  canonical review and its falcon report (`genes/human/ACAD9/`).

### Identity: an alternative gene model, not the canonical product

The analysis is in `ACAD9__A0A7P0T7Z1-bioinformatics/RESULTS.md` (script `compare_gene_model.py`).

- A0A7P0T7Z1 is the translation of Ensembl ENST00000680636 (ACAD9-219, ENSP00000504886). It is 626 aa long,
  against 621 aa for canonical Q9H845 (ENST00000308982).
- Residues 1-521 are identical. At residue 522, an alternative acceptor 94 nt upstream in exon 16 shifts the
  frame (94 mod 3 = 1). The result is an unrelated 105-residue Gly/Pro/His-rich tail (522-626) that MobiDB-lite
  predicts to be disordered. The stop codon is in the last exon, so a simple rule does not predict NMD. The
  exon-1 difference is in the 5' UTR.
- The product retains the transit peptide (1-37), all three ACAD Pfam domains, catalytic Glu426, the linker
  and the ECSIT-contact loop 488-496.
- The product loses most of the vestigial domain (522-587), the ECSIT-contact helix-turn-helix 554-560
  [PMID:33320993 "a helix‐turn‐helix (residues 554–560) and a loop (residues 488–496)"], and the
  domain-swapped dimer-stabilising C-terminal helix [PMID:38086790 "the C-terminal regions (residues
  600–621) form helix loops that are positioned around the neighbouring protomer thereby stabilising the
  active dimer"]. It lacks PF21343/IPR049448 (ACAD9-ACADV_C), which Q9H845 carries.
- PMID:25721401 places activity-preserving, assembly-impairing disease variants in this C-terminal domain,
  and links the domain to inner-membrane association ["Among the ACADs, ACAD9 is structurally closest to
  VLCAD; both of them have an extended C-terminal domain that has been linked with inner mitochondrial
  membrane association"].

### Evolutionary grounding

- PANTHER PTHR43884:SF9 ("COMPLEX I ASSEMBLY FACTOR ACAD9, MITOCHONDRIAL"), the same subfamily as Q9H845,
  mouse Q8JZN5, rat B1WC61 and Drosophila Egm Q5U117 (`interpro/panther/PTHR43884/PTHR43884-entries.csv`).
- PAINT: GO:0003995 is at the deep node PTN000744030. The ACAD9-specific terms (MCIA complex GO:0160295,
  complex I assembly GO:0032981, long- and medium-chain FA metabolism) are at PTN000856878 (taxon 33213),
  seeded by Q9H845. The benchmark accession receives no IBA. Its catalytic function is transferred from
  Q9H845 on the basis of sequence identity of the catalytic module, not a best hit.
- The family review `interpro/panther/PTHR43884/PTHR43884-review.yaml` lists A0A7P0T7Z1 as the SF9
  representative member. There is no disagreement about subfamily placement. One observation for the family
  review: the representative is a frameshifted alternative model, and Q9H845 would be a more representative
  member. This is not edited here, because it is outside this gene folder.

### Decisions (9 rows)

- ACCEPT: GO:0003995, GO:0004466, GO:0016627 and GO:0050660 (catalytic module and FAD-binding fold
  identical), and GO:0005739 (HPA IDA is gene-level, and the transit peptide is intact).
- MODIFY: GO:0006631 → GO:0006635 fatty acid beta-oxidation, and GO:0017099 → GO:0004466, because the
  demonstrated substrates are C16-C22. Both match the canonical review.
- UNDECIDED: GO:0005743 and GO:0031966. The C-terminal domain linked to membrane association is missing,
  and no experiment on this product exists.
- No NEW rows. The canonical ACAD9 complex I assembly / MCIA roles are deliberately not transferred. The
  product lacks the ECSIT-contact HTH and the dimer helix, and PMID:25721401 shows that the C-terminal domain
  carries the assembly-specific function. Downstream complex I deficiency phenotypes are not annotated.

### Relative to review next

The canonical product of the same gene, Q9H845, already has a complete review (`genes/human/ACAD9/`). The
closest experimentally characterised ortholog in a model organism, by PANTHER subfamily (SF9) and descent
from PTN000856878 (Bilateria), is Drosophila Egm (Q5U117), which has experimental (IDA) MCIA-complex membership and mitochondrial localisation (PMID:34386730).
Mouse Acad9 (Q8JZN5) is in the same subfamily but has only ISO/IEA/HDA annotations. Egm already has a
COMPLETE review at `genes/DROME/Egm/Egm-ai-review.yaml`.

### Modules

ACAD9 appears in `modules/fatty_acid_beta_oxidation.yaml`, `modules/complex_i_assembly_factors.yaml`,
`modules/oxphos.yaml` and `modules/electron_transfer_flavoprotein_system.yaml`. Those modules should cite the
canonical Q9H845, not this alternative model. Modules were not edited.
