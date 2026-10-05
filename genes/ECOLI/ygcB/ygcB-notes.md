# ygcB / cas3 (Escherichia coli K-12, P38036) — curation notes

Curation journal for the gene review. Every assertion carries inline provenance.
Deep research via the `deep-research` command was not possible in this environment
(no provider API keys configured), so this file is the research record.

## Identity and architecture

- UniProt `CAS3_ECOLI` (P38036), 888 aa, reviewed, `PE 1: Evidence at protein level`.
  Gene name `ygcB`, synonym `cas3`; locus b2761. Two EC numbers are asserted:
  `EC=3.1.-.-` (from PubMed:22521689) and `EC=5.6.2.-` (from PubMed:21699496), i.e.
  a nuclease *and* an ATP-dependent duplex-remodelling isomerase (helicase)
  [file:ECOLI/ygcB/ygcB-uniprot.txt].
- Domain layout from UniProt features: `HD Cas3-type` 20..231, `Helicase ATP-binding`
  301..504 (Walker A ATP binding 314..321, DEAH box 452..455), `Helicase C-terminal`
  556..735. Mg(2+) binding at residues 75 and 160 (in the HD domain)
  [file:ECOLI/ygcB/ygcB-uniprot.txt].
- The original description of the locus already called out this two-module architecture:
  the E. coli K-12 CRISPR/cas system "comprises eight cas genes: cas3 (predicted
  HD-nuclease fused to a DEAD-box helicase), five genes designated casABCDE, cas1
  (predicted integrase) (13), and the endoribonuclease gene cas2"
  [PMID:18703739 "cas3 (predicted HD-nuclease fused to a DEAD-box helicase)"].

This is the key fact for adjudicating the annotation set: the helicase half of Cas3 is a
superfamily-2 (DEAD/DEAH-box-like) helicase module, which is what the InterPro and
PANTHER pipelines see, while the demonstrated substrate chemistry is DNA and RNA:DNA
hybrid, not duplex RNA.

## Role in the pathway: dedicated to CRISPR interference

Cas3 is encoded inside the `cas` locus and has no known function outside CRISPR
interference. It is the destruction step of the type I-E system.

- Genetic requirement: a strain expressing only Cascade is not protected, whereas
  "strains that expressed Cascade and Cas3 were much less sensitive to phage infection"
  and the resistance was lost without Cascade, "proving that both Cascade and Cas3 are
  required in this process" [PMID:18703739 "strains that expressed Cascade and Cas3 were
  much less sensitive to phage infection"], [PMID:18703739 "proving that both Cascade and
  Cas3 are required in this process"].
