# GLYK (At1g80380; UniProtKB:Q944I4) curation notes

**Deep research could not be run** in this environment (no provider API keys). These notes
are a manual literature summary built only from cached publications in `publications/`
and the UniProt record (`GLYK-uniprot.txt`). No `-deep-research-*.md` file exists for
this gene.

## Identity

- UniProt Q944I4, "D-glycerate 3-kinase, chloroplastic"; 456 aa precursor; predicted
  transit peptide; P-loop NTPase fold with a PRK/URK-like domain (InterPro IPR006083,
  Pfam PF00485); UniProt places it in the "GLYK kinase family"; PANTHER PTHR10285
  (uridine kinase family). Three isoforms in UniProt; isoform 3 lacks residues 1-92 (no
  transit peptide).
- Structurally unrelated to bacterial and animal glycerate kinases [PMID:15980259 "The newly
  identified GLYK is both structurally and phylogenetically distinct from known glycerate
  kinases from bacteria and animals."].

## Molecular function: D-glycerate 3-kinase (EC 2.7.1.31)

- Purified from leaves and identified by MS [PMID:15980259 "We have purified and partially
  sequenced this yet missing enzyme from Arabidopsis thaliana and identified it as a
  putative kinase-annotated single-copy gene At1g80380 ."].
- Recombinant protein active; substrate specificity tested [PMID:15980259 "The exclusive
  catalytic properties of the gene product were confirmed after heterologous expression in
  Escherichia coli ."] and neither PRK nor uridine kinase activity [PMID:15980259 "We
  therefore tested whether purified Arabidopsis GLYK exhibits PRK or uridine kinase (UK)
  activity and found that neither of the two reactions is catalyzed ( Table 2 )."].
- The only GLYK activity source in leaves [PMID:15980259 "These data demonstrate that At
  GLYK represents the only significant source of GLYK activity in Arabidopsis."].
- UniProt catalytic activity: (R)-glycerate + ATP = (2R)-3-phosphoglycerate + ADP + H+
  (Rhea:23516; ECO:0000269 PubMed:15980259). ATP-binding P-loop at 215-222 (ECO:0000255).
- A 2024 study on thermostability engineering of GLYK (PMID:39550762, not cached) reports
  Km values for ATP and glycerate for AtGLYK; not used here.

## Biological process: photorespiration (final step of the C2 cycle)

- [PMID:15980259 "Arabidopsis T-DNA insertional knockout mutants show no GLYK activity and
  are not viable in normal air; however, they grow under elevated CO 2 , providing direct
  evidence of the obligatory nature of the ultimate step of the C 2 cycle."]
- Glycerate accumulates ~200-fold in the mutants [PMID:15980259 "reveals an up to
  ∼200-fold accumulation of glycerate in the mutants"].
- Review [PMID:22303256 "The chloroplastic D-glycerate 3-kinase (GLYK, EC 2.7.1.31)
  catalyzes the phosphorylation of glycerate to 3-phosphoglycerate with ATP as a
  co-substrate."] and [PMID:22303256 "Knock-out of this gene results in a conditionally
  lethal photorespiratory phenotype."]. Unlike most photorespiratory genes, GLYK is not
  light induced [PMID:22303256 "Particularly, Glyk gene expression is not activated by
  light ( Foyer et al., 2009 )."].
- GO:0009854 "oxidative photosynthetic carbon pathway" (C2 pathway: 2-phosphoglycolate to
  3-phosphoglycerate) is part_of GO:0009853 photorespiration (verified via OLS
  hierarchicalParents); both are correct for GLYK.

## Location: chloroplast stroma (isoform 1); cytoplasm (isoform 3, shade)

- Plastid-targeting sequence [PMID:15980259 "According to Target P ( Emanuelsson et al.,
  2000 ) and ChloroP ( Emanuelsson et al., 1999 ), the protein sequence includes a
  plastid-targeting sequence with three potential cleavage sites (after amino acids 63, 107,
  and 118)."]. Stroma: HDA (PMID:18633119, PMID:20061580); the enzyme purifies as a soluble
  protein from leaf extracts (no detergent in the purification protocol).
- Alternative promoter selection controlled by phytochrome gives a cytoplasmic isoform in
  shade [PMID:29129375 "For instance, shade-grown plants accumulate a cytoplasmic isoform of
  glycerate kinase (GLYK), an essential photorespiration enzyme that was previously thought
  to localize exclusively to the chloroplast."] that functions as a bypass
  [PMID:29129375 "Cytoplasmic GLYK constitutes a photorespiratory bypass that alleviates
  fluctuating light-induced photoinhibition."]. Abstract-only in cache; UniProt records
  isoform 1 chloroplast (light) and isoform 3 cytoplasm (dark), ECO:0000269 PubMed:29129375.
- HDA mitochondrion (PMID:28887381) and envelope (PMID:12938931) and ISM nucleus are not
  supported by targeted studies; judged as likely contaminants or predictions.

## Family

- GLYK homologs in fungi and some cyanobacteria; yeast homolog is also a glycerate kinase
  [PMID:15980259 "As shown in Table 2 , the yeast enzyme is a GLYK and does not accept other
  substrates, such as ribulose 5-phosphate or uridine."].
