# CG32086 (M9NF85) re-review: identity, family placement and EF-hand loop analysis

Date: 2026-10-20. Script: `compare_sequences_rereview.py` (run with `uv run compare_sequences_rereview.py`);
raw output in `RESULTS-rereview-raw.txt`. Sequences are fetched live from UniProt REST.

## 1. Gene-model identity

FlyBase gene FBgn0052086 (CG32086, synonym CG6100) has three UniProtKB/TrEMBL entries; none is Swiss-Prot reviewed.

| Accession | Length | Note |
|---|---|---|
| M9NF85 | 475 | benchmark accession; alternative-splice isoform |
| Q8IQG0 | 491 | CG32086-RA (RefSeq NP_729720.1, FBpp0075878); PANTHER 19.0 representative; carries the gene's IBA annotations in GOA |
| Q8T4E3 | 245 | cDNA clone AT02370p; truncated, lacks the C-terminal EFHB EF-hand domain |

M9NF85 is identical to Q8IQG0 except at one internal position: M9NF85 residue N234 replaces the 17-residue
segment KYTFAVPDITFGVPLRS (Q8IQG0 234-250), i.e. M9NF85 lacks 16 residues of Q8IQG0. The C-terminal EFHB
EF-hand domain (M9NF85 399-469, Pfam PF25325) is intact in both isoforms. No annotated domain or motif lies in
the missing segment, so M9NF85 is a full-length alternative isoform, not a fragment.

GOA (QuickGO, queried 2026-10-20) has no annotations on M9NF85 or Q8T4E3; Q8IQG0 has five IBA rows
(GO:0005879, GO:0061891, GO:0030317, GO:0070884, GO:2001256).

## 2. PANTHER placement

PANTHER 19.0 fruit-fly classification file (PTHR19.0_fruit_fly) lines for the fly PTHR12086 members:

```
DROME|FlyBase=FBgn0052086|UniProtKB=Q8IQG0	Q8IQG0	CG6100	PTHR12086:SF12
DROME|FlyBase=FBgn0053489|UniProtKB=Q7KUG5	Q7KUG5	CG6110	PTHR12086:SF12
DROME|FlyBase=FBgn0053490|UniProtKB=Q8MST3	Q8MST3	CG6110	PTHR12086:SF12
DROME|FlyBase=FBgn0030691|UniProtKB=Q9VXP5	Q9VXP5	Efhc1.1	PTHR12086:SF11
DROME|FlyBase=FBgn0034487|UniProtKB=Q7K2N1	Q7K2N1	Efhc1.2	PTHR12086:SF11
```

So CG32086 sits in PTHR12086:SF12 (EF-HAND DOMAIN-CONTAINING FAMILY MEMBER B), the same subfamily as human
EFHB/CFAP21 (Q8N7U6), mouse Efhb (Q8CDU5) and bovine EFHB (F1MMV1), together with two fly paralogs
(FBgn0053489, FBgn0053490). The Alliance orthology set also lists human, mouse, rat and frog EFHB as orthologs of
FBgn0052086, with PANTHER among the matching methods. The M9NF85 UniProt entry itself carries no PANTHER
cross-reference; the placement is gene-level, via the Q8IQG0 isoform.

## 3. EF-hand calcium-binding loop scan (PROSITE PS00018 pattern)

| Accession | PS00018 matches |
|---|---|
| M9NF85 | none |
| Q8IQG0 | none |
| Q7KUG5, Q8MST3 (fly SF12 paralogs) | none |
| Q9VXP5 (fly Efhc1.1) | none |
| Q8N7U6 (human EFHB) | 610 DVDNDGFINYLE |

Human EFHB has one canonical calcium-binding loop in its central EF-hand pair (UniProt EF-hand domains 561-596 and
597-632). None of the fly SF12 proteins, including M9NF85, has a canonical PS00018 loop. Absence of the pattern
does not prove absence of metal binding (non-canonical loops exist), but it removes the sequence basis for
transferring a calcium-sensor activity.

## 4. Local alignments (BLOSUM62, gap -11/-1)

| Target | Score | M9NF85 span | Target span | Aligned | Identity |
|---|---|---|---|---|---|
| Q8N7U6 human EFHB | 136 | 5-442 | 252-708 | 397 | 0.28 |
| Q7KUG5 fly CG6110 | 907 | 1-472 | 1-495 | 456 | 0.48 |
| Q8MST3 fly CG6110 | 873 | 1-472 | 1-530 | 464 | 0.47 |
| Q9VXP5 fly Efhc1.1 | 40 | 335-358 | 738-761 | 24 | 0.38 |

M9NF85 is most similar to its two fly SF12 paralogs (about 48% identity over the full length), and aligns
weakly (28%) over the central/C-terminal part of human EFHB; the human N-terminal 251 residues have no fly
counterpart. Similarity to the EFHC (SF11) proteins is negligible, consistent with the PANTHER subfamily split.

## 5. Characterised relative: human EFHB curated function (UniProt Q8N7U6, 2026-10-20)

UniProt FUNCTION text for human EFHB (Q8N7U6), quoted from the curated entry:

"Microtubule inner protein (MIP) part of the dynein-decorated doublet microtubules (DMTs) in cilia axoneme, which is required for motile cilia beating (PubMed:36191189). Cytosolic sensor for calcium, modulates the interaction of STIM1 and ORAI1 upon store depletion and the activation of store-operated Ca(2+) entry (SOCE) and NFAT translocation from cytosol to nucleus (PubMed:30481768)."

The two halves of this function have different phylogenetic standing for the fly protein. The axonemal MIP role is
the deep, family-wide PAINT inference (PTN000250051, axonemal microtubule, seeded by EFHC1, EFHC2 and EFHB
proteins). The calcium-sensor/SOCE role rests on one human study and, in the fly protein, on an EF-hand region
that lacks a canonical calcium-binding loop.

## Conclusion

M9NF85 is a full-length alternative isoform of CG32086 (16 residues shorter than Q8IQG0, EFHB C-terminal domain
intact). By PANTHER subfamily it is an EFHB (SF12) family member, co-orthologous with two fly paralogs to
vertebrate EFHB. Localization to axonemal doublet microtubules is the best-supported family-level inference;
calcium-sensor activity is not supported by the fly sequence.
