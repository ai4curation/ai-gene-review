# int (P04890) — Curation Notes

## Overview
- **Gene symbol**: `int`
- **UniProt ID**: `P04890` (`VINT_BPP22`)
- **Organism**: Salmonella phage P22 (`NCBITaxon:10754`)
- **Product**: Integrase (387 AA)

## Sequence & Domain Architecture
- **Length**: 387 AA (`file:genes/BPP22/int/int-uniprot.txt`)
- **Domains**:
  - **N-terminal arm-type DNA-binding domain**: `InterPro:IPR062090` (`Phage_integr_N`), `Pfam:PF30395` (`Phage_integr_N`), `InterPro:IPR010998` (`Integrase_recombinase_N`).
  - **Core-binding (CB) domain (residues 57–161)**: `InterPro:IPR044068` (`CB`), `FT   DOMAIN 57..161 /note="Core-binding (CB)"`.
  - **C-terminal tyrosine recombinase catalytic domain (residues 181–362)**: `InterPro:IPR002104` (`Integrase_catalytic`), `InterPro:IPR013762` (`Integrase-like_cat_sf`), `InterPro:IPR011010` (`DNA_brk_join_enz`), `InterPro:IPR050090` (`Tyrosine_recombinase_XerCD`), `Pfam:PF00589` (`Phage_integrase`).
  - **Catalytic pentad & active-site tyrosine**: `FT   ACT_SITE 215, 242, 314, 317, 340` (Arg-215, Lys-242, His-314, Arg-317, His-340) and `FT   ACT_SITE 349 /note="O-(3'-phospho-DNA)-tyrosine intermediate"` (Tyr-349).

## Biological Function
- **Site-specific tyrosine recombinase (integrase) mediating prophage integration and excision**:
  - P22 Int catalyzes site-specific recombination between the phage attachment site (`attP`) and the bacterial host attachment site (`attB` / `ataA`, located within the `thrW` threonyl-tRNA2 gene of *Salmonella*) in concert with host Integration Host Factor (IHF), integrating the phage genome into the host chromosome to establish proviral latency ([PMID:3491212], [PMID:11053393], [PMID:18502866], `file:genes/BPP22/int/int-uniprot.txt`).
  - During prophage induction, Int works in conjunction with the phage-encoded excisionase (Xis) and IHF to catalyze excisive recombination between `attL` and `attR` (`file:genes/BPP22/int/int-uniprot.txt`, [PMID:18502866]).

## Key Literature & Verbatim Evidence
- **[PMID:3491212]** (Leong et al., 1986, *J Mol Biol*):
  > "In this study, we have identified and sequenced the int and xis genes of phi 80 and P22. phi 80 int and xis were identified using a plasmid recombination assay in vivo, and the P22 genes were mapped using Tn1 insertion mutations. In all three phage, the site-specific recombination genes are located directly adjacent to the phage attachment site."
- **[PMID:11053393]** (Vander Byl & Kropinski, 2000, *J Bacteriol*):
  > "The phage integration site, att P22 or ataA , maps within thrW , a gene for threonyl tRNA2 ( 53 ), with site-specific recombination being catalyzed, as it is with coliphage λ, by integration host factor (IHF) and integrase (Int) ( 40 , 62 )."
- **[PMID:18502866]** (Mattis et al., 2008, *J Bacteriol*):
  > "The temperate bacteriophages lambda and P22 share similarities in their site-specific recombination reactions. Both require phage-encoded integrase (Int) proteins for integrative recombination and excisionase (Xis) proteins for excision."

## GO Annotation Decisions
- **Existing GOA**:
  1. `GO:0003677` (`DNA binding`, IEA, `GO_REF:0000120`) -> `ACCEPT` (binds arm-type and core-type `att` DNA sites).
  2. `GO:0006310` (`DNA recombination`, IEA, `GO_REF:0000120`) -> `MODIFY` to `GO:0015074` (`DNA integration`), `GO:0044826` (`viral genome integration into host DNA`), and `GO:0032359` (`provirus excision`).
  3. `GO:0015074` (`DNA integration`, IEA, `GO_REF:0000120`) -> `ACCEPT` (or `MODIFY` to `GO:0044826` if required, check validator; in `LAMBD/int` `GO:0015074` is `ACCEPT`).
  4. `GO:0016740` (`transferase activity`, IEA, `GO_REF:0000043`) -> `MODIFY` to `GO:0008907` (`integrase activity`).
  5. `GO:0016787` (`hydrolase activity`, IEA, `GO_REF:0000043`) -> `MODIFY` to `GO:0008907` (`integrase activity`).
  6. `GO:0044826` (`viral genome integration into host DNA`, IEA, `GO_REF:0000043`) -> `ACCEPT`.
  7. `GO:0046718` (`symbiont entry into host cell`, IEA, `GO_REF:0000043`) -> `REMOVE` (keyword mapping artifact from `KW-1160`; Int acts intracellularly after phage DNA injection).
  8. `GO:0075713` (`establishment of integrated proviral latency`, IEA, `GO_REF:0000043`) -> `ACCEPT`.
- **Proposed `NEW` annotations**:
  - `GO:0008907` (`integrase activity`, `enables`) — tyrosine recombinase / integrase activity via catalytic Tyr-349 (`InterPro:IPR002104`).
  - `GO:0032359` (`provirus excision`, `involved_in`) — catalyzes prophage excision in conjunction with Xis.
  - `GO:0030430` (`host cell cytoplasm`, `located_in`) — acts in the bacterial host cell cytoplasm.
