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


## 2026-11-07 source and ontology audit

Reviewed all original rows, references and core activity. Original annotation payloads/order and historical NEW actions are preserved; no row was added or retired. See `analysis/module_audits/bacterial_lipoprotein_maturation/ecoli-bacsu-consultation/evidence.md` for the complete source/construct and ontology rationale. All genuine Falcon attempts returned authentication HTTP403; manual synthesis is recorded here without creating provider output. Final PAINT lineage inspection reported no IRD/IKR loss; initial cold-cache download races were retried sequentially and logged. Protected publication/provider/raw files remain unchanged.

Retained the specific diacylglyceryl-transfer chemistry and process participation. Membrane claims use topology and enzyme evidence, not the claim that monoderm cells have only one possible membrane. E. coli sided-presence annotation is distinguished from the old peripheral/aquatic catalytic model.

The new full primary PMID:42126242 compares E. coli Δlgt and ΔlgtΔlpp backgrounds and finds that Lpp load, donor homolog and detectable protein production affect complementation. It does not directly test B. subtilis Lgt as a donor; no native loss of chemistry or universal cross-species interchangeability is inferred.
