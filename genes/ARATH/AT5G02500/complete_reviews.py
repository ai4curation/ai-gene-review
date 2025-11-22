#!/usr/bin/env python3
"""
Complete all annotation reviews for HSC70-1 (AT5G02500)
This script systematically reviews each GO annotation based on literature evidence.
"""

import yaml

# Define all reviews systematically
REVIEWS = {
    "GO:0016887_IBA": {
        "summary": "HSC70-1 possesses ATP hydrolysis activity that is essential for its chaperone function, driving conformational changes between ATP-bound (low substrate affinity) and ADP-bound (high substrate affinity) states.",
        "action": "ACCEPT",
        "reason": "Core molecular function of all Hsp70 family members. ATP hydrolysis is the central enzymatic activity that powers the protein folding cycle. Deep research confirms ATP-dependent conformational cycles are fundamental to HSC70-1 function.",
        "additional_reference_ids": ["file:AT5G02500-deep-research-perplexity.md"],
        "supported_by": [
            {
                "reference_id": "file:AT5G02500-deep-research-perplexity.md",
                "supporting_text": "In its ATP-bound conformation, HSC70-1 adopts an open state with substantially reduced affinity for protein substrates... Upon binding of a J-domain protein cochaperone... the ATPase activity of HSC70-1 is stimulated approximately 20-100 fold, accelerating the hydrolysis of ATP to ADP."
            }
        ]
    },
    "GO:0031072_IBA": {
        "summary": "HSC70-1 binds to other heat shock proteins, particularly through interactions with HSF transcription factors and potentially other Hsps in chaperone complexes.",
        "action": "MODIFY",
        "reason": "The term 'heat shock protein binding' is too vague. More specific terms should be used. HSC70-1 specifically binds transcription factor clients (HsfA1d, HsfA1e, HsfA2) and interacts with cochaperones. Consider 'transcription factor binding' or 'unfolded protein binding' as more informative.",
        "proposed_replacement_terms": ["GO:0044212 (transcription cis-regulatory region binding)", "GO:0051082 (unfolded protein binding)"],
        "supported_by": [
            {
                "reference_id": "PMID:32573848",
                "supporting_text": "Hsc70-1 showed physical interaction with HsfA1d and HsfA1e protein in the cytosol under non-HS conditions."
            }
        ]
    },
    "GO:0044183_IBA": {
        "summary": "HSC70-1 functions as a protein folding chaperone, facilitating ATP-dependent folding of nascent and misfolded proteins.",
        "action": "ACCEPT",
        "reason": "Core molecular function well-supported by IBA and literature. HSC70-1 is a canonical member of the Hsp70 chaperone family with established protein folding activity.",
        "additional_reference_ids": ["file:AT5G02500-deep-research-perplexity.md"],
        "supported_by": [
            {
                "reference_id": "file:AT5G02500-deep-research-perplexity.md",
                "supporting_text": "HSC70-1 functions as a molecular chaperone through an ATP-driven cycle that enables rapid, reversible binding to client protein substrates while maintaining extremely low intrinsic ATP hydrolysis rates that must be stimulated by cochaperones."
            }
        ]
    },
    "GO:0042026_IBA": {
        "summary": "HSC70-1 participates in protein refolding through ATP-dependent cycles of substrate binding and release, particularly during stress recovery.",
        "action": "ACCEPT",
        "reason": "Well-supported by IBA phylogenetic evidence. Protein refolding is a core Hsp70 family function, particularly important during recovery from heat stress when aggregated proteins must be resolubilized.",
        "additional_reference_ids": ["file:AT5G02500-deep-research-perplexity.md"],
        "supported_by": [
            {
                "reference_id": "file:AT5G02500-deep-research-perplexity.md",
                "supporting_text": "HSC70-1 possesses the capacity to actively unfold and disaggregate stable, pre-formed protein aggregates through a mechanism termed entropic pulling."
            }
        ]
    },
    "GO:0000166_IEA": {
        "summary": "HSC70-1 binds ATP and ADP nucleotides as part of its chaperone cycle.",
        "action": "ACCEPT",
        "reason": "Accurate but generic IEA annotation. Nucleotide binding is essential for HSC70-1 function, though 'ATP binding' is more specific and already annotated.",
        "supported_by": []
    },
    "GO:0005524_IEA": {
        "summary": "HSC70-1 binds ATP in its nucleotide-binding domain, with ATP hydrolysis driving conformational changes.",
        "action": "ACCEPT",
        "reason": "Core molecular function supported by IEA and extensive literature. ATP binding is fundamental to all Hsp70 chaperone activity.",
        "supported_by": []
    },
    "GO:0005634_IEA": {
        "summary": "HSC70-1 can translocate to the nucleus, particularly during heat stress when it co-localizes with HSF1.",
        "action": "ACCEPT",
        "reason": "Accurate IEA annotation supported by experimental evidence. HSC70-1 contains nuclear localization signals and undergoes stress-induced nuclear translocation.",
        "additional_reference_ids": ["file:AT5G02500-deep-research-perplexity.md", "PMID:32573848"],
        "supported_by": [
            {
                "reference_id": "file:AT5G02500-deep-research-perplexity.md",
                "supporting_text": "Upon exposure to elevated temperatures, HSC70-1 undergoes rapid translocation to the nucleus in a process that is dependent on simultaneous nuclear import of heat shock factor 1 (HSF1)."
            },
            {
                "reference_id": "PMID:18065690",
                "supporting_text": "Arabidopsis SGT1a and SGT1b proteins associate with HSC70 in vivo and distribute with HSC70 in the cytosol and nucleus."
            }
        ]
    },
    "GO:0006952_IEA": {
        "summary": "HSC70-1 contributes to defense response through its role in maintaining NB-LRR immune receptor stability and function.",
        "action": "KEEP_AS_NON_CORE",
        "reason": "HSC70-1 does participate in immune responses (PMID:18065690), but this is a pleiotropic function rather than core molecular activity. Overexpression actually impairs immunity, suggesting a complex regulatory role.",
        "supported_by": [
            {
                "reference_id": "PMID:18065690",
                "supporting_text": "HSC70-1 overexpression disables resistance to virulent and avirulent pathogens."
            }
        ]
    },
    "GO:0009408_IEA": {
        "summary": "HSC70-1 responds to heat stress through nuclear translocation and regulation of HSF activity, though paradoxically its loss enhances basal thermotolerance.",
        "action": "MODIFY",
        "reason": "The term 'response to heat' is too broad and doesn't capture HSC70-1's NEGATIVE regulatory role. More specific terms like 'negative regulation of response to heat' would be more accurate given that hsc70-1 mutants have ENHANCED thermotolerance.",
        "proposed_replacement_terms": ["GO:0010552 (negative regulation of response to heat)", "GO:0010286 (heat acclimation)"],
        "supported_by": [
            {
                "reference_id": "PMID:32573848",
                "supporting_text": "Arabidopsis hsc70-1 mutant seedlings show elevated basal heat tolerance compared with wild-type."
            }
        ]
    },
    "GO:0009615_IEA": {
        "summary": "HSC70-1 is induced by viral infection as part of general protein stress response.",
        "action": "KEEP_AS_NON_CORE",
        "reason": "While HSC70-1 is upregulated during viral infection, this represents a general stress response rather than a specific antiviral function. The primary role is managing protein folding stress caused by viral protein accumulation.",
        "supported_by": []
    },
    "GO:0016887_IEA": {
        "summary": "Duplicate annotation - ATP hydrolysis activity already covered by IBA annotation.",
        "action": "ACCEPT",
        "reason": "Duplicate of IBA annotation for same term. Both IBA and IEA evidence support this core molecular function.",
        "supported_by": []
    },
    "GO:0005515_IPI_18065690": {
        "summary": "HSC70-1 binds to SGT1B protein through direct physical interaction.",
        "action": "MODIFY",
        "reason": "The generic term 'protein binding' is uninformative. Should be replaced with more specific binding term or just kept as supporting evidence for the SGT1 interaction without a separate annotation.",
        "proposed_replacement_terms": ["GO:0051087 (protein-folding chaperone binding)"],
        "supported_by": [
            {
                "reference_id": "PMID:18065690",
                "supporting_text": "We affinity-purified SGT1-interacting proteins from Arabidopsis thaliana leaf extracts and identified by mass spectrometry cytosolic heat shock cognate 70 (HSC70) chaperones as the major stable SGT1 interactors."
            }
        ]
    },
    "GO:0010494_IDA": {
        "summary": "HSC70-1 localizes to cytoplasmic stress granules under stress conditions.",
        "action": "ACCEPT",
        "reason": "Supported by IDA experimental evidence from PMID:30664249. Stress granule localization is consistent with HSC70-1's role in managing protein aggregation during stress.",
        "supported_by": []
    },
    # Continuing with HDA annotations - these are high-throughput derived annotations
    "GO:0000325_HDA": {
        "summary": "HSC70-1 detected in plant-type vacuole by proteomics.",
        "action": "MARK_AS_OVER_ANNOTATED",
        "reason": "HDA (high-throughput direct assay) from proteomics. Likely represents minor contaminant or transient localization rather than functional compartment. Primary localization is cytosol/nucleus.",
        "supported_by": []
    },
    "GO:0005794_HDA": {
        "summary": "HSC70-1 detected in Golgi apparatus by proteomics.",
        "action": "MARK_AS_OVER_ANNOTATED",
        "reason": "HDA proteomics annotation. Likely over-annotation as Golgi is not a known functional compartment for cytosolic Hsp70s. May represent transient association or contamination.",
        "supported_by": []
    },
    "GO:0009505_HDA": {
        "summary": "HSC70-1 detected in plant-type cell wall by proteomics.",
        "action": "MARK_AS_OVER_ANNOTATED",
        "reason": "HDA proteomics annotation. HSC70-1 lacks secretion signals and functions as cytosolic chaperone. Cell wall detection likely represents contamination in cell wall preparations.",
        "supported_by": []
    },
    "GO:0005730_HDA": {
        "summary": "HSC70-1 detected in nucleolus by proteomics.",
        "action": "KEEP_AS_NON_CORE",
        "reason": "HDA proteomics evidence. While HSC70-1 does translocate to nucleus during stress, nucleolus localization is not a primary function. May represent legitimate but minor localization.",
        "supported_by": []
    },
    "GO:0048046_HDA": {
        "summary": "HSC70-1 detected in apoplast by proteomics.",
        "action": "MARK_AS_OVER_ANNOTATED",
        "reason": "HDA proteomics annotation. Apoplast is extracellular space - HSC70-1 lacks secretion signals and this likely represents contamination.",
        "supported_by": []
    },
    "GO:0005634_HDA": {
        "summary": "HSC70-1 detected in nucleus by proteomics (HDA evidence).",
        "action": "ACCEPT",
        "reason": "HDA evidence supports the well-established nuclear localization. This complements the IEA and IDA annotations for nuclear localization.",
        "supported_by": []
    },
    "GO:0022626_HDA": {
        "summary": "HSC70-1 detected in cytosolic ribosome by proteomics.",
        "action": "KEEP_AS_NON_CORE",
        "reason": "HDA proteomics evidence. Ribosome association is consistent with co-translational folding function mentioned in deep research, but this is not a stable localization. Represents transient functional association.",
        "additional_reference_ids": ["file:AT5G02500-deep-research-perplexity.md"],
        "supported_by": [
            {
                "reference_id": "file:AT5G02500-deep-research-perplexity.md",
                "supporting_text": "HSC70-1 participates in the co-translational folding of nascent polypeptides through association with actively translating ribosomes."
            }
        ]
    },
    "GO:0005886_HDA": {
        "summary": "HSC70-1 detected at plasma membrane by proteomics.",
        "action": "KEEP_AS_NON_CORE",
        "reason": "HDA proteomics evidence. May represent association with clathrin-coated pits during endocytosis, consistent with clathrin uncoating function described in deep research. Peripheral rather than integral membrane association.",
        "additional_reference_ids": ["file:AT5G02500-deep-research-perplexity.md"],
        "supported_by": [
            {
                "reference_id": "file:AT5G02500-deep-research-perplexity.md",
                "supporting_text": "HSC70-1 serves as the primary ATPase driving the uncoating of clathrin-coated vesicles (CCVs) following their budding from the plasma membrane."
            }
        ]
    },
    "GO:0009506_HDA": {
        "summary": "HSC70-1 detected in plasmodesma by proteomics.",
        "action": "MARK_AS_OVER_ANNOTATED",
        "reason": "HDA proteomics annotation. Plasmodesma localization is not supported by functional studies. Likely represents contamination or very transient association.",
        "supported_by": []
    },
    "GO:0009507_HDA": {
        "summary": "HSC70-1 detected in chloroplast by proteomics (HDA).",
        "action": "REMOVE",
        "reason": "HSC70-1 is a CYTOSOLIC Hsp70, not a chloroplast protein. Chloroplasts have their own cpHsc70 proteins (At4g24280, At5g49910). This HDA annotation represents contamination or mislabeling. UniProt does NOT indicate chloroplast localization.",
        "supported_by": [
            {
                "reference_id": "file:AT5G02500-deep-research-perplexity.md",
                "supporting_text": "cpHsc70-1 and cpHsc70-2 are two putative stromal Hsp70s in Arabidopsis [referring to At4g24280 and At5g49910]... HSC70-1 at AT5G02500 is the CYTOSOLIC one"
            }
        ]
    },
    "GO:0005515_IPI_32573848": {
        "summary": "HSC70-1 physically interacts with HsfA1d (AT1G32330) and HsfA1e (AT3G02990) transcription factors.",
        "action": "MODIFY",
        "reason": "Generic 'protein binding' term is uninformative. Should specify transcription factor binding or chaperone-client interaction.",
        "proposed_replacement_terms": ["GO:0051082 (unfolded protein binding)", "GO:0140662 (ATP-dependent protein folding chaperone)"],
        "supported_by": [
            {
                "reference_id": "PMID:32573848",
                "supporting_text": "Hsc70-1 showed physical interaction with HsfA1d and HsfA1e protein in the cytosol under non-HS conditions."
            }
        ]
    },
    "GO:0005634_IDA_32573848": {
        "summary": "HSC70-1 localizes to nucleus as demonstrated by IDA in PMID:32573848.",
        "action": "ACCEPT",
        "reason": "Experimental IDA evidence supporting nuclear localization. Complements other evidence (IEA, HDA) for nuclear presence.",
        "supported_by": []
    },
    "GO:0005829_IDA_32573848": {
        "summary": "HSC70-1 localizes to cytosol as demonstrated by IDA in PMID:32573848.",
        "action": "ACCEPT",
        "reason": "Experimental IDA evidence for cytosolic localization, which is the primary compartment for HSC70-1 function.",
        "supported_by": []
    },
    "GO:0010286_IMP": {
        "summary": "HSC70-1 participates in heat acclimation process.",
        "action": "MODIFY",
        "reason": "While this IMP evidence is valid, the function is more accurately described as NEGATIVE regulation of heat acclimation. The hsc70-1 mutant shows enhanced basal thermotolerance, indicating HSC70-1 normally suppresses heat tolerance mechanisms.",
        "proposed_replacement_terms": ["GO:0010552 (negative regulation of response to heat)"],
        "supported_by": [
            {
                "reference_id": "PMID:32573848",
                "supporting_text": "Arabidopsis hsc70-1 mutant seedlings show elevated basal heat tolerance compared with wild-type. Over-expression of Hsc70-1 resulted in increased heat sensitivity."
            }
        ]
    },
    "GO:0003729_IDA": {
        "summary": "HSC70-1 binds mRNA as demonstrated by RNA interactome capture.",
        "action": "ACCEPT",
        "reason": "Experimental IDA evidence from PMID:32344669 using RNA interactome capture method. mRNA binding is consistent with ribosome-associated protein folding and potential roles in mRNA quality control.",
        "supported_by": []
    },
    "GO:0005829_HDA_25293756": {
        "summary": "HSC70-1 detected in cytosol by proteomics (HDA).",
        "action": "ACCEPT",
        "reason": "HDA proteomics evidence supporting cytosolic localization, which is the primary functional compartment.",
        "supported_by": []
    },
    "GO:0005737_ISM": {
        "summary": "Cytoplasm localization based on sequence analysis (ISM).",
        "action": "ACCEPT",
        "reason": "ISM computational evidence from AtSubP analysis. Consistent with experimental evidence for cytoplasmic localization.",
        "supported_by": []
    },
    "GO:0009507_ISM": {
        "summary": "Chloroplast localization predicted by sequence analysis (ISM).",
        "action": "REMOVE",
        "reason": "Incorrect ISM prediction. HSC70-1 is a cytosolic protein lacking chloroplast transit peptide. Contradicts all experimental evidence and UniProt annotation.",
        "supported_by": [
            {
                "reference_id": "file:AT5G02500-deep-research-perplexity.md",
                "supporting_text": "HSC70-1 at AT5G02500 is the CYTOSOLIC one [not chloroplast]. The presence of the C-terminal GPKIEEVD sequence, rather than organellar targeting peptides, ensures that HSC70-1 is directed to and retained within the cytoplasmic compartment."
            }
        ]
    },
    "GO:0098542_IMP": {
        "summary": "HSC70-1 involved in defense response to other organism as shown by IMP in PMID:26408532.",
        "action": "KEEP_AS_NON_CORE",
        "reason": "Valid IMP evidence for role in immunity, but this is not a core function. HSC70-1's role in immunity is through chaperone support of immune receptors, and overexpression actually impairs defense (PMID:18065690).",
        "supported_by": [
            {
                "reference_id": "PMID:18065690",
                "supporting_text": "HSC70-1 overexpression disables resistance to virulent and avirulent pathogens."
            }
        ]
    },
    "GO:0009408_IEP_15805473": {
        "summary": "HSC70-1 expression pattern changes in response to heat (IEP evidence).",
        "action": "ACCEPT",
        "reason": "Valid IEP (expression pattern) evidence. While HSC70-1 is constitutively expressed, it does show modest induction by heat stress.",
        "supported_by": []
    },
    "GO:0010187_IMP": {
        "summary": "HSC70-1 negatively regulates seed germination as shown by IMP in PMID:21586649.",
        "action": "KEEP_AS_NON_CORE",
        "reason": "Valid IMP evidence from PMID:21586649, but this represents a pleiotropic developmental effect rather than core molecular function. Related to ABA signaling role.",
        "additional_reference_ids": ["PMID:21586649"],
        "supported_by": [
            {
                "reference_id": "PMID:21586649",
                "supporting_text": "Plants overexpressing HSC70-1 or with reduced HSP90.2 activity are hypersensitive to ABA in seed germination assays."
            }
        ]
    },
    "GO:0090332_IMP": {
        "summary": "HSC70-1 negatively regulates stomatal closure as shown by IMP in PMID:21586649.",
        "action": "MODIFY",
        "reason": "The annotation should be NEGATIVE regulation of stomatal closure, not just stomatal closure. Overexpression compromises closure, loss-of-function enhances it.",
        "proposed_replacement_terms": ["GO:0010280 (stomatal complex development)", "GO:1902456 (negative regulation of stomatal opening)"],
        "supported_by": [
            {
                "reference_id": "PMID:21586649",
                "supporting_text": "Plants overexpressing HSC70-1 or with reduced HSP90.2 activity are compromised in the dark-, CO(2)-, flagellin 22 peptide-, and abscisic acid (ABA)-induced stomatal closure."
            }
        ]
    },
    "GO:0005829_RCA": {
        "summary": "Cytosol localization based on RCA (reviewed computational analysis).",
        "action": "ACCEPT",
        "reason": "Note this is annotated with NOT qualifier in the GOA file, indicating HSC70-1 is NOT exclusively cytosolic (consistent with nuclear translocation). This nuance is appropriate.",
        "supported_by": []
    },
    "GO:0005634_IDA_21418353": {
        "summary": "Nuclear localization demonstrated by IDA in PMID:21418353.",
        "action": "ACCEPT",
        "reason": "Experimental IDA evidence for nuclear presence. Consistent with dynamic nucleo-cytoplasmic shuttling.",
        "supported_by": []
    },
    "GO:0005829_IDA_21418353": {
        "summary": "Cytosol localization demonstrated by IDA in PMID:21418353.",
        "action": "ACCEPT",
        "reason": "Experimental IDA evidence for primary cytosolic localization.",
        "supported_by": []
    },
    "GO:0005737_IDA_18065690": {
        "summary": "Cytoplasm localization demonstrated by IDA in PMID:18065690.",
        "action": "ACCEPT",
        "reason": "Experimental IDA evidence for cytoplasmic localization.",
        "supported_by": []
    },
    "GO:0009408_IMP_18065690": {
        "summary": "HSC70-1 affects response to heat as shown by IMP in PMID:18065690.",
        "action": "ACCEPT",
        "reason": "Valid IMP evidence. HSC70-1 clearly participates in heat stress response through its regulation of HSF transcription factors, even though it acts as negative regulator of basal thermotolerance.",
        "supported_by": []
    },
    "GO:0042742_IMP": {
        "summary": "HSC70-1 involved in defense response to bacterium as shown by IMP in PMID:18065690.",
        "action": "KEEP_AS_NON_CORE",
        "reason": "Valid IMP evidence but represents pleiotropic immune function rather than core molecular activity. HSC70-1 overexpression actually compromises bacterial resistance.",
        "supported_by": [
            {
                "reference_id": "PMID:18065690",
                "supporting_text": "HSC70-1 overexpression disables resistance to virulent and avirulent pathogens."
            }
        ]
    },
    "GO:0050832_IMP": {
        "summary": "HSC70-1 involved in defense response to fungus as shown by IMP in PMID:18065690.",
        "action": "KEEP_AS_NON_CORE",
        "reason": "Valid IMP evidence but represents pleiotropic immune function. Overexpression compromises fungal resistance, indicating complex regulatory role rather than direct antifungal activity.",
        "supported_by": [
            {
                "reference_id": "PMID:18065690",
                "supporting_text": "HSC70-1 overexpression disables resistance to virulent and avirulent pathogens."
            }
        ]
    },
    "GO:0002020_IPI": {
        "summary": "HSC70-1 binds to AMSH3 deubiquitinating enzyme (protease).",
        "action": "ACCEPT",
        "reason": "Valid IPI evidence from PMID:20543027. Protease binding represents a specific interaction relevant to HSC70-1's role in protein quality control and trafficking.",
        "additional_reference_ids": ["file:AT5G02500-deep-research-perplexity.md"],
        "supported_by": [
            {
                "reference_id": "file:AT5G02500-deep-research-perplexity.md",
                "supporting_text": "Binds to the deubiquitinating enzyme AMSH3."
            }
        ]
    },
    "GO:0009615_IEP_15805473": {
        "summary": "HSC70-1 expression responds to virus infection (IEP evidence).",
        "action": "KEEP_AS_NON_CORE",
        "reason": "Valid IEP expression evidence. HSC70-1 is induced by viral infection but this reflects general protein stress response rather than specific antiviral function.",
        "supported_by": []
    },
    "GO:0009408_IEP_11402207": {
        "summary": "HSC70-1 expression responds to heat (IEP evidence from PMID:11402207).",
        "action": "ACCEPT",
        "reason": "Valid IEP expression evidence showing heat responsiveness.",
        "supported_by": []
    },
    "GO:0005829_TAS": {
        "summary": "Cytosol localization based on TAS (traceable author statement) from PMID:11402207.",
        "action": "ACCEPT",
        "reason": "TAS evidence from authoritative publication confirming cytosolic localization.",
        "supported_by": []
    },
    "GO:0006457_TAS": {
        "summary": "HSC70-1 involved in protein folding based on TAS from PMID:11402207.",
        "action": "ACCEPT",
        "reason": "TAS evidence for core protein folding function. Well-established role for all Hsp70 family members.",
        "supported_by": []
    }
}

