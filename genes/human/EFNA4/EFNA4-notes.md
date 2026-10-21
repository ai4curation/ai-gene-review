# EFNA4 (P52798) — curation notes

Deep-research providers are unavailable in this environment, so these notes come from the
cached publications, the UniProt record and PubMed.

## Protein

Ephrin-A4 (LERK-4, EPLG4) is a GPI-anchored ligand for EphA receptor tyrosine kinases.
Signal peptide 1-25, mature chain 26-170, GPI-anchor site at residue 170 with the
propeptide 171-201 removed. There is no transmembrane segment: the mature protein sits on
the **outer leaflet of the plasma membrane**, fully extracellular apart from the lipid
anchor.
[file:human/EFNA4/EFNA4-uniprot.txt "Cell surface GPI-bound ligand for Eph receptors, a family of receptor tyrosine kinases which are crucial for migration, repulsion and adhesion during neuronal, vascular and epithelial development."]
[file:human/EFNA4/EFNA4-uniprot.txt "SUBCELLULAR LOCATION: [Isoform 1]: Cell membrane; Lipid-anchor, GPI-anchor."]

Isoform 2 is secreted, which is the basis of the extracellular-region annotation.
[file:human/EFNA4/EFNA4-uniprot.txt "SUBCELLULAR LOCATION: [Isoform 2]: Secreted"]

## Function

Promiscuous binding to EphA receptors, with contact-dependent bidirectional signalling.
Surface plasmon resonance shows EphA4 binds ephrin-A4 with the highest affinity of the
ephrins tested.
[PMID:19836338 "We find that EphA4 has greatest affinity for ephrinA4 (KD = 36 nM)"]
EphA1 also binds A-type ligands including ephrin-A4 (PMID:11519828), and EphA10 binds
mainly ephrin-A ligands (PMID:15777695).

## Notable annotation problem

`GO:0005005 transmembrane-ephrin receptor activity` (TAS, PMID:8660976) is a **receptor**
activity term — "Combining with a transmembrane ephrin to initiate a change in cell
activity" — and belongs to Eph receptors, not to a GPI-anchored ephrin-A ligand. The
cited paper is a gene-mapping paper that describes LERK-1/3/4 as membrane-anchored
ligands. Reviewed as MODIFY to `GO:0046875 ephrin receptor binding`.

The two high-throughput interactome rows (TUSC5, TMEM147) carry no functional content and
are removed under the protein-binding policy; the EphA4 and EphA10 rows are modified to
ephrin receptor binding.

Localization conclusion: plasma membrane, GPI-anchored on the extracellular face (cell
surface accessible); a secreted isoform accounts for the extracellular-region row.
