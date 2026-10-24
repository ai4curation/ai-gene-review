# ARHGEF18 (p114RhoGEF) bioinformatics

Two questions, two scripts. Every number below is read from the JSON the scripts write;
re-running regenerates both files and any number that changes is a real change.

| script | writes | question |
|---|---|---|
| `dh_domain.py` | `dh_domain.json` | Is the DH/PH module competent, and can residues call the substrate? |
| `reference_coverage.py` | `reference_coverage.json` | Over-annotation, or missing curation? And is there an ortholog record to lean on? |

```
uv run python dh_domain.py --self-test
uv run python reference_coverage.py --self-test
```

Both self-tests pass as recorded here (`all_controls_pass = true`, 10 control blocks in
`dh_domain.json`; 23 primary papers classified in `reference_coverage.json`).

---

## 1. The catalytic module, reported in both directions

### 1.1 Two papers, two numbering systems, neither stated

ARHGEF18's two experimentally validated loss-of-function substitutions are reported in
numbering that does not match the current canonical sequence, and neither paper says
which sequence it used. `dh_domain.py` does not assume an offset; it enumerates every
offset UniProt's own record licenses and reports which put the paper's residue there.

| paper | as published | offsets tried | consistent | resolves to |
|---|---|---|---|---|
| Arno 2017 (PMID:28132693) | `p.Thr270Ala` | 0, +16, +188, +346 | 1 | **Thr-458** |
| Terry 2011 (PMID:21258369) | `p114RhoGEF-Y260A` | 0, +16, +188, +346 | 1 | **Tyr-606** |

The Arno mapping is a **positive control**, not a finding: UniProt independently records
that variant as `VARIANT 458 T->A`, so the +188 offset — the length UniProt added to the
N-terminus in sequence version 4 (10-OCT-2018, after the paper) — is confirmed from
outside this script.

Terry's tyrosine is the one that had to be derived. It resolves at +346, which is exactly
the offset of the `p114` isoform (`Q6ZSZ5-2`; `VAR_SEQ VSP_059874` deletes residues
1–346) — the protein Terry actually cloned. The **negative control** matters here: the
+188 offset that works for Arno puts an arginine at Terry's position, not a tyrosine, so
the two papers genuinely use different reference sequences and the assignment is not
arbitrary. Both resolved positions fall inside the UniProt DH domain (447–644).

### 1.2 The tyrosine is real, and it is uninformative about substrate

Terry justified the Y→A substitution by noting that "analogous mutations were previously
shown to inactivate the GEF activities of GEF-H1 and Lbc". That is a checkable claim, so
the script checks it rather than repeating it. At the alignment column holding ARHGEF18
Tyr-606:

* **all 14 real panel members carry a tyrosine** — including ARHGEF2/GEF-H1 (Tyr-394) and
  AKAP13/Lbc (Tyr-2153), the two proteins Terry named;
* the scrambled control carries a lysine.

So the residue argument **supports** catalytic competence. It does not establish it, and
it does not need to: Blomquist et al. 2000 (PMID:11085924) showed the purified protein
"efficiently catalysed guanine nucleotide exchange of RhoA". Residue analysis here is
corroborative by construction.

The other direction is the more useful one. That same tyrosine is equally conserved in
TIAM1 and TRIO/KALRN DH1 (RAC1-specific) and in ITSN1 (CDC42-specific). It is a
pan-Dbl-family position.

**Bottom line: Tyr-606 is conserved in all 14 panel members including the Rac- and Cdc42-specific GEFs, so retaining it says the DH domain is of the catalytically competent type and says nothing whatever about which GTPase ARHGEF18 acts on.**

### 1.3 Can sequence arbitrate the RhoA-versus-Rac1 disagreement? No.

The two discovery papers disagree, and UniProt carries both:

* Blomquist 2000 — "interacted specifically with RhoA … **but not with Rac1 and Cdc42**";
* Niu 2003 (PMID:14512443) — "p114RhoGEF activated **RhoA and Rac1** but not Cdc42".

