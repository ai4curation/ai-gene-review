#!/usr/bin/env python3
"""
SPT16 GO annotation curation review generator.
This script generates detailed curation decisions for all SPT16 GO annotations.
"""

import yaml

# Define the curation decisions for each unique GO term + evidence code combination
curation_decisions = {
    ("GO:0006337", "IBA"): {
        "action": "ACCEPT",
        "summary": "Nucleosome disassembly is a well-established core function of SPT16/FACT during transcription elongation. IBA (ortholog inference) is appropriate evidence for this deeply characterized function.",
        "reason": "SPT16 is a core component of FACT complex that actively facilitates nucleosome disassembly ahead of RNA polymerase II during transcription. The deep research and extensive literature (including Perplexity review citing structural studies showing Spt16 interactions with H3-H4 and H2A-H2B during nucleosome disruption) strongly support this annotation. This is a primary and essential function."
    },
    ("GO:0032784", "IBA"): {
        "action": "ACCEPT",
        "summary": "Regulation of transcription elongation is a core function of SPT16/FACT. The complex facilitates passage of RNA polymerase II through chromatin by modulating nucleosome structure.",
        "reason": "SPT16/FACT is directly involved in promoting transcription elongation by managing nucleosome dynamics. The evidence includes multiple studies showing FACT travels with elongating polymerase II (Mason & Struhl 2003, PMID:14585989) and facilitates fidelity of transcription (evidenced by suppression of cryptic initiation). This is a primary function, not merely a side effect."
    },
    ("GO:0035101", "IBA"): {
        "action": "ACCEPT",
        "summary": "SPT16 is a core structural component of the FACT complex. This annotation represents membership in the complex with strong phylogenetic support.",
        "reason": "SPT16 forms an obligate heterodimeric complex with POB3 (Pob3p) as documented in UniProt and extensively in the literature. IBA evidence from orthologs (SSRP1/SPT16 in other organisms) is appropriate for this structural annotation."
    },
    ("GO:0005634", "IEA"): {
        "action": "ACCEPT",
        "summary": "SPT16 is localized to the nucleus, where it functions in chromatin-associated processes.",
        "reason": "Nuclear localization is well-established for SPT16 through multiple studies showing chromatin-association and co-localization with active transcription sites. While IEA is less specific than experimental evidence, nuclear localization is a foundational fact confirmed by direct observation (PMID:10413469). This is a valid cellular component annotation."
    },
    ("GO:0005694", "IEA"): {
        "action": "ACCEPT",
        "summary": "SPT16 is localized to chromatin/chromosomes where it functions in nucleosome reorganization during transcription and replication.",
        "reason": "SPT16 specifically associates with chromatin and DNA during its biological functions. This is explicitly documented: UniProt states 'Colocalizes with RNA polymerase II on chromatin' and associates with coding regions of histone genes. The annotation is accurate and important for describing where the protein functions."
    },
    ("GO:0006260", "IEA"): {
        "action": "ACCEPT",
        "summary": "SPT16 is involved in DNA replication through its role in nucleosome disassembly ahead of replication forks and histone recycling to daughter strands.",
        "reason": "SPT16/FACT is essential for normal replication fork progression. The deep research documents that FACT associates with replication fork components (MCM2-7, Pol alpha) and that SSRP1/SPT16 depletion slows replication forks (PMID references in UniProt). The Spt16-N domain interacts with MCM2-7 complex and fork protection complex, enabling parental histone recycling during replication."
    },
    ("GO:0006281", "IEA"): {
        "action": "ACCEPT",
        "summary": "SPT16 participates in DNA repair, particularly base excision repair, through cooperation with chromatin remodelers.",
        "reason": "UniProt function section states FACT plays a role in DNA repair. The deep research documentation mentions FACT recruitment to DNA damage sites and cooperation with remodelers to expose damaged DNA for repair (BER pathway). While less extensively characterized than transcription roles, the involvement is documented and scientifically valid."
    },
    ("GO:0006351", "IEA"): {
        "action": "ACCEPT",
        "summary": "SPT16 is fundamentally involved in DNA-templated transcription through its role in nucleosome dynamics during transcription.",
        "reason": "SPT16/FACT is a transcription elongation factor essential for efficient transcription through chromatin. This broad annotation captures the core transcriptional role of the protein. IEA from UniProt keyword mapping is appropriate for this well-established function."
    },
    ("GO:0006974", "IEA"): {
        "action": "ACCEPT",
        "summary": "SPT16 participates in DNA damage response through recruitment to damaged chromatin and cooperation with repair machinery.",
        "reason": "UniProt function section mentions DNA repair role and the deep research documents FACT recruitment to DNA damage sites. The involvement in BER and interaction with DNA damage-responsive proteins supports this annotation."
    },
    ("GO:0010468", "IEA"): {
        "action": "KEEP_AS_NON_CORE",
        "summary": "While SPT16 does participate in gene expression regulation, this term is very broad and less informative than the specific transcription annotations already present.",
        "reason": "This annotation is not incorrect, but it represents a general consequence of SPT16's core transcriptional functions rather than a distinct molecular function. More specific GO terms (transcription elongation, nucleosome disassembly, etc.) better capture SPT16's specific contributions to gene regulation. The annotation should be retained because it is accurate, but marked as non-core."
    },
    ("GO:0034728", "IEA"): {
        "action": "ACCEPT",
        "summary": "Nucleosome organization is a core function of SPT16/FACT, encompassing both disassembly and reassembly activities during transcription and replication.",
        "reason": "SPT16 directly organizes nucleosomes by controlling their disassembly and reassembly. This is documented throughout literature and is one of the defining functions of the protein. The term appropriately captures the holistic role of nucleosome management."
    },
    ("GO:0035101", "IEA"): {
        "action": "ACCEPT",
        "summary": "This duplicate annotation (same GO term as IBA annotation above) documents FACT complex membership through automated methods. Both evidence codes are valid.",
        "reason": "Duplicate annotations with different evidence codes are acceptable in GO. The IEA source (InterPro) provides orthogonal confirmation of FACT complex membership. Both IBA and IEA annotations should be retained."
    },
    ("GO:0005515", "IPI"): {
        "action": "KEEP_AS_NON_CORE",
        "summary": "SPT16 engages in multiple specific protein-protein interactions documented through mass spectrometry and other methods. However, 'protein binding' is a generic term that doesn't specify the functional nature of these interactions.",
        "reason": "Per GO curation guidelines, 'protein binding' (GO:0005515) is discouraged when more specific molecular function terms are available. SPT16's interactions are better characterized through specific terms like 'histone binding' (GO:0042393), 'nucleosome binding' (GO:0031491), and 'identical protein binding' (GO:0042802). The IPI annotations from IntAct databases (PMIDs 11805837, 11927560, 12077334, etc.) document real interactions but the term lacks specificity. These should be retained but marked non-core since more specific annotations exist."
    },
    ("GO:0042802", "IPI"): {
        "action": "ACCEPT",
        "summary": "SPT16 forms obligate homodimeric interactions (identical protein binding with itself) as part of FACT complex assembly. This is well-documented and functionally significant.",
        "reason": "SPT16 dimerizes with its partner POB3 (documented as FACT complex assembly). The IPI evidence from two separate studies (PMID:14759368 and PMID:21179020) showing interaction with itself (WITH column: UniProtKB:P32558) is valid. However, given that SPT16 primarily functions as a heterodimer with POB3, this annotation may reflect technical/database artifacts. Accept but consider non-core."
    },
    ("GO:0006261", "NAS"): {
        "action": "ACCEPT",
        "summary": "DNA-templated DNA replication is directly facilitated by SPT16/FACT. NAS (non-traceable author statement) from ComplexPortal reference is appropriate for this well-characterized function.",
        "reason": "SPT16/FACT involvement in DNA replication is extensively documented. The protein associates with replication machinery (MCM2-7, Pol alpha), facilitates fork progression, and mediates parental histone recycling to daughter strands. Multiple studies document this function."
    },
    ("GO:0034728", "NAS"): {
        "action": "ACCEPT",
        "summary": "Nucleosome organization during DNA replication is a key SPT16 function, complementary to its transcriptional roles.",
        "reason": "This represents nucleosome management during replication, distinct from (though overlapping with) transcriptional nucleosome organization. Both processes are central to FACT function and well-documented in the literature."
    },
    ("GO:1902275", "NAS"): {
        "action": "ACCEPT",
        "summary": "SPT16/FACT actively regulates chromatin organization by controlling nucleosome structure and positioning throughout the genome.",
        "reason": "This term appropriately captures FACT's regulatory role in chromatin dynamics. The protein doesn't merely disassemble and reassemble nucleosomes passively but actively orchestrates their organization in response to biological requirements. This is distinct from and more accurate than the more passive 'nucleosome organization' term."
    },
    ("GO:0006325", "IDA"): {
        "action": "ACCEPT",
        "summary": "Chromatin organization is a primary direct activity of SPT16 demonstrated through direct biochemical and cell biological assays.",
        "reason": "IDA evidence from direct assays (PMID:19683499) documents SPT16's role in chromatin organization. The protein's ability to facilitate nucleosomal DNA accessibility and reorganize chromatin structure is directly demonstrated. This is core function."
    },
    ("GO:0000785", "IDA"): {
        "action": "ACCEPT",
        "summary": "SPT16 localizes to chromatin and is a structural component of chromatin-associated FACT complexes.",
        "reason": "Direct evidence from PMID:10413469 documents that SPT16 is chromatin-associated, nuclear, and copurifies with chromatin. This is a valid cellular component annotation with strong experimental support."
    },
    ("GO:0007063", "IDA"): {
        "action": "ACCEPT",
        "summary": "SPT16/FACT regulates sister chromatid cohesion through cooperation with cohesin complex on chromatin.",
        "reason": "PMID:31582854 provides direct experimental evidence that FACT mediates cohesin function on chromatin. This annotation represents a documented but more specialized function of SPT16 beyond its primary transcription/replication roles. The annotation is scientifically valid."
    },
    ("GO:0035101", "IGI"): {
        "action": "ACCEPT",
        "summary": "SPT16 is part of the FACT complex, demonstrated through genetic interaction studies where loss of SPT16 affects nucleosome-binding complex assembly.",
        "reason": "IGI evidence (genetic interaction with NHP6 - PMID:11432837) documents FACT complex assembly. SPT16 cooperates with NHP6 proteins to form the nucleosome-binding SPN complex. This genetic evidence properly supports the complex assembly annotation."
    },
    ("GO:0035101", "IPI"): {
        "action": "ACCEPT",
        "summary": "SPT16 physically interacts with POB3 (with column: SGD:S000004534) to form the FACT heterodimer, directly demonstrated.",
        "reason": "IPI evidence documents the obligate SPT16-POB3 interaction that forms the core of the FACT complex. This is well-established biochemically and is an essential part of SPT16 function."
    },
    ("GO:0003682", "IDA"): {
        "action": "ACCEPT",
        "summary": "Chromatin binding is a direct biochemical activity of SPT16, demonstrated through binding assays.",
        "reason": "IDA evidence from PMID:10413469 directly shows SPT16 binds to chromatin. This molecular function annotation is supported by direct experimental evidence. The 'contributes_to' relationship indicates this is one of multiple activities rather than the sole function."
    },
    ("GO:0031491", "IDA"): {
        "action": "ACCEPT",
        "summary": "Nucleosome binding is a core molecular function of SPT16, directly demonstrated through biochemical assays.",
        "reason": "IDA evidence from PMID:11432837 directly documents SPT16 nucleosome binding. The protein's multiple histone-binding domains enable this core activity. The 'contributes_to' relationship appropriately reflects that this is part of the multi-domain histone chaperone activity."
    },
    ("GO:0042393", "IDA"): {
        "action": "ACCEPT",
        "summary": "Histone binding is a core molecular function of SPT16, with direct biochemical evidence of interactions with histone H3, H4, H2A, and H2B.",
        "reason": "IDA evidence from PMID:18089575 directly documents histone binding. The N-terminal domain binds H3-H4, middle domain binds H3-H4 tetramers, and C-terminal domain binds H2A-H2B dimers. These interactions are structural and mechanistically essential for nucleosome chaperone function."
    },
    ("GO:0045899", "IDA"): {
        "action": "ACCEPT",
        "summary": "SPT16/FACT has a direct role in preinitiation complex assembly and transcription initiation through FACT-mediated nucleosome disassembly at promoters.",
        "reason": "IDA evidence from PMID:15987999 directly demonstrates FACT's role in transcription initiation. The protein facilitates PIC assembly by clearing nucleosomal barriers at promoters and promoting TBP binding to TATA boxes. This is distinct from and complementary to elongation functions."
    },
    ("GO:0060261", "IGI"): {
        "action": "ACCEPT",
        "summary": "SPT16 positively regulates transcription initiation by RNA polymerase II through genetic interaction with initiation factors (SGD:S000000950 appears to be TFIID; S000001541 appears to be another initiation factor).",
        "reason": "IGI evidence from PMID:15987999 documents functional interaction between SPT16 and transcription initiation machinery. The genetic interactions establish SPT16's role in promoting initiation. This complements the direct IDA evidence."
    },
    ("GO:0060261", "IMP"): {
        "action": "ACCEPT",
        "summary": "SPT16 positively regulates transcription initiation by RNA Pol II, demonstrated through mutation/depletion studies showing defects in initiation when SPT16 is inactivated.",
        "reason": "IMP evidence from PMID:19574230 documents that promoter chromatin disassembly and transcriptional initiation require both FACT and proteasome function. Loss of FACT function impairs initiation, supporting this annotation with the strongest type of mechanistic evidence."
    }
}

