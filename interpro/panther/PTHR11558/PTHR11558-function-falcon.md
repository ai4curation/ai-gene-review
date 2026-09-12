---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-24T04:32:00.675936'
end_time: '2026-06-24T04:50:40.042537'
duration_seconds: 1119.37
template_file: templates/treegrafter_family_function.md
template_variables:
  family_id: PTHR11558
  family_name: SPERMIDINE/SPERMINE SYNTHASE
  subfamily: PTHR11558:SF53 PUTRESCINE N-METHYLTRANSFERASE 1
  gene_symbol: NaPMT3
  uniprot: A0A314LG79
  organism: NICAT
  taxon_label: NICAT
  propagated_term: spermidine synthase activity (GO:0004766)
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 27
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: PTHR11558-function-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PTHR11558-function-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# PANTHER Family Function Characterization (TreeGrafter granularity audit)

You are characterizing the function of a **protein family** for AI Gene Review.
This is the companion to a set of blinded gene-level function checks: the point
here is to establish, from primary literature and sequence/structure evidence,
**what function is actually conserved across the family** and **where function
diverges between subfamilies** — because automated phylogenetic annotation
(TreeGrafter/PANTHER) propagates a GO term from an ancestral node to every
descendant, and that is only safe when the family is functionally homogeneous.

## Family Under Review

- **PANTHER family:** PTHR11558 — SPERMIDINE/SPERMINE SYNTHASE
- **Subfamily of interest:** PTHR11558:SF53 PUTRESCINE N-METHYLTRANSFERASE 1
- **Representative member:** NaPMT3 (A0A314LG79), NICAT / NICAT
- **GO term currently propagated at/near this node:** spermidine synthase activity (GO:0004766)

Note: do **not** assume the propagated term is the family's true conserved
function — that is exactly what you are testing.

## Research Objective

1. **Conserved core function.** What molecular function (and reaction/EC where
   relevant) is shared by *characterized* members across the whole family? Anchor
   this to the diagnostic fold, catalytic/binding residues, and obligate
   cofactors/partners — not to the family name.
2. **Functional divergence across subfamilies.** Enumerate the major
   functional subgroups within the family and how they differ (substrate
   specificity, lost catalysis / pseudo-enzymes, neofunctionalization, structural
   co-option). Is the family **homogeneous** (one MF safe to propagate) or
   **heterogeneous** (propagation will mis-annotate some branches)?
3. **Subfamily of interest.** Where does PTHR11558:SF53 PUTRESCINE N-METHYLTRANSFERASE 1 sit — does it carry the
   conserved family function, a more specific specialized activity, or a diverged
   / non-enzymatic role? Name characterized exemplars of that subfamily.
4. **GO granularity verdict.** State the GO MF term appropriate at the **family**
   level versus at the **subfamily** level, and identify any subfamilies for
   which a family-level term would be an over-annotation. This is a lead for
   curators, not a final call.

Where decidable by computation, actually run it (domain/Pfam/InterPro
architecture, catalytic-residue conservation, orthology/paralogy splits) and keep
the result as provenance. Use resources you can access programmatically
(UniProt, InterPro, AlphaFold, sequence computation, public APIs). Prefer PMID
citations to primary literature; treat reviews/databases as orientation. If a
check is web-only or cannot be run, say so — an inconclusive result is acceptable;
never fabricate one.

## Required Output

### Family Function Summary

One paragraph: the conserved core molecular function and the fold/residues that
define it.

### Subfamily Divergence Table

One row per major functional subgroup: subgroup / representative member(s) (PMID)
· molecular function · substrate or specialization · catalytic residues intact?
· GO MF term that fits · notes (pseudo-enzyme, neofunctionalization, etc.).

### Homogeneous vs Heterogeneous Verdict

State plainly whether a single family-level GO MF term is safe to propagate
across this family, and if not, which branches it would mis-annotate.

### Granularity Leads for Curation

Family-level vs subfamily-level GO MF term recommendation, and the subfamilies
(if any) where the currently-propagated term is an over-annotation. Avoid
"protein binding" as a final recommendation.

### Evidence and Gaps

Key citations (PMID preferred), and explicit uncertainties that matter for
deciding the family-vs-subfamily granularity.


## Output

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# PANTHER Family Function Characterization (TreeGrafter granularity audit)

You are characterizing the function of a **protein family** for AI Gene Review.
This is the companion to a set of blinded gene-level function checks: the point
here is to establish, from primary literature and sequence/structure evidence,
**what function is actually conserved across the family** and **where function
diverges between subfamilies** — because automated phylogenetic annotation
(TreeGrafter/PANTHER) propagates a GO term from an ancestral node to every
descendant, and that is only safe when the family is functionally homogeneous.

