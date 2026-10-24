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

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Identity: Q9Y7T6 is the reviewed, canonical, full-length (504 aa) UniProt entry for SPCC63.10c/sec59.
It is not an isoform, fragment or alternative gene model. Ten predicted TM helices (first at 56-76),
Polypren_kinase domain (IPR032974).

Evolutionary grounding:
- PANTHER: PTHR13205:SF15 (DOLICHOL KINASE), the same subfamily as S. cerevisiae SEC59 (P20048, 519 aa)
  and human DOLK (Q9UPQ8, 538 aa) [file:interpro/panther/PTHR13205/PTHR13205-entries.csv "sec59,504,PTHR13205:SF15,DOLICHOL KINASE"].
- PAINT node PTN000324722 (taxon:2759) carries GO:0004168, GO:0005789 and GO:0043048 by IBD, seeded by
  SGD:S000004615 (SEC59), Q9UPQ8 (DOLK), Q38DD5 and AT3G45040. Transfer of activity to pombe is therefore
  phylogenetically grounded, not best-hit based.
- Donor biochemistry: [PMID:1323123 "However, dolichol kinase activity was greatly decreased."];
  Dol-P drops to <10% at restrictive temperature and Dol-P-Man synthesis is rescued by exogenous Dol-P.
  [PMID:12213788] human DOLK complements sec59-1 and separates dolichol from DAG kinase activity.
- Pombe-specific evidence: only the proteome-wide YFP localization (PMID:16823372; ER), curated by UniProt
  as ER membrane. No pombe enzymology.

Decisions (8 rows): GO:0004168 x3 (IBA, IEA, ISS) ACCEPT; GO:0005783 HDA MODIFY -> GO:0005789; GO:0005789 x2
ACCEPT; GO:0043048 IBA ACCEPT; GO:0180047 IC KEEP_AS_NON_CORE. On GO:0180047: the definition covers
"reactions and pathways resulting in the formation" of Dol-P-Man, and Sec59 makes the Dol-P that becomes
its lipid moiety, so it catalyzes a pathway step (not substrate-only); kept non-core because Dol-P also feeds
Dol-PP-oligosaccharide and Dol-P-Glc. No NEW terms: downstream N-glycosylation/O-mannosylation/GPI anchoring
are precursor supply and are not proposed.

Changes vs previous version: replaced templated reasons with row-specific reasoning grounded in PANTHER SF15 /
PTN000324722; HDA row now cites the UniProt subcellular-location line and the screen abstract rather than the
function line; added reference_review entries; added PANTHER entries inventory as a reference; added
suggested question/experiment.

Relative: S. cerevisiae SEC59 (P20048), same subfamily SF15 and PAINT donor; complete review exists at
genes/yeast/SEC59/SEC59-ai-review.yaml. Human DOLK review (genes/human/DOLK) is DRAFT.
PANTHER family review interpro/panther/PTHR13205/PTHR13205-review.yaml places sec59 in SF15; no disagreement.
Modules: modules/dolichol_phosphate_sugar_donor_supply.yaml (lists sec59 Q9Y7T6), modules/dolichyl_phosphate_biosynthesis.yaml.
