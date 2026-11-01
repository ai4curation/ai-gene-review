# LOC541618 (ZmMPK5; UniProt K7VAM9) - manual literature research

No deep-research API was available; this file summarizes literature read directly from the
cached publications (`publications/PMID_*.md`) and NCBI Gene 541618.

## Identity

- NCBI Gene 541618 (LOC541618, "MAP kinase 2"), aliases ZmMPK5, MPK5, MPK6-2, mpk2;
  B73 v4 Zm00001d045310 / GRMZM2G020216; v5 Zm00001eb376640 (chromosome 9).
- UniProt K7VAM9 (TrEMBL), 398 aa, TEY-type MAP kinase (CDD cd07858 STKc_TEY_MAPK; PANTHER PTHR24055).
- The ZmMPK5 cDNA (GenBank AB016802) was cloned from senescent maize leaves
  [PMID:10589842 "Subsequently two MAPK cDNAs were isolated from a cDNA library constructed using mRNAs
  from senescent leaves"]. Its translation matches K7VAM9 except for a short stretch near the
  ATP-binding lysine (see `LOC541618-bioinformatics/RESULTS.md`).
- The anti-ZmMPK5 antibody used in later work was raised against the C-terminal peptide
  [PMID:20693409 "The peptides for ZmMPK5-C (EEQMKDLIYQEALAFNPDYQ) corresponding to the C-terminus of
  ZmMPK5 were synthesized"], which is residues 379-398 of K7VAM9.
- Closest Arabidopsis homolog by pairwise identity is MPK6 (86.7%), a group A MAPK
  (file:MAIZE/LOC541618/LOC541618-bioinformatics/RESULTS.md).

## Kinase activity

- Senescence / temperature up-shift: a 45-kDa MBP-phosphorylating kinase was proposed to be ZmMPK5
  [PMID:10589842 "suggesting that the 45-kDa protein kinase is encoded by ZmMPK5"] (abstract only).
- ABA: the ABA-activated 46-kDa MBP kinase in maize leaves was identified as ZmMPK5 (Ding et al. 2009,
  cited in [PMID:20693409 "A previous study showed that the ABA-activated a 46 kDa MBP kinase is ZmMPK5 in leaves of maize plants (Ding et al., 2009)."]); not cached here.
- Brassinosteroid: immunoprecipitated ZmMPK5 phosphorylates MBP in an in-gel assay and is activated by BR
  [PMID:20693409 "Kinase activity in the immunocomplex was determined by an in-gel kinase assay as described above."];
  activation depends on apoplastic H2O2 and is blocked by MAPKK inhibitors (PD98059, U0126).
- Substrates: ZmMPK5 immunocomplexes phosphorylate recombinant ZmMAP65-1a
  [PMID:23956414 "a strong phosphorylation band was detected, suggesting that ZmMPK5 directly phosphorylates ZmMAP65-1a in maize."]
  and ZmABA2 (a short-chain dehydrogenase/reductase, xanthoxin dehydrogenase) at Ser173, increasing ZmABA2 activity and stability
  [PMID:26096642 "Phosphorylation of Ser173 in ZmABA2 by ZmMPK5 was shown to increase the activity of ZmABA2 and the protein stability."].
  Caveat: immunocomplex assays from plant extracts cannot exclude co-precipitating kinases.

## Physiological roles (perturbation / expression evidence)

- BR-induced antioxidant defence: ZmMPK5 is placed in a positive feedback loop amplifying apoplastic
  H2O2 via NADPH oxidase (rboh) gene expression
  [PMID:20693409 "It was found that the BR-induced initial apoplastic H2O2 production activates ZmMPK5, which is involved in the self-propagation of apoplastic H2O2 via the regulation of NADPH oxidase gene expression in the BR-enhanced antioxidant defence systems."]
  Evidence is mostly pharmacological (MAPKK inhibitors), plus protoplast transient expression/silencing in PMID:23956414.
- ABA content: RNAi silencing of ZmMPK5 in protoplasts lowers ABA content, overexpression raises it
  [PMID:26096642 "These results suggest that both ZmMPK5 and ZmABA2 coordinately regulate the biosynthesis of ABA."].
- Heterologous overexpression in tobacco enhanced salt/oxidative stress tolerance and PR gene expression
  [PMID:23952812 "ZmMPK5 is involved in salt stress, oxidative stress and pathogen defence signalling pathways"] (abstract only).

## Location

- BiFC of ZmMPK5 with ZmABA2 gave signal in nucleus and cytosol
  [PMID:26096642 "Strong yellow fluorescence was observed in the nucleus and in the cytosol (Figure 1 d), suggesting that ZmMPK5 can interact with ZmABA2 in these subcellular sites."].
  No direct localization of ZmMPK5 alone was found in the cached papers.

## Not this gene / uncertain

- PMID:32996127 studies "ZmMPK6" in maize A188 (herbivory, DIMBOA). Abstract only; which locus
  it is cannot be established from the abstract, so it is not used for this gene.
- PMID:17095711, PMID:19936069, PMID:18937034 are large-scale cDNA/transcriptome sequencing papers (no function).
