# phi29 gene 4 (late genes activator p4, P03682) review notes

## Provenance / method

- **Deep research was NOT available in this container** (no provider API keys), so no
  `4-deep-research-*.md` file exists and none was fabricated. Research was done directly
  from the cached publications, the UniProt flat file, NCBI E-utilities, Europe PMC,
  QuickGO, InterPro and WebSearch/WebFetch.
- Papers cached for this review with `just fetch-pmid`: PMID:8432697, PMID:8799127,
  PMID:16600871, PMID:7831803 and PMID:3027653 (abstract only); PMID:21614197 and
  PMID:11689446
  (**full text**, the latter via the ETL's PMC HTML fallback).
- **PMID:12426390 (Calles, Salas & Rojo 2002, EMBO J; PMC137212).** The brief asked for
  another attempt at this paper. *I could read the whole paper*, but only out-of-band:
  `curl` of the rendered PMC page (`https://pmc.ncbi.nlm.nih.gov/articles/PMC137212/`)
  returns the full article HTML (192 kB: Results, Table I, all six figure legends,
  Discussion, Materials and methods). What is **not** available: the PMC OA XML endpoint
  answers "The publisher of this article does not allow downloading of the full text in
  XML form", Europe PMC `fullTextXML` returns HTTP 500, and a forced
  `cache_publication(force=True)` tries XML, then HTML, then PDF and still writes
  `full_text_available: false`. So the repository cache for PMID:12426390 is
  **abstract-only**, and nothing from its body is quotable as `supporting_text`.
  Everything attributed below to its full text comes from the out-of-band read and is
  used as reasoning, not as a quotation.
- **GONUTS is retired, not offline.** `gowiki.tamu.edu` now answers HTTP **410** with
  "GONUTS, the GO wiki, has been retired", and `archive.org/wayback/available` has **no
  snapshot** of `PMID:820555`, `PMID:12426390` or `BPPH2:P03682`. The student evidence
  behind the CACAO rows is permanently unrecoverable, so no row in this review is left
  UNDECIDED pending a GONUTS re-check.
- PMID:820555 (1976) full text is unreachable: Wiley/FEBS returns HTTP 403 (Cloudflare)
  on the article, ePDF and DOI URLs. Only the abstract was available.

## Biology of p4

- 125-residue early protein; the master regulator of the phi29 early-to-late switch.
  Phage gene expression is read out by the **host** *B. subtilis* sigma-A RNA
  polymerase, with no phage-encoded polymerase and no phage sigma factor
  [PMID:21614197 "Phage Ø29 gene expression is directed by the Bacillus subtilis σ A -RNAP"].
- Genome organisation: early genes at both genome ends, late genes in the middle
  [PMID:21614197 "Genes coding for structural proteins and for proteins involved in morphogenesis and cell lysis, centered in the genome, are coded in the complementary DNA strand and are transcribed at later times of infection."]
  and [PMID:21614197 "Late genes are expressed from a single promoter, A3."]
- p4 binds specific sites and both activates A3 and represses A2b/A2c
  [PMID:21614197 "Protein p4 binds to specific target sites and is required for the activation of the late promoter A3 and for the repression of early promoters A2b and A2c"].
- Activation: p4 bound between -50 and -100 relative to the A3 start bends the promoter
  and stabilises RNAP as a **closed complex**
  [PMID:2107318 "binds to a region of the A3 promoter, located between nucleotides -50 and -100"],
  [PMID:8617213 "Activation involves stabilization of RNA polymerase (RNAP) at the A3 promoter as a closed complex"].
  A3 cannot be used without p4, having a poor -35 element
  [PMID:11689446 "RNAP binds to promoters A2c and A2b, but not to promoter A3 that lacks a –35 element"].
- Repression: at A2c, p4 binds immediately upstream of RNAP and blocks **promoter
  clearance** rather than RNAP binding
  [PMID:8799127 "represses the strong viral A2c promoter (PA2c) by preventing promoter clearance; it allows RNA polymerase to bind to the promoter and form an initiated complex, but the elongation step is not reached."].
  At A2b the p4(-p6) complex **displaces** RNAP
  [PMID:11689446 "Concomitantly, the RNAP-derived hypersensitive band at promoter A2b disappeared (band at –134; compare lanes n and p), indicating displacement of RNAP."].
- Both activation and repression run through one contact, to the **C-terminal domain of
  the RNAP alpha subunit**, mainly via p4 Arg120
  [PMID:8617213 "Mutation of protein p4 residue Arg120, which relieves the contact between the two proteins, leads to a loss of repression."],
  [PMID:8799127 "Protein p4 could form a complex at PA2c with purified wild-type alpha subunit, but not with a deletion mutant lacking the 15 C-terminal residues."].
  UniProt curates MUTAGEN 120 "R->Q: 80% loss of transcription activation from the A3
  promoter and 80% loss of transcription repression from the A2c promoter. Complete loss
  of interaction with host RNAP." with ECO:0000269|PubMed:8617213.
- DNA binding is sequence-specific, through an H-T-H motif (UniProt FT DNA_BIND 77..96)
  and an N-hook (PDB 2FIO/2FIP; PMID:16600871); each site is an inverted repeat of two
  6 bp arms separated by a 15 bp spacer, and sites 1 and 3 overlap the -35 boxes of A2c
  and A2b (PMID:12426390 full text, Figures 1A and 6A).
- In vivo a gene-4 nonsense mutant abolishes the switch
  [PMID:11689446 "In bacteria harbouring a nonsense mutant in gene 4, transcription from promoters A2b and A2c increases steadily during infection while the transcripts arising from promoter A3 are almost undetectable"].
- p4 works with the nucleoid protein p6: the two bind cooperatively over the ~200 bp
  A2c-A3 region
  [PMID:12426390 "Proteins p6 and p4 bind cooperatively to an approximately 200 bp DNA region located between the late A3 and the early A2c promoters"],
  and the complex needs the p4 C-terminus
  [PMID:12426390 "We show that stable assembly of this complex requires interaction between protein p6 and the C-terminus of protein p4."].
- **p4 is neither a sigma factor nor a polymerase.** It is not a subunit of RNAP: it is a
  DNA-site-bound regulator that touches alpha-CTD from outside the holoenzyme and stays
  on its site rather than being released at elongation. The "sigma-like" reading is a
  surviving 1980s speculation, still visible in InterPro's own description of IPR008771
  ("may function as a sigma-like component of the host RNA polymerase").

## Shape (a): screen 1, one-paper-many-genes (PMID:820555) — PRESENT

The 2025 CACAO campaign put PMID:820555 on seven phi29 entries. The 1976 abstract
supports exactly two kinds of claim, and they map onto the rows like this:

| Claim in the abstract | Rows it produced | Verdict |
|---|---|---|
| "Mutants in six genes do not synthesize phage DNA." | GO:0039693 on genes 1, 2, 3, 6, 17 (five of the six) | consistent; gene 5 carries GO:0039693 from another paper |
| "A cistron, probably involved in the final lysis of the infected bacteria, has been found." (**one** cistron) | GO:0044659 on gene **4** (P03682) and gene **15** (P11187) | **one of the two is a mis-attribution** |

Gene 4 cannot be the 1976 lysis cistron, and this follows from the abstract alone:

1. The paper reports a **single** lysis cistron, and two entries got the row.
2. The mutant's phenotype was *delayed lysis with a normal or higher burst after
   artificial lysis*
   [PMID:820555 "Mutants in this gene give place, under restrictive conditions, to delayed lysis and produce, after artificial lysis, a burst size similar or higher than that obtained after wild-type phage infection."].
   A gene-4 nonsense mutant makes **no late transcripts at all** (PMID:11689446, quoted
   above), hence no capsid, scaffold, tail or packaging proteins, hence no burst to
   release. The reported phenotype excludes gene 4 by construction.
3. Gene 4 is an early gene; the lysis genes are late genes **downstream** of the single
   promoter p4 activates (PMID:21614197, quoted above).

Which gene the 1976 cistron is cannot be settled from that abstract on phenotype alone,
because a holin null and an endolysin null both give delayed lysis with a normal burst.
The two candidates are adjacent late lysis genes: gene **14** = holin/antiholin
(UniProtKB:P11188) and gene **15** = endolysin (UniProtKB:P11187). Three independent
lines point at **gene 14**:

- it is the gene with a *sus* allele in that region, and that allele is the one the 1976
  screen would have carried
  [PMID:3027653 "The g14 open reading frame (ORF) was confirmed by sequencing a sus14(1241) mutant."];
- its product is the one shown to be required for lysis
  [PMID:8432697 "Phage phi 29 gene 14, the product of which is required for efficient lysis of Bacillus subtilis, was cloned in Escherichia coli."];
- it is the holin, gene 15 being the lysozyme it releases
  [PMID:7831803 "The 131-codon gene 14 of Bacillus subtilis phage phi 29 encodes the holin function, whereas the downstream gene 15 codes for a lysozyme."],
  and delayed lysis with an undiminished burst is the canonical holin-null phenotype.

So the row belongs on **P11188 (gene 14)**, which carries no CACAO row at all, and not on
P03682. The parallel review of gene 15 reached the same conclusion from the same
literature; both reviews rate it PROBABLE rather than CONFIRMED, because the 1976 Eur J
Biochem paper is not in PMC and its text cannot be read. A single-cistron claim was
therefore spread across two numbered genes — 4 and 15 — and missed the one it was about.

**Shape verdict: PRESENT**, in the numeric form the T4 gp5.4 case predicted: a paper's
"gene 14" landing on the entry named "4". The error is selective in the direction the
number predicts — the DNA-replication half of the same paper was distributed correctly
across five genes, and only the lysis half slipped. Gene 4 is also genuinely, if
indirectly, required for lysis (no p4, no A3, no holin and no endolysin), which is what
lets the row survive a term-level sanity check, and why it is recorded as an
over-annotation with a source defect rather than a flat REMOVE: the term is not false,
its evidence is another gene's.

The hedged qualifier `acts_upstream_of_or_within_positive_effect` is on all ten of
phi29's 2025 CACAO rows, so it carries no per-row information. A QuickGO census of the
38 experimental GO:0044659 rows (run for the parallel gene-15 review) shows the hedge is
not a CACAO convention either: 31 rows are `involved_in`, 18 of them CACAO's own, and all
5 hedged rows are from this one 2025-2026 campaign. For gene 4 the hedge happens to be
the only qualifier under which the row is defensible at all, but that is a coincidence
rather than a judgement, and it does not rescue the row: the qualifier plays no part in
the action below, which rests on the term and the evidence.

## Shape (b): PARTNER-MUTANT IMP on p6 from PMID:12426390 — CONFIRMED, as an evidence-code defect

The p6 notes (`genes/BPPH2/6/6-notes.md`) flagged but could not confirm that p6's four
CACAO rows from PMID:12426390 rest on mutants of **p4**, this gene. Having read the whole
paper out-of-band, I can confirm it and sharpen it:

- **Every mutant in the paper is a p4 mutant or a DNA-site mutant.** The p4 series is
  the C-terminal deletion p4(CΔ14+2) plus the single substitutions R116S, L117A, R118Q,
  E119Q, R120Q, R121S and K122Q (Figure 1B, Table I); the DNA series is the A2c promoter
  site mutants A2c-X, A2c-dn and A2c-up (Figure 6). The Results say it plainly: "the
  ability of a set of protein p4 mutants to form such a complex was analysed. The p4
  derivatives used ... contain substitutions or deletions at the C-end", and Table I's
  footnote is "All the p4 mutants analysed can bind to DNA".
- **There is no p6 mutant and no mutant phenotype of any kind.** Materials and methods
  lists purified *B. subtilis* sigma-A RNAP, purified **wild-type** p6, and wild-type or
  mutant p4; the assays are in vitro transcription on TP-DNA, DNase I footprinting and
  band-shift. No phage infection, no *sus* allele, no in vivo experiment. This matches
  what the p6 notes had recorded second-hand.
- **Consequence for p6's rows.** The paper's biology about p6 is sound and directly
  shown: p6 is physically in the p4-p6-DNA complex, p4 raises p6's affinity for the
  A2c-A3 region more than 16-fold, and the stable complex displaces RNAP from A2c. So
  the p6 claims are supported — **as IDA**, purified protein in vitro. What is not
  supported is **IMP** on p6: the mutated entity in every experiment is p4 or the DNA
  site, so no row from this paper can rest on a p6 mutant phenotype. p6's three
  `IMP`/`ECO:0000315` rows from this reference (GO:0001217, GO:0006351, GO:0017053) have
  a `WRONG_EVIDENCE_CODE` defect; its `IDA` GO:0017053 row does not. *This is a finding
  for issue #5733; I have not touched the p6 files.*
- **Does the paper support anything on p4?** Yes, strongly — and this is the inversion
  worth recording. Because the mutant series is p4's, **p4** is the gene for which this
  reference can carry mutant-based evidence, and it establishes that p4's C-terminal
  basic residues are the p6-contact determinants, distinct from the Arg120 determinant
  used for RNAP, and that p4 bound at A2c site 1 nucleates and phases the p6 filament.
  Yet **P03682 carries no GOA row citing PMID:12426390 at all**: the paper whose mutants
  are p4's is cited four times for p6 and zero times for p4. The review therefore cites
  it in prose and in `references` but adds no `NEW` row for the p4-p6 contact, since
  bare protein-binding terms are uninformative and the contact's functional consequence
  is already carried by the activator and repressor rows.

**Shape verdict: PRESENT (confirmed), with a correction to its name.** It is not "IMP
attributed to the wrong gene" — the biology really is p6's. It is "IMP where the mutant
belongs to the partner": a mis-stated evidence *code*, direct in vitro reconstitution
reported as mutant phenotype because a mutant was indeed used, just not of the annotated
protein. The pattern is screenable corpus-wide: an IMP row whose reference's only mutants
are of a different gene product that is itself annotated from the same reference.

## Other defects found (not CACAO)

- **InterPro IPR008771 "Phi-29-like late genes activator"** maps to GO:0003899
  *DNA-directed RNA polymerase activity* and GO:0016987 *sigma factor activity* as well
  as GO:0006355 (checked live against the InterPro API). The first two are wrong: p4 has
  no catalytic activity and is not an RNAP subunit. The family description still says the
  protein "may function as a sigma-like component of the host RNA polymerase", which is
  the speculation those two GO mappings encode.
- **UniProt keyword KW-0731 "Sigma factor"** on P03682 drives the same GO:0016987 claim
  (the entry's own `DR GO; GO:0016987 ... IEA:UniProtKB-KW` line shows the route), and
  GO_REF:0000108 then derived GO:2000142 from it by inter-ontology inference. One wrong
  keyword thus produced two rows. GO:0016987's definition is explicit that a sigma factor
  is "the promoter specificity subunit" of the polymerase and "is released once elongation
  begins", neither of which is true of p4.

## Row-by-row decisions

| Term | Ev | Ref | Action | Why |
|---|---|---|---|---|
| GO:0003677 DNA binding | IDA | 2107318 | MODIFY to GO:0000987 | binding is to inverted-repeat recognition sites in the A3/A2b/A2c regulatory region, not generic DNA |
| GO:0003677 DNA binding | IEA | GO_REF:0000043 | MODIFY to GO:0000987 | same claim, same refinement (KW-0238) |
| GO:0003899 DNA-directed RNA polymerase activity | IEA | GO_REF:0000002 | REMOVE | InterPro2GO from IPR008771; p4 has no polymerase activity |
| GO:0006355 regulation of DNA-templated transcription | IDA | 8617213 | MODIFY to GO:0045893 + GO:0045892 | both directions demonstrated for p4 |
| GO:0006355 | IEA | GO_REF:0000120 | MODIFY to GO:0045893 + GO:0045892 | same claim |
| GO:0016987 sigma factor activity | IEA | GO_REF:0000120 | REMOVE | KW-0731 plus IPR008771; p4 is not an RNAP subunit |
| GO:0044659 viral release from host cell by cytolysis | IMP | 820555 | MARK_AS_OVER_ANNOTATED | shape (a): indirectly true, evidence is gene 14's (P11188) |
| GO:2000142 regulation of DNA-templated transcription initiation | IEA | GO_REF:0000108 | MODIFY to GO:2000144 + GO:2000143 | true claim on a false basis, refined to the demonstrated directions |
| GO:0001216 DNA-binding transcription activator activity | IDA | 8617213 | NEW | GOA carries no MF transcription-regulator term for p4 |
| GO:0001217 DNA-binding transcription repressor activity | IDA | 8617213 | NEW | the repression side of the same activity |
| GO:0070063 RNA polymerase binding | IPI | 8799127 | NEW | the alpha-CTD contact is the mechanism of both activities |