## Family Under Review

- **PANTHER family:** PTHR11558 — SPERMIDINE/SPERMINE SYNTHASE
- **Subfamily of interest:** PTHR11558:SF53 PUTRESCINE N-METHYLTRANSFERASE 1
- **Representative member:** NaPMT3 (A0A314LG79), NICAT / NICAT
- **GO term currently propagated at/near this node:** spermidine synthase activity (GO:0004766)

Note: do **not** assume the propagated term is the family's true conserved
function — that is exactly what you are testing.

## Research Objective

1. **Conserved core function.** What molecular function (and reaction/EC where
   relevant) is shared by *characterized* members across the whole family? Anchor
   this to the diagnostic fold, catalytic/binding residues, and obligate
   cofactors/partners — not to the family name.
2. **Functional divergence across subfamilies.** Enumerate the major
   functional subgroups within the family and how they differ (substrate
   specificity, lost catalysis / pseudo-enzymes, neofunctionalization, structural
   co-option). Is the family **homogeneous** (one MF safe to propagate) or
   **heterogeneous** (propagation will mis-annotate some branches)?
3. **Subfamily of interest.** Where does PTHR11558:SF53 PUTRESCINE N-METHYLTRANSFERASE 1 sit — does it carry the
   conserved family function, a more specific specialized activity, or a diverged
   / non-enzymatic role? Name characterized exemplars of that subfamily.
4. **GO granularity verdict.** State the GO MF term appropriate at the **family**
   level versus at the **subfamily** level, and identify any subfamilies for
   which a family-level term would be an over-annotation. This is a lead for
   curators, not a final call.

Where decidable by computation, actually run it (domain/Pfam/InterPro
architecture, catalytic-residue conservation, orthology/paralogy splits) and keep
the result as provenance. Use resources you can access programmatically
(UniProt, InterPro, AlphaFold, sequence computation, public APIs). Prefer PMID
citations to primary literature; treat reviews/databases as orientation. If a
check is web-only or cannot be run, say so — an inconclusive result is acceptable;
never fabricate one.

## Required Output

### Family Function Summary

One paragraph: the conserved core molecular function and the fold/residues that
define it.

### Subfamily Divergence Table

One row per major functional subgroup: subgroup / representative member(s) (PMID)
· molecular function · substrate or specialization · catalytic residues intact?
· GO MF term that fits · notes (pseudo-enzyme, neofunctionalization, etc.).

### Homogeneous vs Heterogeneous Verdict

State plainly whether a single family-level GO MF term is safe to propagate
across this family, and if not, which branches it would mis-annotate.

### Granularity Leads for Curation

Family-level vs subfamily-level GO MF term recommendation, and the subfamilies
(if any) where the currently-propagated term is an over-annotation. Avoid
"protein binding" as a final recommendation.

### Evidence and Gaps

Key citations (PMID preferred), and explicit uncertainties that matter for
deciding the family-vs-subfamily granularity.


# PANTHER Family PTHR11558 — SPERMIDINE/SPERMINE SYNTHASE: TreeGrafter Granularity Audit

## Family Function Summary

PANTHER family PTHR11558 encompasses enzymes built on a conserved Rossmann-like fold that was ancestrally adapted for binding S-adenosylmethionine (SAM) and its decarboxylated derivative (dcAdoMet) (kozbial2005naturalhistoryof pages 6-7, kozbial2005naturalhistoryof pages 15-16). The majority of characterized members are **aminopropyltransferases** that use dcAdoMet as the aminopropyl group donor and transfer it to polyamine substrates (putrescine, spermidine, agmatine, or cadaverine) (pegg2010sperminesynthase pages 4-6, fuell2010polyaminebiosyntheticdiversity pages 3-4). The catalytic mechanism centers on two conserved aspartate residues: one (e.g., Asp101 in spermidine synthase) in the glycine-rich loop (motif I) that creates a binding cavity too small to accommodate SAM's carboxyl group, thereby enforcing dcAdoMet specificity; and another (e.g., Asp170/Asp276) that deprotonates the amine substrate to enable nucleophilic attack on the methylene carbon of dcAdoMet (pegg2010sperminesynthase pages 4-6, kozbial2005naturalhistoryof pages 6-7). All characterized aminopropyltransferases exist as dimeric or tetrameric structures and share a conserved sequence motif (V/I)(I/V/L)GGG(D/E)G(G/A) surrounding the key acidic residue (pegg2010sperminesynthase pages 4-6). However, the family also contains a neofunctionalized branch — **putrescine N-methyltransferase (PMT, EC 2.1.1.53)** — that has evolved from spermidine synthase to bind unmodified SAM and transfer a methyl group (rather than an aminopropyl group) to putrescine, committing it to nicotine/tropane alkaloid biosynthesis (fuell2010polyaminebiosyntheticdiversity pages 4-6). This functional split means the family is not defined by a single molecular function, and the fold alone is insufficient to predict catalytic activity.

