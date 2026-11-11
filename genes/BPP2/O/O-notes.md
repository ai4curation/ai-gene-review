# Bacteriophage P2 Gene O (Capsid maturation protease and scaffolding protein gpO; UniProt P25478)

## Overview
Gene **O** of temperate myovirus *Escherichia phage P2* (`BPP2`) encodes a bifunctional 284-amino-acid polypeptide (31.4 kDa; `UniProt:P25478`, `EC:3.4.21.-`, Peptidase family S49) that serves as both the internal capsid scaffolding protein and the procapsid maturation serine endopeptidase (`PMID:1837355`, `PMID:17931675`, `PMID:19064277`).
- **N-terminal serine protease domain (residues 1–141, `O*`)**: Contains a classical serine protease catalytic triad (`Asp-19`, `His-48`, `Ser-107`; `PMID:19064277`). During procapsid maturation, gpO autoproteolytically cleaves itself between residues 141 and 142 (generating the 141-aa N-terminal fragment `O*`, which remains incorporated inside mature P2 and P4 virions) and cleaves the N-terminal 31 residues off the major capsid protein gpN (yielding `gpN*`) (`PMID:17931675`, `PMID:19064277`).
- **C-terminal scaffolding domain (residues 195–284)**: Forms alpha-helical oligomers in solution (`residues 197–257`) and requires its C-terminal cysteine (`Cys-284`) to bind gpN and direct the assembly of T=7 P2-size procapsids (`PMID:17931675`, `PMID:19064277`).

## Key Literature & Experimental Evidence
- **PMID:17931675** (*Incorporation of scaffolding protein gpO in bacteriophages P2 and P4.*):
  - `"Here, we use protein analysis and mass spectroscopy to show that P2 and P4 virions as well as procapsids isolated from viral infections contain O(*) and that cleavage occurs between residues 141 and 142 of gpO. By co-expression of gpN with truncated gpO proteins, we show that O(*) binds to gpN and retains the proteolytic activity of gpO and that the C-terminal 90 residues of gpO (residues 195-284) are sufficient to promote the formation of P2-size procapsids."`
- **PMID:19064277** (*Functional domains of the bacteriophage P2 scaffolding protein: identification of residues involved in assembly and protease activity.*):
  - `"We show that gpO is a classical serine protease, with a catalytic triad comprised of Asp 19, His 48 and Ser 107. The C-terminal 90 amino acids of gpO are required and sufficient for capsid assembly. This fragment contains a predicted alpha-helical segment between residues 197 and 257 and exists as a multimer in solution, suggesting that oligomerization is required for scaffolding activity. Correct assembly requires the C-terminal cysteine residue, which is most likely involved in transient gpN interactions."`

## Curation Decisions
- **Molecular Function**:
  - `GO:0008233` (`peptidase activity`, IEA), `GO:0008236` (`serine-type peptidase activity`, IEA), `GO:0016787` (`hydrolase activity`, IEA): **MODIFY** to `GO:0004252` (`serine-type endopeptidase activity`).
  - `GO:0004252` (`serine-type endopeptidase activity`): **NEW** supported by `PMID:19064277` and `PMID:17931675`.
- **Biological Process**:
  - `GO:0019069` (`viral capsid assembly`, IEA): **ACCEPT** (C-terminal scaffolding domain directs T=7 procapsid assembly; `PMID:17931675`, `PMID:19064277`).
  - `GO:0046797` (`viral procapsid maturation`, IEA): **ACCEPT** (N-terminal protease domain cleaves gpN and gpO during procapsid maturation; `PMID:17931675`, `PMID:19064277`).
  - `GO:0006508` (`proteolysis`, IEA): **MODIFY** to `GO:0046797` (`viral procapsid maturation`).
- **Cellular Component**:
  - `GO:0019028` (`viral capsid`): **NEW** supported by `PMID:17931675` (`O*` is retained inside mature P2 and P4 capsids as well as procapsids).
