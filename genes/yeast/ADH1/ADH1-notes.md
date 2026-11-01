# ADH1 notes

## Shared ADH family evidence
- Any of ADH1-5 or SFA1 suffices for the final Ehrlich step [PMID:12499363 "the final step of amino acid catabolism (conversion of an aldehyde to a long chain or complex alcohol) can be accomplished by any one of the ethanol dehydrogenases (Adh1p, Adh2p, Adh3p, Adh4p, Adh5p) or by Sfa1p (formaldehyde dehydrogenase.)"]
- Quadruple-deletion (single-ADH) strains [PMID:22094012 "Adh1 was the only alcohol dehydrogenase capable of efficiently catalysing the reduction of acetaldehyde to ethanol"]; [PMID:22094012 "Strains Q2 and Q3, expressing only ADH2 or ADH3, respectively, produced ethanol from glucose, albeit less than strain Q1, and were also able to oxidise added ethanol."]; [PMID:22094012 "Strains Q4 and Q5 grew poorly on glucose and produced ethanol, but were neither able to utilise the produced ethanol nor grow on added ethanol."]
- Compartments [PMID:2937632 "two in the cytoplasm (ADHI and ADHII) and one in the mitochondrion (ADHIII)"]

## Systematic YeastPathways (RCA) issues seen across ADH1-5
- GLUCFERMEN-PWY maps to GO:0019658 "bifid shunt" (Bifidobacterium pathway) - REMOVE for all ADHs.
- Pathway-default cytosol: wrong for ADH3 (matrix; REMOVE), unsupported for ADH4 (mitochondrial in HTP; over-annotated).
- Ethanol degradation (PWY3O-4300) attached to all five ADHs; ADH4/ADH5 cannot support growth on ethanol (REMOVE).

## ADH1-specific
- Fermentative isozyme [file:yeast/ADH1/ADH1-uniprot.txt "FUNCTION: Preferentially fermentative isozyme that reduces acetaldehyde"]
- Ethanol production requirement [PMID:15082781 "evaluation of strains lacking ADH1, ADH3, and ADH5, as all three genes are involved in ethanol production by yeast"]
- Substrate range decreases with chain length [PMID:8463307 "The yeast enzyme is most active with ethanol, and its activity decreases as the size of the alcohol is increased"]
- protein binding (MYTH ABC transporter screen) and plasma membrane (membrane proteome) treated as HTP artefacts of an abundant cytosolic protein.


## 2026-10-25 alcoholic-fermentation audit

Major cytosolic NADH-dependent acetaldehyde reductase. PMID22094012 is primary quadruple-deletion physiology (not a review) and supports dominance under its laboratory conditions, not exclusive activity under every condition. Ethanol oxidation is a valid alternate role. Original PMID16622836 membrane fraction result is now UNDECIDED: cytosolic abundance cannot prove contamination without the target-specific full evidence. GO:0047655 was checked with QuickGO and requires NADP+-dependent allyl oxidation; allyl-alcohol toxicity does not establish that coenzyme specificity, so the row is UNDECIDED. Original PMID6985717 cache has title/metadata only. PMID26729717 full text read externally also demonstrates recombinant Adh1/Adh3 NADH-dependent diacetyl reduction to S-acetoin; a secondary substrate activity, not promoted into a new process annotation.

Workflow: fetched current gene data using `just fetch-gene`; existing original row fields were preserved (verified against the pre-edit JSON snapshot). All 60 rows were reassessed by term and source, including non-fermentation activities/localizations. Annotation-reviewer and core-function synthesis instructions were applied. `just deep-research-falcon yeast ADH1 --fallback perplexity-lite` ran concurrently with `just fetch-gene-pmids`: Falcon/Edison failed HTTP403 authentication; Perplexity failed HTTP401 insufficient_quota. No generated provider report was fabricated. Publication caching completed successfully. FEBA fitness is a prokaryote-only review requirement and does not apply to yeast.

Family membership from the fetched record (official names independently checked in `interpro/panther/panther.obo`):

```text
DR   PANTHER; PTHR42940; ALCOHOL DEHYDROGENASE 1-RELATED; 1.
DR   PANTHER; PTHR42940:SF3; ALCOHOL DEHYDROGENASE 1-RELATED; 1.
```

GO-CAM index lookup by the UniProt accession returned no entries in the current index; existing RCA/YeastPathways assertions were assessed from their explicit terms and underlying chemistry. No new process rows were manufactured.

Audit decisions by original term (duplicate evidence rows remain intact):

- GO:0004022 alcohol dehydrogenase (NAD+) activity: ACCEPT.
- GO:0004552 octanol dehydrogenase (NAD+) activity: KEEP_AS_NON_CORE.
- GO:0005515 protein binding: REMOVE.
- GO:0005737 cytoplasm: MODIFY.
- GO:0005829 cytosol: ACCEPT.
- GO:0005886 plasma membrane: UNDECIDED.
- GO:0006068 ethanol catabolic process: KEEP_AS_NON_CORE.
- GO:0006550 L-isoleucine catabolic process: KEEP_AS_NON_CORE.
- GO:0006552 L-leucine catabolic process: ACCEPT.
- GO:0006559 L-phenylalanine catabolic process: ACCEPT.
- GO:0006569 L-tryptophan catabolic process: ACCEPT.
- GO:0006572 L-tyrosine catabolic process: KEEP_AS_NON_CORE.
- GO:0006574 L-valine catabolic process: KEEP_AS_NON_CORE.
- GO:0008270 zinc ion binding: ACCEPT.
- GO:0016491 oxidoreductase activity: MODIFY.
- GO:0019170 methylglyoxal reductase (NADH) activity: KEEP_AS_NON_CORE.
- GO:0019655 pyruvate fermentation to ethanol: ACCEPT.
- GO:0019658 bifid shunt: REMOVE.
- GO:0042802 identical protein binding: KEEP_AS_NON_CORE.
- GO:0047018 indole-3-acetaldehyde reductase (NADH) activity: KEEP_AS_NON_CORE.
- GO:0047655 allyl-alcohol dehydrogenase activity: UNDECIDED.
- GO:0120542 ethanol dehydrogenase (NAD+) activity: ACCEPT.
- GO:1904408 melatonin binding: KEEP_AS_NON_CORE.
- GO:1990362 butanol dehydrogenase (NAD+) activity: KEEP_AS_NON_CORE.
