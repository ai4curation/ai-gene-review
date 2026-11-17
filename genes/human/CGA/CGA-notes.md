# CGA (P01215) Curation Notes

## Summary
- **Gene:** `CGA` (UniProtKB:P01215; PANTHER `PTHR11509:SF0`, PAINT node `PTN002608947`)
- **Product:** Glycoprotein hormones alpha chain — the common obligate alpha subunit shared by all four human pituitary and placental glycoprotein hormones: thyroid-stimulating hormone (TSH, heterodimer with `TSHB`), follicle-stimulating hormone (FSH, heterodimer with `FSHB`), luteinizing hormone (LH, heterodimer with `LHB`), and chorionic gonadotropin (hCG, heterodimer with `CGB3`/`CGB5`/`CGB8`) [PMID:22802634, PMID:36001021, PMID:36720854].

## Key Literature & Structural Evidence
- **Shared alpha subunit of heterodimeric glycoprotein hormones:**
  - [PMID:22802634]: *"The glycoprotein hormone (GPH) family has four members: FSH; two other pituitary hormones, luteinizing hormone and thyroid-stimulating hormone (TSH); and one placental hormone, chorionic gonadotropin. The four members are homologous in sequence, structure, and function. Each member is a heterodimer composed of a common α-subunit and a hormone-specific β-subunit."*
- **Direct receptor contact and activation in TSH, FSH, and LH/hCG signaling:**
  - [PMID:36001021]: *"While the β subunit mainly binds to the LRR domain of TSHR, the α subunit simultaneously interacts with the LRR domain and the hinge region of the receptor."*
  - [PMID:36720854]: *"FSH, along with luteinizing hormone (LH), chorionic gonadotropin (CG) and thyroid-stimulating hormone (TSH), constitute the family of glycoprotein hormones14, which share similar 3D architectures and function through binding and activation of a subfamily of G protein-coupled receptors, named glycoprotein hormone receptors15."*

## Annotation Review Decisions
- **Core MF:** `GO:0005179` (*hormone activity*, `ACCEPT` on IEA `GO_REF:0000002` and IMP `PMID:11207219`) and `GO:0016913` (*follicle-stimulating hormone activity*, `ACCEPT` on IDA `PMID:24692546`, `PMID:2494176`, `PMID:36720854`, and IEA `GO_REF:0000117`).
- **Protein binding (`GO:0005515`):** All five IPI rows with `FSHB` (`UniProtKB:P01225`) and `CGB3` (`UniProtKB:P0DN86`) are set to `REMOVE` per the project protein-binding policy; subunit heterodimerization is captured by the complex annotations (`GO:0016914` *follicle-stimulating hormone complex* and `GO:0061696` *pituitary gonadotropin complex*).
- **Signaling pathways:**
  - `GO:0042699` (*follicle-stimulating hormone signaling pathway*, NAS `PMID:11222739`) is `ACCEPT`.
  - Broad signaling terms `GO:0007186` (*G protein-coupled receptor signaling pathway*), `GO:0009755` (*hormone-mediated signaling pathway*), and `GO:0010469` (*regulation of signaling receptor activity*) are `MODIFY` with `proposed_replacement_terms` listing all three specific glycoprotein hormone signaling pathways in which `CGA` participates: `GO:0038194` (*thyroid-stimulating hormone signaling pathway*), `GO:0042699` (*follicle-stimulating hormone signaling pathway*), and `GO:0042698` (*luteinizing hormone signaling pathway*).
  - Added `NEW` annotations for `GO:0038194` (*thyroid-stimulating hormone signaling pathway*, supported by `PMID:36001021` and `Reactome:R-HSA-391375`) and `GO:0042698` (*luteinizing hormone signaling pathway*, supported by `PMID:36720854` and `Reactome:R-HSA-391377`).
- **Downstream / pleiotropic / over-propagated terms:**
  - `GO:0000165` (*MAPK cascade*), `GO:0008284` (*positive regulation of cell population proliferation*), `GO:0030335` (*positive regulation of cell migration*), and `GO:0045944` (*positive regulation of transcription by RNA polymerase II*) are set to `MARK_AS_OVER_ANNOTATED` as downstream intracellular consequences of FSHR/LHCGR/TSHR activation.
  - `GO:0001541` (*ovarian follicle development*), `GO:0007283` (*spermatogenesis*), and `GO:0010893` (*positive regulation of steroid biosynthetic process*) are set to `KEEP_AS_NON_CORE` as downstream physiological processes regulated by gonadotropin signaling.
  - `GO:0035773` (*insulin secretion involved in cellular response to glucose stimulus*, IEA Ensembl Compara from mouse `Cga`) is `REMOVE` as an unverified electronic transfer unrelated to glycoprotein hormone alpha chain function.