## Subfamily Divergence Table

| Subgroup | Representative Member(s) (PMID/Citation) | Molecular Function | Substrate/Specialization | Catalytic Residues Intact? | GO MF Term That Fits | Notes |
|---|---|---|---|---|---|---|
| Spermidine synthase (SpdSyn; EC 2.5.1.16) | *E. coli* SpeE; human SRM/spermidine synthase (pegg2010sperminesynthase pages 4-6, kozbial2005naturalhistoryof pages 6-7, kozbial2005naturalhistoryof pages 15-16) | Aminopropyltransferase; transfers aminopropyl from dcAdoMet to putrescine to form spermidine | Canonical polyamine biosynthesis; widespread across bacteria, archaea, and eukaryotes | Yes; conserved acidic residues for dcAdoMet recognition and amine deprotonation are intact (pegg2010sperminesynthase pages 4-6, kozbial2005naturalhistoryof pages 6-7) | GO:0004766 spermidine synthase activity | Best-supported ancestral/core activity for the aminopropyltransferase branch; Rossmann-like/AdoMet-MT fold adapted for dcAdoMet use (pegg2010sperminesynthase pages 4-6, kozbial2005naturalhistoryof pages 15-16) |
| Spermine synthase (SpmSyn; EC 2.5.1.22) | human SMS/spermine synthase (pegg2010sperminesynthase pages 6-8, pegg2010sperminesynthase pages 4-6) | Aminopropyltransferase; transfers aminopropyl from dcAdoMet to spermidine N8 to form spermine | Metazoa, flowering plants, some fungi; accepts spermidine rather than putrescine | Yes; catalytic acidic residues retained; substrate pocket enlarged relative to SpdSyn, including Trp→Ala change associated with spermidine accommodation (pegg2010sperminesynthase pages 4-6) | GO:0016768 spermine synthase activity | Diverged aminopropyltransferase specificity, not spermidine synthase; metazoan enzymes carry an N-terminal domain derived from bacterial class 1B AdoMetDC that is structural/dimerization-related rather than catalytic (pegg2010sperminesynthase pages 6-8, michael2017evolutionofbiosynthetic pages 9-12) |
| Thermospermine synthase (ACL5/TspSyn) | *Arabidopsis thaliana* ACL5; diatom ACL5 homologue from *Thalassiosira pseudonana* (fuell2010polyaminebiosyntheticdiversity pages 3-4, michael2017evolutionofbiosynthetic pages 9-12) | Aminopropyltransferase; transfers aminopropyl from dcAdoMet to spermidine N1 to form thermospermine | Plants, green algae, red algae, some secondary-plastid lineages; positional isomer specificity distinct from SpmSyn | Yes; aminopropyltransferase catalytic machinery retained (fuell2010polyaminebiosyntheticdiversity pages 3-4, michael2017evolutionofbiosynthetic pages 9-12) | GO:0102542 thermospermine synthase activity | Specialized plant/algal branch; thermospermine is important for plant growth and vascular development, especially in *Arabidopsis* acl5 biology (fuell2010polyaminebiosyntheticdiversity pages 6-6, michael2017evolutionofbiosynthetic pages 9-12) |
| Putrescine N-methyltransferase (PMT; EC 2.1.1.53) | NtPMT (*Nicotiana tabacum*), DsPMT (*Datura stramonium*), NaPMT3 (*Nicotiana attenuata*) (fuell2010polyaminebiosyntheticdiversity pages 4-6, tong2025dnamethylationvalley pages 2-4, riechers1999structureandexpression pages 10-12, shoji2024geneticregulationand pages 2-3) | Methyltransferase; transfers methyl from SAM to putrescine to form N-methylputrescine | Specialized alkaloid biosynthesis in Solanaceae and Convolvulaceae; first committed step toward nicotine/tropane alkaloids | Partly conserved/diverged: catalytic Asp for amine activation retained, but the dcAdoMet-discriminating Asp/glycine-loop environment is altered to permit SAM binding instead of dcAdoMet (kozbial2005naturalhistoryof pages 6-7, fuell2010polyaminebiosyntheticdiversity pages 4-6) | GO:0030737 putrescine N-methyltransferase activity | Clear neofunctionalization from SpdSyn: same fold and high sequence similarity, but different cofactor (SAM), transferred group (methyl), and pathway role; this branch would be misannotated by GO:0004766 (fuell2010polyaminebiosyntheticdiversity pages 4-6, shoji2015polyaminederivedalkaloidsin pages 1-4) |
| Microbial aminopropyltransferases (relaxed specificity) | *Thermus thermophilus* agmatine aminopropyltransferase; *Pyrococcus furiosus* aminopropyltransferase (described in family literature) (fuell2010polyaminebiosyntheticdiversity pages 3-4, pegg2010sperminesynthase pages 1-2, michael2017evolutionofbiosynthetic pages 14-15) | Aminopropyltransferases using dcAdoMet with broader acceptor range | Agmatine, cadaverine, putrescine, spermidine, 1,3-diaminopropane, and related amines; bacteria and archaea | Yes; catalytic aminopropyltransferase residues are generally retained (fuell2010polyaminebiosyntheticdiversity pages 3-4, pegg2010sperminesynthase pages 1-2) | GO:0004766 where true spermidine synthase has been shown; otherwise a more specific aminopropyltransferase term is preferable if available | Functionally broader than classical SpdSyn; can produce unusual polyamines and shows why a single family-level “spermidine synthase activity” call is unsafe across all branches (fuell2010polyaminebiosyntheticdiversity pages 3-4, pegg2010sperminesynthase pages 1-2, michael2017evolutionofbiosynthetic pages 14-15) |


