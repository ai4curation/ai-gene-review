# AIM33 (YML087C) — curation notes

UniProt: Q04516 | SGD: S000004552 | GeneID: 854887 | 312 aa | Chromosome XIII

## Summary of the problem
AIM33 ("Altered Inheritance of Mitochondria 33") is a **poorly characterized** *S. cerevisiae*
protein. UniProt names it "Uncharacterized oxidoreductase AIM33" (EC=1.-.-.-). SGD calls it a
"Protein of unknown function". It is a member (by sequence/domain) of the flavoprotein pyridine
nucleotide cytochrome reductase family (the cytochrome-b5 reductase, CYB5R, superfamily), but
its own catalytic activity, physiological electron acceptor, and cellular role are **not
experimentally established**. This is a "dark gene": the deliverable is an honest knowledge_gaps
section plus domain/orthology-grounded (not invented) reasoning.

## KNOWN (evidence-supported)

### Domain architecture / family (from UniProt Q04516)
- Belongs to the **flavoprotein pyridine nucleotide cytochrome reductase family**
  (`SIMILARITY {ECO:0000305}`).
- **FAD-binding FR-type domain** at residues 70–173 (`FT DOMAIN ... /evidence=ECO:0000255|PROSITE-ProRule:PRU00716`).
- Pfam: **PF00970 FAD_binding_6** + **PF00175 NAD_binding_1** — the classic two-domain
  FAD/NAD(P)H reductase module of cytochrome-b5 reductases.
- InterPro: IPR001834 (CBR-like), IPR008333 (Cbr1-like FAD-bd dom), IPR017927 (FAD-bd FR-type),
  IPR001709 (Flavoprotein pyridine nucleotide cytochrome reductase), IPR001433 (OxRdtase FAD/NAD-bd).
- CDD cd06183 "cyt_b5_reduct_like".
- **PANTHER PTHR19370** "NADH-CYTOCHROME B5 REDUCTASE"; subfamily **PTHR19370:SF143**
  "PLASMA MEMBRANE-ASSOCIATED COENZYME Q6 REDUCTASE PGA3".
- KW: FAD, Flavoprotein, NAD, Oxidoreductase, Membrane, Transmembrane.
- COFACTOR: FAD (`{ECO:0000250}` — by similarity only, not measured for AIM33).
- **Reasoning**: The FAD-binding + NAD-binding module is diagnostic of a flavin-dependent
  pyridine-nucleotide:acceptor oxidoreductase. An oxidoreductase MF (GO:0016491) and even a
  cytochrome-b5-reductase-type activity are therefore *domain-defensible*. What the domain does
  NOT tell us is the physiological electron acceptor — cytochrome b5, coenzyme Q, a P450, or
  something else — which is exactly the open question.

### Membrane topology (multi-pass) — PMID:16847258 (global topology map)
- UniProt SUBCELLULAR LOCATION: **Membrane; Multi-pass membrane protein** (`{ECO:0000305}`).
- Predicted TM helices at 15–35, 42–62, 180–200 (ECO:0000255) with an N-in/loop-out topology;
  the FAD-binding domain (70–173) sits in the large loop.
- AIM33/YML087C is one of the 546 membrane proteins with an experimentally-constrained topology
  model in [PMID:16847258 "we report the cloning and expression of 617 S. cerevisiae membrane
  proteins as fusions to a C-terminal topology reporter and present experimentally constrained
  topology models for 546 proteins."]. (AIM33 is in the dataset; the paper text is genome-wide
  and does not discuss AIM33 individually.)
- **Note**: This makes AIM33 structurally DISTINCT from most soluble CYB5R enzymes. Human
  CYB5R4 (the SGD-stated homolog) is a **soluble** flavohemoprotein; MCR1 is anchored at the
  mitochondrial outer membrane. AIM33 being a genuine *polytopic* membrane reductase is unusual
  in this family and is itself a notable, under-explored feature.

