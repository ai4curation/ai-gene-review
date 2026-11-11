# Qdpr notes

- UniProtKB:P11348 states: FUNCTION: Catalyzes the conversion of quinonoid dihydrobiopterin into tetrahydrobiopterin. [UniProtKB:P11348].
- Core interpretation: quinonoid dihydrobiopterin reduction during tetrahydrobiopterin recycling/biosynthesis.
- Accepted direct GO terms include: 6,7-dihydropteridine reductase activity, pteridine-containing compound metabolic process, tetrahydrobiopterin biosynthetic process.
- Non-core/context terms are mostly localization, binding/cofactor, inferred pathway context, or exposure-response annotations; generic parent terms are modified when a specific catalytic term is available.

## Re-review 2026-10-04

- GOA refresh (commit a3cf70b6d): no new rows and no retired rows; only WITH/FROM and
  qualifier backfill on the 24 existing rows. 0 PENDING.
- Description rewritten as standalone biology (previous text described what "the review
  accepts"); facts from UniProt P11348 (SDR family, homodimer) and the falcon report.
- GO:0010044 response to aluminum ion (IEP, PMID:3477172): MARK_AS_OVER_ANNOTATED -> UNDECIDED.
  The cached record is title-only ("The effect of lead and aluminium on rat dihydropteridine
  reductase"), so whether the observation was direct enzyme inhibition or regulated expression
  cannot be read; the earlier verdict rested on an unread study.
- The other four IEP response/development rows keep MARK_AS_OVER_ANNOTATED, with the generic
  boilerplate reason replaced by what overshoots in each study:
  - liver development: an activity pattern, "the developmental upsurge of dihydropteridine
    reductase ... begins earlier than does that of phenylalanine hydroxylase" [PMID:710385].
  - response to lead ion: lead "inhibit[s] dihydropteridine reductase" [PMID:3815851]; the enzyme
    is the toxicant's target, not a responder.
  - response to glucagon: glucagon "induced liver dihydropteridine reductase more than twofold"
    [PMID:4155291]; an induced output with no shown role in the glucagon response.
  - cellular response to xenobiotic stimulus: only theophylline lowered activity, at 96 h
    [PMID:2484967].
- Positive abstract support added to experimental ACCEPT/KEEP rows whose quotes were only
  methods sentences: PMID:1898002 (bacteria "demonstrate conversion of quinonoid
  dihydropteridines to their tetrahydro forms"), PMID:9235988 (rate-limiting "release of the
  tetrahydropterin product"), PMID:8631945 (active site "requires bound cofactor"),
  PMID:1639779 (native enzyme "has a considerable preference for NADH").
- GO:0006729 tetrahydrobiopterin biosynthetic process rows kept ACCEPT: DHPR regenerates BH4
  from qBH2, which is formation of BH4 within the term definition, and human QDPR carries the
  same term by IBA.
- Open question for a human: PMID:3477172 (aluminium) needs the full paper to adjudicate.
