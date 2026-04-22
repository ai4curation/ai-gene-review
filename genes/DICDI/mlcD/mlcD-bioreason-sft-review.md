# BioReason-Pro SFT Review: mlcD (Dictyostelium discoideum)

Source: mlcD-deep-research-bioreason-sft.md

- **Correctness**: 2/5
- **Completeness**: 3/5

## Functional Summary Review

The BioReason SFT functional summary describes mlcD as:

> A calmodulin-like calcium sensor in Dictyostelium that binds calcium to expose target-specific pockets and engage the myosin II heavy chain.

This contains a fundamental error: MlcD does not bind the myosin **II** heavy chain. MlcD is the dedicated light chain for MyoD, which is a **class I** myosin. The paper that originally characterized MlcD explicitly identifies it as associated with "MyoD, a long-tailed class I myosin" (PMID:12826013). The summary also incorrectly describes MlcD as a "calcium sensor," when the original characterization explicitly states that "the low affinity of MlcD for Ca2+ indicates that it cannot function as a sensor of physiological Ca2+" (PMID:12826013, Kd = 52 uM).

The summary further claims:

> By tuning myosin II filament assembly and contractility at the cortex and cleavage furrow, it coordinates actin polymerization dynamics for cytokinesis, macropinocytosis, phagocytic engulfment, and rapid plasma membrane repair.

This is largely fabricated. There is no evidence that MlcD regulates myosin II filament assembly, participates in cytokinesis, controls actin filament polymerization, mediates phagocytic engulfment, or is involved in plasma membrane repair. The thinking trace arrives at these functions by assuming MlcD acts as a calcium-dependent regulator of myosin II, which is incorrect on both counts (wrong myosin class, and calcium-insensitive binding).

The summary correctly notes localization to macropinocytic cups, which is supported by Brzeska et al. 2019 (PMID:31774725), though this localization derives from the Myo1D heavy chain rather than from MlcD acting independently.

> Its calcium-dependent interactions with kinases, phosphatases, and small GTPase regulators integrate cytoskeletal mechanics with signaling

There is no evidence for any of these interactions. MlcD specifically and exclusively associates with the MyoD heavy chain. Unlike calmodulin, which promiscuously regulates many targets, MlcD has diverged to become a dedicated structural subunit.

## Comparison with interpro2go

The InterPro2GO annotation (GO_REF:0000002) for MlcD predicts GO:0005509 calcium ion binding based on the EF-hand domain (IPR002048). This is technically correct (MlcD does bind calcium, albeit at low affinity) but functionally misleading.

The BioReason SFT trace starts from the same InterPro domain architecture and arrives at the same calcium binding prediction but then makes far more egregious errors. It interprets the calmodulin/myosin light chain family membership (IPR050230) as evidence for calcium-dependent conformational switching and promiscuous target engagement, which is the calmodulin paradigm but not what MlcD actually does. The thinking trace explicitly states: "This EF-hand architecture directly encodes GO:0005509 calcium ion binding as the primary molecular function. The calmodulin/myosin light chain-like family context predicts high-affinity recognition of IQ motifs on myosin heavy chains, supporting GO:0032036 myosin heavy chain binding." The first part is essentially InterPro2GO. The second part (myosin heavy chain binding) is actually correct, but then the trace veers off into myosin II biology, which is wrong.

BioReason adds substantial speculative biology beyond InterPro2GO -- cytokinesis, GTPase regulation, actin polymerization control, phagocytosis, nucleus organization, plasma membrane repair -- none of which is supported by evidence for this specific protein. This represents a hallucination pattern where the model fills in biology from the calmodulin literature and applies it indiscriminately to a divergent family member.

In summary, InterPro2GO is more honest in its limited prediction (calcium binding from EF-hand domains), while BioReason generates a more detailed narrative that is largely incorrect because it fails to account for the functional divergence of MlcD from calmodulin.

## Notes on thinking trace

The thinking trace correctly identifies the InterPro domain architecture with multiple EF-hand domains. However, it makes a critical error early on by treating MlcD as a canonical "Ca2+-dependent conformational switch" rather than recognizing the degenerate calcium-binding sites. The trace states "Ca2+ binding to the N-terminal EF-hands primes the sensor to engage myosin II heavy chain IQ motifs" -- this is wrong on two counts: MlcD binding to MyoD is calcium-insensitive, and the target is myosin I, not myosin II.

The trace then cascades this error into an elaborate but unsupported functional network involving myosin II filament assembly regulation, cytokinesis, ROCO-family kinases, protein phosphatase 2B, IP3 receptors, and Ras GTPase-activating proteins. None of these interactions have been demonstrated for MlcD. This is a clear failure mode where the model treats domain-family membership as sufficient to predict specific protein-protein interactions and biological processes.

The GO term predictions section in the BioReason output is empty (no MF, BP, or CC predictions listed), so the scoring here is based entirely on the functional summary and thinking trace narrative.
