# polA (Pseudomonas putida KT2440, Q88RK6, PP_0123) notes

Reviewer: Claude (AI-assisted). Provider deep research was not available for this gene in
this campaign (no provider API access), and no `-deep-research-*.md` file exists. These notes
use the UniProt record, the cached E. coli Pol I literature and a local alignment.

## Record

- Unreviewed UniProt entry (PE 3, inferred from homology). The RuleBase function statement:
  "In addition to polymerase activity, this DNA polymerase exhibits 3'-5' and 5'-3' exonuclease
  activity." SMART domains: 5'-3' exonuclease 4..266, 3'-5' exonuclease 314..503, family A
  palm 673..879. PANTHER PTHR10133:SF27 ("DNA POLYMERASE NU"), the same subfamily as E. coli
  Pol I (P00582) in the PANTHER member index.
- No KT2440-specific Pol I biochemistry or polA mutant study was found.

## Bioinformatics (`polA-bioinformatics/RESULTS.md`)

- 63.0% identity to E. coli Pol I over the E. coli length. All 13 checked active-site residues
  conserved: 3'-5' exonuclease D355/E357/D424/D501/Y497 -> D339/E341/D408/D487/Y483;
  polymerase R668/D705/Y766/R841/N845/Q849/D882/E883 -> R655/D692/Y753/R828/N832/Q836/D869/E870.
- So the proofreading domain is intact (not a Taq-like degenerate exonuclease domain).

## E. coli ortholog evidence used

- Gap filling and primer replacement [PMID:6262323 "E. coli DNA polymerase I was needed to fill
  the short gap left by DNA polymerase III holoenzyme, and to remove the primer and replace it
  with DNA."].
- Klenow polymerase catalytic residues [PMID:2201688 "Mutations in the second cluster of
  residues, Gln849, Arg668, and Asp882, cause a large decrease in kcat"].
- Klenow exonuclease-site mutants [PMID:2832946 "two mutant proteins lacking 3',5'-exonuclease
  activity but having normal polymerase activity"].

## Decisions

Actions mirror the COMPLETE E. coli polA review: generic terms (nucleic acid binding,
catalytic activity, nucleotidyltransferase, DNA polymerase activity, DNA replication) are
MODIFY to the specific terms already present; DNA binding, the polymerase and both
exonuclease activities, DNA-templated DNA replication, DNA repair and DNA biosynthetic process
are ACCEPT; double-strand break repair is KEEP_AS_NON_CORE. Written independently of the
older unmerged draft in PR #2417, which was consulted (it used MARK_AS_OVER_ANNOTATED for the
generic terms and quoted DE/ARBA lines).
