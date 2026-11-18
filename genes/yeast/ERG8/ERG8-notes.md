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

## 2026-11-18 correction (mevalonate-pathway cross-species campaign)

- Earlier entries above call Arabidopsis PMK (AT1G31910) "PTS1-bearing". That is wrong: the
  Arabidopsis PMK review found no PTS1, and the UniProt PTS2 feature (residues 57-65) does not match
  the PTS2 consensus (genes/ARATH/PMK/PMK-bioinformatics/RESULTS.md). Its peroxisomal location rests on
  YFP fusions in periwinkle cells [PMID:21655959 "PMK and MVD are localised to the peroxisomes, while MVK
  was cytosolic"]. The REMOVE of the inherited peroxisome IBA on yeast Erg8 is unchanged; the review text
  was corrected, and PTN000781523 is a Eukaryota-level node, not a plant sub-node. The PTHR31814 family
  review now proposes moving that IBD to the plant clade PTN008640230.
