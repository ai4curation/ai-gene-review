# GATC notes

Deep research could not be generated (falcon HTTP 402; perplexity-lite unavailable;
openai key rejected). The review uses the cached literature and UniProt.

- Human GatCAB identified and reconstituted [PMID:19805282 "We successfully reconstituted in vitro Gln-tRNA(Gln) formation catalyzed by the recombinant mtGluRS and hGatCAB."].
- COXPD42 and glutamine rescue (PMID:30283131).
- GO:0070681 is obsolete (verified in QuickGO, 2026-10-10). Its obsoletion comment
  points to GO:0050567 for the amidotransferase step and suggests GO:0019988
  charged-tRNA amino acid modification for the process; the three rows were modified to
  GO:0019988 and a NEW contributes_to GO:0050567 annotation was added.

## Mitochondrial translation (GO:0032543) and GO:0070127 (2026-10-30, PR #5739 review round)

- GO:0032543 mitochondrial translation is kept as non-core context, not core, and is no
  longer listed in core_functions. GatCAB transamidates Glu-tRNA(Gln) to Gln-tRNA(Gln); it
  prepares a charged tRNA that translation consumes and performs no step of translation on
  the mitoribosome. The knockdown and patient data (PMID:19805282, PMID:30283131) show that
  GatCAB is necessary for mitochondrial protein synthesis, which is necessity evidence, not
  participation. The earlier justification "in the same sense used for mitochondrial
  aminoacyl-tRNA synthetases" was wrong: none of the human mt-aaRS GOA files checked
  (DARS2, AARS2, EARS2, FARS2, TARS2) carries GO:0032543, and the DARS2 and TARS2 reviews use
  GO:0070127 instead. The MTO1 review likewise does not claim GO:0032543.
- GO:0070127 tRNA aminoacylation for mitochondrial protein translation was considered and
  not added. Its definition is "the synthesis of aminoacyl tRNA by the formation of an ester
  bond between the 3'-hydroxyl group of the most 3' adenosine of the tRNA" (go.db). GatCAB
  forms no ester bond: it amidates the side chain of glutamate already esterified to
  tRNA(Gln) by EARS2, so the reaction is a modification of a charged tRNA (GO:0019988), not
  aminoacylation.
