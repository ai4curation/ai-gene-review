# H (Hairless; UniProt Q02308) notes

Fetched via accession (`just fetch-gene DROME Q02308 --alias H`) because the
symbol H is ambiguous with h (hairy). FlyBase FBgn0001169. No PANTHER family
line in the UniProt record; no IBA rows in GOA.

## Deep research
Falcon launched 2026-09-30; wrapper timed out at 600 s and perplexity fallback
unavailable. See end of file for final status.

## Key findings
- H directly binds Su(H) and inhibits Su(H)-driven activation
  [PMID:7958912 "We show here that H can inhibit the DNA binding of both Su(H) and RBP-J kappa through direct protein-protein interactions."]
- Adaptor recruiting Groucho and dCtBP ("default repression")
  [PMID:12154126 "Here we show that, in vitro, H directly binds two corepressor proteins, Groucho (Gro) and dCtBP."]
- Gro and CtBP needed in combination; second Gro/CtBP-independent mode antagonizing NICD
  [PMID:16287856 "Hairless has a second mode of repression that antagonizes Notch intracellular domain and is independent of Gro or CtBP binding."]
- Su(H) CTD is necessary and sufficient for H binding; Notch and H compete for CSL
  [PMID:21737682 "we demonstrate that Notch and Hairless compete for CSL in vitro and in cell culture."]
- Nucleo-cytoplasmic shuttling, Su(H) follows H localization
  [PMID:31326540 "we reveal that Su(H) protein strictly follows Hairless protein localization."]
- Recruits histone chaperone Asf1
  [PMID:17925233 "Asf1 can be coprecipitated with the DNA-binding protein Su(H) and the corepressor Hairless and interacts directly with two components of this complex, Hairless and SKIP."]
- Su(H)-independent activity in inner bristle lineage [PMID:10842054]
- ISC maintenance requires H-Su(H) repression of E(spl)-C [PMID:20147375]

## Review decisions
- Core MF GO:0003714 transcription corepressor activity; in complex GO:0090571.
- NEW GO:0001222 transcription corepressor binding (Gro/CtBP); protein binding (Asf1) MODIFIED to it.
- negative regulation of Notch signaling pathway: all accepted (core).
- Developmental processes (wing vein/margin, SOP fate, ISC) kept non-core.

## Pathway-variant notes
- Hairless is an arthropod/insect innovation; vertebrate RBPJ repression uses other corepressors (SHARP/SPEN, KyoT2 etc.).

## Deep research final status
Falcon output arrived after the wrapper timeout (`H-deep-research-falcon.md`); reviewed and cited in the review YAML.
