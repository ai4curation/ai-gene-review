# A0A2U1PS28 re-review: placement relative to characterised LepA/GUF1 proteins

Script: `compare_lepa_relatives.py` (run with `uv run --with biopython python compare_lepa_relatives.py`);
raw output in `compare_lepa_relatives.out`. Sequences fetched live from UniProt REST.

## PANTHER placement (from interpro/panther/PTHR43512/PTHR43512-entries.csv)

PTHR43512 has two subfamilies in the fetched member set: SF4 "TRANSLATION FACTOR GUF1 HOMOLOG,
CHLOROPLASTIC" (725 members; bacterial LepA plus plant chloroplast LepA, including E. coli LepA
P60785 and Arabidopsis cpLEPA Q9FNM5/At5g08650) and SF7 "TRANSLATION FACTOR GUF1, MITOCHONDRIAL"
(77 members; yeast Guf1 P46943, human GUF1 Q8N442, Arabidopsis mitochondrial GUF1 Q9FLE4/At5g39900).
A0A2U1PS28 is assigned to SF4, the bacterial/chloroplast subfamily, not the mitochondrial SF7.

## Global pairwise identity (BLOSUM62, gap -10/-0.5)

| Relative | Subfamily | Length | Identity |
|---|---|---|---|
| Q9FNM5 Arabidopsis cpLEPA At5g08650 | SF4 | 681 | 82.9% over 643 aligned columns |
| P60785 E. coli LepA | SF4 | 599 | 55.6% over 576 aligned columns |
| Q9FLE4 Arabidopsis mitochondrial GUF1 At5g39900 | SF7 | 663 | 50.2% over 632 aligned columns |
| Q8N442 human GUF1 | SF7 | 669 | 49.1% over 623 aligned columns |
| P46943 yeast Guf1 | SF7 | 645 | 43.4% over 606 aligned columns |

The target is closest to Arabidopsis cpLEPA and is more similar to bacterial LepA than to any
mitochondrial GUF1, consistent with the SF4 assignment.

## Gene model and targeting features

Length 661 aa, close to Arabidopsis cpLEPA (681 aa); about 60 residues longer than E. coli LepA,
the extension being N-terminal. All LepA domains are annotated (Tr-type G domain 86-245, LepA_C
Pfam PF06421, EFG_C PF00679). The N-terminal 60 residues
(MSMATTSLKLTLSSKPPPQHNHHHHLPVHFSNRTFHTLQSFNPSKLNLNNKTRRRRYKVF) contain no Asp or Glu, 13 Ser/Thr
and 10 Lys/Arg, the composition typical of a chloroplast transit peptide. No transit-peptide
predictor was run, so this is a compositional observation only. The G3/switch II motif DTPGH lies
at 160-164 (catalytic His164). The entry is a complete gene model, not a fragment.
