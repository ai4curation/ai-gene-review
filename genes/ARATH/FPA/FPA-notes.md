# FPA (At2g43410, UniProt Q8LPQ9) curation notes

## 2026-10 review session (autonomous pathway module)

- Accession verified: Q8LPQ9 FPA_ARATH, At2g43410. Spen family (3 RRMs + SPOC; UniProt/InterPro).
- Deep research (falcon) failed (HTTP 402).
- Alternative polyadenylation regulator [PMID:20079695 "We report the identification of an activity for FPA in controlling mRNA 3' end formation."]
- Redundant with FCA at COOLAIR [PMID:20079695 "We show that FPA functions redundantly with FCA, another RNA binding protein that controls flowering and RNA silencing, to control the expression of alternatively polyadenylated antisense RNAs at the locus encoding the floral repressor FLC."]
- AtSN1 'silencing' explained by read-through [PMID:20079695 "defective 3' end formation at an upstream RNA polymerase II-dependent gene explains the apparent derepression of the AtSN1 retroelement in fpa mutants"]
- NLR premature termination [PMID:33904405 "the RNA-binding protein FPA mediates widespread premature cleavage and polyadenylation of NLR transcripts"]

## Decisions
- RNA binding accepted; nucleic acid binding -> RNA binding.
- ncRNA-mediated heterochromatin formation kept non-core.
- NEW mRNA alternative polyadenylation (GO:0110104).


## 2026-10-26 autonomous-flowering RNA-factor audit

All rows were reviewed, preserving original terms, evidence, references, qualifiers, NOT flags and supporting entities. Falcon/fallback research and gene-publication retrieval ran concurrently under the parent workflow; provider attempts failed and logs remain under `.cache/module-audit-logs/autonomous-flowering-fetch/`. No provider report was fabricated. Primary source caches and curated UniProt evidence were inspected independently. Annotation-reviewer consultation with the chromatin-panel reviewer agreed that nuclear predominance is not organelle exclusion, broad RNP membership does not require PABP identity, and FPA termination reinterpretations are locus-specific.

The authoritative PAINT inspection is reproducible in `genes/ARATH/FCA/FCA-bioinformatics/`. It uses exact existing PTNs and is not a reconstructed family phylogeny. The failed full-family download was not used; only its incomplete .part file was removed after disk exhaustion. Current source retrieval is recorded honestly: PMID18223036 refreshed complete; PMID19439664 cache abstract-only but full web text inspected; 16820865 and19561057 recovered normally; optional16753815 fetch returned429 and was not used to support a new claim.

- Nuclear location supported by the publication-linked curated UniProt statement and independent chromatin/termination work; RNA binding and floral-promotion claims retained.
- GO:0031048 changed from non-core to UNDECIDED. PMID:17916737 reports locus-dependent effects; PMID:20079695 explains AtSN1 by read-through. Full PMID:24204292 documents termination defects and no widespread silencing role, without proving absence at every locus. Original2007 detailed locus experiments remain inaccessible.
- Existing NEW alternative mRNA polyadenylation is supported by direct FPA-dependent IBM1/intronic poly(A) sites (PMID:24204292), rather than a COOLAIR-only quotation. No new rows added.
