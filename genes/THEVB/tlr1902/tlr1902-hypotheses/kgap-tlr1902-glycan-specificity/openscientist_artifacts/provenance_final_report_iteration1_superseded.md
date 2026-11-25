# Tlr1902 (Q8DHP3) glycan specificity: hypothesis evaluation for AI Gene Review

Gene: tlr1902, Thermosynechococcus vestitus BP-1 (NCBITaxon:197221), UniProt Q8DHP3
Hypothesis slug: kgap-tlr1902-glycan-specificity
Date: 2026-11-25

## Executive judgment

**Partially supported, with a split verdict between molecular function and biological process.**

The catalytic half of the seed hypothesis is supported. Tlr1902 is a family GH10
glycoside hydrolase with both catalytic glutamates present, a -1 subsite that is
conserved residue-for-residue with crystallised xylanases, and catalytic
carboxylate geometry indistinguishable from retaining GH10 crystal structures.
On architecture alone, xylan is the substrate class the cleft favours. Confidence
in the family assignment is high; confidence in xylan over other beta-glycans is
moderate, because GH10 cleft geometry is not by itself a discriminator (the
closest-matching reference, Cellulomonas fimi Cex, is a GH10 that acts on both
xylan and cellulose-derived substrates).

The pathway half of the hypothesis refutes the current biological process
annotation. Tlr1902 has no signal peptide and no carbohydrate-binding module,
while every characterised GH10 xylanase is a secreted, often modular enzyme. The
genome encodes 1 of 7 xylan utilisation steps and no route at all for xylose
catabolism or uptake. The gene is not in a polysaccharide utilisation locus and
is not co-expressed with its neighbours. Public RNA-seq shows modest, unregulated
expression.

So the final position on the seed question: yes, a cyanobacterium with no access
to plant cell wall polysaccharides and no xylose catabolism makes an endogenous
or non-nutritional substrate the more likely explanation. **GO:0031176
endo-1,4-beta-xylanase activity should be retained but marked as IEA-only and
in vitro in scope; GO:0045493 xylan catabolic process should be removed or
downgraded, because the organism cannot complete that process.** A cellular
component lead of cytoplasm is supportable from the absence of export signals.

Most important caveats. No cyanobacterial GH10 has ever been experimentally
characterised, so there is no close functional anchor. The AlphaFold model is an
apo prediction, so cleft measurements carry prediction error even at pLDDT 97.4.
The signal peptide call is from hydropathy plus the absence of a UniProt SIGNAL
feature, not from a run of SignalP 6.0, which could not be executed here.

## Evidence matrix

