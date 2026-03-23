# BioReason Chat Export
*Exported on March 22, 2026 at 01:21 AM*

---

**Organism:** Caenorhabditis elegans

**Sequence:**
```
MSEKLPPGTLCAVCDDIATGKHYSVASCNGCKTFFRRALVNNREFVCQGNKDCPVNKGVRCACRYCRLQKCLAVGMDKNSIQNDRDRIGYTKRKRRHDDNDMEGGVHHSEHIRDGSSGSPQMNDESPESMDMKDIKIDLNCLDPIADRLTTLENNFTLLLSRCADLHSYATLEDALNAPSRFMQPISCEWSDNVVLTNRDDKLPFWRQRLIALYIDWAKTFSTFRSLPYADKVAMVTNHASSFMIMCEAFRTPEHMKSDVVRKRPDLPNIVTSNSGSGCSRVSSVAGSLVSNGEDVHDDLTNLLHAACIQQSINKGIMFGENSSDDKILLNLPIREIKKEPLEVPSTEGMIQLPTEYGNLPADYASWIPQDYGHPTAGHEGKSDMHNFFEARDFCVGRPSSCNLNERSMKTVSMLESRNFQSPSANNSSLSGITPVLTMMIDLVMKPFRQLNFSTTEFALLQAIMFFDPDTEGLDSASQRNVVAEQKKLLAVLFRHLQKAYNPQAASERYASIILRMPSIRRAAAKKNESLQVLDMLQMHEINSLVKETSLGPRPSNVQQRMGIGGGAGGCLTFPSQED
```

### Thinking Trace
I begin by examining the InterPro architecture and its order along the polypeptide. The N-terminus houses IPR050274 (Nuclear hormone receptor family NR2 subfamily, residues 5–550) and IPR001723 (Nuclear hormone receptor family, residues 72–529), which together define a canonical nuclear receptor scaffold. Within this scaffold, residues 6–107 carry IPR013088 (Zinc finger, NHR/GATA-type homologous superfamily), and residues 8–83 contain IPR001628 (Zinc finger, nuclear hormone receptor-type), establishing the classical two-C4 zinc-finger DNA-binding domain (DBD). IPR049636 (Hepatocyte nuclear factor 4-like, DNA-binding domain, residues 11–86) refines this DBD as NR2-subfamily-specific, pointing to HNF4-like sequence recognition and dimerization behavior. Downstream, residues 164–553 form IPR000536 (Nuclear hormone receptor, ligand-binding domain), which constitutes the activation and dimerization core that senses small hydrophobic ligands and recruits co-regulators. This C-terminal region is encompassed by IPR035500 (Nuclear hormone receptor-like domain superfamily, residues 176–559), reinforcing the presence of an allosteric ligand-binding pocket and co-regulator interface. The ordered layout—N-terminal DBD (residues ~5–110) followed by an extended ligand-binding domain (residues ~164–553)—is diagnostic of nuclear receptors and dictates a transcription-regulatory mechanism.

This domain architecture causally establishes molecular function. The paired zinc fingers and HNF4-like DBD enforce high-affinity, sequence-specific DNA binding and receptor dimerization; this directly supports GO:0005515 molecular function as a DNA-associated regulator and justifies inferring GO:0003700 DNA-binding transcription factor activity. The ligand-binding domain (IPR000536) supplies an allosteric switch that toggles co-repressor versus co-activator recruitment, a hallmark of nuclear receptor activity that modulates transcription in response to small molecules.

From molecular function, the biological process follows. Nuclear receptors regulate RNA polymerase II-driven gene programs by assembling transcriptional complexes at target promoters and enhancers. The DBD-LBD tandem thus drives regulation of transcription, most parsimoniously captured as GO:0006355 regulation of transcription, DNA-templated. In metazoans such regulation frequently orchestrates metabolic and developmental pathways; in Caenorhabditis elegans, NR2-like receptors typically tune neuronal and metabolic gene sets via hormone- and metabolite-responsive circuits.

Cellular localization is dictated by the need to access chromatin and assemble transcriptional machinery. The presence of a DBD and LBD that function on genomic targets necessitates a nuclear residence, aligning with the annotated Subcellular Location and supporting GO:0005634 nucleus. The absence of transmembrane segments and the presence of nuclear receptor hallmarks further anchor this nuclear role.

