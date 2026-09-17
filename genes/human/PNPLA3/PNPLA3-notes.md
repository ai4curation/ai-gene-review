# PNPLA3 (Q9NST1) — curation journal

Human PNPLA3 / adiponutrin / iPLA2-epsilon. Patatin-like phospholipase domain-containing
protein 3; closest paralogue of PNPLA2/ATGL. Single-pass type II membrane protein that
partitions between ER/membranes and the lipid droplet (LD) surface. Catalytic dyad
Ser47 (nucleophile) / Asp166 (proton acceptor) in the PNPLA domain (UniProt Q9NST1).

The common missense variant I148M (rs738409) is the single strongest common genetic risk
factor for steatotic liver disease. Three incompatible mechanistic models are currently in
print, and GOA carries annotations that are traceable to two mutually exclusive
biochemical claims. This file records what each primary source actually reports.

---

## 1. What has actually been measured with purified protein

### TAG lipase / acylglycerol transacylase (Jenkins 2004)
The founding biochemistry. Three iPLA2 family members (adiponutrin/PNPLA3, TTS-2.2, GS2)
expressed in Sf9 cells and affinity purified.
[PMID:15364929 "we demonstrate that each possesses abundant TAG lipase activity"]
[PMID:15364929 "iPLA2epsilon, iPLA2zeta, and iPLA2eta also possess acylglycerol transacylase activity utilizing mono-olein as an acyl donor which, in the presence of mono-olein or diolein acceptors, results in the synthesis of diolein and triolein, respectively."]

Note what the abstract does **not** report: no phospholipase A2 assay result for these three
proteins. The "iPLA2-epsilon"/"phospholipase A2" naming is a family-membership label based on
the dual GXGXXG + GXSXG signature motifs, not a measured PLA2 rate. GOA nevertheless carries
`GO:0004623 A2-type glycerophospholipase activity` IDA from this paper, and UniProt carries
EC 3.1.1.4 with ECO:0000269|PubMed:15364929. Flagged below as a probable name-driven
over-annotation.

### TAG hydrolysis lost in I148M (He 2010)
[PMID:20034933 "In vitro assays using recombinant PNPLA3 partially purified from Sf9 cells confirmed that the wild type enzyme hydrolyzes emulsified triglyceride and that the I148M substitution abolishes this activity."]
[PMID:20034933 "Cell fractionation studies revealed that approximately 90% of wild type PNPLA3 partitioned between membranes and lipid droplets"]

### Substrate scope, and an explicit negative for acyltransferase (Huang 2011)
[PMID:21878620 "Maximal hydrolytic activity of PNPLA3 was observed against the three major glycerolipids, TAG, diacylglycerol, and monoacylglycerol, with a strong preference for oleic acid as the acyl moiety."]
[PMID:21878620 "Purified PNPLA3 also catalyzed the hydrolysis of oleoyl-CoA, but the V(max) was 100-fold lower for oleoyl-CoA than for triolein."]
[PMID:21878620 "The enzyme had little or no hydrolytic activity against the other lipid substrates tested, including phospholipids, cholesteryl ester, and retinyl esters."]
[PMID:21878620 "Neither the wild-type nor mutant enzyme catalyzed transfer of oleic acid from oleoyl-CoA to glycerophosphate, lysophosphatidic acid, or diacylglycerol, suggesting that the enzyme does not promote de novo TAG synthesis."]
Full text, results section heading:
[PMID:21878620 "Purified PNPLA3 has no detectable GPAT, LPAAT, or DGAT activity."]

**Curation problem.** GOA carries `GO:0003841 1-acylglycerol-3-phosphate O-acyltransferase
activity` with evidence code EXP and `PMID:21878620` as the reference, with a plain `enables`
qualifier (no NOT). That paper reports the *opposite*: no detectable LPAAT activity, with
CGI-58 as a positive control. The annotation is traceable to UniProt's EC 2.3.1.51 /
RHEA:19709 catalytic-activity block, which tags both PubMed:21878620 and PubMed:22560221 as
ECO:0000269 evidence; only the latter reports a positive result. Either the annotation should
carry a NOT qualifier or the reference is wrong. Recorded in the review and in
`suggested_questions`; the term itself is kept (see below) because a different paper does
report the activity.

