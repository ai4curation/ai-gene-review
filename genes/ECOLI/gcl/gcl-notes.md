# gcl (P0AEP7) glyoxylate carboligase, E. coli K-12: curation notes

## Deep research

- `just deep-research ECOLI gcl --provider perplexity` was attempted (2026-10-23) and failed:
  "Provider 'perplexity' not available. Available: falcon, openscientist". No deep-research
  file was generated; this review is based on the cached primary literature, UniProt, and
  the PTHR18968 family review.

## Function

- Reaction: 2 glyoxylate -> tartronate semialdehyde + CO2 (EC 4.1.1.47).
  [PMID:8440684 "catalyzes the condensation of two molecules of glyoxylate to give tartronic semialdehyde, a key intermediate in glyoxylate catabolism."]
- ThDP enzyme with an unusual active site: Val replaces the conserved Glu that contacts N1' of ThDP.
  [PMID:18176558 "The crystal structure of glyoxylate carboligase challenges this paradigm by revealing that valine replaces the conserved glutamate."]
- Related to AHAS and pyruvate oxidase; ThDP and FAD binding sites.
  [PMID:8440684 "Gcl contains a quinone binding site as well as binding site for thiamine pyrophosphate and FAD."]
- Not an AHAS-like two-subunit enzyme: [PMID:8440684 "Orf258 does not function as a Gcl subunit."]
  UniProt: homotetramer; Mg2+ and ThDP cofactors (by similarity).
- Pathway: first enzyme of the glycerate pathway (Gcl -> GlxR -> glycerate kinase -> 3-PGA).
  [PMID:10601204 "This central pathway requires the action of glyoxylate carboligase, which forms tartronic semialdehyde"]
- Genetics: gcl mutants cannot oxidize glyoxylate.
  [PMID:4892366 "Organisms blocked in the synthesis of glyoxylate carboligase did not oxidize glyoxylate at a detectable rate"]
- Regulation: gcl promoter induced by glyoxylate and allantoin (anaerobic); AllR represses.
  [PMID:10601204 "φ( gcl-lacZ ) showed inducible expression with glyoxylate and allantoin under anaerobic conditions"]

## Annotation decisions

- Core: GO:0009028 tartronate-semialdehyde synthase activity; GO:0009436 glyoxylate catabolic process.
- ThDP binding and Mg2+ binding accepted as integral cofactor binding.
- FAD binding (IDA GO:0071949) kept non-core; IBA GO:0050660 refined (MODIFY) to GO:0071949.
  The role of FAD in this non-redox reaction is unclear (left as a suggested question).
- REMOVE IBA acetolactate synthase complex and L-valine biosynthesis (AHAS over-propagation
  via PTN000438758; consistent with interpro/panther/PTHR18968/PTHR18968-review.yaml).
- Glycolate catabolic process kept non-core (Gcl acts on glyoxylate; glycolate is one source).
- Identical protein binding (homotetramer) kept non-core.
- Kaplun 2008, Ornston 1969 and Chang 1993 are abstract-only in cache; experimental rows
  from them were deferred to the curators.
- Web check: later structures (PDB 8I01/8I05/8I07/8I08, 2023) exist from enzyme-engineering
  work on formaldehyde/glycolaldehyde condensation; not used as evidence here.
