# NUMB (human, P49757) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: human NUMB is the experimentally characterised reference for the HORSE/NUMB
(A0A5F5PK46) ProtNLM2 benchmark gene. No ProtNLM2 output was opened or used here.

### Deep research

`just deep-research-falcon human NUMB --fallback perplexity-lite` failed: Edison/falcon
returned `403 Forbidden` at `/auth/login`, and the perplexity-lite fallback returned
`401 insufficient_quota`. No deep-research file exists. The review was written from the
cached publications (GOA references plus cached Numb papers) and the UniProt record.

### Evolutionary grounding

- PANTHER PTHR47368 (NUMB) has three subfamilies: SF5 PROTEIN NUMB HOMOLOG (human NUMB
  P49757, mouse Numb Q9QZS3, rat Numb Q2LC84), SF4 NUMB-LIKE PROTEIN (NUMBL) and SF2
  (Drosophila numb, C. elegans num-1) [interpro/panther/PTHR47368/PTHR47368-entries.csv].
- Mouse Numb is a 1:1 ortholog in the same subfamily, so mouse experimental findings
  (radial glia, SVZ, Purkinje cell mGlu1 trafficking, cadherin association) are
  reasonable ortholog transfers, but they are mouse findings, not human ones.
- IBA nodes: PTN000132807 (cytoplasm; donors include mouse Numb and Numbl, zebrafish,
  human NUMB), PTN002599555 (basolateral plasma membrane, cytoplasmic vesicle; mouse Numb,
  zebrafish, human NUMB), PTN008318191 (positive regulation of neurogenesis; mouse and rat
  Numb and Numbl). PAINT did not propagate Notch-pathway terms; for human NUMB I propose
  Notch negative regulation from direct human evidence, not by transfer.

### Experimentally established in human (or with human NUMB)

- Endocytic adaptor at clathrin-coated pits / endosomes: "Numb localizes to endocytic
  organelles and is cotrafficked with internalizing receptors" and associates with the
  alpha-adaptin appendage [PMID:11121447 "Here, we demonstrate that Numb is an endocytic
  protein."]. Binds Eps15/Eps15R EH domains through C-terminal NPF motifs [PMID:11121447;
  PMID:23211419 "In vitro binding measurements indicated exon 9-independent Numb
  interaction with REPS1 and Eps15 EH domains."].
- AAK1 phosphorylates T102 and controls plasma membrane vs perinuclear endosome
  distribution [PMID:18657069].
- Cargo recognition of YxNxxF motifs (NPC1L1, EAAT3) and clathrin recruitment
  [PMID:24336247 "Numb, a clathrin adaptor, specifically recognized this motif and
  recruited clathrin for internalization."; PMID:27358480].
- Integrin alpha5 surface levels and cell migration in HeLa (siRNA) [PMID:19581412].
- p53 stabilisation via NUMB-p53-MDM2 tricomplex; NOTCH activity increased when NUMB is
  lost in human breast cancer [PMID:18172499].
- Reactome: NUMB activates ITCH (binds WW region) to ubiquitinate GLI1 (Hh negative
  regulation) [Reactome:R-HSA-5610735]; NUMB-L1 endocytosis [Reactome:R-HSA-443783].

### Mammalian/mouse (ortholog) findings

- Notch1 ubiquitination and NICD degradation with Itch [PMID:12682059] (mammalian Numb;
  species of construct not stated in abstract).
- Progenitor maintenance with Numbl [PMID:12410312]; radial glia adherens junctions and
  cadherin interaction [PMID:17589506]; SVZ ependymal wall integrity and neuroblast
  survival [PMID:17174898]; Purkinje cell mGlu1 internalization [PMID:26621723].

### Decisions

- Bare protein binding rows: MODIFY where the paper supports a specific MF (EH domain
  binding, clathrin-cargo adaptor activity, p53 binding, ubiquitin protein ligase binding,
  beta-catenin binding); REMOVE for screen-only rows.
- Organism-level developmental terms from mouse KOs (lateral ventricle development) marked
  over-annotated; neurogenesis/neuroblast division kept as non-core.
- `regulation of endocytosis` (IMP) modified to `clathrin-dependent endocytosis`, since
  NUMB is itself the cargo adaptor doing part of the work.
