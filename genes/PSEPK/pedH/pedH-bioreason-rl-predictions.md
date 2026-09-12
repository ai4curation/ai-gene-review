# BioReason Chat Export
*Exported on March 22, 2026 at 02:59 AM*

---

**Organism:** Pseudomonas putida

**Sequence:**
```
MTRSPRRPLFAVSLVLSAMLLAGAAHAAVSNEEILQDPKNPQQIVTNGLGVQGQRYSPLDLLNVNNVKELRPVWAFSFGGEKQRGQQAQPLIKDGVMYLTGSYSRVFAVDARTGKKLWQYDARLPDDIRPCCDVINRGVALYGNLVFFGTLDAKLVALNKDTGKVVWSKKVADHKEGYSISAAPMIVNGKLITGVAGGEFGVVGKIQAYNPENGELLWMRPTVEGHMGYVYKDGKAIENGISGGEAGKTWPGDLWKTGGAAPWLGGYYDPETNLILFGTGNPAPWNSHLRPGDNLYSSSRLALNPDDGTIKWHFQSTPHDGWDFDGVNELISFNYKDGGKEVKAAATADRNGFFYVLDRTNGKFIRGFPFVDKITWATGLDKDGRPIYNDASRPGAPGSEAKGSSVFVAPAFLGAKNWMPMAYNKDTGLFYVPSNEWGMDIWNEGIAYKKGAAFLGAGFTIKPLNEDYIGVLRAIDPVSGKEVWRHKNYAPLWGGVLTTKGNLVFTGTPEGFLQAFNAKTGDKVWEFQTGSGVLGSPVTWEMDGEQYVSVVSGWGGAVPLWGGEVAKRVKDFNQGGMLWTFKLPKQLQQTASVKP
```

### Thinking Trace
I begin with the InterPro architecture. The sequence is dominated by PQQ-dependent dehydrogenase signatures: IPR017512 (PQQ-dependent dehydrogenase, methanol/ethanol family, residues 26–556) and IPR034119 (PQQ-dependent type I alcohol dehydrogenase, residues 34–583) define a soluble, type I quinoprotein alcohol dehydrogenase fold that catalyzes primary alcohol oxidation via a noncovalently bound pyrroloquinoline quinone cofactor. This scaffold is reinforced by IPR011047 (Quinoprotein alcohol dehydrogenase-like superfamily, residues 37–579), indicating a β-propeller architecture that supports redox chemistry. The core repeat framework is specified by IPR002372 (Pyrrolo-quinoline quinone repeat domain, residues 52–538) and IPR018391 (Pyrrolo-quinoline quinone beta-propeller repeat, residues 90–528), which together predict a six-bladed β-propeller that forms the catalytic cavity and cofactor pocket. A catalytic locus is pinpointed by IPR001479 (Quinoprotein dehydrogenase, conserved site, residues 263–284), marking residues that coordinate PQQ and the catalytic base/acid pair. The ordered layout—PQQ-binding repeats forming a propeller, capped by a conserved catalytic site—causally establishes an obligate PQQ-mediated alcohol dehydrogenase chemistry.

From this architecture, the molecular function follows. PQQ-dependent type I dehydrogenases use the PQQ cofactor to abstract hydride equivalents from primary and secondary alcohols and channel electrons to external acceptors. The methanol/ethanol family annotation and β-propeller repeats dictate oxidation of CH–OH groups rather than reduction, and the conserved-site placement matches enzymes that transfer electrons to cytochromes or quinones. This directly supports GO:0004098 alcohol dehydrogenase (NAD) activity as the formal label for alcohol oxidation chemistry, while the quinoprotein nature explains why the enzyme can operate with diverse physiological electron acceptors.

Biological process emerges from coupling this redox activity to cellular metabolism. Oxidation of short-chain alcohols supplies entry points into central carbon pathways and supports anaerobic or microaerophilic energy conservation in soil bacteria. Thus, the enzyme drives GO:0006066 alcohol metabolic process by converting environmental or endogenous alcohols to aldehydes that feed downstream metabolism and respiratory chains.

