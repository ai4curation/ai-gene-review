#!/usr/bin/env python3
"""Build the full DPYSL5 (CRMP5) gene review from the fetched stub.

Mutates the existing existing_annotations in order (asserting term/ref to fail
fast on any drift), fills review summary/action/reason/supported_by, and adds
description, references, aliases, core_functions, suggested_questions/experiments.
"""
from pathlib import Path
import yaml

P = Path("genes/human/DPYSL5/DPYSL5-ai-review.yaml")
d = yaml.safe_load(P.read_text())

UNI = "file:human/DPYSL5/DPYSL5-uniprot.txt"

def sb(ref, text):
    return [{"reference_id": ref, "supporting_text": text}]

CAUTION_TXT = ("Lacks most of the conserved residues that are essential for binding the "
               "metal cofactor and hence for dihydropyrimidinase activity.")
SIM_TXT = "Belongs to the metallo-dependent hydrolases superfamily."
FUNC_TXT = "FUNCTION: Involved in the negative regulation of dendrite outgrowth."

# Per-annotation review content, in the SAME ORDER as the stub.
# Each tuple: (expected_term_id, expected_ref, dict(action, summary, reason, supported_by))
R = [
 ("GO:0005829", "GO_REF:0000033", dict(
   action="ACCEPT",
   summary="DPYSL5/CRMP5 is a cytosolic protein (UniProt: Cytoplasm). is_active_in cytosol by phylogenetic inference is consistent with the CRMP family and with its role as a cytoskeleton-associated regulator.",
   reason="Correct localization. CRMPs are soluble cytoplasmic proteins; UniProt records DPYSL5 as cytoplasmic.",
   supported_by=sb(UNI, "SUBCELLULAR LOCATION: Cytoplasm"))),

 ("GO:0004157", "GO_REF:0000033", dict(
   action="ACCEPT",
   summary="This is a NOT (negated) annotation: DPYSL5 does NOT enable dihydropyrimidinase activity. Although DPYSL5 belongs to the metallo-dependent hydrolase (dihydropyrimidinase/amidohydrolase) superfamily and is ~57% identical to dihydropyrimidinase, it lacks the conserved metal-cofactor-binding residues required for catalysis (UniProt CAUTION).",
   reason="The negation is correct and important. DPYSL5 is a catalytically dead family member; the curated NOT|enables faithfully encodes the loss of activity flagged by the UniProt CAUTION. Retain as-is.",
   supported_by=sb(UNI, CAUTION_TXT))),

 ("GO:0006208", "GO_REF:0000033", dict(
   action="ACCEPT",
   summary="NOT (negated) annotation: DPYSL5 is NOT involved in pyrimidine nucleobase catabolism. This is the process counterpart of the absent dihydropyrimidinase activity.",
   reason="Correct negation, consistent with the loss of catalytic activity (no metal cofactor binding). Retain.",
   supported_by=sb(UNI, CAUTION_TXT))),

 ("GO:0005737", "GO_REF:0000120", dict(
   action="ACCEPT",
   summary="Cytoplasmic localization by automated IEA, consistent with UniProt and with the IBA cytosol annotation.",
   reason="Correct, if broad, localization. CRMP5 is a cytoplasmic protein.",
   supported_by=sb(UNI, "SUBCELLULAR LOCATION: Cytoplasm"))),

 ("GO:0016787", "GO_REF:0000002", dict(
   action="REMOVE",
   summary="Positive IEA 'hydrolase activity' propagated from the metallo-dependent hydrolase fold signature (InterPro IPR006680, Amidohydrolase-related). DPYSL5 belongs to this superfamily by sequence, but the UniProt CAUTION states it lacks the conserved metal-cofactor-binding residues 'essential for ... dihydropyrimidinase activity', and metallo-hydrolase catalysis across this superfamily depends on that metal centre.",
   reason="Domain-based electronic over-propagation that should be removed on biological grounds. The annotation rests solely on the fold signature; the catalytic prerequisite (metal-cofactor binding) is demonstrably absent, the curated GO:0004157 (dihydropyrimidinase) is itself NOT-ed, and there is no positive evidence DPYSL5 performs any hydrolysis. Its established function is non-catalytic (negative regulation of dendrite outgrowth). NB: this is not a logical contradiction with the NOT (GO NOT propagates to child terms, not up to parents) - it is an unsupported, biologically implausible over-annotation. A weaker action (MARK_AS_OVER_ANNOTATED) does not fit, since that is for terms the gene is genuinely related to but peripheral on; here the activity is absent.",
   supported_by=[{"reference_id": UNI, "supporting_text": CAUTION_TXT},
                 {"reference_id": UNI, "supporting_text": SIM_TXT}])),

 ("GO:0016810", "GO_REF:0000002", dict(
   action="REMOVE",
   summary="Positive IEA 'hydrolase activity, acting on carbon-nitrogen (but not peptide) bonds' propagated from the metallo-dependent hydrolase composite fold (InterPro IPR011059). Same basis and same problem as the GO:0016787 parent term.",
   reason="Domain-based over-propagation contradicted on biological grounds by the loss of metal-cofactor-binding residues (UniProt CAUTION). No positive evidence of any C-N hydrolase activity; curated dihydropyrimidinase activity is NOT-ed. Remove, consistent with the GO:0016787 removal.",
   supported_by=[{"reference_id": UNI, "supporting_text": CAUTION_TXT},
                 {"reference_id": UNI, "supporting_text": SIM_TXT}])),
]

