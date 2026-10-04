# PIAS1 (human, UniProt O75925) - curation notes

## Deep research status

Automated deep research could not be generated for this gene: the falcon provider
returned HTTP 402, perplexity was unavailable, and openai returned HTTP 401. No
`-deep-research-*.md` file was created. The synthesis below is my own, built from the
UniProt record (`PIAS1-uniprot.txt`), the cached publications for every PMID in the
GOA annotation set, and five additional papers fetched with `just fetch-pmid`
(PMID:11583632, PMID:11867732, PMID:15311277, PMID:15657437, PMID:20016603).

## Domain architecture (UniProt)

- SAP domain (aa 11-45), with an LXXLL coregulator motif (aa 19-23) inside it
- PINIT domain (aa 124-288)
- SP-RING-type zinc finger (aa 320-405), the E3 catalytic module that binds UBE2I/UBC9;
  C351 mutation abolishes UBE2I binding [file:human/PIAS1/PIAS1-uniprot.txt "C->A,S: Loss of UBE2I-binding; almost complete loss"]
- SUMO1-binding region / SIM (aa 462-473)
- Ser/Thr-rich C-terminus with disordered segments and N-T-S-L repeats
- Two predicted NLSs; family: PIAS family (PIAS1-4 in human; Siz1/Siz2 in yeast)

## Synthesis

### 1. SP-RING-type SUMO E3 ligase

