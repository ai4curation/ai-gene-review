# ANKRD33 notes

- PANKY: photoreceptor- and pineal-specific. CRX induces it, and it suppresses CRX-activated genes and reduces CRX DNA binding [PMID:20026326, mouse, abstract].
- In vivo [PMID:42463452, 2026, abstract; affinage missed it]: single Panky or Panky-like (Ankrd33b) knockouts are normal. Double knockouts lose cone outer-segment and synaptic structure, have raised gangliosides, and later lose cones. PANKY/PANKY-LIKE suppress Crx transactivation of Cerkl.
- NeuroD1 cKO retina: Ankrd33 is down 7.8-fold [PMID:22784109].
- GOA: nucleus (IEA, ISS) and cytosol (IEA), all by similarity to mouse; all ACCEPT.
- MF deliberately not asserted. GO:0003714 corepressor (acts at the locus by binding the DNA-bound TF) and GO:0140416 TF inhibitor (directly binds the TF to keep it off DNA) both require direct CRX binding, which the cached abstracts do not show; the EMSA result fits the inhibitor reading. Recorded as an MF_DARK knowledge gap.
- PMID:31314707 (ANKRD33 in gastric adenocarcinoma) was retracted (PMID:35077532); it is not cited.
- No IBAs; PAN-GO 0.

## Round 2 (reviewer, PR #4115)

- The cytosol reason now explains itself: UniProt asserts cytosol by similarity, the mouse paper says "cytoplasm", and no cytosolic function is known.
- I tried to retrieve the full text of PMID:42463452 (PMC13492463). Europe PMC returned a server error and PMC-OA returned no result. The gap boundary now says the full texts were not retrieved, not that the question is unstudied.
- NEW GO:0000122 negative regulation of transcription by RNA polymerase II (ISS from mouse), now the core BP. It does not depend on the corepressor-vs-inhibitor question.
- The description no longer chains gangliosides causally to Cerkl; the abstract reports them separately, and the Cerkl RNA-seq was done in the Nrl-null background.
- The retracted PMID:31314707 is now listed with is_invalid: true, so it cannot be re-imported.
- The gap boundary mentions the MBD3 and ANKRD11 high-throughput interactions.
