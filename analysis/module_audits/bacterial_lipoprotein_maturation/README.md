# Bacterial lipoprotein maturation audit

The module models the required Lgt/LspA maturation core and five optional, chemically distinct terminal routes: Lnt, Lnb, compatible LnsAB, Lit and LhaT. Taxon Bacteria is an occurrence envelope, with reviewed exemplars from Pseudomonadota, Bacillota and Bacteroidota. It is not a claim that every bacterial lineage carries every route or that these enzymes are universally essential.

Eleven manually assessed references include three review articles and provide 23 source-checked findings. Evidence is attached to individual functions and ordered connections. Primary studies correct older assumptions about unknown monoderm tailoring and universal Lnt. The 2019 review's isolated “thioester” wording for the Lgt product is not adopted; the linkage is a thioether.

## Reviewed members and preserved evidence

Fourteen COMPLETE reviews contain 88 annotations: 73 inherited rows in the original eight-member panel, two unchanged rows in the approved LhaT review, and 13 newly authored assertions in five normally seeded genes. All original ordered source payloads and three inherited NEW proposals remain. No original annotation is deleted or retired. The LhaT gene is reused byte-for-byte from the approved Ac-HepG audit, with commit/blob and fresh-source compatibility proof. Its family review did not exist in that approved PR and is newly curated here.

The four PANTHER reviews cover Lgt, LspA, Lnt and LhaT. Ten existing PAINT assertion payloads remain unchanged. LspA uses the current signal-peptidase activity while retaining its independently supported aspartic mechanism. Lnt's uncertain amidase scope is unresolved rather than categorically excluded from incomplete placement evidence. The Ppm1 classification disagreement is recorded. LhaT's measured P54392 activity is retained while broader family transfer remains unresolved because an inactive homolog is experimentally known. Lnb uses a descriptive whole-protein family with the verified NF051878 and two-domain architecture, avoiding a domain-only or invented PANTHER selector. LnsA/LnsB and Lit use verified InterPro family identifiers.

`check_preservation.py` rechecks the original payloads, immutable sources, released consultation files and all module reference quotations. Individual consultation directories contain source acquisition, identity bridges, scientific reasoning and validation receipts. `root-progress.json` is a dated pre-finalization snapshot; it is not a full-corpus validation result.

## Capacity and product boundaries

The capacity consultation uses the production Boolean circuit plus independent biological gates. The compiler does not descend complex active units; the external audit checks both LnsAB partners and the measured directional cross-species pairing constraint. It also enforces product identity, LhaT activity qualification and carrier availability. Shared-core satisfaction does not imply a terminal product. Lnb's unresolved donor is not replaced with an assumed PG donor; Lit relocates an existing chain and retains two long acyl chains; LhaT adds acetyl rather than a third long chain.

ECOLI and PSEPK have reviewed upstream and Lnt panels; BACSU has reviewed upstream and LhaT genes. The Bacteroides, S. aureus and B. cereus terminal exemplars establish those reactions without constituting complete native upstream panels. B. fragilis rescue in E. coli is explicitly engineered. The S. epidermidis pairing controls have exact RefSeq/UniParc identity bridges but deleted UniProt records; failed empty fetch outputs are archived outside genes and are neither complete reviews nor module representatives.

Lnb reporter purification is not purified-Lnb enzymology. S. aureus LnsAB PG-sn1 preference is not granted to untested pairs. Lit's proposed acid-base intermediate is not a trapped intermediate. LhaT reconstitution uses target-containing membranes, a C20 carrier analogue and mixed acetyl donors; native C35 preference and carrier crossing remain unresolved. Carrier synthesis, precursor export, Lol trafficking and client functions are outside this module.

## Validation and publication

Focused gene, family, module, history and rendering checks precede the frozen full-corpus run. Full-run receipts will name the exact science commit and terminal result. A COMPLETE module curation status does not mean this project audit is merged: the project remains in progress until full validation, a module-specific PR, required review/checks and actual merge. Broad open PR #5076 overlaps the module but does not substitute for this audit.
