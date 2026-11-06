# CodA manual annotation review — 2026-11-06

Applied annotation-reviewer and core-function-synthesizer guidance. Standard fetch seeded four IEA rows. The pristine document, row payloads and raw hashes are in `.cache/module-audit-logs/choline-betaine-20261106/coda-acinetobacter-new-members-baseline.json`. Default Falcon was attempted with `just deep-research ARTGO codA --provider falcon`; authentication failed (HTTP403), so these are manual notes, not a provider report.

## Identity and direct evidence

See `codA-source-analysis/README.md`, the unmodified official ENA record and executable sequence check: ATCC8010 AAP68832.1 exactly equals all546 residues of Q7X2H8. Q7X2H8 also merges MTCC944-related sequence evidence; this review anchors to the corrected ATCC8010 deposit. The primary cloning report states “cloned from genomic DNA of Arthrobacter globiformis strain ATCC 8010” and that recombinant enzyme is active with both substrates [PMID:14678796]. Its abstract establishes purified enzyme activity, homodimerization and covalent FAD. The mechanistic follow-up explicitly identifies this recombinant enzyme and molecular oxygen as primary acceptor [PMID:14690428]. Both sources are normally fetched abstract-only; the claimed facts are in those accessible abstracts.

PMID12637017 independently studies both substrate/oxygen concentration dependencies and finds that the intermediate predominantly stays bound during turnover. Its source stock is not established in the cached abstract; use as mechanistic corroboration only. PMID18072756 structure identifies His99 covalent FAD linkage and Glu312 substrate positioning. The older His87 assignment in PMID12795615 must not replace current residue numbering. No unsupported structure-wide activity transfer is used.

## Annotation decisions

The generic GO0016491 row is MODIFY to both choline oxidase (GO0033713) and aldehyde oxidase (GO0004031). The generic CH-OH row is MODIFY to GO0033713. Exact choline oxidase and FAD binding are ACCEPT. GO0004031 explicitly accommodates aldehyde + O2 + H2O → carboxylate + H2O2 + H+; it does not assert every aldehyde is a CodA substrate. Its second catalytic activity is restricted to betaine aldehyde, supported by the cloned-enzyme dual-substrate assays. No separate NEW MF duplicates these replacements. GO0033713 alone defines only the first oxidation, despite its EC cross-reference also being used for the overall four-electron reaction.

One NEW IDA BP: GO0031456 glycine betaine biosynthetic process. CodA performs both synthesis reactions directly. Current QuickGO parent/ancestor checks show it is a biosynthetic BP, not an ancestor of either MF; no redundant precursor-catabolism or broad biosynthesis terms are proposed. Same-role checks of P17444 BetA, P17445 BetB and P71016 GbsA returned0,1,0 annotations to this BP, respectively. This mixed result is not a reason to presume missing annotations; product-forming catalysis independently supports the process. No Q7X2H8 entry was found in gocams/index.tsv. Queries are frozen in the audit log directory.

Two catalytic cores represent the two real chemical steps. FAD binding supports the mechanism rather than a third separate core. No location term was added without localization evidence. Do not infer native uptake or stress phenotype from recombinant expression or the generic osmoprotectant role of glycine betaine.

## Family scope

Frozen UniProt PTHR11552:SF152 has official name OXIDASE (CODA), PUTATIVE (AFU_ORTHOLOGUE AFUA_8G04090)-RELATED. PTHR11552 is GLUCOSE-METHANOL-CHOLINE  GMC  OXIDOREDUCTASE. Family/domain classification alone is insufficient for choline substrate, oxygen acceptor or dual-step capacity. Exact target biochemistry is the grounding.