*Table: This table summarizes the major functional branches within PTHR11558 and shows that the family is functionally heterogeneous. It is especially useful for curation because it highlights that the PMT branch is a methyltransferase neofunctionalization and should not inherit spermidine synthase activity.*

## Homogeneous vs. Heterogeneous Verdict

**The family PTHR11558 is functionally HETEROGENEOUS.** A single family-level GO molecular function term is **not safe** to propagate across all descendants.

The deepest split is between the aminopropyltransferase branches (spermidine synthase, spermine synthase, thermospermine synthase, and microbial broad-specificity aminopropyltransferases) and the **putrescine N-methyltransferase** (PMT) branch. PMT evolved from spermidine synthase through gene duplication and neofunctionalization in the Solanaceae/Convolvulaceae lineage, retaining ~70% sequence identity but switching from dcAdoMet-dependent aminopropyl transfer to SAM-dependent methyl transfer (fuell2010polyaminebiosyntheticdiversity pages 4-6, kozbial2005naturalhistoryof pages 6-7). The switch can be achieved with changes in only a few amino acid residues affecting cofactor binding (shoji2015polyaminederivedalkaloidsin pages 1-4, kozbial2005naturalhistoryof pages 6-7). Even within the aminopropyltransferase branches, substrate specificity diverges: spermidine synthase aminopropylates putrescine, spermine synthase aminopropylates the N8 position of spermidine, thermospermine synthase aminopropylates the N1 position of spermidine, and microbial enzymes can accept agmatine, cadaverine, or other amines (fuell2010polyaminebiosyntheticdiversity pages 3-4, pegg2010sperminesynthase pages 6-8, pegg2010sperminesynthase pages 1-2, pegg2010sperminesynthase pages 4-6).

**Propagating GO:0004766 (spermidine synthase activity) at the family level would mis-annotate:**
1. **PTHR11558:SF53 (PMT)** — these are methyltransferases, not aminopropyltransferases
2. **Spermine synthase subfamilies** — these have different substrate specificity (spermidine → spermine, not putrescine → spermidine)
3. **Thermospermine synthase subfamilies** — these produce the positional isomer thermospermine, not spermine or spermidine
4. **Microbial broad-specificity aminopropyltransferases** — some have been shown to prefer agmatine or cadaverine over putrescine

## Granularity Leads for Curation

