# PCSK2 (human, P16519) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: PCSK2 was reviewed as the closest experimentally characterised relative of DROME/amon
(Q9VBC7). Both are in PANTHER subfamily PTHR42884:SF13 (NEUROENDOCRINE CONVERTASE 2) and both are
IBD seeds at the bilaterian PC2 PAINT node PTN000082858. ProtNLM2 outputs were not opened or used.

### Deep research

`just deep-research-falcon human PCSK2 --fallback perplexity-lite` failed: falcon returned
"Edison API request failed: Failed to authenticate" (403), and the perplexity-lite fallback also
failed. No deep-research file exists. Literature was gathered from the GOA-cited papers plus a
targeted PubMed (eutils) search, cached with `cache_publication`.

### Evolutionary grounding

- UniProt: PANTHER PTHR42884:SF13; "Belongs to the peptidase S8 family. Furin subfamily."
- PAINT (interpro/panther/PTHR42884/PTHR42884-paint.tsv), node PTN000082858 (Bilateria):
  IBD for GO:0016486 peptide hormone processing (seeds: FB amon, MGI Pcsk2, RGD Pcsk2, human PCSK2,
  WB egl-3), GO:0005576 extracellular region, GO:0043005 neuron projection. IRD (negated) for
  GO:0000139 Golgi membrane and GO:0005802 trans-Golgi network, inherited from the opisthokont node
  PTN000082856: curators deliberately did not give the PC2 clade the Golgi terms of furin/KEX2.
  No Golgi term was added here.
- Deep node PTN002451026 (whole family): serine-type endopeptidase activity, membrane, protein
  processing.

### What is experimentally established for HUMAN PC2

- Serine-type endopeptidase activity at dibasic sites, calcium-dependent, pH optimum 5.0-5.5;
  cleaves des-31,32-proinsulin at the CA junction (recombinant human PC2 in Xenopus oocytes)
  [PMID:7626024 "Recombinant PC2 had the same substrate specificity as the Type-2 endopeptidase,
  cleaving at the CA-junction (Lys64, Arg65) of human des-31,32-proinsulin to generate insulin"].
- Glucagon liberation from human proglucagon by human PC2 in GH4C1 cells; auto-activation of
  secreted proPC2 [PMID:28719828 "we also evaluated the cleavage of co-transfected proglucagon to
  glucagon; the liberation of this peptide is known to be dependent on PC2 expression"].
- Human islets: PC2 is in alpha cells, not healthy beta cells; PC2 inhibition blocks glucagon but
  not insulin production [PMID:32291281 "healthy human β-cells process proinsulin by PC1/3 but not
  PC2"].
- Secretion and trafficking requirements in COS-7 cells [PMID:9020868].
- proPC2 acid-pH membrane association [PMID:8034613, Xenopus oocyte expression].
- 7B2 dependence of human proPC2 activation [PMID:25811241, human PC2 in SK-N-MC cells].

### Inferred from orthologs (same subfamily/node), not shown for human

- Enkephalin processing (recombinant mouse PC2, PMID:9712897).
- proIAPP N-terminal cleavage (PC2-null mouse islets, PMID:11246872).
- Neuron projection / nerve terminal localization (rat brain, PMID:10906712; IBA).

### Decisions

- Generic terms (endopeptidase, serine-type peptidase, proteolysis, protein processing) MODIFY to
  GO:0004252 / GO:0016486.
- Transport vesicle (constitutive vesicles by definition) MODIFY to secretory granule.
- Insulin processing KEEP_AS_NON_CORE (true capability; not the physiological route in human beta
  cells).
- Nervous system development MARK_AS_OVER_ANNOTATED (downstream of peptide processing; PAINT did not
  propagate it).
- Both protein binding rows REMOVE (BOD1 Y2H; 7B2 interaction is a function of 7B2 on PC2).
- NEW GO:0120116 glucagon processing: PC2 is the catalyst (passes participation test). Only DPP4
  (Reactome TAS) carries this term in QuickGO; parallel GO:0030070 insulin processing is carried by
  the convertases, so the absence looks like term recency.

### For transfer to amon

Transferable at the PC2 node: serine-type endopeptidase activity, peptide hormone processing,
secretory granule, extracellular region, neuron projection. Substrate-specific human processes
(glucagon, insulin) should not be transferred to fly as such; amon's own evidence is AKH production
[family review cites PMID:20523747].
