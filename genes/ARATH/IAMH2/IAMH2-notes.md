# IAMH2 (AT4G37560) curation notes

## Identity

- Locus AT4G37560; UniProt F4JS40 (unreviewed TrEMBL, 452 aa; reference proteome UP000006548).
  Other UniProt entries for the same locus: Q8H1G4, Q94CA8 (both 452 aa) and A0A1P8B392 (413 aa,
  alternative Araport11 gene model). F4JS40 was used because it carries TAIR's GO annotations.
- Symbol IAMH2 (INDOLE-3-ACETAMIDE HYDROLASE 2) was assigned by Gao et al. 2020
  [PMID:32327358 "We named At4g37560 IAMH2."]. Natural-variation locus name LA1 (LIGHT ADAPTATION 1)
  [PMID:42844995 "we identified the major locus LA1 (Light Adaptation 1) and pinpointed IAMH2 as the causal gene"].
- Tandem paralog of IAMH1 (AT4G37550) [PMID:32327358 "IAMH2 and IAMH1 share 90% amino acid sequence identity."].

## Domain / family

- Pfam PF03069 FmdA_AmdA; InterPro IPR004304 (FmdA_AmdA), IPR054833 (FormamaseFmdA);
  PANTHER PTHR31891:SF1 "FORMAMIDASE C869.04-RELATED" (from IAMH2-uniprot.txt). The acetamidase/formamidase
  family is distinct from the amidase-signature family that contains AMI1 (AT1G08980), the other
  Arabidopsis enzyme reported to hydrolyse IAM.
- Gao et al. identified the gene from family membership:
  [PMID:32327358 "At4g37550 and At4g37560 encode putative Acetamidase/Formamidases, which potentially have the hydrolase activities that can break an amide bond."]

## Deep research

Automated deep research (`just deep-research-falcon ARATH IAMH2 --fallback perplexity-lite`) failed in this
session: no provider API keys were available ("Provider 'perplexity' not available"). The literature
was searched manually through PubMed (queries "IAMH1 IAMH2 indole-3-acetamide hydrolase Arabidopsis" and
"At4g37560 OR IAMH2 Arabidopsis", 2026-10-21). Only two primary papers deal with IAMH2 function,
PMID:32327358 and PMID:42844995; both are cached with full text.

## Function evidence

### Gao et al. 2020 (PMID:32327358), genetics plus auxin metabolite profiling
- iamh2-1 (T-DNA) single mutant is IAM-resistant:
  [PMID:32327358 "iamh2–1 had short hypocotyls and normal cotyledons when grown on 20 μM IAM whereas wild type plants developed long hypocotyls and epinastic cotyledons, demonstrating that disruption of IAMH2 also led to IAM resistance."]
- CRISPR iamh1 iamh2 double mutants (iamh2-2, iamh2-3) suppress the iaaM overexpression phenotype:
  [PMID:32327358 "When we introduced the same construct into iamh1–1 iamh2–3, the auxin overproduction phenotypes disappeared"]
- In the double mutant, IAM no longer raises IAA conjugates much:
  [PMID:32327358 "In contrast, IAM treatment in iamh1 iamh2 double mutants did not induce a substantial increase in IAA-Asp and IAA-Glu conjugates"]
- The authors' conclusion is that the IAMHs are the main IAM to IAA enzymes:
  [PMID:32327358 "suggesting that the IAMHs are the main enzymes in converting IAM into IAA in Arabidopsis."]
- Steady-state IAA is unchanged in the double mutant, and there is no developmental phenotype under
  standard conditions:
  [PMID:32327358 "The iamh1 iamh2 double mutants did not display obvious developmental defects under our normal growth conditions, suggesting that auxin synthesized from the IAM pathway may not play critical roles in Arabidopsis development."]
- The block is incomplete, so other amidases (e.g. AMI1) may contribute:
  [PMID:32327358 "However, we noticed that iamh1 iamh2 double mutants were not entirely insensitive to IAM"]
- Caveat: I found no in vitro enzyme assay of purified IAMH1 or IAMH2 in this paper. The IAM-hydrolase
  activity is inferred from mutant metabolite profiles and family membership.
- The expression (IAMH1pro:GUS) and localization (IAMH1-GFP, "not expressed in the nucleus") data are for
  IAMH1, not IAMH2.

### X. Gao et al. 2026 (PMID:42844995), natural variation and light adaptation
- The user supplied the PDF; it matches the cached PMC full text.
- The iamh2 T-DNA mutant SALK_208590C has short hypocotyls under low light:
  [PMID:42844995 "This genetic evidence confirms that IAMH2 is a positive regulator of hypocotyl elongation, likely by modulating auxin homeostasis in response to light cues."]
