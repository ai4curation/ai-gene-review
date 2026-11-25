# Existing Mla member consultation

Twelve reviews are COMPLETE: ECOLI mlaA/mlaB/mlaC/mlaD/mlaE/mlaF and PSEPK vacJ/ttg2D/mlaD/mlaE/mlaF/ttg2E. This is an individual-gene evidence audit, not a full-corpus validation or a native-pathway-capacity claim.

## Preserved inputs

`check_preservation.py` compares the ordered non-review payloads against both the root's original `baseline.yaml` and this consultation's `before.yaml`. All 105 rows remain in their original order: 89 machine rows and 16 historical NEW rows. All 16 historical proposals remain active with unchanged source fields, action and lifecycle. There are no added rows, retirements or removals from the document.

The checker verifies 90 protected inputs: 24 raw gene files, 21 genuine provider reports/artifacts (including the separately referenced original module research report), 27 publication caches and 18 raw family entries/metadata/PAINT files. The additional module research source was verified byte-for-byte against the pinned baseline commit before inclusion. No original source was fetched again or edited. Root/family agents own their curated module/family changes, which are excluded from this gene-only preservation boundary.

Existing notes remain exact prefixes; the audit appends dated entries. Twelve new histories were created by `just new-history` and individually validated. `histories.yaml` records their persistent paths.

## Scientific conclusions

- PMID28388411 establishes lipid occupancy and biolayer-interferometry interactions; its complete lipid-handoff narrative is a model. MlaA core support now uses the direct outer-complex-to-MlaC loading experiment in PMID40168124. The inner-complex transfer evidence in PMID34873038 and reconstituted whole-pathway assay in PMID39080293 are kept distinct.
- PMID39080293's figure caption identifies NBD-PE. Its running-text expansion of PE as phosphatidyl glycerol is a source typo, not evidence for an NBD-PG reporter. The cache is unchanged.
- PMID40168124 finds similar PE/PG loading in solution but PG enrichment on cell-derived MlaC. The description and core no longer imply unconditional head-group indifference. The endogenous profiling uses tagged BW25113 MlaC; purified OmpF–MlaA work uses a distinct expression context.
- MlaB's genotoxic-stress survival and complementation in PMID20128927 are real. The two DNA-damage-response rows are UNDECIDED because induced-response participation versus constitutive envelope protection is unresolved. Membrane localization does not disprove the broad term. Antibiotic-response support is retained. MlaB stabilization is qualified by experimental expression conditions and the MlaF-overexpression bypass.
- MlaD genuinely donates phospholipid to MlaC in the purified-protein experiment reported by PMID30284446. The complete GO0120014 definition additionally requires membrane/particle removal, aqueous shielding and delivery to an acceptor membrane/particle. MlaFEDB contribution cores remain; the subunit overannotation reasons now concern this complete activity, not a universal requirement for a complex subunit to act alone or a claim that MlaD only binds lipid.
- The current GO1990531 definition specifically describes a P-type ATPase complex. The existing correction to the ABC transporter complex is retained as a mechanistic correction.
- True broad PSEPK MlaD/E phospholipid-transport rows refine to intermembrane transfer. MlaF nucleotide binding refines to ATP binding instead of being rejected for breadth; broad lipid transport also refines to intermembrane transfer. Its core activity location is the cytoplasmic face of the inner membrane by explicit architecture/ortholog inference.
- Official RCSB and SIFTS records verify PSEPK Ttg2D Q88P91 as the full 215-residue KT2440 sequence in 5UWB, plus LEHHHHHH and selenomethionine substitutions, expressed in E. coli. Lipid occupancy supports the historical binding proposal. The deposited PEF model and the article's cardiolipin-like-density interpretation do not establish exact native cargo identity or stoichiometry. Unmodeled ligand in the original 4FCZ is not proof of an experimentally delipidated apo state.
- No native KT2440 flux, antibiotic export, quantitative cargo stoichiometry, or specific porin compatibility is inferred from E. coli or PAO1 experiments. The process-only Ttg2E core remains deliberately conservative; a generic STAS fold alone is insufficient to establish the role.

`preservation.json` contains a row-specific ledger of every adjudication and the six action changes. `decisions.yaml` summarizes the edited claims; `evidence.md`, the official API snapshots, and `api-provenance.yaml` document source scope and identity.

## Validation and limitations

All twelve focused `just validate` checks, all twelve renders, and all twelve helper-history validations passed. The final results retain three nonblocking warnings: PSEPK mlaE and mlaF do not cite provider research inside annotation support (the genuine reports remain in top-level references), and PSEPK mlaF's precise core location lacks a matching existing row. No NEW row was manufactured to silence that warning. Two pre-existing Ttg2E non-verbatim local quotations were corrected; the shared local-quote baseline was not edited in this scope and may be pruned by root.

All twelve PAINT-loss commands completed. ECOLI target lineages report no IRD/IKR losses. For five PSEPK proteins the leaf is unavailable, and the frozen Ttg2E flat file has no PANTHER cross-reference; these outcomes do not establish absence of evolutionary losses. The family agent separately investigates current official membership.

Existing genuine OpenScientist reports were reused for PSEPK. Six required ECOLI Falcon attempts genuinely failed with HTTP403 authentication and produced no fabricated provider output. Logs are retained. No new publications were fetched by this agent; root acquired the additional shared papers. Abstract-only curator evidence remains explicitly bounded and is not rejected because full text is inaccessible.

Reproduce the payload/source/identity proof from the worktree root:

```sh
uv run python analysis/module_audits/bacterial_mla_intermembrane_phospholipid_transport/existing-review-consultation/check_preservation.py
```

Use `--write-results` only before a release is frozen; the default command does not overwrite the receipt. Root-owned module, families, additional genes, project tracking and any full validation are separate work.
