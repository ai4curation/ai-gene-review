# RGS4: signaling-regulator evidence review

All original annotation payloads, evidence codes, references and qualifiers were preserved. No new annotations were manufactured to populate a module. Actual Falcon and fallback research attempts failed authentication/quota; this is manual literature research, not provider-generated prose.

The whole record was reviewed, including secondary physiology and localization. Existing assertion specificity is judged independently of evidence code. Native, heterologous, mutant and orthology-based results are distinguished below.

## GO:0001965 G-protein alpha-subunit binding — ACCEPT
Purified RGS4 accelerates Gi-family GTP hydrolysis, and the RGS4–Gi1 transition-state structure directly identifies the G alpha-binding interface. These are integral molecular functions, not peripheral binding annotations.
Sources: PMID:8756726, PMID:9108480

## GO:0005096 GTPase activator activity — ACCEPT
Purified RGS4 accelerates Gi-family GTP hydrolysis, and the RGS4–Gi1 transition-state structure directly identifies the G alpha-binding interface. These are integral molecular functions, not peripheral binding annotations.
Sources: PMID:8756726, PMID:9108480

## GO:0003924 GTPase activity — MODIFY
RGS4 stabilizes the transition state of G alpha-mediated GTP hydrolysis; it is a GAP, not itself the guanine-nucleotide-binding GTPase. Refine to its already represented GAP activity.
Sources: PMID:8756726, PMID:9108480

## GO:0005516 calmodulin binding — ACCEPT
PMID10747990 explicitly demonstrates calcium-dependent calmodulin binding to RGS4, including a complex with activated Gi1, and reversal of PIP3-mediated GAP inhibition. Retain this regulatory ligand-binding function.
Sources: PMID:10747990

## GO:0005634 nucleus — KEEP_AS_NON_CORE
Nuclear RGS4 is condition-dependent: PMID10791963 reports nuclear accumulation after inhibition of export or alteration of its export determinants. Predominantly cytoplasmic steady-state localization does not negate that observed pool.
Sources: PMID:10791963

## GO:0005737 cytoplasm — ACCEPT
RGS4 has a cytoplasmic signaling-regulator pool, directly supported by the localization experiments. Its regulated nuclear shuttling and membrane recruitment do not make cytoplasmic localization incorrect.
Sources: PMID:10791963

## GO:0005886 plasma membrane — MODIFY
RGS4 acts on membrane-associated G alpha from the cytoplasmic face. Refine the broad plasma-membrane annotation to the separately retained cytoplasmic-side term rather than imply a transmembrane topology.
Sources: PMID:9108480

## GO:0009898 cytoplasmic side of plasma membrane — ACCEPT
The RGS4 GAP mechanism directly terminates receptor-activated Gi/o and Gq signaling at the intracellular membrane surface. Purified-protein and receptor-current experiments support this core function; it need not be the dominant regulator of every native receptor.
Sources: PMID:8756726, PMID:24421355

## GO:0007186 G protein-coupled receptor signaling pathway — ACCEPT
The RGS4 GAP mechanism directly terminates receptor-activated Gi/o and Gq signaling at the intracellular membrane surface. Purified-protein and receptor-current experiments support this core function; it need not be the dominant regulator of every native receptor.
Sources: PMID:8756726, PMID:24421355

## GO:0045744 negative regulation of G protein-coupled receptor signaling pathway — ACCEPT
The RGS4 GAP mechanism directly terminates receptor-activated Gi/o and Gq signaling at the intracellular membrane surface. Purified-protein and receptor-current experiments support this core function; it need not be the dominant regulator of every native receptor.
Sources: PMID:8756726, PMID:24421355

## GO:0008277 regulation of G protein-coupled receptor signaling pathway — MODIFY
The established RGS4 role is negative regulation through accelerated G alpha inactivation. Refine to the existing negative-regulation term.
Sources: PMID:8756726, PMID:24421355

## GO:0010460 positive regulation of heart rate — KEEP_AS_NON_CORE
The RGS4-selective inhibitor study potentiated muscarinic bradycardia, supporting an RGS4-dependent restraint of the heart-rate-lowering response. Retain this conditional positive heart-rate regulation; it does not imply that RGS4 replaces the predominant native RGS6–GNB5 cardiac mechanism.
Sources: PMID:25844489, PMID:24318880

## GO:0019901 protein kinase binding — UNDECIDED
The traced rat study PMID17084383 shows co-immunoprecipitation of RGS4 in a CASK-associated signaling complex. That supports association with a kinase-containing assembly but the accessible text does not establish a direct binary kinase-binding interaction. The precise binding claim remains unresolved pending target-level interaction mapping.
Sources: PMID:17084383

## GO:0032991 protein-containing complex — ACCEPT
The experimentally resolved RGS4–Gi1–MgGDP–AlF4 assembly establishes physical complex formation. Its transition-state nature does not warrant guessing membership in a constitutive receptor complex; the broad complex term is retained at the demonstrated level.
Sources: PMID:9108480

## GO:0001975 response to amphetamine — KEEP_AS_NON_CORE
Rat RGS4 expression in VTA and nucleus accumbens correlates with amphetamine intake in PMID26321241. Retain the bounded stimulus-response inference without converting correlation into causal drug-seeking behavior.
Sources: PMID:26321241

