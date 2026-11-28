# PA5007 — review notes

UniProt Q9HUF8, **unreviewed**, 252 aa, `PE 4: Predicted`. *Pseudomonas aeruginosa* PAO1.
One GOA row: `GO:0016301` kinase activity, IMP, PMID:10692150.

## Provider deep research is absent, and why

`perplexity` is unavailable here (`Available: asta, openscientist, claude_code`). The `asta` run
returned 20 papers, none about this gene, because the retrieval matched the prompt template's
boilerplate rather than the gene — the same list came back for three other unrelated genes in the
batch — so that output was deleted rather than committed. An `openscientist` run was started and
abandoned after it failed to finish one gene in fifteen minutes; a `falcon` run was started
afterwards. What follows is my own reading.

## The record says less than its name suggests

Everything on this entry is weak, and it is worth listing because the single GOA row has to be
judged against it:

- `DE   RecName: Full=Lipopolysaccharide kinase {ECO:0008006|Google:ProtNLM};` — a **ProtNLM**
  machine-generated name. Per the project rules this is an unvetted prediction and not evidence of
  anything.
- `GN   OrderedLocusNames=PA5007 {ECO:0000313|EMBL:AAG08392.1};` — **no gene name at all**, only the
  locus tag, and that from an unreviewed submitter import. UniProt does not call this gene *wapQ*,
  *wapP* or anything else.
- `PE   4: Predicted` — the weakest protein-existence level.
- The only keyword is `Reference proteome`. No function, no cofactor, no subcellular location, no
  catalytic activity, no publication cited.

What the record does carry, and what is genuinely useful, is a curated family assignment:

- `DR   PIRSF; PIRSF026326; InaA; 1.`
- `DR   InterPro; IPR027023; Put_LipoPS_kinase_InaA.`
- `DR   Pfam; PF06293; Kdo; 1.`
- `DR   InterPro; IPR011009; Kinase-like_dom_sf.`

PIRSF is one of the curated UniRule systems, so family membership is good support. Note what the
family is *called*, though: `Put_LipoPS_kinase_InaA` — **putative** LPS kinase, of the *E. coli*
InaA type.

## It is not a WaaP-family heptose kinase

This matters because `waaP` (PA5009, Q9HUF7) was reviewed in batch 5, where its physiological
activity got a proposed new term, "lipopolysaccharide core heptose kinase activity (EC 2.7.1.235)".
Q9HUF7 and Q9HUF8 are adjacent accessions for adjacent genes, and the obvious guess is that the
same term fits PA5007. It does not. The signatures separate them cleanly:

| | waaP (PA5009) | PA5007 |
|---|---|---|
| shared | `PF06293 Kdo`, `IPR011009 Kinase-like_dom_sf` | same |
| specific | `PIRSF037318 RfaP`, `IPR017172 Lsacc_core_hep_kinase_RfaP`, `NCBIfam NF011703 rfaP` | `PIRSF026326 InaA`, `IPR027023 Put_LipoPS_kinase_InaA` |

PA5007 carries **no** RfaP signature and **no** `rfaP` NCBIfam model. The two proteins share only
the Kdo-kinase fold, which is the level at which the family is defined, not the level at which the
substrate is. So importing waaP's proposed term here would have asserted a specific sugar position
on the strength of a fold. Checking this was the single most useful thing in the review.

## What the cited paper actually reports

PMID:10692150 (Walsh et al. 2000) is the source of the IMP row. Abstract-only in the cache. It
characterises **three** putative kinase genes:

