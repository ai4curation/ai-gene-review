# cem1: ProtNLM2 function-description review

Source: **pre-release `post-processed-2026_02_28k.xml`**, accession `O94297`. The exact entry is preserved in [cem1-protnlm-source.xml](cem1-protnlm-source.xml); all original evidence elements and model scores are retained in [cem1-protnlm-source.json](cem1-protnlm-source.json). This record is currently Swiss-Prot and is absent from the published 26,856-record TrEMBL pilot list. The current public ProtNLM endpoint returns this record; API availability is distinct from membership in the published pilot list. No training-membership inference is made.

## Original paragraph 1

> Involved in the type II fatty acid elongation cycle. Catalyzes the elongation of a wide range of acyl-ACP by the addition of two carbons from malonyl-ACP to an acyl acceptor. Can efficiently catalyze the conversion of palmitoleoyl-ACP (cis-hexadec-9-enoyl-ACP) to cis-vaccenoyl-ACP (cis-octadec-11-enoyl-ACP), an essential step in the thermal regulation of fatty acid composition.

Original evidence key(s): `2`.

| Atomic claim | Assessment | Evidence and limit |
|---|---|---|
| Participation in type II fatty-acid elongation | CNN | Diagnostic ketoacyl-synthase domains and the mitochondrial OXSM/Cem1 assignment support this conserved role. Human OXSM activity and complementation of budding-yeast cem1 establish a transferable mitochondrial mechanism (PMID:15668256). |
| Two-carbon addition from malonyl-ACP to an acyl acceptor | CNN | This is the conserved decarboxylative condensation chemistry of the mitochondrial ketoacyl-ACP synthase family. The target retains the annotated catalytic Cys170/His311/His351 residues, and UniProt explicitly transfers the reaction from characterized human OXSM. |
| Elongation of a wide range of acyl-ACP substrates | CNN as broad family-level capability; target range unresolved | Human OXSM directly elongates C2–C14 acyl substrates and restores growth of budding-yeast cem1. This supports broad chain-extension capability in a conserved mitochondrial homolog, while it does not measure which chain lengths S. pombe Cem1 efficiently accepts. |
| Efficient palmitoleoyl-ACP to cis-vaccenoyl-ACP conversion | UNC | The inspected mitochondrial OXSM experiments establish C2–C14 chain extension and do not establish this exact unsaturated C16 substrate preference in S. pombe. The conserved enzyme family and the presence of a synthase-2 domain label do not resolve target substrate preference. The wording also abbreviates an entire elongation cycle: the synthase itself yields a beta-ketoacyl intermediate, with further reactions required to yield the fully reduced elongated acyl chain. |
| Essential step in thermal regulation of fatty-acid composition | UNC | The available mitochondrial OXSM/Cem1 evidence concerns mitochondrial acyl-chain synthesis and lipoate-related metabolism. It neither demonstrates nor excludes an essential thermal-regulation role for S. pombe Cem1. Bacterial FabF thermoregulation cannot establish that target-specific physiological claim. |

## Primary evidence

- [PMID:15668256](https://pubmed.ncbi.nlm.nih.gov/15668256/) (cached as `publications/PMID_15668256.md`).
- [PMID:17242430](https://pubmed.ncbi.nlm.nih.gov/17242430/) (cached as `publications/PMID_17242430.md`).
- [PMID:16823372](https://pubmed.ncbi.nlm.nih.gov/16823372/) (cached as `publications/PMID_16823372.md`).

Family and feature provenance: [cem1-uniprot.txt](cem1-uniprot.txt).
