# nmt1 (thi3; SPCC1223.02; UniProt P36597) notes

Fetch check: `just fetch-gene SCHPO nmt1` fetched `AC   P36597;` (NMT1_SCHPO, 346 aa) - correct [UniProt:P36597].

## Naming traps
- PomBase **nmt1** ("no message in thiamine") = **thi3** = the THI5-family HMP-P synthase. It is NOT N-myristoyltransferase (human/budding-yeast NMT1); a symbol-only fetch in another organism, or a cross-species lookup by symbol, would hit the myristoyltransferase.
- The nmt1 promoter is the widely used thiamine-repressible expression system in fission yeast; most literature hits for "nmt1" concern the promoter, not the protein.

## Evidence
- Thiamine-repressible gene; disruption gives thiamine auxotrophy [PMID:2358444 "The gene product is most likely involved in thiamine biosynthesis and consistent with this is the observation that the nmt1::ura4 disruption strain is a thiamine auxotroph."]. Abstract-only.
- thi3, defined by pyrimidine requirement, is allelic to nmt1 [PMID:1868574 "Thi3, which is involved in the synthesis of the pyrimidine moiety of the thiamine molecule, is allelic to the thiamine repressible gene nmt1."].
- S. cerevisiae THI5/11/12/13 are homologues of nmt1 and redundant for HMP formation from the pyridoxine pathway [PMID:12777485 "all are homologues of the Schizosaccharomyces pombe nmt1 gene"].
- Mechanism established for C. albicans THI5: HMP-P made from PLP and an active-site histidine; single turnover [PMID:22568620 "These experiments suggest that the THI5 protein is the histidine source for HMP-P formation and that THI5p is a single turnover enzyme."]. UniProt function for P36597 is by similarity to S. cerevisiae THI5 (P43534) [UniProt:P36597].
- ORFeome YFP: cytoplasm + nucleus (PomBase EXP cytoplasm, HDA cytosol + nucleus).

## Ortholog consistency
- S. cerevisiae THI13/THI5 review core: GO:0106344, directly_involved_in GO:0009228, cytosol. Same here. S. pombe-specific difference: a single-copy gene (vs four redundant paralogs in S. cerevisiae), so nmt1 deletion alone gives auxotrophy.

## GO-CAM
- gomodel:66c7d41500000963 activity 66c7d41500000964: nmt1 enables GO:0106344, cytosol, part_of GO:0009228; thi1 and thi5 transcription activators (GO:0001228) indirectly positively regulate (RO:0002407) the nmt1 activity (transcriptional control). Consistent with module and review.
- The module's YeastPathways note that YeastCyc gives the product as free HMP; the enzyme makes HMP-P. Agree.
