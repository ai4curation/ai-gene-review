# SLC27A5 (donkey, Equus asinus) - A0A9L0JNL2

DONKEY40 cohort review. Unreviewed TrEMBL entry, 700 aa, "long-chain-fatty-acid--CoA ligase" (ARBA name); PANTHER PTHR43107:SF25 (LONG-CHAIN FATTY ACID TRANSPORT PROTEIN 5).

## Sources
- Donkey UniProt `SLC27A5-uniprot.txt` (ARBA catalytic activities; AMP-binding domain; PROSITE AMP_BINDING).
- Donkey GOA `SLC27A5-goa.tsv`: 14 IEA rows (3 TreeGrafter GO_REF:0000118, combined GO_REF:0000120, Ensembl Compara GO_REF:0000107).
- Human ortholog review exists: `genes/human/SLC27A5/` (used for consistency; human UniProt file:human/SLC27A5/SLC27A5-uniprot.txt).
- Cached: PMID:10479480, PMID:10749848, PMID:11980911 (human enzyme characterization; abstract-only).

## Sequence
- 81.30% identity to human over 690 aligned residues, full human coverage; 10-residue N-terminal extension [file:EQUAS/SLC27A5/SLC27A5-bioinformatics/RESULTS.md].

## Biology
- Cholate:CoA ligase [PMID:10749848 "exhibited cholate:CoA ligase (choloyl-CoA synthetase) activity with both"].
- Activates chenodeoxycholate, deoxycholate, lithocholate and THCA; main role in recycling C24 bile acids [PMID:11980911 "We hypothesize that the primary function of homolog 2 is in the reactivation and recycling of C24 bile acids"].
- LC/VLC acyl-CoA synthetase; ER-associated [PMID:10479480 "For all substrates tested (C18:0, C20:0, C24:0, C26:0)"; "the protein was associated with the endoplasmic reticulum but not with"].
- Hepatic fatty acid uptake, by similarity to mouse [human UniProt].

## Decisions
- ACCEPT: LC-CoA ligase, VLC-CoA ligase, cholate-CoA ligase, LCFA and VLCFA metabolic process, bile acid metabolic process, ER, ER membrane.
- KEEP_AS_NON_CORE: plasma membrane, basal plasma membrane, LCFA import into cell, LCFA transmembrane transporter activity, bile acid biosynthetic process (main role is recycling; human review ACCEPTs this term - a deliberate difference in emphasis, not a contradiction).
- TOO_GENERAL: fatty acid transmembrane transporter activity (parent of the LCFA transporter term).

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not opened or used. Deep research: `just deep-research-falcon EQUAS SLC27A5 --fallback perplexity-lite` failed (falcon "Failed to authenticate"; perplexity HTTP 401 insufficient_quota), so no deep-research file exists; this re-review uses the cached literature plus two newly cached mouse knockout papers.

### Identity
- A0A9L0JNL2 (700 aa) is the full-length donkey SLC27A5 product, not a fragment or isoform: one ungapped block covers all 690 human residues (81.3% identity) [file:EQUAS/SLC27A5/SLC27A5-bioinformatics/RESULTS.md]. Pfam AMP-binding (130-453) and AMP-binding_C (576-652) and PROSITE PS00455 are present.
- The 10-residue N-terminal extension (MDISQGEAGA) is shared by the horse models A0A5F5PXH2 (700 aa) and F6X2Q2 (UniProt REST query, gene_exact:SLC27A5, 2026-10-21); human, mouse and cow start at the residue aligned to donkey Met11. Likely an equid gene-model start choice; not functionally relevant.
- UniProt SignalP calls 1..31 a signal peptide; in the orthologs this hydrophobic N-terminal segment is the ER membrane anchor, so it is probably not cleaved.

### Evolutionary grounding
- PANTHER PTHR43107:SF25 (LONG-CHAIN FATTY ACID TRANSPORT PROTEIN 5), the same subfamily as human Q9Y2P5, mouse Q4LDG0 and rat Q9ES38 (interpro/panther/PTHR43107/PTHR43107-entries.csv). No disagreement on subfamily placement; no FamilyReview exists for PTHR43107 (only the PAINT/entries/metadata files).
- PAINT (PTHR43107-paint.tsv): GO:0008206 IBD at PTN008678717 (seeds SLC27A2 and SLC27A5); GO:0005324, GO:0004467, GO:0001676, GO:0044539, GO:0005886 IBD at root PTN001945407; GO:0005789 at PTN001186241 (seed includes Q9Y2P5). NOT (IRD) transporter/import only in the SLC27A3 clade (PTN008678715). The donkey TreeGrafter rows (PTN009166993) are consistent with these.

### New literature (mouse ortholog, same subfamily)
- Doege 2006 [PMID:16618416 "localized to the basal plasma membrane of hepatocytes, congruent with a role in LCFA uptake from the circulation"; "FATP5 deletion significantly reduced LCFA uptake by hepatocytes isolated from FATP5 knockout animals"].
- Hubbard 2006 [PMID:16618417 "the majority of gallbladder bile acids was unconjugated, and only a small percentage was conjugated"; "suggesting a specific requirement for FATP5 in reconjugation of bile acids during the enterohepatic recirculation"]. Obesity resistance is a downstream phenotype and is not used.

### Changes from the earlier review
- GO:0008206 bile acid metabolic process: ACCEPT -> MODIFY to GO:0002152 bile acid conjugation (is_a GO:0008206; GO definition comment names cholate-CoA ligase activity as the first step, so SLC27A5 performs a step of the process). Comparator: only BAAT carries GO:0002152 in the repo GOA files; raised as a suggested question. Core function process updated accordingly.
- GO:0005783 endoplasmic reticulum: ACCEPT -> TOO_GENERAL (ER membrane accepted; the old reason argued it was the less specific term).
- GO:0005886 plasma membrane: KEEP_AS_NON_CORE -> TOO_GENERAL (basal plasma membrane, a part_of descendant, retained as non-core with mouse evidence).
- Added mouse knockout support to basal plasma membrane, LCFA import into cell and bile acid biosynthetic process rows. All other actions unchanged after re-examination.

### Relative
- Human SLC27A5 (Q9Y2P5), ortholog in the same SF25 subfamily; genes/human/SLC27A5 has all 40 GOA rows reviewed (status field still INITIALIZED). Modules mentioning SLC27A5: modules/bile_acid_biosynthesis.yaml, modules/bile_acid_synthesis_sidechain_conjugation.yaml, modules/bile_acid_synthesis_ring_modification.yaml.
