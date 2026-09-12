# AFG3L2 notes

## 2026-06-03 Proteostasis PN review

Falcon deep research completed for human AFG3L2/Q9Y4W6 and was used as a synthesis check against the cached GOA-linked literature. The report consistently identifies AFG3L2 as the human mitochondrial inner membrane m-AAA protease subunit, not a soluble matrix protease.

### Literature synthesis

AFG3L2 is an m-AAA protease subunit anchored in the mitochondrial inner membrane, with the catalytic AAA+ ATPase and zinc metalloprotease modules exposed toward the matrix side. The topology point is important for PN projection: the protein acts on matrix-facing substrates but is itself an inner membrane protein [PMID:31327635 "m- and i-AAA proteases, which are tethered to the mitochondrial inner membrane (IM), but expose their enzymatic domains to the matrix and intermembrane spaces (IMS), respectively"]. Older biochemical work also recovered paraplegin and AFG3L2 in the membrane fraction [PMID:14623864 "Paraplegin and AFG3L2 were recovered from the membrane fraction, indicating that both are integral proteins of the mitochondrial inner membrane"].

The core activity is ATP-dependent substrate unfolding/translocation coupled to metalloprotease cleavage. Structural work reports that AFG3L2 has features required for "ATP-dependent translocation to unfold and degrade targeted proteins" [PMID:31327635 "ATP-dependent translocation to unfold and degrade targeted proteins"], and biochemical work describes human AFG3L2 as an "ATP-fueled degradation" protease at the matrix face of the inner membrane [PMID:29932645 "Human AFG3L2 is a compartmental AAA+ protease that performs ATP-fueled degradation at the matrix face of the inner mitochondrial membrane."]. ATP hydrolysis is a real catalytic activity, not just a binding annotation [PMID:19748354 "we demonstrate coordinated ATP hydrolysis within m-AAA protease ring complexes"].

The biological process center is mitochondrial substrate degradation and processing. AFG3L2 is required for mitochondrial protein quality control of newly synthesized or misassembled inner-membrane proteins [PMID:26504172 "The mitochondrial m-AAA protease subunit AFG3L2 is critical to this surveillance mechanism"] and resolves MT-ATP6 insertion defects [PMID:34718584 "defects in the OXA1L-mediated insertion of MT-ATP6 nascent chains into the mitochondrial inner membrane are rapidly resolved by the AFG3L2 protease complex"]. It also processes selected substrates such as MRPL32 [PMID:29932645 "conserved residues within the presequence of the mitochondrial ribosomal protein, MrpL32, target the subunit to the protease for processing into a mature form"].

Several substrate-specific consequences are well supported but should be treated as non-core relative to the m-AAA protease function. AFG3L2/SPG7 degrade unassembled EMRE/SMDT1 to regulate MCU complex assembly and calcium import [PMID:27642048 "the m-AAA protease degrades non-assembled EMRE and ensures efficient assembly of gatekeeper subunits with MCU"; PMID:28396416 "mitochondrial mAAA proteases AFG3L2 and SPG7 rapidly degrade unassembled EMRE using the energy of ATP hydrolysis"]. AFG3L2 also degrades SLC25A39 in a glutathione-sensitive feedback circuit [PMID:37917749 "Under physiological conditions, SLC25A39 is rapidly degraded by mitochondrial protease AFG3L2."; PMID:38157846 "mitochondrial m-AAA protease AFG3L2 is responsible for degrading SLC25A39 through the matrix loop 1"].

### PN projection evaluation

The PN projection proposed two AFG3L2 candidate additions from `Mitochondrial proteostasis|Organelle-specific protein degradation|Matrix protease`:

- `GO:0035694 mitochondrial protein catabolic process`
- `GO:0005759 mitochondrial matrix`

I accepted `GO:0035694 mitochondrial protein catabolic process` as a conservative `NEW` annotation. Existing GOA already has generic `GO:0030163 protein catabolic process` and generic `GO:0006508 proteolysis`; the literature supports a mitochondrial-specific degradation process, and the PN report itself states that "GO mitochondrial protein catabolic process is the conservative shared target."

I did not add `GO:0005759 mitochondrial matrix`. The PN class label "Matrix protease" reflects the side of the inner membrane where the catalytic domains face and where many substrates are exposed. It does not override the stronger cellular component evidence that AFG3L2 is an integral mitochondrial inner membrane protein. The safer cellular component remains `GO:0005743 mitochondrial inner membrane`, including `is_active_in` when available.

### Annotation strategy

Generic proteolysis and protein catabolic process annotations were marked for replacement by `GO:0035694 mitochondrial protein catabolic process`. Broad membrane or mitochondrion cellular component annotations were marked for replacement by `GO:0005743 mitochondrial inner membrane`.

The `protein binding` IPI rows were treated as over-annotations. The reported interactions are real, but the generic MF term does not communicate AFG3L2 function. Where appropriate, the informative biology is captured by `m-AAA complex`, substrate degradation, mitochondrial calcium import regulation, glutathione-response biology, or mitochondrial protein quality control.
