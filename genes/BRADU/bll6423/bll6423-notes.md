# bll6423 review notes

## 2026-11-06 annotation review

Identity: Q89GC2, frozen official USDA110 taxon224911 record; retain locus symbol bll6423. The 2013 paper's Bradyrhizobium japonicum USDA110 name is the historical name of this strain. It describes related operon organization, explicitly leaving function unknown.

bll6423 versus Hsero_1010: 127/192 identical aligned residues (66.1%); lengths 194/196; target coverage 99.0%.

Bll6423 is a cupin type-2 protein in a conserved aromatic-compound catabolic locus of Bradyrhizobium diazoefficiens USDA 110. It is related to Herbaspirillum FdeH. Cupins in the related Variovorax isoflavone pathway catalyze downstream intermediate conversion, but the substrate and biochemical contribution of Bll6423 have not been established; it is not known to be an obligatory ring-cleavage partner.

Reviewed every seeded annotation; preserved each non-review payload and ordering. No new biological-process assertion: candidate locus membership is useful context, but the actual work of this protein in a USDA110 flavonoid reaction remains inferential and competing substrate/partner roles are not resolved. This is not a universal demand for direct assays; reaction-class inference is accepted where sequence, architecture and characterized homolog chemistry agree. No BP comparator query was used to manufacture a gap.

Research: genuine default-provider Falcon request (`just deep-research BRADU bll6423 --provider falcon`) failed with HTTP403 authentication error. No provider research file was created. Manual assessment uses frozen target record, primary PMID23125118, PMID27059806, PMID39107441 and PMID38707841 and the scoped source evidence and sequence comparison in `analysis/module_audits/bacterial_flavonoid_degradation/bradu-panel/`. These primaries are comparative, never target enzyme assays. Existing source files were not refreshed.

Core synthesis retains only supported reaction classes/cofactor properties. No precise molecular-function core is supplied for uncharacterized cupin/epimerase candidates solely to fill the module.
