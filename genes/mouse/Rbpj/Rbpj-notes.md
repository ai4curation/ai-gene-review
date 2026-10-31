# Rbpj (mouse) review notes

UniProt P31266 (SUH_MOUSE), Recombining binding protein suppressor of hairless (RBP-Jkappa, CSL/CBF1),
526 aa. PANTHER PTHR10665 (RECOMBINING BINDING PROTEIN SUPPRESSOR OF HAIRLESS). MGI:96522.
Notch-module role: **CSL — the DNA-binding nuclear effector of canonical Notch signalling**.

## Molecular function
- Sequence-specific DNA-binding TF (CGTGGGAA)
  [PMID:8749394 "The mammalian transcription factor RBP-J kappa binds to the DNA sequence motif CGTGGGAA and is involved in the regulation of gene expression"]
- Binds the Notch1 intracellular RAM domain directly
  [PMID:8749394 "RBP-J kappa and Su(H) bind directly to the RAM23 regions of mouse Notch1 and Drosophila Notch, respectively."]
- Interacts with all four mouse Notch proteins (as opposed to paralog RBP-L/Rbpjl)
  [PMID:9111338 "Surprisingly, RBP-L did not interact with any of the known four mouse Notch proteins."]
- Repressor-to-activator switch; RAM binding creates Mastermind docking site
  [PMID:18381292 "CSL is converted from a repressor to an activator through the formation of the CSL-NotchIC-Mastermind ternary complex."]
- Repression in absence of NICD through corepressors (SHARP/CtIP/CtBP, KyoT2, L3MBTL3-KDM1A)
  [PMID:16287852 "In the absence of Notch, RBP-Jkappa represses Notch target genes through the recruitment of a corepressor complex."]
  [PMID:24290140 "CSL dually functions as an activator and a repressor of transcription through differential interactions with coactivator or corepressor proteins, respectively."]
  [PMID:29030483 "L3MBTL3 competes with NOTCH ICD for binding to RBPJ"]
- Notch-independent role: component of PTF1-J trimeric complex with Ptf1a/E-protein in early pancreas
  [PMID:17938243 "active PTF1a requires interaction with RBPJ, the vertebrate Suppressor of Hairless, within a stable trimeric DNA-binding complex (PTF1)."]
  Later replaced by the pancreas-restricted paralog Rbpjl (constitutively active, Notch-independent).
- Baf60c stabilises NICD-RBP-J interactions [PMID:17210915].

## Biological process
- Required for essentially all canonical Notch signalling; knockout phenocopies Notch1 null
  [PMID:8749394 "in the mouse, the phenotypes of homozygous mutant Notch1 embryos are very similar to those of homozygous mutant RBP-J kappa embryos."]
- Direct Notch target enhancers contain RBP-J sites, e.g. Nodal node enhancer [PMID:12730124].
- Many developmental IMP annotations (heart, vasculature, somitogenesis, skin, immune cells, testis,
  pancreas, etc.) reflect loss of Notch signalling in those tissues: pleiotropic consequences, kept as
  non-core.

## Pathway-variant relevance
- Mammals have one CSL (Rbpj) + tissue-restricted paralog Rbpjl (lung/pancreas) that does not bind Notch
  [PMID:9111338]. Rbpj also functions Notch-independently in PTF1-J.
- Zebrafish has rbpja/rbpjb; Drosophila Su(H); C. elegans lag-1.

## Deep research
Falcon deep research completed (Rbpj-deep-research-falcon.md; wrapper reported a 600 s timeout but the
falcon client finished and wrote the file). Consistent with the above
[file:mouse/Rbpj/Rbpj-deep-research-falcon.md "Rbpj encodes a sequence-specific DNA-binding transcription factor that serves as the central nuclear mediator of canonical Notch signaling in mammals"].

## 2026-10-12 Ortholog/family audit (Dll1, Dll3, Hes7, Rbpj)

- GOA refreshed: no new rows, coverage complete. Compared with human RBPJ and worm lag-1.
- Core functions agree. All three have DNA-binding TF activity (GO:0000981), Pol II cis-regulatory sequence-specific DNA binding, positive regulation of transcription of Notch receptor target (GO:0007221) and the CSL-Notch-Mastermind complex. The Notch binding core MF matches lag-1. Human RBPJ has no Notch binding row in GOA.
- Changed: GO:0043467 regulation of generation of precursor metabolites and energy (IEA and ISO, transferred from human RBPJ) from KEEP_AS_NON_CORE to MARK_AS_OVER_ANNOTATED. The source is a single-gene COX4I2 activation result [PMID:23303788 "We demonstrate that RBPJ and CHCHD2 function towards activating the ORE at 4% oxygen,"], which the human review marks as over-annotated. The earlier mouse summary was a generic phenotype text that did not describe this term.
- Changed: GO:0061629 and GO:0140297 (IEA and ISO, transferred from human RBPJ) from ACCEPT to KEEP_AS_NON_CORE, matching human. The human sources are SPEN corepressor binding (MODIFIED there to corepressor binding) and minor co-binding reports. The term is independently true for mouse because Rbpj binds Ptf1a (PMID:11318877), but that is a tissue-specific function.
- Not changed, documented: human marks transfers of cross-pathway terms (BMP, ERBB and ephrin signalling) as over-annotated. Mouse holds the experimental IMP source (PMID:17336907) and keeps it non-core, consistent with its handling of other pleiotropic Rbpj IMP phenotypes. Worm lag-1 MODIFYs general transcription-regulation terms to GO:0007221; mouse ACCEPTs them as correct but general, and GO:0007221 is already accepted.
- Status set to COMPLETE.
