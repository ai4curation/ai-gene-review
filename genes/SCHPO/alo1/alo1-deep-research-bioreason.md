# BioReason Chat Export
*Exported on March 22, 2026 at 12:31 AM*

---

**Organism:** Schizosaccharomyces pombe

**Sequence:**
```
MSIPHINKLSQDGRVRFSNWAKTFSAISLGLRCPKTEEQLREILVDANSNGKKIRVVGAGHSPSDIVCTSGYLLSLDKMNKVVSFDPDSLSITVQAGIRFYQVQEILQNLGYSLPIVGSISETSVSGIMSTCTHGSSLQHQVLPHYIKSMRIMLADGSIVTCSRELQKDMFAAAQVSLGALGVIVDITISVVPAFDLVATEDVTTVTDLFQDWKNNLIWESAEFVRVHVFPYANRAVVWRANKVEPNTVPHTPKPSLFRLKLDSFVYQCLLFVGKCVNRVTPYLERFWFKCHYGSKLGTALQVAGPGFDVLQMFCYFSQHVSEWGIPLESAPDALEKLINYTVDDAGKIGAYTHWPIEVRVCAPTPEDECWLSTDCKVPTCYIEAIMYRPFSTSINYKPYFKALEDIANQYNGKPHWAKEYSLTKEQLLERYPNLSKWLSLRKLLDPKGVFWNDYLQRHLG
```

### Thinking Trace
The architecture begins with IPR010031 (L-gulonolactone/D-arabinono-1,4-lactone oxidase-like family, residues 7–460) and IPR030654 (Sugar 1,4-lactone oxidase family, residues 14–454), establishing a two-lobed oxidase specialized for carbohydrate-derived 1,4-lactone substrates. The N-terminal half is densely annotated with FAD-binding modules: IPR036318 (FAD-binding, type PCMH-like superfamily, residues 10–193), IPR016167 (PCMH subdomain 1, residues 11–80), IPR016166 (PCMH-type FAD-binding domain, residues 24–194), and IPR006094 (FAD-linked oxidase, N-terminal domain, residues 32–163). Together, these define a canonical PCMH-type Rossmann-like fold that clamps a noncovalently bound FAD cofactor and positions it for hydride transfer. The C-terminal half is specified by IPR007173 (D-arabinono-1,4-lactone oxidase, C-terminal domain, residues 187–459) and capped by IPR016171 (Vanillyl-alcohol oxidase, C-terminal subdomain 2, residues 425–461), which in this enzyme class forms the substrate-recognition and catalytic scaffold that completes the active-site pocket and mediates oxygen activation. The ordered arrangement—an N-terminal FAD-binding core followed by a tailored C-terminal oxidase lobe—causes FAD-dependent two-electron oxidation of sugar 1,4-lactones and their reduction by molecular oxygen.

From this fold logic, the molecular function resolves to an FAD-dependent oxidase. The PCMH-type FAD-binding ensemble dictates FAD interaction and redox chemistry; thus the enzyme exhibits GO:0016491 oxidoreductase activity and binds FAD (GO:0050660 FAD binding). The chemistry of the sugar 1,4-lactone oxidase families channels electrons from substrate to O2, producing H2O2 and driving downstream pathways.

Biologically, oxidation of D-arabinono-1,4-lactone and related pentose/hexose lactones feeds carbohydrate-derived routes that intersect with vitamin C and nucleotide salvage chemistry. By funneling carbohydrate lactone intermediates into oxidase-mediated steps, the enzyme advances GO:0055114 oxidation-reduction process and contributes to GO:0005975 carbohydrate metabolic process, coupling redox flow to sugar economy in fission yeast.

Cellular placement follows the soluble, non-membranous architecture: there are no transmembrane segments or signal peptides in this two-domain soluble oxidase, which supports a cytosolic residency consistent with metabolic redox hubs. Therefore, the enzyme resides in the GO:0005737 cytoplasm, where carbohydrate and nucleotide metabolism converge.

Mechanistically, the N-terminal PCMH-type FAD core accepts a hydride from the sugar 1,4-lactone to form FADH2, while the C-terminal oxidase lobe coordinates O2 reduction to H2O2. This arrangement suggests transient assemblies with cytosolic partners that manage redox and peroxide: catalase to decompose H2O2, FAD biosynthesis machinery to maintain the flavin cofactor, and cytosolic carbohydrate-metabolism enzymes that supply or consume lactone intermediates. Such interactions would stabilize flux through lactone-linked carbohydrate pathways and tune redox balance in the cytoplasm.

