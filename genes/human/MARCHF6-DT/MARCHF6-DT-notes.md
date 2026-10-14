# MARCHF6-DT (PACMP, P0DW81) — review notes

## 2026-10-03 Tier 2 microprotein review (claude-code)

### Identity
- UniProt P0DW81 (PACMP_HUMAN), 44 aa, PE1, HGNC:56238 `MARCHF6-DT` (MARCHF6 divergent
  transcript, chr5). Synonym PACMP. Encoded by a sORF in a transcript annotated as a lncRNA
  (CTD-2256P15.2 in the source paper) — not an alternative ORF of a protein-coding host, so it
  has its own HGNC symbol and folder.
- Sequence MAASGGTKKAQSGGRRLREPSSRPSRRARQRPRRGALRKAGRFL: entirely predicted disordered
  (MobiDB-lite), very basic C-terminal half (24-44). Pfam PF23699 / InterPro IPR057239 (PACMP).
- PAN-GO: 0 IBA annotations.

### Literature
- PubMed searches ("PACMP", "PACMP micropeptide", "PACMP CtIP", "MARCHF6-DT", "CTD-2256P15.2")
  return a single relevant paper: Zhang et al. 2022 Mol Cell 82:1297-1312 (PMID:35219381).
  The task brief's guess of "Nature Chem Biol" is wrong; the paper is in Molecular Cell.
  Other "PACMP" hits are unrelated acronyms (chemical-mechanical polishing, regulatory
  post-approval change management protocol).
- Not in PMC; cached copy is abstract-only. Mechanistic details below beyond the abstract come
  from the UniProt curated entry (which cites the same paper).

Key claims [PMID:35219381]:
- "a human lncRNA, CTD-2256P15.2, encodes a micropeptide, named PAR-amplifying and
  CtIP-maintaining micropeptide (PACMP), with a dual function to maintain CtIP abundance and
  promote poly(ADP-ribosyl)ation"
- "PACMP not only prevents CtIP from ubiquitination through inhibiting the CtIP-KLHL15
  association but also directly binds DNA damage-induced poly(ADP-ribose) chains to enhance
  PARP1-dependent poly(ADP-ribosyl)ation"
- "Targeting PACMP alone inhibits tumor growth by causing a synthetic lethal interaction
  between CtIP and PARP inhibitions and confers sensitivity to PARP/ATR/CDK4/6 inhibitors,
  ionizing radiation, epirubicin, and camptothecin"

UniProt (from same paper): interacts with KLHL15 (Q96M94) and PARP1 (P09874); nucleolus and
chromosome; recruited to DNA damage sites via PAR; 10A (R23-R42) and 4A (R38-R42) Arg->Ala
mutants impair PAR binding.

### Assessment
- Single-lab, single-paper evidence; no independent replication found. All GOA rows derive
  from PMID:35219381 (or UniProt SubCell mappings of it).
- PAR binding (GO:0072572) is the best-defined molecular activity, with mutational support
  (basic-patch mutants) per UniProt — core MF.
- KLHL15 IPI: KLHL15 is the substrate-recognition subunit of a CUL3-RING ubiquitin ligase;
  PACMP competitively blocks CtIP recruitment. Bare protein binding -> ubiquitin protein
  ligase binding (GO:0031625). GO:1990948 ubiquitin ligase inhibitor activity would be more
  informative, but whether PACMP inhibits KLHL15 activity generally or only occludes the CtIP
  site is not stated in the abstract; raised as a question.
- PARP1 IPI: -> enzyme binding (GO:0019899). Unclear whether the interaction is direct or
  bridged by PAR chains (PARP1 is itself auto-PARylated); raised as a question.
- No GO term for "positive regulation of protein ADP-ribosylation" exists (only the parent
  GO:0010835 and GO:0010836 negative regulation), so GO:0010835 is accepted as the most
  specific available.
- Nucleolus: localisation is supported, but the activity is at damage sites; is_active_in
  nucleolus kept as non-core.
- No NEW terms: DNA end resection/HR specificity is plausible via CtIP but not stated in the
  available text.
