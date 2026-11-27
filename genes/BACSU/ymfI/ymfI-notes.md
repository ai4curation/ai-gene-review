# ymfI (O31767, BSU16870, B. subtilis 168) notes

## Deep research availability

Provider deep research was **not available** for this gene in this session: no
provider API keys are configured, so `just deep-research` was not attempted, and
`just mod-description-deep-research BACSU ymfI` reports
`ymfI skipped: no MOD provider configured for organism 'BACSU'` (SubtiWiki is
not wired up as a MOD provider here). No `*-deep-research-*.md` file was
written. These notes come from the cached primary publications, the UniProt
entry, PubMed, QuickGO and Rhea.

## Modification and chemistry

- B. subtilis EF-P does not use either known Gram-negative pathway; it carries a
  5-aminopentanol group on Lys32
  [PMID:27002156 "We identified a 5-aminopentanol moiety attached to Lys(32) of B. subtilis EF-P that is required for swarming motility."].
- YmfI catalyses the final step, reducing the EF-P-bound 5-aminopentanone to
  5-aminopentanol
  [PMID:28787546 "We conclude that YmfI is an enzyme that directly catalyzes the reduction of 5-aminopentanone to 5-aminopentanol."],
  acting on the protein-bound substrate
  [PMID:28787546 "We further conclude, based on YmfI’s ability to alter EF-P electrophoretic mobility in vitro, that YmfI alone is capable of catalyzing the reduction reaction when the substrate is ligated to EF-P."].
- Cofactor requirement, from purified protein
  [PMID:28787546 "We conclude that YmfI is an enzyme that requires the NADPH cofactor and is sufficient in vitro to alter EF-P electrophoretic mobility on a semi-native gel."].
- Needs the EF-P acceptor residue
  [PMID:28787546 "We conclude that YmfI requires EF-P lysine residue 32 to promote swarming motility and alter EF-P electrophoretic mobility."]
  and the SDR catalytic tyrosine
  [PMID:28787546 "The ectopic ymfI complementation construct did not restore swarming motility to the ymfI mutant, however, when the ymfI putative active site residue tyrosine 150 was mutated to an alanine"].
  UniProt records ACT_SITE 150 "Proton acceptor" and an NADP(+) binding site at
  residues 8..15 (both ECO:0000250).
- Pathway placement confirmed independently, with ynbB and gsaB upstream
  [PMID:29615499 "We have recently shown that YmfI reduces 5-aminopentanone to 5-aminopentanol in the final step of EF-P modification (24)."];
  [PMID:29615499 "Tandem mass spectrometry analysis of the PTM mutant strains indicated that ynbB, gsaB, and ymfI are required for modification"].
  The 2018 paper also states the modification is assembled directly on EF-P,
  which supports using a peptidyl-lysine modification process term rather than a
  small-molecule biosynthesis term.
- Phenotype logic: the 5-aminopentanone state is actively inhibitory, not merely
  an incomplete product
  [PMID:28787546 "In the absence of YmfI, accumulation of 5-aminopentanonated EF-P is inhibitory to swarming motility."],
  and abolishing modification (EF-P K32R) suppresses the ymfI defect.

## FabG question (the key judgement call)

- YmfI is a classical SDR
  [file:BACSU/ymfI/ymfI-uniprot.txt "Belongs to the short-chain dehydrogenases/reductases (SDR) family."]
  and sits in PANTHER PTHR42879 / PTHR42879:SF2
  "3-OXOACYL-[ACYL-CARRIER-PROTEIN] REDUCTASE FABG" (UniProt DR lines).
- The paper itself frames it as a FabG paralog with a different job
  [PMID:28787546 "Whereas FabG is essential for growth, cells mutated for ymfI exhibited only a 5% decrease in growth rate resembling the slight growth rate reduction found in cells mutated for efp (Fig S2)."].
- B. subtilis has its own dedicated FabG: `fabG`/`ylpF`, BSU15910,
  UniProtKB:P51831, `RecName: Full=3-oxoacyl-[acyl-carrier-protein] reductase
  FabG` (checked against the UniProt flat file, 2026-11-02). So the fatty acid
  role is filled by another gene in this organism.
- NCBIfam has carved out a YmfI-specific family
  [file:BACSU/ymfI/ymfI-uniprot.txt "NCBIfam; NF047420; EF_P_mod_YmfI; 1."].
- No report of 3-oxoacyl-ACP reductase activity for YmfI; no GO:0004316
  annotation in its GOA.
- Therefore the two IBA rows are treated differently, and this matches the
  family review in `interpro/panther/PTHR42879/PTHR42879-review.yaml`:
  - PTN002449287 -> GO:0016616: the node asserts only the shared SDR
    CH-OH/carbonyl + NAD(P) chemistry, which YmfI demonstrably performs on its
    own substrate. **ACCEPT** (propagation_review root_cause NO_FAILURE_CORE).
  - PTN001211919 -> GO:0030497 fatty acid elongation: both seeds (P0AEK2 E. coli
    FabG, P0A2C9 Salmonella FabG) are enterobacterial FabG, the node is placed
    above the YmfI-type clade, and B. subtilis has its own FabG. **REMOVE** as an
    over-propagated electronic inference to a neofunctionalised paralog
    (propagation_review root_cause PROPAGATION_BAD; failure modes
    WRONG_ORTHOLOG_OR_PARALOG, FUNCTIONAL_DIVERGENCE).

## Term choice

- Rhea has no reaction for the EF-P-bound 5-aminopentanone/5-aminopentanol
  interconversion (query "aminopentanol" returns nothing, checked 2026-11-02),
  and GO has no specific MF term for it. GO:0016616 is therefore as precise as
  the ontology allows, so it is kept as the core molecular function rather than
  proposing a new term; the gap is raised in `suggested_questions`.
- Process: GO:0018205 peptidyl-lysine modification (NEW, IDA). The parallel in
  the E. coli pathway is EpmC with GO:0017185 peptidyl-lysine hydroxylation, a
  child of GO:0018205. There is no child term for aminopentanolylation.
- Location: GO:0005737 cytoplasm (NEW, IC) — substrate is a cytoplasmic
  translation factor modified in vivo, and YmfI is a soluble Rossmann-fold SDR
  with no signal peptide or transmembrane feature.
- No ND rows in this GOA, so the ND policy does not apply.

## Verified PMIDs

- 28787546 — Hummels et al. 2017, Mol Microbiol 106:236-251 (full text cached);
  the YmfI paper.
- 27002156 — Rajkovic et al. 2016, **J Biol Chem** 291:10976-10985 (abstract-only
  in cache). Note: the modification paper is in JBC, not mBio; the mBio paper by
  this group is PMID:29615499.
- 29615499 — Witzky et al. 2018, mBio 9:e00306-18 (full text cached).
- PMID:9384377 and PMID:19383706 are the genome sequence references in the
  UniProt entry; they carry no functional information and are not cited in the
  review.
