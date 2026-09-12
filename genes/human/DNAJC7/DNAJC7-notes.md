# DNAJC7 (Tpr2 / TTC2) research notes

## Identity
- UniProt Q99615 (DNJC7_HUMAN), 494 aa. HGNC:12392. Synonyms TPR2, TTC2.
- Domain architecture: 9 TPR repeats (two TPR clusters) + a C-terminal J domain (DOMAIN 381..451)
  [file:human/DNAJC7/DNAJC7-uniprot.txt FT DOMAIN J / REPEAT TPR 1..9]. This is the classic
  "type III J protein" plus dual TPR domain architecture.

## Core molecular function
- Co-chaperone that bridges/regulates HSP70 and HSP90 chaperone machines.
  [PMID:12853476 "Tpr2 recognizes both Hsp70 and Hsp90 through its TPR domains, and its J domain
  stimulates ATP hydrolysis and polypeptide binding by Hsp70."] -> J-domain stimulates Hsp70 ATPase
  = ATPase activator activity (GO:0001671); TPR domains bind Hsp70 and Hsp90 = heat shock protein binding.
- Mechanism: mediates retrograde transfer of substrates from Hsp90 back onto Hsp70 ("recycling chaperone").
  [PMID:12853476 "unlike other co-chaperones, Tpr2 induces ATP-independent dissociation of Hsp90 but not
  of Hsp70 from chaperone-substrate complexes. ... We propose a novel mechanism in which Tpr2 mediates the
  retrograde transfer of substrates from Hsp90 onto Hsp70."]
- Required at a narrowly defined expression level for GR activation [PMID:12853476 "an increase or decrease
  in Tpr2 expression reduces GR activation, suggesting that Tpr2 is required at a narrowly defined expression
  level."]
- Binds Hsp90 and Hsp70 simultaneously, like Hop, but with distinct ATP-dependence; can substitute for
  type I/II J proteins in Hsp90-dependent chaperoning of PR and the kinase Chk1.
  [PMID:18620420 "Tpr2 can bind Hsp90 and Hsp70 simultaneously, which is also a property of the cochaperone
  Hop." ; "Tpr2 replaced type I and II J proteins in the Hsp90-dependent chaperoning of the PR and the
  protein kinase, Chk1."]
- UniProt FUNCTION: "Acts as a co-chaperone regulating the molecular chaperones HSP70 and HSP90 in folding
  of steroid receptors, such as the glucocorticoid receptor and the progesterone receptor. Proposed to act
  as a recycling chaperone by facilitating the return of chaperone substrates to early stages of chaperoning
  if further folding is required." [file:human/DNAJC7/DNAJC7-uniprot.txt]

## Interactions (UniProt SUBUNIT)
- HSP90AA1, HSP90AB1, HSPA1A/B (ATP-enhanced), HSPA8 (Hsc70), PGR, NR1I3/CAR (recruits to cytoplasm),
  RAD9A/HUS1/RAD1 (9-1-1 checkpoint clamp), NF1 GAP domain.
- Mutagenesis: R101A and R333A impair Hsp90/Hsp70 binding; H409A (J-domain HPD) -> predominantly nuclear,
  abolishes interaction when combined. [file:human/DNAJC7/DNAJC7-uniprot.txt FT MUTAGEN]
- IntAct hits (bare protein binding in GOA): BAG2 (O95816), BAG4 (O95429), DISC1 (Q9NRI5), HSPA1L (P34931),
  MLF2 (Q15773), HIV vif (P12504, xeno). These map the GOA IPI rows.

## Localization
- Cytoplasm (IDA PMID:12853476), Nucleus (EXP PMID:11573955; H409A mutant predominantly nuclear),
  cytoskeleton/microtubules (by similarity; colocalizes with NR1I3). Extracellular exosome and membrane
  are high-throughput proteomics (HDA) — non-core.

## Disease
- DNAJC7 is an ALS risk gene: rare/loss-of-function variants in DNAJC7 cause familial and sporadic ALS,
  first implicated by exome sequencing (Farhan et al. 2019, Nat Neurosci). Recent work links DNAJC7 to
  neuroprotection against proteotoxic stress via modulating HSF1 activity, and biallelic LoF variants cause
  familial ALS with TDP-43 pathology. (Established background; not in cached pubs — not quoted as supporting_text.)

## GOA review logic
- ATPase activator activity (GO:0001671, TAS Reactome): ACCEPT, CORE — J domain stimulates Hsp70 ATPase.
- heat shock protein binding (GO:0031072, IPI): ACCEPT, CORE — binds Hsp70/Hsp90 directly.
- protein folding (GO:0006457, IDA x2 + TAS): KEEP_AS_NON_CORE — co-chaperone assists folding, downstream BP.
- regulation of cellular response to heat (GO:1900034, TAS Reactome): KEEP_AS_NON_CORE — HSF1/HSR pathway role.
- Localization: cytoplasm/cytosol (IDA/EXP) ACCEPT; nucleus/nucleoplasm (EXP/IDA) KEEP_AS_NON_CORE (genuine
  but secondary, J-domain-regulated); cytoskeleton (IEA) KEEP_AS_NON_CORE; membrane/extracellular exosome
  (HDA) MARK_AS_OVER_ANNOTATED (proteomics carryover).
- protein binding (GO:0005515, IPI x8): bare term, KEEP_AS_NON_CORE (real interactions, uninformative term).