The test: compute the GTPase-contacting residues in two structures — LARG/ARHGEF12 DH/PH
bound to **RhoA** (PDB 1X86, 24 DH contacts at 4.0 Å) and TIAM1 DH/PH bound to **RAC1**
(PDB 1FOE, 26 DH contacts) — map both anchor sets through a DH-domain alignment, and take
Δ = %identity(RhoA anchors) − %identity(RAC1 anchors).

The classifier is validated before it is read, on held-out proteins with declared
specificity (both anchors excluded; two RAC1-specific GEFs — TRIO DH1 and KALRN DH1 —
deliberately included from outside the anchor's own family so the contrast is not
circular):

| protein | Δ | truth | predicted |
|---|---|---|---|
| ARHGEF1/p115RhoGEF | +60.9 | RHOA | RHOA ✓ |
| ARHGEF11/PDZ-RhoGEF | +40.7 | RHOA | RHOA ✓ |
| AKAP13/Lbc | +18.9 | RHOA | RHOA ✓ |
| ARHGEF2/GEF-H1 | +11.2 | RHOA | RHOA ✓ |
| ARHGEF28/RGNEF | +10.6 | RHOA | RHOA ✓ |
| TRIO (DH1) | −4.8 | RAC1 | RAC1 ✓ |
| KALRN (DH1) | −4.8 | RAC1 | RAC1 ✓ |
| TIAM1 (human) | −66.7 | RAC1 | RAC1 ✓ |

**8/8 correct.** And yet the ARHGEF18 answer is still not usable:

* **ARHGEF18 Δ = +10.9** — inside the RhoA group's range [+10.6, +60.9], but *at its very
  bottom edge*, 0.3 points from ARHGEF28 and 0.3 from GEF-H1. The distance to the nearest
  RAC1 member is 15.7 points, so the sign is not marginal, but the position within the
  RhoA group carries no information.
* **ITSN1, a CDC42-specific GEF, scores +6.7** — i.e. on the "RhoA" side, in the same
  narrow band as ARHGEF18. The classifier has no CDC42 axis and would mislabel a CDC42
  GEF as RhoA. ARHGEF18 sits in a band that contains a GEF for the one GTPase both
  primary papers agree it does **not** act on.

So the honest reading is: the DH surface is consistent with RhoA and inconsistent with a
TIAM1-like Rac interface, which agrees with Blomquist — but the metric cannot exclude
Rac1 activity of the kind Niu reported in cells, and its behaviour on ITSN1 shows it
should not be pushed. **The substrate question is not settled by sequence.** It is also
not settled by the literature: the one systematic Dbl-family exchange-kinetics panel
(Jaiswal et al., 21 Dbl proteins × 12 Rho GTPases) does not include p114RhoGEF.

### 1.4 The one piece of structure that is ARHGEF18's own

Everything above maps *other* proteins' contacts onto ARHGEF18. **PDB 6BCB is different:
it is ARHGEF18 itself** — the mouse PH domain bound to activated RhoA at 1.4 Å, from
Chen et al. 2018 (PMID:29876405), the structural counterpart of the positive-feedback
binding Medina et al. 2013 (PMID:23493395) reported for all seven Lbc-family RhoGEFs.
This structure is cited nowhere in ARHGEF18's GO record.

Ten mouse PH residues contact RhoA at 4.0 Å. **All ten are identical in human ARHGEF18**:

| mouse Arhgef18 | human ARHGEF18 |
|---|---|
| Ile-779, Arg-781, Glu-782, Val-783, Ala-784, Asn-785, Phe-791, Ile-793, Pro-800, Met-802 | Ile-740, Arg-742, Glu-743, Val-744, Ala-745, Asn-746, Phe-752, Ile-754, Pro-761, Met-763 |

**Bottom line: all ten RhoA-contacting residues of the mouse PH domain are identical in human ARHGEF18 and all ten lie inside the human PH domain (684-786), so the RhoA-binding interface is conserved without exception across the orthologs.**

