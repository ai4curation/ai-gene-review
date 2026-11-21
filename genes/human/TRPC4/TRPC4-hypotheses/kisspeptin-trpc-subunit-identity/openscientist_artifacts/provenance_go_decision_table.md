# GO decision table — TRPC4 kisspeptin subunit-identity hypothesis (leads; curator to verify)

**Hypothesis:** TRPC4 "alone combines the cSrc tyrosine + PIP2 determinants" and therefore
carries the kisspeptin-evoked GnRH-neuron current.
**Overall verdict:** Weakly/partially supported; the determinant-based rationale is **refuted**.

| GO aspect | Candidate term | Current evidence | Recommended action | Rationale / key PMIDs |
|-----------|----------------|------------------|--------------------|------------------------|
| MF | non-selective cation channel activity (e.g., GO:0005262 calcium channel activity / GO:0005216 ion channel activity) | Recombinant TRPC4α forms a PIP2-regulated cation channel | **Retain (generic)** | Legitimate for TRPC4, but **not diagnostic** of the native kisspeptin current. PMID:18230622 |
| MF | "determinant-defined subunit-exclusive kisspeptin channel activity" | None — determinants are trafficking (Y959/Y972) or shared (PIP2) | **Do NOT create / reject** | cSrc tyrosines = trafficking (PMID:16144838); PIP2 pan-TRP & shared with TRPC5 (PMID:37871124, PMID:18665391) |
| MF | phosphatidylinositol-4,5-bisphosphate binding (GO:0005546) | TRPC4α C-terminus binds PIP2 | **Lead — add with α-isoform qualifier** | Better than "protein binding"; isoform-specific. PMID:18230622 |
| BP | regulation of GnRH neuron excitability / cellular response to kisspeptin | Native current via PLCβ/PIP2 depletion + cSrc; TRPC4α mRNA present | **Add as non-core, context-specific (contributes_to)** | Mechanism is subfamily-level; subunit identity unproven. PMID:23744639 |
| BP | "TRPC4 homomer carries the kisspeptin current" | La³⁺-insensitive native current → heteromer | **Do NOT assert exclusivity** | PMID:18434521; native TRPC1/4/5 heteromers PMID:21968068 |
| CC | plasma membrane (GO:0005886) | Established for TRPC4 | **Retain** | — |
| CC | NHERF/cortical-actin association via C-terminal …VTTRL PDZ motif | TRPC4α links to F-actin via NHERF | **Lead — interaction, better than "protein binding"** | Shared with TRPC5. PMID:18230622, PMID:27994151 |

**Competing annotations to flag:** TRPC5 (equivalent PIP2-depletion gating) and heteromeric
TRPC1/4/5 channels are at least as consistent with the native kisspeptin current as a TRPC4 homomer.

**Minimal evidence that would change the call to "supported":** GnRH-neuron-specific TRPC4 (vs TRPC5/TRPC1)
conditional-KO electrophysiology showing loss of the kisspeptin current, and/or Y959F/Y972F knock-in
showing a gating (not trafficking) requirement in GnRH neurons.
