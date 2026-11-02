# MITH1 (Chlamydomonas reinhardtii) curation notes

UniProt A0A2K3DMK6 (TrEMBL, "Uncharacterized protein"). Locus Cre06.g259100
(CHLRE_06g259100v5). 1,304 aa, 138,446 Da predicted. Aliases are SAGA3
(Fauser et al. 2022) and MITH1, MIssing THylakoids 1 (Hennacy et al. 2024).

GOA had 0 rows at review time, so every annotation in the review is a NEW
proposal.

## Deep research

Deep research was not run. The falcon provider returns HTTP 402 and perplexity
is not available in this environment, so the wrapper was skipped as
instructed. The review rests on the cached primary literature below. There is
no `-deep-research-*.md` file for this gene.

## Sequence features (UniProt record)

- Long predicted coiled-coil segments: 208-313, 396-633, 683-710 and 739-990
  (SAM:Coils). There is also a Tropomyosin-like SUPFAM hit (SSF57997).
- Disordered, low-complexity and Gly-rich regions at 60-180, 1194-1222 and
  1258-1304 (MobiDB-lite).
- No CBM20 starch-binding domain, unlike SAGA1 and SAGA2.
- No predicted transmembrane segment.
- No detectable Rubisco-binding motif [PMID:39548241 "it lacks any detectable
  Rubisco-binding motif21"].
- The PANTHER PTHR43941 "structural maintenance of chromosomes protein 2" hit
  probably reflects only the generic long coiled-coil. There is no evidence of
  SMC-like function, so it is ignored.

## Literature summary

### Mackinder et al. 2017 (PMID:28938113)
- Lists Cre06.g259100 as a pyrenoid matrix protein of unknown function
  [PMID:28938113 "a protein of unknown function
  (Cre06.g259100; Kobayashi et al., 2016)"]. This was superseded by the
  tubule localization below.

### Fauser et al. 2022, Nat Genet (PMID:35513725)
- A genome-wide mutant screen found that the gene is needed for normal growth
  at low CO2 and named it SAGA3 for its homology to SAGA1 and SAGA2
  [PMID:35513725 "We named one of these genes, Cre06.g259100, SAGA3 (STARCH
  GRANULES ABNORMAL FAMILY MEMBER 3) because its protein product shows homology
  to the two pyrenoid structural proteins SAGA1 and SAGA2"].
- It localizes to the pyrenoid [PMID:35513725 "Consistent with a role in the
  CCM, SAGA3 localizes to the pyrenoid"].

### Hennacy et al. 2024, Nat Plants (PMID:39548241; preprint PMID:39211136)
- Mutant phenotype and complementation. mith1 pyrenoids lack matrix-traversing
  membranes, and MITH1-Venus restores them [PMID:39548241 "In the complemented
  strain mith1;MITH1-Venus, an apparently normal matrix-traversing membrane
  tubule network is restored"].
- Extension, not initiation. Membranes start at the right place but stall at
  the matrix surface [PMID:39548241 "These observations suggest that pyrenoid
  membrane formation initiates at the correct cellular location in the mith1
  mutant but then stalls before these membranes are extended through the
  pyrenoid matrix."].
- Localization. MITH1 is on the matrix-traversing membranes, not in the matrix
  [PMID:39548241 "Whereas MITH1 was previously proposed to localize to the
  Chlamydomonas pyrenoid matrix19,20, here we observed that it localizes to and
  functions at the matrix-traversing membranes."]. It co-pellets with membranes
  and is released by detergent [PMID:39548241 "MITH1 co-pelleted with membranes
  in the absence of detergent and was solubilized when detergent was added"].
- Interactions:
  - Reciprocal IP-MS shows that MITH1 and SAGA1 bind [PMID:39548241 "SAGA1 was
    MITH1’s most-abundant specific interactor"].
  - No yeast two-hybrid interaction with Rubisco or EPYC1 was found
    [PMID:39548241 "We could not detect evidence of direct MITH1 physical
    interaction with Rubisco or EPYC1 by yeast two-hybrid assay"].
- Epistasis and recruitment. saga1 is epistatic to mith1, and MITH1 needs SAGA1
  to localize [PMID:39548241 "MITH1 requires SAGA1 for its recruitment to the
  condensate and for its function"].
- Heterologous sufficiency. SAGA1 and MITH1 together, but neither alone, make
  thylakoid sheets traverse an EPYC1-Rubisco condensate in Arabidopsis
  [PMID:39548241 "These results demonstrate that SAGA1 and MITH1 together are
  sufficient to generate matrix-traversing thylakoid membranes in a
  heterologous system."]. The membranes are sheets, not tubules, so other
  factors shape the tubules.
- Model. MITH1 raises the membrane-matrix adhesion that SAGA1 provides
  [PMID:39548241 "We propose that MITH1 increases the membrane–matrix adhesive
  force per unit area by binding to SAGA1"].
- Phenotype severity. mith1 grows less poorly than saga1 at air CO2 and has
  fewer extra condensates. CAH3 is found at pyrenoid-peripheral puncta in
  mith1.

### Expansion microscopy preprint, 2026 (PMID:42465278)
- MITH1 is mostly on the peripheral, cylindrical tubules [PMID:42465278 "MITH1
  signal was largely restricted to the cylindrical tubules at the pyrenoid
  periphery"].
- The MITH1 C terminus is distal to the membrane, consistent with an extended
  coiled coil reaching into the matrix [PMID:42465278 "our results suggest that
  the antibody epitope-containing C-terminus of MITH1 is localized distally
  from the tubule membrane"].
- SAGA1 lies more peripheral than MITH1, which fits SAGA1 initiating the
  tubules and MITH1 extending them.
- MITH1 relocalizes with CO2 level [PMID:42465278 "MITH1 was uniformly
  distributed throughout the tubule network at high CO2 and became increasingly
  peripheral during the transition to low CO2."].
- The authors cite their own unpublished or preprint structural work (ref. 40)
  for MITH1 binding membranes and Rubisco [PMID:42465278 "We recently showed
  that MITH1 can bind both membranes and Rubisco"]. That work is not in PubMed
  (esearch "MITH1 AND pyrenoid" returns only 39548241, 39211136 and 42465278),
  so it could not be checked. It also conflicts with the negative yeast
  two-hybrid result.

### Other cached papers
- Meyer et al. 2020 (PMID:33177094) defines the Rubisco-binding motif. MITH1
  is not discussed, and Hennacy cites it for MITH1 lacking the motif.
- Crans et al. 2026 (PMID:42090253), on SAGA1/SAGA2 and the starch sheath,
  does not discuss MITH1. Not cited in the review.

## Decisions

1. **Location, GO:0160223 pyrenoid tubule (NEW, IDA).** Strongly supported by a
   functional fusion, membrane fractionation and antibody-based expansion
   microscopy. No separate GO:1990732 pyrenoid row, because the tubule term is
   part_of pyrenoid.
2. **Process, GO:0010027 thylakoid membrane organization (NEW, IMP).**
   - Participation test. MITH1 is physically on the membranes being
     reorganised, binds SAGA1, and is proposed to supply part of the adhesive
     force that moves the membrane into the matrix. That is a structural
     contribution to the step, not substrate-like necessity.
   - The evidence is complemented loss of function plus heterologous
     sufficiency with SAGA1.
   - Comparator check. VIPP1 and FZL (Arabidopsis thylakoid shapers) carry
     GO:0010027, and SAGA1 was given the same term in its sibling review.
   - There is no "pyrenoid tubule assembly" term. Requesting one is raised as a
     suggested question and an ontology gap.
3. **Molecular function, GO:0043495 protein-membrane adaptor activity (core
   function only, tentative).** The term matches the SAGA1 annoton. MITH1
   associates with membranes and binds SAGA1 (a Rubisco binder), bridging SAGA1
   and the matrix to the membrane surface.
   - Caveats: there is no membrane-binding domain, lipid binding has not been
     measured, and direct Rubisco binding is disputed.
   - It is not added as a NEW existing-annotation row, because no direct assay
     of the activity exists. The validator warns about this, and the warning is
     accepted.
   - "Protein binding" was avoided.
4. **Not proposed:**
   - Starch binding: MITH1 has no CBM20.
   - Rubisco binding: the yeast two-hybrid result is negative, and the only
     positive report is an uncached, unverifiable citation.
   - Any CCM or CO2-response process term: the low-CO2 growth defect is a
     downstream consequence of missing tubules.

## Proposed module annoton (for modules/pyrenoid_ccm.yaml, node tubule_matrix_tethering)

- id: mith1_tubule_extension
- participant: UniProtKB:A0A2K3DMK6 (Chlamydomonas MITH1 / SAGA3, Cre06.g259100)
- function: GO:0043495 protein-membrane adaptor activity (tentative)
- process: GO:0010027 thylakoid membrane organization
- location: GO:0160223 pyrenoid tubule
- role: recruited by SAGA1, and needed to extend the tubules through the matrix
  after SAGA1 has started them.
