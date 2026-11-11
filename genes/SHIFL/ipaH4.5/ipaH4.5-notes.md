# ipaH4.5 (Shigella flexneri, UniProt P18009) — curation notes

## How this review was researched

No deep-research API keys were available in this container, so `just deep-research`
was **not** run and there is no `-deep-research-<provider>.md` file for this gene.
Literature research was done directly: the three cached publications already in
`publications/` were read, PubMed was searched through the PubMed MCP tools
(`IpaH4.5 Shigella`, 11 hits, all inspected by title/abstract), and four further
papers were cached with `just fetch-pmid` (PMID:30414351, PMID:33117724,
PMID:34296983, PMID:1791758).

Of the papers cited here only PMID:33117724 has `full_text_available: true`; the
others are abstract-only. **The GONUTS wiki could not be consulted**: the live site
(`gowiki.tamu.edu`) returns a "site is temporarily offline while we perform
upgrades" notice, the Wayback availability API has no snapshot for
`PMID:23083102` or `PMID:26700764`, and the one archived page that does exist
(`SHIFL:IPA4`, snapshot 2021-10-18) is on `web.archive.org`, which this container
blocks by egress policy. So the CACAO students' own evidence notes were not
readable, and the curator-deference rule was applied throughout: no experimental
CACAO row was removed.

## Gene identity and paralog hazard

`ipaH4.5` is one of a family of ~9 *ipaH* genes in *S. flexneri*, five on the
large virulence plasmid (pWR100/pCP301, where P18009 is CP0079) and several
chromosomal copies. The paralogs share a conserved C-terminal catalytic region
and differ in their N-terminal leucine-rich-repeat substrate-recognition region:

> [PMID:1791758 "The first 197 amino acids in IpaH7.8 were replaced in IpaH4.5 by a unique set of 251 amino acids, generating two related proteins with variable and conserved sequences."]

> [PMID:1791758 "The amino-terminal region of IpaH4.5 displayed an internal repeat structure, also seen in IpaH7.8, characteristic of members of the leucine-rich glycoprotein (LRG) family."]

This is the structural basis for treating substrate claims as paralog-specific
(IpaH9.8→NEMO/ABIN-1/GBPs, IpaH7.8→glomulin/NLRP1B/GBPs, IpaH4.5→p65, TBK1,
RPN13, NLRP3) while treating *secretion* and *catalytic mechanism* claims as
family-level. UniProt's own feature table matches: LRR 1–10 (res. 63–270),
"Interaction with target proteins" 1–284, NEL catalytic domain 295–574.

Because the family shares antigenic determinants and most anti-IpaH antisera are
not paralog-specific, any immuno-detection claim from an "IpaH" blot has to be
read as family-level. That is exactly the situation for the `extracellular
region` IDA (see below).

## Molecular function: a NEL-domain, cysteine-dependent E3 ligase

UniProt assigns the NEL (Novel E3 Ligase) domain to residues 295–574 with an
active site at residue 379:

> [file:SHIFL/ipaH4.5/ipaH4.5-uniprot.txt "FT   ACT_SITE        379 FT                   /note=\"Glycyl thioester intermediate\""]

Residue 379 of P18009 is a cysteine (checked directly against the SQ block:
…DATES**C**EDRVAL…, positions 374–385). A "glycyl thioester intermediate" on a
cysteine is the HECT-like mechanism: the ubiquitin C-terminal glycine is first
transferred onto the enzyme's own catalytic Cys before being passed to the
substrate lysine.

This is independently confirmed for IpaH4.5 itself. The NLRP3 paper uses a
C379A point mutant as its catalytic-dead control throughout:

> [PMID:33117724 "mutation of the IpaH4.5 E3 ligase motif (C379A mutant) did not upregulate NLRP3 ubiquitination to the same intensity as wildtype IpaH4.5 (Figure 2A)"]

> [PMID:33117724 "IL-1β production was specifically upregulated by WT IpaH4.5 but not the C379A mutant (Figure 4C), demonstrating the importance of IpaH4.5 E3 ligase activity in inflammasome activation."]

