# FKBP62 / ROF1 (At3g25230, UniProt Q38931) - manual literature synthesis

No deep-research provider was available for this session; this synthesis was compiled manually
from cached publications (publications/PMID_*.md), the UniProt record and a PubMed search
("(ROF1 OR FKBP62) AND Arabidopsis", 12 hits, Oct 2026).

## Identity and domain architecture

- ROF1 (ROTAMASE FKBP 1) = AtFKBP62, a 551-aa, ~62 kDa multidomain FKBP. It was cloned as a
  homolog of human FKBP59/FKBP52 (FKBP4) [PMID:8914512 "The deduced amino acid sequence of ROF1
  predicts a 551-amino acid, 62 kDa polypeptide which is 44% identical to human FKBP59"].
- Architecture: three N-terminal FKBP12-like domains, a TPR repeat region and a putative
  calmodulin-binding region [PMID:8914512 "ROF1 contains three FKBP12-like domains in the N-terminal
  portion of the protein (in contrast to two domains in mammalian FKBP59), an internal repeat structure
  associated with protein-protein interactions (tetratricopeptide repeats), and a putative calmodulin
  binding domain near the C-terminal region of the protein"]. UniProt: FKBP domains 57-145, 173-262,
  290-383; TPR repeats 400-433, 449-482, 483-516.
- Only FKBD1 is predicted to be a catalytically competent PPIase; FKBD2/3 are degenerate
  [PMID:23133621 "ROF1 contains an FK506 Binding Domain (FKBD) with PPIase activity, (FKBD1), two
  degenerate FKB..."]. PPIase activity in UniProt is "By similarity"; I found no published direct
  rotamase assay on recombinant ROF1.
- Close paralog ROF2/FKBP65 (85% identity) [PMID:17080288].

## HSP90 co-chaperone function

- ROF1 binds HSP90 [PMID:17080288 "By protein interaction assays, it was demonstrated, that ROF1 is a
  novel partner of HSP90."]. Binding is through the TPR domain to HSP90.1 [PMID:19366428 "ROF1 binds
  heat shock proteins HSP90.1 via its tetratricopeptide repeat domain"].
- ROF1 copurifies with HSP90-AGO1 complexes in tobacco BY-2 lysate in an HSP90-dependent manner,
  though NtFKBP62/65 did not affect RISC assembly [PMID:22045333].
- ROF1 heterodimerizes with ROF2 [PMID:19876748 "ROF2 has been shown to interact with ROF1, to form
  heterodimers"].

## Heat stress / acquired thermotolerance

- Cytoplasmic in normal conditions; heat induces nuclear relocalization of the ROF1-HSP90.1
  complex, dependent on HsfA2 [PMID:19366428].
- rof1 knockouts fail long-term acquired thermotolerance and show reduced HsfA2-dependent sHSP
  expression; overexpressors survive 45 C better [PMID:19366428].
- ROF2 acts antagonistically, as negative feedback on HsfA2 [PMID:19876748].
- During heat-stress recovery, ROF1 and HSP90.1 are bound by the selective autophagy receptor
  NBR1 and degraded, attenuating HsfA2 targets and heat-stress memory [PMID:32967551].
- Proteomics of rof1/rof2 mutants after heat acclimation shows altered protein quality control,
  proteasome (CDC48) and other pathways [PMID:38250364].

## Phosphoinositide binding, osmotic stress and germination

- Isolated by PI(3)P / PI(3,5)P2 affinity chromatography from salt-stressed cells; recombinant ROF1
  and FKBD1 bind PI(3)P and PI(3,5)P2 in lipid-overlay assays [PMID:23133621].
- GFP-ROF1 in tobacco is cytoplasmic and at the cell periphery; root immunofluorescence shows
  cytoplasmic localization with membrane association, no nuclear signal [PMID:23133621].
- ROF1 mRNA/protein accumulate under salt; rof1 shows delayed germination on NaCl/mannitol, abolished
  in rof1 rof2; overexpressors germinate better. No germination difference without stress
  [PMID:23133621].
- rof1 rof2 double mutants are also sensitive to intracellular acidification (ROF2 paper)
  [PMID:22268595].

## Expression

- Induced by wounding and NaCl [PMID:8914512], heat [PMID:17080288], salt [PMID:23133621], high light
  (RRGD recovery-induced downregulation locus) [PMID:37947266], malondialdehyde [PMID:14996219].
