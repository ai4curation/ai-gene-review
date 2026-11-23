# sqr (A0A543Q349, GCD22_02301): curation notes

- TrEMBL entry, Acidithiobacillus thiooxidans ATCC 19377. The submitter name is "Pyridine
  nucleotide-disulfide oxidoreductase" and the gene name "sqr" is also from the submitter.
  No EC and no ARBA SQR naming, unlike the Type I entries. PE 4. Folder named
  `sqr__A0A543Q349` because the symbol `sqr` is shared across paralogs and species.
- **Not Type I. Type V (SqrE)-like** (`file:ACIF2/AFE_1792/AFE_1792-bioinformatics/RESULTS.md`):
  - 26-28% identical to the acidophile Type I SQRs (B7JBP8, F9ZQD6, A0A060UVE9, A0A059XTE6).
  - 56.2% identical to Chlorobaculum tepidum CT0876 (Q8KE17), an SqrE homolog
    [PMID:21833341 "tepidum has an SqrE homolog (CT0876/NP_661769), although no SQR activity
    has been demonstrated for this protein"], and 32.0% to the characterized Type V SQR of
    Acidianus ambivalens (Q7ZAG8).
  - Tyr137 sits at the position of the Type I flavin-linked Cys128. C186/C361 align with the
    A. ambivalens active-site C178/C350.
- CT0876 was assayed and had no SQR activity [PMID:19028893 "Recombinantly produced CT1087 and
  CT0117 proteins had SQR activity, while CT0876 did not."]. Membership of the SqrE-like clade
  is therefore not enough to assign GO:0070224, and GO:0016491 was kept as the precise-as-
  warranted MF.
- Expression: in ATCC 19377 the gene designated sqr is [PMID:32231653 "medium to highly
  expressed in all three conditions at comparable levels"]. The locus behind that "sqr" is
  presumed to be this one (the only SQR-family gene with that name in the strain's UniProt
  proteome) but was not confirmed.
- UniProt lists three SQR-family proteins for ATCC 19377 (A0A5P9XLP4, 375 aa; A0A5P9XUB1,
  379 aa; A0A543Q349, 428 aa). None is a Type I SqrA ortholog of AFE_1792. The genome paper
  for strain A01 reports an sqr ortholog with 79% and 72% identity to other Acidithiobacillus
  sqr genes [PMID:24993543], without naming the comparison loci.
- An A. ferrivorans paralog (sqr2, AFERRI_20483) is 89% identical to this protein, so the
  Type V-like SQR is conserved across Acidithiobacillus.

## Annotation decisions
- GO:0016491 (InterPro2GO): ACCEPT as the most specific supported MF. GO:0070224 is not
  proposed (see above).

## CMMMech claim check (overstated)
functional_role (traction-battery-hydrometallurgical-residue;
waste-liquid-crystal-display-panels): "Membrane-bound sulfide-quinone reductase (sqr) in
Acidithiobacillus thiooxidans ATCC 19377 oxidizing reduced sulfur species during acidophilic
consortium bioleaching."
- **Stronger than the evidence.** The protein is a Type V/SqrE-like homolog, whose closest
  characterized relative lacks SQR activity. Neither membrane association nor sulfide:quinone
  activity has been shown, and there is no EC on the UniProt entry. CMMMech's protein_name
  field correctly carries UniProt's "Pyridine nucleotide-disulfide oxidoreductase", but the
  functional_role asserts SQR function as fact. A defensible wording would be "putative Type V
  (SqrE-like) sulfide:quinone oxidoreductase homolog; activity not demonstrated". Its
  sequence differs from the AFE_1792 enzyme used elsewhere in the same CMMMech records
  (28% identity), so the two should not be treated as equivalent representatives.
