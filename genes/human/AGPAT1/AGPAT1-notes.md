# AGPAT1 notes

AGPAT1 is a compact review in `PANTHER:PTHR10434` subfamily `SF65`.
`just fetch-gene human AGPAT1` seeded 32 GOA rows, and the fetched GOA file is
not header-only.

## Family and PAINT

The existing family review for `PTHR10434` already covers the AGPAT/PlsC family
through yeast `SLC1`, fission-yeast `SPAC1851.02` and human `AGPAT2`.
AGPAT1 belongs to the alpha subfamily `PTHR10434:SF65`; human Q99943 is a seed
for the same PAINT nodes already recorded in the family review:

- `PTN000046632` for `GO:0003841` LPA O-acyltransferase activity.
- `PTN000046632` for `GO:0006654` phosphatidic acid biosynthetic process.
- `PTN000046633` for `GO:0005783` endoplasmic reticulum.

PMID:9461603 characterizes the MHC-encoded alpha paralog and reports that
hLPAAT-alpha specifically converts LPA into PA with several acyl-CoA donors and
localizes to the ER. PMID:21873652 compares AGPAT1 and AGPAT2 and reports
similar LPA/acyl-CoA substrate specificities plus ER co-localization.

## Row decisions

All `GO:0003841`, `GO:0006654`, `GO:0005783` and `GO:0005789` rows were
accepted. The `GO:0006644`, `GO:0008654` and `GO:0016024` process rows were
also accepted: AGPAT1 catalyzes the PA-forming step that belongs to those
phospholipid and CDP-DAG biosynthetic routes.

The two generic `GO:0016020 membrane` rows were marked `TOO_GENERAL` because
AGPAT1 has accepted ER-membrane rows. The broad InterPro `GO:0016746
acyltransferase activity` row was left `ACCEPT`; `IPR002123` supports the
acyltransferase fold but does not, by itself, name LPA as the acceptor.

The three bare `GO:0005515 protein binding` rows from Rolland et al. and
BioPlex screens were removed under local protein-binding policy. The cytokine
rows from PMID:9212163 were left `UNDECIDED`: the abstract reports enhanced
TNF-alpha and IL-6 transcription/synthesis after LPAAT overexpression and
IL-1beta stimulation, but the full alpha-specific experiment and the curator's
IC basis were not recovered.

Reactome `R-HSA-163748` is cached as transcriptional activation of AGPAT1 by
ChREBP:MLX and says the resulting AGPAT1 mRNA is translated to ACACB protein.
That event does not support the old AGPAT1 ER-membrane row; the row is retained
because AGPAT1 is truly in the ER membrane, and the likely intended Reactome
event is `R-HSA-75885`.

## Module and GO-CAM

No production GO-CAM in `gocams/index.tsv` names human AGPAT1 or AGPAT2. The
existing `triacylglycerol_biosynthesis` module already uses `PTHR10434` for the
LPA-acylation step with AGPAT2, SLC1 and SPAC1851.02 as reviewed exemplars. This
AGPAT1 pass leaves that module unchanged because the AGPAT1 rows support the
shared PA-forming chemistry and CDP-DAG branch, not a distinct module membership.
