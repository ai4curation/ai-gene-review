# Klf10 (rat, UniProt O08876) - manual literature synthesis

No deep-research API was available; this synthesis was compiled manually from cached
publications (publications/PMID_*.md) and PubMed searches.

## Identity
- Krueppel-like factor 10 (Klf10; synonyms TIEG, TIEG1, Cpg20), 480 aa, three C-terminal
  C2H2 zinc fingers (residues 369-451), member of the Sp1/KLF C2H2 zinc-finger family
  [file:rat/Klf10/Klf10-uniprot.txt "Belongs to the Sp1 C2H2-type zinc-finger protein family"].
- Rat GeneID 81813, RGD:621652.

## DNA binding and transcriptional repression
- UniProt: "Transcriptional repressor which binds to the consensus sequence 5'-GGTGTG-3'"
  (curated by similarity and PMID:20070857).
- TIEG1 binds the Bmal1 promoter and represses it through two juxtaposed GC boxes near the
  transcription start site [PMID:20070857 "TIEG1 bound to Bmal1 gene promoter and repressed its
  transcriptional activity through two juxtaposed GC boxes near the transcription initiation site"].
- KLF10 directly represses the proximal Pepck promoter in mouse liver [PMID:20385766 "functional data
  showed that the proximal Pepck promoter is repressed directly by KLF10"].
- Mechanism: the N-terminal alpha-helical repression motif (alpha-HRM, R1) of TIEG1, like that of
  TIEG2/KLF11, binds the PAH2 domain of the mSin3A-HDAC corepressor [PMID:11438660 "the conserved
  α-helical domains from TIEG1, BTEB1, BTEB3, and BTEB4 pulled down mSin3A"].

## Transcriptional activation (context dependent)
- TIEG increases Smad2 transcription and enhances TGF-beta/Smad signalling [PMID:12244575 "TIEG
  increases transcription of the Smad2 gene but not the Smad3 or Smad4 genes"].
- TIEG1 binds and activates the Runx2 promoter in osteoblasts [PMID:21559363 "TIEG1 directly binds to
  and activates the Runx2 promoter"].

## Circadian clock
- Rat-1 fibroblasts: glucose induces Tieg1; knockdown shortens circadian period
  [PMID:20070857 "siRNA-mediated knock-down of TIEG1 caused period shortening of cellular
  bioluminescence rhythms driven by Bmal1-luciferase and Per2-luciferase reporters"].
- Mouse liver: Klf10 is a CLOCK-BMAL1 target and a clock output regulating gluconeogenic and lipogenic
  genes [PMID:20385766 "establish KLF10 as a required circadian transcriptional regulator that links the
  molecular clock to energy metabolism in the liver"]; Klf10-/- males show "postprandial and fasting
  hyperglycemia".

## Bone
- Klf10 KO mice: female-specific osteopenia; calvarial osteoblasts mineralize slowly
  [PMID:21559363]. KO osteoblasts support fewer osteoclasts (RANKL down, OPG up) [PMID:20087894
  "significantly fewer osteoclasts developed in the KLF10 KO OB cocultures compared with the
  osteoclasts that developed in the wild-type OB co-cultures"]. These are indirect effects.

## Expression responses
- Induced by TGF-beta and other cytokines (named TGF-beta inducible early gene) [PMID:20087894].
- Neonatal rat cardiomyocytes: endothelin-1 gives a small (<2-fold) sustained increase in Klf10 mRNA
  [PMID:18406357 "The increases in expression of Klf9 and Klf10 were relatively small"].
- Overexpression induces apoptosis in pancreatic epithelial cells [PMID:9153278].

## Unknowns
- Which rat genes are direct Klf10 targets in vivo; how the same protein activates some promoters
  (Smad2, Runx2) and represses others (Smad7, Bmal1, Pepck).
- No identified source for the mouse "somatic stem cell population maintenance" annotation.