> PTHR11558 is functionally **heterogeneous**, so a single family-level molecular function term is **not** safe to propagate across all descendants. Characterized members share a Rossmann-like/AdoMet-dependent transferase fold, but they diverge in both cofactor usage and chemistry: classical aminopropyltransferases use **dcAdoMet** to transfer an aminopropyl group, whereas PMT uses **SAM** to transfer a methyl group (pegg2010sperminesynthase pages 4-6, fuell2010polyaminebiosyntheticdiversity pages 4-6, kozbial2005naturalhistoryof pages 6-7).
>
> The currently propagated term **spermidine synthase activity (GO:0004766)** is therefore a **mis-annotation** for **PTHR11558:SF53 Putrescine N-methyltransferase 1**. PMT catalyzes **putrescine + SAM → N-methylputrescine + SAH** (EC 2.1.1.53), the first committed step in nicotine/tropane alkaloid biosynthesis, rather than aminopropyl transfer to form spermidine (shoji2015polyaminederivedalkaloidsin pages 1-4, fuell2010polyaminebiosyntheticdiversity pages 4-6, shoji2024geneticregulationand pages 2-3).
>
> For curation, the most defensible family-level statement is only a very broad **S-adenosylmethionine-dependent transferase activity**, but that term is too coarse to be biologically informative; **subfamily-level annotation is required** (pegg2010sperminesynthase pages 4-6, fuell2010polyaminebiosyntheticdiversity pages 4-6, kozbial2005naturalhistoryof pages 15-16).
>
> Recommended correction for **SF53**: assign **putrescine N-methyltransferase activity (GO:0030737)**, **not** GO:0004766. This is supported by the established evolutionary neofunctionalization of PMT from spermidine synthase, with altered cofactor-binding residues that permit SAM binding instead of dcAdoMet (fuell2010polyaminebiosyntheticdiversity pages 4-6, kozbial2005naturalhistoryof pages 6-7).
>
> Over-annotation risk extends beyond SF53: even the aminopropyltransferase branches are not uniform in acceptor specificity or product. Distinct subfamilies catalyze **putrescine → spermidine (SpdSyn)**, **spermidine → spermine (SpmSyn)**, or **spermidine → thermospermine (TspSyn/ACL5)**, so GO terms should track these branch-specific reactions rather than collapse them to a single family-wide MF (fuell2010polyaminebiosyntheticdiversity pages 3-4, pegg2010sperminesynthase pages 6-8, pegg2010sperminesynthase pages 4-6, michael2017evolutionofbiosynthetic pages 9-12).


*Blockquote: This blockquote summarizes the curator-facing conclusion for PTHR11558. It highlights why family-wide propagation of spermidine synthase activity is unsafe and specifies the correct GO direction for the PMT subfamily SF53.*

**Recommended GO MF terms by subfamily level:**

| Subfamily | Recommended GO MF | Currently Propagated | Assessment |
|---|---|---|---|
| Spermidine synthase (SpdSyn) | GO:0004766 spermidine synthase activity | GO:0004766 | **Correct** |
| Spermine synthase (SpmSyn) | GO:0016768 spermine synthase activity | GO:0004766 | **Over-annotation** — wrong substrate specificity |
| Thermospermine synthase (ACL5) | GO:0102542 thermospermine synthase activity | GO:0004766 | **Over-annotation** — wrong product |
| **PMT (SF53)** | **GO:0030737 putrescine N-methyltransferase activity** | GO:0004766 | **Mis-annotation** — entirely wrong reaction type and cofactor |
| Microbial aminopropyltransferases | Context-dependent; GO:0004766 if SpdSyn confirmed | GO:0004766 | **Risky** — requires experimental validation |

**Family-level safe term:** At most, a very broad term such as "S-adenosylmethionine-dependent transferase activity" could be defended at the family root, but this is too uninformative for practical annotation. **Subfamily-level annotation is required for this family.**

## Subfamily of Interest: PTHR11558:SF53 — Putrescine N-methyltransferase 1

PTHR11558:SF53 encompasses putrescine N-methyltransferases, including NaPMT3 (A0A314LG79) from *Nicotiana attenuata*. PMT catalyzes the reaction: **putrescine + SAM → N-methylputrescine + S-adenosylhomocysteine** (EC 2.1.1.53) (fuell2010polyaminebiosyntheticdiversity pages 4-6). This is the first committed step in nicotine and tropane alkaloid biosynthesis in solanaceous plants (shoji2015polyaminederivedalkaloidsin pages 1-4, shoji2024geneticregulationand pages 2-3). Characterized exemplars include NtPMT1–4 from *Nicotiana tabacum* (five genes total), DsPMT from *Datura stramonium*, and NaPMT genes from *N. attenuata* (riechers1999structureandexpression pages 10-12, riechers1999structureandexpression pages 1-2, riechers1999structureandexpression pages 4-5). PMT expression is root-specific, jasmonate-inducible, and regulated by transcription factors including MYC2 (tong2025dnamethylationvalley pages 2-4, riechers1999structureandexpression pages 12-14, shoji2024geneticregulationand pages 3-4).

