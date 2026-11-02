# ole1 (SPCC1281.06c, UniProt O94523) notes

Fetch: `just fetch-gene SCHPO ole1` FAILED ("Could not find any UniProt ID ... for gene ole1 in SCHPO"; UniProt entry has no gene
name, only ORFNames=SPCC1281.06c). Fetched with `uv run ai-gene-review fetch-gene SCHPO ole1 -u O94523 -o genes` and moved into place.
Accession verified: ACO1_SCHPO, O94523, 479 aa.

## Evidence
- [UniProt:O94523] function by similarity to rat Scd1 (P21147): "Stearoyl-CoA desaturase that utilizes O(2) and electrons from reduced cytochrome b5 to introduce the first double bond into saturated fatty acyl-CoA substrates".
- Domains: FA_desaturase (PF00487) + fused Cyt-b5 (PF00173), like S. cerevisiae OLE1.
- Location: membrane (GFP library, PMID:10759889); ER (ORFeome HDA, PMID:16823372); cortical and perinuclear ER IDA (PMID:36799444, abstract-only).
- [PMID:36799444 "Lem2 and Bqt4 interacted with different types of lipid metabolic enzymes: Cho2, Ole1 and Erg11 for Lem2 and Cwh43 for Bqt4"].
- No S. pombe enzyme assay cached.

## GO-CAM
- gomodel:678073a900002931: ole1 enables GO:0004768 in ER membrane, part_of GO:0006636. Agrees.

## Decisions (consistent with genes/yeast/OLE1)
- Core MF GO:0004768, BP GO:0006636, ER membrane. OLE1 review also lists GO:0032896 (palmitoyl-CoA 9-desaturase) as a second core
  function from S. cerevisiae data; not added for ole1 (no S. pombe substrate data, not in GOA).
- iron binding, lipid metabolic process, membrane, oxidoreductase parent: KEEP_AS_NON_CORE. Cortical/perinuclear ER: KEEP_AS_NON_CORE.
