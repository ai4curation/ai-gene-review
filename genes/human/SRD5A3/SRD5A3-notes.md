# SRD5A3 review notes

UniProtKB:Q9H8P0 (SR5A3_HUMAN). HGNC:25812. 318 aa, multi-pass ER membrane protein.
Steroid 5-alpha reductase family, polyprenal/polyprenol reductase subfamily. Yeast
ortholog = DFG10.

## Core biology (verified)

SRD5A3 is the ER-membrane, NADPH-dependent reductase that acts in the terminal steps of
**de novo dolichol biosynthesis**, supplying dolichol → dolichol-phosphate, the lipid
carrier for N-glycosylation. Loss of function causes **SRD5A3-CDG (CDG type Iq;
MIM:612379)** and Kahrizi syndrome (KHRZ; MIM:612713), with ocular coloboma, cerebellar
vermis hypoplasia, psychomotor/intellectual disability.

Two successive views of the reaction:
- **Cantagrel et al. 2010 (PMID:20637498, Cell):** SRD5A3 "is necessary for the reduction
  of the alpha-isoprene unit of polyprenols to form dolichols, required for synthesis of
  dolichol-linked monosaccharides, and the oligosaccharide precursor used for
  N-glycosylation" — i.e. the long-sought **polyprenol reductase**. Epitope-tagged SRD5A3
  "localized predominantly to the ER." SRD5A3 was the only member of the human 5α-reductase
  family able to rescue the yeast dfg10 CPY-underglycosylation phenotype; H296G mutant is
  catalytically dead. Phylogeny suggested the ancestral substrate "was potentially not a
  steroid."
- **Wilson et al. 2024 (PMID:38821050, Cell):** revised the pathway — dolichol synthesis
  "requires a three-step detour involving additional metabolites, where SRD5A3 catalyzes
  only the second reaction" (the NADPH-dependent reduction of **polyprenal → dolichal**;
  the first/third steps are done by DHRSX). Hence the current MF term is
  **GO:0160198 polyprenal reductase activity** (EC 1.3.1.94; RHEA:80727), and UniProt's
  RecName is now "Polyprenal reductase" with a CAUTION note that it was initially
  characterised as a polyprenol reductase but "catalyzes an intermediate step in this
  pathway and reduce[s] polyprenal."

## Steroid activity: name only, not physiological function

The gene name ("steroid 5-alpha-reductase 3") and the EC 1.3.1.22 annotation come from
its discovery in prostate cancer:
- **Uemura et al. 2008 (PMID:17986282, Cancer Sci):** identified SRD5A2L/SRD5A3 as a
  "putative 5 alpha-steroid reductase" overexpressed in hormone-refractory prostate cancer;
  in-vitro LC-MS/MS validated DHT production from testosterone; H296 mutagenesis abolished
  activity. This is the origin of the 3-oxo-5-alpha-steroid 4-dehydrogenase (NADP+)
  annotation (GO:0047751 IDA) and the Reactome "SRD5A3 dehydrogenates TEST to DHTEST" /
  androgen-biosynthesis TAS annotations.
- Fouad Mansour et al. 2016 (PMID:26855069; NOT cached) is the ECO:0000305 basis for the
  UniProt EC 1.3.1.22 steroid catalytic-activity block.

Physiological role is dolichol/glycosylation, NOT steroid metabolism: null patients have
CDG, not an androgen/steroid phenotype; phylogeny argues against a steroid ancestral
substrate; steroid activity is weak/in-vitro. Steroid-5α-reductase / androgen-biosynthesis
GO annotations are therefore treated as **MARK_AS_OVER_ANNOTATED** (experimental IDA/TAS,
so not REMOVE per policy) except the plainly wrong **IEA EC-mapping GO:0047751 via
GO_REF:0000120**, which is a demonstrably wrong electronic inference and is REMOVEd.

## GOA term notes
- MF core: GO:0160198 polyprenal reductase activity (IBA + IEA EC1.3.1.94 + EXP + IDA).
- BP core: GO:0043048 dolichyl monophosphate biosynthetic process (IDA PMID:20637498 &
  PMID:38821050; also IBA/IEA/TAS). NB GO:0019408 "dolichol biosynthetic process" is now
  OBSOLETE, obsoleted because it "represents an intermediate step in dolichyl monophosphate
  biosynthetic process ; GO:0043048" — so GO:0043048 is the correct current BP.
- BP: GO:0006488 dolichol-linked oligosaccharide biosynthetic process (IBA/IEA) — accept,
  downstream/pathway-level.
- CC core: GO:0005789 endoplasmic reticulum membrane; GO:0005783 endoplasmic reticulum.
- GO:0016627 / GO:0016628 (CH-CH oxidoreductase parents) — accept as correct but general.
- GO:0006629 lipid metabolic process — over-broad IEA, keep as non-core.
