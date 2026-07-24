# ARSJ review notes

## Retrieval and scope

- UniProt/GOA data were fetched on 2026-07-18. The GOA snapshot contains seven grouped annotations.
- Falcon deep research failed with HTTP 402, and the required Perplexity-lite fallback failed with HTTP 401 (quota). Manual research is recorded in `ARSJ-deep-research-manual.md`; no provider-named file was authored.
- The central curation problem is that ARSJ has convincing class-I sulfatase architecture but no defined native substrate and no positive ARSJ-specific biochemical assay.

## Protein identity and catalytic inference

- Human ARSJ is a reviewed 599-aa precursor (UniProt Q5FYB0) with a predicted signal peptide at residues 1-49, a mature chain at residues 50-599, and a conserved sulfatase catalytic cysteine at position 122. UniProt transfers calcium-binding and catalytic residues from ARSB by homology.
- The family catalog identifies ARSJ among the 17 human sulfatases and reports that the sulfatase active site is especially evolutionarily constrained [PMID:16174644, "the active site, which is the target of the post-translational modification, is the most evolutionarily constrained region of sulfatases"]. This supports the broad GO:0008484 sulfuric ester hydrolase activity inference.
- A later primary study states that recombinant ARSI and ARSJ had previously been expressed in HeLa cells without detectable activity against the standard arylsulfatase assay [PMID:19262745, "ARSI and ARSJ cDNAs have been cloned and expressed in HeLa cells, but no ARS activity has been detected"]. This does not disprove activity against an unknown physiological sulfate ester, but it means GO:0004065 arylsulfatase activity is too specific at present.

## Localization

- The N-terminal signal peptide and reviewed UniProt secretion assignment support GO:0005576 extracellular region, although direct secretion of ARSJ itself has not been demonstrated in a primary paper available here.
- Reactome places ARSJ in the ER lumen during SUMF1-mediated conversion of the catalytic cysteine to formylglycine. This is a biosynthetic/maturation location rather than an established site of mature ARSJ action, so it is retained as non-core.
- Human Protein Atlas immunofluorescence maps ARSJ to actin filaments in BJ fibroblasts with an enhanced score and concordant staining from two antibodies; other tested cell lines showed no staining. The GO annotation is retained as a cell-context observation, not treated as a core location. The relationship between a signal-peptide-bearing protein and actin-associated staining remains unresolved.

## Expression and biological context

- Mouse embryonic in situ hybridization detected Arsj in developing joints [PMID:20503373, "novel expression patterns for ArsG in choroid plexus, ArsI in hypertrophic chondrocytes and ArsJ in joints were identified"]. This is expression evidence only and does not justify a human developmental-process annotation.
- A human tissue RNA panel found ARSJ transcript highest in lung among the tissues tested [PMID:30760748, "ARSJ showed the highest expression in the lung compared to all other tissues"]. That study explicitly did not assay ARSJ enzymatic activity, so no COPD or lung-process term is proposed.

## Annotation decisions

| GO term | Evidence | Decision | Rationale |
|---|---|---|---|
| GO:0008484 sulfuric ester hydrolase activity | IBA | ACCEPT | Conserved class-I sulfatase catalytic machinery and phylogenetic inference support the broad activity. |
| GO:0004065 arylsulfatase activity | IEA | MODIFY to GO:0008484 | No ARSJ-specific aryl-sulfate cleavage has been demonstrated; a standard assay was negative. |
| GO:0005576 extracellular region | IEA | ACCEPT | Signal peptide plus reviewed secretion assignment support entry into the extracellular secretory route. |
| GO:0008484 sulfuric ester hydrolase activity | IEA | ACCEPT | InterPro sulfatase-core mapping agrees with the IBA and conserved catalytic residues. |
| GO:0015629 actin cytoskeleton | IDA | KEEP_AS_NON_CORE | Enhanced HPA immunofluorescence is retained, but it is cell-context-specific and mechanistically unresolved. |
| GO:0005788 ER lumen | TAS | KEEP_AS_NON_CORE | Appropriate for SUMF1-dependent maturation/transit, not established as the mature functional site. |
| GO:0004065 arylsulfatase activity | TAS | MODIFY to GO:0008484 | PMID:16174644 establishes family membership and catalytic conservation, not ARSJ aryl-substrate turnover. |

## Open issues

- Identify the native sulfate-ester substrate and determine whether ARSJ cleaves any small aryl-sulfate surrogate under conditions that ensure SUMF1-dependent formylglycine formation.
- Directly resolve whether mature ARSJ is secreted, retained in the ER, membrane-associated, or present in more than one pool.
- Test whether joint expression in mouse embryos or lung-enriched human transcript abundance reflects a conserved physiological role.

