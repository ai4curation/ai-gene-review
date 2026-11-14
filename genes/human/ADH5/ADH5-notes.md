# ADH5 (human, P11766) review notes

2026-11-11. Reviewed as the animal exemplar (PANTHER PTHR43880:SF4) of the
oxidation step of the glutathione-dependent formaldehyde detoxification module.

- Deep research: no deep-research provider credentials were available in this
  session, so no deep-research file was generated. Evidence comes from cached
  publications, Reactome R-HSA-5692237 and the curated UniProt record.
- Arg115 is needed for S-(hydroxymethyl)glutathione binding and fatty-acid
  activation [PMID:8460164 "critical for the binding of S-hydroxymethylglutathione in glutathione-dependent formaldehyde dehydrogenase activity"].
- Ethanol is a very poor substrate; long-chain alcohols are good substrates
  [PMID:6375718 "chi-ADH oxidizes ethanol very poorly."].
- Human genetics: ADH5 + ALDH2 deficiency causes AMeD syndrome
  [PMID:33355142 "our results suggest that the combined deficiency of formaldehyde clearance mechanisms leads to the complex clinical features due to overload of formaldehyde-induced DNA damage"].
- GO:0018467 (glutathione-independent formaldehyde dehydrogenase) is the wrong
  reaction for the IDA observation; MODIFY to GO:0051903.
- GO:0009055 electron transfer activity (TAS) removed: ADH5 is not an electron carrier.
- 20-HETE omega-oxidation rows marked over-annotated: in vitro activity, the
  cited study attributes the cellular reaction to ADH4.
