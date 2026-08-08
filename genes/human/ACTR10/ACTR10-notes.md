# ACTR10 (Q9NZ32) — review notes

Human ACTR10 / ARP11 (also ACTR11, ARP10, hARP11), 417 aa, Swiss-Prot since 2003,
`PE 1: Evidence at protein level`. Reviewed as part of the PAINT + affinage campaign.

## 1. What the protein is

ACTR10 is the pointed-end capping subunit of **dynactin**, the ~1.2 MDa activator of
cytoplasmic dynein-1. UniProt states what that end does
[file:human/ACTR10/ACTR10-uniprot.txt "important for binding dynein-dynactin cargo adapters."]
and lists ACTR10 in the four-subunit pointed-end module
[file:human/ACTR10/ACTR10-uniprot.txt "subunits: ACTR10, DCNT4, DCTN5 and DCTN6."],
with location `Cytoplasm, cytoskeleton` and family assignment
[file:human/ACTR10/ACTR10-uniprot.txt "SIMILARITY: Belongs to the actin family."].
Both the FUNCTION and SUBUNIT lines are `ECO:0000250|UniProtKB:I3LHK5`, i.e.
by similarity to **pig** ACTR10 — the accession behind the pig dynactin cryo-EM series.

The protein was discovered as the fourth, previously unrecognised subunit of dynactin's
pointed-end complex, in bovine brain dynactin
[PMID:10525537 "The p62 and p27 subunits are associated with two previously undetected dynactin subunits, p25 and a novel actin-related protein, Arp11, in dynactin"].

## 2. The scientific crux: fold retained, one interface lost

ACTR10 is *actin-related* — Pfam PF00022 (Actin), CDD `cd10207 ASKHA_NBD_Arp10`,
PANTHER PTHR11937 (ACTIN). The campaign's most repeated defect is a fold or domain
NAME propagating into GO as an activity, and the mirror-image error is asserting
"fold without function" without checking residues. Both were tested
(`ACTR10-bioinformatics/RESULTS.md`, sections A–C). The answer is not one-sided:

**The nucleotide site is intact and occupied.** Eckley et al. predicted this from
sequence in 1999
[PMID:10525537 "a primordial core structure that contains nucleotide and metal binding elements"],
and the structures bear it out. A nucleotide is modelled in the Arp11 chain in
**19 of 24** deposited PDB entries that contain ACTR10, in the same maps where the
Arp1 and β-actin chains of the same filament carry ADP — the strongest single
statement being the methods line of the 3.37 Å pointed-end structure
[PMID:36071160 "Based on our density, ATP-Mg was built into Arp11 and ADP-Mg was built into"]
β-actin and the Arp1 subunits. Computing contacts from the 7Z8M coordinates gives
**18** Arp11 residues within 4 Å of that ATP, laid out canonically for the actin fold
(G21-E22-A23-F24…K26 ≡ actin G13-S14-G15-M16…K18; G142 ≡ actin G156; K211 ≡ actin
K213; G307-G308-T309 ≡ actin G301-G302-T303). **17/18 are identical in human ACTR10**,
and **0/17** of β-actin's own ADP contacts fall in an alignment gap. So the site has
not decayed.

**The polymerisation interface has gone.** Eckley et al.'s specific prediction was a
large deletion of actin residues 38–57, the subdomain-2 loop on the pointed-end face
[PMID:10525537 "The most conspicuous difference is a large deletion (actin residues 38–57) that eliminates an entire surface loop"],
against a conserved barbed-end face
[PMID:10525537 "The Arp11 barbed-end face is generally well conserved and is not predicted to contain large insertions that would prevent interactions with the pointed end of an Arp1 (or actin) filament."],
whence the conclusion
[PMID:10525537 "The predicted structure of Arp11 suggests it will not form filaments by itself and will only interact with filaments of Arp1, or conventional actin, at their pointed ends."].
In the alignment, **20/20** of actin positions 38–57 align to a gap in human ACTR10 —
the prediction is confirmed exactly, 26 years on. The cryo-EM structures give the
mechanism
[PMID:25814576 "The bottom protofilament directly binds Arp11 which prevents further subunit addition because its subdomain-2 loop is too short"]
and
[PMID:25814576 "Our structural data reveal how a single Arp11 subunit can cap both protofilaments."],
with Arp11 the only capping element at that end
[PMID:25814576 "Only Arp11 directly caps the pointed end"].
Biochemically Arp11 binds Arp1 directly
[PMID:12857853 "Recombinant Arp11 and Arp1 were demonstrated to interact by coprecipitation."],
and in cells has no free pool
[PMID:12857853 "Like Arp1, cytosolic Arp11 is found only in dynactin, suggesting that Arp11 and free cytosolic actin do not interact significantly."].
That second sentence must not be read as "Arp11 cannot bind actin" — the immediately preceding
clause reports the opposite result
[PMID:12857853 "We tested the ability of Arp11 to interact with conventional actin and found it could coassemble."],
so the statement is about the absence of a free Arp11 pool in cells, not about binding capacity.
The same paper raises an Arp2/3-like nucleation role as a hypothesis while arguing Arp1 needs no
nucleator
[PMID:12857853 "Arp1 has a vanishingly low critical concentration for polymerization (<1 nM) and assembles without a lag phase, suggesting nucleation is not required"],
which is why no nucleation or polymerisation term is annotated here: not demonstrated, rather
than excluded. See §14 — and note that the clause refuting the stronger claim was in the cached
abstract all along, two lines above the sentence I quoted.

