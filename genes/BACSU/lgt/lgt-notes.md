# lgt (Bacillus subtilis 168, O34752) curation notes

Added as the monoderm exemplar of the Lgt step in `modules/bacterial_lipoprotein_maturation.yaml`.

- Provider deep research could not run: `just deep-research-falcon BACSU lgt` failed with a 403 authentication error
  (2026-11-02), the only configured provider key, and no MOD description provider exists for BACSU. The review relies on the
  UniProt record and the two cached primary papers below. Both are abstract-only in the cache.
- lgt inactivation abolishes lipid modification and signal peptide cleavage but is not lethal
  [PMID:10096076 "Inactivation of Igt in B. subtilis by a nonsense mutation (prs-11 mutation) or by disruption was shown here to abolish lipomodification of prelipoproteins completely"].
- Non-lipidated precursors are still translocated but partly released, lowering cell-bound PrsA and impairing secretion
  [PMID:10096076 "there was release of both precursors from cells"].
- gerF germination mutations map to lgt [PMID:9846746 "All known gerF mutations affecting Bacillus subtilis spore germination have been mapped"].
  This is a downstream consequence of losing lipoprotein maturation (germinant-receptor C subunits are lipoproteins), so no
  germination process term is proposed: Lgt is necessary for, but does not do the work of, germination.
- All six GOA rows (IBA from PTN000778741 and IEA) are accepted; the monoderm genetics supports the PAINT root placement.
- 2026-11-02 retry: `just deep-research BACSU lgt --provider perplexity` failed with "Provider 'perplexity' not available.
  Available: falcon, openscientist, claude_code" (no Perplexity key in this environment). No provider-named deep-research
  file exists for this gene.
