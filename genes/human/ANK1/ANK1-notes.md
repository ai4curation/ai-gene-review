# ANK1 research and annotation review

## 2026-09-27 — genuine seed and source provenance

The seed7 ordinary hosted fetch supplied the human ANK1 record (HGNC:492, UniProt:P16157), 61 GOA rows and 60 distinct seeded annotation objects. All 60 source objects are preserved, including their evidence types, source identifiers and partner sets. The 23 alternative-product records are unchanged. Their names do not authorize assigning new tested-isoform fields to existing rows. Root imported the exact seed and selected normal auxiliary records; seven pre-existing Reactome records were retained without overwriting. All 14 cited PMID and nine Reactome records are now present. Actual import provenance is retained in `tmp/seed7-canonical-import-receipt.json` and `tmp/seed7-selected-auxiliary-import-receipt.json`.

An ordinary `just deep-research-falcon human ANK1 --fallback perplexity-lite` invocation used the installed client and workspace UV directories. Falcon reached authentication but failed; the fallback failed DNS. The finite attempt ended after 5.85 seconds and produced no provider report. The receipt and sanitized logs are under `tmp/ANK1-initial/`. These are manual research notes, not an authored provider report.

## Biological synthesis

Ankyrin-1 physically links membrane proteins to beta-spectrin in the erythrocyte membrane skeleton. The original human biochemistry distinguishes spectrin binding to ankyrin-linked band 3 from free band 3; this establishes an adaptor mechanism rather than a generic binding claim [PMID:379653, “Spectrin binds to solubilised ankyrin-linked band 3, but not to free band 3.”]. Human hereditary-spherocytosis variants support the physiological importance of this linkage, but disease association alone is not treated as a new functional assay [PMID:8640229]. The native erythrocyte complex study independently defines partner interfaces and membrane-protein clustering [PMID:35835865].

The gene produces large erythroid and neuronal products as well as short muscle proteins with distinct N-termini. The alternative muscle promoter paper uses human sequence and human muscle immunoblotting; its predicted 155-residue product is not the full-length spectrin-binding erythroid protein [PMID:9430667]. Small ank1.5/ank1.9 products associate with obscurin and the M-band region, consistent with a sarcoplasmic-reticulum attachment mechanism. Their historical names are retained as reported, without silently mapping ank1.9 to a current human UniProt product [PMID:16962094].

## Primary source scopes

- **PMID:379653:** complete normal abstract read. Human erythrocyte extracts establish the ankyrin–band-3–spectrin linkage. This supports structural, membrane, spectrin-binding and adaptor annotations.
- **PMID:8159688:** complete normal abstract read. Recombinant human erythrocyte spectrin and Na,K-ATPase domains are tested against erythrocyte Ank1 and kidney Ank3 separately. Both ankyrins bind spectrin and ATPase domains. Inclusion of Ank3 does not make the Ank1 experiments a paralog error.
- **PMID:12719424:** complete normal abstract read. Ankyrin-R interacts with Rh/RhAG tails in yeast-two-hybrid and erythroid membrane-skeleton assays, with separate mutant-mouse observations. The later native-complex RhCE interface does not negate the earlier isolated RhAG-tail result.
- **PMID:16580865:** complete review abstract read. The text distinguishes erythroid Rh/RhAG–ankyrin-R anchoring from epithelial RhBG–ankyrin-G. Only the former informs ANK1.
- **PMID:16962094:** complete normal abstract read. Small ank1.5 and ank1.9 bind the obscurin C-terminus; recombinant interactions are tested in NIH3T3 cells and colocalization in cultured myotubes. Efficient obscurin binding contrasts with weak titin binding. The proposed connection of reticulum and contractile apparatus is distinguished from a fully resolved native complex structure.
- **PMID:9430667:** complete normal abstract read. Human alternative-promoter and transcript work establishes short muscle products, with human muscle immunoblots and heterologous promoter assays. Its introductory erythroid function is not reassigned to every short product.
- **PMID:8640229:** complete normal abstract read. Human ANK1 variants and explicit spectrin–band-3 linkage support a structural role; no enzymatic function is inferred from hereditary spherocytosis.
- **PMID:1833445:** complete normal abstract read. Antibodies raised against erythrocyte ankyrin localize antigen in bovine chromaffin cells. The authors infer a possible relationship to exocytosis and/or membrane retrieval from coated-region localization. The broad cytoskeletal function is independently established for ANK1, but the specific exocytosis assertion remains unresolved.
- **PMID:11427698:** complete normal family-review abstract read. It directly describes the erythrocyte linker mechanism but combines many tissue and family-member pathways. Epithelial polarity is not assigned to ANK1 solely because it is discussed for ankyrins collectively.

### CD45 and renal epithelial studies require different gene assignments

