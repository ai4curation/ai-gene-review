# Bacillus cereus phnX curation notes

## 2026-10-25

The fetched protein is O31156 (PHNX_BACCE), the experimentally characterized phosphonatase from strain ATCC 43881 / AI-2 recorded by UniProt. It is an appropriate Bacillota exemplar for the PhnWX carbon-phosphorus cleavage step. The enzyme is not merely a sequence-based candidate: PMID:9649311 describes recombinant purification and kinetics for Bacillus and Salmonella proteins, and PMID:10956028 provides the Bacillus enzyme structure with magnesium and product analogue. The exact protein therefore complements the inferred KT2440 exemplar without transferring strain-specific measurements to it.

Sources inspected include the cached abstracts of PMID:9649311, PMID:10956028, PMID:15109258 and PMID:17070898; the full text of PMID:17070898 was also read at https://pmc.ncbi.nlm.nih.gov/articles/PMC1941675/. The full-text download helper initially returned an abstract-only record; a retry successfully cached the full text. Quotes in the YAML occur in the cached abstract.

- Reaction evidence: [PMID:10956028, The crystal structure of bacillus cereus phosphonoacetaldehyde hydrolase, "phosphonoacetaldehyde to acetaldehyde and phosphate using Mg(II) as cofactor."]
- Direct target-species experiment: [PMID:15109258, Investigation of metal ion binding in phosphonoacetaldehyde hydrolase identifies sequence markers for metal-activated enzymes of the HAD enzyme superfamily, "Mg(II)-activated Bacillus cereus phosphonoacetaldehyde hydrolase (phosphonatase)"]
- Pathway role: [PMID:17070898, Diversification of function in the haloacid dehalogenase enzyme superfamily, "Phosphonatase functions in the 2-aminoethylphosphonate (AEP) degradation pathway of bacteria"]

The seven seeded annotations were individually assessed. Magnesium binding, phosphonatase activity and organic phosphonate catabolism are supported; catalytic activity is refined to the existing specific hydrolase term. The TreeGrafter phosphoglycolate phosphatase and DNA-repair transfers are rejected because the target has experimentally established phosphonatase specialization, not because an ancestral family label looks unfamiliar. The source PTN001822734 is recorded in the machine-seeded supporting_entities; its underlying donor functions were not re-curated here. No absence-of-promiscuity claim is made. The cytosol transfer remains UNDECIDED: soluble preparations and crystal structures are not native-cell localization experiments.

Older papers number catalytic residues differently from the current UniProt sequence (for example Lys53 versus current Lys50); UniProt records an erroneous initiation in the older sequence. No residue-level propagation claim is asserted, and current residue numbers are not silently substituted into quotations.

Provider research was attempted with `just deep-research-falcon BACCE phnX --fallback perplexity-lite`. Falcon failed authentication; the fallback failed with insufficient quota. No generated research report was produced or fabricated. Manual literature research above supplies the evidence. `just fetch-fitness BACCE phnX` was also attempted; BACCE has no configured FEBA mapping and no reachable data source, so no fitness artifact was produced. The missing optional provider/fitness results do not replace or weaken the direct biochemical evidence.
