# lap (PA2939, Q9HZQ8) — PaAP secreted aminopeptidase — review notes

No deep-research provider was available; the notes below are from my own
reading of the cached publications (`publications/PMID_*.md`) and the UniProt
record (`lap-uniprot.txt`).

## Identity

- UniProt Q9HZQ8 (LAP_PSEAE), 536 aa precursor, signal peptide 1-24, peptidase
  M28 family, M28A subfamily; PA domain + M28 Zn-peptidase domain. PANTHER
  PTHR12147:SF26. MEROPS M28.003/M28.008. Crystal structures 8AC7, 8AC9, 8ACG,
  8ACK, 8ACR.
- Names: PaAP, LAP, PaaP (Zhao et al. 2018 named the gene paaP)
  [PMID:30047246 "PaAP, encoded by PA2939 that we named the gene as paaP in this study"].

## Activity

- Discovery: aminopeptidase activity on Leu-pNA in culture filtrates; AP56
  converted to active AP28 by heating with elastase; Zn-chelator sensitive;
  N-terminal sequences matched PA2939 [PMID:11533066 "Using leucine-p-nitroanilide (Leu-pNA) as a substrate, we demonstrated
  aminopeptidase activity in the culture filtrates of several Pseudomonas
  aeruginosa strains"; "This activity was inhibited by Zn
  chelators but not by inhibitors of serine- or thiol-proteases, suggesting that
  AP(28) is a Zn-dependent enzyme"]. Abstract only in cache; UniProt
  curated CC FUNCTION/CATALYTIC ACTIVITY from the full text (ECO:0000269) adds
  that peptides with a free N-terminus are hydrolysed (Leu > Met > Ala).
- Per the 2024 review, Cahan et al. also showed hydrolysis of Leu-Ala and Ala4
  (free N-termini) and no cleavage of N-blocked peptides
  [PMID:39126017 "Leu-Ala and Ala4, having free N-termini, are both cleaved readily [17]"].
  This is direct evidence of peptide-bond hydrolysis in peptides, i.e. the
  basis of the PseudoCAP IDA "proteolysis" row.
- Promiscuous aminopeptidase on unstructured regions of peptides and proteins;
  autoinhibited by its C-terminal propeptide [PMID:37386135 "PaAP is a
  promiscuous aminopeptidase acting on unstructured regions of peptides and
  proteins"].
- Binuclear zinc active site confirmed by crystal structure
  [PMID:37386135 "The active site contains two zinc ions; Zn1 is coordinated by D306, H296 and D369, while Zn2 is coordinated by E341, H467 and D306."]
  (note: the 2024 review numbers the first Asp as 308; I do not rely on the
  residue number). So the specific MF is metalloaminopeptidase activity
  (GO:0070006, is_a aminopeptidase activity and is_a metalloexopeptidase activity).
- Lys-pNA and Leu-pNA are best substrates; AP56 and AP28 have the same kinetics
  on small substrates [PMID:34133429 "Lys-pNA was hydrolyzed 2 to 3-fold more rapidly than Leu-pNA"].
- EC: UniProt gives EC 3.4.11.1 (leucyl aminopeptidase). EC 3.4.11.1 is formally
  the M17 cytosol aminopeptidase; PaAP is an M28 SGAP-like enzyme. I therefore do
  not propose the EC-linked GO term and stay at metalloaminopeptidase activity.

## Activation, secretion, location

- Secreted via the Xcp type II secretion system, activated extracellularly by
  LysC cleavage of the C-terminal propeptide (Lys512-Ala513) [PMID:34133429
  "pointed at LysC as the principal
  activating protease, cleaving a Lys512-Ala513 peptide bond at the C-terminal end
  of pro-PaAP"]; review [PMID:39126017 "Elastase, LasA protease, LysC endopeptidase, and PaAP are secreted via the type 2 secretion system (T2SS)"].
- Braun et al. 1998 (PMID:9642203) found the uncharacterised SGAP homologue
  accumulating in culture medium of protease-deficient strains; N-terminal
  sequence (residues 25-34) shows the signal peptide removed. Full text not
  available (PMC restricts). The 2024 review cites it as the source for Xcp-dependent
  outer membrane passage [PMID:39126017 "the resulting pro-PaAP is secreted across the outer membrane via the Xcp export machinery (step 2) [23]"].
- Extracellular; abundant in biofilm matrix and in outer membrane vesicles,
  especially from CF isolates [PMID:16807039 "The aminopeptidase PaAP (PA2939) was highly enriched
  in vesicles from CF isolates."].

## Biology

- Nutrient acquisition: completes extracellular protein digestion begun by
  endopeptidases; RpoS-controlled public good [PMID:32184248 "Our results suggest that PaAP is an integral
  part of a proteolytic sequence in P. aeruginosa that permits the utilization of
  protein as a nutrient source."].
- Biofilm modulation: deletion increases early attachment, late cell death and
  biofilm disruption; catalytic activity required [PMID:30047246 "PaAP functioned
  extracellularly and aminopeptidase catalytic activity was essential for its
  effect on biofilm development."]; OMV-associated anti-biofilm/detachment
  activity [PMID:31744920 "OMVs from PaAP-expressing strains
  could cause protease-mediated biofilm detachment"]. These are pleiotropic
  phenotypes downstream of nutrient supply; I do not propose biofilm process terms.
- Regulation: LasR/LasI quorum sensing and RpoS (principal activator) [PMID:39126017].

## Annotation decisions (summary)

- Aminopeptidase activity (EXP, IEA) and metalloexopeptidase activity (IEA):
  correct but general; MODIFY to metalloaminopeptidase activity GO:0070006
  (Zn-chelator inhibition + binuclear Zn site in the crystal structure).
- Proteolysis (IDA PseudoCAP, IBA, IEA): ACCEPT. Process-level term for a
  peptidase; consistent across rows.
- Extracellular region (EXP, IEA): ACCEPT.
- Protein secretion by the T2SS and protein transport by the Sec complex (IDA
  PseudoCAP, PMID:9642203): PaAP is the cargo, not a component of either
  machine. Under GO practice, cargo is not annotated as participating in its own
  transport process (the transporter does the work). MARK_AS_OVER_ANNOTATED, with
  a PROBABLE PseudoCAP source defect (the cargo role is the positive basis).
  The only evidence we could see for the Sec row is signal-peptide removal
  (N-terminal sequencing), which does not by itself identify the Sec
  translocon. Full text of PMID:9642203 was not available (PubMed MCP and
  Europe PMC returned no body text, 2026-10-29), so whether it holds
  Sec-specific evidence is unchecked.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---:|---:|---|---|---|
| PTN000254534 | GO:0006508 proteolysis | 1 (sole seed) | 272 (109 taxa) | GO:0006508 proteolysis, IDA, PMID:11533066 (PseudoCAP) | SOUND | Cahan et al. purified the enzyme and showed Zn-dependent hydrolysis of amino-acid p-nitroanilides and of peptides with free N-termini (Leu-Ala, Ala4), i.e. direct peptide-bond hydrolysis; the gene product does the work. Abstract only in cache, but the UniProt ECO:0000269 curation and the 2024 review corroborate the full-text content. The node term is deliberately general: PTHR12147 M28 members (SGAP-like aminopeptidases, fungal "probable zinc metalloproteases", Mtb LpqL, E. coli YfbL) are peptidases with the conserved Zn ligands, so "proteolysis" is safe at the node. It is the only IBD in the whole family (PTHR12147-paint.tsv), so the clade carries no MF; a metalloaminopeptidase activity IBD would be more informative, but needs seeds beyond PaAP (e.g. SGAP P80561, B. subtilis YwaD P25152) and a check of the node's membership. |

Non-seeding PseudoCAP rows on this gene (T2SS secretion, Sec transport;
PMID:9642203) are cargo annotations; see above.

## Open questions

- Which subtree does PTN000254534 span? If it covers only bacterial SGAP-like
  M28A enzymes, PAINT could add an MF IBD (metalloaminopeptidase activity) using
  SGAP/YwaD/PaAP as seeds.
- Is the PA domain involved in protein-substrate recruitment or OMV association?
