# Activin receptor signaling cross-species audit

## 2026-10-25 — audit initiated

The original module has seven annotons but only the INHBA ligand is family-grounded; the remaining six use gene-product selectors, and none carries a molecular function. Its Metazoa envelope and broad PTHR11848/PTN anchor require reassessment. The existing Falcon report is retained unedited as a research lead; its references are being independently checked.

Comparative literature identified: PMID:27328872 (activin/inhibin mechanisms including Drosophila); PMID:28130362 (Drosophila TGF-beta family pathways); PMID:38124338 (2024 BMP/activin comparative component table); PMID:22651914 (receptor specificity/evolution); PMID:30540228 (mammalian activin A physiology); PMID:34520530 (activin-receptor ligand diversity); PMID:39595638 (recent activin/inhibin review). Source caches and decisive primary studies are being fetched through the repository pipeline. Initial concurrent fetches encountered HTTP429; follow-up source requests are serialized with delays.

The initial representative set is six human proteins (INHBA P08476, ACVR1B P36896, ACVR2A P27037, SMAD2 Q15796, SMAD3 P84022, SMAD4 Q13485) plus five Drosophila proteins (Actbeta O61643, babo A1Z7L8, put Q24468, Smox O96660, Med O62609). Exact UniProt identities and PANTHER subfamilies were read from current records. Member gene reviews are in progress; no module completion is claimed.

Important distinctions to preserve:

- INHBA participates in agonistic activin dimers and antagonistic inhibin A; the module must specify the mature activin ligand form rather than assign one behavior to every INHBA-containing complex.
- Type II activin receptors are shared with some BMP signaling. Type I receptor activation and R-Smad specificity, not receptor names alone, determine the branch.
- Fly Babo isoforms and ligand-specific pairing are not interchangeable. The canonical A1Z7L8 sequence is BaboB; gene-level activities may derive from other isoforms. Native Actbeta evidence must be distinguished from experiments using vertebrate activin.
- Full-length SMAD2 DNA binding cannot be categorically excluded: cached PMID:31582430 reports direct DNA binding by properly folded E3-containing protein. The SMAD2 review is examining this evidence.
- SMADs act as transcriptional effectors/cofactors, not receptor kinases. Broad phenotypic functions need source-specific assessment without assuming every response is a core pathway step.
- A PAINT node supporting a broad TGF-beta process is not automatically an ancestral activin-specific assertion. Inspect its actual placement before retaining that evolutionary claim.

Independent module PRs already open: PhnWX #5538 (checks passed on the rebased curation commit; required approval pending after automated reviewer failure) and ABA #5540 (draft, targeted checks passed; repository-wide validation running). This activin work is isolated in branch cmungall/aigr-activin-taxon-audit.

## 2026-10-25 — comparative boundary and molecular-step evidence audit

Read-only module-YAML assessment by Codex, followed by this requested notes append. PMID:19192293 and PMID:23020873 were requested serially through the supported publication pipeline with a four-second interval; both now have cached full text. The seven original background reviews were examined at their available level: PMID:27328872, PMID:38124338, PMID:34520530 and PMID:39595638 have full text; PMID:22651914 and PMID:30540228 are abstract-only. PMID:28130362 is abstract-only locally, but its published full PDF and indexed full-text sections were consulted online. No provider report was manufactured or edited.

### Taxon boundary: ancestral toolkit versus demonstrated native relay

Retain **Metazoa (NCBITaxon:33208) as a non-universal evolutionary envelope**, while explicitly distinguishing the native ligand-defined relay established in the reviewed bilaterian exemplars from homology-based expectations elsewhere. Neither the human/fly sample nor the absence of a retrieved nonbilaterian coupling experiment establishes an origin at Bilateria or absence outside Bilateria. Equally, membership in Metazoa must not imply that every animal retains every ligand/receptor pair or the same downstream developmental outputs. This is not an ancestral activin-activity assignment to any PAINT PTN.

