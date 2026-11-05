# fliC (PA1092, P72151, B-type flagellin) review notes

No deep-research provider was available. Sources: UniProt record (Swiss-Prot), cached PMID:9423837
(full text available in the cache). PubMed MCP searches on 2026-11-05 returned no hits (search service
failing), so later PAO1 fliC literature was not surveyed.

## Function

- UniProt: "Flagellin is the subunit protein which polymerizes to form the filaments of bacterial
  flagella." PAO1 carries the b-type flagellin; flagellin family (Pfam PF00669, PF07196, PF00700).
- PMID:9423837 (Feldman et al. 1998) works in strain PAK, which carries an a-type flagellin. fliC was
  disrupted by gene replacement in PAK and PAK/NP and the mutants were identified as nonmotile
  [PMID:9423837 "Nonmotile mutants of PAK were analyzed to confirm that the expected gene replacement events, in which the interrupted copy of fliC , the gene encoding flagellin protein, introduced into PAK and PAK/NP had replaced the wild-type coding sequence, had occurred."].
  The paper's main data are virulence in neonatal mouse pneumonia, adherence and ganglioside binding.
  PAO1 is used only for adherence assays, not for fliC mutagenesis
  [PMID:9423837 "Fla − mutants of PAK and PAK/NP were isolated by gene replacement."].
- So the PseudoCAP IDA of GO:0071973 to PAO1 FliC rests on a mutant phenotype (loss of motility) of the
  orthologous, antigenically distinct a-type fliC of PAK. The term is correct for flagellin (the
  filament subunit is the propeller), but the evidence code should be IMP and the experiment was on the
  PAK allele.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001250065 | GO:0071973 bacterial-type flagellum-dependent cell motility | 2 | 67 (19 taxa) | GO:0071973, IDA, PMID:9423837 (PseudoCAP) | SOUND | Term is right for a flagellin: PAK fliC disruption mutants are nonmotile (full text). The row is a mutant phenotype in strain PAK (a-type allele), so the code should be IMP; recorded as a CONFIRMED PSEUDOCAP WRONG_EVIDENCE_CODE defect. The node term suits a flagellin clade. | H. pylori FlaA P0A0S1 (IMP GO:0071978 flagellum-dependent swarming motility, PMID:8501031, CACAO; is_a GO:0071973) | Yes; the H. pylori seed carries an experimental descendant term and flagellins are the filament subunit throughout. No GO_CENTRAL defect. |

Consistency with fliD (filament cap, reviewed earlier): flagellum CC row MODIFY to the specific
filament term, extracellular region KEEP_AS_NON_CORE, structural molecule activity core MF.

Defects recorded: PSEUDOCAP 1 (WRONG_EVIDENCE_CODE, CONFIRMED, REPOINT IDA to IMP); GO_CENTRAL 0.
