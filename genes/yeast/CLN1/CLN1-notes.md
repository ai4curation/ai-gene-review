# CLN1 (YMR199W, P20437) — curation notes

*Saccharomyces cerevisiae* S288C. Reviewed for the
[Yeast Cell Cycle & Translation Control](../../../projects/YEAST_CELL_CYCLE.md)
project (issue #3960).

Automated deep research was unavailable in this run (no provider API keys were
configured, so `just deep-research yeast CLN1` failed for every provider). These
notes are therefore hand-assembled from the cached publications in
`publications/` plus the UniProt record, and are **not** a
`-deep-research-<provider>.md` file.

## Identity and family

- 546 aa, single chain, no reported processing
  [file:yeast/CLN1/CLN1-uniprot.txt "SEQUENCE   546 AA;  62050 MW;"].
- Cyclin-box protein: Pfam `PF00134` Cyclin_N, PROSITE `PS00292` CYCLINS,
  PIRSF `PIRSF001770` Cyclin_CLN, InterPro `IPR014399` Cyclin_CLN, and the
  CDD model `cd20559` CYCLIN_ScCLN_like
  [file:yeast/CLN1/CLN1-uniprot.txt "CDD; cd20559; CYCLIN_ScCLN_like; 1."].
  UniProt places it in the cyclin family
  [file:yeast/CLN1/CLN1-uniprot.txt "Belongs to the cyclin family."].
- The `IPR014399`/`PIRSF001770` Cyclin_CLN signature is the Cln1/Cln2-type
  G1/S cyclin family, distinct from Cln3 and from the B-type Clb cyclins. Only
  one disordered region is annotated (residues 224-265, MobiDB-lite), i.e. the
  cyclin box is the only structured module; the long C-terminal half is the
  PEST-rich instability region characteristic of this family.
- A low-abundance protein: 319 molecules/cell in log-phase SD medium
  [file:yeast/CLN1/CLN1-uniprot.txt "Present with 319 molecules/cell in log phase SD medium."].

## Discovery and genetics

- *CLN1* and *CLN2* were isolated together as dosage suppressors of a
  *cdc28* temperature-sensitive allele, which is what first tied them to the
  Cdc28 kinase [PMID:2569741 "Two Saccharomyces cerevisiae genes were isolated based upon their
  dosage-dependent rescue of a temperature-sensitive mutation of the gene CDC28"]. The two
  gene products are close paralogs [PMID:2569741 "CLN1 and
  CLN2 encode closely related proteins that also share homology with cyclins."].
- The three *CLN* genes are mutually redundant for viability but collectively
  essential: loss of all three arrests cells in G1
  [PMID:2147225 "Null mutations in three genes encoding cyclin-like proteins (CLN1, CLN2, and
  CLN3) in Saccharomyces cerevisiae cause cell cycle arrest in G1 (cln arrest)."], and any one
  suffices [PMID:2574633 "Mutational elimination of the CLN1, CLN2, and DAF1/WHI1 products leads
  to cell cycle arrest independent of cell type, while expression of any one of
  the genes allows cell proliferation."].
- Conditional *CLN1* expression was the experiment that localised the essential
  Cln requirement to G1 [PMID:2574633 "Using strains where CLN1 was expressed
  conditionally, the essential function of Cln proteins was found to be limited to
  the G1 phase."]. The arrest point is Start
  [PMID:2147225 "These results are consistent with a specific CLN requirement for START transit."].
  Those two papers are the `WITH/FROM`-paired IGI rows for
  `GO:0007089 traversing start control point of mitotic cell cycle`, with
  *CLN3* (SGD:S000000038) and *CLN2* (SGD:S000006177) as the interacting genes —
  exactly the redundancy design the IGI code is for. Watch the SGD ids here: CLN1
  is S000004812, CLN2 is S000006177 and CLN3 is S000000038, so the numbering does
  not follow the gene names, and the IBA `WITH/FROM` lists are easy to misread.
- The inferred mechanism from the outset was activation of Cdc28
  [PMID:2574633 "The data
  are consistent with the hypothesis that Cln proteins activate the Cdc28 protein
  kinase, shown to be essential for the G1 to S phase transition in S. cerevisiae."].

## Cln1 is in the abundant, cell-cycle-regulated tier of Cln proteins

Tyers et al. compared the three Cln proteins directly, and Cln1 falls on the
Cln2 side of every axis:

- Abundance and kinase activity: [PMID:8387915 "We find that Cln3 is a much rarer protein than Cln1 or Cln2 and has a
  much weaker associated histone H1 kinase activity."] — i.e. Cln1-associated
  Cdc28 is a strong histone H1 kinase.
- Periodicity: [PMID:8387915 "Unlike Cln1 and Cln2, Cln3 is
  not significantly cell cycle regulated, nor is it down-regulated by mating
  pheromone-induced G1 arrest."]. Consistent with UniProt
  [file:yeast/CLN1/CLN1-uniprot.txt "CLN1 and CLN2 mRNAs fluctuate periodically in the"].
- Position in the circuit: Cln3 acts upstream and induces *CLN1*; Cln1 is a
  less potent activator of Start when expressed artificially
  [PMID:8387915 "In similar experiments, CLN1 is less efficient than CLN3 at
  activating Start."]. So Cln1 is an output/feedback cyclin, not the cell-size sensor.
- *CLN1* transcription is SBF-dependent late-G1 transcription
  [PMID:10409718 "CLN1 transcription is regulated through MCB elements that are dependent upon SBF (Swi4/Swi6)"].

## Direct Cln1 biochemistry: the Cln1-Cdc28 holoenzyme

The cleanest CLN1-specific molecular-function experiment is the Stb1 kinase
assay. Cyclin-tagged complexes were pulled from yeast and assayed:

- [PMID:10409718 "Epitope-tagged cyclins were used to immunoprecipitate Cln1-Cdc28 and Cln2-Cdc28 kinases from yeast extracts"]
- [PMID:10409718 "Stb1 was an excellent substrate for both the Cln1-Cdc28 and Cln2-Cdc28 kinases in vitro and was a better in vitro substrate than histone H1"]
- and the genetics assign the in vivo kinase to Cln1/Cln2 rather than Cln3
  [PMID:10409718 "several observations suggest that Cln1-Cdc28 and Cln2-Cdc28 are the physiological kinases for Stb1 phosphorylation"].

This is a Cln1-containing kinase complex, with Cln1 as the regulatory subunit —
the direct basis for both `GO:0016538`/`GO:0061575` and
`GO:0000307 cyclin-dependent protein kinase holoenzyme complex`. ComplexPortal
curates the complex explicitly as `CPX-1699` CLN1-CDC28 kinase complex
[file:yeast/CLN1/CLN1-uniprot.txt "ComplexPortal; CPX-1699; CLN1-CDC28 kinase complex."].

Cln1 also binds the second CDK Pho85, with two curated experiments
[file:yeast/CLN1/CLN1-uniprot.txt "P20437; P17157: PHO85; NbExp=2; IntAct=EBI-4479, EBI-13327;"].
The cited paper (PMID:9032248) is cached abstract-only and its abstract is about
the Pcl cyclins, so the Cln1-Pho85 affinity experiment itself is not visible in
our cache; the interaction is nonetheless recorded by IntAct and UniProt. Whether
a Cln1-Pho85 complex is physiologically meaningful is unresolved.

## Localisation

Cln1-GFP is in both compartments, imaged side by side with Cln2-GFP:
[PMID:11080155 "Cln1–GFP as well as Cln2–GFP were localized in both the nucleus and the cytoplasm"].
This is the IDA source for the `GO:0005634` and `GO:0005737` rows. Note that the
finer-grained localisation results in the Cln literature (nuclear exclusion driven
by C-terminal phosphorylation, concentration at sites of polarised growth) were
obtained with **Cln2**, not Cln1; for Cln1 the evidence resolves no further than
nucleus and cytoplasm.

## Turnover

Cln1 and Cln2 are substrates of SCF(Grr1), not SCF(Cdc4)
[PMID:11080155 "ubiquitylation of the G 1 cyclins, Cln1 and Cln2, and the bud emergence protein Gic2 is mediated by SCF Grr1"].
This is a review statement within the cited paper rather than a Cln1 experiment
in it, so it is recorded here as background, not as annotation support.

## Where Cln1 differs from Cln3: post-Start execution and Cln1/2-specific substrates

- Division of labour: [PMID:10409718 "CLN1 and CLN2 are not required for gene activation but are important for the proper execution of other Start-related events such as budding and DNA synthesis"].
  Overexpressed *CLN1* is nonetheless able to substitute for the missing Start
  transcription in a *stb1 cln3* strain
  [PMID:10409718 "Overexpression of either CLN1 or CLN2 suppressed the slow-growth phenotype of the stb1Δcln3 Δ mutant"].
- Cln1 shares with Cln2 a cyclin-specific substrate repertoire reached through
  LP docking motifs. Direct Cln1 experiment:
  [PMID:21945277 "phosphorylation of the Ste5 and Ste20 fragments was observed only with Cln1 and Cln2, and not with Cln3, Clb5, or Clb2"],
  and these are described as a cyclin class property
  [PMID:21945277 "Notably, Ste20 and Ste5 are Cln1/2-specific substrates [10–12], but the mechanistic basis of this specificity is unknown."].
  Ste5 and Ste20 are pheromone-pathway components, so Cln1-Cdc28 contributes to
  shutting off mating signalling after Start.
- The late-G1 cyclin-CDK burst that *CLN1* contributes to is required for
  morphogenesis specifically, and not for replication
  [PMID:14688790 "a build-up or burst of G1
  cyclin-dependent kinase (CDK) activity through activation of the cyclin genes
  CLN1,2 and PCL1,2 is essential for cell morphogenesis, but not for other events
  associated with the G1-S-phase transition, including DNA replication."]. This is a
  combined *cln1 cln2 pcl1 pcl2* phenotype, not a *cln1* phenotype, so it informs
  the description but does not by itself license a CLN1 morphogenesis annotation.

## Annotation decisions and the one `NEW` I decided against

Actions mirror those taken on the paralog `genes/yeast/CLN2`, because CLN1's
annotation set is a strict subset of CLN2's and the same term-level arguments
apply:

- `GO:0016538` (4 rows: IBA, IEA, IDA x2) -> `MODIFY` to
  `GO:0061575 cyclin-dependent protein serine/threonine kinase activator activity`.
  Cln1 does not merely regulate Cdc28, it activates it; the regulator term is the
  parent and `GO:0061575` is the supported descendant.
- `GO:0005515` (7 IPI rows, 6 with CDC28 and 1 with PHO85) -> `MODIFY` to
  `GO:0019901 protein kinase binding`. Both partners are protein kinases, and the
  interaction-detection rows support binding; the activator activity is asserted
  separately from the IDA rows. Bare protein binding is uninformative and the
  policy forbids `ACCEPT`/`KEEP_AS_NON_CORE` on it.
- `GO:2000045` and `GO:1902806` (both unsigned "regulation of G1/S") -> `MODIFY`
  to `GO:1900087 positive regulation of G1/S transition of mitotic cell cycle`.
  A sign correction, not a redundancy claim.
- `GO:0000082`, `GO:0000307`, `GO:0005634`, `GO:0005737`, `GO:0007089` ->
  `ACCEPT`.

**Considered and rejected:** a `NEW`
`GO:0180040 negative regulation of pheromone response MAPK cascade` row, on the
strength of the Cln1-specific Ste5/Ste20 phosphorylation above. The comparator
check argues against it. In budding yeast only PPQ1 and AKR1 carry `GO:0180040`
(QuickGO, taxon 559292/4932, queried 2026-10-23), and CLN2 — which has
considerably stronger Ste5 evidence than CLN1, including PMID:17289571 — does not
carry it either. What CLN2 carries instead is
`GO:0000321 re-entry into mitotic cell cycle after pheromone arrest` (IGI,
PMID:9927449). That is a convention about how SGD annotates the Cln-pheromone
relationship, not a twenty-year gap, so the point is raised in
`suggested_questions` rather than asserted. CLN1 has no `GO:0000321` row of its
own and I did not propose one: the PMID:9927449 genetics behind CLN2's rows is
not in our cache and I cannot tell whether CLN1 was assayed.

## Open questions

Recorded in `suggested_questions` / `suggested_experiments` of the review:
whether Cln1 and Cln2 are genuinely interchangeable or have private substrates;
whether the Cln1-Pho85 interaction is physiological; and what, if anything,
distinguishes Cln1's contribution to the morphogenesis burst from Cln2's.
