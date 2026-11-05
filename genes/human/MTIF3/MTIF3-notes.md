# MTIF3 notes

## Deep research

`MTIF3-deep-research-claude-code.md` (claude_code provider) ran for about 39 s with 2 web
searches and 6 citations (Koripella 2019, a 2020 Nat Commun paper, an eLife 2023 obesity
eQTL study, aggregator pages). It was used only for leads; claims below were checked
against cached publications.

## Function

- Identification and biochemistry [PMID:12095986 "IF3(mt) shifts the equilibrium between the
  55 S mitochondrial ribosome and its subunits toward subunit dissociation."]
- 28S binding Kd about 30 nM, does not bind 55S, dissociates 55S [PMID:18056078].
- C-terminal domain residues 170-175 needed for 39S displacement; C-terminal extension
  residues 247-248 needed to block fMet-tRNA binding without mRNA [PMID:19239245].
- Structure on the 28S subunit [PMID:30677741 "The location of the C-terminal domain (CTD)
  clarifies its anti-association activity"].
- Human knockouts: mtIF3 dispensable for leaderless mRNAs but essential for ATP6
  [PMID:36629253 "mtIF3 activity is not required for translation of leaderless mitochondrial
  transcripts but is essential for translation of ATP6 in the case of the bicistronic ATP8/ATP6
  transcript"]; independent HeLa knockout [PMID:32346061 "the translation of ATP6 mRNA was
  selectively decreased which compromised the assembly of ATP synthase"].
- Mouse: [PMID:31903419 "We show that MTIF3 is essential for survival and that heart- and
  skeletal muscle-specific loss of MTIF3 causes cardiomyopathy."]

## Judgement calls

- All 77 protein binding IPI rows (76 HuRI, 1 HI-II-14) removed; the partners are mostly
  membrane or secreted proteins.
- Ribosome disassembly (IDA) accepted: the GO definition includes subunit dissociation.
- The mitochondrion ISS row cites bovine IF-2mt (P46198) as the similarity partner, which looks
  like a with/from slip; the localisation itself is correct, so it is accepted.
- The obesity-associated MTIF3 eQTL (eLife 2023, from deep research) was not fetched or
  used; it does not bear on the molecular function.
- No Mendelian disease is established for MTIF3.
