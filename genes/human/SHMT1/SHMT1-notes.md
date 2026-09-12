# SHMT1 (cytosolic serine hydroxymethyltransferase) — review notes

UniProt: P34896 (GLYC_HUMAN); gene SHMT1 (HGNC:10850); 483 aa; chromosome 17p11.2.
EC 2.1.2.1. Cytosolic isozyme (paralog of mitochondrial SHMT2/P34897).

## Core biology (from UniProt P34896)

SHMT1 is the cytosolic, PLP-dependent serine hydroxymethyltransferase. The
central reaction is the reversible interconversion of L-serine + THF with glycine
+ 5,10-methylene-THF (Rhea:RHEA:15481; EC 2.1.2.1), the major source of one-carbon
units in the cytosol for thymidylate and purine synthesis and for the methylation
cycle.

> "Pyridoxal phosphate (PLP)-dependent enzyme that catalyzes the reversible
> conversion of serine and tetrahydrofolate (THF) to glycine and 5,10-methylene
> THF, serving as a critical component of the folate cycle and facilitating
> one-carbon biosynthetic reactions essential for methionine, purine, and
> pyrimidine synthesis" [file:human/SHMT1/SHMT1-uniprot.txt FUNCTION].

Catalytic activity (authoritative Rhea in UniProt):
`(6R)-5,10-methylene-5,6,7,8-tetrahydrofolate + glycine + H2O = (6S)-5,6,7,8-tetrahydrofolate + L-serine; EC=2.1.2.1`
[file:human/SHMT1/SHMT1-uniprot.txt CATALYTIC ACTIVITY].

Cofactor: pyridoxal 5'-phosphate, bound via Schiff base at Lys-257
[file:human/SHMT1/SHMT1-uniprot.txt COFACTOR; FT BINDING].

