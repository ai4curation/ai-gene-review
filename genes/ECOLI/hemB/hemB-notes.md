# hemB (P0ACB2) notes, Escherichia coli K-12

## Sources and deep research

- Deep research was not available: the one attempted provider run for this batch
  (`just deep-research ECOLI hemA --provider perplexity`, 2026-11-10) failed with a missing
  template error ("All providers failed"). No deep-research file exists; this review uses
  the UniProt record and cached abstracts. All GOA-cited primary papers are abstract-only in
  the cache except PMID:18304323 (full text; HemB not named in the cached text, the
  per-protein list is supplementary).

## Function

- PBGS/ALAD condenses two ALA to porphobilinogen; homo-octamer [PMID:8439296 "The enzyme is a
  homo-octamer of subunit M(r) 36554 +/- 17."].
- Zn(II) metalloenzyme [PMID:8424649 "We conclude from these data that E. coli PBGS is a
  Zn(II)-metalloenzyme and that Zn(II) is required for catalytic activity"].
- Allosteric stimulatory Mg(II) (Mgc), distinct from the zinc sites [PMID:7819203 "This
  stimulatory Mg(II) is called Mgc. Mgc is not required for activity and is distinct from
  the two zinc ions (ZnA and ZnB)"]. Note PMID:8424649 (1993) said E. coli PBGS lacks the
  plant-type Mg site; later structural work (UniProt FT BINDING 232, PMID:11444968,
  PMID:11909869, not cached) placed Mg elsewhere. Not a conflict for the Mg binding row.
- Genetics: heme-requiring hemB mutants [PMID:387909], cloned hemB complements
  [PMID:3276659].

## Verdict summary

- GO:0004655 (IBA, IDA x2, IEA, IMP): ACCEPT, core.
- GO:0008270 zinc (IDA x2), GO:0000287 Mg (IDA): KEEP_AS_NON_CORE (cofactor/allosteric
  metal; PSEPK hemB accepted its IEA zinc row, here judged non-core relative to the
  catalytic activity).
- GO:0046872 metal ion binding: MODIFY -> GO:0008270 + GO:0000287 (as PSEPK, plus zinc).
- GO:0005829 cytosol (HDA, IBA, IDA): ACCEPT.
- GO:0006783 (IBA, IMP x2): ACCEPT. GO:0033014: ACCEPT (trunk, consistent with hemA/hemL).
- GO:0006779 (ARBA): TOO_GENERAL (entailed by accepted GO:0006783).
