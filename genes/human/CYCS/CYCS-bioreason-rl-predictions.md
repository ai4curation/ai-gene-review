# BioReason Chat Export
*Exported on March 22, 2026 at 01:45 AM*

---

**Organism:** Homo sapiens

**Sequence:**
```
MGDVEKGKKIFIMKCSQCHTVEKGGKHKTGPNLHGLFGRKTGQAPGYSYTAANKNKGIIWGEDTLMEYLENPKKYIPGTKMIFVGIKKKEERADLIAYLKKATNE
```

### Thinking Trace
I begin by dissecting the InterPro architecture. The sequence is dominated by IPR036909 (Cytochrome c-like domain superfamily, residues 1–105), which frames the entire polypeptide within the canonical cytochrome c fold—a compact β-sandwich that positions a covalently attached heme c for rapid one-electron transfer. Nested within this scaffold, IPR002327 (Cytochrome c, class IA/IB family, residues 2–103) specifies the class I/II cytochrome c lineage that employs the CXXCH motif for heme attachment and creates a positively charged surface for transient docking to redox partners. IPR009056 (Cytochrome c-like domain, residues 2–103) further resolves the core electron-transfer domain, reinforcing that the central structural module is optimized for reversible Fe3+/Fe2+ transitions and fast outer-sphere electron exchange. The ordered architecture—superfamily envelope (1–105) containing a class I/IB core (2–103) and a cytochrome c-like domain (2–103)—causally dictates a heme-based electron shuttle with high-potential, low-spin chemistry and precise electrostatic steering of partner interactions.

From this architecture, the molecular function resolves as electron transfer mediated by a c-type heme. The class IA/IB signature and cytochrome c-like fold necessitate GO:0009055 electron carrier activity: the heme c center accepts and donates single electrons, and the surface electrostatics and axial ligation geometry enforce rapid, reversible exchange without intrinsic catalysis.

This electron-shuttle role slots directly into the mitochondrial electron transport chain. By transiently accepting an electron from cytochrome b6 in complex III and delivering it to cytochrome a in complex IV, the protein drives the broader pathway that reduces oxygen and supports proton motive force generation. Thus, its activity advances the biological process formalized as mitochondrial electron transport, and more generally oxidative phosphorylation, by coupling electron flow to downstream oxidative steps.

Cellular placement follows from both fold-function logic and explicit localization cues. Cytochrome c-like proteins are soluble and lack transmembrane segments; they operate within aqueous compartments adjacent to respiratory complexes. The InterPro-defined soluble architecture supports a matrix-facing soluble pool. The stated subcellular distribution—matrix, intermembrane space, and cristae—maps onto a shuttle that diffuses within the mitochondrial intermembrane space while residing predominantly in the mitochondrial matrix pool. The presence in cristae-associated regions is consistent with proximity to complexes III and IV. Therefore, I assign localization to the mitochondrion, with enrichment in the mitochondrial matrix and functional residence consistent with the intermembrane space interface.

Mechanistically, the heme c domain binds a covalently attached c-type heme that cycles between redox states while the protein’s basic surface guides encounters with cytochrome b6f and cytochrome c oxidase. I hypothesize transient assemblies with complex III and IV components to funnel electrons efficiently. Additional matrix-associated interactions with soluble chaperones and redox-balancing factors likely stabilize the shuttle and buffer reactive oxygen chemistry.

### Functional Summary
A soluble mitochondrial redox shuttle that carries a covalently bound heme cofactor to transfer single electrons between respiratory complexes. It cycles between reduced and oxidized states to pass electrons from the cytochrome b6f complex toward cytochrome a of cytochrome c oxidase, thereby sustaining the electron transport chain that underpins oxidative phosphorylation. It resides predominantly in the mitochondrial matrix with functional availability in the intermembrane space and is enriched within cristae, where it engages respiratory assemblies through electrostatically guided encounters.

### UniProt Summary
Electron carrier protist between cytochrome b6 and cytochrome a.

### InterPro Domains
- **Cytochrome c-like domain superfamily** (`IPR036909`, homologous_superfamily) — residues 1-105
- **Cytochrome c, class IA/ IB** (`IPR002327`, family) — residues 2-103
- **Cytochrome c-like domain** (`IPR009056`, domain) — residues 2-103

