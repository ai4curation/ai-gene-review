# C2 (P69202) — Curation Notes

## Overview
- **Gene symbol**: `C2` (`c2`)
- **UniProt ID**: `P69202` (`RPC2_BPP22`)
- **Organism**: Salmonella phage P22 (`NCBITaxon:10754`)
- **Product**: Regulatory protein C2 (216 AA)

## Sequence & Domain Architecture
- **Length**: 216 AA (`file:genes/BPP22/C2/C2-uniprot.txt`)
- **N-terminal DNA-binding domain (residues 1–76)**:
  - `InterPro:IPR001387` (`Cro/C1-type_HTH`), `InterPro:IPR010982` (`Lambda_DNA-bd_dom_sf`), `Pfam:PF01381` (`HTH_3`)
  - Contains a helix-turn-helix (HTH) motif at residues 21–40 (`FT   DOMAIN 10..64 /note="HTH cro/C1-type"`, `FT   DNA_BIND 21..40 /note="H-T-H motif"`).
  - NMR solution structure (`PDB:1ADR`, [PMID:8289306]): five alpha-helices (residues 6–17, 21–28, 32–39, 47–57, and 61–65).
  - X-ray crystal structures in complex with operator DNA (`PDB:2R1J`, `PDB:3JXB`, `PDB:3JXC`, `PDB:3JXD`).
- **C-terminal dimerization and S24 autopeptidase domain (residues 84–216)**:
  - `InterPro:IPR039418` (`LexA-like`), `InterPro:IPR036286` (`LexA/Signal_pep-like_sf`), `InterPro:IPR050077` (`LexA_repressor`), `InterPro:IPR015927` (`Peptidase_S24_S26A/B/C`), `Pfam:PF00717` (`Peptidase_S24`), `MEROPS:S24.002`.
  - The C-terminal 133 amino acids are homologous to the C-terminal sequence of coliphage lambda cI repressor ([PMID:7260059]).

## Biological Function
1. **Transcriptional repression and maintenance of lysogeny (`immC` region)**:
   - Regulatory protein C2 is the primary immunity repressor of phage P22 (`immC`). It binds cooperatively to the tripartite `OL` and `OR` operators (`OR1`, `OR2`, `OR3`) to repress transcription from the early lytic promoters `PL` and `PR`, maintaining the prophage in a latent (lysogenic) state and conferring immunity against homoimmune superinfection ([PMID:7260059], [PMID:11053393], `file:genes/BPP22/C2/C2-uniprot.txt`).
   - Unlike phage lambda cI (which is inactivated only by RecA*-stimulated autoproteolysis), P22 C2 can also be inactivated non-covalently by the P22 antirepressor protein Ant encoded in the `immI` region ([PMID:6350606], [PMID:11053393]).
2. **RecA-stimulated serine-type endopeptidase (autoproteolytic) cleavage during prophage induction**:
   - Like lambda cI and LexA, P22 C2 contains a C-terminal Peptidase S24 domain (`Pfam:PF00717`, `MEROPS:S24.002`) that undergoes RecA-stimulated intramolecular autocleavage upon host DNA damage (SOS response), inactivating the repressor and triggering prophage induction (release from viral latency) ([PMID:7260059], `file:genes/BPP22/C2/C2-uniprot.txt`).

## Key Literature & Verbatim Evidence
- **[PMID:7260059]** (Sauer et al., 1981, *Biochemistry*):
  > "The repressor is a single-chain 216 amino acid polypeptide. Basic residues in the sequence tend to be clustered, and residues 9-20 are highly basic, containing five arginyl and three lysyl residues. The carboxyl-terminal 133 amino acids of the c2 repressor are homologous to the carboxyl-terminal sequence of the coliphage lambda cI repressor."
- **[PMID:8289306]** (Sevilla-Sierra et al., 1994, *J Mol Biol*):
  > "The solution structure of the N-terminal DNA-binding domain of the P22 c2 repressor (residues 1 to 76) was determined by nuclear magnetic resonance (NMR) spectroscopy."
  > "The molecular architecture includes five alpha-helical segments with residues 6 to 17, 21 to 28, 32 to 39, 47 to 57 and 61 to 65."
- **[PMID:11053393]** (Vander Byl & Kropinski, 2000, *J Bacteriol*):
  > "In the lysogenic state, P22 expresses three different systems that may interfere with superinfection by homologous phages. These are immunity conferred by the prophage repressor ( c2 ), superinfection exclusion mediated by the sieA and sieB genes, and serotype conversion. The presence of the C2 protein represses the replication of homoimmune phage genomes"

## GO Annotation Decisions
- **Existing GOA (`GO:0003677` DNA binding, IEA)**: `ACCEPT` as core function (direct operator binding via N-terminal HTH domain).
- **Proposed `NEW` annotations**:
  - `GO:0003700` (`DNA-binding transcription factor activity`, `enables`) — sequence-specific transcriptional repressor at `OL` and `OR`.
  - `GO:0032897` (`negative regulation of viral transcription`, `involved_in`) — represses lytic transcription from `PL` and `PR`.
  - `GO:0019044` (`maintenance of viral latency`, `involved_in`) — maintains the lysogenic state of the prophage.
  - `GO:0004252` (`serine-type endopeptidase activity`, `enables`) — C-terminal S24 autopeptidase domain (`Pfam:PF00717`, `MEROPS:S24.002`) mediates RecA-stimulated self-cleavage.
  - `GO:0019046` (`release from viral latency`, `involved_in`) — autocleavage inactivates C2 to trigger prophage induction.
  - `GO:0030430` (`host cell cytoplasm`, `located_in`) — acts in the bacterial host cytoplasm at the phage genome.
