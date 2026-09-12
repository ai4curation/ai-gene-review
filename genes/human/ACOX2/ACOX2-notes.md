# ACOX2 (human) — gene review notes

UniProtKB: Q99424; HGNC:120; gene ACOX2 (chromosome 3p14.3). 681 aa; C-terminal SKL
peroxisomal targeting signal (PTS1). EC 1.3.3.6. FAD flavoprotein. Homodimer (by similarity).

Deep research note: falcon deep-research provider is out of credits (HTTP 402), so no
`-deep-research-falcon.md` was generated. This review is grounded in the UniProt record,
the seeded GOA, and cached publications only.

## Function

ACOX2 is the human **peroxisomal branched-chain acyl-CoA oxidase** (originally "hBRCACox";
homolog of rat trihydroxycoprostanoyl-CoA / THCC oxidase). It is a FAD-dependent oxidase
that catalyses the **first, oxygen-dependent, rate-limiting dehydrogenation** step of
peroxisomal beta-oxidation, removing two hydrogens and introducing a trans-2,3 double bond
into the acyl-CoA, producing H2O2 as a byproduct (UniProt FUNCTION; EC 1.3.3.6).

Two physiological substrate classes:
1. **C27 bile-acid intermediates** — (25S)-THCA-CoA and DHCA-CoA. ACOX2 initiates the
   side-chain shortening that converts C27 cholestanoic acids to the mature C24 bile acids
   (cholic / chenodeoxycholic). [PMID:27884763 "Acyl-CoA oxidase (ACOX2) is involved in the
   shortening of C27 cholesterol derivatives to generate C24 bile acids"]
2. **2-methyl-branched-chain fatty acyl-CoAs** — e.g. (2S)-pristanoyl-CoA; stereospecific
   for (2S)-methyl isomers. Redundant with ACOX3 for pristanoyl-CoA (PMID:29287774, per
   UniProt). Also mono-methyl branched-chain FAs (mmBCFA) in brown adipose tissue (by
   similarity to mouse Q9QXD1). Low-efficiency straight-chain activity (C10, C16).

The 1990 human-liver enzymology paper [PMID:2079609] established that human liver contains a
**separate trihydroxycoprostanoyl-CoA oxidase** distinct from palmitoyl-CoA oxidase (ACOX1),
explaining why bile-acid metabolism is normal in ACOX1 deficiency — this separate THCC
oxidase is ACOX2.

## Localization

Peroxisome / peroxisomal matrix. Direct protein evidence in human liver
[PMID:8943006] (immunocytochemistry; SKL PTS1; absent in Zellweger livers) and
[PMID:2079609]. IMP peroxisomal localization confirmed for both WT and R225W mutant in
HepG2 [PMID:27884763 "similar protein size and peroxisomal localization for both normal and
mutated variants"]. The Reactome TAS `cytosol` annotations refer to the peroxisomal-import
transit state (PEX5 cargo in cytosol before matrix translocation), not the site of
catalytic activity.

## Disease

**ACOX2 deficiency / Congenital bile acid synthesis defect 6 (CBAS6; MIM:617308)** —
autosomal recessive inborn error of bile-acid synthesis. Accumulation of toxic C27
intermediates (THCA, DHCA), negligible C24 bile acids, persistent hypertransaminasemia /
liver fibrosis; variable neurological features (ataxia, cognitive impairment). Known
variants: R225W [PMID:27884763] and a large N-terminal deletion (69-682 del) [PMID:27647924,
via UniProt]. Phytanic/pristanic acids remain normal (redundancy with ACOX3 for BCFA).

## Molecular function GO landscape

- GO:0003997 acyl-CoA oxidase activity — parent MF; core (EC 1.3.3.6). Best single MF.
- GO:0033791 THCA-CoA 24-hydroxylase activity — the bile-acid-specific reaction, IDA in
  [PMID:27884763]; also directly matches Rhea:46728 in UniProt. Core bile-acid MF.
- GO:0016402 pristanoyl-CoA oxidase activity — BCFA reaction; UniProt Rhea:40459
  (PubMed:29287774). Valid but redundant with ACOX3.
- GO:0120523 / GO:0120524 medium-/long-chain fatty acyl-CoA oxidase activity — RHEA IEA
  (decanoyl/hexadecanoyl-CoA). UniProt calls straight-chain activity "low efficiency", so
  these are minor/over-annotations relative to the branched-chain and bile-acid core.
- GO:0005504 fatty acid binding (IBA) — substrate binding is implied by catalysis but a bare
  "fatty acid binding" MF is uninformative for this enzyme; over-annotation.
- GO:0050660 FAD binding / GO:0071949 FAD binding — cofactor binding; supported (COFACTOR FAD).
- GO:0042803 protein homodimerization activity (ISS from P07872/ACOX1) — UniProt SUBUNIT
  "Homodimer (By similarity)"; accept as by-similarity.
- GO:0005515 protein binding (IPI, STRN3 / DYNLT1) — bare "protein binding" from high-throughput
  interactome screens; uninformative, over-annotated.

## Biological process

- GO:0006699 bile acid biosynthetic process (IDA, PMID:27884763) — core BP.
- GO:0033540 fatty acid beta-oxidation using acyl-CoA oxidase — the precise BP; IDA/IMP core.
- GO:0006635 fatty acid beta-oxidation — parent BP; accept.
- GO:0000038 very long-chain fatty acid metabolic process (IBA) — ACOX2 handles
  branched-chain and C27 bile-acid substrates, not straight VLCFA (that is ACOX1). Likely
  IBA over-propagation; mark over-annotated.
- GO:0006631 fatty acid metabolic process — broad InterPro IEA; accept as broad-but-correct.
</content>
