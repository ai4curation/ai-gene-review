# Synpcc7942_0873 (Q31PW6) notes: DUF4062 TIR-like NADase candidate

## Origin: KBase gene-annotate dashboard (Dark Protein Atlas)

- Dashboard protein: `CP088958.1_900` (*Synechococcus elongatus*, 362 aa). Strata:
  Environmental, Core. DeepTMHMM class GLOB (cytoplasmic 1–362). Homologs in only 3
  organisms across 3 genera.
- Mapping: the sequence is identical to Q31PW6 over all 362 residues. The MD5 checksum
  resolves to UniParc UPI000049B91D, whose active UniProtKB entries are Q31PW6 and
  A0A0H3K6U6; global alignment to the PCC 7942 reference proteome UP000889800 gives
  Q31PW6 at 100% identity and 100% coverage (hackathon run
  `20261030T220633Z-map-cp088958-1-900-uniprot`). The dashboard contig CP088958.1 is the
  PCC 6311 chromosome, so this is a different strain carrying an identical protein. The
  dashboard ID is recorded as an alias.
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
homologs, and Pfam HMM match state 78 with consensus E and P(E) = 0.602. The
deep-research report proposed Glu81 instead; the HMM puts Glu81 at a weak state
(P(E) = 0.197), so Glu81 was rejected.

Conservation is not activity. Of four human DUF4062-NACHT proteins assayed, only TEP1
hydrolysed NAD+, so the family is not uniformly catalytic, and nothing has been measured
for this protein. The review therefore records GO:0003953 as ISS and withholds any
phage-defence process term.

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
  aligned directly to the tested E97. The companion Evangelion preprint
  (doi:10.64898/2026.06.25.731849), which reports a putative catalytic Glu87 in a
  plasmid-borne DUF4062 system, was not read.

## Tooling notes

- EBI OLS was down. `just fetch-gene SYNE7 Synpcc7942_0873 --uniprot-id Q31PW6` failed at
  the taxon-label lookup, so the stub was seeded by calling `fetch_gene_data` with the
  label resolved through `ubergraph:` instead, giving "Synechococcus elongatus PCC 7942 =
  FACHB-805". For the same reason `validate-terms` was run with `--offline`, against the
  local cache only.
- `just fetch-fitness` has no FEBA mapping for SYNE7.
- UniProt lists no gene symbol for Q31PW6, so the directory uses the locus tag.
