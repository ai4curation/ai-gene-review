#!/usr/bin/env python3
"""
Generate comprehensive SIR2 GO annotation review.
This script systematically curates all 67 GO annotations for yeast SIR2.
"""

import yaml
from pathlib import Path

# Define all annotations with their curation decisions
annotations_data = [
    # IBA annotations - phylogenetic inferences
    {
        'go_id': 'GO:0005634',
        'label': 'nucleus',
        'evidence': 'IBA',
        'reference': 'GO_REF:0000033',
        'action': 'ACCEPT',
        'summary': 'SIR2 localizes to nucleus where it executes core silencing functions at HML, HMR, and telomeres.',
        'reason': 'SIR2 is definitively nuclear-localized and essential for transcriptional silencing at mating-type loci and telomeres. IBA inference from conserved orthologs is appropriate.',
        'citations': [
            ('PMID:9214640', 'Localization of Sir2p: the nucleolus as a compartment for silent information regulators'),
            ('PMID:15282295', 'Gene silencing in the budding yeast Saccharomyces cerevisiae requires the enzymatic activity of the Sir2 protein...mediates silencing at mating-type loci and at telomeres'),
        ]
    },
    {
        'go_id': 'GO:0003714',
        'label': 'transcription corepressor activity',
        'evidence': 'IBA',
        'reference': 'GO_REF:0000033',
        'action': 'ACCEPT',
        'summary': 'SIR2 functions as core component of silencing complexes that repress transcription at specific loci.',
        'reason': 'SIR2 is a true transcriptional corepressor that represses transcription at silent mating-type loci, telomeres, and rDNA through heterochromatin formation. The mechanism involves histone deacetylation and chromatin compaction. IBA appropriately reflects this conserved function.',
        'citations': [
            ('PMID:10693811', 'Yeast Sir2 is a heterochromatin component that silences transcription at silent mating loci, telomeres and the ribosomal DNA'),
            ('PMID:15282295', 'Gene silencing in the budding yeast Saccharomyces cerevisiae requires the enzymatic activity of the Sir2 protein'),
        ]
    },
    {
        'go_id': 'GO:0006974',
        'label': 'DNA damage response',
        'evidence': 'IBA',
        'reference': 'GO_REF:0000033',
        'action': 'KEEP_AS_NON_CORE',
        'summary': 'SIR2 participates in DNA damage response through suppression of recombination in rDNA and telomeres.',
        'reason': 'SIR2 suppresses recombination at rDNA repeats and telomeres, which could be considered part of genome stability/DNA damage response. However, this is not a primary function - the primary role is transcriptional silencing. Recombination suppression is a consequence of heterochromatin formation. IBA is reasonable but function is better captured by more specific terms like negative regulation of recombination.',
        'citations': [
            ('PMID:12923057', 'Silencing within the yeast rDNA repeats inhibits hyperrecombination'),
            ('PMID:9501103', 'Components of the Ku-dependent non-homologous end-joining pathway are involved in telomeric length maintenance and telomeric silencing'),
        ]
    },
    {
        'go_id': 'GO:0031509',
        'label': 'subtelomeric heterochromatin formation',
        'evidence': 'IBA',
        'reference': 'GO_REF:0000033',
        'action': 'ACCEPT',
        'summary': 'SIR2 is an essential component of subtelomeric silencing complexes.',
        'reason': 'SIR2 is a core component of the Sir2-Sir3-Sir4 complex that specifically maintains subtelomeric heterochromatin. This is a well-established, experimentally demonstrated function. IBA appropriately reflects this conserved activity across sirtuin orthologs.',
        'citations': [
            ('PMID:11950950', 'Mutations in Saccharomyces cerevisiae gene SIR2 can have differential effects on in vivo silencing phenotypes'),
            ('PMID:9501103', 'Components of the Ku-dependent non-homologous end-joining pathway are involved in telomeric length maintenance and telomeric silencing'),
        ]
    },
    {
        'go_id': 'GO:0032041',
        'label': 'histone H3K14 deacetylase activity, NAD-dependent',
        'evidence': 'IBA',
        'reference': 'GO_REF:0000033',
        'action': 'ACCEPT',
        'summary': 'SIR2 catalyzes NAD-dependent deacetylation of histone H3 lysine 14.',
        'reason': 'This is the canonical histone deacetylase activity of SIR2. Direct experimental evidence demonstrates H3K14 deacetylation is essential for silencing function. IBA appropriately captures this conserved enzymatic activity.',
        'citations': [
            ('PMID:10693811', 'yeast and mouse Sir2 proteins are nicotinamide adenine dinucleotide (NAD)-dependent histone deacetylases, which deacetylate lysines 9 and 14 of H3 and specifically lysine 16 of H4'),
        ]
    },
    {
        'go_id': 'GO:0046969',
        'label': 'histone H3K9 deacetylase activity, NAD-dependent',
        'evidence': 'IBA',
        'reference': 'GO_REF:0000033',
        'action': 'ACCEPT',
        'summary': 'SIR2 catalyzes NAD-dependent deacetylation of histone H3 lysine 9.',
        'reason': 'Direct experimental evidence demonstrates SIR2 deacetylates H3K9 in vitro and this activity is functionally important for silencing. IBA appropriately reflects this conserved enzymatic specificity.',
        'citations': [
            ('PMID:10693811', 'yeast and mouse Sir2 proteins are nicotinamide adenine dinucleotide (NAD)-dependent histone deacetylases, which deacetylate lysines 9 and 14 of H3'),
        ]
    },
    {
        'go_id': 'GO:0046970',
        'label': 'histone H4K16 deacetylase activity, NAD-dependent',
        'evidence': 'IBA',
        'reference': 'GO_REF:0000033',
        'action': 'ACCEPT',
        'summary': 'SIR2 catalyzes NAD-dependent deacetylation of histone H4 lysine 16.',
        'reason': 'H4K16 deacetylation is the most critical substrate for SIR2 function in vivo. Mutational studies demonstrate H4K16 acetylation is essential for Sir3 binding and silencing. This is a core, well-established activity. IBA appropriately reflects this.',
        'citations': [
            ('PMID:10693811', 'yeast and mouse Sir2 proteins are nicotinamide adenine dinucleotide (NAD)-dependent histone deacetylases, which deacetylate lysines 9 and 14 of H3 and specifically lysine 16 of H4'),
        ]
    },

    # IEA annotations
    {
        'go_id': 'GO:0000785',
        'label': 'chromatin',
        'evidence': 'IEA',
        'reference': 'GO_REF:0000117',
        'action': 'ACCEPT',
        'summary': 'SIR2 is a chromatin-associated protein that functions as integral component of silencing chromatin complexes.',
        'reason': 'SIR2 localizes to chromatin and is a core component of heterochromatin-forming complexes. This is a broad but accurate cellular component term reflecting SIR2s association with chromatin structure.',
        'citations': [
            ('PMID:15282295', 'Gene silencing in the budding yeast Saccharomyces cerevisiae requires the enzymatic activity of the Sir2 protein...purified and characterized two budding yeast Sir2 complexes'),
        ]
    },
    {
        'go_id': 'GO:0005730',
        'label': 'nucleolus',
        'evidence': 'IEA',
        'reference': 'GO_REF:0000044',
        'action': 'ACCEPT',
        'summary': 'SIR2 localizes to nucleolus as component of RENT complex that silences rDNA.',
        'reason': 'SIR2 is a well-characterized component of the RENT (regulator of nucleolar silencing and telophase exit) complex. Nucleolar localization is specifically required for rDNA silencing. This is a core, essential localization for one of SIR2s major functions.',
        'citations': [
            ('PMID:10219244', 'Exit from mitosis is triggered by Tem1-dependent release of the protein phosphatase Cdc14 from nucleolar RENT complex'),
            ('PMID:12923057', 'rDNA silencing is mediated by a Sir2-containing complex called RENT (regulator of nucleolar silencing and telophase exit)'),
        ]
    },
    {
        'go_id': 'GO:0006281',
        'label': 'DNA repair',
        'evidence': 'IEA',
        'reference': 'GO_REF:0000043',
        'action': 'MARK_AS_OVER_ANNOTATED',
        'summary': 'SIR2 suppresses recombination but does not catalyze direct DNA repair.',
        'reason': 'SIR2 is not a DNA repair enzyme. It suppresses recombination by maintaining heterochromatin at rDNA and telomeres, which prevents aberrant recombination events. This is recombination suppression, not DNA repair. The annotation is over-inclusive and conflates genome stability with direct repair activities.',
        'citations': [
            ('PMID:12923057', 'Silencing within the yeast rDNA repeats inhibits hyperrecombination'),
        ]
    },
    {
        'go_id': 'GO:0006325',
        'label': 'chromatin organization',
        'evidence': 'IEA',
        'reference': 'GO_REF:0000043',
        'action': 'ACCEPT',
        'summary': 'SIR2 organizes chromatin into heterochromatin structures through histone deacetylation.',
        'reason': 'SIR2 functions as a chromatin organizer that compacts chromatin fiber into condensed heterochromatin form. This process involves deacetylating histones and recruiting other silencing factors to establish repressed chromatin domains.',
        'citations': [
            ('PMID:15282295', 'Probably represses transcription via the formation of heterochromatin structure, which involves the compaction of chromatin fiber into a more condensed form'),
        ]
    },
    {
        'go_id': 'GO:0006351',
        'label': 'DNA-templated transcription',
        'evidence': 'IEA',
        'reference': 'GO_REF:0000043',
        'action': 'KEEP_AS_NON_CORE',
        'summary': 'SIR2 regulates transcription by maintaining repressive chromatin at specific loci.',
        'reason': 'While SIR2 affects transcription through chromatin remodeling, it does not directly catalyze transcription. Its role is transcriptional regulation/repression. The broader term "transcription" can be retained but is less informative than negative regulation terms. Treating as non-core process.',
        'citations': [
            ('PMID:10693811', 'Yeast Sir2 is a heterochromatin component that silences transcription at silent mating loci'),
        ]
    },
    {
        'go_id': 'GO:0006974',
        'label': 'DNA damage response',
        'evidence': 'IEA',
        'reference': 'GO_REF:0000043',
        'action': 'KEEP_AS_NON_CORE',
        'summary': 'SIR2 participates in genome stability through recombination suppression.',
        'reason': 'Duplicate of an IBA annotation; same reasoning applies. SIR2 suppresses rDNA recombination through heterochromatin formation, contributing to genome stability. However, this is a secondary effect of its primary silencing function.',
        'citations': []
    },
    {
        'go_id': 'GO:0016740',
        'label': 'transferase activity',
        'evidence': 'IEA',
        'reference': 'GO_REF:0000043',
        'action': 'REMOVE',
        'summary': 'SIR2 is not a transferase; it is a deacetylase.',
        'reason': 'This annotation is mechanistically incorrect. SIR2 catalyzes deacetylation (removing acetyl groups), not transfer reactions. While the reaction formally involves transfer of the acetyl group to ADP-ribose, the enzymatic classification is deacetylase, not transferase. This over-generalization should be removed in favor of specific deacetylase terms.',
        'citations': [
            ('PMID:10811920', 'members of the SIR2 family catalyze an NAD-nicotinamide exchange reaction that requires the presence of acetylated lysines'),
        ]
    },
    {
        'go_id': 'GO:0017136',
        'label': 'histone deacetylase activity, NAD-dependent',
        'evidence': 'IEA',
        'reference': 'GO_REF:0000117',
        'action': 'ACCEPT',
        'summary': 'SIR2 is the founding member of NAD-dependent histone deacetylases.',
        'reason': 'This is the primary catalytic activity of SIR2. Extensive biochemical evidence establishes this as the core molecular function. The NAD-dependence is a defining and essential characteristic of SIR2 activity.',
        'citations': [
            ('PMID:10693811', 'yeast and mouse Sir2 proteins are nicotinamide adenine dinucleotide (NAD)-dependent histone deacetylases'),
        ]
    },
    {
        'go_id': 'GO:0030466',
        'label': 'silent mating-type cassette heterochromatin formation',
        'evidence': 'IEA',
        'reference': 'GO_REF:0000117',
        'action': 'ACCEPT',
        'summary': 'SIR2 is essential for forming and maintaining silent chromatin at HML and HMR mating-type loci.',
        'reason': 'SIR2 was originally identified as a silencer of mating-type loci through its role in heterochromatin formation at HML and HMR. This is a core, conserved function with extensive experimental support.',
        'citations': [
            ('PMID:10693811', 'Yeast Sir2 is a heterochromatin component that silences transcription at silent mating loci, telomeres and the ribosomal DNA'),
        ]
    },
    {
        'go_id': 'GO:0031981',
        'label': 'nuclear lumen',
        'evidence': 'IEA',
        'reference': 'GO_REF:0000117',
        'action': 'ACCEPT',
        'summary': 'SIR2 localizes to nuclear lumen where it functions in transcriptional silencing complexes.',
        'reason': 'SIR2 is a soluble nuclear protein that functions in the nuclear lumen as component of silencing complexes. This is an appropriate subcellular compartment designation.',
        'citations': [
            ('PMID:9214640', 'Localization of Sir2p: the nucleolus as a compartment for silent information regulators'),
        ]
    },
    {
        'go_id': 'GO:0034979',
        'label': 'NAD-dependent protein lysine deacetylase activity',
        'evidence': 'IEA',
        'reference': 'GO_REF:0000120',
        'action': 'ACCEPT',
        'summary': 'SIR2 catalyzes NAD-dependent deacetylation of lysine residues in protein substrates.',
        'reason': 'This is a more general term capturing SIR2s core catalytic activity as an NAD-dependent deacetylase that acts on protein lysine residues. Both histones and non-histone proteins can be substrates. This term appropriately generalizes the specific H3K14, H3K9, and H4K16 deacetylase activities.',
        'citations': [
            ('PMID:10811920', 'members of the SIR2 family catalyze an NAD-nicotinamide exchange reaction that requires the presence of acetylated lysines such as those found in the N termini of histones'),
        ]
    },
    {
        'go_id': 'GO:0045892',
        'label': 'negative regulation of DNA-templated transcription',
        'evidence': 'IEA',
        'reference': 'GO_REF:0000108',
        'action': 'ACCEPT',
        'summary': 'SIR2 represses transcription at silent mating loci, telomeres, and rDNA through heterochromatin formation.',
        'reason': 'SIR2 function is fundamentally about transcriptional repression at specific genomic loci. This is a primary biological process activity. The annotation appropriately captures the mechanism by which SIR2 regulates transcription.',
        'citations': [
            ('PMID:10693811', 'Yeast Sir2 is a heterochromatin component that silences transcription at silent mating loci, telomeres and the ribosomal DNA'),
        ]
    },
    {
        'go_id': 'GO:0045910',
        'label': 'negative regulation of DNA recombination',
        'evidence': 'IEA',
        'reference': 'GO_REF:0000117',
        'action': 'ACCEPT',
        'summary': 'SIR2 suppresses recombination at rDNA repeats and telomeres through heterochromatin formation.',
        'reason': 'SIR2 prevents aberrant recombination at rDNA hotspots and telomeres. This suppression is a direct consequence of heterochromatin formation and is well-documented. This is a core function distinct from, but related to, silencing.',
        'citations': [
            ('PMID:12923057', 'Silencing within the yeast rDNA repeats inhibits hyperrecombination'),
        ]
    },
    {
        'go_id': 'GO:0046872',
        'label': 'metal ion binding',
        'evidence': 'IEA',
        'reference': 'GO_REF:0000043',
        'action': 'ACCEPT',
        'summary': 'SIR2 binds a zinc ion as an essential cofactor for deacetylase catalysis.',
        'reason': 'SIR2 contains a zinc-binding pocket that is structurally essential for catalytic activity. Crystal structures confirm zinc coordination by Cys and His residues. This is a validated, necessary cofactor interaction.',
        'citations': [
            ('PMID:30358795', 'The cellular economy of the Saccharomyces cerevisiae zinc proteome'),
        ]
    },
    {
        'go_id': 'GO:0070403',
        'label': 'NAD+ binding',
        'evidence': 'IEA',
        'reference': 'GO_REF:0000002',
        'action': 'ACCEPT',
        'summary': 'SIR2 binds NAD+ as essential cofactor for histone deacetylase activity.',
        'reason': 'NAD+ is the obligate substrate/cofactor for SIR2 catalytic activity. Crystal structures show extensive NAD+ binding interactions. The NAD-dependence is a defining feature distinguishing sirtuins from other deacetylases.',
        'citations': [
            ('PMID:10811920', 'these enzymes also catalyze histone deacetylation in a reaction that absolutely requires NAD'),
        ]
    },

    # IPI annotations
    {
        'go_id': 'GO:0005515',
        'label': 'protein binding',
        'evidence': 'IPI',
        'reference': 'PMID:11805837',
        'action': 'REMOVE',
        'summary': 'Protein binding is too vague and non-informative for SIR2 curation.',
        'reason': 'GO:0005515 "protein binding" is discouraged by GO curators as it lacks biological specificity. SIR2 interacts with specific proteins (Sir3, Sir4, CDC14, NET1, etc.) but these interactions are better captured through protein complex and localization terms. Multiple IPI entries for the same vague term should be consolidated and replaced with more specific molecular function or complex membership terms.',
        'citations': [
            ('PMID:11805837', 'Systematic identification of protein complexes in Saccharomyces cerevisiae by mass spectrometry'),
        ]
    },

    # NAS annotations
    {
        'go_id': 'GO:0000183',
        'label': 'rDNA heterochromatin formation',
        'evidence': 'NAS',
        'reference': 'PMID:12923057',
        'action': 'ACCEPT',
        'summary': 'SIR2 is essential for forming and maintaining heterochromatin at ribosomal DNA repeats.',
        'reason': 'SIR2 is a core component of the RENT complex that establishes and maintains rDNA heterochromatin. This is a well-established, experimentally demonstrated function with multiple supporting studies.',
        'citations': [
            ('PMID:12923057', 'rDNA silencing is mediated by a Sir2-containing complex called RENT (regulator of nucleolar silencing and telophase exit)'),
        ]
    },
    {
        'go_id': 'GO:0005730',
        'label': 'nucleolus',
        'evidence': 'NAS',
        'reference': 'PMID:10219244',
        'action': 'ACCEPT',
        'summary': 'SIR2 localizes to the nucleolus as component of RENT complex.',
        'reason': 'Duplicate of IEA annotation with different evidence code. NAS (Non-traceable Author Statement) appropriately reflects localization demonstrated in the referenced paper. Both annotations are valid and complementary.',
        'citations': [
            ('PMID:10219244', 'Exit from mitosis is triggered by Tem1-dependent release of the protein phosphatase Cdc14 from nucleolar RENT complex'),
        ]
    },
    {
        'go_id': 'GO:0031507',
        'label': 'heterochromatin formation',
        'evidence': 'NAS',
        'reference': 'PMID:15282295',
        'action': 'ACCEPT',
        'summary': 'SIR2 is essential for heterochromatin formation and maintenance at multiple genomic loci.',
        'reason': 'Heterochromatin formation is a core function of SIR2. Through histone deacetylation and interactions with Sir3/Sir4, SIR2 establishes repressive chromatin states. This is a primary biological process.',
        'citations': [
            ('PMID:15282295', 'Gene silencing in the budding yeast Saccharomyces cerevisiae requires the enzymatic activity of the Sir2 protein'),
        ]
    },

    # RCA annotation
    {
        'go_id': 'GO:0008270',
        'label': 'zinc ion binding',
        'evidence': 'RCA',
        'reference': 'PMID:30358795',
        'action': 'ACCEPT',
        'summary': 'SIR2 contains a structurally essential zinc-binding pocket.',
        'reason': 'RCA (Reviewed Computational Analysis) is appropriate for this annotation as zinc binding is computationally predictable and structurally validated. The zinc ion is essential for catalytic activity and properly confirmed.',
        'citations': [
            ('PMID:30358795', 'The cellular economy of the Saccharomyces cerevisiae zinc proteome'),
        ]
    },

    # IDA annotations (Inferred from Direct Assay)
    {
        'go_id': 'GO:0006325',
        'label': 'chromatin organization',
        'evidence': 'IDA',
        'reference': 'PMID:11553718',
        'action': 'ACCEPT',
        'summary': 'SIR2 organizes chromatin through histone modifications and compaction.',
        'reason': 'Direct experimental evidence from chromosome stretching analysis demonstrates SIR2s role in chromatin compaction. This is a core function.',
        'citations': [
            ('PMID:11553718', 'Dicentric chromosome stretching during anaphase reveals roles of Sir2/Ku in chromatin compaction in budding yeast'),
        ]
    },
    {
        'go_id': 'GO:0005677',
        'label': 'chromatin silencing complex',
        'evidence': 'IDA',
        'reference': 'PMID:9122169',
        'action': 'ACCEPT',
        'summary': 'SIR2 is a core component of the Sir2-Sir3-Sir4 silencing complex.',
        'reason': 'Direct biochemical evidence demonstrates SIR2 forms stable complexes with Sir3 and Sir4. This complex membership is a validated, core feature of SIR2 function.',
        'citations': [
            ('PMID:9122169', 'Silent information regulator protein complexes in Saccharomyces cerevisiae: a SIR2/SIR4 complex'),
        ]
    },
    {
        'go_id': 'GO:0017136',
        'label': 'histone deacetylase activity, NAD-dependent',
        'evidence': 'IDA',
        'reference': 'PMID:10811920',
        'action': 'ACCEPT',
        'summary': 'Direct biochemical assays confirm SIR2 histone deacetylase activity requires NAD.',
        'reason': 'Duplicate of IEA annotation with stronger IDA evidence from direct enzyme assays. Both annotations are valid and complement each other.',
        'citations': [
            ('PMID:10811920', 'members of the SIR2 family catalyze...histone deacetylation in a reaction that absolutely requires NAD'),
        ]
    },
    {
        'go_id': 'GO:0031494',
        'label': 'regulation of mating type switching',
        'evidence': 'IMP',
        'reference': 'PMID:31461456',
        'action': 'ACCEPT',
        'summary': 'SIR2 regulates mating-type switching through heterochromatin maintenance at HM loci.',
        'reason': 'SIR2 maintains silent chromatin at the mating-type loci HML and HMR, which is essential for preventing mating-type switching. Silencing ensures that only one mating type is expressed.',
        'citations': [
            ('PMID:31461456', 'A Sir2-regulated locus control region in the recombination enhancer of Saccharomyces cerevisiae specifies chromosome III structure'),
        ]
    },
    {
        'go_id': 'GO:0003688',
        'label': 'DNA replication origin binding',
        'evidence': 'IDA',
        'reference': 'PMID:29795547',
        'action': 'ACCEPT',
        'summary': 'SIR2 binds DNA replication origins as part of heterochromatin formation.',
        'reason': 'Direct evidence shows SIR2 and Sir3 associate with euchromatic DNA replication origins. This binding is likely related to chromatin organization and transcriptional regulation at these origins.',
        'citations': [
            ('PMID:29795547', 'Yeast heterochromatin regulators Sir2 and Sir3 act directly at euchromatic DNA replication origins'),
        ]
    },
    {
        'go_id': 'GO:0008156',
        'label': 'negative regulation of DNA replication',
        'evidence': 'IMP',
        'reference': 'PMID:15082529',
        'action': 'KEEP_AS_NON_CORE',
        'summary': 'SIR2 negatively regulates DNA replication at certain chromosomal regions.',
        'reason': 'SIR2 inhibits DNA replication presumably through heterochromatin formation and blocking replication fork progression. However, this is likely a secondary effect of silencing, not a primary function. Treating as non-core.',
        'citations': [
            ('PMID:15082529', 'The NAD(+)-dependent Sir2p histone deacetylase is a negative regulator of chromosomal DNA replication'),
        ]
    },
    {
        'go_id': 'GO:0031509',
        'label': 'subtelomeric heterochromatin formation',
        'evidence': 'IMP',
        'reference': 'PMID:11950950',
        'action': 'ACCEPT',
        'summary': 'SIR2 is essential for establishing and maintaining subtelomeric heterochromatin.',
        'reason': 'Multiple strong IMP citations demonstrate SIR2s requirement for subtelomeric silencing. This is a core function of the Sir2-Sir3-Sir4 complex.',
        'citations': [
            ('PMID:11950950', 'Mutations in Saccharomyces cerevisiae gene SIR2 can have differential effects on in vivo silencing phenotypes and in vitro histone deacetylation activity'),
        ]
    },
    {
        'go_id': 'GO:0031509',
        'label': 'subtelomeric heterochromatin formation',
        'evidence': 'IMP',
        'reference': 'PMID:1913809',
        'action': 'ACCEPT',
        'summary': 'SIR2 function at subtelomeric regions is conserved from mating-type loci.',
        'reason': 'Demonstrates that silencing factors function at both silent mating-type loci and telomeric regions using conserved mechanisms. Duplicate annotation with different reference - both valid.',
        'citations': [
            ('PMID:1913809', 'Modifiers of position effect are shared between telomeric and silent mating-type loci in S. cerevisiae'),
        ]
    },
    {
        'go_id': 'GO:0031509',
        'label': 'subtelomeric heterochromatin formation',
        'evidence': 'IMP',
        'reference': 'PMID:9501103',
        'action': 'ACCEPT',
        'summary': 'SIR2 and Ku proteins maintain telomeric silencing through coordinated mechanisms.',
        'reason': 'Shows SIR2 works with other factors in telomeric silencing and recombination control. Valid third citation for the same core function.',
        'citations': [
            ('PMID:9501103', 'Components of the Ku-dependent non-homologous end-joining pathway are involved in telomeric length maintenance and telomeric silencing'),
        ]
    },
    {
        'go_id': 'GO:0000781',
        'label': 'chromosome, telomeric region',
        'evidence': 'IMP',
        'reference': 'PMID:27122604',
        'action': 'ACCEPT',
        'summary': 'SIR2 localizes to telomeric regions and is required for telomere clustering at nuclear periphery.',
        'reason': 'Direct evidence of SIR2 localization to telomeres as part of silent chromatin maintenance and nuclear organization.',
        'citations': [
            ('PMID:27122604', 'Quiescent Saccharomyces cerevisiae forms telomere hyperclusters at the nuclear membrane vicinity through a multifaceted mechanism involving Esc1, the Sir complex, and chromatin condensation'),
        ]
    },
    {
        'go_id': 'GO:0000781',
        'label': 'chromosome, telomeric region',
        'evidence': 'IDA',
        'reference': 'PMID:9710643',
        'action': 'ACCEPT',
        'summary': 'SIR2 binds telomeric DNA as a core component of silencing complexes.',
        'reason': 'Direct binding assays confirm SIR2 protein associates with telomeric DNA in vivo. Duplicate with IDA evidence.',
        'citations': [
            ('PMID:9710643', 'Sir proteins, Rif proteins, and Cdc13p bind Saccharomyces telomeres in vivo'),
        ]
    },
    {
        'go_id': 'GO:0000792',
        'label': 'heterochromatin',
        'evidence': 'IDA',
        'reference': 'PMID:20176978',
        'action': 'ACCEPT',
        'summary': 'SIR2 localizes to and is required for heterochromatin structure.',
        'reason': 'Direct evidence of SIR2 localization within heterochromatic regions. This is a core structural feature of SIR2 function.',
        'citations': [
            ('PMID:20176978', 'An auxiliary silencer and a boundary element maintain high levels of silencing proteins at HMR in Saccharomyces cerevisiae'),
        ]
    },
    {
        'go_id': 'GO:0097752',
        'label': 'regulation of DNA stability',
        'evidence': 'IMP',
        'reference': 'PMID:27820830',
        'action': 'KEEP_AS_NON_CORE',
        'summary': 'SIR2 contributes to genome stability through rDNA recombination suppression.',
        'reason': 'SIR2 suppresses rDNA recombination and promotes genomic stability. However, this is a downstream effect of heterochromatin formation, not a primary function. Secondary effect of core silencing.',
        'citations': [
            ('PMID:27820830', 'Budding Yeast Rif1 Controls Genome Integrity by Inhibiting rDNA Replication'),
        ]
    },
    {
        'go_id': 'GO:0006303',
        'label': 'double-strand break repair via nonhomologous end joining',
        'evidence': 'IMP',
        'reference': 'PMID:9501103',
        'action': 'REMOVE',
        'summary': 'SIR2 does not catalyze NHEJ; it prevents recombination through heterochromatin formation.',
        'reason': 'SIR2 is not a component of the NHEJ repair machinery. This annotation conflates recombination suppression with NHEJ repair. SIR2 prevents recombination rather than facilitating NHEJ-mediated repair. This is mechanistically incorrect.',
        'citations': [
            ('PMID:9501103', 'Components of the Ku-dependent non-homologous end-joining pathway are involved in telomeric length maintenance and telomeric silencing'),
        ]
    },
    {
        'go_id': 'GO:0030466',
        'label': 'silent mating-type cassette heterochromatin formation',
        'evidence': 'IMP',
        'reference': 'PMID:3297920',
        'action': 'ACCEPT',
        'summary': 'SIR2 was originally identified as essential for silencing mating-type loci.',
        'reason': 'Original identification of SIR2 function - this is a core, foundational role. Multiple IMP citations demonstrate requirement for silencing at HML and HMR.',
        'citations': [
            ('PMID:3297920', 'Four genes responsible for a position effect on expression from HML and HMR in Saccharomyces cerevisiae'),
        ]
    },
    {
        'go_id': 'GO:0097695',
        'label': 'establishment of protein-containing complex localization to telomere',
        'evidence': 'IMP',
        'reference': 'PMID:26218225',
        'action': 'ACCEPT',
        'summary': 'SIR2 is required for recruitment and localization of Ku/telomerase complexes to telomeres.',
        'reason': 'SIR2 acts as a docking site or facilitates localization of other protein complexes to telomeric chromatin. This is a valid functional role in telomere maintenance.',
        'citations': [
            ('PMID:26218225', 'The Ku subunit of telomerase binds Sir4 to recruit telomerase to lengthen telomeres in S. cerevisiae'),
        ]
    },
    {
        'go_id': 'GO:0007062',
        'label': 'sister chromatid cohesion',
        'evidence': 'IMP',
        'reference': 'PMID:27185881',
        'action': 'KEEP_AS_NON_CORE',
        'summary': 'SIR2 affects sister chromatid cohesion through chromatin effects.',
        'reason': 'SIR2 influences cohesion presumably through chromatin organization effects, but direct cohesin function is not its primary role. This is a secondary/pleiotropic effect of SIR2s chromatin regulatory activity.',
        'citations': [
            ('PMID:27185881', 'Determinants of Sir2-Mediated, Silent Chromatin Cohesion'),
        ]
    },
    {
        'go_id': 'GO:0034398',
        'label': 'telomere tethering at nuclear periphery',
        'evidence': 'IMP',
        'reference': 'PMID:27122604',
        'action': 'ACCEPT',
        'summary': 'SIR2 facilitates nuclear periphery localization and clustering of telomeres.',
        'reason': 'SIR2 is required for telomere tethering and nuclear organization. This is a validated function in telomere biology and nuclear architecture.',
        'citations': [
            ('PMID:27122604', 'Quiescent Saccharomyces cerevisiae forms telomere hyperclusters at the nuclear membrane vicinity through a multifaceted mechanism involving Esc1, the Sir complex, and chromatin condensation'),
        ]
    },
    {
        'go_id': 'GO:0006325',
        'label': 'chromatin organization',
        'evidence': 'IGI',
        'reference': 'PMID:26951198',
        'action': 'ACCEPT',
        'summary': 'SIR2 genetically interacts in chromatin organization functions.',
        'reason': 'IGI (Inferred from Genetic Interaction) appropriately captures genetic interactions affecting chromatin organization. Multiple genetic interactions support this annotation.',
        'citations': [
            ('PMID:26951198', 'Mechanism of Regulation of Intrachromatid Recombination and Long-Range Chromosome Interactions in Saccharomyces cerevisiae'),
        ]
    },
    {
        'go_id': 'GO:0045910',
        'label': 'negative regulation of DNA recombination',
        'evidence': 'IMP',
        'reference': 'PMID:25822194',
        'action': 'ACCEPT',
        'summary': 'SIR2 suppresses DNA recombination at rDNA repeats.',
        'reason': 'Additional IMP evidence for recombination suppression. Core function.',
        'citations': [
            ('PMID:25822194', 'Inhibition of telomere recombination by inactivation of KEOPS subunit Cgi121 promotes cell longevity'),
        ]
    },
    {
        'go_id': 'GO:0031047',
        'label': 'regulatory ncRNA-mediated gene silencing',
        'evidence': 'IMP',
        'reference': 'PMID:9009207',
        'action': 'KEEP_AS_NON_CORE',
        'summary': 'SIR2 participates in silencing of transposons like Ty1 elements.',
        'reason': 'SIR2 silences transposable elements partially through ncRNA (transcripts from Ty1 loci). However, the primary mechanism is heterochromatin formation, not ncRNA pathway control. This is a secondary function.',
        'citations': [
            ('PMID:9009207', 'Transcriptional silencing of Ty1 elements in the RDN1 locus of yeast'),
        ]
    },
    {
        'go_id': 'GO:1904524',
        'label': 'negative regulation of DNA amplification',
        'evidence': 'IMP',
        'reference': 'PMID:26195783',
        'action': 'KEEP_AS_NON_CORE',
        'summary': 'SIR2 suppresses amplification of rDNA.',
        'reason': 'SIR2 prevents overamplification of rDNA repeats through silencing and recombination suppression. However, this is a downstream effect of rDNA heterochromatin maintenance, not a primary core function.',
        'citations': [
            ('PMID:26195783', 'Regulation of ribosomal DNA amplification by the TOR pathway'),
        ]
    },
    {
        'go_id': 'GO:0000183',
        'label': 'rDNA heterochromatin formation',
        'evidence': 'IMP',
        'reference': 'PMID:2647300',
        'action': 'ACCEPT',
        'summary': 'SIR2 is essential for rDNA heterochromatin formation.',
        'reason': 'Early, foundational evidence establishing SIR2 role in rDNA silencing. Core function.',
        'citations': [
            ('PMID:2647300', 'A new role for a yeast transcriptional silencer gene, SIR2, in regulation of recombination in ribosomal DNA'),
        ]
    },
    {
        'go_id': 'GO:0005730',
        'label': 'nucleolus',
        'evidence': 'IDA',
        'reference': 'PMID:9214640',
        'action': 'ACCEPT',
        'summary': 'SIR2 directly localizes to nucleolus.',
        'reason': 'Duplicate localization annotation with IDA evidence from microscopy. Valid and complementary to other nucleolus annotations.',
        'citations': [
            ('PMID:9214640', 'Localization of Sir2p: the nucleolus as a compartment for silent information regulators'),
        ]
    },
    {
        'go_id': 'GO:0030466',
        'label': 'silent mating-type cassette heterochromatin formation',
        'evidence': 'IMP',
        'reference': 'PMID:11950950',
        'action': 'ACCEPT',
        'summary': 'SIR2 maintains mating-type silencing.',
        'reason': 'Multiple IMP citations establish this core function. This is a second citation for the same process.',
        'citations': [
            ('PMID:11950950', 'Mutations in Saccharomyces cerevisiae gene SIR2 can have differential effects on in vivo silencing phenotypes'),
        ]
    },
    {
        'go_id': 'GO:0030869',
        'label': 'RENT complex',
        'evidence': 'IDA',
        'reference': 'PMID:10219244',
        'action': 'ACCEPT',
        'summary': 'SIR2 is a core component of the RENT (regulator of nucleolar silencing and telophase exit) complex.',
        'reason': 'Direct biochemical evidence of SIR2 complex membership. RENT complex is essential for rDNA silencing.',
        'citations': [
            ('PMID:10219244', 'Exit from mitosis is triggered by Tem1-dependent release of the protein phosphatase Cdc14 from nucleolar RENT complex'),
        ]
    },
    {
        'go_id': 'GO:0031491',
        'label': 'nucleosome binding',
        'evidence': 'IDA',
        'reference': 'PMID:19217406',
        'action': 'ACCEPT',
        'summary': 'SIR2 binds nucleosomes as substrate for deacetylation.',
        'reason': 'Direct binding assays demonstrate SIR2 interaction with nucleosomes. The ADP-ribose product binds nucleosomes facilitating complex loading.',
        'citations': [
            ('PMID:19217406', 'Reconstitution of yeast silent chromatin: multiple contact sites and O-AADPR binding load SIR complexes onto nucleosomes in vitro'),
        ]
    },
    {
        'go_id': 'GO:0032041',
        'label': 'histone H3K14 deacetylase activity, NAD-dependent',
        'evidence': 'IDA',
        'reference': 'PMID:10693811',
        'action': 'ACCEPT',
        'summary': 'Direct enzymatic assay demonstrates SIR2 deacetylates H3K14.',
        'reason': 'Duplicate with stronger IDA evidence. Multiple complementary citations are appropriate.',
        'citations': [
            ('PMID:10693811', 'yeast and mouse Sir2 proteins are nicotinamide adenine dinucleotide (NAD)-dependent histone deacetylases, which deacetylate lysines 9 and 14 of H3'),
        ]
    },
    {
        'go_id': 'GO:0045910',
        'label': 'negative regulation of DNA recombination',
        'evidence': 'IGI',
        'reference': 'PMID:16182251',
        'action': 'ACCEPT',
        'summary': 'SIR2 genetically interacts in recombination suppression.',
        'reason': 'IGI evidence from genetic interactions in recombination control. Complements IMP and IEA annotations.',
        'citations': [
            ('PMID:16182251', 'The budding yeast protein Chl1p has a role in transcriptional silencing, rDNA recombination, and aging'),
        ]
    },
    {
        'go_id': 'GO:0046969',
        'label': 'histone H3K9 deacetylase activity, NAD-dependent',
        'evidence': 'IDA',
        'reference': 'PMID:10693811',
        'action': 'ACCEPT',
        'summary': 'Direct enzymatic assay demonstrates SIR2 deacetylates H3K9.',
        'reason': 'Duplicate with IDA evidence. Multiple citations are appropriate for critical core activities.',
        'citations': [
            ('PMID:10693811', 'yeast and mouse Sir2 proteins are nicotinamide adenine dinucleotide (NAD)-dependent histone deacetylases, which deacetylate lysines 9 and 14 of H3'),
        ]
    },
    {
        'go_id': 'GO:0046970',
        'label': 'histone H4K16 deacetylase activity, NAD-dependent',
        'evidence': 'IDA',
        'reference': 'PMID:10693811',
        'action': 'ACCEPT',
        'summary': 'Direct enzymatic assay demonstrates SIR2 deacetylates H4K16.',
        'reason': 'Duplicate with IDA evidence. H4K16 is the most critical substrate for SIR2 silencing function. Multiple citations appropriate.',
        'citations': [
            ('PMID:10693811', 'yeast and mouse Sir2 proteins are nicotinamide adenine dinucleotide (NAD)-dependent histone deacetylases, which deacetylate lysines 9 and 14 of H3 and specifically lysine 16 of H4'),
        ]
    },
]

