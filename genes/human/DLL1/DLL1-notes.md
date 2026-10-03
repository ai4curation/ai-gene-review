# DLL1 (human, O00548) review notes

## Identity
- Delta-like protein 1; DSL-family transmembrane Notch ligand. PANTHER PTHR24049 / PTHR24049:SF38.
- IBA nodes: Notch binding PTN002371879; plasma membrane, Notch signaling pathway, negative regulation of Notch signaling PTN001170801.

## Key findings (with provenance)
- Direct Ca2+-dependent binding to NOTCH1/NOTCH3 ectodomains [PMID:11006133 "All interactions between the DSL proteins and soluble Notch proteins were dependent on Ca(2+)."]
- MNNL-EGF3 sufficient for NOTCH1 activation; NOTCH1 prefers DLL4 over DLL1 by >10-fold affinity [PMID:23839946 "Truncation studies of the Dll1 and Dll4 ectodomains showed that the MNNL-EGF3 region was both necessary and sufficient for full activation."]
- Soluble DLL1 is a weak activator; ICD needed for full NOTCH2 S3 cleavage [PMID:11823422 "Here we show that soluble Delta1 (sD1) activates Notch2 (N2), but much more weakly than full-length Delta1 (fD1)."]
- C-terminal ATEV PDZ-binding motif binds MAGI1-3 PDZ4 [PMID:15509766]; SYNJ2BP stabilises DLL1/DLL4 via PDZ motif [PMID:24025447].
- Cis-inhibition: NOTCH2NL relieves cis DLL1-NOTCH interactions [PMID:29856955 "At the molecular level, NOTCH2NL function by activating the Notch pathway through inhibition of cis Delta/Notch interactions."]
- Lymphoid fate: DLL1 blocks B and promotes T/NK precursors [PMID:11581320].
- DOS motif present in EGF1-2 (unlike DLL4) [file:human/DLL1/DLL1-deep-research-falcon.md].
- Ubiquitinated by MIB1 (Lys-613) -> endocytosis/pulling force (UniProt, by similarity).

## Curation decisions
- Core: Notch binding (GO:0005112), receptor ligand activity (GO:0048018), PDZ domain binding (GO:0030165, via MODIFY of protein binding/Tat binding rows); Notch signaling pathway, lateral inhibition; plasma membrane.
- Tat protein binding (GO:0030957, IPI PMID:15509766) -> MODIFY to PDZ domain binding (partners are MAGIs).
- Many mouse-orthology developmental terms kept as non-core; blood pressure/energy homeostasis/growth/proliferation/transcription/endocytosis terms marked over-annotated.

## Variant-relevant biology
- DLL1 has a DOS motif (DLL4 does not); has C-terminal PDZ-binding ATEV motif (shared with DLL4, absent from JAG1); acts in trans (activation) and cis (inhibition).

## Deep research
- Falcon deep research completed: file:human/DLL1/DLL1-deep-research-falcon.md (the wrapper reported a 600 s timeout, but the client finished writing the report after 941 s). Key statements quoted in the review are verbatim from that file.
