# B6HR98 (Penicillium rubens Pc22g24830) — curation notes

## Identity

UniProtKB:B6HR98, 326 aa, locus `Pc22g24830` (also `PCH_Pc22g24830`) of
Penicillium rubens Wisconsin 54-1255 (the strain formerly named *Penicillium
chrysogenum* Wisconsin 54-1255), NCBITaxon:500485, reference proteome
UP000000724. The entry carries Pfam PF13714 (PEP_mutase) and PROSITE PS00161,
and no gene symbol; the folder is named by accession per repo convention.

## The TrEMBL name is wrong: this is oxaloacetate acetylhydrolase

UniProt names the entry "Isocitrate lyase, EC 4.1.3.1" on PROSITE-ProRule
PRU10119 alone. Two independent lines show that is a mis-assignment.

1. **Direct genetic evidence that Pc22g24830 encodes the oxaloacetase.**
   Gombert et al. cloned the two candidate paralogs into a yeast that makes no
   oxalate: "Only the expression of Pc22g24830 led to production of" oxalic acid
   in *S. cerevisiae*, and deleting it in *P. chrysogenum* eliminated oxalate
   formation entirely [PMID:21549851 "Only the expression of Pc22g24830 led to production of"].
   The paper frames the activity as the standard fungal route, "oxaloacetate
   hydrolase (OAH; EC3.7.1.1) is generally responsible for oxalate" production
   [PMID:21549851 "oxaloacetate hydrolase (OAH; EC3.7.1.1) is generally responsible for oxalate"],
   and notes that "The P. chrysogenum genome harbours four orthologs of the A. niger"
   oahA gene [PMID:21549851 "The P. chrysogenum genome harbours four orthologs of the A. niger"],
   of which only this one has the activity. (The abstract's deletion sentence
   contains an evident typo, "Pc22g28430"; the gene cloned, assayed and deleted
   is Pc22g24830, as its own title and the preceding sentence state.)
2. **Sequence evidence.** B6HR98 is 81.6% identical to *A. niger* OahA and
   68-70% identical to the two OAHs with enzymology (*C. parasitica* D5LIR7,
   *B. cinerea* Q6PNM8), against ~30% to genuine isocitrate lyases; it lacks the
   ICL domain PF00463 altogether and is 326 aa where ICLs are 428-590 aa; and
   *P. rubens* has its own separate PF00463 isocitrate lyases (B6HRS2, B6HVG1).
   It carries the OAH specificity serine and the full PEPM/ICL catalytic set.
   See [file:CONPW/A0A5M3MM75/A0A5M3MM75-bioinformatics/RESULTS.md].

The marker serine comes from Joosten et al., who found that presence of the
"serine in family members correlates with presence of OAH activity whereas its"
absence correlates with its absence
[PMID:17654546 "serine in family members correlates with presence of OAH activity whereas its"],
and from the *C. parasitica* OAH structure, where "OAH contains a serine residue,
Ser-308, and DMML contains a proline residue instead, Pro-240"
[PMID:20558740 "OAH contains a serine residue, Ser-308, and DMML contains a proline residue instead, Pro-240"]
and the *B. cinerea* S260P swap "reduced its OAH activity 40-fold and increased
the (2 R ,3 S )-dimethylmalate lyase activity 15-fold"
[PMID:20558740 "reduced its OAH activity 40-fold and increased the (2 R ,3 S )-dimethylmalate lyase activity 15-fold"].

The oxaloacetase reaction itself is the hydrolytic C-C cleavage of oxaloacetate
to oxalate and acetate [PMID:20558740 "catalyzes the hydrolysis of oxalacetate to oxalic acid and acetate"],
and the enzyme family needs a divalent metal: "All PEPM/ICL superfamily members
require Mg 2+ or Mn 2+ for activity"
[PMID:20558740 "All PEPM/ICL superfamily members require Mg 2+ or Mn 2+ for activity"].
That the single OAH gene accounts for all secreted oxalate in two other fungi was
shown by disruption of *B. cinerea* oahA: "the disruption of this gene results in
the loss of" oxalate formation
[PMID:17244616 "the disruption of this gene results in the loss of"], with
"oxalate production in A. niger and B. cinerea is solely dependent" on it
[PMID:17244616 "oxalate production in A. niger and B. cinerea is solely dependent"].
The founding *A. niger* gene was cloned from purified enzyme: "The enzyme
oxaloacetate hydrolase (EC 3.7.1.1), which is involved in oxalate" formation was
purified from *A. niger*
[PMID:10778746 "The enzyme oxaloacetate hydrolase (EC 3.7.1.1), which is involved in oxalate"].

## Curation decisions

- `GO:0004451` isocitrate lyase activity (IEA, EC mapping) and `GO:0046421`
  methylisocitrate lyase activity (IEA, EC mapping): REMOVE. Both descend from
  the PRU10119 name; the protein has no ICL domain, the organism has separate
  ICLs, and the specificity serine excludes the methylisocitrate/dimethylmalate
  lyases, which carry a proline there.
- `GO:0016833` oxo-acid-lyase activity (IEA, ARBA): MODIFY to `GO:0030603`
  oxaloacetase activity. The C-C cleavage is real but is hydrolytic; GO:0030603
  (EC 3.7.1.1) sits under hydrolase activity acting on C-C bonds in ketonic
  substances, not under lyase. Chen et al. note the formal ambiguity (if the
  gem-diol binds pre-formed, OAH is formally a lyase), but the GO class for this
  EC is the hydrolase one.
- `GO:0003824` catalytic activity (IEA, InterPro): TOO_GENERAL, entailed by the
  proposed GO:0030603 row.
- NEW rows: `GO:0030603` oxaloacetase activity (IMP, PMID:21549851) and
  `GO:0033610` oxalate biosynthetic process (IMP, PMID:21549851). Both rest on
  the deletion and the heterologous-expression result in that paper; the gene
  product performs the committed step itself, so the process term is warranted.
- Source defects filed against UNIPROT (protein name + EC) and against the
  PROSITE/ProRule mapping (resource OTHER).

## CMMMech context

CMMMech's `allanite-leachate.yaml` grounds *Issatchenkia orientalis* strain JL04
and records that the strain carries three codon-optimised copies of this
*P. chrysogenum* oxaloacetate hydrolase ("Pcoah"), but omits B6HR98 as a
ProteinExample precisely because TrEMBL calls it isocitrate lyase. This review
supports re-adding it: the identification of Pc22g24830 as the oxaloacetase is
experimentally established (PMID:21549851), and the TrEMBL name is the defect.
Nothing in this review supports CMMMech's downstream mineral-recovery claims at
the level of this protein; those rest on the engineered-strain phenotype, not on
any assay of B6HR98 itself.
