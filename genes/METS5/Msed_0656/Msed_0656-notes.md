# Msed_0656 (A4YEH9) notes

Automated deep research was unavailable for this review. These notes come from my own
reading of the cached full texts (PMID:24532060, PMID:21169482, PMID:32218776), the
UniProt record and the GO term definitions in OLS. No `-deep-research-*.md` file was
created.

## Identity

- 395 aa, unreviewed TrEMBL entry, named "Acetyl-CoA acetyltransferase" (EC 2.3.1.9).
- Thiolase family (Pfam Thiolase_N PF00108 and Thiolase_C PF02803, PROSITE PS00737
  THIOLASE_2, NCBIfam TIGR01930 AcCoA-C-Actrans, CDD cd00751). PANTHER PTHR18919:SF107.
- UniProt keywords from ARBA: Acyltransferase, Isoprene biosynthesis. UniProt also
  carries an ARBA lipid metabolic process (GO:0006629) line that is not in the GOA file.
- M. sedula has several thiolase homologs (Msed_1647, Msed_1290, Msed_0396, Msed_0386,
  Msed_0271, Msed_0270) [PMID:32218776 table 1]. Msed_0386 and Msed_0396 sit in a
  crotonase/dehydrogenase gene cluster [PMID:32218776 "msed_0386, msed_0396,
  β-ketothiolases"].

## Identification (Ramos-Vera et al. 2011, PMID:21169482)

- Msed_0656 was assigned by similarity to the bacterial enzyme and by co-regulation, and
  the experiment was done on the Thermoproteus ortholog [PMID:21169482 "hospitalis
  contained a beta-ketothiolase gene (Msed_0656, Tneu_0249, and Igni_1401, respectively)
  that was highly similar to the eubacterial enzyme"]. [PMID:21169482 "The purified
  recombinant enzyme catalyzed the expected thiolytic cleavage of acetoacetyl-CoA into
  two molecules of acetyl-CoA."] That sentence refers to Tneu_0249.
- [PMID:21169482 "Therefore, these similar genes most likely code for beta-ketothiolase,
  catalyzing the last step in the two carbon fixation cycles."]

## Biochemistry (Hawkins et al. 2014, PMID:24532060)

- Recombinant His-tagged Msed_0656 was produced aerobically in E. coli and assayed by the
  substrate-dependent loss of CoA (DTNB) at 70 C [PMID:24532060 "For the β-ketothiolase,
  enzyme activity was measured using the discontinuous DTNB assay to measure the
  substrate-dependent disappearance of CoA at 70°C."]
- Km for acetoacetyl-CoA [PMID:24532060 "Msed_0656 on acetoacetyl-CoA, 0.18 mM"]. It is
  the fastest enzyme of the branch [PMID:24532060 "more than 100-fold lower than that of
  the β-ketothiolase (Msed_0656) (140 μmol −1 min −1 mg −1 )"].
- It is one of the four enzymes used to reconstitute 4HB to acetyl-CoA in vitro
  [PMID:24532060 "were produced recombinantly in Escherichia coli , combined in vitro ,
  and shown to convert 4HB to acetyl-CoA"].
- Liu et al. 2020 call it the characterized beta-ketothiolase, and note that a paralog
  (Msed_0386) may also contribute [PMID:32218776 "in addition to the characterized
  β-ketothiolase Msed_0656 gene"].

## Assessment

- GO:0003985 acetyl-CoA C-acetyltransferase activity (2 acetyl-CoA = CoA +
  acetoacetyl-CoA; OLS-verified) is the core MF. It is supported experimentally for
  Msed_0656 itself (PMID:24532060), and the IEA row is accepted. The direct evidence is
  for the thiolytic direction, which is the physiological direction in the cycle.
- GO:0016746 and GO:0016747 are ancestors of GO:0003985 (OLS). They are correct but
  general, so both rows are MODIFIED to GO:0003985.
- Process: NEW GO:0015977 carbon fixation. It catalyses the last step of the cycle,
  which regenerates the acetyl-CoA acceptor.
- Open question: archaea make isoprenoids by the mevalonate pathway, which starts from
  acetoacetyl-CoA. Msed_0656, or a paralog, may also supply acetoacetyl-CoA for
  isoprenoid synthesis, as the ARBA keyword hints, but no evidence for this was found.
