# CACNB3: paired evidence notes

Human reference: https://www.uniprot.org/uniprotkb/P54284/entry

Primary source: [PMID:8119293 Cloning, chromosomal location and functional expression of the human voltage-dependent calcium-channel beta 3 subunit.](https://pubmed.ncbi.nlm.nih.gov/8119293/).

> The cloned H beta 3
> subunit was further expressed in Xenopus oocytes to demonstrate its ability to
> modulate VDCC activity.

The horse sequence comparison is in [CACNB3-bioinformatics/RESULTS.md](CACNB3-bioinformatics/RESULTS.md). Transfer is assessed for this exact accession; human biochemical evidence is not equine experimental validation.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not opened or used. Evidence: human CACNB3 UniProt record (P54284), cached abstracts, the PTHR11824 PAINT file and family review, and a new paralog/gene-model analysis (`CACNB3-bioinformatics/RESULTS-rereview.md`, script `compare_paralogs_rereview.py`).

### Identity of the benchmark accession

- A0A5F5PZM5 (517 aa, TrEMBL, PE3) is one of five UniProt products of the single horse gene ENSECAG00000012018 (VGNC:15992). It is an **alternative N-terminal (first-exon) gene model**, not a fragment: residues 1-49 (MAQGAKVSLRTNLSVELEGPRRFFPSLVRRQGLLQGKSGAAACPHIHQG) replace the 15-residue exon 1 of human isoform 1 (MYDDSYVPGFEDSEA); the remaining 465-residue core is identical to every other horse model and 99.78% identical to human P54284 (one substitution, S->N near the C-terminus).
- SH3, HOOK, guanylate-kinase-like (alpha-interaction-domain binding) and C-terminal regions are all present. Beta subunits have no catalytic residues; the GK-like domain is a protein-interaction module.
- No reviewed horse CACNB3 exists; the closest horse model to the human canonical sequence is F6SZ27 (same exon 1 as human isoform 1). The alternative exon 1 has no known functional consequence; beta N-termini tune inactivation kinetics in other paralogs but function transfer here rests on the conserved core.

### Evolutionary grounding

- Core identity to human paralogs: CACNB3 99.78%, CACNB4 74.14%, CACNB2 65.09%, CACNB1 63.36%. Plus beta3-specific signatures (IPR008079, PR01696, cd12042). Horse protein is the beta3 ortholog (human P54284 is PTHR11824:SF8).
- PAINT node PTN000930213 (family-wide in PTHR11824) carries voltage-gated calcium channel complex, calcium ion transport and high voltage-gated calcium channel activity. The MF IBA is seeded by one mouse beta subunit; beta subunits do not form the pore, so the MF is restated as calcium channel regulator activity (same conclusion as the human review and the PTHR11824 family review).
- PAINT node PTN002625095 (chemical synaptic transmission, seeded by one mouse beta) appears in the UniProt DR GO lines but is not in the horse GOA file; not added.

### Literature

- [PMID:8119293 "The cloned H beta 3 subunit was further expressed in Xenopus oocytes to demonstrate its ability to modulate VDCC activity."]
- [PMID:11160515 alpha1D L-type currents studied "co-expressed with alpha(2)delta-1 and beta(3a)"] - beta3 in an L-type complex.
- [PMID:34234349 "cryo-electron microscopy structures of human Cav2.2 (comprising the core α1 and the ancillary α2δ-1 and β3 subunits)"] - beta3 is a structural component of an N-type complex too, so beta3 is not L-type-restricted.

### Decisions

- voltage-gated / high voltage-gated calcium channel activity (IEA, IBA): MODIFY -> GO:0005246 calcium channel regulator activity.
- voltage-gated calcium channel complex (IBA, IEA), L-type VGCC complex (IEA), cytoplasm (IEA), calcium ion transmembrane transport (IEA): ACCEPT.
- calcium ion transport (IBA, IEA): MODIFY -> GO:0070588 calcium ion transmembrane transport (already carried; the beta subunit acts on transmembrane influx through the channel).
- membrane (IEA, projected from a human proteomics IDA): KEEP_AS_NON_CORE; beta3 is a peripheral, cytoplasmic-face subunit and has no transmembrane segment.

### Relative

Human CACNB3 P54284 (ortholog, same PANTHER subfamily SF8), reviewed at `genes/human/CACNB3/CACNB3-ai-review.yaml` (all annotations have actions). No horse canonical Swiss-Prot entry to review instead.
