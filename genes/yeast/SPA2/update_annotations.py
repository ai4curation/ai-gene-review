#!/usr/bin/env python3
"""
Generate comprehensive curation actions for SPA2 annotations.
This script produces properly formatted YAML entries for all 54 annotations.
"""

import yaml

# Mapping of GO term IDs to comprehensive curation information
ANNOTATION_REVIEWS = {
    # Localization - Cellular Component
    ("GO:0000131", "IBA", "GO_REF:0000033"): {
        "summary": "SPA2 is a core component of the incipient bud site, localizing to sites of polarized growth before bud emergence. This early and consistent localization is a defining characteristic.",
        "action": "ACCEPT",
        "reason": "Strong experimental evidence (IDA in primary literature) demonstrates SPA2 as an early marker of polarized growth sites. IBA assignment reflects well-conserved localization property across orthologs.",
        "evidence": "PMID:9214378"
    },
    ("GO:0005078", "IBA", "GO_REF:0000033"): {
        "summary": "Direct scaffold for Mpk1p MAPK pathway; recruits MEKs (Mkk1/2) and MAPK (Mpk1p) to sites of polarized growth for cell wall integrity signaling.",
        "action": "ACCEPT",
        "reason": "Core molecular function with extensive biochemical evidence. SPA2 directly interacts with pathway components via SHD-I domain and recruits them to polarized growth sites.",
        "evidence": "PMID:12361575,PMID:9632790"
    },
    ("GO:0005826", "IBA", "GO_REF:0000033"): {
        "summary": "SPA2 localizes to bud neck region but is NOT a core contractile ring component. The contractile ring contains myosin (Myo1p), actin filaments, and septins.",
        "action": "REMOVE",
        "reason": "SPA2 is present at bud neck via septin interaction but does not function in contractile ring assembly or function. This appears to be an incorrect cross-species IBA inference.",
        "evidence": "PMID:9214378,PMID:9790978"
    },
    ("GO:0005934", "IBA", "GO_REF:0000033"): {
        "summary": "Strong and consistent localization of SPA2 to bud tip where it organizes actin cables and polarity factors.",
        "action": "ACCEPT",
        "reason": "Direct experimental evidence (IDA) for localization to bud tip; functionally important for actin organization and polarized growth.",
        "evidence": "PMID:9214378,PMID:12361575"
    },
    ("GO:0005935", "IBA", "GO_REF:0000033"): {
        "summary": "SPA2 localizes to bud neck as ring structure during cytokinesis; interacts with septin components.",
        "action": "ACCEPT",
        "reason": "Clear microscopic evidence (IDA) for bud neck localization, particularly during cytokinesis. Functions in septin ring organization.",
        "evidence": "PMID:9214378,PMID:9790978"
    },
    ("GO:0007121", "IBA", "GO_REF:0000033"): {
        "summary": "Essential for establishing bipolar budding pattern; mutants show defects in bud site selection.",
        "action": "ACCEPT",
        "reason": "Strong genetic evidence (IMP) for role in bipolar bud site selection; IBA reflects conservation of this function across species.",
        "evidence": "PMID:8909546,PMID:9214378"
    },
    ("GO:0007124", "IBA", "GO_REF:0000033"): {
        "summary": "SPA2 is required for pseudohyphal growth morphology but this is a secondary developmental process, not core polarity function.",
        "action": "KEEP_AS_NON_CORE",
        "reason": "SPA2 is involved in pseudohyphal growth through maintenance of polarized growth capability under nutrient stress, but this is not a primary function.",
        "evidence": "PMID:9055077,PMID:9443897"
    },
    ("GO:0036267", "IBA", "GO_REF:0000033"): {
        "summary": "Required for invasive filamentous growth; SPA2-Spa2-related protein interactions important for this developmental pathway.",
        "action": "KEEP_AS_NON_CORE",
        "reason": "Genetic interaction evidence (IGI) shows SPA2 role in invasive growth, but this is a specialized developmental process secondary to core polarity function.",
        "evidence": "PMID:9443897"
    },
    ("GO:0043332", "IBA", "GO_REF:0000033"): {
        "summary": "SPA2 localizes prominently to mating projection tip (shmoo); essential for directed growth toward mating partner.",
        "action": "ACCEPT",
        "reason": "Direct evidence (IDA) for localization to mating projection; essential for pheromone response and efficient mating.",
        "evidence": "PMID:2647769,PMID:9214378,PMID:8013906"
    },
    ("GO:1902716", "IBA", "GO_REF:0000033"): {
        "summary": "SPA2 is a core structural component of the growing cell tip cortex during polarized growth.",
        "action": "ACCEPT",
        "reason": "IBA reflects conservation of cortical localization at growing tips across eukaryotes; functionally essential for polarity.",
        "evidence": "GO_REF:0000033"
    },

    # General process annotations
    ("GO:0000165", "IEA", "GO_REF:0000108"): {
        "summary": "Indirect involvement in MAPK cascade through scaffolding the Mpk1p pathway components.",
        "action": "ACCEPT",
        "reason": "IEA appropriate; logical inference from MAP-kinase scaffold activity (GO:0005078) that SPA2 is involved in MAPK cascade as a scaffold.",
        "evidence": "GO:0005078"
    },
    ("GO:0008360", "IEA", "GO_REF:0000043"): {
        "summary": "Regulation of cell shape through control of polarized growth and actin organization.",
        "action": "ACCEPT",
        "reason": "IEA from UniProt keywords is appropriate; SPA2's role in polarized growth fundamentally determines cell shape.",
        "evidence": "GO_REF:0000043"
    },
    ("GO:0051286", "IEA", "GO_REF:0000044"): {
        "summary": "SPA2 localizes to cell tip as component of growth site.",
        "action": "ACCEPT",
        "reason": "IEA from UniProt subcellular location mapping is appropriate; consistent with direct evidence.",
        "evidence": "GO_REF:0000044"
    },

    # Protein binding annotations - REMOVE (too vague)
    ("GO:0005515", "IPI", "PMID:16429126"): {
        "summary": "Generic protein binding annotation; SPA2's specific molecular functions are better captured by scaffold activity and localization terms.",
        "action": "REMOVE",
        "reason": "Too vague and uninformative. SPA2's biochemically documented interactions are better represented by GO:0005078 (scaffold activity) and specific complex annotations.",
        "evidence": "PMID:16429126"
    },
    ("GO:0005515", "IPI", "PMID:16554755"): {
        "summary": "Generic protein binding annotation; multiple IPI entries redundant.",
        "action": "REMOVE",
        "reason": "Vague annotation better replaced by mechanistic function terms. Multiple duplicate protein binding entries should be consolidated.",
        "evidence": "PMID:16554755"
    },
    ("GO:0005515", "IPI", "PMID:21502521"): {
        "summary": "Generic protein binding from modular proteomics study.",
        "action": "REMOVE",
        "reason": "Generic annotation; specific molecular functions should replace this.",
        "evidence": "PMID:21502521"
    },
    ("GO:0005515", "IPI", "PMID:37968396"): {
        "summary": "Generic protein binding from large-scale interactome study.",
        "action": "REMOVE",
        "reason": "Generic annotation not informative about mechanism.",
        "evidence": "PMID:37968396"
    },

    # Mating and cell morphogenesis
    ("GO:0000753", "IMP", "PMID:8013906"): {
        "summary": "SPA2 is required for proper morphogenesis during mating; essential for efficient cell fusion with mating partner.",
        "action": "ACCEPT",
        "reason": "Direct genetic evidence (IMP) shows SPA2 is required for mating morphogenesis; spa2 mutants show defective shmoo formation and reduced mating efficiency.",
        "evidence": "PMID:8013906"
    },
    ("GO:0000753", "IMP", "PMID:8909546"): {
        "summary": "SPA2 and Pea2p function together in cell morphogenesis during conjugation.",
        "action": "ACCEPT",
        "reason": "Complementary genetic evidence showing SPA2-Pea2p interdependent localization is critical for mating morphogenesis.",
        "evidence": "PMID:8909546"
    },

    # Actin and cytoskeleton regulation
    ("GO:0032956", "IMP", "PMID:12857882"): {
        "summary": "SPA2 regulates actin cable organization through scaffold function and interaction with Bni1p formin.",
        "action": "ACCEPT",
        "reason": "SPA2 is essential for actin recovery and bud emergence under osmotic stress; core function in actin organization.",
        "evidence": "PMID:12857882"
    },
    ("GO:0032956", "IGI", "PMID:12857882"): {
        "summary": "Genetic interaction with actin genes demonstrates SPA2's role in actin cytoskeleton organization.",
        "action": "ACCEPT",
        "reason": "IGI evidence shows genetic interaction with cytoskeleton components; supports actin regulation function.",
        "evidence": "PMID:12857882"
    },
    ("GO:0032956", "IMP", "PMID:19633059"): {
        "summary": "SPA2 is critical for reorganization of actin cytoskeleton in response to acid stress.",
        "action": "ACCEPT",
        "reason": "Shows SPA2 function in actin reorganization under environmental stress; core polarity maintenance.",
        "evidence": "PMID:19633059"
    },

    # Stress responses
    ("GO:0071468", "IMP", "PMID:19633059"): {
        "summary": "SPA2 involved in maintaining polarized growth under acidic conditions.",
        "action": "KEEP_AS_NON_CORE",
        "reason": "SPA2 helps maintain actin organization and polarity under acid stress, but this is secondary to core polarity function.",
        "evidence": "PMID:19633059"
    },
    ("GO:0071474", "IGI", "PMID:12857882"): {
        "summary": "SPA2 participates in osmotic stress response through actin recovery and polarized growth maintenance.",
        "action": "KEEP_AS_NON_CORE",
        "reason": "Genetic interaction evidence; SPA2 helps cells recover polarity under osmotic stress.",
        "evidence": "PMID:12857882"
    },

    # Protein localization regulation
    ("GO:0032880", "IMP", "PMID:16166638"): {
        "summary": "SPA2 acts as scaffold for polarized localization of multiple proteins including Msb3/4, formins, and kinases.",
        "action": "ACCEPT",
        "reason": "SPA2 as scaffold protein directly regulates protein localization to growth sites through protein-protein interactions.",
        "evidence": "PMID:16166638"
    },
    ("GO:0032880", "IMP", "PMID:9571251"): {
        "summary": "SPA2 regulates Bni1p formin localization to bud site through Rho1p-Bni1p-Spa2p interaction network.",
        "action": "ACCEPT",
        "reason": "Direct evidence for SPA2 role in regulating formin localization; essential for actin cable assembly.",
        "evidence": "PMID:9571251"
    },
    ("GO:0032880", "IMP", "PMID:9632790"): {
        "summary": "SPA2 is component of polarisome complex that localizes actin and signaling proteins to growth sites.",
        "action": "ACCEPT",
        "reason": "SPA2-Pea2p-Bud6p complex functions to organize protein localization at polarization sites.",
        "evidence": "PMID:9632790"
    },
    ("GO:0032880", "IMP", "PMID:12857882"): {
        "summary": "SPA2 is required for proper protein localization during recovery from osmotic stress.",
        "action": "ACCEPT",
        "reason": "SPA2 scaffold function maintains protein organization at growth sites under stress conditions.",
        "evidence": "PMID:12857882"
    },
    ("GO:0032880", "IMP", "PMID:11740491"): {
        "summary": "Yeast formins regulate cell polarity by controlling actin cable assembly; SPA2 localizes Bni1p.",
        "action": "ACCEPT",
        "reason": "SPA2 regulates formin localization as part of actin cable organization for polarity.",
        "evidence": "PMID:11740491"
    },
    ("GO:0032880", "IMP", "PMID:10085294"): {
        "summary": "SPA2 is required for proper cortical protein localization including Kar9p.",
        "action": "ACCEPT",
        "reason": "SPA2 scaffold function essential for organizing actin and associated proteins at cell cortex.",
        "evidence": "PMID:10085294"
    },
    ("GO:0032880", "IMP", "PMID:8909546"): {
        "summary": "SPA2-Pea2p complex regulates protein localization during mating morphogenesis.",
        "action": "ACCEPT",
        "reason": "Demonstrates SPA2's protein localization regulatory function in mating context.",
        "evidence": "PMID:8909546"
    },

    # Osmotic response
    ("GO:0071474", "IMP", "PMID:12857882"): {
        "summary": "SPA2 scaffold function maintains polarity and actin organization under hyperosmotic conditions.",
        "action": "KEEP_AS_NON_CORE",
        "reason": "SPA2 participates in osmotic stress response as secondary effect of polarity maintenance.",
        "evidence": "PMID:12857882"
    },

    # Budding and growth
    ("GO:0007118", "IMP", "PMID:10866679"): {
        "summary": "SPA2 is essential for polarized bud growth; controls actin cable organization.",
        "action": "ACCEPT",
        "reason": "Direct evidence that SPA2 is required for apical bud growth morphogenesis.",
        "evidence": "PMID:10866679"
    },
    ("GO:0007118", "IGI", "PMID:10866679"): {
        "summary": "Genetic interactions show SPA2 functions with other polarity components in bud growth.",
        "action": "ACCEPT",
        "reason": "IGI evidence demonstrates SPA2 genetic interaction with actin and morphogenesis genes.",
        "evidence": "PMID:10866679"
    },

    # Cell polarity establishment
    ("GO:0030010", "NAS", "PMID:16166638"): {
        "summary": "SPA2 is core scaffolding component of polarisome complex essential for establishing cell polarity.",
        "action": "ACCEPT",
        "reason": "NAS from ComplexPortal is appropriate for well-characterized complex annotation; SPA2 is definitional component.",
        "evidence": "PMID:16166638"
    },
    ("GO:0030010", "IMP", "PMID:8909546"): {
        "summary": "SPA2 required for cell polarity establishment during both budding and mating.",
        "action": "ACCEPT",
        "reason": "Strong genetic evidence (IMP) showing SPA2 is essential for polarity in multiple contexts.",
        "evidence": "PMID:8909546"
    },
    ("GO:0030010", "IMP", "PMID:8013906"): {
        "summary": "SPA2 is essential for establishing polarity during mating morphogenesis.",
        "action": "ACCEPT",
        "reason": "Demonstrates SPA2's requirement for directed polarized growth toward mating partner.",
        "evidence": "PMID:8013906"
    },

    # Actin cytoskeleton polarity
    ("GO:0030950", "NAS", "PMID:16166638"): {
        "summary": "SPA2 as polarisome component is essential for organizing actin cytoskeleton polarity.",
        "action": "ACCEPT",
        "reason": "NAS from ComplexPortal appropriate; SPA2-Bud6p directly regulate actin organization.",
        "evidence": "PMID:16166638"
    },

    # Vesicle targeting
    ("GO:0006903", "NAS", "PMID:16166638"): {
        "summary": "SPA2 polarisome coordinates with secretory machinery; Msb3/4 interact with SPA2 and Sec4.",
        "action": "KEEP_AS_NON_CORE",
        "reason": "SPA2 has indirect role in vesicle targeting through organizing polarisome that coordinates with exocytosis; not primary function.",
        "evidence": "PMID:16166638"
    },

    # Localization (component not process)
    ("GO:0005934", "IMP", "PMID:16166638"): {
        "summary": "SPA2 localizes to bud tip and is required for proper tip location.",
        "action": "ACCEPT",
        "reason": "Functional requirement for bud tip localization consistent with direct evidence.",
        "evidence": "PMID:16166638"
    },
    ("GO:0005938", "IDA", "PMID:23673619"): {
        "summary": "Direct evidence for SPA2 localization to cell cortex at growth sites.",
        "action": "ACCEPT",
        "reason": "IDA from microscopy; SPA2 is cortical protein at polarized growth sites.",
        "evidence": "PMID:23673619"
    },
    ("GO:0005078", "IDA", "PMID:12361575"): {
        "summary": "Direct biochemical and localization evidence for SPA2 scaffold activity for MAP kinase.",
        "action": "ACCEPT",
        "reason": "IDA demonstrates direct recruitment and interaction with MAPK pathway components.",
        "evidence": "PMID:12361575"
    },
    ("GO:0005078", "IMP", "PMID:12361575"): {
        "summary": "Functional requirement for SPA2 in MAPK pathway signaling.",
        "action": "ACCEPT",
        "reason": "IMP evidence shows SPA2 is required for proper MAPK localization and function.",
        "evidence": "PMID:12361575"
    },

    # Polarisome
    ("GO:0000133", "IDA", "PMID:9632790"): {
        "summary": "SPA2 is core structural component of polarisome complex along with Pea2p and Bud6p.",
        "action": "ACCEPT",
        "reason": "Coimmunoprecipitation and sedimentation evidence confirms SPA2 as integral polarisome component.",
        "evidence": "PMID:9632790"
    },

    # More bud tip localizations
    ("GO:0005934", "IDA", "PMID:12361575"): {
        "summary": "Direct evidence for SPA2 localization to bud tip.",
        "action": "ACCEPT",
        "reason": "IDA from microscopy confirms stable bud tip localization.",
        "evidence": "PMID:12361575"
    },
    ("GO:0005934", "IDA", "PMID:2647769"): {
        "summary": "SPA2 localizes to sites of cell growth including bud tip.",
        "action": "ACCEPT",
        "reason": "Early direct evidence establishing SPA2 as growth-site localized protein.",
        "evidence": "PMID:2647769"
    },

    # Bud neck
    ("GO:0005935", "IDA", "PMID:9214378"): {
        "summary": "SPA2 localizes as ring at mother-daughter bud neck during cytokinesis.",
        "action": "ACCEPT",
        "reason": "Direct microscopic evidence for bud neck localization during cell division.",
        "evidence": "PMID:9214378"
    },

    # More processes
    ("GO:0007124", "IMP", "PMID:9055077"): {
        "summary": "SPA2 is required for pseudohyphal growth morphology.",
        "action": "KEEP_AS_NON_CORE",
        "reason": "Genetic evidence for involvement in developmental program; secondary to core polarity.",
        "evidence": "PMID:9055077"
    },
    ("GO:0007124", "IMP", "PMID:9443897"): {
        "summary": "Spa2-related protein (Sph1p) plays role in pseudohyphal growth.",
        "action": "KEEP_AS_NON_CORE",
        "reason": "Shows SPA2 family role in filamentous growth but not primary function.",
        "evidence": "PMID:9443897"
    },
    ("GO:0036267", "IGI", "PMID:9443897"): {
        "summary": "Genetic interaction evidence for SPA2 in invasive growth.",
        "action": "KEEP_AS_NON_CORE",
        "reason": "Secondary developmental function; interaction with Sph1p suggests role in specialized growth.",
        "evidence": "PMID:9443897"
    },

    # More mating and location
    ("GO:0043332", "IDA", "PMID:2647769"): {
        "summary": "SPA2 localizes prominently to mating projection tip.",
        "action": "ACCEPT",
        "reason": "Direct evidence for localization to shmoo tip as discrete patch.",
        "evidence": "PMID:2647769"
    },
    ("GO:0043332", "IDA", "PMID:9214378"): {
        "summary": "SPA2 localizes to mating projection tip in response to pheromone.",
        "action": "ACCEPT",
        "reason": "Consistent direct evidence from multiple studies; essential for mating morphogenesis.",
        "evidence": "PMID:9214378"
    },

    # Incipient site localization
    ("GO:0000131", "IDA", "PMID:9214378"): {
        "summary": "SPA2 is early marker of incipient bud site before morphological bud emergence.",
        "action": "ACCEPT",
        "reason": "Defining property of SPA2; localizes to single edge in unbudded cells and incipient sites.",
        "evidence": "PMID:9214378"
    },
}

