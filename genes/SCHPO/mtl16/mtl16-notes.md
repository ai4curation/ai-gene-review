# mtl16 (SPAC27D7.08c, O42662) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: Mtl16 is the closest experimentally characterised relative of NEUCR/NCU11362
(A7UX10). Both are in PANTHER PTHR13393:SF0 and under PAINT node PTN000333540
(eukaryotic METTL16). Mtl16 is the experimental donor at that node for GO:0120048 and
GO:0000398. No ProtNLM2 output was consulted.

### Deep research
`just deep-research-falcon SCHPO mtl16 --fallback perplexity-lite` failed. Falcon
returned "Exception: Failed to authenticate", and Perplexity returned HTTP 401
insufficient_quota. No deep-research file was produced, so this review relies on the
cached full-text primary literature (PMID:28525753, PMID:34050143, PMID:37637271,
PMID:40841561) and the UniProt record.

### Experimentally established in S. pombe (use these for transfer)
- **U6 snRNA m6A37 methyltransferase.** In the deletion mutant, m6A37 is completely
  absent by LC-MS [PMID:34050143 "By contrast, m6A37 was completely absent in the U6 snRNA isolated from the mtl16Δ strain"].
  U6 m6A-IP is lost while U2 m6A-IP is unaffected [PMID:28525753 "M6A-IP of U6 snRNA was lost on RNA from two independent ΔDuf890 colonies, but m6A-IP of the U2 snRNA control was unaltered"].
  Recombinant enzyme methylates A37 in vitro with SAM [PMID:34050143 "m6A was efficiently introduced at position 37 of U6 snRNA in the presence of SAM"].
  Kinetics: kcat 0.38 per min and Km(U6) 0.182 uM for the full-length enzyme
  [PMID:40841561].
- **KA-1 domain binds the U6 internal stem-loop.** The KA-1 domain recruits the substrate
  and raises kcat/Km about 50-fold. The MTD alone fails to rescue splicing in vivo
  [PMID:40841561 "the KA-1 domain of spMETTL16 facilitates the m6A modification of spU6 snRNA, thereby promoting the efficient splicing of specific pre-mRNAs in vivo"].
- **Splicing of A4 introns depends on catalytic activity.** The P169A/P170A (NPPF)
  mutant does not rescue [PMID:34050143].
- **Genetics.** Mtl16 is synthetically lethal with dim1-35 and strongly synthetic sick
  with prp31-E1 [PMID:37637271].
- **Location.** Nucleus and cytosol, from the HDA ORFeome screen [PMID:16823372].

### Inferred only (PAINT / sequence), not established in S. pombe
- mRNA m6A methyltransferase activity (IBA from human, mouse and worm donors). No S.
  pombe mRNA target is known, and sam1 is unaffected by the deletion
  [PMID:34050143 "S. pombe sam1 mRNA, an ortholog of MAT2A, is not affected in the mtl16Δ strain"].
- Post-transcriptional regulation of gene expression (IBA). The SAM-feedback circuit is
  vertebrate/nematode biology and was marked as over-annotated here.
- 23S rRNA A1618 methyltransferase (ISO from E. coli RlmF). Removed: the substrate does
  not exist in the compartments where Mtl16 acts, and the PAINT eukaryotic node does not
  carry rRNA methylation.

### Sequence numbering caveat
Ishigami et al. 2021 report that the database start codon lies inside an unannotated
intron, so the real protein is longer at the N-terminus: 398 aa in Ju & Tomita 2025,
385 aa in UniProt. Their residue numbers are therefore offset by +13 relative to UniProt
O42662. I checked this against the UniProt sequence. The NPPF catalytic motif is at
UniProt 155-158, i.e. P169/P170 in the paper's numbering. The KA-1 arginine-rich region
R339/R342/R343 corresponds to UniProt R326/R329/R330. Take account of the offset when
mapping residues from the literature onto UniProt-based alignments, for example to
NCU11362.

### Actions summary
15 GOA rows reviewed. GO:0120048 (x3), GO:0120049 and nucleus (x3) were ACCEPTed. The
splicing rows (IBA and IGI), mRNA m6A MTase (IBA), cytoplasm and cytosol were kept as
non-core. Methyltransferase activity was marked TOO_GENERAL. GO:0010608 was marked as
over-annotated. GO:0052907 was REMOVEd. No NEW terms were added. U6 snRNA binding by the
KA-1 domain is real, but it is substrate binding by the enzyme and is captured by the
core MF.