### LPAAT (Kumari 2012)
[PMID:22560221 "Here we show that ADPN promotes cellular lipid synthesis by converting lysophosphatidic acid (LPA) into phosphatidic acid. The ADPN-catalyzed LPA acyltransferase (LPAAT) reaction is specific for LPA and long-chain acyl-CoAs."]
[PMID:22560221 "Notably, the I148M variant of human ADPN exhibits increased LPAAT activity leading to increased cellular lipid accumulation."]

So two groups, using purified/immunoisolated protein, reach opposite conclusions on the same
reaction, and they also disagree on the *direction* of the I148M effect (Huang/He: loss of
hydrolase; Kumari: gain of acyltransferase). A protein cannot be the physiologically relevant
catalyst of both the hydrolysis and the synthesis of the same acyl linkage; at most one of
these is the reaction that matters in vivo. GOA currently carries both, which is why the
lipase and acyltransferase branches are adjudicated differently below rather than all
accepted at face value.

### Acyl-chain remodelling (Ruhanen 2014)
[PMID:24511104 "This study reveals a function of PNPLA3 in FA-selective TAG remodeling, resulting in increased TAG saturation."]
A cell-based readout that is compatible with either a lipase or a transacylase mechanism; it
constrains the *net* metabolic effect rather than the elementary reaction.

### Lipid droplet targeting (Chamoun 2013)
[PMID:23398201 "We demonstrate that PNPLA3 is targetted to LDs in a process that requires an intact Brummer box domain"]
[PMID:23398201 "We show that increased levels of the NAFLD-linked PNPLA3 isoform leads to larger LDs, whereas decreased levels of PNPLA3 had the opposite effect."]

---

## 2. The three current models of I148M

### (a) Loss-of-function: PNPLA3 is a PUFA-selective TG lipase feeding VLDL
Johnson et al. 2024, Nat Commun.
[PMID:38844467 "we show that PNPLA3 preferentially hydrolyzes polyunsaturated triglycerides, mobilizing polyunsaturated fatty acids for phospholipid desaturation and enhancing hepatic secretion of triglyceride-rich lipoproteins."]
This paper explicitly frames the open question:
[PMID:38844467 "Recent evidence indicates that the I148M mutant functions as an inhibitor of PNPLA2/ATGL-mediated lipolysis, leaving the role of wild-type PNPLA3 undefined."]

### (b) Gain-of-function: 148M sequesters ABHD5/CGI-58 away from ATGL
Wang et al. 2025, J Hepatol.
[PMID:39550037 "ABHD5 interacted preferentially with PNPLA3 relative to ATGL in cultured hepatocytes."]
[PMID:39550037 "luciferase reconstitution assays were used in cultured hepatocytes to show that ABHD5 binds preferentially to PNPLA3 over ATGL"]
[PMID:39550037 "These findings support the premise that PNPLA3(148M) is a gain-of-function mutation that promotes hepatic steatosis by accumulating on lipid droplets and inhibiting ATGL-mediated lipolysis in an ABHD5-dependent manner."]
[PMID:39550037 "Although the substitution of methionine for isoleucine reduces the TG hydrolase activity of PNPLA3, the loss of enzymatic function is not directly related to the steatotic effect of the variant."]

Crucially, the *same* paper is the first to show that PNPLA3's own lipase activity is
ABHD5-stimulated, i.e. it does not deny that PNPLA3 is a lipase:
[PMID:39550037 "Addition of ABHD5 increased the TG hydrolase activity of both forms of PNPLA3"]
[PMID:39550037 "We concluded from these experiments that PNPLA3, as well as ATGL, is activated by ABHD5 and that this effect occurs in the absence of other proteins."]

The genetic argument against pure LOF, from the same discussion: Pnpla3-/- mice do not
develop steatosis even on high-carbohydrate diets, whereas 148M knock-in mice do, and a
catalytically dead S47A knock-in phenocopies 148M only when the protein is expressed.

### (c) Neomorph: 148M blocks both lipolysis and VLDL/ApoB secretion
Sherman et al. 2025, Cell Rep (abstract only in cache).
[PMID:41046517 "we find that the variant impairs cellular secretion of apolipoprotein B (ApoB), the scaffolding protein of very-low-density lipoprotein (VLDL). This is not due to loss-of-function of wild-type PNPLA3."]
[PMID:41046517 "We propose that I148M is a neomorph that exacerbates fatty liver risk by simultaneously impeding two major CGI-58-dependent pathways for liver triglyceride clearance: lipolysis and secretion."]

