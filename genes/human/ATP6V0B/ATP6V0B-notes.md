# ATP6V0B notes

## 2026-06-03 PN batch review

Falcon deep research was already present as `ATP6V0B-deep-research-falcon.md`, so
no fallback provider run was needed. I re-reviewed the existing ATP6V0B YAML in
Proteostasis PN context.

ATP6V0B is the human V-ATPase V0 proteolipid c'' subunit. The primary cloning
paper identifies hATP6F/ATP6V0B as a second human V-ATPase proteolipid and states
that it has five putative transmembrane segments and a conserved Glu98 essential
for H(+)-transporting activity [PMID:9653649 "hATP6F is a hydrophobic protein
with five putative transmembrane segments"]. The human V-ATPase structure paper
frames V-ATPase as an ATP-driven proton pump with cytoplasmic V1 ATP hydrolysis
and membrane-embedded Vo proton transfer [PMID:33065002 "V-ATPases are ATP-driven
proton pumps comprised of a cytoplasmic V1 complex for ATP hydrolysis and a
membrane-embedded Vo complex for proton transfer"].

For PN projection, ATP6V0B appears in the Autophagy-Lysosome Pathway under V0
lysosomal v-ATPase proton pump component. The projection already matches GOA for
lysosomal lumen acidification and the broader V-type ATPase V0 domain, and it has
one conservative more-specific candidate: GO:0046610 lysosomal
proton-transporting V-type ATPase, V0 domain [file:projects/PROTEOSTASIS/reports/pn_projection/pn_projected_annotations.tsv
"ATP6V0B		Autophagy-Lysosome Pathway|Pre-initiation autophagy signaling|mTORC1 pathway,
upstream|Nutrient sensing|V0 lysosomal v-ATPase proton pump component"]. I added
this as a `NEW` reviewed annotation because it is a component-level refinement,
not a new biological-process claim.

Conservative decisions:

- Accepted the V-ATPase component, proton transport, and organelle acidification
  annotations as core or directly supportive of core function.
- Modified broad `monoatomic ion transport` to `proton transmembrane transport`.
- Modified generic `proton transmembrane transporter activity` to the more
  specific complex-level rotary V-ATPase activity, while describing ATP6V0B as a
  contributor to the complex rather than an independent ATPase.
- Removed generic `protein binding` annotations from the GLP-1R and HuRI
  interaction screens because they do not describe ATP6V0B mechanism.
- Marked `regulation of macroautophagy` as over-annotation. ATP6V0B supports
  autophagic flux through lysosomal acidification, but the cited paper does not
  show a specific ATP6V0B regulatory role [PMID:22982048 "macroautophagy is
  responsible for the uptake of lipofuscin into the lysosomes"].
