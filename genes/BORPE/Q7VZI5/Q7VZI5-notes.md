# Q7VZI5 (BP0922, Bordetella pertussis) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

This re-review does not use the ProtNLM2 prediction files or the ProtNLM-generated
UniProt name ("3-methylitaconate isomerase", ECO:0008006) as evidence.

### Identity

- UniProt Q7VZI5 is an unreviewed TrEMBL entry: 391 aa, PE 3, ordered locus BP0922,
  and the only entry for this locus. It is a full-length family member, not a
  fragment or isoform. Pfam PF04303 and two SSF54506 DapF-like domain halves are
  present, and the catalytic Lys/Cys pair is retained.
- PANTHER places it in PTHR43709 (ACONITATE ISOMERASE-RELATED), subfamily SF2
  ("DUF453 DOMAIN PROTEIN (AFU_ORTHOLOGUE AFUA_6G00360)"). This agrees with the
  family review at `interpro/panther/PTHR43709/PTHR43709-review.yaml`, which also
  scores GO:0050100 as UNRESOLVED.
- GOA has no annotations for Q7VZI5. The only GO line in UniProt is
  `GO:0016853 IEA:UniProtKB-KW`, which is not in the GOA file.

### Evolutionary evidence

See `Q7VZI5-bioinformatics/RESULTS.md` (script `compare_prpf_family.py`).

- The PrpF clade (TIGR02334) consists of Shewanella PrpF Q8EJW4, Cupriavidus PrpF
  Q937N7 and B. pertussis BP2370 (Q7VW94). These are 78-80% identical to each other.
  Q7VZI5 is about 36% identical to each and lacks TIGR02334.
- Q7VZI5 is 35-45% identical to every other characterised member: Mii Q0QLE6 at
  43.7%, Adi1 at 35.5%, YraM at 39.2%, and the SF3 proteins YbhH, LigU and GalD at
  39-45%. None of these is a clear nearest characterised relative.
- The PAINT file for PTHR43709 has one IBD, GO:0016863 at PTN002017920, seeded by
  Q8EJW4. Q7VZI5 has not received the matching IBA, which suggests it is outside
  that node. I treat this as a deliberate scoping of the PAINT node.
- Mapping the Shewanella PrpF active site onto Q7VZI5 gives K73->K65, C107->C99,
  K281->R266 and H317->H301.
- Genomic context: B. pertussis has a complete prp cluster, BP2368 prpC, BP2369
  AcnD-type aconitase, BP2370 PrpF and BP2371 prpD. BP0922 sits elsewhere, beside
  BP0918 (MmgE/PrpD family), BP0919 (succinate-semialdehyde dehydrogenase), BP0920
  (exported FAD-binding protein), BP0921 ("citrate utilization protein B"), BP0923,
  BP0924 (regulator) and BP0925 (FAH-family hydrolase).

### Changes to the review

The earlier draft proposed three NEW rows, none of them in GOA. They were rebuilt
from the earlier ProtNLM-era deep research.

1. **GO:0050100 methylitaconate delta-isomerase activity (NEW): withdrawn.** It
   rested on the ProtNLM name and the claim that PrpF-family proteins are
   methylitaconate isomerases. Only Mii is one, and Q7VZI5 is no closer to Mii than
   to the SF3 tautomerases. Mii works in anaerobic nicotinate fermentation in
   Eubacterium barkeri. The validator does not allow a non-GOA row to carry any
   action other than NEW, so the row was deleted rather than set to UNDECIDED. Its
   rationale is recorded here instead. The activity is unresolved, not refuted.
2. **GO:0019543 propionate catabolic process (NEW): withdrawn.** The
   methylcitrate-cycle isomerase role belongs to the paralog BP2370
   [PMID:17567742 "Bacteria that use AcnD also require the function of the PrpF
   protein"]. BP0922 is not in the prp cluster. Proposing the term would be a
   paralog over-annotation.
3. **GO:0005737 cytoplasm (NEW): kept.** I now support it with a hydropathy screen
   (no signal peptide or TM segment) rather than with deep-research prose.
4. **GO:0016853 isomerase activity (NEW): added.** This activity is shared by
   every characterised member of the family, and Q7VZI5 retains the catalytic
   residues [PMID:17567742 "Results from in vitro studies show that PrpF isomerizes
   trans -aconitate to cis -aconitate."]. A narrower class is not warranted,
   because the family spans C=C delta-isomerases (5.3.3.x) and a keto-enol
   tautomerase (GalD, 5.3.2.x).

I rewrote the description and core_functions to be family-level and
substrate-agnostic. The falcon deep-research file is rated LOW_QUALITY: it
mis-describes the reaction and cites an irrelevant 2023 Foods paper on herbal
extracts.

### Relative to review next

There is no close characterised relative. PANTHER SF2 is heterogeneous, and
pairwise identity does not resolve the placement. The best-characterised SF2
member, and the only PAINT seed in the family, is Shewanella oneidensis PrpF
(Q8EJW4, prpF; PMID:17567742, PMID:29145506). The repo has no review for it. The
repo reviews of PSEPK prpF (Q88KF3) and PSEPK galD cover the PrpF clade and the SF3
tautomerase. E. barkeri Mii (Q0QLE6) is the alternative relative if a tree places
BP0922 with it.

### Modules

`modules/methylcitrate_cycle.yaml` models the AcnD/PrpF route with PSEPK PrpF.
BP0922 should **not** be added there. The B. pertussis member of that route is
BP2370.
