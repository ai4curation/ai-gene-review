# mlaE (P64606, Escherichia coli K-12) - curation notes

## Deep research
- 2026-10-23: `just deep-research ECOLI mlaE --provider perplexity` was attempted once and failed
  ("Provider 'perplexity' not available. Available: falcon, openscientist"). No deep-research file
  was generated; this review is built directly from cached full-text publications and the UniProt record.

## Identity and topology
- MlaE (YrbE) is the 260-residue integral inner-membrane permease (TMD) of the MlaFEDB ABC transporter;
  member of the MlaE permease family (Pfam PF02405; NCBIfam TIGR00056) [file:ECOLI/mlaE/mlaE-uniprot.txt
  "Belongs to the MlaE permease family."].
- Inner-membrane location: global topology mapping placed the C terminus in the cytoplasm
  [PMID:15919996, abstract only]; UniProt "Cell inner membrane {ECO:0000269|PubMed:15919996".
  Membrane proteomics of an E. coli K-12 inner-membrane fraction [PMID:17309111, abstract only].

## Complex
- MlaF, MlaE, MlaD and MlaB form a stable complex [PMID:27529189 "We conclude that MlaF, MlaE, MlaD and
  MlaB form a stable complex."]; stoichiometry MlaF2E2D6B2.
- Cryo-EM: "A homohexameric ring of MCE domains from MlaD sits atop the periplasmic end of MlaE like a
  crown." [PMID:33236984]. MlaE is distantly related to the TMDs of LptFG / MacB and ABCA/ABCG.
- MlaD modulates complex ATPase "via its interaction with MlaE" [PMID:27529189].

## Substrate binding (key MF evidence)
- [PMID:33236984 "Additional density was apparent in the outward-open pocket of MlaE, which is the right
  size and shape to accommodate two diacyl phospholipids"].
- In vivo photocrosslinking with BPA at pocket residues: [PMID:33236984 "Thus, the phospholipid-binding
  site observed in our MlaFEDB structure is occupied by phospholipids in vivo."]
- Continuous pathway: [PMID:33236984 "A continuous transport pathway extends from the MlaE
  substrate-binding site, through the channel of MlaD, and into the periplasm."]
- Tang et al. 2021 [PMID:33199922, abstract only] also solved E. coli MlaFEDB with phospholipid bound
  and built a proteoliposome MlaFEDB/MlaC/MlaA-OmpF transport system.

## Transport and direction
- Disruption: PL accumulates in OM outer leaflet; SDS-EDTA sensitivity [PMID:19383799, abstract only].
- Reconstituted point-to-point assays: "PLs equilibrate between MlaC and MlaFEDB, and ATP hydrolysis drives
  overall transport in the retrograde direction." [PMID:34873038]. Combined lipid-binding cavity formed by
  MlaD and MlaE; ATP binding collapses the MlaE lipid-binding cavity [PMID:34873038].
- Direction remains debated (anterograde transfer reported by Tang et al.), so process annotation uses the
  direction-neutral GO:0120010 intermembrane phospholipid transfer.

## Curation decisions (summary)
- GO:0005515 protein binding (IPI, with MlaF/MlaD): REMOVE per protein-binding policy; complex membership
  captured by GO:0043190.
- GO:1990531 phospholipid-translocating ATPase complex: definition is a P-type ATPase (flippase) complex;
  MlaFEDB is an ABC transporter -> MODIFY to GO:0043190 ABC transporter complex.
- GO:0015914 phospholipid transport (IBA, NAS): correct but general -> MODIFY to GO:0120010 (is_a child,
  already on the gene).
- GO:0016020 membrane (NAS): MODIFY to GO:0005886 plasma membrane. The cited Tat paper (PMID:29358647)
  does not mention Mla at all; ComplexPortal mis-cited it (recorded as a WRONG_REFERENCE source defect).
- GO:0120014 phospholipid transfer activity (IDA, enables): MARK_AS_OVER_ANNOTATED (revised in PR review);
  the activity belongs to the assembled MlaFEDB complex with MlaC, so the core function records it as
  contributes_to, the same reading applied to MlaB, MlaD and MlaF.
- NEW: GO:0005543 phospholipid binding (IDA, PMID:33236984) based on cryo-EM + in vivo crosslinking.