Nucleotide binding is a defining property of the actin *fold*, not of actin alone
[PMID:42439233 "While actin is defined by its ability to form dynamic filaments, bind and hydrolyze ATP, and serve as a major cytoskeletal scaffold, Arps and actin-like proteins have evolved specialized roles in cytoplasmic and nuclear protein complexes."],
so retention of the site in a divergent member is not itself surprising — what is
notable is that no one has annotated it.

**Curation consequence.** GOA has *no* nucleotide-binding annotation for ACTR10 —
so the fold-derived over-annotation the campaign usually finds is absent here, and
what is present instead is the opposite defect: a real, structurally observed
nucleotide site with no annotation at all. Correspondingly, no polymerisation or
actin-nucleation term is annotated, which is right. The honest caveat is that the
nucleotide is modelled into cryo-EM density in *pig* Arp11; the two human dynactin
structures (9B7J, 9B85, 3.47–3.49 Å) model ADP on the Arp1 chains and AMP-PNP on
β-actin but leave chain J empty. A human annotation therefore belongs as **ISS from
I3LHK5**, not IDA, and no hydrolysis or exchange has ever been assayed.

## 3. Function: capping, complex integrity, cargo coupling

Three strands, of quite different strength.

*Structural (strongest).* Arp11 caps the pointed end and is the platform on which the
rest of the pointed-end module assembles
[PMID:25814576 "Arp11 binds p25, p27 and p62 to form the pointed end complex"],
[PMID:33734450 "The p62 saddle wraps around the Arp11 subunit at the end of dynactin"].
Arp11 is recruited by a composite site made by the terminal Arp1 and β-actin subunits
[PMID:25814576 "The unique interface formed by Arp1-I and β-actin-H specifically recruits Arp11."],
and is the most divergent family member
[PMID:25814576 "the most evolutionarily distant of all the actin related proteins"].

*Complex integrity (functional, monkey Cos7 RNAi).* Yeh & Schroer showed Arp11 is
required for dynactin to exist at all
[PMID:22918948 "Arp11 and p62 were found to be essential for preservation of dynactin structure, whereas p150Glued, p27, and p25 were not."],
which is why Arp11 knockdown is used as a proxy for whole-dynactin loss
[PMID:22918948 "Cells lacking dynactin (Arp11 RNAi) showed a redistribution of EEA1 punctae from the cell center toward the periphery"];
cross-linking places Arp11 at the centre of the module
[PMID:22918948 "These results indicate Arp11 contacts both p62 and p25 directly"],
[PMID:22918948 "Together these approaches revealed that the pointed-end complex contains two distinct binding activities, comprising the subunit pairs p62/Arp11 and p27/p25."].

*Cargo coupling (zebrafish genetics).* A forward screen gave `actr10` mutants with a
cargo-selective retrograde defect
[PMID:28414272 "Analysis of cargo localization and movement in the actr10 mutant revealed clustering of mitochondria, but not other cargos analyzed, at microtubule plus ends due to failed retrograde mitochondrial movement."],
traced to the linkage step
[PMID:28414272 "Furthermore, we demonstrated that abnormal mitochondrial movement in actr10 mutants is due to failed attachment of mitochondria to the dynein-dynactin complex in the absence of Actr10."],
with a separation-of-function construct
[PMID:28414272 "Importantly, Actr10 engineered to lack the dynactin binding domain maintains mitochondrial interaction, hinting at a specific role for Actr10 in mediating dynactin-mitochondria interaction."].
Consequence for organelle homeostasis
[PMID:33376159 "In contrast, inhibition of retrograde mitochondrial movement in the actr10nl15 mutant line leads to a significant reduction of mitochondrial load in the soma and an accumulation of this organelle in axon terminals"].
A second `actr10` allele shows the generic dynactin phenotypes too
[PMID:29073112 "This mutation in actr10, which encodes the Arp11 protein, results in dynein/dynactin loss-of-function phenotypes, such as photoreceptor loss and aberrant melanosome distribution in pigment cells."],
so the cargo-selectivity of the `nl15` allele should not be over-read as ACTR10 being
a mitochondria-only subunit.

Note the tension worth flagging to experts: Yeh & Schroer report Arp11 loss destroys
dynactin, whereas the zebrafish mutant has a *cargo-selective* defect. Either the
zebrafish allele is hypomorphic for the structural role, or vertebrate dynactin
tolerates partial Arp11 loss better than Cos7 dynactin.

## 4. Human-specific evidence, and a missing IDA

Human dynactin was purified and solved for the first time in 2025 using a *Chlamydia*
effector as an affinity handle
[PMID:40186871 "By exploiting Dre1 as an affinity reagent, we purified dynactin from human cell culture and solved the first cryo-EM structure of human dynactin."],
after AP-MS from HEK293T recovered
[PMID:40186871 "all 11 subunits of the host dynactin complex"].
Human ACTR10 (Q9NZ32) is chain J of the deposited models 9B7J and 9B85. GOA still
carries `GO:0005869 dynactin complex` for human ACTR10 only as **IBA**; the annotation
is correct but under-evidenced, and an **IDA** from PMID:40186871 is now available.
Mouse Actr10 already has the IDA (from PMID:10525537), so human lags its own ortholog.

