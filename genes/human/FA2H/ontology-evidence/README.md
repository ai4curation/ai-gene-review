# FA2H ontology evidence: ceramide and glycosylceramide biosynthesis

This directory preserves the actual official QuickGO responses used for the FA2H specificity decisions. It allows review without network access. The raw response bytes and original HTTP receipts were saved on **2026-10-25 at 09:21:01–09:21:02 UTC** and are copied unchanged here. They are supporting evidence, not edits to the repository's generated ontology cache.

| Child | Typed relation | Parent |
|---|---|---|
| GO:0006679 glucosylceramide biosynthetic process | `is_a` | GO:0046513 ceramide biosynthetic process |
| GO:0006682 galactosylceramide biosynthetic process | `is_a` | GO:0046513 ceramide biosynthetic process |
| GO:0046513 ceramide biosynthetic process | `is_a` | GO:0030148 sphingolipid biosynthetic process |

These are explicit `children[].relation` entries in [terms.json](terms.json), not relationships inferred from names or chemistry. The separate [is-a-ancestors.json](is-a-ancestors.json) request restricts traversal to `relations=is_a`: both branch terms include GO:0046513 and GO:0030148 in their ancestor lists, and neither branch includes the other. The [readable projection](projection.json) includes the complete returned ancestor lists, term definitions, exact JSON pointers to each direct edge, URLs, times and SHA-256 hashes.

| Saved response | SHA-256 |
|---|---|
| [terms.json](terms.json) | `873d8a3a046400ac2e8f61b02eec4d8de09489081beee9743e6792bac6ce7ac0` |
| [is-a-ancestors.json](is-a-ancestors.json) | `6bcdc909416abb747d774442cfc6d8ab697ced077d3877ab03de3302c78d3a66` |

The [term retrieval receipt](terms.json.receipt.json) and [ancestor retrieval receipt](is-a-ancestors.json.receipt.json) preserve HTTP 200, request/final URLs, start/end times, byte lengths and hashes. No GO release identifier is present in those saved responses or receipts; none is invented. These records establish the retrieved snapshot, not an assertion that the service can never change.

Public service locators are the [term request](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0006679,GO:0006682,GO:0046513,GO:0030148,GO:0061436,GO:0120520,GO:0120521) and the [is_a-only ancestor request](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0006679,GO:0006682,GO:0046513,GO:0030148,GO:0061436,GO:0120520,GO:0120521/ancestors?relations=is_a). The saved responses are sufficient for this check; following these links performs a new live query.

Run `python3 verify.py` from this directory, or provide the script's path from any working directory. The verifier uses only the Python standard library, reads these files, verifies response hashes and the exact projection, and checks the typed relations and mutual non-ancestry. It makes no network request or file changes. It does not validate gene biology or replace gene-review schema checks.

See the [source guide](../FA2H-source-guide.md#cross-source-refinement-and-offline-ontology-evidence) for the separate experimental support and the meaning of the review actions. An ontology edge does not imply that one experiment assayed both downstream branches.
