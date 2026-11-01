# ADH4 notes

## Shared ADH family evidence
- Any of ADH1-5 or SFA1 suffices for the final Ehrlich step [PMID:12499363 "the final step of amino acid catabolism (conversion of an aldehyde to a long chain or complex alcohol) can be accomplished by any one of the ethanol dehydrogenases (Adh1p, Adh2p, Adh3p, Adh4p, Adh5p) or by Sfa1p (formaldehyde dehydrogenase.)"]
- Quadruple-deletion (single-ADH) strains [PMID:22094012 "Adh1 was the only alcohol dehydrogenase capable of efficiently catalysing the reduction of acetaldehyde to ethanol"]; [PMID:22094012 "Strains Q2 and Q3, expressing only ADH2 or ADH3, respectively, produced ethanol from glucose, albeit less than strain Q1, and were also able to oxidise added ethanol."]; [PMID:22094012 "Strains Q4 and Q5 grew poorly on glucose and produced ethanol, but were neither able to utilise the produced ethanol nor grow on added ethanol."]
- Compartments [PMID:2937632 "two in the cytoplasm (ADHI and ADHII) and one in the mitochondrion (ADHIII)"]

## Systematic YeastPathways (RCA) issues seen across ADH1-5
- GLUCFERMEN-PWY maps to GO:0019658 "bifid shunt" (Bifidobacterium pathway) - REMOVE for all ADHs.
- Pathway-default cytosol: wrong for ADH3 (matrix; REMOVE), unsupported for ADH4 (mitochondrial in HTP; over-annotated).
- Ethanol degradation (PWY3O-4300) attached to all five ADHs; ADH4/ADH5 cannot support growth on ethanol (REMOVE).

## ADH4-specific
- Iron-containing ADH family (IPR001670), unrelated fold to ADH1/2/3/5.
- Metal ambiguity: [PMID:3282541 "we could demonstrate that ADHIV is activated by zinc ions, like the other yeast alcohol dehydrogenase isozymes, and not by ferrous ions"] vs [PMID:17938904 "partial compensation by the upregulation of the poorly efficient Fe-dependent Adh4p in our conditions"]
- Mitochondrial by GFP [file:yeast/ADH4/ADH4-uniprot.txt "SUBCELLULAR LOCATION: Mitochondrion {ECO:0000269|PubMed:14562095}."]
- Ty insertions activate ADH4 in adh1 strains [PMID:3023838 "another 65% of the mutations are Ty insertions at ADH4, a new locus identified and cloned as described in this paper"]


## 2026-10-25 alcoholic-fermentation audit

The primary purified-enzyme abstract PMID3282541 explicitly reports activation by zinc, not ferrous ions. Family group III naming does not identify the native cofactor. PMID17938904 reports zinc-limited industrial-yeast compensation associated with Adh4 upregulation but calls it Fe-dependent without a direct metal-reconstitution assay in the accessible abstract. PMID22094012 finds Q4 fails to use ethanol and does not attribute its modest ethanol production confidently to Adh4. PMID3023838 identifies activating Ty insertions at ADH4 in adh1 mutants selected for low-temperature antimycin resistance. Therefore standard-culture weak contribution is conditional, not proof of catalytic incapacity. Cytosolic reaction compartment remains UNDECIDED despite mitochondrial localization; pathway projection alone is insufficient. Ehrlich reduction remains supported by combinatorial mutants (PMID12499363).

Workflow: fetched current gene data using `just fetch-gene`; existing original row fields were preserved (verified against the pre-edit JSON snapshot). All 43 rows were reassessed by term and source, including non-fermentation activities/localizations. Annotation-reviewer and core-function synthesis instructions were applied. `just deep-research-falcon yeast ADH4 --fallback perplexity-lite` ran concurrently with `just fetch-gene-pmids`: Falcon/Edison failed HTTP403 authentication; Perplexity failed HTTP401 insufficient_quota. No generated provider report was fabricated. Publication caching completed successfully. FEBA fitness is a prokaryote-only review requirement and does not apply to yeast.

Family membership from the fetched record (official names independently checked in `interpro/panther/panther.obo`):

```text
DR   PANTHER; PTHR11496; ALCOHOL DEHYDROGENASE; 1.
DR   PANTHER; PTHR11496:SF102; ALCOHOL DEHYDROGENASE 4; 1.
```

GO-CAM index lookup by the UniProt accession returned no entries in the current index; existing RCA/YeastPathways assertions were assessed from their explicit terms and underlying chemistry. No new process rows were manufactured.

Audit decisions by original term (duplicate evidence rows remain intact):

- GO:0004022 alcohol dehydrogenase (NAD+) activity: ACCEPT.
- GO:0005739 mitochondrion: ACCEPT.
- GO:0005829 cytosol: UNDECIDED.
- GO:0006068 ethanol catabolic process: REMOVE.
- GO:0006550 L-isoleucine catabolic process: KEEP_AS_NON_CORE.
- GO:0006552 L-leucine catabolic process: ACCEPT.
- GO:0006559 L-phenylalanine catabolic process: ACCEPT.
- GO:0006569 L-tryptophan catabolic process: ACCEPT.
- GO:0006572 L-tyrosine catabolic process: KEEP_AS_NON_CORE.
- GO:0006574 L-valine catabolic process: KEEP_AS_NON_CORE.
- GO:0008270 zinc ion binding: ACCEPT.
- GO:0016491 oxidoreductase activity: MODIFY.
- GO:0019658 bifid shunt: REMOVE.
- GO:0046395 carboxylic acid catabolic process: MODIFY.
- GO:0046872 metal ion binding: MODIFY.
- GO:0047018 indole-3-acetaldehyde reductase (NADH) activity: KEEP_AS_NON_CORE.
- GO:0120542 ethanol dehydrogenase (NAD+) activity: ACCEPT.