PMID:19192293 is a primary comparative analysis of 33 genomes, not merely a human/fly review. It reconstructs an “ancestral eumetazoan repertoire of four Smads” and places the repertoire in placozoans and cnidarians as well as arthropods and lophotrochozoans. The full discussion distinguishes inferred ancestral duplications from direct biochemical experiments and documents lineage-specific diversification, especially the atypical nematode system. It establishes ancient Smad/receptor machinery, not a complete experimentally reconstituted native activin ligand-to-Smad relay in each lineage.

PMID:23020873 directly tests cnidarian NvSmad2/3 in **Xenopus** embryos/animal caps, together with fly and frog orthologs. Its experimental description explicitly uses “ligand-independent overexpression of either Xenopus or Nematostella Smad2/3”. The same paper reports that “NvActivin is expressed in the endoderm during gastrulation”, citing the Nematostella expression study PMID:16837574. Thus the study provides functional evidence for ancient activin-branch Smad competence and separate expression evidence for a cnidarian activin candidate; it does not connect native NvActivin, native type I/II receptors, NvSmad2/3 and native co-Smad in one ligand-dependent biochemical relay. NvSmad2/3 activates general mesendoderm markers but differs from bilaterian orthologs in organizer/secondary-axis assays, so vertebrate output programs are not universal module outputs.

Additional primary PMID:25156256 (Hydra Nodal-related Ndr and Pitx; DOI10.1038/nature13666) establishes a native nonbilaterian Nodal-related developmental signal. This is relevant evidence for prebilaterian related signaling, but **Nodal is not activin**. It cannot substitute for direct native activin coupling evidence. Targeted searches did not locate a native nonbilaterian agonistic activin ligand→type I/II receptor→Smad2/3–co-Smad experiment. This is a limitation of the present evidence audit, not a proven absence and not an author-stated unresolved biology claim suitable for automatically generating a knowledge_gap. No explicit primary-paper statement establishing that precise unknown was located. If a narrower operational scope is desired, Bilateria (NCBITaxon:33213) must be labelled as the scope of the currently exemplified native relay rather than its evolutionary origin or a hard exclusion boundary; the non-universal Metazoa envelope is preferable here.

### Native fly relay and sharing with BMP

The native agonist anchor is PMID:18820452: “Only Drosophila Activin (dACT) and the Activin-like ligand Dawdle (DAW) signal through BABO in combination with the type II receptor PUNT and activate dSMAD2.” This tests endogenous fly ligands, unlike early Atr-I/Atr-II assays using vertebrate activin. The negative Myoglianin result is restricted to the tested assay and does not invalidate subsequent Myo/Babo isoform findings.

The canonical chemistry is: ligand-driven assembly of Babo/Punt receptor complexes; constitutive type II receptor kinase activity phosphorylates/activates the type I receptor; Babo phosphorylates the terminal R-Smad serines; phospho-Smox associates with Medea; the complex accumulates in the nucleus and regulates transcription. PMID:9887103 says activated Babo “phosphorylates the carboxy-terminal SSXS motif and induces heteromeric complex formation with Medea”. PMID:10320478 states “dSMAD2 complexes with MEDEA only in the presence of ATR-I and PUNT.” The latter paper's shorthand that Smox is phosphorylated by ATR-I and PUNT denotes receptor-complex dependence; it must not assign the direct canonical R-Smad phosphorylation reaction to Punt instead of Babo. Neither Smox nor Medea is a receptor kinase.

PMID:19766717 provides the context-specific pairing result: “Dawdle signaling is active in the presence of the Type-II receptor Punt but not Wit”. It establishes Daw/Babo-C/Punt in the tested cells, not exclusive Actbeta/Babo-B pairing. The published Figure1 legend of review PMID:28130362 explicitly warns that evidence for Actbeta–BaboB is lacking. Therefore the displayed Babo-B UniProt isoform must not be equated to every gene-level Babo assay. Myo can use other Babo isoform/receptor contexts; optional Wit use is not a mandatory alternative for the native dACT/Punt experiment.