# 7 protein-binding (GO:0005515) IPI entries, by reference.
PB_CRMP2 = dict(
  action="KEEP_AS_NON_CORE",
  summary="IPI 'protein binding' annotation; the with/from partner is DPYSL2/CRMP2 (Q16555). DPYSL5 forms homo- and hetero-oligomers with other CRMP-family members, so this captures a real CRMP5-CRMP2 interaction.",
  reason="The interaction is biologically meaningful (CRMP hetero-oligomerization) but the generic 'protein binding' term is uninformative about molecular function (curation guideline). Keep as non-core supporting evidence for oligomerization rather than as a core function.",
  supported_by=sb(UNI, "Homotetramer, and heterotetramer with other DPYS-like proteins"))
PB_SCREEN = dict(
  action="MARK_AS_OVER_ANNOTATED",
  summary="Generic 'protein binding' from a large-scale interactome screen. Uninformative about DPYSL5's molecular function.",
  reason="High-throughput interactome 'protein binding' carries no specific functional signal; per curation guidelines avoid 'protein binding' in favour of informative MF terms. Over-annotation.",
  supported_by=None)
PB = {
 "PMID:25416956": ("GO:0005515", PB_CRMP2),
 "PMID:28514442": ("GO:0005515", PB_CRMP2),
 "PMID:29892012": ("GO:0005515", PB_CRMP2),
 "PMID:31515488": ("GO:0005515", PB_CRMP2),
 "PMID:32296183": ("GO:0005515", PB_SCREEN),
 "PMID:32814053": ("GO:0005515", PB_SCREEN),
 "PMID:33961781": ("GO:0005515", PB_CRMP2),
}
for ref, (tid, body) in PB.items():
    R.append((tid, ref, body))

