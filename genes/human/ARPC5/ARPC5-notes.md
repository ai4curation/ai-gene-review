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

## 2026-10-04 review round (PR #4204)

- The ARPC5/ARPC5L split in nuclear actin depends on the stimulus, not the compartment [PMID:37162507 "Interestingly, nuclear actin polymerization triggered by a different stimulus, DNA replication stress, specifically requires ARPC5 but not ARPC5L."]. Nucleus rows are now ACCEPT; the DSB-site ISS row is non-core because the isoform at breaks is untested.
- Autoinhibitory tail: [PMID:40042350 "The structures reveal that NPF binding to Arp2 is allosterically linked to the release of ArpC5's N-terminal tail from Arp2 ..."].
- PMID:22447776 (mouse Arpc5 as a germ-cell translational suppressor) is set aside. It is a single mouse study of a non-cytoskeletal role in spermatids, it has no human data, and it has no GOA row. It is recorded as LOW relevance.
