# SLC16A11 (horse, F6YMY3) gene-model comparison

Script: `compare_gene_models.py` (run with `uv run --script compare_gene_models.py`);
raw output: `results_compare_gene_models.txt`. Sequences fetched live from UniProt REST.
The human reference record used for comparison is saved as `SLC16A11-human-Q8NCK7-uniprot.txt`.

## Gene models

All five horse TrEMBL SLC16A11 entries are products of one Ensembl gene, ENSECAG00000023791.
Ensembl flags ENSECAT00000025548 (protein ENSECAP00000021253 = F6YMY3, 614 aa) as the
canonical transcript. Other products: A0A9L0RBE3 (520 aa), A0A5F5PX05 (415 aa),
A0A9L0SMV2 (392 aa), A0A9L0SA34 (308 aa). F6YMY3 and A0A9L0RBE3 are both placed in
PANTHER PTHR11360:SF80 (MONOCARBOXYLATE TRANSPORTER 11), the subfamily of human SLC16A11 (Q8NCK7, 447 aa).

## Findings

- F6YMY3 residues 74-487 align to the full human sequence (1-447). Identity is 86.5% over aligned pairs.
- N-terminus: F6YMY3 has a 73-residue extension upstream of the residue matching human Met1
  (horse `AMTPKPAGPPDGG...` vs human `MTPQPAGPPDGG...`). MobiDB-lite calls it disordered. The human
  UniProt entry records "Erroneous initiation; Note=Extended N-terminus" cautions for three human cDNAs.
  The horse extension is therefore most likely an upstream-initiation artefact. It is not a conserved domain.
- C-terminus: identity in 40-aa windows stays at 0.80-0.97 through human residue ~380. It falls to 0.12-0.35
  over human 361-440. That stretch covers human TM12 (383-403) and the cytoplasmic C-terminal tail.
  F6YMY3 has a divergent 127-residue C-terminal overhang in its place, and Phobius predicts only 9 TM helices for it.
  A0A9L0RBE3 is a product of the same gene. It keeps the conserved C-terminus (window identity 0.78-0.95 to the end),
  so the divergent C-terminus of F6YMY3 comes from alternative or mispredicted 3' exon structure.
  It is not a horse-specific loss of the ancestral C-terminal region.
- Conclusion: F6YMY3 is an alternative (Ensembl-canonical but probably aberrant) gene model of horse SLC16A11.
  It keeps TM1-TM11 of the MFS fold and lacks the conserved TM12 and C-terminal tail. Function claims in the
  review apply to the gene product (the SLC16A11 transporter). Whether the F6YMY3 polypeptide itself is a
  functional transporter has not been tested.