| Citation | Evidence type | Stance | Claim tested | Key finding | Context | Confidence / limitations |
|---|---|---|---|---|---|---|
| This work, computational (UniProt Q8DHP3, PROSITE PS51760) | Computational | Supports | Can a GH family be assigned and are both catalytic residues present? | GH10 domain 60-329; acid/base E166 in INEF**DVNNE**M, nucleophile E264 in NLPLK**ITEV** | Sequence, 385 aa | High. Rule-based domain call, but motif contexts are canonical |
| This work, computational (AlphaFold AF-Q8DHP3-F1 v6) | Structural, computational | Supports | Is the active site intact and of retaining geometry? | mean pLDDT 97.4; E166 CD to E264 CD 6.96 A, closest O-O 5.37 A vs 7.15/5.62 A in 2EXO and 6.93/5.23 A in 1E0V | Predicted apo monomer | High for fold, moderate for exact distances (apo prediction) |
| This work, computational (NW alignment, BLOSUM62) | Structural/evolutionary | Supports | Does the cleft match xylan-active GH10s? | 29 cleft residues 58.6-65.5% identical vs 29.5-30.4% global; Fisher one-sided p = 3.1e-5, 3.9e-5, 9.2e-4. Conserved -1 set K84, H117, W121, N165, E166, N201, D202, Y203, Q234, H236, E264, W298, W306 | vs P07986 Cex, P26514 XlnA, P14768 Xyn10A | High that the site is functional; moderate that it is xylan-specific |
| PMID 14670951 | Direct assay + structure | Qualifies | Does GH10 cleft variation change the catalytic profile? | CjXyn10C "hydrolyzes xylan at a rate similar to other previously described GH10 enzymes but displays very low activity against xylooligosaccharides"; subsite polymorphisms change chain-length preference while the enzyme stays a xylanase | Cellvibrio japonicus, 1.85 A structure | High. Shows cleft comparison predicts profile, not substrate class, within GH10 |
| This work, computational (KEGG orthology over genome tel) | Computational, pathway context | Refutes the BP term | Does the genome encode a xylan or xylose utilisation pathway? | K01181 present (tlr1902 only). Absent: K01198, K15921, K01811, K01209, K01051, K01805, K00854, K17743, K05351, K10439, K10543, K01179, K01225 | 2524-gene genome | High. KEGG KO coverage can miss divergent orthologues |
| This work, computational (KEGG positional neighbourhood) | Computational | Refutes gene-cluster claim | Is tlr1902 in a relevant cluster? | Flanked by crtR (carotenoid), two ABC ATPases and hypotheticals; no solute-binding protein, permease, sugar kinase or regulator | 1986642-1993668 | High |
| This work, GEO GSE94125 (20 RNA-seq samples) | Dataset reanalysis | Qualifies / weakly refutes | Is tlr1902 transcriptionally regulated? | Expression 5.24 log2, 39th percentile; co-culture vs axenic log2FC +0.36, raw p 0.005, BH FDR q 0.366; neighbour correlations r = -0.33 to -0.14, all p > 0.15 | T. vestitus BP-1 axenic vs Meiothermus ruber co-culture | Moderate. n=10 vs 10, no carbohydrate-supplementation condition tested |
| This work, computational (hydropathy + UniProt features) | Localization, computational | Refutes the BP term | Can Tlr1902 reach extracellular xylan? | Q8DHP3 max 19-residue KD hydropathy 0.87 at residue 285, no SIGNAL/TRANSMEM feature. Cex SIGNAL 1..41 (1.52 at 27), XlnA SIGNAL 1..41 (2.58 at 17), Xyn10A SIGNAL 1..26 (1.56 at 8) | Sequence comparison | Moderate-high. SignalP 6.0 not run; a non-classical export route is not formally excluded |
| This work, computational (AlphaFold contacts and PAE) | Structural | Qualifies | Is there a carbohydrate-binding module? | Discontinuous beta-sandwich from residues 1-58 + 330-385 (164 CA-CA contacts under 8 A between segments vs 13 to the barrel; intra-domain PAE 3.9 A), centroid 34.4 A from the catalytic centre, all 10 aromatics buried (147-225 neighbours within 10 A) | Predicted structure | Moderate. Burial metric is crude; a low-affinity surface site is not excluded |
| This work, computational (UniProtKB PF00331 census) | Evolutionary | Qualifies | Is GH10 a core cyanobacterial function? | 136 of 18,880 PF00331 proteins are cyanobacterial, from 96 organisms in 56 genera against 4,477 cyanobacterial proteomes (~2%); 0 in Swiss-Prot; conserved at 385 aa in T. sichuanensis E542 (A0A3B7MDL9) | UniProtKB, Nov 2026 | High for the counts; proteome counts are redundancy-inflated |
| PMID 41161445 | Direct assay + crystal structure | Competing / orienting | Is tlr1902 the characterised T. elongatus glucosidase? | TeGH116 is "the one beta-glucosidase in this model cyanobacterium", hydrolyses pNP-beta-D-glucopyranoside, phenolic glucosides and beta-1,3/beta-1,4-gluco-oligosaccharides | T. elongatus BP-1, recombinant | High. TeGH116 is tll1043 (KEGG K05349), a different gene; do not conflate |
| PMID 37552253 | Direct assay, composition | Competing hypothesis | Does a cyanobacterium make a xylose-containing polysaccharide? | "Levels of individual monosaccharides correlated with specific culture media components, e.g. xylose with sulfur"; data suggest "a protective role for xylose-rich EPS" | Synechocystis sp. PCC 6803 EPS | Moderate. Different species; EPS xylose is in a heteropolymer, not beta-1,4-xylan |
| PMID 12240834 | Database/genome | Orienting | Source of the annotation | Complete genome of T. elongatus BP-1; tlr1902 called "probable endo-1,4-beta-xylanase" by similarity at genome-annotation time | Genome paper | High that this is the origin of the call; it is a prediction, not an assay |

## GO curation implications

All leads below require curator verification.

