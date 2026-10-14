# Notes for DANRE cyp51

- Core function is ER sterol 14-alpha-demethylase activity in cholesterol biosynthesis [PMID:24361620 "The recombinant protein bound lanosterol and"].
- Response to yeast is kept as non-core because the cited study places Cyp51 in a host-pathogen/redox network, not as the enzyme's conserved sterol-biosynthetic role [PMID:23947337 "Six zebrafish proteins in the pathogenesis subnetwork, that is, Cyb5r2, Cyp51"].

## Re-review 2026-09-28

Full re-review against the refreshed GOA/UniProt records and the cached full text of
PMID:24361620 (full_text_available: true, PMC4118742), which had previously been cited
only through two short abstract fragments.

- **GO:0033488 (cholesterol biosynthetic process via 24,25-dihydrolanosterol, IBA) row
  deleted.** The term is obsolete in the current ontology (QuickGO: "OBSOLETE. The chemical
  reactions and pathways resulting in the formation of cholesterol ... via the intermediate
  24,25-dihydrolanosterol") and the row is absent from the refreshed goa.tsv, so the yaml
  row was stale rather than a GOA remapping. The previous review had kept it with a MODIFY
  to GO:0006695.
- **GO:0006695 cholesterol biosynthetic process added as NEW (involved_in).** This restores
  the pathway-level process the obsoletion removed. Participation is by catalysis, not by
  necessity: the zebrafish enzyme performs a step of the pathway itself
  [PMID:24361620 "Sterol 14α-demethylase activity was catalyzed in the reconstituted assay
  with both CYP51ZF and CYP51ZFT, determined by GC-MS detection of production of 4,
  4-dimethyl-5α-cholesta-8,14,24-triene-3ß-ol (FF-MAS)"], and UniProt places it at
  "zymosterol from lanosterol: step 1/6". Comparator check via QuickGO
  (goId=GO:0006695&taxonId=7955, 41 annotations): lss, dhcr7, tm7sf2 and hsd17b7 - zebrafish
  enzymes in the same catalytic role in this pathway - all carry the term, so its absence
  here is an ontology artefact, not a curation convention.
- **GO:0016491 oxidoreductase activity (IBA) resolved from PENDING to MODIFY -> GO:0008398.**
  The PAINT node placement is not disputed; the issue is granularity (TERM_SCOPING_PROBLEM /
  GRANULARITY_MISMATCH). propagation_review records PANTHER:PTN001209376 as SUPPORTS_TRANSFER
  and notes that the target's own ZFIN:ZDB-GENE-040625-2 in the WITH/FROM is the expected
  marker of experimental grounding, not circularity.
- **All templated "consistent with the curated UniProt/GOA record" summaries replaced** with
  the actual evidence for each claim, and the single pasted FUNCTION quote replaced with the
  line that bears on each term: catalytic quotes for the activity terms, the heme/CO-spectrum
  quotes for the cofactor terms, the SUBCELLULAR LOCATION line for the localization terms.
- Key quotes now carrying the review: substrate binding
  [PMID:24361620 "CYP51ZFT demonstrated a Type I spectrum when mixed with 35μM lanosterol
  (Figure 4B), reflecting a heme Fe spin-state change indicative of substrate binding to the
  active site."]; turnover
  [PMID:24361620 "the conversion of 50 μM lanosterol to the 4,
  4-dimethyl-5α-cholesta-8,14,24-triene-3β-ol metabolite was measured as 3.20 nmol/min/nmol
  CYP51ZFT"]; cofactor requirement
  [PMID:24361620 "The reaction demonstrated NADPH dependence, ketoconazole sensitivity, and
  potassium cyanide insensitivity."]; heme iron
  [PMID:24361620 "binding of antifungal azole compounds to CYP51 produces a Type II spectral
  shift, as the inhibitor imidazole N3 or triazole N4 binds directly with the heme iron"].
- **GO:0005789 ER membrane kept as ACCEPT but the basis is now stated honestly**: UniProt
  assigns the compartment by similarity to mouse Q64654 and predicts a single-pass helix; the
  only zebrafish-relevant statement is that CYP51 is generally "a microsomal enzyme"
  [PMID:24361620]. The falcon report agrees and says explicitly that no zebrafish localization
  experiment exists in its corpus.
- **GO:0001878 response to yeast (IDA) kept as KEEP_AS_NON_CORE with a real argument.** The
  cited study is a network-inference paper; its evidence for cyp51 is transcript repression
  during infection [PMID:23947337 "Six zebrafish proteins in the pathogenesis subnetwork, that
  is, Cyb5r2, Cyp51, Kmo, Nsdhl, Sc5d, and zgc:77112, were annotated with oxidation-reduction
  process (Figure 3) and all of their gene expressions were repressed over time"]. The gene
  product does no work in the antifungal response, so the term is peripheral - but not
  contradicted, and an experimental curator call is not overruled on that basis.
- reference_review added to both PMIDs (PMID:24361620 HIGH/VERIFIED; PMID:23947337
  LOW/VERIFIED, with a note that it carries no direct assay of Cyp51). findings expanded for
  both. description rewritten as standalone biology including organ expression
  [PMID:24361620 "The highest levels of expression were found in intestine in both sexes,
  followed by liver, especially in female, and then brain"]. Three suggested_questions and two
  suggested_experiments added (the file previously had none).
- Validation: zero errors, zero warnings.