**Noted source defect.** UniProt P18009 carries
`AltName: Full=Probable RING-type E3 ubiquitin transferase ipaH4.5
{ECO:0000305}`. That is inconsistent with the same record's NEL domain and
Cys379 glycyl-thioester active site, and with the C379A data above: NEL-domain
IpaH/SspH ligases are not RING-type (RINGs are scaffolds with no catalytic
residue and no thioester intermediate). Recorded as a `source_defects` entry
(`resource: UNIPROT`) on the `GO:0061630` row.

## Substrates and biological roles

| Substrate | Chain | Outcome | Reference |
|---|---|---|---|
| NF-κB p65 (RELA) | polyUb | dampened NF-κB transcriptional output, less MIP-2/TNF-α | PMID:23083102 |
| TBK1 | K48 | proteasomal degradation, IRF3 not activated | PMID:26700764 |
| RPN13 (ADRM1) | polyUb | 19S RP dysfunction, less MHC-I cross-presentation | PMID:30414351 |
| NLRP3 | K63 | NLRP3 *stabilized*, inflammasome/pyroptosis up | PMID:33117724 |
| Rab31 (reported as GAP, not ligase) | — | CD-MPR mistrafficking, lysosome attenuated | PMID:34296983 |
| ELMO2 | polyUb | RAC activation disrupted (preprint, not cited in review) | PMID:42538988 |

### p65 / NF-κB (PMID:23083102) — the paper behind three CACAO rows

> [PMID:23083102 "the effector, IpaH4.5 dampens the pro-inflammatory cytokine response"]

> [PMID:23083102 "the Shigella ΔipaH4.5 mutant strain caused more severe inflammatory responses and significantly induced higher pro-inflammatory cytokine levels (MIP-2 and TNF-α) in the lung homogenates of wild type-infected mice"]

> [PMID:23083102 "Yeast two-hybrid screening showed that IpaH4.5 specifically interacts with the p65 subunit of NF-κB."]

> [PMID:23083102 "In vitro, IpaH4.5 displayed ubiquitin ligase activity towards ubiquitin and p65."]

> [PMID:23083102 "the transcriptional activity of NF-κB was shown to be inhibited by IpaH4.5 utilizing a dual-luciferase reporter gene detection system containing NF-κB promoter response elements"]

> [PMID:23083102 "the IpaH4.5 protein is an E3 ubiquitin ligase capable of directly regulating the host inflammatory response by inhibiting the NF-κB signalling pathway"]

Note what this paper does **not** contain: any assay of host protein synthesis.
Everything on the output side is transcriptional (an NF-κB-response-element
luciferase reporter) or cytokine protein levels downstream of that. This matters
for the `GO:0039604 symbiont-mediated suppression of host translation` CACAO row —
see the CACAO audit below.

### TBK1 (PMID:26700764) — the paper behind two CACAO rows

> [PMID:26700764 "TBK1 is a novel target of the IpaH4.5 protein, a Shigella type III effector possessing E3 ubiquitin ligase activity"]

> [PMID:26700764 "IpaH4.5 interacts with TBK1 and promotes its K48-linked polyubiquitylation."]

> [PMID:26700764 "polyubiquitylated TBK1 undergoes proteasome-dependent degradation, which perturbs the phosphorylation, nuclear translocation, and activation of IRF3"]

> [PMID:26700764 "Because IRF3 and TBK1 are required for restricting Shigella growth, we propose that the polyubiquitylation and degradation of TBK1 during Shigella infection are new bacterial strategies to modulate the host antibacterial responses."]

### RPN13 / proteasome (PMID:30414351)

> [PMID:30414351 "Shigella flexneri invasion plasmid antigen H (IpaH) 4.5, a member of the E3 ubiquitin ligase effector family, targets the proteasome regulatory particle non-ATPase 13 (RPN13) and induces its degradation via the ubiquitin-proteasome system (UPS)"]

A second, independent ubiquitin-proteasome substrate; corroborates
`GO:0043161 proteasome-mediated ubiquitin-dependent protein catabolic process`
beyond the TBK1 paper.

