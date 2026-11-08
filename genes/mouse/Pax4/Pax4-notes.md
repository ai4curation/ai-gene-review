# Pax4 (mouse, P32115) review notes

Journal for the de novo review of mouse Pax4 (MGI:97488), done for the
BGEEDB_EXPRESSION project (projects/BGEEDB_EXPRESSION.md). Mouse was chosen
because Bgee has the richest data for this gene in mouse.

## 2026-11-08: sources read

- UniProt P32115 (Swiss-Prot). Paired domain 5-131, homeodomain 170-229,
  transcription-repression region 278-349 (ECO:0000269, PubMed:10567552). No
  octapeptide and no Pax6-type PST transactivation domain is annotated.
- Deep research (claude_code provider) read as leads only. Two errors found
  and recorded in its reference_review:
  - It attributes PMID:10364449 to "Ritz-Laser B et al.". The paper is
    Kalousova et al. 1999, BBRC 259:510 (UniProt RN[3]; cached abstract).
  - It says Pax4 "restrains Arx-dependent subtypes: L (GLP-1), I (CCK),
    K (GIP), G and N cells". PMID:22570716 says the opposite for K, G and N
    cells: ["Pax4, like Arx, is necessary for the proper development of GIP,
    Gastrin and Neurotensin cells in the small intestine while
    Serotonin-producing cells are exclusively Pax4-dependent"].
- Cached publications: full text for 19665969, 22570716, 19012751, 24951566,
  40614820 and 26503027. The rest are abstract-only (9121556, 14561778,
  10567552, 10891400, 15930104, 14729487, 14970313, 10197584, 18818287,
  17260022, 10601637, 10364449, 9439631, 37883554, 26319183). I fetched
  10364449, 9439631, 37883554 and 28473536 in this session.

## Core biology (with provenance)

- Bipartite DNA binding: [PMID:10567552 "identified a bipartite consensus DNA
  binding sequence consisting of a homeodomain binding site separated from a
  paired domain binding site by 15 nucleotides"]. The homeodomain dimerises on
  inverted TAAT repeats [PMID:10364449 "The Pax-4 homeodomain was shown to
  preferentially dimerize on DNA sequences consisting of an inverted TAAT
  motif, separated by 4-nucleotide spacing"].
- Active repressor, not only a competitor of Pax6: [PMID:10567552 "This
  repression is not simply due to competition with the PAX6 transcriptional
  activator for the same binding site"]; [PMID:10891400 "stable expression of
  Pax4 in a rat glucagon-producing cell line inhibits the endogenously
  expressed glucagon gene completely"].
- Weak activation potential: [PMID:10364449 "The Pax-4 transactivation domain
  was localized within its C-terminal region, which transactivated GAL-based
  reporter 2.5-fold less than the C-terminal region of Pax-6"]. So
  GO:0000981 (sign-neutral Pol II TF activity) is the right umbrella; the
  repressor term GO:0001227 is the core activity.
- Pancreatic fate allocation: [PMID:9121556 "Inactivation of Pax4 by
  homologous recombination results in the absence of mature insulin- and
  somatostatin-producing cells (beta and delta, respectively) in the pancreas
  of Pax4 homozygous mutant mice, but glucagon-producing alpha cells are
  present in considerably higher numbers"]; cross-repression with Arx
  [PMID:15930104 "both Arx and Pax4 act as transcriptional repressors that
  control the expression level of one another"]; sufficiency
  [PMID:19665969 "Pax4 forces endocrine precursor cells, as well as mature
  alpha cells, to adopt a beta cell destiny"].
- Delta cells: needed in the single mutant, but in Arx/Pax4 double mutants
  delta cells form almost exclusively [PMID:15930104 "concomitantly with a
  virtually exclusive generation of somatostatin-producing cells"]. So Pax4's
  delta-cell role runs through Arx repression rather than a positive
  delta-specifying activity. I did not add a NEW pancreatic D cell
  differentiation row.
- Gut: [PMID:22570716 "The strong induction of Arx, both in the small
  intestine and colon of Pax4 KO mice, suggests that Pax4 controls the
  specification of endocrine subtypes through the repression of Arx"].
- Human: complete PAX4 loss gives transient neonatal diabetes and nothing
  else [PMID:40614820 "No extra pancreatic features were reported in either
  patient."].

## Eye and brain IBA rows: arguing with the node

- `just paint-losses mouse Pax4`: no IRD or IKR on the lineage.
- No FamilyReview for PTHR45636 (only entries, metadata and paint.tsv), so a
  gene-level REMOVE creates no family/gene disagreement.
- PAINT IBDs (interpro/panther/PTHR45636/PTHR45636-paint.tsv):
  - PTN002900580 (Euteleostomi): GO:0003309 (seeds include MGI:97488, Pax4
    itself); GO:0030900 (seeds mouse and rat Pax6, zebrafish pax6a and
    pax6b); GO:0060041 (seeds mouse and rat Pax6, **RGD:620433 rat Pax4**,
    zebrafish pax6a, pax6b and pax10).
  - PTN008693041 (Bilateria): GO:0007420 (fly ey and toy, Pax6 orthologs);
    GO:0007423 (adds RGD:620433 and pax10).
- ZFIN ids resolved via UniProt xrefs: ZDB-GENE-081022-10 is pax10 (I3IT91),
  ZDB-GENE-001031-1 is pax6b, ZDB-GENE-990415-200 is pax6a. Zebrafish pax4
  (ZDB-GENE-041210-244) is not a seed of any IBD.
- Rat Pax4 seed annotations (QuickGO, UniProtKB:O88436, retrieved today): the
  only rat Pax4 rows to retina development, circadian rhythm, response to cAMP
  and response to xenobiotic stimulus are IEP (PMID:19012751, PMID:18818287).
  So an expression pattern seeded an IBD, and Ensembl Compara projected the
  same IEP rows to mouse as GO_REF:0000107 IEA rows.
- What PMID:19012751 actually shows: Pax4 mRNA appears in rat photoreceptors
  only after birth [PMID:19012751 "Pax4 expression is not detectable in the
  foetal eye; however, postnatal Pax4 transcript levels rapidly increase"],
  peaks at P18-P30, is rhythmic in the adult, and the authors themselves say
  [PMID:19012751 "The finding that Pax4 expression is highest in the adult
  argues against a role in development, as is the case with Pax6."]. They
  speculate about a role in maturing photoreceptors. No function was tested.
- Tree: `genes/mouse/Pax4/Pax4-bioinformatics/panther_tree_paths.py` (output in
  `panther_tree_paths.md`) shows that PANTHER 19 splits PAX4 from PAX6 twice:
  once at a Mammalia duplication (PTN000676674) below a Tetrapoda duplication,
  and once at a Neopterygii duplication (PTN009180006) for gar, medaka and
  zebrafish pax4. Synteny puts a single origin in the 2R genome duplications
  [PMID:24951566 "Our synteny analysis showed that Pax4, -6, and -10
  originated in the 2R genome duplications early in vertebrate evolution."].
  The PANTHER topology is therefore not species-reconciled for this class, and
  there is no single Pax4 clade node on which PAINT could place a loss.
- Divergence evidence on the Pax4 lineage:
  - [PMID:24951566 "The Pax4 genes of mammals and teleost fishes are not
    implicated in the development of eyes"];
  - Pax4 and Pax6 are not interchangeable [PMID:10364449 "Pax-4 and Pax-6
    cannot substitute for each other in tissue with overlapping expression of
    both genes"];
  - the mouse knockout phenotype reported in the literature is confined to
    pancreatic and intestinal endocrine cells (PMID:9121556, PMID:22570716),
    and human nulls have no extra-pancreatic features (PMID:40614820).
- Bgee (RESULTS.md):
  - Eye calls are neonatal and early-postnatal eyeball and lens only (scores
    47-77). In bgee_calls.tsv, retina and retinal neural layer are absent
    (gold) for Pax4 while Pax6 is present at the top of its profile. That is
    a controlled absence, but stage-merged, so for a developmental term it
    counts as consistency only.
  - Forebrain presence is one Theiler stage 21 in situ timepoint plus adult
    Affymetrix hippocampus and cortex. Embryonic brain is absent (gold, 13.1)
    in bgee_calls.tsv.
  - Pineal body: RESULTS.md section 4 lists no stage-resolved Pax4 present
    call. The stage-merged bgee_calls.tsv has Pax4 absent from pineal body
    (gold, 52.83), where Pax6 is present (gold, 81.75). So the rat pineal
    pattern behind the IEP rows is not even confirmed in mouse. These are not
    developmental terms, so this is the one controlled absence that counts
    here, though it is still a minor point beside the IEP argument.
  - As the project concluded, presence cannot establish function and absence
    here is stage-merged. Expression is consistent with the decision, not its
    basis.
- Decisions:
  - Brain development and forebrain development: REMOVE (no Pax4 evidence of
    any kind; IBDs rest on Pax6/ey/toy biology; Pax4 diverged).
  - Retina development (IBA and the rat-IEP IEA) and sensory organ
    development: MARK_AS_OVER_ANNOTATED, not REMOVE. A role in late
    photoreceptor maturation remains untested, because germline nulls die by
    P3 and no conditional retina knockout exists, so the claim exceeds the
    evidence rather than being contradicted.

## Other rat-derived rows

- Circadian rhythm, response to cAMP, response to xenobiotic stimulus: IEA
  copies of rat IEP rows. The mouse rows assert participation, while the
  papers measured transcript changes: diurnal mRNA in retina and pineal, and
  suppression by adrenergic agonists and a cAMP analogue. REMOVE.
- Negative regulation of apoptotic process: rat INS-1E shRNA knockdown (IMP,
  PMID:17260022) plus mouse gain-of-function and reporter data (PMID:26503027).
  This is a genuine but secondary adult beta-cell survival role. MODIFY to
  GO:2000675 negative regulation of type B pancreatic cell apoptotic process.
- Double-stranded DNA binding / negative regulation of DNA-templated
  transcription (rat IDA PMID:10601637, C2 box of the insulin promoter): MODIFY
  to GO:0000978 and GO:0000122.

## Terms checked with OAK (sqlite:obo:go)

- GO:0000978 is_a GO:0000976, GO:1990837, GO:0003690 and GO:0003677, so the
  MODIFYs to GO:0000978 are refinements.
- GO:0003309 is_a GO:0035883 (enteroendocrine cell differentiation).
- GO:2000227 negative regulation of pancreatic A cell differentiation is_a
  GO:7770019 (already carried), so per CLAUDE.md I did not add it as NEW.
  core_functions uses the carried parent GO:7770019 instead, because
  validation warns on a core-function process absent from the annotations.
  It is a candidate for a future curator-made annotation (comparators: Hes1
  carries GO:2000227 by IMP, and Arx carries GO:0003310 by IMP,
  PMID:14561778).

## Open questions

See suggested_questions in the review: PAINT IRDs on the PAX4 clades, the
rat IEP seed, adult photoreceptor and pineal function, and whether Arx is a
direct in vivo target.
