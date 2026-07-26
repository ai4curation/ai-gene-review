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
Biochemically, Arp11 binds Arp1 but not free actin
[PMID:12857853 "Recombinant Arp11 and Arp1 were demonstrated to interact by coprecipitation."],
[PMID:12857853 "suggesting that Arp11 and free cytosolic actin do not interact significantly."].

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
2. Not a complex-level property (checked per subunit via QuickGO). ACTR10 is the only
   one of the 11 dynactin subunits annotated to azurophil granule lumen at all, and only
   three (ACTR10, ACTR1B and CAPZA1) carry any Reactome TAS granule or extracellular
   term; DCTN1, DCTN2, DCTN3, DCTN4, DCTN5, DCTN6, ACTR1A, ACTB and CAPZB carry none.
   The two that share the pattern are precisely the subunits with large non-dynactin
   pools - CAPZA1 is a bona fide F-actin capping protein and ACTR1B a centractin paralog
   - so the pattern is per-protein detection in granule fractions, not secretion of the
   complex.
   If dynactin were genuinely packaged into azurophil granules, all subunits would be
   there. ACTB does carry `GO:0005576` but by **HDA**, i.e. mass spectrometry, not this
   Reactome route.
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
actin. `GO:0005870 actin capping protein of dynactin complex` is obsolete with no
replacement and was a CC term for the CapZ heterodimer at the *barbed* end.

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

- affinage deep research ran with `gates_passed: True`, 3 numeric PMID citations, all
  three of which were fetched and read in full text. Its narrative is accurate on the
  zebrafish work; its "Affinage mechanism profile" grounding (`GO:0060090 molecular
  adaptor activity`, `GO:0005739 mitochondrion`) was not imported.
- `ACTR10-bioinformatics/` regenerates its own `RESULTS.md`; a second run was
  `diff`-identical to the committed file.
