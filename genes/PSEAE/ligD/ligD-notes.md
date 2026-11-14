# ligD manual review

Reviewed 13 ordered source annotations; no new rows or retirements. Raw UniProt, GOA and seed snapshots remain unchanged.

The exact target descends from its seeded IBD node in the official PANTHER tree. Broad family membership is not a grant of every LigD domain, primase process, or partner interaction. No donor-count or self-source objection is used.

GO:0045027 DNA-end binding is a distinct branch from duplex-binding3690; both describe real Ku properties. GO:0140078 captures AP beta-lyase cleavage; GO:0051575 captures terminal5′-dRP elimination. These are distinct from PE-mediated3′phosphatase0046403. No BER process NEW is inferred from necessity or a purified reconstitution.

Primase-process IBA GO:0006269 is ACCEPT: its definition explicitly includes DNA-damage priming, the exact target inherits PTN001627042, and no target-specific catalytic loss is established. A lack of direct target de novo assays is not evidence against this inference. The native conditions of use remain a legitimate question.

PAO1 target evidence is kept separate from PA14 LigD-independent NHEJ in PMID:42306942. The latter is not a PAO1 deletion experiment. Ku-(1–253) end protection, full-length stimulation and other truncation assays are distinguished in PMID:20018881. PMID:25355514 explicitly clones Ku from PAO-1 genomic DNA.

The recent Mycobacterium POL-regulation result PMID:42953966 is not transferred as a universal sign to these proteins. The shared Falcon authentication failure is documented in the prior session; this file is manual synthesis, not a fabricated provider report.

- PMID:15520014: Abstract-only positive biochemical evidence for purified P. aeruginosa LigD polymerase and ATP-ligase domains. No negative conclusion about an unexamined primase assay is drawn.
- PMID:15897197: Abstract-only direct P. aeruginosa LigD terminal-ribonucleotide resection evidence. The preferred substrate is a DNA primer bearing a short 3′ ribonucleotide tract, not bulk cellular RNA. Sequential nucleoside removal and 3′-phosphate hydrolysis are distinguished.
- PMID:16046407: Abstract explicitly reports P. aeruginosa LigD phosphatase activity on an all-DNA primer-template. This supports the DNA substrate in GO:0046403; RNA-terminal phosphatase activity alone would not establish it. Full Figure5 was not independently inspected here.
- PMID:20018881: Full primary text: recombinant P. aeruginosa Ku/LigD, DNA gap filling with dNTPs, and Ku stimulation of LigD. End protection used Ku-(1–253); full-length and other truncations were separately tested. This is not a native PA14 or KT2440 assay.
- PMID:26826709: Full primary biochemistry directly tests Bacillus LigD dCTP gap filling and 5′-dRP lyase, and confirms 5′-dRP lyase in purified P. aeruginosa LigD. Native Bacillus strain168-derived spore experiments suggest overlapping repair with Nfo but do not alone prove the proposed full BER role.

Final RNA-chemistry scope: GO:0003887 core is restricted to dNTP incorporation. PAO1 PMID:20018881 shows multiple templated rNMP additions and rNTP gap closure, supporting GO:0003899 for extension of the nascent RNA tract. This is not a transcription claim. No NEW annotation row was added.

Recovery provenance (2026-11-07): reconstructed from the preserved historical curation helper and recorded final edits after deletion of the prior uncommitted worktree. Fresh seed bytes match the historical observed seeds; raw sources were reacquired by root and are frozen independently. Validation, renders and generated histories are new recovery outputs; the lost historical handoff is not recreated.


## 2026-11-08 — recovery PR review follow-up

Replace functional methods-only quotes with result statements; retain construct provenance in reference findings and notes. Separate measured AP/dRP lyase capabilities from unproven native process assignments. Original annotation payloads and raw-source files remain unchanged.


## 2026-11-08 — source-specific evidence follow-up

Strengthen ATP, duplex/end-binding and multistep rNMP-extension support where applicable; remove duplicate evidence entries. Explicit NEW MF proposals record measured AP/5′-dRP chemistry without assigning a general native BER process. Abstract-only PMID:17293412 is scoped to the quoted mutant-spore phenotype, with no unverified strain details. Original source annotation payloads are unchanged. See the evidence-followup-20261108 receipt for the exact file scope.


## 2026-11-10 — terminal synthesis and phosphate removal

Retain nucleotidyltransferase activity to cover both templated synthesis and non-templated ribonucleotide/deoxyribonucleotide addition. GO:0003912 names deoxynucleotide addition and cannot replace the preferred ribonucleotide terminal addition. Added the direct all-DNA 3-prime phosphatase annotation already supported in core synthesis. Original source rows remain unchanged.


## 2026-11-11 — template-directed RNA synthesis

Add the directly assayed DNA-directed RNA polymerase activity already supported in the core functions. The multistep ribonucleotide extension in PMID:20018881 is distinct from non-templated terminal addition. Original source rows remain unchanged.


## Incoming historical PseudoCAP review (preserved; reconciled below)

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


## 2026-11-13 — reconcile independent LigD reviews

The incoming identity, domain architecture, PAINT seed provenance and positive catalytic evidence are retained. The current GO:0006269 definition includes DNA-damage priming, so the incoming chromosome-only objection and associated source-defect claim are superseded. GO:0000175 specifies mononucleotide cleavage; LigD releases a nucleoside before its separate phosphatase step, so the original experimental RNA-exonuclease claim is kept without that unsupported refinement. ATP binding is catalytic, and broad nucleotidyltransferase activity retains the independently measured non-templated addition that is not covered by DNA-directed polymerase activity. DNA-repair and recombination rows retain the supported NHEJ refinement; DNA synthesis remains a directly performed repair step.

The incoming GO:0046403 NEW payload is preserved but retired as a duplicate with less precise substrate provenance. The live proposal cites PMID:16046407, whose abstract explicitly establishes the all-DNA substrate required by the current GO definition. This does not deny the incoming paper's ribonucleotide-end healing chemistry. The current core functions and all 13 original source rows remain intact. Identical or nested supporting quotations are collapsed when evidence lists are combined.
