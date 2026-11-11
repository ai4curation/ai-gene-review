# EMENI/avaA manual review notes

## Scope and source availability

Provider deep research was unavailable in this sparse worktree because the
configured deep-research providers require credentials that were not present. I
used the seeded GOA review, the cached UniProt flat file, the cached PTHR47981
PAINT rows, the full-text cached Abenza et al. 2012 endosomal-maturation paper,
the cached Ohsumi et al. 2002 avaA abstract, the full-text cached Pinar et al.
2013 autophagy paper, and PubMed/Europe PMC searches for direct or newer
A. nidulans AvaA/RabS papers.

## PANTHER/IBA assessment

PTHR47981 is the Rab-family PAINT tree. A. nidulans AvaA/RabS (`C8VQY7`) is in
`PTHR47981:SF20`, `RAS-RELATED PROTEIN RAB-7A`, with S. cerevisiae YPT7, S.
pombe ypt7, N. crassa gtp-14, and other Rab7/Ypt7 proteins.

The key fungal node is `PTN001178553`. It places fungal-type vacuole membrane,
regulation of vacuole fusion, and vacuole fusion on the fungal Rab7/Ypt7 branch
from S. cerevisiae and S. pombe seeds, and the `GO:0042144` placement is also
seeded by `UniProtKB:C8VQY7` itself. That target seed is appropriate direct
grounding, not circular evidence: the A. nidulans experimental row was one of
the descendant annotations used to place the IBD at the fungal node. There is
no sign of wrong-paralog propagation.

The broader Rab7 node `PTN000635769` places late endosome and the generic
vacuole compartment. Late endosome is supported directly by Abenza et al., who
showed RabS recruitment to the late side of the Rab5-to-Rab7 transition
[PMID:22456509, "RabS(Rab7) is recruited to membranes already at the stage of
late endosomes still lacking vacuolar morphology"]. The generic vacuole row is
true but less specific than the fungal-type vacuole membrane.

The eukaryotic Rab7 node `PTN001939797` places `GO:0003925` G protein activity
from mammalian and fungal Rab7 seeds. This PAINT row is absent from the seeded
GOA for AvaA even though it matches the direct A. nidulans GDP/GTP mutant work,
so I added it as a conservative `NEW` molecular-function annotation.

## Cached publication findings

Ohsumi et al. 2002 is the original direct avaA functional study. The cached
abstract verifies that avaA encodes the A. nidulans Vam4/Ypt7 homolog, that
avaA disruption or GDP-locked replacement fragments vacuoles, and that
GTP-locked avaA overexpression causes swollen vacuoles [PMID:12095681, "The
avaA disruptants exhibited highly fragmented vacuoles."].

Abenza et al. 2012 is the direct A. nidulans RabS paper. It localizes RabS to
vacuolar and late-endosomal membranes, shows that GTP-loaded RabS recruits HOPS
components, and establishes a model in which RabS replaces RabA/RabB and
promotes HOPS-dependent fusion of late endosomes and vacuoles [PMID:22456509,
"RabS(Rab7) mediates homotypic fusion of late endosomes/vacuoles"].

Pinar et al. 2013 followed the A. nidulans autophagosome cycle by live-cell
GFP-Atg8 imaging and showed that autophagosomes fuse with vacuoles in a
RabS/Rab7-HOPS-dependent manner [PMID:23722157, "autophagosomes fuse with
vacuoles directly in a RabS"].

Pinar and Penalva 2021 is a review of A. nidulans Rab GTPases. It is useful
background for Rab nomenclature and the integrated endocytic/exocytic Rab
system but does not supersede the primary RabS experiments.

## 2024-2026 literature search

Searched PubMed and Europe PMC for:

- `(avaA OR RabS OR Rab7) AND ("Aspergillus nidulans" OR "Emericella
  nidulans")`
- `(avaA OR RabS OR Rab7) AND "Aspergillus nidulans"`
- `("Aspergillus nidulans" OR "Emericella nidulans") AND autophagosome vacuole
  fusion RabS`

The main later A. nidulans hits were the 2026 TRAPPIII/autophagy paper and the
2026 RAB11/Sec4/exocyst tip-growth paper. They are not direct AvaA/RabS papers
and did not require new row-level avaA curation. Searches did not find a newer
primary study that changed the RabS/Rab7 function established in 2002, 2012, and
2013.
