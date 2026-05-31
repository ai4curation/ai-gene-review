# Rab7 (mouse, Rab7a) — Review Notes

UniProt: **P51150** (RAB7A_MOUSE), 207 aa. Official MGI symbol **Rab7a** (MGI:105068),
historical/synonym symbol **Rab7**. Directory and files use the `Rab7` prefix (as
fetched). NCBI taxon 10090.

## Summary of gene function

Mouse Rab7 (Rab7a) is the direct ortholog of human RAB7A and is functionally identical:
a Rab-family small GTPase (EC 3.6.5.2) that acts as the master regulator of the late
endocytic pathway. It cycles between an inactive GDP-bound (cytosolic) state and an
active GTP-bound (membrane-associated) state. When GTP-loaded by the Mon1–Ccz1 GEF on
maturing endosomes (Rab5→Rab7 conversion), it recruits effectors (RILP, HOPS,
retromer, FYCO1, PLEKHM1, ORP1L) to drive late endosome–lysosome fusion,
autophagosome–lysosome fusion, phagosome maturation, retrograde endosome→Golgi
transport, and lysosome positioning. It is inactivated by TBC-domain GAPs.

The mouse-specific experimental literature emphasizes physiological roles:
- **Lipophagy / β-adrenergic lipolysis** in adipocytes [PMID:23708524].
- **Synaptic AMPA-receptor trafficking and LTD** in neurons [PMID:24217640].
- **Osteoclast bone resorption / ruffled border** via PLEKHM1/DEF8 and RUFY4
  [PMID:27777970, PMID:38744829, PMID:22467241].
- **Secretory-lysosome trafficking** via V-ATPase a3-mediated Rab7 recruitment
  [PMID:29712939].
- Numerous late-endosome/lysosome co-localization studies (TrkB/NHE6, TrkA/Nedd4-2,
  BACE1, TMEM127, WASH/strumpellin, C9ORF72, etc.).

## Key requested reference

**[PMID:41814093]** Jozić et al. (2026) *Nature Biotechnology*,
"In vivo endosomal escape assay identifies mechanisms for efficient hepatic LNP
delivery." DOI: 10.1038/s41587-026-03022-6.
- Used **LysoTag mice** for immunoisolation of liver lysosomes and lysosomal
  proteomics to quantify endosomal escape of lipid nanoparticles (LNPs) in vivo.
- Key Rab7 finding: *"Loss of Rab7, a mediator of late endosomal maturation,
  increased LNP escape."* In vivo evidence (mouse liver) that Rab7 is a mediator of
  **late endosomal maturation** and that its loss diverts cargo away from the
  degradative lysosomal route, increasing cytosolic escape.
- This supports the core Rab7 functions of late-endosome maturation
  (early→late endosome transport, endosome→lysosome transport) in an intact mouse.
- Added as a reference and cited as supporting evidence on the relevant
  maturation/transport annotations.

## Deep research provider status

Automated deep research could not be run in this environment: the **Falcon**
provider requires the `agentapi` binary (not in PATH), and the
OpenAI/Perplexity/Anthropic providers require API keys that are unset. No
`-deep-research-{provider}.md` file was fabricated (per project policy). A manual,
fully-cited synthesis was written to `Rab7-deep-research-manual.md` instead.

## Annotation review approach

119 GOA annotations seeded. The biology mirrors human RAB7A
(genes/human/RAB7A/RAB7A-ai-review.yaml). Decisions:
- ACCEPT core MF (GTPase activity, G protein activity, GTP/GDP binding) and core
  CC/BP (late endosome, lysosome, endosome→lysosome transport, retromer, retrograde
  transport, autophagy/lipophagy, phagosome maturation).
- REMOVE all `GO:0005515 protein binding` (uninformative per curation guidelines);
  the underlying effector interactions are captured by specific terms.
- KEEP_AS_NON_CORE for tissue/context-specialized roles (synaptic, bone resorption,
  melanosome, mitophagy, exosome, viral, sterol sensing, EGF catabolism).
- MARK_AS_OVER_ANNOTATED for Golgi apparatus (GO:0005794, IDA from a bulk Golgi
  membrane proteomics study [PMID:11042173]) — Rab7 is a late-endosome/lysosome
  protein and this is most consistent with co-fractionation/contamination rather
  than a genuine steady-state Golgi pool.
