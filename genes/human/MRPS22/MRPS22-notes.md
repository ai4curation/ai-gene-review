# MRPS22 (mS22) curation notes

## Deep research
`MRPS22-deep-research-claude-code.md` ran for 33 s with 2 web searches (`web_search_requests: 2`) and 7 citations.
It is thin: it flags several statements as unverified background knowledge, and it misattributes PMID:25838379
(Amunts et al. 2015, not Greber & Ban). Used only as leads; it pointed to the Smits et al. 2011 report, which was
fetched and read (PMID:21189481, full text).

## Evidence
- Identified as a 28S small-subunit protein by proteomics of purified mammalian mitoribosomal small subunits
  [PMID:10938081 "Mammalian mitochondrial small subunit ribosomal proteins were separated by two-dimensional polyacrylamide gel electrophoresis"].
- Present in the human mitoribosome cryo-EM structure; UniProt SUBUNIT "Component of the mitochondrial small ribosomal subunit (mt-SSU)" cites PMID:25838379.
- COXPD5 (Saada et al. 2007): "Marked reduction of 12s rRNA, the core of the mitochondrial small ribosomal subunit, was found in fibroblasts";
  "Transfection of the patient cells with wild-type MRPS22 cDNA increased the 12s rRNA content and normalised the enzymatic activities" [PMID:17873122].
- Smits et al. 2011, Leu215Pro: "Analysis of mitochondrial protein synthesis revealed a marked impairment in mitochondrial translation" [PMID:21189481];
  their discussion cites an earlier finding that "a MRPS22 defect was shown to strongly hamper assembly of the small ribosomal subunit".
- ODG7 (Chen et al. 2018): POI variants p.R135Q and p.R202H; p.R202H fibroblasts showed "no differences ... in the expression levels of the 12S and 16S rRNA";
  "complete deficiency of Mrps22 results in embryonic lethality"; Drosophila mRpS22 knockdown in germ cells gives agametic ovaries [PMID:29566152].

## Decisions
- Structural constituent of ribosome, mitochondrial small ribosomal subunit and mitochondrial translation: ACCEPT (core).
- Protein binding (MRPS18B, a fellow small-subunit protein, from crosslinking-MS and BioPlex): REMOVE as uninformative.
- Mitochondrial inner membrane (Reactome TAS and NAS): KEEP_AS_NON_CORE, consistent with MRPS7 and PTCD3.
- No NEW terms. Ovarian/germ-cell development is a necessity phenotype of loss of mitochondrial translation, not
  participation, so no oogenesis term was proposed. Mitochondrial small ribosomal subunit assembly (GO:0180026) was
  considered but not added: the assembly evidence is second-hand (cited in Smits 2011) and the sibling MRPS7 review did
  not add it either.
