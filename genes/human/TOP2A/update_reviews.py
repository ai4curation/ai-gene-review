#!/usr/bin/env python3
"""Script to systematically update TOP2A annotation reviews."""

import yaml
from pathlib import Path

# Load the current YAML file
yaml_file = Path("/Users/cjm/repos/ai-gene-review/genes/human/TOP2A/TOP2A-ai-review.yaml")
with open(yaml_file) as f:
    data = yaml.safe_load(f)

# Define reviews for each GO term
reviews = {
    # MOLECULAR FUNCTIONS - Core catalytic activity
    "GO:0003918": {  # DNA topoisomerase type II (double strand cut, ATP-hydrolyzing) activity
        "summary": "This is the core molecular function of TOP2A. The enzyme catalyzes ATP-dependent double-strand DNA passage to resolve topological entanglements.",
        "action": "ACCEPT",
        "reason": "This correctly captures TOP2A's primary catalytic function as confirmed by biochemical assays (PMID:15491148, PMID:12711669, PMID:16611985, PMID:22323612).",
        "supported_by": [
            {
                "reference_id": "file:human/TOP2A/TOP2A-deep-research-openai.md",
                "supporting_text": "TOP2A encodes a critical enzyme that controls DNA topology. It can cut and rejoin double-stranded DNA to resolve DNA tangles and supercoils. This enzyme works as a homodimer and uses ATP hydrolysis to drive a strand-passage reaction"
            }
        ]
    },

    "GO:0003916": {  # DNA topoisomerase activity
        "summary": "This is a parent term of GO:0003918. Less specific than the type II annotation.",
        "action": "ACCEPT",
        "reason": "While correct, this is broader than GO:0003918 (DNA topoisomerase type II activity). Both annotations can coexist - the more specific IBA/IDA annotations capture the type II specificity, while this IEA annotation provides a general classification.",
        "supported_by": []
    },

    "GO:0003677": {  # DNA binding
        "summary": "TOP2A binds DNA as part of its mechanism, but this is too general for the core function.",
        "action": "ACCEPT",
        "reason": "TOP2A does bind DNA directly as confirmed by biochemical studies (PMID:12079377, PMID:10788521, PMID:9049244, PMID:22323612). However, this is a very general molecular function term. The enzyme's DNA binding is integral to its topoisomerase activity, and this annotation provides useful but non-specific information about the protein's molecular capabilities.",
        "supported_by": [
            {
                "reference_id": "PMID:22323612",
                "supporting_text": "DNA binding and bending activity demonstrated for human topoisomerase IIα"
            }
        ]
    },

    "GO:0003682": {  # chromatin binding
        "summary": "TOP2A binds chromatin, especially during mitosis when it is a major chromosome scaffold component.",
        "action": "ACCEPT",
        "reason": "Well-supported by experimental evidence (PMID:9049244). The deep research emphasizes that 'Topo IIα is a major component of the mitotic chromosome scaffold' and 'proteomic analyses of isolated human chromosomes identified Topo IIα as a major scaffold protein'. This binding is functionally important for chromosome structure.",
        "supported_by": [
            {
                "reference_id": "file:human/TOP2A/TOP2A-deep-research-openai.md",
                "supporting_text": "Topo IIα is a major component of the mitotic chromosome scaffold. Proteomic analyses of isolated human chromosomes identified Topo IIα as a major scaffold protein that remains bound after high-salt extractions, consistent with an architectural role"
            }
        ]
    },

    "GO:0008301": {  # DNA binding, bending
        "summary": "TOP2A bends DNA as part of its catalytic mechanism.",
        "action": "ACCEPT",
        "reason": "Directly demonstrated in PMID:22323612, which showed that 'DNA cleavage and opening reactions of human topoisomerase IIα are regulated via Mg2+-mediated dynamic bending of gate-DNA'. This bending is mechanistically important for the strand passage reaction.",
        "supported_by": [
            {
                "reference_id": "PMID:22323612",
                "supporting_text": "DNA cleavage and opening reactions of human topoisomerase IIα are regulated via Mg2+-mediated dynamic bending of gate-DNA"
            }
        ]
    },

    "GO:0008094": {  # ATP-dependent activity, acting on DNA
        "summary": "TOP2A's catalytic activity is ATP-dependent.",
        "action": "ACCEPT",
        "reason": "Correct and supported by PMID:12079377. This is a broader term than GO:0003918 but accurately describes the ATP-dependent nature of TOP2A's DNA manipulation activity. The enzyme uses ATP hydrolysis to drive conformational changes needed for strand passage.",
        "supported_by": [
            {
                "reference_id": "file:human/TOP2A/TOP2A-deep-research-openai.md",
                "supporting_text": "This ATP-dependent double-strand passage reaction is the hallmark of Topo IIα's catalytic function. Each Topo IIα monomer contributes an active-site tyrosine that cleaves one strand of the DNA duplex. The enzyme dimer then undergoes a large conformational change (powered by ATP binding and hydrolysis)"
            }
        ]
    },

    "GO:0005524": {  # ATP binding
        "summary": "TOP2A binds ATP as required for its catalytic cycle.",
        "action": "ACCEPT",
        "reason": "TOP2A contains an N-terminal ATPase domain and requires ATP for its strand passage mechanism. While very general, this is correct.",
        "supported_by": [
            {
                "reference_id": "file:human/TOP2A/TOP2A-deep-research-openai.md",
                "supporting_text": "The enzyme's N-terminal domain contains an ATPase motor (a member of the GHKL ATPase family). Binding of ATP at the N-terminal domains brings the dimer together and is allosterically transmitted to the DNA-gate in the core, triggering cleavage and strand passage"
            }
        ]
    },

    "GO:0000287": {  # magnesium ion binding
        "summary": "Mg2+ is a cofactor required for TOP2A's DNA cleavage activity.",
        "action": "ACCEPT",
        "reason": "Directly demonstrated in PMID:22323612. Mg2+ ions are essential cofactors for the DNA cleavage reaction and regulate the enzyme's mechanism.",
        "supported_by": [
            {
                "reference_id": "PMID:22323612",
                "supporting_text": "Mg2+-mediated dynamic bending of gate-DNA regulates DNA cleavage and opening reactions"
            }
        ]
    },

    "GO:0046872": {  # metal ion binding
        "summary": "TOP2A binds metal ions (Mg2+) as cofactors.",
        "action": "ACCEPT",
        "reason": "This is a parent term of GO:0000287 (magnesium ion binding). Both annotations are correct, with the Mg2+ term being more specific.",
        "supported_by": []
    },

    "GO:0042803": {  # protein homodimerization activity
        "summary": "TOP2A functions as a homodimer.",
        "action": "ACCEPT",
        "reason": "Well-established that TOP2A operates as a homodimer. PMID:10473615 specifically identified dimerization regions. The deep research states 'This enzyme works as a homodimer' and 'The enzyme operates as a dimeric molecular clamp'.",
        "supported_by": [
            {
                "reference_id": "file:human/TOP2A/TOP2A-deep-research-openai.md",
                "supporting_text": "This enzyme works as a homodimer. The enzyme operates as a dimeric molecular clamp. Each Topo IIα monomer contributes an active-site tyrosine that cleaves one strand of the DNA duplex"
            }
        ]
    },

    "GO:0046982": {  # protein heterodimerization activity
        "summary": "TOP2A can form heterodimers with TOP2B or truncated isoforms.",
        "action": "ACCEPT",
        "reason": "Supported by PMID:10473615. While TOP2A primarily functions as a homodimer, it can heterodimerize with TOP2B or with truncated isoforms, which is relevant for some cellular contexts and drug resistance mechanisms.",
        "supported_by": []
    },

    "GO:0005080": {  # protein kinase C binding
        "summary": "TOP2A interacts with protein kinase C.",
        "action": "ACCEPT",
        "reason": "Demonstrated in PMID:16611985, which showed that 'Protein kinase C delta activates topoisomerase IIα to induce apoptotic cell death in response to DNA damage'. This interaction is functionally relevant for regulation.",
        "supported_by": [
            {
                "reference_id": "PMID:16611985",
                "supporting_text": "Protein kinase C delta activates topoisomerase IIα to induce apoptotic cell death in response to DNA damage"
            }
        ]
    },

    "GO:0043130": {  # ubiquitin binding
        "summary": "TOP2A binds ubiquitin.",
        "action": "ACCEPT",
        "reason": "Demonstrated in PMID:15965487 in the context of BRCA1-mediated decatenation. This may be relevant for regulation or protein-protein interactions.",
        "supported_by": []
    },

    "GO:0003723": {  # RNA binding
        "summary": "TOP2A was identified in RNA-binding proteome studies.",
        "action": "ACCEPT",
        "reason": "Identified by HDA (high-throughput direct assay) in PMID:22681889. TOP2A was found in mRNA-bound proteome. While not a primary function, this may reflect associations in ribonucleoprotein complexes or non-canonical roles.",
        "supported_by": [
            {
                "reference_id": "GO_REF:0000052",
                "supporting_text": "Identified in high-throughput mRNA-bound proteome study"
            }
        ]
    },

    "GO:0016853": {  # isomerase activity
        "summary": "Topoisomerases are classified as isomerases (EC 5.x.x.x).",
        "action": "ACCEPT",
        "reason": "This is the general enzyme class for topoisomerases. TOP2A is EC 5.6.2.2, which is an isomerase that changes DNA topology. This parent term is correct but very broad.",
        "supported_by": []
    },

    "GO:0000166": {  # nucleotide binding
        "summary": "TOP2A binds nucleotides (ATP).",
        "action": "ACCEPT",
        "reason": "This is a very general parent term of ATP binding. Correct but uninformative compared to more specific terms.",
        "supported_by": []
    },

    "GO:0005515": {  # protein binding (multiple IPI annotations)
        "summary": "TOP2A interacts with numerous proteins.",
        "action": "REMOVE",
        "reason": "Per curation guidelines, 'protein binding' is too vague and should be avoided. TOP2A does interact with many proteins (BRCA1, PKC, histone deacetylase, 14-3-3, p53, etc.) as documented in the many PMIDs, but the generic 'protein binding' term provides no useful functional information. More specific binding terms (like GO:0005080 protein kinase C binding) should be retained, but these generic IPI annotations should be removed.",
        "supported_by": []
    },

    # BIOLOGICAL PROCESSES - Core functions
    "GO:0006265": {  # DNA topological change
        "summary": "This is the direct biological process result of TOP2A's catalytic activity.",
        "action": "ACCEPT",
        "reason": "This accurately describes what TOP2A does - it changes DNA topology by resolving supercoils and catenanes. Directly demonstrated in PMID:22323612 and confirmed throughout the literature as the core biological process mediated by the enzyme.",
        "supported_by": [
            {
                "reference_id": "file:human/TOP2A/TOP2A-deep-research-openai.md",
                "supporting_text": "Through this mechanism, TOP2A unties DNA knots, relieves supercoiling tension, and decatenates (unlinks) intertwined DNA molecules. By changing DNA linking number in steps of two, Topo IIα can both relax positive/negative supercoils and untangle concatenated DNA rings"
            }
        ]
    },

    "GO:0007059": {  # chromosome segregation
        "summary": "TOP2A is essential for chromosome segregation in mitosis.",
        "action": "ACCEPT",
        "reason": "Core function demonstrated in multiple studies (PMID:11136718, PMID:15456904, PMID:15965487). TOP2A decatenates sister chromatids allowing them to separate during anaphase. The deep research emphasizes this is 'absolutely required' and 'essential for cell viability' in dividing cells.",
        "supported_by": [
            {
                "reference_id": "file:human/TOP2A/TOP2A-deep-research-openai.md",
                "supporting_text": "During prophase and metaphase, Topo IIα localizes to chromosome axes and centromeric regions, where it resolves the last DNA catenanes holding sister chromatids together. Experimental depletion or inhibition of TOP2A prior to mitosis causes severe defects: chromosomes fail to achieve proper compaction and remain connected by DNA strands, leading to anaphase bridges or chromosome breakage"
            }
        ]
    },

    "GO:0000819": {  # sister chromatid segregation
        "summary": "More specific than chromosome segregation - TOP2A decatenates sister chromatids.",
        "action": "ACCEPT",
        "reason": "This IBA annotation is more specific than GO:0007059 and correctly emphasizes the sister chromatid decatenation function. This is a core role of TOP2A in mitosis.",
        "supported_by": [
            {
                "reference_id": "file:human/TOP2A/TOP2A-deep-research-openai.md",
                "supporting_text": "It can also untangle interlinked sister chromatids after DNA replication – a process known as decatenation. TOP2A is required to alleviate topological stress. By resolving torsional strain and decatenating replicated DNA, TOP2A enables replication to complete and prepares chromosomes for segregation"
            }
        ]
    },

    "GO:0030261": {  # chromosome condensation
        "summary": "TOP2A contributes to mitotic chromosome condensation.",
        "action": "ACCEPT",
        "reason": "Well-supported. The deep research states 'Topo IIα is essential for the condensation and segregation of mitotic chromosomes' and 'TOP2A becomes a component of mitotic chromosomes... contributes to the structural integrity of condensed chromosomes'. This is both a structural and enzymatic role.",
        "supported_by": [
            {
                "reference_id": "file:human/TOP2A/TOP2A-deep-research-openai.md",
                "supporting_text": "Topo IIα is essential for the condensation and segregation of mitotic chromosomes. Topo IIα becomes a component of mitotic chromosomes and contributes to the structural integrity of condensed chromosomes. Acute degradation of Topo IIα in mitotic human cells leads to aberrant chromosome morphology"
            }
        ]
    },

    "GO:0030263": {  # apoptotic chromosome condensation
        "summary": "TOP2A is involved in chromosome condensation during apoptosis.",
        "action": "ACCEPT",
        "reason": "Demonstrated in PMID:10959840, which showed 'DNA topoisomerase IIα interacts with CAD nuclease and is involved in chromatin condensation during apoptotic execution'. This is a specific role in apoptosis.",
        "supported_by": [
            {
                "reference_id": "PMID:10959840",
                "supporting_text": "DNA topoisomerase IIα interacts with CAD nuclease and is involved in chromatin condensation during apoptotic execution"
            }
        ]
    },

    "GO:0006325": {  # chromatin organization
        "summary": "TOP2A contributes to chromatin structure through its topoisomerase activity and scaffold role.",
        "action": "ACCEPT",
        "reason": "Supported by PMID:12711669 (IMP evidence). TOP2A affects chromatin organization both through resolving topological stress and as a structural chromosome scaffold component. This is a broader term that encompasses its roles in condensation and decatenation.",
        "supported_by": [
            {
                "reference_id": "file:human/TOP2A/TOP2A-deep-research-openai.md",
                "supporting_text": "Topo IIα can drive chromatin condensation via a phase-transition mechanism, requiring its CTD and ATPase activity. The CTD can mediate liquid–liquid phase separation with DNA and other proteins, and this condensation activity can modulate its catalytic function and impact chromatin organization"
            }
        ]
    },

    "GO:0000712": {  # resolution of meiotic recombination intermediates
        "summary": "TOP2A resolves DNA entanglements during meiotic recombination.",
        "action": "ACCEPT",
        "reason": "IBA annotation suggesting TOP2A orthologs function in resolving meiotic recombination intermediates. While TOP2A is highly expressed in proliferating cells, it is also expressed in germline cells and could resolve topologically complex DNA structures arising from recombination.",
        "supported_by": []
    },

    "GO:0007143": {  # female meiotic nuclear division
        "summary": "TOP2A function in female meiosis.",
        "action": "ACCEPT",
        "reason": "IEA annotation from ortholog transfer (GO_REF:0000107). While specific to female meiosis, this is consistent with TOP2A's general role in chromosome segregation during cell division. Less well-characterized than mitotic roles but plausible.",
        "supported_by": []
    },

    "GO:0006974": {  # DNA damage response
        "summary": "TOP2A participates in DNA damage response signaling.",
        "action": "ACCEPT",
        "reason": "Demonstrated in PMID:16611985 showing TOP2A activation in response to DNA damage via PKC delta signaling. TOP2A's DNA cleavage activity can also trigger DNA damage checkpoints when the enzyme is inhibited by drugs.",
        "supported_by": [
            {
                "reference_id": "PMID:16611985",
                "supporting_text": "Protein kinase C delta activates topoisomerase IIα to induce apoptotic cell death in response to DNA damage"
            }
        ]
    },

    "GO:0043065": {  # positive regulation of apoptotic process
        "summary": "TOP2A activation can promote apoptosis.",
        "action": "ACCEPT",
        "reason": "Demonstrated in PMID:16611985 in the context of DNA damage response. When activated by PKC delta, TOP2A activity contributes to apoptotic cell death. This is a context-dependent function.",
        "supported_by": []
    },

    "GO:0006259": {  # DNA metabolic process
        "summary": "Very broad parent term for DNA-related processes.",
        "action": "ACCEPT",
        "reason": "This is an extremely general term from IEA (InterPro-based annotation). While correct, it provides minimal information compared to more specific terms like DNA topological change or chromosome segregation.",
        "supported_by": []
    },

    "GO:0045870": {  # positive regulation of single stranded viral RNA replication via double stranded DNA intermediate
        "summary": "TOP2A was shown to affect HIV-1 replication.",
        "action": "KEEP_AS_NON_CORE",
        "reason": "Demonstrated in PMID:16712776 studying HIV-1 replication. This is a very specific process involving retroviruses and represents a non-core, context-specific function. The term is oddly specific for what is likely a general role of TOP2A in resolving topological stress during reverse transcription/integration.",
        "supported_by": []
    },

    "GO:0042752": {  # regulation of circadian rhythm
        "summary": "TOP2A may play a role in circadian rhythm regulation.",
        "action": "KEEP_AS_NON_CORE",
        "reason": "IEA and ISS annotations suggest a role in circadian regulation. This is mentioned in deep research but is peripheral to core function. May relate to transcriptional regulation of clock genes or cell cycle timing.",
        "supported_by": []
    },

    "GO:0048511": {  # rhythmic process
        "summary": "Parent term of circadian rhythm regulation.",
        "action": "KEEP_AS_NON_CORE",
        "reason": "Very broad term related to GO:0042752. Peripheral to core function.",
        "supported_by": []
    },

    "GO:0045944": {  # positive regulation of transcription by RNA polymerase II
        "summary": "TOP2A may affect transcription regulation.",
        "action": "KEEP_AS_NON_CORE",
        "reason": "IEA annotation from ortholog data. While TOP2A can affect transcription by resolving topological stress, and has been implicated in Wnt/β-catenin signaling (PMID:35012441), direct transcriptional regulation is not a primary function. TOP2B is the main topoisomerase II isoform for transcriptional roles.",
        "supported_by": [
            {
                "reference_id": "file:human/TOP2A/TOP2A-deep-research-openai.md",
                "supporting_text": "TOP2A and TOP2B share the core mechanism but differ in regulation and context: TOP2A is cell-cycle regulated and essential for cell proliferation, whereas TOP2B is expressed more constitutively for transcriptional roles. However, in rapidly dividing cells, Topo IIα likely contributes significantly to managing transcription-induced supercoils"
            }
        ]
    },

    "GO:0002244": {  # hematopoietic progenitor cell differentiation
        "summary": "TOP2A expression in hematopoietic development.",
        "action": "KEEP_AS_NON_CORE",
        "reason": "IEA annotation from Ensembl ortholog transfer. This likely reflects TOP2A's general requirement in proliferating cells rather than a specific developmental function. Any rapidly dividing hematopoietic progenitors would require TOP2A.",
        "supported_by": []
    },

    "GO:0040016": {  # embryonic cleavage
        "summary": "TOP2A function in early embryonic cell divisions.",
        "action": "KEEP_AS_NON_CORE",
        "reason": "IEA annotation. TOP2A would be required for rapid cell divisions during embryonic cleavage, but this is a developmental context rather than a specialized function.",
        "supported_by": []
    },

    # CELLULAR COMPONENTS
    "GO:0005634": {  # nucleus
        "summary": "TOP2A is predominantly nuclear.",
        "action": "ACCEPT",
        "reason": "Well-established localization supported by multiple IDA studies (PMID:9155056, PMID:10959840, PMID:10788521, PMID:16611985). The deep research states 'Topo IIα is predominantly a nuclear enzyme. It localizes to the cell nucleus, where the chromosomal DNA is housed'. Contains multiple nuclear localization sequences.",
        "supported_by": [
            {
                "reference_id": "file:human/TOP2A/TOP2A-deep-research-openai.md",
                "supporting_text": "Topo IIα is predominantly a nuclear enzyme. It localizes to the cell nucleus, where the chromosomal DNA is housed. The protein contains multiple Nuclear Localization Sequences (NLS) in its C-terminal domain that ensure its import into the nucleus"
            }
        ]
    },

    "GO:0005654": {  # nucleoplasm
        "summary": "TOP2A localizes to nucleoplasm in interphase.",
        "action": "ACCEPT",
        "reason": "Multiple IDA studies confirm nucleoplasmic localization (PMID:8299728, PMID:9049244, GO_REF:0000052). Also TAS evidence from Reactome pathways. This is where TOP2A functions during S-phase replication.",
        "supported_by": [
            {
                "reference_id": "file:human/TOP2A/TOP2A-deep-research-openai.md",
                "supporting_text": "In interphase cells, immunofluorescence studies show Topo IIα distributed throughout the nucleus. During S-phase, Topo IIα likely colocalizes with replication foci to remove supercoils and catenanes"
            }
        ]
    },

    "GO:0005730": {  # nucleolus
        "summary": "TOP2A has been detected in nucleoli.",
        "action": "ACCEPT",
        "reason": "Demonstrated by multiple IDA studies (PMID:8299728, PMID:9049244, PMID:9155056, PMID:17567603, GO_REF:0000052). While not the primary site of function, TOP2A is found in nucleoli, possibly related to ribosomal DNA topology.",
        "supported_by": []
    },

    "GO:0005737": {  # cytoplasm
        "summary": "Some TOP2A detected in cytoplasm.",
        "action": "ACCEPT",
        "reason": "Demonstrated by IDA in PMID:9155056. While primarily nuclear, some TOP2A may be in cytoplasm during transit or in specific cell types. Less significant than nuclear localization.",
        "supported_by": []
    },

    "GO:0000228": {  # nuclear chromosome
        "summary": "TOP2A associates with nuclear chromosomes.",
        "action": "ACCEPT",
        "reason": "Demonstrated in PMID:9049244. This is accurate - TOP2A binds to chromosomes particularly during mitosis when it is a major scaffold component.",
        "supported_by": []
    },

    "GO:0000775": {  # chromosome, centromeric region
        "summary": "TOP2A enriched at centromeres.",
        "action": "ACCEPT",
        "reason": "IEA annotation. The deep research mentions TOP2A 'concentrate[s] along metaphase chromosome axes and at centromeric regions, which are last to be decatenated'. Centromeric localization is functionally important for final sister chromatid separation.",
        "supported_by": [
            {
                "reference_id": "file:human/TOP2A/TOP2A-deep-research-openai.md",
                "supporting_text": "As cells progress to mitosis, Topo IIα becomes a component of mitotic chromosomes – it has been observed to concentrate along metaphase chromosome axes and at centromeric regions, which are last to be decatenated"
            }
        ]
    },

    "GO:0000793": {  # condensed chromosome
        "summary": "TOP2A is a major component of condensed mitotic chromosomes.",
        "action": "ACCEPT",
        "reason": "Well-supported. The deep research extensively describes TOP2A as 'a major component of the mitotic chromosome scaffold' and 'the most abundant scaffold protein by mass' on condensed chromosomes.",
        "supported_by": [
            {
                "reference_id": "file:human/TOP2A/TOP2A-deep-research-openai.md",
                "supporting_text": "Topo IIα is a major component of the mitotic chromosome scaffold – scaffold proteins such as condensin complexes and kinesin KIF4A co-localize on chromatid cores, and Topo IIα is the most abundant scaffold protein by mass"
            }
        ]
    },

    "GO:0009330": {  # DNA topoisomerase type II (double strand cut, ATP-hydrolyzing) complex
        "summary": "TOP2A forms a dimeric complex.",
        "action": "ACCEPT",
        "reason": "Demonstrated in PMID:10473615. TOP2A functions as a homodimeric complex, which is the active form of the enzyme.",
        "supported_by": []
    },

    "GO:0032991": {  # protein-containing complex
        "summary": "TOP2A is found in protein complexes.",
        "action": "ACCEPT",
        "reason": "Demonstrated in PMID:16611985. This is very general but correct - TOP2A interacts with many proteins and is part of various complexes (e.g., with DHX9, condensins, etc.).",
        "supported_by": []
    },

    "GO:1990904": {  # ribonucleoprotein complex
        "summary": "TOP2A found in ribonucleoprotein complexes.",
        "action": "ACCEPT",
        "reason": "Demonstrated in PMID:12711669 showing interaction with RNA helicase A (DHX9). This may reflect functional interactions during transcription or RNA processing.",
        "supported_by": []
    },

    "GO:0005814": {  # centriole
        "summary": "TOP2A detected at centrioles.",
        "action": "ACCEPT",
        "reason": "Demonstrated in PMID:9049244 during cell cycle progression. This is a minor localization compared to chromosomal localization but has been observed.",
        "supported_by": []
    },
}

# Update annotations
for annot in data["existing_annotations"]:
    go_id = annot["term"]["id"]
    if go_id in reviews:
        review_data = reviews[go_id]
        annot["review"] = {
            "summary": review_data["summary"],
            "action": review_data["action"],
            "reason": review_data["reason"]
        }
        if review_data.get("supported_by"):
            annot["review"]["supported_by"] = review_data["supported_by"]
    elif go_id == "GO:0005515":  # Handle all protein binding annotations
        annot["review"] = reviews["GO:0005515"]

# Save updated YAML
with open(yaml_file, 'w') as f:
    yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True, width=120)

print("Updated all annotation reviews!")
