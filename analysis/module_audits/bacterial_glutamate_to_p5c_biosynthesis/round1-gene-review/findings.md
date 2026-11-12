# PR6160: gene evidence follow-up

Reviewed published head `bbb9f7c1bf6d26ba46d2e28555a52c6cfd01f90c`, review 5809414491 and issue comment 6700784559. Eleven reviews contain 123 ordered historical annotations. Eight reviews receive evidence/prose corrections; ECOLI proA/proB and PSEPK proA require no change for these findings. No annotation action, non-review payload, ordering or historical NEW assertion changes. The bounded SCHPO comparator retains its pre-existing DRAFT status; the other ten reviews remain COMPLETE. No new annotation or publication is added.

## CORGL ProA and ProB evidence

The criticism of the ProA quotation is valid. PMID:8755867 says: “Null proA alleles still grow slowly under proline starvation, which suggests that a proA-independent bypass of this metabolic step exists in C. glutamicum.” The truncated first clause cannot positively support ProA catalysis. All three affirmative uses now quote the abstract's canonical-pathway sentence instead: “Together with a proA gene described earlier, these new genes describe the major C. glutamicum proline biosynthetic pathway.” The complete bypass finding remains separately recorded. The actual target reaction support is the frozen HAMAP MF_00412 curated reaction, not a claim that this abstract directly measures catalysis.

For ProB the abstract explicitly reports isolation of ATCC 17965 proB/proC loci by complementation of E. coli auxotrophs. That is stronger functional evidence than the nonspecific morphology phenotype and now accompanies the target HAMAP reaction in the molecular-function, process and core support. The original auxotrophy finding is retained. In both genes the reference sequence is ATCC 13032; the primary study is ATCC 17965. The abstract is accessible, but full text was not recovered in this review; no purified target kinetics are asserted.

## RNA binding: justified disagreement with the requested action

The comment names **six** untested targets: PSEPK ProB, BACSU ProB and ProJ, CORGL ProB, yeast Pro1 and SCHPO SPAC17H9.13c. All six RNA rows are InterPro IEA mappings from IPR002478/IPR036974. They are not PAINT RNA-binding assertions. The frozen PTHR43654 PAINT table contains no GO:0003723 assertion. PAINT losses were checked: none on the available BACSU/yeast/SCHPO lineages; Q88Q07 and P0C1E2 are absent from this tree, so their losses cannot be checked. Absence from a tree is not evidence of biological loss.

Full PMID:37511294, Results and Methods, establishes the following:

- K-12 ASKA-derived proB was recloned into pET21a with a C-terminal His tag and expressed in BL21-Gold (DE3).
- Genomic SELEX selected RNA fragments; EMSA showed a stronger tktA-fragment complex than the random-RNA control. The paper states: “The specificity of the interaction was further confirmed by competition experiments involving a 50-fold excess of unlabeled control RNAs (Figure 7B).”
- The estimated affinity is KD >>10 µM. The authors did not identify the binding site and explicitly leave assay optimization and native RNA targets open. Their conclusion that PUA may mediate binding is plausible, not site mapping.
- ProB was **not** among the iCLIP-tested proteins (Mdh, PykF, RpiA, KdsA, Upp, Pgk and AnsB). These data do not demonstrate a native ProB RNA-regulatory process.

Thus the directly tested E. coli molecular binding claim remains KEEP_AS_NON_CORE. Low affinity and unknown physiological function do not invalidate a molecular interaction. For the other six proteins, a PUA signature alone does not establish target binding, but neither the positive homolog result nor a metabolic role supplies a counter-assay or a demonstrated loss. Conservation is genuinely unresolved. UNDECIDED is retained, with the uncertainty and construct/transfer limits made explicit; no text concludes that these target claims are false or demonstrably over-annotated.

The action policy does not restrict UNDECIDED to inaccessible publications: the skill defines it as an “Unclear annotation requiring more evidence (always use if unable to access relevant publications).” The accessibility clause is mandatory when applicable, not exhaustive. Changing all six to MARK_AS_OVER_ANNOTATED merely because the comparative paper is accessible would overstate the present biological judgment.

## Localization and row-specific rationale

BACSU ProB/ProJ and CORGL ProB retain cytoplasm→cytosol MODIFY. The independent grounds are curated HAMAP cytoplasmic localization, soluble kinase/PUA architecture, absence of annotated signal/TM/transit features, and E. coli native-locus monomeric-GFP localization in PMID:39514317. The latter is explicitly comparative, not a target localization experiment. The actual quote is: “When we express ProB and ProA tagged with monomeric superfolder GFP (msfGFP) from a gene integrated into the native locus, both proteins are dispersed throughout the cytoplasm”. The accepted finer compartment is a conserved-role inference; the existing GOA row is not evidence. BACSU IBA provenance is PTN000115542; CORGL's TreeGrafter assertion does not provide a directly inspected target PAINT lineage.

BACSU and CORGL ProA retain the explicitly curated cytoplasm granularity. Absence of a cytosol annotation is not offered as biological evidence. Their source does not independently resolve cytosolic fluid from transient intracellular associations, so this bounded follow-up makes no new narrower assertion.

Boilerplate molecular-function and process reasons were made reaction/branch-specific. ARBA caveats were removed from IBA process rows. ProJ's existing osmoadaptive core and full-primary JH642-derived pathway evidence are retained, with a question about strain-168 flux/feedback regulation added; no new process row is manufactured.

## Limits and ownership

No module, family or project file was edited. The family reflow/quote advisory is root-owned. All source caches, provider reports and raw files remain unchanged. This follow-up does not claim stable ProA–ProB assembly, universal substrate channeling or universally conserved RNA binding. Focused validation results and reproducible preservation checks accompany this file.
