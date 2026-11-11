# DYSF source-audit results

The executed replay matches the 2,080-residue human DYSF sequence in a tree and alignment containing 194 entries. PANTHER geneinfo maps the target to PTHR45911:SF3, whereas the saved UniProt record points to PTHR12546:SF44. The target sequence and both imported ancestral nodes are present in the former tree. This lookup discrepancy does not invalidate the curated ancestral assertions.

The three imported IBA contexts join to genuine IBD rows on the target path: calcium binding at PTN002473508; synaptic-vesicle membrane and regulation of neurotransmitter secretion at PTN000413636. Four literal IBD rows occur at those source nodes, including one broader membrane assertion. These results establish the inheritance path, not a target-specific synaptic experiment. MCTP donor specialization and the unresolved relevance to human dysferlin are evaluated separately in the review. A short donor list and the target's own experimental contribution are not evidence of circularity.

The saved IntAct query contains 101 records. Publication-and-partner joins select 34 records across six PMID:23414517 pairs. All 68 participant occurrences have matching reconstructed reference ROGIDs, including four occurrences requiring the specific NEB-1 FASTA. These are repeated reference checks, not 68 distinct proteins or complete experimental clone sequences. Four other source pairs have no matching record in this saved query; their separately reviewed papers and curated assertions remain distinct evidence.

| Partner | IntAct records | Original supplement row | Source-specific validation field |
|---|---:|---:|---|
| MYBPC1 | 4 | 399 | Y2H score A; no orthogonal validation listed |
| MYOM1 | 3 | 402 | Y2H score A; positive IP and proximity ligation; negative colocalization |
| NEB | 4 | 403 | Y2H score A; positive proximity ligation; medium colocalization |
| TTN | 17 | 405 | Y2H score A; positive proximity ligation |
| MYOM2 | 3 | 469 | Y2H score D; positive proximity ligation; negative colocalization |
| SGCG | 3 | 1137 | SGCG is bait and DYSF prey; score A; positive proximity ligation |

These six rows are selected from 137 DYSF-containing rows in `2044-5040-3-3-S1.xls`, worksheet `Table S2`; they are the six partners cited by the source annotations, not the entire DYSF interactome. The independent bait workbook `2044-5040-3-3-S2.xls`, worksheet `Table S1`, identifies the DYSF L2–I485 bait at Excel row 12. IntAct also records additional DYSF fragments for particular experiments. The paper distinguishes human library screens, mouse co-IP samples and human biopsy imaging. Proximity ligation reports close proximity and does not establish a purified binary interface. These limits do not negate a supported partner-class binding assertion. [Original study and supplementary files](https://pmc.ncbi.nlm.nih.gov/articles/PMC3610214/)

Independent partner classes are documented in the saved official records and the following direct locators. The table describes the partner rather than transferring its activity to DYSF.

| Partner | Independent class or role relevant to interpretation | Official source |
|---|---|---|
| NEB | Actin-associated sarcomeric structural protein | [P20929](https://www.uniprot.org/uniprotkb/P20929/entry) |
| MYOM1 | Structural component of the sarcomeric M band | [P52179](https://www.uniprot.org/uniprotkb/P52179/entry) |
| MYOM2 | Structural component of the sarcomeric M band | [P54296](https://www.uniprot.org/uniprotkb/P54296/entry) |
| MYBPC1 | Thick-filament-associated sarcomeric protein | [Q00872](https://www.uniprot.org/uniprotkb/Q00872/entry) |
| TTN | Sarcomeric structural protein | [Q8WZ42](https://www.uniprot.org/uniprotkb/Q8WZ42/entry) |
| SGCG | Transmembrane sarcoglycan component of the dystrophin-associated complex, which links cytoskeleton and extracellular matrix; membership alone does not resolve the narrower actin/microtubule/intermediate-filament component boundary | [Q13326](https://www.uniprot.org/uniprotkb/Q13326/entry) |
| AHNAK / AHNAK2 | Large scaffold proteins with independently curated dysferlin associations | [Q09666](https://www.uniprot.org/uniprotkb/Q09666/entry), [Q8IVF2](https://www.uniprot.org/uniprotkb/Q8IVF2/entry) |
| HDAC6 | Histone deacetylase, also acting on nonhistone substrates | [Q9UBN7](https://www.uniprot.org/uniprotkb/Q9UBN7/entry) |
| RIPOR2 | RHOA regulator and cytoskeletal-signaling protein; not itself a Rho GTPase | [Q9Y4F9](https://www.uniprot.org/uniprotkb/Q9Y4F9/entry) |

The saved definitions place [cytoskeletal protein binding](https://www.ebi.ac.uk/QuickGO/term/GO:0008092) and [histone deacetylase binding](https://www.ebi.ac.uk/QuickGO/term/GO:0042826) under protein binding. Positive binding to an independently established class member does not require evidence that DYSF performs that partner's activity. The HDAC6 pair is supported by the separately read human endogenous co-IP study, rather than by an absent IntAct join. [PMID:24687993](https://pubmed.ncbi.nlm.nih.gov/24687993/)

The second execution uses human MCTP2 Q6DN12 and reproduces its 878-residue sequence in the same family tree. This checks reusable accession selection, path traversal and sequence reconstruction; it does not determine whether DYSF shares every donor specialization.

Analysis checklist:

- [x] Scripts derive counts, rows, paths and sequence checks from saved source inputs; no biological conclusion or expected result is hardcoded into computation.
- [x] The reusable tree/sequence analysis was executed on a second accession, Q6DN12.
- [x] Both executions completed, and the saved outputs reproduce byte for byte.
- [x] Direct machine outputs, input hashes, acquisition locators and fixed dependencies are included.
- [x] Interpretation separates reference identity, assayed fragment, partner class and physiological mechanism.

No new publication quotation is authored in this analysis. Source tables and machine responses retain their original data; interpretation is paraphrased. The automated replay does not replace the source-specific literature assessments.
