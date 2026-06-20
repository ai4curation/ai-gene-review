# MKRN2 (Q9H000) research notes

Makorin RING finger protein 2 (RNF62). RING-type E3 ubiquitin ligase, makorin family
(paralog of MKRN1). Contains C3HC4 RING and CCCH/C3H zinc fingers (RNA-binding). Less
characterized than MKRN1; most functional assignments are By similarity / ISS from the
mouse ortholog (Q9ERV1).

## Core MF: RING E3 ubiquitin ligase
UniProt: "E3 ubiquitin ligase catalyzing the covalent attachment of ubiquitin moieties onto
substrate proteins (By similarity). Promotes the polyubiquitination and proteasome-dependent
degradation of RELA/p65, thereby suppressing RELA-mediated NF-kappaB transactivation and
negatively regulating inflammatory responses (By similarity). Plays a role in the regulation
of spermiation and in male fertility (By similarity)." CATALYTIC EC=2.3.2.27 (by similarity).
RING domain (CDD RING-HC_MKRN2).

## Substrate / signaling (ISS / by similarity)
- RELA/p65 polyubiquitination -> negative regulation of NF-kB / inflammatory response
  (GO:1901223, GO:0002862, GO:0006511). ISS from GO_REF:0000024 (ortholog transfer).
- PI3K/AKT signaling, transcription regulation, spermiation — ISS, ortholog-based.

## RNA binding
GO:0003723 RNA binding (HDA, PMID:22681889) — consistent with CCCH zinc fingers; genuine.

## protein binding IPI (all HT / virus-host)
- PMID:17500595 Huntingtin interacting proteins (HT screen)
- PMID:22046132 SARS-coronavirus-host interactome
- PMID:25416956 HI-III human interactome (Y2H)
- PMID:32296183 HuRI binary interactome
- PMID:32814053 neurodegenerative disease interactome
- PMID:32838362 virus-host interactome (virulence factors)
- PMID:36217029 SARS-CoV-2-human contactome
-> all KEEP_AS_NON_CORE / MARK_AS_OVER_ANNOTATED.

## Annotation plan
- GO:0061630 ubiquitin protein ligase activity (IBA/IEA/ISS): ACCEPT (core MF, makorin RING).
- GO:0016567 protein ubiquitination / GO:0000209 polyubiquitination / GO:0006511 ubiquitin-
  dependent catabolic process: ACCEPT.
- GO:0046872 metal ion binding (IEA): KEEP_AS_NON_CORE (Zn coordination).
- NF-kB / inflammatory / RELA terms (ISS): KEEP_AS_NON_CORE (ortholog-based, plausible but not
  directly demonstrated in human).
- transcription terms (DNA-templated transcription, pos reg pol II), PI3K/AKT (ISS): KEEP_AS_NON_CORE
  or MARK_AS_OVER_ANNOTATED (broad, ortholog-transferred, weakly supported).
- nucleus/cytoplasm localization: ACCEPT/KEEP_AS_NON_CORE.
- GO:0003723 RNA binding (HDA): ACCEPT.
Note: unlike MKRN1, there is no direct evidence (in the available set) for an MKRN2-specific
poly(A)-RQC role; the family RQC role is noted but should not be over-asserted for MKRN2.
