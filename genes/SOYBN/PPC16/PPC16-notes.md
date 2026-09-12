# PPC16 (Q02909) — research notes

Gene: PPC16 / soybean (Glycine max, NCBITaxon:3847)
UniProt: Q02909 (CAPP1_SOYBN) — "Phosphoenolpyruvate carboxylase, housekeeping isozyme", EC 4.1.1.31, 967 aa.
Reviewed for the SPKW-PLANTS retrospective validation subproject.

## 1. What this protein is

Q02909 is a soybean phosphoenolpyruvate carboxylase (PEPC). UniProt explicitly names it
the **housekeeping isozyme** ("PEPC 1"). It catalyzes the irreversible β-carboxylation of
phosphoenolpyruvate (PEP) using bicarbonate to form oxaloacetate (OAA) + Pi
(Rhea:RHEA:28370). The UniProt FUNCTION text states the role plainly:

> "Through the carboxylation of phosphoenolpyruvate (PEP) it forms oxaloacetate, a
> four-carbon dicarboxylic acid source for the tricarboxylic acid cycle."
> [UniProt Q02909 FUNCTION]

Key UniProt facts: homotetramer; cytoplasmic (Cytoplasm subcellular location);
regulated by light-reversible (Ser-11) phosphorylation; allosteric enzyme; Mg2+ cofactor;
"Belongs to the PEPCase type 1 family" — i.e. a **plant-type PEPC (PTPC)**, not a
bacterial-type PEPC (BTPC). PE level 2 (evidence at transcript level).

## 2. The defining literature: original cloning paper

The single primary reference cited by UniProt is the cDNA cloning paper:

