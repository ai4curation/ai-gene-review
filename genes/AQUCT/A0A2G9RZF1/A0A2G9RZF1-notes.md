# A0A2G9RZF1 (Aquarana catesbeiana) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not consulted. No `*-protnlm-*` file or prediction-evidence
folder was opened.

### Identity (fragment of TLL1)

- UniProt A0A2G9RZF1 is unreviewed, 156 aa, PE 4. Its only annotated feature is a
  CUB domain at 31-147, and it carries a PROSITE-ProRule caution: "Lacks conserved
  residue(s) required for the propagation of feature annotation". ORF
  AB205_0007200 on draft scaffold KV928989.
- New analysis (`A0A2G9RZF1-bioinformatics/RESULTS.md`): residues 30-156 are
  126/127 identical to residues 879-1005 of the complete bullfrog TLL1 RefSeq
  model XP_073462190.1 (1005 aa). The match to bullfrog BMP1 XP_073478370.1 is
  51% identical. Among UniProt reviewed tolloids the identity order is Xenopus
  TLL1 86.6% > human TLL1 78.0% > mouse TLL1 74.0% > BMP1 and TLL2 at 66-68%.
  This is the pattern of a TLL1 ortholog.
- **Conclusion:** A0A2G9RZF1 is a fragmentary gene model covering only the
  C-terminal CUB5 domain of bullfrog TLL1, about 13% of the 1005-aa product. It
  lacks the astacin metalloprotease domain and all catalytic residues, as well
  as the signal peptide, prodomain, CUB1-4 and the EGF domains.
- This settles the previous review's open "BMP-1 or TLL1?" question: it is TLL1.
- No reviewed or canonical UniProt entry exists for bullfrog TLL1. The UniProt
  proteome UP000228934 is still built on the 2017 draft assembly.

### PANTHER / PAINT

- UniProt places the entry in PTHR24251:SF37 "CUB DOMAIN-CONTAINING PROTEIN".
  That subfamily is a heterogeneous bin: its members in the family entries table
  include nas-39, Mfrp, cubilin and the RP43 exoskeleton protein. The placement
  is a fragment artefact. The complete gene belongs in SF45 "METALLOENDOPEPTIDASE",
  which contains human, mouse, chicken and Xenopus TLL1 (O43897, Q62381, Q9DER7,
  Q8JI28).
- `interpro/panther/PTHR24251/PTHR24251-review.yaml` records A0A2G9RZF1 as the
  SF37 representative and calls it a "sponge target". That is wrong: the
  organism is the bullfrog. Its SF37 description also inherits the fragment
  placement. This disagreement is recorded here; the family file was not edited
  (outside this gene folder).
- PAINT: PTN000013301 (family root, Eukaryota) carries IBD GO:0004222
  metalloendopeptidase activity and GO:0005576 extracellular region. The seeds
  include human BMP1 (P13497), Drosophila tolloid and tolkin, mouse Bmp1, and
  worm and zebrafish tolloids. GOA holds no IBA rows for this entry. That is
  consistent with the fragment being excluded from the inheriting clade.

### Literature

- No literature on this bullfrog protein. PMID:29127278 is the draft genome paper.
- TLL1 function (mammalian): PMID:10479448 (abstract) reports that "mTLL-1 is
  shown to specifically process procollagen C-propeptides at the physiologically
  relevant site" and that "BMP-1 and mTLL-1 are shown to cleave Chordin". These
  are activities of the full-length protease, whose catalytic domain this
  fragment lacks.
- CUB domain biology: PMID:21954942. CUB pairs cooperate in PCPE-1 and single
  CUBs lose affinity (PMID:19801683). The older GO:0005201 (via PCPE FunFam)
  hypothesis stays rejected.

### Review decisions

- GOA has no annotations, so there are no existing rows to act on.
- No NEW annotations are proposed for the fragment entry. The fragment cannot
  perform the protease reaction, and BP terms such as chordin or procollagen
  processing would be subfamily-specific transfers to a non-catalytic piece.
- The core function is recorded at gene level: TLL1 has metalloendopeptidase
  activity (GO:0004222) in the extracellular region. It is supported by TLL1
  orthology (99% match to bullfrog TLL1, SF45 orthogroup) and the family-root
  PAINT node. The description states plainly that the fragment itself has none
  of this activity. This replaces the prior placeholder root term GO:0003674.
- Bracket-only `supporting_text` entries from the previous version were
  replaced with verbatim quotes.
- Relative to review next: human TLL1 (O43897), in the same SF45 orthogroup.
  No review of it exists in the repo.
- Modules: no tolloid, chordin-processing or procollagen-processing module in
  `modules/`. `dmel_bmp_signaling.yaml` mentions tolloid in the Drosophila
  context only.
