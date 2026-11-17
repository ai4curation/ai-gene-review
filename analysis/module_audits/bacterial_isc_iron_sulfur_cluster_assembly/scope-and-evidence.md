# Bacterial Isc comparative audit

The audit reviews the Fdx-supported, HscBA-assisted bacterial Isc mechanism. Five
roles are required within this profile: sulfur mobilization, transient scaffold
assembly, reducing-equivalent delivery, scaffold recruitment and ATP-coupled
cluster transfer. IscA is an optional carrier branch with condition-dependent
importance and unresolved native directionality. Two HscA classifications are
alternative descriptions of one role, not two required chaperones.

Twenty references have explicit manual assessments and mined findings, including
five reviews. Access scopes distinguish cached full text, abstracts and externally
read primary methods. Four connections now carry evidence. Iron supply, reduction
of ferredoxin and target-client selection remain input or downstream boundaries.
The comparison does not assume autonomous flux from a list of family matches.

The panel contains eighteen completed gene reviews: six each from ECOLI, PSEPK
and AZOVI. All 208 original annotation payloads and their order remain intact,
apart from the explicitly documented retirement flag on the historical PSEPK
HscA folding proposal. All three historical NEW rows remain present, two active;
no annotation rows were added. Original source/provider inputs and independently
released consultation files are checked by `check_preservation.py`.

Seventeen proteins qualify as module representatives. AZOVI IscA O31271 remains
a reviewed comparator because broad cluster binding and native participation do
not establish the specific carrier activity. The original AF010139 sequence
deposit identifies all six AZOVI sequences; strain differences remain explicit.
Native AZOVI Fdx redox capability and ISC dependence support an inferred donor role,
whereas an exact cognate donor chain remains untested. Cluster transfer *to*
apo-Fdx is not evidence of electron donation *by* Fdx.

Bacteria is the distribution envelope. The three positive panels sample
Gammaproteobacteria and do not demonstrate universal conservation across bacterial
phyla. Mitochondrial ISC, SUF and NIF are outside the boundary. Reduced ISC
implementations also exist: PMID26560204 distinguishes anaerobic Fdx dispensability
in a SUF-deletion background from separate IscU suppressor mutations that partially
bypass HscBA. An incomplete canonical profile does not mean that all Fe-S assembly
is biologically impossible.

PTHR10093's universal cluster-delivery claim remains unresolved because of the
mechanistically distinct SufU members. The E. coli iron-binding evidence corrects
an earlier negative premise without manufacturing a phylogenetic node placement.
PTHR19375's universal folding claim likewise remains unresolved. Hsp110's negative
judgment is preserved in the family review, with its old exception object archived
because that field is not legal under an unresolved universal scope. Neither
specialized HscA uncertainty nor generic ATPase activity becomes a universal
family assertion.

The finite-panel capacity consultation uses production module logic with separate
identity, classification, molecular-function, taxon, specific-role and cognate-
interface checks. Its qualified-inference profile differs from its separate-assay
profile; neither claims simultaneous native pathway reconstitution. Descriptor
withdrawals and structural mutations test sensitivity, not native knockout
phenotypes. Exact results and source limits are recorded in
`capacity-consultation/` and the root verification artifacts.

Focused gene, family, module, history and render checks precede the full-corpus
validation gate. Publication, independent review, CI and actual merge remain
required; this audit is not complete merely because local checks pass.
