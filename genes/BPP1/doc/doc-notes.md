# doc (death on curing) — Escherichia phage P1, UniProt Q06259

Curation journal for the CACAO annotation audit (see `projects/CACAO.md`).

## Provenance note on research method

**Deep research was unavailable for this review.** No deep-research API keys are
configured in this container, so `just deep-research` was not run and there is no
`doc-deep-research-<provider>.md` file. The literature below was assembled by hand from
the cached publications in `publications/`, the UniProt flat file
(`genes/BPP1/doc/doc-uniprot.txt`), PubMed, and QuickGO.

**GONUTS is offline.** `https://gowiki.tamu.edu/wiki/index.php/PMID:11222604` returns only
"This site is temporarily offline while we perform upgrades", confirming the status
recorded in `projects/CACAO.md` as of 2026-10-29. The student-recorded evidence behind
the four CACAO rows could therefore not be inspected, and the abstract-only rows
(PMID:11222604, PMID:18398006) were judged from the published abstracts plus the later
mechanistic literature.

## What the protein is

Doc is a 126-residue protein encoded by the second gene of the *phd/doc* operon of
bacteriophage P1, which lysogenises *E. coli* as a single-copy plasmid prophage
[PMID:8411153 "P1 lysogens of Escherichia coli carry the prophage as a stable low copy
number plasmid"]. It is the toxin of a type II toxin–antitoxin (addiction) module: loss
of the prophage stops synthesis of the labile antitoxin Phd, ClpXP degrades the residual
Phd, and free Doc kills the plasmid-free segregant [PMID:8411153 "The plasmid withdrawal
response depends on a gene named doc (death on curing), encoding a 126 amino acid
protein."; PMID:9829946 "Degradation of antidote by the host-encoded ClpXP protease
liberates the toxin, which then poisons the plasmid-free segregant"].

Structurally it is a single Fido (Fic/Doc) domain, PROSITE PS51459, Pfam PF02661 Fic,
NCBIfam TIGR01550 DOC_P1, with four crystal structures (3DD7, 3DD9, 3K33, 3KH2)
[file:BPP1/doc/doc-uniprot.txt "DOMAIN 4..120 /note=\"Fido\""]. Its Fic motif
HxFx(D/N)(A/G)NKR is degenerate relative to the canonical AMPylating motif
[PMID:24448800 "The Fic motif H X F X (D/N)(A/G)NKR of Doc proteins differs slightly from
that in other Fic proteins"], and that degeneracy is what converts the enzyme from an
adenylyltransferase to a kinase.

## Core mechanism: an EF-Tu Thr kinase, not a ribosome blocker

The mechanism was revised between 2008 and 2014, and this matters for the GO annotations.

**2008 model (superseded in its mechanistic part).** Liu et al. showed that inducing Doc
in *E. coli* arrests growth and sharply inhibits translation without perturbing
transcription or replication, and does so without mRNA cleavage [PMID:18398006 "Doc
expression resulted in rapid cell growth arrest and marked inhibition of translation
without significant perturbation of transcription or replication."]. They interpreted
this as direct occupancy of the 30S subunit at the hygromycin B site in helix 44
[PMID:18398006 "Doc toxicity is the result of inhibition of translation elongation,
possibly at the translocation step, through its interaction with the 30S ribosomal
subunit."]. The *phenotype* (host translation inhibited) is solid; the *mechanism* (30S
occlusion) is not.

**2013/2014 model (current).** Two independent groups showed that Doc is a protein kinase
that phosphorylates a single conserved threonine of elongation factor EF-Tu:

- Castro-Roa et al. reconstituted translation from purified components and found Doc had
  no effect when added to ribosomes before initiation or to preformed ternary complexes,
  but blocked peptide synthesis when allowed to act on free EF-Tu
  [PMID:24141193 "These results indicated that Doc does not interfere with tRNA binding to
  ribosomes, as was suggested earlier13 but rather inhibits formation of the ternary
  tRNA:EF-Tu:GTP complex."]. Phosphorylation of Thr382 renders EF-Tu unable to bind
  aminoacyl-tRNA [PMID:24141193 "Doc is a new type of kinase that inhibits bacterial
  translation by phosphorylating the conserved threonine (Thr382) of the translation
  elongation factor EF-Tu, rendering EF-Tu unable to bind aminoacylated tRNAs."]. The rate
  is ~20 EF-Tu per second per Doc, and either ATP or GTP serves as donor
  [PMID:24141193 "We found that Doc phosphorylated EF-Tu (using either ATP or GTP) at a
  relatively high rate of ~20 EF-Tu molecules per second by one molecule of Doc"].
  They explicitly reassign the 2008 ribosome association to an indirect effect
  [PMID:24141193 "Co-purification of Doc with ribosomes as found in an earlier study13 is
  likely caused by association of Doc with ribosomes through EF-Tu."] and conclude
  [PMID:24141193 "Inhibition of translation by Doc is the direct result of phosphorylation
  of the translation elongation factor EF-Tu without the involvement of the ribosome
  itself or of any other player of the translation machinery."].
- Cruz et al. (the same Woychik lab that published the 2008 model) reached the same
  conclusion by an unbiased route: in a defined transcription/translation system Doc gave
  no [α-32P]ATP signal but a strong [γ-32P]ATP signal on a single ~43 kDa band
  [PMID:24448800 "potent phosphorylation of a single product migrating just above 40 kDa
  was observed, indicating that Doc is in fact a kinase"], identified as EF-Tu
  [PMID:24448800 "EF-Tu is the sole target of Doc toxin"], with MS/MS giving one site
  [PMID:24448800 "Sample analysis resulted in 100% protein coverage and yielded a single
  EF-Tu phosphorylation site in this Doc-treated sample at Thr-382"] confirmed genetically
  [PMID:24448800 "we demonstrated that Doc was unable to phosphorylate a T382A EF-Tu
  mutant"]. Activity requires the Fic histidine (H66Y is dead) and is abolished by Phd
  [PMID:24448800 "preincubation of Doc with Phd prevented labeling of EF-Tu"].

**Only a threonine is phosphorylated.** The Cruz MS search was run against EF-Tu with
"differential modifications of phosphorylated tyrosine, serine, and threonine residues"
[PMID:24448800] at 100% sequence coverage and returned Thr-382 alone. No serine
phosphorylation by Doc has been reported by anyone. This is the basis for the review's
treatment of `GO:0106310 protein serine kinase activity` (see below).

Residue numbering caveat: the papers write Thr-382 of mature *E. coli* EF-Tu, while
UniProt's FUNCTION line for Q06259 writes 'Thr-383' (P0CE47 numbering, which retains the
initiator Met). Same residue, two conventions — do not record a bare residue number
without saying which sequence it is on.

**Reverse reaction.** Doc also removes the phosphate when ADP or GDP is present
[PMID:24141193 "in the presence of ADP or GDP (the levels of which are likely elevated
during dormancy), the phosphorylation of EF-Tu could be reverted"], so the same active
site runs both directions depending on the nucleotide pool. Phd blocks both directions.

## Second function: Phd-dependent autoregulation of the operon, without DNA binding

Doc is a corepressor of its own operon, and does it through Phd rather than through DNA.
The decisive experiment is with the non-toxic DocH66Y allele: [PMID:9829946 "DocH66Y
failed to bind DNA in vitro yet enhanced the affinity, cooperativity, and specificity with
which Phd bound the operator."]. In vivo, Doc deepens Phd-mediated repression ~4-fold
[PMID:9829946 "transcription was repressed 40-fold, while in the presence of Phd,
transcription was repressed only 10-fold, indicating that under these conditions, Doc
enhanced repression about fourfold."], and at high Doc:Phd ratios the effect inverts
[PMID:9829946 "Strikingly, higher levels of Doc, obtained by adding higher concentrations
of IPTG, partially derepressed the operon"] — conditional cooperativity. The structural
basis: monomeric Doc engages two Phd dimers and orders Phd's intrinsically disordered
C-terminal domain, which in turn structures Phd's N-terminal DNA-binding domain
[PMID:20603017 "The binding of Doc to the intrinsically disordered C-terminal domain of
Phd structures its N-terminal DNA-binding domain"]. Doc does join the protein–DNA complex
(supershift) but contributes no DNA contact of its own [PMID:9829946 "Mobility of the
protein-DNA complex is further retarded in the presence of Doc, indicating that Doc may
directly participate in the protein-DNA complex"].

Comparator check: Phd itself (UniProtKB:Q06253) carries GO:0003677 DNA binding (IDA,
PMID:20603017), GO:0001217 DNA-binding transcription repressor activity and GO:0045892
negative regulation of DNA-templated transcription in GOA; Doc carries none of the
transcription terms but does carry GO:0003677 by UniProt keyword projection. The division
of labour in GOA is therefore exactly inverted from the experimental picture, and this
review corrects it (REMOVE GO:0003677; NEW GO:0003714 + GO:0045892).

## Relation to host death systems

Hazan et al. reported that *phd/doc* post-segregational killing requires the *E. coli*
chromosomal *mazEF* module [PMID:11222604 "Here we show that the postsegregational killing
mediated by the P1 phd-doc module depends on the presence of the E. coli mazEF system."]
and that host protein synthesis is inhibited under PSK conditions [PMID:11222604 "we
demonstrate that under conditions of postsegregational killing, mediated by phd-doc,
protein synthesis of E. coli is inhibited"]. Separately, Doc overexpression induces the
mRNA interferase activity of host RelE [file:BPP1/doc/doc-uniprot.txt "Overexpression of
doc can induce the mRNA interferase activity of host RelE in vivo"]. Both are downstream
host responses, not activities of Doc, and neither was annotated as such — correctly.

## Working judgements on the 13 GOA rows

| Term | Evid | Source | Action |
|---|---|---|---|
| GO:0004674 protein Ser/Thr kinase activity | IDA | CACAO (PMID:24448800) | ACCEPT (core) |
| GO:0004674 | IEA EC:2.7.11.1 | UniProt | ACCEPT |
| GO:0106310 protein serine kinase activity | IEA RHEA:17989 | RHEA | MODIFY → GO:0004674 (GO:0106311 protein threonine kinase activity was merged into GO:0004674) |
| GO:0005524 ATP binding | IEA KW | UniProt | ACCEPT |
| GO:0000166 nucleotide binding | IEA KW | UniProt | TOO_GENERAL |
| GO:0016301 kinase activity | IEA InterPro+KW | UniProt | TOO_GENERAL |
| GO:0016740 transferase activity | IEA KW | UniProt | TOO_GENERAL |
| GO:0003677 DNA binding | IEA KW-0238 | UniProt | REMOVE (+ source defect) |
| GO:0005515 protein binding (Phd) | IPI | IntAct | MODIFY → GO:0003714 |
| GO:0005515 protein binding (EF-Tu) | IPI | IntAct | MODIFY → GO:0004674 |
| GO:0039604 symbiont-mediated suppression of host translation | IDA | CACAO (PMID:18398006) | ACCEPT (core) |
| GO:0039604 | IMP | CACAO (PMID:11222604) | ACCEPT |
| GO:0044696 killing by virus of host cell by post-segregational killing | IMP | CACAO (PMID:11222604) | ACCEPT (core) |

Plus three NEW rows: GO:0005525 GTP binding (IDA, PMID:24141193), GO:0003714 transcription
corepressor activity (IDA, PMID:9829946) and GO:0045892 negative regulation of
DNA-templated transcription (IDA, PMID:9829946).

### CACAO assessment

All four CACAO rows survive. This is a well-curated gene product: each row is on the right
protein, from a paper that assays it, with an evidence code matching the assay, and with a
term at an appropriate granularity. None of the batch-1 failure shapes applies:

- Not phenotype-as-process. `GO:0039604` is the direct readout of both cited papers
  (translation inhibition), not an effect several steps downstream, and `GO:0044696` is
  the term GO created for precisely this addiction-module phenomenon.
- Not paper-not-about-gene. All four papers are about P1 Doc.
- Not single-assay localization. No CC rows exist for this protein at all.
- No wrong-arm or sign inversion.

The one notable point is a **timing** observation rather than a defect: the
`GO:0039604` IDA row rests on PMID:18398006, whose mechanistic conclusion (30S occlusion)
was overturned five years later by PMID:24141193 and PMID:24448800. The *term* is
unaffected, because GO:0039604 asserts the outcome and not the mechanism — but it is a
reminder that a CACAO row anchored to a mechanism paper can outlive the mechanism. This is
recorded in the review as a `finding_review` with `finding_status: OVERTURNED` on the
30S-binding finding, not as an action change. Worth adding to the taxonomy as
**mechanism superseded, term unaffected**: a row that remains correct for a reason the
original curator did not intend.

The defects in this gene's GOA are all on the *automatic* side, from UniProt keyword and
Rhea projection: a DNA-binding term that the 1998 paper explicitly refutes, and a
serine-kinase term for an enzyme with no serine substrate. Both predate and are unrelated
to the student work.
