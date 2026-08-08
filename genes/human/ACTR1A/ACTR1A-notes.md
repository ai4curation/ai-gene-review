# ACTR1A (alpha-centractin / Arp1 / centractin) — review notes

UniProt: P61163 (ACTZ_HUMAN), 376 aa, `PE 1: Evidence at protein level`.
HGNC:167. Chromosome 10. Reviewed as part of the PAINT + affinage campaign.

## One-paragraph picture

ACTR1A is the actin-related protein that *is* the backbone of dynactin. Eight
copies of it, plus a single beta-actin, form a two-protofilament mini-filament
about 37 nm long, capped by CAPZA1/CAPZB at the barbed end and by ACTR10 (Arp11)
plus the p25/p27/p62 pointed-end module at the other. The shoulder (p150Glued,
p50/dynamitin, p24) coats three faces of the filament and sets its length; the
remaining face is the platform on which the cytoplasmic dynein-1 heavy-chain
tails and a coiled-coil cargo adaptor (BICD2, BICDR1, HOOK3, ...) dock. So Arp1's
molecular contribution is structural and interaction-surface, not catalytic and
not motile: it builds the ruler-length polymer whose translational symmetry
matches that of the dynein tail and whose length forces dynein into its active,
processive conformation.

## The fold-name question, settled with coordinates

The campaign's default suspicion — "actin-like protein, therefore the actin
annotations are wrong" — does **not** hold for Arp1. It does hold for its
pointed-end partner ACTR10. I checked this computationally rather than by
argument; the script and its output are in
`ACTR1A-bioinformatics/analyze_arp1_actin_fold.py` and
`ACTR1A-bioinformatics/RESULTS.md`.

Method: derive the nucleotide-contacting residues of beta-actin from a real
ATP-bound structure (PDB 2BTF chain A — **bovine** beta-actin, source organism
read from the mmCIF and 99.7% identical to human ACTB over the modelled region,
which is why the contacts are transferred *through* human ACTB rather than read
off directly; 4.5 A heavy-atom cutoff, 25 residues found from coordinates,
nothing hard-coded), map them onto ACTR1A/ACTR1B/ACTR10; then do the same inside the *human* dynactin cryo-EM
structure (PDB 9B85); then compute the inter-subunit interfaces of that
structure.

Results:

- ACTR1A retains **19 of 25** of beta-actin's nucleotide-contact residues
  (76%); ACTR1B 20/25; **ACTR10 only 10/25** (40%), and the ones it loses
  include actin's D157/G158 phosphate-binding pair, which becomes Y143/R144
  [file:human/ACTR1A/ACTR1A-bioinformatics/RESULTS.md "| ACTR10 | 28.0 | 25 | 10 | 40.0 |"].
- In the human dynactin structure, **all eight ACTR1A protomers have ADP
  modelled** (the single beta-actin subunit has AMPPNP instead)
  [file:human/ACTR1A/ACTR1A-bioinformatics/RESULTS.md "ACTR1A chains with a modelled nucleotide: **8/8**, ligand(s) ADP."].
  20 of the 22 nucleotide-contacting ACTR1A positions align onto residues that
  contact ATP in beta-actin, i.e. the nucleotide is in the conserved actin cleft.
- The ACTR1A-ACTR1A interfaces split cleanly by contact count into **six** large
  intra-protofilament contacts (>= 230 heavy-atom contacts: A-C, B-D, C-E, D-F,
  E-G, G-I) and a set of smaller lateral ones. All six large interfaces share
  ACTR1A residues **44-49, 51, 52, 65-68, 205, 213 and 243-246**
  [file:human/ACTR1A/ACTR1A-bioinformatics/RESULTS.md "splitting the ACTR1A-ACTR1A interfaces at the largest gap in their contact counts separates 6 large (>= 230 atom contacts, intra-protofilament) interfaces from the smaller lateral ones"].
  In beta-actin numbering the subdomain-2 members of that consensus are 40-45, 47,
  48 and 61-64 — actin's own DNase-I-binding loop, the canonical longitudinal
  polymerisation contact; the rest (beta-actin 200, 208, 242-245) are
  subdomain-3/4 contacts on the partner face. So Arp1 polymerises using actin's
  polymerisation surface, not a repurposed one — and this is a property of the
  whole filament, not of one hand-picked chain pair. The full per-pair residue
  lists are in RESULTS.md; nothing is omitted there.
