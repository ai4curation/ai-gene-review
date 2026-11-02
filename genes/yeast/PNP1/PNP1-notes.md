# PNP1 (YLR209C) notes

UniProt Q05788, purine nucleoside phosphorylase, PNP/MTAP phosphorylase family [UniProt:Q05788].

## Activity
- Specific for inosine and guanosine [PMID:11466296 "This protein specifically metabolized inosine and guanosine."]; disruption causes excretion of these nucleosides [PMID:11466296 "Disruption of PNP1 led to inosine and guanosine excretion in the medium"].
- Phosphorolytic, not hydrolytic: Belenky 2009 purified Pnp1 "to measure the phosphorylase activity of recombinant Pnp1 and bovine Pnp on both inosine and NR" [PMID:19001417]. NR specificity constant ~9% of inosine [PMID:19001417 "yeast Pnp1 exhibited a specificity constant for NR greater than 9% of the corresponding value for inosine"]. NaR is a very poor substrate [PMID:19001417 "These data suggest that Pnp1 may play a negligible role in NaR utilization."].
- => SGD IDA rows for inosine nucleosidase (GO:0047724) and NR hydrolase (GO:0070635) from PMID:19001417 mis-type the reaction class (hydrolase vs phosphorylase). Reviewed as MODIFY; GO lacks an NR phosphorylase term (proposed NTR).

## Pathways
- NR salvage (Nrk1-independent): Urh1 > Pnp1 > Meu1 [PMID:17482543 "the Urh1/Pnp1/Meu1 pathway, which is Nrk1 independent"]; Pnp1 accounts for 25-35% of this flux [PMID:19001417].
- Ribose salvage from RNA degradation during starvation [PMID:23670538 "Thus, Pnp1 and Urh1 work in concert to convert purine and pyrimidine nucleosides into bases and ribose or ribose-1-phosphate."].
- YeastCyc RCA for PWY3O-236 (NaR salvage) is weakly supported for Pnp1 (negligible NaR activity).

## Localization
- No direct localization paper cited; soluble enzyme, cytosol by IBA/RCA.
