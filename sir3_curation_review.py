#!/usr/bin/env python3
"""
Comprehensive curation review for yeast SIR3 GO annotations.
This script generates the structured review for all 45 GO annotations.

SIR3 is a structural protein in the Sir2-3-4 silent chromatin complex.
Key distinction: SIR3 is NOT a catalytic deacetylase (that's SIR2).
SIR3 provides structural scaffolding through histone and DNA binding.
"""

annotations_review = {
    "GO:0006270": {
        "label": "DNA replication initiation",
        "evidence": "IBA",
        "action": "REMOVE",
        "summary": "IBA-seeded from phylogenetic inference. SIR3 directly localizes to euchromatic origins but suppresses MCM loading (negative regulation), not initiation.",
        "reason": "SIR3 does not participate in DNA replication initiation. SIR3 suppresses MCM loading and origin activity (GO:0008156), which is negative regulation, not initiation itself. Core machinery includes ORC, CDC6, CDT1, MCM2-7, not SIR3."
    },

    "GO:0003688_IBA": {
        "label": "DNA replication origin binding",
        "evidence": "IBA",
        "action": "REMOVE",
        "summary": "IBA-seeded annotation. While SIR3 does bind origin-adjacent nucleosomes, this is not origin binding per se - it is nucleosome/chromatin binding that happens to occur near origins.",
        "reason": "SIR3 binds nucleosomes adjacent to origins, not origins directly. Origins are DNA sequences recognized by ORC. SIR3 binding is to chromatin (GO:0003682) and nucleosomes (GO:0031491), not to the DNA origins themselves."
    },

    "GO:0033314": {
        "label": "mitotic DNA replication checkpoint signaling",
        "evidence": "IBA",
        "action": "REMOVE",
        "summary": "IBA-seeded annotation. No evidence that SIR3 has any role in checkpoint signaling mechanisms.",
        "reason": "SIR3 has no documented role in DNA damage checkpoints or checkpoint signaling. This IBA appears to be a spurious phylogenetic inference. SIR3's functions are in heterochromatin formation and chromatin structure, not checkpoint control."
    },

    "GO:0003677_IEA": {
        "label": "DNA binding",
        "evidence": "IEA",
        "action": "ACCEPT",
        "summary": "SIR3 directly binds DNA and double-stranded DNA (PMID:19099415). Nucleic acid binding is experimentally validated (PMID:17176117, EXP evidence code).",
        "reason": "SIR3 is experimentally shown to bind both double-stranded (PMID:19099415) and single-stranded DNA (PMID:19099415). This is a core molecular function. More specific terms (GO:0003690, GO:0003697) exist but DNA binding is also appropriate."
    },

    "GO:0003682_IEA": {
        "label": "chromatin binding",
        "evidence": "IEA",
        "action": "ACCEPT",
        "summary": "Critical molecular function. SIR3 binds chromatin and nucleosomes (PMID:19217406, PMID:18195043, PMID:19099415). This is the primary mechanism of SIR3 action.",
        "reason": "SIR3 directly binds to chromatin and nucleosomes, which is central to its function. IDA evidence exists (PMID:18195043). This is a core part of SIR3's mechanism for heterochromatin formation."
    },

    "GO:0005634_IEA": {
        "label": "nucleus",
        "evidence": "IEA",
        "action": "ACCEPT",
        "summary": "SIR3 localizes to the nucleus where it functions in heterochromatin formation at mating-type loci, telomeres, and euchromatic origins.",
        "reason": "SIR3 is exclusively nuclear. It functions at HML, HMR, telomeres, rDNA, and euchromatic origins, all nuclear loci. This is correct."
    },

    "GO:0005694_IEA": {
        "label": "chromosome",
        "evidence": "IEA",
        "action": "ACCEPT",
        "summary": "SIR3 localizes to chromosomes as a structural component of heterochromatin and silencing complexes.",
        "reason": "SIR3 is a chromosomal protein that functions at multiple chromosomal loci (telomeres, HM loci, rDNA, euchromatic origins)."
    },

    "GO:0006351_IEA": {
        "label": "DNA-templated transcription",
        "evidence": "IEA",
        "action": "MODIFY",
        "summary": "This term is vague and misleading. SIR3's role is in transcriptional repression/silencing (GO:0006354), not in the transcription process itself.",
        "reason": "GO:0006351 is DNA-templated transcription, which refers to the core process of RNA synthesis. SIR3 is not involved in the transcription machinery. Instead, SIR3 represses transcription at specific loci (HML, HMR, telomeres) by forming heterochromatin. GO:0006354 (negative regulation of transcription) or locus-specific terms (GO:0030466 for mating-type silencing) are more accurate.",
        "proposed_replacement_terms": [
            {"id": "GO:0006354", "label": "negative regulation of transcription, DNA-templated"},
            {"id": "GO:0030466", "label": "silent mating-type cassette heterochromatin formation"}
        ]
    },

    "GO:0005515_IPI_11689698": {
        "label": "protein binding",
        "evidence": "IPI",
        "action": "KEEP_AS_NON_CORE",
        "summary": "SIR3 binds RAP1 (PMID:11689698). However, protein binding is too vague - more specific MF terms exist for SIR3's binding interactions.",
        "reason": "GO:0005515 (protein binding) is uninformative per curation guidelines. SIR3 binds specific partners: SIR2, SIR4, RAP1 (all verified), and histones. These interactions are better captured by: identical protein binding (GO:0042802 for SIR3-SIR3), and nucleosome/histone binding terms."
    },

    "GO:0005515_IPI_11805837": {
        "label": "protein binding",
        "evidence": "IPI",
        "action": "KEEP_AS_NON_CORE",
        "summary": "Protein complex membership documented by mass spectrometry (PMID:11805837). Too vague compared to specific binding partners.",
        "reason": "IPI from complexomics study. More informative to list the actual binding partners and complex membership rather than generic protein binding."
    },

    "GO:0005515_IPI_16554755": {
        "label": "protein binding",
        "evidence": "IPI",
        "action": "KEEP_AS_NON_CORE",
        "summary": "Protein complex documented (PMID:16554755). Vague annotation.",
        "reason": "Generic protein binding annotation obscures the specifics of which proteins SIR3 binds."
    },

    "GO:0005515_IPI_16717101": {
        "label": "protein binding",
        "evidence": "IPI",
        "action": "KEEP_AS_NON_CORE",
        "summary": "SIR3 binding to SIR4 and interaction analysis (PMID:16717101). Vague.",
        "reason": "Uninformative without specifying binding partners."
    },

    "GO:0005515_IPI_21217703": {
        "label": "protein binding",
        "evidence": "IPI",
        "action": "KEEP_AS_NON_CORE",
        "summary": "RAP1 binding documented (PMID:21217703). Generic annotation.",
        "reason": "Protein binding is too vague. The specific interaction (RAP1 binding) should be noted but more specific MF terms are preferred."
    },

    "GO:0042802_16717101": {
        "label": "identical protein binding",
        "evidence": "IPI",
        "action": "ACCEPT",
        "summary": "SIR3 forms homodimers (PMID:16717101). This is a core structural feature essential for heterochromatin formation.",
        "reason": "SIR3 self-associates extensively to form oligomers (PMID:17176117). Homodimerization through the C-terminal winged helix domain (PMID:23299941) is critical for silencing function."
    },

    "GO:0042802_21179020": {
        "label": "identical protein binding",
        "evidence": "IPI",
        "action": "ACCEPT",
        "summary": "SIR3 homodimer formation confirmed by ChIP-chromatin association (PMID:21179020).",
        "reason": "Multiple lines of evidence confirm SIR3 homodimerization is essential for function."
    },

    "GO:0042802_23299941": {
        "label": "identical protein binding",
        "evidence": "IPI",
        "action": "ACCEPT",
        "summary": "SIR3 C-terminal winged helix domain (WH) mediates homodimerization (PMID:23299941), essential for heterochromatin formation.",
        "reason": "Structural evidence shows SIR3 WH domain dimerizes and this is required for silencing. This is a core structural function."
    },

    "GO:0031507_NAS": {
        "label": "heterochromatin formation",
        "evidence": "NAS",
        "action": "ACCEPT",
        "summary": "SIR3 is essential for heterochromatin formation at HML, HMR, telomeres, and rDNA. Core function documented in multiple studies.",
        "reason": "SIR3 is a core component of the Sir2-3-4 complex required for heterochromatin formation. This is a defining function."
    },

    "GO:0003676_EXP": {
        "label": "nucleic acid binding",
        "evidence": "EXP",
        "action": "ACCEPT",
        "summary": "Direct experimental evidence (PMID:17176117) that SIR3 binds nucleic acids. Domain organization studies confirm nucleic acid binding capability.",
        "reason": "EXP evidence from biochemical characterization. SIR3 directly binds both DNA and RNA. This is experimentally validated."
    },

    "GO:0003688_IDA_29795547": {
        "label": "DNA replication origin binding",
        "evidence": "IDA",
        "action": "REMOVE",
        "summary": "While SIR3 localizes to origins, it binds nucleosomes at origins, not origins themselves. Origins are DNA sequences bound by ORC.",
        "reason": "SIR3 binds chromatin/nucleosomes that are located near origins, not the origin DNA itself. The ChIP-Seq data (PMID:29795547) show Sir3 binding to nucleosomes adjacent to origins. Origin binding is attributed to ORC (origin recognition complex), not SIR3."
    },

    "GO:0005677_IDA_9122169": {
        "label": "chromatin silencing complex",
        "evidence": "IDA",
        "action": "ACCEPT",
        "summary": "SIR3 is an integral component of the chromatin silencing complex (Sir2-SIR3-SIR4). Documented by co-immunoprecipitation and biochemical studies.",
        "reason": "SIR3 is part of the Sir2-3-4 silent chromatin complex. This is core function. Both 'is_active_in' and 'part_of' relationships exist in GOA."
    },

    "GO:0008156": {
        "label": "negative regulation of DNA replication",
        "evidence": "IMP",
        "action": "ACCEPT",
        "summary": "SIR3 suppresses MCM loading at euchromatic origins (PMID:29795547) and maintains repression at heterochromatic origins. This is negative regulation of replication.",
        "reason": "SIR3 directly suppresses MCM complex loading at the majority of euchromatic origins, and negatively regulates rDNA and telomeric origin function. This is a key SIR3 function."
    },

    "GO:0031509_IMP_1913809": {
        "label": "subtelomeric heterochromatin formation",
        "evidence": "IMP",
        "action": "ACCEPT",
        "summary": "SIR3 is required for silencing at telomeres and subtelomeric regions. Classic position-effect data (PMID:1913809).",
        "reason": "SIR3 is essential for telomeric and subtelomeric heterochromatin. This is a core function."
    },

    "GO:0031509_IMP_31599702": {
        "label": "subtelomeric heterochromatin formation",
        "evidence": "IMP",
        "action": "ACCEPT",
        "summary": "SIR3 role in telomeric silencing in context of lifespan and aging (PMID:31599702).",
        "reason": "Multiple genetic studies confirm SIR3 requirement for telomeric silencing."
    },

    "GO:0031509_IMP_9501103": {
        "label": "subtelomeric heterochromatin formation",
        "evidence": "IMP",
        "action": "ACCEPT",
        "summary": "SIR3 mutation effects on telomeric and NHEJ processes (PMID:9501103).",
        "reason": "SIR3 is required for telomeric silencing and maintenance."
    },

    "GO:0000781_IMP_27122604": {
        "label": "chromosome, telomeric region",
        "evidence": "IMP",
        "action": "ACCEPT",
        "summary": "SIR3 localizes to telomeric regions and is required for telomere clustering in quiescent cells (PMID:27122604).",
        "reason": "SIR3 directly localizes to and functions at telomeres. This is a cellular component annotation documenting where SIR3 acts."
    },

    "GO:0000781_IDA_9710643": {
        "label": "chromosome, telomeric region",
        "evidence": "IDA",
        "action": "ACCEPT",
        "summary": "Direct experimental evidence of SIR3 binding at telomeres (PMID:9710643).",
        "reason": "ChIP evidence documenting SIR3 at telomeric chromatin."
    },

    "GO:0000792": {
        "label": "heterochromatin",
        "evidence": "IDA",
        "action": "ACCEPT",
        "summary": "SIR3 is a component of heterochromatin and is required for its formation and maintenance.",
        "reason": "SIR3 localizes to and is part of heterochromatin at all silenced loci."
    },

    "GO:0005739_HDA_14576278": {
        "label": "mitochondrion",
        "evidence": "HDA",
        "action": "REMOVE",
        "summary": "HDA from proteomics study. SIR3 is not mitochondrial. This is likely a false positive from mass spectrometry contamination.",
        "reason": "SIR3 is a nuclear protein with no known mitochondrial function or localization. HDA (homology-based direct assay) from mitochondrial proteomics is spurious. No biochemical evidence supports mitochondrial localization."
    },

    "GO:0005739_HDA_16823961": {
        "label": "mitochondrion",
        "evidence": "HDA",
        "action": "REMOVE",
        "summary": "HDA from mitochondrial proteomics. Spurious annotation.",
        "reason": "SIR3 is exclusively nuclear. This HDA is likely experimental artifact."
    },

    "GO:0006303": {
        "label": "double-strand break repair via nonhomologous end joining",
        "evidence": "IMP",
        "action": "REMOVE",
        "summary": "SIR3 has been implicated in NHEJ through studies with Ku complex (PMID:9501103), but this is likely indirect through telomere maintenance, not direct NHEJ activity.",
        "reason": "SIR3 itself is not a NHEJ component or catalyst. The association with NHEJ appears to be through telomeric regulation - SIR3 represses telomeric origins and helps maintain telomere structure, which affects DSB signaling at telomeres. This is not direct NHEJ participation. SIR3 has no role in the core NHEJ machinery (Ku70/80, ligase IV, XLF)."
    },

    "GO:0030466_IMP_3297920": {
        "label": "silent mating-type cassette heterochromatin formation",
        "evidence": "IMP",
        "action": "ACCEPT",
        "summary": "Classic position-effect data (PMID:3297920). SIR3 is essential for HML and HMR silencing. Founding function of the SIR genes.",
        "reason": "SIR3 is required for mating-type silencing. This is a core function defined in the original SIR studies."
    },

    "GO:0097695": {
        "label": "establishment of protein-containing complex localization to telomere",
        "evidence": "IMP",
        "action": "ACCEPT",
        "summary": "SIR3 is part of the Sir complex that localizes to telomeres (PMID:26218225). Ku complex recruitment to telomeres involves SIR4.",
        "reason": "SIR3 as part of the Sir complex is required for complex localization to telomeres. This process involves interaction with Ku complex for telomerase recruitment."
    },

    "GO:0034398_IMP_26399229": {
        "label": "telomere tethering at nuclear periphery",
        "evidence": "IMP",
        "action": "ACCEPT",
        "summary": "SIR3 is part of the complex involved in telomere clustering and nuclear organization (PMID:26399229).",
        "reason": "SIR3, as a component of the Sir complex, participates in telomere tethering and clustering at the nuclear periphery."
    },

    "GO:0034398_IMP_27122604": {
        "label": "telomere tethering at nuclear periphery",
        "evidence": "IMP",
        "action": "ACCEPT",
        "summary": "SIR3 required for telomere hyperclustering and nuclear organization in quiescent cells (PMID:27122604).",
        "reason": "Additional evidence for SIR3's role in telomere clustering."
    },

    "GO:0000781_IDA_16956377": {
        "label": "chromosome, telomeric region",
        "evidence": "IDA",
        "action": "ACCEPT",
        "summary": "SIR3 localization at telomeres documented (PMID:16956377).",
        "reason": "Confirms telomeric localization of SIR3."
    },

    "GO:0003682_IDA_18195043": {
        "label": "chromatin binding",
        "evidence": "IDA",
        "action": "ACCEPT",
        "summary": "Long-range communication and chromatin structure study (PMID:18195043). SIR3 directly binds chromatin.",
        "reason": "Experimental evidence for chromatin binding in silencer analysis."
    },

    "GO:0003690": {
        "label": "double-stranded DNA binding",
        "evidence": "IDA",
        "action": "ACCEPT",
        "summary": "SIR3 binds double-stranded DNA in vitro (PMID:19099415).",
        "reason": "Direct biochemical evidence for dsDNA binding. Core molecular function."
    },

    "GO:0003697": {
        "label": "single-stranded DNA binding",
        "evidence": "IDA",
        "action": "ACCEPT",
        "summary": "SIR3 binds single-stranded DNA in vitro (PMID:19099415).",
        "reason": "Direct biochemical evidence. SIR3 binds both ss and dsDNA."
    },

    "GO:0005730": {
        "label": "nucleolus",
        "evidence": "IDA",
        "action": "ACCEPT",
        "summary": "SIR3 redistributes from telomeres to nucleolus in long-lived yeast strains (PMID:9150138). This reflects differential regulation in aging.",
        "reason": "SIR3 can localize to the nucleolus where rDNA silencing occurs. This is documented and represents a secondary localization site."
    },

    "GO:0030466_IMP_16581798": {
        "label": "silent mating-type cassette heterochromatin formation",
        "evidence": "IMP",
        "action": "ACCEPT",
        "summary": "SIR3 BAH domain structure and function (PMID:16581798). Essential for HM silencing.",
        "reason": "Structural basis of SIR3 function in mating-type silencing documented."
    },

    "GO:0030466_IGI_16581798": {
        "label": "silent mating-type cassette heterochromatin formation",
        "evidence": "IGI",
        "action": "ACCEPT",
        "summary": "Genetic interaction studies showing SIR3-SIR1 relationship in silencing (PMID:16581798).",
        "reason": "Genetic interactions confirm SIR3's role in mating-type silencing."
    },

    "GO:0031491": {
        "label": "nucleosome binding",
        "evidence": "IDA",
        "action": "ACCEPT",
        "summary": "SIR3 binds nucleosomes in vitro (PMID:19217406). Histone H4 tail and H3K79 are contact sites.",
        "reason": "Direct biochemical evidence. SIR3 binds nucleosomes through multiple interaction sites. Core mechanism of action."
    },

    "GO:0031507_IMP_16908543": {
        "label": "heterochromatin formation",
        "evidence": "IMP",
        "action": "ACCEPT",
        "summary": "SIR3 C-terminal domain involvement in heterochromatin initiation and spreading (PMID:16908543).",
        "reason": "Functional analysis of SIR3 domains in heterochromatin formation."
    },

    "GO:0070481": {
        "label": "nuclear-transcribed mRNA catabolic process, non-stop decay",
        "evidence": "IMP",
        "action": "REMOVE",
        "summary": "Genomic screen (PMID:17660569) identified SIR3 as affecting nonstop mRNA decay. However, mechanism is unclear and likely indirect.",
        "reason": "SIR3 was recovered in a genomic screen for nonstop mRNA decay factors, but SIR3's primary functions are in chromatin and heterochromatin formation, not mRNA surveillance. This is likely an indirect effect through changes in gene expression or cell stress responses, not a core function of SIR3 in the mRNA decay pathway itself."
    }
}

# Print summary statistics
total_annotations = len(annotations_review)
remove_count = sum(1 for a in annotations_review.values() if a['action'] == 'REMOVE')
accept_count = sum(1 for a in annotations_review.values() if a['action'] == 'ACCEPT')
keep_non_core = sum(1 for a in annotations_review.values() if a['action'] == 'KEEP_AS_NON_CORE')
modify_count = sum(1 for a in annotations_review.values() if a['action'] == 'MODIFY')

print(f"SIR3 Annotation Curation Summary")
print(f"================================")
print(f"Total annotations: {total_annotations}")
print(f"ACCEPT (core): {accept_count}")
print(f"REMOVE: {remove_count}")
print(f"KEEP_AS_NON_CORE: {keep_non_core}")
print(f"MODIFY: {modify_count}")
print(f"\nKey principles:")
print(f"- SIR3 is a STRUCTURAL protein, not catalytic (unlike SIR2)")
print(f"- SIR3 binds histones and DNA, not DNA origins themselves")
print(f"- SIR3 suppresses replication initiation (negative regulation), not activation")
print(f"- Core functions: heterochromatin formation, nucleosome binding, complex assembly")
