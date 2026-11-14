# NA1000 PtsP–HPr–PtsN manual review

All three reviews are COMPLETE after reviewing all 15 seeded rows. No source row was added, removed, reordered, requalified, or retired; there are zero historical or newly proposed NEW rows. This completion is the individual review status, not a claim that every biological uncertainty has been resolved.

| Target | Core synthesis | Original-row adjudication |
|---|---|---|
| A0A0H3C823 / ptsP / CCNA_00892 | GO:0008965 PEP-dependent protein phosphotransfer | Cytoplasm and donor-specific chemistry ACCEPT; generic phosphotransferase MODIFY to GO:0008965; sugar-uptake process MAOA |
| A0A0H3C344 / ptsH / CCNA_00241 | GO:0016775 nitrogenous-acceptor phosphotransfer | Cytoplasm ACCEPT as mechanistic inference; kinase MODIFY laterally and transferase MODIFY by descendant refinement to GO:0016775; sugar/mannose transport MAOA |
| A0A0H3CDT8 / ptsN / CCNA_03710 | GO:0004857 enzyme inhibition, specifically SpoT hydrolase control | Sugar/mannose-specific claims MAOA; kinase activation UNDECIDED, not a claimed loss |

MAOA means MARK_AS_OVER_ANNOTATED. It evaluates substrate/process overreach of these electronic mappings; it does not assert that every possible secondary carbohydrate activity has been disproven. All source qualifiers remain verbatim.

## Primary evidence and limits

Read full canonical PMID27109061 (Ronneau et al., 2016) and PMID26489861 (Sanselicio and Viollier, 2015). Both explicitly use NA1000-derived Caulobacter strains. The 2016 paper identifies the three CCNA loci. Frozen UniProt identity/signature records independently connect those loci to the three accessions. No CB15 protein is substituted for an unavailable NA1000 reference-tree leaf.

- **PtsP chemistry:** the 2016 preparation is a fraction containing EI Ntr, not homogeneous purified PtsP. Radiolabeled PEP phosphorylation and its glutamine sensitivity support the catalytic interpretation. L83Q changes glutamine responsiveness; this is not a direct glutamine-binding measurement. The 2015 affinity-purification/MS and GFP-SpoT co-IP results support a PtsP–SpoT cellular complex, not isolated binary binding or an independently demonstrated direct regulatory reaction.
- **HPr chemistry and downstream effects:** native knockout/phosphostate results, the conserved HPr phosphohistidine-site signature, and restoration of PtsN–SpoT association by Caulobacter HPr in an E. coli npr mutant support phosphorelay competence. These are not purified NA1000 HPr-to-PtsN kinetics. HPr-to-SpoT effects remain indirect; the tested two-hybrid constructs did not interact. A PtsN-independent branch remains unresolved.
- **PtsN output:** wild-type and H66E phosphomimetic proteins associate with SpoT in two-hybrid experiments in E. coli. H66E is not an actual phosphorylated histidine. Engineered NA1000 cells separate an introduced RelA synthetase from SpoT hydrolase activity and support PtsN-dependent hydrolase inhibition. These are not purified binary inhibition kinetics. SpoT is not a protein kinase; this measured output cannot be used to accept kinase-activator activity, but it does not refute a different undiscovered kinase target.
- **Compartments:** retained PtsP/HPr cytoplasm is a broad mechanistic inference, not an ARBA quotation or independent resolved fractionation result. Neither is refined to cytosol solely because that word seems more specific.

The complete clauses used in each review are checked verbatim against the canonical publications or appropriate raw UniProt signature section. No provider prose or GOA statement is used as biological evidence.

## Ontology and phylogeny

Official QuickGO definitions/relationships were independently acquired by the coordinating reviewers and read locally in `psepk-review-20261107/go-terms.json`, `go-ancestors.json`, and `npr-phosphotransfer-{term,ancestors,children}.json`. API origin is `https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0016775` (with `/ancestors` and `/children` for the corresponding relationships). These files are hashed as dependencies in the release.

GO:0016775 is a descendant of GO:0016740 and GO:0016772, but not GO:0016301. Thus the kinase replacement is explicitly lateral. A non-ATP donor alone does not disprove the broad kinase definition; ATP-specific protein histidine kinase and hybrid-kinase/response-regulator phosphotransfer terms would assert the wrong specific chemistry. GO:0009401 and the specific sugar-PTS MFs include sugar uptake/coupling, rather than all regulatory PTS phosphotransfer.

Root's dated official tree receipts for PTHR46244/PTHR33705/PTHR47738 contain no leaf for the exact three NA1000 accessions. The PtsN source node PTN002412133 is not the kinase-activation node PTN002021052 in the locally available PAINT slice. A target path cannot be reconstructed from donor names, CB15 substitution, or an unrelated node. Therefore loss/absence of loss is unresolved. No target-loss or family-wide negative is asserted. The global `paint-losses` download was not invoked under the explicit disk/cache constraint; the frozen actual trees and PAINT slices were examined instead. There are no IBA rows in these seeds; the PtsN TreeGrafter row is IEA.

## Research provenance

No genuine gene-specific provider report existed. Root's shared Falcon research attempt failed HTTP403 during provider authentication; see `acquisition-20261107/module-falcon-attempt.json`. Manual notes document this actual shared attempt; no synthetic provider output was created. Root normally acquired PMID26489861 after this consultation baseline. Its canonical full text is additive, not a refresh of an existing source.

## Verification and reuse

`check-results.json` records the actual helper, validation and render commands with exit codes and log paths. All three `just validate` calls (schema, GO terms, references and best practices), all three helper-history validations and all three renders passed sequentially. PtsN has one intentional core-MF coverage warning for GO:0004857; no annotation was manufactured to clear it. The source-labeling backfill added five UniProt record-section fields without changing any claim.

`verify.py` is the reproducible, lightweight preservation and quotation check. It compares complete ordered source payloads (everything except each row's review), lifecycle counts, six raw files, and all 45 publication files present at baseline. It independently checks 48 quotation occurrences. `curate.py` records the initial manual decision application; subsequent independent UniProt signature attachments and normal section backfill are represented by the final files/histories. Do not rerun `run_checks.py` as a passive verification step: it creates new history records.

Environment: existing root `.venv`, `UV_NO_SYNC=1`, `PYTHONSAFEPATH=1`, `PYTHONDONTWRITEBYTECODE=1`, and this worktree's `src` on `PYTHONPATH`. No environment build, member-index build, full validation, commit, or remote publication was performed. Shared module/family/project files were not edited. The release manifest contains owned artifacts separately from read-only source dependencies.
