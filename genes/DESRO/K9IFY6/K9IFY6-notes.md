# K9IFY6 Research Notes

## Key findings
- UniProt names this protein a C-C motif chemokine [file:DESRO/K9IFY6/K9IFY6-uniprot.txt "RecName: Full=C-C motif chemokine"].
- UniProt indicates the protein is secreted [file:DESRO/K9IFY6/K9IFY6-uniprot.txt "SUBCELLULAR LOCATION: Secreted"].
- Deep research confirms K9IFY6 as a C-C motif chemokine from vampire bat [file:DESRO/K9IFY6/K9IFY6-deep-research-falcon.md "UniProt K9IFY6 corresponds to a C-C motif chemokine from Desmodus rotundus (common vampire bat)"]
- UniProt places this protein in the chemokine CC family [file:DESRO/K9IFY6/K9IFY6-uniprot.txt "Belongs to the intercrine beta (chemokine CC) family."].

## 2026-07-31 compliance review

**The protein is CCL28, and the record already says so.** The UniProt entry
cross-references `GeneID; 112315258`, `CTD; 56477`, `RefSeq; XP_024427703.1`,
and [file:DESRO/K9IFY6/K9IFY6-uniprot.txt "PANTHER; PTHR12015:SF205; C-C MOTIF
CHEMOKINE 28; 1."]. Resolving the two gene ids against NCBI Gene confirms
56477 = *Homo sapiens* CCL28 and 112315258 = *Desmodus rotundus* CCL28 (queried
2026-07-31 via `esummary.fcgi?db=gene`). The deep-research file missed this
entirely and reasoned only at the level of "some CC chemokine", which is why its
`reference_review` is `relevance: LOW`.

The EMBL record behind this accession (JAA45050.1, TISSUE=Salivary gland) comes
from the Vampirome study, now cached as PMID:23411029, which has a dedicated
CCL28 section. Key points used:

- Confirmed at both transcript and protein level in the gland: [PMID:23411029
  "In our analysis, bat salivary CCL28 was found to be abundant at the
  transcriptional (Table 4) and proteome (Figure 2A) levels."]
- Receptor usage and tissue distribution: [PMID:23411029 "CCL28 is a chemokine
  signaling via CCR10 and CCR3 that is selectively expressed in certain mucosal
  tissues such as exocrine glands, trachea, and colon."]
- Defining role: [PMID:23411029 "CCL28 is particularly abundant in SGs and plays
  an important role in mucosal immunity as a chemoattractant for IgA-producing
  plasma cells into the mucosal lamina propria"]
- Second, receptor-independent activity: [PMID:23411029 "More recently, it has
  been shown that CCL28 had a potent antimicrobial activity against Candida
  albicans, Gram-negative bacteria, and Gram-positive bacteria."] — this is
  human CCL28. The bat protein does carry the corresponding basic C-terminal
  extension (UniProt COMPBIAS 92..114 "Basic residues"), but the authors only
  hypothesise the activity: [PMID:23411029 "CCL28 may function as a
  broad-spectrum antimicrobial protein in the saliva."]. Recorded as a knowledge
  gap, **not** as a `defense response to bacterium` annotation.

Annotation calls: all 8 PENDING resolved. `GO:0007165 signal transduction` was
marked over-annotated — it is an inter-ontology logical inference from cytokine
activity, and it describes what the *responding* cell does, not what a secreted
ligand does; the content is already carried by chemokine activity + cell
chemotaxis. One `NEW` annotation proposed: `GO:0048020 CCR chemokine receptor
binding` (ISS), using the CCR-family parent rather than `GO:0031735` CCR10-
specific, since mammalian CCL28 uses both CCR10 and CCR3 and neither has been
tested for the bat protein.
