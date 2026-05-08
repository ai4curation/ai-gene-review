# BioReason Chat Export
*Exported on March 22, 2026 at 02:31 AM*

---

**Organism:** Pseudomonas putida

**Sequence:**
```
MSQSSQQETIKDMIGVGFGPSNLALAIALEELAESRGHALDALFIDKQQDYHWHGETLATQSELQISFLKDLVSLRTPTSPYSFVNYLHQKQRLADFINLGTFYPCRLEYNDYLRWAAEHFTSQAVYGQEVLRIEPHVHAGRVQHLCVITRDRQGREYSRPTRSVVVGSGGTPKIPENFGAFKDDPRVFHHSQYLSSLTKLPCTAGKPMRIAVIGSGQSAAEAFIDLNDSYPSVKVDMILRGSALKPADDSPFVNEIFSPDYTDLVYNEPADQRSKLLGEYHNTNYSVVDLNLIERIYGILYRQKVAHQHRHNVLCRRQVEAVVATREGLELTLRDLATGQQQTHRYDAVILATGYERRSHRELLAPLADYLEDFSVDRNYRVLASPDLQASVYLQGFCESSHGLSDTLLSVLPTRAAEIGRALYQDLEQLHEKPQAAVALTRA
```

### Thinking Trace
I begin with the InterPro architecture. The sequence is dominated by IPR025700 (L-lysine 6-monooxygenase/L-ornithine 5-monooxygenase family) spanning residues 3–428, a hallmark of soluble flavin-dependent amine monooxygenases that hydroxylate basic amino acids. This family assignment is reinforced by IPR036188 (FAD/NAD(P)-binding domain superfamily) extending from residues 8–440, indicating a Rossmann-like fold that binds FAD and often exchanges reducing equivalents with NAD(P)H. The near-full-length coverage of both signatures establishes a soluble FAD-enzyme core without transmembrane elements or signal peptides, pointing to a cytosolic enzyme that executes oxidative N-hydroxylation chemistry.

From this architecture, the molecular function follows. Members of the IPR025700 family catalyze flavin-mediated monooxygenation of primary aliphatic amino groups on lysine or ornithine scaffolds. The FAD/NAD(P)-binding superfamily domain provides the redox relay that activates molecular oxygen at the flavin cofactor. This causes hydroxylation of a bound diamine/trimine substrate—here tuned by the L-lysine 6-monooxygenase chemistry—to yield L-beta-hydroxylysine. The mechanistic hallmarks (FAD-dependent oxygen activation, substrate hydroxylation on an amino acid backbone) align with GO:0016705 oxidoreductase activity, acting on paired donors with incorporation or reduction of molecular oxygen.

Linking function to process, L-beta-hydroxylysine production in soil bacteria ties into lysine utilization and nitrogen flux. By converting free lysine into a hydroxylated derivative, the enzyme channels carbon and nitrogen through downstream catabolic or salvage routes. This situates the enzyme in lysine-centered metabolism, consistent with the biological process of lysine metabolic process.

Cellular location is inferred from the soluble, cofactor-binding architecture and the absence of targeting signals. A soluble FAD monooxygenase of this sort operates in the cytoplasm, where amino acid pools and redox cofactors are managed; thus the cellular component is the cytoplasm.

A coherent mechanistic hypothesis emerges: the enzyme binds FAD in a Rossmann-like core (residues 8–440), receives electrons from NAD(P)H, activates O2, and hydroxylates the epsilon-amino group of L-lysine within a basic-amino-acid pocket shaped by the IPR025700 family scaffold (residues 3–428). In Pseudomonas putida and related Arthrobacter lineages, this chemistry integrates lysine catabolism with broader nitrogen economy in nutrient-rich soils. Likely interaction partners include cytosolic redox and amino-acid-metabolism hubs: NADPH-supplying dehydrogenases (e.g., glucose-6-phosphate dehydrogenase), glutathione-dependent systems that buffer flavin redox states, and lysine-pathway enzymes that hand off L-beta-hydroxylysine. Together these associations would stabilize the monooxygenase cycle and coordinate flux through lysine metabolism in the cytoplasm.

### Functional Summary
A soluble flavin-dependent monooxygenase in soil bacteria that uses a Rossmann-like FAD-binding core to hydroxylate the epsilon-amino group of L-lysine, generating L-beta-hydroxylysine in the cytoplasm. By coupling electron transfer from cellular redox systems to oxygen activation, it modifies lysine for downstream utilization, thereby integrating nitrogen and amino-acid metabolism in nutrient-rich environments.

### UniProt Summary
Catalyzes the formation of L-beta-hydroxylysine from L-lysine.

### InterPro Domains
- **L-lysine 6-monooxygenase/L-ornithine 5-monooxygenase** (`IPR025700`, family) — residues 3-428
- **FAD/NAD(P)-binding domain superfamily** (`IPR036188`, homologous_superfamily) — residues 8-440

### GO Terms
**Molecular Function:** molecular_function (`GO:0003674`), catalytic activity (`GO:0003824`), oxidoreductase activity (`GO:0016491`), monooxygenase activity (`GO:0004497`), oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen (`GO:0016705`), oxidoreductase activity, acting on single donors with incorporation of molecular oxygen (`GO:0016701`), oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen (`GO:0016709`)

**Biological Process:** biological_process (`GO:0008150`), metabolic process (`GO:0008152`), cellular process (`GO:0009987`), biosynthetic process (`GO:0009058`), cellular metabolic process (`GO:0044237`), secondary metabolic process (`GO:0019748`), organic substance metabolic process (`GO:0071704`), nitrogen compound metabolic process (`GO:0006807`), siderophore metabolic process (`GO:0009237`), secondary metabolite biosynthetic process (`GO:0044550`), cellular biosynthetic process (`GO:0044249`), cellular nitrogen compound metabolic process (`GO:0034641`), amide metabolic process (`GO:0043603`), organonitrogen compound metabolic process (`GO:1901564`), organic substance biosynthetic process (`GO:1901576`), organonitrogen compound biosynthetic process (`GO:1901566`), amide biosynthetic process (`GO:0043604`), cellular nitrogen compound biosynthetic process (`GO:0044271`), peptide metabolic process (`GO:0006518`), siderophore biosynthetic process (`GO:0019290`), peptide biosynthetic process (`GO:0043043`), nonribosomal peptide biosynthetic process (`GO:0019184`)

**Cellular Component:** cellular_component (`GO:0005575`), cellular anatomical entity (`GO:0110165`), cytoplasm (`GO:0005737`), intracellular anatomical structure (`GO:0005622`)

---
*Generated by [BioReason](https://bioreason.net)*
