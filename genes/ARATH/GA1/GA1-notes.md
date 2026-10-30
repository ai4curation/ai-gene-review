# GA1 (ent-copalyl diphosphate synthase, CPS; At4g02780; UniProt Q38802) - curation notes

- Accession check: Q38802 = KSA_ARATH, gene names GA1/CPS/CPS1/ABC33, At4g02780. Fetched by accession (`just fetch-gene ARATH Q38802 --alias GA1`).
- Falcon deep research was attempted (`just deep-research-falcon ARATH GA1`) and failed (provider exit code 1); review based on cached primary literature.

## Function
- First committed step of GA biosynthesis, GGPP -> ent-CPP (RHEA:14841, EC 5.5.1.13) [PMID:7994182 "In Escherichia coli cells that express both the Arabidopsis GA1 gene and the Erwinia uredovora gene encoding GGPP synthase, CPP was accumulated."]
- ga1-3 complemented by the cDNA [PMID:7994182 "able to complement the dwarf phenotype in ga1-3 mutants"].
- Class II cyclase chemistry (DXDD general acid) [PMID:20430888 "Class II diterpene cyclases mediate the acid-initiated cycloisomerization reaction that serves as the committed step"]; GA-specific CPS have a His switch residue [PMID:20430888 "this residue is conserved as a histidine in enzymes involved in gibberellin biosynthesis"].
- Mg2+/GGPP synergistic substrate inhibition [PMID:17384166 "Mg(2+) and GGPP exert synergistic substrate inhibition effects on CPS activity"].
- Structure: active site at beta/gamma domain interface [PMID:21602811].

## Location
- Imported and processed in pea chloroplasts [PMID:7994182]; GFP targeting to chloroplasts [PMID:11722763].
- Promoter active in provasculature of germinating seeds, spatially separate from late steps [PMID:11737781].

## Curation decisions
- terpene synthase activity (GO:0010333) and lyase activity (GO:0016829): GO places GO:0010333 under lyase activity; ent-CPP synthase (GO:0009905) is under isomerase/intramolecular lyase. Lyase REMOVED (wrong EC class); terpene synthase MODIFY -> GO:0009905.
- GA signaling TAS: over-annotation (biosynthesis is upstream of signaling).
- Mg2+ binding: non-core.
