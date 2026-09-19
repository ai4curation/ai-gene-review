# APOF (Q13790) — research notes

Working notes for the GO annotation review of human apolipoprotein F. Journal
style, oldest reasoning first, with inline provenance. Quotes are verbatim from
the cached publications in `publications/`.

## 0. Identity check

`APOF-uniprot.txt` is `ID APOF_HUMAN Reviewed; 326 AA.` / `AC Q13790; Q8TC13;`,
`GN Name=APOF`, `OX NCBI_TaxID=9606`. This is the expected accession and the
expected protein — not a merged or redirected entry. HGNC:615, chromosome 12,
MANE-Select ENST00000398189.4. PANTHER family from the record's own `DR` line:
`PTHR15011; APOLIPOPROTEIN F` and subfamily `PTHR15011:SF3; APOLIPOPROTEIN F`.

UniProt names it `RecName: Full=Apolipoprotein F; Short=Apo-F;` with
`AltName: Full=Lipid transfer inhibitor protein; Short=LTIP;`. The two names are
the same protein, which matters enormously for literature retrieval: most of the
mechanistic work is published under LTIP and never says "apolipoprotein F" in the
title.

## 1. What the GOA record actually contains

14 rows. Counted from the seeded YAML, not asserted:

| aspect | rows |
|---|---|
| CC GO:0005576 extracellular region | 5 (EXP x2, IDA, IBA, IEA) |
| MF | 5 (GO:0005102 TAS, GO:0005319 TAS, GO:0015485 TAS, GO:0005515 IPI x2) |
| BP | 4 (GO:0006629 TAS, GO:0006869 TAS, GO:0008203 TAS, GO:0008203 IBA) |

Two IBAs (matching `DR PAN-GO; Q13790; 2 GO annotations based on evolutionary
models`), one IEA, two IPIs, three EXP/IDA, six TAS.

**The single most important observation about this record: not one row describes
the activity the protein is named for.** ApoF/LTIP is defined in the literature by
its inhibition of CETP-mediated lipid transfer, and the five MF rows are
"signaling receptor binding", "lipid carrier activity", "cholesterol binding" and
two bare "protein binding" rows. The BP rows are "lipid metabolic process",
"lipid transport" and "cholesterol metabolic process". Nothing regulatory,
nothing about CETP, nothing about LDL.

The six TAS rows are all legacy ProtInc annotations dated 2003-09-04, drawn from
two papers from 1982 and 1994 that predate the discovery of what the protein does
(1999). The record is, in effect, frozen at the pre-1999 understanding.

Reference projection check (scripted against QuickGO, counting distinct gene
products, full pagination):

| reference | annotations | distinct entities |
|---|---|---|
| PMID:6816269 | 4 | 1 |
| PMID:8093033 | 3 | 1 |
| PMID:204339 | 1 | 1 |
| PMID:28935895 | 1 | 1 |
| PMID:9880564 | **0** | **0** |
| PMID:28514442 (BioPlex 2.0) | 3,731 | 2,324 |
| PMID:33961781 (BioPlex 3.0) | 9,514 | 4,757 |

Two things fall out. The apoF-specific references are genuinely gene-specific,
not projections. And PMID:9880564 — the paper that identified LTIP as apoF and
demonstrated the CETP-inhibitory activity of recombinant human apoF — carries
**zero GO annotations anywhere in the GO corpus**. The defining functional paper
for this gene has never been used for an annotation, in any species.

## 2. The literature, in order

### 1978-1994: an acidic minor apolipoprotein of unknown function