## 5. PAINT source resolution — the decisive check

Full table in `ACTR10-bioinformatics/RESULTS.md` section A. Summary of what each IBA
row was propagated from.

| term | sources | verdict |
|---|---|---|
| GO:0005869 dynactin complex | mouse Actr10 (Q9QZB7, IDA), pig ACTR10 (I3LHK5), *C. elegans* arp-11 (Q9GYR2, TrEMBL, IDA) | true orthologs → sound |
| GO:0098958 retrograde axonal transport of mitochondrion | zebrafish actr10 (Q7ZVU0, TrEMBL, **IMP**) | true ortholog, real loss-of-function experiment → sound |
| GO:0005200 structural constituent of cytoskeleton | 10 protein sources, 10/10 Swiss-Prot with own experimental evidence: mouse/rat ACTG1, yeast ACT1, 2 *Dictyostelium* actins, human ACTR2 + ACTR3, yeast **ARP1** (centractin), yeast **ARP10** | mixed: mostly polymerising actins, but includes the dynactin filament subunit and the true *S. cerevisiae* Arp11 ortholog (Arp10) → defensible but coarse |
| GO:0005634 **nucleus** (`is_active_in`) | yeast **ARP9** (Q05123), *Candida* **ARP9** (Q5A9X7, TrEMBL), mouse **ACTL7A** (Q9QY84), *T. brucei* "Actin-like protein, putative" (Q57ZL0, TrEMBL) | **not one is an ARP11 ortholog** → wrong subfamily |

The nucleus row is the clean failure. Yeast Arp9 is a subunit of the SWI/SNF
(GO:0016514, IDA) and RSC (GO:0016586, IDA) chromatin remodellers; mouse Actl7a is a
testis actin-like protein with nucleus IDA/EXP. All four sources carry their own
experimental evidence for nucleus, so the **source annotations are sound and the
propagation is what fails** — `PROPAGATION_BAD` plus `WRONG_ORTHOLOG_OR_PARALOG`, not
`SOURCE_WEAK_OR_INFERRED`. Mechanically visible in the WITH/FROM itself: dynactin
membership was propagated at node `PTN000232945` and mitochondrial transport at
`PTN000232947` (both ARP11-specific), whereas nucleus came from `PTN008986520`, a
deeper node that groups ARP11 with the nuclear ARPs.

The subfamily boundary being crossed is not my own construction. The Arps pair up by
function — Arp1 with Arp11 in dynactin, Arp7 with Arp9 in the nuclear remodellers
[PMID:16291862 "consistent with the general pattern of paired Arps engaged in related functions (Arp2/Arp3 and Arp7/Arp9)"]
— and the current family review draws the same three-way split, with dynactin's Arps
cytoplasmic
[PMID:42439233 "whereas the dynactin complex, containing Arp1 and Arp11, functions as an activator and cargo-adaptor for dynein-dependent intracellular transport"],
a nuclear group
[PMID:42439233 "In the nucleus, multiple Arps, actin, and actin-like proteins are incorporated into large ATP-dependent chromatin-remodelling and histone-modifying complexes"],
and a testis group covering ACTL7A
[PMID:42439233 "many of which exhibit tissue-specific expression, particularly in the testis, and are associated with spermiogenesis and male fertility"].
Arp10p being the yeast ARP11 is likewise established, not assumed
[PMID:16291862 "Using both genetic and biochemical approaches, we demonstrate that Arp10p is the functional yeast homologue of Arp11, suggesting the possible existence of a pointed-end complex in yeast."],
[PMID:16291862 "Conversely, Arp10p stabilizes the dynactin complex by association with the Arp1p filament pointed end."],
which is why `SGD:S000002513` on the `GO:0005200` row counts as an ortholog transfer and
`SGD:S000004636` on the nucleus row does not.

Independent check (`RESULTS.md` section D): in Human Protein Atlas
immunofluorescence, 3/4 human nuclear ARPs (ACTL6A, ACTL6B, ACTR8) show a nuclear
compartment and 0/3 dynactin ARPs (ACTR10, ACTR1A, ACTR1B) do. ACTR10's HPA locations
are vesicles, plasma membrane, focal adhesion sites and several sperm structures —
including "Perinuclear theca", which contains the string "nuclear" but is a sperm-head
cytoplasmic structure, not the nucleus. (The analysis script matches HPA's controlled
vocabulary by exact name for precisely this reason; substring matching scored ACTR10
as nuclear on the first run and inverted the result.)

## 6. The IPI rows

Three `GO:0005515 protein binding` rows, resolved from WITH/FROM:

* **Q9UJW0 DCTN4/p62** (PMID:32296183, HuRI Y2H) — real and structurally validated:
  p62's saddle wraps around Arp11 [PMID:33734450], and cross-linking puts Arp11 in
  direct contact with p62 [PMID:22918948]. Deserves an informative term.
