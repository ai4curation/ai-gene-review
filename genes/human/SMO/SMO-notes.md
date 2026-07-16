# SMO review notes

## Scope and sources

This journal records the manual review of the 98 seeded human SMO GO annotations plus one proposed new molecular-function annotation. I inspected the reviewed UniProtKB record Q99835, the complete GOA seed, every locally cached publication cited by GOA, and the current official GO records used in `core_functions`. No deep-research provider output was available: the previously attempted Falcon and Perplexity-lite calls failed, so they were not retried and no provider-named report was created.

The official QuickGO service was checked on 2026-07-14 for the author-supplied core-function terms. It returned current, non-obsolete records for GO:0004930 “G protein-coupled receptor activity,” GO:0015485 “cholesterol binding,” GO:0004862 “cAMP-dependent protein kinase inhibitor activity,” GO:0007224 “smoothened signaling pathway,” and GO:0098804 “non-motile cilium membrane.”

## Project-independent molecular model

SMO is a class-F seven-pass GPCR and the membrane transducer between Patched/sterol control and GLI activation. Direct structural work describes it as a Frizzled-class GPCR and shows oxysterol-bound human SMO coupled to heterotrimeric Gi [PMID:31168089 “We present a cryo-electron microscopy structure of human SMO bound to 24(S),25-epoxycholesterol and coupled to a heterotrimeric Gi protein.”]. In the same study, 24(S),25-epoxycholesterol stimulated Gi activation through SMO, supporting the GPCR activity and adenylate-cyclase-inhibiting pathway annotations rather than relying only on family classification.

Sterol binding is mechanistically integral, not an incidental ligand interaction. Human SMO structures identified cholesterol in the extracellular cysteine-rich-domain pocket [PMID:27437577 “Unexpectedly, we find a cholesterol molecule bound to Smoothened in the CRD binding site.”], and mutations predicted to disrupt this binding impaired native Hh signal transmission. Later structural work mapped connected sterol sites through the receptor and concluded that sterol movement regulates signaling [PMID:32929279 “These data indicate that sterol transport through the core of SMO is a major regulator of SMO-mediated signaling.”]. I therefore retained cholesterol and oxysterol binding and represented cholesterol binding as a distinct core molecular function.

The current evidence also establishes a second immediate effector mechanism beyond Gi. SMO's C-terminal PKI motif acts as a pseudosubstrate that occupies the PKA catalytic active site [PMID:36202993 “SMO uses a decoy substrate sequence to physically block the active site of the cAMP-dependent protein kinase (PKA) catalytic subunit (PKA-C) and extinguish its enzymatic activity.”]. Follow-up work showed that GRK2 phosphorylation enables direct active-SMO/PKA-C binding in cilia [PMID:39138140 “GRK2 phosphorylation enables active SMO to bind PKA-C directly.”]. This evidence supports PKA catalytic-subunit binding and protein sequestering activity, but the more informative molecular function is GO:0004862, “cAMP-dependent protein kinase inhibitor activity.” I added it as a proposed `NEW` annotation and made it a core function.

## Functional location and trafficking

The signaling-competent locations are the plasma membrane and non-motile primary-cilium membrane. Human RPE1-cell experiments show agonist-dependent endogenous SMO entry into cilia [PMID:22072986 “In control siRNA transfected cells, SMO localizes to the cilia in response to SMO agonist (SAG) but not in SAG-untreated cells”]. BBSome/LZTFL1 perturbations alter that trafficking, while the 2024 GRK2 study places SMO phosphorylation and PKA-C engagement in the cilium. These observations justify accepting plasma-membrane, cilium, ciliary-membrane, and non-motile-cilium-membrane annotations.

Endocytic-vesicle membrane, Golgi, ciliary tip, caveolar/raft microdomains, dendrite, and extracellular-exosome detections were retained as non-core locations. The caveolar/raft paper directly reports that both proteins occur in caveolin-enriched microdomains [PMID:11278759 “both Smoothened and Patched are in caveolin-1-enriched/raft microdomains.”], but this is a trafficking/localization context, not a defining SMO activity. The urinary and prostatic exosome terms come from high-throughput proteomics and likewise do not identify a signaling site.

