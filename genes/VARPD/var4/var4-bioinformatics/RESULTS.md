# Sequence, Topology, and GenBank KT362218.1 Cluster Audit: Var4 (UniProtKB:A0A0N7FMV9)

- **Source records:** `genes/VARPD/var4/var4-uniprot.txt` (`ALG65339.1`, `EMBL:KT362218`) and `genes/VARPD/var4/var4-bioinformatics/KT362218_features.gb` (`KT362218.1`, 41,899 bp)
- **Sequence length:** 2345 aa
- **`CC -!- SUBCELLULAR LOCATION` lines:** 0
- **Secretory signal/transit features (`FT SIGNAL` / `FT TRANSIT` / `FT PROPEP`):** 0
- **Membrane-spanning features (`FT TRANSMEM` / `FT INTRAMEM`):** 0
- **Annotated features:** DOMAIN 16..450, DOMAIN 1433..1508, MOD_RES 1468
- **Ser1468 residue check (1-based):** `S` within `ELGGDSLVAIQLL` (residues 1463-1475, `DSL` phosphopantetheine attachment motif)
- **Adenylation (`PF00501`) match count:** 0 (confirms Var4 lacks an intrinsic NRPS adenylation domain; the position-3 aspartate monomer is activated in trans by the adjacent cluster NRPS module Var5 / `ALG65340.1`)

## GenBank `KT362218.1` (`41,899 bp`) 14-CDS Feature Map (`var1`–`var14`)

| Gene | Coordinates (`KT362218.1`) | `protein_id` | Product | Length (aa) | GenBank `/note` |
| --- | --- | --- | --- | ---: | --- |
| `var1` | `1..834` | `ALG65337.1` | `Var1` | 277 | thioesterase |
| `var2` | `812..1513` | `ALG65338.1` | `Var2` | 233 | phospantetheinyl transferase |
| `var3` | `1510..6735` | `ALG65336.1` | `Var3` | 1741 | nonribosomal peptide synthetase |
| `var4` | `6735..13772` | `ALG65339.1` | `Var4` | 2345 | polyketide synthase |
| `var5` | `13769..16882` | `ALG65340.1` | `Var5` | 1037 | nonribosomal peptide synthetase |
| `var6` | `16879..24630` | `ALG65341.1` | `Var6` | 2583 | nonribosomal peptide synthetase |
| `var7` | `24670..31965` | `ALG65342.1` | `Var7` | 2431 | nonribosomal peptide synthetase |
| `var8` | `complement(32061..34508)` | `ALG65343.1` | `Var8` | 815 | TonB receptor |
| `var9` | `complement(34707..35735)` | `ALG65344.1` | `Var9` | 342 | fecr-like protein |
| `var10` | `complement(35732..36310)` | `ALG65345.1` | `Var10` | 192 | RNA polymerase subunit sigma-24 |
| `var11` | `complement(36472..37791)` | `ALG65346.1` | `Var11` | 439 | lysine N-monooxygenase |
| `var12` | `complement(37778..38884)` | `ALG65347.1` | `Var12` | 368 | n-acetyltransferase |
| `var13` | `complement(38953..39738)` | `ALG65348.1` | `Var13` | 261 | ferric iron reductase |
| `var14` | `40220..41899` | `ALG65349.1` | `Var14` | 559 | cyclic peptide transporter |

GenBank `KT362218.1` (`41,899 bp`) contains 14 CDSs (`var1`–`var14`) with non-monotonic `protein_id` assignment across the first three ORFs (`var1` `1..834` = `ALG65337.1` thioesterase, `var2` `812..1513` = `ALG65338.1` phospantetheinyl transferase, `var3` `1510..6735` = `ALG65336.1` nonribosomal peptide synthetase) followed in locus order by `var4`–`var14` (`ALG65339.1`–`ALG65349.1`): var1 (1..834) = ALG65337.1 [thioesterase]; var2 (812..1513) = ALG65338.1 [phospantetheinyl transferase]; var3 (1510..6735) = ALG65336.1 [nonribosomal peptide synthetase]; var4 (6735..13772) = ALG65339.1 [polyketide synthase]; var5 (13769..16882) = ALG65340.1 [nonribosomal peptide synthetase]; var6 (16879..24630) = ALG65341.1 [nonribosomal peptide synthetase]; var7 (24670..31965) = ALG65342.1 [nonribosomal peptide synthetase]; var8 (complement(32061..34508)) = ALG65343.1 [TonB receptor]; var9 (complement(34707..35735)) = ALG65344.1 [fecr-like protein]; var10 (complement(35732..36310)) = ALG65345.1 [RNA polymerase subunit sigma-24]; var11 (complement(36472..37791)) = ALG65346.1 [lysine N-monooxygenase]; var12 (complement(37778..38884)) = ALG65347.1 [n-acetyltransferase]; var13 (complement(38953..39738)) = ALG65348.1 [ferric iron reductase]; var14 (40220..41899) = ALG65349.1 [cyclic peptide transporter].

## Conclusion
Var4 (`A0A0N7FMV9`, 2,345 aa) contains 0 signal/transit peptides (`FT SIGNAL` = 0) and 0 transmembrane helices (`FT TRANSMEM` = 0), carries a covalent 4'-phosphopantetheinyl carrier domain (`Ser1468`), and requires cytosolic malonyl-/methylmalonyl-CoA, NADPH, Fe(II), and 2-oxoglutarate cofactors, supporting cytoplasmic localization (`GO:0005737`).
