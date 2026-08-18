# Kurtz (krz) — Drosophila melanogaster non-visual (β-)arrestin — review notes

UniProt: Q9V393 (Q9V393_DROME) · FlyBase: FBgn0040206 · CG1487 · 470 aa.

## Gene identity / architecture
- Krz is the **single non-visual β-arrestin** of Drosophila. UniProt: "Belongs to the arrestin family"; two arrestin domains (Arrestin_N PF00339, Arrestin_C PF02752), PANTHER PTHR11792:SF17 "KURTZ ARRESTIN". Synonym `beta-arr2`.
- Molnar et al. frame it clearly: "In Drosophila melanogaster there is only a single non-visual β-arrestin, encoded by kurtz (krz), which function is essential for development, survival and neural function" [PMID:21437272]. A related gene CG32683 "lacks the clathrin-binding domain" and cannot substitute for Krz.
- Krz "has all the molecular features of a canonical β-arrestin"; conserved residues implicated in GPCR→clathrin-coated-pit targeting (Val94) and in clathrin binding (Leu440/IsoLeu441/Leu443) are functionally required [PMID:21437272].

## Molecular function — canonical arrestin core
- Canonical arrestin pathway restated in the Hh paper's intro: agonist-activated GPCRs are phosphorylated by GRKs, "followed by binding of the cytosolic arrestin proteins," and "the GRK/ß-arrestin pathway facilitates receptor internalization from the cell surface through clathrin-coated pits," leading to receptor degradation/recycling [PMID:21437272].
- Krz "has recently been shown to promote internalization of GPCRs on receptor activation" [PMID:20802461] (citing Johnson et al. 2008), and "controls Drosophila olfaction, behaviour, sensitivity to osmotic stress" [PMID:20802461] — i.e. bona fide GPCR-regulator behaviour.
- Direct receptor binding demonstrated for the GPCR-family receptor Smoothened: co-IP shows Krz–Smo interaction; "these results... suggest that Krz binds to Smo and internalizes it via clathrin-coated vesicles" [PMID:21437272].

## MAP-kinase (ERK) sequestration — a distinctive Krz molecular function
- Krz directly binds ERK (rolled). "Krz can directly bind and sequester an inactive form of ERK, thus preventing its activation by the upstream kinase, MEK" [PMID:20802461]. IntAct records the Krz–rl interaction with NbExp=12 (UniProt Q9V393 INTERACTION block). This is the basis of the bare `GO:0005515 protein binding` IPI (PMID:20802461) → should be an informative MF (mitogen-activated protein kinase binding, GO:0051019).
- Consequence: "loss of krz function results in an overall increase in ERK activity" [PMID:20802461] → negative regulation of the MAPK cascade (rolled/ERK) and of the Torso RTK pathway.

## Biological processes (mostly pleiotropic developmental-signalling roles)
- **Torso (RTK) / MAPK**: "the normal function of Krz is to limit the activity of ERK, and hence the Torso pathway, in the early embryo" [PMID:20802461]. Distinct from Notch mechanism; a "molecular sponge" sequestering inactive ERK.
- **Toll / NF-κB (Dorsal–Cactus)**: "Krz functions during normal development to limit the activity of Toll" [PMID:20802461]; Krz binds and stabilises Cactus (IκBα orthologue). Independently, in the immune/larval context "Loss of function of krz or Ulp1 in Drosophila larvae results in a similar inflammatory phenotype" [PMID:24077307] — Krz limits Toll signalling via the SUMO protease Ulp1.
- **Hedgehog / Smoothened**: over-expressed Krz promotes Smo internalization and degradation, "in a clathrin- and proteosomal-dependent manner" [PMID:21437272]; "Krz enhances Smo degradation via the proteosomal pathway" (protein destabilization). Antagonism of Hh is "only observed upon its over-expression" [PMID:21437272]; loss-of-function has no Smo phenotype (Smo unchanged in krz clones). In Cheng et al., "overexpression of Gprk2 or the β-arrestin orthologue Krz led to a reduction of Smo levels" — "first evidence that arrestins participate in Smo regulation in flies" [PMID:19850026], though "Smo levels were unchanged in krz mutant wing disc clones."
- **SUMO/Smo**: Krz promotes Smo desumoylation by bridging Smo to Ulp1: "Krz likely facilitates the interaction between Smo and Ulp1 because knockdown of Krz by RNAi attenuates Smo-Ulp1 interaction"; "inhibits Smo sumoylation and prevents Smo accumulation through Krz regulatory domain" [PMID:28195188].
- **Notch**: trimeric Notch–Deltex–Krz complex; "This complex mediates the degradation of the Notch receptor through a ubiquitination-dependent pathway" [PMID:16284625] (abstract-only cache; IGI + Reactome R-DME-2071846 "Deltex recruits Kurtz arrestin to Notch", R-NUL-2071858 "Kurtz promotes ubiquitination of Notch").
- **Behaviour / sensory**: "There is a specific requirement for the kurtz nonvisual arrestin in the nervous system for both the exploration stimulated by the novel arena and the mechanically stimulated activity" [PMID:17151232]; Krz essential for CNS/neural function and viability [PMID:21437272].

## Localization
- Predominantly cytoplasmic: "the Krz protein is expressed throughout the blastoderm embryo and is predominantly cytoplasmic" [PMID:20802461]; "the protein is localized in the cytoplasm of imaginal cells, being detected at higher levels close to the apical side of the epithelium" [PMID:21437272]. Consistent with `cytoplasm`/`cytosol` (IBA, IDA, Reactome TAS). Functions transiently at the plasma membrane/endosome during receptor internalization but no dedicated experimental CC annotation for those compartments in GOA.

## Curation synthesis
- **Core** (canonical, evolutionarily conserved arrestin functions): GPCR binding (GO:0001664), GPCR internalization (GO:0002031), positive regulation of receptor-mediated endocytosis (GO:0048260), cytoplasm/cytosol localization. A second, well-supported direct MF is MAP-kinase (ERK) binding (GO:0051019), underlying ERK/Torso/MAPK inhibition.
- **Non-core** (pleiotropic developmental / immune signalling-attenuation roles, many seen only on over-expression): negative regulation of Toll (×2), Torso, Smoothened (×2), MAPK cascade, Notch; protein destabilization; positive regulation of protein desumoylation; locomotory exploration behavior; sensory perception.
- **`GO:0005515 protein binding` (IPI, PMID:20802461)** is uninformative → MODIFY to `GO:0051019 mitogen-activated protein kinase binding` (Krz–ERK/rolled).
- **`GO:0007165 signal transduction` (IEA)** is very general but not wrong (arrestin is a signalling regulator) → ACCEPT.
- No REMOVE calls: every experimental annotation is supported by its cited paper; abstract-only Notch (PMID:16284625) is directly supported by its own abstract.

## GO IDs verified
- GO:0051019 mitogen-activated protein kinase binding — MF, subclass of protein kinase binding (AmiGO). Used for the protein-binding MODIFY and core_function 2.
- GO:0001664 (GPCR binding, MF), GO:0002031 (GPCR internalization, BP), GO:0048260 (positive regulation of receptor-mediated endocytosis, BP), GO:0043409 (negative regulation of MAPK cascade, BP), GO:0005737 (cytoplasm, CC), GO:0005829 (cytosol, CC) — used in core_functions.
