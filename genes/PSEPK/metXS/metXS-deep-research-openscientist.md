---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-11T16:19:41.793704'
end_time: '2026-07-11T16:39:05.872831'
duration_seconds: 1164.08
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: PSEPK
  gene_id: metXS
  gene_symbol: metXS
  uniprot_accession: Q88CT3
  protein_description: 'RecName: Full=Homoserine O-succinyltransferase {ECO:0000255|HAMAP-Rule:MF_00296};
    Short=HST {ECO:0000255|HAMAP-Rule:MF_00296, ECO:0000303|PubMed:28581482}; EC=2.3.1.46
    {ECO:0000255|HAMAP-Rule:MF_00296, ECO:0000269|PubMed:28581482}; AltName: Full=Homoserine
    transsuccinylase {ECO:0000255|HAMAP-Rule:MF_00296}; Short=HTS {ECO:0000255|HAMAP-Rule:MF_00296};'
  gene_info: Name=metXS {ECO:0000255|HAMAP-Rule:MF_00296, ECO:0000303|PubMed:28581482};
    OrderedLocusNames=PP_5097;
  organism_full: Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB
    11950 / KT2440).
  protein_family: Belongs to the AB hydrolase superfamily. MetX family.
  protein_domains: AB_hydrolase_1. (IPR000073); AB_hydrolase_fold. (IPR029058); HAT_MetX-like.
    (IPR008220); Abhydrolase_1 (PF00561)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 3
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: metXS-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: metXS-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** Q88CT3
- **Protein Description:** RecName: Full=Homoserine O-succinyltransferase {ECO:0000255|HAMAP-Rule:MF_00296}; Short=HST {ECO:0000255|HAMAP-Rule:MF_00296, ECO:0000303|PubMed:28581482}; EC=2.3.1.46 {ECO:0000255|HAMAP-Rule:MF_00296, ECO:0000269|PubMed:28581482}; AltName: Full=Homoserine transsuccinylase {ECO:0000255|HAMAP-Rule:MF_00296}; Short=HTS {ECO:0000255|HAMAP-Rule:MF_00296};
- **Gene Information:** Name=metXS {ECO:0000255|HAMAP-Rule:MF_00296, ECO:0000303|PubMed:28581482}; OrderedLocusNames=PP_5097;
- **Organism (full):** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
- **Protein Family:** Belongs to the AB hydrolase superfamily. MetX family.
- **Key Domains:** AB_hydrolase_1. (IPR000073); AB_hydrolase_fold. (IPR029058); HAT_MetX-like. (IPR008220); Abhydrolase_1 (PF00561)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "metXS" matches the protein description above**
2. **Verify the organism is correct:** Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'metXS' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **metXS** (gene ID: metXS, UniProt: Q88CT3) in PSEPK.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: metXS (Q88CT3) in *Pseudomonas putida* KT2440

**Gene:** metXS · **Ordered locus:** PP_5097 · **UniProt:** Q88CT3
**Enzyme:** Homoserine O-succinyltransferase (HST/HTS) · **EC 2.3.1.46**
**Organism:** *Pseudomonas putida* (strain ATCC 47054 / DSM 6125 / KT2440)
**Family:** AB hydrolase superfamily, MetX family (Pfam PF00561 Abhydrolase_1; InterPro IPR008220 HAT_MetX-like, IPR029058 AB_hydrolase_fold)

---

## 1. Summary (answer to the research question)

metXS (PP_5097) encodes a **homoserine O-succinyltransferase**, a cytoplasmic acyl-CoA–dependent
acyltransferase of the MetX (α/β-hydrolase) family. Its primary function is to catalyze the **first
committed step of the transsulfuration branch of L-methionine biosynthesis**:

> **succinyl-CoA + L-homoserine → CoA + O-succinyl-L-homoserine**  (EC 2.3.1.46)

