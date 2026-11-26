# PSEPK fliR

## 2026-11-06 export-panel review

Identity: Q88EV0, Pseudomonas putida KT2440. Frozen local UniProt provides the accession/locus and the independent classification `DR   NCBIfam; TIGR01400; fliR; 1.`. No direct KT2440 assay is substituted for a Salmonella experiment.

FliR supplies a distinct structural subunit of the FliPQR polypeptide channel, participating in gating and the interface with the proximal flagellar rod.

Primary PMID21934659 (https://doi.org/10.1038/ncomms1488) examines Salmonella wild-type and FliHI bypass backgrounds: FliJ–FlhA interaction activates efficient export. PMID29946050 (https://doi.org/10.1128/mBio.00988-18) uses Salmonella inverted membrane vesicles, FlhB(N269A) rod/hook-locked preparations and separate wild-type-FlhB hook-length experiments. Added FliHI plus FliJ improves transport; ΔFoF1 vesicles with MgATP still export without bulk PMF. The hydrolysis-defective FliI(E211Q) control loses that activity. Neither result converts FliI into an ATP synthase. The earlier PMID18216858/18216859 bypass observations show ATPase dispensability under particular conditions, not the irrelevance of ATPase-assisted export. Exact native stoichiometry and energetics in KT2440 remain inferred.

GO audit: current QuickGO snapshots in the ignored export-panel cache verify that 0008564 does not descend from 0016887, and 0120102 does not descend from 0030257; preserve those distinct claims. Membrane→plasma membrane and flagellum/basal body→secretion apparatus are genuine refinements. Non-catalytic subunits receive process/location cores rather than invented autonomous ATPase or generic chaperone functions. Motility/chemotaxis consequences of failed export are distinguished from doing the motion/signaling work.

Research provenance: the bare deep-research recipe requires an explicit provider. The subsequent real `--provider falcon` request failed with authentication HTTP403; no provider report was created or synthesized. This manual review uses the cited primary caches and target classification.

Additional primary grounding: PMID29967543 (https://doi.org/10.1038/s41594-018-0086-9) resolves Salmonella FliPQR at 4.2 Å and shows noncanonical membrane topologies; plasma-membrane localization does not mean a conventional membrane-spanning arrangement for each folded subunit. PMID40833400 (https://doi.org/10.1073/pnas.2507221122) uses Salmonella SJW1368 expression of FliP/Q and C-terminal His-tagged FliR in peptidiscs, with cryo-EM and mutational tests. The FliP/FliR cap templates FliE assembly; these strain-specific constructs are not represented as KT2440 assays.
