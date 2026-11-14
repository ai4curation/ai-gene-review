# E. coli LptM and YedD/LptY accessory consultation

Both reviews are COMPLETE with all four original ordered annotation payloads preserved. No NEW rows were proposed. No existing raw/provider/publication source was changed or refreshed, and no publication was fetched by this worker.

LptM's experimentally observed binding to LptDE is retained in the biological synthesis; the bare GO:0005515 row is removed as uninformative, not as a denial of interaction. Its existing outer-membrane location and assembly annotation are accepted. The core distinguishes structural stabilization of oxidative maturation from oxidoreductase catalysis, and includes mature translocon support established by the newer structure/functional study.

YedD is the official frozen symbol; LptY is the new literature name. Its seeded plasma-membrane IEA maps an old UniProt location prediction. Full-primary identification, co-purification and structural placement support the mature outer-membrane translocon location, so the row is MODIFY to GO:0009279 with a structured UniProt source defect. This is a lateral compartment correction, not an ancestry claim or denial of biosynthetic transit through the inner membrane.

Both cores use **contributes_to** LPS transmembrane transporter activity. The proteins perform structural work in the active translocon: LptM contacts the lateral gate and LptY stabilizes the LptD beta-taco domain. Neither is asserted to independently translocate LPS, hydrolyze ATP or catalyze disulfide formation. The supported process synthesis is not based on knockout necessity alone. Cellular assays measure conditional envelope permeability and LPS-migration effects during DsbA loss or LptC overproduction; simulations propose dynamics and are not direct single-protein flux measurements. These proteins remain lineage-qualified accessories, not universal requirements of every Lpt pathway.

`source-scope.md` records primary strains, tagged complexes, map/model limits and controlled phenotype interpretation. `sequence-bridge.json` and the official RCSB captures independently establish P0ADN6 as the 67-residue precursor plus His8 in 9IA5, and P31063 residues21–137 in 9FZ5. The latter is identity provenance, not a claim that its separate paper's functional evidence was reviewed. The 2025 holo-complex map contains LptY density fitted with an AF model; the associated deposited 9IA5 atomic model lacks a complete LptY chain. Model contents are not silently equated with all constituents of the experimental map.

Family classification uses the immutable target records: LptM IPR032831/PF13627/NF047847 and YedD IPR025596/PF13987/NF007705. Neither has a PANTHER family in those records. Normal PAINT tooling therefore could not test losses; absence of a family identifier is not a loss-free phylogenetic result. Two real Falcon attempts failed HTTP403 and no provider report was fabricated.

## Checks and preserved handoffs

Two focused gene validations, renders and helper-generated history validations pass. Four advisory warnings remain: each protein's core LPS-transport process and Lpt-system membership lacks a dedicated annotation row. These do not justify manufacturing NEW rows. The runtime pkg_resources deprecation is separate. File-scoped Ruff and format checks pass.

`check_preservation.py` verifies four seed rows, 87 unique protected/consulted source files, both deposited sequence matches and the exact 76-file E. coli and 40-file Neisseria frozen handoffs. No previously released consultation was edited. Run it with:

```sh
uv run python analysis/module_audits/bacterial_lps_transport/accessory-consultation/check_preservation.py
```

No module, family, project, full-corpus validation, commit or publication is included in this handoff.