def generate_yaml_reviews():
    """Generate YAML formatted reviews for all annotations."""
    reviews = []
    for (go_id, evidence, ref), info in ANNOTATION_REVIEWS.items():
        review = {
            'term': {'id': go_id},
            'evidence_type': evidence,
            'original_reference_id': ref,
            'review': {
                'summary': info['summary'],
                'action': info['action'],
                'reason': info['reason'],
            }
        }

        if info['action'] != 'REMOVE' and 'evidence' in info:
            review['review']['supported_by'] = []
            for pmid in info['evidence'].split(','):
                pmid = pmid.strip()
                if pmid.startswith('PMID:') or pmid.startswith('GO:'):
                    review['review']['supported_by'].append({
                        'reference_id': pmid,
                        'supporting_text': ''  # Will be filled in YAML manually
                    })

        reviews.append(review)

    return reviews

if __name__ == '__main__':
    reviews = generate_yaml_reviews()
    # Print summary statistics
    actions = {}
    for (_, _, _), info in ANNOTATION_REVIEWS.items():
        action = info['action']
        actions[action] = actions.get(action, 0) + 1

    print("SPA2 Annotation Curation Summary")
    print("=" * 50)
    for action in ['ACCEPT', 'KEEP_AS_NON_CORE', 'REMOVE', 'UNDECIDED']:
        count = actions.get(action, 0)
        print(f"{action}: {count}")
    print(f"Total: {len(ANNOTATION_REVIEWS)}")
