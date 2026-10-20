# PRKCH__C0HM02 (uPEP2, PRKCH uORF2 peptide) - review notes

## Identity

- UniProt C0HM02 (PKHUO_HUMAN), 26 aa, MASRGALRRCLSPGLPRLLHLSRGLA. PE1. Gene name in UniProt is the
  host symbol PRKCH (HGNC:9403); no HGNC symbol of its own, hence the `PRKCH__C0HM02` folder.
- Encoded by uORF2 in the 5' leader of the PRKCH (PKC-eta) mRNA, starting at -148 relative to the
  main-ORF AUG [PMID:19797084 "It encodes a small putative peptide of 26 amino acids, starting at position −148 relative to the first AUG of the main ORF."]
- Pfam PF21952 / InterPro IPR054137 (PRKCH_uORF2). The 2021 paper reports the peptide sequence
  conserved in several mammals [PMID:34593629 "The conserved uORF2 sequences reside on the same transcripts as PKC-η homologs and encode closely related peptides of the same length"].

## Literature (PubMed search: uPEP2 / PKC-eta uORF / PRKCH uORF) - only three primary papers, all one lab (Livneh, Ben-Gurion Univ.)

### PMID:19797084 Raveh-Amit et al. 2009 MCB (full text cached)

- Purely a cis-regulatory study of the 5' UTR with luciferase reporters; uAUG -> ACG mutations.
  The peptide itself was never detected or tested here; it is called a "putative peptide".
- Both uORFs repress basal translation of the main ORF [PMID:19797084 "Our results demonstrate that PKCη, a signaling molecule, has two functional conserved uORFs that constitutively suppress its expression under normal growth conditions."]
- Amino-acid starvation induces PKC-eta translation via GCN2-dependent leaky scanning *past* uORF2
  [PMID:19797084 "providing evidence that under these conditions ribosomes bypass uORF2 by leaky scanning"].
  So, under stress, the uORF2 peptide is made *less*, not more; the stress induction is a property
  of the mRNA and the eIF2/GCN2 system.
- Conclusion: this paper is the source of 4 GOA rows (negative regulation of translation; positive
  regulation of translation in response to stress; cellular response to amino acid starvation;
  translation regulator activity). None of them describes an activity of the peptide. They describe
  the act of translating the uORF (ribosome occupancy) on the PRKCH mRNA in cis.

### PMID:34593629 Jayaram et al. 2021 PNAS (full text cached)

- Peptide exists: ribosome profiling, uORF2-luciferase fusion, and IP of an ~3 kDa band with an
  anti-uPEP2 antibody [PMID:34593629 "the presence of an ∼3-kDa peptide that was not immunoprecipitated by a control IgG antibody was depicted"].
- Fig 1E: uORF2 start-codon mutation up-regulates PKC-eta; the authors themselves call this a cis
  effect [PMID:34593629 "in accordance with our previous studies demonstrating that uORF2 acts as a cis-repressor element that suppresses expression of PKC-η and maintains its low basal levels"].
  This is the basis of the IMP "negative regulation of translation" row. A start-codon mutation removes
  both the translation event and the peptide, so it cannot attribute the effect to the peptide.
- Trans activity (synthetic peptide, in vitro kinase assays on immunoprecipitated PKCs, MBP substrate):
  inhibits PKC-eta, -delta, -theta, -epsilon (IC50 ~2 uM), not PKC-alpha, -gamma, -zeta
  [PMID:34593629 "We found that uPEP2 inhibited the kinase activity of PKCη with a half-maximal inhibitory concentration (IC50) of about 2 μM."]
  [PMID:34593629 "uPEP2 also inhibited the kinase activity of other novel PKC isoforms, including PKCδ, PKCθ, and PKCε, with a similar IC50 of ∼2 μM."]
- Binding: pulldown with tagged peptide [PMID:34593629 "uPEP2 was found to interact with the four novel PKC isoforms but not with PKC-γ or PKC-ζ"].
- Pseudosubstrate mechanism: A6S/A6T converts it to a substrate [PMID:34593629 "uPEP2 transformed from an inhibitor into a favorable substrate for PKC-η and PKC-ε but not for PKC-α"].
- Caveats: the peptide is used at micromolar concentrations, exogenously (myristoylated for cell
  entry); the IC50 is ~2 uM and endogenous concentration is unknown. Binding was by pulldown from
  overexpressing lysates, so "direct" is inferred, not shown with purified proteins. Kinase assays
  used immunoprecipitated kinases (could include associated proteins).
- Endogenous CRISPR deletion of uORF2 in MCF-7: raised PKC-eta, -epsilon, -delta protein and
  proliferation. PKC-epsilon/-delta are encoded elsewhere, so their rise is a genuine trans effect,
  but the mechanism (stability vs translation) is not established; the authors suggest stability
  [PMID:34593629 "Our results suggest that binding of the uORF2-translated peptide to novel PKCs reduce their catalytic activity and protein phosphorylation, which may affect their protein stability."]

### PMID:41698898 Liju et al. 2026 Signal Transduct Target Ther (full text cached)

- Mostly about PKC-eta/YAP in TNBC. Exogenous myristoylated uPEP2 lowers PKC-eta protein and
  phenocopies PKC-eta KO [PMID:41698898 "Treatment of 4T1 and MDA-MB-231 cells with uPEP2 resulted in a reduction in PKCη and YAP/TAZ expression"].
- Calls uPEP2 a "PKCη degrader"; mechanism of degradation not dissected. Pharmacological, not
  physiological. Not used for GO terms.

## Decisions

- Kinase inhibitor activity: well supported in vitro; refine to GO:0008426 protein kinase C inhibitor
  activity (is_a GO:0030291; all inhibited targets are novel PKCs).
- PKC binding IPIs (4 partners: PRKCH P24723, PRKCE Q02156, PRKCQ Q04759, PRKCD Q05655): refine
  GO:0120283 -> GO:0005080 protein kinase C binding (more specific; all partners PKCs).
- All translation / starvation rows: REMOVE. They describe a cis effect of the uORF (the mRNA and the
  scanning ribosome) not an activity of the peptide; under starvation uORF2 is bypassed. Full text
  of both papers read; the authors themselves call it cis. The participation test (CLAUDE.md) fails:
  the peptide performs no step of translation regulation in any experiment.
- No NEW BP: inhibitor activity already implies negative regulation of PKC activity; endogenous
  cell-level effects (proliferation) are confounded by the cis effect on PKC-eta.
- No location data for the endogenous peptide.

## Open questions

- Endogenous uPEP2 concentration vs 2 uM IC50; does endogenous peptide inhibit PKC in cells?
- Can the cis (translation-of-uORF) and trans (peptide) effects be separated, e.g. by a
  synonymous-frame/missense uORF2 (A6S, or scrambled peptide keeping ORF length and Kozak)?
- Mechanism of novel-PKC protein loss (degradation pathway).
