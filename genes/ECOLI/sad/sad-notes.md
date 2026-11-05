# sad (P76149, E. coli K-12) evidence notes

## 2026-11-02

Reviewed as the reference protein of PANTHER PTHR43217 (SUCCINATE SEMIALDEHYDE
DEHYDROGENASE [NAD(P)+] SAD), for the family review that the module
`bacterial_4_hydroxybutyrate_oxidation` needs. P76149 is the only
experimentally characterized member of that family with a complete curated
UniProt record, and it is the PAINT seed for the family's GO:0004777 IBD node
[file:interpro/panther/PTHR43217/PTHR43217-paint.tsv].

**No provider deep research is available in this environment.** Both
`just deep-research ECOLI sad --provider perplexity` and `--provider falcon`
failed (perplexity is not an installed provider here; falcon returned
`403 Failed to authenticate`, no API key). No `-deep-research-*.md` file was
fabricated. The review was built from the curated UniProt flat file, the GOA
rows, the five cached publications, and the PANTHER/PAINT slices.

## Enzyme identity and chemistry

Two succinate-semialdehyde dehydrogenase activities were separated from
*E. coli* decades before either gene was known: a large NADP-specific enzyme
induced by GABA, and a smaller NAD-preferring enzyme induced by
p-hydroxyphenylacetate that reduces NADP at 15% of the NAD rate, mainly through
a higher Km, and is dimeric with ~55 kDa subunits
[PMID:7011797 "reduces NADP at 15% of the rate observed for NAD, primarily because of a"],
[PMID:7011797 "weight was estimated to be 55 000, indicating that the native enzyme is dimeric."],
[PMID:7004491 "separated and partially purified by ammonium sulphate fractionation or Sephadex"].

The gene behind the NAD-dependent activity was identified as *yneI* (now *sad*)
by a gap-filling prediction plus direct biochemistry, which also showed the
enzyme works with either nicotinamide cofactor
[PMID:17873044 "here that the E. coli gene yneI is responsible for this activity"],
[PMID:17873044 "dehydrogenase can use either NAD(+) or NADP(+) to oxidize succinate semialdehyde"].
UniProt curates both reactions on this accession (RHEA 13217 and RHEA 13213),
each with ECO:0000269 evidence from that paper, which is why the review keeps
the cofactor-general GO:0009013 as the core molecular function and keeps the
NADP-specific child as a non-core secondary branch rather than removing it.

## Physiological role and the division of labour with GabD

The paralog GabD is the dedicated NADP-specific GABA-shunt enzyme; Sad is
induced by succinate semialdehyde itself and by putrescine, and its principal
job is to keep this reactive aldehyde from accumulating
[PMID:17873044 "yneI-encoded activity, in contrast, functions primarily as a valve to prevent"],
[PMID:20639325 "conditions; in contrast, GabT is almost constitutive. Similarly, YneI is induced"].
Both PuuE and YneI are needed to use putrescine as a carbon source, defining a
putrescine-inducible GABA degradation route
[PMID:20639325 "of putrescine as a sole nitrogen source and both PuuE and YneI are important for"],
and *yneI* mutants are impaired on arginine, which is catabolized through
putrescine and GABA
[PMID:17873044 "growth on arginine and probably has an essential function during growth on"].
The GABA rows are therefore accepted (Sad does perform the terminal oxidation of
that route), while the arginine and putrescine rows are kept as non-core
substrate context.

## Two judgement calls worth recording

1. **GO:0006099 tricarboxylic acid cycle (IBA) was removed.** The IBD at
   PTN000193476 for this process is seeded by *M. tuberculosis* GabD1 (P9WNX9),
   where the GABA shunt is read as a bypass of the oxidative decarboxylation
   segment of the cycle. *E. coli* K-12 has a complete oxidative TCA cycle, and
   Sad feeds succinate into the cycle's intermediate pool from outside the
   cycle. Supplying a cycle metabolite is not participating in the cycle, so
   this is a lineage-specific pathway reading propagated too far, recorded with
   a structured `propagation_review`. The same node's GO:0004777 assertion is
   accepted.
2. **GO:0070458 cellular detoxification of nitrogen compound was modified to
   GO:0110095 cellular detoxification of aldehyde.** The toxic species the
   enzyme removes is succinate semialdehyde, which contains no nitrogen; it
   simply arises downstream of nitrogen-compound catabolism. GO:0110095 takes
   aldehyde (CHEBI:17478) as its has-input class and is the matching term. This
   is a lateral substrate-class correction, not a refinement, so the replacement
   is not a descendant of the original.

GO:0042803 protein homodimerization activity is kept as non-core: the dimer is
real and experimentally recorded, but it describes assembly of the active enzyme
rather than its evolved catalytic assignment. The GOA row cites PMID:7004491,
whose cached abstract does not itself state the subunit stoichiometry; the full
text was not accessible here, so the attribution is not second-guessed and the
dimer claim is supported from the UniProt SUBUNIT line and PMID:7011797.
