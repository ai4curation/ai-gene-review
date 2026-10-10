# erg7 (SPAC13G7.01c, UniProt Q10231) notes

Module: `ergosterol_biosynthesis` (lanosterol synthase); S. cerevisiae ortholog ERG7 (P38604). Fetch verified: Q10231.

## Evidence
- cDNA cloned by complementing S. cerevisiae lanosterol synthase mutant [PMID:8604986 "A Schizosaccharomyces pombe cDNA encoding lanosterol synthase was cloned by"].
- Reaction (S)-2,3-epoxysqualene = lanosterol [UniProt:Q10231 "Reaction=(S)-2,3-epoxysqualene = lanosterol; Xref=Rhea:RHEA:14621,"].
- Localisation only by similarity (lipid droplet, ER membrane peripheral) plus ORFeome HTP cytosol call [PMID:16823372].

## Curation decisions
- Core location: ER membrane + lipid droplet (by orthology). Yeast ERG7 core uses lipid droplet only; PomBase GO-CAM uses ER (GO:0005783). No S. pombe-specific localisation experiment exists.
- intramolecular transferase IEA MODIFY -> GO:0000250; triterpenoid / secondary alcohol biosynthesis kept non-core; cytosol HDA kept non-core.