Cellular component is inferred from the soluble quinoprotein architecture. The absence of transmembrane segments and the soluble β-propeller fold indicate a cytosolic enzyme. Therefore, the most parsimonious localization is the cytoplasm (GO:0005737 cytoplasm), where both PQQ loading and soluble electron-acceptor partners are readily available in bacteria.

These features suggest a mechanism and interaction landscape. The β-propeller with the IPR001479 conserved site binds PQQ, forming a redox-active pocket that oxidizes long-chain and short-chain primary/secondary alcohols. Electrons flow from substrate to PQQ and then to physiological acceptors. In Pseudomonas-lineage systems, plausible acceptors include soluble cytochromes and periplasm-linked redox modules via cytoplasmic-to-periplasm electron flow through periplasmic cytochromes and carriers. I therefore hypothesize transient interactions with soluble cytochrome c-like proteins and with quinone-linked respiratory components, as well as assembly with PQQ biogenesis/loading machinery to maintain the cofactor state. Together, these contacts position the enzyme as a cytosolic redox hub that initiates alcohol utilization and supports energy metabolism.

### Functional Summary
A soluble quinoprotein alcohol dehydrogenase that uses a PQQ-cofactor β‑propeller to oxidize long‑chain and short‑chain primary and secondary alcohols to aldehydes, initiating their assimilation into central metabolism and supporting energy conservation pathways. Its soluble architecture and catalytic site coordinate PQQ chemistry to transfer electrons to physiological acceptors, situating the enzyme in cytoplasmic redox networks that couple alcohol utilization to broader metabolic processes.

### UniProt Summary
Catalyzes the oxidation of different types of alcohol.

### InterPro Domains
- **PQQ-dependent dehydrogenase, methanol/ethanol family** (`IPR017512`, family) — residues 26-556
- **PQQ-dependent type I alcohol dehydrogenase** (`IPR034119`, family) — residues 34-583
- **Quinoprotein alcohol dehydrogenase-like superfamily** (`IPR011047`, homologous_superfamily) — residues 37-579
- **Pyrrolo-quinoline quinone repeat domain** (`IPR002372`, domain) — residues 52-538
- **Pyrrolo-quinoline quinone beta-propeller repeat** (`IPR018391`, repeat) — residues 90-528
- **Quinoprotein dehydrogenase, conserved site** (`IPR001479`, conserved_site) — residues 263-284

### GO Terms
**Molecular Function:** molecular_function (`GO:0003674`), binding (`GO:0005488`), catalytic activity (`GO:0003824`), small molecule binding (`GO:0036094`), heterocyclic compound binding (`GO:1901363`), quinone binding (`GO:0048038`), organic cyclic compound binding (`GO:0097159`), ion binding (`GO:0043167`), oxidoreductase activity (`GO:0016491`), electron transfer activity (`GO:0009055`), tetrapyrrole binding (`GO:0046906`), organic acid binding (`GO:0043177`), anion binding (`GO:0043168`), cation binding (`GO:0043169`), heme binding (`GO:0020037`), carboxylic acid binding (`GO:0031406`), metal ion binding (`GO:0046872`), calcium ion binding (`GO:0005509`)

**Biological Process:** biological_process (`GO:0008150`), metabolic process (`GO:0008152`), cellular process (`GO:0009987`), small molecule metabolic process (`GO:0044281`), cellular metabolic process (`GO:0044237`), organic substance metabolic process (`GO:0071704`), organic hydroxy compound metabolic process (`GO:1901615`), organic acid metabolic process (`GO:0006082`), oxoacid metabolic process (`GO:0043436`), carboxylic acid metabolic process (`GO:0019752`), monocarboxylic acid metabolic process (`GO:0032787`)

**Cellular Component:** cellular_component (`GO:0005575`), cellular anatomical entity (`GO:0110165`), protein-containing complex (`GO:0032991`), catalytic complex (`GO:1902494`), intracellular anatomical structure (`GO:0005622`), organelle (`GO:0043226`), intracellular organelle (`GO:0043229`), oxidoreductase complex (`GO:1990204`), non-membrane-bounded organelle (`GO:0043228`), intracellular non-membrane-bounded organelle (`GO:0043232`), thylakoid (`GO:0009579`)

---
*Generated by [BioReason](https://bioreason.net)*
