# APLN (apelin, Q9ULZ1) — review notes

Working notes for the GO annotation review of human APLN. Inline provenance throughout:
`[PMID:NNNN "verbatim quote"]`. Everything numeric that could be counted was counted, by
the scripts in `APLN-bioinformatics/` (see its `RESULTS.md`); nothing here is a
recollection of a number.

---

## 1. Inputs, and what they are

- **Accession check.** `APLN-uniprot.txt` is `ID APEL_HUMAN Reviewed; 77 AA.`,
  `AC Q9ULZ1; Q4VY08; Q8WU89;`, gene `Name=APLN {ECO:0000312|HGNC:HGNC:16665}`. This is the
  expected entry, not a merged accession redirecting to another protein. Sequence version 1
  (01-MAY-2000), entry version 169.
- **GOA.** 41 rows. One IBA, one PANTHER family (`DR PANTHER; PTHR15953; APELIN; 1.`,
  subfamily `PTHR15953:SF0`). `check_goa_reconciliation.py` confirms 41 GOA rows ↔ 41
  reviewed YAML entries with identical normalised `supporting_entities`.
- **Affinage.** `self_evaluation_pairwise: win`, `faith_pct: 100.0`, 31 citations, all
  numeric PMIDs (no `PMID:bio_...` bioRxiv ids), and `.affinage.log` records
  `trust gates clear`. The record describes the right protein — apelin, APJ/APLNR, ACE2 —
  with no symbol collision of the AGT/AGXT kind. It is a good map of the modern apelin
  literature and it is where I found the ACE2/NEP metabolism thread, the I109^3.32 bias
  residue, and the ELA-versus-apelin distinct-binding-mode work.
- **Cached publications.** Seven seeded from GOA; I fetched eleven more (listed in §13). Four of the
  seven seeded papers are abstract-only (`full_text_available: false`): PMID:9792798,
  PMID:10525157, PMID:11359874 and PMID:38428423. Of the eleven I fetched, four have full
  text (PMID:15231996, PMID:19767528, PMID:24251091, PMID:28890073) and seven are
  abstract-only.

## 2. What the gene product actually is

Apelin is *not* a protein that does something; it is a 77-residue **precursor** whose
C-terminal tail is released as a family of short peptides. UniProt lists four named
chains — `PEPTIDE 42..77 Apelin-36`, `47..77 Apelin-31`, `50..77 Apelin-28`,
`65..77 Apelin-13` — behind `SIGNAL 1..22` and `PROPEP 23..41`, with
[file:human/APLN/APLN-uniprot.txt "Several active peptides may be produced by proteolytic processing"].
Apelin-17 (residues 61–77, "K17F") is used throughout the literature but has no UniProt
PEPTIDE feature.

This is the same shape of problem as AGT: nearly every annotation on the gene is really
about a peptide cleaved out of it, tested as a synthetic, often in another species. Two
questions decide how much that matters, and both are answerable.

**(a) Is the rodent peptide the human peptide?** Yes, exactly.
`cterm_conservation.py` fetched all 333 UniProtKB members of PTHR15953 and measured
per-column identity to human over the C-terminal 13 residues, against an N-terminal window
of the same size as an internal control. Mean identity 93.7 % versus 47.2 %. Column by
column, positions 66–77 (`RPRLSHKGPMPF`) are 97.0–98.5 % identical while position 65 (Q,
the residue that becomes the pyroglutamate of `[Pyr1]apelin-13`) is only 41.1 %. Among the
five Swiss-Prot members — all 77 aa — human, rat, mouse and bovine apelin-13 **and**
apelin-17 are *identical*; only apelin-36 diverges (2–4 substitutions), i.e. divergence is
confined to the part that is trimmed off. Zebrafish differs at one position in apelin-13.

The consequence is concrete: when Reaux et al. stimulate a rat receptor with
K17F = `Lys-Phe-Arg-Arg-Gln-Arg-Pro-Arg-Leu-Ser-His-Lys-Gly-Pro-Met-Pro-Phe`, that peptide
*is* human apelin-17, residue for residue. The usual "this was rodent work" caveat does not
apply at the level of the ligand. It still applies at the level of the receptor, the tissue
and the organism.

