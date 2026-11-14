# Carnitine family consultation — 2026-11-07

## Provenance and scope

The frozen PAINT assertion tables, member inventories and compact PANTHER trees were inspected together. `baseline.json` preserves pre-edit review documents and raw-input SHA256 hashes; `tree-scope.json` records actual descendant leaves and input tree hashes. Trees originate from the normal PANTHER treeinfo endpoint, https://pantherdb.org/services/oai/pantherdb/treeinfo?family=PTHR48075 (substitute the family identifier), via the repository's `etl/panther_trees.py`. No new topology was inferred from GOA absence. Cached trees are snapshots, not a claim that every contemporary UniProt accession is present.

## Transport families

PTHR47737 PTN000766131 covers all 13 cached leaves, including PAO1 Q9HTI7 and E. coli ProW P14176. PTHR43869 PTN002466744 covers all 14 cached leaves, including PAO1 Q9HTI8. The frozen PAO1 UniProt records independently assign Q9HTI7 to PTHR47737:SF1 and Q9HTI8 to PTHR43869:SF1. Their current review paths are genes/PSEAE/cbcW and genes/PSEAE/cbcV; PA5377 and PA5376 are locus tags. HutW Q9KKE2 and HutV Q9KKE1 occur in the inventories but not in these tree snapshots, so their descent from these particular PTNs is unverified.

PMID19919675 establishes PAO1 CbcWV construct function with compatible binding proteins and distinguishes PA14 native mutants and heterologous uptake hosts. Binding proteins select tested cargo; the experiments do not prove that the permease has no intrinsic selectivity or that arbitrary family members are interchangeable. Known alternative native cargo is insufficient to establish a loss of all carnitine, choline or betaine transport capability. Root cargo-specific assessments therefore remain unresolved without an exact supported pruning boundary; positive CbcWV transport evidence is retained. The chemically distinct amine versus quaternary-ammonium term correction is retained, based on the existing independent ontology analysis, not on donor count.

## Dehydrogenase family

PTHR48075 PTN002455225 covers 157 cached leaves. PTN000592731 covers 45 SF1 leaves, including Bradyrhizobium Q89HA7 and Sulfolobus Q7LXQ8 as well as animal, fungal and other eukaryotic members. SF1 is not animal-only. The pre-existing PAINT gulonate judgment is retained as a phylogenetic inference, not as experimental characterization of every leaf.

PTN008732775 covers 16 bacterial leaves, including E. coli PaaH P76083 and M. tuberculosis FadB2 P9WNP7. PAO1 CdhA Q9HTH8 is present elsewhere in the tree and is not below this node. KT2440 Q88R32 and S. meliloti Q92NF5 are absent from this tree snapshot; their absence from a GOA term cannot establish their ancestry. PaaH's alternative physiological pathway alone does not disprove secondary fatty-acid chemistry, so the native beta-oxidation node scope stays unresolved. Positive acyl-CoA dehydrogenase inference at the node and exact carnitine chemistry of named proteins are retained separately. Mixed SF5 membership cannot grant carnitine activity to the entire subfamily.

The RHIME primary/sequence bridge is documented in genes/RHIME/bcoE-bcoF/bcoE-bcoF-source-analysis/primary-scope.md: the assayed 3D0a2 clone is identical to Rm2011, whose translated products match the Rm1021 reference sequences. This does not make the reported native growth phenotypes identical. BcoEF is one fusion with dehydrogenase and thioesterase regions and three measured reactions; the upstream carnitinyl-CoA hydrolysis is distinct from the two free-carnitine catabolic steps.

## BKACE substrate range

PTHR37418 has 17 cached leaves and no extracted PAINT IBD assertions. The exact-target supplementary-data mapping and source access limits are recorded in ../psepk-consultation/evidence.md and its reproducible spreadsheet analysis. Q88R31 is BKACE511. Dehydrocarnitine screening values are 146.407 and 237.1; (S)-KAH values are 50.55 and 81.021. These are pre-process screen signals, not target kinetic constants. The substrate-specific positive threshold was not recovered. KAH activity is therefore unresolved, not excluded because the protein participates in carnitine catabolism. Other G5 enzymes have measured KAH promiscuity, so 'only Kce orthologs' is an unsound categorical boundary. Conserved acyltransfer chemistry and named-member carnitine reactions remain supported; no family-wide exact substrate grant is made.

## Hotdog thioesterase family

PTHR31793 PTN001273712 covers 212 cached leaves, including PAO1 CdhB Q9HTH9. PTN001273713 covers 97 plant/algal leaves spanning several subfamilies; it excludes bacterial CdhB. The plant acyl-ACP and chloroplast positive PAINT assertions are retained. The associated IRD is preserved exactly but its loss judgment is unresolved: acyl-ACP use alone does not demonstrate absence of acyl-CoA hydrolysis. Similarly, demonstrated betainyl-CoA hydrolysis does not establish that every SF2 protein lacks secondary fatty-acyl-CoA activity. The original broad fatty-acyl node cannot be confidently affirmed or pruned from the available substrate evidence. Positive FadM chemistry remains represented by the original experimental seed and is not denied. The exact substrate range of the mixed family requires member-level evidence.

## Interpretation

UNRESOLVED concerns the reach of a family assertion or a proposed evolutionary loss, not the falsity of a measured member reaction. No node, seed, date, negation or evidence code is rewritten. Exact pathway capacity must additionally require the reviewed reaction and compatible partner/architecture; family membership alone is insufficient.