- Endogenous auxin metabolites in dissected hypocotyls (in vivo evidence that IAMH2 contributes to the
  IAA pool, with no exogenous IAM):
  [PMID:42844995 "Under low‐light conditions, IAA levels were significantly lower in iamh2 than in Col‐0, whereas under normal light, the reduction was not statistically significant (Figure 2H)."]
  [PMID:42844995 "IAM levels were significantly elevated in the mutant under normal light (Figure 2H), consistent with reduced IAM hydrolysis upon loss of IAMH2."]
  [PMID:42844995 "These data indicate that IAMH2 contributes to the hypocotyl IAA pool, particularly under low light."]
- The 3' UTR poly(U) motif is bound by the CCCH zinc-finger proteins C3H14 and C3H15, which repress IAMH2
  mRNA. The Tibet allele carries a structural variant that disrupts this motif and escapes repression:
  [PMID:42844995 "IAMH2 expression was significantly elevated in the mutant compared with Col‐0 under both normal and low light (Figure 4H), demonstrating that C3H14 and C3H15 repress endogenous IAMH2 expression."]
  [PMID:42844995 "Under low light, the triple mutant exhibited hypocotyl lengths comparable to those of the iamh2 single mutant (Figure 4I, J), indicating that IAMH2 is epistatic to C3H14 and C3H15."]
- The coding sequence differs little between the alleles:
  [PMID:42844995 "While three amino acid substitutions were found in the coding sequence, none were located within functional domains or predicted to affect protein structure (Figure S6)."]
- Non-redundancy with IAMH1 under low light (added after the automated PR review, 2026-10-22):
  [PMID:42844995 "IAMH1 was upregulated in the iamh2 mutant under low light (Figure S8A), indicating partial compensation."]
  [PMID:42844995 "However, only IAMH2 was light‐responsive in Col‐0 (Figure S8B), and this compensation did not restore hypocotyl elongation, suggesting that IAMH2 plays a non‐redundant role in this context."]
  The core function now says IAMH2 is redundant with IAMH1 for exogenous or iaaM-derived IAM, but
  non-redundant for the low-light hypocotyl IAA pool.
- Light conditions of the metabolite data: IAA is significantly lower in iamh2 hypocotyls under low light
  only, and IAM is significantly elevated under normal light (Figure 2H). An earlier version of the review
  description put both under low light; that was corrected.
- Pathway caveat: the paper cites Moya-Cuevas et al. 2026 as questioning whether the IAM pathway contributes
  to auxin biosynthesis under standard conditions, and proposes that the pathway is conditionally recruited
  under low light:
  [PMID:42844995 "We therefore propose that the IAM pathway is not essential for basal auxin homeostasis, but is conditionally recruited under low‐light stress to provide local IAA for adaptive growth."]
  I resolved that citation through PubMed to PMID:41362017 (New Phytol 249:2452-2466) and read the full
  text. It does not mention the IAMHs; it proposes that IAM also signals through ABA. It qualifies but
  does not refute the IAM-to-IAA role, so the NEW GO:0009684 annotation is kept with the caveat.
- The regulation by C3H14/C3H15 acts on the IAMH2 transcript; it is not an activity of the IAMH2 protein,
  so it is not a GO annotation for IAMH2.

## GO annotation decisions (summary)

- GO:0016811 (IEA, InterPro2GO): correct but general. MODIFY to GO:0043864 indoleacetamide hydrolase
  activity, which is_a GO:0004040 amidase activity, under GO:0016811 (OLS ancestors checked 2026-10-22).
- GO:0005829 cytosol (HDA, Aryal et al. 2014 cytosolic-fraction SEC proteomics): ACCEPT. It fits a
  soluble enzyme with no predicted targeting signal; the IAMH1-GFP signal was not nuclear.
- NEW GO:0009684 indoleacetic acid biosynthetic process (IMP, PMID:42844995 endogenous IAA/IAM data;
  also PMID:32327358).
  - Participation test: IAMH2 is proposed to catalyse the last step, IAM to IAA.
  - Comparator check (QuickGO, taxon 3702, 2026-10-22): AMI1 (Q9FR37), which catalyses the same IAM to
    IAA step, carries GO:0043864 (IDA) and GO:0009684 (IDA). TAA1, YUC7, CYP79B2 and SUR1 carry
    GO:0009684 (IMP).
- I did not propose a hypocotyl-elongation process term. No "hypocotyl elongation" GO term was found in
  OLS, and the phenotype is an indirect, auxin-dependent consequence.

## Open questions
- Is there direct biochemical evidence (purified IAMH2 kinetics) for IAM hydrolysis, and does IAMH2 also
  hydrolyse formamide or acetamide, as the family name suggests?
- What is the endogenous source of IAM in Arabidopsis hypocotyls (IAOx-derived? CYP79B2/B3-dependent)?
