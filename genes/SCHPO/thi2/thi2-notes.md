# thi2 (nmt2; SPBC26H8.01; UniProt P40998) notes

Fetch check: `just fetch-gene SCHPO thi2` fetched `AC   P40998; O74785;` (THI4_SCHPO, 328 aa) - correct accession [UniProt:P40998].

## Naming trap
- PomBase **thi2** = **nmt2** = the THI4-type thiazole synthase (UniProt entry name THI4_SCHPO). S. pombe has its own **thi4** (SPAC23H4.10c), which is the bifunctional hydroxyethylthiazole kinase / thiamine-phosphate synthase (S. cerevisiae THI6 equivalent), not the THI4 orthologue. Budding-yeast THI2 is a transcription factor; unrelated.
- Historical: Schweingruber 1991 defined complementation groups thi2, thi3 (=nmt1) and thi4 [PMID:1868574 "The genes thi2, thi3 and thi4 control thiamine biosynthesis and probably code for thiamine biosynthetic enzymes."].

## Evidence
- UniProt (HAMAP MF_03158): single-turnover ADP-thiazole synthase using NAD+ and glycine, sulfur from own cysteine (Cys-215 in pombe), Fe-dependent, homo-octamer [UniProt:P40998 "Catalyzes the conversion of NAD and glycine to adenosine diphosphate 5-"].
- nmt2 disruption causes thiamine auxotrophy; thiamine-repressible, co-regulated with nmt1 [PMID:7992507 "Disruption of nmt2 also resulted in thiamine auxotrophy, indicating a role for the nmt2 gene product in thiamine biosynthesis."]. Abstract-only.
- PomBase IMP to thiazole biosynthetic process from PMID:1868574 (abstract-only; abstract assigns thi3 to the pyrimidine branch; the thiazole assignment of thi2 presumably comes from the full text, e.g. supplementation tests). Defer to curator.
- ORFeome YFP: cytoplasm and nucleus (PomBase HDA cytosol + nucleus) [UniProt:P40998 "ECO:0000269|PubMed:16823372}. Nucleus"].
- PomBase phenotype: thiamine auxotroph (PomBase API).
- Ortholog biochemistry (S. cerevisiae THI4): suicide enzyme, iron-dependent sulfide transfer [PMID:22031445 "These observations suggested that the THI4p catalyzed sulfur incorporation reactions are iron-dependent."].

## Ortholog consistency
- S. cerevisiae THI4 review core: GO:0160205; directly_involved_in GO:0052837 + GO:0009228; cytosol. Iron binding rows kept non-core; pentosyltransferase MODIFY -> GO:0160205; nucleus non-core. Followed identically here. No S. pombe-specific divergence.
- The UniProt "May have additional roles in adaptation to various stress conditions and in DNA damage tolerance" line is HAMAP text from plant/fungal THI4 homologs; no S. pombe evidence.

## GO-CAM
- gomodel:66c7d41500000963 activity 66c7d41500001022: thi2 enables GO:0160205, occurs_in cytosol, part_of GO:0009228. Consistent with module (THI4 step) and this review.
- Also appears in gomodel:698e557b00000821 (NAD+ biosynthetic process model) with the same activity (gocams/index.tsv), presumably as an NAD+ consumer. Not reviewed further.
