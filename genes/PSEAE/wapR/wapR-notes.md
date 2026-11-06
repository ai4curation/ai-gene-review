# wapR (PA5000, Q9HUG5) notes

## Literature (own research, 2026-11-05)

- [PMID:18178733 "The capped core of the wapR mutant was found to be truncated and lacked alpha-1,3-L-Rha."]; the alpha-1,3-L-Rha is where O antigen caps the core [PMID:18178733 "one form is capped with O antigen through an alpha-1,3-linked L-rhamnose (L-Rha)"]; hence [PMID:18178733 "The wapR mutant produced LPS lacking O antigen, and addition of wapR in trans complemented this defect."].
- [PMID:22685285 "preferential expression of migA and wapR correlated with the levels of uncapped and O polysaccharide-capped core, respectively"].
- All cached papers abstract-only; full text not retrievable this session.
- O antigen biosynthetic process (IMP) is a downstream effect of the missing acceptor: REMOVE, PSEUDOCAP WRONG_TERM PROBABLE.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000531320 | GO:0016757 glycosyltransferase activity | 7 | 44 (17 taxa) | GO:0016757, IDA, PMID:18178733 | SOUND | Specific loss of alpha-1,3-L-Rha in the mutant; evidence is mutant structure, not an enzyme assay. | RfbV, WcaA, Rv2957, SunS, PA1014 (all IDA), MigA | Yes |
| PTN000531351 | GO:0009244 lipopolysaccharide core region biosynthetic process | 2 | 18 (10 taxa) | GO:0009244, IMP, PMID:18178733 | SOUND | Mutant LPS structure lacks the sugar WapR adds. | MigA Q9I5M1 only | Yes, on MigA alone; but node term does not suit the clade |
| PTN000531351 | GO:0009244 lipopolysaccharide core region biosynthetic process | 2 | 18 (10 taxa) | GO:0009244, IDA, PMID:22685285 | SOUND | wapR expression tracks the capped glycoform; term correct. | MigA | Yes |

Node-level problem at PTN000531351, recorded here once (GO_CENTRAL WRONG_TERM, CONFIRMED, on the WapR GO:0009244 IBA row) and cross-referenced from genes/PSEAE/migA: both seeds are sound, but the 18 leaves include Salmonella RfbV (P26401; IDA GO:0009243 O antigen biosynthesis, GO:0047600 abequosyltransferase, PMID:7541787) and E. coli WcaA (P77414; IDA GO:0009242 colanic acid biosynthesis, PMID:30821147), plus Yersinia WbyL, five Geobacter paralogues and Haemophilus, Helicobacter and Coxiella GT2 proteins. An LPS-core term is wrong for at least RfbV and WcaA. Leaf list from .cache/paint/leaf.gaf.gz; seed experimental annotations from live QuickGO, 2026-11-05.

PseudoCAP defects: GO:0009243 O antigen biosynthetic process WRONG_TERM (PROBABLE); GO:0015920 lipopolysaccharide transport WRONG_TERM (PROBABLE).

## Action counts

ACCEPT 4, TOO_GENERAL 3, REMOVE 2, MARK_AS_OVER_ANNOTATED 1.