[PMID:10692150 "We have used chemical and genetic techniques to characterize three putative kinase
genes that are involved in the addition of phosphate to the inner core region of P. aeruginosa
lipopolysaccharide. The first gene is a waaP homologue, whereas the other two (wapP and wapQ) are
unique to P. aeruginosa."]

Note "**putative** kinase genes" — the paper's own hedge.

Two of the three could not be inactivated:

[PMID:10692150 "Repeated attempts using a variety of membrane-stabilizing conditions to generate
waaP:Gm (Gm, gentamicin) or wapP:Gm mutants were unsuccessful."]

The third could, and its phenotype was close to nothing:

[PMID:10692150 "A wapQ:Gm mutant was isolated and it had an unaltered minimum inhibitory
concentration (MIC) for novobiocin and only a small decrease in the MIC for sodium dodecyl
sulphate (SDS), suggesting that the loss of a phosphate group transferred by WapQ may only be
having a small impact on outer-membrane permeability."]

The only enzymology in the paper is on WaaP, not on the other two:

[PMID:10692150 "Nuclear magnetic resonance and methylation linkage analysis showed that WaaPPa
could add one phosphate to O4 of HepI in a Salmonella typhimurium waaP mutant."]

So if PA5007 is *wapQ*, the IMP rests on a mutant with essentially no phenotype, and no phosphate
transfer by that protein was ever demonstrated. If PA5007 is *wapP*, no mutant was obtained at all,
so there is no mutant phenotype for an IMP to be inferred from.

## Which gene PA5007 is cannot be settled from what I have

Two sources disagree, and a later paper adds a fourth gene:

- The later open-access mBio paper (PMID:21810964, PMC3147165, full text read) describes the
  operon and uses gene names for three and a locus tag for the fourth:
  [PMID:21810964 "P. aeruginosa waaP occurs within a gene cluster containing LPS sugar transferase
  genes waaF, waaC, and wapG; two other LPS kinase genes, wapP and wapQ; and a putative LPS kinase
  gene, PA5006"]
  and
  [PMID:21810964 "The four proposed LPS kinase genes waaP, wapP, wapQ, and PA5006 are annotated as
  a single operon among other LPS synthesis genes in P. aeruginosa PAO1."]
  It never writes PA5007, PA5008 or PA5009, so it does not map the names to those tags.
- A web search of the secondary literature turned up a direct conflict: the *Pseudomonas*
  Metabolome Database lists **PA5007 as wapG** — a sugar *transferase*, which the mBio paper groups
  with waaF and waaC rather than with the kinases — while the primary literature is read as naming
  PA5007 *wapQ*. Transcriptome annotations reportedly follow the wapG reading.

With waaP = PA5009 established from its own UniProt record (`OrderedLocusNames=PA5009`), the
descending order waaP/wapP/wapQ/PA5006 would put PA5007 at wapQ. But that is an inference from gene
order, not a statement anyone makes, and it is exactly contradicted by the wapG assignment. The
same search also reported that "the kinase role of WapQ has not been firmly established, and a wapQ
mutant showed no clear LPS change", which is consistent with the abstract above.

### The databases decline to name it, which is the sharpest finding here

I checked the two authoritative sources that could be read. Neither assigns PA5007 any gene name:

| locus | KEGG/RefSeq Symbol | KEGG/RefSeq product | UniProt gene name |
|---|---|---|---|
| PA5006 | none | "(RefSeq) hypothetical protein" | — |
| **PA5007** | **none** | **"(RefSeq) hypothetical protein"** | **none, locus tag only** |
| PA5008 | none | "(RefSeq) hypothetical protein" | — |
| PA5009 | **waaP** | "(RefSeq) lipopolysaccharide kinase WaaP" | waaP |

So PA5009 is unambiguously *waaP* in KEGG as well — `Symbol waaP`, KO K02848, EC 2.7.1.235 — while
PA5006, PA5007 and PA5008 are all nameless "hypothetical protein" in RefSeq. The *wapP* and *wapQ*
names from the primary literature are attached to no locus in either database.

Two consequences:

- RefSeq claims **less** for PA5007 than UniProt's ProtNLM name does. "Hypothetical protein" against
  "Lipopolysaccharide kinase": the only reason the record says "kinase" at all is a machine-generated
  name, which the project rules exclude as evidence.
- The IMP row therefore connects a paper that names *wapQ* to a locus that no database names.
  Whoever made the annotation had to make that mapping themselves, and the mapping is not recorded
  anywhere I can read. That is the specific thing the `CHECK` query asks the resource to supply.

`pseudomonas.com`, which the secondary literature says lists PA5007 as *wapG*, returned HTTP 403 and
could not be read, so that assignment stays unverified rather than confirmed or refuted.

I could not resolve this. Both candidate identities point the same way for the review, which is
what makes `UNDECIDED` defensible rather than evasive:

- if PA5007 is **wapQ**: the kinase role is unestablished and the mutant had no real phenotype;
- if PA5007 is **wapP**: no mutant exists, so no IMP is possible;
- if PA5007 is **wapG**: it is a transferase and the kinase term is simply wrong.

None of the three supports a confident kinase activity, and two of them would make the row wrong
rather than merely weak. But distinguishing them changes what the *correction* should be, and I
cannot do that from an abstract.

## Why UNDECIDED rather than REMOVE or MARK_AS_OVER_ANNOTATED

The project rules are explicit that an experimental annotation should not be overruled from
incomplete evidence, and that `UNDECIDED` is the action when the relevant publication cannot be
read. Both apply here with unusual force: the paper is abstract-only, and an IMP means a curator
read the full text and saw which gene they were annotating — which is the very thing I cannot
determine.

What stops this from being a case where I defer and accept: the abstract itself states the weakness
for the one gene whose mutant was obtained, and the record offers nothing independent — a ProtNLM
name, no gene name, PE 4, and a family whose own name says "putative". There is no second line of
evidence to lean on, the way there was for PA0328, where the record's own features corroborated the
paper.

So the row is left `UNDECIDED` with the identity question recorded as a `CHECK` query to the
resource, rather than asserting a removal I cannot justify or an acceptance the evidence does not
earn.

## What would settle it

The full text of PMID:10692150, which gives locus tags in its strain and plasmid tables, or the
*Pseudomonas* Genome DB entry for PA5007. Either would say in one line whether this gene is wapQ,
wapP or wapG, and the review could then be finished properly.