- ACTR10 appears in a **single** copy and touches only the two chains at the
  pointed end; CAPZA1/CAPZB cap the other end. That is the structural
  difference between a subunit that builds a filament and subunits that stop one.

Independent literature support for the same two facts:

- Polymerisation: [PMID:7518465 "Antibodies to the actin-related protein Arp1
  (previously referred to as actin-RPV), bound at various sites along the
  filament, demonstrating that this protein assembles in a polymer similar to
  conventional actin."]; [PMID:10074429 "Arp1 was found to polymerize rapidly
  into short filaments that were similar, but not identical, in length to those
  in dynactin."]
- Nucleotide site: [PMID:25814576 "Both consist of four subdomains surrounding a
  nucleotide binding site (fig. S4)."] — said of Arp1 and actin together, in the
  same sentence as "the high (53%) sequence identity between".

**But the transfer is not unlimited.** The Arp1 polymer is not an actin
filament and does not behave like one:

- Fixed length, not dynamic: [PMID:25814576 "Together with CapZαβ binding to the
  barbed end this results in a highly stable complex of an exactly defined
  length."], and the free polymer is explicitly *different*: [PMID:25814576
  "What makes the filament in dynactin short and defined, when purified Arp1
  filaments vary in length (18)?"]
- Even free Arp1 never reaches F-actin lengths: [PMID:10074429 "With time, these
  filaments appeared to anneal to form longer assemblies but never attained the
  length of conventional actin filaments."]

Curation consequence: `GO:0051258 protein polymerization` transfers;
`GO:0030041 actin filament polymerization` does **not**, because the polymer is
an Arp1 mini-filament (eight Arp1 + one beta-actin) rather than an actin
filament, and the monomers added are Arp1, not actin. Terms about actin filament
*dynamics*, treadmilling, severing or depolymerisation should not be applied at
all. Note also that Bingham & Schroer's ATP statement is a *prediction*, not a
measurement: [PMID:10074429 "on the basis of conserved sequence features, is
predicted to bind ATP and possibly polymerize"] — the direct observation is the
ADP in 9B85, which is why I propose `GO:0043531 ADP binding` rather than
`GO:0005524 ATP binding`.

## The headline finding: ACTR1A has lost both of its good molecular functions

Current GOA for P61163 (43 rows, verified against
`https://www.ebi.ac.uk/QuickGO/services/annotation/search?geneProductId=UniProtKB:P61163`
returning `numberOfHits: 43`, matching `ACTR1A-goa.tsv`) contains exactly **two**
molecular-function rows:

1. `GO:0106006 cytoskeletal protein-membrane anchor activity` (IBA,
   contributes_to) — transferred from *S. pombe* arp1.
2. `GO:0005515 protein binding` (IPI, BCCIP) — uninformative by design.

Meanwhile the UniProt flat file fetched the same day still lists two GO
cross-references that GOA no longer has:

```
DR   GO; GO:0005524; F:ATP binding; IEA:UniProtKB-KW.
DR   GO; GO:0005200; F:structural constituent of cytoskeleton; IBA:GO_Central.
```

and `DR   PAN-GO; P61163; 2 GO annotations based on evolutionary models.`
QuickGO returns **0 hits** for both `GO:0005524` and `GO:0005200` on P61163.

Important caveat, and the obvious counter-argument to pre-empt: **that `DR   GO`
block diverges in both directions.** It also *omits* `GO:0030473`, `GO:0106006`,
`GO:0005515`, `GO:0005815` and `GO:0005856`, all of which GOA does have. So it is
a divergent snapshot, and "UniProt still lists it" would on its own be consistent
with nothing more than a stale cross-reference block. The load-bearing evidence
for the losses is therefore the QuickGO queries, not the DR lines: 0 human hits
for `GO_REF:0000043`, and 0 hits for `GO:0000166` with `goUsage=descendants` on
ACTB, ACTR1A, ACTR1B and ACTR10.

Two separate losses, with different causes:

- **`GO:0005524 ATP binding`** reached ACTR1A only through the UniProt-keyword
  pipeline `GO_REF:0000043`, which GOA has retired: a QuickGO query for
  `reference=GO_REF:0000043&taxonId=9606` now returns **0 hits** for the whole
  human proteome. The collateral damage is not ACTR1A-specific — **human ACTB
  (P60709) also now has no ATP-binding annotation**, although it retains
  `GO:0016887 ATP hydrolysis activity` (IDA) and `GO:0005200` (TAS,
  PMID:6202424). The loss is not confined to `GO:0005524` either: a QuickGO query
  for `GO:0000166` with `goUsage=descendants` returns **0 hits** for each of
  P60709 (ACTB), P61163 (ACTR1A), P42025 (ACTR1B) and Q9NZ32 (ACTR10), so no
  nucleotide-binding molecular function of any granularity survives anywhere in
  the human actin/Arp set — at a moment when human structures model the
  nucleotide in every Arp1 protomer.
- **`GO:0005200 structural constituent of cytoskeleton`** is the best available
  MF for a filament-forming structural subunit, is the exact analogue of
  "structural constituent of ribosome", is carried by ACTB itself, and is
  carried **by IDA** by *S. cerevisiae* ARP1/Act5p (P38696, PMID:9658168).
  ACTR1A does not have it. **ACTR10 does** — `GO:0005200` IBA with the
  `enables` qualifier — i.e. within one family PAINT has given the
  structural-constituent function to the subunit that *terminates* the filament
  and withheld it from the subunit present in eight copies that *forms* it. That
  inversion is the single most useful thing this review found.

The two IBA rows GOA does have are dated 20260416 (`GO:0106006`) and 20260528
(`GO:0030473`); the `GO:0005869` IBA is dated 20251218. So the family's PAINT
annotations were revised recently, and the revision appears to have swapped a
well-founded structural MF for a fission-yeast cortical-anchor MF.

## WITH/FROM resolution (every token, plus each source's own evidence)

Resolved with `rest.uniprot.org` (`size=2`+ where a token could be ambiguous) and
QuickGO `annotation/search?geneProductId=...&goId=...&goUsage=descendants`.

| token | resolves to | status | own evidence for the propagated term |
|---|---|---|---|
| `PANTHER:PTN000233666` | tree node, **not a protein** | not resolvable to a gene product | n/a |
| `PANTHER:PTN007551901` | tree node, **not a protein** | not resolvable to a gene product | n/a |
| `PomBase:SPBC1347.12` | O94630 `ARP1_SCHPO` "Centractin", **Swiss-Prot** | ortholog | `GO:0030989` IMP (PMID:25736293); `GO:0106006` **EXP** contributes_to (PMID:25736293); `GO:0005869` IPI (PMID:25736293) |
| `SGD:S000001171` | P38696 `ARP1_YEAST` "Centractin", **Swiss-Prot** | ortholog | `GO:0005869` IDA + IPI (PMID:9658168, PMID:18245366); also `GO:0005200` **IDA** |
| `UniProtKB:F2Z5G5` | `ACTZ_PIG` ACTR1A, **Swiss-Prot** | ortholog | `GO:0005869` IPI (PMID:33734450); `GO:0030989` IDA (PMID:36071160) — **see below, this one is bad** |
| `UniProtKB:Q5BBX7` | *Aspergillus nidulans* ANIA_01953 / FungiDB AN1953, **unreviewed (TrEMBL)**, submitted name "Uncharacterized protein" | ortholog by family (IPR004000 Actin, PANTHER PTHR11937), architecture actin-like | `GO:0030473` **IMP** acts_upstream_of_or_within (PMID:10467007) |
| `WB:WBGene00013168` | **two** TrEMBL accessions for the same gene, Q9NA98 and U4PR70, both `arp-1`, neither with a recommended name | ortholog, no reviewed entry | Q9NA98 `GO:0005869` **IDA** (PMID:20964796); U4PR70 has no annotations |

Notes on method, for the record:
- `WB:WBGene00013168` is exactly the `size=1` trap from the campaign brief: a
  single-hit query would have picked one of two TrEMBL entries and hidden the
  ambiguity. Both are unreviewed, so **neither entry's protein name may be cited
  as evidence of function**; only its curated GO evidence counts (Q9NA98 does
  carry its own IDA).
- `Q5BBX7` is likewise unreviewed. Its *name* ("Uncharacterized protein") says
  nothing; its *evidence* is a real IMP from a real nuclear-migration mutant
  screen, in which nudK was cloned and identified as Arp1: [PMID:10467007 "We
  have cloned one of the genes, nudK, and determined that it encodes the
  actin-related protein Arp1, which is a component of the dynactin complex. This
  provides the first evidence that dynactin is involved in nuclear migration in
  A. nidulans."]
- So for `GO:0005869`, 4 of the 5 resolvable sources carry their own
  experimental evidence. "The sources only carry the same family-level
  inference" would have been factually false here; `SOURCE_WEAK_OR_INFERRED` is
  not available as an excuse.

### A source annotation that is demonstrably wrong, and is spreading

`UniProtKB:F2Z5G5` (pig ACTR1A) carries `GO:0030989 dynein-driven meiotic
oscillatory nuclear movement` with evidence **IDA**, assigned by
**ComplexPortal**, citing **PMID:36071160** — which is Chaaban & Carter,
"Structure of dynein-dynactin on microtubules shows tandem adaptor binding", a
cryo-EM structure paper. A structure of dynein-dynactin on microtubules cannot
be a direct assay of a meiotic nuclear-oscillation process, and `GO:0030989`'s
definition is explicitly about an "astral microtubule array emanating from the
spindle pole body" — an organelle pigs do not have.

This is not a one-off row. The same PMID gives the same IDA to pig DCTN1,
DCTN2, DCTN4, DCTN5, CAPZA1 and CAPZB, i.e. the whole complex; and RGD has
since propagated it to rat Dctn3, Dctn5, Dctn6, Actr10 and Capza1 by **ISO**.
It looks like a complex-level process annotation applied to every member with
the wrong term picked. It matters here because F2Z5G5's *only* experimental
annotation anywhere under the `GO:0030473` branch is this bad row — so the human
`GO:0030473` IBA's only mammalian support is an artefact. Reported in
`suggested_questions`.

## `GO:0106006` — why MARK_AS_OVER_ANNOTATED and not REMOVE

Definition (QuickGO `/ontology/go/terms/GO:0106006/complete`, secondaryIds
`['GO:0140362']`): "The binding activity of a molecule that brings together a
cytoskeletal protein or protein complex and a plasma membrane lipid or
membrane-associated protein, in order to maintain the localization of the
cytoskeleton at a specific cortical membrane location."

Against transferring it to human ACTR1A:

1. Arp1's structurally defined contacts, computed from 9B85, are all
   intra-complex: other Arp1 protomers, beta-actin, ACTR10, CAPZA1/CAPZB, the
   p50 shoulder, and (from PMID:25814576) the dynein heavy-chain tail. None is
   a membrane or a membrane protein.
2. In human cells the cortical link is supplied by Galphai-LGN-NuMA and dynactin is
   the *anchored* partner, not the anchor: [PMID:22327364 "we found that LGN was
   required for the cortical localization of dynein-dynactin"]. The direction of
   dependency is the opposite of an anchor activity residing in dynactin.
3. The donor evidence is a single fission-yeast EXP annotation on arp1, where
   the cortical anchor is Num1/Mcp5 and dynactin *cooperates* with it:
   [PMID:25736293 "These subunits transiently colocalized with dynein foci at
   the cell cortex and were essential for the cortical anchoring of dynein."]

For REMOVE I would need to show the complex-level activity is false, and I
cannot: the `contributes_to` qualifier only asserts that *dynactin* has the
activity and ACTR1A is part of it, and in fission yeast dynactin genuinely is
required for cortical dynein anchoring. Untested in mammals + activity localised
to other subunits and to LGN/NuMA = over-annotation, not error. Hence
`MARK_AS_OVER_ANNOTATED`, `root_cause: PROPAGATION_BAD` (the pombe source is
sound; the term should not travel), `failure_modes: [ROLE_CONFLATION,
COMPARTMENT_OR_COMPLEX_MISMATCH]`.

## `GO:0030473` — KEEP_AS_NON_CORE

Definition: "The directed movement of the nucleus along microtubules within the
cell, mediated by motor proteins" (secondaryIds `['GO:0000065']`). Dynein-dynactin
does drive nuclear positioning in mammalian cells, and ACTR1A is an obligate
structural subunit, so involvement is likely true. But every piece of donor
evidence is fungal (A. nidulans germ-tube nuclear migration; S. pombe meiotic
horsetail oscillation), the one mammalian donor row is the bad ComplexPortal IDA
above, and nuclear migration is one cargo among many for dynactin. Non-core,
kept, with the donor problems recorded.

## Cell cortex, centrosome, cytosol

- `GO:0005938 cell cortex` IDA (PMID:22327364) is sound and specific: ACTR1A was
  imaged at the cortex and its distribution is *regulated* —
  [PMID:22327364 "In contrast, Arp1A accumulated asymmetrically at the cell
  cortex during metaphase such that it is preferentially localized to the cortex
  that is distal to the mitotic spindle"]. The construct was GFP-Arp1A; GO uses
  IDA for fusion-protein localisation (`GO_REF:0000054` is exactly that), so the
  code is appropriate. Accepted.
- `GO:0005813 centrosome` has both an IDA (PMID:21399614, centrosome proteomics
  with imaging validation) and a SubCell IEA; UniProt additionally cites
  PMID:14654843. Dynein-dynactin anchoring microtubules at the centrosome is
  long established. Accepted / non-core.
- `GO:0005829 cytosol` appears **27 times**, once per Reactome reaction. The
  term is right — dynactin is a soluble cytoplasmic complex — but these are 27
  compartment assignments emitted per reaction, not 27 observations, and several
  of the reactions (`C2CD3 binds the mother centriole`, `MARK4 binds ODF2 in the
  centriole`, `RAB3IP stimulates nucleotide exchange on RAB8A`) carry no
  ACTR1A-specific evidence at all; ACTR1A is present because Reactome lists the
  dynactin complex as a participant. Kept as non-core, each row reviewed
  individually.
- `GO:0005875 microtubule associated complex` TAS and `GO:0005869 dynactin
  complex` TAS come from the *same* reference (PMID:7696711), and `GO:0005869`
  **is_a** `GO:0005875` (QuickGO ancestors of GO:0005869 include GO:0005875,
  GO:0005856 and GO:0015629). Annotating a term and its ancestor from one
  evidence line is redundant, so the parent is MODIFY-ed to the child. The
  paper does support the general statement — it describes centractin as "an
  actin-related protein localized to microtubule-associated structures" — and
  although its title foregrounds beta-centractin, it explicitly discusses
  alpha-centractin, so this is not a paralog mis-attribution.
- `GO:0070062 extracellular exosome` (two HDA rows, urinary and prostatic-
  secretion exosome proteomes) is the standard cytoskeletal-contaminant pattern:
  ACTR1A is a cytosolic subunit of a 1 MDa motor cofactor with no secretion
  signal, and no functional study places it outside the cell. Marked as
  over-annotated rather than removed, since the peptides were genuinely detected.

## `GO:0005515 protein binding` / BCCIP

The IPI is real and isoform-resolved: [PMID:28394342 "BCCIPα, but not BCCIPβ or
GST itself, was sufficient to pull down the dynactin components, p150 glued and
Arp-1"], matching GOA's `with` value `UniProtKB:Q9P287-2` (BCCIP isoform
2/alpha). This is not screen noise. But p150Glued came down in the same
pull-down, i.e. what was captured was intact dynactin from mitotic lysate, so
the experiment does not localise a binding surface to ACTR1A and does not
license an ACTR1A-specific informative MF. Kept as a non-core partner record
with that caveat stated, rather than modified into a specific term the evidence
does not support.

## What the review proposes to add

- `GO:0005200 structural constituent of cytoskeleton` (enables, IDA,
  PMID:40186871) — restores the family-standard structural MF, now supported by
  a *human* structure rather than only by ortholog inference.
- `GO:0043531 ADP binding` (enables, IDA, PMID:40186871) — the nucleotide
  actually modelled, in the conserved actin cleft, in all eight protomers.
- `GO:0045504 dynein heavy chain binding` (contributes_to, ISS from pig
  F2Z5G5) — [PMID:25814576 "The dynein tail binds directly to the Arp1
  filament"], at sites that are inter-subunit clefts, hence `contributes_to`
  rather than `enables`: [PMID:25814576 "They bind adjacent clefts between
  Arp1-D & F (chain-1) and Arp1-F & β-actin-H (chain-2) (Fig. 5F,G)."]
- `GO:0051258 protein polymerization` (involved_in, IDA, PMID:40186871).
- MODIFY `GO:0016192 vesicle-mediated transport` to `GO:0047496 vesicle
  transport along microtubule`, which is what the cited paper actually reports:
  [PMID:1528266 "Actin-RPV is a major component of the dynactin complex, an
  activator of dynein-driven vesicle movement, indicating that unlike
  conventional actins which work in conjunction with myosin motors, actin-RPV
  may be involved in cytoplasmic movements via a microtubule-based system."]

And one genuinely missing term. GO has `GO:0005869 dynactin complex` (CC) and
`GO:0034452 dynactin binding` (MF) but **no dynactin assembly process** — a
QuickGO ontology search for "dynactin" returns only those two plus two obsolete
terms. Yet dynactin assembly is a well-studied, mechanistically distinctive
process with its own length-control logic: [PMID:25814576 "The shoulder and ERs
recruit eight Arp1s and stabilize their polymerization into a structure with 5
subunits on the top protofilament and three on the bottom."] GO already has the
sibling `GO:0070286 axonemal dynein complex assembly`, so `dynactin complex
assembly` under `GO:0065003` is a natural addition, and it is the only process
in which Arp1's polymerisation activity is deployed. Filed in
`proposed_new_terms`.

## Deliberately not annotated

- **TLR2 signalling.** [PMID:31221720 "RNA interference studies revealed an
  important role for ACTR1A in induction of pro-inflammatory cytokines."] One
  paper, cross-linking proteomics plus knockdown, no mechanism, and dynactin's
  general role in receptor trafficking could produce the phenotype indirectly.
  Raised as a question, not annotated.
- **SETD3 methylation.** [PMID:41142317 "In this study, we report the
  identification of α-centractin (ACTR1A) as a novel SETD3 substrate in vitro."]
  In vitro only, no in-cell site, and the authors themselves hedge. A PTM
  observation, not a function of ACTR1A.
- **Dre1.** The *Chlamydia* effector binds the **pointed end**, not the Arp1
  filament: [PMID:40186871 "these results suggest that Dre1 binds to the
  pointed-end complex of dynactin"]. Cited only for the human structure, not for
  an ACTR1A interaction.

## Distinction from ACTR1B (reviewed in parallel)

ACTR1A and ACTR1B (beta-centractin) are 91% identical and both are genuine
dynactin subunits, so it would be easy to mirror their annotations. They are
nonetheless distinguishable, and the discriminating experiment is the very paper
that GOA cites for two of ACTR1A's TAS rows:

- **Stoichiometry in the complex.** Isoform-specific antibodies plus 2D gels put
  the two isoforms in dynactin at [PMID:7696711 "The isoforms were found in a
  constant ratio of approximately 15:1 (alpha:beta) in the dynactin complex."]
  So ACTR1A is the filament subunit and ACTR1B a minor variant component.
- **Expression does not explain the ratio.** [PMID:7696711 "alpha-centractin and
  beta-centractin mRNAs are equally distributed in all populations of mRNA
  examined"] — so the 15:1 protein ratio inside dynactin reflects incorporation,
  not transcription. (Gamma-centractin, by contrast, is tissue-specific.)
- **Neither has a free pool.** [PMID:7696711 "Both isoforms were found
  predominantly in the cytosolic fraction as a part of a previously identified
  20S complex (referred to as the dynactin complex) with no evidence for a free
  pool of either isoform."] So neither should acquire annotations that presuppose
  an independent monomeric role.
- **Structure.** All eight filament positions in the human dynactin structure are
  assigned to ACTR1A; the deposition's entity sequence is 100% identical to
  P61163. That assignment is the depositors', not an independent 91%-identity
  discrimination, so it is evidence of what the model represents rather than
  proof that no ACTR1B is present in any particle.
- **Sequence.** In my analysis ACTR1B retains 20/25 of beta-actin's
  nucleotide-contact residues versus 19/25 for ACTR1A, i.e. the nucleotide site
  and polymerisation competence are equally well preserved — the difference
  between the paralogs is abundance in the complex, not fold integrity.

Consequence for curation: the structural, nucleotide-binding and dynein-binding
annotations proposed here apply to ACTR1A on human structural evidence, and
transferring them to ACTR1B would rest on paralogy plus the 1994 stoichiometry
paper, not on structure. Nothing here licenses a claim that ACTR1B is
functionally *different*; the open question — whether ACTR1B-containing dynactin
is a distinct population with distinct cargo — is filed in
`suggested_questions`.

## Distinction from ACTR10 (reviewed in parallel)

The two are not interchangeable and their annotations should not mirror each
other. ACTR1A: 8 copies, polymerises through actin's subdomain-2 loop, keeps
19/25 nucleotide-site residues, ADP-bound, provides the dynein-tail platform.
ACTR10/Arp11: 1 copy, keeps 10/25 nucleotide-site residues, no nucleotide
modelled in 9B85, contacts only the two terminal protofilament chains, and its
function is to *stop* elongation — [PMID:25814576 "Only Arp11 directly caps the
pointed end, suggesting that the other components have a different role such as
cargo attachment (28)."] Consequently `GO:0005200` belongs on ACTR1A at least as
much as on ACTR10, and any nucleotide-binding or polymerisation annotation
should go to ACTR1A and not to ACTR10.

## Process log

- `just fetch-gene human ACTR1A` -> 43 GOA rows, 3 PMIDs newly cached.
- affinage record: `self_evaluation_pairwise: win`, trust gates clear, 2 citations (both
  numeric PMIDs:
  31221720, 41142317), no bioRxiv-DOI-in-PMID-field entries. Its narrative is
  confined to TLR2 and SETD3 and says nothing about dynactin architecture, so
  the structural content of this review comes from UniProt, the primary
  structural literature and the computed analysis, not from the provider.
- 13 further PMIDs fetched with `ai-gene-review fetch-pmid`.
- Bioinformatics: `ACTR1A-bioinformatics/` (uv project; gemmi + biopython);
  `RESULTS.md` and `results.json` are regenerated by the script and must not be
  hand-edited.
- The review YAML was generated from `ACTR1A-goa.tsv` by a builder script that
  asserts (i) every GOA row has a hand-written review, (ii) no review is left
  unused, (iii) exactly 43 GOA rows and 27 cytosol rows are produced, (iv)
  `source_entities` counts match the GOA WITH/FROM field, and (v) every
  `supporting_text` is a verbatim whitespace-normalised substring of its source.
  106 quotes checked, 0 problems.
- `just validate human ACTR1A` -> `✓ Valid (with 1 warnings)`. The remaining
  warning ("No annotations reference available deep research files") is left
  standing deliberately: the affinage record's only two findings are a candidate
  TLR2 signalling role and an in-vitro SETD3 methylation event, both of which
  this review declines to annotate with reasons, so no annotation legitimately
  rests on it. Silencing the warning would mean citing provider text for a claim
  I am not making. The judgement is recorded in the reference's
  `reference_review` instead.
- `GO:0005829 cytosol` is deliberately absent from `core_functions.locations`.
  It is correct, but it arrives as 27 identical Reactome reaction-level rows all
  reviewed `KEEP_AS_NON_CORE`, and promoting it would have required marking all
  27 as core, contradicting the reason given on those rows. The functionally
  meaningful locations carried into `core_functions` are the centrosome and the
  mitotic cell cortex, both `ACCEPT`ed.
