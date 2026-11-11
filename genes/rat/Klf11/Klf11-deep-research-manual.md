# Klf11 (rat, E9PTS6) - manual literature synthesis

No deep-research API was available in this session; this synthesis was assembled manually from
cached publications (publications/PMID_*.md) and PubMed searches (title search for KLF11/TIEG2,
108 hits, of which the functionally foundational papers were cached and read). Rat-specific
experimental literature on Klf11 is essentially limited to expression profiling; mechanism comes
from the human and mouse orthologs (KLF11/TIEG2, UniProt O14901; mouse Klf11, Q8K1S5).

## Identity and domain architecture

- Rat Klf11 (E9PTS6, 501 aa, unreviewed TrEMBL; RGD:1306646; GeneID 313994) carries the three
  C-terminal C2H2 zinc fingers of the Sp/KLF family (PROSITE PS50157 at 383-412, 413-442, 443-470)
  and a KLF11_N CDD domain (cd21584). PANTHER PTHR23235:SF65 (KRUEPPEL-LIKE FACTOR 11).
- TIEG2 was cloned as a TGF-beta-inducible Sp1-like gene: "Biochemical characterization reveals
  that TIEG2 is a nuclear protein, which, as predicted from the primary structure, specifically
  binds to an Sp1-like DNA sequence in vitro and can repress a promoter containing Sp1-like binding
  sites" [PMID:9748269].
- Preferred binding site: "the most probable GC-box sequence that binds KLF11 as T/G-GGGCGGGG/A"
  [PMID:15774581].

## Repression mechanism

- "TIEG2 ... represses transcription through recruitment of the mSin3A-histone deacetylase complex"
  via an N-terminal alpha-helical repression motif (alpha-HRM) in repression domain R1 [PMID:11438660].
- ERK2 phosphorylation of sites adjacent to the SID "disrupts the SID-mSin3A interaction and thereby
  inhibits TIEG2's repression activity" [PMID:12006497].
- Targets repressed: Smad7 ("KLF11 represses TGF-beta-induced transcription from the Smad7 promoter
  by recruiting mSin3a via GC-rich sites" [PMID:15300592]); SOD2 and catalase ("these genes are
  bonafide targets of KLF11" [PMID:12970187]); caveolin-1 ("KLF11 acts as a dominant repressor of
  the caveolin-1 gene" [PMID:15531587]); Bcl-XL ("inhibits transcription driven by the Bcl-X(L)
  promoter" [PMID:17308981]).

## Activation

- KLF11 also activates some promoters: "KLF11 binds and activates the human insulin promoter in beta
  cells under high-glucose levels" [PMID:15774581]; Pdx-1 activation is p300-dependent ("KLF11
  interacts with the coactivator p300 via its zinc finger domain in vivo to mediate Pdx-1
  activation" [PMID:19843526]); MAO-B ("TIEG2 increased MAO B gene expression" [PMID:15024015]).

## Cellular / physiological roles

- Growth inhibition: overexpression "inhibits cell proliferation" [PMID:9748269]; KLF11 "inhibits
  cell growth in vitro and in vivo, and suppresses neoplastic transformation" [PMID:12970187].
- Apoptosis: "TIEG2 induces Caspase3-dependent apoptosis in murine OLI-neu cells" [PMID:17308981].
- Human genetics: rare variants segregate with early-onset type 2 diabetes (MODY7) and impair
  transcriptional activity [PMID:15774581]; the Q62R association did not replicate in 8,676 people
  [PMID:17130512, not cached].
- Mouse knockout: "Hematopoiesis at all stages of development was normal in the KLF11(-/-) mice"
  and mice showed no evident pathology [PMID:15607700] - basis of the NOT hemopoiesis ISO row.

## Rat-specific data

- Neonatal rat cardiomyocytes: endothelin-1 downregulates Klf11 mRNA, "the decrease in expression
  of Klf11 and Klf15 was sustained over at least 6 h" [PMID:18406357, full text]. This is an
  expression response only.

## Gaps

- The human source for the "regulation of G1/S transition of mitotic cell cycle" annotation
  transferred to rat was not identified among the cached papers.
- No rat protein-level, DNA-binding or loss-of-function data for Klf11.
