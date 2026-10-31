# Synpcc7942_0873 (Q31PW6) notes: DUF4062 TIR-like NADase candidate

## Origin: KBase gene-annotate dashboard (Dark Protein Atlas)

- Dashboard protein: `CP088958.1_900` (*Synechococcus elongatus*, 362 aa). Strata:
  Environmental, Core. DeepTMHMM class GLOB (cytoplasmic 1–362). Homologs in only 3
  organisms across 3 genera.
- Mapping: the sequence is identical to Q31PW6 over all 362 residues. The MD5 checksum
  resolves to UniParc UPI000049B91D, whose active UniProtKB entries are Q31PW6 and
  A0A0H3K6U6; global alignment to the PCC 7942 reference proteome UP000889800 gives
  Q31PW6 at 100% identity and 100% coverage (hackathon run
  `20261030T220633Z-map-cp088958-1-900-uniprot`). NCBI titles the dashboard contig
  CP088958.1 "Synechococcus elongatus PCC 6311 chromosome" (BioSample SAMN22215176;
  esummary frozen as
  `Synpcc7942_0873-dashboard-prediction-evidence/CP088958.1_nuccore_summary.json`), while
  the PCC 7942 chromosome is CP000100. So this is a different strain carrying an
  identical protein. The dashboard ID is recorded as an alias.
- "Hackathon run" IDs here and in `Synpcc7942_0873-bioinformatics/RESULTS.md` are BERIL
  runs in the LBNL hackathon workspace project (`projects/LBNL_HACKATHON.md`). That
  workspace is not in this repository; the committed scripts and `data/` copies are the
  record.
- The frozen call and page are in `Synpcc7942_0873-dashboard-prediction-evidence/`,
  copied from hackathon run `20261030T220616Z-dashboard-page-cp088958-1-900`.
- Prior names: eggNOG and InterPro both give only "Domain of unknown function
  (DUF4062)". GOA has no annotations for Q31PW6.

## The call's error: an orthogroup label crossing a domain boundary

The call was "DUF4062 domain-containing protein, putative NACHT-family NTPase" with
GO:0017111. The NTPase half rests entirely on the STRING orthogroup COG5635,
"Predicted NTPase, NACHT family domain". That label describes the large multidomain
members of the group, such as TEP1, in which the NTP-hydrolysing NACHT domain sits
*next to* DUF4062 as a separate domain. It is not a property of DUF4062 itself.

This protein has no NACHT or P-loop domain and no Walker A or Walker B motif in any
form. Among DUF4062 proteins of 450 aa or less, a P-loop domain occurs in 23 of 1720
(1.3%), against 2514 of 2925 (85.9%) among longer ones. Details and the scripts are in
`Synpcc7942_0873-bioinformatics/`.

## What the family actually does

Osinski et al. 2026 (PMID:42146377, bioRxiv, **not peer reviewed**) show DUF4062 is a
TIR-like NADase that hydrolyses NAD+ to ADP-ribose and nicotinamide, using a conserved
catalytic Glu. Bacterial members form the Swarożyc antiphage system: a TIR-like domain,
a helical stalk and an auxiliary domain, activated by the phage portal protein, killing
the infected cell by depleting NAD+.

This protein has the same compact layout (DUF4062 at 6–146, coiled coil at 170–197, an
unassigned C-terminal region) and keeps the family's most conserved Glu at **Glu83**, in
`GLSYTEKEY`. Two independent estimates agree: identical in 93% of 375 short bacterial
homologs, and Pfam HMM match state 78 with consensus E and P(E) = 0.602. The tested
human TEP1 E1008 maps to the same HMM state, in a matching `SVTEME` / `SYTEKE` motif
(RESULTS.md section 3b); a naive pairwise alignment misplaces it by a gap. The
deep-research report proposed Glu81 instead; the HMM puts Glu81 at a weak state
(P(E) = 0.197), so Glu81 was rejected.

Conservation is not activity. Of four human DUF4062-NACHT proteins assayed, only TEP1
hydrolysed NAD+, so the family is not uniformly catalytic, and nothing has been measured
for this protein. The review therefore records GO:0003953 as ISS and withholds any
phage-defence process term.

## Independent structure-based reviews converge, and add a domain

Two other reviewers on the dashboard reached the same verdict independently, and between
them supplied a domain this review had left unassigned. Their reasoning is recorded on
the dashboard page for `CP088958.1_900`, not in this repository, so it is summarised here
rather than cited as verified evidence. (A hackathon run that saved this review's own
dashboard verdict also scraped the two comments, but they are other reviewers' words and
are not republished here.) For that reason the winged-helix assignment is kept out of the
review's `description` and annotations. It informs the reading below but carries no
annotation.