Critically, although MetX enzymes are historically assumed to be *acetyl*-transferases, the substrate
specificity of this protein was **experimentally determined to be succinyl-CoA**, which is why UniProt
names it *metXS* (the "S" = succinyl) rather than metX/metXA (Bastard et al. 2017, PMID 28581482). The
enzyme acts in the cytoplasm and its activity in *Pseudomonas* is modulated by the partner protein MetW
and feedback-inhibited by S-adenosylhomocysteine.

---

## 2. Primary function: reaction catalyzed and substrate specificity

**Reaction.** The enzyme transfers the succinyl moiety from succinyl-CoA onto the γ-hydroxyl of
L-homoserine, producing **O-succinyl-L-homoserine** and free CoA. This is the entry reaction that
diverts L-homoserine (a branch-point intermediate of the aspartate pathway) away from threonine/
isoleucine biosynthesis and into methionine biosynthesis.

**Substrate specificity — the central annotation issue.** MetA and MetX are two phylogenetically
unrelated families of acyl-L-homoserine transferases. Members are "prone to incorrect annotation
because MetX and MetA enzymes are assumed to always use acetyl-CoA and succinyl-CoA, respectively"
(Bastard et al. 2017, PMID 28581482). By assaying **100 enzymes** and combining the results with
structural active-site classification, that study showed >60% of the ~10,000 database sequences in
these families are mis-annotated, and it explicitly resolved the acyl-donor preference for individual
proteins. On this basis *P. putida* PP_5097 is classified as a genuine **succinyl**transferase (metXS,
EC 2.3.1.46) — a determination carried in UniProt with experimental evidence
(ECO:0000269|PubMed:28581482). The study further inferred that acetyl-CoA was the ancestral substrate
and that exclusive succinyl-CoA usage arose in more recently derived bacteria.

The related MetX literature confirms that acyl-donor and acyl-acceptor specificity (succinyl vs
acetyl; homoserine vs serine) is dictated by residues lining the substrate-binding pocket, not by the
invariant catalytic machinery. In *M. tuberculosis* homoserine acetyltransferase, single substitutions
reprogrammed specificity — e.g. Leu322→Arg switched the enzyme toward **succinylation**, and Ala59Gly/
Gly62Pro created a serine-acetyltransferase-like activity (Maurya et al. 2021, PMID 34090964). This
establishes the molecular logic by which a MetXS such as PP_5097 achieves succinyl selectivity.

## 3. Catalytic mechanism and structure

The MetX/homoserine-transacylase fold is well characterized by crystallography of family members
(*Haemophilus influenzae*, PMID 16313180; *Leptospira interrogans*, PMID 17927957):

- **Two-domain architecture:** a core **α/β-hydrolase domain** carrying the catalytic site, plus a
  **helical "lid" domain**.
- **Catalytic triad Ser–Asp–His** (e.g. Ser143/Asp304/His337 in *H. influenzae*), housed at the end of
  a **deep tunnel** formed at the domain interface.
- **Double-displacement (ping-pong) mechanism:** the nucleophilic serine attacks the acyl-CoA to form
  an **acyl(succinyl)-enzyme intermediate** with release of CoA; the succinyl group is then transferred
  to the hydroxyl of L-homoserine. The tunnel geometry favors transfer to the amino-acid acceptor
  (transferase) over water (hydrolysis) (PMID 16313180).

**Direct sequence/annotation evidence for Q88CT3 (UniProt review, 379 aa, 41.7 kDa, homodimer):** the
protein carries an **AB-hydrolase domain spanning residues 51–360** and an annotated catalytic triad at
**Ser157 – Asp323 – His356** (UniProt ACT_SITE 157/323/356), plus substrate-binding residues **Arg227**
and **Asp357** (BINDING). Inspection of the sequence confirms these identities, and **Ser157 sits in the
canonical nucleophile-elbow motif G-x-S-x-G** (local sequence ...GG**S**LG...), the hallmark of the
α/β-hydrolase superfamily. Thus Q88CT3 uses the same conserved Ser–Asp–His triad and acyl-enzyme
chemistry described above, with Ser157 as the catalytic nucleophile, His356 as the general base, Asp323
orienting the histidine, and Arg227 in the substrate/oxyanion-binding region — a succinyl-tuned acyl
pocket.

