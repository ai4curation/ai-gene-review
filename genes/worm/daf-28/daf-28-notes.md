# daf-28 notes

Deep research: falcon failed and the perplexity-lite fallback was unavailable (2026-10-08). No deep-research file was created. Q9NEK7 is an unreviewed TrEMBL entry, and it is the accession the module uses.

## Key findings
- daf-28 encodes an insulin-like protein expressed in ASI and ASJ. Its expression is down-regulated under dauer-inducing conditions [PMID:12654727]. sa191 is a dominant-negative processing-site allele [PMID:12654727 "This DAF-28 mutant is likely to be poisonous to wild-type DAF-28 and other insulins."].
- daf-28 plays the primary role in inhibiting dauer entry [PMID:21343369 "daf-28 plays a more primary role in inhibiting dauer entry"]. Neuronal ILPs inhibit intestinal DAF-16 [PMID:24671950].
- DAF-28 co-localizes with SNB-1 at ASJ synaptic regions [PMID:25048458].

## Decisions
- The 8 dauer larval development rows were changed (MODIFY) to negative regulation of dauer entry (GO:1905910).
- protein import into nucleus (IMP, acts upstream): MARK_AS_OVER_ANNOTATED, because it is indirect and already captured by GO:1900181.

## Description follow-up (2026-10-30): IDA-1
- WormBase says the transmembrane protein-tyrosine phosphatase-like protein IDA-1 is required for DAF-28 function, and that an ida-1 null allele enhances daf-28(sa191). IDA-1 is the C. elegans IA-2/phogrin homologue, a dense-core vesicle protein that genetically interacts with UNC-31/CAPS [PMID:15044551 "CeIA-2 has a specific and novel genetic interaction with UNC-31/CAPS, a protein that has been shown in other systems to regulate dense-core vesicle cargo release"]. Its loss enhances weak insulin-pathway alleles [PMID:15044551 "loss of CeIA-2 activity enhances weak alleles in the insulin-like signaling pathway"].
- Only the abstract is cached, and it does not name daf-28, so the daf-28(sa191) enhancement could not be checked directly. The interaction fits a role for IDA-1 in dense-core vesicle release of insulin-like peptides. That makes IDA-1 a regulator of DAF-28 secretion, not a DAF-28 activity, so no annotation was added.
