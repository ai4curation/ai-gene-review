# pqsA (PA0996, Q9I4X3) — review notes

Provider deep research is **not** available for this gene. `just deep-research PSEAE pqsA
--provider perplexity` fails (perplexity is not a configured provider; available: asta,
openscientist, claude_code), and the asta run returned 20 citations none of which concern
pqsA, PQS, *P. aeruginosa* or anthranilate — they are papers on bioinformatics databases,
grey seal influenza, bovine spermatozoa, saffron pharmacology and PCOS. The retrieval
keyed on the template's boilerplate ("gene annotation", "functional annotation") rather
than on the gene, so the output was discarded rather than committed as provider research.
These notes stand in its place, per the project rule that a failed deep-research run is
documented in `-notes.md` rather than written up under a provider name.

## What the protein does

PqsA is the anthranilate–CoA ligase (EC 6.2.1.32) that primes anthranilate for entry into
the 2-alkyl-4(1H)-quinolone pathway of *P. aeruginosa*. It is the first gene of the
`pqsABCDE` operon.

The reaction is ATP-dependent thioesterification:

    anthranilate + ATP + CoA -> anthraniloyl-CoA + AMP + diphosphate   (RHEA:10828)

[file:PSEAE/pqsA/pqsA-uniprot.txt, "Catalyzes the formation of anthraniloyl-CoA, which is the
priming step for entry into the Pseudomonas quinolone signal (PQS) biosynthetic pathway."]

Direct evidence is a purified-enzyme assay: [PMID:18083812 "The PqsA protein was purified as a
recombinant His-tagged polypeptide, and this protein was shown to have anthranilate-CoA ligase
activity."] and, in extracts, [PMID:18083812 "Extracts prepared from Escherichia coli expressing
PqsA were shown to catalyze the formation of anthraniloyl-CoA from anthranilate, ATP, and CoA."]

Downstream, anthraniloyl-CoA is condensed with a malonyl thioester by PqsD (with PqsB/PqsC)
to give the 4-quinolone ring. PqsH then hydroxylates HHQ at C3 to give PQS itself
[PMID:18728009 "The first step is the formation of anthraniloyl-CoA by PqsA."]

## Why the pathway term is the one the operon carries, not a quorum-sensing term

PQS (2-heptyl-3-hydroxy-4(1H)-quinolone, CHEBI:29472) is a quorum-sensing signal acting
through PqsR/MvfR, so it is tempting to annotate the synthase to `GO:0009372 quorum sensing`,
whose definition does include "producing small, diffusible, signal molecules".

A comparator check says otherwise, and the check is sound because it returns positives:
four PSEAE genes in this corpus carry `GO:0009372` (fabY, hfq, mexT, ppx), so an absence is
informative rather than a malformed query. Within the signal-synthesis machinery the term is
absent everywhere — **lasI**, the canonical AHL synthase, does not carry it, and neither does
any pqs gene. Every pqs biosynthetic gene in the corpus (pqsA, pqsB, pqsC, pqsH) instead
carries `GO:0044550 secondary metabolite biosynthetic process`.

That is a convention, not an oversight: the signal *synthases* get the biosynthesis term and
`GO:0009372` goes to the genes that detect or regulate. No `NEW` quorum-sensing row is
proposed here.

## Specificity: the measured breadth is not the function

The purified enzyme is promiscuous in vitro — [PMID:18083812 "The enzyme was active on a variety
of aromatic substrates, including benzoate and chloro and fluoro derivatives of anthranilate."]
— and the 2002 genetic paper identified the gene by homology to a benzoate-CoA ligase
[PMID:12426334 "Gene pqsA encodes a product homologous to benzoate coenzyme A ligase, which may be
involved in activating anthranilate for PQS synthesis"].

Three things place anthranilate as the physiological substrate:

1. Affinity. `KM=3 uM for anthranilate` against 22 uM for CoA and 71 uM for ATP
   (file:PSEAE/pqsA/pqsA-uniprot.txt), a low-micromolar Km consistent with a dedicated
   substrate rather than adventitious turnover.
2. Loss of function abolishes the products, not merely reduces them:
   [file:PSEAE/pqsA/pqsA-uniprot.txt "Mutants show no detectable levels of 2,4-dihydroxyquinoline
   (DHQ) or other quinolines."]
3. No benzoate-CoA ligase activity is annotated on the gene, and no pathway in PAO1 requires
   one from this locus.

So the benzoate activity is in vitro breadth of an AMP-binding enzyme, not a second function.
It is not annotated, so there is nothing to action here; it matters because the same breadth is
what makes anthranilate analogues useful inhibitors
[PMID:18083812 "These results indicate that the PqsA protein is responsible for priming anthranilate
for entry into the PQS biosynthetic pathway"].

## The IMP row, and what it does not say

The PseudoCAP IMP for `GO:0044550` comes from a transposon screen scored on pyocyanin
[PMID:12426334 "The largest set of pleiotropic mutations blocked the production of the extracellular
Pseudomonas quinolone signal (PQS), a molecule required for the synthesis of secondary metabolites
and extracellular enzymes."]

The row is sound, because PQS, HHQ and DHQ are themselves secondary metabolites made by this
pathway. But the phenotype that identified the mutant — reduced pyocyanin — is a *regulatory*
consequence of losing the signal, not evidence that PqsA participates in phenazine
biosynthesis. The row should not be read that way, and no phenazine term is proposed.

## Ontology gap

GO has `GO:0102164 2-heptyl-3-hydroxy-4(1H)-quinolone synthase activity` (carried by pqsH) but
no biological-process term for alkylquinolone or PQS biosynthesis; a search returns nothing
while the same search style resolves `GO:0102164`, so the gap is real rather than a failed
query. The whole operon therefore sits on `GO:0044550`, which cannot distinguish this pathway
from pyoverdine or phenazine biosynthesis. Recorded as a `proposed_new_terms` entry.

## Family placement

UniProt assigns the protein to the ATP-dependent AMP-binding enzyme family (Pfam PF00501
AMP-binding, PF13193 AMP-binding_C; IPR000873). PANTHER places it in **PTHR43352**, whose
family name is "ACETYL-COA SYNTHETASE", with anthranilate specificity recognised only at the
subfamily level (**PTHR43352:SF1**, "ANTHRANILATE--COA LIGASE"). That split is why the PAINT
IBD at PTN002458530 asserts the substrate-agnostic `GO:0016878 acid-thiol ligase activity`
rather than the anthranilate term: the node spans acyl-CoA synthetases of differing substrate,
including an *M. tuberculosis* member (UniProtKB:P9WQ61) in the WITH/FROM. The gene's own
accession also appears in that WITH/FROM, which is expected — it marks the target's own
experimental annotation among the descendant evidences the PAINT curator used, and is not
circularity.