* **Q9UJ70 NAGK** (PMID:25416956, HI-II-14 Y2H) — N-acetyl-D-glucosamine kinase. Not
  replicated, no dynactin connection in the literature; UniProt records `NbExp=3`
  from IntAct alone.
* **Q15323 KRT31** (PMID:32296183, HuRI Y2H) — hair-cuticle keratin. A canonical
  sticky Y2H partner class, and a hair-shaft-restricted protein has no cell in common
  with cytoplasmic dynactin.

## 7. The Reactome granule annotations, and the harm they have already done

Four TAS rows put ACTR10 in `GO:0005576 extracellular region` (×2),
`GO:0035578 azurophil granule lumen` and `GO:1904813 ficolin-1-rich granule lumen`,
via Reactome's "Exocytosis of azurophil granule lumen proteins" (R-HSA-6798751) and
"Exocytosis of ficolin-rich granule lumen proteins" (R-HSA-6800434). Reactome's
Neutrophil degranulation pathway cites bulk granule proteomics — Rørvig et al.
[PMID:23650620] — as the source of these protein sets.

Reasons this is not credible for ACTR10:

1. Topology. ACTR10 has no signal peptide and no transmembrane segment (UniProt FT
   table lists only CHAIN, sequence CONFLICTs and secondary structure), and UniProt
   gives one location: `Cytoplasm, cytoskeleton`. A subunit buried in a 1.2 MDa
   cytosolic complex has no route to a secretory granule *lumen*.
2. Not a complex-level property — **computed**, not hand-checked, by
   `ACTR10-bioinformatics/subunit_granule_survey.py` (RESULTS.md §F), which resolves each
   reaction's pathway from Reactome rather than guessing it from the reaction id. The
   canonical roster is the 11 in UniProt's own SUBUNIT line: DCTN1/DCTN2/DCTN3 (shoulder),
   ACTR1A/ACTB (filament), CAPZA1/CAPZB (barbed end), ACTR10/DCTN4/DCTN5/DCTN6 (pointed
   end).

   - **1/11** carries any annotation from Reactome's Neutrophil degranulation route —
     **ACTR10 alone**.
   - **1/11** is annotated to azurophil granule lumen — **ACTR10 alone**.
   - 3/11 carry any of the three terms by *any* evidence code: ACTR10, plus two that do
     **not** share its route — **ACTB** only by `HDA` mass spectrometry (a different
     artefact class), and **CAPZA1** only from `R-HSA-879377`, an S100B/AGER binding
     reaction that is not under Neutrophil degranulation at all.
   - The one protein that genuinely shares the route is **ACTR1B**, the β-centractin
     paralog substituting for ACTR1A in a fraction of dynactin — a *twelfth* protein, not
     one of the 11, and like CAPZA1 one with a large non-dynactin pool.

   So the pattern is per-protein detection in granule fractions, not secretion of the
   complex: if dynactin were genuinely packaged into azurophil granules, all 11 would be
   there and exactly one is. (Earlier drafts of this paragraph said CAPZA1 shared the
   pattern and that ACTB carried nothing. Both were wrong; §11 records how the module
   found it.)
3. It has already misled a downstream paper. A 2024 HCC study describes ACTR10 as
   [PMID:39697424 "ACTR10 is predicted to involve in the retrograde axonal transport of mitochondria and is suggested to be present in the cytosol, extracellular region and secretory granules."]
   — reading the GO annotations back out as ACTR10 biology. That is the concrete cost
   of leaving them in place.

## 8. Actions taken

19 GOA rows, one review entry each, plus one proposed NEW row = 20 entries. (`fetch-gene`
seeds the two `GO:0005515` IPI rows that share PMID:32296183 as a single stub; they are
split back out here so the KRT31 and DCTN4 partners are judged separately, row-for-row
with GOA.)

- ACCEPT 8 — dynactin complex (IBA), structural constituent of cytoskeleton (IBA),
  retrograde axonal transport of mitochondrion (IBA), and 5 × cytosol (Reactome TAS)
- MODIFY 2 — `GO:0005856 cytoskeleton` → `GO:0005869` (strict ancestor, redundant);
  DCTN4 `protein binding` → `GO:0005200`
- KEEP_AS_NON_CORE 2 — cytoskeleton organization, axon cytoplasm (both GO_REF:0000108
  inferences taking their input from another propagated row on this same gene)
- MARK_AS_OVER_ANNOTATED 2 — NAGK and KRT31 `protein binding`
- REMOVE 5 — nucleus (IBA from nuclear ARPs); azurophil granule lumen;
  ficolin-1-rich granule lumen; 2 × extracellular region
- NEW 1 — `GO:0005524 ATP binding` (ISS from I3LHK5)

The five cytosol rows are all ACCEPT rather than a mix: the compartment is correct and
is where ACTR10 works, and validation requires one action per term. Each reason records
that the four later rows restate the same fact from further Reactome reactions rather
than adding evidence.