R += [
 ("GO:0030182", "GO_REF:0000120", dict(
   action="KEEP_AS_NON_CORE",
   summary="Neuron differentiation (IEA). DPYSL5/CRAM is brain-specific, strongly up-regulated during neuronal differentiation and in fetal/neonatal brain.",
   reason="Correct but broad developmental process; non-core relative to the specific dendrite-morphogenesis role.",
   supported_by=sb("PMID:10851247", "CRAM expression is up-regulated during neuronal differentiation of embryonal carcinoma P19 and PC12 cells"))),

 ("GO:0030425", "GO_REF:0000107", dict(
   action="ACCEPT",
   summary="Dendrite localization (IEA from ortholog transfer), consistent with CRMP5's role in regulating dendrite outgrowth/morphogenesis.",
   reason="Consistent with the cytoskeletal/dendritic function and with the IMP dendrite-morphogenesis annotation.",
   supported_by=sb(UNI, FUNC_TXT))),

 ("GO:0032991", "GO_REF:0000107", dict(
   action="KEEP_AS_NON_CORE",
   summary="Part of a protein-containing complex (IEA). DPYSL5 forms homotetramers and heterotetramers with other DPYS-like (CRMP) proteins.",
   reason="Correct but very generic complex term; non-core. The specific oligomerization is better captured by the CRMP2 interaction evidence.",
   supported_by=sb(UNI, "Homotetramer, and heterotetramer with other DPYS-like proteins"))),

 ("GO:0043025", "GO_REF:0000107", dict(
   action="KEEP_AS_NON_CORE",
   summary="Neuronal cell body localization (IEA from ortholog transfer).",
   reason="Plausible neuronal localization, consistent with brain-specific cytoplasmic expression; non-core.",
   supported_by=sb(UNI, "SUBCELLULAR LOCATION: Cytoplasm"))),

 ("GO:0045202", "GO_REF:0000107", dict(
   action="KEEP_AS_NON_CORE",
   summary="Synapse (IEA from ortholog transfer).",
   reason="Broad neuronal localization; plausible but non-core and electronically inferred.",
   supported_by=None)),

 ("GO:0098978", "GO_REF:0000107", dict(
   action="KEEP_AS_NON_CORE",
   summary="Glutamatergic synapse (IEA from ortholog transfer / SynGO-style mapping).",
   reason="Specific synaptic-type localization by electronic transfer; plausible but non-core, no direct experimental support in hand.",
   supported_by=None)),

 ("GO:0050774", "PMID:33894126", dict(
   action="ACCEPT",
   summary="Negative regulation of dendrite morphogenesis (IMP). Jeanne et al. 2021 showed missense variants in DPYSL5 cause a neurodevelopmental disorder (corpus callosum agenesis, cerebellar abnormalities) and link DPYSL5 to control of dendrite/neurite outgrowth.",
   reason="Core function with direct mutational (IMP) evidence and matching the UniProt FUNCTION statement. This is the best-supported specific role of DPYSL5.",
   supported_by=[{"reference_id": "PMID:33894126", "supporting_text": "Missense variants in DPYSL5 cause a neurodevelopmental disorder with corpus callosum agenesis and cerebellar abnormalities."},
                 {"reference_id": UNI, "supporting_text": FUNC_TXT}])),

 ("GO:0005829", "Reactome:R-HSA-399944", dict(
   action="ACCEPT",
   summary="Cytosol localization (Reactome TAS, semaphorin/CRMP signalling reaction).",
   reason="Correct cytosolic localization, consistent with other location annotations.",
   supported_by=sb(UNI, "SUBCELLULAR LOCATION: Cytoplasm"))),
 ("GO:0005829", "Reactome:R-HSA-399947", dict(
   action="ACCEPT",
   summary="Cytosol localization (Reactome TAS).",
   reason="Correct cytosolic localization (duplicate-by-reaction of the same valid annotation).",
   supported_by=sb(UNI, "SUBCELLULAR LOCATION: Cytoplasm"))),
 ("GO:0005829", "Reactome:R-HSA-399951", dict(
   action="ACCEPT",
   summary="Cytosol localization (Reactome TAS).",
   reason="Correct cytosolic localization (duplicate-by-reaction of the same valid annotation).",
   supported_by=sb(UNI, "SUBCELLULAR LOCATION: Cytoplasm"))),

 ("GO:0007165", "PMID:10851247", dict(
   action="KEEP_AS_NON_CORE",
   summary="Signal transduction (TAS, Inatome et al. 2000). CRAM/CRMP5 associates with CRMP3 and protein-tyrosine kinase(s) in developing brain.",
   reason="Very broad process term; true in spirit (CRMP signalling) but uninformative and non-core.",
   supported_by=sb("PMID:10851247", "a novel CRMP3-associated protein, designated CRAM ... associates with CRMP3 and protein-tyrosine kinase(s) in the developing rat brain"))),

 ("GO:0007399", "PMID:10851247", dict(
   action="KEEP_AS_NON_CORE",
   summary="Nervous system development (TAS). DPYSL5/CRAM is brain-specific and developmentally regulated.",
   reason="Correct but broad; non-core relative to the specific dendrite-morphogenesis role.",
   supported_by=sb("PMID:10851247", "The expression of CRAM is brain-specific, is high in fetal and neonatal rat brain"))),

 ("GO:0007411", "PMID:10851247", dict(
   action="KEEP_AS_NON_CORE",
   summary="Axon guidance (TAS). The CRMP family transduces semaphorin-induced growth-cone collapse during neural development; CRAM/CRMP5 associates with CRMP3 in this context.",
   reason="Genuine CRMP-family process, but DPYSL5's distinguishing, experimentally supported role is negative regulation of dendrite morphogenesis; keep axon guidance as a valid non-core process.",
   supported_by=sb("PMID:10851247", "Four members of collapsin response mediator proteins (CRMPs) are thought to be involved in the semaphorin-induced growth cone collapse during neural development"))),
]

anns = d["existing_annotations"]
assert len(anns) == len(R), f"count mismatch: {len(anns)} vs {len(R)}"
for a, (tid, ref, body) in zip(anns, R):
    assert a["term"]["id"] == tid, f"term drift: {a['term']['id']} != {tid}"
    assert str(a.get("original_reference_id")) == ref, f"ref drift at {tid}: {a.get('original_reference_id')} != {ref}"
    review = {"summary": body["summary"], "action": body["action"], "reason": body["reason"]}
    if body.get("supported_by"):
        review["supported_by"] = body["supported_by"]
    a["review"] = review

