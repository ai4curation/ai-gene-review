# PSMB5 notes

PSMB5 encodes proteasome subunit beta type-5, the constitutive beta5 catalytic
subunit of the 20S proteasome core. Unlike PSMA1, PSMB5 should receive direct
enzyme-function attribution because it carries the mature beta5 active site.

Evidence summary:

- The eukaryotic 26S proteasome contains a 20S core particle of 28 subunits capped
  by 19S regulatory particles [PMID:23495936 "barrel-shaped proteolytic 20S core
  particle (CP) of 28 subunits"].
- The beta1, beta2, and beta5 subunits carry the core proteolytic active sites
  [PMID:23495936 "The β1, β2, and β5 subunits contain the proteolytic active sites"].
- PSMB5's UniProt feature table identifies residues 1-59 as a removed propeptide and
  Thr60 as the nucleophilic active site [genes/human/PSMB5/PSMB5-uniprot.txt
  "ACT_SITE        60"].
- Human 20S proteasome activity assays support multicatalytic protease activity
  [PMID:27176742 "The proteasome is a multicatalytic protease responsible for the
  degradation of misfolded proteins"].
- Structural and inhibitor studies support beta5 chymotrypsin-like activity and
  inhibitor-pocket interpretation [PMID:18565852 "marked changes in chymotrypsin-like
  proteasome activity"; PMID:25599644 "selectivity for chymotrypsin-like sites"].
- AKIRIN2-mediated nuclear import supports nuclear localization/active-location
  annotations for assembled proteasomes [PMID:34711951 "directly bind to fully
  assembled 20S proteasomes to mediate their nuclear import"].

Curation decisions:

- Accept threonine-type endopeptidase activity as the core molecular function.
- Modify broader peptidase/endopeptidase/proteolysis annotations to the more specific
  threonine-type endopeptidase or proteasomal protein catabolic process terms.
- Accept specific 20S beta/core complex membership annotations.
- Keep cytosol, cytoplasm, nucleus, nucleoplasm, and other localization annotations as
  non-core context.
- Keep proteasome assembly as non-core context: PSMB5 maturation and incorporation are
  real, but the mature gene product's main role is beta5 proteolysis.
- Mark generic protein binding and pathway-level exports such as DNA repair, apoptosis,
  spermatogenesis, and immune response as over-annotated for the individual PSMB5
  subunit.
