# PAINT, PTHR31646: mannan biosynthesis IBD seeded only by Candida reaches algae, oomycetes and choanoflagellates

**Destination:** PAINT curators (GO annotation tracker, label PAINT).

**Summary.** Node PTN001270341 in the MNN2-type alpha-1,2-mannosyltransferase
family PTHR31646 carries an IBD for GO:0046354 mannan biosynthetic process.
In QuickGO on 2026-10-01:
- All 56 IBA rows from this node list the same six *Candida albicans* (CGD)
  seed genes.
- The term reaches 129 proteins from this node, IBA and TreeGrafter IEA
  combined.

| Taxon | IBA rows |
|---|---:|
| *Phytophthora ramorum* (oomycete) | 22 |
| *Klebsormidium nitens* (green alga) | 8 |
| *Chlamydomonas reinhardtii* (green alga) | 3 |
| other taxa | 23 |

By TreeGrafter it also reaches the choanoflagellate *S. rosetta* couscous
(F2UJ78).

**Why it is a problem.** GO defines GO:0046354 as the biosynthesis of mannan,
"the main hemicellulose of soft (coniferous) wood". Fungal Mnn2-family enzymes
build the mannan outer chains of cell-wall mannoproteins, a different product.
Nothing suggests that oomycetes, chlorophyte algae or choanoflagellates make
either. *S. rosetta* couscous modifies the basal extracellular matrix of
rosettes (PMID:30556809).

**Requested change.**
- Restrict the GO:0046354 IBD to the fungal clade.
- Check whether the *Candida* seeds themselves should use a cell-wall
  mannoprotein term rather than GO:0046354.

**Repo references.** `genes/SALRS/couscous/couscous-ai-review.yaml` (REMOVE).
