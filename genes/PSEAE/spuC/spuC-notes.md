# spuC (PA0299, Q9I6J2) review notes

## What the gene does, and why GO cannot say it

SpuC is the putrescine aminotransferase of the *spu* locus. The primary characterisation is
explicit about the amino acceptor:
[PMID:12081945 "enzymatic measurements indicated that spuC encodes putrescine aminotransferase
with pyruvate as the amino group receptor."] — i.e. putrescine + pyruvate → 4-aminobutanal +
L-alanine, **EC 2.6.1.113**, which is how the Swiss-Prot entry names and numbers the protein. A
later study calls it, in the same words, [PMID:18192388 "SpuC, the major putrescine-pyruvate
transaminase"], and shows the pathway it serves is indispensable:
[PMID:18192388 "Corresponding mutant strains were severely hampered in polyamine utilization."]

GO has **no term for EC 2.6.1.113**. A search of GO for putrescine transaminase activities
returns exactly one term, `GO:0033094` putrescine:2-oxoglutarate transaminase activity, which is
the *other* reaction (EC 2.6.1.82, the PatA/YgjG route, using 2-oxoglutarate as acceptor). The
distinction is not cosmetic: the pyruvate-dependent route produces L-alanine, which is why
PMID:18192388 reports that "the alanine-pyruvate cycle was shown to be indispensable for
polyamine utilization" and couples SpuC to the *dadRAX* alanine transaminase/racemase locus. The
2-oxoglutarate route produces glutamate and makes no such demand.

So the review proposes a new term rather than forcing the gene onto `GO:0033094`, and the general
`GO:0008483` transaminase activity rows are handled as pointing at it.

## The biotin IBAs are a paralog transfer, and the real BioA is in the same genome

`GO:0004015` S-adenosyl-L-methionine:8-amino-7-oxononanoate transaminase activity and
`GO:0009102` biotin biosynthetic process both arrive by IBA from `PTN000241343`, whose donors are
BioA orthologues — *E. coli* BioA (P12995), *M. tuberculosis* BioA (P9WQ81), yeast and
*Arabidopsis* members. The donors are genuine; the transfer is not, and two checks settle it in
opposite directions:

- **Target-specific evidence of a different activity.** SpuC is a reviewed entry with EC
  2.6.1.113 assigned from enzymatic measurement, a `CC FUNCTION` statement carrying
  `ECO:0000269|PubMed:12081945` and `ECO:0000269|PubMed:18192388`, a disruption phenotype, a
  pathway assignment to putrescine degradation, and four crystal structures. This is not a
  protein of unknown function that inherited a plausible guess.
- **The organism has its own BioA, and it carries exactly these two terms.** PA0420 (UniProt
  Q9I693) is annotated "Adenosylmethionine-8-amino-7-oxononanoate aminotransferase", and QuickGO
  returns `GO:0004015` and `GO:0009102` on it by IBA from the same `GO_REF:0000033`. The biotin
  claim is therefore not missing from *P. aeruginosa*; it is already on the gene that makes
  biotin, and its appearance on SpuC is a second copy on the wrong member.

Both are class-III pyridoxal-phosphate-dependent aminotransferases — SpuC's `CC SIMILARITY` says
so, and PANTHER puts it in `PTHR43094:SF1`, "AMINOTRANSFERASE CLASS-III" — which is the fold the
transfer rides on. Class III is a large family whose members differ precisely in which amine
donor and which keto acceptor they use, so family membership predicts the chemistry and not the
substrate.

## The transaminase IMP cites a paper that does not mention the gene

`GO:0008483` is annotated IMP from PMID:21622750, whose abstract is about the seven
γ-glutamylpolyamine synthetase genes (*pauA1*–*pauA6*, *pauB*, *pauC*, *pauD*) and the *bauRABCD*
locus, and never names *spuC*. That paper's subject is the **alternative** γ-glutamylation route
to GABA, not the transaminase route SpuC works in. The full text is not cached
(`full_text_available: false`), and *spuC* could well appear in it — a study of polyamine
catabolism would plausibly use a *spuC* background or compare the two routes. This is therefore
recorded as a query (`CHECK`, `SUSPECTED`), not as a defect: it is exactly the case the
repository's rule reserves for `SUSPECTED`, where the unread text could overturn the claim.

The practical consequence is that the refinement proposed for that row does not rest on it. It
rests on PMID:12081945, the gene's own characterisation, which this review cites directly.