## 4. Pathway context

metXS catalyzes the **first, committed step of the succinylation route to methionine**, producing the
activated intermediate O-succinyl-L-homoserine. The downstream fate of this intermediate is
organism-specific, and *P. putida* has been studied directly:

**Primary route in *P. putida* — direct sulfhydrylation.** Vermeij & Kertesz (1999, PMID 10482527)
showed that *P. putida* (strain S-313), like *P. aeruginosa*, uses **direct sulfhydrylation of
O-succinylhomoserine** for methionine synthesis. In this route the succinyl intermediate reacts
directly with free sulfide (H₂S) to give **L-homocysteine**, catalyzed by an O-succinylhomoserine
sulfhydrylase (MetZ/MetY-type; the *metZ* gene was identified in *P. aeruginosa*, Foglino et al. 1995,
PMID 7704274). The transsulfuration enzymes (cystathionine γ-synthase and β-lyase) were expressed at
low levels and only strongly upregulated when cysteine was the sole sulfur source — i.e.
transsulfuration is a secondary, cysteine-inducible branch in this organism. Notably, *Pseudomonas* is
unusual in performing direct sulfhydrylation on the **O-succinyl** (rather than O-acetyl) homoserine
substrate (PMID 7704274).

Overall pathway topology:

1. **L-homoserine + succinyl-CoA → O-succinyl-L-homoserine** *(metXS / PP_5097 — this enzyme)*
2. O-succinyl-L-homoserine + sulfide → **L-homocysteine** (direct sulfhydrylation, MetZ-type; *primary
   route in P. putida*)
   — or, secondarily, O-succinyl-L-homoserine + L-cysteine → L-cystathionine (cystathionine γ-synthase)
   → L-homocysteine (cystathionine β-lyase) *(cysteine-inducible transsulfuration branch)*
3. L-homocysteine → **L-methionine** (methionine synthase, MetE/MetH)

Because O-succinyl-L-homoserine (rather than O-acetyl-L-homoserine) is produced, PP_5097 places
*P. putida* in the **succinyl** branch typical of many Gram-negative bacteria (analogous in outcome to
*E. coli* MetA, but achieved by a structurally unrelated MetX-family enzyme — a textbook case of
**parallel/convergent evolution of isofunctional enzymes**, PMID 28581482).

## 5. Regulation

The succinyltransferase step is a **regulated control point**. In the closely related *P. aeruginosa*,
the adjacent gene **MetW** encodes a protein that physically interacts with and **activates the HST
activity of MetX**; the MetW–MetX complex (but not MetX alone) is subject to **feedback inhibition by
S-adenosyl-L-homocysteine (SAH)** via a glycine-rich SAM/SAH-binding motif in MetW (Gly24 required)
(Hasebe 2021, PMID 33604638). This couples methionine-pathway flux to the cellular methylation cycle.
The same metW–metX genomic arrangement and regulatory logic are the most likely physiological control
on PP_5097 in *P. putida* (inference from the same genus).

## 6. Localization

The gene product functions in the **cytoplasm** (UniProt SUBCELLULAR LOCATION: Cytoplasm; SUBUNIT:
homodimer). This is consistent with (i) its role as a soluble intermediary-metabolism enzyme acting on
cytosolic substrates (L-homoserine, succinyl-CoA), (ii) the absence of a signal peptide or transmembrane
segments in MetX-family proteins, and (iii) the cytosolic localization annotated for MetX/MetA-family
homoserine transacylases generally. No evidence indicates secretion or membrane association.

## 6b. Physiological requirement in *P. putida* KT2440

A genome-wide transposon screen of *P. putida* KT2440 on glucose minimal medium recovered **methionine
auxotrophs**, confirming that de novo methionine biosynthesis is functionally required (conditionally
essential) when methionine is not supplied (Molina-Henares et al. 2010, PMID 20158506). As the enzyme
catalyzing the committed entry step, metXS/PP_5097 is expected to be conditionally essential under such
conditions (methionine-free minimal medium), while dispensable when methionine is available in the
environment.

