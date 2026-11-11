# spo2 (C6Y4C2) — evidence and prediction assessment

Spo2 is a meiosis-induced spindle pole body protein that connects Spo15 with Spo13 on the cytoplasmic face of the meiotic spindle pole body. Its ordered recruitment is required for remodeling the spindle pole body and initiating forespore membrane formation during sporulation. It is not required for the meiotic nuclear divisions themselves.

## Evidence and family boundary

The [primary paper](https://pubmed.ncbi.nlm.nih.gov/18367542/) directly supports the Spo15→Spo2→Spo13 recruitment hierarchy and an adaptor interpretation. PubMed figure8 describes two-hybrid, GST pulldown and co-immunoprecipitation experiments; figure6 describes reciprocal localization dependencies. The cache is abstract-only; PMC and EuropePMC full-text retrieval attempts were unsuccessful. No experimental annotation is removed on that basis.

The exact 133-aa C6Y4C2 sequence matches the terminal segment of the large Vps1302 sequence, but the [reproducible identity analysis](../../../projects/PROTNLM_EVALUATION/family-curation/unassigned-results.json) finds distinct PomBase locus identifiers. Falcon identifies primary full-cDNA evidence for an independent small spo2 transcript; that is a source lead requiring inspection of the full primary text before claiming a gene-model error. Neither shared sequence nor the UniProt VPS13-family sentence establishes that Spo2 has the long lipid-transfer channel of full-length Vps13. Do not conflate family ancestry with retained lipid-transfer activity.

## External ProtNLM statements

[Exact retained output](spo2-protnlm-source.json). These are name/location claims, not emitted GO/EC predictions. CNN denotes overlap with existing supported annotation; it does not establish literal membership in the training set.

| Claim type | Verbatim output | Assessment | Evidence and interpretation |
|---|---|---|---|
| name | Uncharacterized protein | UNSCORED | The returned uncharacterized name has no ECO:0008006 evidence object and is an API default, not an attributable ProtNLM hypothesis. Spo2 is experimentally characterized. |
| location | Membrane | UNC | The target is at the cytoplasmic face of the meiotic SPB beside the nascent forespore membrane. Participation in membrane assembly does not establish membrane residence. The retained source shows a string match to a function comment about membrane formation, not a membrane-localization assay (PMID:18367542). |

## Source quotations

[PMID:18367542](https://pubmed.ncbi.nlm.nih.gov/18367542/):

> Spo2 physically
> associated with both Spo15 and Spo13, but Spo13 and Spo15 did not interact
> directly.

[PMID:18367542](https://pubmed.ncbi.nlm.nih.gov/18367542/):

> Spo13 and Spo2 localized on the cytoplasmic side of
> the SPB in close contact with the nascent FSM.

[PMID:18367542](https://pubmed.ncbi.nlm.nih.gov/18367542/):

> The
> respective deletion mutants are viable, but defective in SPB modification and in
> the onset of FSM formation.

## Research provenance

The genuine [Falcon report](spo2-deep-research-falcon.md) is retained with its provider metadata and artifact. Its conclusions were checked against the target record, exact accession and primary sources described above. Scientific uncertainties are recorded as UNC/UNDECIDED findings rather than a request for another reviewer to perform this assessment.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: re-examined every GOA row, the description and core functions against PMID:18367542 (abstract-only in cache; Europe PMC full-text XML for PMC2397300 not retrievable today), the curated UniProt entry, and a new sequence/signature analysis. ProtNLM2 output was not consulted.

### Identity
- C6Y4C2 is the reviewed Swiss-Prot entry for PomBase locus SPBC16C6.14 (spo2); it is the canonical product of this gene, not an isoform or fragment of another entry for the same gene.
- New analysis ([RESULTS-rereview.md](spo2-bioinformatics/RESULTS-rereview.md), script `compare_vps1302_rereview.py`): all 133 residues equal Vps1302 (O42926, SPBC16C6.02c, 3131 aa) residues 2999-3131; Spo2 Met1 = Vps1302 Met2999. Spo2 has no InterPro/Pfam/PANTHER match, and no VPS13 domain signature of Vps1302 (all end by residue 2938) overlaps the Spo2 segment; only the whole-protein fungal-Vps13 family spans (IPR017148/PIRSF037235, 1-3042) overlap its first 44 residues.
- So UniProt's "Belongs to the VPS13 family" (ECO:0000305) reflects nested sequence identity with the vps1302 3' coding region, not a VPS13 lipid-transfer module. No VPS13 function is transferable. PomBase keeps two loci; the Falcon summary of the full text reports an independent spo2 cDNA. Whether the vps1302 model genuinely extends through spo2 is an open gene-model question (suggested_questions).
- No PANTHER assignment for C6Y4C2; PTHR16166 (interpro/panther/PTHR16166) lists O42926 but not C6Y4C2, and its span stops at 2938, so there is no subfamily-placement disagreement. No PAINT node covers Spo2. No orthologue outside fission yeasts is recognised (abstract: "15-kDa nonconserved protein").

### Annotation decisions (changes vs previous review)
- protein binding IPI x2 (Spo15 = Q10411/SPAC1F3.06c; Spo13 = C6Y4C9/SPCC1183.12): MODIFY, replacement now GO:0030674 protein-macromolecule adaptor activity (is_a GO:0060090, verified in OLS) instead of the root adaptor term; added the recruitment-hierarchy quote.
- spindle pole body IEA: MODIFY to GO:0035974 meiotic spindle pole body (unchanged).
- ascospore formation IMP: changed ACCEPT -> MODIFY to GO:0031322 (an is_a/part_of descendant the gene already carries; OLS ancestors verified), per the correct-but-general rule.
- GO:0031322 IMP and GO:0035974 IDA: ACCEPT (unchanged). SPB remodeling definition includes recruitment of sporulation proteins to the outer plaque; Spo2 is one and recruits Spo13, so this is participation, not mere necessity.
- No NEW terms. Forespore membrane formation was considered but not added: Spo2 acts at the SPB upstream of membrane initiation, and the SPB remodeling term already captures its contribution.

### Relative
- Closest sequence relative is Vps1302 (O42926) by nested identity, not by PANTHER/PAINT phylogeny; it is a distinct locus and the shared segment carries no VPS13 domain. No review exists in genes/SCHPO/. No modules in modules/ cover meiotic SPB / forespore membrane assembly.