[PMID:1450389 "A full-length cDNA encoding a subunit of phosphoenolpyruvate carboxylase
(PEPC) was isolated from a developing seed expression library of the C3 plant Glycine
max."]

This paper directly settles two of the central biological questions:

- **Soybean is a C3 plant** — stated explicitly: "the C3 plant Glycine max".
- **This isozyme is a C3-type / housekeeping PEPC, NOT a photosynthetic C4 PEPC:**
  [PMID:1450389 "The soybean encoded protein tends to resemble other 'C3-type' PEPC
  proteins more closely than those implicated in C4 or crassulacean acid metabolism."]
- **Ubiquitous, non-photosynthesis-specific expression:**
  [PMID:1450389 "The corresponding mRNA is present at similar levels in leaf, stem, root
  and developing seed."] — a housekeeping expression pattern, not the mesophyll-specific,
  light-induced pattern of a C4 photosynthetic PEPC.
- The paper also notes two potential start codons and that the protein could be subject
  to regulation by protein kinase (consistent with the UniProt phosphoserine site).

## 3. Plant PEPC isozyme families (background)

The authoritative review is O'Leary, Park & Plaxton 2011 [PMID:21524275]:

- Plant genomes encode a small multigene family: several **plant-type PEPCs (PTPCs)** and
  one distantly related **bacterial-type PEPC (BTPC)**.
  [PMID:21524275 "PEPC belongs to a small multigene family encoding several closely
  related PTPCs (plant-type PEPCs), along with a distantly related BTPC (bacterial-type
  PEPC)."]
- PTPCs are ~110 kDa, carry the conserved N-terminal seryl-phosphorylation site, and form
  homotetrameric Class-1 PEPCs. Q02909 is 967 aa / ~110 kDa with the Ser-11 phosphosite —
  a textbook PTPC.
  [PMID:21524275 "PTPC genes encode ~110-kDa polypeptides containing conserved
  serine-phosphorylation and lysine-mono-ubiquitination sites, and typically exist as
  homotetrameric Class-1 PEPCs."]
- The well-studied role of PEPC in photosynthesis is restricted to the dedicated C4/CAM
  isoforms; PEPC ALSO does a broad set of NON-photosynthetic jobs, dominated by
  anaplerosis:
  [PMID:21524275 "The critical role of PEPC in assimilating atmospheric CO2 during C4 and
  Crassulacean acid metabolism photosynthesis has been studied extensively. PEPC also
  fulfils a broad spectrum of non-photosynthetic functions, particularly the anaplerotic
  replenishment of tricarboxylic acid cycle intermediates consumed during biosynthesis
  and nitrogen assimilation."]

C4/CAM photosynthetic PEPC isoforms evolved repeatedly and independently from
non-photosynthetic C3 progenitor genes by gene duplication and acquisition of
mesophyll-specific, light-responsive expression plus kinetic adaptations (e.g. the
C4-diagnostic Ser-775 residue) [PMID:14644912; PMID:16136331; PMID:24913627]. A C3 plant
like soybean has only the ancestral, non-photosynthetic-type PTPCs — it has no C4 CO2-pump
machinery.

## 4. Anaplerotic / housekeeping role of PEPC in C3 plants

The "housekeeping" PEPC (= anaplerotic PEPC) in C3 plants performs:

- **Anaplerosis**: refilling TCA-cycle C4 intermediates (oxaloacetate, malate) drained for
  biosynthesis. PEPC is not a TCA-cycle enzyme; it feeds OAA into the cycle from outside.
  [PMID:21524275 "anaplerotic replenishment of tricarboxylic acid cycle intermediates
  consumed during biosynthesis and nitrogen assimilation."]
- **Nitrogen assimilation / amino-acid biosynthesis**: OAA → aspartate and glutamate-family
  amino acids; provides carbon skeletons for NH4+ assimilation.
- **Cellular pH regulation / charge balance**, osmotic regulation (e.g. guard-cell malate
  for stomatal opening), and seed/fruit organic-acid accumulation.

Singh et al. 2022 [PMID:36309625] reviews how, in C3 plants, the non-photosynthetic
isoforms of "C4 enzymes" (including PEPC) serve general metabolism rather than
photosynthesis:
[PMID:36309625 "all the genes of the C4 photosynthetic pathway are present in C3 plants,
although they are involved in diverse non-photosynthetic functions. Non-photosynthetic
isoforms of carbonic anhydrase (CA), phosphoenolpyruvate carboxylase (PEPC) ... catalyze
reactions that are essential for major plant metabolism pathways, such as the
tricarboxylic acid (TCA) cycle, maintenance of cellular pH, uptake of nutrients and their
assimilation."]

Ting, She & Plaxton 2017 [PMID:29240945] similarly frames PTPC function as anaplerotic in
biosynthetically active sink tissues:
[PMID:29240945 "Class-2 PEPCs simultaneously maintain rapid anaplerotic PEP carboxylation
and respiratory CO2 refixation in diverse, biosynthetically active sinks that accumulate
high malate levels."] (PTPCs such as Q02909 are the catalytic backbone; note BTPC is a
separate gene, not Q02909.)

## 5. PEPC in soybean nodules / N fixation

In legume root nodules PEPC activity is induced and supplies OAA/malate as carbon skeletons
for the assimilation of fixed nitrogen and as a respiratory substrate for bacteroids — an
anaplerotic, non-photosynthetic role. Importantly, the contribution of nodule
PEPC-mediated CO2 fixation to whole-plant carbon is minor: a field 13C/15N study of
nodulating vs non-nodulating soybean concluded
[PMID:10938812 "the expected contribution by phosphopenolpyruvate carboxylase-mediated CO2
fixation in the root nodules to plant C-incorporation could not have been significant."]
This reinforces that PEPC carboxylation in soybean is anaplerotic (replenishing organic
acids), not net autotrophic "carbon fixation". PPC16/Q02909 is the ubiquitously expressed
housekeeping isozyme (leaf/stem/root/seed) and is the kind of PTPC that operates in roots
and nodules.

## 6. Family/domain evidence

- InterPro/PANTHER place Q02909 in PTHR30523 (PHOSPHOENOLPYRUVATE CARBOXYLASE), subfamily
  PTHR30523:SF33 ("PHOSPHOENOLPYRUVATE CARBOXYLASE 3"). HAMAP MF_00595 = PEPcase type 1.
- InterPro signatures: IPR021135 (PEP_COase), IPR022805 (PEP_COase bacterial/plant-type),
  IPR018129 / IPR033129 (Lys and His active-site signatures). Active-site His-172 and
  Lys-602 (UniProt FT ACT_SITE) are consistent with canonical PEPC catalysis.

## 7. Assessment of the GO annotations under review

### Retired SPKW annotation — photosynthesis (GO:0015979), GO_REF:0000043
GO:0015979 def: "The synthesis by organisms of organic chemical compounds, especially
carbohydrates, from carbon dioxide (CO2) using energy obtained from light..."
This annotation came purely from the UniProt keyword "Photosynthesis" (KW line), which is
applied broadly to all PEPCs because the *family* is famous for its C4/CAM role. But:
(a) soybean is C3 [PMID:1450389]; (b) this isozyme is explicitly the housekeeping/C3-type
PEPC [PMID:1450389; UniProt RecName]; (c) C3 plants have no light-driven CO2-fixation by
PEPC. The protein has no role in photosynthesis. **GOA's removal of this annotation was
JUSTIFIED — it was a keyword-driven, pathway-context over-annotation.** Action: REMOVE
(keep `retired: true`).

### carbon fixation (GO:0015977), IEA UniProtKB-KW / InterPro
GO:0015977 def: "A metabolic process in which carbon (usually derived from carbon dioxide)
is incorporated into organic compounds (usually carbohydrates)." Every child of GO:0015977
is an autotrophic CO2-fixation pathway: C4 photosynthesis, CAM photosynthesis, reductive
TCA cycle, carbon fixation by acetyl-CoA pathway, 3-hydroxypropionate cycle. The term is an
autotrophic / net-carbon-gain concept. Housekeeping PEPC carboxylates PEP to OAA for
anaplerosis — it does not perform autotrophic carbon fixation and does not produce
carbohydrate. So `carbon fixation` is an over-annotation/mis-mapping for the housekeeping
isozyme. The UniProt keyword "Carbon dioxide fixation" was again applied at family level.
The most biologically accurate replacement for the actual process is
**oxaloacetate metabolic process (GO:0006107)** — def: "The chemical reactions and pathways
involving oxaloacetate ... an important intermediate in metabolism, especially as a
component of the TCA cycle." Action: MODIFY → GO:0006107.

### tricarboxylic acid cycle (GO:0006099), IEA InterPro
GO:0006099 def describes the cyclic oxidation of acetyl-CoA via citrate → isocitrate →
2-oxoglutarate → succinyl-CoA → succinate → fumarate → malate → oxaloacetate. PEPC is NOT
one of the eight TCA-cycle enzymes. It is an **anaplerotic** enzyme that *feeds* OAA into
the cycle from PEP [PMID:21524275]. Annotating PEPC `involved_in tricarboxylic acid cycle`
conflates anaplerosis with the cycle itself. This InterPro2GO mapping (IPR021135/IPR022805
→ GO:0006099) is too coarse. Better: `oxaloacetate metabolic process (GO:0006107)`, which
captures the anaplerotic provision of the TCA intermediate without asserting cycle
membership. Action: MODIFY → GO:0006107.

### phosphoenolpyruvate carboxylase activity (GO:0008964), IEA
Catalytic activity directly matching UniProt CATALYTIC ACTIVITY / EC 4.1.1.31 / Rhea
RHEA:28370. Correct and core. Action: ACCEPT.

### cytosol (GO:0005829), IBA GO_REF:0000033
PTPCs are cytosolic enzymes; UniProt subcellular location = Cytoplasm. IBA from the PEPC
phylogenetic group. Correct and core. Action: ACCEPT.

### cytoplasm (GO:0005737), IEA GO_REF:0000044
From UniProt subcellular-location mapping (Cytoplasm). Correct but less specific than
cytosol. Action: ACCEPT (consistent, broader term).

## 8. Core function summary

PPC16/Q02909 is the cytosolic, homotetrameric **housekeeping (anaplerotic) plant-type
PEPC** of soybean (a C3 legume). Its core molecular function is phosphoenolpyruvate
carboxylase activity (EC 4.1.1.31), carboxylating PEP with bicarbonate to oxaloacetate.
Its core biological role is **anaplerotic provision of oxaloacetate** to replenish
TCA-cycle C4-dicarboxylic-acid intermediates consumed by biosynthesis and nitrogen
assimilation. It is NOT a photosynthetic CO2-fixing enzyme and is NOT a TCA-cycle enzyme.

## 9. Over-annotation pattern identified

This gene is a clean example of **family-level / pathway-context keyword over-annotation**:
because the PEPC enzyme family is famous for C4/CAM photosynthesis, family-wide UniProt
keywords ("Photosynthesis", "Carbon dioxide fixation") and coarse InterPro2GO mappings
(→ photosynthesis, carbon fixation, TCA cycle) get propagated onto every PEPC, including
the housekeeping C3 isozymes that do none of those things. GOA's retirement of the SPKW
"photosynthesis" annotation correctly removed one instance of this pattern; the surviving
IEA "carbon fixation" and "tricarboxylic acid cycle" annotations are the same error class
and should be modified to the anaplerotic-accurate term GO:0006107.
