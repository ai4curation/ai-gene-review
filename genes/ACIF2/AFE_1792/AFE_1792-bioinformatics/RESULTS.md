# SQR type assignment for five acidophile sulfide:quinone oxidoreductase entries

Reproduce with:

```bash
bash genes/ACIF2/AFE_1792/AFE_1792-bioinformatics/fetch_sequences.sh
uv run python genes/ACIF2/AFE_1792/AFE_1792-bioinformatics/sqr_typing.py
```

Raw output is in `sqr_typing_output.md`. Sequences are from UniProt REST
(`sequences.fasta`). Method: Biopython global pairwise alignment, BLOSUM62, gap
open -10, extend -0.5; identity is computed over the shorter sequence. No
phylogeny or profile HMM was run, so type calls rest on pairwise identity to typed
references and on conserved active-site cysteines. They are inferences, not
classifier output.

## References used

- Type I (SqrA): B7JBP8 (A. ferrooxidans AFE_1792, crystal structure and mutagenesis)
  and O67931 (Aquifex aeolicus). Both are explicitly Type I in PMID:23103448.
- Type II: Q9Y6N5 (human SQOR).
- Type III candidates: A8MAC9 and A8MCW1 (Caldivirga maquilingensis paralogs). It
  was not resolved which of the two is the protein characterized in PMID:23103448.
- Type IV (SqrD): Q8KDG3 (Chlorobaculum tepidum CT1087).
- Type V (SqrE): Q7ZAG8 (Acidianus ambivalens, characterized SQR) and Q8KE17
  (C. tepidum CT0876, an SqrE homolog that showed no SQR activity in PMID:19028893).
- Type VI (SqrF): Q8KG51 (C. tepidum CT0117).
- FCSD flavoprotein (sulfide:cytochrome c, not an SQR): Q8KAS4 (C. tepidum FccB-2).
- B7J411 (A. ferrooxidans AFE_0267, the "sqr" named in the genome paper, PMID:19077236).

## Results

| target | best typed hit (% identity) | aligned to B7JBP8 C128 / C160 / C356 | call |
|---|---|---|---|
| B7JBP8 AFE_1792 (A. ferrooxidans) | O67931 Type I (41.9) | C128 / C160 / C356 | **Type I (SqrA)**, characterized |
| F9ZQD6 Atc_1705 (A. caldus SM-1) | B7JBP8 (87.6) | C128 / C160 / C356 | **Type I (SqrA)**, close ortholog of AFE_1792 |
| A0A060UVE9 sqr (A. ferrivorans) | B7JBP8 (94.4) | C128 / C160 / C356 | **Type I (SqrA)**, close ortholog of AFE_1792 |
| A0A059XTE6 Y981_02650 (L. ferriphilum YSK) | B7JBP8 (57.5); O67931 (41.7) | C128 / C160 / C354 | **Type I (SqrA)**, more distant homolog |
| A0A543Q349 sqr (A. thiooxidans ATCC 19377) | Q8KE17 CT0876 SqrE homolog (56.2); Q7ZAG8 Type V (32.0) | Y137 / C186 / C361 | **Type V (SqrE)-like**; not Type I |

Identity of every target with the Type II, III, IV and VI references, and with the
FCSD flavoprotein, is 22-35%.

Main points:

1. **Three entries are close orthologs of the characterized Type I enzyme.**
   F9ZQD6 (87.6%) and A0A060UVE9 (94.4%) conserve all three catalytic and
   FAD-proximal cysteines of B7JBP8 (Cys128, Cys160 and Cys356). Their SQR activity
   is a strong orthology inference.
2. **A0A059XTE6 (Leptospirillum) is a more distant Type I homolog.** It shares 57%
   identity with B7JBP8 and conserves all three cysteines. Calling it an SQR is
   reasonable, but the inference is weaker than for the Acidithiobacillus
   orthologs, and no Leptospirillum SQR has been assayed.
3. **A0A543Q349 (A. thiooxidans) is not Type I.** It lacks the Type I
   flavin-linked cysteine (Tyr at the Cys128 position). Its two active-site
   cysteines (C186 and C361) align with the persulfide cysteines of the Type V
   A. ambivalens SQR (C178 and C350). Its closest typed relative is C. tepidum
   CT0876 (56%), an SqrE homolog that showed no SQR activity when made
   recombinantly (PMID:19028893). The entry is therefore a putative Type V
   SQR/SqrE homolog without demonstrated activity.
4. **PANTHER placement is inconsistent within the Type I orthologs.** UniProt puts
   B7JBP8 in PTHR42913:SF6 (SULFIDE-QUINONE REDUCTASE, inside the AIF/NDH-2-like
   family). Its 87-94% identical orthologs F9ZQD6 and A0A060UVE9, and the
   Leptospirillum homolog, are in PTHR43755:SF1, the family that also holds the
   Type IV, V and VI SQRs and the FCSD flavoprotein. PTHR43755 membership alone
   therefore cannot tell an SQR from an FCSD flavoprotein, or one SQR type from
   another.
5. **A. ferrooxidans ATCC 23270 encodes more than one SQR-family protein.**
   AFE_0267 (B7J411) is only 27.5% identical to AFE_1792 and has no residue
   aligned to Cys160. The A. ferrooxidans genome paper calls AFE_0267 the
   experimentally validated "sqr", while the crystallized and kinetically
   characterized enzyme is AFE_1792. CMMMech's records use AFE_1792.

## Limitations

- These are pairwise global alignments only. Type assignment by Marcia et al. 2010
  (PMID:20077566) uses structure-based fingerprints, including capping loops and the
  C-terminal extension, which were not scored here.
- The Caldivirga Type III references are uncertain (two paralogs).
- Cysteine positions were mapped by pairwise alignment to each reference. In
  low-identity pairs (below 30%) a mapped residue can shift by a few positions.
