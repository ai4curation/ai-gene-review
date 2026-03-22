# BioReason Chat Export
*Exported on March 22, 2026 at 02:13 AM*

---

**Organism:** Drosophila melanogaster

**Sequence:**
```
MIVKISWPKNNITSECFRRFGSFKRRSKSKKMSAFIEETKSLLPRIAFIACGCFSPPTPMHLRMFEIAKDHFEMQGTHRVVGGIISPTHDSYGKKGLASALDRCAMVKLATQSSNWIRLSDWEVHQNQWMRTQAVLQHHQNYINNHINSGGGGGDDGENTHLPGWLPRGLHDSRDPVHLKLLCGADLLESFAVPGLWAEADIEDIVANHGLVVITRAGSNPGKFIFDSDILTKYQSNITLITNWVPNEVSSTLIRRLLGRGQSVKYLLDDLVLEYIKRQRLFNFKSKYITDAVRPNHLLFNHAYTDNNKNANSYSIGDQLEQDMDESDTPSPQLQHTPTSRVFCCGEVPLRGSKVLRSGPGQAVQVITMQADEKEESQAKKQKISQVQL
```

### Thinking Trace
I begin with the InterPro architecture. The core of the protein is a continuous catalytic module spanning roughly residues 45–291 that carries multiple concordant annotations: IPR014729 (Rossmann-like alpha/beta/alpha sandwich fold, residues 45–291) defines the overall nucleotide-handling scaffold; IPR051182 (Eukaryotic NMN adenylyltransferase family, residues 45–285), IPR045094 (Nicotinamide/nicotinate mononucleotide adenylyltransferase, eukaryotic family, residues 46–282), and IPR005248 (Nicotinate/nicotinamide nucleotide adenylyltransferase family, residues 49–281) all specify an NMNAT-class adenylyltransferase; and IPR004821 (Cytidyltransferase-like domain, residues 49–256) pinpoints the catalytic fold used by adenylyl- and cytidyltransferases. The tight overlap of these domains indicates a soluble, oligomerization-prone enzyme that binds ATP or AMN and catalyzes adenylate transfer. The Rossmann-like sandwich provides the phosphate-binding and alignment geometry necessary for forming diadenosine phosphate intermediates and driving NAD biosynthesis.

From this architecture, the molecular function follows directly. The cytidyltransferase-like core and NMNAT-family signatures dictate adenylyltransferase chemistry: transferring AMP from ATP to nicotinamide mononucleotide (NMN) or nicotinate mononucleotide (NaMN), with pyrophosphate release. This chemistry corresponds to GO:0016740 (GO: molecular_function label), and in biochemical terms is an adenylyltransferase reaction that builds NAD and, by extension, NaAD.

This enzymatic role causally links to NAD metabolism and salvage. NMNATs supply NAD biosynthetic pathways by converting NMN to NAD+ (and NaMN to NAD+ via upstream routing), thereby sustaining cellular pools for redox reactions and signaling. That places the enzyme squarely in GO:0016740 (molecular_function) and connects upward to GO:0006757 (NAD metabolic process) and GO:0009435 (NAD biosynthetic process). By maintaining NAD levels, the enzyme supports energy balance and transcriptional responses that depend on NAD availability.

Cellular location is inferred from the soluble Rossmann-like architecture and absence of transmembrane features: such NMNAT-family enzymes function as cytosolic oligomers that assemble into higher-order complexes. This supports a soluble compartment assignment consistent with GO:0005737 cytoplasm, aligning with the need to service abundant cytosolic NAD-utilizing pathways.

Mechanistically, the enzyme likely forms a homomeric assembly that creates a composite active site with a conserved lysine/arginine-lined pocket for phosphate transfer. It binds ATP and NMN/NaMN, forms an AMP-enzyme intermediate, and releases AMP-linked products to generate NAD or NaAD. I hypothesize that it cooperates with cytosolic NAD-salvage and signaling hubs: transiently associating with NAMPT and NME to channel precursors; with sirtuin and PARP families that draw on NAD; and with cytosolic scaffolds that regulate nucleotide metabolism. These partnerships would localize NAD production near its major consumers, stabilizing redox and signaling homeostasis in the cytoplasm.

