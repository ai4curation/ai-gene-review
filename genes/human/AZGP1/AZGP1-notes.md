# AZGP1 notes

## 2026-10-05 review (PAINT, affinage)

- Structure: AZGP1 has an MHC class I fold without beta2m, and its groove holds a non-peptide ligand [PMID:10206894 "The 2.8 angstrom crystal structure of ZAG resembles a class I major histocompatibility complex (MHC) heavy chain, but ZAG does not bind the class I light chain beta2-microglobulin."]. It binds fatty acids (PMID:11425849). The crystal ligand is PEG, which competes with the fatty acid (PMID:15477100).
- All five MHC-type IBA rows are removed as PROPAGATION_BAD/FUNCTIONAL_DIVERGENCE: immune response, two antigen-presentation rows, T-cell cytotoxicity, and external side of plasma membrane (the last also COMPARTMENT_OR_COMPLEX_MISMATCH, since AZGP1 is secreted). The extracellular-region IBA is accepted.
- Transporter NAS and its derived IEA are removed: the 1982 paper proposes a soluble "carrier", which is not transmembrane transport. RNase NAS is UNDECIDED. The bitter-taste IDA (salivary correlation) and the sperm-nucleus HDA are marked as over-annotations.
- NEW: fatty acid binding (IDA, PMID:11425849), beta-3 adrenergic receptor binding (IDA, PMID:22227600) and positive regulation of lipid catabolic process (IDA, PMID:21245862). In the BP, ZAG is the signalling ligand, so it is placed in the regulation term rather than in lipolysis itself.
- The cancer and fibrosis literature in affinage (EMT, TGF-beta and others) is context-specific and is not annotated.

## 2026-10-05 revision (reviewer round 1)

- The NEW process is now GO:0010898 [PMID:21245862 "Recombinant ZAG stimulated lipolysis in human adipocytes."]. ABHD5 is a comparator in the repo that uses this term.
- Bitter taste was changed to REMOVE. Beta-2 AR binding was added. Receptor ligand activity is not asserted, because agonism in native cells is untested; it is raised as a question instead.
