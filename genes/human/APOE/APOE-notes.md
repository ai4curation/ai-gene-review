# APOE Notes

## 2026-06-19

Manual notes created because provider deep research was unavailable in this run.
`timeout 180 just deep-research-falcon human APOE --fallback perplexity-lite`
stayed silent and timed out without writing an artifact. Publication caching was
refreshed separately with `just fetch-gene-pmids human APOE` and confirmed all
104 APOE review PMIDs were already cached. Per project instructions, no
provider-named deep-research file was written manually.

Core biology: APOE encodes apolipoprotein E, a secreted exchangeable
apolipoprotein whose primary function is lipid and lipoprotein transport.
ABCA1-dependent APOE lipidation supports cholesterol and phospholipid efflux
[PMID:11162594 "ApoA-I and all of the other exchangeable apolipoproteins tested
(apoA-II, apoA-IV, apoC-I, apoC-II, apoC-III, apoE) showed greater than a
threefold increase in cholesterol and phospholipid efflux from ABCAI-GFP
transfected cells compared to control cells."]. The C-terminal lipid-binding
domain is sufficient for ABCA1 lipid efflux and HDL particle assembly
[PMID:17305370 "the CT lipid-binding domain of apoE encompassing amino acids
222-299 is necessary and sufficient for mediating ABCA1 lipid efflux and HDL
particle assembly."].

Lipoprotein clearance: APOE acts as a receptor/proteoglycan ligand on
lipoprotein particles. LRP mediates uptake and lysosomal hydrolysis of
cholesteryl esters in apoE-enriched lipoproteins [PMID:2762297 "We conclude
that LRP can mediate the cellular uptake and lysosomal hydrolysis of cholesteryl
esters contained in lipoproteins that are enriched in apo E."]. Hepatic HSPG
clearance of triglyceride-rich lipoproteins is mediated in part by ApoE
[PMID:23676495 "We conclude that clearance of TRLs by hepatic HSPGs is
atheroprotective and mediated by multivalent binding to ApoE and ApoAV."].

CNS context: APOE also mediates glial/CNS lipid transport. Astrocytes expressing
human APOE isoforms release cholesterol and phospholipids into HDL-like
particles [PMID:12042316 "Cholesterol and phospholipids were released into the
culture media, resulting in the generation of two types of high density
lipoprotein (HDL)-like particles; one was associated with apoE and the other
with apoJ."]. This supports retaining CNS lipid-transport annotations while
keeping downstream synaptic, neurite, and behavior annotations as non-core
phenotypes.

Amyloid and immune interactions: APOE has credible Alzheimer-relevant
interactions with amyloid-beta, tau, TREM2/LILRB4, extracellular vesicles, and
other partners, but these should not displace the core lipid/lipoprotein
function. ApoE affects amyloid-beta oligomer/fibril growth [PMID:25207746 "apoE
binds primarily to and affects the growth of oligomers that lead to the nuclei
required for fibril growth."] and APOE-containing lipoprotein particles can act
as TREM2 ligands [PMID:27477018 "we identified a set of lipoprotein particles
(including LDL) and apolipoproteins (including CLU/APOJ and APOE) as ligands of
TREM2."]. These were retained as non-core or marked over-annotated when the term
was only generic `protein binding`.

Knowledge gaps to curate:

- Which APOE receptor/proteoglycan interactions should be represented by
  particle class, receptor family, and tissue, rather than as generic receptor
  binding?
- Which CNS APOE phenotypes are direct consequences of normal glial lipid
  transport, and which are downstream disease-model effects involving amyloid,
  tau, inflammation, or synapses?
- Which extracellular-vesicle and multivesicular-body APOE pools are normal
  physiological lipid-transport pools versus specialized contexts such as PMEL
  amyloid formation in pigment cells?

Review update: completed first-pass review of all 293 seeded GO annotations.
Final action distribution after validation: 145 ACCEPT, 120 KEEP_AS_NON_CORE,
and 28 MARK_AS_OVER_ANNOTATED. `just validate human APOE` passes cleanly. The
reference title for PMID:1530612 was aligned to the validator's cached parser
output, which truncates at the `----` sequence in the publication title; the
publication cache itself was not edited.

## 2026-06-20 second-pass audit

The second-pass audit added manual `reference_review` metadata for the key APOE references supporting ABCA1-dependent lipid efflux, astrocyte APOE lipoprotein release, LRP-mediated uptake of apoE-enriched particles, amyloid-beta binding/aggregation effects, and TREM2-mediated microglial uptake of APOE-containing amyloid-lipoprotein complexes. No annotation action changes were needed: the core remains lipid/lipoprotein transport and receptor-mediated particle handling, while amyloid, synaptic, immune, and disease-model outcomes remain non-core or over-annotated when they do not describe the primary evolved APOE function.