Ontology gap proposed: a new GO term for pointed-end capping of the dynactin Arp1
minifilament. The mismatch is one of scope. `GO:0051694 pointed-end actin filament
capping` is defined as *"The binding of a protein or protein complex to the pointed (or
minus) end of an actin filament, thus preventing the addition, exchange or removal of
further actin subunits"*, and `GO:0005884 actin filament` is *"A filamentous structure
formed of a two-stranded helical polymer of the protein actin and associated proteins"* —
whereas dynactin's backbone is, per `GO:0005869`'s own definition, *"an actin-like 40 nm
filament composed of actin-related protein"*. The subunits Arp11 blocks are Arp1, not
actin. `GO:0005870 actin capping protein of dynactin complex` is about the wrong end and the
wrong aspect regardless of status: it is a CC term for the CapZ heterodimer at the
*barbed* end. On status, QuickGO returns `isObsolete: true`, renders the label as
"obsolete actin capping protein of dynactin complex" and prefixes the definition
"OBSOLETE."; OLS adds `term_replaced_by: GO:0008290 F-actin capping protein complex`,
which is again barbed-end CapZ and again a CC. Separately, and recorded in the PR rather than in the GO-facing justification: the term is
still present in `cache/enums/gotermenum` and
`cache/enums/goproteincontainingcomplexenum`, so **enum-membership validation can admit a
term that is obsolete upstream**. Two inferences about *why* are withdrawn as unsupported —
see §11.

Two placements are offered in the proposal, since the choice is an editorial call about
`GO:0051693`'s intended scope: as its child if `actin filament capping` is meant to cover
filaments of any actin-family protein, or under `GO:0065003 protein-containing complex
assembly` if it is to stay strictly F-actin. (Checked all definitions against QuickGO
`/complete` rather than paraphrasing — an earlier draft of this justification attributed
the `GO:0005884` wording to `GO:0051694`, which was wrong.)

Two `core_functions` knowledge gaps are recorded on the cargo-coupling function: the
unidentified mitochondrial outer-membrane partner, and the complete absence of any
human-system assay of the coupling.

