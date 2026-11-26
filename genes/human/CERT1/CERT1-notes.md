# CERT1 notes

Manual notes for the CPTP/CERK GO-CAM review batch. Falcon and the requested
Perplexity fallback were not available in this checkout, so no provider
`CERT1-deep-research-*.md` artifact was created.

## Core function

CERT1 is the cytosolic ceramide transfer protein that carries ER-made ceramide
to Golgi/TGN membranes without vesicles. The original substrate-specific
transfer paper directly supports the cargo call: CERT transferred common natural
ceramides and not sphingosine or sphingomyelin [PMID:15596449, "CERT did not
mediate the transfer of sphingosine or sphingomyelin at all"].

Kawano et al. showed why the soluble START-domain transfer reaction is routed
from ER to Golgi in cells: CERT has a Golgi-targeting PH domain and an
ER-interacting FFAT motif, and the VAP interaction was lost when the FFAT motif
was mutated [PMID:16895911, "Both VAPs were actually co-immunoprecipitated with
CERT"]. MOSPD2 is a related ER FFAT-motif receptor that can also recruit
STARD11/CERT1 [PMID:29858488, "MOSPD2 possesses a Major Sperm Protein (MSP)
domain which binds FFAT motifs"].

The START domain structural paper supports ceramide binding and transfer, not
C1P transfer: the structures captured one ceramide molecule in a long
amphiphilic cavity and explained how CERT distinguishes ceramide from other
lipids [PMID:18184806, "one ceramide molecule is buried in a long amphiphilic
cavity"].
Kumagai et al. also detected very-low-efficiency transfer of diacylglycerol by
the START domain, but under the promiscuous-activity policy this is in vitro
secondary activity of unclear physiological relevance rather than evidence to
keep a generic lipid-transfer term: the same assay and Hanada et al.'s cell
biology identify ceramide as the evolved cargo [PMID:14685229, "We conclude
that CERT mediates the intracellular trafficking of ceramide in a
non-vesicular manner"].

CERT1 is part of ceramide metabolism and sphingomyelin biosynthesis because it
delivers the ceramide pool used at the Golgi/TGN. Down-regulating CERT lowered
newly synthesized C1P, supporting delivery to CERK [PMID:17392267,
"downregulation of CERT by RNA interference technology dramatically reduced the
levels of newly synthesized C1P"], and the CPTP discovery paper summarizes that
CERK can use ceramide delivered from the ER to the Golgi by CERT
[PMID:23863933, "CERK uses ceramide delivered from its ER synthetic site to the
Golgi by either CERT"].

## Curation decisions

All bare `GO:0005515` protein-binding rows are removed under the
protein-binding policy. This includes true VAPB and MOSPD2 interactions: they
are important targeting interactions, but the GO row asserts only generic
binding. The high-throughput IntAct interactome edges are still weaker evidence
for gene function.

The Reactome `endoplasmic reticulum membrane` rows were narrowed to
`GO:0098554 cytoplasmic side of endoplasmic reticulum membrane`. CERT1 is a
soluble protein that binds the cytosolic domains of ER membrane tethers rather
than an integral ER membrane protein; Reactome's current CERA transport event
explicitly places CERT1-2 on the cytosolic face of the ER membrane
[Reactome:R-HSA-9956909].

The PAINT `PTN000027019` C1P-binding, C1P-transfer and derived C1P-transport
rows are over-propagated. Human CPTP, `UniProtKB:Q5TA50`, is the appropriate
C1P transfer protein [PMID:23863933, "human GLTPD1, named here CPTP, is shown to
specifically transfer C1P between membranes"], whereas CERT1 transports
ceramide.

The old Goodpasture/GPBP immune-response annotation is removed. UniProt now
keeps the original kinase claim only as a cautionary historical statement, and
the old expression data in autoimmune lesions do not show that CERT1 executes an
immune-response step.

## GO-CAM consistency

GO-CAM `68b0f0d000008519` models CERT1 with `GO:0120017` ceramide transfer
activity, `GO:0006672` ceramide metabolic process and `GO:0160258`
ER-trans-Golgi network membrane contact site. Those terms are all retained in
the gene review, so no CERT1-side GO-CAM defect is apparent.