### Disruption phenotype — PMID:19300474 (Hess et al., mitochondrial biogenesis screen)
- UniProt DISRUPTION PHENOTYPE: "**Increases frequency of mitochondrial genome loss.**"
  (`{ECO:0000269|PubMed:19300474}`).
- This study systematically measured the **petite frequency** (rate of generation of cells
  lacking respiratory-competent mitochondria) of ~193 deletion strains and confirmed 109 genes
  (including the AIM-named genes) with altered mitochondrial transmission phenotypes. AIM33 is
  one of these; the specific value is in the paper's supplementary tables (S2/S6), not the main
  text, so no gene-specific verbatim quote is available from the cached full text.
- WT S288C baseline: [PMID:19300474 "genetic background produce petite daughter cells at a
  baseline frequency of ~20%"] and "mutation of genes involved in mitochondrial biogenesis can
  significantly alter this rate."
- The "AIM" name (Altered Inheritance of Mitochondria) was assigned to genes discovered/confirmed
  in this class of screens for altered mitochondrial genome transmission.

### DISCREPANCY on phenotype direction (record in knowledge_gaps)
- UniProt curation of PMID:19300474: deletion **INCREASES** frequency of mitochondrial genome loss.
- SGD gene description: "null mutant displays **REDUCED** frequency of mitochondrial genome loss."
- Both cannot be literally true; the direction of the petite-frequency shift for AIM33 is
  ambiguous between the two curated sources. Either way, AIM33 loss perturbs mitochondrial genome
  maintenance/petite frequency. (Note: PMID:19300474 discusses that *decreased* petite frequency
  can indicate a "petite-negative" synthetic-lethality phenotype, so a decrease is also
  mechanistically meaningful.)

### Other large-scale phenotypes (SGD, from high-throughput surveys)
- Null mutant: cannot grow on non-fermentable carbon sources (respiratory phenotype); decreased
  calcium and sodium ion accumulation; reduced starvation and ethanol resistance; abnormal
  mitochondrial genome maintenance. (These are HTP/large-scale phenotypes, not deep mechanism.)

### Family / paralog / ortholog context
- **Paralog**: PGA3 (arose from the whole-genome duplication). PGA3 = plasma-membrane-associated
  NADH:coenzyme-Q6 reductase (the PANTHER SF143 exemplar). [WebSearch: SGD/Wikidata]
- Related family members in yeast: **MCR1** (YKL150W; mitochondrial OMM/IMS NADH-cytochrome b5
  reductase; electron donor to sterol-biosynthetic cytochrome P450s Erg11/Erg5/Erg1 and to
  fatty-acid/sterol desaturation; oxidative-stress response), **CBR1** (ER NADH-cytochrome b5
  reductase). AIM33 is a fourth, distinct member.
- **Human homolog/ortholog**: SGD states **CYB5R4**; NCBI Gene lists **CYB5R1/CYB5R3** as
  orthologs. The mapping is family-level, not an unambiguous 1:1 ortholog. Human CYB5R4 is a
  soluble flavohemoprotein (extra cytochrome-b5 and p23 domains) important for beta-cell/oxidative-
  stress protection — a different domain architecture from the polytopic yeast AIM33.

## NOT known (the real knowledge gaps)
1. **Catalytic activity of AIM33 itself.** No enzyme assay demonstrates cytochrome-b5 reductase
   (or any) activity for AIM33. EC is 1.-.-.- (class assigned, sub-subclass unknown). The
   GO:0004128 (cytochrome-b5 reductase acting on NAD(P)H) and GO:0016491 annotations are IBA/IEA
   propagations from the family, not measurements on AIM33.
2. **Physiological electron donor/acceptor.** NAD(P)H as donor is likely (NAD_binding_1 domain);
   the acceptor (cytochrome b5? coenzyme Q? a P450? a desaturase? an as-yet-unknown mitochondrial
   redox partner?) is unknown for AIM33.
3. **Cellular localization.** UniProt/GO say "Membrane / plasma membrane (IBA)". But the AIM
   phenotype and the CYB5R4 orthology imply a possible **mitochondrial** role. The IBA
   plasma-membrane call is propagated (partly via the PGA3 branch) and is not experimentally
   confirmed for AIM33; its true membrane (mitochondrial vs plasma vs ER) is unresolved.
4. **Ergosterol-pathway involvement (GO:0006696, IBA).** Established for the paralog MCR1 (electron
   donor to sterol P450s), NOT demonstrated for AIM33. This is a candidate over-annotation.
5. **Mechanism behind the AIM (mitochondrial genome maintenance) phenotype**, and even its
   direction (increase vs decrease in petite frequency; see discrepancy above).

## Annotation-by-annotation reasoning (see AIM33-ai-review.yaml)
- GO:0005886 plasma membrane (IBA) — IBA-propagated location; contradicted by predicted polytopic
  topology consistent with an internal membrane and by the mitochondrial phenotype. MODIFY toward
  the more general/defensible GO:0016020 membrane (the location is real; "plasma membrane"
  specificity is unsupported for AIM33).
- GO:0004128 cytochrome-b5 reductase activity, acting on NAD(P)H (IBA and IEA) — domain-plausible
  activity but not measured for AIM33 and possibly over-specific (electron acceptor unproven).
  Keep as non-core / mark as over-annotated: retain the reductase idea but flag that the specific
  cytochrome-b5 acceptor is not established for this paralog.
- GO:0006696 ergosterol biosynthetic process (IBA) — propagated from MCR1/PGA3; no AIM33-specific
  evidence; AIM33's phenotype points elsewhere (mitochondrial genome maintenance). Candidate
  over-annotation → MARK_AS_OVER_ANNOTATED.
- GO:0016020 membrane (IEA, UniProt SubCell) — defensible; membrane protein is well supported. ACCEPT.
- GO:0016491 oxidoreductase activity (IEA, InterPro) — the safest, best-supported MF given the
  FAD/NAD reductase module. ACCEPT (keep as the honest, general MF).
- GO:0003674 / GO:0005575 / GO:0008150 ND root annotations — placeholder root annotations
  (GO_REF:0000015). ACCEPT (standard; represent "not yet determined").

## Provenance index
- [PMID:19300474] Hess et al. 2009 PLoS Genet — mitochondrial biogenesis / petite frequency screen; source of DISRUPTION PHENOTYPE. Full text cached (abstract + body; AIM33 in supp tables only).
- [PMID:16847258] Kim et al. 2006 PNAS — global membrane topology map; AIM33 topology model. Cache has abstract plus a partial full-text (Results intro) section only, not the complete article; the quoted supporting_text is a verbatim substring of that cached text.
- [PMID:9169872] Bowman et al. 1997 Nature — chromosome XIII sequence (genome). Abstract only.
- [PMID:24374639] Engel et al. 2014 G3 — reference genome reannotation. Full text cached.
- SGD S000004552 (WebFetch), NCBI Gene 854887 (WebFetch), WebSearch — family/paralog/ortholog and additional phenotypes.
- UniProt Q04516 (AIM33-uniprot.txt) — domains, cofactor, topology, family, disruption phenotype.

## Deep research provenance
- Falcon deep research was attempted (first run timed out at 600s; perplexity-lite fallback failed
  with a 401 quota error). A single retry of falcon was run. This review is grounded directly in
  UniProt (Q04516), GOA, cached primary literature (PMID:19300474, PMID:16847258), and
  PubMed-verified secondary sources (SGD S000004552, NCBI Gene 854887); it does not depend on the
  deep-research file. If the falcon retry produced `AIM33-deep-research-falcon.md`, it is included
  for the record but was not the basis for any specific claim.
