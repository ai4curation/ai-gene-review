# lgt notes

## 2026-10-02

`just deep-research-falcon ECOLI lgt` could not run in this Orca environment because
`agentapi` was not available on `PATH` and no provider API keys were configured, so
this review uses the cached primary literature from `just fetch-gene` plus the
fetched UniProtKB record.

Manual synthesis:

- Lgt is an inner-membrane phosphatidylglycerol--prolipoprotein
  diacylglyceryl transferase. Mao et al. directly solved E. coli Lgt structures
  and report that "Phosphatidylglycerol:prolipoprotein diacylglyceryl
  transferase (Lgt) is an integral membrane enzyme that catalyses the first
  reaction of the three-step post-translational lipid modification"
  [PMID:26729647].
- The chemistry is the first committed lipidation step in bacterial
  lipoprotein maturation: Lgt transfers the diacylglyceryl group from
  phosphatidylglycerol to the conserved lipobox cysteine. Sankaran and Wu
  established that "lipid modification of prolipoprotein involves the transfer
  of diacylglyceryl moiety from phosphatidylglycerol to the sulfhydryl group
  of the cysteine residue with the concomitant formation of sn-glycerol
  1-phosphate" [PMID:8051048].
- The 2008 cytosolic-side annotation should not be treated as a separate core
  compartment. Selvan and Sankaran reported extraction behavior consistent with
  cytosolic-side association [PMID:18602442], but later topology and structural
  work place Lgt as a seven-transmembrane inner-membrane enzyme with a
  membrane/periplasmic catalytic cavity [PMID:22287519; PMID:26729647].


## 2026-11-07 source and ontology audit

Reviewed all original rows, references and core activity. Original annotation payloads/order and historical NEW actions are preserved; no row was added or retired. See `analysis/module_audits/bacterial_lipoprotein_maturation/ecoli-bacsu-consultation/evidence.md` for the complete source/construct and ontology rationale. All genuine Falcon attempts returned authentication HTTP403; manual synthesis is recorded here without creating provider output. Final PAINT lineage inspection reported no IRD/IKR loss; initial cold-cache download races were retried sequentially and logged. Protected publication/provider/raw files remain unchanged.

Retained the specific diacylglyceryl-transfer chemistry and process participation. Membrane claims use topology and enzyme evidence, not the claim that monoderm cells have only one possible membrane. E. coli sided-presence annotation is distinguished from the old peripheral/aquatic catalytic model.

The new full primary PMID:42126242 compares E. coli Δlgt and ΔlgtΔlpp backgrounds and finds that Lpp load, donor homolog and detectable protein production affect complementation. It does not directly test B. subtilis Lgt as a donor; no native loss of chemistry or universal cross-species interchangeability is inferred.