Punt and Medea are shared with the BMP branch, independently grounded in primary PMID:7697720 and PMID:9502724 and the comparative BMP review PMID:38124338. BMP normally uses Tkv/Sax→Mad, whereas activin uses Babo→Smox; this receptor/R-Smad specificity defines the branch more reliably than the names of shared components. Conditional Babo→Mad cross-signaling is a documented exception, not the default activin step and not grounds to mark the pathway absent. Likewise mammalian ACVR2 receptors and SMAD4 are not activin-exclusive.

### Functions and family selection for the intracellular steps

For the catalytic steps, use type II activin receptor activity GO:0016362 for ACVR2/Punt and type I activin receptor activity GO:0016361 for ALK4/Babo, with descriptions that identify their different phosphorylation substrates. Ligand cytokine/growth-factor activity is separate from kinase catalysis; the mature agonist dimer is the signaling entity, not every complex containing a beta subunit. An INHBA-containing inhibin-alpha/beta heterodimer must not inherit an agonistic activin activity from sequence membership alone.

SMAD2/SMAD3/Smox have an activated R-Smad assembly/relay role, including co-SMAD binding GO:0070410, and a transcriptional role. SMAD4/Medea contribute R-SMAD binding GO:0070412 and the shared co-Smad transcriptional complex. These binding/assembly steps can be separated from nuclear DNA-dependent regulation; phosphorylation is an input state of the Smads, not a kinase activity they catalyze. Human structural primary PMID:15350224 states: “Both complexes are heterotrimers, comprising two phosphorylated R-Smad subunits and one Smad4 subunit”. This supports the assayed human heterotrimer, without imposing universal promoter-complex stoichiometry in every animal.

For transcription, GO:0000981 (DNA-binding transcription factor activity, RNA polymerase II-specific) is independently supported for all reviewed R-Smad/co-Smad exemplars. Human PMID:31582430 states “properly folded SMAD2 protein has intrinsic DNA-binding activity” and reports that “the full-length SMAD4 protein bound the Gsc1 probe”. Thus full-length E3-containing SMAD2 is not merely a DNA-incompetent cofactor; E3 conformation regulates affinity, and partner-directed targeting remains important. Do not encode the outdated full-length-SMAD2 prohibition or infer that every SMAD2/SMAD3 action is equivalent. Fly PMID:24244197 directly shows that “recombinant Smox protein (MH1-DNA binding domain) binds to Smad binding element (AGAC AGAC)”. Medea DNA binding and activation/repression are independently established in its reviewed primary sources PMID:9694800, PMID:20010841 and PMID:12705870. Transcription can be activating or repressive depending on partners/promoter; generic growth or differentiation outcomes should remain outside the invariant core.

Exact PANTHER identifiers and official labels were checked against both current UniProt flat files and local interpro/panther/panther.obo:

| Exemplar | PANTHER subfamily | Official label |
| --- | --- | --- |
| Human SMAD2 Q15796 | PTHR13703:SF42 | MOTHERS AGAINST DECAPENTAPLEGIC HOMOLOG 2 |
| Human SMAD3 P84022 | PTHR13703:SF53 | MOTHERS AGAINST DECAPENTAPLEGIC HOMOLOG 3 |
| Human SMAD4 Q13485 | PTHR13703:SF63 | MOTHERS AGAINST DECAPENTAPLEGIC HOMOLOG 4 |
| Fly Smox O96660 | PTHR13703:SF25 | MOTHERS AGAINST DECAPENTAPLEGIC HOMOLOG |
| Fly Med O62609 | PTHR13703:SF45 | MOTHERS AGAINST DECAPENTAPLEGIC HOMOLOG |

PTHR13703 itself has official label SMAD and includes functionally different R-, co- and inhibitory Smads. It is valid family membership context, not a blanket activin-function assertion. Use the verified subfamilies as lineage alternatives, or a free-text functional ortholog-group descriptor without an asserted union ID when no single narrower PANTHER term covers the intended role. Do not guess one PANTHER subfamily encompassing human SMAD2/3 plus fly Smox or human SMAD4 plus fly Medea.

