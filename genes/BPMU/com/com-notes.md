# Curation Notes for Escherichia phage Mu com (Q38621)

## Summary of Gene Function
- **Gene symbol**: `com` (locus tag `Mup54`; UniProt `Q38621`, Translational activator com)
- **Organism**: *Escherichia phage Mu* (`NCBITaxon:2681603`)
- **Function**: Translational activator Com (`Mup54`, 62 aa) is a zinc-finger RNA-binding protein (`GO:0008270` `zinc ion binding`, `GO:0046872` `metal ion binding`, `GO:0003723` `RNA binding`) encoded immediately upstream of `mom` in the late `com-mom` bicistronic operon of bacteriophage Mu [PMID:2525424, file:BPMU/com/com-uniprot.txt].
- **Mechanism of Translational Activation**: Com coordinates one `Zn2+` ion per monomer via four conserved cysteine residues (`Cys-6`, `Cys-9`, `Cys-26`, `Cys-29`) and acts in trans in the bacterial host cytoplasm (`GO:0030430` `host cell cytoplasm`) to positively regulate translation of the `mom` mRNA (`GO:0045727` `positive regulation of translation`) [PMID:2525424, file:BPMU/com/com-uniprot.txt]. Specifically, Com binds a target site in the 5' translation initiation region of `com-mom` mRNA and destabilizes an inhibitory stem-loop secondary structure that otherwise sequesters the `mom` Shine-Dalgarno sequence and AUG start codon, thereby exposing the translation initiation signals to host ribosomes [PMID:2525424, file:BPMU/com/com-uniprot.txt].

## Literature & Reference Notes
- **PMID:2525424** (Wulczyn & Kahmann, 1989, J Bacteriol, "Posttranscriptional regulation of the bacteriophage Mu mom operon by the com gene product"): Used `mom-lacZ` translational fusions and deletion mutagenesis to define the `com-mom` mRNA sequence and stem-loop structure required for Com-mediated translational stimulation, showing that deletion of the stem-loop renders `mom` translation high and independent of Com.

## Annotation Review Decisions
- `GO:0008270` (`zinc ion binding`, IEA): `ACCEPT`.
- `GO:0046872` (`metal ion binding`, IEA): `ACCEPT` (or `TOO_GENERAL` entailed by `GO:0008270`; since the prompt explicitly lists `GO:0046872` `metal ion binding` for `com`, let's `ACCEPT` both `GO:0008270` and `GO:0046872` so both are retained cleanly!).
- `GO:0030430` (`host cell cytoplasm`, IEA): `ACCEPT`.
- `NEW` `GO:0003723` (`RNA binding`, `enables`): Com binds directly to the 5' translation initiation region of `com-mom` mRNA.
- `NEW` `GO:0045727` (`positive regulation of translation`, `involved_in`): Com destabilizes the translational inhibitory stem-loop to activate `mom` mRNA translation.