**(b) Which forms are endogenous?** Apelin-13 dominates.
[PMID:15231996 "We first characterized the predominant molecular forms of endogenous hypothalamic and plasma apelin as corresponding to apelin 13 and, to a lesser extent, to apelin 17."]
Processing runs straight to the short form: furin cleaves proapelin directly to apelin-13
[PMID:24251091 "We show direct cleavage of proapelin to apelin-13 by proprotein convertase subtilisin/kexin 3 (PCSK3, or furin) in vitro, with no production of longer isoforms."],
which contradicts the textbook cascade proapelin → apelin-36 → shorter forms.

**(c) How is it terminated?** By ACE2, which removes exactly one residue.
[PMID:11815627 "in each case, the proteolytic activity resulted in removal of the C-terminal residue only"]
and the derived motif
[PMID:11815627 "An alignment of the ACE2 peptide substrates reveals a consensus sequence of: Pro-X((1-3 residues))-Pro-Hydrophobic, where hydrolysis occurs between proline and the hydrophobic amino acid."].
Human apelin ends `...K72-G73-P74-M75-P76-F77`, so `P74-M75-P76-F77` is Pro-X(1)-Pro-Phe
and the residue removed is **Phe77**. `cterm_conservation.py` finds that motif in 328/333
(98.5 %) family members and Phe as the terminal residue in the same 328/333. The physiology
follows: [PMID:27217402 "In ACE2 knockout mice, hypotensive action of pyr-apelin 13 and apelin 17 was potentiated"]
and [PMID:27217402 "We conclude that ACE2 represents a major negative regulator of apelin action in the vasculature and heart."]

Phe77 is also what UniProt flags as `SITE 77 Important for the balance between G(i) and
beta-arrestin pathways induced by apelin-13-APLNR system` (ECO:0000269|PubMed:38428423),
alongside `SITE 75`. So the same terminal Phe sets signalling bias and is the switch ACE2
throws. The review therefore carries a **retention** residue claim (human keeps the Phe its
rodent/bovine orthologs carry), not the more usual loss claim.

The N-terminal half of the peptide matters too, and there is a clean measured negative:
[PMID:11359874 "In contrast, the apelin fragments R10F (Arg8-Leu-Ser-His-Lys-Gly-Pro-Met-Pro-Phe17) and G5F (Gly13-Pro-Met-Pro-Phe17) were inactive."]
R10F begins one residue into the `RPRL` motif, so both ends of apelin-13 are required.

## 3. The molecular function: which term, and for which entity

Three MF terms are on the gene: `GO:0005102 signaling receptor binding` (TAS ×2),
`GO:0031704 apelin receptor binding` (IDA, IEA) and `GO:0005179 hormone activity`
(IDA, IEA, IMP).

- `GO:0031704` is `is_a GO:0001664 G protein-coupled receptor binding is_a GO:0005102`
  (QuickGO ancestors), so the two `GO:0005102` rows are the generic parent of a term the
  gene already has. That is a straight granularity fix, not a disagreement.
- `GO:0005179 hormone activity` is `is_a GO:0048018 receptor ligand activity` in current
  GO, and its definition is permissive about route:
  *"any substance formed in very small amounts in one specialized organ or group of cells
  and carried (sometimes in the bloodstream) to another organ or group of cells"*. The
  parenthetical is what saves it here, because the best human measurement of circulating
  apelin comes with an explicit authorial caveat:
  [PMID:28137936 "Both ELA and apelin were detectable in human plasma at subnanomolar levels, more indicative of peptides acting as locally released autocrine/paracrine mediators than as circulating hormones."]
  I read this as: `hormone activity` is defensible under the GO definition and should be
  kept, but the review should say plainly that apelin's dominant mode is autocrine/paracrine
  — and it is worth a question to GO whether `GO:0005179` is the term a paracrine peptide
  should carry when `GO:0048018` exists and the term's own comment says
  *"Also consider annotating to 'receptor agonist activity ; GO:0048018'."*

The functional pharmacology is real and human where it counts:
[PMID:22810587 "Engineered cells stably expressing human APJ (APJ-HEK) responded to apelin by increasing the content of pERK"],
[PMID:22810587 "apelin addition decreased cAMP levels in the APJ-HEK cells"],
[PMID:22810587 "Using a β-arrestin/APJ complementation assay, apelin was found to induce a dose-dependent increase in β-arrestin signaling, as expected"],
and binding in native human tissue:
[PMID:28137936 "ELA competed for binding of apelin in human heart with overlap for the 2 peptides indicated by in silico modeling."]
Structures now exist for the complex: [PMID:38428423 "we report cryoelectron microscopy (cryo-EM) structures of APLNR-Gi1 complexes bound to three agonists with divergent signaling profiles"],
and UniProt records `PDB 8XZH; EM; 2.60 A; L=66-77`, i.e. the modelled ligand is apelin-13
minus its first residue.

