# Azotobacter comparative-member consultation

Six species-level AZOVI entries are linked to the original isc-region deposit AF010139.1
(PMID:9582371). `member-map.yaml` gives accessions, deposited protein identifiers and
sequence hashes. The deposited DJ116 sequences exactly match the fetched UniProt proteins.
The strain annotations on the curated and unreviewed UniProt entries differ; the map
records that difference rather than silently equating all strains. In the native 2006 study,
DJ and derivative strains and reused original isc-region clones connect the experiments
to this housekeeping region. IscA O31271 is not the NifIscA paralog, and Fdx O69222 is
FdIV/FdxD, not FdI/FdxA.

## Source access and limits

- PMID:9582371: repository abstract plus the original ENA AF010139.1 record.
  The publisher full-text route returned an access error; no unseen methods are asserted.
- PMID:16936042: repository abstract retained; full text read through
  https://pmc.ncbi.nlm.nih.gov/articles/PMC1636278/ (including Table 1 and Results/Discussion).
  Native IscA dependence is oxygen conditional; HscBA depletion is a paired experiment.
- PMID:17237162: repository abstract retained; full text read through
  https://pmc.ncbi.nlm.nih.gov/articles/PMC1855825/.
  NifU replacement of IscU depends on expression/oxygen conditions; no tested replacement
  of IscS by NifS was established.
- PMID:16964969: repository abstract retained; full text read through
  https://pmc.ncbi.nlm.nih.gov/articles/PMC2518968/.
  This is an A. vinelandii protein reconstitution, with HscA hydrolysis and HscB-dependent
  transfer acceleration. Fdx is the cluster recipient in this experiment.
- PMID:18562278: repository abstract retained; PMC browser access returned a challenge,
  but the publisher full text was read at https://www.pnas.org/doi/10.1073/pnas.0803173105.
  Native scaffold occupancy and the substituted IscU-IscS complex are distinguished.
  The experiment does not assign a cluster-coordinating ligand to native IscS.
- PMID:10542283, PMID:10891064, PMID:16165131 and PMID:25447670: cached abstracts
  read at their stated scope. The last paper explicitly concerns archaeal IscS and cannot
  be relabeled as an Azotobacter binding experiment.

No cached publication was edited. External full-text access is additional review context,
not a claim that the repository contains the full text. Review quotations are from the
unchanged local cache or UniProt record.

## Decisions and validation limits

All 33 seeded annotations retain their original payload and ordering. There are no NEW
rows or retirements. Broad IscA cluster binding is inferred from independently classified
A-type domains and supported by native cysteine dependence; its specific cluster chemistry
remains unresolved. HscA/B folding annotations remain unresolved: their direct specialized maturation work
does not by itself demonstrate the correct-tertiary-structure endpoint required by GO0006457. The HscB oligomerization-domain name and ferredoxin
P450-associated fold do not establish those respective biological processes.

Configured Falcon research was attempted for all six genes; every request returned HTTP403
authentication failure. No provider research file was fabricated. PAINT-loss checks ran for
all six, but none of these accessions is a leaf in the corresponding cached family tree.
Their 'no loss' terminal messages therefore do not establish a checked loss-free lineage.

`check_preservation.py` checks seed payloads, frozen source hashes, complete decisions,
member-to-deposit sequence identity, and action accounting. These are preservation and
consistency checks, not independent biological assay validation. Gene validators check
schema, term use and citations. The full repository source snapshot remains in ignored cache;
`seed-baseline.yaml` retains the scoped subset and the complete snapshot's hash. `--all-sources`
checks that larger original snapshot as well when available. The frozen source snapshot
contains the publications that existed before review; new fetches are explicitly listed
in the final handoff and their hashes are recorded separately.
