# DUSP5 (human, Q16690) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: human DUSP5 is reviewed as the experimentally characterised SF40 relative
of donkey (EQUAS) DUSP5 A0A8C4MED2. No ProtNLM2 output was consulted.

### Deep research

`just deep-research-falcon human DUSP5 --fallback perplexity-lite` failed for both
providers (Edison/falcon: `403 Forbidden` on `/auth/login`; perplexity: `401
insufficient_quota`). No deep-research file exists. The review below rests on
cached publications that I read directly (all abstracts; full text for
PMID:25519881, PMID:39749114, PMID:25489104, PMID:18927432, PMID:36115835).

### Evolutionary placement

- UniProt: PANTHER PTHR10159:SF40 "DUAL SPECIFICITY PROTEIN PHOSPHATASE 5"; the
  repo PANTHER member file (interpro/panther/PTHR10159/PTHR10159-entries.csv) lists
  human Q16690 and rat O54838 in SF40.
- Domain architecture: N-terminal rhodanese-like (CH2) domain 19-141 containing the
  KIM/NLS region (NLS motif 53-74), C-terminal DSPc catalytic domain 178-319 with the
  HCXAGXXR signature and catalytic Cys263 [PMID:7961985 "the HCXAGXXR signature
  sequence for PTPs was located at positions 261-268"]. Crystal structure of the
  catalytic domain: PDB 2G6Z [PMID:17078075].
- PAINT nodes behind IBA rows: PTN000017039 (endoderm formation; covers DUSP1/2/4/5
  of human and mouse; sole experimental donor zebrafish dusp4, ZFIN
  ZDB-GENE-040426-709, morpholino IMP from PMID:18719100, checked via QuickGO);
  PTN000806857 (nucleus; nuclear class-I MKPs DUSP1/2/4); PTN001605855 (cytoplasm,
  negative regulation of MAPK cascade; broad MKP clade including cytoplasmic MKPs);
  PTN004128558 (phosphoprotein phosphatase activity, signal transduction; whole DSP
  family).

### Experimentally established in human (or with human protein)

- Dual-specificity phosphatase activity in vitro, highest relative activity toward
  phospho-ERK1 [PMID:7961985 "Among the substrates tested, B23 displayed the highest
  relative activity toward phosphorylated extracellular signal regulated kinase-1"].
- Both phosphates of the ERK activation-loop pT-E-pY tripeptide removed, pTyr
  preferred first [PMID:39749114 "Both phosphates of the pT-E-pY tripeptide are
  dephosphorylated, based on 31P NMR"].
- Recombinant human GST-DUSP5 dephosphorylates pERK in vitro [PMID:25519881].
- ERK2-selective docking via KIM in the N-terminal domain; inactivates ERK2 but not
  JNK or p38; functional NLS; nuclear translocation and sequestration of inactive
  ERK2, also by catalytically inactive mutant [PMID:15713638 "DUSP5 is an inducible
  nuclear ERK-specific MAP kinase phosphatase that functions as both an inactivator
  of and a nuclear anchor for ERK2 in mammalian cells"]. Note: cell work in that
  paper used mammalian cell lines with human DUSP5 constructs.
- Induction depends on ERK1/2 activation; DUSP5 is an ERK substrate (Thr321, Ser346,
  Ser376); stabilised by ERK2 binding [PMID:19666109].
- Secondary anion-binding pocket / E264 regulates catalysis [PMID:27739308].

### Mouse knockout data (orthologue, not this species)

- Dusp5-/- MEFs: increased nuclear phospho-ERK, failure to accumulate nuclear ERK;
  increased HRas-driven papilloma formation [PMID:25489104].
- DUSP5 deletion causes BRAFV600E-induced ERK hyperactivation and senescence; DUSP5
  increases cytoplasmic ERK activity indirectly via relief of ERK-RAF feedback
  [PMID:28053233].

These are consistent with a negative regulator of ERK1/2 signalling and are
transferable within the SF40 subfamily, but disease/phenotype outcomes (skin
carcinogenesis, senescence, T-cell or eosinophil phenotypes) are downstream and not
annotated.

### Not annotated

- Zebrafish dusp5 morpholino angioblast phenotype [PMID:18927432]: morpholino,
  downstream developmental phenotype.
- IBA endoderm formation: inherited only from a zebrafish dusp4 morpholino; DUSP4
  and DUSP5 are different subfamilies within the nuclear MKP clade. Removed.
- PDZ-domain interactions from fragmentomics (PMID:36115835): peptide-level affinity
  screen of the C-terminal motif; no functional consequence for DUSP5 established.

### Actions summary

Core MF: GO:0017017 MAP kinase tyrosine/serine/threonine phosphatase activity
(ERK1/2-selective). Core BP: GO:0070373 negative regulation of ERK1 and ERK2
cascade. Location: nucleus/nucleoplasm. Binding: GO:0051019 MAPK binding (KIM
docking, also needed for nuclear anchoring independent of catalysis).
