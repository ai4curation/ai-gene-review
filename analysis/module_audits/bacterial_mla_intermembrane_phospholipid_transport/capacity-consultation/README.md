# Independent Mla capacity and scientific closure audit

This audit evaluates the actual production `compile_node`/`is_satisfied` circuit while supplying explicitly external biological predicates. It does not change the module, genes, families, production compiler or previously frozen releases. Authored biological requirements and cases are YAML; machine receipts are JSON.

## Biological meaning

The profile is source-supported intermembrane phospholipid capacity in a compatible diderm envelope. It requires outer-membrane MlaA, a periplasmic MlaC carrier, and matched MlaF/E/D machinery with ATP and suitable phospholipid cargo. MlaB is required by the sampled native six-component architecture; the positively supported Bordetella architecture lacks an identifiable B. An arbitrary B deletion does not establish that alternative. Same-family matches alone do not establish a compatible substrate/interface system.

| Panel | Finite-profile conclusion | Evidence limit |
|---|---|---|
| ECOLI | Complete six-component capacity | Characterized interfaces and purified reconstitution; not a claim that every experiment measured native whole-cell flux |
| PSEPK | Complete matched inferred capacity | Specific family/locus/structure and conserved-function inference, not a KT2440 full-pathway assay |
| BORPE | Complete five-component inferred capacity | B213 native pathway genetics plus Tohama I locus bridge and conserved roles; direct BP3761 structural binding does not establish target flux |
| PSEAE | Carrier step only | PAO1 Ttg2D cargo and periplasmic evidence; missing reviewed matched interfaces prevent a complete-panel conclusion |

Unknown native flux is not negative functional evidence. Positive E. coli MlaF-overexpression rescue without B (PMID32602838) is a supported conditional comparator outside the two encoded reference architectures. Its negative encoded-profile result means incomplete representation, not biological impossibility. The cases do not assert a universal MlaB requirement or deny other possible routes.

`biology.yaml` is independently source-qualified: exact existing review paths, panel/strain limits, role requirements and source claims. The checker derives the actual participants and conjunction of active units from the current module. It then requires exact reviewed member identity, official family classification, independently assigned source role, supported core activity or qualified structural contribution, appropriate compartment and matched biological context. The current Q88P90 family is read from the separately archived official UniProt snapshot without changing its preserved older flat file.

For PSEPK Ttg2E, the qualified structural contribution consists of a supported core in the ABC complex and intermembrane-transfer process; the oracle does not invent an enzymatic MF. A carrier's binding-only core can support the finite carrier role only with its reviewed intermembrane participation and independent specific carrier/system evidence. This is not a rule that any phospholipid-binding protein performs transfer.

## Production limitations and independent checks

The production compiler creates four atoms and two routes. It does not inspect complex `active_units`, enforce `connections`, interpret biological context prose, or enforce EXACTLY_ONE exclusivity. The checker demonstrates these facts by removing all units or connections and observing unchanged raw routes, and by satisfying both alternative atoms simultaneously. It never claims those requirements are enforced by the compiler.

The external oracle evaluates actual active-unit declarations conjunctively. An independent source-based structural contract rejects missing required roles, wrong/deleted declared molecular functions or compartments, and wiring that makes required steps optional or requires both alternative assemblies. Current annoton and active-unit function IDs are bound to the independently supported activities and reviewed cores; a changed declaration cannot silently inherit a hardcoded successful gene gate.

The finite suite has60 cases,14 structural mutations and12 gate sensitivities. Cases include each missing required role in three panels, missing B, carrier-only/isolated components, mixed panels, absent ATP/cargo/interfaces/compartment/diderm context, unknown flux, and source/role/function/identity masking. Masks alter actual copied evidence/member/core fields rather than just changing an expected answer. Gate bypasses must restore the corresponding positive witness, proving that the tested requirement is causally active in the oracle.

Mutations include omitted parts and units, optional carrier/assemblies, wrong family, forced B in Bordetella, both-assembly wiring, wrong ATPase/complex MF, deleted carrier MF and wrong carrier compartment. Some invalid mutations leave raw production satisfaction unchanged because the compiler cannot represent the requirement; their source-contract rejection is reported separately. Others produce a false positive or false negative witness. The mutation receipt distinguishes these outcomes rather than claiming all were caught by production alone.

Eight actual alternative proteins test broad-classification overreach. Official family-tree evidence places MceG, YrbE1A/YrbE4A, Mce1D/Mce4D and chloroplast TGD1 in the same sampled MlaF/E/D subfamilies; six therefore pass a naive family selector. TGD3 is in a different subfamily. SpoIIAA P10727 provides a genuine unrelated STAS-domain protein with curated anti-sigma-factor-antagonist context. None is licensed as a replacement in the finite matched Mla profile. The challenge even grants the substituted protein the tested role's reviewed activity to show that identity/source/interface evidence still matters. These are not assertions that those proteins lack all phospholipid activity, nor that GO0120010 is diderm-specific.

## Scientific preservation and closure

`check_closure.py` verifies all105 pre-existing ordered annotation payloads plus ten newly seeded payloads, the sixteen active historical NEW rows, zero added/retired rows, protected raw/provider/publication bytes, and every file in the seven frozen release manifests, including the explicit three-file family prose supersession and independent scientific review/follow-up. It includes the final COMPLETE module, render, histories and all local module/member citations. Its closure is scientific; root-owned project/full-corpus/publication metadata is excluded. All inputs must be durable repository-relative files; ignored-cache inputs are rejected.

Run from the worktree:

```
uv run python analysis/module_audits/bacterial_mla_intermembrane_phospholipid_transport/capacity-consultation/check_capacity.py
uv run python analysis/module_audits/bacterial_mla_intermembrane_phospholipid_transport/capacity-consultation/check_closure.py
```

The source ledger verifies every short fixture quote against the actual source. The final closure waits for all releases and the final module; it must not freeze a partial or stale hash set. These checks establish finite source-qualified representational behavior and preservation, not independent experimental validation, a proteome-wide classifier, definitive lineage loss, partner interchangeability or universal native transport direction.
