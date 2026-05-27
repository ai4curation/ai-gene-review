# BioReason Chat Export
*Exported on March 22, 2026 at 12:33 AM*

---

**Organism:** Schizosaccharomyces pombe

**Sequence:**
```
MPRLNTQLPRMYSAPPGHSKAVSTELNKDLSSVGGRSAKLGQVIHHCFYKTGLIILESRLNVFGTSRPRESSKNNKWFNLEIVETELYAEQFKIWKNIELSPSRKIPPMVLHTYLDISDLSKNQTLSVSDGTHSHAINFNNMSTMKIVLERWIVNLDGEALSTPLELAVLYKKLVVLFRSLYTYTHLMPLWKLKSKIHKLRAHGTSLKVGCALSTDDVLSNDFLPISAPISSSLGSSIATFSFSPVGTPAGDFRISVQYRKNCHFEVHDSDALLSNQLLSADKHQLAASNNSQDFEDGKQYDQPPPSFATRLAKQSDPNSLLQSEIQHLASIESITAQAAPLVTIHPFKSPSLSASPGSNFDNMSISPKVAVNRYIHRGPSATSLNKFSMISDAASKSRAKLPPLTSGSLKLNTLDISNTPNLRRFSSSFGPRERKESFSSRNRLPLVNHPIRSIFKHNVSENPITDHSEHAVYDSEFASKDDLSGFIQLLDSHAHHLNASEGSKSSGSFPGKVQTLTSGISPVAHPHNSLGSSNEIFDIDTYNHSIDNSGSRFTEAVKHNLGNSSHSIMRHHTLGTLRSRPSFSEKSTFPAPLTSISQASTFQGDNRSPSTVIPHTQTEVPSANDTSKQLASLHDMRKSQSPICARSATSAGLPRFEYHTSLSKSLEHSSTPASLQATKTPSPSFVLEPGIPQEYKKHFDNLSEERRQCLTPSTPTYEYYNEHNPNYDDDLLFTMTDMTLEPHDVSAIRLGSPKSDD
```

### Thinking Trace
I begin with the InterPro architecture. The N-terminal half contains IPR036570 (HORMA domain superfamily, residues 30–269) and a more specific N-terminal module IPR018731 (Autophagy-related protein 13, N-terminal domain, residues 44–265). This tandem arrangement creates a structured HORMA-like fold that typically mediates regulated conformational switching and avid protein–protein interactions rather than catalysis. Encompassing almost the entire polypeptide is IPR040182 (Autophagy-related protein 13 family, residues 34–675), which anchors the sequence within the autophagy initiation machinery. The ordered layout—an interaction-centric HORMA-like core at the N-terminus feeding into an extended autophagy-scaffold body—causally dictates a molecular role dominated by multivalent binding and complex assembly.

This domain architecture enforces a molecular function centered on protein binding (GO:0005515). The HORMA superfamily fold is a hallmark of conformationally dynamic adaptors that recruit and coordinate partner proteins; the explicit N-terminal autophagy-specific domain further biases this scaffold toward assembling initiation complexes. The absence of enzymatic signatures and the prevalence of interaction modules argue that binding and assembly are primary activities.

From this binding-centric foundation, the biological process follows. Placement in the autophagy-initiation apparatus is signaled by the autophagy-related family signature and by the known systems-level role of such scaffolds in forming the pre-autophagosomal structure. The HORMA-like module provides a switchable hub that nucleates autophagy initiation complexes, which mechanistically drives macroautophagy (GO:0016236). The architecture naturally supports autophagosome biogenesis by stabilizing and timing the assembly of upstream factors that seed the isolation membrane.

Cellular localization is inferred from where such assemblies operate. Autophagy initiation occurs at cytoplasmic sites that often coalesce near the nucleus and endomembrane interfaces. The soluble, scaffold-like architecture without transmembrane features supports a cytoplasmic residence, aligning with a cytoplasm localization (GO:0005737) and the stated subcellular location.

Mechanistically, I hypothesize that the N-terminal HORMA-like core nucleates higher-order assemblies that recruit early autophagy factors, while the extended family-specific body provides additional docking surfaces and regulatory sites. Likely partners include the ULK/Atg1-Atg13 initiation module and its adaptors. Through multivalent binding, the protein times and positions the initiation complex, thereby gating autophagosome formation. I further hypothesize transient interactions with PI3K complex components that generate phosphoinositide platforms and with membrane-remodeling factors that execute vesicle biogenesis.

### Functional Summary
A cytoplasmic autophagy-initiation scaffold in fission yeast that uses an interaction-driven N-terminal core to assemble and regulate early autophagy machinery. By organizing and timing the formation of initiation complexes that precede autophagosome biogenesis, it coordinates cytoplasmic events of macroautophagy through multivalent protein binding and higher-order assembly rather than catalysis.

### UniProt Summary
Autophagy factor.

### InterPro Domains
- **HORMA domain superfamily** (`IPR036570`, homologous_superfamily) — residues 30-269
- **Autophagy-related protein 13** (`IPR040182`, family) — residues 34-675
- **Autophagy-related protein 13, N-terminal** (`IPR018731`, domain) — residues 44-265

### GO Terms
**Molecular Function:** molecular_function (`GO:0003674`), binding (`GO:0005488`), protein binding (`GO:0005515`)

**Biological Process:** biological_process (`GO:0008150`), metabolic process (`GO:0008152`), cellular process (`GO:0009987`), cellular component organization or biogenesis (`GO:0071840`), cellular metabolic process (`GO:0044237`), process utilizing autophagic mechanism (`GO:0061919`), catabolic process (`GO:0009056`), cellular component organization (`GO:0016043`), cellular catabolic process (`GO:0044248`), autophagy (`GO:0006914`), macroautophagy (`GO:0016236`), autophagy of mitochondrion (`GO:0000422`), organelle organization (`GO:0006996`), cellular component disassembly (`GO:0022411`), mitochondrion organization (`GO:0007005`), organelle disassembly (`GO:1903008`), mitochondrion disassembly (`GO:0061726`)

**Cellular Component:** cellular_component (`GO:0005575`), protein-containing complex (`GO:0032991`), cellular anatomical entity (`GO:0110165`), cytosol (`GO:0005829`), catalytic complex (`GO:1902494`), intracellular anatomical structure (`GO:0005622`), cytoplasm (`GO:0005737`), phagophore assembly site (`GO:0000407`), Atg1/ULK1 kinase complex (`GO:1990316`), transferase complex (`GO:1990234`), transferase complex, transferring phosphorus-containing groups (`GO:0061695`), protein kinase complex (`GO:1902911`), serine/threonine protein kinase complex (`GO:1902554`)

---
*Generated by [BioReason](https://bioreason.net)*