The same interface is 90% conserved in
AKAP13 and 80% in GEF-H1 — the Lbc clade — and 10–30% in TIAM1, TRIO, KALRN and ITSN1.
The reciprocal test on 6BCA (the AKAP13 PH·RhoA structure from the same paper) puts
ARHGEF18 at 75%, again well above every Rac/Cdc42 GEF.

This is a **molecular function that GO does not record for this gene at all**: a
GTP-loaded-RhoA-binding surface on the PH domain, distinct from the DH exchange site,
resolved at 1.4 Å in the protein itself.

### 1.5 Controls

| control | kind | outcome |
|---|---|---|
| structure→sequence fit, 1X86 | positive | offset 0, 99.7% over 362 residues, runner-up 16.4%; agrees with PDBe SIFTS |
| structure→sequence fit, 1FOE | positive | offset 0, 100% over 368 residues, runner-up 21.4%; SIFTS omits author numbering for this legacy entry, which is why the fit exists |
| structure→sequence fit, 6BCB | positive | offset +384, 97.9%; chain is an ARHGEF18 ortholog |
| Arno variant resolves to Thr-458 | positive | pass (asserted independently by UniProt) |
| ARHGEF2 carries Tyr at Terry's column | positive | pass (Tyr-394) |
| mouse→human PH contacts conserved | positive | 100%, scrambled control 0% |
| Terry's position at the Arno offset | negative | Arg, not Tyr — offsets are distinguishable |
| RHOA and DOCK2 excluded by the DH gate | negative | both excluded; DOCK2 is a genuine RAC1 GEF with no DH domain, so the gate is tested against a GEF and not only against a GTPase |
| scrambled DH domain vs anchors | negative | 4.2% (1X86) and 0.0% (1FOE), against a real-protein minimum of 33.3% and 26.9% |

One bug was caught by these guards rather than by inspection: waters, the GTP analogue
and Mg are deposited under the *same* author chain as the protein in 6BCB, and counting
them as residues drove that structure's fit to 48% identity. The fit guard failed, the
polymer filter was added, and the fit went to 97.9%.

---

## 2. Over-annotation, or missing curation?

`reference_coverage.py` asks QuickGO **by reference** rather than by gene, species-blind,
for 23 papers whose subject is ARHGEF18 itself (its protein, its gene, its ortholog, or a
patient allele), plus four high-throughput sources held separately.

**19 of the 23 primary papers have produced no GO annotation on any gene, in any
species.** None is undetermined — every result set fit inside one page, so every zero is
a real zero rather than an unseen page.

| PMID | paper | annotations anywhere |
|---|---|---|
| 11085924 | Blomquist 2000 — the founding in-vitro exchange assay, RhoA-specific | **0** |
| 15558029 | Nagata 2005 — SEPT9b binds and inhibits SA-RhoGEF | **0** |
| 20810787 | Tsuji 2010 — Dvl/Daam1; Wnt-3a-induced RhoA activation | **0** |
| 21258369 | Terry 2011 *Nat Cell Biol* — junctional RhoA, cingulin/ROCK-II/myosin-IIA | **0** |
| 23185572 | Terry 2012 — cortical myosin double phosphorylation, migration, invasion | **0** |
| 23493395 | Medina 2013 — activated RhoA binds the Lbc PH domains | **0** |
| 23648482 | Xu 2013 — LKB1 interaction, apical junction assembly | **0** |
| 23698346 | Herder 2013 — medaka `arhgef18` mutant, retinal apicobasal polarity | **0** |
| 26217016 | Loie 2015 — CRB3A/Ehm2 recruitment | **0** |
| 26483385 | Kim 2015 — lumen consolidation in tubulogenesis | **0** |
| 28132693 | Arno 2017 *AJHG* — biallelic mutation causes RP78 | **0** |
| 28536193 | Schell 2017 *PNAS* — EPB41L5 binds and recruits ARHGEF18 in podocytes | **0** |
| 29876405 | Chen 2018 — 1.4 Å p114RhoGEF-PH·RhoA structure (PDB 6BCB) | **0** |
| 31051012 | Martin 2016 — Gα12-specific binding region | **0** |
| 31409654 | Silver 2019 — Drosophila ortholog Cysts, Crumbs/Bazooka, Rho1 | **0** |
| 33842485 | Beal 2021 — syncytiotrophoblast differentiation | **0** |
| 36912772 | Safavian 2023 — SEPTIN9 activates ARHGEF18 at the ciliary base | **0** |
| 39977269 | Batta 2025 — shear-stress-responsive endothelial barrier | **0** |
| 40920138 | Shannon 2025 — SEPTIN9–ARHGEF18 at mitochondrial fission sites | **0** |
| 14512443 | Niu 2003 — Gβγ stimulation | 4, all on ARHGEF18 |
| 22006950 | Nakajima 2011 — Lulu2/Patj | 11, 2 on ARHGEF18 |
| 25753039 | Tornavaca 2015 — ZO-1/JACOP | 43, 3 on ARHGEF18 |
| 29601110 | Turton 2018 — eosinophil isoforms | 1, on ARHGEF18 |