### Supporting mechanism: LD targeting is required for the ABHD5 interaction
Teskey et al. 2025, J Biol Chem.
[PMID:39814233 "PNPLA3 148M functions to sequester ABHD5 and prevent coactivation of PNPLA2, which has implications for initiating MASLD"]
[PMID:39814233 "Here, we demonstrate that LD targeting of both ABHD5 and PNPLA3 I148M is required for the interaction."]

### The field acknowledges the conflict
Mikaeeli & Cohen 2025, J Hepatol, is a dedicated editorial titled "Loss or gain of function:
The functional complexity of the PNPLA3 I148M variant" (PMID:39892821). PubMed holds no
abstract for it, so it is cited as evidence that the dispute is recognised rather than quoted.

---

## 3. Position taken in this review

**Is PNPLA3's physiological molecular function catalytic at all?** The honest answer is that
it is *both* catalytic and non-catalytic, and the non-catalytic arm is the one that carries
the disease signal.

1. **Triacylglycerol lipase activity (GO:0004806) is real and is kept as a core molecular
   function.** Four independent groups measured TG hydrolysis with purified protein
   (Jenkins 2004, He 2010, Huang 2011, Wang 2025), it is ABHD5-stimulated like ATGL's, and
   Johnson 2024 gives it a substrate preference (polyunsaturated TG) and an in vivo readout.
   What is disputed is not the activity but its quantitative importance: Pnpla3-null mice
   have no hepatic phenotype, so the lipase is dispensable in mouse liver under standard
   conditions.

2. **The ABHD5-competition arm is not represented in GOA at all, and it should be.** All
   three 2024-25 models converge on ABHD5/CGI-58 as the node. Wang 2025 shows WT PNPLA3 —
   not only 148M — binds ABHD5 preferentially over ATGL and competes with ATGL for it; 148M
   differs by escaping degradation and accumulating ~40x on LDs, so the same molecular
   activity is simply present in much greater amount. The molecular function is therefore
   sequestration of a lipase co-activator, i.e. inhibition of ATGL. The nearest existing MF
   terms are `GO:0055102 lipase inhibitor activity` and `GO:0140311 protein sequestering
   activity`; neither captures "sequesters the co-activator of a lipase", so a new term is
   proposed. Downstream BP: `GO:0010897 negative regulation of triglyceride catabolic
   process`.

3. **The acyltransferase branch is demoted, not deleted.** `GO:0003841`,
   `GO:0042171` and `GO:0016411` rest on Kumari 2012 (plus Reactome TAS) and are directly
   contradicted by Huang 2011 with an appropriate positive control. Marked
   `MARK_AS_OVER_ANNOTATED` throughout, with the PMID:21878620 provenance error called out.
   The transacylation terms `GO:0051264`/`GO:0051265` are different: those are the CoA-*in*dependent
   mono-olein/diolein transacylase reactions that Jenkins 2004 did measure directly, so they
   are kept as non-core rather than flagged.

4. **A2-type glycerophospholipase (GO:0004623) is marked over-annotated.** It is a
   family-name inference; Huang 2011 tested phospholipids and found little or no activity.

5. **Rodent-orthology BP transfers** (`GO:0009744` response to sucrose, `GO:0032869` cellular
   response to insulin stimulus, `GO:0050872` white fat cell differentiation, `GO:1905243`
   response to T3) describe transcriptional regulation *of* PNPLA3 by nutritional state, not
   processes PNPLA3 carries out. UniProt records the same:
   "By changes in energy balance: down-regulated following very low-calorie diet, whereas
   refeeding elevates the mRNA level" (Q9NST1 INDUCTION). Demoted to non-core.

## 4. Open questions carried into the review
- Which reaction is physiological: TG hydrolysis or LPA acylation? Are the two labs' assays
  measuring the same protein preparation quality / detergent state?
- Is the GOA `GO:0003841` EXP annotation citing PMID:21878620 a missing NOT qualifier, or a
  wrong reference?
- Does WT PNPLA3 at physiological abundance measurably restrain ATGL, or only the
  overaccumulated 148M protein? (Determines whether the inhibitor MF belongs to the gene at
  all, or only to the variant.)
- Reconciling Johnson 2024 (Pnpla3 KO → steatosis, reduced VLDL-TG) with Hobbs/Cohen
  (Pnpla3 KO → no phenotype).
