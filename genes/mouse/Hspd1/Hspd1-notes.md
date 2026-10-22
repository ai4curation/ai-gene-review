# Hspd1 (mouse, P63038) review notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

No earlier review existed for this gene. This review does not use any ProtNLM2 output.

### Process and data

- `just fetch-gene mouse Hspd1` seeded 177 GOA rows and cached the GOA-cited PMIDs.
- `just deep-research-falcon mouse Hspd1 --fallback perplexity-lite` **failed**: falcon
  returned "Failed to authenticate" and the perplexity-lite fallback returned HTTP 401
  "insufficient_quota". No deep-research file exists. The review uses the cached
  publications, the UniProt record, the PANTHER PTHR45633 PAINT table and a PubMed search
  for mouse genetic studies. The new mouse papers cached with `just fetch-pmid` are
  PMID:20393889, 23466696, 24151936, 31209364, 38588611, 31601784, 27786175, 24084737
  and 34153520.
- The review of the human ortholog (`genes/human/HSPD1`, COMPLETE) was read for the
  biochemical literature on mammalian Hsp60. All of that biochemistry used human or other
  non-mouse mammalian protein.

### Evolutionary grounding

- UniProt places P63038 in PANTHER PTHR45633 ("60 KDA HEAT SHOCK PROTEIN, MITOCHONDRIAL").
  It has the Cpn60/GroEL signatures (IPR001844, IPR018370) and the 1–26 mitochondrial
  transit peptide. The transit peptide was confirmed in mouse by N-terminal sequencing
  (FT TRANSIT, ECO:0000269 PubMed:7523108).
- PAINT nodes in `interpro/panther/PTHR45633/PTHR45633-paint.tsv`:
  - PTN000143677 (the whole family, GroEL through Hsp60): GO:0006457 protein folding,
    seeded by E. coli GroEL, M. tuberculosis Cpn60s, yeast HSP60 and human HSPD1.
  - PTN000143509 (mitochondrial Hsp60 clade): matrix, inner membrane, GO:0051087
    protein-folding chaperone binding (Hsp10) and GO:0007005 mitochondrion organization.
    GOA has no mouse IBA row for GO:0007005, and none was added.
  - PTN000143510 (Opisthokonta, taxon:33154): GO:0034514 mitochondrial UPR (worm hsp-60
    seed) and GO:0045041 protein import into mitochondrial IMS (yeast HSP60 seed only).
  - PTN000888030: GO:0008637 apoptotic mitochondrial changes (rat Hspd1 seed only).
  - PTN002900230 (Euteleostomi, taxon:117571): the immune terms IFN-alpha, IFN-gamma,
    IL-6, T cell activation and positive regulation of T cell activation. Mouse Hspd1
    (MGI:96242) is a seed for every one of these except IL-6. IL-6 is seeded by rat and
    human.
  - PAINT put GO:0005524 ATP binding, GO:0009408 response to heat and GO:1990220
    GroEL-GroES complex at the bacterial node PTN000143644 only. None of the three was
    propagated to the mitochondrial clade. I treat that as a deliberate decision and
    added no NEW rows for them.
- Mouse Hspd1 and human HSPD1 are one-to-one orthologs in the same mitochondrial Hsp60
  node, so the chaperonin core mechanism transfers. The extra-mitochondrial "moonlighting"
  claims come from human tumour-cell lines or from rat. For mouse they are inferences
  (ISO/IEA), not mouse experiments, and the review records them as such.

### What is experimentally established in mouse

