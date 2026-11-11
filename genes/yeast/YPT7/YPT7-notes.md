# YPT7 review notes

## Scope

YPT7 encodes the S. cerevisiae Rab7/Ypt7 small GTPase that acts on late endosomes
and fungal-type vacuole membranes. I reviewed the full GOA-seeded annotation set
with emphasis on the PTHR47981 PAINT rows and on replacing generic
`GO:0005515 protein binding` where the source paper supports a HOPS or retromer
complex interaction.

## PAINT/IBA rows

PTHR47981 has three Ypt7-relevant nodes in the local PAINT export:

- `PTN001178553`, the fungal Rab7/Ypt7 node, supports `GO:0000329 fungal-type
  vacuole membrane`, `GO:0032889 regulation of vacuole fusion, non-autophagic`,
  and the newer `GO:0042144 vacuole fusion, non-autophagic` row. This is a valid
  fungal placement seeded by S. cerevisiae and S. pombe Ypt7 descendants rather
  than a broad animal Rab7 transfer.
- `PTN000635769` supports `GO:0005770 late endosome`; S. cerevisiae YPT7 is in
  the supported Rab7 branch, and the direct retromer literature places Ypt7 at
  late endosomes.
- `PTN001939797` supports `GO:0003925 G protein activity`; this is a better
  description of a Rab-family GTP/GDP molecular switch than the generic
  `GO:0003924 GTPase activity` rows currently in GOA.

## Existing-annotation triage

The core molecular role is small-G-protein switching, supported by the InterPro
Small_GTPase/Small_GTP-bd signatures and the Ypt/Rab experimental literature.
Rows with `GO:0003924` were kept as sound but modified to `GO:0003925` for the
more precise G-protein activity.

Ypt7's core compartments are the late endosome and fungal-type vacuole membrane.
Broad `vacuole` and generic `vacuolar membrane` rows were treated as too general
or modified to `fungal-type vacuole membrane`; the whole-mitochondrion and
mitochondrial outer membrane HDA rows were removed because they are better
explained by vacuole-mitochondrion contacts than by Ypt7 residency in the
mitochondrial outer membrane.

The directed HOPS interaction rows from PMID:11062257, PMID:18809726,
PMID:20604902, and PMID:21325627 were modified from `protein binding` to
`GO:0044877 protein-containing complex binding`. The Vps35/retromer row from
PMID:22593205 was narrowed further to `GO:1905394 retromer complex binding`.
Yip, Ivy1, Gdi1, and proteome-scale rows were removed because no more
informative Ypt7 molecular-function term follows from those physical contacts.

The 1993 alpha-factor study, PMID:8308065, was added to support
`GO:0045324 late endosome to vacuole transport`, replacing broad
`endocytosis`. PMID:22593205 supports keeping `GO:0042147 retrograde transport,
endosome to Golgi` and modifying the broad `protein localization to vacuole`
phenotype to the same retromer-mediated retrograde process.

The PMN row from PMID:18701704 remains marked over-annotated: the ypt7 deletion
phenotype is real, but the paper frames the defect as a likely consequence of
vacuolar biogenesis rather than a dedicated Ypt7 step in piecemeal
microautophagy of the nucleus.

## Newer literature

PMID:39307308 reports that very-long-chain-fatty-acid sphingolipids regulate
the Ypt7/HOPS tethering stage of vacuole fusion. PMID:40766606 reports that
vacuolar PI(3,4,5)P3 controls vertex enrichment of Ypt7 and HOPS during fusion.
These refine the lipid dependence of the same Ypt7/HOPS vacuole-fusion module
and do not require a new GO assertion.

PMID:42593964 reports a 2026 lipid-droplet internalization pathway in which
Mon1-Ccz1 activates Ypt7 and retromer at Pdr16-marked lipid droplet/vacuole
interfaces during nutrient limitation. I recorded this as a follow-up question
because the process annotation for Ypt7 should wait until curators decide
whether the pathway is a dedicated lipophagy route or another use of the
late-endosome/vacuole Ypt7-retromer machinery.