ApoF was isolated from HDL [PMID:204339, title: "Isolation and partial
characterization of a new acidic apolipoprotein (apolipoprotein F) from high
density lipoproteins of human plasma."]. Note: this reference is abstract-less in
PubMed — the cached file has no abstract body at all, only the citation. The
title is all the text there is.

Koren et al. resolved three apoF-containing particles by sequential
immunosorption [PMID:6816269, "three different ApoF-containing lipoproteins were
isolated from normolipidemic fasting human plasma"] — LpF:A-I:A-II, LpF:A-I and
LpF — and determined their lipid composition by TLC. Their conclusion is
explicitly speculative and is about the *particles*, not the protein: [PMID:6816269,
"It is suggested that ApoF-containing lipoproteins may be involved in transport
and/or esterification of cholesterol."] This one sentence is the source of four
GOA rows (lipid carrier activity, lipid transport, cholesterol metabolic process,
cholesterol binding).

Day et al. cloned it [PMID:8093033, "Apolipoprotein F, with an apparent molecular
mass of 29 kilodaltons, was purified from human high density lipoproteins using a
modified two dimensional electrophoresis procedure."] and established the
precursor relationship [PMID:8093033, "The cDNA encodes apolipoprotein F, which is
composed of 162 amino acids, and predicts that apolipoprotein F is a proteolytic
product of a larger protein."] plus liver-restricted expression [PMID:8093033,
"Northern blot analysis indicates that apolipoprotein F mRNA is detected only in
liver for the tissues examined."]. Nothing in this paper concerns receptors —
which matters for the GO:0005102 row.

### 1989-1994: LTIP, under a different name

In parallel and without knowing it was the same protein, Nishide et al. purified
a lipid transfer inhibitor from an HDL subclass [PMID:2715721, "a potent lipid
transfer inhibitor protein (LTIP) that inhibited cholesteryl ester, triglyceride,
and phospholipid transfer mediated by the lipid transfer protein, LTP-I"] and
localised its activity [PMID:2715721, "Assay of ultracentrifugally obtained
lipoprotein fractions revealed that approximately 85% of the total functional LTIP
activity was in the d 1.063-1.21 g/ml HDL fraction."]. Apparent mass 29,000, pI
4.6 — the same protein Day et al. would clone five years later.

Morton and Greene then established the defining property, selectivity among
lipoprotein pairs [PMID:8071606, "Inhibition followed the order of very low
density lipoprotein (VLDL)-low density lipoprotein (LDL) transfers > LDL-high
density lipoprotein (HDL) transfers > VLDL-HDL transfers."], and the consequence
[PMID:8071606, "By preferentially diminishing transfer events involving LDL,
especially those between VLDL and LDL, LTIP enhances the ability of LTP to remove
CE from HDL, and thus alters HDL metabolism."].

### 1999: the two literatures merge

[PMID:9880564] is the pivotal paper. Purification exploited LDL association
["Purification of LTIP, in contrast to other published protocols, took advantage
of the tight association of this protein with LDL."]; N-terminal sequencing
matched the apoF cDNA; recombinant apoF from transfected COS-7 cells reproduced
the activity ["Conditioned media containing secreted apoF demonstrated CETP
inhibitor activity, whereas cells transfected with vector alone did not."]; and
the conclusion is flat ["We conclude that LTIP and apoF are identical."].

It also stated the selectivity ["Although LTIP inhibits CETP activity among
different lipoprotein classes, it preferentially suppresses transfer events
involving low density lipoprotein (LDL), whereas transfers involving high density
lipoprotein as donor are less affected."] and — importantly for the particle
question below — contradicted the earlier HDL assignment ["In contrast to that
previously reported, apoF was shown to be associated almost exclusively with LDL,
identical to the distribution of LTIP activity."].

This is the annotation-relevant paper that GO has never used.

### 1999-2011: the mechanism, and what it is not

The crucial mechanistic result is that apoF does **not** change what CETP does; it
changes which particles CETP acts on [PMID:10073979, "LTIP had no effect on the
selection of CE or TG by CETP or its mechanism of action."]; and the physiological
preference of CETP for HDL is an apoF artefact, not a CETP property
[PMID:10073979, "These data suggest that LTIP is responsible for the preferential
transfer of CE from HDL that occurs in plasma."].

Nor is apoF a pure inhibitor. Within HDL it is bidirectional [PMID:12907677, "In
contrast, VLDL to HDL3 transfer was stimulated, resulting in a CETP preference for
HDL3 that was 3-fold greater than that for LDL or HDL2."], and the authors'
summary is a retargeting one [PMID:12907677, "these results show that LTIP tailors
CETP-mediated remodeling of HDL3 and HDL2 particles in subclass-specific ways"].

The site of action is the lipoprotein surface, not CETP. The 2020 expert review
is explicit and also explicit about the limits of what is known [PMID:32520778,
"While much remains to be determined about the mechanism of LTIP's action, the
data suggest LTIP blocks CETP activity by disrupting and/or preventing the binding
of CETP to the lipoprotein surface (12, 13)."] and [PMID:32520778, "We hypothesize
that LTIP binds to the surface of lipoproteins and modifies this molecular
organization."]. Consistent with a surface-lipid mechanism, activity tracks LDL
surface chemistry: [PMID:12951364, "Thus, the negative charge of LDL surface
lipids, but not protein, is an important regulator of CETP and LTIP activity."]
with binding and activity decoupled [PMID:12951364, "LTIP binding to LDL was not
decreased by oleate."], and binding tracks LDL composition [PMID:21937674,
"Compositional changes that reduce the surface-to-core lipid ratio of LDL promote
LTIP binding and activation."].

**No study reports apoF binding CETP.** I searched for one (see §6) and found
none; the expert review describes the mechanism as substrate-directed and
unresolved. This is the single fact that decides which GO molecular function
terms are admissible (§4).

### 2008-2011: the active and inactive pools — and why the LDL/HDL literature conflicts

The apparent contradiction between "apoF is on HDL" (1978, 1982, 1989, 1994) and
"apoF is almost exclusively on LDL" (1999) is real and was resolved, not
adjudicated. Plasma contains two apoF pools [PMID:18369235, "Plasma fractionated
by gel filtration chromatography revealed two LTIP protein peaks, one coeluting
with LDL, and another of approximately 470 kDa."]. The large one is an HDL-density
particle [PMID:18369235, "The 470 kDa LTIP complex had a density of 1.134 g/ml,
indicating approximately 50% lipid content, and contained apolipoprotein A-I."]
and it is inactive [PMID:18369235, "Unlike LDL-associated LTIP, the 470 kDa LTIP
complex does not inhibit CETP activity."].

The review states the proportions [PMID:32520778, "In normolipidemic plasma, more
than 85% of ApoF is contained in the inactive complex (40)."] and the resolution
[PMID:32520778, "Most importantly, the ApoF associated with LDL is active in
regulating CETP, whereas ApoF in the 470kDa complex is inactive (38)."].
Independently, [PMID:19008531, "greater than 90% of the ApoF in human plasma was
found on HDL(3), with only a small amount on LDL."].

So **both** particle assignments are correct: most apoF protein is on HDL, and
essentially all apoF activity is on LDL. This is not a dispute to be resolved by
choosing a side; it is a two-state system, and any CC annotation that records only
one of the two misrepresents the biology.

VLDL is a different matter. Lagor et al. found none ["Apo F was not detected on
VLDL or HDL2."], and the review qualifies the later report
[PMID:32520778, "Although ApoF was not detected on VLDL in that study, a recent
lipoproteomic analysis showed that ApoF in VLDL is 5-fold lower that than
associated with LDL (39)."]. UniProt's FUNCTION line nonetheless says apoF "Also
associates to a lesser degree with VLDL, Apo-AI and Apo-AII", citing
PubMed:9880564, whose abstract does not mention VLDL. **Decision: no VLDL
particle term.** The direct evidence is one negative result and one secondary
report of a 5-fold-lower signal; that is not an annotation.

### In vivo: the direction of the effect depends on the diet

Mice lack CETP, so the informative in-vivo model is the hamster
[PMID:31511396, "ApoF knockdown in fat-fed male hamsters created a phenotype in
which endogenous CETP-mediated CE transfer from HDL to LDL increased up to 2-fold,
LDL cholesterol increased 40%, HDL declined 25%, LDL and HDL lipid compositions
were altered, and hepatic LDLR gene expression was decreased."]. This is the
in-vivo confirmation of the in-vitro inhibition, in the right direction.

But the reverse-cholesterol-transport effect inverts with diet
[PMID:31511396, "Notably, ApoF knockdown impaired HDL RCT in fat-fed hamsters but
increased sterol excretion in chow-fed animals."], restated in the review
[PMID:32520778, "Conversely, ApoF knockdown in chow-fed animals increased reverse
cholesterol transport."]. **Decision: no reverse-cholesterol-transport term.** A
process whose sign flips with diet cannot be annotated with a positive- or
negative-regulation term, and the unsigned parent would say nothing.

Mouse loss-of-function is mild [PMID:22363685, "deletion of ApoF had no
substantial impact on plasma lipid concentrations, HDL size, lipid or protein
composition."] with one lipid phenotype [PMID:22363685, "Female ApoF KO mice had
increased liver cholesteryl ester content relative to wild type controls on a chow
diet"]. That measurement is the seed of the GO:0008203 IBD (§3).

A caveat that must travel with any use of that mouse line: its non-lipid
phenotypes are confounded by a neighbouring gene [PMID:24529150, "These effects
were attributable to hypomorphic expression of Stat2 in the ApoF KO mice, a
critical gene in the Type I IFN pathway that is situated just 425 base pairs
downstream of ApoF."]. The authors invoke Stat2 for the interferon and macrophage
phenotypes, not for hepatic cholesteryl ester, so this does not void the GO:0008203
seed — but it does mean the line is not clean, and the 39% lesion reduction in
ApoF/Ldlr double knockouts should not be read as an apoF lipid effect.

Overexpression, in both species, lowers HDL [PMID:19008531, "Overexpression of
murine ApoF significantly reduced total cholesterol levels by 28% (P<0.001), HDL
by 27% (P<0.001), and phospholipid levels by 19% (P<0.001)."] — but this is
AAV-driven ectopic expression in a CETP-free animal, so it is IMP-grade at best
and cannot be transferred to human apoF as a native function.

Finally, the evolutionary point that frames the whole IBA question
[PMID:22363685, "This lack of a consistent requirement for plasma CE transfer
activity across species suggests that ApoF has been conserved throughout evolution
for a purpose distinct from CETP inhibition."]. ApoF is present in mice and rats,
which have no CETP at all. Whatever apoF does in those animals, it is not
inhibiting CETP.

## 3. The two IBAs

Family PAINT slice fetched with `just fetch-panther-paint PTHR15011` and committed
at `interpro/panther/PTHR15011/PTHR15011-paint.tsv`. The whole family carries one
node and two annotations:

```
PTHR15011  PTN002687490  GO:0005576  C  IBD  false  UniProtKB:Q13790  taxon:117571
PTHR15011  PTN002687490  GO:0008203  P  IBD  false  MGI:MGI:104539    taxon:117571
```

`taxon:117571` resolves via the UniProt taxonomy REST endpoint to **Euteleostomi**
(bony vertebrates). No IRD or IKR anywhere in the family (`negated` is false on
both rows and there are no other nodes). PTHR15011 is a single-family,
two-subfamily group of 642 proteins across 1,723 taxa; all three reviewed members
are ApoF orthologues in one subfamily, PTHR15011:SF3 (human Q13790, mouse Q91V80,
rat Q5M889 — from `PTHR15011-entries.csv`). There is no paralogue to confuse with,
which removes the most common IBA failure mode before it starts.

**GO:0005576 (extracellular region), WITH/FROM `PANTHER:PTN002687490|UniProtKB:Q13790`.**
The IBD seed is the target's own accession. Per the project rules this is expected
and correct, not circular: human APOF has direct experimental evidence of secretion
(three UniProt `ECO:0000269` citations behind `SUBCELLULAR LOCATION: Secreted`), and
that evidence is one of the descendant evidences the PAINT curator used to place
the node. The node then says something the direct annotation does not — that
secretion is an ancestral property of the family, inherited rather than
human-specific. The 35-residue signal peptide is present in the mouse and rat
orthologues too. Verdict: `NO_FAILURE_CORE`, both sources `SUPPORTS_TRANSFER`.

**GO:0008203 (cholesterol metabolic process), WITH/FROM `MGI:MGI:104539|PANTHER:PTN002687490`.**
One gene donor, so "the IBD seed" is a legitimate singular here. Resolved via the
UniProt cross-reference search (`xref:mgi-104539`, size=5): two hits, Swiss-Prot
**Q91V80 APOF_MOUSE** and TrEMBL A0A0R4J0M4 — the reviewed entry is mouse Apof, the
1:1 orthologue. QuickGO on Q91V80 shows the donor annotation is
`GO:0008203 | IMP | PMID:22363685 | acts_upstream_of_or_within | MGI:3800154`,
i.e. the ApoF knockout allele and the hepatic cholesteryl ester measurement quoted
above.

Two features of this transfer deserve recording rather than objection:

1. The seed phenotype is **CETP-independent** (mice have no CETP) and
   **sex-specific** (females only, chow diet). The human function is
   CETP-dependent. The two are different mechanisms.
2. GO:0008203 is broad enough to be true of both, and given a node spanning
   Euteleostomi — which includes the CETP-less rodents and the CETP-bearing fish
   and primates — a broad cholesterol-metabolism term is the correct
   least-common-denominator call, not an under-call. This is not
   `GRANULARITY_MISMATCH`: there is one gene donor, so donors cannot "agree", and
   no more specific term is true across the whole clade.

The human target also has independent, direct evidence for cholesterol metabolism
that does not depend on the mouse at all. Verdict: `NO_FAILURE_CORE`, no failure
modes; sources `SUPPORTS_TRANSFER` with the CETP-independence noted in the source
comments.

QuickGO also shows mouse Apof carries `GO:0003674 | ND | GO_REF:0000015` — the
molecular function of the mouse orthologue is formally recorded as *unknown*,
while the human orthologue's actual molecular function is undescribed by any of
its five MF rows. The family's molecular function is dark at both ends.

## 4. Which GO terms fit, judged on definitions

Definitions pulled from QuickGO `/ontology/go/terms/<id>/complete`, not from
labels.

**GO:0005102 signaling receptor binding** — "Binding to one or more specific sites
on a receptor molecule, a macromolecule that undergoes combination with a hormone,
neurotransmitter, drug or intracellular messenger to initiate a change in cell
function." No apoF-receptor interaction has ever been reported, and the cited
paper is a purification/cloning study. Even on the most charitable reading — that
ProtInc meant a lipoprotein receptor — that would be GO:0070325 lipoprotein
particle receptor binding, which is also unsupported. Wrong under either reading.

**GO:0005319 lipid carrier activity** — "Directly binding to a specific lipid and
delivering it either to an acceptor molecule or to a specific location." This is
the *parent* of GO:0120013 lipid transfer activity (confirmed via the QuickGO
ancestors endpoint: GO:0120013's ancestors include GO:0005319 and GO:0005215), and
GO:0120013 is the branch containing GO:0120020 cholesterol transfer activity —
which is CETP's own IDA-supported molecular function. So the GOA record assigns
apoF the parent class of the activity it exists to suppress. The polarity is
inverted, and the evidence for the row is a 1982 speculation about particle
composition.

**GO:0015485 cholesterol binding** — "Binding to cholesterol". No apoF-cholesterol
binding assay exists. The cited paper measured the lipid composition of
immunoaffinity-isolated particles by TLC. What has actually been measured is apoF
binding to the LDL particle, and the determinant is particle geometry, not
cholesterol content [PMID:35016907, "Only LDL particle size correlated with ApoF
binding capacity."]. The bioinformatics analysis adds a mechanistic reason to
doubt a lipid-binding site: apoF has 7.6% strongly amphipathic 18-mer windows
versus 21-49% for APOA1/APOA2/APOE/APOC3. Note that CETP *does* carry GO:0015485
by IDA from a direct assay — the term is in use correctly elsewhere in this
pathway, which is the contrast that makes the apoF row look like what it is.

**GO:0141110 transporter inhibitor activity** — "Binds to and stops, prevents, or
reduces the activity of a transporter." Its ancestor GO:0098772 molecular function
regulator activity is defined as regulating "the activity of its target via
non-covalent binding" — binding of the *target*. CETP's transfer activity is a
descendant of GO:0005215 transporter activity, so the transporter half fits. The
binding half does not: apoF binds the lipoprotein, not CETP. Rejected, and
recorded as an ontology gap (§5).

**GO:0004857 enzyme inhibitor activity** — "A molecular function regulator that
reduces a catalytic activity." CETP has no catalytic activity; its GO molecular
functions are transfer and binding terms. Rejected on the definition.

**GO:0030169 low-density lipoprotein particle binding** — "Binding to a
low-density lipoprotein particle..." This is the molecular activity that has
actually been measured, repeatedly, by several groups, in human plasma and with
recombinant human protein, and it is the activity the inhibition requires
[PMID:35016907, "This ApoF activity requires that it is bound to LDL."]. This is
the correct MF.

**GO:0032375 negative regulation of cholesterol transport** — "Any process that
stops, prevents, or reduces the frequency, rate or extent of the directed movement
of cholesterol..." CETP itself carries the mirror term GO:0032376 positive
regulation of cholesterol transport by IDA, which is the precedent that settles
this: apoF does to plasma cholesterol movement the opposite of what CETP does. The
parent GO:0032369 negative regulation of lipid transport is also true, since
inhibition extends to triglyceride and phospholipid transfer, but the cholesterol
child is the better-evidenced and more informative call.

**GO:0034362 low-density lipoprotein particle / GO:0034364 high-density
lipoprotein particle** — both supported, and both needed, for the two-pool reason
in §2.

## 5. Ontology gaps found

1. **No regulation terms for LDL or HDL particle remodeling.** GO has
   GO:0034372/0034373/0034374/0034375 for VLDL/IDL/LDL/HDL particle remodeling,
   and regulation children only for VLDL (GO:0010901, GO:0010902, GO:0010903).
   Verified by keyword search of the GO ontology endpoint. GO:0034374's own
   definition names "the transfer of cholesterol esters from LDL to a
   triglyceride-rich lipoprotein particle by cholesteryl ester transfer protein
   (CETP)" — exactly the reaction apoF inhibits — so the process apoF regulates is
   in GO, but the regulation of it is not, for the one particle class that matters
   here. ApoF is the paradigm gene for the missing term.

2. **No MF term for substrate-directed inhibition of a transfer reaction.** GO's
   molecular-function-regulator branch is built on the regulator binding its
   target. ApoF reduces CETP's activity without binding CETP, by occupying and
   altering the particle CETP must dock on. There is no term for this, and the
   existing inhibitor terms cannot be stretched to cover it without asserting a
   protein-protein interaction that has never been demonstrated.

## 6. What affinage missed, and what I searched

The affinage record (`APOF-deep-research-affinage.md`, `self_evaluation_pairwise:
win`, `faith_pct: 100.0`, 16 citations, trust gates clear per `.affinage.log`) is
accurate about this protein — no symbol collision, no non-numeric ids — and it is
strong on transcriptional regulation (FXR, LXR/PPARα, ETS-1/C-EBPα, SHP) and on
the in-vivo mouse/hamster work. Its mechanism_profile GO grounding
(GO:0098772, GO:0008289, GO:0140313 molecular sequestering activity) was not
imported; GO:0140313 in particular inverts the finding it presumably comes from —
apoF is the protein that *gets* sequestered into the inactive 470 kDa complex, not
a sequestering agent.

What it missed is the entire Morton mechanistic series. Of its 16 citations only
PMID:9880564 belongs to it. Found independently by PubMed E-utilities searches on
`apolipoprotein+F+CETP` (16 hits) and `LTIP+lipid+transfer+inhibitor+protein`
(18 hits) — the LTIP alias is the key, since these papers are titled for LTIP and
several never say "apolipoprotein F":

- PMID:2715721 (1989) original LTIP purification, 85% of activity in the HDL density range
- PMID:8071606 (1994) the selectivity order among lipoprotein pairs
- PMID:10073979 (1999) LTIP, not CETP, creates the HDL preference; LTIP does not change CETP's mechanism
- PMID:12907677 (2003) LTIP stimulates VLDL-to-HDL3 transfer — the sign is not uniform
- PMID:12951364 (2003) LDL surface lipid charge controls activity; binding and activity are separable
- PMID:18369235 (2008) the two pools, and that the HDL-associated pool is inactive
- PMID:21937674 (2011) LDL composition drives the active/inactive switch
- PMID:32520778 (2020) the expert review, full text, which states the mechanism and its limits

Without these the review would have had no basis for the MF analysis in §4, would
have had to pick a side in the LDL-vs-HDL conflict rather than recognising it as a
two-pool system, and would probably have annotated reverse cholesterol transport
in the wrong direction.

Europe PMC REST was returning HTTP 503, so all searching used NCBI E-utilities
(`esearch.fcgi` / `esummary.fcgi`), QuickGO REST for annotations and ontology, and
the UniProt REST API for taxonomy, cross-references and sequences.

## 7. Bioinformatics

Full write-up in `APOF-bioinformatics/RESULTS.md`; script `analyze_apof.py`
fetches all sequences live from UniProt. Headline results:

- CHAIN 165-326 is exactly 162 residues of a 326-residue precursor, matching both
  PMID:8093033 and PMID:19008531. The boundary is experimentally fixed, not
  predicted: mutating Arg-164 abolishes maturation [PMID:19008531].
- The unmodified mature chain computes to 17.42 kDa against an apparent 29-33 kDa,
  i.e. 66-89% of the observed mass is not polypeptide.
- The precursor is a charge dipole: propeptide 36-164 pI 9.51 / +3.70 at pH 7.4;
  mature chain 165-326 pI 4.40 / -10.78. This is why apoF was named an "acidic
  apolipoprotein" and matches the review's Figure 1 description.
- Three N-X-S/T sequons in the precursor: N118 and N139 in the propeptide, **N267
  alone in the mature chain**. Found only afterwards that this exact inventory was
  established experimentally by mutagenesis in PMID:19008531, which also shows
  N267 is glycosylated on the secreted mature protein. UniProt annotates only N118
  — a predicted site inside the propeptide that cannot be on the mature protein —
  and omits both experimentally supported sites.
- ApoF has 7.6% strongly amphipathic 18-mer windows versus 21.3-49.2% for
  APOA1/APOA2/APOE/APOC3, quantifying PMID:22363685's claim.
- Smith-Waterman: 60.5%/65.8% identity to mouse/rat ApoF (scores 917/866) versus
  scores of 28-41 over 32-67 columns against APOA1/APOA2/APOE/APOC3 — no homology
  to the classical apolipoproteins, consistent with its solitary PANTHER family
  and dedicated Pfam family PF15148.

## 8. Curation decisions

| row | term | evidence | action |
|---|---|---|---|
| 1 | GO:0005102 signaling receptor binding | TAS | REMOVE |
| 2 | GO:0005319 lipid carrier activity | TAS | MODIFY -> GO:0030169 |
| 3 | GO:0005515 protein binding (GALNT4) | IPI | MARK_AS_OVER_ANNOTATED |
| 4 | GO:0005515 protein binding (GALNT4) | IPI | MARK_AS_OVER_ANNOTATED |
| 5 | GO:0005576 extracellular region | EXP | ACCEPT |
| 6 | GO:0005576 extracellular region | EXP | ACCEPT |
| 7 | GO:0005576 extracellular region | IBA | ACCEPT |
| 8 | GO:0005576 extracellular region | IDA | ACCEPT |
| 9 | GO:0005576 extracellular region | IEA | ACCEPT |
| 10 | GO:0006629 lipid metabolic process | TAS | KEEP_AS_NON_CORE |
| 11 | GO:0006869 lipid transport | TAS | MODIFY -> GO:0032375 |
| 12 | GO:0008203 cholesterol metabolic process | IBA | ACCEPT |
| 13 | GO:0008203 cholesterol metabolic process | TAS | ACCEPT |
| 14 | GO:0015485 cholesterol binding | TAS | REMOVE |
| N1 | GO:0030169 low-density lipoprotein particle binding | IDA | NEW |
| N2 | GO:0034362 low-density lipoprotein particle | IDA | NEW |
| N3 | GO:0034364 high-density lipoprotein particle | IDA | NEW |

On the two IPI rows: the partner Q8N4A0 is GALNT4, polypeptide
N-acetylgalactosaminyltransferase 4 (EC 2.4.1.41), a Golgi membrane enzyme that
"Catalyzes the initial reaction in O-linked oligosaccharide biosynthesis". ApoF is
an O-GalNAc glycoprotein (UniProt CARBOHYD 274, experimental) that transits the
Golgi on its way out of the hepatocyte, and its secreted form is maturely
glycosylated [PMID:19008531, "Apo F in the media was PNGase F-sensitive but Endo
H-resistant, indicating that the secreted forms of Apo F are maturely
glycosylated"]. An AP-MS co-purification between a GalNAc-transferase and one of
its class of substrates is an enzyme-substrate encounter, and a substrate is not
the agent. Combined with the projection statistics in §1 (2,324 and 4,757 gene
products from the two BioPlex releases, one interaction reported twice — UniProt
records `NbExp=2` for this pair), these rows carry no functional information about
apoF. Not removed — the interaction is real and may well be the enzyme that puts
the Thr-274 glycan on — but marked as over-annotation.

Nothing is annotated for the precursor processing or the glycosylation, and
nothing should be: PCSK7 is the agent of the cleavage [PMID:25349778, "Our present
results show that PC7 and PC7-R504H exhibit similar processing of transferrin
receptor-1, proSortilin, and apolipoprotein-F."] and GALNT4 is a candidate agent
of the glycosylation. A PTM the protein carries is not an activity it has.

## 9. Validation

Scripted, not asserted. Counts from `.scratch/reconcile_apof.py`, which reconciles the
GOA tsv against the review 1:1 on (term, evidence, reference, normalized WITH/FROM):

- 14 GOA rows against 14 non-NEW YAML entries, plus 3 NEW entries; 0 failures.
- Actions: ACCEPT 7, KEEP_AS_NON_CORE 1, MARK_AS_OVER_ANNOTATED 2, MODIFY 2, NEW 3, REMOVE 2.
- `propagation_review` present on all three rows that carry `supporting_entities` and a
  propagated evidence code (GO:0005576 IBA, GO:0005576 IEA, GO:0008203 IBA). The two IPI
  rows carry `supporting_entities` too, but their WITH/FROM is the interaction partner,
  not a propagation source, so no `propagation_review` is written for them.
- 26 references, all 26 with a `reference_review`.
- `source_entities` are generated from the seeded `supporting_entities` by
  `.scratch/build_apof_sources.py`, which refuses to emit an entry for which the curator
  supplied no note and errors on any note that matches no row, so the id lists cannot
  drift from the GOA WITH/FROM column.

Checks run:

- `just validate human APOF` -> `✓ Valid (with 1 warnings)`.
- `checkquotes.py` -> `checked 67 quotes: 0 failures, 0 skipped`.
- duplicate-key loader -> `no duplicate keys`.
- `cache/go/terms.csv` -> one insertion (GO:0032375), no deletions, no duplicate ids.

The one warning is that no annotation cites the affinage deep-research file as
`supporting_text`. That is deliberate: the campaign brief forbids quoting affinage prose
as supporting text, and the validator's check is satisfied only by such a quote. Every
claim in this review is anchored to a primary PMID or to the local sequence analysis, and
the affinage record is assessed where it belongs, in `references[].reference_review`.

A second, non-blocking observation: the pre-write hook rejected the review when written
through the editing tool, reporting that `file:human/APOF/APOF-deep-research-affinage.md`
and `file:human/APOF/APOF-bioinformatics/RESULTS.md` do not exist. Both exist in this
worktree; the hook validates a temporary copy and resolves the project root elsewhere, so
this is the known sibling-worktree misresolution. The authoritative in-worktree validator
resolves both file references without complaint, and `checkquotes.py` reads both files and
matches their quotes.
