# Citations for Research Query

**Query:** # Hypothesis: is this "dGTPase-like" protein a catalytically intact enzyme, and of what activity?

You are an independent computational biologist. A bacterial protein has been
assigned to a family whose members are named a specific enzyme, but many
individual members are cautiously named "**-like**" by curators, who withheld the
specific catalytic activity. Decide whether this representative is a
**catalytically competent enzyme of the assigned activity**, a **degraded /
pseudo-enzyme**, or an enzyme of a **different substrate**.

## What is known (do not assume beyond this)

- NCBI Protein Family **NF002326** (NCBIFAM/PGAP), an *equivalog*, product name
  "**deoxyguanosinetriphosphate triphosphohydrolase**" (dGTPase; EC 3.1.5.1).
- This representative, UniProt **Q92Q32** (*Sinorhizobium meliloti* 1021, 405 aa),
  is UniProt-named "Deoxyguanosinetriphosphate triphosphohydrolase-**LIKE**
  protein" — the curator did NOT assign the specific activity or an EC number.
- dGTPases belong to the **HD superfamily** of metal-dependent phosphohydrolases,
  whose active site is a conserved **H...HD...D** motif of His/Asp residues that
  coordinate the catalytic divalent metal(s).

## Representative sequence

UniProt **Q92Q32**, 405 aa:

```
MTVDRQALGFGYGEHAAYASNPWASRGRLYPEASSPTRSDFQRDRDRIVHTTAFRRLKHKTQVFIAADGDHYRTRLTHTIEVAQIARALARALKLDEDLAEGVALVHDFGHTPFGHTGEDALHEVLEPYGGFDHNAQSLRIVTKLERRYAEFDGLNLTWESLEGLVKHNGPLMTADGQGLRGPVPQPILDYCALHDLELASFASLEAQVAAIADDIAYNTHDIDDGLRAGYLTFEMLEEIPFLARLMREVHDRYPGLESSRFTHEIMRRQITAMVEDVIAVAQKRLGEVRPESAKDVRCAGRVMATFSDEMSETDRQIKNLLMTRIYRHPEVMRVRQGAASIVTDLYRAFMDDPSLMKEHYWIDQIAGMAEPARARHVGDYLAGMTDTFAISVHRRLFDHTPDLR
```

## The decisive question (scope your work to this)

**Is Q92Q32 a catalytically intact HD-domain triphosphohydrolase (consistent with
dGTPase activity), or is its active site degraded / altered?** Answer by:
1. Foldseek fold assignment of the AlphaFold model (an AF model exists) — does it
   adopt the HD-domain phosphohydrolase fold, and what are the closest
   experimentally characterized structural homologs (dGTPase? SAMHD1-like dNTP
   triphosphohydrolase? something else)?
2. Identify the **HD-motif metal-coordinating His/Asp residues** and state whether
   they are **present and intact** or substituted/lost.
3. Give the most specific enzyme/EC and substrate call you can, and state whether
   propagating "**dGTPase activity (GO:0008832 / EC 3.1.5.1)**" to this protein is
   **supported, an over-annotation, or a different-substrate call**.

Keep other analyses light. Give one clear conclusion with confidence and the one
experiment that would confirm it.
**Provider:** openscientist
**Generated:** 2026-07-18T19:56:29.712604

1. PMID:27849620
2. PMID:35643313
3. PMID:31019074
4. PMID:40568220
5. PMID:8995266
6. PMID:25694425
7. PMID:23880768
8. PMID:32576829
9. PMID:30380297
10. PMID:28321930