| GO term | Aspect | Current basis | Lead |
|---|---|---|---|
| GO:0031176 endo-1,4-beta-xylanase activity | MF | IEA, UniProtKB-UniRule / RuleBase RU361174, PROSITE PRU01096 | **Retain, do not promote.** Structurally well supported at the level of catalytic competence. Keep IEA. Add a review note that no cyanobacterial GH10 has been assayed and that the xylan-versus-other-beta-glycan call rests on cleft comparison only. |
| GO:0016798 hydrolase activity, acting on glycosyl bonds, or GO:0004553 hydrolase activity, hydrolyzing O-glycosyl compounds | MF | not currently used | **Candidate generalisation.** If the curator judges GO:0031176 too specific for an uncharacterised cyanobacterial GH10, GO:0004553 is the defensible parent. Prefer this over removing the MF entirely. |
| GO:0045493 xylan catabolic process | BP | IEA, PROSITE PRU01096 pathway rule | **Remove, or mark as not supported.** The genome encodes 1 of 7 steps, no xylose catabolism and no xylose uptake. The gene product cannot complete or contribute to this process in this organism. This is the clearest curation action. |
| GO:0005975 carbohydrate metabolic process | BP | not currently used | **Candidate replacement** for GO:0045493 if a BP term is wanted. Broad, but it is the level the evidence actually reaches. |
| GO:0005737 cytoplasm | CC | not currently used | **Candidate new term, ISS/IC lead.** No signal peptide, no TM segment, no CBM, unlike all characterised secreted GH10 xylanases. Weak on its own; worth raising because it is what makes the BP term untenable. |
| GO:0005576 extracellular region | CC | not currently used | **Do not add.** No export signal was found. |

Non-core assessment: an endo-xylanase activity is a plausible in vitro property of
this protein but is unlikely to be its core cellular function in an obligate
photoautotroph with no xylan access and no xylose metabolism.

## Mechanistic scope

Direct gene-product activity being tested: hydrolysis of a beta-glycosidic bond
by a retaining, double-displacement GH10 mechanism using E166 as general
acid/base and E264 as nucleophile, with the glycone bound in a -1 subsite formed
by K84, H117, W121, N165, N201, D202, Y203, Q234, H236, W298 and W306.

Everything else in the annotation is inference at a further remove. "Xylan
catabolic process" is a pathway-level claim that requires downstream
beta-xylosidase, xylose transport and xylose catabolism, none of which exist in
this genome. "Xylan degradation" as a UniProt PATHWAY statement is transferred
from the PROSITE GH10 rule and carries no organism-specific evidence. No
phenotype, no localization experiment and no interaction data exist for tlr1902.

## Conflicts and alternatives

1. **Database carry-over is the dominant signal.** Every piece of functional
   annotation on Q8DHP3 traces to one rule chain: PROSITE PRU01096 and RuleBase
   RU361174 assign EC 3.2.1.8, GO:0031176, GO:0045493 and the xylan degradation
   pathway to anything with a GH10 domain. The KEGG call K01181 and the original
   genome annotation (PMID 12240834) are the same inference, made independently.
   Four agreeing sources here are one piece of evidence, not four.

2. **Name confusion with TeGH116.** PMID 41161445 characterises "the one
   beta-glucosidase in this model cyanobacterium" from T. elongatus BP-1. That is
   tll1043 (KEGG K05349, GH116), a different gene. A curator searching the
   literature for "Thermosynechococcus elongatus glycoside hydrolase" will hit
   this paper first; it must not be cited as evidence for tlr1902.

3. **GH10 is not strictly a xylanase family.** Cellulomonas fimi Cex, the
   reference whose cleft matches Q8DHP3 most closely (65.5% cleft identity), is a
   GH10 that acts on both xylan and cellulose-derived substrates. PMID 14670951
   shows that cleft polymorphism within GH10 changes chain-length preference
   substantially. Cleft comparison therefore cannot rule out a beta-glucan or
   mixed-linkage glucan substrate for tlr1902.

4. **Endogenous substrate alternatives.** T. vestitus BP-1 encodes two
   cellulose-synthase-like genes (tll0007, tlr1795) and about 20 glycosyl
   transferases, so it makes its own beta-glycans. Cyanobacterial EPS routinely
   contains xylose (PMID 37552253 in Synechocystis). A role in remodelling or
   turning over self-made extracellular or periplasmic polysaccharide is a
   competing explanation that the available data neither confirm nor exclude.
   Against it: no export signal was found.

