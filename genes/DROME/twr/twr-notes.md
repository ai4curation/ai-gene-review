# twr review notes

UniProt O97066 (Signal peptidase complex catalytic subunit SEC11); peptidase S26B; PANTHER PTHR10806. Called Spase18/21 in PMID:23573290.

## Literature journal

- Fly SPC composition [PMID:23573290 "The Drosophila SPC comprises four proteins: Spase18/21, Spase22/23, Spase25 and Spase12."]
- SPC role [PMID:23573290 "A vital component of the translocation machinery is the signal peptidase complex (SPC)--which is conserved from yeast to mammals--and functions to cleave the signal peptide sequence (SP) of secretory and membrane proteins entering the ER."]
- No twr-specific experimental study is cached; HDA rows come from organelle proteomics (PMID:19317464) and serine hydrolase activity profiling (PMID:33827210), both abstract-only here.

## Curation decisions (SPC module, applied to twr, Spase12, Spase22-23, Spase25)

- GO:0005787 signal peptidase complex ACCEPTED for all subunits; GO:0005789 ER membrane ACCEPTED; membrane / endomembrane system / ER -> MODIFY to ER membrane.
- GO:0051604 protein maturation -> MODIFY to GO:0016485 protein processing (GO:0006465 signal peptide processing is obsolete and was redirected to protein maturation; protein processing is the more specific valid child).
- IBA protein targeting to ER -> REMOVE (SPC acts after targeting), as in the human SPCS1-3 reviews.
- twr: signal peptidase activity is the core MF; peptidase activity -> MODIFY to signal peptidase activity; serine hydrolase activity -> MODIFY to serine-type endopeptidase activity (kept, mechanism term). Accessory subunits: contributes_to signal peptidase activity.

## Deep research

`just deep-research-falcon` had not produced a report when this review was committed; any late-arriving report will be added in a follow-up commit.
