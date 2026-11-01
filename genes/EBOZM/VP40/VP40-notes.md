# VP40 (Zaire ebolavirus, Mayinga-76; UniProt Q05128) — curation notes

## Provenance of this research

**Deep research was unavailable for this review.** No deep-research API keys are
configured in this container, so `just deep-research` was not run and no
`-deep-research-<provider>.md` file exists for this gene. The notes below were
assembled directly from (a) the cached publications in `publications/`, (b) the
UniProt flat file `VP40-uniprot.txt`, and (c) PubMed/PMC lookups.

Attempts to read the GONUTS wiki pages that would record the CACAO students'
own evidence (`https://gowiki.tamu.edu/wiki/index.php/PMID:11333902`,
`.../PMID:14673115`) returned only a site-wide notice that the wiki is
"temporarily offline while we perform upgrades" (fetched 2026-10-29), so the
student-side rationale for the six CACAO rows could not be inspected. PMC
full text for the two abstract-only CACAO IDA papers (PMC114926 for
PMID:11333902, PMC307671 for PMID:14673115) was also not retrievable through
the PMC OA service, so those rows were judged on their abstracts plus the
surrounding literature, under the curator-deference rule.

## What VP40 is

VP40 is the 326-residue matrix protein of Zaire ebolavirus and the most abundant
protein in the virion ("Most abundant protein in the virion",
`file:EBOZM/VP40/VP40-uniprot.txt`). It is a two-domain protein: an N-terminal
domain that mediates oligomerisation and a C-terminal domain that mediates
membrane binding [PMID:23297401 "VP40 consists of an N-terminal domain that has
been shown to mediate oligomerization and a C-terminal domain has been shown to
mediate lipid binding."]. UniProt records a conformationally plastic oligomer
series — dimer, hexamer, octamer — with "Hexamers are critical for budding" and
"Octamers function in genome replication and RNA binding"
(`file:EBOZM/VP40/VP40-uniprot.txt`).

## Core role: plasma-membrane assembly and budding

- VP40 expressed alone is sufficient to make membrane-bound particles, and this
  depends on its N-terminal PPxY late domain [PMID:11333902 "We found that VP40
  is indeed able to induce particle formation when it is expressed in mammalian
  cells, and this process appeared to rely on a conserved N-terminal PPXY motif,
  as mutation or loss of this motif resulted in markedly reduced particle
  formation."].
- The same paper is the direct membrane-association evidence: "Flotation gradient
  analysis indicated that VP40 binds to membranes in a hydrophobic manner, as
  NaCl at 1 M did not release the protein from the lipid bilayer."
  [PMID:11333902] — note this is a bulk cellular-membrane assay, not a
  plasma-membrane-resolved one.
- The membrane in question is the plasma membrane inner leaflet. VP40
  selectively penetrates PM-mimetic monolayers, and hydrophobic C-terminal
  residues Leu213/Ile293/Leu295/Val298 are required for PM localisation,
  oligomerisation and VLP egress [PMID:23297401 "Mutagenesis of this hydrophobic
  region consisting of Leu 213 , Ile 293 , Leu 295 , and Val 298 demonstrated
  that membrane penetration is critical to plasma membrane localization, VP40
  oligomerization, and viral particle egress."]. Confocal imaging in that study:
  "WT EGFP-VP40 was predominantly localized to the PM with strong visual evidence
  of VLP extensions stemming from the PM".
- Penetration depth was measured at 8.1 Å into the bilayer hydrocarbon core, and
  VP40 tubulates liposomes and vesiculates GUVs [PMID:23663837 "hydrophobic
  residues that penetrate deeply into the plasma membrane are essential for
  plasma membrane localization and virus-like particle formation and release from
  cells."].
- PI(4,5)P2 is required for the extensive (>12-mer) oligomerisation at the PM and
  for egress [PMID:26753796 "VP40 is the most abundant protein in EBOV virions
  and can form authentic looking virus like particles (VLPs) that bud from the
  plasma membrane of live cells in the absence of other EBOV proteins"].
- Oligomers sit in detergent-resistant/raft membrane: "we demonstrate VP40
  oligomers in lipid rafts of mammalian cells, virus-like particles, and in the
  authentic Ebola virus" and "we demonstrate the active recruitment of TSG101
  into lipid rafts by VP40" [PMID:14673115].
- VP40–VP40 complexes visualised by bimolecular complementation "localized
  predominantly at the plasma membrane", whereas VP40–NP and NP–NP complexes
  "displayed a more dispersed pattern throughout the cytoplasm" [PMID:21987757].

## Host ESCRT and E3-ligase recruitment

UniProt FUNCTION: VP40 "Acts by interacting with viral ribonucleocapsid and host
members of the ESCRT (endosomal sorting complex required for transport) system
such as host VPS4, PDCD6IP/ALIX, NEDD4 or TGS101"
(`file:EBOZM/VP40/VP40-uniprot.txt`). The two overlapping late domains are a
PTAP/PSAP motif (TSG101 UEV domain) and a PPxY motif (NEDD4 WW3, SMURF2 WW
domains) (same file, DOMAIN block).

- SMURF2: "the multiple WW domains of SMURF2 interact with eVP40 and mVP40 in a
  PPxY-dependent manner" and "siRNA knockdown of endogenous SMURF2 led to
  inhibition of eVP40 VLP egress, suggesting that the interaction between eVP40
  and SMURF2 is functional by positively regulating eVP40 VLP budding"
  [PMID:33673144].
- WWP1: "WWP1 colocalizes with eVP40 at the site of budding at the plasma
  membrane in a WW-domain-dependent manner" [PMID:28768865]; WWP1 ubiquitinates
  VP40 and this "mediates efficient viral budding"
  (`file:EBOZM/VP40/VP40-uniprot.txt`).

## RNA binding / octamer

The octameric ring binds a specific ssRNA sequence in a pocket at the
dimer–dimer interface [PMID:12679020 "This strongly indicates, together with the
RNA binding properties of full-length oligomeric VP40 in vitro, that octameric
VP40 bound to a specific RNA sequence plays a role in the virus life cycle."].
The octamer is detectable in infected cells but "octameric VP40 might not be
abundantly present in virus particles" [PMID:12679020], and UniProt assigns the
octamer to "genome replication and RNA binding"
(`file:EBOZM/VP40/VP40-uniprot.txt`). Octamers are essential for virus
replication (PMID:15650213, cited in UniProt). So RNA binding is a real second
activity, distinct from the matrix/budding activity, but it is a minor-abundance
form and there is no evidence that VP40 is a stoichiometric subunit of the viral
nucleocapsid RNP.

## Secondary / host-perturbing activities

- Innate immunity: in an siRNA-based screen of all EBOV proteins, "In addition to
  viral protein 35 (VP35), we found that VP30 and VP40 independently act as SRSs"
  (suppressors of RNA silencing) [PMID:21228243]. Mechanism was worked out for
  VP30 and VP35 only; the VP40 claim rests on the suppression phenotype.
- Cell cycle: "Nuclear VP40 upregulates cyclin D1 levels, resulting in
  dysregulated cell cycle and EV biogenesis" and "VP40 clones were accelerated
  in growth due to cyclin D1 upregulation, and nuclear VP40 was found bound to
  the cyclin D1 promoter" [PMID:30169850].
- Exosomes: UniProt records "Secreted, extracellular exosome
  {ECO:0000269|PubMed:27872619}" and that VP40 "May play a role in immune cell
  dysfunction by being packaged into exosomes that can decrease the viability of
  recipient cells" (`file:EBOZM/VP40/VP40-uniprot.txt`). This is the only basis
  for the extracellular-region annotation.

## Is VP40 required for intracellular transport of the nucleocapsid?

This matters for the CACAO row `GO:0075733 intracellular transport of virus`.
PMID:23297401 states, citing an earlier study rather than its own data, that "in
the absence of VP40 the nucleocapsid is not effectively transported to the PM,
the site of assembly and budding". Against that, Takamatsu et al. concluded that
NP, VP35 and VP24 are essential *and sufficient* to mediate nucleocapsid
transport (PubMed:29339477, cited in `VP40-uniprot.txt` reference list) — i.e.
VP40 is not part of the transport machinery, and the earlier observation is
consistent with VP40 being needed at the destination (the PM assembly site)
rather than performing the movement. PMID:23297401 itself ran monolayer
penetration, confocal localisation, TIRF/number-and-brightness oligomerisation
and VLP Western assays; it ran no transport assay.

## CACAO rows (ASSIGNED BY = CACAO in `VP40-goa.tsv`)

| Term | Evid | PMID | What the paper shows | Verdict |
|---|---|---|---|---|
| GO:0033644 host cell membrane | IDA | 11333902 | flotation-gradient membrane binding, Triton X-114 partitioning | right claim, coarse granularity → MODIFY to GO:0020002 |
| GO:0046761 viral budding from plasma membrane | IMP | 11333902 | PPxY mutation / C-terminal truncation abolishes particle formation | ACCEPT |
| GO:0045121 membrane raft | IDA | 14673115 | VP40 oligomers in lipid rafts of cells, VLPs and authentic virus; TSG101 recruited into rafts | ACCEPT |
| GO:0046755 viral budding | IMP | 16837071 | luciferase budding assay; budding-deficient VP40 mutant loses luciferase in VLP fraction | right claim, coarse granularity → MODIFY to GO:0046761 |
| GO:0033644 host cell membrane | IMP | 23297401 | hydrophobic CTD mutants lose PM localisation and VLP egress | right claim, coarse granularity → MODIFY to GO:0020002 |
| GO:0075733 intracellular transport of virus | IMP | 23297401 | no transport assay in the paper; the mutants affect PM penetration, oligomerisation and egress | wrong process → MODIFY to GO:0046761 |

Pattern notes for the CACAO taxonomy:

- **Wrong granularity (new-ish pattern, 3 of 6 rows).** Three CACAO rows pick the
  parent where the paper's own assay supports the child: `host cell membrane`
  twice where the paper reads out plasma-membrane localisation (and UniProt's
  curated location, SL-0375, maps to `host cell plasma membrane`), and `viral
  budding` where the assay is VLP release from the cell surface. None of these is
  wrong; all three are less informative than the data.
- **Egress read as transport (a variant of phenotype-as-process).**
  `GO:0075733 intracellular transport of virus` on PMID:23297401 converts "this
  mutant does not get to the plasma membrane / does not release VLPs" into a
  claim that VP40 moves virus within the cell. It also propagated: the
  `GO:0043657 host cell` IEA row (GO_REF:0000108) is an inter-ontology inference
  *from* GO:0075733, so one student process call seeded a second annotation.
- **No paper-not-about-gene and no single-assay-localization failures here.** All
  six CACAO rows cite papers whose primary subject is EBOV VP40, and the
  `membrane raft` localisation is supported in three systems (cells, VLPs,
  authentic virus) in one paper plus the detergent-resistant-membrane results of
  PMID:23297401.