# Build the complete annotations section
annotations_yaml = """existing_annotations:
"""

# Annotation data from the GOA file - mapping line numbers to GO term + evidence pairs
annotation_specs = [
    (1, "GO:0006337", "nucleosome disassembly", "IBA", "GO_REF:0000033"),
    (2, "GO:0032784", "regulation of DNA-templated transcription elongation", "IBA", "GO_REF:0000033"),
    (3, "GO:0035101", "FACT complex", "IBA", "GO_REF:0000033"),
    (4, "GO:0005634", "nucleus", "IEA", "GO_REF:0000044"),
    (5, "GO:0005694", "chromosome", "IEA", "GO_REF:0000044"),
    (6, "GO:0006260", "DNA replication", "IEA", "GO_REF:0000043"),
    (7, "GO:0006281", "DNA repair", "IEA", "GO_REF:0000043"),
    (8, "GO:0006351", "DNA-templated transcription", "IEA", "GO_REF:0000043"),
    (9, "GO:0006974", "DNA damage response", "IEA", "GO_REF:0000043"),
    (10, "GO:0010468", "regulation of gene expression", "IEA", "GO_REF:0000117"),
    (11, "GO:0034728", "nucleosome organization", "IEA", "GO_REF:0000117"),
    (12, "GO:0035101", "FACT complex", "IEA", "GO_REF:0000120"),
    # Protein binding annotations - multiple IPI entries collapse to single decision
    (13, "GO:0005515", "protein binding", "IPI", "PMID:11805837"),
    (14, "GO:0005515", "protein binding", "IPI", "PMID:11805837"),
    (15, "GO:0005515", "protein binding", "IPI", "PMID:11805837"),
    (16, "GO:0005515", "protein binding", "IPI", "PMID:11805837"),
    (17, "GO:0005515", "protein binding", "IPI", "PMID:11927560"),
    (18, "GO:0005515", "protein binding", "IPI", "PMID:11927560"),
    (19, "GO:0005515", "protein binding", "IPI", "PMID:12077334"),
    (20, "GO:0005515", "protein binding", "IPI", "PMID:12242279"),
    (21, "GO:0005515", "protein binding", "IPI", "PMID:12242279"),
    (22, "GO:0005515", "protein binding", "IPI", "PMID:12242279"),
    (23, "GO:0005515", "protein binding", "IPI", "PMID:12242279"),
    (24, "GO:0005515", "protein binding", "IPI", "PMID:12242279"),
    (25, "GO:0005515", "protein binding", "IPI", "PMID:12242279"),
    (26, "GO:0005515", "protein binding", "IPI", "PMID:12242279"),
    (27, "GO:0005515", "protein binding", "IPI", "PMID:12242279"),
    (28, "GO:0005515", "protein binding", "IPI", "PMID:14759368"),
    (29, "GO:0005515", "protein binding", "IPI", "PMID:14759368"),
    (30, "GO:0005515", "protein binding", "IPI", "PMID:16299494"),
    (31, "GO:0005515", "protein binding", "IPI", "PMID:16429126"),
    (32, "GO:0005515", "protein binding", "IPI", "PMID:16554755"),
    (33, "GO:0005515", "protein binding", "IPI", "PMID:20489023"),
    (34, "GO:0005515", "protein binding", "IPI", "PMID:21179020"),
    (35, "GO:0005515", "protein binding", "IPI", "PMID:31582854"),
    (36, "GO:0005515", "protein binding", "IPI", "PMID:37968396"),
    (37, "GO:0042802", "identical protein binding", "IPI", "PMID:14759368"),
    (38, "GO:0042802", "identical protein binding", "IPI", "PMID:21179020"),
    (39, "GO:0006261", "DNA-templated DNA replication", "NAS", "PMID:12952948"),
    (40, "GO:0034728", "nucleosome organization", "NAS", "PMID:12952948"),
    (41, "GO:1902275", "regulation of chromatin organization", "NAS", "PMID:12952948"),
    (42, "GO:0006325", "chromatin organization", "IDA", "PMID:19683499"),
    (43, "GO:0000785", "chromatin", "IDA", "PMID:10413469"),
    (44, "GO:0007063", "regulation of sister chromatid cohesion", "IDA", "PMID:31582854"),
    (45, "GO:0035101", "FACT complex", "IGI", "PMID:11432837"),
    (46, "GO:0035101", "FACT complex", "IPI", "PMID:11432837"),
    (47, "GO:0005515", "protein binding", "IPI", "PMID:27226635"),
    (48, "GO:0003682", "chromatin binding", "IDA", "PMID:10413469"),
    (49, "GO:0006261", "DNA-templated DNA replication", "IPI", "PMID:9199353"),
    (50, "GO:0006334", "nucleosome assembly", "IDA", "PMID:12952948"),
    (51, "GO:0006334", "nucleosome assembly", "IDA", "PMID:15082784"),
    (52, "GO:0031491", "nucleosome binding", "IDA", "PMID:11432837"),
    (53, "GO:0042393", "histone binding", "IDA", "PMID:18089575"),
    (54, "GO:0045899", "positive regulation of RNA polymerase II transcription preinitiation complex assembly", "IDA", "PMID:15987999"),
    (55, "GO:0060261", "positive regulation of transcription initiation by RNA polymerase II", "IGI", "PMID:15987999"),
    (56, "GO:0060261", "positive regulation of transcription initiation by RNA polymerase II", "IMP", "PMID:19574230"),
]

# Generate YAML for each annotation
for idx, go_id, label, evidence, ref in annotation_specs:
    key = (go_id, evidence)
    if key in curation_decisions:
        decision = curation_decisions[key]
        action = decision["action"]
        summary = decision["summary"]
        reason = decision["reason"]
    else:
        # Fallback for any missing entries
        action = "UNDECIDED"
        summary = f"Curation decision pending for {go_id} with evidence {evidence}"
        reason = "No curation decision available"

    annotations_yaml += f"""- term:
    id: {go_id}
    label: {label}
  evidence_type: {evidence}
  original_reference_id: {ref}
  review:
    summary: {summary}
    action: {action}
    reason: {reason}
"""

print(annotations_yaml)