Quaternary structure: homotetramer ("dimer of dimers"); crystal structure 1BJ4
[PMID:9753690 "The tetramer association is best described as a 'dimer of dimers'"].
Rat-liver work established the tetramer with 4 mol PLP/mol enzyme
[PMID:3110140 "showed a Mr value of 220,000 on gel filtration, indicating a
tetrameric structure"; PMID:6795186 "each of the isozymes is composed of 4
identical polypeptide chains"].

Pathway (UniProt): "One-carbon metabolism; tetrahydrofolate interconversion";
also "Amino-acid degradation" (via HTMLA/threonine-aldolase side activities)
[file:human/SHMT1/SHMT1-uniprot.txt PATHWAY].

## Secondary / promiscuous catalytic activities

SHMT1, like other fold-type-I PLP aldolases, cleaves several 3-hydroxy amino
acids by retro-aldol:
- L-allo-threonine, L-threonine → glycine + acetaldehyde
- 3-phenylserine → glycine + benzaldehyde (by similarity, P35623)
- HTML (3-hydroxy-N6,N6,N6-trimethyl-L-lysine) → glycine + 4-(trimethylamino)butanal
  (the second, "missing" step of carnitine biosynthesis; HTMLA activity)
[file:human/SHMT1/SHMT1-uniprot.txt CATALYTIC ACTIVITY].

Carnitine/HTMLA activity was demonstrated experimentally in PMID:38615009 (OSMES
docking + biochemical validation): "the top-ranked candidates, serine
hydroxymethyl transferase (SHMT) 1 and 2, catalyze the HTMLA reaction"; a
kcat/Km of 32.17 s-1 M-1 was measured for SHMT1 on HTML. The paper explicitly
frames this as partial compensation for a lost gene: "HTMLA activity of SHMT
partially compensating for its function" [PMID:38615009]. So SHMT1's carnitine
role is a low-efficiency moonlighting/backup activity, not a dedicated function.
The threonine-aldolase activities (GO:0004793, GO:0008732) share the same active
site and are genuine but promiscuous.

## Nuclear / de novo thymidylate role

SHMT1 (and the cytosolic SHMT2α splice form) translocate to the nucleus, where
SHMT1 acts as a scaffold anchoring the de novo thymidylate synthesis complex
(SHMT1 + DHFR + TYMS) to the nuclear lamina (LMNB1) at replication forks
[PMID:22235121 "SHMT serves as scaffold protein that is essential for complex
formation"; "de novo thymidylate biosynthesis occurs at replication forks"].
This is IDA-supported (interaction with TYMS, DHFR, LMNB1; lamin binding
GO:0005521; replication fork GO:0005657). Nuclear import is SUMO-dependent
(SUMOylation at Lys-38/39 by UBC9) [PMID:17446168].

PMID:30035852 showed the *catalytic* activity (not just scaffolding/oligomeric
state) is required for de novo nuclear dTMP synthesis in lung cancer cells:
"de novo thymidylate synthesis requires SHMT1 to be active, regardless of its
oligomeric state". Nuclear translocation is RAN-dependent and independent of
oligomeric state / catalysis [file:human/SHMT1/SHMT1-uniprot.txt SUBCELLULAR LOCATION].

Both nuclear thymidylate function and the moonlighting scaffold/lamin-binding
role are well-supported but represent a specialized, non-core (cell-cycle /
proliferation-context) deployment of the enzyme rather than its evolved core
catalytic function. Treated as KEEP_AS_NON_CORE.

## RNA-binding / riboregulation (moonlighting)

SHMT1 is an mRNA-binding protein. It binds its own 5'-UTR and represses its own
translation [PMID:10995219 "Human cSHMT protein at 10 microM inhibits in vitro
translation of cSHMT 5' UTR-luciferase fusion mRNA templates by more than 90%"].
The riboregulation was later structurally characterized: RNA binding acts as an
allosteric switch that selectively inhibits the serine-cleavage direction and
promotes glycine→serine conversion, feeding THF/serine to mitochondrial SHMT2
[PMID:38996576 "the RNA modulator competes with polyglutamylated folates and
acts as an allosteric switch, selectively altering the enzyme's reactivity vs.
serine"]. This is a well-supported moonlighting/regulatory function; the mRNA
5'-UTR binding (GO:0048027), translation repressor activity (GO:0000900) and
negative regulation of translation (GO:0017148) IDA annotations are kept as
non-core.

## Protein interactions

- BRISC-SHMT complex (ABRAXAS2, BRCC3/BRCC36, BABAM2, BABAM1); deubiquitinates
  IFNAR1 [UniProt SUBUNIT; PMID:24075985, not in review list].
- IDH3A/cSHMT interaction regulating one-carbon metabolism in glioblastoma
  [PMID:30613765 "IDH3α, by colocalizing and interacting with cytosolic serine
  hydroxymethyltransferase (cSHMT), regulates one-carbon metabolism"].
- Various IntAct binary interactors (DDX6, GORASP2, MAPK9, MDFI, SULT1A4, self).
- The bare `protein binding` (GO:0005515) IPI annotations are uninformative;
  MARK_AS_OVER_ANNOTATED (never REMOVE an IPI). `identical protein binding`
  (GO:0042802) reflects the homotetramer (kept as non-core, corroborates
  GO:0051289). `small molecule binding` (GO:0036094, IPI with CHEBI:67016 =
  (6S)-5-formyl-THF) is a very generic MF and is marked over-annotated in favour
  of PLP/serine binding.

## Localization

- Cytosol (GO:0005829) IDA/TAS — core.
- Nucleus (GO:0005634) IDA — real but conditional (S/G2M, thymidylate complex);
  kept as non-core.
- Cytoplasm (GO:0005737) IDA — broad parent of cytosol, over-annotated.
- Mitochondrion (GO:0005739) IBA — SHMT1 is the *cytosolic* isozyme; this IBA is
  a mis-propagation from mitochondrial SHMT orthologs (SHMT2) across the family
  tree (with/from includes SHMT2 P34897 and plant/fungal mito orthologs). REMOVE
  candidate but IBA — treated as over-annotation; the with/from list mixes mito
  and cytosolic orthologs, so the mitochondrion call is a branch artifact.
- Extracellular exosome (GO:0070062) HDA — high-throughput proteomics of urinary/
  prostatic exosomes; a common contaminant/secretion catch-all for abundant
  cytosolic enzymes. Kept as non-core.
- Replication fork (GO:0005657) IDA — real, part of nuclear thymidylate complex;
  non-core.

## Notable annotations to scrutinize

- GO:0006565 "L-serine catabolic process" IDA (PMID:17482557): that paper is
  about vitamin-B6 effects on SHMT activity/expression; it supports SHMT
  catalysis on serine. The serine-cleavage reaction is reversible; "catabolic"
  is one directional framing. Kept but the more accurate/less committal parent is
  L-serine metabolic process (GO:0006563). MARK_AS_OVER_ANNOTATED (directionally
  over-specific), not removed (IDA).
- GO:0009113 "purine nucleobase biosynthetic process" IDA (PMID:11516159): that
  13C-NMR paper actually concludes cytosolic SHMT is NOT a major one-carbon
  source for purine/thymidylate in MCF-7 ("The cleavage of serine to glycine and
  5,10-methylenetetrahydrofolate by cytosolic serine hydroxymethyltransferase
  does not appear to be a major source of one-carbon groups for either purine or
  thymidylate biosynthesis"). It is an IDA — do not remove; mark as
  over-annotated (the paper argues against a major role).
- GO:0006207 "'de novo' pyrimidine nucleobase biosynthetic process" IDA
  (PMID:22235121, PMID:30035852): SHMT1 supplies methylene-THF for dTMP; dTMP is
  a pyrimidine deoxyribonucleotide. The precise term is dTMP biosynthetic process
  (GO:0006231), also annotated. GO:0006207 is defensible but broad; kept.

## Core function synthesis

1. **Glycine hydroxymethyltransferase (serine hydroxymethyltransferase) activity**
   — GO:0004372 (MF) + PLP binding GO:0030170; directly involved in one-carbon
   metabolic process (GO:0006730), tetrahydrofolate interconversion (GO:0035999),
   L-serine metabolic process (GO:0006563), glycine biosynthetic process
   (GO:0006545); location cytosol (GO:0005829). Homotetramer (GO:0051289).
   This is the evolved core.

Secondary (non-core but real): nuclear de novo thymidylate synthesis / scaffold
(dTMP biosynthetic process GO:0006231, lamin binding), riboregulation / mRNA
5'-UTR binding, and HTMLA/threonine-aldolase promiscuous activities (carnitine
biosynthesis backup).
