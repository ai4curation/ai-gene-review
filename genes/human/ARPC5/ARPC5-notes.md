# ARPC5 (p16-Arc) review notes

## Sources
- Affinage: trust gates clear.
- Key papers:
  - PMID:11741539: peripheral to the p34-p20 core.
  - PMID:26655834: ARPC5 vs ARPC5L complex activity.
  - PMID:36662867 (full text): isoform protrusion differences.
  - PMID:37162507 (full text): ARPC5 drives cytoplasmic and ARPC5L nuclear actin in T cells.
  - PMID:37349293 (full text): biallelic loss causes an actinopathy.
- Handled consistently with the ARPC1B and ARPC4 reviews: structural constituent, cytosol (18 Reactome rows, per-row summaries), actin cytoskeleton and actin filament binding (contributes_to).
- IBA nodes: PTN000291131 (Arp2/3 complex, nucleation, adaptor, cortical cytoskeleton) and PTN000974138 (cell migration).
- The nucleus/DSB ISS donor is Xenopus arpc5-b (synonym arpc5l); noted in the propagation review.

## Decisions
- ACCEPT:
  - Arp2/3 complex and Arp2/3-mediated nucleation.
  - Structural constituent; actin filament binding (contributes_to).
  - Lamellipodium, actin cytoskeleton and cytosol.
- KEEP_AS_NON_CORE:
  - Cell migration (downstream outcome).
  - Regulation of actin filament polymerization, cortical cytoskeleton, adaptor (yeast-seeded, intra-complex).
  - Cytoplasm, actin cytoskeleton organization, cytoskeleton.
  - Nucleus/DSB (nuclear actin is ARPC5L-type in T cells).
  - Focal adhesion, neutrophil granule/extracellular rows, exosome.
- REMOVE: ARPC4 protein binding (intra-complex; policy).
