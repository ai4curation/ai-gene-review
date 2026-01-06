#!/usr/bin/env python3
"""
Script to update RAS2 annotation reviews with curation decisions.
"""
import yaml
from pathlib import Path

yaml_file = Path("/Users/cjm/repos/ai-gene-review/genes/yeast/RAS2/RAS2-ai-review.yaml")

# Load the YAML
with open(yaml_file) as f:
    data = yaml.safe_load(f)

# Define curation decisions
decisions = {
    # (GO:ID, evidence_type, reference) -> (action, reason_snippet, supported_by)

    # IBA Annotations
    ("GO:0005886", "IBA", "GO_REF:0000033"): (
        "ACCEPT",
        "IBA annotation confirmed by multiple IDA annotations. RAS2 is farnesylated and palmitoylated, essential for plasma membrane anchoring.",
        []
    ),
    ("GO:0007163", "IBA", "GO_REF:0000033"): (
        "ACCEPT",
        "RAS2 regulates cell polarity through protein localization to bud neck and Cdc42/MAPK signaling pathway controlling cell division morphogenesis.",
        []
    ),
    ("GO:0007265", "IBA", "GO_REF:0000033"): (
        "ACCEPT",
        "Core function of RAS2. Acts as primary regulator of adenylate cyclase and PKA signaling pathway.",
        []
    ),
    ("GO:0003924", "IBA", "GO_REF:0000033"): (
        "ACCEPT",
        "Core catalytic function. RAS2 hydrolyzes GTP to GDP, enabling regulation of downstream signaling.",
        []
    ),

    # IEA Annotations
    ("GO:0000166", "IEA", "GO_REF:0000043"): (
        "ACCEPT",
        "Appropriate computational annotation. RAS2 binds guanine nucleotides (GTP/GDP) as substrate for catalytic cycle.",
        []
    ),
    ("GO:0003924", "IEA", "GO_REF:0000120"): (
        "ACCEPT",
        "Valid InterPro-based inference. Multiple evidence types acceptable for same term.",
        []
    ),
    ("GO:0003925", "IEA", "GO_REF:0000003"): (
        "ACCEPT",
        "Appropriate parent term. RAS2 is a GTP-binding protein with GTPase activity (G protein).",
        []
    ),
    ("GO:0005525", "IEA", "GO_REF:0000120"): (
        "ACCEPT",
        "Appropriate computational annotation. RAS2 canonical substrate is GTP.",
        []
    ),
    ("GO:0005886", "IEA", "GO_REF:0000044"): (
        "ACCEPT",
        "Consistent with IBA and IDA evidence from subcellular localization mapping.",
        []
    ),
    ("GO:0007165", "IEA", "GO_REF:0000002"): (
        "ACCEPT",
        "Appropriate parent term for RAS2 signaling function.",
        []
    ),
    ("GO:0016020", "IEA", "GO_REF:0000002"): (
        "ACCEPT",
        "Appropriate parent term. RAS2 is a membrane-anchored protein.",
        []
    ),
    ("GO:0016787", "IEA", "GO_REF:0000043"): (
        "ACCEPT",
        "Appropriate parent term for GTPase activity (hydrolysis of phosphodiester bonds).",
        []
    ),
    ("GO:0097271", "IEA", "GO_REF:0000117"): (
        "REMOVE",
        "IEA annotation for specific subcellular localization is overly detailed for computational inference. Specific experimental evidence (IGI) already provided.",
        []
    ),

    # IPI Protein Binding Annotations - all removed per GO best practices
    ("GO:0005515", "IPI", "PMID:11805837"): (
        "REMOVE",
        "Generic protein binding term is non-informative. RAS1 interaction is properly described by signal transduction and protein localization terms. Remove per GO guidelines.",
        []
    ),
    ("GO:0005515", "IPI", "PMID:12782684"): (
        "REMOVE",
        "Generic protein binding term is non-informative. LTE1 recruitment to bud neck is captured by specific process terms (protein localization, cell division).",
        []
    ),
    ("GO:0005515", "IPI", "PMID:16554755"): (
        "REMOVE",
        "Generic protein binding term is non-informative per GO curation guidelines. Use specific process terms instead.",
        []
    ),
    ("GO:0005515", "IPI", "PMID:21073870"): (
        "REMOVE",
        "Generic protein binding term is non-informative. CDC25 GEF interaction is properly described through signal transduction pathways.",
        []
    ),
    ("GO:0005515", "IPI", "PMID:21457714"): (
        "REMOVE",
        "Generic protein binding term is non-informative. PKA regulation of RAS2 is captured by PKA signaling pathway terms.",
        []
    ),
    ("GO:0005515", "IPI", "PMID:23831759"): (
        "REMOVE",
        "Generic protein binding term is non-informative. YCF1 interaction not core to RAS2 function.",
        []
    ),

    # HDA Annotations
    ("GO:0005739", "HDA", "PMID:24769239"): (
        "KEEP_AS_NON_CORE",
        "Minor mitochondrial localization during respiratory growth. Not primary site of RAS2 signaling.",
        []
    ),
    ("GO:0071944", "HDA", "PMID:26928762"): (
        "KEEP_AS_NON_CORE",
        "General cell periphery localization. Less specific than plasma membrane.",
        []
    ),
    ("GO:0005886", "HDA", "PMID:11914276"): (
        "ACCEPT",
        "Proteomics evidence supporting plasma membrane localization.",
        []
    ),
    ("GO:0005886", "HDA", "PMID:16622836"): (
        "ACCEPT",
        "Plasma membrane proteome study confirming RAS2 localization.",
        []
    ),

    # IMP/IGI Experimental Process Annotations
    ("GO:0010603", "IMP", "PMID:21925385"): (
        "ACCEPT",
        "RAS2/PKA pathway regulates P body formation. PMID:21925385 demonstrates cAMP/PKA controls mRNA processing body assembly.",
        []
    ),
    ("GO:0042149", "IMP", "PMID:21925385"): (
        "ACCEPT",
        "RAS2 is critical regulator of nutrient starvation response. Loss of RAS2 leads to constitutive starvation response.",
        []
    ),
    ("GO:0016236", "IGI", "PMID:15016820"): (
        "MODIFY",
        "PMID:15016820 demonstrates RAS/PKA pathway INHIBITS autophagy during growth. Annotation reflects inhibitory relationship.",
        [{"term_id": "GO:0031406", "label": "negative regulation of autophagy"}]
    ),
    ("GO:0032258", "IMP", "PMID:15016820"): (
        "MODIFY",
        "PMID:15016820 demonstrates RAS/PKA pathway INHIBITS Cvt pathway during growth. Annotation should reflect inhibitory regulation.",
        [{"term_id": "GO:0051804", "label": "negative regulation of cytoplasm to vacuole targeting"}]
    ),
    ("GO:2000222", "IMP", "PMID:1547504"): (
        "ACCEPT",
        "Well-documented. RAS2 (especially constitutively active RAS2val19) promotes pseudohyphal growth in response to nitrogen starvation.",
        []
    ),
    ("GO:2000222", "IMP", "PMID:8643578"): (
        "ACCEPT",
        "PMID:8643578 demonstrates RAS2 signals via Cdc42/MAPK pathway to induce filamentous growth.",
        []
    ),
    ("GO:0005634", "IDA", "PMID:23127800"): (
        "ACCEPT",
        "PMID:23127800 demonstrates RAS2-GTP localizes to nucleus, supporting transcriptional regulation functions.",
        []
    ),
    ("GO:0005886", "IDA", "PMID:23127800"): (
        "ACCEPT",
        "Direct experimental evidence for plasma membrane localization confirmed by fluorescence imaging.",
        []
    ),
    ("GO:0097271", "IGI", "PMID:12782684"): (
        "ACCEPT",
        "PMID:12782684 demonstrates RAS2 recruits mitotic exit regulator Lte1 to bud cortex.",
        []
    ),
    ("GO:0000411", "IMP", "PMID:16292676"): (
        "UNDECIDED",
        "Insufficient information on mechanism. Paper addresses phosphoglucomutase activity and metabolic effects rather than direct transcriptional regulation.",
        []
    ),
    ("GO:0030437", "IMP", "PMID:2558958"): (
        "KEEP_AS_NON_CORE",
        "RAS2 plays permissive role in sporulation response to nutrient starvation. Not primary regulator of meiosis.",
        []
    ),
    ("GO:0032880", "IMP", "PMID:15917658"): (
        "ACCEPT",
        "PMID:15917658 demonstrates RAS2 collaborates with Cdc42/Cla4 to target and anchor Lte1 at bud cortex.",
        []
    ),
    ("GO:0005789", "IDA", "PMID:22575457"): (
        "ACCEPT",
        "PMID:22575457 demonstrates RAS2 localizes to ER membrane during lipid modification and trafficking to plasma membrane.",
        []
    ),
    ("GO:0005739", "IDA", "PMID:22575457"): (
        "KEEP_AS_NON_CORE",
        "PMID:22575457 shows minor mitochondrial localization. Not primary site of RAS2 signaling function.",
        []
    ),
    ("GO:0005886", "IDA", "PMID:20162532"): (
        "ACCEPT",
        "Direct experimental evidence. Chemical inhibition of CaaX protease disrupts RAS2 localization.",
        []
    ),
}

