# PTHR42803 specificity and lineage evidence

The canonical family review was absent. Existing metadata and reviewed-member inventory were frozen before this audit; neither was edited. The metadata description is explicitly unchecked LLM text and is not used as experimental evidence.

## Tree and PAINT

The cached PANTHER tree contains 23 leaves and 13 internal nodes. Twenty-one sampled leaves are SF1 and two are SF3. Q9I610 maps to PTN002450036 and Q9I612 to PTN002450040, both SF1. O53666 maps to PTN002450030 in SF1. Their classification is independently confirmed by current UniProt cross-references.

The shared Pseudomonas node PTN002450031 contains Q9HU02, Q9HWI2, Q9I610, Q9I460, Q9I612 and Q9I611. Two characterized descendants do not establish uniform substrate chemistry across these six paralogs. No branch-specific functional origin or loss is assigned here.

Normal scoped PAINT retrieval resolved 36 nodes but no IBD, IRD, IKR or other node-level assertion for this family. An independent intersection of the TreeGrafter family-node set and IBD.gaf also returned zero rows. Thus there is no actual assertion to mark SOUND or TOO_DEEP; inventing a node assessment would be incorrect. Absence from the retrieved snapshot is not proof that the family has no biological function. Source URLs and hashes are recorded in lineage-proof.yaml.

## Subfamily heterogeneity

### Q5LLW7
URL https://rest.uniprot.org/uniprotkb/Q5LLW7.json ; accessed 2026-11-06; SHA256 9cf32811acdd75b14d537b4b99ef79508431cdfb7bb0bb32c18d9133cbf66933.
Involved in the assimilation of dimethylsulphoniopropionate (DMSP), an important compound in the fixation of carbon in marine phytoplankton, by mediating the conversion of 3-(methylthio)propanoyl-CoA (MMPA-CoA) to 3-(methylthio)acryloyl-CoA (MTA-CoA)
Experimental attribution: PubMed:21562561.

### O53666
URL https://rest.uniprot.org/uniprotkb/O53666.json ; accessed 2026-11-06; SHA256 f2260013441f11805b2ecb125df053e6cf1ce60fc2cc98ef578588489d982295.
Acyl-CoA dehydrogenase that exhibits broad specificity for linear acyl-CoA substrates, with a preference for long-chain substrates
Experimental attribution: PubMed:32601219.

These are curated experimentally attributed UniProt FUNCTION statements, not an independent reanalysis of those two original papers. Q5LLW7 is DmdC/SPO3804 in Ruegeria pomeroyi DSS-3 and O53666 is FadE5/Rv0244c in M. tuberculosis H37Rv. Both classify as SF1 despite different physiological substrate contexts. Q5LLW7 is not a leaf in the cached tree; no PTN is invented for it.

## Exact PAO1 characterization

The independently verified PA0506/Q9I612 and PA0508/Q9I610 constructs are full-length PAO1 sequences with a GH tag remnant. Wild-type structures are 8PNS and 8PNG, while 8PU5 is Q9I612 E441A and 8R1E is Q9I610 M130G/E296A/Q303A. The released gene source analysis records exact full-sequence identity and mutant differences.

PMID40057486 Table1 supports FadE1 turnover of C16/C18/C8 and weaker C6; C4 is not determined. FadE2 turns over C4/C6/C8 but has no detected activity on C16/C18 in the reported assay. The widened FadE2 triple mutant acquires low C16 activity; its property must not be transferred to the wild type. SF1 membership therefore cannot grant a uniform long-chain range, broad linear-substrate preference, or a sulfur-specific DmdC substrate.

The assays use artificial ferrocenium, and the paper explicitly calls physiological ETF transfer predicted rather than demonstrated. The shared catalytic concept used in the exact gene reviews is acyl-CoA dehydrogenase activity (acceptor unspecified). GO0003995 and its chain-specific descendants instead name ETF; they cannot be granted family-wide from these data. A bound FAD cofactor is distinct from an experimentally identified physiological ETF partner.

PAO1 recombinant enzyme chemistry, PA14 growth mutants, Pa10348 proteomics and PAO1 Galleria infection mutants are kept separate. The two PAO1 gene process proposals are IC participation in beta-oxidation, not direct PAO1 growth/flux measurements or autonomous complete-chain oxidation. Family membership is insufficient to transfer these pathway roles to every SF1 member, especially the characterized DmdC context.

GO:0052890 names a flavin acceptor without naming ETF. The family review retains this broad flavin-dependent CH-CH chemistry; the uncertainty about downstream physiological electron transfer applies to ETF-specific terms and does not negate the FAD catalytic step.
