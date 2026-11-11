# IRAK3 (horse, F6QZW8) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

This is a new review of the Ensembl-canonical horse IRAK3 product F6QZW8 (614 aa, ENSECAT00000029063, RefSeq XP_023499869.1). It is filed under the `IRAK3__F6QZW8` folder because `genes/HORSE/IRAK3/` holds the review of the non-canonical gene model A0A3Q2HDT6 from the same Ensembl gene, ENSECAG00000026958. No ProtNLM2 output was consulted.

### Deep research

`just deep-research-falcon HORSE IRAK3__F6QZW8 --fallback perplexity-lite` failed. Falcon gave "Exception: Failed to authenticate" and Perplexity returned HTTP 401 for insufficient quota, so no deep-research file exists. The review relies on the cached primary literature on human and mouse IRAK-M and on the existing human review (`genes/human/IRAK3/`).

### Evolutionary grounding

- UniProt places F6QZW8 in PANTHER PTHR24419:SF7 (IRAK3), the subfamily of human IRAK3 Q9Y616. VGNC:19127 names it as the horse IRAK3 gene. Over the full human length the two proteins are 81.4% identical. Mouse Irak3 Q8K4B2, the knockout donor of most Ensembl Compara IEAs, is 76.2% identical to human. [RESULTS.md](IRAK3__F6QZW8-bioinformatics/RESULTS.md); `map_human_features.py`; `features.json`.
- PAINT nodes behind the IBAs:
  - PTN002815516 (IL-1-mediated signaling). Its donors are human IRAK3 and mouse Irak3 (MGI:1921164, which resolves to Irak3 in UniProt), so the node sits at or just above IRAK3 itself.
  - PTN000701353 (LPS signaling, Toll signaling, plasma membrane). This is the IRAK/Pelle clade, with donors Irak1, Irak2, IRAK1, IRAK3 and Drosophila Pelle/Tube.
  - PTN008405164 (positive regulation of canonical NF-kB). IRAK clade, with donors Irak1, Irak2, Irak3, IRAK1 and IRAK4.
  - PTN000784925 (cytoplasm, nucleus, intracellular signal transduction). A deep kinase-superfamily node.
- PAINT did **not** propagate protein kinase activity to IRAK3. That choice is consistent with the pseudokinase active site. The kinase-activity IEAs (Compara/ARBA) are removed.

### Conservation of experimentally mapped residues

Every human/mouse functional residue tested is conserved in F6QZW8:

- death-domain W74 → W79 (MyD88/IRAK4 surface) and R97 → R102 (IRAK1/TRAF6)
- CGS catalytic loop (296-298) and DFA Mg loop (316-318)
- glycine-rich loop and ATP lysine K197
- the two dimer-interface cysteines C202/C287 → C207/C292 (mouse lacks C202)
- the TRAF6-binding region SIPVEND

The exception is human Ser110, the IRAK1 phosphosite recognised by PIN1, which is Asn115 in horse (Thr in mouse). For that reason the IL-33/PIN1 nuclear-translocation function and IL-33 pathway terms were not transferred.

### Decisions

- REMOVE: magnesium ion binding, protein kinase activity, protein serine/threonine kinase activity (pseudokinase, DFA/CGS).
- ACCEPT (core, inferred): negative regulation of TLR signaling, negative regulation of protein-containing complex disassembly, negative regulation of canonical NF-kB, protein kinase binding, protein homodimerization, IL-1- and LPS-mediated signaling, cytoplasm, and the negative-regulation-of-cytokine-production and endotoxin-tolerance terms.
- MODIFY: signal transduction and intracellular signal transduction → MyD88-dependent TLR signaling; cytokine-mediated signaling → IL-1-mediated signaling only (no IL-33); regulation of NF-kB → both directional terms; regulation of complex disassembly → negative; regulation of innate immune response → negative; MAPK cascade → p38MAPK; negative regulation of cytokine-mediated signaling → negative regulation of IL-1-mediated signaling.
- MARK_AS_OVER_ANNOTATED: Toll signaling pathway (Drosophila pathway term), response to virus, positive regulation of immune system process.
- No NEW terms. Every function in the core set already has an inferred row.

None of these functions has been tested experimentally in horse. Every positive call is a transfer resting on SF7 membership, the PAINT nodes and residue conservation. When this review serves as a reference for transfer, treat it as an inferred reference, not an experimental one.

### Curation follow-ups (not knowledge gaps)

- The PTHR24419 family review (`interpro/panther/PTHR24419/PTHR24419-review.yaml`) uses A0A3Q2HDT6 as the horse SF7 representative. F6QZW8 is the canonical product and the entry that carries the PAINT IBAs, so it would be the better representative. The family file was left untouched because it is outside this task's scope.
