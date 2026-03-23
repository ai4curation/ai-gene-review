# BioReason Chat Export
*Exported on March 22, 2026 at 12:40 AM*

---

**Organism:** Schizosaccharomyces pombe

**Sequence:**
```
MKDDKGRSDTVNGYYISNSKLSSGFYKRNNANTASNDEKPNLEQNDIPSVTSSGSSTPSSISIEKEIKISKGNVIVKAIRSWSLYVAIIAILLLLVILHSFQGRPQDNGCGKSYVWPSYVRFVDFDERYTRFANKYSLYLYREKSVEESDEPSGIPILFIPGNAGSYKQVRAFAAQAAHVYANAYAEDADGTLNAGKLVPDFFVVDFNEDFSAFHGQTLLDQAEYVNDAIPYILSLYRQNRKISSEYDNEAFPPPTSVILLGHSMGGIVAQATFTMKNYVDGSVNTLITLATPHAMAPLPFDRHLVEFYESIKNFWSQSFLLSPEENSLDDVLLVSIAGGGLDTHVVPEYSSISTFVPPSNGLMVFTSGIPSVWAEIDHQAMAWCENFRRVLIRGIFAIMDARTSKCTVSLNLRKELLSRAYIQGSSFQNDITQISKPIAQYKALDLDLTYVYSEMPGQLLFLNQLGVSYIRHHIFPIPKPTSSIDRFELLTDQPIDLSSSNIKVLACRLDPKIDNTISALLENGNNKVINANCHLLRELVTLLPASTAYTSSPYGGDSFYNYVLPKEKMDDYHFILVSDDSKAPASGFVVGGFSNVSLDPKTIKGSQIELFKSGRKFQFDTKGSISKRFRFPGIQSSIMAYTISVTYELYPGAVPQKEFTPMLKQSIESPFETKYHVNMSNTELSVHGISPFMEFFGKESEKSLTLEFFLNPAIYKSVYVSIQPSYYRSAGRLLMRYRTLLASFPVVVISLAAYNQFRYFHYGSAYLSMSAALEVMIRKGLIKLLFLVSILSIAFSYLISRVELIVADGADPVASWKIFAMMVPKSFWKQNHLLFGLQTAQFWFLAPLLTLMFVGLVITASVIILCVMHLLAFIYGIYLRYKGLTFTGVCQAVKFSFQCLRTRNTRKLDHGEFKKLSSFLSQRNMYYANPSLCYVYGKKHMQARIIGIMLLLLMAMTVVPFQLVYGVALCTQTVTTAKALHLARFCTKSSHYRKKLWDFYNFSCTITILMLLLAPLDFPVLIVWARNLSMHWSIPFPTHHNFFSIIPFILLTEILRTGKMLPRLNDVEYYINNVFLFLLSFYSLIYGAEKPYLIHNVVGLYFFWLLFLYAKNGFFVQNISKWPIIPRMKYFIKHKFLRSIS
```

### Thinking Trace
I begin with the InterPro architecture. A broad family signature, IPR039529 (GPI inositol-deacylase, residues 79–1121), spans essentially the full polypeptide, indicating a dedicated enzyme that removes an acyl chain from the inositol ring of glycosylphosphatidylinositol anchors. Within its N-terminal half sits IPR029058 (Alpha/Beta hydrolase fold, residues 150–397), overlapped by IPR012908 (PGAP1-like alpha/beta domain, residues 152–398). This tandem strongly implies an α/β-hydrolase catalytic core that uses a nucleophile–acid–histidine triad to hydrolyze an ester linkage; the PGAP1-like designation narrows this chemistry to inositol deacylation rather than generic lipase activity. The C-terminal region carries IPR056824 (GPI inositol-deacylase, transmembrane domain, residues 741–1110), a multi-pass membrane module that anchors the enzyme and positions the soluble α/β-hydrolase domain toward the luminal/extracytoplasmic side where GPI-anchored substrates are presented during secretory pathway trafficking.

This domain arrangement dictates molecular function. The α/β-hydrolase core (IPR029058/IPR012908) provides the catalytic machinery for ester hydrolysis, while the PGAP1-like family signature (IPR039529) specifies the substrate as the inositol-linked acyl group of GPI anchors. The transmembrane block (IPR056824) secures the enzyme in membranes and enforces substrate proximity. Together, this architecture causes hydrolase activity acting on ester bonds (GO:0016788), matching the inositol-deacylase reaction that prepares GPI-anchored proteins for subsequent maturation and trafficking.

From function to process, inositol deacylation is a committed step in the GPI-anchored protein maturation pathway and contributes to the broader flow of glycosylphosphatidylinositol anchor biosynthesis and remodeling. By removing the inositol-linked acyl chain, the enzyme licenses further processing and sorting, thereby advancing the pathway that produces and recycles GPI-anchored surface and secreted proteins. This places the protein squarely within GPI anchor biosynthetic/metabolic routes and, more generally, membrane protein biogenesis.

