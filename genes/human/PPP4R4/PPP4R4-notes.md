# PPP4R4 notes


## 2026-09-08 paired human–horse review



PPP4R4 is a cytosolic regulatory subunit of protein phosphatase 4. It forms a stable complex with the PP4 catalytic subunit that is distinct from complexes containing PP4R1 or PP4R2–PP4R3. Its association changes PP4 activity and subcellular organization rather than providing intrinsic phosphatase catalysis.

## Complex formation versus universal inhibition

The primary affinity-purification study identifies PP4R4 as a stable PP4c-specific partner and distinguishes it from PP2A/PP6 interactions and other PP4 regulatory complexes. PP4R4-associated activity toward fluorogenic substrate and gammaH2AX is lower than free PP4c and different from PP4R2/3-associated activity. This supports a regulatory subunit and an inhibitory effect in the tested assays, but does not establish that it inhibits all physiological PP4 substrates. It also does not establish blastocyst hatching. The selected horse sequence is nearly full-length and highly conserved, allowing stronger transfer of complex membership than a particular developmental phenotype.

## Decisive inspected evidence

From [PMID:18715871](https://pubmed.ncbi.nlm.nih.gov/18715871/):

> we identify  a novel, stable cytosolic PP4c interacting partner, KIAA1622, which we have  renamed PP4R4.

## Evidence inventory

- [PMID:18715871: PP4R4/KIAA1622 forms a novel stable cytosolic complex with phosphoprotein phosphatase 4.](https://pubmed.ncbi.nlm.nih.gov/18715871/). [DOI:10.1074/jbc.M803443200](https://doi.org/10.1074/jbc.M803443200). The repository cache contains the abstract; source-specific claims beyond it remain unresolved.

## Transfer to the selected horse protein

The exact target is [A0A9L0S961](https://www.uniprot.org/uniprotkb/A0A9L0S961/entry), not an arbitrary horse record with a matching name. The reproducible [paired-sequence analysis](../../HORSE/PPP4R4/PPP4R4-bioinformatics/RESULTS.md) records identity, coverage and internal gaps. It supports homology but is not a reciprocal orthology test. Molecular properties are transferred only with the relevant domain, targeting and paralog constraints. The prediction-time sequence is not independently verified.

## Open evidence questions

The following annotation scopes need source-specific follow-up: protein binding. Experimental annotations are not removed merely because a cached abstract omits the gene or a specific assay. High-throughput protein-binding rows require their actual partner or complex context before replacement with an informative molecular function.


Research provenance: external Falcon/Edison was attempted with Perplexity fallback. Some requests returned HTTP 429 and fallback returned insufficient-quota HTTP 401; successful external reports are preserved separately. Primary-source manual synthesis is explicitly labeled manual where no external report was available.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Scope: full re-review of every existing annotation, description and core function for Q6NUP7. No ProtNLM2 output was consulted.

### Identity
- Q6NUP7 is the reviewed, canonical UniProt entry (isoform 1, 873 aa, HEAT/ARM-type repeats at 213-251, 252-290, 392-427; C-terminal disordered regions). The benchmark accession is the canonical product, not a fragment or alternative model. Isoform 2 (Q6NUP7-2) is a 120-aa truncation (VSP_029616/VSP_029617) lacking all HEAT repeats; no annotation is isoform-specific.

### Deep research
- `just deep-research-falcon human PPP4R4 --fallback perplexity-lite` failed today: Edison/falcon returned 403 Forbidden at auth, and the perplexity-lite fallback timed out at 600 s. No deep-research file was produced. Proceeded from primary literature.
- PubMed search (PPP4R4 / PP4R4 / KIAA1622 in title/abstract) returns only one functional study, PMID:18715871 (Chen et al. 2008); the rest are expression/association screens. PMC2662017 full text could not be retrieved (Europe PMC and BioC both empty), so all quotes are from the abstract.

### Evolutionary grounding
- PANTHER PTHR21467 (single subfamily SF0); human Q6NUP7 and mouse Q8C0Y0 are the cached members. Human PP4R4 is the only experimentally characterised member; IBA rows (PTN001087371) list Q6NUP7 as donor, which is the expected marker of experimental grounding on the target, not circularity.
- The family review `interpro/panther/PTHR21467/PTHR21467-review.yaml` places human and horse in SF0; no subfamily disagreement.
- Weak homology to PP2A A subunit (PPP2R1A) is a different PANTHER family; no PP2A-A scaffolding function is transferred (the paper shows PP4R4 does not bridge PP4c to other regulatory subunits).

### Decisions (changes from the previous review)
- Protein binding (6 IPI rows, all with PPP4C P60510): UNDECIDED -> MODIFY to protein phosphatase binding (GO:0019903).
- Phosphatase inhibitor activity / Ser/Thr phosphatase inhibitor activity (IDA): KEEP_AS_NON_CORE -> MODIFY to protein phosphatase regulator activity (GO:0019888). Reduced activity of the PP4c-PP4R4 complex vs free PP4c is shared by PP4c-PP4R2-PP4R3 [PMID:18715871 "this activity is lower than that associated with the PP4c.PP4R2.PP4R3 complex, which itself is less active than the free PP4c catalytic subunit"], so it is a generic holoenzyme effect rather than evidence for an inhibitor.
- Cytoplasm (IDA, IEA): ACCEPT -> MODIFY to cytosol (already carried by IDA and IBA).
- Protein serine/threonine phosphatase complex (IDA, IBA): ACCEPT -> MODIFY to protein phosphatase 4 complex (GO:0030289, verified is_a GO:0008287 in OLS); PP4R4 binds PP4c, not PP2Ac/PP6c.
- Cytosol (IDA, IBA) and protein phosphatase regulator activity (IBA): ACCEPT.
- No NEW process terms: no evidence identifies a process in which PP4R4 itself does work; PP4-level processes (DNA damage response, etc.) are not transferred from the catalytic subunit or other regulatory subunits.
- Description rewritten; core function now records regulator activity, cytosol and protein phosphatase 4 complex.

### Relatives
- No characterised ortholog outside human; the horse ortholog A0A9L0S961 (genes/HORSE/PPP4R4) is in the same subfamily and already has a complete review. No modules reference PPP4R4.
