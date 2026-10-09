# HtrA2 (Omi; Q9VFJ3) notes

## Identity
- HtrA-family mitochondrial serine protease (trypsin-like protease domain + PDZ), fly orthologue of HTRA2/Omi (PARK13).

## Literature journal
- Mitochondrial; translocates on apoptotic stimuli; cleaves DIAP1 [PMID:17397804 "DmHtrA2 specifically cleaves Drosophila inhibitor-of-apoptosis protein 1 (DIAP1), a cellular caspase inhibitor, and induces cell death both in vitro and in vivo"]; stays near mitochondria [PMID:17397804 "the extramitochondrial DmHtrA2 does not diffuse throughout the cytosol but stays near the mitochondria"].
- IMS protein with IAP-binding motifs; released to cytosol; degrades DIAP1 [PMID:17557079 "a developmentally regulated mitochondrial intermembrane space protein that undergoes processive cleavage, in situ, to generate two distinct inhibitor of apoptosis (IAP) binding motifs"; "dOmi alleviates DIAP1 inhibition of all caspases by proteolytically degrading DIAP1"].
- DIAP1 binds both mature isoforms and ubiquitinates dOmi [PMID:18259196 "DIAP1 was able to bind to both isoforms via its BIR1 and BIR2 domains"; "The binding of DIAP1 to dOmi also resulted in DIAP1-mediated polyubiquitination of dOmi"].
- Rhomboid-7 cleaves Omi precursor; Omi acts downstream of Pink1 (overexpression assays) [PMID:19048081 "it acts genetically downstream of pink1 but functions independently of Parkin"].
- Loss of function: dispensable for apoptosis [PMID:19282869 "we find HtrA2 appears to be dispensable for developmental or stress-induced apoptosis"]; mitochondrial integrity role debated - null mutants lack mitochondrial morphology defects [PMID:19118185 "Omi/HtrA2 null mutants in Drosophila, in contrast to pink1 or parkin null mutants, do not show mitochondrial morphological defects"].
- Germ cell death in testis, catalytic not IAP-antagonist [PMID:23523076 "as an important mediator of GCD, acting mainly through its catalytic activity rather than by antagonizing inhibitor of apoptosis proteins"]. This GCD is spontaneous elimination of male germ cells in the testis, not death of ectopic/migratory germ cells.
- ABPP serine hydrolase atlas detected HtrA2 activity [PMID:33827210].
- Deep research (falcon) failed on the first attempt (OOM / fallback provider unavailable); retried.

## Curation thoughts
- Core: IMS serine endopeptidase; on release, IAP antagonist by binding/cleaving DIAP1 (shown mostly by overexpression); physiologically required for spermatogonial germ cell death.
- "ectopic germ cell programmed cell death" does not match the paper (spontaneous testis GCD) -> MODIFY to programmed cell death.
- No GO MF term exists for IAP binding; DIAP1-binding protein-binding rows kept as non-core.

## Deep research (falcon) additions
- Retry produced HtrA2-deep-research-falcon.md. It agrees on serine endopeptidase activity with DIAP1 as a direct substrate ["DIAP1 is a directly demonstrated fly substrate."], cleavage between DIAP1 Ile165/Gly166, catalytic Ser266 required, and the catalytic (not IAP-antagonist) role in spermatogonial germ cell death.