The cellular location follows from both the transmembrane signature and the secretory-pathway role of GPI-anchored substrates. IPR056824 predicts a multi-pass membrane topology, and the overall architecture lacks soluble export signals, arguing for an integral membrane residence. GPI assembly and remodeling occur in the endoplasmic reticulum and early Golgi; the combination of a luminal hydrolase domain and extensive transmembrane segments therefore points to an integral component of membrane (GO:0016020), with the most parsimonious site being ER/early Golgi membranes.

Mechanistically, I hypothesize a membrane-embedded scaffold that presents the α/β-hydrolase active site to luminal GPI-anchored cargo. The enzyme likely engages nascent GPI-anchored proteins and transient complexes with GPI-assembly and sorting machinery. It probably associates with ER/Golgi GPI biogenesis factors (such as GPI transamidase and GPI-remodeling modules) to hand off substrates post-deacylation. By coupling a catalytic α/β-hydrolase core to a large multi-pass membrane platform, the protein ensures timely inositol deacylation that gates subsequent trafficking and surface delivery of GPI-anchored clients.

### Functional Summary
A multi-pass membrane hydrolase in fission yeast that catalyzes inositol deacylation of glycosylphosphatidylinositol anchors. Its α/β-hydrolase catalytic core, mounted on an extensive membrane-embedded scaffold, removes the inositol-linked acyl group to prepare GPI-anchored proteins for maturation and trafficking. Operating along the secretory pathway, it likely resides as an integral membrane protein in early endoplasmic reticulum–Golgi compartments, where it coordinates with GPI assembly and remodeling machinery to control the flow of GPI-anchored cargo to the cell surface.

### UniProt Summary
Involved in inositol deacylation.

### InterPro Domains
- **GPI inositol-deacylase** (`IPR039529`, family) — residues 79-1121
- **Alpha/Beta hydrolase fold** (`IPR029058`, homologous_superfamily) — residues 150-397
- **GPI inositol-deacylase PGAP1-like alpha/beta domain** (`IPR012908`, domain) — residues 152-398
- **GPI inositol-deacylase, transmembrane domain** (`IPR056824`, domain) — residues 741-1110

### GO Terms
**Molecular Function:** molecular_function (`GO:0003674`), catalytic activity (`GO:0003824`), hydrolase activity (`GO:0016787`), hydrolase activity, acting on ester bonds (`GO:0016788`), carboxylic ester hydrolase activity (`GO:0052689`)

**Biological Process:** biological_process (`GO:0008150`), metabolic process (`GO:0008152`), cellular process (`GO:0009987`), biosynthetic process (`GO:0009058`), GPI anchor biosynthetic process (`GO:0044238`), cellular metabolic process (`GO:0044237`), organic substance metabolic process (`GO:0071704`), cellular lipid metabolic process (`GO:0044255`), cellular biosynthetic process (`GO:0044249`), organic substance biosynthetic process (`GO:1901576`), lipid metabolic process (`GO:0006629`), organophosphate metabolic process (`GO:0019637`), phosphorus metabolic process (`GO:0006793`), phosphate-containing compound metabolic process (`GO:0006796`), glycerolipid metabolic process (`GO:0046486`), lipid biosynthetic process (`GO:0008610`), phospholipid metabolic process (`GO:0006644`), glycerolipid biosynthetic process (`GO:0045017`), organophosphate biosynthetic process (`GO:0090407`), glycerophospholipid metabolic process (`GO:0006650`), glycerophospholipid biosynthetic process (`GO:0046474`), phospholipid biosynthetic process (`GO:0008654`), phosphatidylinositol biosynthetic process (`GO:0006661`), phosphatidylinositol metabolic process (`GO:0046488`)

**Cellular Component:** cellular_component (`GO:0005575`), cellular anatomical entity (`GO:0110165`), intracellular anatomical structure (`GO:0005622`), organelle (`GO:0043226`), membrane (`GO:0016020`), cytoplasm (`GO:0005737`), endomembrane system (`GO:0012505`), organelle subcompartment (`GO:0031984`), nuclear outer membrane-endoplasmic reticulum membrane network (`GO:0042175`), Golgi apparatus (`GO:0005794`), organelle membrane (`GO:0031090`), endoplasmic reticulum (`GO:0005783`), intracellular organelle (`GO:0043229`), membrane-bounded organelle (`GO:0043227`), endoplasmic reticulum subcompartment (`GO:0098827`), intracellular membrane-bounded organelle (`GO:0043231`), endoplasmic reticulum membrane (`GO:0005789`)

---
*Generated by [BioReason](https://bioreason.net)*
