# bll6422 review notes

## 2026-11-06 annotation review

Identity: Q89GC3, frozen official USDA110 taxon224911 record; retain locus symbol bll6422. The 2013 paper's Bradyrhizobium japonicum USDA110 name is the historical name of this strain. It describes related operon organization, explicitly leaving function unknown.

bll6422 versus Hsero_1011: 202/327 identical aligned residues (61.8%); lengths 344/327; target coverage 95.1%.

Bll6422 is a fumarylacetoacetate-hydrolase-fold enzyme candidate in a conserved aromatic-compound catabolic locus of Bradyrhizobium diazoefficiens USDA 110. It is related to FdeI proteins; the fold accommodates several reaction classes, and the proposed late flavonoid-intermediate decarboxylation and dehydration reactions remain unassigned experimentally. Its native substrate and reaction are unknown.

Reviewed every seeded annotation; preserved each non-review payload and ordering. No new biological-process assertion: candidate locus membership is useful context, but the actual work of this protein in a USDA110 flavonoid reaction remains inferential and competing substrate/partner roles are not resolved. This is not a universal demand for direct assays; reaction-class inference is accepted where sequence, architecture and characterized homolog chemistry agree. No BP comparator query was used to manufacture a gap.

Research: genuine default-provider Falcon request (`just deep-research BRADU bll6422 --provider falcon`) failed with HTTP403 authentication error. No provider research file was created. Manual assessment uses frozen target record, primary PMID23125118, PMID27059806, PMID39107441 and PMID38707841 and the scoped source evidence and sequence comparison in `analysis/module_audits/bacterial_flavonoid_degradation/bradu-panel/`. These primaries are comparative, never target enzyme assays. Existing source files were not refreshed.

Core synthesis retains only supported reaction classes/cofactor properties. No precise molecular-function core is supplied for uncharacterized cupin/epimerase candidates solely to fill the module.