PMT evolved from spermidine synthase by gene duplication and neofunctionalization before the divergence of Solanaceae and Convolvulaceae (fuell2010polyaminebiosyntheticdiversity pages 4-6). Despite sharing the same Rossmann-like fold and ~70% sequence identity with SpdSyn (kozbial2005naturalhistoryof pages 6-7), PMT underwent critical changes: (1) the dcAdoMet-discriminating aspartate in the glycine-rich loop was altered to permit SAM binding; (2) the putrescine-binding site was modified; and (3) the transferred chemical group switched from aminopropyl to methyl (kozbial2005naturalhistoryof pages 6-7, fuell2010polyaminebiosyntheticdiversity pages 4-6). This represents a clear case of **neofunctionalization** — the enzyme retains the ancestral fold but performs a categorically different reaction. Down-regulation of PMT in transgenic plants reduces nicotine accumulation but increases anatabine and polyamine levels, confirming its non-redundant role in alkaloid rather than polyamine biosynthesis (shoji2024geneticregulationand pages 2-3, shoji2024geneticregulationand pages 3-4).

**This subfamily does not carry the conserved aminopropyltransferase function** and should not be annotated with GO:0004766. The correct annotation is **GO:0030737 (putrescine N-methyltransferase activity)**.

## Evidence and Gaps

**Key citations supporting this analysis:**
- Pegg & Michael (2010) *Cell. Mol. Life Sci.* 67:113–121 — comprehensive review of spermine synthase structure and aminopropyltransferase mechanism (PMID: 19756388) (pegg2010sperminesynthase pages 4-6, pegg2010sperminesynthase pages 6-8, pegg2010sperminesynthase pages 1-2)
- Kozbial & Mushegian (2005) *BMC Struct. Biol.* 5:19 — natural history of SAM-binding proteins, documents ~70% identity between SpdSyn and PMT (PMID: 16225687) (kozbial2005naturalhistoryof pages 6-7, kozbial2005naturalhistoryof pages 15-16)
- Fuell et al. (2010) *Plant Physiol. Biochem.* 48:513–520 — polyamine biosynthetic diversity in plants, confirms PMT evolution from SpdSyn (PMID: 20219381) (fuell2010polyaminebiosyntheticdiversity pages 4-6, fuell2010polyaminebiosyntheticdiversity pages 3-4)
- Shoji & Hashimoto (2015) in *Polyamines*, Springer — details PMT mechanism and SAM vs dcAdoMet switch (shoji2015polyaminederivedalkaloidsin pages 1-4)
- Michael (2017) *Biochem. J.* 474:2277–2299 — evolution of biosynthetic diversity in polyamine metabolism (PMID: 28687717) (michael2017evolutionofbiosynthetic pages 9-12)
- Riechers & Timko (1999) *Plant Mol. Biol.* 41:387–401 — PMT gene family structure in *N. tabacum* (PMID: 10598105) (riechers1999structureandexpression pages 10-12, riechers1999structureandexpression pages 1-2, riechers1999structureandexpression pages 12-14, riechers1999structureandexpression pages 4-5)
- Shoji, Hashimoto & Saito (2024) *J. Exp. Bot.* 75:1741–1753 — genetic regulation of nicotine biosynthesis, PMT role (shoji2024geneticregulationand pages 2-3, shoji2024geneticregulationand pages 3-4)
- Tong, Wang & Wu (2025) *Front. Plant Sci.* — NaPMT root-specific expression and epigenetic regulation in *N. attenuata* (tong2025dnamethylationvalley pages 2-4, tong2025dnamethylationvalley pages 1-2)
- Biastoff et al. (2009) *FEBS Lett.* — evolution of PMT from SpdSyn with substrate binding alterations (referenced but full text unobtainable)
- Junker et al. (2013) — demonstrated few amino acid changes can switch between SpdSyn and PMT activity (referenced in Shoji 2015 but full text unobtainable)

