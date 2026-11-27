# arcC (PA5173, P13982) review notes

## Literature

- ArcC is the carbamate kinase of the arginine deiminase (ADI) pathway, the third enzyme of the arcDABC operon. The enzyme was purified from PAO1 and shown to be distinct from carbamoyl-phosphate synthetase and acetate kinase [PMID:6286599 "Pseudomonas aeruginosa PAO1 possessed a carbamate kinase (CKase) distinct from carbamoylphosphate synthetase as well as from a constitutive acetate kinase which also catalyzes the phosphorylation of ADP by carbamoylphosphate"]. It is a dimer, inhibited by ATP, and induced by anaerobiosis and arginine [PMID:6286599 "CKase was induced to high levels by anaerobiosis, induced to moderate levels by arginine, and repressed by ammonia"]; its role is to supply ATP anaerobically (and ammonia aerobically) [PMID:6286599 "CKase expression is regulated in a manner that allows the enzyme to function as a provider of ammonia under aerobic conditions and of ATP under anaerobic conditions"].
- arcC mutants were isolated among mutants unable to grow anaerobically on arginine and map in the arc cluster [PMID:6438064 "The mutations arcA (arginine deiminase), arcB (catabolic ornithine carbamoyltransferase), arcC (carbamate kinase), and arcD were highly cotransducible"].
- UniProt (curated): physiological direction is ATP formation from carbamoyl phosphate and ADP; pathway L-arginine degradation via ADI pathway [file:PSEAE/arcC/arcC-uniprot.txt "Amino-acid degradation; L-arginine degradation via ADI"]. Crystal structure 8CRV.
- arcA and arcB were reviewed in this batch's predecessors (`genes/PSEAE/arcA`, `genes/PSEAE/arcB`); both use GO:0006527 L-arginine catabolic process as the process term (GO:0019546 L-arginine deiminase pathway is obsolete). This review follows them.

Search: both cached papers are abstract-only (PMC220422 and PMC215798 exist but were not retrieved as full text). Sibling seed E. coli AllK (P37306) checked in UniProt and QuickGO (live query, 2026-11-05): its experimental annotations are GO:0008804 IDA and GO:0000256 allantoin catabolic process IDA (PMID:36384810, EcoCyc), and its curated function is "Kinase involved in the anaerobic nitrogen utilization via the assimilation of allantoin".

## Catabolic/anabolic check (cf. arcB)

ArcB carried anabolic IBAs (arginine and citrulline biosynthesis) from an OTC family node. ArcC has no anabolic IBA; carbamate kinase runs the ATP-generating direction both in the ADI pathway and in allantoin assimilation. The analogous problem here is a pathway mismatch rather than a direction mismatch: the PTN000764469 IBD of GO:0000256 allantoin catabolic process rests on E. coli AllK alone, and propagates to the ADI-pathway carbamate kinases in the same clade (P. aeruginosa ArcC, H. influenzae ArcC P44769, Salmonella STM4466, Geobacter CpkA). Carbamate kinase is a terminal enzyme shared by several carbamoyl-phosphate-producing catabolic pathways; which pathway each paralog serves is set by operon context, not by the kinase fold. P. aeruginosa arcC sits in the arc operon and is induced by arginine and anaerobiosis. So the allantoin process IBA is removed with one GO_CENTRAL defect.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001252214 | GO:0016301 kinase activity | 2 | 15 (12 taxa) | GO:0008804, IMP, PMID:6438064 | SOUND | arcC mutants lack carbamate kinase activity; the locus was later shown to encode the purified enzyme (UniProt EXP, PMID:6286599; sequence and structure). Generic node term entailed by the gene's activity. | E. coli AllK (P37306; GO:0008804 IDA, PMID:36384810) | Yes |
| PTN000764469 | GO:0008804 carbamate kinase activity | 2 | 7 (6 taxa) | GO:0008804, IMP, PMID:6438064 | SOUND | As above; term is the gene's own MF, and it suits a clade of carbamate kinases. | E. coli AllK (P37306; IDA) | Yes |

Not a PseudoCAP seed: PTN000764469 also carries an IBD of GO:0000256 allantoin catabolic process seeded only by E. coli AllK. Node term does not suit the clade (it includes ADI-pathway kinases). GO_CENTRAL defect recorded on the arcC GO:0000256 IBA row (PROBABLE).