## 7. Supported and refuted hypotheses

**Supported**
- PP_5097 is a homoserine O-**succinyl**transferase (EC 2.3.1.46), not an acetyltransferase — experimentally validated (PMID 28581482).
- It catalyzes the first committed step of methionine biosynthesis (succinyl branch).
- It uses an α/β-hydrolase fold with a Ser–Asp–His triad and double-displacement chemistry (family structural evidence).
- Its activity is regulated by MetW and by SAH feedback in *Pseudomonas* (PMID 33604638).
- It functions in the cytoplasm.
- The product O-succinyl-L-homoserine is channeled **primarily via direct sulfhydrylation** to homocysteine in *P. putida* (PMID 10482527), with transsulfuration as a secondary, cysteine-inducible branch.

**Refuted / corrected**
- The default database assumption that "MetX = acetyl-CoA" is **incorrect** for this protein; the metXS
  designation and EC 2.3.1.46 explicitly correct it.
- The initial framing that the succinyl intermediate feeds mainly the *cystathionine transsulfuration*
  route is **corrected**: in *P. putida* the dominant downstream route is direct sulfhydrylation to homocysteine.

## 8. Evidence quality and limitations

- The **substrate-specificity** assignment rests on a high-quality, targeted enzymology study covering
  100 family members plus structural modeling (PMID 28581482) — strong, but PP_5097's kinetic constants
  are not individually reported here.
- **Mechanism/structure** is inferred from crystal structures of MetX-family homologs (PMID 16313180,
  17927957) and specificity-mutation studies (PMID 34090964), not from a PP_5097 structure.
- **Regulation** (MetW, SAH feedback) is demonstrated in *P. aeruginosa* (PMID 33604638); direct
  *P. putida* confirmation would strengthen the claim.
- **Localization** is by strong bioinformatic/functional inference rather than direct measurement.

**Future directions:** determine PP_5097 kinetics (k_cat/K_m for succinyl-CoA vs acetyl-CoA), solve
its structure to map the succinyl-specificity residues, and test MetW dependence and SAH feedback
directly in *P. putida* KT2440.

---

### Key references
- Bastard et al. 2017, *Nat. Chem. Biol.* — Parallel evolution of non-homologous isofunctional enzymes in methionine biosynthesis (**PMID 28581482**). *Defining reference for the metXS/EC 2.3.1.46 assignment.*
- Hasebe 2021 — MetW regulates the enzymatic activity of MetX in *Pseudomonas* (**PMID 33604638**).
- Maurya et al. 2021 — Key residues in M. tuberculosis HAT and the evolution of the MetX family (HAT/SAT/HST) (**PMID 34090964**).
- Mirza et al. 2005 — Crystal structure of homoserine transacetylase from *H. influenzae* (**PMID 16313180**).
- Wang et al. 2007 — Crystal structure of homoserine O-acetyltransferase from *L. interrogans* (**PMID 17927957**).
- Molina-Henares et al. 2010 — Conditionally essential genes for growth of *P. putida* KT2440 on minimal medium; methionine auxotrophs recovered (**PMID 20158506**).
- Vermeij & Kertesz 1999 — Pathways of assimilative sulfur metabolism in *P. putida*; direct sulfhydrylation of O-succinylhomoserine is the primary methionine route (**PMID 10482527**).
- Foglino et al. 1995 — Direct sulfhydrylation pathway for methionine biosynthesis in *P. aeruginosa*; identification of *metZ* (**PMID 7704274**).
- UniProt Q88CT3 (METXS_PSEPK) — reviewed entry: 379 aa homodimer, cytoplasm, ACT_SITE Ser157/Asp323/His356, EC 2.3.1.46.


## Artifacts

- [OpenScientist final report](metXS-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](metXS-deep-research-openscientist_artifacts/final_report.pdf)