### GO Terms
**Molecular Function:** molecular_function (`GO:0003674`), binding (`GO:0005488`), organic cyclic compound binding (`GO:0097159`), heterocyclic compound binding (`GO:1901363`), protein binding (`GO:0005515`), tetrapyrrole binding (`GO:0046906`), heme binding (`GO:0020037`)

**Biological Process:** biological_process (`GO:0008150`), metabolic process (`GO:0008152`), biological regulation (`GO:0065007`), positive regulation of biological process (`GO:0048518`), regulation of biological process (`GO:0050789`), cellular process (`GO:0009987`), cellular metabolic process (`GO:0044237`), regulation of metabolic process (`GO:0019222`), nitrogen compound metabolic process (`GO:0006807`), positive regulation of metabolic process (`GO:0009893`), regulation of molecular function (`GO:0065009`), organic substance metabolic process (`GO:0071704`), primary metabolic process (`GO:0044238`), regulation of catalytic activity (`GO:0050790`), positive regulation of molecular function (`GO:0044093`), organonitrogen compound metabolic process (`GO:1901564`), positive regulation of macromolecule metabolic process (`GO:0010604`), protein metabolic process (`GO:0019538`), regulation of nitrogen compound metabolic process (`GO:0051171`), regulation of macromolecule metabolic process (`GO:0060255`), regulation of primary metabolic process (`GO:0080090`), macromolecule metabolic process (`GO:0043170`), generation of precursor metabolites and energy (`GO:0006091`), positive regulation of nitrogen compound metabolic process (`GO:0051173`), proteolysis (`GO:0006508`), regulation of protein metabolic process (`GO:0051246`), regulation of hydrolase activity (`GO:0051336`), positive regulation of protein metabolic process (`GO:0051247`), protein maturation (`GO:0051604`), positive regulation of catalytic activity (`GO:0043085`), energy derivation by oxidation of organic compounds (`GO:0015980`), gene expression (`GO:0010467`), cellular respiration (`GO:0045333`), positive regulation of proteolysis (`GO:0045862`), regulation of proteolysis (`GO:0030162`), protein processing (`GO:0016485`), positive regulation of hydrolase activity (`GO:0051345`), regulation of peptidase activity (`GO:0052547`), zymogen activation (`GO:0031638`), positive regulation of peptidase activity (`GO:0010952`), regulation of endopeptidase activity (`GO:0052548`), activation of cysteine-type endopeptidase activity (`GO:0097202`), positive regulation of endopeptidase activity (`GO:0010950`), regulation of cysteine-type endopeptidase activity (`GO:2000116`), positive regulation of cysteine-type endopeptidase activity (`GO:2001056`), regulation of cysteine-type endopeptidase activity involved in apoptotic process (`GO:0043281`), positive regulation of cysteine-type endopeptidase activity involved in apoptotic process (`GO:0043280`), activation of cysteine-type endopeptidase activity involved in apoptotic process (`GO:0006919`)

**Cellular Component:** cellular_component (`GO:0005575`), protein-containing complex (`GO:0032991`), cellular anatomical entity (`GO:0110165`), intracellular anatomical structure (`GO:0005622`), organelle (`GO:0043226`), envelope (`GO:0031975`), membrane (`GO:0016020`), cytosol (`GO:0005829`), cytoplasm (`GO:0005737`), membrane-enclosed lumen (`GO:0031974`), organelle membrane (`GO:0031090`), organelle envelope (`GO:0031967`), mitochondrion (`GO:0005739`), organelle lumen (`GO:0043233`), intracellular organelle (`GO:0043229`), membrane-bounded organelle (`GO:0043227`), mitochondrial envelope (`GO:0005740`), organelle inner membrane (`GO:0019866`), intracellular membrane-bounded organelle (`GO:0043231`), organelle envelope lumen (`GO:0031970`), intracellular organelle lumen (`GO:0070013`), mitochondrial membrane (`GO:0031966`), mitochondrial intermembrane space (`GO:0005758`), mitochondrial inner membrane (`GO:0005743`), nucleus (`GO:0005634`)

---
*Generated by [BioReason](https://bioreason.net)*