- Cas3 acts downstream of crRNA-guided target recognition, not as part of it:
  "Assisted by the helicase Cas3, these mature CRISPR RNAs then serve as small guide RNAs
  that enable Cascade to interfere with virus proliferation."
  [PMID:18703739 "Assisted by the helicase Cas3, these mature CRISPR RNAs then serve as
  small guide RNAs that enable Cascade to interfere with virus proliferation."].
- Recruitment is via the Cascade large subunit after target licensing:
  [PMID:22521689 "After Cascade-mediated R loop formation, the Cse1 subunit recruits Cas3,
  which catalyzes nicking of target DNA through its HD-nuclease domain."].
- Point mutants in the HD domain lose immunity *in vivo*: H74A, D75A, K78A, K320N and
  D452N all give "Loss of CRISPR immunity to lambda DNA and of CRISPR-mediated plasmid
  curing" [file:ECOLI/ygcB/ygcB-uniprot.txt]. The helicase-motif mutant K320N "Nicks
  target plasmid DNA but does not degrade it", which separates the nicking step from the
  processive degradation step [file:ECOLI/ygcB/ygcB-uniprot.txt].
- A mutant protein defective in the conserved motif raises phage sensitivity in vivo
  [PMID:21699496 "Cells expressing the mutant Cas3 protein are more sensitive to plaque
  formation by the phage λvir"].

## The three demonstrated catalytic activities

1. **Single-stranded DNA endonuclease (nicking).** The HD domain nicks the target.
   [PMID:22521689 "After Cascade-mediated R loop formation, the Cse1 subunit recruits
   Cas3, which catalyzes nicking of target DNA through its HD-nuclease domain."]
   In the direct assay on a partially single-stranded substrate,
   [PMID:22521689 "reveals that Cas3 has endonuclease and 3′ to 5′ exonuclease activity
   on the single stranded region of the DNA substrate"]. Cleavage is confined to the
   single-stranded region, so `GO:0000014` (single-stranded DNA endonuclease activity) is
   exactly right and is not an over-call.

2. **3′→5′ exonuclease on single-stranded DNA.** Same assay, same quote. The direction and
   the processivity are restated in the discussion
   [PMID:22521689 "The exonucleolytic degradation of target DNA by Cas3 in the 3′ to 5′
   direction is in line with the reported activities of the helicase MjaCas3′ and the
   nuclease MjaCas3″"] and in the summary
   [PMID:22521689 "Altogether, these data demonstrate that during type I CRISPR-interference
   in E. coli target DNA recognition by Cascade is followed by Cas3-mediated DNA nicking
   and progressive ATP-dependent degradation of target DNA in the 3′ to 5′ direction."].
   GOA records the generic `GO:0008296` (3'-5'-DNA exonuclease activity); GO also has
   `GO:0008310` single-stranded DNA 3'-5' DNA exonuclease activity, which is a descendant
   of `GO:0008296` (QuickGO ancestor query: GO:0008310 ancestors include GO:0008296) and
   matches "on the single stranded region of the DNA substrate" precisely. This is the one
   substantive refinement I propose on the function set.

3. **ATP-dependent DNA/RNA (R-loop) helicase, plus ATP-independent annealing.**
   [PMID:21699496 "purified E. coli Cas3 catalyses ATP-independent annealing of RNA with
   DNA forming R-loops, hybrids of RNA base-paired into duplex DNA"] and
   [PMID:21699496 "ATP abolishes Cas3 R-loop formation and instead powers Cas3 helicase
   unwinding of the invading RNA strand of a model R-loop substrate"]. Magnesium is a
   cofactor of the annealing reaction
   [PMID:21699496 "R-loop formation by Cas3 requires magnesium as a co-factor and is
   inactivated by mutagenesis of a conserved amino acid motif"]. The two activities work
   together on the target:
   [PMID:22521689 "The target is then progressively unwound and cleaved by the joint
   ATP-dependent helicase activity and Mg(2+)-dependent HD-nuclease activity of Cas3,
   leading to complete target DNA degradation and invader neutralization."].

   The substrate of the unwinding reaction is an RNA strand base-paired into duplex DNA —
   an RNA:DNA hybrid. `GO:0033677` "DNA/RNA helicase activity" is defined as "Unwinding of
   a DNA/RNA duplex, i.e. a double helix in which a strand of DNA pairs with a
   complementary strand of RNA, driven by ATP hydrolysis" (QuickGO), which is this reaction
   verbatim.

## The `GO:0003724` RNA helicase activity IBA — the one annotation I argue against

GOA carries `GO:0003724` RNA helicase activity by IBA (GO_REF:0000033) from
`PANTHER:PTN002776767` with donors `UniProtKB:P0A9P6`, `UniProtKB:P96614`,
`UniProtKB:Q55804` and `AGI_LocusCode:AT1G12770`
[file:ECOLI/ygcB/ygcB-goa.tsv]. P38036's PANTHER assignment is
`PTHR47963:SF9 CRISPR-ASSOCIATED ENDONUCLEASE_HELICASE CAS3` inside family
`PTHR47963 DEAD-BOX ATP-DEPENDENT RNA HELICASE 47, MITOCHONDRIAL`
[file:ECOLI/ygcB/ygcB-uniprot.txt]. P0A9P6 is the E. coli DEAD-box RNA helicase DeaD/CsdA;
the plant and cyanobacterial donors are likewise DEAD-box RNA helicases.

So this is not a case where the IBD node placement can be defended on Cas3's own biology:
the ancestral function being propagated is duplex-RNA unwinding by a DEAD-box helicase,
and Cas3 is a Cas3-subfamily protein whose helicase module has been repurposed. The
divergence is documented rather than assumed — `GO:0003724` requires "Unwinding of an RNA
helix" (QuickGO), and neither primary paper reports Cas3 acting on an RNA duplex. What is
reported is unwinding of the *RNA strand of an RNA:DNA hybrid*
[PMID:21699496 "ATP abolishes Cas3 R-loop formation and instead powers Cas3 helicase
unwinding of the invading RNA strand of a model R-loop substrate"], which is `GO:0033677`,
a sibling of `GO:0003724` under `GO:0004386` and not a descendant of it (QuickGO ancestor
query on GO:0033677 returns GO:0004386, GO:0008094, GO:0008186, GO:0016853 — no
GO:0003724). The right call is therefore `MODIFY` to the term for the reaction that was
actually measured, and the root cause is the family-level lumping of the Cas3 helicase
module with DEAD-box RNA helicases, i.e. term scoping on the ancestral node rather than a
bad source annotation.

The sibling `GO:0003723` RNA binding IBA from the same node is a different matter: Cas3
demonstrably engages an RNA strand (it anneals RNA into duplex DNA and then unwinds it),
so the term is true. It is just uninformative relative to `GO:0097098`/`GO:0033677`, and is
a consequence of the hybrid-directed activities rather than an independent core function.

## The missing process term: `GO:0099048`

GOA gives Cas3 `GO:0051607` defense response to virus twice (IDA and IMP) with the weak
`acts_upstream_of_or_within` qualifier, and no CRISPR-specific process term. A QuickGO
annotation query on `GO:0099048` "CRISPR-cas system" returns 33 annotations, among them
**every other cas gene of the same E. coli K-12 type I-E system**, all `involved_in` and
all IDA: `Q46901` casA, `P76632` casB, `Q46899` casC, `Q46898` casD, `Q46897` casE,
`Q46896` ygbT/cas1, `P45956` ygbF/cas2, plus the Cascade complex itself
(`ComplexPortal:CPX-1005`). P38036 is absent.

Comparator check (per CLAUDE.md): the comparators here are the other subunits of the very
same system, annotated from the very same papers, standing in the *same* role —
participants in the three-stage CRISPR process. They all carry the term; Cas3 alone does
not. And Cas3 unambiguously performs work in the process rather than merely being required
for it: it is the enzyme that nicks, unwinds and degrades the target
[PMID:22521689 "The target is then progressively unwound and cleaved by the joint
ATP-dependent helicase activity and Mg(2+)-dependent HD-nuclease activity of Cas3, leading
to complete target DNA degradation and invader neutralization."]. `GO:0099048` is also not
redundant with `GO:0051607`: QuickGO ancestor queries show the two are independent
branches under `GO:0006952` (GO:0099048 sits under GO:0098542/GO:0099046; GO:0051607 under
GO:0009615), neither being an ancestor of the other. This is a genuine curation gap and the
single `NEW` I propose.

## Module cross-check: `modules/crispr_cas_adaptive_immunity.yaml`

The `cas3_target_degradation` annoton in the `cascade_cas3_variant` currently declares:

- `function` = `GO:0008296` 3'-5'-DNA exonuclease activity, with
- `evidence: [{source_id: GO:0008296, statement: "GOA records P38036 as enabling GO:0008296
  and the GO:0033677 DNA/RNA helicase activity that couples unwinding to degradation."}]`

Two problems, one minor and one substantive.

1. **The evidence item cites the GO term as evidence for itself.** `source_id: GO:0008296`
   restates the annotation rather than grounding it. The grounding exists and is a cached
   full-text paper: PMID:22521689, which contains the direct assay. An `EvidenceItem` with
   a literature `source_id` plus `supporting_text` is verbatim-checked by the module
   validator, so the quote above can be dropped in as-is.
2. **`GO:0008296` is one level too general, and it is the wrong one of Cas3's two nuclease
   activities to stand alone.** The measured exonuclease acts "on the single stranded
   region of the DNA substrate", so `GO:0008310` single-stranded DNA 3'-5' DNA exonuclease
   activity is the accurate id. More importantly, the committed destruction step the
   annoton's own `role_description` describes ("processively unwinds and degrades the
   target") is a *coupled* activity: the HD domain first nicks the displaced strand
   (`GO:0000014`, the step that commits the target and the one abolished by the
   immunity-null HD mutants H74A/D75A/K78A/D452N), and the helicase then feeds ssDNA to the
   nuclease (`GO:0033677`). The K320N helicase mutant separates them cleanly — it "Nicks
   target plasmid DNA but does not degrade it" [file:ECOLI/ygcB/ygcB-uniprot.txt].

   So the honest single-function choice for this annoton is `GO:0000014` (the licensing,
   committed, immunity-essential step), with `GO:0008310` and `GO:0033677` as the coupled
   activities noted in the description — rather than `GO:0008296` as the function with
   `GO:0033677` merely mentioned in an evidence sentence. If a single catalytic id must
   carry the degradation, `GO:0008310` should replace `GO:0008296`.

Nothing else about the annoton needs changing: the family grounding
(`InterPro:IPR006474 Helicase Cas3, CRISPR-associated, core`) contains both representative
members, and the `role_description` is accurate.

## Not annotated, deliberately

- Cas3 is a workhorse of type I genome-editing/"DNA-shredding" reagents. That is a
  laboratory use, not a function of the gene in its host, and is kept out of the review
  entirely per project scope discipline.
- `GO:0097098` DNA/RNA hybrid annealing activity is real and directly observed, but the
  authors themselves describe annealing and ATP-driven unwinding as "apparently
  antagonistic roles" in the abstract, and the in vivo role of the annealing reaction is
  unresolved (Cascade also forms R-loops). It is kept as a non-core activity rather than
  promoted into `core_functions`.
- No new ontology term is proposed. Unlike Cascade — which needs a crRNA-guided target
  recognition MF that GO lacks — every activity Cas3 has been shown to perform maps onto an
  existing GO term.
