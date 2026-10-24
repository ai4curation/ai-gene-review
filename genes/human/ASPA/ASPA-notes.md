# ASPA manual research, 2026-09-28

The normal seed contains 35 source assertions for human ASPA (P45381, HGNC:756), with no alternative-product list. The protected baseline remains unchanged. One deep-research attempt ended without an artifact; one ordinary publication batch reached its 100-second bound without creating a cache. These outcomes do not establish a provider-specific cause. The following is manual research, not provider output.

## Catalysis and cellular role

Human ASPA hydrolyzes N-acetyl-L-aspartate (NAA) into acetate and L-aspartate. The cleaved bond is an amide C–N bond. The complete cached and official abstracts for [PMID:12706335](https://pubmed.ncbi.nlm.nih.gov/12706335/) and [PMID:17027983](https://pubmed.ncbi.nlm.nih.gov/17027983/) report recombinant human enzyme activity; the first also measures selected N-acyl analogues, and the second identifies zinc-coordinating residues and catalytic Glu178. The E178D mutant retains reduced turnover; the abstract's abbreviated loss-of-activity wording should not be converted into absolute inactivity of every variant.

[PMID:18293939](https://pmc.ncbi.nlm.nih.gov/articles/PMC2666850/) examines a human enzyme–intermediate-analogue complex and supports amide hydrolysis. The cached abstract and indexed original structural Results were read; whole Methods and supplements were not. [PMID:8252036](https://pubmed.ncbi.nlm.nih.gov/8252036/) directly reports activity from cloned human cDNA expressed in bacteria. Its historical proposed Ser/His/Glu triad is not adopted as the modern catalytic mechanism.

[PMID:28101991](https://pmc.ncbi.nlm.nih.gov/articles/PMC5412892/) was read through its abstract and targeted cached XML Methods/Results. Human wild-type and variant ASPA-mGFP constructs were expressed in HEK293 cells; NAA-dependent aspartate production was measured by LC-MS/MS, with mock controls and triplicate measurements. Wild-type activity substantially exceeded mock activity. These experiments support the existing catalytic annotation without converting patient severity correlations into new molecular functions. [PMID:24036223](https://pubmed.ncbi.nlm.nih.gov/24036223/) is an abstract-only case report of two siblings with I177T and loss of activity; its detailed assay was not read. The catalytic function is independently established by the other human studies.

The [GO:0019807 definition](https://amigo.geneontology.org/amigo/term/GO:0019807) explicitly describes N-acyl-L-aspartate hydrolysis and places it below GO:0016811, linear-amide hydrolase activity. [GO:0016788](https://zfin.org/ZDB-TERM-091209-10636) instead specifies ester-bond hydrolysis. The existing InterPro IEA to GO:0016788 is therefore a candidate for removal on reaction chemistry, not on incomplete experimental evidence. The exact current InterPro entry could not be opened; its identifier is preserved as supplied in GOA, and no claim of curator correction upstream is made.

## Localization and association

The official [Human Protein Atlas subcellular page](https://www.proteinatlas.org/ENSG00000108381-ASPA/subcellular) reports supported cytosol localization, with HPA022145 and A-431, CACO-2 and U2OS assay rows. Text was inspected, not image pixels. [Reactome R-HSA-5691507](https://reactome.org/content/schema/instance/browser/R-HSA-5691507) places the human ASPA:Zn2+ dimer catalyst in cytosol and explicitly records NAA and water inputs and acetate/aspartate outputs.

The official abstract of [PMID:16935940](https://pubmed.ncbi.nlm.nih.gov/16935940/) distinguishes rodent native nuclear/cytoplasmic staining from an enzymatically active human GFP-ASPA fusion in COS-7 cells. These data support retaining nuclear localization with context; they do not establish a separate nuclear catalytic or chromatin function. Native rat active monomer and recombinant crystal dimers are distinct observations.

[PMID:17254025](https://pubmed.ncbi.nlm.nih.gov/17254025/) reports biochemical, proteomic and immunoblot evidence for ASPA in purified myelin and soluble fractions. The complete abstract and mouse MeSH provenance were read, not full Methods. This supports the original mouse-derived myelin localization as contextual. A separate rat localization study, [PMID:21598311](https://pubmed.ncbi.nlm.nih.gov/21598311/), shows that staining patterns depend on compartment and method; it does not establish absence of all myelin-associated enzyme. No direct human myelin assay is claimed.

[PMID:22284616](https://pmc.ncbi.nlm.nih.gov/articles/PMC3278530/) was read in indexed Results 2.5, Figure 9 caption and Methods 4.5. The paper explicitly uses a human kidney cDNA library and recombinant human ASPA in the MYO1D binding work, despite its broader mouse neurodevelopment focus. Yeast two-hybrid mapping and controlled pull-down support binding to the ASPA C-terminal domain. Suggested regulation of catalysis or trafficking remains a hypothesis; refine the existing interaction to myosin I binding, without adding a binding core or regulatory process.

[PMID:17194761](https://pmc.ncbi.nlm.nih.gov/articles/PMC1766406/) was read through its complete abstract and indexed oligomeric-state Results: both human and rat crystals contain analogous dimers; solution gel filtration described there is rat. This supports human self-association while not proving that obligate dimerization is required in every physiological compartment. The original Rual screen's ASPA self-pair has not been independently inspected.

The exact ASPA partner records in PMID:25416956, PMID:25910212, PMID:32296183 and PMID:32814053 remain unread. Searching the available canonical text yielded no explicit ASPA passage, which is an access limitation and not evidence of misattribution. Their ten original pair-specific protein-binding assertions remain candidates for UNDECIDED, not automatic removal.

## Pathway and inference boundaries

No human ASPA hit was found in the local GO-CAM index. The actual Aspa activity nodes in mouse models 63894f2500001094, 63894f2500001874 and 69729a3800001853 were inspected. They place aspartoacylase activity in cytosol and in aspartate metabolism, acetate metabolism and L-aspartate biosynthesis, respectively. ASPA itself catalyzes formation of these products, so the existing process annotations describe participation rather than substrate necessity. No new myelination, lipid-synthesis or histone-acetylation process is proposed.

The broad linear-amide IBA is consistent with the independently established human reaction. Its self donor is expected descendant evidence, not circularity; no donor-count argument is used. No PAINT tree reconstruction or new family assignment is claimed. The intended core is one cytosolic NAA/N-acyl-L-aspartate hydrolase activity with its direct metabolite-producing role.

## Final synthesis and consultation

Independent annotation/core consultation covered all 35 rows. The MYO1D interaction is refined to [GO:0017024 myosin I binding](https://amigo.geneontology.org/amigo/term/GO:0017024). A more specific heavy-chain term currently displays an unexpected myosin-Ia partner axiom; no resolution of that ontology inconsistency is assumed. The measured MYO1D TH1-tail interaction is stated explicitly in the reason.

The shipped UniProt record positively corroborates the unresolved partners: ACY3 has NbExp=15, KEAP1 has NbExp=4, and COPS3, DUSP29, PIAS1, UBQLN2, UBQLN3 and UBQLNL each have NbExp=3. These are database counts across records, not counts assigned to each cited paper. Their specific original pair-level records remain unread. Self-association has independent human crystallographic support; no obligatory physiological dimer is asserted.

The single cytosolic catalytic core includes acetate metabolism and L-aspartate biosynthesis. Aspartate metabolism remains ACCEPT as an original assertion but is omitted from the synthesized core because it is an ancestor of L-aspartate biosynthesis. No new process or second binding core is proposed.

Decisions: 14 ACCEPT, 5 KEEP_AS_NON_CORE, 5 MODIFY, 10 UNDECIDED and 1 REMOVE. All 35 original source assertions are preserved without new rows. No alternative products were supplied by the normal seed. The two additional localization references were recovered by the normal fetcher; actual cache availability is reflected in each reference flag, while the bounded reading scope remains explicit.


## 2026-09-28 review follow-up

Retain GO:0016811 IBA as ACCEPT: the PTN007644184 IBD table records chemically concordant inherited amide hydrolysis, with human ASPA among descendant evidence. The table does not establish an independently inspected full phylogeny; no target-specific loss is established. Three other refinements now explicitly acknowledge that their specific replacements already exist.

Add zinc ion binding (GO:0008270, IDA, PMID:17194761), supported by human crystal metal coordination and human ligand mutagenesis (PMID:17027983). Independent consultation inspected original PMC1766406 Zinc Coordination Results: zinc soaking, anomalous signal and zinc-edge comparison support human binding; no native intracellular metal-occupancy claim follows. The canonical paper cache remains abstract-only. This physical binding supports the existing single catalytic core, not a second physiological activity. The description now includes brain white matter and Canavan disease. The E178D note preserves the abstract's loss-of-activity language and its altered-kcat observation without inventing a residual value.

The ten source-specific interaction records remain UNDECIDED: the original assay evidence has not been read. UniProt partner corroboration does not establish the contents of each cited assay. Generic-term policy clarification remains pending; no inference that an interaction is false is made. Final counts: 15 ACCEPT, 5 KEEP_AS_NON_CORE, 4 MODIFY, 10 UNDECIDED, 1 REMOVE and 1 NEW (36 rows, 35 original source objects unchanged).
