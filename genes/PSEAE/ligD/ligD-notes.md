# ligD (PA2138, Q9I1X7) notes

## Identity

Swiss-Prot entry, 840 aa, "Multifunctional non-homologous end joining protein
LigD". Three autonomous domains: N-terminal 3'-phosphoesterase (PE, 7-162),
central ATP-dependent ligase (219-521, active-site Lys238 N6-AMP), C-terminal
polymerase/primase (Pol, 549-793). NCBIfam TIGR02776 NHEJ_ligase_prk, PANTHER
PTHR42705:SF2. [file:PSEAE/ligD/ligD-uniprot.txt "N6-AMP-lysine intermediate"]

## Literature (Shuman laboratory; all abstracts only except where noted)

- Zhu and Shuman 2005, PMID:15520014. Purified LigD; autonomous polymerase and
  ligase domains; templated primer extension and non-templated addition.
  [PMID:15520014 "Here we purify LigD and show that it possesses an intrinsic polymerase function resident within an autonomous C-terminal polymerase domain, LigD-(533-840), that flanks an autonomous DNA ligase domain, LigD-(188-527)."]
  [PMID:15520014 "(iii) templated extension of a 5'-tailed duplex DNA primer-template"]
- Zhu and Shuman 2005, PMID:15897197. PE domain has 3'-ribonuclease and
  3'-phosphatase activities, Mn2+-dependent.
  [PMID:15897197 "(i) the 3'-terminal nucleoside is first removed to yield a primer strand with a ribonucleoside 3'-PO4 terminus, and (ii) the 3'-PO4 is hydrolyzed to a 3'-OH"]
- Zhu and Shuman 2010, PMID:20018881. Gap filling; Ku stimulates LigD and
  promotes plasmid end joining by full-length LigD.
  [PMID:20018881 "We find that Pseudomonas Ku stimulates POL-catalyzed ribonucleotide addition to a plasmid DSB end and promotes plasmid end joining by full-length Pseudomonas LigD."]
  [PMID:20018881 "Many bacterial pathogens, including Pseudomonas aeruginosa, have a nonhomologous end joining (NHEJ) system of DNA double strand break (DSB) repair driven by Ku and DNA ligase D (LigD)."]

The ligase activity itself is not described in the 15520014 abstract beyond
"autonomous DNA ligase domain"; UniProt (curated, ECO:0000269 PubMed:15520014)
records that the Lig domain "functions as an independent domain", and the EC
6.5.1.1 nick-sealing activity of PaeLigD is well established. The IDA is
accepted (defer to curator; abstract-only).

## PseudoCAP IBA-seed assessment

Seeds from .cache/paint/IBD.gaf; Mtb LigD (P9WNV3) experimental rows from
QuickGO 2026-11-05.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001627042 | GO:0003910 DNA ligase (ATP) activity | 2 | 15 (10 taxa) | GO:0003910, IDA, PMID:15520014 (PseudoCAP; same row from UniProt) | SOUND | Purified PaeLigD with an autonomous ATP-dependent ligase domain; Ku-stimulated end joining (PMID:20018881). Exact activity, suits a LigD clade. | M. tuberculosis LigD P9WNV3 (GO:0003910 IDA PMID:12215643, 16023671, 16476729) | Yes |
| PTN001627042 | GO:0003887 DNA-directed DNA polymerase activity | 2 | 15 (10 taxa) | GO:0003887, IDA, PMID:15520014 (PseudoCAP; same row from UniProt) | SOUND | Templated extension of a primer-template by the purified Pol domain, abolished by D669A/D671A. | P9WNV3 (GO:0003887 IDA PMID:15499016) | Yes |

Other IBDs at this node that ligD receives but does not seed:
- GO:0006303 NHEJ (seed P9WNV3 only): sound, and true of PaeLigD (PMID:20018881). ACCEPT.
- GO:0006269 DNA replication, synthesis of primer (seed P9WNV3 only, MTBBASE
  IDA PMID:16023671): LigD Pol has in vitro primase-like activity, but LigD acts
  in NHEJ DSB repair, not chromosomal replication. The node term does not suit
  the clade. MARK_AS_OVER_ANNOTATED with a GO_CENTRAL CHECK (now PROBABLE
  after the tree check below; the Mtb paper was still not read).

No PSEUDOCAP defects. One GO_CENTRAL defect (GO:0006269, PROBABLE).

## PANTHER tree check (2026-11-05)

Topology of PTN001627042 in PTHR42705 fetched with
`projects/PSEUDOCAP/panther_tree.py node PTN001627042 --depth 5`. The node is a
**SPECIATION** node (LUCA), 15 leaves, PTHR42705:SF2 12 + SF3 3.

| Child node | Event | Leaves | Subfamilies | Contents | Verdict |
|---|---|---|---|---|---|
| PTN005127089 | SPECIATION (Eukaryota) | 2 | SF2 | *Monosiga* MONBRDRAFT_36321 "DNA ligase D", *Gossypium* LOC107941224 "DNA ligase (ATP)" | LigD-type ligase |
| PTN000048875 | SPECIATION (Eubacteria) | 13 | SF2 10, SF3 3 | the two clades below | LigD-type ligases |
| &nbsp;&nbsp;PTN008085115 | SPECIATION (Terrabacteria) | 7 | SF2 4, SF3 3 | PTN000048869 (DUPLICATION, 6: *Streptomyces* SCO5308/SCO6709/SCO6498 + **Mtb LigD P9WNV3**), **B. subtilis LigD O34398** | NHEJ LigD + *Streptomyces* ligase paralogs |
| &nbsp;&nbsp;PTN005127091 | SPECIATION (Proteobacteria) | 6 | SF2 | *Bradyrhizobium* bll6773; PTN005127092 (Gammaproteobacteria, 5: *Coxiella* CBU_1934, two *Xanthomonas* ligases, and PTN005127093 HORIZ_TRANSFER with *Ricinus* RCOM_0053280 and **PAO1 LigD Q9I1X7**) | NHEJ LigD |

Verdict: the clade is **homogeneous** - every leaf is a LigD-type or
ATP-dependent DNA ligase, the two fully named ones (Mtb, B. subtilis) are
bifunctional NHEJ proteins, and there is no replicative primase or DnaG-type
enzyme anywhere below the node. So the concern is not a node-placement problem
that a narrower clade would solve: GO:0006269 is the wrong kind of term for the
whole family, and the fix is to remove the IBD rather than move it. The two
activity IBDs at the same node (GO:0003910, GO:0003887) and the GO:0006303 NHEJ
IBD do suit the clade and already cover what the primase assay shows.

Confidence raised SUSPECTED -> PROBABLE: the tree is primary data and settles
that relocation is not the remedy, but whether the Mtb seed paper
(PMID:16023671) describes something genuinely replicative was not checked, and
only reading it would settle that.

## Review decisions

- ACCEPT: DNA ligase (ATP) activity (IBA, IDA, IEA); DNA-directed DNA
  polymerase activity (IBA, IDA); NHEJ (IBA).
- MODIFY: RNA exonuclease activity -> 3'-5'-RNA exonuclease activity
  (GO:0000175; removes the 3'-terminal ribonucleoside).
- NEW: polynucleotide 3'-phosphatase activity (GO:0046403), IDA PMID:15897197.
- TOO_GENERAL: DNA repair (NHEJ accepted); nucleotidyltransferase activity
  and DNA biosynthetic process (entailed by DNA-directed DNA polymerase activity).
- KEEP_AS_NON_CORE: ATP binding.
- MARK_AS_OVER_ANNOTATED: DNA recombination (IEA), DNA replication synthesis
  of primer (IBA).
