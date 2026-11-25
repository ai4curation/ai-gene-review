# PTPRN2 notes


## 2026-09-08 paired human–horse review



PTPRN2 is a membrane protein of neuroendocrine secretory vesicles that traffics between secretory granules and the plasma membrane. It regulates vesicle accumulation and secretion and has a phosphatase-like intracellular domain. Conventional phosphoprotein activity is impaired, whereas phosphoinositide phosphatase activity and regulation of membrane PI(4,5)P2 have been reported in mammalian cells.

## Substrate-specific catalysis and process participation

The 1996 cloning report states that recombinant IAR/PTPRN2 has phosphatase activity, but its abstract does not name the substrate. Later human cell work explicitly distinguishes lack of phosphoprotein-substrate activity from phosphoinositide phosphatase activity and tests the effect of a catalytic-domain mutant on migration and metastasis. Vesicle accumulation, insulin/neurotransmitter release, and membrane phosphoinositide regulation are not interchangeable with protein tyrosine dephosphorylation. Conversely, a biological-process annotation can describe regulation through another enzyme: losing intrinsic protein phosphatase activity alone does not refute all participation in protein dephosphorylation. The exact experimental annotation therefore remains unresolved while the inappropriate electronic intrinsic protein-phosphatase terms can be challenged.

## Decisive inspected evidence

From [PMID:26620550](https://pubmed.ncbi.nlm.nih.gov/26620550/):

> As a transmembrane protein, PTPRN2 shuttles between secretory vesicles and the plasma membrane.

## Evidence inventory

- [PMID:8798755: Cloning and characterization of islet cell antigen-related protein-tyrosine phosphatase (PTP), a novel receptor-like PTP and autoantigen in insulin-dependent diabetes.](https://pubmed.ncbi.nlm.nih.gov/8798755/). The repository cache contains the abstract; source-specific claims beyond it remain unresolved.
- [PMID:26620550: PTPRN2 and PLCβ1 promote metastatic breast cancer cell migration through PI(4,5)P2-dependent actin remodeling.](https://pubmed.ncbi.nlm.nih.gov/26620550/). [DOI:10.15252/embj.201591973](https://doi.org/10.15252/embj.201591973). Full text is available in the repository cache.

## Transfer to the selected horse protein

The exact target is [A0A9L0T4W6](https://www.uniprot.org/uniprotkb/A0A9L0T4W6/entry), not an arbitrary horse record with a matching name. The reproducible [paired-sequence analysis](../../HORSE/PTPRN2/PTPRN2-bioinformatics/RESULTS.md) records identity, coverage and internal gaps. It supports homology but is not a reciprocal orthology test. Molecular properties are transferred only with the relevant domain, targeting and paralog constraints. The prediction-time sequence is not independently verified.

## Open evidence questions

The following annotation scopes need source-specific follow-up: ficolin-1-rich granule membrane, protein dephosphorylation, signaling receptor complex, transmembrane receptor protein tyrosine phosphatase activity. Experimental annotations are not removed merely because a cached abstract omits the gene or a specific assay. High-throughput protein-binding rows require their actual partner or complex context before replacement with an informative molecular function.


Research provenance: external Falcon/Edison was attempted with Perplexity fallback. Some requests returned HTTP 429 and fallback returned insufficient-quota HTTP 401; successful external reports are preserved separately. Primary-source manual synthesis is explicitly labeled manual where no external report was available.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

**Identity.** Q92932 is the reviewed, canonical human PTPRN2 entry (PTPR2_HUMAN, 1015 aa, isoform 1 displayed; four splice isoforms). It is not a fragment or alternative gene model: it has the signal peptide (1-21), luminal pro-region and RESP18 domain, transmembrane helix (616-636), cytoplasmic PTP-like domain (745-1005) and the annotated catalytic Cys945. PANTHER PTHR46106:SF5 (RECEPTOR-TYPE TYROSINE-PROTEIN PHOSPHATASE N2), the same subfamily as mouse Ptprn2 (P80560) and rat Ptprn2/phogrin (Q63475); paralog PTPRN is SF1, invertebrate IDA-1/IA-2 SF4. The family review interpro/panther/PTHR46106/PTHR46106-review.yaml places Q92932 in SF5; no disagreement.

**Evidence read.** Caromile et al. 2010 [PMID:20097759 "phogrin is able to dephosphorylate specific inositol phospholipids, including phosphatidylinositol (PI) 3-phosphate and PI 4,5-diphosphate but not PI 3,4,5-trisphosphate"; "The PIPase activity of phogrin depended on the catalytic site cysteine and correlated with effects on glucose-stimulated insulin secretion"] (rat, SF5 ortholog). Kubosaki et al. 2004 [PMID:15220191 "showed mild glucose intolerance and impaired glucose-stimulated insulin secretion"]. Cai et al. 2011 [PMID:21732083 "Islets from single and DKO mice all showed a significant decrease in insulin content, insulin secretion and the number and half-life of DCV"]. Nishimura et al. 2009 [PMID:19361477 "IA-2beta, but not IA-2, co-purifies with fractions rich in synaptic vesicles (SV)"]; neurotransmitter release defects are from the Ptprn/Ptprn2 double KO. Doi et al. 2006 [PMID:16418280] IA-2beta overexpression inhibits GSIS in MIN6 cells. Human: Sengelaub et al. 2016 [PMID:26620550 "PTPRN2 belongs to the protein tyrosine phosphatase family, but does not exhibit activity against phosphoprotein substrates"].

**Decisions (changed from previous version).**
- GO:0004725 (IEA) REMOVE kept; GO:0005001 (TAS, PMID:8798755) and GO:0006470 (TAS) changed UNDECIDED -> REMOVE. These are TAS/IEA author/domain inferences, contradicted by direct assays (no phosphoprotein/pNPP activity; the cloning-paper activity was weak, at pH 4.5, of questioned relevance per UniProt). No receptor/ligand activity exists.
- Plasma membrane (2 TAS rows): ACCEPT -> KEEP_AS_NON_CORE (transient post-exocytosis residence).
- Secretory granule (IBA, IEA) and secretory granule membrane (IEA, ISS): MODIFY -> GO:0032127 dense core granule membrane.
- Synapse (IBA): MODIFY -> GO:0030672 synaptic vesicle membrane (already carried, ACCEPT).
- Neurotransmitter secretion (IEA, ISS from mouse SF5 ortholog): ACCEPT -> KEEP_AS_NON_CORE; decisive data are double-KO, and PAINT did not place this term on the family nodes.
- Insulin secretion in response to glucose (IBA PTN000439772 vertebrate node, IEA, ISS) and regulation of secretion (IBA PTN000439769 family node): ACCEPT.
- Ficolin-1-rich granule membrane (Reactome TAS): UNDECIDED -> MARK_AS_OVER_ANNOTATED (neutrophil granule proteomics; neuroendocrine protein).
- Signaling receptor complex (IDA PMID:23382219): UNDECIDED retained; the cached SNX17/27 PX-FERM paper does not mention PTPRN2, and an NPxY cargo-peptide binding assay would not establish complex membership.
- NEW GO:0052866 phosphatidylinositol phosphate phosphatase activity now ISS from rat phogrin (PMID:20097759, same SF5 subfamily) rather than IMP from the human cancer-cell paper, which shows PI(4,5)P2 effects but cites Caromile for the catalytic dependence.

**Relative.** Mouse Ptprn2 (P80560), SF5 ortholog with knockout data; no review exists in the repo.
**Modules.** No module in modules/ mentions PTPRN2 or PTHR46106; no GO-CAM index entry.
