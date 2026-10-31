# SKIP (Drosophila melanogaster) manual literature review

No deep-research API was available, so this review was done manually from PubMed
searches and cached full texts. Searches: "SKIP3 Shal Drosophila", "(CG31163 OR
"Shal K+ channel interacting protein" OR SKIP3) AND Drosophila", "SKIP Shal
Tsunoda S[Author]". Only two Drosophila papers study SKIP (FBgn0051163, CG31163). Hits on
human "SKIP3" (TRIB3, PMID:12743605, PMID:21896644) concern an unrelated tribbles-family
kinase-like protein and were excluded.

## Gene and protein

- SKIP (Shal K+ channel interacting protein), CG31163, chromosome 3R (94A). The locus
  encodes several products. UniProt A0A0B4K6C1 (1034 aa, NP_001247234.1) is a long
  isoform with an N-terminal SAM domain (7-66), an SH3 domain (727-788), a second SAM
  domain (819-879) and several disordered regions (UniProt FT lines, PROSITE/MobiDB-lite
  evidence). It belongs to the SASH1/SAMSN1 (SAM and SH3 domain) family, PANTHER
  PTHR12301:SF8.
- Diao et al. described three products: SKIP1 (CG31163-PB/PC, 952 aa; SAM1 + SH3 + SAM2),
  SKIP2 (CG31163-PA, 778 aa; SH3 + SAM2) and SKIP3 (SAM1 + 61-residue tail)
  [PMID:19463952 "SKIP1 contains both SAM1 and SAM2 domains, while SKIP2 contains only the
  SAM2 domain and SKIP3 contains only the SAM1 domain. Additionally, SKIP1 and SKIP2 contain
  the same SH3 domain."].
- The authors proposed an adaptor/scaffold role from the domain content alone
  [PMID:19463952 "Given that SAM and SH3 domains have been shown to mediate protein-protein
  interactions, SKIP proteins are likely to function as a family of adaptor or scaffolding
  proteins."]. SAM1-SAM1, SAM1-SAM2 and SAM2-SAM2 interactions were not detected in Y2H
  [PMID:19463952 "None of these combinations of SAM domains tested positive for an
  interaction (data not shown)."].

## Shal (Kv4) channel interaction and regulation (SKIP3 isoform)

- SKIP3 was isolated in a Y2H screen with the Shal1 C-terminus and confirmed by GST
  pulldown [PMID:19463952 "both GST-Shal1C and GST-Shal2C pulled-down large quantities of
  SKIP3"]. The interaction was specific relative to Shaker, Shaw and Shab C-termini.
- Shal binding needs the eight C-terminal residues unique to SKIP3 [PMID:19463952
  "truncation of these eight residues completely disrupted the interaction between SKIP3
  and Shal1C (Fig. 2B), suggesting that Shal binding requires these unique C-terminal
  residues. Thus, SKIP3 is likely to be the only SKIP isoform that interacts with Shal
  channels."].
- My isoform comparison (file:DROME/SKIP/SKIP-bioinformatics/RESULTS.md) identifies the
  128-aa UniProt product A0A0B4KH49 as SKIP3. Its unique C-terminal octapeptide is absent
  from A0A0B4K6C1, so the Shal-binding data do not apply to the product reviewed here.
- In Sf9 cells SKIP3 did not change Shal currents [PMID:19463952 "these results suggest
  that SKIP3 does not directly modulate the biophysical properties of Shal channels in Sf9
  cells."]. In embryonic neurons homozygous for Df(3R)Exel6190, a deficiency removing SKIP
  and about 17 other genes, more neurons had very fast-inactivating Shal currents, and
  myc-SKIP3 expression reversed this [PMID:19463952 "We found that myc-SKIP3 expression in
  ΔSKIP neurons indeed decreased the percentage of neurons with such a rapidly
  inactivating Shal current to 35%"].
- Localization: myc-tagged SKIP1 and SKIP3, expressed with elav-GAL4, are found in neuronal
  cell bodies and in puncta along processes [PMID:19463952 "We found that myc-SKIP3 and
  myc-SKIP1 are localized to neuronal cell bodies and in puncta along neuronal processes
  (Fig. 3)"]. SKIP1/3 transcripts are expressed in the embryonic CNS and PNS.

## Olfactory behaviour (gene level)

- In a gene-trap screen, line BG00076 (pGT insertion in the SKIP 5' UTR) had reduced
  olfactory trap responses. Precise excision restored behaviour, and SKIP transcript was
  reduced about five-fold [PMID:22530061 "For BG00076 we found that precise excision of the
  pGT element in two independent excision lines rescued the olfactory response in both
  females and males (Figure 4A and 4B), confirming that the olfactory behaviour defect is due
  to the pGT element insertion."].
- Electroantennograms were normal, so the defect does not lie in primary odorant
  transduction. The authors suggest it may act centrally or in synaptic transmission
  [PMID:22530061 "There was no effect on the EAG, but a limited set of odours was tested, and
  in addition if the gene is involved in synaptic transmission then we would not expect to
  see a primary EAG defect."]. Which isoforms the insertion affects is not known.

## Gaps

- No molecular activity has been shown for the long SAM-SH3-SAM isoforms, including
  A0A0B4K6C1. No partners of SAM1, SH3 or SAM2 are known.
- No single-gene null allele was used in the electrophysiology. The deficiency removes 18
  genes, but the defect was rescued by SKIP3.
