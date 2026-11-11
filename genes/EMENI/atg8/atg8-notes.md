# EMENI/atg8 manual review notes

## Scope and source availability

Provider deep research was unavailable in this sparse worktree because the
configured deep-research providers require credentials that were not present. I
used the seeded GOA review, the cached UniProt flat file, the cached PTHR10969
PAINT rows, the full-text cached 2013 Aspergillus nidulans GFP-Atg8 paper, and
a PubMed/Europe PMC search for direct or newer A. nidulans Atg8/autophagy
papers.

## PANTHER/IBA assessment

PTHR10969 is a compact ATG8/LC3/GABARAP family. The A. nidulans Atg8 protein
Q5B2U9 is a 118-aa fungal ATG8 member in the same family as S. cerevisiae ATG8,
S. pombe atg8, Candida albicans ATG8 and Aspergillus fumigatus atg8.

The main PAINT node `PTN000103522` is the eukaryotic ATG8/LC3/GABARAP node. It
places the inherited Atg8 claims to `GO:0000045` autophagosome assembly,
`GO:0000421` autophagosome membrane, `GO:0008429`
phosphatidylethanolamine binding, `GO:0000423` mitophagy, `GO:0006995`
cellular response to nitrogen starvation and `GO:0097352` autophagosome
maturation. These rows are plausible for A. nidulans: Pinar et al. directly
followed GFP-Atg8 from PAS puncta into phagophores and autophagosomes, and the
Swiss-Prot record retains the conserved mature glycine that is lipidated with
phosphatidylethanolamine [PMID:23722157, "Initially, GFP-Atg8 puncta give rise
to expanding phagophores engulfing a portion of cytoplasm."].

The fungal-specific `PTN000861115` node places `GO:0000329` fungal-type vacuole
membrane from S. cerevisiae and S. pombe Atg8 evidence. This is a sound PAINT
transfer for A. nidulans Atg8 because this is a fungal member of PTHR10969.
Direct GFP-Atg8 proteolysis shows delivery into the vacuolar lumen rather than
stable vacuolar-membrane action [PMID:23722157, "GFP accumulation following
vacuolar GFP-Atg8 proteolysis is a bona fide indicator of autophagy"].

## Cached Publication Findings

Pinar et al. 2013 is the key direct cell-biological paper for A. nidulans Atg8.
It established GFP-Atg8 as a PAS/phagophore/autophagosome marker during
nitrogen starvation, showed Atg8-positive puncta give rise to expanding
phagophores, and used GFP-Atg8 processing as a vacuolar delivery assay
[PMID:23722157, "Initially, GFP-Atg8 puncta give rise to expanding
phagophores engulfing a portion of cytoplasm."].

Katz et al. 2015 compared starvation responses in `atgA`, the ATG1 ortholog,
and `atgH`, the ATG8 ortholog. The cached abstract is enough to show that the
ATG8 ortholog was directly assayed under carbon- and nitrogen-limiting
conditions, but full text would be needed for detailed mutant interpretation
[PMID:26296599, "Compared to wild-type strains and the xprGΔ and xprG1
mutants, conidiation of the autophagy mutants was reduced in carbon- or
nitrogen-limiting conditions but not during growth on nutrient-sufficient
medium."].

Balasubramanian and Osmani 2025 imaged GFP-Atg8 with Tom20-mRFP and found
mitophagy during nitrogen-limited A. nidulans biofilm formation. The paper
corroborates the inherited mitophagy row, but it does not add a specific
Atg8 molecular activity beyond the conserved autophagic membrane role
[PMID:40860045, "The data confirm the accumulation of GFP-Atg8 and Tom20-mRFP
signals in vacuoles results from autophagy/mitophagy during biofilm development
in nitrogen-limiting media."].

Pinar et al. 2026 localized TRAPPC11 and TRAPPC12 to Atg8-positive
preautophagosomes and refined how A. nidulans TRAPPIII is recruited to
autophagy. This is upstream of Atg8 but confirms continued use of Atg8 as a PAS
marker in direct A. nidulans autophagy experiments [PMID:42483769,
"TRAPPC11 and TRAPPC12 localize to pre-autophagosomes and their ablation
impairs autophagy."].

## 2024-2026 PubMed/Europe PMC Search

Searched PubMed and Europe PMC for:

- `(atg8 OR AN5131) AND ("Aspergillus nidulans" OR "Emericella nidulans")`
- `("Aspergillus nidulans" OR "Emericella nidulans") AND autophagy AND
  2024:2026`
- `Atg8 AND Aspergillus AND 2024:2026`

The 2024-2026 A. nidulans hits were Pinar et al. 2026 on TRAPPIII targeting,
Balasubramanian and Osmani 2025 on nitrogen-limited biofilm mitophagy, and a
2024 tyrosol transcriptomics paper. The first two are useful pathway context;
neither supports adding a new EMENI/atg8 GO process beyond the seeded PAINT and
UniProt rows. The broader 2024-2026 `Atg8 AND Aspergillus` search mostly found
other Aspergillus species or mammalian LC3-associated phagocytosis work, with
no A. nidulans Atg8 curation change.
