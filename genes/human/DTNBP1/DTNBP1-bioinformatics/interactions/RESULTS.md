# Interaction reference-identity results

The frozen DTNBP1 input contains 95 selected IntAct records. All 190 side-specific sequence/taxon ROGIDs match the 26 supplied official reference sequences. The independent SNAPIN-target run selects nine records and verifies 18 reference identities. These counts were read from the actual script outputs; they are not encoded as expected results in the algorithm.

The computational result verifies database reference identity only. It cannot establish experimental insert sequence, native physiology, directness of co-complex association, affinity or product-specific function. The original methods, spoke-expansion markers, negative flags and side-specific features remain decisive. In particular, the SYBU pair's 1–189 feature is attached to DTNBP1, while the separate source table does not confirm that boundary.

`source-manifest.json` records the live-source URL, original snapshot hash, unchanged source-line selection and sequence provenance. The finite inputs permit reproduction without a network request. The control uses SNAPIN, a different protein, without adding any functional conclusion about it.

- [x] The algorithm accepts arbitrary supplied MITAB, FASTA and target; no gene-specific result or biological conclusion is encoded.
- [x] It was executed on DTNBP1 and on the independent SNAPIN input.
- [x] Both runs completed and their direct JSON outputs are included.
- [x] All source lines and reference sequences are derived from authenticated database captures.
- [x] The conclusions remain limited to reference identity and preserve assay/insert uncertainty.

## Independent partner-class evidence

The binding refinements combine positive interaction records with separately established partner functions. The reference-identity calculation above does not derive these biological classifications. Official records below were inspected in the 2026-10-18 source audit.

| Partner | Classification supporting the binding term | Source and scope |
|---|---|---|
| ELOVL7 / A1L3X0 | Fatty-acid elongation enzyme, EC 2.3.1.199; supports enzyme binding (GO:0019899). | [Official UniProt function and catalytic-activity record](https://rest.uniprot.org/uniprotkb/A1L3X0.json); the catalytic assignment includes experimental evidence. |
| P4HA3 / Q7Z4N8 | Prolyl hydroxylase catalytic subunit, EC 1.14.11.2; supports enzyme binding (GO:0019899). | [Official UniProt function and catalytic-activity record](https://rest.uniprot.org/uniprotkb/Q7Z4N8.json); the catalytic assignment includes experimental evidence. |
| DRC12 / Q494R4 | Axonemal nexin-dynein regulatory-complex component; supports cytoskeletal protein binding (GO:0008092). | [Official UniProt function record](https://rest.uniprot.org/uniprotkb/Q494R4.json); this functional assignment is by similarity to Q22RH5, not a newly established human functional assay. |
| KANSL1 / Q7Z3B3 | Participates in spindle assembly and microtubule stability; supports cytoskeletal regulatory protein binding (GO:0005519). | [Official UniProt function record](https://rest.uniprot.org/uniprotkb/Q7Z3B3.json) and [Meunier et al. 2015, *An epigenetic regulator emerges as microtubule minus-end binding and stabilizing factor in mitosis*](https://pmc.ncbi.nlm.nih.gov/articles/PMC4918316/). |

The KANSL study reports human-cell spindle localization and perturbation evidence for KANSL1 and KANSL3. Its cell-free work uses Drosophila proteins and Xenopus extracts; the autonomous minus-end-binding activity is specifically established for KANSL3. KANSL1's regulatory classification does not require transferring that autonomous activity to KANSL1 or to dysbindin. This is a documented mitotic role alongside KANSL1's NSL-complex transcriptional role.

These classifications describe the assayed partners. They do not assign their catalysis, spindle regulation or native compartments to DTNBP1, and do not turn a positive two-hybrid result into demonstrated physiological colocalization. SSC5D's association remains non-core because an informative replacement for that assayed association has not been established.