High-throughput sources, held separately because a zero there means something different:
PMID:18570454 exosome proteomics (66 annotations, one on ARHGEF18), PMID:35271311
OpenCell (2876, truncated), PMID:18669648 and PMID:21269460 (0 each).

### There is no ortholog record to lean on

The obvious remedy for a thin human record is to lean on an ortholog — ISS or IBA both
need a curated source somewhere. So the script asks the complementary question, and the
answer closes that door:

| gene product | annotations | experimental | evidence codes |
|---|---|---|---|
| mouse `Arhgef18` (Q6P9R4) | 23 | **0** | ISO 10, IEA 6, IBA 4, ISS 3 |
| human `ARHGEF18` (Q6ZSZ5) | 32 | 14 | IDA 7, TAS 8, IEA 6, IBA 4, EXP 2, IMP 2, IPI 2, HDA 1 |

Neither result set was truncated, so both counts are totals rather than floors. The human
row is the **positive control** for the evidence-code split: if it had come back at zero
experimental, the mouse zero would be an artefact of the classifier rather than a finding.

The mouse record is not an independent record. Ten of its 23 rows are ISO — projected
*from* human — so transferring back by similarity would only recirculate the same four
experiments. And note where that leaves PDB 6BCB: the 1.4 Å RhoA complex was solved on
the **mouse** protein, and the mouse record does not carry it either.

### What that means

**ARHGEF18's GO record is a coverage failure, not an over-annotation problem.** Every
experimental row it carries is defensible. The problem is the size of what is absent:

* the **founding biochemistry** (PMID:11085924) produced nothing, so ARHGEF18's only
  molecular-function annotation traces to Niu 2003 — the paper whose title asserts the
  Rac1 activity that Blomquist's freely readable abstract contradicts;
* the paper that defined the gene's central cell-biological role (Terry 2011, *Nat Cell
  Biol*) produced nothing;
* the **human disease paper** (Arno 2017, *AJHG*) produced nothing;
* the only **structure of the protein** produced nothing;
* an entire vertebrate **knockout** (medaka) produced nothing.

Meanwhile the *Drosophila* ortholog `cyst` **is** curated — `GO:0005085` IDA,
`GO:0090688` IDA and `GO:1902408` IEP, from PMID:36917931 — annotations that could
legitimately seed ISS or IBA to the human gene and have not.

Three of the missed papers were found only by searching partners, paralogs and
misspellings rather than the gene symbol: Chen 2018 is titled for the *family*
("Lbc family of RhoGEFs"), Safavian 2023 is titled for the *partner* ("Septin-mediated
RhoA activation"), and Schell 2017 is titled for a *different protein* and spells the
gene **"ARGHEF18"** in its own abstract — "by binding and recruiting the RhoGEF ARGHEF18
to the leading edge".