## 4. The ELABELA/APELA confound — where it does and does not bite

APLNR has a second, unrelated endogenous ligand, ELABELA/Toddler (gene APELA), and several
APLN rows are sourced from papers whose *subject* is ELA. I checked each.

**PMID:28137936 (Yang 2017, Circulation) — four APLN rows. Verdict: legitimate.**
The paper is titled for ELA, but `[Pyr1]apelin-13` is run as a head-to-head comparator in
every assay, so there are genuine apelin measurements:
[PMID:28137936 "Levels of ELA and apelin in healthy human plasma (n=25) were measured by using enzyme immunoassays"] →
[PMID:28137936 "ELA and apelin were detectable in healthy human plasma at 0.34±0.03 nmol/L and 0.26±0.03 nmol/L, respectively"]
(the `GO:0005576` IDA); cAMP inhibition
[PMID:28137936 "completely inhibited forskolin-induced cAMP production in a concentration-dependent manner"]
and β-arrestin
[PMID:28137936 "stimulated β-arrestin recruitment in a concentration-dependent manner"]
(the `GO:0060183` rows); and competition binding in human left ventricle (the `GO:0031704`
IDA). The one thing that does not fit is the evidence code: two of the four rows are coded
**IMP** (`GO:0005179`, `GO:0060183`) and the paper contains no APLN mutant or knockdown —
its apelin data are synthetic-peptide pharmacology. Worth flagging to UniProt, but it does
not change the biology, so these are ACCEPTs.

**PMID:28890073 (Sharma 2017, Dev Cell) — the source of `GO:0060976 coronary vasculature
development`. Verdict: transfers, but with the sign inverted relative to how it reads.**
The human rows are ISS and Ensembl-Compara IEA from mouse Q9R0R4, whose GO:0060976 is IMP
from this paper (confirmed via the GO API on Q9R0R4). The paper's thesis is
*"the ELABELA (ELA)-APJ signaling axis is only required for sinus venosus-derived
progenitors"*. Its apelin data say the opposite of what the transferred term suggests:
[PMID:28890073 "but Apelin KO animals did not phenocopy the coronary defect seen in Apj KOs"],
[PMID:28890073 "In fact, Apelin-deficient hearts displayed a phenotype opposite to that in Apj mutants with an increase in coronary growth so that the heart was fully covered at developmental time points earlier than wild-type controls"],
[PMID:28890073 "The opposing phenotypes in Apln and Ela KOs indicate that these two ligands may have opposing functions vis-a-vis APJ in the context of coronary vessel formation."]
GO:0060976 is an unsigned developmental term used with `involved_in`, and an Apln KO with
*accelerated* coronary coverage is still involvement — so the term survives. What does not
survive is the directional gloss UniProt puts on it,
`Plays a role in early coronary blood vessels formation (By similarity)`
(ECO:0000250|UniProtKB:Q9R0R4). GO has no `regulation of coronary vasculature development`
child to move to (QuickGO search returns only `GO:0060977 coronary vasculature
morphogenesis`, `GO:0060978`, `GO:0060982`, `GO:0003169`, `GO:0003201`), so the honest
action is KEEP_AS_NON_CORE with the sign recorded in the propagation block.

**PMID:26611206 (Perjés 2016, Basic Res Cardiol) — the source of rat `GO:0045823` and rat
`GO:0031704`, which reach human by ISS. Verdict: apelin is present, as the comparator.**
Title and subject are apela/ELA: [PMID:26611206 "We also provide evidence that apela binds to apelin receptors in the heart."]
The apelin content is the benchmark it is measured against:
[PMID:26611206 "just like the fellow receptor agonist apelin, apela increases cardiac contractility and induces coronary vasodilation already in the nanomolar level"].
Abstract-only in the cache, so I cannot see the apelin panel itself; the rat annotation is
a curator's call on the full text and I defer to it. It is still worth noting that the rat
row is coded **IMP** from a paper with no Apln mutant.

