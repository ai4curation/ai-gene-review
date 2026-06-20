# ADRM1 manual deep research

Falcon deep research was attempted with `just deep-research-falcon human ADRM1 --fallback
perplexity-lite`. Falcon timed out after 600 seconds, and the configured fallback failed
with a Perplexity API 401 quota error. This manually curated summary is based on the
cached UniProt record, GOA, PN projection reports, and cached publications.

## Core identity

ADRM1 encodes proteasomal ubiquitin receptor ADRM1/Rpn13, a 407-aa human 19S
regulatory-particle protein. UniProt describes it as a component of the 26S proteasome
that functions as a proteasomal ubiquitin receptor and engages UCHL5/UCH37 during protein
degradation. The protein contains an N-terminal Pru domain and a C-terminal DEUBAD region.

## Primary evidence

Qiu et al. identified ADRM1/GP110 as human Rpn13, "a novel 46-kDa (407 residues) subunit
of its 19S regulatory complex" [PMID:17139257]. They report that "The C-terminal half of
hRpn13 binds directly to the proteasome-associated deubiquitinating enzyme, UCH37, and
enhances its isopeptidase activity" [PMID:17139257]. ADRM1 knockdown increased cellular
ubiquitin conjugates and decreased degradation of short-lived proteins, supporting a
direct role in ubiquitin-dependent proteasomal degradation [PMID:17139257].

Hamazaki et al. independently identified Adrm1 as "a novel proteasome interacting protein
in mammalian cells" and found that hRpn13 recruits UCH37 to 26S proteasomes [PMID:16990800].
The same abstract reports that hRpn13 knockdown caused loss of UCH37 proteins and decreased
deubiquitinating activity of 26S proteasomes [PMID:16990800].

Husnjak et al. identified Rpn13/ADRM1 as a proteasomal ubiquitin receptor. They state that
"Rpn13 binds ubiquitin through a conserved amino-terminal region termed the pleckstrin-like
receptor for ubiquitin (Pru) domain" [PMID:18497817]. Chen et al. later showed that
hRpn13 binding to the hRpn2/PSMD1 scaffold activates ubiquitin binding and that adding
wild-type hRpn13 to hRpn13-deficient proteasomes strongly stimulated degradation of
ubiquitinated cyclin B [PMID:20471946].

## PN projection assessment

The Proteostasis PN projection places ADRM1 under ubiquitin-proteasome-system regulatory
particle/base and ubiquitin-binding proteasomal-subunit categories. The projected
GO:0000502 proteasome complex is already present in GOA and is safe. The projected
GO:0005838 proteasome regulatory particle is safe as an entailed broader term. The
projected GO:0008540 proteasome regulatory particle, base subcomplex is also supported:
Zhu et al. describe Rpn10 and Rpn13 as "the base subunits within the holoenzyme" involved
in ubiquitylated substrate recognition [PMID:29636472]. This supports modifying the
existing IBA GO:0008541 lid-subcomplex annotation to GO:0008540 base subcomplex.

## Curation conclusions

- Core molecular functions: ubiquitin binding (GO:0043130), proteasome binding
  (GO:0070628), deubiquitinase activator activity (GO:0035800), and
  ubiquitin-specific protease binding (GO:1990381) for UCHL5/UCH37.
- Core process: proteasome-mediated ubiquitin-dependent protein catabolic process
  (GO:0043161), with ADRM1 acting as a receptor/cofactor rather than the proteolytic
  catalytic subunit.
- Core complex/location: 26S proteasome/19S regulatory particle, most specifically
  proteasome regulatory particle, base subcomplex (GO:0008540), acting in cytosolic
  and nuclear proteostasis.
- Conservative removals/over-annotation calls: generic protein binding, broad pathway
  response terms, molecular function inhibitor activity, proteasome assembly, synaptic
  vesicle, and RNA polymerase II transcription elongation should not be treated as ADRM1
  core functions without more direct evidence.
