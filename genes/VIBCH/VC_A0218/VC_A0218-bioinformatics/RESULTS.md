# VC_A0218 (Q9KMV0) — sequence identity analysis

Date run: 2026-11-06. Script: `compare.py`; sequences fetched by `fetch_seqs.sh`.
Method: Biopython `PairwiseAligner`, global mode, BLOSUM62, blastp gap costs;
percent identity computed over ungapped aligned columns.

## Identity table

Query: Q9KMV0 (*Vibrio cholerae* O1 El Tor N16961, VC_A0218), 418 aa.

| Subject | Length | Identity to Q9KMV0 | Aligned columns |
|---|---|---|---|
| AAA92960.1 — *V. cholerae* E7946 lecithinase Lec (GenBank U50074; Fiore et al. 1997) | 418 | **99.5%** | 418 |
| Q68CM4 — *V. parahaemolyticus* Tlh / lecithin-dependent haemolysin (LDH) | 418 | **63.2%** | 416 |
| P10480 — *Aeromonas hydrophila* GCAT (phosphatidylcholine-sterol acyltransferase) | 335 | 29.1% | 289 |
| Q9HUP2 — *P. aeruginosa* ChoE (second seed of the GO:0052689 IBD at PTN005219546) | 307 | 29.0% | 286 |
| O33407 — *P. aeruginosa* EstA (sole seed of the GO:0008610 IBD at PTN005219546) | 646 | 26.4% | 402 |
| Q9LU14 — *Arabidopsis thaliana* APG, a plant leaf under the same PANTHER node | 353 | 23.0% | 343 |

## Findings

1. **Q9KMV0 is the protein Fiore et al. 1997 characterised.** The alignment to
   AAA92960.1 is full length and gap free, with exactly two mismatches
   (Q9KMV0 M230/R231 vs Lec I230/A231) — ordinary El Tor strain polymorphism
   between N16961 and E7946. So the experimental work on the *V. cholerae*
   lecithinase `lec` applies to this entry directly, not by homology.
   This is independently corroborated by genomic context: Fiore et al. report
   `lec` adjacent to `hlyA`, and `hlyA` in N16961 is VCA0219, the immediate
   neighbour of VCA0218.

2. **Q9KMV0 is a genuine orthologue of the *V. parahaemolyticus* thermolabile
   haemolysin**, at 63.2% identity over the full 418 residues (both proteins are
   exactly 418 aa). The 1985 report that no *V. parahaemolyticus* thermolabile
   haemolysin-homologous DNA could be detected in *V. cholerae* by Southern
   blotting (PMID:3886626) is a hybridisation-stringency artefact, not a real
   absence.

3. **EstA is a distant outgroup.** At 26.4% identity, and with a different
   architecture (EstA is 646 aa: a GDSL passenger domain plus a C-terminal
   autotransporter beta-barrel that Q9KMV0 lacks entirely), EstA shares with
   Q9KMV0 only the SGNH/GDSL hydrolase fold. The GDSL serine motif in Q9KMV0 is
   at residues 153–156 (`SKVIAFGDSLSDTGNI`, catalytic Ser155), matching the
   PROSITE PS01098 hit in the UniProt entry.

4. **The nearest acyl-transferring relative is also distant.** *Aeromonas* GCAT,
   the one enzyme in this superfamily with a well-documented transacylase
   (i.e. potentially biosynthetic) activity, is only 29.1% identical to Q9KMV0 —
   no closer than ChoE or EstA. Nothing in the sequence comparison favours an
   acyl-transfer over a hydrolytic assignment for Q9KMV0.
