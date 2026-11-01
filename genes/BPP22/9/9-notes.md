# Curation Notes: Salmonella phage P22 Tail spike protein gp9 / Endo-1,3-alpha-L-rhamnosidase (gene `9`, UniProt `P12528`)

## Identity & Domain Architecture
- **Gene symbol:** `9` (`FIBER_BPP22`)
- **UniProt ID:** `P12528` (667 AA, ~71.9 kDa monomer; 215 kDa homotrimer; mature chain residues 2-667 after initiator Met cleavage)
- **EC number:** `EC:3.2.1.242` (endo-1,3-alpha-L-rhamnosidase; CAZy family `GH90`)
- **InterPro / Pfam / Structural Classification:**
  - `InterPro:IPR009093` (`P22_tailspike_N`) / `Pfam:PF09008` (`Head_binding`, residues 5-108): N-terminal trimeric dome-like head-binding domain that anchors non-covalently and quasi-irreversibly to the hexameric gp10 tail hub.
  - `InterPro:IPR015331` (`P22_tailspike_C`) / `Pfam:PF09251` (`PhageP22-tail`, residues 114-363) & `InterPro:IPR011050` (`Pectin_lyase_fold`): central 13-turn right-handed parallel beta-helix domain (residues 143-540) harboring the O-antigen binding groove and endorhamnosidase active site (`Glu359`, `Asp392`, `Asp395`).
  - `InterPro:IPR012332` (`Betaprismlike_sf`) / `InterPro:IPR036730` (`Sialidase_C_dom_sf`): C-terminal interdigitated triple beta-helix / beta-prism clamp domain (residues 540-666) required for protrimer folding and extreme thermostability ($T_m \approx 88^\circ\text{C}$).
- **PDB structures:** `1TSP` (2.0 Å C-terminal domain), `1TYU` / `1TYV` / `1TYW` / `1TYX` (1.8 Å complexes with *Salmonella* O-antigen oligosaccharides), `1LKT` (2.3 Å N-terminal head-binding domain), `2VFM` (full-length crystal structure), `8I1T` / `8I1V` (cryo-EM of P22 tail apparatus).

## Literature & Functional Synthesis
1. **Receptor Binding and Endo-1,3-alpha-L-rhamnosidase Catalysis (`PMID:383902`, `PMID:8023158`, `PMID:8889178`, `PMID:8855221`, `PMID:9135118`):**
   - Six homotrimers of gp9 attach via their N-terminal head-binding domains (residues 1-124) around the hexameric gp10 tail hub in the final step of P22 morphogenesis (`PMID:9135118`, `PMID:37952769`).
   - Each subunit of the C-terminal parallel beta-helix domain exposes a 21-Å cleft that binds the O-antigen polysaccharide repeats of *Salmonella* serogroups A, B, and D1 lipopolysaccharide (`PMID:383902`, `PMID:8889178`, `PMID:9135118`) and cleaves the $\alpha(1\to 3)$-O-glycosidic linkage between L-rhamnose and D-galactose using catalytic triad residues Glu359, Asp392, and Asp395, yielding octasaccharide (two repeating units) as the principal product (`PMID:383902`, `PMID:8855221`, `PMID:9135118`).
2. **Essential Role in Virion Attachment and LPS-Triggered Genome Ejection (`PMID:20817910`, `PMID:30886360`, `PMID:37952769`):**
   - Reconstitution of tailspike-less P22 heads with wild-type versus catalytically deficient gp9 mutants (`D392N`, `D395N`, `T307K`) proves that both O-antigen binding and endorhamnosidase hydrolysis are strictly required prior to DNA ejection in vitro and infection in vivo (`PMID:20817910`).
   - Cryo-electron tomography (`PMID:30886360`) shows that P22 virions initially attach obliquely via two of the six tailspikes plus the gp26 needle tip, then hydrolyze O-antigen chains down to ~5 repeat units (~8 nm from the outer membrane) to reorient the virion perpendicularly and force the gp26 needle into the outer membrane.

## GO Annotation Decisions
- `GO:0052775` (endo-1,3-alpha-L-rhamnosidase activity, IDA `PMID:383902`, IDA `PMID:20817910`, IEA `GO_REF:0000003`, IEA `GO_REF:0000120`): `ACCEPT` on all 4 rows.
- `GO:0016787` (hydrolase activity, IEA `GO_REF:0000043`): `MODIFY` -> `GO:0052775`.
- `GO:0016798` (hydrolase activity, acting on glycosyl bonds, IEA `GO_REF:0000043`): `MODIFY` -> `GO:0052775`.
- `GO:0019062` (virion attachment to host cell, IDA `PMID:20817910` & IEA `GO_REF:0000120`): `ACCEPT` on both rows.
- `GO:0098995` (symbiont entry into host cell via enzymatic degradation of host lipopolysaccharide, IDA `PMID:20817910`, IEA `GO_REF:0000043`, IEA `GO_REF:0000104`): `ACCEPT` on all 3 rows.
- `GO:0044409` (entry into host, IDA `PMID:20817910` & IEA `GO_REF:0000104`): `MODIFY` -> `GO:0098995`.
- `GO:0046718` (symbiont entry into host cell, IEA `GO_REF:0000043`): `MODIFY` -> `GO:0098995`.
- `GO:0098994` (symbiont entry into host cell via disruption of host cell envelope, IEA `GO_REF:0000043`): `MODIFY` -> `GO:0098995`.
- `GO:0098671` (modulation by virus of host lipopolysaccharide metabolic process, IDA `PMID:20817910`): `KEEP_AS_NON_CORE` (captures the extracellular cleavage of host surface LPS O-antigen chains by the virion tailspike, whereas its core process role is `GO:0098995`).
- `GO:0098024` (virus tail, fiber, IDA `PMID:8023158`, IDA `PMID:20817910`, IEA `GO_REF:0000120`): `ACCEPT` on all 3 rows.
- `GO:0098015` (virus tail, IDA `PMID:37952769` & IEA `GO_REF:0000043`): `MODIFY` -> `GO:0098024` (`virus tail, fiber`).
