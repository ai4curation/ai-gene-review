# exsA (PA1713, P26993) review notes

AraC/XylS-family master activator of the P. aeruginosa type III secretion system.
Purified ExsA binds T3SS promoters [PMID:18373522 "ExsA(His) specifically bound T3SS promoters with high affinity as determined by electrophoretic mobility shift assays (EMSA)."] and its C-terminal domain activates transcription [PMID:19376850 "we show that the CTD of ExsA binds to ExsA-dependent promoters in vitro and activates transcription from ExsA-dependent promoters both in vitro and in vivo"]. It is held inactive by ExsD [PMID:20008065 "find that the ExsD.ExsA complex lacks DNA binding activity"]. ExsA is required for (activates) the pathway [PMID:1655713 "The ExsA gene product appeared to be required for induction of exoenzyme S synthesis above a low basal level."].

## PseudoCAP IBA-seed assessment

Other seeds from .cache/paint/IBD.gaf, 2026-11-05.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002457187 | GO:0006355 regulation of DNA-templated transcription | 10 | 166 (24 taxa) | GO:0006355, IDA PMID:7635828 (PseudoCAP) | SOUND | Purified ExsA binds its promoters and activates transcription. Term correct, under-specific for ExsA (GO:2000144 is supported). Generic regulation suits the broad AraC/XylS clade. | E. coli AraC (P0A9E0), MelR, RhaS, ChbR, AdiY, GadW, YdeO, AppY, RclR; Yersinia LcrF (P28808) - all with experimental annotations | Yes |

Node term is generic transcriptional regulation and suits a 24-taxon AraC clade. No
PSEUDOCAP or GO_CENTRAL defect on the GO:0006355 seed; the leaf row is marked
TOO_GENERAL because GO:2000144 (CACAO IDA) entails it.

Other rows:
- GO:0050709 negative regulation of protein secretion IMP (PMID:1655713): WRONG term for
  a transcriptional activator. ExsA regulates transcription of the secretion genes, not
  secretion; and the sign is inverted (ExsA activates). REMOVE + PSEUDOCAP WRONG_TERM
  (PROBABLE; 1655713 full text not read).
- GO:0005515 protein binding IPI (ExsD, PMID:20008065): REMOVE per protein-binding policy;
  the ExsA-ExsD anti-activation is the informative content.
- GO:0003700, GO:0043565: TOO_GENERAL (entailed by GO:0001216 and GO:0000976).