### Functional Summary
A soluble cytoplasmic adenylyltransferase that builds cellular NAD pools by converting nicotinamide/nicotinate mononucleotides with ATP to form diadenosine phosphate intermediates and ultimately regenerate NAD. Its Rossmann-like catalytic core supports oligomerization and precise phosphate handling, enabling efficient NAD biosynthesis and salvage in the cytoplasm. By sustaining NAD-dependent redox and signaling pathways, it helps maintain energy balance and transcriptional responses.

### UniProt Summary
Has a role in NAD biosynthesis.

### InterPro Domains
- **Rossmann-like alpha/beta/alpha sandwich fold** (`IPR014729`, homologous_superfamily) — residues 45-291
- **Eukaryotic NMN adenylyltransferase** (`IPR051182`, family) — residues 45-285
- **Nicotinamide/nicotinate mononucleotide adenylyltransferase, eukaryotic** (`IPR045094`, family) — residues 46-282
- **Nicotinate/nicotinamide nucleotide adenylyltransferase** (`IPR005248`, family) — residues 49-281
- **Cytidyltransferase-like domain** (`IPR004821`, domain) — residues 49-256

### GO Terms
**Molecular Function:** molecular_function (`GO:0003674`), binding (`GO:0005488`), catalytic activity (`GO:0003824`), GO:0003824 GO:0016740 (`GO:0016740`), protein binding (`GO:0005515`), unfolded protein binding (`GO:0051082`), transferase activity, transferring phosphorus-containing groups (`GO:0016772`), nucleotidyltransferase activity (`GO:0016779`), adenylyltransferase activity (`GO:0070566`)

**Biological Process:** biological_process (`GO:0008150`), cellular process (`GO:0009987`), biological regulation (`GO:0065007`), regulation of biological process (`GO:0050789`), negative regulation of biological process (`GO:0048519`), multicellular organismal process (`GO:0032501`), homeostatic process (`GO:0042592`), regulation of signaling (`GO:0023051`), cellular component organization or biogenesis (`GO:0071840`), negative regulation of signaling (`GO:0023057`), photoreceptor cell maintenance (`GO:0045494`), multicellular organismal-level homeostasis (`GO:0048871`), negative regulation of cellular process (`GO:0048523`), regulation of cellular process (`GO:0050794`), cellular component organization (`GO:0016043`), negative regulation of cell communication (`GO:0010648`), regulation of trans-synaptic signaling (`GO:0099177`), tissue homeostasis (`GO:0001894`), regulation of cell communication (`GO:0010646`), anatomical structure homeostasis (`GO:0060249`), negative regulation of synaptic transmission (`GO:0050805`), cell projection organization (`GO:0030030`), retina homeostasis (`GO:0001895`), postsynapse organization (`GO:0099173`), cell junction organization (`GO:0034330`), negative regulation of neuromuscular synaptic transmission (`GO:1900074`), cellular component maintenance (`GO:0043954`), modulation of chemical synaptic transmission (`GO:0050804`), synapse organization (`GO:0050808`), plasma membrane bounded cell projection organization (`GO:0120036`), dendritic spine organization (`GO:0097061`), regulation of neuromuscular synaptic transmission (`GO:1900073`), neuron projection organization (`GO:0106027`)

**Cellular Component:** cellular_component (`GO:0005575`), cellular anatomical entity (`GO:0110165`), presynaptic active zone (`GO:0048786`), intracellular anatomical structure (`GO:0005622`), presynapse (`GO:0098793`), somatodendritic compartment (`GO:0036477`), cytoplasm (`GO:0005737`), cell junction (`GO:0030054`), cell body (`GO:0044297`), neuronal cell body (`GO:0043025`), synapse (`GO:0045202`), neuromuscular junction (`GO:0031594`)

---
*Generated by [BioReason](https://bioreason.net)*
