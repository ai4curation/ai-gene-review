# YWHAE notes

## Workflow

- Seeded `YWHAE-ai-review.yaml`, `YWHAE-goa.tsv`, and `YWHAE-uniprot.txt` with the
  shared retained runtime rather than a local `.venv`.
- Warmed the publication cache for all PMID references listed in the seeded review.
- Attempted Falcon deep research with Perplexity Lite fallback via
  `scripts/deep_research_wrapper.py`; the cached client reported only the Claude Code
  provider as available, so no provider-authored deep-research file was written.
- Created `YWHAE-deep-research-manual.md` from the cached publications, UniProt record,
  and the GO-CAM context.
- Ran `gene_paint_losses` for `human YWHAE`: no IRD or IKR loss lies on the YWHAE
  lineage.

## Curation summary

- The review keeps the conserved 14-3-3 activities as core: phosphoserine motif
  recognition, dimerization, client sequestration, and signaling adaptor activity.
- All bare `GO:0005515 protein binding` rows were removed under the project
  protein-binding policy. This does not dispute the physical interactions; it avoids
  representing hundreds of IntAct client rows as independent molecular functions.
- Client-specific rows were kept when the paper assayed an interpretable 14-3-3
  mechanism: RIG-I translocon assembly, RNF115 recruitment to ER/Golgi, HSF1 and TAZ
  sequestration, hnRNP C export, HDAC4/5 binding, CDC25C inhibition, NDEL1/LIS1
  neuronal migration control, HERG/KCNH2 channel regulation, and PMCA1/PMCA3 pump
  regulation.
- The two PMCA molecular-function rows were changed from calcium-channel regulation to
  `GO:0042030 ATPase inhibitor activity`: PMCA1 and PMCA3 are plasma-membrane
  Ca2+-transporting P-type ATPases, not calcium channels, and 14-3-3 epsilon inhibits
  both pumps.
- Two imported UniProt GOA rows carry wrong references. PMID:1266503 is a 1976
  anti-brain-antibody paper and does not support the YWHAE-NRIP1 protein-binding row;
  PMID:12042314 is a p27Kip1 paper and does not support the YWHAE melanosome row.
  These are recorded as `WRONG_REFERENCE` source defects while the duplicate
  PMID:17081065 melanosome row remains supported.
- Rows from broad high-throughput surveys were marked over-annotated when the source was
  only recovery in an mRNA-binding, exosome, focal-adhesion, cadherin, Parkin AP-MS, or
  substantia-nigra proteomics dataset.

## GO-CAM 65692e7e00001822 consistency

- The model's YWHAE activity uses `GO:0035591 signaling adaptor activity`, `part_of`
  `GO:0070972 protein localization to endoplasmic reticulum`, and `occurs_in`
  `GO:0005783 endoplasmic reticulum`. All three are kept in this gene review, so the
  activity is consistent with the review at the GO term level.
- The model still over-specifies the 14-3-3 paralog. PMID:35343654 identified theta,
  eta, zeta, epsilon, gamma and beta 14-3-3 proteins as RNF115 interactors and treated
  the chaperone function as family-level. The final GO-CAM consistency PR should retain
  the existing note that a 14-3-3 entity set would express the evidence more precisely
  than a YWHAE-only activity.
