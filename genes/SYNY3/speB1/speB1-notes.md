# speB1 (sll0228, P72703) — Synechocystis sp. PCC 6803 — review notes

## Session 2026-10-19

### Deep research
`just deep-research SYNY3 speB1 --provider falcon` was attempted once and failed
(recipe exit code 1; falcon/Edison is currently failing with an auth error for all
users). Per instructions it was not retried and no `-deep-research-*.md` file was
created. The review is grounded in the UniProt record, GOA, and primary literature
cached in `publications/`.

### Identity
- 306 aa, arginase/ureohydrolase family (Pfam PF00491, PROSITE PS01053/PS51409,
  NCBIfam TIGR01230 "agmatinase", PANTHER PTHR11358:SF26). UniProt name
  N(1)-aminopropylagmatine ureohydrolase (APAUH), EC 3.5.3.24 (ECO:0000269 from
  PMID:37878710).
- RefSeq WP_010871340.1, identical to P72703; named by BlastRule NBR017633.

### Function: APA ureohydrolase in the CAPA spermidine pathway (Xi et al. 2023)
- Pathway: agmatine + aspartate semialdehyde -> carboxyaminopropylagmatine (CAPA,
  by CAPADH Slr0049) -> APA (by CAPADC Sll0873) -> spermidine + urea (by APAUH
  Sll0228) [PMID:37878710 "a CAPA dehydrogenase (CAPADH) that catalyzes the
  reductive condensation of agmatine and ASA into CAPA, a CAPA decarboxylase
  (CAPADC) that decarboxylates CAPA to form APA, and an APA ureohydrolase (APAUH)
  that converts APA to spermidine"].
- Genetics: deletion of sll0228 causes APA accumulation and spermidine loss; rescued
  by complementation [PMID:37878710 "a 200-fold increase in the APA level was
  observed in the sll0228-knockout mutant compared to the wild type"];
  [PMID:37878710 "Complementation of the individual gene-deletion mutants by
  expressing the respective genes fully restored the spermidine biosynthesis"].
- Biochemistry with purified protein: APA -> spermidine + urea [PMID:37878710
  "Incubation of the purified Sll0228 with APA resulted in the formation of
  spermidine"]; [PMID:37878710 "Complete conversion of APA to spermidine and urea
  was achieved after 1 hour of incubation of the reaction mixture"].
- Kinetics kcat 70.8 s-1, Km 1.78 mM for APA [PMID:37878710 "Kinetic
  characterization of Synechocystis APAUH toward APA shows a kcat of 70.8"].
- Manganese: [PMID:37878710 "the purified APAUH contains 1.34 Mn2+ per subunit"].
  Mn ligands predicted from PROSITE ProRule PRU00742 (H121, D145, H147, D149, D228,
  D230 in UniProt FT lines).
- Mutagenesis: E60 (from neighbouring subunit) and R151 are APAUH-specific residues
  that interact with the diaminopropane moiety; E60A/Q, R151A/N retain only 1-6%
  activity [PMID:37878710 "E60 and R151 are only conserved in the APAUH orthologs"].
  The intersubunit E60 contact implies an oligomer, but no complex term is
  warranted from this alone.

### Key question: agmatinase activity?
- **Direct biochemistry says no.** [PMID:37878710 "Putrescine was not detectable in
  the assay mixture containing the APAUH and agmatine"]; [PMID:37878710 "The APAUH
  is highly specific to APA and incapable of releasing measurable urea from CAPA,
  agmatine, arginine, guanidine, guanidinobutyrate, and guanidinopropionate"].
- **Phylogeny says it is a distinct subfamily.** [PMID:37878710 "Phylogenetic
  analysis revealed that APAUH and its orthologs are clustered as a separate group
  from arginase and agmatine ureohydrolase and form a distinct clade within the
  ureohydrolase superfamily"].
- **Precedent from thermophiles.** The T. thermophilus SpeB homologue hydrolyzes APA
  but not agmatine [PMID:15983049 "the enzyme hydrolyzes N1-aminopropylagmatine to
  spermidine but does not act on agmatine"]. In T. kodakarensis spermidine is made
  mainly via APA [PMID:20675472 "In T. kodakarensis, spermidine is produced mainly
  from agmatine via N1-aminopropylagmatine"].
- **Conflicting older evidence.** Quintero et al. 2000 measured a very low
  "agmatinase" activity in crude extracts (about 0.28 nmol/min/mg protein) that was
  absent from the sll0228 insertion mutant and concluded that sll0228 encodes an
  agmatinase [PMID:10648527 "Strain CSMJ3, however, lacked any agmatinase activity,
  while strain CSMJ4 showed about 69% of the agmatinase activity found in the wild
  type"]; [PMID:10648527 "ORF sll0228 clearly encodes an agmatinase and, therefore,
  represents an speB gene"]. This was an extract assay, before APA/CAPA were known
  to exist in Synechocystis; it did not show that the purified protein acts on
  agmatine. The 2023 purified-enzyme data supersede the 2000 inference. The
  residual extract activity may reflect an indirect route or a minor activity below
  the 2023 detection limit; this is noted as an open question rather than resolved.
  Quintero et al. also showed sll0228 is not the arginase [PMID:10648527 "exhibited
  arginase activities, as determined in cell extracts, identical to that found in
  the wild-type strain"].
- **Paralog sll1077 is not an agmatinase either.** The other Synechocystis
  arginase-family paralog, once annotated agmatinase, is a guanidinase
  [PMID:34446715 "We posit that Sll1077 is more likely a guanidinase because it
  degrades guanidine rather than agmatine into urea and ammonium"]. So the
  "agmatinase" label in Synechocystis has been wrong for both paralogs.
- **Conclusion:** GO:0008783 agmatinase activity (and TIGR01230's EC 3.5.3.11) is a
  paralog-type over-annotation for this enzyme. The IBA row (PTN000144486, seeded by
  E. coli SpeB, Arabidopsis ARGAH1/2 and others) places agmatinase at a node that
  includes the APAUH clade, but the target itself has direct evidence of no activity
  on agmatine, i.e. functional divergence within the clade.

### Putrescine
- The CAPA route bypasses putrescine [PMID:37878710 "The CAPA pathway does not
  involve putrescine and uses ASA rather than decarboxylated AdoMet as the
  aminopropyl group donor"]. APAUH produces no putrescine from agmatine (above). So
  GO:0009446 putrescine biosynthetic process (IBA) is unsupported for speB1.

### Context
- Synechocystis argininolysis uses arginase pathway; the arginase is not sll0228
  [PMID:10648527].
- Thermus TtARG arginase does have agmatinase activity [PMID:37001547], showing that
  substrate range differs among family members and cannot be read from family
  membership.
- Bacterial CAPADH homologs elsewhere prefer agmatine [PMID:42754158].

### PGAP
- WP_010871340.1: name "N(1)-aminopropylagmatine ureohydrolase", EC 3.5.3.24,
  BlastRule NBR017633, no GO. Correct; EC matches UniProt's experimentally
  supported EC (likely the rule was built from this very protein: CNN).
- Genome record NC_000911.1 (annotation GCF_000009725.1-RS_2026_01_07) carries, on the
  sll0228 CDS (locus_tag SGL_RS02550, gene "speB"), EC 3.5.3.24 and the product name
  above, plus GO:0008783 agmatinase activity and GO:0008295 spermidine biosynthetic
  process (both IEA) [file:SYNY3/speB1/speB1-pgap-prediction-evidence/genome_record_CDS_sll0228.txt
  '/GO_function="GO:0008783 - agmatinase activity [Evidence']. The WP_ record has no GO.
  These two terms are exactly the model GO of TIGR01230 (agmatinase equivalog;
  GO:0008295, GO:0008783; EC 3.5.3.11) per `pgap_models.yaml`, which is the most likely
  source; the record shows the GO but not which model supplied it. The CDS is internally
  inconsistent (EC 3.5.3.24 with agmatinase GO). Agmatinase is
  wrong (PLI, paralog over-annotation); spermidine biosynthesis is right by
  coincidence (the TIGR01230 logic assumes agmatine -> putrescine -> spermidine,
  which is not this enzyme's route).