1. **Essential mitochondrial chaperonin needed for folding of matrix proteins in vivo.**
   - Homozygous gene-trap null embryos die at E6.5–7.5. Heterozygotes are viable, and
     Hspe1/Hsp10 is co-regulated with Hspd1 [PMID:20393889 "Homozygous Hspd1 mutant
     embryos, however, died shortly after implantation"].
   - Adult cardiomyocyte deletion: proteomics identifies proteins "that rely on HSP60
     (HSP60-dependent) for correctly folding in mitochondria". Import of SIRT3 and NDUFA9
     is normal, but the imported protein is degraded faster [PMID:31209364]. So the
     mouse protein acts after import, as a folding and stability factor, not in import.
   - Hspd1+/- mice develop a late-onset motor deficit with a defect in complex III
     assembly [PMID:23466696]. Hsp60 interacts with MnSOD, which needs it to fold
     [PMID:24151936 "we propose that MnSOD is a substrate of the Hsp60 folding
     machinery"].
   - Tissue-specific deletions in intestinal epithelium (MT-UPR activation, loss of
     stemness; PMID:27786175), embryonic heart (PMID:38588611) and Tie2 lineage
     (yolk-sac erythropoiesis; PMID:31601784), plus the Hsp60+/- metabolic phenotypes
     (PMID:24084737, 34153520), are downstream organismal consequences of losing
     mitochondrial proteostasis. They are not annotated as process participation.
2. **Mitochondrial localisation.** Many IDA and HDA rows from mouse liver, islet, testis
   and skin. The transit peptide was confirmed by protein sequencing. The matrix is the
   specific compartment; GOA's matrix rows are by similarity (ISS/ISO/IBA).
3. **Extracellular immunomodulation by exogenous Hsp60** (Osterloh/Breloer, PMID:15371451,
   17164250, 18256040). Recombinant murine and human Hsp60 expressed in eukaryotic cells,
   or low-endotoxin preparations, bind macrophages and DC (not T or B cells). They bind
   LPS and colocalise with CD14. They enhance antigen-specific T-cell IFN-gamma via
   APC-derived IFN-alpha (IFNAR-dependent, IGI with Ifnar1). This LPS-free effect is
   independent of TLR4 and MyD88. LPS-free Hsp60 does **not** induce IL-6, IL-12 or TNF
   in APC, and TNF induction by recombinant Hsp60 is lost on endotoxin removal. These
   are real, mouse-tested properties of the protein as an exogenous ligand, but they rest
   on added protein in culture. The physiological role of endogenous extracellular Hsp60
   is not established.
4. Surface Hsp60 on capacitated sperm heads (PMID:15252132). Immunoreactivity in
   beta-cell secretory granules (PMID:1516759, 8824711; the second paper reports a
   *family* of cross-reactive proteins of different sizes, so these may not all be
   Hspd1). Hsp60-marked mitochondria in migrasomes (PMID:34048705).
5. Mouse Hsp60, like human Hsp60, does **not** compete with M. tuberculosis Cpn60.2 for
   CD43-dependent macrophage binding (PMID:20633027; NOT adhesion of symbiont to host).

### Inferred in mouse (not tested in mouse)

- The ATP-dependent folding cycle, refolding activity and Hsp10 binding come from human or
  other mammalian recombinant chaperonin (PMID:1346131, 11422376, 11050098, 32317635).
  The ortholog relationship and PAINT clade support the transfer.
- p53 binding, procaspase-3 activation, survivin stabilisation, HDL and apoA-I binding,
  Listeria LAP binding and Parkin binding all come from human cell systems. In mouse
  they are kept as non-core ISO/IEA inferences.
- The rat-derived "response to X" rows (hypoxia, ischemia, cocaine, estrogen, resveratrol
  and others) are IEP expression changes in rat, projected by Ensembl Compara. They are
  not functional participation and are marked as over-annotations.

### Decisions worth flagging

- IL-6, IL-12, IL-10 and macrophage-activation and TNF rows are marked over-annotated.
  The mouse data (PMID:18256040, 15371451) show that LPS-free Hsp60 does not induce these
  cytokines, so the effect is attributable to bound LPS. The IL-6 IBA is not REMOVED:
  the PAINT node is seeded by rat and human, and the mouse data argue only against the
  LPS-free effect.
- The MyD88-dependent TLR signalling rows are REMOVED. Mouse data show that the LPS-free
  Hsp60 effect is TLR4- and MyD88-independent, and an exogenous ligand carrier is not a
  pathway component.
- GO:0045041 protein import into the IMS (IBA from yeast only) is UNDECIDED. Mouse import
  assays (PMID:31209364) show that matrix import is normal without Hsp60, which argues
  against a general import role in mammals, but no mouse experiment tested IMS sorting.