### Functional Summary
A cytosolic FAD-dependent oxidase in fission yeast that converts carbohydrate 1,4-lactones through oxygen-dependent reactions, generating hydrogen peroxide and channeling sugar-derived intermediates into broader carbohydrate and vitamin C–related routes. Its N-terminal flavin-binding core and C-terminal oxidase lobe cooperate to accept electrons from lactone substrates and reduce oxygen, thereby supporting cytoplasmic redox balance and carbohydrate metabolism through soluble, non-membranous assemblies.

### UniProt Summary
Probable oxidase.

### InterPro Domains
- **L-gulonolactone/D-arabinono-1,4-lactone oxidase-like** (`IPR010031`, family) — residues 7-460
- **FAD-binding, type PCMH-like superfamily** (`IPR036318`, homologous_superfamily) — residues 10-193
- **FAD-binding, type PCMH, subdomain 1** (`IPR016167`, homologous_superfamily) — residues 11-80
- **Sugar 1,4-lactone oxidase** (`IPR030654`, family) — residues 14-454
- **FAD-binding domain, PCMH-type** (`IPR016166`, domain) — residues 24-194
- **FAD linked oxidase, N-terminal** (`IPR006094`, domain) — residues 32-163
- **FAD-binding, type PCMH, subdomain 2** (`IPR016169`, homologous_superfamily) — residues 82-207
- **D-arabinono-1,4-lactone oxidase, C-terminal domain** (`IPR007173`, domain) — residues 187-459
- **Vanillyl-alcohol oxidase, C-terminal subdomain 2** (`IPR016171`, homologous_superfamily) — residues 425-461

### GO Terms
**Molecular Function:** molecular_function (`GO:0003674`), catalytic activity (`GO:0003824`), oxidoreductase activity (`GO:0016491`), oxidoreductase activity, acting on CH-OH group of donors (`GO:0016614`), oxidoreductase activity, acting on the CH-OH group of donors, oxygen as acceptor (`GO:0016899`)

**Biological Process:** biological_process (`GO:0008150`), metabolic process (`GO:0008152`), cellular process (`GO:0009987`), biosynthetic process (`GO:0009058`), cellular metabolic process (`GO:0044237`), small molecule metabolic process (`GO:0044281`), organic substance metabolic process (`GO:0071704`), primary metabolic process (`GO:0044238`), organic cyclic compound metabolic process (`GO:1901360`), organic substance biosynthetic process (`GO:1901576`), small molecule biosynthetic process (`GO:0044283`), heterocycle metabolic process (`GO:0046483`), organic acid metabolic process (`GO:0006082`), cellular biosynthetic process (`GO:0044249`), monosaccharide metabolic process (`GO:0005996`), carbohydrate metabolic process (`GO:0005975`), vitamin metabolic process (`GO:0006766`), lactone metabolic process (`GO:1901334`), organic cyclic compound biosynthetic process (`GO:1901362`), water-soluble vitamin metabolic process (`GO:0006767`), vitamin biosynthetic process (`GO:0009110`), monosaccharide biosynthetic process (`GO:0046364`), oxoacid metabolic process (`GO:0043436`), organic acid biosynthetic process (`GO:0016053`), heterocycle biosynthetic process (`GO:0018130`), carbohydrate biosynthetic process (`GO:0016051`), L-ascorbic acid metabolic process (`GO:0019852`), carboxylic acid metabolic process (`GO:0019752`), water-soluble vitamin biosynthetic process (`GO:0042364`), lactone biosynthetic process (`GO:1901336`), L-ascorbic acid biosynthetic process (`GO:0019853`), carboxylic acid biosynthetic process (`GO:0046394`)

**Cellular Component:** cellular_component (`GO:0005575`), cellular anatomical entity (`GO:0110165`), intracellular anatomical structure (`GO:0005622`), organelle (`GO:0043226`), cytoplasm (`GO:0005737`), intracellular organelle (`GO:0043229`), mitochondrion (`GO:0005739`), membrane-bounded organelle (`GO:0043227`), intracellular membrane-bounded organelle (`GO:0043231`)

---
*Generated by [BioReason](https://bioreason.net)*
