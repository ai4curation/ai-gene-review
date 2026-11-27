# arh1 (O59710, SPBC3B8.01c) review notes

## Sources

No deep-research provider output is available (no provider API keys in this
environment). The review rests on the UniProt record (function by similarity to
S. cerevisiae Arh1, P48360) and the cached literature; PMID:34660592 was read in full,
PMID:18399988 and PMID:21536008 from the abstracts.

## Literature

- Ferredoxin reductase activity [PMID:18399988 "In this paper, we present evidence that
  the S. pombe ferredoxin reductase, arh1, and ferredoxin, etp1fd provide mammalian class
  I cytochromes P450 with reduction equivalents."]
- No NADH/NADPH preference in vitro [PMID:18399988 "The modified reductase arh1_A18G
  displayed spectroscopic characteristics similar to AdR and was shown to be capable of
  accepting electrons with no evident preference for NADH or NADPH, respectively."]
- Weak FAD binding [PMID:18399988 "The recombinant reductase showed an unusual weak
  binding of flavin adenine dinucleotide (FAD), which was mastered by modifying the
  FAD-binding region by site-directed mutagenesis yielding a stable holoprotein."]
- Role in CoQ synthesis is by homology only (no S. pombe test).

## Audit decisions (2026-11)

- Replaced supporting texts that were paper titles or unrelated sentences (rows on
  GO:0004324 IDA PMID:21536008, GO:0071949, GO:0099128) with verbatim claims.
- GO:0099128 mitochondrial [2Fe-2S] assembly complex (TAS, PMID:34660592) changed from
  KEEP_AS_NON_CORE to MARK_AS_OVER_ANNOTATED: the review does not make the reductase a
  complex subunit.
- Core function GO:0004324 agrees with the module's ferredoxin-system annoton.
