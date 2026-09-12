# sec59 (Q9Y7T6) — evidence and prediction assessment

Sec59 is an endoplasmic-reticulum membrane dolichol kinase that produces dolichyl phosphate by CTP-dependent phosphorylation of dolichol. Dolichyl phosphate supplies the lipid carrier needed for protein N-glycosylation, O-mannosylation and GPI-anchor formation. Conserved Sec59/DOLK orthology supports this function in fission yeast; the related CTP-dependent phosphorylation of diacylglycerol is a distinct enzyme activity.

## Evidence and family boundary

The full 504-aa target has a curated Sec59/DOLK assignment and multipass ER membrane architecture. Its [P20048 ortholog source](sec59-P20048-ortholog-uniprot.txt) traces to experiments. [PMID:1323123](https://pubmed.ncbi.nlm.nih.gov/1323123/) links the budding-yeast sec59 defect to loss of dolichol kinase and depletion of dolichyl phosphate; adding the lipid carrier restores downstream mannose-carrier synthesis. [PMID:12213788](https://pubmed.ncbi.nlm.nih.gov/12213788/) distinguishes CTP-dependent dolichol phosphorylation from DAG kinase activity.

This supports target function by orthology, not a claim that those enzyme assays used pombe Sec59. The target HDA ER observation is retained despite Falcon’s failure to retrieve it. Dolichol-phosphate-mannose biosynthesis is valid downstream process participation through precursor supply; the direct core reaction is dolichol phosphorylation, not mannose transfer.

## External ProtNLM statements

[Exact retained output](sec59-protnlm-source.json). These are name/location claims, not emitted GO/EC predictions. CNN denotes overlap with existing supported annotation; it does not establish literal membership in the training set.

| Claim type | Verbatim output | Assessment | Evidence and interpretation |
|---|---|---|---|
| name | dolichol kinase | CNN | The target has the full membrane-kinase architecture and a curated transfer from experimentally characterized P20048/Sec59. Donor biochemistry distinguishes CTP-dependent dolichol phosphorylation from DAG kinase activity (PMID:1323123; PMID:12213788). |
| location | Membrane | LSP | The target is more specifically an ER membrane protein according to the curated localization and membrane topology. The broad membrane statement is correct but adds no compartment resolution (PMID:16823372; Q9Y7T6). |

## Source quotations

[PMID:12213788](https://pubmed.ncbi.nlm.nih.gov/12213788/):

> Dolichol kinase (DK) catalyzes the CTP-mediated phosphorylation of dolichol in 
> eukaryotic cells, the terminal step in dolichyl monophosphate (Dol-P) 
> biosynthesis de novo.

## Research provenance

The genuine [Falcon report](sec59-deep-research-falcon.md) is retained with its provider metadata and artifact. Its conclusions were checked against the target record, exact accession and primary sources described above. Scientific uncertainties are recorded as UNC/UNDECIDED findings rather than a request for another reviewer to perform this assessment.