# Update annotations
for i, ann in enumerate(data['existing_annotations']):
    go_id = ann['term']['id']
    evidence = ann['evidence_type']
    ref = ann.get('original_reference_id', '')

    key = (go_id, evidence, ref)

    if key in decisions:
        action, reason, proposed_terms = decisions[key]

        # Initialize review section if needed
        if 'review' not in ann:
            ann['review'] = {}

        ann['review']['summary'] = f"Curation review of {ann['term']['label']} ({go_id}) with {evidence} evidence."
        ann['review']['action'] = action
        ann['review']['reason'] = reason

        if proposed_terms:
            ann['review']['proposed_replacement_terms'] = proposed_terms

        if 'supported_by' in ann['review']:
            del ann['review']['supported_by']

# Add description and core functions
if 'description' not in data or data['description'] == 'TODO: Add description for RAS2':
    data['description'] = 'RAS2 is a small GTPase that serves as the primary regulator of cAMP-dependent protein kinase (PKA) signaling. RAS2 cycles between GTP-bound (active) and GDP-bound (inactive) states, controlled by GEF CDC25 and GAPs IRA1/IRA2. RAS2 functions in nutrient sensing, growth control, stress response, replicative lifespan, and morphogenetic pathways (pseudohyphal growth, cell polarity).'

# Save the updated YAML
with open(yaml_file, 'w') as f:
    yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

print(f"Updated {yaml_file}")
print(f"Total annotations processed: {len(data['existing_annotations'])}")
