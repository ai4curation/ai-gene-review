# MIM1 (YOL026C / TOM13), *Saccharomyces cerevisiae* — research notes

UniProt: Q08176 · SGD: S000005386 · 113 aa, 12.8 kDa · single predicted TM helix (residues 39–62)
Pfam PF08219 (TOM13) · InterPro IPR013262 (OMP_MIM1/TOM13_mt) · PANTHER PTHR28241 / PTHR28241:SF1
ComplexPortal CPX-2281 (MIM mitochondrial import complex)

> **Provenance note.** All automated deep-research providers failed in this environment
> (falcon → HTTP 402 Payment Required; perplexity → provider not configured; openai →
> invalid API key), so no `MIM1-deep-research-<provider>.md` file exists. The notes below
> were assembled by hand from the cached publications in `publications/` and from the
> UniProt record. Every assertion carries an inline citation with verbatim supporting text.

---

## 1. Identity and discovery

`YOL026C` was independently named twice in 2004–2005:

- **Tom13**, in a screen for essential outer-membrane proteins of unknown function
  [PMID:15326197 "Tom13, the gene product of YOL026C"].
- **Mim1** (*mitochondrial import 1*), in a proteomic characterisation of the *Neurospora
  crassa* outer membrane whose 14.2 kDa hit was traced to the *S. cerevisiae* orthologue
  [PMID:15608614 "A protein of a molecular mass of 14.2 kDa (NCU01101.1) that had a high
  sequence similarity to Mim1 (mitochondrial import) from Saccharomyces cerevisiae (open
  reading frame YOL026C ) was identified."].

Mim1 is the accepted name; Tom13 survives as a synonym and as the Pfam family name. Note
that despite the "Tom13" name, **Mim1 is not a TOM-complex subunit** — see §3.

## 2. Localisation and topology

Mitochondrial outer membrane, integral, with the N-terminus facing the cytosol.

- Protease-protection and alkaline-carbonate extraction of isolated mitochondria place
  Tom13/Mim1 as an integral outer-membrane protein
  [PMID:15326197 "Tom13 and Tom38 are mitochondrial outer membrane proteins"].
- Independently confirmed by protease shaving of mitochondria carrying an N-terminally
  His-tagged allele: "Mim1 was degraded and could no longer be immunodecorated with
  antibodies against the His tag ( Fig 1E ). Hence, the N terminus of the protein is
  exposed to the cytosol." [PMID:15608614].
- The topology is cytosolic-N / IMS-C with one central α-helical TM segment
  [PMID:28916712 "The 13-kD protein Mim1 contains a predicted central α-helical
  transmembrane segment and exposes its N-terminal domain to the cytosol and its
  C-terminal domain to the intermembrane space"].

UniProt records `Mitochondrion outer membrane` with ECO:0000269 from both PMID:15326197
and PMID:15608614. This is one of the best-supported facts about the protein.

## 3. The MIM complex

Mim1 self-associates into an oligomer that is the bulk of a ~400–450 kDa complex, distinct
from both TOM and TOB/SAM:

- [PMID:15608614 "Mim1 was present in a high-molecular-mass complex of a molecular size of
  about 400–450 kDa, which is distinct from that of the TOM and TOB complexes."] and
  "Therefore, Mim1 is not a Tom or Tob component."
- [PMID:28916712 "Mim1 oligomers form the major constituent of the MIM complex"].

The second, low-abundance subunit is **Mim2** (Q3E798, ~10 kDa, same topology, 1–2 copies
per complex):

- [PMID:22467864 "Mim2 physically and\ngenetically interacts with Mim1, and both proteins
  form the MIM complex."] — this is the reference behind both the `GO:0140595 MIM complex`
  IPI annotations and the `GO:0005515 protein binding` IPI (WITH `UniProtKB:Q3E798`).
- [PMID:28916712 "A second subunit, the 10-kD protein Mim2, possesses the same topology as
  Mim1 yet is present in the MIM complex in lower abundance (one to two copies per
  complex; Dimmer et al., 2012)."]

`GO:0140595 MIM complex` is definitionally about exactly this: "A protein complex located
in the mitochondrial outer membrane that functions as an insertase, mediating the insertion
of alpha-helical proteins from the cytosol into the outer membrane."

## 4. Biological role — insertase for α-helical outer-membrane proteins

The MIM complex is the outer-membrane insertase for α-helically anchored precursors. Client
classes established over ~15 years:

| Client class | Examples | Reference |
|---|---|---|
| Multi-span α-helical | Ugo1, Om14, Scm4 | [PMID:21825073], [PMID:21825074] |
| Signal-anchored (N-terminal anchor) | Tom20, Tom70 | [PMID:17974559], [PMID:18187149] |
| Tail-anchored (C-terminal anchor) | subset | [PMID:32348752] |
| β-barrel, indirectly (late TOM assembly) | Tom40 | [PMID:15326197], [PMID:15608614] |

- [PMID:22467864 "Some of the single-span proteins and all known\nmultiple-span proteins
  are inserted into the membrane in a pathway that depends\non the MOM protein
  Mitochondrial Import 1 (Mim1)."]
- [PMID:32348752 "the mitochondrial import (MIM) complex\ninserts precursors of
  multi-spanning α-helical proteins"] and "We report that the yeast MIM\ncomplex promotes
  the insertion of proteins with N-terminal (signal-anchored) or\nC-terminal
  (tail-anchored) membrane anchors."
- The 2020 study concludes "the MIM complex\nis a major and versatile protein translocase
  of the mitochondrial outer\nmembrane" [PMID:32348752].

MIM also cooperates with the TOM receptor Tom70 to accept precursors — [PMID:32348752 "MIM
interacts with TOM to accept precursor proteins from\nthe receptor Tom70."] — and
UniProt records a direct Mim1–Tom70 interaction from [PMID:21825073].

## 5. Role in TOM complex assembly

This is the phenotype through which Mim1 was discovered, and it is largely a *consequence*
of the insertase activity acting on Tom20/Tom70 plus a late, less well-defined step in
Tom40 maturation.

- Depletion abrogates TOM assembly: [PMID:15608614 "Depletion of Mim1 abrogates assembly of
  the TOM complex"]; the block is downstream of TOB/SAM-mediated Tom40 insertion — "The
  steps in the assembly of the TOM complex requiring Mim1 are located after the
  TOB-complex-dependent insertion of Tom40 into the outer membrane."
- Independently: [PMID:15326197 "Depletion of Tom13 or Tom38 affects assembly of Tom40 and
  porin in the mitochondrial outer membrane in vitro."]
- Receptor specificity: [PMID:17974559 "We report that Mim1 is required\nfor efficient
  membrane insertion and assembly of Tom20 and Tom70, but not Tom22."] — Tom22, being
  tail-anchored and requiring pre-existing Tom receptors, is Mim1-independent here.
- Mim1 physically joins SAM: [PMID:17974559 "We show that Mim1 associates with SAM(core)
  components to a large SAM complex,\nexplaining its role in late steps of the assembly
  pathway of Tom40."], echoed in 2020 as "coupling of MIM and SAM\npromotes early assembly
  steps of TOM subunits" [PMID:32348752].
- Disruption phenotype (UniProt, ECO:0000269|PubMed:17974559): "Leads to reduced levels of
  TOM complex but retains the respiratory chain."

Importantly, the specificity is real, not a generic import collapse: β-barrel machineries
other than TOM are unaffected — [PMID:15608614 "The biogenesis of other outer membrane
complexes containing β-barrel proteins, such as TOB/SAM and porin complexes, was not
affected by the lack of Mim1."], and depletion does not impair import of matrix or inner
membrane clients (mtHsp60, AAC) [PMID:15326197 "Depletion of Tom13 or Tom38 does not affect
import of mtHsp60 or AAC into mitochondria in vitro."].

## 6. The channel activity (basis of GO:0022832) — read carefully

[PMID:28916712] screened yeast outer-membrane proteins for channel activity and reported
Mim1 as one of four new channels. The relevant measurements, verbatim:

- "Upon reconstitution into planar lipid bilayers, Mim1 exhibited a characteristic channel
  activity that was inhibited by Mim1-specific antibodies"
- "We observed a main conductance state of ΔG¯main=580 pS that closed upon application of
  high positive or negative voltages"
- "The Mim1 channel was cation selective with a ratio of PK+/PCl− of 23.5:1 based on a
  positive reversal potential of 53 mV"
- Co-reconstitution with Mim2 reduced selectivity to PK+/PCl− = 11:1 — the channel is
  MIM-complex-relevant, not an artefact of Mim1 alone.

Assessment for curation:

1. **The observation is solid.** Recombinant protein, antibody-inhibited, reproduced with a
   second expression system ("Mim1 synthesized in wheat germ lysate exhibited the same
   channel activity"), modulated by its physiological partner Mim2. SGD's IDA is warranted.
2. **The GO term is imprecise in two ways.** `GO:0022832 voltage-gated channel activity` is
   an unspecified-substrate voltage-gated channel term. The measured behaviour is (a)
   strongly **cation**-selective (23.5:1) and (b) voltage-dependent only in the sense that
   the pore *closes* at high |Vm| — the classic gating description for a protein-conducting
   channel (Tom40, Sam50, Mdm10 all behave this way), not for a signalling voltage sensor.
   `GO:0022843 voltage-gated monoatomic cation channel activity` is the substrate-correct
   child if an ion-channel framing is kept.
3. **The biological reading is protein conduction, not ion conduction.** The authors' own
   framing is "The mitochondrial import component Mim1 forms a channel that is predicted to
   have an α-helical structure for protein import." No physiological ion flux through Mim1
   has been demonstrated; the cation preference is shared with every known protein-import
   channel of this membrane, whose *in vivo* cargo is polypeptide. Treating GO:0022832 as
   MIM1's molecular function would misstate what the protein does.

Downstream consequence: the `GO:0055085 transmembrane transport` IEA (GO_REF:0000108) is
generated *logically* from GO:0022832 via an MF→BP inter-ontology link (WITH/FROM field is
literally `GO:0022832`). It inherits whatever imprecision GO:0022832 carries, and adds
nothing — "transmembrane transport" is far too general to describe MIM1 and does not capture
protein insertion.

## 7. What is missing from GOA

**No molecular function term describes what Mim1 actually does.** The only MF annotations
are `GO:0005515 protein binding` (uninformative by project convention) and `GO:0022832`
(imprecise, see §6). `GO:0032977 membrane insertase activity` — "Binds transmembrane
domain-containing proteins and mediates their integration into a membrane" — is an exact
description of the MIM complex's activity and is supported by [PMID:32348752],
[PMID:21825073] and [PMID:22467864]. It should be proposed.

Because insertase activity is delivered by the Mim1–Mim2 heterocomplex rather than Mim1
alone, `contributes_to` is the appropriate qualifier at the gene-product level.

## 8. Orthology / PANTHER

PANTHER PTHR28241 "MITOCHONDRIAL IMPORT PROTEIN 1", 1248 proteins across 2583 taxa, one
subfamily (SF1). The IBA annotations (GO_REF:0000033) for `GO:0140595` and `GO:0045040`
derive from node `PANTHER:PTN002000670`, and MIM1's own SGD annotation
(`SGD:S000005386`) appears in the WITH/FROM — i.e. *S. cerevisiae* Mim1 is itself one of
the experimentally characterised descendants the PAINT curator used to place the IBD. That
is expected and is a marker of experimental grounding, not circularity. The family is
fungal/eukaryote-restricted; the functional counterpart in higher eukaryotes (MTCH1/2)
lacks sequence homology and is a case of convergent evolution, which is why the family is
narrow.

## 9. Summary of curation judgements

| Term | Evidence | Judgement |
|---|---|---|
| GO:0140595 MIM complex (IPI ×2, IBA) | PMID:22467864, GO_REF:0000033 | ACCEPT — core |
| GO:0045040 protein insertion into MOM (IDA, IMP, IBA) | PMID:32348752, PMID:15608614, GO_REF:0000033 | ACCEPT — core BP |
| GO:0070096 MOM translocase complex assembly (IMP ×2) | PMID:15608614, PMID:17974559 | ACCEPT — core BP |
| GO:0005741 mitochondrial outer membrane (IDA ×3, IEA) | PMID:15326197, PMID:15608614, PMID:28916712 | ACCEPT — core CC |
| GO:0005515 protein binding (IPI) | PMID:22467864 | MARK_AS_OVER_ANNOTATED — uninformative; the real content is MIM complex membership |
| GO:0022832 voltage-gated channel activity (IDA) | PMID:28916712 | MODIFY → GO:0022843 (substrate-correct); flag that protein conduction, not ion conduction, is the physiological role |
| GO:0055085 transmembrane transport (IEA) | GO_REF:0000108 from GO:0022832 | REMOVE — uninformative logical by-product; misrepresents an insertase as a solute transporter |
| **GO:0032977 membrane insertase activity** | not annotated | **PROPOSE** (contributes_to) |

---

## 10. Addendum — reviewer adjudication (annotation-reviewer pass)

The provisional table in §9 was independently re-checked against the cached full texts.
Two amendments, plus two corrections of detail.

**Amendment 1 — `GO:0022832` is MARK_AS_OVER_ANNOTATED, not MODIFY → `GO:0022843`.**
The substrate-correctness argument in §6.2 is right as far as it goes, but MODIFY to the
cation-specific child moves the annotation in the wrong direction overall. GO:0022843
*asserts* that MIM1's molecular function is to conduct monoatomic cations; GO:0022832 leaves
the substrate open. Since §6.3 concludes that the physiological permeant is polypeptide, the
vaguer parent is the less false of the two. There is also a mechanical consequence:
GO:0022832 already generates the spurious `GO:0055085` BP by inter-ontology inference
(GO_REF:0000108), and GO:0022843 would generate a *more specific* and more definitely wrong
cation-transport process in its place. KEEP_AS_NON_CORE was also considered and rejected —
it implies a genuine secondary activity, whereas the measured pore is the same conduit that
performs the insertase function, observed with an electrode.

**Amendment 2 — `GO:0032977` is entered as a `NEW` annotation, not only as a proposal.**
`contributes_to` is retained as the qualifier, per §7. In addition, a genuinely new ontology
term is proposed: **protein-conducting channel activity** (parent `GO:0015267 channel
activity`). No such term exists — checked against OLS — and its absence is exactly why the
electrophysiology of Tom40, Sam50, Mdm10 and Mim1 keeps being curated with ion-channel terms.

**Correction A — quotation error in §4.** The sentence quoted as
`"MIM interacts with TOM to accept precursor proteins from\nthe receptor Tom70."` is not a
verbatim substring of `publications/PMID_32348752.md`: the cached text has a non-breaking
space, `to\xa0accept`. Use
`"Free MIM complexes insert single-spanning proteins that are\nimported in a Tom70-independent manner."`
instead, which verifies.

**Correction B — topology is not fully settled.** [PMID:15326197], using a C-terminally
tagged allele, states "These results indicate that Tom13 and Tom38 are an integral membrane
protein and a peripheral membrane protein, respectively, of the mitochondrial outer membrane
and expose at least their COOH termini to the cytosol" — i.e. **C-terminus cytosolic**, the
opposite of the later consensus recorded in §2. The outer-membrane assignment is unaffected
(both papers agree), but the discrepancy is real and is now recorded as a suggested question.
Note also that the "residues 39–62" TM span in the header is UniProt `FT TRANSMEM 39..62`
with `ECO:0000255` — a sequence-analysis prediction, not experimental.

**Final actions (14 GOA-derived entries + 1 NEW).** ACCEPT ×11 (GO:0140595 IBA; GO:0045040
IBA; GO:0005741 IEA; GO:0005741 IDA ×3; GO:0045040 IMP; GO:0045040 IDA; GO:0140595 IPI;
GO:0070096 IMP ×2) · MARK_AS_OVER_ANNOTATED ×2 (GO:0005515 IPI; GO:0022832 IDA) ·
REMOVE ×1 (GO:0055085 IEA) · NEW ×1 (GO:0032977, contributes_to).

---

## 11. Addendum 2 — five UniProt-cited references folded in

`fetch-gene` seeds `references:` from the GOA only, so five papers that UniProt cites with
`ECO:0000269` on Q08176 were absent from the first pass. None is in the GOA, so none
supports an existing annotation, but two change what the review can say. All are now cached
and cited.

**PMID:18177669** (Popov-Čeleketić, Waizenegger & Rapaport 2008) — *the most valuable of
the five.* Two contributions:

1. **Settles the topology.** It states the arrangement directly — "The protein is composed
   of an N-terminal cytosolic domain, a\ncentral putative transmembrane segment (TMS) and a
   C-terminal domain facing the\nintermembrane space." This is the primary source that
   [PMID:28916712] was merely restating. Combined with [PMID:15608614]'s note that "a
   C-terminally tagged Mim1 had compromised function", it explains why the C-tagged
   construct in [PMID:15326197] reported a cytosolic C-terminus. **Correction B in §10 is
   therefore resolved, not open** — the suggested question has been removed and the
   resolution recorded in the PMID:15326197 `reference_review`.
2. **Supplies the oligomerisation mechanism.** "We show that Mim1 forms homo-oligomeric
   structures via\nits TMS, which contains two helix-dimerization GXXXG motifs. Mim1 with
   mutated\nGXXXG motifs did not form oligomeric structures and was inactive", and "Thus,
   the TMS of Mim1 is the minimal functional\ndomain of the protein." This is the
   explanation for the odd conservation pattern Waizenegger flagged in 2005 (conservation
   concentrated in the TM segment, unusual for a membrane protein) and it is now cited in
   `core_functions`.

**PMID:21825073** (Becker 2011) — full text available. Strengthens the proposed
`GO:0032977` from inference to direct observation: "The critical component for the
subsequent import into the outer membrane is Mim1, and the precursor proteins directly
interact with Mim1." GO:0032977 is defined as *binding* TM-domain-containing proteins *and*
mediating their integration; before this, only the integration half was evidenced and the
binding half was inferred from depletion phenotypes.

It also carries a **mechanistic correction to §5**: "a recent study showed that Mim1 does
not directly promote the biogenesis of Tom40 but functions via the import of small Tom
proteins that are needed for Tom40 assembly (Becker et al., 2010)". So the β-barrel row in
the §4 client table is indirect in a stronger sense than "late step" conveys — Mim1 never
handles Tom40 itself. This does not change the `GO:0070096` action (involvement in TOM
assembly is not in doubt) but is now recorded in that annotation's `reason`.

**PMID:21825074** (Papić 2011) — companion paper, independent group, same conclusion for
Ugo1. Its value is that the multispan substrate class rests on two laboratories, not one.

**PMID:18187149** (Hulett 2008) — third-laboratory corroboration of the Tom20 dependency,
via the Tom20 TM segment. Uses the Tom13 synonym.

**PMID:15242642** (Mnaimneh 2004) — the promoter-shutoff screen that gave MIM1 its name.
Historical provenance only; a genome-scale phenotypic inference, marked `relevance: LOW`.

**Organism caveat.** The abstracts of PMID:18177669 and PMID:18187149 do not name the
organism, and the cached records are abstract-only. The yeast attribution rests on UniProt's
`ECO:0000269` links to Q08176 and on [PMID:28916712] citing Popov-Čeleketić for yeast Mim1
topology — not on anything the abstracts state. This is recorded in both
`reference_review.review_notes` rather than being silently assumed. By contrast
PMID:21825073 ("in the model organism Saccharomyces cerevisiae") and PMID:21825074 ("using
yeast mitochondria") state it outright.

**Not done: the *N. crassa* orthologue.** Q8X0G8 (MIM1_NEUCR, NCU01101) carries three
annotations, none experimental: `GO:0140595` and `GO:0045040` are IBAs propagating from
`PTN002000670` with **`SGD:S000005386`** — yeast MIM1 — in the WITH/FROM, and `GO:0005741`
is an InterPro IEA. UniProt's FUNCTION line is `ECO:0000250` (by similarity). PubMed returns
one hit for Mim1 + Neurospora, and it is a Rapaport-lab study the field cites for *yeast*
Mim1. A review would therefore have no independent evidence to weigh; every judgement would
resolve to "correct, because yeast MIM1 is correct". The one real gain available is
upgrading `GO:0005741` from IEA to experimental on the strength of the *N. crassa* outer
membrane proteomics in [PMID:15608614], which identified NCU01101.1 in that fraction. Judged
not worth a review file on its own.

---

## 12. Addendum 3 — full texts of the two 2008 J Mol Biol papers

Publisher PDFs for [PMID:18177669] and [PMID:18187149] were supplied and extracted into
`publications/` (`full_text_extraction_method: pdf`). Both had been abstract-only. This
resolves one open caveat and adds several findings that the abstracts do not carry.

**Organism caveat closed.** §11 flagged that neither abstract names its organism, so the
yeast attribution rested on UniProt's `ECO:0000269` links. Both full texts state it
outright: [PMID:18177669 "The S. cerevisiae WT strain YPH499 was used."] and
[PMID:18187149 "The Δtom20 strain BY4743 was purchased from the Saccharomyces Genome
Deletion Consortium."] (also W303). The indirect attribution is no longer needed.

**`mim1Δ` is viable.** Both papers build and use null strains — PMID:18177669 replaced the
ORF with a HIS3 cassette. MIM1 has been carried as "essential" since the deletion-project
database and the promoter-shutoff screen [PMID:15242642], and [PMID:18187149] addresses this
directly: "Mim1 was first described as an essential gene required for mitochondrial import
by Mnaimneh et al. ... on the grounds that down regulation of MIM1 expression with a TetR
promoter caused a loss of growth on nonfermentable carbon sources". The null is sick, not
dead. Nothing in the review asserted essentiality, but it is worth having on record.

### PMID:18177669 — what the abstract omits

- **GXXXG motifs are mapped:** two consecutive GXXXG/A motifs at residues 57–61 and 63–67.
  The single G61L change is tolerated; the triple mutant (G61L + G63I + A67I, "Mim1-LII")
  "was not able to complement the function of native Mim1 under all conditions tested",
  forms no dimer, and yields no detectable Mim1 complex on BN-PAGE — while phenocopying
  `mim1Δ` for reduced Tom20 and the low-mass Tom40 species.
- **Oligomerisation is necessary, not merely correlated:** "Collectively, these results
  demonstrate that the ability of Mim1 to form oligomers is essential for the function of
  the protein in the biogenesis of the TOM complex."
- **Stoichiometry:** cross-linking plus dual-tag (7His / 3HA) co-isolation show the
  "Mim1-containing complex harbours at least two copies of Mim1."
- **Cross-species complementation** — directly relevant to the *N. crassa* question in §11.
  [PMID:18177669 "Mim1 from N. crassa could rescue the growth phenotype of Δmim1 cells only
  partially and upon its overexpression"], with expression verified by Western blot so the
  weak rescue is not a level artefact. By contrast, "cells harbouring S. pombe Mim1 did not
  present any growth phenotype under all tested conditions" — full complementation. The
  authors say plainly they cannot explain the difference. **This is the only direct
  functional evidence on the *N. crassa* protein, and it argues mildly against treating the
  IBA propagation to that orthologue as functional equivalence.** It reinforces rather than
  reverses the §11 decision not to curate NEUCR MIM1: the one experiment that exists says
  the orthologue behaves differently, which is a reason not to copy the yeast review across.
- **TMS boundary discrepancy:** the paper places the TMS at residues 34–79 (deletions were
  1–34 and 76–113); UniProt annotates `TRANSMEM 39..62` with `ECO:0000255` (prediction).
  Not consequential for any GO term, but the UniProt span is narrower than the functional
  segment this paper defines.

### PMID:18187149 — the more valuable of the two, on re-reading

- **Mim1 acts catalytically.** Using a cysteine-free Mim1(3S) allele that is fully
  functional, the authors show "Mim1 is not one of the prominent cross-linked partners of
  Tom20" — the cross-link fingerprint of docked Tom20 is unchanged. So Mim1 drives the
  assembly reaction and is released: "or else Mim1 catalyzes Tom20 assembly with known
  subunits of the TOM complex". **This is the cleanest experimental warrant for an
  insertase molecular function rather than a structural-subunit role**, and it is now cited
  on the proposed `GO:0032977` entry and in `core_functions`. It is also the experimental
  substance behind Waizenegger's 2005 speculation that Mim1 "seems to act catalytically".
- **Independent, earlier evidence that the Tom40 requirement is indirect.** §11 recorded
  this correction from Becker 2010 via [PMID:21825073]. This 2008 paper got there first by a
  different route: loss of Mim1 reduces the amount of Tom40 imported "but does not diminish
  the overall rate of Tom40 assembly", because "This is consistent with the known role of
  Tom20 as a receptor for Tom40 import:" — less functional Tom20 means less Tom40 arrives,
  though what arrives assembles normally through the 250K and 100K intermediates.
  **Two different indirect mechanisms are proposed** (via Tom20 as receptor here; via the
  small Tom proteins in Becker 2010), and both are indirect. Note this specific observation
  is **in tension with [PMID:15608614]**, which reported intermediate II reduced on Mim1
  depletion. The disagreement is about how much of the Tom40 defect is import versus
  assembly, not about whether Mim1 is required for TOM biogenesis, so no GO action changes.
- **Third value for the complex size:** ~300 kDa by BN-PAGE, against 400–450 kDa by gel
  filtration [PMID:15608614] and ~180 kDa by glycerol gradient. The paper also notes the
  Mim1 complex needs 0.3% digitonin to solubilise where TOM needs 0.1–0.2%, which is a
  plausible methodological source of the spread. The existing suggested question has been
  updated with all three values and this hint.
- **Specificity control:** "porin is assembled into the outer membrane of mitochondria
  without need of Mim1", confirming TOM and SAM are functional in these mitochondria.

### Cache provenance

The two cached records now carry `full_text_available: true` /
`full_text_extraction_method: pdf`, written in the same format the ETL produces. Text is the
publisher PDF's, not authored here; PDF extraction leaves minor artefacts (one residual
"homooligomer" where a hyphenated line break was rejoined, and some GXXXG occurrences render
as "G XXXG" in the source layout). Quotes used as `supporting_text` avoid those spans. All
114 `supporting_text` values in the review verify as verbatim substrings.

---

## 13. Addendum 4 — systematic literature sweep and final pass

Searched PubMed on `Mim1 AND mitochondri*` (32 hits), `Mim2 AND mitochondri*`, `Tom13 AND
mitochondri*`, `"MIM complex" AND (outer membrane)` and `YOL026C` (0 hits — the systematic
name is not indexed). Eight further papers were cached and cited, taking the reference list
from 14 to 22.

**Name collisions to be aware of.** Several PubMed hits for "MIM1" are not this gene:
**MIM1 the Mcl-1 BH3-mimetic small molecule** (PMID:40892149, PMID:31410885, PMID:30796196,
PMID:30134184) and the chicken c-Myb target gene **mim-1** (PMID:37752090). Anyone re-running
a naive `MIM1` search will hit these; none is relevant.

### The significant find — a second function (PMID:41748941, Nat Cell Biol 2026)

"Here we report that the MIM complex performs a second major function in\nlipid-droplet
homeostasis." The lipid metabolism enzyme **Ayr1** captures MIM and nucleates
**mitochondria–lipid droplet contact sites**; MIM and Ayr1 together set cellular lipid
droplet number. The mechanism is the elegant part: "Ayr1 binds to MIM via its single
hydrophobic segment in a\nsubstrate-mimicry mechanism but remains bound and is not released
into the outer\nmembrane." So this is a *captured insertase*, not a second catalytic
activity — and the two jobs are done by distinct populations, "MIM-Ayr1 for recruiting lipid
droplets and MIM-preprotein for protein insertion".

A pleasing loop closes here: **Ayr1 was the other new channel** identified alongside Mim1 in
the same 2017 bilayer screen [PMID:28916712]. The two proteins were already known to co-occur
in the outer-membrane fraction.

Curation consequences:
- New annotation proposed: `GO:0034389 lipid droplet organization` (IMP, involved_in),
  flagged provisional — one 2026 study, no replication, abstract-only in cache.
- **Ontology gap.** GO has `GO:0160259` (ER–lipid droplet contact site) and `GO:0170007`
  (ER–lipid droplet tether activity), and `GO:0044233` for ER–mitochondrion, but **nothing
  for mitochondrion–lipid droplet**. Two terms proposed, and the gap is recorded as a
  `knowledge_gaps` entry (ONTOLOGY / CC_DARK) on a second `core_functions` block.

### A genuine disagreement in the literature (PMID:19345216)

Lueder & Lithgow 2009, "The three domains of Mim1 have discrete functions", **contradicts**
PMID:18177669 on the soluble domains: it assigns the N-terminal domain a role regulating the
SAM-mediated early reaction of Tom40 assembly, where Popov-Čeleketić found ΔN and ΔC
variants phenotypically normal and concluded the TMS is the minimal functional domain. The
assays differ (in vitro multi-step assembly kinetics vs in vivo complementation), so a
quantitative contribution invisible to a growth assay would reconcile them. Marked
`correctness: DISPUTED` **for the domain-function claim only** — its topology report is not
disputed and in fact makes the cytosolic-N/IMS-C assignment two-laboratory. No GO action
turns on the disputed point. Recorded as a suggested question and experiment.

### Tom40 indirectness — primary source, and a second route

- **PMID:20026336** (Thornton/Becker 2010) is the actual "Becker et al., 2010" that
  [PMID:21825073] cites and that the review had been relying on second-hand. Mim1 inserts the
  small α-helical subunit **Tom6**, which SAM-Tom5/Tom40 then acts on. It also explains the
  Tom22 exception from [PMID:17974559]: Tom22 is handled by the parallel SAM-Mdm10 module.
- So there are now **two proposed indirect routes** to the Tom40 phenotype — via Tom20 as
  import receptor [PMID:18187149] and via the small Toms [PMID:20026336] — plus the unresolved
  disagreement about whether assembly rate is actually reduced. The suggested question has
  been rewritten to ask which contributes and in what proportion, rather than the now-answered
  "is it direct or indirect".

### Substrate scope is narrower than "the" insertase implies

- [PMID:31945731 "we\nfound that the MIM complex is required for the membrane insertion of
  some\nsingle-span proteins"] — others are MIM-independent. Also independently establishes
  tail-anchored proteins as MIM substrates.
- [PMID:35262629 "We\nfurther demonstrate that Mim1 and Porin support optimal membrane
  integration of\nOm14 but none of them are absolutely required."] — even a multi-span client
  is not absolutely MIM-dependent.
- Against this, [PMID:41748941] credits MIM with >90% of integral outer-membrane precursors.
  Both are now in the `description`: main translocase, but substrate-specific rather than
  obligatory.

### Orthology put on an experimental footing (PMID:29923829)

The convergent-evolution story previously rested on the `GO:7770059` term definition. Vitali
et al. 2018 demonstrate it: Mim1/Mim2 is "fungi-specific", and trypanosome **pATOM36** is a
functional analogue "even though these proteins show neither sequence nor topological
similarity", shown by **reciprocal** complementation. This explains why PTHR28241 is fungal
and why phylogenetic propagation of MIM function should stop at the fungal clade. The
`description` now says *restricted to* fungi rather than *highly conserved among* fungi.
[PMID:40782022] (the `GO:7770059` xref) adds MTCH1/MTCH2 as the mammalian solution.

### Also added

- **PMID:23959800** — Djp1 and Tom70 are needed for the biogenesis of *Mim1 itself*. Recorded
  mainly as a **confusability warning**: the Mim1–Tom70 relationship appears in this review in
  the opposite direction (Tom70 handing precursors *to* MIM), and the two are easy to conflate.

### Final-pass checks

- 146 `supporting_text` values verified verbatim against the cache (one wrap error caught and
  fixed during the sweep).
- No reference declared-but-uncited or cited-but-undeclared; every reference has both
  `findings` and `reference_review`; all `full_text_unavailable` flags agree with the cache.
- Two suggested questions that the new evidence had answered were rewritten rather than left
  standing (the Tom40 direct/indirect question, and the non-homologous-counterpart question).
- Final tallies: 16 annotations (ACCEPT ×11, MARK_AS_OVER_ANNOTATED ×2, REMOVE ×1, NEW ×2),
  22 references (HIGH 13 / MEDIUM 5 / LOW 4; VERIFIED 21 / DISPUTED 1), 2 core functions,
  3 proposed new terms, 2 knowledge gaps, 10 questions, 10 experiments.
- Schema, term-branch, GOA-consistency and compliance checks all pass; `status: COMPLETE`.
