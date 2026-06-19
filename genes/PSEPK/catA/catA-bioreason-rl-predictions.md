# BioReason Chat Export
*Exported on March 22, 2026 at 02:33 AM*

---

**Organism:** Pseudomonas putida

**Sequence:**
```
MTVKISHTADIQAFFNRVAGLDHAEGNPRFKQIILRVLQDTARLIEDLEITEDEFWHAVDYLNRLGGRNEAGLLAAGLGIEHFLDLLQDAKDAEAGLGGGTPRTIEGPLYVAGAPLAQGEARMDDGTDPGVVMFLQGQVFDADGKPLAGATVDLWHANTQGTYSYFDSTQSEFNLRRRIITDAEGRYRARSIVPSGYGCDPQGPTQECLDLLGRHGQRPAHVHFFISAPGHRHLTTQINFAGDKYLWDDFAYATRDGLIGELRFVEDAAAARDRGVQGERFAELSFDFRLQGAKSPDAEARSHRPRALQEG
```

### Thinking Trace
I begin with the InterPro architecture. The sequence is covered end-to-end by IPR015889 (Intradiol ring-cleavage dioxygenase, core homologous superfamily, residues 1–311), establishing a classic ferric-heme fold that binds and activates O2 for intradiol aromatic ring scission. Within this scaffold, two family-level signatures reinforce the enzyme class: IPR012801 (Catechol 1,2-dioxygenase, proteobacteria family, residues 8–291) and IPR050770 (Intradiol Ring-Cleavage Dioxygenase family, residues 21–295). The architecture resolves into two functional lobes: an N-terminal catalytic module IPR007535 (Catechol dioxygenase, N-terminal domain, residues 27–96) followed by IPR000627 (Intradiol ring-cleavage dioxygenase, C-terminal domain, residues 105–292). This bipartite arrangement is typical of soluble bacterial catechol/ intradiol dioxygenases, where the N-terminus helps coordinate the ferric cofactor and shape the substrate pocket, and the C-terminus completes the oxygenase barrel and substrate channel.

This domain ensemble dictates molecular function. The intradiol dioxygenase core and proteobacterial catechol 1,2-dioxygenase signatures specify a non-heme Fe(III)-dependent dioxygenase that incorporates both atoms of molecular oxygen into a catecholic substrate via intradiol cleavage chemistry. That chemistry defines dioxygenase activity and inherently requires heme/iron cofactor binding. Thus, the primary molecular function is dioxygenase catalysis (GO:0051213), supported by a heme-binding catalytic core and consistent with iron-dependent oxygenation.

From function to process, intradiol dioxygenation of catechols is a central step in aromatic compound catabolism. The explicit proteobacterial catechol 1,2-dioxygenase family mark ties the enzyme to the aerobic degradation routes of catechol and related intermediates, funneling diverse ring-containing aromatics toward central metabolism. This places the enzyme squarely in aromatic compound catabolic pathways, i.e., the biological process of breaking down aromatic molecules.

Cellular location follows from the soluble, non-membranous architecture. The absence of signal peptides or transmembrane segments in this soluble oxygenase fold, together with the cytosolic nature of catechol/ intradiol pathways in Gram-negative bacteria, indicates a cytoplasmic enzyme. This aligns with a soluble, intracellular localization where substrate pools and downstream enzymes are accessible.

Mechanistically, the N-terminal dioxygenase domain and the C-terminal barrel assemble a ferric-heme center that polarizes and activates O2 for intradiol cleavage of catechol to form cis,cis-muconate. The iron center and adjacent residues enforce catechol binding and concerted O–O scission. In vivo, this enzyme likely operates downstream of catechol-forming steps and upstream of muconate-cleavage enzymes, creating a metabolic node that couples oxygenation to ring fission. I therefore hypothesize transient assemblies with catechol-forming enzymes and muconate-processing enzymes to channel intermediates efficiently in the cytoplasm of Pseudomonas putida.

### Functional Summary
A soluble bacterial oxygenase that catalyzes intradiol cleavage of catecholic substrates as part of aerobic aromatic breakdown. It uses a non-heme iron–heme catalytic core to incorporate molecular oxygen into catechol, producing ring-opened muconate intermediates that feed into central metabolism. Operating as a cytoplasmic enzyme, it likely forms transient assemblies with adjacent steps in the pathway to streamline the flow of aromatic intermediates.

### UniProt Summary
Involved in the degradation of aromatic compounds.

### InterPro Domains
- **Intradiol ring-cleavage dioxygenase, core** (`IPR015889`, homologous_superfamily) — residues 1-311
- **Catechol 1,2-dioxygenase, proteobacteria** (`IPR012801`, family) — residues 8-291
- **Intradiol Ring-Cleavage Dioxygenase** (`IPR050770`, family) — residues 21-295
- **Catechol dioxygenase, N-terminal** (`IPR007535`, domain) — residues 27-96
- **Intradiol ring-cleavage dioxygenase, C-terminal** (`IPR000627`, domain) — residues 105-292

### GO Terms
**Molecular Function:** molecular_function (`GO:0003674`), binding (`GO:0005488`), catalytic activity (`GO:0003824`), sulfur compound binding (`GO:1901681`), ion binding (`GO:0043167`), oxidoreductase activity (`GO:0016491`), cation binding (`GO:0043169`), dioxygenase activity (`GO:0051213`), oxidoreductase activity, acting on single donors with incorporation of molecular oxygen (`GO:0016701`), oxidoreductase activity, acting on single donors with incorporation of molecular oxygen, incorporation of two atoms of oxygen (`GO:0016702`), metal ion binding (`GO:0046872`), transition metal ion binding (`GO:0046914`), iron ion binding (`GO:0005506`)

**Biological Process:** biological_process (`GO:0008150`), metabolic process (`GO:0008152`), cellular process (`GO:0009987`), catabolic process (`GO:0009056`), cellular metabolic process (`GO:0044237`), organic substance metabolic process (`GO:0071704`), organic substance catabolic process (`GO:1901575`), organic hydroxy compound metabolic process (`GO:1901615`), cellular aromatic compound metabolic process (`GO:0006725`), organic cyclic compound metabolic process (`GO:1901360`), aromatic compound catabolic process (`GO:0019439`), phenol-containing compound metabolic process (`GO:0018958`), organic cyclic compound catabolic process (`GO:1901361`)

**Cellular Component:** cellular_component (`GO:0005575`), cellular anatomical entity (`GO:0110165`), cytoplasm (`GO:0005737`), intracellular anatomical structure (`GO:0005622`)

---
*Generated by [BioReason](https://bioreason.net)*