### Ligand diversity, Nodal and source cautions

Mammalian activin A/AB/B and the fly Actbeta/Daw/Myo branch share receptor/Smad architecture without one-to-one equivalence of every ligand or isoform. Review PMID:27328872 supports ActA preference for ALK4, broader ALK4/ALK7 use by ActB, and sharing of receptors/SMAD2/3 with Nodal. It also distinguishes Cripto's enhancement of Nodal from inhibition of activin receptor assembly in tested contexts. Therefore Nodal/Cripto-dependent mesendoderm phenotypes do not establish an activin ligand requirement. Activin induction in Xenopus animal caps demonstrates competence of the relay, not that endogenous embryonic mesoderm induction is universally activin-driven. Keep mammalian Nodal signaling as a related module sharing steps rather than a synonym for activin signaling.

Review PMID:34520530 is useful for receptor sharing, variable ligand/receptor affinities and cellular context; its broad superfamily evolutionary discussion is not proof of activin-specific ancient coupling. PMID:22651914 distinguishes receptor-assembly mechanisms among TGF-beta, BMP and activin and should not be generalized to one ligand-binding mechanism. PMID:30540228 explicitly concerns mammalian activin A physiology, so its organ-level outputs do not set the cross-metazoan core.

The C/E-inactivity claims in older review PMID:27328872 and repeated in 2024 review PMID:39595638 are superseded. Primary PMID:35736809 demonstrates ActC/ActAC-dependent ALK7→SMAD2/3 signaling; peer-reviewed PMID:38533769 demonstrates ActE signaling through ALK7 and canonical activin type II receptors (it supersedes preprint PMID:37808681). Root is caching these sources. Do not use the review age or PANTHER family membership to exclude activin C/E from the broader ligand class, nor add these unreviewed exemplars as mandatory members of this compact module. The same caution applies to receptor-name ambiguities: ACVR1/ALK2 is not ACVR1B/ALK4, and activin-binding to a shared BMP receptor does not automatically mean productive canonical SMAD2/3 signaling.


## 2026-10-25 — completed module construction and member review

The final module has four steps, five family selectors, 11 verified PANTHER
subfamilies and 29 curated literature references. Both direct phosphorylation
steps and the three causal edges have primary evidence. The ligand selector is
explicitly conditional on a mature agonistic activin complex; the human GO-CAM
67b1629100002705 likewise represents the agonist as activin A complex rather
than an unassembled INHBA chain. Its ACVR2A/ACVR1B and SMAD2/SMAD3 activities were
checked and linked. The related inhibin model 678073a900001673 represents the
antagonist separately. The cached source models were not edited.

All 11 member reviews now adjudicate all 1658 original rows: human INHBA104,
ACVR1B81, ACVR2A102, SMAD2 284, SMAD3 349, SMAD4 428; fly Actbeta24, babo45,
put83, Smox71 and Med87. Unavailable or unresolved individual claims remain
UNDECIDED. No empty PENDING rows are concealed by the module summary.

The authoritative PANTHER member index was built from release19 classifications
and UniProt, and all selected subfamilies/member placements pass the module
membership checks. The 11 exact member mappings were also independently checked
against their fetched UniProt records. `family_terms` expresses the explicit
union of lineage-specific subfamilies for each functional role; no invented
single family ID or unverified ancestral node stands for that union.

Independent module QA checked all steps, causal edges, reference findings,
taxon limits and GO-CAM activity identifiers and found no blocking defect.
The co-SMAD annoton was strengthened with direct human SMAD4 DNA binding and
SMAD4-dependent activin response-element transcription. Schema and scoped
module validation pass; the final module reports zero warnings, including
member-function conformance. Broader repository validation and PR review are
separate gates, not implied by this local module status.