**Where the confound is real and already correctly handled:** the gene-level phenotypes.
[PMID:22810587 "In contrast, mice lacking apelin (the endogenous APJ ligand) remain sensitive, suggesting an apelin-independent function of APJ."]
and [PMID:19767528 "differences in the developmental phenotype between apelin and APJ null mice suggest the possibility of undiscovered APJ ligands or ligand-independent effects of APJ"].
Nothing in the GOA record annotates APLN to an APJ-only phenotype, which is the trap this
gene could most easily have fallen into.

## 5. The IBA, and why the family is almost silent

One IBA row: `GO:0005576 extracellular region`, `is_active_in`, GO_REF:0000033,
WITH/FROM `PANTHER:PTN001041490|RGD:620672|UniProtKB:Q9TUI9|UniProtKB:Q9ULZ1`.

The committed PAINT slice resolves it completely — and it is the **only** node-level
annotation in the entire family:

```
family     node           go_id      aspect evidence negated seeds                                          taxon
PTHR15953  PTN001041490   GO:0005576 C      IBD      false   RGD:620672|UniProtKB:Q9TUI9|UniProtKB:Q9ULZ1   taxon:32523
```

- `taxon:32523` is **Tetrapoda** (NCBI Datasets: `"tax_id":32523,"organism_name":"Tetrapoda"`,
  rank CLADE). Human is inside that clade, so the target inherits.
- **Three** gene-level donors, not four: `resolve_withfrom.py` shows `RGD:620672` resolves
  to exactly one hit, Q9R0R3 APEL_RAT — the same entity as the rat Ensembl protein appearing
  on the IEA rows. So the seeds are rat Apln, bovine APLN and human APLN. Rat's own
  `GO:0005576` is **EXP** from PMID:10525157 and bovine's is experimental from PMID:10525157
  and PMID:9792798 (QuickGO), so the node has real experimental grounding on two species.
- Human APLN appears in its own WITH/FROM. This is the expected, valid case: the target's own
  experimental `GO:0005576` annotations are among the descendant evidences the PAINT curator
  used to place the IBD. Not circular, not inflationary.
- No IRD/IKR anywhere in the family slice, and no reason to expect one: the protein has a
  signal peptide, no TM segment, and is measured in plasma, colostrum and conditioned medium.

What is striking is the **incompleteness**. UniProt's own cross-reference says it:
`DR PAN-GO; Q9ULZ1; 1 GO annotation based on evolutionary models.` A family in which the
mature peptide is 97-98.5 % invariant at every position from R66 to F77 across 333 proteins, whose receptor is known, and whose
zebrafish member carries experimental `GO:0007507 heart development` (IMP, PMID:17336905 and
PMID:17336906), `GO:0008078 mesodermal cell migration` (IMP), `GO:0002040 sprouting
angiogenesis` (IGI) and `GO:0048018 receptor ligand activity` (TAS) — that family propagates
nothing but a localisation. `GO:0031704 apelin receptor binding` and `GO:0060183 apelin
receptor signaling pathway` are experimentally attested in human, rat, mouse and zebrafish
and would be obvious IBD candidates. This belongs in the IBA-incompleteness column, and I
have raised it as a question for the PAINT curators.

## 6. Tracing the ISS/IEA chains — the two real defects

All 16 GOA-seeded rows requiring `propagation_review` (IEA ×10, ISS ×5, IBA ×1) — 17 in
the finished review, counting the one `NEW` ISS row — were traced to the
donor's *own* GO record via QuickGO/the GO API, not assumed.

| human row | donor | donor evidence | donor reference | verdict |
|---|---|---|---|---|
| GO:0042756 drinking behavior (ISS, IEA) | Q9R0R3 rat | IMP | PMID:11359874 | supported |
| GO:0045776 neg. reg. blood pressure (ISS, IEA) | Q9R0R3 rat | IMP | PMID:11359874 | **donor citation does not support it** |
| GO:0045823 pos. reg. heart contraction (ISS, IEA) | Q9R0R3 rat | IMP | PMID:26611206 | supported; apela paper, apelin as comparator |
| GO:0060976 coronary vasculature dev. (ISS, IEA) | Q9R0R4 mouse | IMP | PMID:28890073 | **term survives, sign inverted** |
| GO:0060183, GO:1904022 (IEA ×2 each) | Q9R0R3 + Q9R0R4 | IDA | PMID:11359874 | supported |
| GO:0031704 (IEA) | Q9R0R3 + IPR026155 | IDA | PMID:26611206 | supported |
| GO:0005576 (ISS) | Q9TUI9 bovine | experimental | PMID:10525157, PMID:9792798 | supported |
| GO:0005576 (IEA) | SubCell SL-0112/SL-0243 | — | GO_REF:0000044 | supported |
| GO:0005179, GO:0007165 (IEA) | IPR026155 'Apelin' | — | GO_REF:0000002 | see §7 |