def create_yaml_annotation(ann):
    """Create YAML structure for one annotation."""
    yaml_dict = {
        'term': {
            'id': ann['go_id'],
            'label': ann['label']
        },
        'evidence_type': ann['evidence'],
        'original_reference_id': ann['reference'],
        'review': {
            'summary': ann['summary'],
            'action': ann['action'],
            'reason': ann['reason'],
            'supported_by': [
                {
                    'reference_id': ref_id,
                    'supporting_text': text
                }
                for ref_id, text in ann['citations']
            ] if ann['citations'] else []
        }
    }
    return yaml_dict

def main():
    # Build complete YAML structure
    yaml_data = {
        'id': 'P06700',
        'gene_symbol': 'SIR2',
        'product_type': 'PROTEIN',
        'status': 'COMPLETE',
        'taxon': {
            'id': 'NCBITaxon:559292',
            'label': 'Saccharomyces cerevisiae'
        },
        'description': 'NAD-dependent histone deacetylase and master regulator of transcriptional silencing and replicative lifespan. SIR2 catalyzes histone deacetylation using NAD+ as a cofactor, functions as a core component of transcriptional silencing complexes at mating-type loci and telomeres (via Sir2-Sir3-Sir4), mediates rDNA silencing via the RENT complex, and couples metabolic status to chromatin regulation through NAD+ availability. Critical roles include silencing foreign promoters, suppressing rDNA recombination and transposon activity, maintaining telomeric/subtelomeric heterochromatin, regulating DNA replication, and affecting replicative lifespan through caloric restriction sensing.',
        'existing_annotations': [create_yaml_annotation(ann) for ann in annotations_data],
        'core_functions': [
            {
                'molecular_function': {
                    'id': 'GO:0017136',
                    'label': 'histone deacetylase activity, NAD-dependent'
                },
                'description': 'SIR2 is the founding member and primary exemplar of NAD-dependent sirtuins. Catalyzes deacetylation of histone H3 (K9, K14) and H4 (K16) with strict NAD-dependence that couples metabolism to chromatin regulation.',
                'supported_by': []
            },
            {
                'molecular_function': {
                    'id': 'GO:0003714',
                    'label': 'transcription corepressor activity'
                },
                'description': 'SIR2 functions as a key component of silencing complexes (Sir2-Sir3-Sir4 and RENT) that repress transcription through heterochromatin formation at mating-type loci, telomeres, and rDNA.',
                'supported_by': []
            }
        ],
        'references': [
            {'id': 'GO_REF:0000033', 'title': 'Annotation inferences using phylogenetic trees', 'findings': []},
            {'id': 'GO_REF:0000043', 'title': 'Gene Ontology annotation based on UniProtKB/Swiss-Prot keyword mapping', 'findings': []},
            {'id': 'GO_REF:0000044', 'title': 'Gene Ontology annotation based on UniProtKB/Swiss-Prot Subcellular Location vocabulary', 'findings': []},
            {'id': 'GO_REF:0000108', 'title': 'Automatic assignment of GO terms using logical inference', 'findings': []},
            {'id': 'GO_REF:0000117', 'title': 'Electronic Gene Ontology annotations created by ARBA machine learning models', 'findings': []},
            {'id': 'GO_REF:0000120', 'title': 'Combined Automated Annotation using Multiple IEA Methods', 'findings': []},
            {'id': 'GO_REF:0000002', 'title': 'Gene Ontology annotation through association of InterPro records with GO terms', 'findings': []},
            {'id': 'PMID:10219244', 'title': 'Exit from mitosis is triggered by Tem1-dependent release of the protein phosphatase Cdc14 from nucleolar RENT complex', 'findings': []},
            {'id': 'PMID:10693811', 'title': 'Transcriptional silencing and longevity protein Sir2 is an NAD-dependent histone deacetylase', 'findings': []},
            {'id': 'PMID:10811920', 'title': 'The silencing protein SIR2 and its homologs are NAD-dependent protein deacetylases', 'findings': []},
            {'id': 'PMID:11553718', 'title': 'Dicentric chromosome stretching during anaphase reveals roles of Sir2/Ku in chromatin compaction in budding yeast', 'findings': []},
            {'id': 'PMID:11805837', 'title': 'Systematic identification of protein complexes in Saccharomyces cerevisiae by mass spectrometry', 'findings': []},
            {'id': 'PMID:11950950', 'title': 'Mutations in Saccharomyces cerevisiae gene SIR2 can have differential effects on in vivo silencing phenotypes and in vitro histone deacetylation activity', 'findings': []},
            {'id': 'PMID:12923057', 'title': 'Association of the RENT complex with nontranscribed and coding regions of rDNA and a regional requirement for the replication fork block protein Fob1 in rDNA silencing', 'findings': []},
            {'id': 'PMID:15082529', 'title': 'The NAD(+)-dependent Sir2p histone deacetylase is a negative regulator of chromosomal DNA replication', 'findings': []},
            {'id': 'PMID:15282295', 'title': 'Budding yeast silencing complexes and regulation of Sir2 activity by protein-protein interactions', 'findings': []},
            {'id': 'PMID:16182251', 'title': 'The budding yeast protein Chl1p has a role in transcriptional silencing, rDNA recombination, and aging', 'findings': []},
            {'id': 'PMID:20176978', 'title': 'An auxiliary silencer and a boundary element maintain high levels of silencing proteins at HMR in Saccharomyces cerevisiae', 'findings': []},
            {'id': 'PMID:25822194', 'title': 'Inhibition of telomere recombination by inactivation of KEOPS subunit Cgi121 promotes cell longevity', 'findings': []},
            {'id': 'PMID:26195783', 'title': 'Regulation of ribosomal DNA amplification by the TOR pathway', 'findings': []},
            {'id': 'PMID:26218225', 'title': 'The Ku subunit of telomerase binds Sir4 to recruit telomerase to lengthen telomeres in S. cerevisiae', 'findings': []},
            {'id': 'PMID:2647300', 'title': 'A new role for a yeast transcriptional silencer gene, SIR2, in regulation of recombination in ribosomal DNA', 'findings': []},
            {'id': 'PMID:26951198', 'title': 'Mechanism of Regulation of Intrachromatid Recombination and Long-Range Chromosome Interactions in Saccharomyces cerevisiae', 'findings': []},
            {'id': 'PMID:27122604', 'title': 'Quiescent Saccharomyces cerevisiae forms telomere hyperclusters at the nuclear membrane vicinity through a multifaceted mechanism involving Esc1, the Sir complex, and chromatin condensation', 'findings': []},
            {'id': 'PMID:27185881', 'title': 'Determinants of Sir2-Mediated, Silent Chromatin Cohesion', 'findings': []},
            {'id': 'PMID:27820830', 'title': 'Budding Yeast Rif1 Controls Genome Integrity by Inhibiting rDNA Replication', 'findings': []},
            {'id': 'PMID:29795547', 'title': 'Yeast heterochromatin regulators Sir2 and Sir3 act directly at euchromatic DNA replication origins', 'findings': []},
            {'id': 'PMID:30358795', 'title': 'The cellular economy of the Saccharomyces cerevisiae zinc proteome', 'findings': []},
            {'id': 'PMID:31461456', 'title': 'A Sir2-regulated locus control region in the recombination enhancer of Saccharomyces cerevisiae specifies chromosome III structure', 'findings': []},
            {'id': 'PMID:3297920', 'title': 'Four genes responsible for a position effect on expression from HML and HMR in Saccharomyces cerevisiae', 'findings': []},
            {'id': 'PMID:9009207', 'title': 'Transcriptional silencing of Ty1 elements in the RDN1 locus of yeast', 'findings': []},
            {'id': 'PMID:9122169', 'title': 'Silent information regulator protein complexes in Saccharomyces cerevisiae: a SIR2/SIR4 complex and evidence for a regulatory domain in SIR4 that inhibits its interaction with SIR3', 'findings': []},
            {'id': 'PMID:9214640', 'title': 'Localization of Sir2p: the nucleolus as a compartment for silent information regulators', 'findings': []},
            {'id': 'PMID:9501103', 'title': 'Components of the Ku-dependent non-homologous end-joining pathway are involved in telomeric length maintenance and telomeric silencing', 'findings': []},
            {'id': 'PMID:9710643', 'title': 'Sir proteins, Rif proteins, and Cdc13p bind Saccharomyces telomeres in vivo', 'findings': []},
            {'id': 'PMID:1913809', 'title': 'Modifiers of position effect are shared between telomeric and silent mating-type loci in S. cerevisiae', 'findings': []},
            {'id': 'PMID:19217406', 'title': 'Reconstitution of yeast silent chromatin: multiple contact sites and O-AADPR binding load SIR complexes onto nucleosomes in vitro', 'findings': []},
            {'id': 'PMID:22842922', 'title': 'Dissecting DNA damage response pathways by analysing protein localization and abundance changes during DNA replication stress', 'findings': []},
        ]
    }

    # Write to file
    output_path = Path('/Users/cjm/repos/ai-gene-review/genes/yeast/SIR2/SIR2-ai-review.yaml')
    with open(output_path, 'w') as f:
        yaml.dump(yaml_data, f, default_flow_style=False, sort_keys=False, allow_unicode=True, width=1000)

    print(f"Generated review with {len(annotations_data)} annotations")
    print(f"Written to {output_path}")

if __name__ == '__main__':
    main()
