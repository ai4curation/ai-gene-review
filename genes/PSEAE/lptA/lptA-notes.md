# lptA (PA0005) — review notes

UniProt Q9I7C1, reviewed, 257 aa, entry name `PLSC_PSEAE`. *Pseudomonas aeruginosa* PAO1.

## Provider deep research is absent, and why

`perplexity` is unavailable here (`Available: asta, openscientist, claude_code`). The `asta` run
returned 20 papers, none about this gene — the retrieval matched the prompt template's boilerplate
rather than the gene, and returned essentially the same list for three other unrelated genes in the
same batch, so the output was deleted rather than committed. An `openscientist` run was attempted
and did not finish in the time available. Below is my own reading, with provenance.

## The name is a collision, and it is worth flagging before anything else

`lptA` in *Escherichia coli* and in most of the literature is **LPS transport protein A**, the
periplasmic component of the Lpt bridge that ferries lipopolysaccharide to the outer membrane. That
is not this gene. PA0005 is a PlsC-family acyltransferase of **phospholipid** biosynthesis, and the
symbol comes from the paper that characterised it, where the expansion is "**L**ysophosphatidic
acid acyl**t**ransferase **A**":

`DE   AltName: Full=Lysophosphatidic acid acyltransferase A {ECO:0000303|PubMed:16079332};`

UniProt is not at fault — the entry name is `PLSC_PSEAE`, the recommended name is the
1-AGPAT activity, and the `lptA` gene name carries `ECO:0000303` to the paper that coined it. But
anyone matching this review's symbol against *E. coli* `lptA` will land on an unrelated protein, and
the two have no functional relationship at all. Recorded here rather than as a source defect,
because nothing in the record is wrong.

## Architecture and reaction

Two transmembrane segments (`FT TRANSMEM 10..30`, `FT TRANSMEM 105..125`), a single
acyltransferase signature family (`DR InterPro; IPR002123; Plipid/glycerol_acylTrfase.`,
`DR Pfam; PF01553; Acyltransferase; 1.`, `DR SMART; SM00563; PlsC; 1.`), and the curated reaction:

`Reaction=a 1-acyl-sn-glycero-3-phosphate + an acyl-CoA = a 1,2-diacyl-sn-glycero-3-phosphate + CoA;`
(RHEA:19709, EC 2.3.1.51)

The record places it at a defined step of a named pathway: "Phospholipid metabolism;
CDP-diacylglycerol biosynthesis; CDP-diacylglycerol from sn-glycerol 3-phosphate: **step 2/3**".

What matters for the review is the evidence tag on all of that: `ECO:0000250|UniProtKB:P26647` —
inferred by curators from *E. coli* PlsC, not measured here. The HXXXXD motif note is
`ECO:0000250|UniProtKB:Q9D517`, and the inner-membrane location is `ECO:0000305`, a curator
inference. So the catalytic assignment for this protein is a homology statement.

## What the primary paper does and does not show

PMID:16079332 is a quorum-sensing paper, not an enzymology paper. Its relevant content:

