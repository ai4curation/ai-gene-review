# iwr1 (SPAC23H4.08 / O13951) — S. pombe — curation notes

## Identity (verified from UniProt record `iwr1-uniprot.txt`)
- UniProt: **O13951**, `IWR1_SCHPO`, 277 aa, reviewed. PE level **3 (Inferred from homology)**.
- Gene: `iwr1`; systematic/ORF name `SPAC23H4.08`; Chromosome I.
- Taxon: *Schizosaccharomyces pombe* 972 / ATCC 24843, NCBITaxon:284812.
- RecName: "RNA polymerase II nuclear localization protein iwr1".
- Family: **IWR1/SLC7A6OS family** (UniProt SIMILARITY, ECO:0000305).
- Domains/family signatures (DR lines):
  - Pfam **PF08574** (Iwr1)
  - InterPro **IPR040150** (Iwr1), **IPR013883** (TF_Iwr1_dom / "Interactor of Rpb1")
  - PANTHER **PTHR28063** = "RNA POLYMERASE II NUCLEAR LOCALIZATION PROTEIN IWR1" (SF1 same name)
- Feature table: C-terminal **disordered region 222–277**; MobiDB-lite compositional bias — basic+acidic (225–234), strongly **acidic** (251–277). No annotated structured/globular domain outside the family fold.
- UniProt curated statements (all **by similarity, ECO:0000250** — i.e. NOT direct pombe experiment):
  - FUNCTION: "Directs RNA polymerase II nuclear import."
  - SUBUNIT: "Associates with RNA polymerase II."
  - SUBCELLULAR LOCATION: Cytoplasm + Nucleus; "shuttles between the nucleus and cytoplasm."

## GOA annotation landscape (`iwr1-goa.tsv`) — 9 annotations, ALL inferred
No experimental (IDA/IMP/IGI/IPI/IEP) annotation exists for **pombe** iwr1. Evidence is entirely:
- **IBA** (GO_REF:0000033, PANTHER PTN002821512 | SGD:S000002273): nucleus (is_active_in), cytoplasm (is_active_in), protein import into nucleus (involved_in).
- **ISO** (GO_REF:0000024, from **SGD:S000002273** = *S. cerevisiae* IWR1/YDL115C): nucleus (is_active_in), protein import into nucleus (involved_in).
- **IEA** (GO_REF:0000044, UniProt-SubCell): nucleus, cytoplasm (located_in).
- **IEA** (GO_REF:0000002, InterPro IPR040150): protein import into nucleus (involved_in).
- **ND** (GO_REF:0000015, PomBase): molecular_function root GO:0003674 — i.e. PomBase records **no experimentally-supported MF**.

=> This is a genuinely **dark / understudied** gene in pombe: all functional inference is by orthology to the well-characterized budding-yeast IWR1, plus family signatures.

## Ortholog literature (S. cerevisiae IWR1 = SGD:S000002273; the source of the ISO transfers)
The pombe annotations transfer from experimentally characterized S. cerevisiae IWR1.

- **Czeko et al. 2011, Mol Cell** [PMID:21504834] — *S. cerevisiae* (abstract-only in cache; full_text_available: false):
  - "Pol II nuclear import requires the protein Iwr1" [PMID:21504834 "Here we show that Pol II nuclear import requires the protein Iwr1 and provide evidence for cyclic Iwr1 function."]
  - Mechanism: "Iwr1 binds Pol II in the active center cleft between the two largest subunits, maybe facilitating or sensing complete Pol II assembly in the cytoplasm." [PMID:21504834]
  - "Iwr1 then uses an N-terminal bipartite nuclear localization signal that is recognized by karyopherin α to direct Pol II nuclear import." [PMID:21504834]
  - Recycling: "In the nucleus, Iwr1 is displaced from Pol II by transcription initiation factors and nucleic acids, enabling its export and recycling." [PMID:21504834]
  - Specificity/conservation: "Iwr1 function is Pol II specific, transcription independent, and apparently conserved from yeast to human." [PMID:21504834]

- **Esberg et al. 2011, PLoS ONE** [PMID:21695216] — *S. cerevisiae* (full text in cache):
  - Originally identified via physical interaction with Pol II: "Iwr1, a protein conserved throughout eukaryotes, was originally identified by its physical interaction with RNA polymerase (Pol) II." [PMID:21695216 "Iwr1, a protein conserved throughout eukaryotes, was originally identified by its physical interaction with RNA polymerase (Pol) II."]
  - Broader PIC role: "Iwr1 plays an important role in preinitiation complex formation by all three nuclear RNA polymerases." [PMID:21695216 "Thus, Iwr1 plays an important role in preinitiation complex formation by all three nuclear RNA polymerases."]
  - iwr1 mutant defects: "an iwr1 mutant strain shows reduced association of TBP and Pol III at Pol III promoters, a decreased rate of Pol III transcription, and lower steady-state levels of Pol III transcripts." [PMID:21695216]
  - Note: the Pol I/III effects are interpreted (in the field / Cramer lab) as downstream/indirect consequences of impaired Pol II import; the *direct, Pol II-specific* import function is the defining molecular role (Czeko 2011).

## KNOWN (by orthology + family signature, not pombe experiment)
- Molecular role: dedicated **RNA polymerase II assembly/import chaperone** — binds the assembled 12-subunit Pol II in its active-center cleft; not a general karyopherin but an adaptor that presents its own bipartite NLS to karyopherin-α.
- Biological role: **protein import into nucleus** (of Pol II specifically), enabling nuclear transcription; cyclic loading/unloading and recycling.
- Localization: nucleocytoplasmic shuttling (cytoplasm + nucleus).

## NOT known for pombe iwr1 (knowledge gaps — primary deliverable)
- No direct S. pombe experimental evidence for ANY molecular function (PomBase MF = ND).
- Whether the Pol II import role is conserved and essential/non-essential in pombe (S. cerevisiae iwr1Δ is viable but growth-impaired; not tested here for pombe).
- Whether pombe iwr1 physically binds pombe Pol II (Rpb1/Rpb2 cleft) — no pombe IPI.
- Deletion/mutant phenotype in pombe (no pombe phenotype annotation captured in GOA).
- Whether it has any Pol I/Pol III-related or transcription-elongation roles in pombe.
- Precise molecular-function GO term: there is no dedicated "Pol II import chaperone" MF term; role is currently captured only at the BP level (protein import into nucleus) — genuine MF gap.

## Curation reasoning for actions
- BP `GO:0006606 protein import into nucleus`: well-supported by orthology + family; the IBA (best phylogenetic evidence) is the core representative; ISO and InterPro-IEA are corroborating duplicates — KEEP core one, mark the duplicate lower-evidence ones as non-core/over-annotated as appropriate (do not REMOVE, all consistent).
- CC `GO:0005634 nucleus` + `GO:0005737 cytoplasm`: consistent with shuttling; IBA is_active_in reflects site of action. Keep; SubCell IEA duplicates are redundant but not wrong.
- MF `GO:0003674` root with ND: this is a placeholder meaning "no MF determined"; keep as-is (standard), acknowledge the MF gap.
- Never REMOVE the ISO/IBA import annotation: it is a defensible orthology transfer from an experimentally solid budding-yeast function; the family signature (Pfam Iwr1) directly supports it.
