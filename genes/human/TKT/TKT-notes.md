# TKT (human transketolase, UniProtKB:P29401) — review notes

## Summary of gene function

TKT encodes transketolase (EC 2.2.1.1), a thiamine-diphosphate (TPP/ThDP)- and
divalent-cation (Mg2+; also Ca2+/Mn2+/Co2+)-dependent enzyme of the non-oxidative
branch of the pentose phosphate pathway. It reversibly transfers a two-carbon
glycolaldehyde (ketol) unit from a ketose donor to an aldose acceptor via a covalent
ThDP intermediate, interconverting sugar phosphates and linking the PPP to glycolysis.

Key reactions (Reactome/UniProt):
- xylulose-5-P + ribose-5-P <-> sedoheptulose-7-P + glyceraldehyde-3-P
- xylulose-5-P + erythrose-4-P <-> fructose-6-P + glyceraldehyde-3-P

This balances the cell's supply of ribose-5-phosphate (nucleotide synthesis) versus
NADPH regeneration by feeding excess pentoses back into glycolytic intermediates.

## Provenance for key assertions

- Function / catalytic activity / ThDP-dependent two-carbon transfer:
  [UniProt P29401 FUNCTION, "Catalyzes the transfer of a two-carbon ketol group from a
  ketose donor to an aldose acceptor, via a covalent intermediate with the cofactor
  thiamine pyrophosphate"]; catalytic activity RHEA:10508, EC 2.2.1.1.
- Structure / cofactor / mode of action:
  [PMID:20667822 "The crystal structure of human transketolase (TKT), a thiamine diphosphate
  (ThDP) and Ca(2+)-dependent enzyme that catalyzes the interketol transfer between ketoses
  and aldoses as part of the pentose phosphate pathway"]. Homodimer; Km values for
  xylulose-5-P/ribose-5-P reported.
- Mg2+ / ThDP binding, dimerization: [PMID:9357955 "Active human transketolase is a
  homodimeric enzyme possessing two active sites, each with a non-covalently bound thiamine
  diphosphate and magnesium"]; D155 essential for ThDP-Mg binding and dimer formation.
- Recombinant kinetics: [PMID:9611778 "the K(m) values were 0.27 +/- 0.02 and 0.51 +/- 0.05
  mM for the substrates D-xylulose 5-phosphate and D-ribose 5-phosphate"].
- cDNA cloning, single-copy gene, Wernicke-Korsakoff context: [PMID:8419340 "human
  transketolase cDNA clones were isolated"; "Transketolase was found to be a single copy
  gene"].
- Disease (SDDHD) and in-vivo role: [PMID:27259054 "an autosomal-recessively inherited
  deficiency of transketolase"; "Enzymatic testing confirmed significantly reduced
  transketolase activity"; "Transketolase deficiency is one of a growing list of inborn
  errors of metabolism in the non-oxidative part of the pentose phosphate pathway"].

## Localization

TKT is a cytosolic enzyme (IBA cytosol; multiple Reactome TAS cytosol). It is not a
peroxisomal or nuclear enzyme in any established sense:
- Peroxisome (ISS from S. cerevisiae P50137 ortholog, GO_REF:0000024): questionable
  transfer; human/mammalian TKT is cytosolic. Yeast TKL1 peroxisomal targeting does not
  clearly transfer to human TKT (no PTS1/PTS2 in the human protein per UniProt). Mark as
  over-annotation.
- Nuclear (nucleoplasm/nuclear body/nuclear speck, HPA IDA GO_REF:0000052): high-throughput
  immunofluorescence localization; a glycolytic/PPP enzyme detected in the nucleoplasm is
  common in HPA data and likely reflects moonlighting/diffuse distribution rather than a
  core function. Keep as non-core.
- Extracellular exosome / vesicle (HDA, large-scale exosome proteomics): abundant cytosolic
  metabolic enzymes are routinely co-isolated in exosome/vesicle proteomes; not a bona fide
  functional localization. Mark as over-annotation.

## Notable

- SDDHD = "short stature, developmental delay, and congenital heart defects" (MIM:617044),
  autosomal recessive transketolase deficiency (PMID:27259054). No common Mendelian disease
  otherwise; erythrocyte TKT activity is a classic index of thiamine (vitamin B1) status
  (Wernicke-Korsakoff).
- TKTL1/TKTL2 are paralogs; PMID:20667822 discusses putative properties of these
  transketolase-like proteins.
- Calcium ion binding (IDA, PMID:20667822): the crystal structure was solved with Ca2+ in
  the divalent-cation site (a substitute for the physiological Mg2+); UniProt lists Mg2+ as
  the physiological cofactor and Ca2+/Mn2+/Co2+ as alternatives. The metal site is the
  cofactor-anchoring site, so "calcium ion binding" and "magnesium ion binding" describe the
  same divalent-cation site.
- protein binding (IPI, PMID:21044950): TERF1/TRF1 interaction from a genome-wide YFP
  complementation telomere-interactome screen; uninformative bare protein-binding term.

## Curation decisions (see YAML)
- Core: transketolase activity (GO:0004802), TPP binding (GO:0030976), Mg2+ binding
  (GO:0000287), non-oxidative PPP branch (GO:0009052), cytosol (GO:0005829).
- Non-core: nuclear localizations; pentose-phosphate shunt (parent BP); G3P biosynthetic/
  metabolic processes; xylulose-5-P biosynthetic process.
- Over-annotation: peroxisome (ISS), exosome/vesicle (HDA), calcium ion binding (structural
  surrogate metal), transketolase-or-transaldolase (ARBA grouping term), bare protein binding.
</content>
</invoke>
