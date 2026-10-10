# SLC1 (YDL052C, P33333) notes

Evidence journal compiled from the UniProt record and cached publications (no paid deep research).

## Activity
- sn-2 acyl-CoA:LPA acyltransferase (LPAAT, EC 2.3.1.51) [PMID:17675291 "In yeast, it is generated from lysophosphatidic acid, which is acylated by Slc1p, an sn-2-specific, acyl-coenzyme A-dependent 1-acylglycerol-3-phosphate O-acyltransferase."]
- In slc1 lipid particles acylation stops at LPA [PMID:9401016 "the second step, acylation of lysophosphatidic acid, requires S1c1p"]
- SLC1-1 variant acylates sn-1 oleoyl-LPA in vitro [PMID:9212466 "The SLC1-1 gene product was shown in vitro to encode an sn-2 acyltransferase capable of acylating sn-1 oleoyl-lysophosphatidic acid"]
- Broad lysophospholipid acceptor range in microsomes (LPA, LPC, LPE, LPS, LPI) and reversibility on PA [PMID:26643989 "Slc1 has no detectable reverse reaction towards PtdCho substrate, but has the highest capacity of reversibility towards the PtdOH substrate of all tested enzymes."]; [PMID:17675291 "affinity-purified Slc1p displays Mg2+-dependent acyltransferase activity not only toward lysophosphatidic acid but also lyso forms of phosphatidylserine and phosphatidylinositol"]
- Redundancy: slc1 ale1(slc4) double deletion lethal [PMID:17675291 "The simultaneous deletion of SLC1 and SLC4 is lethal."]

## Location
- ER and lipid droplets [PMID:24868093 "While both Say1 and Rer2 are present and active at the LD and ER, similar to Ayr1 (60), Gpt2 (61), and Slc1 (62), not all proteins are active in all subcellular populations."]
- UniProt: Lipid droplet [UniProt:P33333]

## Curation observations
- YeastPathways RCA rows place LPAAT activity in "cytosol" (pathway default) -> MODIFY to ER membrane.
- TAG biosynthesis and CDP-DAG biosynthesis are downstream uses of PA; kept as non-core.
- Lyso-PC/PE/PS acyltransferase activities are real in vitro but secondary (Ale1 is the main remodelling enzyme).
