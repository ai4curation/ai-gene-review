# algD Deep Research Manual Summary

## Identification

AlgD in *Pseudomonas putida* KT2440 (UniProt `Q88NC4`, locus `PP_1288`) is annotated in UniProt as GDP-mannose 6-dehydrogenase / GMD, EC 1.1.1.132, a member of the UDP-glucose/GDP-mannose dehydrogenase family with an NAD(P)-binding Rossmann-like domain.

## Molecular Function

The most defensible direct function assignment is GDP-mannose 6-dehydrogenase activity. UniProt states that AlgD catalyzes oxidation of GDP-D-mannose to GDP-D-mannuronic acid, matching the specific GO catalytic term and the broader oxidoreductase parent term. The presence of an NAD(P)-binding Rossmann-like domain and annotated NAD(+) binding residues supports the NAD-binding annotation.

## Biological Process

AlgD is directly involved in alginate biosynthesis because it generates GDP-mannuronate, the committed precursor for alginate polymerization. In KT2440-specific literature, alginate production and alginate-gene expression are most prominent under water-limiting / matric-stress conditions rather than as a uniformly dominant biofilm matrix program across all conditions.

Chang et al. 2007 showed that alginate production rises under matric stress, that alginate changes biofilm architecture, and that alginate deficiency reduces desiccation survival. Li et al. 2010 found transient induction of alginate biosynthesis genes, including the `algD` operon context, during dehydration in KT2440 biofilms. Gülez et al. 2012 found early upregulation of alginate genes during water stress. Nilsson et al. 2011, however, found that the `alg` cluster played only a minor role in KT2440 biofilm formation and stability under their tested standard conditions.

## Curation Conclusion

The existing GOA annotations are broadly sound:

- `GO:0047919` GDP-mannose 6-dehydrogenase activity: core catalytic function, accept.
- `GO:0016616` oxidoreductase activity, acting on the CH-OH group of donors, NAD or NADP as acceptor: correct mechanistic parent term, accept.
- `GO:0051287` NAD binding: valid cofactor-binding support term, accept.
- `GO:0042121` alginic acid biosynthetic process: accept, but note that the physiological importance of alginate in KT2440 is condition dependent and strongest under water limitation.

I do not see a strong case for adding broader downstream phenotype/process terms such as generic biofilm formation or stress response as core annotations, because the evidence is contextual and mediated through alginate production rather than a separate direct role for AlgD itself.
