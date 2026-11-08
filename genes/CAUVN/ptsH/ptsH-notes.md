
## 2026-11-07 manual primary-source review

Reviewed all 6 original rows in order; no NEW row or lifecycle change. Target A0A0H3C344 is NA1000 (taxon 565050), not CB15. PMID27109061 explicitly identifies the relevant CCNA loci and uses NA1000-derived Caulobacter strains. Its bacterial two-hybrid experiments use E. coli hosts; H66E is a phosphomimetic. Read canonical full PMID27109061 and, for PtsP, full PMID26489861.

HPr (CCNA_00241) is the small histidine phosphocarrier of the nitrogen-responsive PtsP–HPr–PtsN relay in Caulobacter vibrioides NA1000. It accepts and transfers phosphoryl groups through a conserved histidine and couples upstream PtsP signaling to PtsN. Native genetic and phosphostate studies and heterologous phosphorelay complementation support this role. HPr also influences (p)ppGpp production through an incompletely resolved branch; the tested two-hybrid assay did not detect HPr–SpoT binding. Its established role is regulatory rather than mannose uptake.

Current GO definitions distinguish sugar-coupled transport from regulatory phosphotransfer. GO0016775 describes a nitrogenous acceptor; it is a transferase descendant but not a kinase descendant. Thus HPr's kinase refinement is lateral, without an unsupported assertion that all kinases require ATP. No ATP-specific or response-regulator kinase term is substituted. The cytoplasmic interpretation, where retained, is mechanistic inference, not ARBA evidence or a resolved microscopy/fractionation result.

No independent gene provider report is fabricated. Root's shared module Falcon attempt failed with HTTP403 authentication (sanitized receipt in acquisition-20261107/module-falcon-attempt.json); these are manual notes. Available official tree receipts do not locate the exact NA1000 accessions, so no CB15 replacement, target loss, or loss-free lineage is asserted. PtsN kinase activation remains genuinely unresolved beyond the measured SpoT output.

No process proposal was added merely to populate the module. Gene core activities summarize independently supported chemistry/regulation even when no suitable existing annotation carries it; intentional coverage warnings should not trigger invented NEW rows.


## 2026-11-08 — consistent Ntr/sugar scope and evidence limits

The action discriminator is target evidence, not species labels or donor count: P. putida has a native sugar-independent route and a documented failure of PtsN to replace fructose EIIA; Caulobacter separates its Ntr effectors from sugar permeases and its mannose assignments originate in an incorrect transporter EC mapping. E. coli has measured cross-system phosphate exchange in vitro but lacks demonstrated native sugar-uptake participation for the Ntr branch, so physiological process assignment is over-annotation rather than an absolute negative. Bona fide E. coli/Bacillus HPr controls retain the sugar process because they feed sugar-specific EIIA proteins in the native carbohydrate route; common ancestry at PTN002135312 does not erase this functional divergence.

Where the only localization assertion is ARBA-derived, compartment adjudication remains UNDECIDED and the core location is omitted. PtsN–KdpD target interaction plus regulatory output supports direction-neutral regulator inference without claiming an isolated kinase assay. Source annotation payloads are unchanged.
