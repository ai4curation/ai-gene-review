# ATG8 review notes

Manual review date: 2026-10-21

## Core biology

Atg8 is the yeast member of the eukaryotic ATG8 family. It is synthesized with a
C-terminal Arg117, processed by Atg4 to expose Gly116, and then conjugated
through Gly116 to phosphatidylethanolamine by the Atg7/Atg3 conjugation
machinery. Ichimura et al. established that Apg8/Atg8 is covalently conjugated
to PE through the C-terminal glycine and that this lipidation is necessary for
autophagic membrane dynamics (PMID:11100732). Nakatogawa et al. showed that the
Atg8-PE form can tether and hemifuse membranes and connected that activity to
autophagosomal membrane expansion in vivo (PMID:17632063).

Atg8 has two linked autophagy functions:

- The lipidated protein is a PE-linked membrane factor at the phagophore,
  autophagosome, and Cvt vesicle membrane, where it drives membrane tethering,
  hemifusion, expansion, and later autophagosome maturation.
- Atg8 also supplies the ATG8-family docking surface on those membranes for
  Atg8-interacting proteins, including Cvt cargo receptors and selective
  autophagy receptors.

The general autophagosome-assembly and autophagosome-maturation annotations are
therefore core. Cvt, mitophagy, ER-phagy, nucleophagy, and protein targeting to
the vacuole by autophagy are direct uses of the same Atg8 membrane platform, not
separate enzymatic activities.

## PAINT and IBA rows

`interpro/panther/PTHR10969/PTHR10969-paint.tsv` places the conserved ATG8
autophagy terms on `PANTHER:PTN000103522`, a eukaryotic ATG8-family node:

- `GO:0000421` autophagosome membrane
- `GO:0008429` phosphatidylethanolamine binding
- `GO:0000045` autophagosome assembly
- `GO:0000423` mitophagy
- `GO:0006995` cellular response to nitrogen starvation
- `GO:0097352` autophagosome maturation

Those placements are appropriate for Saccharomyces ATG8. The seed lists include
the yeast target itself for several terms, which is expected for PAINT because
the yeast experimental annotation contributes descendant evidence for the IBD
node rather than making the subsequent IBA circular.

The same PAINT file also places `GO:0000329` fungal-type vacuole membrane on
`PANTHER:PTN000861115`, a fungal node supported by PomBase `SPBP8B7.24c` and
SGD `S000000174`. I kept that IBA as valid but non-core: it reflects real
fungal Atg8 vacuolar-membrane behavior, now corroborated by the Hfl1-dependent
early-stationary-phase vacuolar membrane protein turnover described by He et al.
(PMID:34088313), rather than the primary phagophore/autophagosome location.

I did not challenge any IBA because of short `WITH/FROM` lists or because ATG8
appears among the source entities. No PTHR10969 IBA row showed an ATG8-specific
loss, a fungal/eukaryotic taxon mismatch, or an unsafe PAINT node placement.

## Cached publication review highlights

Key cached papers used to review the seeded GOA rows:

- PMID:10525546: localized Apg8/Aut7 to autophagosomes and intermediates in
  autophagosome formation, supporting autophagosome localization.
- PMID:10837468: reported genetic and physical links between Aut7/Atg8 and
  SNARE-dependent ER-to-Golgi and vacuolar traffic. The full text is not in the
  cache; I retained these curator-reviewed experimental rows as secondary.
- PMID:11100732: established Atg8 phosphatidylethanolamine conjugation through
  the C-terminal glycine.
- PMID:11149920: showed Aut7/Atg8 membrane recruitment in autophagy and Cvt
  requires the Atg conjugation machinery.
- PMID:17632063: showed Atg8-mediated membrane tethering and hemifusion and
  linked that biochemical activity to autophagosome expansion.
- PMID:19398890: mapped the Atg19/cargo-receptor-binding face on Atg8 and tied
  that interface to Cvt, cargo sorting, Atg8 lipidation, and vesicle formation.
- PMID:19793921: identified ATG8 in a genome-wide screen for mutants defective
  in selective mitochondrial autophagy.
- PMID:22652539: showed Atg4-mediated deconjugation of Atg8-PE supports both
  early Atg8 supply and late maturation of fusion-capable autophagosomes.
- PMID:22885598: established direct binding between Atg8 and Atg1/ULK1 and
  showed that it controls Atg1 autophagic targeting.
- PMID:23549786: mapped Atg8 to the VICS and cup-shaped isolation membrane.
- PMID:24705553: showed that cargo-activated Atg19 uses multiple Atg8-binding
  sites to bring cargo against Atg8-positive membranes during Cvt.
- PMID:26040717 and PMID:26181331: support Atg8-dependent ER-phagy, with
  Atg39/Atg40 receptors and macro-ER-phagy using canonical Atg machinery.
- PMID:28003432: supports the non-core, autophagy-independent lipid droplet
  role of Atg8.
- PMID:31616012: supports non-core regulation of vacuolar membrane invagination
  by Atg8.
- PMID:34088313: supports non-core Hfl1-dependent recruitment of Atg8 to the
  vacuolar membrane for early-stationary-phase turnover.

Most `GO:0005515 protein binding` rows were real S. cerevisiae interactions or
large-scale physical-interaction calls, but the term itself is uninformative for
Atg8. Five rows from ParkinsonsUK-UCL or IntAct transfer human or mammalian
LC3/GABARAP receptor interactions onto yeast ATG8; those were also removed, but
as wrong-species transfers rather than as SGD yeast Atg8 interactions.
Mechanistic yeast interaction evidence was retained through process-level
annotations such as Cvt, ER-phagy, Atg1 targeting, and autophagosome assembly.

## 2024-2026 literature search

Manual PubMed/open-web searches for `Saccharomyces ATG8 2024 2025 2026`,
`yeast Atg8 mitophagy 2024`, `yeast Atg8 vacuole 2025`, and similar queries
found recent papers that refine regulatory context but do not change the GO
decisions above:

- PMID:38843068 (2024) quantified multiple non-selective and selective
  autophagy routes across yeast atg mutants and found that Atg8-system mutants
  retain some nonselective, Cvt, and pexophagy activity but have undetectable
  mitophagy and ER-phagy in those assays.
- PMID:40294649 (2025) identified Rsa1 as an Atg8-interacting receptor for
  starvation-induced selective ribophagy.
- PMID:40568955 (2025) connected Atg8 and TORC1 activities, suggesting both
  lipidation-dependent and Hfl1-related lipidation-independent Atg8 functions
  in survival during impaired TORC1 activity.
- PMID:40945725 (2025) implicated Atg8 in TOR-regulated vacuolar delivery of
  active GPCR during the yeast mating pathway.
- PMID:41584683 (2026) reported that Sir2 limits stationary-phase selective
  autophagy by stabilizing Ume6 and reducing ATG8 transcription.

None of these newer papers adds a better GO term for ATG8 than the supported
core autophagy, selective-autophagy, vacuolar, or receptor-docking annotations
already present in GOA, so I did not cache them or cite them in the curated YAML.
