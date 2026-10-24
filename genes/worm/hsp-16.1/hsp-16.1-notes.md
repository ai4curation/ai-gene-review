# hsp-16.1 curation notes

UniProt P34696 (Swiss-Prot) = HSP-16.1/HSP-16.11, encoded by identical genes
hsp-16.1 (T27E4.8) and hsp-16.11 (T27E4.2). Deep research: not run (falcon
timeout; perplexity-lite unavailable).

## Gene structure / family
- hsp16-1 and hsp16-48 are head-to-head, duplicated as an inverted repeat [PMID:2632349 "One cluster contains two distinct genes, hsp16-1 and hsp16-48, arranged in divergent orientations separated by only 348 base pairs (bp). An identical pair, duplicated and inverted with respect to the first pair, is located 415 bp away."].
- Subclasses: [PMID:2632349 "Comparisons of the derived amino acid sequences show that hsp16-1 and hsp16-2 form a closely related pair, as do hsp16-41 and hsp16-48."].

## Expression
- Strictly heat-inducible [PMID:1550963 "Transcription of the hsp16-lacZ transgenes was totally heat-shock dependent and resulted in the rapid synthesis of detectable levels of beta-galactosidase."].
- Hypoxia-responsive (unlike hsp-16.41/48) [PMID:15522291 "The hsp-16.1 and hsp-16.2 genes in Caenorhabditis elegans responded to hypoxia"].

## Function
- Holdase: inferred from paralogue HSP-16.2 [PMID:9305934 "both wild-type and C-terminally-truncated HSP16-2 can function as molecular chaperones by suppressing the thermally-induced aggregation of citrate synthase"]. GO:0140309 rows MODIFY -> NTR holdase chaperone activity (as hsp-16.2).
- Golgi / PMR-1 / heat stroke [PMID:22972192 "HSP-16.1 localizes to the Golgi, where it functions with the Ca(2+)- and Mn(2+)-transporting ATPase PMR-1 to maintain Ca(2+) homeostasis under heat stroke."]. No NEW process added: abstract-only, and the precise role (chaperone of PMR-1 vs regulator) is not established.
- Abeta co-IP of HSP-16s [PMID:12089340 "Mass spectrometry analysis of proteins that specifically coimmunoprecipitate with A beta has identified six likely chaperone proteins"].
- Immunity requirement (IGI, PMID:16916933) kept as non-core.

## Note on protein refolding IBA
hsp-16.2 review REMOVEd this IBA; here KEEP_AS_NON_CORE (sHSPs contribute the
holding step upstream of HSP70 refolding; PAINT node not contradicted).