For **PMID:12354383**, the normal abstract and indexed publisher Results/Methods were read. The binding assay uses human erythrocyte AnkR; human lymphocyte complexes contain an AnkR-reactive protein. This supports the CD45 interaction while distinguishing purified binding from cellular association. Direct publisher opening failed, so a complete full-text or supplement reading is not claimed. [Original publisher article](https://www.sciencedirect.com/science/article/pii/S1074761302003965)

For **PMID:12409278**, the normal abstract plus indexed publisher Introduction/Results/Discussion specify an AnkG190-selective antibody in rat kidney and canine MDCK experiments. Those inspected experiments do not establish ANK1 basolateral localization. The ANK1 row remains unresolved because this assessment does not exclude other evidence or an ANK1 pool in that compartment. [Original publisher article](https://journals.physiology.org/doi/full/10.1152/ajprenal.00100.2002)

### Selective cargo trafficking: PMID:18768923

The normal extracted body was read for relevant Methods, Results and Discussion. Ankyrin-R and ankyrin-G shRNAs are distinguished. Human HEK293F, canine MDCK and monkey COS7 hosts are used in different assays; rat Na,K-ATPase constructs and human erythrocyte ankyrin-R add-back are separate reagents. The paper's Methods and Results describe the semipermeabilized-cell system differently, so no single host identity is invented to reconcile them.

Cargo carrying the ATPase ankyrin-binding segment acquires ankyrin-dependent ER-to-Golgi transport. Ankyrin-R depletion impairs selected cargo, and purified human erythrocyte ankyrin restores transport. This supplies a physical cargo-adaptor role rather than only a necessity phenotype. The engineered VSV-MAB chimera reaches Golgi but does not behave like native cargo in stable surface accumulation; its trafficking is not generalized to all plasma-membrane proteins. No supplemental-movie reading is claimed [PMID:18768923].

### Hydroxylation: PMID:21177872

The complete abstract and targeted normal full-body Methods/Results were read. Native human and mouse erythrocyte ankyrin-R is hydroxylated, and recombinant human D34 repeats are tested in separate expression and biochemical systems. FIH/HIF1AN performs the chemistry; ankyrin-R is the substrate. The fragment's stability and band-3 interaction change after hydroxylation, but these observations do not make ANK1 an oxygenase or a demonstrated FIH inhibitor. The real enzyme interaction is retained outside the compact structural core [PMID:21177872].

### Native complex: PMID:35835865

The normal full-body native-complex purification methods, partner-interface Results and relevant Discussion were read. The material is isolated from human erythrocytes. Ankyrin-1 directly organizes membrane partners, including RhCE, band 3, protein 4.2 and a subset containing AQP1. Observed interfaces are distinguished from an inferred autoinhibitory transition. A possible gas-transport metabolon is a proposal about coordinated partner function, not a catalytic activity of ANK1. The source does not justify rewriting the older RhAG-tail interaction as an error [PMID:35835865].

## Phylogenetic and electronic evidence

The actual local `interpro/panther/PTHR24123/PTHR24123-paint.tsv` records the six relevant IBDs at **PTN002380879**: plasma membrane, neuron projection, cytoskeletal adaptor activity, spectrin binding, transmembrane transporter binding and protein localization to plasma membrane. The slice is source evidence for those node assertions; the full tree and MSA were not reconstructed. ANK1's inclusion among experimental descendants is legitimate grounding, and a short donor list is not weak evidence. Target biochemistry independently corroborates the main molecular functions. Broad neuronal localization is retained outside the compact erythroid/muscle core.

The narrower electronic localizations cite rat UniProt A0A8I5ZJ94 and Ensembl ENSRNOP00000076708. One bounded attempt to retrieve the donor failed DNS. Sarcoplasmic-reticulum and M-band assertions have independent small-muscle evidence; Z-disc, A-band, sarcolemmal, axolemmal and postsynaptic-membrane assertions remain unresolved because their original donor experiments were not recovered. These uncertainties do not assert that the source is a wrong paralog or that human ANK1 lacks neuronal activity.

InterPro IPR000488 in the actual UniProt record is the death domain. It is not treated as proof of apoptosis or enzyme catalysis. A broad contextual signaling role is retained from the CD45-associated scaffold, separate from the compact membrane-skeleton core. The nine complete Reactome cached event summaries inform cytosolic location; their reaction names do not assign enzyme activities to ANK1.

The official GO:0008093 definition and parents were checked. Bringing membrane-associated components together with cytoskeletal proteins is consistent with cytoskeletal adaptor activity. [Official GO term](https://amigo.geneontology.org/amigo/term/GO:0008093)

No ANK1/P16157 match was found in the cached `gocams/index.tsv`. No NEW process is proposed. The single core combines cytoskeletal adaptor activity, cytoskeleton organization and plasma-membrane protein localization, without repeating ancestor/descendant process terms. Binding-partner species, host-cell species and tested splice products remain distinct.

## Draft checkpoint

All 60 source objects and 23 alternative products are preserved. The draft has 42 ACCEPT, six MODIFY, four KEEP_AS_NON_CORE and eight UNDECIDED decisions, with zero NEW annotations. The six refinements subsume generic structural/binding assertions into already-seeded informative terms. Independent all-row consultation, final checks and a new history record remain pending at this checkpoint.

## Completed review and verification

Independent annotation-reviewer consultation considered all 60 authored rows, core synthesis and preserved source objects. It supported the decisions and requested stronger direct evidence attachments for obscurin binding and the sarcoplasmic-reticulum location; both were added as exact cached excerpts. The final review is COMPLETE with 42 ACCEPT, six MODIFY, four KEEP_AS_NON_CORE and eight UNDECIDED, no NEW rows, one core and all 23 alternative products preserved. The eight scientific uncertainties do not represent missing normal caches.

Final gene validation passed, including term branches, source coverage and citation checks, and HTML rendering succeeded. The 68 supporting-text attachments are exact cached substrings; all 25 raw seed/source files are unchanged. One nonblocking same-term action warning remains: the enzyme-binding IPI concerns ANK1 as an FIH/HIF1AN substrate and is non-core, while the generic enzyme-binding TAS is refined using independent ATPase-binding evidence. Different partners and roles justify the different actions; this is not a preference for an evidence code. The official GO page currently uses the adaptor label, while the local validation ontology uses its anchor label for GO:0008093; authored fields follow the validator label and every original source term label is preserved.

Independent consultation receipt: `tmp/ANK1-initial/independent-annotation-consultation.json` (SHA256 `49fd8e648faad86394068888ba20d38238a76932e7c909a8f20cb647c68213ee`). A new scaffolded history record accompanies the review. No Git, remote or shared source-cache writes were performed by the annotation author.
