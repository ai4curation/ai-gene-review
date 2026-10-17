# cII (P03042) - Curation Notes

## Overview
- **Gene symbol**: `cII`
- **UniProt ID**: `P03042` (`RPC2_LAMBD`)
- **Protein name**: Transcriptional activator II (97 AA)
- **Organism**: Escherichia phage lambda (`NCBITaxon:2681611`)

## Function & Biological Context
- **Master activator for establishment of lysogeny**: CII is a homotetrameric helix-turn-helix transcriptional activator (4 x 11 kDa) that is the primary determinant for establishing the lysogenic state upon initial infection of *Escherichia coli* [PMID:16061804, "Crucial to the lysis/lysogeny decision is the homotetrameric transcription-activator protein CII (4 x 11 kDa) of the phage that binds to a unique direct-repeat sequence T-T-G-C-N6-T-T-G-C at each of the three phage promoters it activates: p(E), p(I), and p(aQ)."].
- **Direct-repeat DNA recognition and coordinate activation of three promoters**: Unlike CI and Cro, which bind inverted repeats on the B-DNA major groove as dimers, CII assembles into an asymmetric dimer-of-dimers homotetramer that recognizes two direct-repeat tetranucleotide sequences (`TTGC-N6-TTGC`) flanking the RNA polymerase `-35` hexamer on the opposite face of the DNA helix [PMID:16039594, "The tetrameric cII protein from bacteriophage lambda activates transcription from the phage promoters P(RE), P(I), and P(AQ) by binding to two direct repeats that flank the promoter -35 element."]. By binding these sites and contacting the RNA polymerase alpha-subunit C-terminal domain (alpha-CTD) and sigma70, CII coordinately activates three phage promoters:
  1. `PRE` (`pE`): promoter for repressor establishment, driving high-level synthesis of the CI immunity repressor.
  2. `PI` (`pI`): promoter for `int` (integrase) synthesis, enabling site-specific integration of the phage genome into the host chromosome.
  3. `PaQ` (`paQ`): antisense promoter within the `Q` gene that antagonizes expression of the late lytic antiterminator Q, delaying late lytic transcription.
- **Proteolytic control by host FtsH (HflB) and HflD, and protection by phage CIII**: CII is intrinsically unstable in vivo (half-life ~1-2 minutes) because its unstructured C-terminal tail (residues 80-97) is recognized and degraded by the host ATP-dependent membrane metalloprotease FtsH (HflB) [PMID:20599668, "These membrane proteins copurify as a tightly bound complex 'HflKC' that inhibits the HflB (FtsH)-mediated proteolysis of CII both in vitro and in vivo."], and its DNA binding/activation is also impaired by host HflD [PMID:19853572, "An unstable homotetrameric transcription activator of the three phage promoters p(E), p(I) and p(aQ), lambdaCII is stabilized by lambdaCIII and destabilized by the host protease, Escherichia coli HflB (FtsH)."]. The phage-encoded protease inhibitor CIII competitively inhibits FtsH to stabilize CII and promote lysogeny.

## Review of Existing GO Annotations
- `GO:0003677` (DNA binding, IEA, `GO_REF:0000120`): **ACCEPT** (core molecular function supported by `PMID:16061804` and `PMID:16039594`, which show direct binding to the `TTGC-N6-TTGC` direct repeats at `PRE`, `PI`, and `PaQ`).
- `GO:0005515` (protein binding, IPI, `PMID:20599668`, with `UniProtKB:P0AAI3` FtsH): **REMOVE**. Although the physical interaction with host FtsH (`P0AAI3`) is real and mediates CII proteolysis, bare `GO:0005515` carries no informative molecular function for CII.
- `GO:0006355` (regulation of DNA-templated transcription, IEA, `GO_REF:0000002`): **MODIFY** to `GO:0050434` (positive regulation of viral transcription), which specifically captures CII's role as a transcriptional activator of the viral `PRE`, `PI`, and `PaQ` promoters.
- `GO:0019042` (viral latency, IEA, `GO_REF:0000043`): **ACCEPT**. CII is the decisive factor for establishing viral latency (lysogeny) upon infection.