## Patched relationship

Older biochemical work reported PTCH1 and PTCH2 complexes with SMO [PMID:9811851 “they can form a complex with SMO.”], so the patched-binding annotations were retained rather than rejected. They are non-core because the modern mechanism is primarily indirect: Patched regulates availability/access of activating sterols, and stable PTCH-SMO binding is not required to explain pathway control. This distinction avoids treating a historical co-complex observation as the central molecular function.

## Development and disease evidence

SMO's core biochemistry is deployed broadly in morphogen interpretation. The IBA/ISS/IEA annotations for CNS development, pattern specification, commissural axon guidance, neural-tube patterning, left-right asymmetry, heart, somite, gut, forebrain, and urinary-system morphogenesis are biologically coherent context-specific outputs and were retained as non-core rather than promoted to defining functions.

Human genetic evidence strongly supports pleiotropic developmental importance. Individuals with biallelic loss-of-function variants had brain, heart, skeletal, and enteric nervous-system anomalies, and patient-derived cells showed altered Hh signal transduction/primary-cilium pathway dynamics [PMID:32413283 “Cells derived from affected individuals showed normal ciliogenesis but severely altered Hh-signal transduction as a result of either altered PC trafficking or abnormal activation of the pathway downstream of SMO.”]. Activating SMO variants provide reciprocal evidence for pathway activation and oncogenesis [PMID:9422511 “These findings support the role of SMO as a signalling component of the SHH-receptor complex”].

The developing urinary-tract paper is expression-based rather than a perturbation study. It found SMO/PTCH patterns consistent with paracrine signaling during detrusor smooth-muscle differentiation [PMID:17850284 “The expression patterns of the SHH-transducing proteins Patched (PTCH) and Smoothened (SMO) were consistent with long-range paracrine signalling associated with detrusor smooth muscle differentiation in the urogenital sinus.”]. I retained smooth-muscle development as non-core and accepted the smoothened-pathway term because that pathway assignment is independently established by extensive direct evidence.

## Annotation triage decisions

- Broad `transmembrane signaling receptor activity`, `cell surface receptor signaling pathway`, `membrane`, and `plasma membrane bounded cell projection` annotations were modified to the experimentally established GPCR/pathway/plasma-or-ciliary terms.
- Broad tissue development, whole-organism growth, organ growth, and generic positive/negative transcription annotations were marked over-annotated because they conflate downstream GLI-dependent outcomes with SMO's direct activity.
- The liver-cancer migration and gene-expression IMP annotations were marked over-annotated. The study shows that miR-338-3p targets SMO and that SMO knockdown reverses invasion-related readouts [PMID:21671467 “small interfering RNA targeted SMO reversed the effects induced by blockade of miR-338-3p.”], but migration and generic gene-expression regulation are indirect pathway outputs.
- The generic `protein binding` annotation supported by Gas8 interaction was marked over-annotated because the physical interaction is real [PMID:21659505 “Here we demonstrate that Growth Arrest Specific 8 (Gas8), a microtubule associated subunit of the Dynein Regulatory Complex (DRC), interacts with Smo to modulate this process.”] but `protein binding` is not informative about SMO function.
- The KIF7 `protein binding` IPI and the `contact inhibition` IMP were left `UNDECIDED`. Their cached papers are abstract-only and do not expose enough assay detail to verify those exact claims. The experimental curators were not overruled.

## Remaining mechanistic questions

The major unresolved issue is how much heterotrimeric-Gi coupling versus direct PKI-motif-mediated PKA inhibition contributes to SMO-to-GLI signaling in different human tissues. A second question is which endogenous sterol occupies each SMO site in each physiological context. Separation-of-function endogenous alleles, assayed in multiple human ciliated organoid lineages with local cAMP, PKA, GLI-processing, and transcriptional readouts, would distinguish these branches without conflating them with downstream developmental phenotypes.
