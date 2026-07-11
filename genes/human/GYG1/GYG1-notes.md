# GYG1 (Glycogenin-1, UniProtKB:P46976) — review notes

## Summary of verified biology

GYG1 encodes **glycogenin-1**, the self-glucosylating **primer/initiator of glycogen
biosynthesis**. It is a member of the glycosyltransferase 8 (GT8/CAZy GT8) family,
glycogenin subfamily. Using UDP-alpha-D-glucose as sugar donor and a divalent metal
cofactor (Mn2+ most effective), it **autoglucosylates its own Tyr195**, building a short
covalently attached alpha-1,4-glucan chain (~8–12 glucose residues) via a
glucose-1-O-tyrosyl linkage. This maltosaccharide primer is then elongated by glycogen
synthase (GYS1 in muscle/most tissues, GYS2 in liver), with glycogen branching enzyme
(GBE1) adding alpha-1,6 branch points. Glycogenin remains covalently buried at the core
of the mature glycogen granule.

- EC 2.4.1.186; glycogenin glucosyltransferase activity (GO:0008466).
- Reactions (from UniProt, RHEA:23360 initiation and RHEA:56560 elongation of the
  self-glucosyl chain).
- Cofactor Mn2+ (CHEBI:29035), required for self-glucosylation
  [file:human/GYG1/GYG1-uniprot.txt "Required for self-glucosylation. Manganese is"].
- Structure: many crystal structures of residues 1–262 with Mn/UDP/UDP-glucose
  (PMID:22160680, PDBs 3Q4S etc.); cryo-EM of the GYS1–GYG1 complex (PMID:35835870,
  PMID:35690592).

## Complex / subunit

Part of the GYS1–GYG1 complex, a heterooctamer of a GYS1 tetramer + 2 GYG1 dimers, each
GYS1 protomer binding one GYG1 subunit via the GYG1 C-terminus
[file:human/GYG1/GYG1-uniprot.txt]. The GYG1 C-terminal ~33 residues mediate the
interaction with glycogen synthase [PMID:17055998, "The interaction with glycogenin was
found to be mediated by the region of glycogenin which contains the 33 COOH-terminal amino
acid residues."]. GYG1 forms homodimers (IDA, PMID:22160680, PMID:30356213). ComplexPortal
entries CPX-26491 (GYG1-GYS1) and CPX-26492 (GYG1-GYS2).

## Disease

- **Glycogen storage disease 15 / GSD XV** (MIM:613507): muscle weakness with skeletal
  muscle glycogen depletion + cardiac arrhythmia with abnormal cardiac storage material;
  Thr83Met abolishes autoglucosylation [PMID:20357282; PMID:22160680].
- **Polyglucosan body myopathy 2 (PGBM2)** (MIM:616199): polyglucosan accumulation in
  muscle, skeletal myopathy without cardiac involvement (variants Ala16Pro, Asp102His;
  PMID:25272951).

## Localization

Cytoplasmic; localizes to glycogen granules (glycosomes) in the cytoplasm; also reported
nucleus (by similarity). GOA carries many Reactome TAS "cytosol" annotations and a small
number of dubious localization terms (nucleus IEA/ISS via SubCell mapping; membrane HDA
from an NK-cell membrane proteome; and Reactome neutrophil-degranulation-pathway CC terms:
extracellular region, secretory/ficolin-1-rich granule lumen, lysosomal lumen). These
extracellular/granule/lysosomal-lumen terms come from GYG1's incidental appearance in
neutrophil-degranulation and Pompe-disease Reactome pathways and do not reflect the core
cytosolic/glycogen-granule biology; treated as over-annotations.

## Annotation review disposition

- Core MF: GO:0008466 glycogenin glucosyltransferase activity (EXP/IDA/IBA) — ACCEPT.
- GO:0016757 glycosyltransferase activity (IEA InterPro) — parent of 0008466; ACCEPT as
  a correct-but-general IEA.
- GO:0030145 manganese ion binding (IDA x2) — ACCEPT (structural + functional cofactor).
- GO:0042803 protein homodimerization activity (IDA x2) — ACCEPT.
- GO:0005515 protein binding IPI x5 — bare, uninformative; MARK_AS_OVER_ANNOTATED
  (real MF captured by homodimerization + the GYS1 complex). Do not REMOVE per policy.
- GO:0005978 glycogen biosynthetic process (IBA/IEA/TAS/IDA/IMP) — ACCEPT (core BP).
  Note UniProt DR also has GO:0160249 "glycogen biosynthetic process via UDP-glucose"
  (IMP) which is not in GOA; more precise child; noted as a proposed refinement.
- GO:1902494 catalytic complex (IDA, ComplexPortal PMID:35835870) — ACCEPT (GYS1-GYG1).
- Cytoplasm/cytosol (IBA is_active_in cytoplasm; ISS; Reactome TAS cytosol x17) — ACCEPT
  the cytoplasm/cytosol location; is_active_in cytoplasm reflects where it acts.
- Nucleus (IEA SubCell; ISS) — MARK_AS_OVER_ANNOTATED (SubCell keyword propagation; no
  direct experimental support for a nuclear function; core biology is cytosolic).
- membrane (HDA, NK-cell membrane proteome PMID:19946888) — MARK_AS_OVER_ANNOTATED
  (mass-spec membrane co-fractionation; glycogenin is a peripheral/soluble protein).
- extracellular region / secretory granule lumen / ficolin-1-rich granule lumen /
  lysosomal lumen (Reactome TAS from neutrophil-degranulation & Pompe pathways) —
  MARK_AS_OVER_ANNOTATED (pathway-context artifacts, not core localization).