PIAS1 was identified as a SUMO-1-binding protein that also binds UBC9 and p53 and
catalyses p53 sumoylation via its RING-like domain [PMID:11583632 "PIAS1 catalyzed the
sumoylation of p53 both in U2OS cells and in vitro in a domain-dependent manner"].
Independently, PIAS1 and PIASxbeta were shown to act as E3-like ligases for p53 and
c-Jun [PMID:11867732 "two members of the PIAS family, PIAS1 and PIASxβ, act as specific E3-like ligases that promote sumoylation of p53 and c-Jun"].
The E3 activity of PIAS proteins resides in the SP-RING [PMID:20972456 "the E3 activity of the five mammalian PIAS proteins and their yeast homologues, Siz1 and Siz2, is associated with a different RING-like domain, SP-RING"].

Documented substrates (selection, from cached papers):
- Sp3 [PMID:12356736 "PIAS1 strongly stimulated SUMO conjugation to Sp3, thus acting as an E3 ligase for SUMO conjugation to Sp3"]; recombinant GST-PIAS1 drives near-complete conjugation in vitro.
- Mdm2 [PMID:12393906 "Mdm2 is also sumoylated in an in vitro system containing PIASxbeta, PIAS1, and RanBP2"].
- ZNF76 [PMID:15280358 "ZNF76 is sumoylated by PIAS1 at lysine 411"].
- HIC1 [PMID:17283066 "a bona fide E3 ligase for HIC1, PIAS1"].
- Nkx2.5 [PMID:18579533 "E3 ligase PIAS proteins PIAS1, PIASx, and PIASy, but not PIAS3, enhanced SUMO-1 attachment to Nkx2.5"].
- MTA1 [PMID:21965678 "Protein inhibitor of activated STAT (PIAS) proteins enhance SUMOylation of MTA1"].
- Blimp-1/PRDM1 [PMID:22555612 "a modification mediated by SUMO E3 ligase PIAS1"].
- FLASH/CASP8AP2 (PMID:21338522; RING-finger mutant fails to enhance FLASH activity).
- MRE11, the best-characterised recent substrate [PMID:36050397 "PIAS1 is the major SUMO E3 ligase for MRE11"]; in vitro reconstitution with purified MBP-PIAS1 enhances SUMO2 conjugation.
- PIAS1 is also routinely used as a positive-control SUMO E3 (e.g. PMID:27068747).
- Reactome lists many further PIAS1 SUMOylation reactions (BRCA1, SP3, MTA1, DDX5, FOXL2, SAFB, NRIP1, HIC1, MBD1, AR, ESR1, NR3C2, NR5A1/2, XRCC4, SATB1/2, THRB, CASP8AP2, L3MBTL2).

### 2. Transcriptional coregulator / inhibitor of activated transcription factors

- STAT1: PIAS1 was discovered as a specific inhibitor of STAT1 [PMID:9724754 "PIAS1, but not other PIAS proteins, blocked the DNA binding activity of Stat1 and inhibited Stat1-mediated gene activation in response to interferon"]. The C-terminal region (aa 392-541) binds the STAT1 N-terminal domain and only dimeric, tyrosine-phosphorylated STAT1 [PMID:10805787 "A mutant PIAS1 lacking the Stat1-interacting domain failed to inhibit Stat1-mediated gene activation"]. In Pias1-/- mice a subset of IFN-inducible genes is derepressed [PMID:15311277 "PIAS1 selectively regulates a subset of IFN-gamma- or IFN-beta-inducible genes by interfering with the recruitment of STAT1 to the gene promoter"].
- NF-kB: [PMID:15657437 "PIAS1 blocks the DNA binding activity of p65 both in vitro and in vivo"]; Pias1-null cells show increased p65 promoter occupancy and mice show elevated proinflammatory cytokines.
- PIAS1 can also act positively: e.g. it enhances c-Myb coactivation by FLASH (PMID:21338522), and relieves ZNF76-mediated repression of p53 targets by sumoylating ZNF76 (PMID:15280358). The mechanism of action (inhibition vs activation) is context- and substrate-dependent, as UniProt notes.
- The SAP domain binds p53 and A/T-rich DNA [PMID:15133049 "this domain possesses a binding ability to tumor suppressor p53, a target protein for sumoylation by PIAS1, whereas gel mobility assays showed that it has a strong affinity toward A/T-rich DNA"]; this is the basis for the "cis-regulatory region binding" ISS annotation (from mouse Pias1 + Msx1 data), but sequence-specific DNA binding as a function in vivo is not established for human PIAS1.

### 3. DNA damage response

- PIAS1 and PIAS4 are recruited to DSBs via their SAP domains and are needed for SUMO accrual, BRCA1/53BP1/RNF168 retention, DSB repair and IR resistance [PMID:20016603 "we show that PIAS1 and PIAS4 promote DSB repair and confer IR resistance"].
- PIAS1 sumoylates MRE11 on chromatin to stabilise it and promote end resection [PMID:36050397 "PIAS1 is recruited to damaged chromatin, which facilitates MRE11 SUMOylation to enhance MRE11 stability by antagonizing ubiquitylation"].

### 4. Localization

Nuclear; nuclear speckles and PML bodies (UniProt; [PMID:27068747 "Most of hDREF foci overlapped with PIAS1 foci, suggesting that hDREF might exist in the PML nuclear bodies"]). Cytoskeletal localization is a partial redistribution under CSRP2 overexpression (UniProt note), not a primary location. Mouse SynGO-based synaptic cytosol annotations are peripheral.

## Judgements on problematic annotations

- 55 GO:0005515 protein binding IPI rows: 42 come from a single Y2H neurodegeneration
  interactome (PMID:32814053) plus other Y2H/high-throughput screens (PMID:23275563,
  PMID:21911577, PMID:16154161) -> REMOVE (uninformative; HTT interaction was not
  confirmed by LUMIER in PMID:23275563). Rows from papers that show PIAS1 acting on a
  transcription factor or coregulator substrate -> MODIFY to DNA-binding transcription
  factor binding / p53 binding / transcription coregulator binding / SUMO binding.
- "transcription corepressor activity" (TAS, PMID:10805787) -> MODIFY to transcription
  regulator inhibitor activity: PIAS1 inhibits STAT1 by blocking its DNA binding, not by
  recruiting repressive machinery.
- "cell surface receptor signaling pathway via JAK-STAT" -> MODIFY to negative regulation.
- "positive regulation of protein sumoylation" -> MODIFY to protein sumoylation (PIAS1 is
  the E3 itself, so it participates directly).
- Rat/mouse Ensembl-Compara IEAs for visual learning, spermatogenesis, G1/S transition,
  apoptosis, proliferation, protein-DNA complex assembly: physiological outcomes of
  transcription-factor sumoylation, not core functions -> MARK_AS_OVER_ANNOTATED or
  KEEP_AS_NON_CORE.
- NEW: negative regulation of canonical NF-kappaB signal transduction (GO:0043124),
  passes participation (PIAS1 itself binds p65 and blocks its DNA binding) and comparator
  (NFKBIA, TNFAIP3 and PIAS4 carry the term in QuickGO, 2026-10).

## Open questions

- Is PIAS1 inhibition of STAT1/p65 DNA binding dependent on its E3 activity? (Evidence
  suggests not for STAT1; PMID:12356736 discussion notes this is unclear.)
- Extent of redundancy with PIAS4 in the DDR and SUMO paralog selectivity in vivo.