**The `GO:0045776` chain is the one clear source-side problem.** Rat Apln's
`GO:0045776 negative regulation of blood pressure` is IMP from PMID:11359874, and that
paper's abstract states the opposite result for its blood-pressure readout:
[PMID:11359874 "central injection of pE13F significantly decreased water intake in dehydrated normotensive rats but did not affect blood pressure"].
The same sentence is the sole support for the drinking-behaviour annotation, which it does
support. The cache is abstract-only, so I cannot exclude a peripheral-route experiment in
the full text — but the paper's stated conclusion is central fluid homeostasis, and its own
blood-pressure result is negative.

The *biology* is nonetheless right, from other work: apelin is a vasodepressor
[PMID:11384769 "mean arterial pressure after the administration of apelin-12, apelin-13, and apelin-36 at a dose of 10 nmol/kg in anaesthetized rats was reduced by 26+/-5, 11+/-4, and 5+/-4 mm Hg, respectively"],
[PMID:11384769 "In the presence of a nitric oxide (NO) synthase inhibitor, the effect of apelin-12 on blood pressure was abolished."],
and in mouse [PMID:22810587 "Apelin infusion significantly decreased systolic blood pressure in WT animals but not in APJ-KO mice"].
So the term stays; the chain, not the claim, is what is weak. Recorded as
`root_cause: SOURCE_WEAK_OR_INFERRED` with `failure_modes: [SOURCE_EVIDENCE_WEAK]`, and put
to UniProt as a question.

A second pattern, not a defect but worth naming: of the four rat/mouse experimental
annotations that feed the human ISS rows, **three are coded IMP from papers that contain no
apelin mutant** (PMID:11359874 and PMID:26611206 are both peptide-infusion pharmacology).
Genuine Apln-null phenotypes do exist and would be better anchors —
[PMID:17673668 "aged Apelin knockout mice developed progressive impairment of cardiac contractility associated with systolic dysfunction in the absence of histological abnormalities"],
[PMID:17673668 "These genetic data show that the endogenous peptide Apelin is crucial to maintain cardiac contractility in pressure overload and aging."],
[PMID:19767528 "Under basal conditions, both apelin and APJ null mice that survived to adulthood manifested modest decrements in contractile function."]
— so `GO:0045823` is the best-supported of the organismal terms even though its current
citation chain is the weakest kind.

## 7. The InterPro2GO rows

`IPR026155` resolves to `'Apelin', type=family, 345 proteins` — a signature that matches
this gene family and essentially nothing else. It maps to two GO terms here:
`GO:0005179 hormone activity` (right, and specific) and `GO:0007165 signal transduction`.
`GO:0007165` is the root-ish signalling term, while `GO:0060183 apelin receptor signaling
pathway` exists, is family-exact, and is already on the gene from three IDAs. A
gene-family-specific signature mapping to the generic term is a granularity loss that the
mapping itself could fix. Same reasoning applies to the legacy ProtInc TAS
`GO:0007165` row from PMID:9792798, whose actual content is
[PMID:9792798 "Synthetic peptides derived from the C-terminal amino acid sequence of bovine preproapelin were capable of specifically promoting the acidification rate in the cells expressing the APJ receptor in a range from 10(-7) to 10(-10) M, indicating that apelin is an endogenous ligand for the APJ receptor."]
— that is apelin receptor signalling, described before the specific term existed.

## 8. The two legacy ProtInc rows that do not survive

**`GO:0007595 lactation` (TAS, PMID:10525157).** The GO definition is *"The regulated
release of milk from the mammary glands and the period of time that a mother lactates to
feed her young."* What the cited paper reports is abundance:
[PMID:10525157 "Although apelin mRNA was widely detected in a variety of tissues, the highest expression of apelin mRNA was detected in the mammary gland of pregnant rats."]
and [PMID:10525157 "a large amount of apelin (14-93 pmol/ml) was found to be secreted in the bovine colostrum, and it was still detectable even in commercial bovine milk"].
Apelin is a *constituent of milk* — a localisation fact already carried by `GO:0005576` —
not a regulator of milk release. No experiment in that paper or since perturbs apelin and
measures milk ejection or milk yield; PubMed searches on apelin with lactation/milk
ejection/oxytocin return nothing on point. This is the expression→process inference GO
explicitly disallows, so: REMOVE.

