# BioReason Chat Export
*Exported on March 22, 2026 at 03:17 AM*

---

**Organism:** Bacillus subtilis

**Sequence:**
```
MENNRLSQDEIDALLNGTGSTLDEPEIPEVDDLSEMERDAIGEIGNISFGSSATALSTLLNQKVDITTPSVTVIPRSKISDAFPEPYVAIEVNYTEGFSGSNLLVVEQSDAAIIADLMIGGDGKGADPSLGEIHLSAVQEAMNQMMGSAATSMSTVFSKKIDISPPRVELLDVTEEKGTDRIPDDEMLVKVSFNLKVGELIDSSIMQLYPLTFAKDLISSLMNSESAEEEETVQPEVTYEQPKEPVTPEPRIEPKQQQQPPKRQGTAKKAAPVQVSPVEFSAFDPNEAVQAPIHNLDMLLDIPLSITVELGRTKRSVKEILELSAGSIIELDKLAGEPVDILVNQRIVAKGEVVVIEENFGVRVTDILSQAERINNLK
```

### Thinking Trace
I begin with the domain architecture. The polypeptide is globally assigned to IPR051469 (Flagellar motor switch protein FliN/MopA/SpaO family, residues 1–378), marking it as a FliN-class C-ring component of the bacterial flagellar motor. The N-terminal half carries IPR028976 (CheC-like superfamily, residues 31–228) and the embedded IPR007597 (CheC-like protein domain, residues 36–169). CheC-like folds are adaptor/scaffold modules that create curved β-sandwich surfaces for assembling multiprotein switches and for transiently engaging chemotaxis factors. This N-terminal adaptor architecture causes the protein to nucleate and stabilize higher-order oligomers and to present docking grooves for partner proteins rather than catalyzing chemistry.

The C-terminal half transitions into IPR036429 (SpoA-like superfamily, residues 287–378) and converges with multiple FliN-defining signatures: IPR012826 (Flagellar motor switch FliN family, residues 295–370), IPR001543 (FliN-like C-terminal domain, residues 298–368), and IPR001172 (FliN/Type III secretion HrcQb family, residues 298–359). This SpoA-like β-sandwich provides rigid oligomerization interfaces that assemble the C-ring and couple it to other switch elements. The juxtaposition of an N-terminal CheC-like adaptor and a C-terminal FliN/SpoA-like oligomerization core is a canonical switch-scaffold architecture: the N-terminus recruits and organizes partners; the C-terminus locks the assembly into a torque-transducing lattice. Such a lattice confers protein binding and structural support as the immediate molecular functions, matching GO:0005515 protein binding and GO:0005198 structural molecule activity.

From these molecular activities, the biological role follows. By forming the C-ring scaffold that gates the transition between clockwise and counterclockwise flagellar rotation, this protein directly governs directional switching in chemotaxis. That switching is the pivotal control point for taxis behavior, placing the protein squarely in the process formalized as GO:0006935 chemotaxis.

The cellular context is dictated by the switch architecture. FliN-class assemblies localize to the cytoplasmic face of the flagellar basal body, where the rotor and stator meet. This positions the protein at the bacterial flagellum, consistent with the cellular component label GO:0009288 bacterial flagellum and the experimentally observed subcellular location.

Mechanistically, the N-terminal CheC-like domain seeds trimeric/oligomeric assemblies and transiently accommodates chemotaxis regulators, while the C-terminal FliN/SpoA-like core forms a rigid ring that interfaces with other switch elements. I therefore hypothesize that this protein oligomerizes with cognate switch proteins to build the C-ring and recruits chemotaxis effectors that tune switching kinetics. Likely interaction partners include the other switch constituents that couple chemotaxis signals to motor output and assembly factors that stabilize the basal body interface.

### Functional Summary
A scaffold subunit of the bacterial flagellar motor switch that assembles into the C-ring to control rotational direction during taxis. Its N-terminal adaptor module organizes partner binding, while its C-terminal oligomerization core builds a rigid lattice that transmits and gates signals from chemotaxis pathways to motor output. Operating at the flagellar base, it provides structural support and multivalent binding surfaces that coordinate assembly and switching within the flagellar apparatus.

### UniProt Summary
Probable component of the flagellar drive system.

### InterPro Domains
- **Flagellar motor switch protein FliN/MopA/SpaO** (`IPR051469`, family) — residues 1-378
- **CheC-like superfamily** (`IPR028976`, homologous_superfamily) — residues 31-228
- **CheC-like protein** (`IPR007597`, domain) — residues 36-169
- **SpoA-like superfamily** (`IPR036429`, homologous_superfamily) — residues 287-378
- **Flagellar motor switch FliN** (`IPR012826`, family) — residues 295-370
- **Flagellar motor switch protein FliN-like, C-terminal domain** (`IPR001543`, domain) — residues 298-368
- **Flagellar motor switch FliN/Type III secretion HrcQb** (`IPR001172`, family) — residues 298-359

### GO Terms
**Molecular Function:** molecular_function (`GO:0003674`), catalytic activity (`GO:0003824`), catalytic activity, acting on a protein (`GO:0140096`), hydrolase activity (`GO:0016787`), phosphoprotein phosphatase activity (`GO:0004721`), hydrolase activity, acting on ester bonds (`GO:0016788`), phosphoric ester hydrolase activity (`GO:0042578`), phosphatase activity (`GO:0016791`)

**Biological Process:** biological_process (`GO:0008150`), metabolic process (`GO:0008152`), locomotion (`GO:0040011`), cellular process (`GO:0009987`), biological regulation (`GO:0065007`), response to stimulus (`GO:0050896`), regulation of biological process (`GO:0050789`), response to external stimulus (`GO:0009605`), cellular component organization or biogenesis (`GO:0071840`), cell motility (`GO:0048870`), cellular metabolic process (`GO:0044237`), response to chemical (`GO:0042221`), taxis (`GO:0042330`), regulation of locomotion (`GO:0040012`), regulation of cellular process (`GO:0050794`), phosphorus metabolic process (`GO:0006793`), cilium or flagellum-dependent cell motility (`GO:0001539`), cellular component organization (`GO:0016043`), cellular component biogenesis (`GO:0044085`), regulation of cell motility (`GO:2000145`), chemotaxis (`GO:0006935`), cellular component assembly (`GO:0022607`), archaeal or bacterial-type flagellum-dependent cell motility (`GO:0097588`), phosphate-containing compound metabolic process (`GO:0006796`), cell projection organization (`GO:0030030`), regulation of bacterial-type flagellum-dependent cell motility (`GO:1902021`), organelle organization (`GO:0006996`), organelle assembly (`GO:0070925`), cell projection assembly (`GO:0030031`), dephosphorylation (`GO:0016311`), bacterial-type flagellum organization (`GO:0044781`), bacterial-type flagellum-dependent cell motility (`GO:0071973`), bacterial-type flagellum assembly (`GO:0044780`), bacterial-type flagellum-dependent swarming motility (`GO:0071978`), non-membrane-bounded organelle assembly (`GO:0140694`)

**Cellular Component:** cellular_component (`GO:0005575`), cellular anatomical entity (`GO:0110165`), intracellular immature spore (`GO:0042763`)

---
*Generated by [BioReason](https://bioreason.net)*