### NLRP3 (PMID:33117724) — the one full-text paper, and an opposite sign

> [PMID:33117724 "the ubiquitination of NLRP3 was catalyzed by IpaH4.5 mainly at position K63 (Figure 2B)"]

> [PMID:33117724 "Quantitative RT-PCR showed that NLRP3 mRNA levels were not affected by IpaH4.5 overexpression (Figure 3D), suggesting that IpaH4.5 stabilized NLRP3 protein by posttranscriptional modification."]

> [PMID:33117724 "We demonstrate that IpaH4.5 mediates NLRP3 protein stability, caspase-1 activation, IL-1β production, and cell death in Shigella-infected macrophages."]

> [PMID:33117724 "We observed significantly lower LDH release in BMDMs infected with IpaH4.5-deficient Shigella when compared to that of WT and ΔIpaH4.5/IpaH4.5 Shigella (Figure 5B)."]

This is the mechanistically cleanest IpaH4.5 paper available (substrate
interaction, chain-linkage mapping, C379A catalytic control, Δ mutant plus
complementation, and a `ΔipaH4.5/ipaH4.5(C379A)` strain). It is also the only
*positive*-sign activity: K63 chains stabilize NLRP3 rather than destroying it,
so the same ligase both suppresses NF-κB/IRF3 signalling and **promotes**
inflammasome signalling. One `NEW` row (`GO:0141087 positive regulation of
inflammasome-mediated signaling pathway`, IDA) is proposed from it; nothing in
the existing GOA set covers this arm.

### Reported RabGAP activity (PMID:34296983) — deliberately not annotated

> [PMID:34296983 "IpaH4.5 harbours TBC-like dual-finger motifs and exhibits potent RabGAP activities towards Rab31."]

A second molecular function (GTPase activator activity) in a protein whose only
recognized catalytic module is the NEL domain would be a significant claim.
It rests on one abstract-only paper from one group, UniProt records no TBC-like
motif in P18009, and PROSITE/Pfam match only LRR_TTSS and NEL. Not asserted as
a `NEW` annotation; raised instead as a `suggested_questions` entry and a
`suggested_experiments` entry.

### ELMO2 (PMID:42538988) — preprint, mentioned only

A 2026 bioRxiv preprint identifies ELMO2 as an IpaH4.5 substrate with strict
paralog selectivity (no activity on ELMO1/ELMO3), mapped to the ELMO2 Armadillo
repeat region. Not cited in the review YAML because it is an un-peer-reviewed
preprint, but worth revisiting on publication — it would be the clearest
demonstration of LRR-encoded substrate specificity for this paralog.

## Localization

Secretion/location evidence is family-level, not IpaH4.5-specific:

> [PMID:11418613 "we investigated the IpaH proteins for their ability to be secreted via the type III secretion system and their fate in mammalian cells"]

> [PMID:11418613 "Upon incubation in a medium containing Congo red, the bacteria secrete IpaH into the medium, but secretion of IpaH occurs later than that of IpaBCD."]

The title and most of the paper are about **IpaH(9.8)**, including the nuclear
import work. UniProt nevertheless cites this paper on the P18009 entry under
`SUBCELLULAR LOCATION, AND SECRETION VIA TYPE III SECRETION SYSTEM` (reference
[6]), i.e. the UniProt curator read the Congo-red secretion data as covering the
IpaH proteins generically, which the quoted sentences support. So the
`GO:0005576 extracellular region` IDA is kept, but as non-core: the medium is
where a T3SS effector is caught in transit under artificial induction, not where
it works. Every known IpaH4.5 substrate (p65, TBK1, RPN13, NLRP3, Rab31) is a
host cytosolic protein, which is what makes `GO:0030430 host cell cytoplasm` the
functionally relevant compartment. Note that no paper reports nuclear IpaH4.5;
the nuclear-transport result belongs to IpaH9.8 and must not be propagated here.

## CACAO audit (6 rows, `ASSIGNED BY = CACAO`)

