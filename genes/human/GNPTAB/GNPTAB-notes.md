# GNPTAB (GlcNAc-1-phosphotransferase alpha/beta subunits, UniProtKB:Q3T906) - review notes

Literature work for this review was done manually from the cached publications and
UniProt (no provider deep-research file was available when the review was written).

## Biology

- GNPTAB encodes the alpha/beta-subunit precursor of UDP-GlcNAc:lysosomal enzyme
  N-acetylglucosamine-1-phosphotransferase (EC 2.7.8.17), an alpha2beta2gamma2 hexamer
  (gamma = GNPTG) that catalyses the first step of mannose 6-phosphate (M6P) formation on
  high-mannose N-glycans of soluble lysosomal acid hydrolases in the Golgi
  [PMID:19955174 "mediates the first step in the synthesis of the mannose 6-phosphate
  recognition marker on lysosomal acid hydrolases"].
- The alpha/beta subunits are the catalytic subunits and also recognise the protein
  determinant on acid hydrolases [PMID:19955174 "the alpha/beta subunits recognize the protein
  determinant of acid hydrolases in addition to mediating the catalytic function of the
  transferase"]; the DMAP interaction domain is a substrate-recognition module
  [PMID:23733939], the Stealth domains harbour the catalytic site [PMID:25505245 "the Stealth
  domain harbors the catalytic site"].
- The precursor is a type III Golgi membrane protein cleaved by site-1 protease (MBTPS1)
  into alpha and beta subunits, which is required for activity
  [PMID:21719679 "Cleavage of the membrane-bound α/β-subunit precursor by an unknown protease is
  required for catalytic activity."]. The small Golgi membrane protein LYSET/TMEM251 binds
  GNPTAB and is required for its stability, cleavage and Golgi retention [PMID:36074821].
- GNPTG binds a dedicated GNPTG-binding domain on the alpha subunit
  [PMID:26385638 "we identified the binding regions of γ-subunits in a previously
  uncharacterized domain of α-subunits"].
- Location: Golgi membrane [PMID:16200072 "expression and localization of GNPTA in the Golgi
  apparatus, accompanied by the correction of hypersecretion of lysosomal enzymes"].

## Disease

Biallelic GNPTAB variants cause mucolipidosis II (I-cell disease; null alleles) and
mucolipidosis III alpha/beta (residual activity); hydrolases lacking M6P are hypersecreted
and lysosomes become deficient in many hydrolases [PMID:16200072 "Mucolipidosis II (ML II) is
a fatal lysosomal storage disorder resulting from defects in the multimeric
GlcNAc-1-phosphotransferase"].

## Curation decisions

- Core MF GO:0003976; core BP GO:0016256 N-glycan processing to lysosome (part_of
  GO:0006622 protein targeting to lysosome); location Golgi membrane; complex GO:0070622.
- High-throughput Y2H/AP-MS "protein binding" partners (ZNF250, AEN, PSMA1, FAM90A1,
  STAMBPL1, B3GALT2) have no functional support -> over-annotated. GNPTG and LYSET
  interactions are functionally meaningful but are better represented by the complex term
  and by LYSET's own annotations.
