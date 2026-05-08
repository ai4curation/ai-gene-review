# BioReason Chat Export
*Exported on March 22, 2026 at 12:51 AM*

---

**Organism:** Schizosaccharomyces pombe

**Sequence:**
```
MKYVLVSGGVISGIGKGVIASSTGLLLKTLGLKVTSIKIDPYMNIDAGTMSPLEHGEVFVLNDGGEVDLDLGNYERYLNVTLTHDNNITTGKVYSNVIQKERRGDYLGKTVQIVPHVTNEIQDWVERVARIPVDQSGEEPDVCIVELGGTVGDIESAAFVEAMRQFQFRVGHENFVSIHVSLVPVINGEQKTKPTQQAIRDLRSLGITPDLIACRCKQPLEKSVIDKISLFCHVGPEQVLAVHDVSSTYHVPQLLEDKLLEYLKIRFALDKISVSRELALAGENMWSSWKHLTQGYDHLFKKVTIVLVGKYTHLQDSYISVIKALEHSAMRCGRKLDLQWVEASHLEASTNTSDPLSYHKAWHLVCSANGILVPGGFGSRGVEGMIAAAKWARENNTPYLGICLGMQVAVIEFARSVCGIEGAFSEEFDKECENNVVVYMPEIDKDKLGGTMRLGLRPTFFQPNSEWSKLRKLHKMVDEVLERHRHRYEINPAFVSRLEQGGISFIGKDERGERMEIIEKRDHPYFVGVQYHPEYLSKPLKPSPPIFGLVAASAGLLDEFIQSGEEVEWSNFSHFNAESALADMNDSVEVTEEATVVTIS
```

### Thinking Trace
I begin with the InterPro architecture. The sequence is covered end-to-end by IPR004468 (CTP synthase family, residues 1–562), establishing the enzyme class and overall fold. The N-terminus is defined by IPR027417 (P-loop containing nucleoside triphosphate hydrolase homologous superfamily, residues 1–295) and IPR017456 (CTP synthase, N-terminal domain, residues 2–263). This N-terminal module forms the ATP-dependent “synthetase” core that activates UTP via a phosphoryl transfer cycle and binds ATP and other nucleotides. The C-terminal half is specified by IPR029062 (Class I glutamine amidotransferase-like homologous superfamily, residues 299–567), IPR033828 (CTP synthase GATase domain, residues 303–550), and IPR017926 (Glutamine amidotransferase domain, residues 314–544). This composite amidotransferase module generates ammonia from glutamine and delivers it intramolecularly to the activated UTP intermediate. The ordered layout—N-terminal ATP-utilizing synthetase followed by a C-terminal class I glutamine amidotransferase—creates a bifunctional enzyme that couples ATP hydrolysis to nitrogen transfer, a hallmark of CTP synthases.

This domain architecture dictates molecular function. The N-terminal P-loop/synthetase region binds and hydrolyzes ATP to form a UTP-adenylate intermediate, while the C-terminal glutamine amidotransferase domain supplies ammonia from glutamine; together they cause the amination and isomerization chemistry that defines CTP synthase activity. Thus, the enzyme’s molecular function aligns with GO:0003889 CTP synthase activity.

From this chemistry, the biological process follows directly. By converting UTP to CTP using glutamine-derived nitrogen and ATP energy, the enzyme sets the cellular CTP pool that feeds RNA synthesis and the CDP-/CTP-dependent steps of phospholipid biosynthesis. Therefore, the activity drives pyrimidine nucleotide biosynthesis and balances the nucleotide economy, supporting GO:0006220 pyrimidine nucleotide biosynthetic process.

Cellular location is inferred from solubility and assembly behavior typical of this architecture. The absence of transmembrane segments and the soluble, oligomerization-prone N- and C-terminal domains indicate a cytosolic enzyme that assembles higher-order complexes in the soluble compartment. This supports a cytoplasmic localization consistent with GO:0005737 cytoplasm.

Mechanistically, the N-terminal synthetase binds ATP and UTP, forming a transient phosphoenzyme intermediate that primes UTP. The C-terminal glutamine amidotransferase hydrolyzes glutamine to ammonia and glutamate; intramolecular tunneling then channels ammonia to the activated intermediate, completing CTP formation. Allosteric regulation is expected: cytosolic nucleotide and amino acid levels modulate activity, and filamentation/oligomerization likely tunes flux. Given its role and location, plausible interaction partners include cytosolic nucleotide-metabolic enzymes and pathway neighbors such as UTP-producing enzymes and downstream CTP-utilizing assemblies, as well as self-association into higher-order cytoplasmic complexes that coordinate pyrimidine biosynthesis with cellular demand.