# ---- top-level fields ----
d["status"] = "DRAFT"
d["description"] = (
  "Dihydropyrimidinase-related protein 5 (DPYSL5; also CRMP5, CRAM, DRP-5, ULIP-6), a "
  "brain-enriched cytoplasmic member of the collapsin response mediator protein (CRMP) / "
  "dihydropyrimidinase-related family. Although it is ~57% identical to dihydropyrimidinase "
  "and belongs to the metallo-dependent hydrolase (amidohydrolase) superfamily, DPYSL5 lacks "
  "the conserved metal-cofactor-binding residues required for catalysis and has no "
  "dihydropyrimidinase / amidohydrolase activity - it is a catalytically dead (pseudoenzyme) "
  "family member. Its function is as a cytoskeleton-associated regulator of neuronal "
  "morphogenesis: it negatively regulates dendrite/neurite outgrowth and is most highly "
  "expressed in fetal and neonatal brain, where it is up-regulated during neuronal "
  "differentiation. DPYSL5 forms homotetramers and heterotetramers with other CRMP-family "
  "proteins (notably DPYSL2/CRMP2) and associates with CRMP3 and protein-tyrosine kinases, "
  "acting within the semaphorin/collapsin growth-cone signalling system. Loss-of-function "
  "and dominant missense variants cause a neurodevelopmental disorder featuring agenesis of "
  "the corpus callosum and cerebellar abnormalities."
)

d["aliases"] = ["CRMP5", "CRAM", "DRP-5", "DRP5", "ULIP-6", "ULIP6",
                "CRMP3-associated molecule", "Collapsin response mediator protein 5"]

d["references"] = [
 {"id": "GO_REF:0000002", "title": "Gene Ontology annotation through association of InterPro records with GO terms",
  "findings": [], "reference_review": {"relevance": "MEDIUM", "correctness": "MISCITED",
   "review_notes": "Source of the two domain-based IEA hydrolase annotations (GO:0016787, GO:0016810). The InterPro2GO mapping fires on the metallo-hydrolase fold but DPYSL5 lacks the catalytic metal site; the activity annotations are not supported for this member."}},
 {"id": "GO_REF:0000033", "title": "Annotation inferences using phylogenetic trees", "findings": []},
 {"id": "GO_REF:0000107", "title": "Automatic transfer of experimentally verified manual GO annotation data to orthologs using Ensembl Compara", "findings": []},
 {"id": "GO_REF:0000120", "title": "Combined Automated Annotation using Multiple IEA Methods", "findings": []},
 {"id": "PMID:10851247",
  "title": "Identification of CRAM, a novel unc-33 gene family protein that associates with CRMP3 and protein-tyrosine kinase(s) in the developing rat brain.",
  "findings": [
    {"statement": "DPYSL5/CRAM is a CRMP-family protein (~57% identical to dihydropyrimidinase, 50-51% to CRMPs) that associates with CRMP3 and protein-tyrosine kinases.",
     "supporting_text": "a novel CRMP3-associated protein, designated CRAM ... shows 57% identity with dihydropyrimidinase, and shows 50-51% identity with CRMPs"},
    {"statement": "Brain-specific expression, highest in fetal/neonatal brain and up-regulated during neuronal differentiation.",
     "supporting_text": "The expression of CRAM is brain-specific, is high in fetal and neonatal rat brain ... up-regulated during neuronal differentiation"}],
  "reference_review": {"relevance": "HIGH", "correctness": "VERIFIED",
   "review_notes": "PubMed-verified primary identification of CRMP5/CRAM; abstract read. Establishes CRMP-family membership and neuronal/developmental context."}},
 {"id": "PMID:33894126",
  "title": "Missense variants in DPYSL5 cause a neurodevelopmental disorder with corpus callosum agenesis and cerebellar abnormalities.",
  "findings": [
    {"statement": "Missense variants in DPYSL5 cause a neurodevelopmental disorder; DPYSL5 controls dendrite/neurite outgrowth.",
     "supporting_text": "Missense variants in DPYSL5 cause a neurodevelopmental disorder with corpus callosum agenesis and cerebellar abnormalities."}],
  "reference_review": {"relevance": "HIGH", "correctness": "VERIFIED",
   "review_notes": "PubMed-verified; primary human genetics paper supporting the IMP negative-regulation-of-dendrite-morphogenesis annotation."}},
 {"id": "PMID:25416956", "title": "A proteome-scale map of the human interactome network.", "findings": []},
 {"id": "PMID:28514442", "title": "Architecture of the human interactome defines protein communities and disease networks.", "findings": []},
 {"id": "PMID:29892012", "title": "An interactome perturbation framework prioritizes damaging missense mutations for developmental disorders.", "findings": []},
 {"id": "PMID:31515488", "title": "Extensive disruption of protein interactions by genetic variants across the allele frequency spectrum in human populations.", "findings": []},
 {"id": "PMID:32296183", "title": "A reference map of the human binary protein interactome.", "findings": [],
  "reference_review": {"relevance": "LOW", "correctness": "VERIFIED",
   "review_notes": "High-throughput interactome; supports generic protein binding only."}},
 {"id": "PMID:32814053", "title": "Interactome Mapping Provides a Network of Neurodegenerative Disease Proteins and Uncovers Widespread Protein Aggregation in Affected Brains.", "findings": [],
  "reference_review": {"relevance": "LOW", "correctness": "VERIFIED",
   "review_notes": "High-throughput neurodegenerative-disease interactome; generic protein binding only."}},
 {"id": "PMID:33961781", "title": "Dual proteome-scale networks reveal cell-specific remodeling of the human interactome.", "findings": []},
 {"id": "Reactome:R-HSA-399944", "title": "Other semaphorin interactions (CRMP signalling).", "findings": []},
 {"id": "Reactome:R-HSA-399947", "title": "CRMP phosphorylation / semaphorin signalling reaction.", "findings": []},
 {"id": "Reactome:R-HSA-399951", "title": "CRMP signalling reaction.", "findings": []},
 {"id": UNI, "title": "UniProt entry Q9BPU6 (DPYSL5)",
  "findings": [
    {"statement": "DPYSL5 lacks the metal-cofactor-binding residues essential for dihydropyrimidinase activity.",
     "supporting_text": CAUTION_TXT},
    {"statement": "DPYSL5 belongs to the metallo-dependent hydrolase superfamily and negatively regulates dendrite outgrowth.",
     "supporting_text": SIM_TXT}]},
]

