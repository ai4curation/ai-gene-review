# ERG8 (YMR220W) notes

UniProt P24521; phosphomevalonate kinase, EC 2.7.4.2; GHMP-type (fungal/plant) PMK, unrelated to animal PMVK [UniProt:P24521].

## Evidence journal
- [PMID:1846667 "Saccharomyces cerevisiae strains that contain the ery8-1 mutation are temperature sensitive for growth due to a defect in phosphomevalonate kinase, an enzyme of isoprene and ergosterol biosynthesis."]
- Essential [PMID:1846667 "Disruption of the chromosomal ERG8 coding region by integration of URA3 or HIS3 marker fragments was lethal in haploid cells, indicating that this gene is essential."]; GAL1-ERG8 raises PMK activity 1000-fold; soluble 48 kDa protein.
- [PMID:200835 "phosphomevalonic kinase (erg 8), mevalonic kinase (erg12)"].
- C-terminus ...ETYLDK: no PTS1 [UniProt:P24521 sequence].

## Decisions
- Vacuole NAS (Hu et al. 2017 review) REMOVE: unsupported, contradicts GFP/soluble data.
- Peroxisome IBA (plant node PTN000781523, Arabidopsis AT1G31910 only) REMOVE: plant PTS1-bearing PMK; yeast Erg8 lacks PTS1 and is cytoplasmic.
- ATP binding, nucleus HDA KEEP_AS_NON_CORE. Rest ACCEPT.

## 2026-11-24: vacuole NAS query to UniProt

The is_active_in vacuole NAS row (PMID:28904410, Hu et al. 2017 review) now carries a UniProt WRONG_TERM CHECK source defect (PROBABLE). It is one of the 2022-02-18 batch UniProt made from that review on ERG10, ERG8, MVD1, ERG20 and IDI1; the ERG10 review already queries the batch, and each entry now records it. The cached PMC text of the review does not mention the vacuole, so the claim was not read in context, which is why this is a query and not a deletion request.