### Functional Summary
A cytoplasmic enzyme that converts UTP to CTP using ATP energy and glutamine-derived nitrogen. Its N-terminal synthetase core activates UTP and uses ATP, while a C-terminal glutamine amidotransferase module generates and channels ammonia to complete CTP formation. By sustaining the cellular CTP pool, it supports RNA and membrane lipid precursor pathways and adjusts metabolic flux through soluble, oligomerization-prone assemblies in the cytoplasm.

### UniProt Summary
Catalyzes the ATP-dependent amination of UTP to CTP with glutamine as an nitrogen source.

### InterPro Domains
- **CTP synthase** (`IPR004468`, family) — residues 1-562
- **P-loop containing nucleoside triphosphate hydrolase** (`IPR027417`, homologous_superfamily) — residues 1-295
- **CTP synthase, N-terminal** (`IPR017456`, domain) — residues 2-263
- **Class I glutamine amidotransferase-like** (`IPR029062`, homologous_superfamily) — residues 299-567
- **CTP synthase GATase domain** (`IPR033828`, domain) — residues 303-550
- **Glutamine amidotransferase** (`IPR017926`, domain) — residues 314-544

### GO Terms
**Molecular Function:** molecular_function (`GO:0003674`), catalytic activity (`GO:0003824`), ligase activity (`GO:0016874`), ligase activity, forming carbon-nitrogen bonds (`GO:0016879`)

**Biological Process:** biological_process (`GO:0008150`), metabolic process (`GO:0008152`), cellular process (`GO:0009987`), biosynthetic process (`GO:0009058`), cellular metabolic process (`GO:0044237`), small molecule metabolic process (`GO:0044281`), nitrogen compound metabolic process (`GO:0006807`), organic substance metabolic process (`GO:0071704`), primary metabolic process (`GO:0044238`), organic cyclic compound metabolic process (`GO:1901360`), organonitrogen compound metabolic process (`GO:1901564`), organic substance biosynthetic process (`GO:1901576`), nucleobase-containing compound metabolic process (`GO:0006139`), heterocycle metabolic process (`GO:0046483`), nucleobase-containing small molecule metabolic process (`GO:0055086`), organophosphate metabolic process (`GO:0019637`), cellular biosynthetic process (`GO:0044249`), cellular nitrogen compound metabolic process (`GO:0034641`), cellular aromatic compound metabolic process (`GO:0006725`), carbohydrate derivative metabolic process (`GO:1901135`), phosphorus metabolic process (`GO:0006793`), organonitrogen compound biosynthetic process (`GO:1901566`), organic cyclic compound biosynthetic process (`GO:1901362`), nucleoside phosphate metabolic process (`GO:0006753`), ribose phosphate metabolic process (`GO:0019693`), heterocycle biosynthetic process (`GO:0018130`), aromatic compound biosynthetic process (`GO:0019438`), organophosphate biosynthetic process (`GO:0090407`), cellular nitrogen compound biosynthetic process (`GO:0044271`), phosphate-containing compound metabolic process (`GO:0006796`), carbohydrate derivative biosynthetic process (`GO:1901137`), pyrimidine-containing compound metabolic process (`GO:0072527`), nucleobase-containing compound biosynthetic process (`GO:0034654`), ribonucleotide metabolic process (`GO:0009259`), nucleoside triphosphate metabolic process (`GO:0009141`), pyrimidine-containing compound biosynthetic process (`GO:0072528`), pyrimidine nucleotide biosynthetic process (`GO:0006220`), nucleotide metabolic process (`GO:0009117`), ribose phosphate biosynthetic process (`GO:0046390`), nucleoside phosphate biosynthetic process (`GO:1901293`), nucleoside triphosphate biosynthetic process (`GO:0009142`), nucleotide biosynthetic process (`GO:0009165`), ribonucleotide biosynthetic process (`GO:0009260`), pyrimidine nucleotide biosynthetic process (`GO:0006221`), ribonucleoside triphosphate metabolic process (`GO:0009199`), pyrimidine nucleoside triphosphate metabolic process (`GO:0009147`), pyrimidine ribonucleotide metabolic process (`GO:0009218`), ribonucleoside triphosphate biosynthetic process (`GO:0009201`), pyrimidine ribonucleotide biosynthetic process (`GO:0009220`), pyrimidine ribonucleoside triphosphate metabolic process (`GO:0009208`), pyrimidine nucleoside triphosphate biosynthetic process (`GO:0009148`)

**Cellular Component:** cellular_component (`GO:0005575`), cellular anatomical entity (`GO:0110165`), intracellular anatomical structure (`GO:0005622`), cytoplasm (`GO:0005737`), supramolecular complex (`GO:0099080`), supramolecular polymer (`GO:0099081`), supramolecular fiber (`GO:0099512`)

---
*Generated by [BioReason](https://bioreason.net)*
