# A0A8C2TBA7 (quail PAM) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM2 files were consulted.

### Identity
- A0A8C2TBA7 is an unreviewed Ensembl model (846 aa) of quail PAM (chromosome Z). It is one
  of five unreviewed quail PAM models (A0A8C2Y9Y4 970, A0A8C2YA38 952, A0A8C2TDQ8 915,
  A0A8C2TGR3 869 aa). No reviewed quail PAM exists.
- In an alignment with human PAM P19021-1 (973 aa), the quail model lacks all 107 residues of the exon-16 linker
  (P19021 388-494, VSP_001227). That makes it a PAM-2-like splice form [PMID:26667899 "This
  endoprotease-sensitive region is not included in the PAM-2 isoform, and PHM and PAL are rarely
  separated by cleavage."]. The model is not a fragment. The transmembrane and cytosolic
  segments are retained, and all Cu (6), Zn (3) and Ca-site ligands are conserved
  (file:COTJA/A0A8C2TBA7/A0A8C2TBA7-bioinformatics/RESULTS-rereview.md).

### Evolutionary grounding
- PANTHER PTHR10680:SF14 ("PEPTIDYL-GLYCINE ALPHA-AMIDATING MONOOXYGENASE"). The same subfamily
  contains human P19021, rat P14925, mouse P97467, bovine P10731, Xenopus pam-a/pam-b, and the
  fly/worm PHM proteins.
- PAINT: GO:0004504 IBD at PTN000073733 (Deuterostomia), seeded by human, bovine, mouse, rat and
  zebrafish PAM. GO:0005576 IBD at PTN000840899 (Eumetazoa), seeded by fly and rat. No PAINT IBD
  for GO:0004598 or GO:0001519 in the family table, so those rest on the domain and residue
  conservation plus subfamily membership.
- The family review (interpro/panther/PTHR10680/PTHR10680-review.yaml) also places this protein
  in SF14, so there is no disagreement.

### Changes from the previous review
- Correct-but-general terms are now MODIFY with descendant replacements: catalytic activity
  -> GO:0004504 + GO:0004598; monooxygenase activity and GO:0016715 -> GO:0004504; peptide
  metabolic process -> GO:0001519; membrane -> GO:0030667. These rows were previously
  MARK_AS_OVER_ANNOTATED or KEEP_AS_NON_CORE.
- Transport vesicle membrane: MODIFY to secretory granule membrane (a lateral correction; the
  UniProt SubCell line is ARBA-derived).
- Extracellular region: ACCEPT -> KEEP_AS_NON_CORE (secreted soluble PHM/PAL is a secondary
  location). Copper ion binding: ACCEPT -> KEEP_AS_NON_CORE (cofactor binding).
- Quotes of ARBA-derived catalytic-activity, subcellular-location and EC lines were replaced
  with primary literature (PMID:9360928, PMID:19604476, PMID:26667899) and the new
  alignment analysis.
- No NEW annotations. Secretory granule biogenesis and copper-homeostasis roles described for
  mammalian PAM were not added, because they are mammal-specific findings not tested in birds.

### Relative to review next
- Human PAM (P19021): an SF14 member and a seed of the PAINT GO:0004504 node. No review of it
  exists in the repository.
- No modules in modules/ cover peptide amidation.
