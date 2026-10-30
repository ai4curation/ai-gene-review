# LOC541618 (K7VAM9, ZmMPK5) bioinformatics

Script: `ortholog_identity.py` (global Needleman-Wunsch, BLOSUM62, gap open -10 / extend -0.5;
sequences fetched live from UniProt REST). Raw output: `ortholog_identity_output.txt`.

## Motifs in K7VAM9 (398 aa)

- ATP-binding subdomain II motif VAIKK at 93 (Lys97 = UniProt FT BINDING 97).
- Catalytic loop HRDLKP at 191 (Asp193 = UniProt proton-acceptor ACT_SITE 193).
- Activation-loop phosphorylation motif TEY at 225 (Thr225-Glu226-Tyr227): a TEY-type (group A/B) plant MAPK.
- The C-terminal peptide EEQMKDLIYQEALAFNPDYQ used to raise the anti-ZmMPK5 antibody in PMID:20693409
  occurs at residues 379-398, i.e. exactly at the C-terminus of K7VAM9.

## Identity to characterized plant MAPKs

| Protein | Length | Identity over aligned columns |
|---|---|---|
| Arabidopsis MPK6 (Q39026) | 395 | 0.867 |
| Arabidopsis MPK3 (Q39023) | 370 | 0.758 |
| Arabidopsis MPK4 (Q39024) | 376 | 0.690 |

K7VAM9 is most similar to Arabidopsis MPK6 (group A MAPK), consistent with the NCBI Gene alias
"MPK6-2" and with the N-terminal extension (residues 1-34, disordered) shared with AtMPK6.
This is pairwise identity only, not a phylogeny.

## Note on the original ZmMPK5 cDNA

The translation of GenBank AB016802 (BAA74734.1, the cDNA cited as ZmMPK5 in PMID:20693409 and
PMID:23956414) is identical to K7VAM9 except in a short stretch around residues 75-98, where it
reads ...SAVNSETAAEGGPSKKIA... instead of ...SALNSETAEQVAIKKIA..., which would remove the invariant
ATP-binding lysine (VAIK). The genome-derived K7VAM9 sequence retains the canonical motif, so the
difference is most likely a sequencing error in the 1999 cDNA. (Comparison done by eye from
NCBI efetch output of AB016802 fasta_cds_aa; not scripted.)
