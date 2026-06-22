# ATP6AP2 notes

## Research workflow

- Ran `just fetch-gene human ATP6AP2`, which seeded the UniProt record, GOA file, cached publications, and review YAML.
- Falcon deep research has now completed successfully (`ATP6AP2-deep-research-falcon.md`, 21 citations); see the synthesis section at the end of this file. The original PN-batch attempt timed out before the `deep_research_unified` tool bugs were fixed.
- Used cached UniProt, GOA, publications, and the PN projection artifacts for this review.

## Curation synthesis

- ATP6AP2 is best treated as a V-ATPase accessory/regulatory protein rather than as a canonical chaperone or protease. UniProt summarizes it as "involved in the assembly of the lysosomal proton-transporting V-type ATPase (V-ATPase) and the acidification of the endo-lysosomal system" [file:human/ATP6AP2/ATP6AP2-uniprot.txt].
- The strongest primary evidence comes from ATP6AP2 disease and perturbation studies: missense mutations impair interaction with ATP6AP1 and V-ATPase assembly, with downstream defects in glycosylation and autophagy [PMID:29127204 "Our results suggest that ATP6AP2 has a crucial role in V-ATPase assembly, both in invertebrates and vertebrates."].
- The neuronal disease paper supports the PN proteostasis angle because ATP6AP2 deficiency caused "severe deficiency in lysosomal acidification and protein degradation" and decreased V-ATPase membrane assembly [PMID:30985297 "severe deficiency in lysosomal acidification and protein degradation leading to neuronal cell death"].
- The EV-A71/autophagy paper provides direct knockdown support for lysosomal pH control: ATP6AP2 was described as an auxiliary V-ATPase component, and ATP6AP2 knockdown significantly increased lysosomal pH [PMID:32276428 "ATP6AP2 is an important auxiliary component of the V-ATPase complex and coordinates correct V-ATPase assembly"].
- The PN projection proposes ATP6AP2 to `GO:0060590 ATPase regulator activity` from lysosomal V-ATPase regulator leaves and already recognizes `GO:0007042 lysosomal lumen acidification` as present in GOA [file:projects/PROTEOSTASIS/reports/pn_projection/pn_projected_annotations.tsv].

## PN decision

- Accept ATP6AP2 for the Proteostasis PN batch only through the Autophagy-Lysosome Pathway / lysosomal acidification / V-ATPase regulator branch.
- Add `GO:0060590 ATPase regulator activity` conservatively: ATP6AP2 is not the proton-pumping catalytic subunit, but multiple lines of evidence support an accessory/regulatory role in V-ATPase assembly and lysosomal acidification.
- Add `GO:0070072 vacuolar proton-transporting V-type ATPase complex assembly` because the primary literature explicitly supports assembly-factor biology.
- Keep Wnt signaling, CNS development, angiotensin maturation, MAPK signaling, TGF-beta production, plasma membrane/external side, and high-throughput exosome/granule localizations as non-core or over-broad where appropriate. These are real or plausible contexts but should not be used to broaden the PN proteostasis projection.

## Falcon deep research synthesis (2026-06-21)

The Falcon report (`file:human/ATP6AP2/ATP6AP2-deep-research-falcon.md`) reinforces
the PN decision above (V-ATPase accessory/assembly is the proteostasis-relevant
core; RAS/Wnt/MAPK are non-core elaborations) and adds three useful points.

**Evolutionary argument that the V-ATPase function is ancestral/primary.**
ATP6AP2 is conserved from yeast to human, and homologs that **lack renin-binding
function exist in organisms with no renin-angiotensin system**, indicating the
V-ATPase accessory role is the fundamental, conserved function and the
(pro)renin-receptor/RAS role is a vertebrate-specific elaboration
(falace2024vatpasedysfunctionin; figueiredo2021). This is a strong independent
justification for treating the V-ATPase-assembly / lysosomal-acidification
branch as core and the RAS/angiotensin annotations as non-core.

**Proteolytic processing nuance (relevant to which "form" does what).** In the
trans-Golgi, ATP6AP2 is cleaved by furin / site-1 protease (S1P) / ADAM19 into a
~28-kDa **soluble (pro)renin receptor (sPRR)** and a truncated membrane fragment
**M8.9** that remains associated with V-ATPase. Reviews describe M8.9 as the
V-ATPase-associated portion — i.e. the proteostasis-relevant activity is carried
by the membrane-retained fragment, while the soluble ectodomain participates in
RAS signaling (kourieh2025overviewofrenin). Worth noting when interpreting
isoform/fragment-specific annotations.

**Structural placement (Abbas 2020; Wang 2020).** Cryo-EM of mammalian/human
V-ATPase places the ATP6AP2/PRR transmembrane anchor inside the V0 c-ring
alongside the cleaved ATP6AP1/Ac45 anchor (enzyme ATP:H+ ratio 3:10), confirming
ATP6AP2 as a structural/assembly contributor to the membrane sector rather than a
catalytic subunit — consistent with the `GO:0070072` V-ATPase-assembly and
`GO:0060590` ATPase-regulator calls already made.

**Other corroborated (non-core) roles:** trafficking/stabilization of
LRP6/β-catenin and N-cadherin/β-catenin at the membrane (Wnt; xiong2024),
megalin/cubilin receptor-mediated endocytosis in renal proximal tubule
(figueiredo2021), and tissue-specific KO phenotypes (osteoblast bone formation,
placental trophoblast invasion, endothelial tip-cell polarity/angiogenesis). No
change to the core call.
