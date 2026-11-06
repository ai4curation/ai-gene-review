# opuCB evidence notes

2026-11-06. Annotation-reviewer and core-function-synthesizer consultation.

Identity: O34878, Bacillus subtilis subsp. subtilis str. 168; verified against the normal fetched UniProt record. The pristine seed and all non-review fields/raw hashes are frozen in `.cache/module-audit-logs/choline-sulfate-20261106/bacillus-baseline.json`. No source row was removed. Default Falcon attempt failed HTTP403; the genuine failure is logged, and these are manual notes, not a provider report.

Integral membrane translocation subunit of OpuC. PMID10216873 establishes four gene-product types; the accepted importer architecture contains two OpuCA copies plus OpuCB, OpuCC and OpuCD. ATP coupling, membrane translocation and substrate capture are distinct contributions. The whole-complex glycine-betaine/choline activities are not autonomous activities of an isolated subunit.

PMID9925583 (author-hosted full text: https://www.uni-marburg.de/de/fb17/fachgebiete/mikrobiologie/ag-bremer/pdf-fuer-publikationen/057.pdf) identifies JH642 as a derivative of strain168 and parent of the RMKB mutants. Radiolabeled choline-O-sulfate uptake, competition and NMR accumulation establish the route. COS accumulates intact and does not serve as sole carbon, nitrogen or sulfur source under the tested conditions. No sulfatase, sulfate release, sulfur assimilation, or COS-dependent glycine-betaine biosynthesis is assigned. Complex uptake is positive biochemical evidence, beyond knockout necessity.

PMID10216873 (author full text: https://www.uni-marburg.de/de/fb17/fachgebiete/mikrobiologie/ag-bremer/pdf-fuer-publikationen/058.pdf) compares the cloned JH642 proteins with the genome-project sequences: identical except two adjacent OpuCC substitutions. Preserve this comparison as a strain/sequence boundary, not a proven current gene-model error. OpuCC lipid labeling and globomycin-sensitive processing were tested; ATPase and permease roles were assigned from conserved architecture. OpuB is not a glycine-betaine transporter despite its close similarity: OpuC substrate scope is grounded in direct uptake, not family naming.

Specific existing transport terms are retained or refined; new complex MF proposals explicitly use contributes_to. The generic transmembrane-process rows are refined to glycine-betaine/choline/carnitine transport. COS is distinct from all three and from sulfate transport. No COS-specific GO term was found; the gap is explicit rather than a fabricated identifier. No new process row is manufactured from loss-of-function alone.

Completion: explicit complex-membership proposals are added where absent; OpuCC already carries a broader complex term and is refined in place. Machine GOA fields and raw files remain untouched. All four statuses are COMPLETE.
