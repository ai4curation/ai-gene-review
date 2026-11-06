# PSEPK fliJ

## 2026-11-06 export-panel review

Identity: Q88ET8, Pseudomonas putida KT2440. Frozen local UniProt provides the accession/locus and the independent classification `DR   NCBIfam; TIGR02473; flagell_FliJ; 1.`. No direct KT2440 assay is substituted for a Salmonella experiment.

FliJ is the soluble central-stalk component of the flagellar export ATPase apparatus. It promotes FliI ring formation and connects ATPase assembly to activation of FlhA-dependent protein export.

Primary PMID21934659 (https://doi.org/10.1038/ncomms1488) examines Salmonella wild-type and FliHI bypass backgrounds: FliJ–FlhA interaction activates efficient export. PMID29946050 (https://doi.org/10.1128/mBio.00988-18) uses Salmonella inverted membrane vesicles, FlhB(N269A) rod/hook-locked preparations and separate wild-type-FlhB hook-length experiments. Added FliHI plus FliJ improves transport; ΔFoF1 vesicles with MgATP still export without bulk PMF. The hydrolysis-defective FliI(E211Q) control loses that activity. Neither result converts FliI into an ATP synthase. The earlier PMID18216858/18216859 bypass observations show ATPase dispensability under particular conditions, not the irrelevance of ATPase-assisted export. Exact native stoichiometry and energetics in KT2440 remain inferred.

GO audit: current QuickGO snapshots in the ignored export-panel cache verify that 0008564 does not descend from 0016887, and 0120102 does not descend from 0030257; preserve those distinct claims. Membrane→plasma membrane and flagellum/basal body→secretion apparatus are genuine refinements. Non-catalytic subunits receive process/location cores rather than invented autonomous ATPase or generic chaperone functions. Motility/chemotaxis consequences of failed export are distinguished from doing the motion/signaling work.

NEW0030254: the protein performs carrier/docking/activation work, rather than serving as a substrate. Same-role E. coli FliH/P31068 and FliJ/P52613 carry this process; Salmonella counterparts lack it. Thus the proposal rests on direct primary mechanism plus target classification, not a claim that annotation absence proves oversight. Current rows do not already entail the new process.

Research provenance: the bare deep-research recipe requires an explicit provider. The subsequent real `--provider falcon` request failed with authentication HTTP403; no provider report was created or synthesized. This manual review uses the cited primary caches and target classification.

Adjudication check: existing GO0071973 motility claims are retained as non-core broad functional participation because same-role FliH/FliJ comparators consistently carry them. Lack of torque production alone is not a sufficient negative argument. Chemotaxis GO0006935 remains UNDECIDED: its definition includes directed locomotion, not only signal transduction, and the available sources do not settle the intended breadth for export factors.

## 2026-11-06 — PR6138 evidence follow-up

Reassessed chemotaxis as over-annotation: export/assembly evidence identifies FliJ molecular work but does not establish guided-movement participation. This differs from the ongoing torque supplied by stators during the response.