| GO term | Code | PMID | What the paper shows for ipaH4.5 | Verdict |
|---|---|---|---|---|
| GO:0000209 protein polyubiquitination | IDA | 23083102 | in vitro ligase activity "towards ubiquitin and p65"; K48 chains on TBK1 and K63 chains on NLRP3 in two later papers | matches — ACCEPT |
| GO:0051865 protein autoubiquitination | IDA | 23083102 | abstract reports activity "towards ubiquitin and p65", not towards itself; full text and GONUTS notes unreadable | plausible family property, peripheral — KEEP_AS_NON_CORE |
| GO:0039604 symbiont-mediated suppression of host translation | IDA | 23083102 | no protein-synthesis assay anywhere; the readout is an NF-κB-response-element luciferase reporter plus cytokine levels | **wrong term** — MODIFY → GO:0085034 |
| GO:0006511 ubiquitin-dependent protein catabolic process | IMP | 26700764 | "polyubiquitylated TBK1 undergoes proteasome-dependent degradation"; RPN13 likewise via the UPS | right but under-specific — MODIFY → GO:0043161 |
| GO:0052170 symbiont-mediated suppression of host innate immune response | IMP | 26700764 | TBK1 degraded, IRF3 phosphorylation/nuclear import/activation lost, host antibacterial response dampened | matches — ACCEPT |
| GO:0000209 / GO:0051865 / GO:0039604 all key to the same paper | — | — | three BP rows from one abstract-only paper | see individual rows |

**The notable failure is `GO:0039604`.** It is not a phenotype-read-as-process and
not a wrong-paper case; it is a *wrong-mechanism* substitution. The paper
repeatedly says "transcriptional activity of NF-κB … inhibited" and "inhibiting
the NF-κB signalling pathway", and the student (or the curation interface's term
search) landed on the translation sibling of the host-gene-expression branch.
Because the aspect (symbiont suppression of host gene expression) is right and
only the step is wrong, `MODIFY` to `GO:0085034 symbiont-mediated suppression of
host NF-kappaB cascade` is the correct action rather than `REMOVE` — the claim is
not false, it is misfiled, and GO:0085034 is precisely the mechanism the paper
demonstrates. For the CACAO failure taxonomy this is a fourth pattern worth
naming: **right pathway, wrong molecular step** — a term chosen from the correct
neighbourhood of the ontology but describing a different biochemical process
(translation vs transcription/signalling) than the one assayed. It is invisible
to every mechanical check (the PMID resolves, the paper is about the gene, the
evidence code fits the assay) and can only be caught by reading the term
definition against the figures.

Two of the six rows are also *slightly* generous with the IDA code:
`GO:0039604`/`GO:0051865`/`GO:0000209` are all keyed to one paper whose relevant
panels we cannot see. None of that justifies removal under the curator-deference
rule, and the two IMP rows from PMID:26700764 are both well matched to the
abstract's own statements.

## Non-CACAO rows

- `GO:0004842 ubiquitin-protein transferase activity` (IEA, InterPro NEL) and
  `GO:0061630 ubiquitin protein ligase activity` (IEA, EC:2.3.2.27) are the same
  claim at two granularities; the specific one is kept and the general one
  modified to it.
- `GO:0016567 protein ubiquitination` (IEA, InterPro NEL) is modified to
  `GO:0000209`, which the gene already carries.
- `GO:0035821 modulation of process of another organism` (IEA, ARBA) is an
  effector-generic placeholder two levels above what is demonstrated; modified
  to `GO:0052170` and `GO:0085034`.
- `GO:0030430 host cell cytoplasm` (IEA, UniProt SubCell) is accepted as the
  core location.

## Open questions carried into the review

1. Is the reported Rab31 GAP activity real, and if so does it use the NEL
   catalytic Cys or a separate TBC-like surface?
2. How are the suppressive (p65, TBK1, RPN13) and activating (NLRP3) arms
   reconciled in one infection — different cell types, different times, or
   different effector doses?
3. Should UniProt's "RING-type" alternative name be corrected to NEL/HECT-like?
