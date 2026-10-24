# acnA (P25516, E. coli K-12) curation notes

## Session 2026-10-23

Provider deep research (`just deep-research ...`) could not be run in this session because
provider API credentials were unavailable. No `*-deep-research-*.md` file was created; these
notes are built only from the cached publications and the UniProt record.

Fetched additional abstracts via `just fetch-pmid`: PMID:8000525, PMID:9202458, PMID:9421904
(all abstract-only). Only PMID:12486059 and PMID:18304323 have full text cached.

### Identity and activity

- Monomeric aconitase purified from E. coli and cloned as `acn` [PMID:1838390 "It was shown to
  be a monomeric protein of Mr 95,000 or 97,500 by gel filtration and SDS-PAGE analysis"].
- Kinetics: AcnA "is more stable than AcnB, has a higher affinity for citrate, and operates
  optimally over a wider pH range, consistent with its role as a maintenance or survival enzyme
  during nutritional or oxidative stress" [PMID:10585860].
- [4Fe-4S] cluster by EPR/MCD [PMID:7588761 "Active [4Fe-4S]-containing AcnA can be reduced to
  yield an EPR signal due to a [4Fe-4S]+ cluster"]; 53% identity with mammalian c-aconitase/IRP
  [PMID:7588761 "The amino acid sequence of AcnA has 53% identity with mammalian cytosolic
  aconitase (c-aconitase)"].

### Regulation and physiology

- Two isozymes; acnA mutant retains AcnB activity [PMID:8000525 "This activity was due to an
  analogous unstable enzyme(s) designated aconitase B"]; acnA regulated by CRP, ArcA, Fur, SoxRS
  [PMID:8000525 "the acnA gene belongs to at least four global regulatory networks, crp, arcA,
  fur and soxRS"].
- "AcnA is an aerobic stationary-phase enzyme that is specifically induced by iron and
  redox-stress" [PMID:9421904]; AcnB is the major TCA enzyme [PMID:9202458 "AcnB is the major
  aconitase"].
- acnA partially complements acnB [PMID:9202458 "the lesion is partially complemented by the
  acnA+ gene"].
- Oxidant resistance in vivo: [PMID:12486059 "AcnA is evidently resistant to superoxide in
  vivo."]; resistant to iron chelation [PMID:12486059 "AcnA (in the acnB mutant) was completely
  resistant to this treatment."]; physiological rationale [PMID:12486059 "the induction of AcnA
  during oxidative stress provides a mechanism to circumvent a block in the tricarboxylic acid
  cycle"].
- acn mutants are redox-stress sensitive; AcnA stabilises sodA mRNA [PMID:11932448 "AcnA enhances
  the stability of the sodA transcript"].

### mRNA binding (moonlighting)

- [PMID:10589714 "the AcnA and AcnB apo-proteins each interact with the 3' untranslated regions
  (3'UTRs) of acnA and acnB mRNA at physiologically significant protein concentrations"];
  apo-forms bind >3-fold more tightly than holo-enzymes. Targets are acn 3'UTRs, not canonical
  eukaryotic IREs, hence the IBA for iron-responsive element binding was modified to mRNA 3'-UTR
  binding.

### 2-methylcitrate cycle (GO:0047456 / GO:0019543)

- Brock et al. 2002 (PMID:12473114, abstract-only) attribute the 2-methyl-cis-aconitate
  hydration step to AcnB: "AcnB was purified as 2-methylaconitate hydratase from E. coli cells
  grown on propionate and identified by its N-terminus." The abstract says nothing about AcnA.
- No experimental or curated UniProt statement supports 2-methylisocitrate dehydratase activity
  or propionate catabolism for E. coli AcnA, and GOA carries neither term for P25516. Not added;
  raised as a suggested question/experiment.

### Decisions worth flagging

- GO:0009061 anaerobic respiration (IDA, PMID:12486059) REMOVED: full text shows anaerobic
  cultures/extracts were an assay device to protect clusters, not evidence of a role in anaerobic
  respiration; acnA is anaerobically repressed by ArcA/FNR [PMID:9421904].
- iron ion binding / metal ion binding -> MODIFY to 4 iron, 4 sulfur cluster binding.
- cytoplasm -> cytosol; cellular respiration -> TCA cycle; mRNA binding -> mRNA 3'-UTR binding.
- Considered but did not add a NEW process term for post-transcriptional regulation (AcnB has
  regulation of translation IDA from PMID:10589714, AcnA does not); left as a suggested question.
- A history record was not created in this session (edits restricted to the gene folder).
