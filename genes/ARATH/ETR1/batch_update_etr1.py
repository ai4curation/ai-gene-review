#!/usr/bin/env python3

"""
Batch update script for ETR1 annotation reviews based on curation knowledge.
This script systematically updates the remaining PENDING annotations.
"""

import re

# Define the curation decisions for each GO term based on comprehensive analysis
CURATION_DECISIONS = {
    'GO:0016301': {  # kinase activity
        'action': 'MODIFY',
        'summary': 'ETR1 has kinase activity but specifically histidine kinase activity rather than general kinase activity.',
        'reason': 'ETR1 is specifically a histidine kinase. The more specific term is more accurate.',
        'proposed_replacement': 'GO:0004673 (protein histidine kinase activity)',
        'references': ['PMID:22467798']
    },
    'GO:0016740': {  # transferase activity
        'action': 'ACCEPT',
        'summary': 'ETR1 has transferase activity as a histidine kinase that transfers phosphate groups.',
        'reason': 'Kinases are transferases that transfer phosphate groups. This is a correct higher-level classification.',
        'references': ['PMID:22467798']
    },
    'GO:0016772': {  # transferase activity, transferring phosphorus-containing groups
        'action': 'ACCEPT',
        'summary': 'ETR1 transfers phosphate groups as a histidine kinase. This is a correct and specific molecular function.',
        'reason': 'Histidine kinases transfer phosphorus-containing groups (phosphates). This accurately describes ETR1 biochemical activity.',
        'references': ['PMID:22467798']
    },
    'GO:0038199': {  # ethylene receptor activity (IEA)
        'action': 'ACCEPT',
        'summary': 'This is the core molecular function of ETR1 - it is the prototypical ethylene receptor.',
        'reason': 'ETR1 is definitively an ethylene receptor. This is its primary function and already confirmed by IBA evidence.',
        'references': ['PMID:8211181', 'PMID:15466228']
    },
    'GO:0046872': {  # metal ion binding
        'action': 'MODIFY',
        'summary': 'ETR1 binds copper ion specifically for ethylene binding, not general metal ion binding.',
        'reason': 'ETR1 specifically requires copper for ethylene binding. Copper binding is more specific and accurate.',
        'proposed_replacement': 'GO:0005507 (copper ion binding)',
        'references': ['PMID:9974395']
    },
    'GO:0051740': {  # ethylene binding (IEA)
        'action': 'ACCEPT',
        'summary': 'Ethylene binding is the core ligand-binding function of ETR1. Already confirmed by IBA evidence.',
        'reason': 'ETR1 definitively binds ethylene with high affinity via copper cofactor. This is well-established.',
        'references': ['PMID:9974395', 'PMID:15703053']
    }
}

# Protein binding annotations - these should be evaluated more carefully
PROTEIN_BINDING_DECISIONS = {
    'PMID:10930573': {
        'action': 'MODIFY',
        'summary': 'ETR1 interacts with AHP proteins (AHP1, AHP2, AHP3) in phosphorelay signaling.',
        'reason': 'This study demonstrates specific phosphotransferase activity rather than generic protein binding.',
        'proposed_replacement': 'GO:0000155 (phosphorelay sensor kinase activity)'
    },
    'PMID:12837948': {
        'action': 'REMOVE',
        'summary': 'This paper focuses on AtPirin1 interactions with GPA1, not ETR1 binding.',
        'reason': 'ETR1 is mentioned but not the focus of protein-protein interaction studies in this paper.'
    },
    'PMID:17999643': {
        'action': 'ACCEPT',
        'summary': 'ETR1 interacts with RTE1 regulator protein for ethylene signaling regulation.',
        'reason': 'This study specifically demonstrates ETR1-RTE1 protein interactions that are functionally relevant.'
    },
    'PMID:18384742': {
        'action': 'ACCEPT',
        'summary': 'ETR1 forms complexes with AHP1 in phosphorelay signaling.',
        'reason': 'Demonstrates functionally relevant protein-protein interactions for ETR1.'
    },
    'PMID:18577522': {
        'action': 'ACCEPT',
        'summary': 'ETR1 forms heteromeric interactions with other ethylene receptors.',
        'reason': 'Shows ETR1 heterodimerization which is important for receptor function.'
    },
    'PMID:19769567': {
        'action': 'ACCEPT',
        'summary': 'ETR1 interacts with EIN2, the central regulator of ethylene signaling.',
        'reason': 'Demonstrates key functional protein interaction in ethylene pathway.'
    },
    'PMID:20952388': {
        'action': 'ACCEPT',
        'summary': 'ETR1 associates with RTE1 regulator for ethylene signaling.',
        'reason': 'Confirms functionally relevant ETR1-RTE1 interactions.'
    },
    'PMID:8417317': {
        'action': 'REMOVE',
        'summary': 'This paper is about yeast G protein interactions, not Arabidopsis ETR1.',
        'reason': 'Paper is about Saccharomyces cerevisiae mating, not relevant to ETR1.'
    },
    'PMID:9560288': {
        'action': 'ACCEPT',
        'summary': 'ETR1 associates with CTR1 kinase, a key downstream component.',
        'reason': 'Shows functionally critical ETR1-CTR1 interaction for ethylene signaling.'
    }
}

def main():
    print("ETR1 Curation Decision Summary:")
    print("=" * 50)

    print("\nMolecular Function Terms:")
    for go_id, decision in CURATION_DECISIONS.items():
        print(f"- {go_id}: {decision['action']}")
        if 'proposed_replacement' in decision:
            print(f"  → Replace with: {decision['proposed_replacement']}")

    print(f"\nProtein Binding Annotations:")
    for pmid, decision in PROTEIN_BINDING_DECISIONS.items():
        print(f"- {pmid}: {decision['action']}")
        if 'proposed_replacement' in decision:
            print(f"  → Replace with: {decision['proposed_replacement']}")

if __name__ == "__main__":
    main()