5. **A sugar-independent role is possible.** GH10 folds have been repurposed. A
   non-hydrolytic or regulatory function cannot be excluded for a gene retained
   at identical length across the genus but absent from 98% of cyanobacteria.

## Knowledge gaps

| Gap | What was checked | Why it matters | What would resolve it |
|---|---|---|---|
| No enzyme assay on Tlr1902 or any cyanobacterial GH10 | PubMed searches for cyanobacterial GH10/xylanase returned nothing; 0 of 136 cyanobacterial PF00331 entries are in Swiss-Prot | The entire MF annotation is predicted. An experimental ECO code is unattainable today | Recombinant expression and a substrate panel (see below) |
| Subcellular location is predicted, not measured | UniProt has no SIGNAL/TRANSMEM; hydropathy max 0.87. SignalP 6.0 and TatP could not be run in this environment | This is the load-bearing argument against GO:0045493 | Run SignalP 6.0 and TatFind; confirm with cell-fractionation Western or a GFP fusion |
| Xylose catabolism absence rests on KEGG KO coverage | 13 KOs queried, 11 absent, 2 present | A divergent, unannotated xylose isomerase or xylosidase would change the pathway argument | HMM search of the proteome with Pfam PF01261, PF00294, PF04616, PF07745 |
| Accessory beta-sandwich (1-58 + 330-385) function unknown | Contacts, PAE and aromatic burial computed; KEGG lists it as CarboxypepD_reg-like | If it is a CBM, the enzyme targets a specific polymer and the substrate question narrows | DALI or Foldseek search of the isolated domain against the CBM structure set; affinity gel electrophoresis against xylan, cellulose and self-EPS |
| No transcriptomic condition tests carbohydrate availability | 5 GEO series found; only GSE94125 has a processed matrix, covering light, oxygen and co-culture. GSE70086 (hot/cold stress) has no deposited count table | Substrate-responsive induction would be the cheapest in vivo clue | Reanalyse GSE70086 from raw SRA; or run RNA-seq with xylan, xylose and cellobiose supplementation |
| The T. vestitus BP-1 EPS and sheath sugar composition is unknown | Only cross-species EPS data found (PMID 37552253, Synechocystis) | Determines whether an endogenous xylose-containing polymer exists at all in this organism | Acid hydrolysis plus GC-MS or HPAEC-PAD monosaccharide analysis of BP-1 EPS and cell wall |

## Discriminating tests

Ranked by information per unit effort.

1. **Substrate panel on recombinant Tlr1902.** Express Q8DHP3 in E. coli (it is
   thermostable, so heat purification works as it did for TeGH116). Assay against
   beech/birch glucuronoxylan, wheat arabinoxylan, carboxymethylcellulose,
   barley beta-glucan, lichenan, laminarin, and purified BP-1 EPS. This single
   experiment settles xylan versus beta-glucan versus endogenous polymer and
   would convert GO:0031176 from IEA to a direct-assay code. Include the E166A
   and E264A mutants as controls.
2. **Localization.** SignalP 6.0 and TatFind on the sequence first (free,
   immediate). Then cell fractionation of BP-1 into cytoplasm, periplasm and
   extracellular medium with an anti-Tlr1902 Western. A cytoplasmic result
   finalises the removal of GO:0045493.
3. **Foldseek or DALI on the isolated accessory domain** (residues 1-58 joined to
   330-385 from the AlphaFold model) against the PDB and the CBM families. Cheap,
   and the single most likely source of a substrate-targeting clue.
4. **Growth and knockout.** Delete tlr1902 in BP-1 and compare EPS yield,
   monosaccharide composition, sheath morphology and flocculation against wild
   type. Tests the endogenous-substrate alternative directly.
5. **HMM sweep of the BP-1 proteome** for divergent xylosidase, xylose isomerase
   and xylulokinase. Confirms or breaks the pathway-incompleteness argument.
6. **Reanalyse GSE70086 from raw reads** and any xylan-supplementation dataset.
   Low cost; would show whether the gene responds to any carbohydrate cue.

## Curation leads

All items below are leads for a curator to verify, not finished curation.

