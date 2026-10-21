# FTSH12 (A0A1P8ARD2, At1g79560) review notes

## 2026-10-20 full re-review

This re-review is independent of any machine-learning prediction output. The earlier version of
these notes and of `FTSH12-bioinformatics/` read the benchmark sequence from a prediction-source JSON.
The comparison script now reads the sequence only from `FTSH12-uniprot.txt` and the reviewed reference
from `FTSH12-same-gene-reference.json` (UniProt Q9SAJ3).

### Identity of the benchmark accession

- A0A1P8ARD2 (TrEMBL, 991 aa; RefSeq NP_001321597.1, EMBL ANM59220.1) is an **alternative gene model**
  of At1g79560/FTSH12. The reviewed canonical product is Q9SAJ3, which has 1008 aa.
- The two are identical over residues 1–983. Q9SAJ3 then ends `EELLPHKDRVSYQPVDLRAAPLHRS` (25 aa),
  and A0A1P8ARD2 ends `VVYILSSC` (8 aa). This looks like an alternative 3' exon or splice choice
  ([RESULTS.md](FTSH12-bioinformatics/RESULTS.md)).
- Every annotated feature is retained: transit peptide 1–49, TM 154–174 and 427–447, Walker A
  GPPGTGKT (533–540), Walker B VDEID (D591-E592), the second region of homology with both arginine fingers
  (RSGR vs canonical RPGR), and the zinc site H769/E770/H773/D849. No domain or catalytic residue is
  lost. Whether the alternative C-terminal tail is expressed has not been tested.
- The pore-loop region (~556–563, `FASGAEF...`) lacks the aromatic FVG motif of canonical FtsH. This
  matches Kikuchi et al. 2018 [PMID:30309901 "were well conserved in FtsHi1, FtsHi2, FtsHi3, FtsHi4,
  and FtsHi5, but not in FtsH12"].

### Biology (primary literature)

- FTSH12 is a subunit of the 2-MDa Ycf2/FtsHi complex [PMID:30309901 "The inner envelope-localized Ycf2,
  FtsHi1, FtsHi2, FtsHi4, FtsHi5, FtsH12, and pdNAD-MDH proteins therefore form a stable 2-MD complex
  (the Ycf2/FtsHi complex), which interacts with the translocating preproteins."]. This was confirmed
  with native-promoter Myc-FtsH12 pull-downs [PMID:33216923 "In two independent experiments, we were
  able to pull-down FtsH12 together with FtsHi1, FtsHi5, and the plastidic form of MDH from isolated
  chloroplasts"].
- It associates with translocation intermediates in an ATP-dependent way, but only for inner-envelope
  clients [PMID:30309901 "Thus, the transient associations with Ycf2 and FtsHi/FtsH12 proteins are
  specific to preproteins destined to be translocated across the inner envelope membrane."].
- It is located in the inner envelope, with the C-terminal domains facing the stroma [PMID:33216923
  "this unambiguously confirms the localization of FtsH12 in the inner chloroplast envelope"].
- The zinc site is dispensable [PMID:30309901 "Furthermore, even the FtsH12 zinc binding site is
  dispensable for its essential function."]. N-terminomics shows no FTSH12-dependent processing
  [PMID:33216923 "N-terminome analyses further demonstrated normal proteolytic maturation of
  plastid-imported proteins irrespective of FTSH12 abundance."].
- Mielke et al. speculate that FTSH12's ATPase is impaired [PMID:33216923 "FtsH12 contains several amino
  acid exchanges in the Walker B motif and the second region of homology of its AAA-type domain that
  likely impair the ATPase activity function"]. My motif inspection finds the Walker B glutamate and
  both SRH arginines retained, so I do not accept this as evidence against ATPase activity. I still
  use `contributes_to` for the complex-level import ATPase.
- The deep research (falcon) agrees with this picture; its key claims were checked against the papers.

### Evolutionary placement and the relative

- UniProt places FTSH12 in PANTHER **PTHR43655:SF19** (FTSH12, chloroplastic), within PTHR43655
  "ATP-DEPENDENT PROTEASE". In this repo's entries table, SF19 holds only Arabidopsis FTSH12. The other
  PTHR43655 subfamilies are bacterial FtsH and AFG3L2-like (SF2), AFG3L2 (SF9), paraplegin/SPG7 (SF8),
  yeast YTA12 (SF14) and Arabidopsis mitochondrial FTSH3/FTSH10 (SF35, SF2).
- The FtsHi partners (FTSHI1/2/4/5) and the thylakoid FtsH1/2/5 fall in a **different family**,
  PTHR23076 (checked with a UniProt REST query of the PANTHER cross-references).
- Kikuchi et al.'s phylogeny instead places FTSH12 in the cyanobacterium-derived clade with the
  FtsHi proteins [PMID:30309901 "Ycf2, FtsHi1, FtsHi2, FtsHi4, FtsHi5, and FtsH12 are all derived from
  the chloroplast genome-encoded FtsH in the ancestral cyanobacterial endosymbiont"].
- PAINT: canonical Q9SAJ3 gets IBA GO:0004222 (PTN008683692) and IBA GO:0005745 m-AAA complex plus
  GO:0034982 mitochondrial protein processing (PTN000554085, Eukaryota node, human/mouse/fly/yeast m-AAA
  donors). The mitochondrial terms contradict the inner-envelope localization and look like
  over-propagation from SF19 sitting under the eukaryotic m-AAA node. A0A1P8ARD2 itself has no IBA
  rows. This disagreement is raised as a suggested question.
- Closest experimentally characterised relative by PANTHER placement: the m-AAA proteases of the same
  family (different subfamily). I chose human AFG3L2 (Q9Y4W6, SF9), whose review is
  `genes/human/AFG3L2/AFG3L2-ai-review.yaml` with no PENDING rows. **No subfamily-specific m-AAA
  functions** (mitochondrial localisation, m-AAA complex, mitochondrial protein processing) are
  transferred. The only transfer considered is the ancestral FtsH metalloprotease chemistry, which is
  kept as non-core.
- Family review `interpro/panther/PTHR43655/PTHR43655-review.yaml` lists SF19 with FTSH12 and leaves
  metalloendopeptidase and import scope UNRESOLVED. That is consistent with this review. It does not
  discuss the PTN000554085 mitochondrial propagation to SF19.
- Modules: no chloroplast protein-import or Ycf2/FtsHi module exists in `modules/`. The FtsH hits there
  concern bacterial FtsH (LpxC/lambda CII degradation) and do not apply.

### Action changes from the previous version

- Peptidase, metalloendopeptidase and proteolysis rows: MARK_AS_OVER_ANNOTATED changed to
  KEEP_AS_NON_CORE. The HEXXH and D849 zinc ligands are intact and conserved across land plants, so
  the activity is plausible but unproven, and it is dispensable for the essential function.
- Cytoplasm: kept as MODIFY to chloroplast inner membrane.
- ATP binding and ATP hydrolysis: kept as ACCEPT, with the motif analysis added.
- NEW rows (same gene, direct evidence; the canonical Q9SAJ3 carries them): part_of GO:0062091
  Ycf2/FtsHi complex, contributes_to GO:0016464 chloroplast protein-transporting ATPase activity, and
  involved_in GO:0045037 protein import into chloroplast stroma.
- Core function: the MF is now contributes_to GO:0016464 in the GO:0062091 complex; the earlier MF was
  GO:0016887.
- The reference to the prediction-source JSON was removed.
