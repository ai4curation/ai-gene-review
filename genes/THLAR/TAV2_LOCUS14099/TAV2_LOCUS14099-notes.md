# TAV2_LOCUS14099 (LAC4 / IRX12, A0AAU9S9S2) Curation Notes — *Thlaspi arvense*

## Orthology and Domain Architecture
- **Gene symbol / Locus**: `TAV2_LOCUS14099` (`Tarvense_20158`, protein accession `CAH2058852.1`, UniProt `A0AAU9S9S2`, 558 AA, Chromosome 4).
- **Ortholog**: Direct 1:1 pennycress ortholog of *Arabidopsis thaliana* **LAC4 / IRX12** (`AT2G38080`, `Q9SR40`, Laccase-4 / Irregular xylem 12, 558 AA).
- **Conserved Domain Architecture** ([TAV2_LOCUS14099-uniprot.txt](TAV2_LOCUS14099-uniprot.txt)):
  - `FT:SIGNAL 1..24`: N-terminal secretory signal peptide targeting the protein to the apoplast/secondary cell wall.
  - `FT:DOMAIN 33..146`, `160..307`, `409..541`: Three cupredoxin / plastocyanin-like multicopper oxidase domains (`Pfam:PF07732`, `PF00394`, `PF07731`; `InterPro:IPR017761`, `IPR002355`) coordinating four copper ions (Type 1, Type 2, and binuclear Type 3 copper centers).
  - `DR:PANTHER`: `PTHR11709:SF370` (`LACCASE-4`).

## Biological Function & miR397 Regulation of Lignification
- **Lignin Biosynthesis vs. Lignin Catabolism (InterPro2GO / RuleBase Defect)**:
  - Unreviewed TrEMBL record `A0AAU9S9S2` carries an automated RuleBase/InterPro2GO annotation to `GO:0046274` (*lignin catabolic process*) from `InterPro:IPR017761` (*Laccase*) and `RuleBase:RU361119` ("Lignin degradation and detoxification of lignin-derived products"), which was authored for wood-rotting basidiomycete fungal laccases.
  - In land plants, apoplastic laccases (`LAC4`/`IRX12`, `LAC17`, `LAC2`, `LAC15`) do **not** degrade lignin; instead, they oxidize monolignols (coniferyl and sinapyl alcohols) to phenoxyl radicals that undergo oxidative radical coupling to **polymerize/synthesize** lignin (`GO:0009809`, *lignin biosynthetic process*) in vascular secondary cell walls and seed coats ([PMID:25533953](../../../publications/PMID_25533953.md), [PMID:31559647](../../../publications/PMID_31559647.md)).
- **miR397 Target Site in Pennycress**:
  - Cross-reference of the 72 pennycress miRNA loci ([PMID:34990041](../../../publications/PMID_34990041.md)) against the `T_arvense_v2` transcriptome ([thlar_mirna_targets.tsv](../../../projects/THLAR_OILSEED/mirna_targets/thlar_mirna_targets.tsv)) shows that `TAV2_LOCUS14099` (`A0AAU9S9S2`) contains a conserved `miR397` (`tar-mir-397`, mature sequence `TCATTGAGTGCATCGTTGATG`) target site at CDS positions `669..689` (expectation score `2.5`), matching the experimentally verified Category-0 degradome cleavage site in *Arabidopsis* `LAC4`/`IRX12` (`AT2G38080.1`, `p = 0.00084` in [tardb_ath_degradome.tsv](../../../projects/THLAR_OILSEED/mirna_targets/tardb_ath_degradome.tsv)).
  - In pennycress domestication, reducing seed coat thickness and klason lignin content (analogous to *tt8* transparent testa lines) improves seed meal protein digestibility and oil extraction efficiency.

## Review of Existing GOA Annotations (5 IEA rows)
1. `GO:0052716` (*hydroquinone:oxygen oxidoreductase activity*, `IEA`) — **ACCEPT** (core laccase catalytic activity, `EC 1.10.3.2`).
2. `GO:0005507` (*copper ion binding*, `IEA`) — **ACCEPT** (core cofactor binding of multicopper oxidase).
3. `GO:0048046` (*apoplast*, `IEA`) — **ACCEPT** (core cellular component; secreted into the apoplast/cell wall via signal peptide `AA 1..24`).
4. `GO:0016491` (*oxidoreductase activity*, `IEA`) — **MODIFY** to `GO:0052716` (*hydroquinone:oxygen oxidoreductase activity*).
5. `GO:0046274` (*lignin catabolic process*, `IEA`, `InterPro:IPR017761`) — **MODIFY** to `GO:0009809` (*lignin biosynthetic process*) (corrects the fungal-laccase catabolic mis-mapping to the true plant monolignol-polymerizing biosynthetic process).