**Action changes**
- Change the action on GO:0045493 (xylan catabolic process) to removal, with the
  rationale that the genome encodes 1 of 7 xylan utilisation steps, no xylose
  catabolism (K01805, K00854 absent), no xylose uptake (K10439, K10543 absent),
  and that the protein has no export signal.
- Keep GO:0031176 (endo-1,4-beta-xylanase activity) at IEA. Add a note that the
  assignment is rule-propagated and that the structural evidence supports
  catalytic competence of a GH10 site, not an in vivo xylanolytic role.
- Consider GO:0004553 as a generalisation lead if the curator prefers not to
  assert xylan specificity for an uncharacterised cyanobacterial GH10.
- Consider adding GO:0005737 (cytoplasm) as a low-confidence lead, flagged as
  requiring SignalP 6.0 confirmation.

**Candidate references, with exact snippets to verify**
- PMID 41161445, Beagbandee et al. 2025. Snippet to verify: "We describe the
  functional and structural characterization of Thermosynechococcus elongatus
  BP-1 TeGH116, the one beta-glucosidase in this model cyanobacterium." Use only
  as a disambiguation note: TeGH116 is tll1043 (GH116), not tlr1902 (GH10).
- PMID 14670951, Pell et al. 2004. Snippet to verify: "Comparison of CjXyn10C
  with other family GH10 enzymes reveals "polymorphisms" in the substrate binding
  cleft". Supports the caveat that within-GH10 cleft comparison predicts catalytic
  profile but does not cleanly separate substrate classes.
- PMID 37552253, Madsen et al. 2023. Snippet to verify: "Comparison with RNA
  sequencing data suggests a Wzy-dependent biosynthetic pathway and a protective
  role for xylose-rich EPS." Supports the endogenous-substrate alternative, in a
  different cyanobacterium.
- PMID 12240834, Nakamura et al. 2002. The genome paper; the origin of the
  "probable endo-1,4-beta-xylanase" call. Cite as database-level, not evidence.

**Suggested questions for the review**
- Is there any evidence that T. vestitus BP-1 encounters, imports or metabolises
  xylose or any xylan-derived sugar? (Answer from this analysis: no.)
- Does Tlr1902 carry a Sec or Tat signal? (Not found here; needs SignalP 6.0.)
- Is the N/C-terminal beta-sandwich a carbohydrate-binding module?
- Should a GH10 domain alone license a BP pathway term when the pathway is absent
  from the genome? This case is a good template for a general rule.

**Suggested experiments**
See Discriminating tests, items 1-4.

## Supported and refuted parts of the seed hypothesis

| Seed claim | Verdict |
|---|---|
| Family can be assigned from sequence and structure | Supported: GH10, high confidence |
| Both catalytic acid/base and nucleophile are present | Supported: E166 and E264, canonical motifs and geometry |
| Cleft comparison with structurally characterised GH10s is informative | Supported: cleft 58.6-65.5% identical vs 29.5-30.4% global, Fisher p < 1e-3 |
| Cleft geometry favours xylan | Partially supported: the -1 subsite is the xylanase set, but the closest reference (Cex) is dual-specificity, so beta-glucan is not excluded |
| Genome encodes the rest of a xylan utilisation pathway | Refuted: 1 of 7 steps, no xylose catabolism or uptake |
| tlr1902 sits in a relevant gene cluster | Refuted: flanked by crtR, two ABC ATPases and hypotheticals; no co-expression with neighbours |
| Public transcriptomic evidence of regulation | Weakly negative: expressed at the 39th percentile, co-culture log2FC +0.36 with FDR q = 0.37 |
| An endogenous substrate is the more likely explanation | Supported, by elimination rather than by positive evidence |

## Limitations

The structural work is entirely on an AlphaFold apo prediction and sequence
alignments I computed here; no new experiment was performed. Pairwise global
Needleman-Wunsch handled the multi-domain XynZ (P26222) poorly (14% cleft
identity, an alignment artefact), so that reference was excluded from the
conclusions. The signal-peptide call uses hydropathy and the absence of a UniProt
feature because SignalP could not be run in this environment. KEGG orthology
coverage can miss divergent enzymes, so "pathway absent" is a strong inference
rather than proof. GSE94125 has 10 samples per arm and no carbohydrate
manipulation, so it cannot exclude substrate-responsive regulation under
untested conditions.
