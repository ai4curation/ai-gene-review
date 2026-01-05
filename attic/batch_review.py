#!/usr/bin/env python3
"""
Batch review script for P14713 (PHYB) annotations.
This script helps systematically review the 98 GOA annotations.
"""

import yaml
from pathlib import Path

# Load the current YAML
yaml_path = Path("P14713-ai-review.yaml")
with open(yaml_path) as f:
    data = yaml.safe_load(f)

# Define review decisions for different annotation types
reviews = {
    # Cellular Components - ACCEPT core localizations
    "GO:0005634": {  # nucleus (multiple instances)
        "action": "ACCEPT",
        "summary": "PHYB translocates to nucleus upon red light activation. Core function.",
    },
    "GO:0016604": {  # nuclear body
        "action": "ACCEPT",
        "summary": "PHYB forms nuclear photobodies upon light activation, core structural feature.",
    },
    "GO:0005829": {  # cytosol
        "action": "ACCEPT",
        "summary": "PHYB is cytoplasmic in darkness (Pr form), translocates to nucleus in light.",
    },
    "GO:0005737": {  # cytoplasm
        "action": "ACCEPT",
        "summary": "PHYB is cytoplasmic in darkness, broader term than cytosol but correct.",
    },
    "GO:0005654": {  # nucleoplasm
        "action": "ACCEPT",
        "summary": "PHYB localizes to nucleoplasm when in nucleus.",
    },
    "GO:0016607": {  # nuclear speck
        "action": "ACCEPT",
        "summary": "PHYB forms nuclear speckles/photobodies upon light activation.",
    },
    "GO:0005886": {  # plasma membrane
        "action": "REMOVE",
        "summary": "No evidence PHYB localizes to plasma membrane. Cytoplasm and nucleus only.",
        "reason": "ISM annotation without experimental support. PHYB is cytoplasmic/nuclear, not membrane-associated.",
    },

    # Molecular Functions - ACCEPT core activities
    "GO:0031516": {  # far-red light photoreceptor activity
        "action": "ACCEPT",
        "summary": "Core function. PHYB absorbs far-red light in Pfr form.",
    },
    "GO:0031517": {  # red light photoreceptor activity
        "action": "ACCEPT",
        "summary": "Core function. PHYB absorbs red light in Pr form.",
    },
    "GO:0009883": {  # red or far-red light photoreceptor activity
        "action": "ACCEPT",
        "summary": "Core function. PHYB is photoconvertible between red/far-red absorbing forms.",
    },
    "GO:0009881": {  # photoreceptor activity
        "action": "ACCEPT",
        "summary": "Core function, parent term of red/far-red photoreceptor activity.",
    },
    "GO:0042803": {  # protein homodimerization activity
        "action": "ACCEPT",
        "summary": "Core function. PHYB functions as a homodimer, confirmed by crystal structure.",
    },
    "GO:0042802": {  # identical protein binding (multiple instances)
        "action": "ACCEPT",
        "summary": "PHYB forms homodimers and heterodimers with other phytochromes.",
    },
    "GO:0043565": {  # sequence-specific DNA binding
        "action": "ACCEPT",
        "summary": "PHYB binds DNA in temperature-dependent manner to regulate transcription.",
    },
    "GO:1990841": {  # promoter-specific chromatin binding
        "action": "ACCEPT",
        "summary": "PHYB associates with promoters of target genes in temperature-dependent manner.",
    },
    "GO:0017012": {  # protein-phytochromobilin linkage
        "action": "ACCEPT",
        "summary": "Core function. PHYB has covalently-linked phytochromobilin chromophore at Cys-357.",
    },
    "GO:0017006": {  # protein-tetrapyrrole linkage
        "action": "ACCEPT",
        "summary": "Parent term of phytochromobilin linkage. Chromophore is a tetrapyrrole.",
    },

    # Kinase activity - KEEP_AS_NON_CORE (not primary function)
    "GO:0000155": {  # phosphorelay sensor kinase activity
        "action": "KEEP_AS_NON_CORE",
        "summary": "PHYB has histidine kinase-related domain but kinase activity is not well-established as core function.",
        "reason": "Domain present but regulatory activity primarily through PIF interactions, not kinase activity.",
    },

    # Generic terms - KEEP_AS_NON_CORE or REMOVE
    "GO:0005515": {  # protein binding (many instances)
        "action": "KEEP_AS_NON_CORE",
        "summary": "PHYB interacts with many proteins (PIFs, CRYs, VOZs, etc.) but this is too generic.",
        "reason": "Generic term. More specific molecular function terms better describe PHYB's role.",
    },
    "GO:0003677": {  # DNA binding
        "action": "MODIFY",
        "summary": "Too generic. PHYB has sequence-specific DNA binding activity.",
        "reason": "Replace with more specific term GO:0043565 (sequence-specific DNA binding).",
    },

    # Signal transduction - KEEP_AS_NON_CORE
    "GO:0007165": {  # signal transduction
        "action": "KEEP_AS_NON_CORE",
        "summary": "PHYB transduces light signals but this is too generic.",
        "reason": "More specific terms describe PHYB's role in red/far-red light signaling.",
    },
    "GO:0000160": {  # phosphorelay signal transduction system
        "action": "KEEP_AS_NON_CORE",
        "summary": "Inferred from kinase domain but not proven as core mechanism.",
        "reason": "PHYB signal transduction primarily through PIF degradation, not phosphorelay.",
    },

    # Transcriptional regulation
    "GO:0006355": {  # regulation of DNA-templated transcription
        "action": "KEEP_AS_NON_CORE",
        "summary": "PHYB regulates transcription but indirectly via PIF degradation.",
        "reason": "Generic term. More specific negative regulation term exists.",
    },
    "GO:0045892": {  # negative regulation of DNA-templated transcription
        "action": "ACCEPT",
        "summary": "PHYB negatively regulates transcription by promoting PIF degradation.",
    },

    # Biological Processes - Core functions
    "GO:0009640": {  # photomorphogenesis
        "action": "ACCEPT",
        "summary": "Core biological role. PHYB is master regulator of photomorphogenesis.",
    },
    "GO:0010161": {  # red light signaling pathway
        "action": "ACCEPT",
        "summary": "Core process. PHYB mediates red light signaling.",
    },
    "GO:0010018": {  # far-red light signaling pathway
        "action": "ACCEPT",
        "summary": "PHYB involved in far-red light responses (dark reversion, phyA interaction).",
    },
    "GO:0010017": {  # red or far-red light signaling pathway
        "action": "ACCEPT",
        "summary": "Parent term encompassing PHYB's role in both red and far-red signaling.",
    },
    "GO:0009585": {  # red, far-red light phototransduction
        "action": "ACCEPT",
        "summary": "Core process. PHYB transduces red/far-red light signals.",
    },
    "GO:0009584": {  # detection of visible light
        "action": "ACCEPT",
        "summary": "Parent term. PHYB detects visible light (red/far-red region).",
    },
    "GO:0009416": {  # response to light stimulus (multiple instances)
        "action": "ACCEPT",
        "summary": "Broad but correct. PHYB responds to and mediates light responses.",
    },
    "GO:0010218": {  # response to far red light
        "action": "ACCEPT",
        "summary": "PHYB involved in far-red light responses including dark reversion.",
    },
    "GO:0010244": {  # response to low fluence blue light stimulus by blue low-fluence system
        "action": "KEEP_AS_NON_CORE",
        "summary": "PHYB has minor role in blue light signaling via CRY interaction.",
        "reason": "Not a core function. PHYB primarily red/far-red photoreceptor.",
    },
    "GO:0010202": {  # response to low fluence red light stimulus
        "action": "ACCEPT",
        "summary": "PHYB mediates low fluence red light responses.",
    },

    # Temperature sensing - Core function
    "GO:0009266": {  # response to temperature stimulus (multiple instances)
        "action": "ACCEPT",
        "summary": "Core function. PHYB functions as thermosensor with temperature-dependent Pfr stability.",
    },
    "GO:0009409": {  # response to cold (multiple instances)
        "action": "KEEP_AS_NON_CORE",
        "summary": "PHYB involved in cold responses but indirect/modulatory role.",
        "reason": "PHYB modulates cold-regulated gene expression but not primary cold sensor.",
    },
    "GO:0009408": {  # response to heat
        "action": "KEEP_AS_NON_CORE",
        "summary": "PHYB thermosensor function relates to warm temperatures but broader than core function.",
    },

    # Circadian
    "GO:0009649": {  # entrainment of circadian clock
        "action": "ACCEPT",
        "summary": "Core function. PHYB entrains circadian clock to light-dark cycles.",
    },
    "GO:0010617": {  # circadian regulation of calcium ion oscillation
        "action": "KEEP_AS_NON_CORE",
        "summary": "PHYB regulates circadian calcium oscillations but downstream effect.",
        "reason": "Specific downstream phenotype, not core function.",
    },

    # Developmental processes - KEEP_AS_NON_CORE (downstream)
    "GO:2000028": {  # regulation of photoperiodism, flowering
        "action": "KEEP_AS_NON_CORE",
        "summary": "PHYB regulates flowering time but downstream developmental process.",
        "reason": "Important role but consequence of light/temperature sensing, not core molecular function.",
    },
    "GO:0010029": {  # regulation of seed germination
        "action": "KEEP_AS_NON_CORE",
        "summary": "PHYB regulates seed germination via ABA/GA balance but downstream process.",
    },
    "GO:0010374": {  # stomatal complex development
        "action": "KEEP_AS_NON_CORE",
        "summary": "PHYB affects stomatal development but indirect developmental role.",
    },
    "GO:0009630": {  # gravitropism
        "action": "KEEP_AS_NON_CORE",
        "summary": "PHYB has role in gravitropism but minor/modulatory.",
        "reason": "PHYB modulates gravitropic responses but not primary gravity sensor.",
    },
    "GO:0009638": {  # phototropism
        "action": "KEEP_AS_NON_CORE",
        "summary": "PHYB contributes to phototropism but PHOT photoreceptors are primary.",
    },

    # Metabolic/physiological processes - KEEP_AS_NON_CORE
    "GO:0015979": {  # photosynthesis
        "action": "KEEP_AS_NON_CORE",
        "summary": "PHYB enhances photosynthesis by regulating stomata/development but indirect.",
        "reason": "PHYB regulates photosynthesis indirectly via development, not direct role.",
    },
    "GO:0010148": {  # transpiration
        "action": "KEEP_AS_NON_CORE",
        "summary": "PHYB affects transpiration via stomatal regulation but indirect.",
    },
    "GO:0009687": {  # abscisic acid metabolic process
        "action": "KEEP_AS_NON_CORE",
        "summary": "PHYB regulates ABA metabolism in seeds but downstream effect.",
    },
    "GO:0009643": {  # photosynthetic acclimation
        "action": "KEEP_AS_NON_CORE",
        "summary": "PHYB involved in photosynthetic acclimation via thermosensing but indirect.",
    },

    # Stress responses - KEEP_AS_NON_CORE or MARK_AS_OVER_ANNOTATED
    "GO:0042742": {  # defense response to bacterium
        "action": "KEEP_AS_NON_CORE",
        "summary": "PHYB modulates defense responses but indirect role.",
        "reason": "PHYB affects defense via JA signaling modulation, not primary defense regulator.",
    },
    "GO:0009867": {  # jasmonic acid mediated signaling pathway
        "action": "KEEP_AS_NON_CORE",
        "summary": "PHYB modulates JA signaling but not core function.",
    },
    "GO:0031347": {  # regulation of defense response
        "action": "KEEP_AS_NON_CORE",
        "summary": "PHYB modulates defense via light/JA crosstalk but indirect.",
    },
    "GO:0071588": {  # hydrogen peroxide mediated signaling pathway
        "action": "KEEP_AS_NON_CORE",
        "summary": "PHYB involved in ROS signaling during stress but indirect role.",
        "reason": "PHYB modulates ROS responses but not primary ROS sensor/generator.",
    },

    # Chromatin
    "GO:0006325": {  # chromatin organization
        "action": "ACCEPT",
        "summary": "PHYB controls chromatin compaction in light-dependent manner.",
    },
}

print(f"Loaded {len(data['existing_annotations'])} annotations")
print(f"Defined reviews for {len(reviews)} unique GO terms")
print("\nAnnotations by action:")
for action in ["ACCEPT", "KEEP_AS_NON_CORE", "MODIFY", "REMOVE", "MARK_AS_OVER_ANNOTATED"]:
    count = sum(1 for v in reviews.values() if v["action"] == action)
    print(f"  {action}: {count}")
