# Curatorial Notes for `mdo` (`B9U5L8`, `VPARA_05600`) in *Variovorax paradoxus* TBEA6

## 1. Gene & Protein Identity
- **UniProt Accession:** `B9U5L8` (`B9U5L8_VARPD`)
- **Gene Symbol:** `mdo`
- **Locus Tag / EMBL CDS:** `VPARA_05600` / `KLN58445.1` on contig `JZWI01000003` (`KEGG:ag:ACB72254`, `MetaCyc:MONOMER-18546`, `BRENDA:1.13.11.91`, `RefSeq:WP_047783194.1`)
- **Protein Length:** 195 aa (21,607 Da); 3-mercaptopropionate (3MP) dioxygenase Mdo (EC 1.13.11.66 / BRENDA 1.13.11.91).
- **Domain Architecture & Catalytic Triad:**
  - Belongs to the RmlC-like cupin / cysteine dioxygenase type-I family (`CDD:cd10548` `cupin_CDO`, `Pfam:PF05995` `CDO_I`, `InterPro:IPR010300` `CDO_1`, `InterPro:IPR011051` `RmlC_Cupin_sf`, `PANTHER:PTHR12918:SF1`).
  - Coordinates a catalytic non-heme ferrous iron ($\text{Fe}^{2+}$) cofactor via the conserved 3-His cupin triad at `His90`, `His92` (within `89-IHNHTVW-95`), and `His143` (`FT BINDING 90`, `92`, `143` `/ligand="Fe cation" /ligand_note="catalytic"`, `PIRSR:PIRSR610300-51`).

## 2. Direct Experimental Characterization in *Variovorax paradoxus* TBEA6
- **[PMID:19001372]** (Bruland, Wübbeler & Steinbüchel 2009 *J Biol Chem*):
  - Isolated *Variovorax paradoxus* strain TBEA6 for its ability to grow on 3,3'-thiodipropionic acid (TDP) as sole carbon and energy source.
  - `Tn5::mob` transposon mutagenesis of *V. paradoxus* TBEA6 identified two TDP-negative mutants disrupted in `mdo` (`VPARA_05600`, `ACB72254.1` / `KLN58445.1`).
  - Heterologous expression, purification, and in vivo / in vitro enzyme assays of *V. paradoxus* TBEA6 Mdo demonstrated that it catalyzes the dioxygenation of 3-mercaptopropionic acid (3MP) with $\text{O}_2$ to 3-sulfinopropionate (3SP), and does not use L-cysteine or cysteamine as substrates.
- **[PMID:24317404]** (Schürmann et al. 2014 *J Bacteriol*): Confirms the downstream pathway in *V. paradoxus* TBEA6 in which 3SP produced by Mdo is activated to 3SP-CoA by Act (`VPARA_05450`) and desulfinated to propionyl-CoA and sulfite by Acd (`VPARA_05440`).

## 3. Annotation Review Decisions
- `GO:0005506` (`iron ion binding`, IEA `GO_REF:0000002`, `enables`, `InterPro:IPR010300`): **TOO_GENERAL** — parent of `GO:0008198` (`ferrous iron binding`) already accepted in this review.
- `GO:0008198` (`ferrous iron binding`, IEA `GO_REF:0000118`, `enables`, `PANTHER:PTN002293406`): **ACCEPT** — core cofactor-binding activity at the 3-His cupin triad (`His90`, `His92`, `His143`).
- `GO:0016702` (`oxidoreductase activity, acting on single donors with incorporation of molecular oxygen, incorporation of two atoms of oxygen`, IEA `GO_REF:0000120`, `enables`): **ACCEPT** — most specific existing GO molecular function for 3-mercaptopropionate dioxygenase (EC 1.13.11.66 / RHEA:53808); propose `3-mercaptopropionate dioxygenase activity` in `proposed_new_terms`.
- `GO:0044273` (`sulfur compound catabolic process`, IMP from `PMID:19001372`, `involved_in`): **NEW** — directly demonstrated by `Tn5::mob` mutagenesis and enzyme assays in *V. paradoxus* TBEA6 (`PMID:19001372`).
- `GO:0005829` (`cytosol`, IC from `file:VARPD/mdo/mdo-uniprot.txt`, `located_in`): **NEW** — soluble 195-aa cytoplasmic enzyme purified from the soluble fraction (`PMID:19001372`).