- **MorganP**: neither CDD nor InterPro links the protein to NTPase domains; the
  predicted structure has two domains, a TIR domain and a winged helix. They suggested a
  transcriptional regulator, noting it as speculative.
- **JMC-Claude-SCOP**: a SCOPe 2.08 comparison of the AlphaFold model AF-Q31PW6-F1.
  Residues ~1-168 (median pLDDT 94) give TIR (c.23.2) as the strongest superfamily
  over-representation of 524 tested, with all three SCOPe TIR representatives in the top
  1% of 3,910 alignments, while individual hits stay weak. Residues ~206-348 return ten
  hits, all winged-helix DNA-binding domains (a.4.5), likewise weak. They record that the
  P-loop signal looks like generic alpha/beta similarity, that there is no Walker A or B
  motif, and that a TIR-like domain plus a winged helix leaves no room for a NACHT domain
  in 362 residues.

Three points follow. First, the TIR reading of DUF4062 is now supported structurally and
independently of the preprint. Second, the absence of Walker motifs was found twice, by
regular-expression scan here and by structural comparison there. Third, the winged helix
matters: Osinski et al. describe the KpSwz portal-recognition auxiliary domain as adopting
a "helix-turn-helix (HTH)/winged fold", so the predicted architecture completes the
Swarożyc layout of TIR-like domain, stalk and winged-helix sensor.

That last point is also where the readings diverge. A winged helix often binds DNA, which
is why MorganP suggested a regulator; in this family, however, the equivalent fold is a
phage sensor. The defence reading is better supported for a DUF4062 protein, but a
regulatory role is not excluded, and the discriminator is whether a phage protein
activates it rather than a DNA-binding assay alone.

## Family-level contribution to DUFMech

The family finding was contributed to [DUFMech](https://github.com/CultureBotAI/DUFMech),
the DUF mechanism knowledge base, as the PF13271 record:
**[CultureBotAI/DUFMech#384](https://github.com/CultureBotAI/DUFMech/pull/384)**.

That entry holds two mechanistic causal graphs, for human TEP1 and for the *Klebsiella*
portal-activated protein, with the source extracts. Deliberately, it curates **no causal
edge for Q31PW6**: the repo's rule is that causal edges may not be inferred from
similarity, so this protein appears there only as an open question about whether short
stand-alone bacterial members are active, and under what trigger. Anyone revisiting this
gene should read that record for the family-level evidence, and this file for the gene.

## Open questions

- Does purified Synpcc7942_0873 hydrolyse NAD+, and does Glu83Ala abolish it?
- Does it defend *S. elongatus* against cyanophage, and is a portal protein the trigger?
- Its neighbours include an SNF2/RAD54-family helicase and a protein with a UvrC-like
  endonuclease domain. Do they form a defence island with it? Not examined here.
- The KpSwz sequence is only in the preprint's supplementary material, so Glu83 was never
  aligned directly to the tested E97. (It does map to the HMM state of the other tested
  Glu, TEP1 E1008.) The companion Evangelion preprint
  (doi:10.64898/2026.06.25.731849), which reports a putative catalytic Glu87 in a
  plasmid-borne DUF4062 system, was not read.

## Tooling notes

- EBI OLS was down. `just fetch-gene SYNE7 Synpcc7942_0873 --uniprot-id Q31PW6` failed at
  the taxon-label lookup, so the stub was seeded by calling `fetch_gene_data` with the
  label resolved through `ubergraph:` instead, giving "Synechococcus elongatus PCC 7942 =
  FACHB-805". For the same reason `validate-terms` was run with `--offline`, against the
  local cache only.
- `just fetch-fitness` has no FEBA mapping for SYNE7.
- On 2026-10-31 InterPro and UniProt REST returned HTTP 500, so the TEP1 mapping reused the
  saved PF13271 HMM and fetched the UniProt sequences through NCBI efetch.

## Evidence code for GO:0003953

ISS rather than ISM. The Pfam HMM locates the domain and the catalytic position, but the
activity is transferred from two experimentally characterized family members, KpSwz and
TEP1, whose activity depends on the mapped Glu (E1008A abolishes TEP1 NADase activity).
Transfer from characterized homologs with a residue-level check fits ISS, and ISS is the
parent code in either case.
- UniProt lists no gene symbol for Q31PW6, so the directory uses the locus tag.