## GO:0042220 response to cocaine — KEEP_AS_NON_CORE
Chronic cocaine and subsequent abstinence reduce rat RGS4 transcript levels, with restoration after context re-exposure. This supports a contextual response annotation, not a primary cocaine-processing function.
Sources: PMID:17632279

## GO:0045471 response to ethanol — KEEP_AS_NON_CORE
Rat prefrontal RGS4 mRNA and protein rise after chronic intermittent ethanol and withdrawal. The transferred response term is retained with that experimental scope.
Sources: PMID:28736108

## GO:0051924 regulation of calcium ion transport — KEEP_AS_NON_CORE
In dopamine-depleted striatal cholinergic interneurons, increased RGS4 attenuates M4 autoreceptor control of calcium channels. This is regulation of calcium transport through receptor signaling, not direct calcium-channel pore activity.
Sources: PMID:16699510

## GO:0060160 negative regulation of dopamine receptor signaling pathway — KEEP_AS_NON_CORE
RGS4 coexpression inhibits D2/D3 receptor signaling through its N-terminal interaction region in HEK293 assays. Retain this receptor-selective regulatory function without asserting equal activity toward all dopamine receptors; D4 was unaffected in a separate cortical experiment.
Sources: PMID:21896332, PMID:17220354

## GO:0061052 negative regulation of cell growth involved in cardiac muscle cell development — KEEP_AS_NON_CORE
RGS4 expression in cultured cardiomyocytes blocks agonist-driven growth and myofilament organization; a GAP-defective mutant fails to block the transcriptional response. These are contextual downstream consequences of its active signaling-regulator role, not intrinsic actin-remodeling catalysis.
Sources: PMID:9918533

## GO:0110053 regulation of actin filament organization — KEEP_AS_NON_CORE
RGS4 expression in cultured cardiomyocytes blocks agonist-driven growth and myofilament organization; a GAP-defective mutant fails to block the transcriptional response. These are contextual downstream consequences of its active signaling-regulator role, not intrinsic actin-remodeling catalysis.
Sources: PMID:9918533

## GO:1900924 negative regulation of glycine import across plasma membrane — UNDECIDED
The donor study PMID21798518 reports modulation of glycine-evoked patch-clamp currents, while GO:1900924 requires reduced glycine import into the cell. Glycine-receptor current and amino-acid uptake are distinct endpoints. Full target-level results and independent uptake measurements were not recovered, so the transferred uptake claim remains unresolved rather than accepted from the current assay.
Sources: PMID:21798518

## GO:1901379 regulation of potassium ion transmembrane transport — MODIFY
RGS4 regulates M2-gated potassium currents, and PMID24421355 specifically demonstrates inhibitory control of pilocarpine-mediated currents. Refine the unsigned transport-regulation term to the already asserted negative term; the older developmental-expression source alone is not a channel assay.
Sources: PMID:24421355, PMID:11906535

## GO:1901380 negative regulation of potassium ion transmembrane transport — KEEP_AS_NON_CORE
Rat atrial and Xenopus reconstitution experiments demonstrate RGS4-dependent suppression of M2–G protein activation of inwardly rectifying potassium currents, especially for the partial agonist pilocarpine. Retain this conditional channel-regulatory role.
Sources: PMID:24421355

## GO:1990791 dorsal root ganglion development — MARK_AS_OVER_ANNOTATED
The traced rat source PMID14550772 establishes adult sensory-neuron expression, regulation by GDNF and injury-induced downregulation. Those observations do not establish that RGS4 executes dorsal-root-ganglion development. The developmental transfer exceeds the source endpoint; an undiscovered developmental role is not excluded.
Sources: PMID:14550772

## GO:2000463 positive regulation of excitatory postsynaptic potential — KEEP_AS_NON_CORE
RGS4 attenuates 5-HT1A-dependent suppression of NMDA receptor current in rat prefrontal pyramidal neurons. This disinhibitory mechanism supports increased excitatory postsynaptic responses in that context, without making RGS4 an excitatory receptor or universal positive synaptic regulator.
Sources: PMID:17220354

## Research and access
Normal publication fetches and targeted refreshes are logged under `.cache/module-audit-logs/acetylcholine-*`. Canonical abstract-only caches were not manually rewritten. Full publisher recovery for cone localization is cited separately. PAINT assertions are treated as ancestral-node judgments, not pairwise transfers; target appearance among descendant evidence is not circular.

## Validation
Focused strict/schema, source/quote and ontology checks, record-section backfill, rendering and helper-generated history are recorded in the final panel proof.

## Final source and propagation audit

Original machine payloads and all qualifiers were compared with the authoritative baseline. There are no NOT assertions or new annotation rows in this 15-target panel. Full sources were inspected where a source-specific sign/mechanism challenge required them; unresolved fine-localization/source claims are retained as UNDECIDED rather than inferred absent. Bare binding removals apply the project policy and do not dispute experimental interactions.

UniProt/PANTHER placement inspected: `PTHR10845:SF184`. Broad G-alpha family PTHR10218 is GTP-BINDING PROTEIN ALPHA SUBUNIT; GRK PTHR24355 is G PROTEIN-COUPLED RECEPTOR KINASE/RIBOSOMAL PROTEIN S6 KINASE. Surprising official family names were not mechanically repointed. RGS6 current PTHR45746 placement does not invalidate a historical PAINT PTHR10845 assertion by itself.