**Explicit uncertainties:**
1. **No crystal structure of PMT** is currently available in the PDB; structural inferences rely on homology modeling against SpdSyn structures. A PMT crystal structure would definitively confirm the cofactor-binding site alterations.
2. **Junker et al. (2013)** is cited as demonstrating that only a few amino acid residues are needed to switch between SpdSyn and PMT activity, but the full text was unobtainable for direct verification of specific residue identities.
3. **Exact PANTHER subfamily boundaries** within the aminopropyltransferase branches (SpdSyn vs. SpmSyn vs. TspSyn) could not be verified computationally in this analysis; subfamily assignments depend on the PANTHER tree topology, which was not directly inspected.
4. **Microbial aminopropyltransferases with relaxed specificity** may span multiple PANTHER subfamilies; their precise placement relative to the named subfamilies is uncertain without tree inspection.
5. The **NaPMT3 protein (A0A314LG79)** specifically has not been biochemically characterized in isolation; its PMT activity is inferred from homology to characterized NtPMT proteins and gene expression context in *N. attenuata* nicotine biosynthesis.

References

1. (kozbial2005naturalhistoryof pages 6-7): Piotr Z Kozbial and Arcady R Mushegian. Natural history of s-adenosylmethionine-binding proteins. BMC Structural Biology, 5:19-19, Oct 2005. URL: https://doi.org/10.1186/1472-6807-5-19, doi:10.1186/1472-6807-5-19. This article has 407 citations and is from a peer-reviewed journal.

2. (kozbial2005naturalhistoryof pages 15-16): Piotr Z Kozbial and Arcady R Mushegian. Natural history of s-adenosylmethionine-binding proteins. BMC Structural Biology, 5:19-19, Oct 2005. URL: https://doi.org/10.1186/1472-6807-5-19, doi:10.1186/1472-6807-5-19. This article has 407 citations and is from a peer-reviewed journal.

3. (pegg2010sperminesynthase pages 4-6): Anthony E. Pegg and Anthony J. Michael. Spermine synthase. Cellular and Molecular Life Sciences, 67:113-121, Oct 2010. URL: https://doi.org/10.1007/s00018-009-0165-5, doi:10.1007/s00018-009-0165-5. This article has 220 citations and is from a domain leading peer-reviewed journal.

4. (fuell2010polyaminebiosyntheticdiversity pages 3-4): Christine Fuell, Katherine A. Elliott, Colin C. Hanfrey, Marina Franceschetti, and Anthony J. Michael. Polyamine biosynthetic diversity in plants and algae. Plant physiology and biochemistry : PPB, 48 7:513-20, Jul 2010. URL: https://doi.org/10.1016/j.plaphy.2010.02.008, doi:10.1016/j.plaphy.2010.02.008. This article has 237 citations.

5. (fuell2010polyaminebiosyntheticdiversity pages 4-6): Christine Fuell, Katherine A. Elliott, Colin C. Hanfrey, Marina Franceschetti, and Anthony J. Michael. Polyamine biosynthetic diversity in plants and algae. Plant physiology and biochemistry : PPB, 48 7:513-20, Jul 2010. URL: https://doi.org/10.1016/j.plaphy.2010.02.008, doi:10.1016/j.plaphy.2010.02.008. This article has 237 citations.

6. (pegg2010sperminesynthase pages 6-8): Anthony E. Pegg and Anthony J. Michael. Spermine synthase. Cellular and Molecular Life Sciences, 67:113-121, Oct 2010. URL: https://doi.org/10.1007/s00018-009-0165-5, doi:10.1007/s00018-009-0165-5. This article has 220 citations and is from a domain leading peer-reviewed journal.

7. (michael2017evolutionofbiosynthetic pages 9-12): Anthony J. Michael. Evolution of biosynthetic diversity. The Biochemical journal, 474 14:2277-2299, Jul 2017. URL: https://doi.org/10.1042/bcj20160823, doi:10.1042/bcj20160823. This article has 51 citations.

8. (fuell2010polyaminebiosyntheticdiversity pages 6-6): Christine Fuell, Katherine A. Elliott, Colin C. Hanfrey, Marina Franceschetti, and Anthony J. Michael. Polyamine biosynthetic diversity in plants and algae. Plant physiology and biochemistry : PPB, 48 7:513-20, Jul 2010. URL: https://doi.org/10.1016/j.plaphy.2010.02.008, doi:10.1016/j.plaphy.2010.02.008. This article has 237 citations.

9. (tong2025dnamethylationvalley pages 2-4): Ahui Tong, Bingwu Wang, and Jinsong Wu. Dna methylation valley as a distinguishing feature occurs in root-specific expressed nicotine-related genes in nicotiana attenuata. Frontiers in Plant Science, Aug 2025. URL: https://doi.org/10.3389/fpls.2025.1647622, doi:10.3389/fpls.2025.1647622. This article has 2 citations.

