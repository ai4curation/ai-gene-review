# Mla family consultation — 2026-11-07

Six existing family reviews were reassessed against the actual PANTHER19 reference trees/MSAs, current official UniProt records, current GO definitions and primary evidence. This is a family consultation, not a new whole-corpus validation or a proof of native flux. The root and other agents own the module and genes. No protected source, original history, PAINT seed/date/payload or gene record is rewritten here.

## Classification and activity are separate

| Role | Verified classification for the reviewed panel | Functional boundary |
|---|---|---|
| MlaA | PTHR30035:SF3; ECOLI P76506, PSEPK Q88KX6, BORPE Q7VSZ7 | Positive MlaA architecture and envelope context; SF1 has unresolved physiology, not a demonstrated loss. Exact E. coli OmpC/F partners are not universal. |
| MlaC | PTHR36573:SF1; P0ADV7, Q88P91, Q7VSZ6, Q9HVW4 | Positive bacterial carriers; pocket occupancy does not prove every family member has a bacterial periplasm or completes the route. |
| MlaF | PTHR43023:SF6; P63386, Q88P94, Q7VT00 | ATPase chemistry is supported; SF6 also contains MceG P9WQL5. Shared ATPase ancestry does not license the same cargo/partners. |
| MlaE | PTHR30188:SF4; P64606, Q88P93, Q7VSZ9 | Same subfamily also contains TGD1 Q8L4R0 and YrbE1A O07412/YrbE4A O53546. Require positive bacterial Mla role and interface context. |
| MlaD | PTHR33371:SF4; P64604, Q88P92, Q7VSZ8 | Same subfamily contains Mce1D O07416/Mce4D I6XHD6. Binding, donation and assembled transfer are distinct claims. |
| MlaB | PTHR35849:SF1; P64602 and **current** Q88P90 | Q88P90's immutable older flatfile lacks the assignment; dated current official JSON and refreshed index support SF1. Do not replace the old source. No B representative is invented for Bordetella. |

These exact classification IDs can remain on role descriptors with positive member, cargo, compartment and partner gates. An UNRESOLVED universal function grant is not a claim that an established family identity is false. Conversely, a family ID cannot stand in for those biological gates. `target-membership.json` captures the 18 immutable raw records; the explicit newer Q88P90 source is `Q88P90-uniprot.json` plus `additional-acquisition.json`.

All 21 original PAINT payloads remain ordered and exact. Eleven unrelated node objects remain completely unchanged. Twenty term-scope judgments are now UNRESOLVED where the previous grant/exclusion exceeded evidence. There are no added PAINT rows or invented residue/site determinants. Broad MlaF ATP binding/hydrolysis remains supported: all 90 reference-leaf sequences contain a Walker-A candidate and all four SF4 leaves also contain the ABC LSGGQ signature. This supports the ABC genus, not a lipid substrate or transport direction.

## Material corrections

* **MlaF SF4 is populated.** The official tree contains Q9F3K7, Q89T24, Q2FVL4 and A0A3N4B1K8. Current UniProt moves Q9F3K7 and Q2FVL4 to PTHR43166; both official assignments are archived, without an override or a false claim that one source was absent. MlaE SF14 likewise contains two Brassica leaves, previously described as unrepresented.
* **GO0120010 is not diderm-specific.** Its definition permits transfer between membranes generally. Chloroplast TGD function is a different cellular mechanism, not automatically a false GO0120010 assertion. Mycobacterial alternate cargo is positive evidence of another role, not a target-negative phospholipid assay. Twelve former member-exception objects are explicitly withdrawn to uncertainty, preserving their exact historical objects.
* **The genuine plant localization loss remains current.** The exact PTHR30188 PTN001575509 LOSS_SUPPORTED object is unchanged. Its real 50-leaf clade spans SF4 and SF14; a family-wide plasma-membrane grant with only Arabidopsis excluded would falsely license other plants. `current-member-assessments.json` retains Q8L4R0 as CURRENT_SUPPORTED_NEGATIVE with original supporting evidence. The production checker rejects a live `member_exceptions` field under UNRESOLVED (`EXCEPTION_OUTSIDE_SCOPE`), reproduced by the negative control. The current ledger is **not** consumed by that production checker; the original PAINT loss stays live, and the supported member judgment is retained explicitly rather than disguised as a universal scope.
* **MlaC's reference coverage is not exclusively bacterial.** Current official A8DVR8 is labelled Nematostella and classified SF1; the Ricinus B9TGW9 reference leaf is now an inactive UniProt record. Assembly/classification artifacts are possible. Neither a biological alternative function nor contamination is asserted. Positive bacterial carriers remain supported; root-level periplasm/route propagation is unresolved.
* **MlaB contribution and requirement are separate.** Binding/stabilizing MlaF and regulating assembly/ATPase are positive mechanistic contributions. They do not make MlaB an aqueous lipid carrier. E. coli conditional ATPase-overexpression rescue and the Bordetella locus lacking identifiable B qualify an unconditional B requirement; neither proves universal dispensability.
* **MlaB DNA-response exclusion was too categorical.** Full PMID20128927 reports genotoxic survival controls and yrbB complementation. The GO definition is broader than DNA repair. Whether MlaB supplies response-specific work or constitutive envelope protection remains unresolved; both the original node payload and the archived former negative verdict remain traceable.

The older Mce host-entry node judgment and P-type-complex exclusions were outside the bounded Mla-role changes and remain exact. Preserving that older host-entry assessment is not a claim that this consultation independently resolved its broader evolutionary argument.

## Source and assay limits

`evidence.md` records primary context and verbatim excerpts. `quotes.json` deterministically verifies every structured quotation against its actual source; source-byte identity is captured in `preservation.json`. Reference titles are validated against the immutable publication caches. The annotation-reviewer guidance was applied to family/node judgments; no inference from donor counts, self-donors, missing GOA or isolated-subunit assay absence was used as a loss proof.

The frozen preflight is read without rerunning its in-place-writing verifier. PMID28388411 directly measures interactions by BLI; its handoff description is a discussion model. Later reconstituted transfer experiments support movement and ATP bias. Positive native/heterologous evidence for new members is held in the released new-member consultation, with Bordetella B213-to-Tohama I lineage mapping distinguished from complete sequence identity and individual assays. This family review does not turn a native MlaF perturbation into direct assays of every Bordetella subunit.

## Verification and release

Run `uv run python <this-directory>/check_preservation.py` and `inspect_evidence.py` to reproduce the source/node/membership checks. The former's outputs are deterministic under different Python hash seeds. `run_checks.py` invokes focused production schema, term, reference, family/gene and Ruff checks; `grounding.log` reports 142 PASS, 0 FAIL, 0 UNRESOLVED for the six selected families after the single incremental index refresh. Six histories are generated with `just new-history` and validated. No family HTML renderer exists in the repository convention.

The member index is a derived ignored artifact, not a cited biological source. The refresh resolves all 18 panel members; its global unresolved/disagreement totals concern the whole referenced corpus. `handoff.json` freezes only owned curated files, new histories and consultation artifacts, plus an exact input closure. Root retains responsibility for module integration, full validation and publication. No commit, staging, push or full-corpus run was performed.
