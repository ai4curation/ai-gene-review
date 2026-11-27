# Irs2 (rat, F1MAL5) - manual literature summary

No deep-research API was available; this summary was compiled by hand from cached
publications in `publications/` and the UniProt record.

## Identity and architecture
- Rat Irs2 (RGD:69316, GeneID 29376), UniProt F1MAL5 (unreviewed TrEMBL, 1327 aa).
- N-terminal PH domain and IRS-type PTB domain (InterPro IPR001849, IPR002404; PROSITE PS50003, PS51064),
  followed by a long, largely disordered C-terminal tail (MobiDB-lite regions) carrying tyrosine
  phosphorylation motifs.
- [PMID:7675087 "Alignment of the sequences of IRS-2 and IRS-1 revealed a highly conserved amino terminus containing a pleckstrin-homology domain and a phosphotyrosine-binding domain, and a poorly conserved carboxy terminus containing several tyrosine phosphorylation motifs."]

## Molecular function: docking/adaptor for receptor tyrosine kinases
- IRS proteins act as an interface between SH2 proteins and activated insulin/IGF-1/cytokine receptors
  [PMID:7675087 "The protein IRS-1 acts as an interface between signalling proteins with Src-homology-2 domains (SH2 proteins) and the receptors for insulin, IGF-1"].
- Tyrosine-phosphorylated IRS-2 recruits p85 PI3K, SHP2 and Grb2 [Reactome:R-RNO-1168854 "Tyrosyl phosphorylation of IRS-1 and IRS-2 in response to insulin provides binding sites for specific proteins containing SH2 domains"].
- [PMID:22912850 "Phosphorylation of insulin receptor substrate (IRS)-2 on tyrosine residues is a key event in IGF-1/insulin signaling and leads to activation of the PI 3-kinase and the Ras/MAPK pathway."]

## Rat experimental data
- Fetal rat liver: IRS-2 is the dominant insulin-responsive substrate, with insulin-stimulated tyrosine
  phosphorylation and PI3K binding/activation from E15 [PMID:12891559 "robust PI3K binding and activation"].
- MSG insulin-resistant rats: adipose IRS-2 phosphorylation and association with PI3-kinase increased
  [PMID:12850498 "IRS-2 phosphorylation and association with PI3-kinase and Akt serine phosphorylation were increased"] (abstract only).
- Rat islet beta-cells: glucose induces Irs2 transcription/protein [PMID:16574657 "Glucose (> or = 6 mM) increased IRS-2 mRNA and protein levels in a dose-dependent manner"] (abstract only).
- Neonatal rat cardiomyocytes: Irs2 is an ET-1 immediate-early gene [PMID:18406357 "Irs2 was upregulated as an IEG by ET-1"] (full text).
- Fao rat hepatoma cells: insulin/IGF-1 promote 14-3-3 binding to IRS-2 via pSer573 (Akt-dependent),
  a negative-feedback site [PMID:22912850 "Insulin-stimulated interaction between endogenous IRS-2 and 14-3-3 was observed in rat hepatoma cells"] (full text).

## Physiology (mouse orthologue)
- Irs2 knockout mice develop type 2 diabetes from combined hepatic/muscle insulin resistance and beta-cell
  failure [PMID:9495343 "disruption of IRS-2 impairs both peripheral insulin signalling and pancreatic beta-cell function."].
  These are necessity phenotypes; downstream metabolic/proliferative processes are consequences of IRS-2-mediated signalling.
