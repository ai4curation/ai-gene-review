# ADRM1 notes

Review started from `just fetch-gene human ADRM1` for the Proteostasis PN batch. Falcon
deep research was requested with `just deep-research-falcon human ADRM1 --fallback
perplexity-lite`. Falcon timed out after 600 seconds, and the `perplexity-lite` fallback
failed with a Perplexity API 401 quota error. Because no provider file was produced, the
supporting synthesis was recorded in `ADRM1-deep-research-manual.md`.

ADRM1 encodes the human Rpn13 proteasomal ubiquitin receptor. Qiu et al. report that
"we discovered a novel 46-kDa (407 residues) subunit of its 19S regulatory complex"
and that "The C-terminal half of hRpn13 binds directly to the proteasome-associated
deubiquitinating enzyme, UCH37, and enhances its isopeptidase activity" [PMID:17139257
"hRpn13/ADRM1/GP110 is a novel proteasome subunit that binds the deubiquitinating
enzyme, UCH37."]. Hamazaki et al. similarly describe "the identification of Adrm1 as a
novel proteasome interacting protein in mammalian cells" and report that "hRpn13
recruits UCH37, a deubiquitinating enzyme known to associate with 26 proteasomes"
[PMID:16990800 "A novel proteasome interacting protein recruits the deubiquitinating
enzyme UCH37 to 26S proteasomes."].

The direct molecular function should be captured with specific terms, not generic protein
binding. Husnjak et al. report that "Rpn13 binds ubiquitin through a conserved
amino-terminal region termed the pleckstrin-like receptor for ubiquitin (Pru) domain"
[PMID:18497817 "Proteasome subunit Rpn13 is a novel ubiquitin receptor."]. Chen et al.
state that "Rpn13 is a subunit of the proteasome that serves as a receptor for both
ubiquitin and Uch37" and that hRpn2/S1 binding activates hRpn13 for ubiquitin binding
[PMID:20471946 "Structure of proteasome ubiquitin receptor hRpn13 and its activation by
the scaffolding protein hRpn2."]. Therefore, GO:0005515 protein binding rows should be
modified or marked over-annotated in favor of ubiquitin binding, proteasome binding, and
ubiquitin-specific protease binding/deubiquitinase activator functions.

PN projection assessment: ADRM1 is projected to GO:0000502 proteasome complex,
GO:0005838 proteasome regulatory particle, and GO:0008540 proteasome regulatory
particle, base subcomplex from the ubiquitin-proteasome-system PN categories. The broad
proteasome complex term is already in GOA and is acceptable. The regulatory-particle term
is entailed by existing proteasome/regulatory-particle evidence and is safe. The base
subcomplex projection is also supported: a structural review states that recognition of a
ubiquitylated substrate is mediated by "ubiquitin receptors Rpn10 and Rpn13, the base
subunits within the holoenzyme" [PMID:29636472 "Structural mechanism for
nucleotide-driven remodeling of the AAA-ATPase unfoldase in the activated human 26S
proteasome."]. This argues that the existing IBA annotation to GO:0008541 proteasome
regulatory particle, lid subcomplex should be modified to GO:0008540 rather than retained.

The broad process annotations should be handled conservatively. ADRM1 directly contributes
to proteasome-mediated ubiquitin-dependent protein catabolism: Qiu et al. report that
"Knockdown of hRpn13 in 293T cells increases the cellular levels of ubiquitin conjugates
and decreases the degradation of short-lived proteins" [PMID:17139257], and Chen et al.
show that reconstituted hRpn13 stimulates degradation of ubiquitinated cyclin B
[PMID:20471946]. However, the oxidative-stress, type-I-interferon, synaptic-vesicle, and
RNA polymerase II transcription-elongation annotations are not direct ADRM1 core
functions based on the cached text. The transcription-elongation paper is cached only as
partial/abstract text and discusses human Elongator rather than ADRM1, so that annotation
is left undecided pending accessible full text [PMID:11818576 "Human Elongator
facilitates RNA polymerase II transcription through chromatin."].

Annotation stance:

- Core: ubiquitin binding, proteasome binding/base-subcomplex membership, and
  deubiquitinase activator activity for UCHL5/UCH37.
- Accept: broad cytosol/cytoplasm and nucleus/nucleoplasm localization, proteasome
  complex membership, proteasome binding, proteasomal protein catabolic process, and
  proteasome-mediated ubiquitin-dependent protein catabolic process.
- Modify: GO:0008541 lid subcomplex to GO:0008540 base subcomplex; GO:0061133
  endopeptidase activator activity to GO:0035800 deubiquitinase activator activity;
  direct generic protein binding to GO:0043130 ubiquitin binding, GO:0070628 proteasome
  binding, or GO:1990381 ubiquitin-specific protease binding where supported.
- Mark over-annotated: generic screen-derived protein binding, molecular function
  inhibitor activity, proteasome assembly, oxidative stress, type-I-interferon response,
  and synaptic-vesicle localization.
