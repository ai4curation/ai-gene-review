# LPAR5 literature notes

## Research provenance

- The user made provider deep research optional, so no provider run or provider-named file was created. Primary literature was identified through PubMed/Europe PMC searches and citation chaining, then fetched with the project's `fetch-pmid` tooling. Every quotation below was checked against its local publication cache.

## Direct receptor identity, ligand recognition, and coupling

- One independent 2006 deorphanization study measured direct high-affinity binding: “The binding of LPA to GPR92 was of high affinity (K(D) = 6.4 +/- 0.9 nM) and led to an increase in both phosphoinositide hydrolysis and cAMP production.” [PMID:16651401, abstract]
- A second study found that “LPA induced concentration-dependent activation of G(12/13) and G(q) and increased cAMP levels.” It also detected “Specific [3H]LPA binding” only in membranes heterologously expressing GPR92. [PMID:16774927, abstract] These establish human-receptor capability in heterologous systems, not fixed branch weights in every native cell.
- LPAR5 agonism is chemically broader than LPA alone. FPP and LPA activated both Gq/11 and Gs pathways, whereas N-arachidonylglycine activated only Gq/11. [PMID:18499677, abstract, “FPP and lysophosphatidic acid were able to activate both G(q/11)- and G(s)-mediated signaling pathways, whereas NAG activated only the G(q/11)-mediated signaling pathway.”]
- The comparative structure-activity series ranked agonists as “alkyl glycerol phosphate > LPA > farnesyl phosphates >> N-arachidonoylglycine.” [PMID:19366702, abstract] Thus FPP and NAG are assay-supported agonists, but the evidence does not establish them as universally dominant endogenous ligands.
- Mutagenesis implicated ligand-contact residues in two studies. The 2008 work identified Thr97, Gly98, Phe101, and Arg267 for FPP/NAG responses; the 2009 work found that R2.60N abolished activation and H4.64E, R6.62A, and R7.32A strongly reduced it. [PMID:18499677; PMID:19366702]

## Structural evidence and trafficking

- The 2026 cryo-EM study directly captured “LPAR5 bound to 1-oleoyl-lysophosphatidic acid (LPA) in complex with Gq at 2.96 Å resolution”. [PMID:42313925, abstract]
- Its ligand pocket separates phosphate-headgroup recognition from acyl-tail burial: “The phosphate headgroup of LPA forms extensive polar interactions with residues from extracellular loop 2 and transmembrane helices TM5-TM7, while the lipid tail inserts into a deep hydrophobic cavity formed by TM3-TM5.” [PMID:42313925, abstract]
- The Gq interface is noncanonical: the Gα α5 “wavy hook” is positioned toward the intracellular-loop-1/helix-8 interface rather than primarily engaging TM6. [PMID:42313925, abstract]
- Agonist-dependent trafficking capability was shown in a tagged-receptor system: “LPA-dependent receptor internalization following exposure to LPA but not related lysophospholipids was observed.” [PMID:16774927, abstract] The endogenous internalization route, arrestin dependence, recycling, and degradation remain unresolved by the audited set.

## Tissue and species boundaries

- The first human survey reported expression mainly in heart, placenta, spleen, brain, lung, and gut, with especially high expression in small-intestinal intraepithelial CD8+ cytotoxic T cells. [PMID:16651401, abstract, “It is the most abundant GPCR activated by LPA found in the small intestinal intraepithelial CD8+ cytotoxic T cells.”]
- Another survey found broad low expression with enrichment in small intestine, sensory dorsal-root ganglia, embryonic brain, and embryonic stem cells. [PMID:16774927, abstract]
- The alternative-ligand study reported GPR92/TRPV1 colocalization “in mouse and human DRG.” [PMID:18499677, abstract] This is expression/localization evidence, not proof that every TRPV1-positive human sensory neuron uses the same ligand or downstream branch.
- The reviewed UniProt record defines no `ALTERNATIVE PRODUCTS` section or curated functional variants. RefSeq lists two protein accessions, but the audited literature does not establish distinct isoform-specific receptor functions; transcript multiplicity must not be converted into isoform biology without direct evidence.

## Pain and development boundaries

- The strongest causal pain evidence is murine. “Homozygous null mutants did not show obvious base-line phenotypic defects. However, following PSNL, LPA(5)-deficient mice were protected from developing neuropathic pain.” [PMID:22461625, abstract]
- The knockout also reduced dorsal-horn phosphorylated CREB while other pain markers remained induced, distinguishing the Lpar5 pathway from the previously studied Lpar1 response. [PMID:22461625, abstract]
- These results support injury-induced neuropathic-pain development in mice. They do not by themselves establish a constitutive human pain function, and the lack of gross baseline phenotype argues against broad developmental claims from this model.

## Human platelet-lineage and disease contexts

- Human platelet transcripts and pharmacology suggested an LPAR5 contribution, but antagonist inhibition alone was not fully receptor selective. [PMID:19366702, abstract, “Because LPA(5) transcripts are abundant in human platelets, we tested its antagonists on platelet activation and found that these non-lipid LPA(5) antagonists inhibit platelet activation.”]
- Stronger receptor-selective evidence came from human megakaryocytic cells: “Knock-down of individual LPA receptors by siRNA showed that LPA-mediated activation of MK cells was mediated by LPA₅, but not by LPA₁₋₄,₆,₇.” [PMID:21106562, abstract]
- Human plaque material also induced megakaryocytic-cell shape change that was inhibited after LPAR5 silencing. [PMID:21106562, abstract] This supports a platelet-lineage and atherosclerotic-plaque context, while direct genetic manipulation of mature anucleate platelets was not possible in that design.
- In EBV-associated nasopharyngeal carcinoma, “we show that one of the LPA receptors, LPA receptor 5 (LPAR5), is down-regulated in primary NPC tissues and that this down-regulation promotes the LPA-induced migration of NPC cell lines.” [PMID:25294670, abstract] This disease result suggests a migration-suppressive role in that context, not a universal normal-tissue function.

## Interaction and evidence gaps

- No decisive receptor-specific protein partner or stable endogenous LPAR5 complex was identified in the audited primary set. Generic Reactome Gq/Gi cycle entries model pathway steps, not physical interaction experiments.
- Direct Gq coupling is supported by both functional assays and the LPA-bound LPAR5-Gq structure. By contrast, the seeded Reactome Gi entries are generic, and the audited primary studies emphasize increased cAMP rather than canonical Gi-mediated cAMP suppression; LPAR5-Gi coupling should remain unverified unless receptor-specific evidence is supplied.
- Important open questions include endogenous human coupling weights, physiological competition among LPA/FPP/NAG ligands, receptor-specific trafficking regulators, isoform/proteoform validity, and whether mouse pain and human platelet/cancer contexts generalize to other tissues.