[PMID:16079332 "The lptA gene encoding a functional homologue of PlsC, an Escherichia coli enzyme
that catalyses the second step of the phospholipid biosynthesis pathway, was identified and
disrupted."]

[PMID:16079332 "Inactivation of lptA altered the fatty acid profile of phospholipids and the
membrane properties, resulting in decreased membrane fluidity."]

UniProt cites it for the `DISRUPTION PHENOTYPE` only, in PAO1, and records exactly that: the
mutant's phospholipids shift towards longer-chain (C18) fatty acids.

The phrase "functional homologue" is the load-bearing one for the two IMP rows, and it **was
demonstrated**. The record says so, on a line I initially missed:

`CC   -!- MISCELLANEOUS: Can complement the E.coli plsC mutant. {ECO:0000269|PubMed:16079332}.`

`ECO:0000269` with a PubMed id is the strongest UniProt support class there is — a curator read a
published experiment. So the protein was put into a *plsC* null and supplied the missing function.
That is a functional test of this protein, not a sequence inference, and it is in-species evidence
about this gene product rather than a transfer from PlsC.

### How I got this wrong, because the mechanism matters

An earlier version of these notes said the opposite: that whether complementation was shown "cannot
be seen" from an abstract-only cache. That claim was false, and false about a file this review
quotes five times.

The cause was a truncating command. My first read of the CC block was
`sed -n '/^CC   -!-/,/^DR/p' … | grep -E "^CC" | head -20`, and `head -20` stopped inside the
`DISRUPTION PHENOTYPE` paragraph — two lines before `MISCELLANEOUS`. I then wrote about what the
record contains on the strength of a view I had cut short myself.

This is the same mechanism as the nudC title fabrication in batch 7, where I read a `title:` field
through a truncating command and reconstructed the missing tail. Both times the output looked
complete, and both times the thing I needed was just past the cut. The lesson that generalises:
when asserting that a source does *not* contain something, the read has to be complete by
construction — no `head`, no `tail`, or an explicit count showing the whole section was seen.

The mutant phenotype remains real and is still the right shape for an IMP: losing the enzyme that
installs the 2-position acyl chain changes which chains end up in the membrane. It is simply no
longer the *only* evidence.

## Two GO terms for one reaction

This is the gene's notable curation feature. GOA carries both:

| term | label | rows |
|---|---|---|
| `GO:0003841` | 1-acylglycerol-3-phosphate O-acyltransferase activity | IBA, IEA (EC:2.3.1.51), ISS |
| `GO:0042171` | lysophosphatidic acid acyltransferase activity | IMP |

Their definitions are the same reaction:

- `GO:0003841`: "Catalysis of the reaction: acyl-CoA + 1-acyl-sn-glycerol-3-phosphate = CoA +
  1,2-diacyl-sn-glycerol-3-phosphate."
- `GO:0042171`: "Catalysis of the transfer of acyl groups from an acyl-CoA to lysophosphatidic acid
  to form phosphatidic acid."

Lysophosphatidic acid *is* 1-acyl-sn-glycerol-3-phosphate, and phosphatidic acid is
1,2-diacyl-sn-glycerol-3-phosphate, so the two sentences describe one transformation under two
naming conventions — the systematic/EC one and the lipidologist's one.

**Neither subsumes the other.** Checked in OLS rather than assumed: `GO:0042171`'s ancestors run
`GO:0071617` lysophospholipid acyltransferase activity → `GO:0016747` → `GO:0016746` →
transferase, and `GO:0003841` does not appear among them. They sit in different places under
acyltransferase activity.

So the annotations are not wrong and neither is redundant *as an annotation* — the redundancy is in
the ontology. Both rows are accepted and the duplication is raised as an ontology question rather
than being resolved by picking a winner here, which would silently drop a true annotation. For
`core_functions` I use `GO:0003841`, because it is the EC-grounded term that the curated catalytic
activity, the RHEA cross-reference and three of the four rows converge on.

## Term granularity

Two rows are true ancestors of terms asserted elsewhere in the review, verified in OLS:

- `GO:0008654` phospholipid biosynthetic process (IMP) is an ancestor of `GO:0006654` phosphatidic
  acid biosynthetic process (IBA), via `GO:0046474` glycerophospholipid biosynthetic process. Both
  are annotated, so the broader one is uninformative.
- `GO:0016746` acyltransferase activity (IEA, from the generic `IPR002123` signature) is an
  ancestor of `GO:0042171`, which is annotated here.

Both are `TOO_GENERAL` rather than wrong — the same reading applied to `GO:0016614` on mqo2 in this
batch, and the opposite of the wrong-branch removal that term got on soxA in batch 4.

## Open questions

- Whether the 2-acyl transfer is this protein's only activity. The PlsC family includes enzymes with
  broader lysophospholipid specificity, and nothing has been measured on the purified
  *P. aeruginosa* protein. Complementation establishes that the function is supplied; it says
  nothing about kinetics, chain-length preference or substrate breadth, which is where the real gap
  now sits.
- Whether the quorum-sensing effects are a consequence of membrane fluidity or of a signalling role.
  The paper's own framing is the former, through the stringent response and `relA`, and nothing in
  this review annotates the QS phenotypes — they are several steps from anything the enzyme does
  molecularly.
