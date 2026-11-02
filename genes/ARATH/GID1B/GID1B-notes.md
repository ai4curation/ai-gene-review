# GID1B (At3g63010, UniProt Q9LYC1) curation notes

## Identity
- UniProt Q9LYC1 GID1B_ARATH, "Gibberellin receptor GID1B"; synonyms CXE14, GID1L2; locus At3g63010. Verified in GID1B-uniprot.txt.
- PANTHER PTHR23024:SF98 (GIBBERELLIN RECEPTOR GID1B) within PTHR23024 (ARYLACETAMIDE DEACETYLASE).

## Key findings (with provenance)
- All three AtGID1s bind GA, highest affinity for GA4; GID1B is ~10-fold higher affinity with narrow pH range [PMID:16709201 "AtGID1b was unique in its binding affinity to GA(4) and in its pH dependence when compared with the other two"].
- GA-dependent DELLA interaction in yeast [PMID:16709201 "A two-hybrid yeast system only showed in vivo interaction in the presence of GA(4) between each AtGID1 and the Arabidopsis DELLA proteins (AtDELLAs), negative regulators of GA signaling"].
- Receptor function: each AtGID1 rescues rice gid1-1 [PMID:16709201 "These results demonstrate that all three AtGID1s functioned as GA receptors in Arabidopsis"].
- Triple mutant is GA-insensitive [PMID:17521411 "the triple knockout seedlings completely lost their ability to respond to exogenously applied GA"]; gid1a gid1b has short stamens and low fertility [PMID:17521411 "The stamens of the double knockout mutant atgid1a atgid1b were significantly shorter than those of the wild-type, and this leads to low fertility"].
- Positive regulators of GA signaling [PMID:17194763 "GID1a, GID1b, and GID1c function as positive regulators of the GA-signaling cascade in Arabidopsis"].
- No hydrolase activity in GID1 receptors [PMID:24961590 "GID1 was first described in rice as a nuclear localized protein similar to hormone-sensitive lipase family without hydrolase activity"].
- Fruit/ovule: GID1B mainly in ovules/funiculi; gid1a gid1b reduced seed-set with WT pollen [PMID:24961590 "However, we found that the double mutant gid1a gid1b, which does not have GID1 activity in ovules, showed reduced seed-set even when fertilized by WT pollen"].
- GID1B overexpression relieves sly1-2 seed dormancy without DELLA proteolysis [PMID:23818171 "GID1b overexpression rescues sly1-2 germination through proteolysis-independent DELLA down-regulation"].
- GID1b transcript rises with after-ripening [PMID:26136598 "Partial after-ripening resulted in increased GID1b, but not GID1a or GID1c mRNA levels"].
- Separate eudicot GID1b clade; GID1b cannot replace GID1ac in germination [PMID:21778177 "GA signalling via the GID1ac receptors is required for Arabidopsis seed germination, GID1b cannot compensate for the impaired germination of the gid1agid1c mutant"].
- Falcon deep research (GID1B-deep-research-falcon.md) adds: Yamamoto et al. 2010 Plant Cell (GA-independent GID1B-GAI binding in yeast, loop swap) and root-biased function; not cached as PMIDs here.

## Curation decisions
- Hydrolase activity (IEA InterPro, IBA PTN009058710): REMOVE, pseudoenzyme over-propagation.
- NOT response to gibberellin (CAFA IMP/IGI, PMID:24961590): REMOVE; negation based on absence of phenotype in mutants retaining redundant paralogs, contradicted by receptor biochemistry.
- Negative regulation of gene expression (IGI): over-annotation (feedback up-regulation of GID1A in gid1b gid1c).
- Protein binding rows: REMOVE per protein-binding policy; the PMID:19429606 (FRIGIDA) row is also REMOVE (2026-10-06), with a note that the cached text never mentions GID1/DELLA (probable IntAct reference mismatch).
- Core: GO:0010331 gibberellin binding; GO:0010476; nucleus. Proposed NTR "gibberellin receptor activity" (as in GID1A).