Mechanistically, the protein likely binds DNA as a monomer or homodimer through its NR-type zinc fingers, with HNF4-like specificity guiding target-site selection. Ligand occupancy within the LBD reshapes helix 12 to form an activation surface that recruits co-regulators. I therefore hypothesize interactions with co-activators (e.g., CBP/p300-like HATs and Mediator subunits) and co-repressors (e.g., NCoR/SMRT-like factors), as well as potential homotypic partners in the NR2 subfamily. In C. elegans, such assemblies would position this receptor as a nuclear transcriptional regulator that senses endogenous metabolites to modulate gene expression programs in the nucleus.

### Functional Summary
A nuclear transcriptional regulator in Caenorhabditis elegans that uses a paired zinc-finger DNA-binding module and a ligand-responsive activation domain to control gene expression in the nucleus. By binding specific genomic sites and switching between co-repressor and co-activator states in response to small hydrophobic ligands, it assembles transcriptional complexes that fine-tune RNA polymerase II-driven programs linked to development and metabolism.

### UniProt Summary
Orphan nuclear receptor.

### InterPro Domains
- **Nuclear hormone receptor family NR2 subfamily** (`IPR050274`, family) — residues 5-550
- **Zinc finger, NHR/GATA-type** (`IPR013088`, homologous_superfamily) — residues 6-107
- **Zinc finger, nuclear hormone receptor-type** (`IPR001628`, domain) — residues 8-83
- **Hepatocyte nuclear factor 4-like, DNA-binding domain** (`IPR049636`, domain) — residues 11-86
- **Nuclear hormone receptor** (`IPR001723`, family) — residues 72-529
- **Nuclear hormone receptor, ligand-binding domain** (`IPR000536`, domain) — residues 164-553
- **Nuclear hormone receptor-like domain superfamily** (`IPR035500`, homologous_superfamily) — residues 176-559

### GO Terms
**Molecular Function:** molecular_function (`GO:0003674`), binding (`GO:0005488`), - GO:0003700 (`GO:0005515`)

**Biological Process:** biological_process (`GO:0008150`), biological regulation (`GO:0065007`), positive regulation of biological process (`GO:0048518`), regulation of biological process (`GO:0050789`), multicellular organismal process (`GO:0032501`), determination of adult lifespan (`GO:0008340`), positive regulation of cellular process (`GO:0048522`), regulation of metabolic process (`GO:0019222`), regulation of cellular process (`GO:0050794`), positive regulation of metabolic process (`GO:0009893`), positive regulation of macromolecule metabolic process (`GO:0010604`), positive regulation of cellular metabolic process (`GO:0031325`), regulation of biosynthetic process (`GO:0009889`), regulation of small molecule metabolic process (`GO:0062012`), regulation of nitrogen compound metabolic process (`GO:0051171`), regulation of macromolecule metabolic process (`GO:0060255`), regulation of cellular metabolic process (`GO:0031323`), regulation of primary metabolic process (`GO:0080090`), positive regulation of biosynthetic process (`GO:0009891`), positive regulation of nitrogen compound metabolic process (`GO:0051173`), positive regulation of macromolecule biosynthetic process (`GO:0010557`), positive regulation of nucleobase-containing compound metabolic process (`GO:0045935`), positive regulation of RNA metabolic process (`GO:0051254`), regulation of cellular ketone metabolic process (`GO:0010565`), regulation of macromolecule biosynthetic process (`GO:0010556`), regulation of cellular biosynthetic process (`GO:0031326`), regulation of nucleobase-containing compound metabolic process (`GO:0019219`), regulation of RNA metabolic process (`GO:0051252`), regulation of lipid metabolic process (`GO:0019216`), positive regulation of cellular biosynthetic process (`GO:0031328`), regulation of gene expression (`GO:0010468`), positive regulation of RNA biosynthetic process (`GO:1902680`), regulation of RNA biosynthetic process (`GO:2001141`), regulation of DNA-templated transcription (`GO:0006355`), regulation of fatty acid metabolic process (`GO:0019217`), regulation of transcription by RNA polymerase II (`GO:0006357`), positive regulation of DNA-templated transcription (`GO:0045893`), positive regulation of nucleic acid-templated transcription (`GO:1903508`), regulation of nucleic acid-templated transcription (`GO:1903506`), positive regulation of transcription by RNA polymerase II (`GO:0045944`)

**Cellular Component:** cellular_component (`GO:0005575`), cellular anatomical entity (`GO:0110165`), intracellular anatomical structure (`GO:0005622`), organelle (`GO:0043226`), intracellular organelle (`GO:0043229`), membrane-bounded organelle (`GO:0043227`), intracellular membrane-bounded organelle (`GO:0043231`), nucleus (`GO:0005634`)

---
*Generated by [BioReason](https://bioreason.net)*