For `core_functions` the schema's subunit pattern applies literally:
`molecular_function: GO:0005200 structural constituent of cytoskeleton` (the
subunit-specific activity) and
`contributes_to_molecular_function: GO:0140660 cytoskeletal motor activator activity`
(dynactin's complex-level activity, which ACTR10 does not enable on its own), with
`in_complex: GO:0005869` — never `locations` — for complex membership.

## 9. Provenance / process

- affinage deep research ran with `self_evaluation_pairwise: win` and clear trust gates,
  3 numeric PMID citations, all
  three of which were fetched and read in full text. Its narrative is accurate on the
  zebrafish work; its "Affinage mechanism profile" grounding (`GO:0060090 molecular
  adaptor activity`, `GO:0005739 mitochondrion`) was not imported.
- `ACTR10-bioinformatics/` regenerates its own `RESULTS.md`; a second run was
  `diff`-identical to the committed file.

## 10. Round-2 review response (PR #2274)

Six items from `ai4c-agent`; none changed a GO term, evidence code or action.

> **Dated log — kept as written.** Item 1 below records the round-2 outcome, which round 3
> then falsified: `subunit_granule_survey.py` showed CAPZA1 does **not** share ACTR10's
> Reactome route, so the "two of the 11" figure stated there is superseded by the 1/11 in
> §7 item 2 and §11. Left unedited because it is the history of how the claim moved.

1. **Cross-subunit arithmetic, second pass.** The reviewer was right that ACTR1B is a
   *twelfth* protein, not one of the 11 canonical subunits, so "only three of the 11" was
   3-of-12. Reframed in four YAML sites and here: **two of the 11** (ACTR10, CAPZA1)
   carry a Reactome TAS granule/extracellular term, ACTR10 alone carries azurophil
   granule lumen, and ACTR1B was checked alongside as the β-centractin paralog. The
   roster is now stated explicitly from UniProt's own SUBUNIT line rather than left
   implicit, which is what allowed the count to drift twice.
2. **`GO:0005870` status re-verified.** It *is* obsolete — see §"Ontology gap" above for
   the QuickGO/OLS evidence and the `cache/enums` staleness that prompted the query. The
   justification no longer *rests* on obsoletion: the term is barbed-end CapZ and a
   cellular component, so it is the wrong end and the wrong aspect either way.
3. **BP-vs-MF framing.** Correct catch: the proposed term is a BP, so it could never
   replace the `GO:0005200` MF row. The reason now says so and explains why no
   `proposed_replacement_terms` is given.
4. **ATP vs an ADP-majority observation set.** Answered with data rather than prose — new
   `RESULTS.md` section E surveys nucleotide-binding annotation across a 12-member
   actin/Arp panel, and section A now tallies the ligand split. Results: the Arp11 chain
   carries **ADP in 14 entries and ATP in 5**; only **2/12** panel members carry any term
   under `GO:0000166`, and both use `GO:0005524` — human ACTA1 (TAS, together with
   `GO:0043531 ADP binding`) and yeast ACT1 (IDA). So the gap is family-wide (ACTB,
   ACTG1 and ACTR1A all carry nothing), `GO:0005524` is the term GO actually uses for
   this site, and `GO:0043531` or the parent `GO:0032559` are named as defensible
   alternatives. **Note the reviewer's premise was wrong in one detail:** ACTB does *not*
   carry `GO:0005524` (QuickGO returns zero annotations under `GO:0000166` for P60709).
   The precedents are ACTA1 and yeast ACT1.
5. **The `GO:0005856` MODIFY collapses into an existing row.** Stated in the reason: the
   gene already has `GO:0005869` as `part_of` by IBA, and the SubCell pipeline behind
   `GO_REF:0000044` cannot emit a complex term from `SL-0090`, so this is a
   drop-the-redundant-ancestor recommendation, not a new `located_in` annotation.
6. **HPA denominators no longer shrink silently.** `nuclear_arp_control.py` now prints
   which genes were excluded and why (ACTR5 and ACTB, both "HPA record present but no
   location reported") plus the clade sizes before exclusion, so "3/4" and "0/3" cannot
   be read as a census of the panel.

Reproducibility re-checked after all three code changes: a fresh `uv run python
analyze.py` is `diff`-identical to the committed `RESULTS.md`.

## 11. Round-3 review response (PR #2274) — and two withdrawn inferences

`ai4c-reviewer` **APPROVED**, closing both round-2 🟡 items, and raised two optional 🔵
items. Both are done, because both turned out to matter more than "optional" suggested.

### 🔵 7 — the cross-subunit number now has a module, and it found two errors in my prose

The reviewer's point was procedural: the per-subunit Reactome check was the only
load-bearing number in the review with no module behind it, and it was the one number that
had drifted twice. `subunit_granule_survey.py` (RESULTS.md §F) computes it. Building it
immediately exposed two mistakes that hand-checking had missed:

1. **`O15507` is an *inactive* (deleted) UniProt entry.** I had used it as DCTN3. It returns
   no gene name and no annotations, so querying it is indistinguishable from a subunit that
   genuinely carries nothing — my "DCTN3 carries none" was vacuous. The real accession is
   **O75935** (`DCTN3_HUMAN`). ~~The module now prints the entry name for every accession
   so this cannot recur silently.~~ **Superseded — that fix does not work, see §12 🔵 3:**
   UniProt *follows the merge*, so printing the entry name displays `GFRA1_HUMAN`, a
   different protein's identity, and reads as a healthy answer. The working guard asserts
   `primaryAccession`. Do not copy the entry-name pattern into another gene's module.
   *A dead accession is the quietest possible false negative.*
2. **CAPZA1's extracellular TAS is not the granule route.** It comes from `R-HSA-879377`,
   "The TRTK-12 fragment of F-actin capping protein alpha binds the AGER ligand S100B",
   which is **not** under Neutrophil degranulation (`R-HSA-6798695`). Counting it beside
   ACTR10's, as my prose did, overstated how shared the pattern is.

With the route resolved from Reactome rather than guessed from the reaction id, the number
the four `REMOVE`s rest on is sharper than what I had claimed:

- canonical subunits on the Neutrophil degranulation route: **1/11 — ACTR10 alone**
- canonical subunits annotated to azurophil granule lumen: **1/11 — ACTR10 alone**
- carrying any of the three terms by *any* evidence code: 3/11 (ACTB by HDA mass
  spectrometry, CAPZA1 by the unrelated S100B reaction, ACTR10)
- outside the canonical 11: ACTR1B shares the route (`R-HSA-6798748`, `R-HSA-6800434`)

So the argument improved by being automated. Lesson for the campaign: *the claim worth
building a module for is the one that has already drifted.*

### 🔵 8 — the cache parenthetical is out of the GO-facing justification, and two inferences are withdrawn

Removed from `proposed_new_terms[].justification`, which is written for GO editors and where
repo housekeeping is noise. It lives in the PR body and here instead.

More importantly, the reviewer showed my *reasoning* was wrong, and checking it myself showed
a second inference was wrong too. Both withdrawn:

1. ~~The enums are stale because `GO:0005870` is absent from `cache/ontologies/go.tsv`.~~
   Does not follow. `go.tsv` is a lazily-populated label-fetch cache — `fetched_date` column,
   **7,717** rows against GO's ~40k — so absence means "never fetched", not "removed". Its
   `is_obsolete` column is unreliable in the same direction: **261** rows carry an
   `obsolete `-prefixed label but only **26** are flagged `True`.
2. ~~The enum generator's obsolete filter depends on `go.tsv` coverage, so a never-fetched
   term escapes it.~~ Also unsupported. The two caches have **independent producers**:
   `cache/enums/*.csv` are branch-reachability sets from the external
   `linkml-term-validator`/oaklib expansion (`gotermenum` is a flat 38,751-CURIE list),
   while `go.tsv` comes from this repo's own label fetches. There is no shared code path.

What *is* verified: `GO:0005870` is obsolete upstream (QuickGO `isObsolete: true`; OLS
`is_obsolete: true` with `term_replaced_by: GO:0008290`) yet present in two enum caches, so
enum-membership validation can admit an upstream-obsolete term. As a corroborating pattern
only — not a mechanism — all **261** `obsolete `-labelled `go.tsv` terms appear in **zero**
of the 7 enum files, which makes `GO:0005870` an anomaly rather than the rule. Actionable
item is a scheduled enum regeneration, not a per-PR fix.

Also noted from the reviewer, not acted on: ACTB appears under the HPA "excluded from those
denominators" line although as `conventional actin` it was never in either clade denominator
— the parenthetical clade label makes it readable, and the reviewer agreed it was not worth
a commit on its own.

## 12. Round-4 review response (PR #2274)

One 🟡 and four 🔵 from `ai4c-reviewer`. No GO term, evidence code, qualifier or action
changed.

### 🟡 The notes' standing argument still carried the claim round 3 falsified

Correct and the most important item of the round. Round 3 fixed the two YAML sites and added
§11, but left §7 item 2 — the *undated, standing* argument, which is where the next reader
looks — still saying CAPZA1 and ACTR1B share ACTR10's pattern, and still listing ACTB as
carrying nothing while the same paragraph's last sentence said it carries `GO:0005576` by
HDA. So one file contradicted itself in three places. Rewritten from the module's numbers
(1/11 on the route, 1/11 azurophil, 3/11 by any code) with the two non-sharers named and why.
The dated round-2 log in §10 is kept as written per the reviewer, but now carries a
*superseded* marker pointing forward, since a log stating a falsified outcome without a
pointer misleads exactly as effectively as a stale argument.

This is the failure the brief warns about in its own words — *a changed line is not a changed
claim*. Appending a correction note is not the same as propagating the correction. The
generalisable fix is what was done here: after any correction, **grep the whole gene folder
for the falsified claim**, not just the sites the reviewer cited.

### 🔵 3 — the dead-accession guard, and a worse trap than I described

Round 3's claim that "the module prints the entry name so a dead accession cannot recur
silently" was **wrong**, and testing the guard proved it. What `O15507` actually does:

- It is `entryType: Inactive`, `inactiveReason: {MERGED, mergeDemergeTo: [P56159]}` — merged
  into **GFRA1**, an unrelated protein.
- UniProt **follows the merge**, so the request returns `GFRA1_HUMAN`. Printing the entry
  name therefore displays a *different protein's identity* and reads as a healthy answer.
- `entryType` does not discriminate reliably: repeated identical requests for this accession
  returned `Inactive` on some and `UniProtKB reviewed (Swiss-Prot)` on others. A guard on
  that field passes or fails by luck. My first guard was written on `entryType` and did not
  fire.
- What holds in every observed response: the returned **`primaryAccession` is the merge
  target, never the accession requested**. That is the reliable check, and the guard now
  asserts it (verified: `O15507` rejected, `O75935` accepted).

This is the `size=1` lesson in a new guise — an identifier lookup converting a bad input into
a confident wrong answer — and worth a campaign line of its own: **a merged UniProt accession
silently substitutes another protein; check `primaryAccession`, never the name or the
entryType.** The same guard is now in `nucleotide_gap_survey.py` and
`nuclear_arp_control.py`, which also resolve hand-written panels. `paint_sources.py` gets a
*reported* flag instead of an abort, because its accessions come from the GOA WITH/FROM field
— there a redirect is informative data about a stale GOA reference, not a code defect.

### 🔵 4 — no silent truncation

`limit=100` with no check is the same class of defect as a denominator that silently shrinks.
All three QuickGO callers now compare `numberOfHits` against the returned page and abort
naming the URL. (Largest real count in this panel is 9, so nothing was truncated.)

### 🔵 2 — scope of the three-term screen, stated only as far as it is supported

The reviewer suggested documenting that the filter is complete because every degranulation
exocytosis reaction also emits `GO:0005576`. That is plausible but I could **not verify it** —
Reactome's `containedEvents` endpoint was returning HTTP 521 — so it is not asserted. The
docstring states what is supported (within this panel every route-derived set does include
`GO:0005576`) and names the limitation (a route reaction emitting a granule term *without*
`GO:0005576` would be missed).

The outage also exposed a design point worth recording: route classification is a hard
dependency on Reactome, and the module **aborts** rather than degrading to "route unknown".
Degrading would emit a different, weaker report that still looked complete — the ABRA failure
mode. So the committed `RESULTS.md` cannot be regenerated while Reactome is down, and that is
the intended trade. `RESULTS.md` is byte-identical to the round-3 commit, and the three
modules that do **not** depend on Reactome — `paint_sources.py`, `nuclear_arp_control.py` and
`nucleotide_gap_survey.py`; all five modules require network access, so "network-independent"
would be wrong — were each re-run and confirmed to emit only lines already present in it, so
this round's code changes are output-neutral.

### 🔵 5 — the ficolin row's "like CAPZA1" comparison

Fixed: it now says ACTR1B and CAPZA1 are alike in having large non-dynactin pools but only
ACTR1B is on this Reactome route.

## 13. Round-5 review response (PR #2274) — APPROVED

`ai4c-reviewer` **approved** on `f8fdcf970` and left three cosmetic suggestions, none
blocking. All three taken, because the first was the round-4 mistake about to repeat itself.

1. **§11 still carried the sentence §12 falsifies.** §11 said *"The module now prints the
   entry name for every accession so this cannot recur silently"* — the exact claim §12 opens
   by disproving. §10 got a superseded marker in round 4; §11 did not, and as the reviewer
   noted it is the more consequential of the two, because a reader could copy that guard
   pattern into another gene's module. Now struck through with the working alternative
   (`primaryAccession`) and an explicit "do not copy the entry-name pattern". *Correcting a
   claim in one section while leaving it standing in another is the same failure twice; the
   rule is to grep for the falsified sentence, not the falsified section.*
2. **`assert_not_truncated`'s `limit` parameter was dead** in both copies — the check reads
   `numberOfHits` against `len(results)` and never consulted it. Removed rather than wired
   up, since the caller's limit is already implicit in the comparison. Both copies re-tested:
   they pass a complete page and abort on a truncated one.
3. **"the three network-independent modules" was imprecise** — all five modules require
   network access; the three meant are those that do not depend on Reactome
   (`paint_sources.py`, `nuclear_arp_control.py`, `nucleotide_gap_survey.py`). Reworded,
   since that sentence is doing the provenance work for the byte-identical `RESULTS.md`
   claim.

**Reproducibility, resolved.** Reactome's ContentService was returning HTTP 521 throughout
rounds 4 and 5, so at the close of round 5 the byte-identical `RESULTS.md` claim rested only on
a partial re-run: the three non-Reactome modules emitted lines already present in the file, and
section F could not be regenerated at all. A retry loop was left cycling, and Reactome came back
(HTTP 200). On attempt 9 a **full end-to-end `uv run python analyze.py` produced a file
identical to the committed `RESULTS.md`** — so all five modules, section F included, are now
verified reproducible, and the partial-re-run caveat above is superseded. This is the
`diff`-reproducibility gate met properly rather than argued around.

## 14. I quoted one sentence and ignored the one before it

**The refuting clause was in the cached abstract the whole time.** My pre-merge,
abstract-only copy of `publications/PMID_12857853.md` contained *"found it could
coassemble"* on line 49 — two lines above the sentence I quoted from line 50. A merge
conflict later replaced that file with main's full-text copy and I re-read it, which is
*when* I noticed; but nothing was unavailable to me when I made the error. Attributing the
catch to the merge, as an earlier draft of this section did, gets the lesson backwards and
implies the mitigation is "fetch full text" — which CLAUDE.md warns is frequently
impossible. The actual mitigation is free and always available: **read the whole paragraph
around the sentence you are about to quote.**

Two claims were falsified, both in the same way.

**What went wrong.** The abstract reads: *"We tested the ability of Arp11 to interact with
conventional actin and found it could coassemble. Like Arp1, cytosolic Arp11 is found only
in dynactin, suggesting that Arp11 and free cytosolic actin do not interact
significantly."* I quoted the **second** sentence and built on it, and the **first** —
sitting immediately before it and reporting the opposite result — went unused. This is
the ACBD3 lesson verbatim: *quote to the end of the interpreting clause*, and note that
here the disconfirming clause came *before* the quoted one, which is the harder direction
to catch.

**The two corrections:**

1. `proposed_new_terms` claimed that annotating ACTR10 to `GO:0051694` "would assert the
   one thing the biochemistry excludes". **Wrong** — Arp11 *can* coassemble with
   conventional actin in vitro, and its conserved barbed-end face was predicted to let it
   interact with filament pointed ends generally. The surviving argument is narrower and
   cleaner: in dynactin the subunits Arp11 blocks are Arp1, not actin, so what GO lacks is
   a term for capping the **Arp1 minifilament** specifically — a question of grain, not a
   prohibition on relating Arp11 to actin.
2. The `GO:0005200` reason said Arp11 "binds Arp1 but not free actin, so no
   actin-polymerisation or actin-nucleation term should follow". **Overstated.** The same
   paper explicitly floats an Arp2/3-like nucleation role for Arp11. It was never
   demonstrated, and the authors argue Arp1 needs no nucleator (critical concentration
   <1 nM, no lag phase) — so the right ground for withholding those terms is *not
   demonstrated*, not *excluded*.

Both rows now cite **both halves** of the actin result rather than the half that suited
the argument, which is the structural fix: a one-sided quote set is the symptom.

**One more datum from the full text (🔵 4).** The paper maps a minimal actin-binding
fragment
[PMID:12857853 "We identified a minimal actin-binding fragment as amino acids 23–137, which corresponds roughly to subdomains 1 and 2 in conventional actin"],
i.e. subdomains 1–2 carry Arp11's actin-binding surface. This does **not** conflict with the
subdomain-2 loop being deleted: the missing element is actin's 38–57 surface loop, a
sub-feature within subdomain 2, not the subdomain itself, and its absence is what stops a
further subunit adding beyond Arp11 rather than what stops Arp11 binding. Recording it because
this round's lesson is precisely about noticing the adjacent fact — and because a reader who
found this line independently might otherwise read it as contradicting §2.

**Process note.** I noticed the error while re-reading the file after a merge conflict
replaced it. but the file's abstract had always
contained the refuting clause, so the merge changed only when I looked, not what was there.
Nothing in the review had flagged it — the quote was verbatim, the reference title matched, and
the quote checker passed, because none of those checks can see a *quotation that is true but
selectively bounded*. That is the gap worth remembering: every mechanical check in this repo
validates a quote against its source, and none validates it against its own neighbouring
sentence. The `reference_review` for PMID:12857853 now
records the full-text reading, and the stale `full_text_unavailable: true` flag is
removed. (It is retained on PMID:42439233 and PMID:23650620, which really are
abstract-only.)