10. (riechers1999structureandexpression pages 10-12): Dean E. Riechers and Michael P. Timko. Structure and expression of the gene family encoding putrescine n-methyltransferase in nicotiana tabacum: new clues to the evolutionary origin of cultivated tobacco. Plant Molecular Biology, 41:387-401, Oct 1999. URL: https://doi.org/10.1023/a:1006342018991, doi:10.1023/a:1006342018991. This article has 149 citations and is from a peer-reviewed journal.

11. (shoji2024geneticregulationand pages 2-3): Tsubasa Shoji, Takashi Hashimoto, and Kazuki Saito. Genetic regulation and manipulation of nicotine biosynthesis in tobacco: strategies to eliminate addictive alkaloids. Journal of Experimental Botany, 75:1741-1753, Aug 2024. URL: https://doi.org/10.1093/jxb/erad341, doi:10.1093/jxb/erad341. This article has 43 citations and is from a domain leading peer-reviewed journal.

12. (shoji2015polyaminederivedalkaloidsin pages 1-4): Tsubasa Shoji and Takashi Hashimoto. Polyamine-derived alkaloids in plants: molecular elucidation of biosynthesis. ArXiv, pages 189-200, Nov 2015. URL: https://doi.org/10.1007/978-4-431-55212-3\_16, doi:10.1007/978-4-431-55212-3\_16. This article has 12 citations.

13. (pegg2010sperminesynthase pages 1-2): Anthony E. Pegg and Anthony J. Michael. Spermine synthase. Cellular and Molecular Life Sciences, 67:113-121, Oct 2010. URL: https://doi.org/10.1007/s00018-009-0165-5, doi:10.1007/s00018-009-0165-5. This article has 220 citations and is from a domain leading peer-reviewed journal.

14. (michael2017evolutionofbiosynthetic pages 14-15): Anthony J. Michael. Evolution of biosynthetic diversity. The Biochemical journal, 474 14:2277-2299, Jul 2017. URL: https://doi.org/10.1042/bcj20160823, doi:10.1042/bcj20160823. This article has 51 citations.

15. (riechers1999structureandexpression pages 1-2): Dean E. Riechers and Michael P. Timko. Structure and expression of the gene family encoding putrescine n-methyltransferase in nicotiana tabacum: new clues to the evolutionary origin of cultivated tobacco. Plant Molecular Biology, 41:387-401, Oct 1999. URL: https://doi.org/10.1023/a:1006342018991, doi:10.1023/a:1006342018991. This article has 149 citations and is from a peer-reviewed journal.

16. (riechers1999structureandexpression pages 4-5): Dean E. Riechers and Michael P. Timko. Structure and expression of the gene family encoding putrescine n-methyltransferase in nicotiana tabacum: new clues to the evolutionary origin of cultivated tobacco. Plant Molecular Biology, 41:387-401, Oct 1999. URL: https://doi.org/10.1023/a:1006342018991, doi:10.1023/a:1006342018991. This article has 149 citations and is from a peer-reviewed journal.

17. (riechers1999structureandexpression pages 12-14): Dean E. Riechers and Michael P. Timko. Structure and expression of the gene family encoding putrescine n-methyltransferase in nicotiana tabacum: new clues to the evolutionary origin of cultivated tobacco. Plant Molecular Biology, 41:387-401, Oct 1999. URL: https://doi.org/10.1023/a:1006342018991, doi:10.1023/a:1006342018991. This article has 149 citations and is from a peer-reviewed journal.

18. (shoji2024geneticregulationand pages 3-4): Tsubasa Shoji, Takashi Hashimoto, and Kazuki Saito. Genetic regulation and manipulation of nicotine biosynthesis in tobacco: strategies to eliminate addictive alkaloids. Journal of Experimental Botany, 75:1741-1753, Aug 2024. URL: https://doi.org/10.1093/jxb/erad341, doi:10.1093/jxb/erad341. This article has 43 citations and is from a domain leading peer-reviewed journal.

19. (tong2025dnamethylationvalley pages 1-2): Ahui Tong, Bingwu Wang, and Jinsong Wu. Dna methylation valley as a distinguishing feature occurs in root-specific expressed nicotine-related genes in nicotiana attenuata. Frontiers in Plant Science, Aug 2025. URL: https://doi.org/10.3389/fpls.2025.1647622, doi:10.3389/fpls.2025.1647622. This article has 2 citations.

## Artifacts

- [Edison artifact artifact-00](PTHR11558-function-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PTHR11558-function-falcon_artifacts/artifact-01.md)