# ARMC8 review notes

## Sources
- The affinage narrative (trust gates clear) centres on cancer-cell EMT and Wnt phenotypes and omits the CTLH complex. I marked it LOW_QUALITY.
- CTLH (mammalian GID E3) literature:
  - PMID:17467196: ARMC8alpha/beta in the RanBPM complex.
  - PMID:31285494: human CTLH E3 targets muskelin.
  - PMID:35682545: review; ARMC8 is a scaffold "similar to Gid5".
  - Reactome R-HSA-9861563 and R-HSA-9861640: CTLH ubiquitinates LDHA and PKM.
- Orthology: PMID:30482882 concludes "Armc8 is not the human ortholog of yeast Gid5/Vid28". PMID:35682545 notes the two are structurally similar. The IBA (PTN000402070, seeded by yeast Gid5) is still sound for GID complex membership, because ARMC8 has direct human evidence.

## Decisions
- ACCEPT:
  - GID complex (IBA, NAS) and proteasome-mediated catabolism (IBA, NAS).
  - Nucleus, nucleoplasm, cytoplasm and cytosol (IDA, IEA, TAS).
- KEEP_AS_NON_CORE: extracellular region and neutrophil granule lumens (Reactome degranulation proteomics).
- REMOVE: RMND5A and TCF12 protein binding (policy).

## Review round 1 (PR #4192)
- PMID:29911972 (Lampert 2018, full text) is now cited. It used ARMC8 as the AP-MS bait that defined the human GID/CTLH complex, and showed that the recombinant complex ubiquitinates HBP1 in vitro with UBE2H.
- NEW ubiquitin protein ligase activity (GO:0061630), qualifier contributes_to (IDA). It is also the core function's contributes_to_molecular_function.
- The nucleus and cytoplasm rows now quote the complex's nucleus-and-cytoplasm localization, replacing a content-free sentence.
- The GID complex row quotes the alpha-isoform GID4 binding (PMID:35682545). HBP1 in suggested_experiments now has provenance.
- The EMT/Wnt cancer literature in the affinage record yields no GO terms, because it consists of knockdown or overexpression phenotypes in cancer cell lines without a mechanism tied to the CTLH activity.
