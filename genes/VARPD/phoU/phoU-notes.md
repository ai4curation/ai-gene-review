# Curatorial Notes for `phoU` (`A0A0H2MBK2`, `VPARA_10440`) in *Variovorax paradoxus* TBEA6

## 1. Gene & Protein Identity
- **UniProt Accession:** `A0A0H2MBK2` (`A0A0H2MBK2_VARPD`)
- **Gene Symbol:** `phoU`
- **Locus Tag / EMBL CDS:** `VPARA_10440` / `KLN58032.1` on contig `JZWI01000005` (`RefSeq:WP_047783561.1`)
- **Protein Length:** 233 aa (25,818 Da); cytoplasmic homodimer (`PIRNR:PIRNR003107`) containing two tandem symmetric three-alpha-helix bundle PhoU domains (`Pfam:PF01895` at residues 22–108 and 129–210; `InterPro:IPR028366`, `NCBIfam:TIGR02135` `phoU_full`, `PANTHER:PTHR42930:SF3`).
- **Conserved Metal-Binding & Signaling Motifs:**
  - Conserves the charged metal-coordinating and pocket residues in both three-helix bundles (`Glu54`, `Asn58`, `Glu96`, `Asp100` plus conserved `Arg97` in bundle 1, and `Asp159`, `Asp163`, `Glu198`, `Asp202` plus conserved `Arg199` in bundle 2, corresponding to the *E. coli* PhoU metal ligands `D58/N62/E100/D104` and `D161/D165/E200/D204` and conserved `R101`/`R201` characterized in `PMID:24563032`).

## 2. Operon Context on Contig `JZWI01000005`
- Encoded immediately between `phoB1` (`VPARA_10430`, `KLN58031.1`) and `pstB` (`VPARA_10450`, `KLN58033.1`) within the `phoR1-phoB1-phoU-pstB-pstA-pstC-pstS-ppx` (`VPARA_10420`–`VPARA_10490`) phosphate regulon gene cluster.

## 3. Literature & Comparative Evidence
- **[PMID:24563032]** (Gardner et al. 2014 *J Bacteriol*): Demonstrates by bacterial two-hybrid, affinity co-elution, gel filtration, ICP-MS, tryptophan fluorescence, and chromosomal integration of `phoUQuad` mutants that PhoU is a homodimer that binds $\text{Mn}^{2+}$ and $\text{Mg}^{2+}$ (which may be important for localizing PhoU to the inner membrane) and physically bridges the PstB ATPase subunit of PstSCAB to the PAS domain of the PhoR sensor kinase, negatively regulating the Pho regulon and modulating PstSCAB phosphate transport under phosphate-replete conditions.
- **[PMID:3881386]** (Surin et al. 1985 *J Bacteriol*): Nucleotide sequence and organization of `phoU` at the 3' end of the `phoS-pstC-pstA-pstB-phoU` operon.

## 4. Annotation Review Decisions
- `GO:0005737` (`cytoplasm`, IEA `GO_REF:0000044`): **ACCEPT** — core location of soluble PhoU homodimers that peripherally associate with the inner membrane via PstB and PhoR1 (`PMID:24563032`).
- `GO:0030643` (`intracellular phosphate ion homeostasis`, IEA `GO_REF:0000002`): **ACCEPT** — PhoU couples PstSCAB transport activity to PhoR1-PhoB1 signaling and prevents toxic hyperaccumulation of inorganic phosphate and polyphosphate (`PMID:24563032`).
- `GO:0045936` (`negative regulation of phosphate metabolic process`, IEA `GO_REF:0000002`): **ACCEPT** — PhoU is the essential negative regulator of the PhoR1-PhoB1 phosphate starvation regulon under phosphate-replete conditions (`PMID:24563032`).
- `GO:0030145` (`manganese ion binding`, IC from `file:VARPD/phoU/phoU-uniprot.txt`): **NEW** — PhoU coordinates $\text{Mn}^{2+}$ via conserved acidic/arginine pockets (including `Glu96/Arg97` and `Glu198/Arg199`) in each of its two `Pfam:PF01895` three-helix bundles (`22..108` and `129..210`); metal binding may be important for PhoU membrane interactions (`PMID:24563032`).
- `GO:0000287` (`magnesium ion binding`, IC from `file:VARPD/phoU/phoU-uniprot.txt`): **NEW** — PhoU also binds $\text{Mg}^{2+}$, which may be important for PhoU membrane interactions (`PMID:24563032`).
