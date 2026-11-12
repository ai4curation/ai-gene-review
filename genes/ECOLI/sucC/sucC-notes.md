# sucC (P0A836) notes

## 2026-11-11 first review

Written as part of the evolutionary review of the succinyl-CoA synthetase families; the E. coli subunits are PAINT seeds for both families. See genes/yeast/LSC2/LSC2-bioinformatics/RESULTS.md.

- Genes and operon [PMID:3543212 "The newly defined genes express polypeptides of 41 kDa (sucC) and 31 kDa (sucD), corresponding to the beta and alpha subunits of succinyl-CoA synthetase, respectively."].
- Structure: alpha2beta2 [PMID:8144675 "The quaternary organization of the E. coli enzyme is an alpha 2 beta 2 heterotetramer."]; CoA and the phosphohistidine on the alpha subunit [PMID:8144675 "One molecule of coenzyme A is bound to each alpha-subunit at a typical nucleotide-binding motif, and His-246 of each alpha-subunit is phosphorylated."]; nucleotide on the beta subunit [PMID:10625475 "X-ray diffraction data revealed an ADP-Mg(2+) complex bound in the ATP-grasp fold of the N-terminal domain of each beta-subunit"].
- Nucleotide use: ATP preferred, GTP accepted [PMID:22751660 "This contrasts with Escherichia coli SCS, which uses GDP/GTP but prefers ADP/ATP"]. UniProt gives Km 70 uM for ATP and 394 uM for GTP, kcat 2684 and 1471 per minute (attributed to PMID:10353839), so kcat/Km with GTP is about a tenth of that with ATP. GDP-forming activity is therefore kept as a non-core secondary activity, not accepted as core and not removed.
- Position 20 of the beta subunit is Pro; changing it to Gln, the residue of GTP-specific animal subunits, improves GTP use [PMID:10353839 "A mutant protein designed to probe nucleotide specificity (P20betaQ) had a Km(app) for GTP that was more than 5 times lower than that of wild-type SCS"].
- Evolutionary reading: the E. coli enzyme shows the dual-specificity bacterial state. It is the reason PAINT can defend GDP-forming activity at the root of the alpha family, and it is not a guide to fungi, whose single beta subunit does not use GTP.
- cytoplasm (HDA) modified to cytosol; GO:0042709 marked too general beside GO:0009361; protein binding rows with the partner subunit removed under the policy.
- metal ion binding (IEA) modified to magnesium ion binding.
- PMID:7040388 has no abstract and no cached full text; its EXP row is accepted on the UniProt attribution only.

### Not done

- Fitness data: just fetch-fitness failed (the fitness browser was unreachable and no local FEBA database is installed).
- Most cited papers are abstract-only in the cache.

### OpenScientist deep research (added after the review)

`just deep-research-openscientist ECOLI sucC` completed and is stored as sucC-deep-research-openscientist.md. It agrees with every action in the review and changed none. It added two references that were then cached and checked: solubility and the His246 substitution [PMID:2548486 "No activity was detected after the histidine residue at the phosphorylation site of the alpha-subunit was replaced by aspartate"], and anaerobic repression of the operon [PMID:9209026 "is provided by the arcA and fnr gene products"]. The run was given the gene name, so it is a second reading of the literature, not independent evidence.
