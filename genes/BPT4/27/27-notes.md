# Bacteriophage T4 Gene 27 (gp27) — Curation Notes

## Summary of Gene Function
Bacteriophage T4 gene `27` encodes the baseplate central hub and spike-complex protein gp27 (UniProt `P17172`, 391 amino acids, ~44.5 kDa). It forms a homotrimeric hollow cylinder at the center of the T4 baseplate that serves two essential structural functions: (1) it acts as a symmetry adaptor converting the three-fold symmetry of the central membrane-puncturing needle (`(gp5)3–gp5.4`) into the pseudo-six-fold symmetry required to interface with the six surrounding baseplate wedges (primarily via gp6 and gp25) and the hexameric tail-tube junction ring (gp48); and (2) its internal ~30-Å-diameter lumen forms the proximal extension of the tail-tube channel for viral genomic DNA ejection (PubMed 11823865, PubMed 15701513, PubMed 27193680).

## Structural Organization and Assembly
- **Symmetry Mismatch Adaptor**: Each gp27 monomer contains two homologous beta-barrel torus domains alongside binding domains that give the `(gp27)3` trimer a pseudo-six-fold cylindrical upper ring while maintaining true three-fold symmetry at its lower interface where the three N-terminal OB-fold beta-barrel domains of `(gp5)3` insert into the `(gp27)3` cup (PubMed 11823865, PubMed 27193680).
- **Role in Baseplate Assembly and Triggering**: During morphogenesis, `(gp5–gp27)3` forms the core of the central hub around which the six peripheral baseplate wedges circularize (via interactions with gp6 and gp25) and onto which the gp48/gp54 tail-tube initiator rings assemble (PubMed 27193680).

## Annotation Review Notes
- `GO:0098003` (`viral tail assembly`, IEA from `GO_REF:0000043`): Directly supported by structural and genetic studies demonstrating that the `(gp27)3` hub trimer is essential for nucleating baseplate wedge circularization and tail tube initiation (`ACCEPT`).
- `GO:0098025` (`virus tail, baseplate`, IDA from PubMed 27193680 and IEA from `GO_REF:0000120`): Directly supported by X-ray crystallography and atomic cryo-EM reconstructions of the T4 baseplate (`ACCEPT`).
- `GO:0098015` (`virus tail`, IDA from PubMed 15701513 and IEA from `GO_REF:0000043`): True but overly general relative to `GO:0098025` (`virus tail, baseplate`), which is already present on this gene (`MODIFY` -> `GO:0098025`).
- `GO:0005515` (`protein binding`, IPI from PubMed 11823865 and PubMed 15701513): Directly supported by crystal structures of the `(gp5–gp27)3` heterohexameric complex showing direct binding between the gp27 trimer and the N-terminal domain of gp5 (`ACCEPT`).
