# Aldh1l1 notes

- UniProtKB:P28037 states: FUNCTION: Cytosolic 10-formyltetrahydrofolate dehydrogenase catalyzes the NADP(+)-dependent conversion of 10-formyltetrahydrofolate to tetrahydrofolate and carbon dioxide. [UniProtKB:P28037].
- Core interpretation: cytosolic 10-formyltetrahydrofolate oxidation to tetrahydrofolate, CO2, and NADPH.
- Accepted direct GO terms include: 10-formyltetrahydrofolate catabolic process, NADPH regeneration, aldehyde dehydrogenase (NADP+) activity, folic acid metabolic process, formyltetrahydrofolate dehydrogenase activity, tetrahydrofolate biosynthetic process, tetrahydrofolate interconversion.
- Non-core/context terms are mostly localization, binding/cofactor, inferred pathway context, or exposure-response annotations; generic parent terms are modified when a specific catalytic term is available.


## Evidence re-review, 2026-09-20

Reviewed all 35 rows and the seven cited primary studies, available abstract coverage, UniProt and PTHR11699 PAINT assertions. NADP-dependent FDH/aldehyde oxidation is supported; NADP preference alone does not establish zero NAD+ turnover. The GO:0004029 ancestor PTN000192666 includes mouse Aldh1l1, so a generic wrong-paralog accusation is inadequate. NAD+-specific rows are UNDECIDED pending direct cofactor comparisons. The mitochondrial ancestor PTN008524390 uses ALDH1L2 evidence; principal cytosolic localization does not by itself exclude a secondary pool, so this localization also awaits focused adjudication. Restored broad NAD(P)+ terms because they permit NADP+, and made the principal cytosolic location core. PMID:17669278 reports an FDH/CPS1/BHMT complex isolated by SBTI affinity chromatography, not merely the FDH homotetramer; supporting text and reasons now reflect that experiment. Removed project-specific review commentary from the gene description.


### Independent report incorporated, 2026-09-20

Read the full cofactor/localization OpenScientist output and its sequence CSV. Its NAD+ headline exceeds its own limitation: "no NAD⁺ kinetics given (absence of evidence, not a formal negative)". The NAD+-specific rows therefore remain UNDECIDED after report incorporation. The N-terminal targeting comparison is stronger: the cached rat sequence starts MKIAVIGQSL, while primary [PMID:20498374](https://pubmed.ncbi.nlm.nih.gov/20498374/) demonstrates the additional ALDH1L2 targeting leader and mitochondrial fusion localization. This paralog-specific targeting distinction supports restoring REMOVE for the broad mitochondrial IBA, with rare noncanonical pools not formally excluded. The report's apparent 27-residue extension counts the five shared pre-anchor ALDH1L1 residues; the primary-paper comparison calls the additional segment 22 residues. NADP-dependent free-aldehyde oxidation is retained as a real non-core capability. No NAD+-absence claim or generic-ALDH ISO misidentification was adopted from the report.

## Re-review 2026-10-10

- GOA refresh added four rows: GO:0005829 cytosol ISO, GO:0009258 10-formyltetrahydrofolate catabolic process ISO, and GO:0016155 formyltetrahydrofolate dehydrogenase activity ISO (all donor-splits from human ALDH1L1, UniProtKB:O75891), plus GO:0009258 IBA from PANTHER:PTN008524390 (donors mouse Aldh1l1 MGI:1340024, mouse Aldh1l2 MGI:2444680, rat Aldh1l1 RGD:621294, human ALDH1L1 O75891, human ALDH1L2 Q3SY69). All ACCEPT [UniProtKB:P28037 "Cytosolic 10-formyltetrahydrofolate dehydrogenase that catalyzes the NADP(+)-dependent conversion of 10-formyltetrahydrofolate to tetrahydrofolate and carbon dioxide"; UniProtKB:P28037 "SUBCELLULAR LOCATION: Cytoplasm, cytosol"]. The IBA for the catabolic process is shared by both paralogs, unlike the mitochondrion IBA from the same node, which the 2026-09-21 re-review removed on targeting-divergence grounds; that judgment is unchanged.
- Retired by GOA: GO:0006081 aldehyde metabolic process IBA and GO:0006740 NADPH regeneration IBA. Both already carried SOURCE_STALE_OR_MISSING propagation reviews noting no current IBD; added a sentence that GOA has now withdrawn them. Actions unchanged.
- UniProt rewrote the FUNCTION text ("dehydrogenase catalyzes" -> "dehydrogenase that catalyzes", with appended PubMed citations); replaced 17 stale quotes with the current wording. Checker: 0 stale.
- No other actions changed; the 2026-09-21 codex judgments (NAD+-activity rows UNDECIDED, mitochondrion IBA REMOVE, aldehyde dehydrogenase rows non-core) were preserved, since no new evidence bears on them.
