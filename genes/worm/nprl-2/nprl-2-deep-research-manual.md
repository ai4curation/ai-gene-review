# nprl-2 (C. elegans, F49E8.1; UniProt W6RQZ3) - manual literature review

No deep-research API was available for this review. This file records a manual
literature survey done from the cached publications in `publications/` and PubMed
searches (query: `(nprl-2 OR NPRL2 OR "nprl-3" OR GATOR1) AND "Caenorhabditis elegans"`,
5 hits: PMID:32287270, PMID:31594908, PMID:30192747, PMID:29769719, PMID:26109047;
plus PMID:23705068 supplied as the key paper).

## Identity and family

- W6RQZ3 is an unreviewed TrEMBL entry, 451 aa, gene `nprl-2`, ORF F49E8.1
  (WormBase WBGene00018635, GeneID 177532). UniProt: "Belongs to the NPR2 family"
  (ARBA-only evidence), Pfam PF06218 NPR2, InterPro IPR009348 NPR2-like, PANTHER
  PTHR12991:SF10 "GATOR COMPLEX PROTEIN NPRL2".
- It is the single C. elegans member of the NPR2/NPRL2 family, i.e. the ortholog of
  yeast Npr2, Drosophila Nprl2 and human NPRL2 (GATOR1 subunit).

## Conserved function of the family (from orthologs)

- Human GATOR1 (DEPDC5, NPRL2, NPRL3) is a negative regulator of the Rag GTPases and
  of amino-acid signalling to mTORC1: [PMID:23723238 "Inhibition of GATOR1 subunits
  (DEPDC5, Nprl2, and Nprl3) makes mTORC1 signaling resistant to amino acid
  deprivation."] and [PMID:23723238 "GATOR1 has GTPase-activating protein (GAP)
  activity for RagA and RagB"]. (Abstract only in cache.)
- Cryo-EM of GATOR1: [PMID:29590090 "NPRL2 links DEPDC5 and NPRL3, and DEPDC5
  contacts the Rag GTPase heterodimer"] and [PMID:29590090 "weaker interactions
  between the NPRL2-NPRL3 heterodimer and RAGA execute GAP activity"]. The GAP
  activity is thus a property of the complex, executed through the NPRL2-NPRL3
  heterodimer, so for a single subunit it is `contributes_to`. (Abstract only.)
- Lysosomal recruitment of mammalian GATOR1 by KICSTOR: [PMID:28199306 "KICSTOR
  localizes to lysosomes; binds and recruits GATOR1, but not GATOR2, to the lysosomal
  surface"].
- Drosophila: [PMID:24786828 "Nprl2 and Nprl3 physically interact and are targeted
  to lysosomes and autolysosomes"].

## C. elegans experimental literature

### Zhu et al. 2013 eLife (PMID:23705068; full text read)

- Screen for suppressors of the L1 arrest of mmBCFA-deficient `elo-5(-)` animals
  identified `nprl-3(ku540)`; RNAi of `nprl-2` phenocopied it:
  [PMID:23705068 "nprl-2 dsRNA injection also rescued 42.4% of elo-5(−) animals to or
  beyond L3 stage (n = 128)."]
- Authors' interpretation: [PMID:23705068 "This suggested that NPRL-2 and NPRL-3 in C.
  elegans may also function in a complex to negatively impact
  mmBCFA/d17iso-GlcCer-mediated L1 growth."]
- TORC1 dependency was tested with `nprl-3(ku540)` (raga-1, rheb-1, rsks-1, ife-2
  RNAi reverse the suppression), not with `nprl-2`; conclusion stated jointly:
  [PMID:23705068 "These results led to the conclusion that TORC1 acts downstream of
  d17iso-GlcCer to promote L1 growth and development and that this activity is
  negatively regulated by NPRL-2/3."]
- No biochemical, localization or complex-membership data for NPRL-2 itself; the
  complex is inferred from the yeast Npr2/Npr3 heterodimer.

### Zhu et al. 2015 Genes Dev (PMID:26109047)

- Follow-up focused on `nprl-3(lf)`: [PMID:26109047 "In addition, we showed that the
  NPRL-2/3 complex negatively regulates this lipid-promoted TORC1 activity (Zhu et
  al."]; the paper proposes that NPRL-3 represses intestinal TORC1 partly via apical
  membrane polarity, and notes this as distinct from the mammalian Rag-GAP role.
  `nprl-2` itself not separately assayed in the passages examined.

### Schmeisser et al. 2019 PLoS Genet (PMID:30192747)

- Neuronal ANMT-1 (NNMT ortholog) competes with LCMT-1 for SAM; reduced LET-92/PP2A
  methylation is proposed to leave NPRL-2 phosphorylated and induce autophagy:
  [PMID:30192747 "This leads to decreased methylation and activity of LET-92, which can
  no longer dephosphorylate NPRL-2, thus inducing autophagy."]
- `nprl-2` RNAi lowered basal and starvation-induced autophagy (mCherry::LGG-1
  puncta): [PMID:30192747 "a downregulation of basal autophagy under feeding conditions
  compared to the control RNAi was found"]. The NPRL-2 phosphorylation step is a model
  borrowed from yeast; no direct phospho-assay of worm NPRL-2 was found in the text
  examined.

### Other hits

- PMID:31594908 (TOR signalling in C. elegans review), PMID:29769719 (KLHL22, human
  DEPDC5), PMID:32287270 (SESN2 mitochondrial localization): no nprl-2-specific
  experimental data relevant to GO annotation.

## Synthesis

nprl-2 encodes the C. elegans NPRL2 ortholog, a predicted GATOR1 subunit. Worm data
are genetic only: reducing nprl-2 bypasses a lipid (d17iso-GlcCer)-dependent
TORC1-requiring L1 growth checkpoint, as does loss of nprl-3; and nprl-2 RNAi reduces
autophagy in some contexts. The molecular function (contribution to Rag GAP activity
within GATOR1) and lysosomal-surface location are inferred from orthologs.