d["core_functions"] = [
 {"description": (
   "Catalytically inactive CRMP-family cytoskeletal regulator that negatively regulates "
   "dendrite/neurite outgrowth and morphogenesis during neuronal development. Acts within "
   "the semaphorin/collapsin growth-cone signalling system and through homo- and "
   "hetero-oligomerization with other CRMPs (notably DPYSL2/CRMP2); it has lost the ancestral "
   "dihydropyrimidinase activity of the family."),
  "directly_involved_in": [
    {"id": "GO:0050774", "label": "negative regulation of dendrite morphogenesis"}],
  "locations": [{"id": "GO:0005829", "label": "cytosol"},
                {"id": "GO:0030425", "label": "dendrite"}],
  "supported_by": [
    {"reference_id": "PMID:33894126",
     "supporting_text": "Missense variants in DPYSL5 cause a neurodevelopmental disorder with corpus callosum agenesis and cerebellar abnormalities."},
    {"reference_id": UNI, "supporting_text": FUNC_TXT}]},
]

d["suggested_questions"] = [
 {"question": "Does DPYSL5/CRMP5 retain any residual or neofunctionalized enzymatic activity, or is it strictly a non-catalytic scaffold? The UniProt CAUTION asserts loss of dihydropyrimidinase activity, but no assay has excluded all hydrolase activities."},
 {"question": "What is the molecular mechanism by which DPYSL5 negatively regulates dendrite outgrowth - does it antagonize CRMP2 (DPYSL2) within hetero-oligomers, and is this mediated through microtubule dynamics?"},
]
d["suggested_experiments"] = [
 {"hypothesis": "DPYSL5 has no metallo-hydrolase activity of any kind, consistent with loss of the metal-binding site.",
  "description": "Express and purify recombinant DPYSL5 and assay a panel of amidohydrolase/C-N hydrolase substrates (including dihydropyrimidinase substrates) with and without divalent metal supplementation; compare to active DPYS as a positive control."},
 {"hypothesis": "DPYSL5 negatively regulates dendrite outgrowth by antagonizing CRMP2 in hetero-oligomers.",
  "description": "Test dendrite outgrowth in neurons co-expressing DPYSL5 and CRMP2 variants that disrupt hetero-oligomerization, quantifying dendrite number/length."},
]

P.write_text("# yaml-language-server: $schema=../../../src/ai_gene_review/schema/gene_review.yaml\n" +
             yaml.dump(d, sort_keys=False, default_flow_style=False, allow_unicode=True, width=100))
print("wrote", P, "with", len(anns), "reviewed annotations")
