# nudC (PA1823, O86062) review notes

## The IMP asserts a phenotype the paper says does not exist

`GO:0016787` hydrolase activity is annotated **IMP** from PMID:24989777. That paper studied both
orthologues side by side, and its central result is that the *P. aeruginosa* mutant has no
phenotype:

[PMID:24989777 "Opposite to P. syringae NudC, the P. aeruginosa NudC deficiency as well as its
overproduction had no visible impact on cells."]

An IMP is inferred from a *mutant phenotype*. Here the paper reports the absence of one, and says
so as its headline conclusion: [PMID:24989777 "These results indicate that NudC from P. syringae,
but not from P. aeruginosa is vital for bacteria."] So the evidence code is not merely weak, it
names the wrong kind of experiment — and the same paper does contain direct evidence of the right
kind.

## What the paper actually shows for this protein

It is not, as the title alone suggests, only about *P. syringae*. The *P. aeruginosa* enzyme was
purified and assayed:

[PMID:24989777 "We have investigated NudC Nudix proteins from the plant pathogen Pseudomonas
syringae pv. tomato str. DC3000 and from the human pathogen Pseudomonas aeruginosa PAO1161. We
found that these homologous enzymes are homodimeric and in vitro preferentially hydrolyse NADH."]

That is in vitro enzymology on the annotated protein — **IDA**, and it reaches a specific activity,
NADH hydrolysis, not the bare `hydrolase activity` the row carries. The strain, PAO1161, is a PAO1
derivative, so the annotated locus is the right one. The subunit observation also matches the
curated record, which states `SUBUNIT: Homodimer`.

So one row carries two separate problems — too general a term, and an evidence code contradicted
by its own reference — and the fix for each is in the same sentence of the same paper.

## The metal terms are all genuine

Three metal-binding terms looked at first like a redundant cluster to prune: `GO:0000287`
magnesium, `GO:0030145` manganese and `GO:0008270` zinc, all from one UniRule. Reading the record
rather than assuming:

```
COFACTOR: Name=Mg(2+) ... Name=Mn(2+) ... Note=Divalent metal cations. Mg(2+) or Mn(2+).
COFACTOR: Name=Zn(2+) ... Note=Binds 1 zinc ion per subunit.
```

These are two distinct cofactor blocks in HAMAP-Rule MF_00297: a catalytic divalent cation that
may be either Mg or Mn, and a separate structural zinc, one per subunit. All three terms are
supported, and none is a duplicate of another. Only `GO:0046872` metal ion binding, mapped from
InterPro, is the general parent of the three and so uninformative once they are asserted.

Had I pruned on the pattern rather than the record I would have removed two correct annotations.

## Which activity is the core one

The entry is **reviewed**, built on **HAMAP-Rule MF_00297**, whose `RecName` is "NAD-capped RNA
hydrolase NudC" with the short name "DeNADding enzyme NudC". The rule carries two catalytic
activities with Rhea reactions — removal of the NAD cap from mRNA (RHEA:60876) and hydrolysis of
free NAD+ (RHEA:11800) — and the function text gives the mRNA-decapping role first, noting a
preference for mRNAs with a 5'-end purine.

So the gene has three accepted activity terms that are not rivals: `GO:0110153` for the deNADding
reaction on RNA, `GO:0000210` for free NAD+, and `GO:0035529` for NADH, which is the one actually
measured on this protein. The review treats the deNADding activity as the core function, since
that is what the curated rule names the protein for, while recording that the only direct
measurement on the *P. aeruginosa* enzyme is the NADH preference.

`GO:0006742` NADP+ catabolic process arrives by IBA and is kept as non-core: the rule says the
enzyme "catalyzes the hydrolysis of a broad range of dinucleotide pyrophosphates", which makes
NADP+ plausible substrate promiscuity rather than a role the organism needs, and nothing has
measured it here.

## A fabricated title, and what caught it

Recorded because it is worth recording. The first version of this review gave PMID:24989777's
title as:

> "NudC Nudix hydrolase from Pseudomonas syringae, but not its counterpart from Pseudomonas
> aeruginosa, **is essential for survival and biofilm formation**."

The real title is:

> "NudC Nudix hydrolase from Pseudomonas syringae, but not its counterpart from Pseudomonas
> aeruginosa, **is a novel regulator of intracellular redox balance required for growth, motility
> and biofilm formation**."

I had read the cached record with a command that truncated the `title:` field at the line break,
saw the first half, and wrote a plausible second half from what the abstract said — rather than
going back for the field. The reference validator rejected the file, since it checks each cited
title against the fetched record precisely so that an invented or transposed citation cannot pass.

Two things follow. First, the check earned its keep: nothing else in the review would have caught
it, and a fabricated title in a reference list is worse than a wrong one, because it looks
authoritative and is not traceable to any source. Second, the invented version was *lossy in a way
that mattered* — the real title names intracellular redox balance, which is the paper's own framing
and ties the in vitro NADH preference to the mutant's NADH accumulation. Writing the title from the
abstract did not merely risk being wrong; it discarded the one piece of interpretation the title
carried, and the review was missing it until the validator forced a second look. The NADH-accumulation
finding and the redox half of the first knowledge gap were added as a result.
