# dusA (Q92P85, SMc04235) notes

## Source of request

Reviewed from the KBase Dark Protein Atlas item
https://gene-annotate-dashboard.kbase.us/review/NZ_RPHN01000062.1_55
(Sinorhizobium meliloti, 398 aa). The protein comes from contig 62 of
*Ensifer meliloti* strain USDA1810 (NZ_RPHN01000062.1). Its residues 40-398 are
identical to UniProt Q92P85 (S. meliloti 1021 SMc04235, 359 aa); the extra 39
residues are an N-terminal extension from a different start-codon call (see
below). The review is filed under the 1021 reference proteome as `genes/RHIME/dusA`.

Dashboard call (tier A): "FMN-binding tRNA-dihydrouridine(20/20a) synthase DusA
(EC 1.3.1.91), reducing uridine residues at tRNA positions 20 and 20a to
dihydrouridine", with GO:0017150 tRNA dihydrouridine synthase activity,
GO:0010181 FMN binding and GO:0006400 tRNA modification. Prior annotations:
eggNOG dusA (U20/U20a), Pfam PF01207, KEGG K05539.

**Dashboard verdict: supported.** The call matches the HAMAP and PANTHER
subfamily assignments on the query and all prior annotations. The annotator was
right to set aside the "tRNA-U16,U17" labels on the Pseudomonas syringae Fitness
Browser homologs (49%): U16 and U17 are the DusC and DusB sites, and those labels
contradict the DusA subfamily models. It was also right not to turn the fitness
data into a stress role. Two refinements:
- The GO terms can be sharpened to the position-specific activities already in
  GOA (GO:0102264 and GO:0102266) and to GO:0002943 tRNA dihydrouridine synthesis.
- The dashboard did not notice that the protein is a mosaic of gene-model calls.
  This does not change the function call.

## Evidence

- Subfamily: HAMAP MF_02041 (DusA_subfam), InterPro IPR004653 (DusA), NCBIfam
  PRK11815, Pfam PF01207, and the PROSITE Dus conserved site (UniProt Q92P85;
  dashboard InterProScan HAMAP 27-389 and PANTHER 29-393 on the 398-aa model).
- Catalytic Cys conserved: E. coli DusA C114 -> Q92P85 C83 (NVGCPSDRV). All
  MF_02041 FMN-binding residues are conserved except E. coli P32 (absent from the
  truncated model) and L34 (present as I2),
  as are the tRNA-contact residues N111 and R201 and the subfamily
  signature residues R314 and R317 (K198 -> R). Identity to E. coli DusA is 53.1%
  over 311 aligned columns (`dusA-bioinformatics/RESULTS.md`).
- E. coli DusA is the U20/U20a enzyme [PMID:29294097 "DusC and DusB are mono-site
  specific flavoenzymes involved in D16 and D17 biosynthesis, respectively, while
  DusA is a U20/U20a bi-site specific enzyme"]. COG0042 genes were first shown to be
  the tRNA dihydrouridine synthases by E. coli deletions [PMID:11983710].
- FMN cofactor and catalytic Cys from Thermus Dus (the D20/D20a enzyme)-tRNA
  structures [PMID:22123979 "C5 of the U20 uracil ring is covalently cross linked to
  the thiol group of Cys93"].
- The tRNA orientation is set by subfamily "binding signatures" [PMID:25902496].
- In E. coli, DusA is the most active Dus in vivo and in vitro and uses NADPH
  [PMID:39460624 "revealing DusA as the most active enzyme, followed by DusB"]. It
  binds tRNA in two steps and enhances translation at specific codons [PMID:42080256].
- Brucella ovis DusA (BOV_RS04255, 56.4% identity per the dashboard's PaperBLAST
  panel; same order Hyphomicrobiales) is
  listed in that organism's flavoproteome as a tRNA dihydrouridine20/20a synthase
  (PMID:35315701; a comparative assignment, not an assay).

## Gene model

- Q92P85 (and RefSeq WP_010969552.1, also used on the USDA1810 contig) starts at
  MIDWTD, which aligns to E. coli DusA M33. Of the HAMAP FMN-binding feature at
  E. coli 32-34 (P-M-L), only P32 is missing (L34 is present as I2); the codon for
  it lies just upstream in an open frame in both strains. The truncation
  explains the UniProt caution "Lacks conserved residue(s) required for the
  propagation of feature annotation".
- Current RefSeq for the 1021 locus (SM_RS09780, WP_015241224.1, 385 aa) starts 26
  codons upstream and contains the motif. The KBase 398-aa model starts 39 codons
  upstream in USDA1810.
- The extensions in the two strains differ. In USDA1810 a tyrosine
  recombinase/integrase (CN234_RS21645) meets dusA 5'-to-5'. This is the
  dusA-associated integrase island architecture, in which the island supplies a new
  dusA 5' end [PMID:25883135 "The 5′ portion of the dusA gene affected by the
  integration is replaced by a new 5′ end (white) provided by the GEI"].
  Sinorhizobium fredii USDA 257 is among the genomes with such islands (same paper).

## Fitness data (from the dashboard; Fitness Browser not reachable from here)

- S. meliloti 1021 SMc04235: fitness +3.0 (t = 15.7) in 10 mM perchlorate, i.e.
  mutants are fitter. Klebsiella michiganensis homolog (48%): -4.1 in 0.5 mM CoCl2.
- These are single-condition phenotypes. They do not define a function and are not
  used for GO annotation. A redox link is plausible, since E. coli DusA activity
  depends on NADPH and Dus activities respond to paraquat (PMID:39460624), but it is
  untested.

## Caveats

- No experimental work exists on any rhizobial DusA. Function and site
  specificity are inferred from the E. coli and Thermus enzymes plus the subfamily
  models.
- Q92P85 has no IBA rows, although E. coli DusA has IBAs for GO:0017150,
  GO:0002943 and GO:0005829 (QuickGO, 2026-10-30). Q92P85 is in PANTHER
  PTHR42907:SF1. I did not check why the PAINT node does not reach this entry.