**`GO:0006955 immune response` (TAS, PMID:10525157).** The evidence is one ex vivo assay,
stated with the authors' own hedge:
[PMID:10525157 "Since apelin partially suppressed cytokine production by mouse spleen cells in response to T cell receptor/CD3 cross-linking, the oral intake of apelin in the colostrum and milk might modulate immune responses in neonates."]
`GO:0006955` is *"Any immune system process that functions in the calibrated response of an
organism to a potential internal or invasive threat"* — apelin is not mounting a response;
it is damping cytokine output. If the row is kept at all it should be
`GO:0001818 negative regulation of cytokine production` (*"Any process that stops, prevents,
or reduces the rate of production of a cytokine"*, verified live on QuickGO, not obsolete).
MODIFY, with the weakness of the underlying experiment stated.

## 9. Core versus non-core: the line I drew

Core, for a peptide hormone precursor, is the molecular act and its immediate pathway:
hormone/receptor-ligand activity, apelin receptor binding, the apelin receptor signalling
pathway (including the β-arrestin-dependent receptor internalisation it drives), and the
extracellular location in which all of that happens. Everything else on this gene —
blood pressure, cardiac contraction, drinking, coronary development, endothelial and smooth
muscle proliferation, the miR-424/503–FGF2 axis — is a physiological consequence, mostly
measured by infusing a synthetic peptide into a rodent. Real, but downstream, so
KEEP_AS_NON_CORE. This is the same line drawn for AGT, and for the same reason: it keeps
`core_functions` about the gene product rather than about the peptide's pharmacology.

The one place this is genuinely arguable is `GO:0045823 positive regulation of heart
contraction`, because apelin is described as
[PMID:28137936 "In heart, apelin is reportedly the most potent inotrope in vitro"]
and because Apln-null mice really do lose contractility with age and overload
(PMID:17673668, PMID:19767528). I still put it non-core: it is an organ-level readout of
APLNR signalling, not a second molecular function.

## 10. The miR-424/503 rows (PMID:23263626), graded

Five rows come from Kim 2013, all in human pulmonary artery endothelial cells with APLN
siRNA and APLN lentiviral overexpression — i.e. perturbation of the gene, IMP/overexpression
grade, whatever the GOA evidence code says.

- `GO:1902895 positive regulation of miRNA transcription` (IDA):
  [PMID:23263626 "We generated a putative miR-424/503 promoter based luciferase reporter construct, which was robustly induced by APLN overexpression in PAECs (Fig."]
  and the loss direction
  [PMID:23263626 "We confirmed via real-time quantitative PCR that both the pri-form and the mature form of miR-424 and miR-503 are significantly downregulated with APLN knockdown (Fig."].
  Both directions present. Apelin is not a transcription factor — this is downstream of
  APLNR — but `involved_in` a regulation term tolerates indirection. Non-core.
- `GO:0010629` and `GO:0040037` (IGI with hsa-miR-424-5p and hsa-miR-503-5p, resolved from
  the RNAcentral ids): [PMID:23263626 "Lastly, we found that APLN knockdown resulted in robust increases of FGF2 and FGFR1, that were abrogated with concurrent overexpression of miR-424 and miR-503 (Fig."].
  The genetic-interaction partners are exactly the two miRNAs, so the IGI is well formed.
  `GO:0010629` is very generic but not wrong. Non-core.
- `GO:1904706 negative regulation of vascular associated smooth muscle cell proliferation`
  (IMP): the effect is indirect, via endothelial conditioned medium —
  [PMID:23263626 "we found that CM from normal PAECs subjected to APLN knockdown induced a significant increase in PASMC proliferation, which was reduced to baseline by concurrent overexpression of miR-424/503 in PAECs (Fig."].
  Non-core, and the indirection is worth stating.
- `GO:1905564 positive regulation of vascular endothelial cell proliferation` (IDA): the sign
  is context-dependent in the same paper —
  [PMID:23263626 "We also found that whereas augmentation of APLN signaling in normal PAECs led to an increase in PAEC proliferation as previously described,9 augmentation of APLN signaling in PAH PAECs had a reverse effect of inhibiting proliferation (Supp."]
  — and the authors themselves discount the literature it rests on:
  [PMID:23263626 "Nevertheless, these effects have been modest at best, and others have refuted such findings,23 suggesting a strong context-dependence for APLN’s effects on the endothelium."]
  Kept, non-core, with the caveat recorded rather than smoothed over.

## 11. What affinage missed

The affinage record is a good map of *mechanism* but it is organised around the modern
signalling/structure literature, and it missed most of what the GOA record actually rests
on. Specifically absent from its 31 citations:

- **Every paper the GOA rows cite** except PMID:38428423 — no PMID:9792798 (the discovery
  paper), no PMID:10525157, no PMID:11359874, no PMID:22810587, no PMID:23263626, no
  PMID:28137936. A review driven by the affinage citation list alone would have had nothing
  to check the existing annotations against.
- **The knockouts.** PMID:17673668 (Kuba, Apelin-null contractility), PMID:19767528 (Charo,
  apelin vs APJ nulls) — the only genetic evidence for apelin's organismal roles.
- **The donor-side papers.** PMID:26611206 and PMID:28890073, which are where two of the
  human ISS chains actually terminate. Finding the `GO:0060976` sign inversion required
  going to the mouse donor's own GO record and reading its citation.
- **The primary ACE2 paper.** It cites the 2005 review (PMID:15907343) for ACE2 cleavage but
  not PMID:11815627, which is where the cleavage-site consensus that makes the Phe77 claim
  checkable comes from; and not PMID:27217402, the in vivo demonstration.
- **The fluid-homeostasis pair.** PMID:15231996 (De Mota) and PMID:11384769 (Tatemoto, the
  blood-pressure paper) — between them the basis for two ISS rows.
- **Processing.** PMID:24251091 (furin/PCSK3 → apelin-13 directly), which is the only
  mechanistic account of how the annotated gene product becomes the assayed peptide.

Its dating column is also unreliable (e.g. PMID:30061698 and PMID:32879139 both listed 2018
against journals of other years), so I used it for leads only and re-verified every claim
against the PMID. Recorded as `relevance: MEDIUM`, `correctness: LOW_QUALITY` on the
`file:` reference — not because the gates tripped (they did not) but because the record is
a lead list whose bibliography does not overlap the record under review.

## 12. Open questions carried into the review

1. Why does PTHR15953 carry one IBD node for a localisation and nothing for the receptor
   binding or the signalling pathway, when those are experimentally attested in four
   species? (question for PAINT)
2. Should a peptide that its own best human measurement calls a paracrine mediator be
   `GO:0005179 hormone activity`, or `GO:0048018`? (question for GO)
3. Rat `GO:0045776` from PMID:11359874: what supports it, given the abstract's negative
   blood-pressure result? (question for UniProt)
4. Would GOA accept annotations against the `PRO_0000001760`–`PRO_0000001763` chain
   identifiers UniProt already defines? Most of this gene's record is about apelin-13 and
   apelin-17, not about the 77-mer. (question for GOA/UniProt)
5. Is apelin-17 worth a UniProt PEPTIDE feature? It has none, yet it is one of the two
   dominant endogenous forms (PMID:15231996) and the form used in most central work.

## 13. Session log

- Read brief, worktree `CLAUDE.md`, `annotation-reviewer` SKILL, `projects/IBA_REVIEW.md`
  propagation taxonomy, `genes/human/AGT/` as the style exemplar.
- Verified accession, term ids/definitions (QuickGO `/ontology/go/terms/<id>/complete` for
  all 19 GOA terms plus candidates; none obsolete, `GO:0048018` carries secondary
  `GO:0071884`, `GO:0031704` carries `GO:0042569`).
- `just fetch-panther-paint PTHR15953` → 1 node, 1 node-level annotation.
- Europe PMC was avoided; all literature search via NCBI E-utilities esearch/esummary, all
  caching via `just fetch-pmid`.
- Eleven extra PMIDs cached and cited: 11384769, 11815627, 15231996, 17673668, 18617693,
  19046574, 19767528, 24251091, 26611206, 27217402, 28890073.
- Bioinformatics: `APLN-bioinformatics/` (3 scripts, `RESULTS.md`).