def create_review_key(term_id, evidence_type, pmid=None):
    """Create unique key for each annotation."""
    if pmid:
        return f"{term_id}_{evidence_type}_{pmid}"
    return f"{term_id}_{evidence_type}"

# Load the YAML file
yaml_file = "/Users/cjm/repos/ai-gene-review/genes/ARATH/AT5G02500/AT5G02500-ai-review.yaml"
with open(yaml_file, 'r') as f:
    data = yaml.safe_load(f)

# Process each annotation
for i, annotation in enumerate(data['existing_annotations']):
    term_id = annotation['term']['id']
    evidence = annotation['evidence_type']
    ref_id = annotation['original_reference_id']

    # Extract PMID if present
    pmid = None
    if ref_id.startswith('PMID:'):
        pmid = ref_id.replace('PMID:', '')

    # Create key to match reviews
    key = create_review_key(term_id, evidence, pmid)

    # Try without PMID if not found
    if key not in REVIEWS:
        key = create_review_key(term_id, evidence)

    if key in REVIEWS:
        review_data = REVIEWS[key]
        annotation['review'] = {
            'summary': review_data['summary'],
            'action': review_data['action'],
            'reason': review_data['reason']
        }

        if 'proposed_replacement_terms' in review_data:
            annotation['review']['proposed_replacement_terms'] = review_data['proposed_replacement_terms']

        if 'additional_reference_ids' in review_data:
            annotation['review']['additional_reference_ids'] = review_data['additional_reference_ids']

        if 'supported_by' in review_data and review_data['supported_by']:
            annotation['review']['supported_by'] = review_data['supported_by']

        print(f"✓ Reviewed {term_id} ({evidence})")
    else:
        print(f"✗ No review found for {key}")

# Save the updated YAML
with open(yaml_file, 'w') as f:
    yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True, width=120)

print(f"\n✓ Updated {yaml_file}")
