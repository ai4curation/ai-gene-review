# COX15 research notes

## 12 October 2026 — heme A synthesis and product scope

COX15 converts heme O to heme A in the mitochondrial inner membrane. The current heme A synthase definition specifies oxidation of the C8 methyl group to a formyl group and lies under oxidoreductases acting on CH or CH2 groups. The older CH-CH subclass therefore needs correction to GO:0120547. Heme A synthesis is the integrated catalytic core; supplying a prosthetic group to complex IV does not by itself demonstrate a separate insertase or scaffold activity.

The original human study tested sequence-verified **COX15.1** in patient fibroblasts. Oxidase activity increased from 28% to 61% of control. The heme A/B ratio increased from 0.030 to 0.090, compared with 0.064 in untransduced controls and 0.139 in controls overexpressing COX15. Thus the rescue is substantial but not uniform normalization. Heme O accumulated in patient heart but was undetectable in patient fibroblasts. The native-gel antibodies detected respiratory subunits, not COX15 itself. See [PMID:12474143](https://pmc.ncbi.nlm.nih.gov/articles/PMC378614/), Methods “Cell Culture and Retroviral Expression” and “Electrophoretic Methods,” Results Tables 2–3 and Figure 3, and the final isoform discussion.

The official products contain 410 and 388 residues. VSP_011281 replaces canonical positions 368–410 with a different 21-residue tail, changing the C-terminal membrane architecture and a by-similarity heme-binding position. Sequence change alone establishes neither loss of activity nor equal activity. The human rescue tested only COX15.1; the suggestion that both products may be needed for optimal function remains a hypothesis.

## Oligomers, heme binding and assembly

[PMID:26940873](https://pmc.ncbi.nlm.nih.gov/articles/PMC4858986/) directly tests tagged yeast Cox15, conserved histidines and linker variants. Its native mammalian oligomer analysis uses **porcine kidney**; the human patient-cell assays measure steady-state COX15 abundance. The original Results on heme depletion show that oligomerization can persist without available heme, and histidine mutations do not by themselves distinguish catalytic from ligating roles. No direct purified human heme-binding measurement follows from those experiments.

GO:0070069 means a protein complex containing a redox-active heme protein and is broader than mature respiratory complex IV. The 2003 human study does not establish COX15 membership, while the independently observed oligomers make a broader cytochrome-containing assembly plausible. The exact human IDA assertion remains unresolved. GO:0098803 specifically concerns a respiratory-chain complex; its PMID:9878253 basis remains unresolved because the complete original was not recovered. The [complete abstract](https://pubmed.ncbi.nlm.nih.gov/9878253/) positively supports mitochondrial import and protease protection. This is an access limit, not evidence that COX15 can never associate with a respiratory assembly.

## Positive PRDX6 association

[PMID:29128334](https://doi.org/10.1016/j.cels.2017.10.010) reports a mitochondrial interaction map using tagged human proteins and antibody-based immunoprecipitation. The [original author-lab PDF](https://www.yulab.org/static/pdf/29128334.pdf), pages 565–567 and STAR Methods e1/e3/e7–e9, describes the constructs, cross-linking, purification and assay context. The exact COX15–PRDX6 records include two spoke-expanded cross-link associations and one anti-bait co-IP record in HEK293 cells. Both official sequences match the interaction-record ROGIDs; the COX15 sequence is the displayed 410-residue product.

Human PRDX6 is an independently established phospholipase A2 as well as a peroxidase. Its class is documented in the reviewed [P30041 record](https://www.uniprot.org/uniprotkb/P30041/entry), and the complete [PMID:10893423 abstract](https://pubmed.ncbi.nlm.nih.gov/10893423/) describes separate catalytic activities and mutational controls. GO:0043274 specifies binding to a phospholipase. This refines the positive association by counterpart class without asserting regulation, a particular contacted active site, native binary affinity or activity of the shorter COX15 product. The original target-specific supplementary image and table were not independently inspected; their assay attribution rests on the literal curated records.

## Location and propagated evidence

The current Human Protein Atlas ICC/IF summary identifies mitochondria as the main location with supported reliability, and nucleoplasm as additional. The returned summary, rather than image pixels, was assessed. The MitoCoP study [PMID:34800366](https://pmc.ncbi.nlm.nih.gov/articles/PMC8664129/) combines subtractive/spatial proteomics, importomics and literature curation. Its selected original Methods and Results were read, but the exact COX15 supplementary Table S1 row and numerical pool assignment were not recovered. The broad mitochondrial annotation agrees with independent human targeting evidence.

Current PTHR23289 topology places the exact human sequence below PTN000590786, with experimental support on both yeast lineages. The human target in location/process WITH/FROM is legitimate descendant evidence. The current v19 GO-slim chemistry fields differ from the current GOA assertion; they do not replay the historical IBD decision. The current ISS synthase donor is bacterial **Bacillus subtilis CtaA/P12946**. The inherited yeast-donor wording remains unverified because its historical WITH/FROM was omitted; the current donor does not reconstruct every historical source version.

IPR003780 and IPR023754 explicitly support membrane/heme A pathway mappings. The current ARBA membrane rule contains many FunFam-dependent branches for which target assignments were not obtained, so no particular current ARBA branch is claimed as confirmed. Independent InterPro and target evidence remain sufficient for the biological membrane judgment. The broad membrane record is refined to the inner membrane.

The historical InterPro-only membrane source is retained as retired, alongside the distinct active combined-source record. Nine historical objects omitted WITH/FROM values; their original fields remain, while the complete current objects and explicit identity mapping are available in [the evidence index](COX15-source-evidence-index.json). Retirement and these omissions describe source history, not a loss of biological function.

## Reactome scope and remaining questions

The current heme pathway reaches the COX15 heme A reaction through an explicit catalyst/entity/reference chain. Three assembly events reach the same inner-membrane COX15 entity through the modeled metallochaperone complex. Those paths support location and pathway context; they do not establish autonomous COX15 copper insertion. Other-participant differences between event prose and component lists are retained as limits rather than copied into new mechanistic claims.

Priorities for experiments are product-specific heme synthesis and import, endogenous human oligomer/assembly composition, the physiological meaning of the PRDX6 association, and the transfer of synthesized heme A to nascent oxidase. Each can be tested without assuming that synthesis, binding and insertion are the same activity.
