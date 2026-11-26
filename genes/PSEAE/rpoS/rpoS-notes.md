# rpoS (PA3622, P45684) review notes

## Literature

Search (Europe PMC REST, 2026-11-05: `TITLE:rpoS AND TITLE:aeruginosa`, 30 hits read as
titles). Papers used:

1. Suh et al. 1999 [PMID:10383954], full text cached. PAO1 rpoS mutant phenotypes:
   hypersensitive to heat shock, osmolarity and prolonged H2O2 [PMID:10383954 "In
   addition, the PAO1 rpoS mutant was hypersensitive to heat shock at 50°C, increased
   osmolarity, and prolonged exposure to high concentrations of H 2 O 2 ."]; 60% less
   catalase; less exotoxin A; more pyocyanin and pyoverdine; altered twitching; much less
   alginate in FRD1. I searched the full text for transcription assays (lacZ fusions,
   primer extension, RT-PCR, in vitro transcription, gel shift): none; the only mRNA
   mention is background on rpoS's own expression. All data are mutant phenotypes.
2. Hong et al. 2005 [PMID:15687221], abstract only. rpoS deletion abolishes Aer-2-mediated
   aerotaxis; cheY2-cheA2-cheW2-aer-2 transcribed RpoS-dependently.
3. Irie et al. 2010 [PMID:20735777], full text cached. RpoS is a positive transcriptional
   regulator of psl; psl -10 matches the RpoS consensus.
4. Bouillet et al. 2019 [PMID:31019225], full text cached. HsbR anti-sigma domain binds
   RpoS (bacterial two-hybrid) [PMID:31019225 "Clearly, HsbRD3 interacted with RpoS from
   P. aeruginosa as well as with CrsR."]; RpoS acts downstream of HptB in biofilm control.
5. PMID:37328957 (abstract only): RssB and
   RssC needed for ClpXP-dependent RpoS degradation in P. aeruginosa.

UniProt P45684 (reviewed): sigma-70 family, RpoS subfamily (HAMAP MF_00959); regions 1-4;
H-T-H 293-312.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000779307 | GO:0006355 regulation of DNA-templated transcription | 7 | 419 (77 taxa) | GO:0006355, IDA, PMID:10383954 (PseudoCAP) | INDIRECT-PHENOTYPE (term true, evidence code wrong) | Full text read: only mutant phenotypes (stress sensitivity, catalase, exoproducts, twitching, alginate), no transcription measurement. The claim is true of a sigma factor, but the evidence is IMP at most. PSEUDOCAP WRONG_EVIDENCE_CODE defect, CONFIRMED. | E. coli RpoD (P00579), M. tuberculosis SigA (P9WGI5), Arabidopsis sigma factors (AT1G64860, AT2G36990, AT5G24120), rice SIG (Q0J7T6) | Yes; RpoD and SigA have direct transcription evidence. Term suits a sigma-70 clade. No GO_CENTRAL defect for this term. |

Other node-level issue (not this gene's seed): the GO:0003899 DNA-directed RNA polymerase
activity IBD at the same PTN000779307 node is seeded by one TAIR annotation of SIG3
(O24621, AT3G53920; IMP PMID:17175536 and ISS PMID:9280303, QuickGO 2026-11-05). Sigma
factors have no catalytic site; the activity belongs to the core enzyme. GO_CENTRAL defect
recorded on the rpoS GO:0003899 row (PROBABLE). algU and pvdS (ECF sigma factors, a
different node) do not carry this row.

## Consistency with algU/pvdS

Same treatment of sigma-factor rows: GO:0016987 ACCEPT, GO:0003700 TOO_GENERAL,
GO:0003677 KEEP_AS_NON_CORE, GO:0006352 and GO:2000142 ACCEPT, GO:0000976 MODIFY to
GO:0001046. One difference: algU/pvdS MODIFY GO:0006355 to GO:2000142, whereas this review
uses TOO_GENERAL because GO:2000142 is_a GO:0006355 and is accepted here (the convention
in the tier-2 brief). The claim is the same.

## Annotation decisions

Stress/virulence IMP rows (heat, oxidative, salt, secondary metabolite, motility,
chemotaxis, biofilm): KEEP_AS_NON_CORE; they are regulatory outputs of the RpoS regulon.
