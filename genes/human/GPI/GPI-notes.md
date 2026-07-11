# GPI (P06744) review notes

## Core biology
GPI = glucose-6-phosphate isomerase / phosphoglucose isomerase (PGI), EC 5.3.1.9. Second
enzyme of glycolysis; reversibly interconverts glucose-6-phosphate and fructose-6-phosphate
(aldose-ketose isomerization), and runs in reverse in gluconeogenesis. Cytosolic homodimer
in the active form.

UniProt FUNCTION [file:human/GPI/GPI-uniprot.txt]: "Isomerase that catalyzes the conversion
of alpha-D-glucose-6-phosphate to beta-D-fructose-6-phosphate, the second step in glycolysis,
and the reverse reaction in gluconeogenesis, within the cytoplasm (PubMed:28803808)."
PATHWAY: "Carbohydrate degradation; glycolysis; ... step 2/4."
SUBUNIT: "Homodimer; in the catalytically active form ... Monomer in the secreted form."
SUBCELLULAR LOCATION: "Cytoplasm ... Secreted."

## Moonlighting (classic multifunctional / MoonDB-curated)
The same protein acts extracellularly as a secreted cytokine/growth factor with several
historical names: Neuroleukin (NLK), Autocrine Motility Factor (AMF), maturation factor,
sperm antigen 36. Signals through the AMF receptor gp78 / AMFR.
- [PMID:24810856] full text: "AMF is a moonlighting protein. When secreted outside tumor
  cells, it acts as a cytokine to promote cancer cell invasion and metastasis by stimulating
  cell motility upon binding to gp78 [30]. Inside the cell, AMF is equal to previously
  identified phosphoglucose isomerase (PGI) that catalyzes the interconversion of glucose
  6-phosphate and fructose 6-phosphate [31]." Establishes GPI–gp78 (AMFR, Q9UKV5) direct
  binding + polyubiquitylation (basis of the IPI GO:0031625 ubiquitin protein ligase binding).
- [PMID:11437381] AMF is an angiogenic factor: "AMF stimulated in vitro motility of human
  umbilical vein endothelial cells (HUVECs)"; basis for extracellular region + cytoplasm EXP
  localization and positive regulation of endothelial cell migration.
- [PMID:1649192] Purification of AMF from HT-1080 fibrosarcoma conditioned medium; cloned its
  receptor gp78 (78-kDa cell surface glycoprotein). Basis for GO:0010595 pos reg endothelial
  cell migration (IDA).
- [PMID:3020690] Neuroleukin: "a lymphokine product of lectin-stimulated T cells that induces
  immunoglobulin secretion by cultured human peripheral blood mononuclear cells." Basis for
  positive regulation of immunoglobulin production (IDA) + humoral immune response (TAS).

## Enzyme/disease evidence
- [PMID:13538944] Tsuboi 1958: purification & properties of human erythrocyte phosphoglucose
  isomerase — classic enzyme characterization (EXP GO:0004347).
- [PMID:28803808] CNSHA4 patients with GPI deficiency; measured residual GPI activity;
  IDA GO:0004347 + glucose-6-phosphate metabolic process. "the second most common red blood
  cell glycolytic enzymopathy."
- [PMID:7435496] First stable GPI variant with severe hemolytic anemia; altered kinetics
  (F6P/G6P affinity). Basis of TAS hemostasis? (see below).
- [PMID:8575767] GPI exon mapping / gene structure — basis of NAS carbohydrate metabolic process.

## Judgments
- Core = MF GO:0004347 (glucose-6-phosphate isomerase activity) + glycolysis GO:0006096 +
  gluconeogenesis GO:0006094 + glucose 6-phosphate metabolic process GO:0051156, cytosol.
- Moonlighting cytokine/AMF/neuroleukin functions (endothelial migration, Ig production,
  humoral immune response, extracellular localization, ubiquitin ligase binding) = real but
  NON-CORE (KEEP_AS_NON_CORE).
- Ensembl GO_REF:0000107 rat-ortholog transfers (learning/memory, response to hormones,
  immobilization stress, muscle stretch, cadmium, negative regulation of apoptosis, plasma
  membrane, ciliary membrane, fructose-6-P metabolic process): mostly over-propagated
  phenotype-context IEAs, not GPI's core function. Mark over-annotated except F6P metabolic
  process (real substrate) which is ACCEPT.
- GO:0047938 glucose-6-phosphate 1-epimerase / GO:0016857 racemase-epimerase / GO:0016853
  isomerase: broad or by-similarity anomerase/epimerase side activities. UniProt lists
  C2-epimerase & anomerase "By similarity". Keep as accept (isomerase) or non-core.
- GO:0005515 protein binding (IPI, PMID:27499296, TAMM41): bare protein binding — MARK_AS_OVER_ANNOTATED
  per policy (uninformative; mito interactome screen).
- hemostasis GO:0007599 (TAS, PMID:7435496): paper is about a hemolytic-anemia GPI variant,
  not hemostasis/clotting. Over-annotation.
- exosome/membrane HDA (5 papers): large-scale proteomic surveys; keep as non-core / over-annotated.
