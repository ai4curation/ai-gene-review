# MYCTU argA / O33289 / Rv2747 review notes

## 2026-10-25 systematic review

Seeded normally with `just fetch-gene MYCTU O33289 --alias argA`; all 10 original rows are preserved. Applied review and annotation-reviewer skills, with independent annotation-reviewer consultation. No NEW annotations added.

Deep research and publication caching were launched in parallel. Falcon failed authentication (403); fallback perplexity-lite failed with quota401. Logs: `.cache/module-audit-logs/arginine-myctu-argA-research.log` and `arginine-myctu-argA-fetch.log`. No provider report was fabricated. FEBA was attempted and had neither an MYCTU mapping nor a reachable data source; no fitness artifact or absence-of-phenotype inference was made. Manual research follows.

## Primary evidence and architecture

[PMID:15838030 Functional characterization of a novel ArgA from Mycobacterium tuberculosis] is the actual target primary paper, fetched normally with full text and independently inspected. PMID17012791 is instead preliminary characterization/crystallization of Rv1652/ArgC and Rv1656/ArgF and is not an ArgA source.

Rv2747 is a short approximately19kDa GNAT homolog corresponding to the acetyltransferase portion of classical two-domain ArgA. It acetylates both L-glutamate and L-glutamine; neither D-enantiomer nor ornithine was a substrate in the reported panel. Glutamine was better than glutamate, which did not saturate even at600mM. The measured glutamine Km is280±40mM, acetyl-CoA Km150±30micromolar and kcat200±15/min. The sequential kinetic mechanism was fit using glutamine. HPLC/NMR directly identified N-alpha-acetylglutamine; this is not direct NMR confirmation of the glutamate product. Glutamate activity is independently supported by enzyme assays and curated reaction evidence.

The enzyme was inhibited by L-arginine (IC50 26±3micromolar); the detailed inhibition assay used glutamine and acetyl-CoA. Analytical gel filtration showed “a mixture of equal amounts of a dimer and a tetramer.” Both existing oligomerization annotations are accepted as observed in vitro forms without asserting one obligatory native assembly. Cytoplasm is retained as phylogenetic/soluble metabolic localization, not direct target imaging.

Important source correction: the downloaded UniProt kinetic line says acetyl-CoA KM150mM; the primary paper says150micromolar. Do not propagate that thousandfold discrepancy. UniProt source remains unedited.

The primary authors propose native pathway priming and/or partner-assisted activity to explain poor glutamate affinity; neither efficient native flux, a particular activating partner nor N-acetylglutamine deamidation is established. Existing direct glutamate MF and arginine BP are retained with those limits. Broad N-acetyl/acyltransferase rows are refined to the supported glutamate-specific activity without denying glutamine promiscuity.

[PMID:17347518 Surprising arginine biosynthesis] supports the comparative short-NAGS architecture; fused ArgH-NAGS proteins are another implementation not represented by this target. UniProt and PANTHER ontology agree: PTHR43626 = ACYL-COA N-ACYLTRANSFERASE; SF4 = GCN5-RELATED N-ACETYLTRANSFERASE 2, CHLOROPLASTIC. These are broad family labels, not exclusive NAGS functional definitions; a module selector needs an exact member/GO function constraint or a free descriptor. The chloroplastic label does not imply bacterial organelle targeting.
