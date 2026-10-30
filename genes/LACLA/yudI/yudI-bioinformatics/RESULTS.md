# yudI (Q9CE84) bioinformatics: Dus subfamily placement and conserved residues

Query: KBase Dark Protein Atlas item CP006766.1_2177 (*Lactococcus lactis*, 334 aa),
filed on UniProt Q9CE84 (*L. lactis* subsp. *lactis* IL1403 yudI / L19272, 334 aa).

Scripts: `fetch_sequences.sh` (UniProt sequences and proteome Dus counts into `data/`),
`analyze.py` (pairwise alignments; output in `analysis_output.txt`). Run with
`bash fetch_sequences.sh && uv run python analyze.py > analysis_output.txt`.
Alignments are global (Biopython PairwiseAligner, BLOSUM62, gap open -10, extend -0.5);
identity is identical residues divided by the length of the shorter sequence.

## 1. Dashboard query vs Q9CE84

The two sequences are the same length and differ at one position: query E267 / Q9CE84 G267.
The MG1363 orthologue A2RN88 also has E at 267, so the IL1403 glycine is a strain
variant (or sequencing difference) in the C-terminal helical domain, away from the
catalytic and FMN-binding residues. Identity 99.7% (1 difference).

## 2. Identity to characterised and reference Dus proteins

| Protein | Identity to Q9CE84 |
|---|---|
| L. lactis MG1363 llmg_2209 (A2RN88) | 98.8% |
| B. subtilis Dus1 / YacF (P37567, BSU00810) | 57.4% |
| M. capricolum DusB (Q2SR34, MCAP_0837) | 43.8% |
| E. coli DusB (P0ABT5) | 36.4% |
| E. coli DusC (P33371) | 29.5% |
| E. coli DusA (P32695) | 29.0% |
| B. subtilis Dus2 / YfjN (O31546, BSU08030) | 28.0% |

Q9CE84 is closest to E. coli DusB of the three E. coli enzymes, consistent with
NCBIfam TIGR00737 (DusB-like) and InterPro IPR004652 on the UniProt entry. Among the
two B. subtilis paralogs it groups clearly with Dus1 (57.4%) and not Dus2 (28.0%).
M. capricolum DusB, the only Dus of a Mollicute and the one experimentally shown to
make D17, D20 and D20a (PMID:33685366), is also much closer to B. subtilis Dus1 (46.4%)
than to Dus2 (26.6%). Faivre et al. report that Mollicutes kept the DusB1 subgroup and
lost DusB2. Taken together, the lactococcal protein most likely belongs to the
Firmicute DusB1 subgroup, the same subgroup as the multisite M. capricolum enzyme.
This assignment is inferred from pairwise identity only; we could not access the
Faivre et al. full text to check which B. subtilis paralog they place in each
subgroup, and no phylogeny was built here.

## 3. Number of Dus enzymes in Lactococcus

UniProt reference proteomes searched for Pfam PF01207 or InterPro IPR001269/IPR035587:

- IL1403 (UP000002196): Q9CE84 only.
- MG1363 (UP000000364): A2RN88 (llmg_2209) only.

*L. lactis* therefore encodes a single Dus enzyme, like Mollicutes and unlike
B. subtilis (two) or E. coli (three). If lactococcal tRNAs carry D at more than one
position (D17, D20, D20a are the bacterial sites), this one enzyme would have to make
all of them. No tRNA modification map exists for L. lactis, so this is an expectation,
not an observation.

## 4. E. coli DusB functional residues mapped onto Q9CE84

UniProt P0ABT5 features mapped through the pairwise alignment:

| E. coli DusB feature | E. coli | Q9CE84 |
|---|---|---|
| Active site (proton donor) | C100 | C111 (conserved; motif NMGCPVPKV) |
| FMN binding 16-18 | P16 M17 A18 | P26 M27 A28 |
| FMN binding 70 | Q70 | Q80 |
| FMN binding 139 | K139 | K150 |
| FMN binding 200-202 | N200 G201 D202 | N213 G214 D215 |
| FMN binding 224-225 | G224 R225 | G237 R238 |

The catalytic cysteine and every FMN-binding residue annotated on E. coli DusB are
conserved, so the protein is an intact Dus enzyme rather than a degenerate paralog.

## Unresolved

- Which uridines the lactococcal enzyme modifies. The DusB1 placement and its being
  the only Dus in the genome suggest it could, like M. capricolum DusB, act on U17
  and U20/U20a, but this has not been tested in any Lactococcus or Streptococcus.
- Whether DusB1 vs DusB2 placement holds on a proper phylogeny with the Faivre et al.
  sequence set.
- No RB-TnSeq fitness data exist for L. lactis (`just fetch-fitness LACLA yudI`
  found no FEBA organism).
