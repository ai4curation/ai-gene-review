# PlzA review notes

## Ligand receptor and strain identity

B31 BB_0733 (O51675) is PlzA, a protein with an extended PilZ architecture. [PMID:20030712](https://pubmed.ncbi.nlm.nih.gov/20030712/) directly measures specific c-di-GMP binding, lost after mutation of conserved Arg residues. Constructs come from B31-5A4; host-expression experiments also use B31-A3. [PMID:34117751](https://pubmed.ncbi.nlm.nih.gov/34117751/) provides the ligand-bound 7MIE structure, cross-referenced to the B31 UniProt sequence. No ligand activity is inferred solely from a PilZ domain prediction.

## Effector chemistry

[PMID:37086029](https://pubmed.ncbi.nlm.nih.gov/37086029/) uses recombinant PlzA cloned from B31-5A4. Direct synthetic-RNA assays establish annealing, strand displacement and unwinding; apo and holo forms accelerate annealing, whereas only apo PlzA unwinds/strand-displaces under the tested conditions. This supports NEW GO:0140691 RNA folding chaperone. Live QuickGO definition checked 2026-11-05: binding RNA to assist folding. It does not establish an ATP-dependent helicase, a particular endogenous RNA target or a direct role in every downstream gene-expression phenotype. GO:0033592 RNA strand annealing activity is a distinct ontology branch but is not separately added here because the chaperone judgment already describes the measured RNA-remodelling activity.

[PMID:38527857](https://pubmed.ncbi.nlm.nih.gov/38527857/) explicitly reports DNA/RNA binding requiring c-di-GMP; DNA binding supports NEW GO:0003677. The fetched published cache is abstract-only. The associated full author manuscript [PMC9915621](https://pmc.ncbi.nlm.nih.gov/articles/PMC9915621/) was additionally read via Europe PMC XML; its methods identify wild-type B31 plzA expressed as an N-terminal His fusion. The same manuscript discusses differences from the 2023 RNA work: substrates, mutant proteins, ligand concentrations, protein preparation and assay methods. Its methods are retrieval context, while the supporting quote is verbatim from the published PMID cache. Neither manuscript is used to erase the other's results. RNA binding may depend on substrate and conditions; native consequences of the in-vitro DNA binding require further work.

The seed has no GOA rows. Three NEW MFs cover distinct activities: cyclic-di-GMP binding (IDA), RNA folding chaperone (IDA), and DNA binding (IDA). No redundant generic nucleotide/RNA binding rows or speculative process terms are added. The core functions keep receptor occupancy and downstream nucleic-acid activities distinct. The 2014 review [PMID:24822172](https://pubmed.ncbi.nlm.nih.gov/24822172/) is historical context and predates the decisive effector studies.

## Retrieval and provenance, 2026-11-05

The standard `just fetch-gene` scaffold and its raw UniProt/GOA files were pinned by the parent audit in `analysis/module_audits/bacterial_c_di_gmp_signaling/seed-baseline.yaml`. Original annotation fields are preserved; only review judgments and explicitly NEW rows are authored here. No source files were edited manually.

`just deep-research-falcon BORBU plzA` was attempted on 2026-11-05 and failed with HTTP 403 (authentication/access failure). There is no provider-authored report; these are manual research notes. Logs are under `.cache/module-audit-logs/c-di-gmp-20261105/`. `just paint-losses BORBU plzA` was also run. PANTHER lineage losses could not be assessed because the accession is absent from the locally available family tree (or, for PlzA, no PANTHER family is present); this is an unavailable check, not evidence that no loss exists. The seeded rows contain no IBA.

The module boundary is synthesis, degradation and receptor occupancy. Tick survival, mammalian infection, motility and nucleic-acid regulation are informative gene-level outputs, not assertions that every bacterial representative shares those outputs. No new biological-process annotations were manufactured from necessity or infection phenotypes.


## PR #6062 review follow-up — 2026-11-06

Retained the directly assayed RNA-folding-chaperone and DNA-binding NEW rows, but removed them from core_functions. Cyclic-di-GMP binding remains the established core. The description, annotation reasons and existing questions distinguish in vitro capability from unresolved native targets, physiological significance and assay-dependent ligand effects.
