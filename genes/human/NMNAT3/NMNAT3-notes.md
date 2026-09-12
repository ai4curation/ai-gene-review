# NMNAT3 (human) — gene review notes

UniProt: Q96T66 (NMNA3_HUMAN). HGNC:20989. Gene: NMNAT3. 252 aa. Chromosome 3.
EC 2.7.7.1 (nicotinamide-nucleotide adenylyltransferase) and EC 2.7.7.18
(nicotinate-nucleotide adenylyltransferase).

## Core identity / function

NMNAT3 is the **mitochondrial isoform** of nicotinamide/nicotinic acid mononucleotide
adenylyltransferase, one of three human NMNATs (NMNAT1 nuclear, NMNAT2 Golgi/cytosolic,
NMNAT3 mitochondrial). It catalyses the central, shared reaction of NAD+ biosynthesis:
adenylyl transfer from ATP to a pyridine mononucleotide.

- Deamidated branch: NaMN + ATP -> NaAD (deamido-NAD+) + PPi  (EC 2.7.7.18)
- Amidated branch:   NMN  + ATP -> NAD+ + PPi                  (EC 2.7.7.1)

Both branches are catalysed with comparable efficiency; NMNAT3 has a notably broad
substrate tolerance among the three isoforms.

[file:human/NMNAT3/NMNAT3-uniprot.txt "Catalyzes the formation of NAD(+) from nicotinamide
mononucleotide (NMN) and ATP (PubMed:16118205, PubMed:17402747, PubMed:26616331). Can also
use the deamidated form; nicotinic acid mononucleotide (NaMN) as substrate with the same
efficiency."]

[file:human/NMNAT3/NMNAT3-uniprot.txt "Nicotinamide mononucleotide adenylyltransferase
(NMNAT) is the central enzyme of"] — from PMID:16118205 abstract.

PMID:16118205 (Berger et al. 2005) [PMID:16118205 "Analyses of the subcellular localization
confirmed NMNAT1 to be a nuclear protein, whereas NMNAT2 and -3 were localized to the Golgi
complex and the mitochondria, respectively."] — establishes NMNAT3 mitochondrial localization
and differential catalytic properties (broad substrate tolerance; can also form NADH directly
from reduced NMN). Source of the GO:0000309, GO:0004515 (IDA) and GO:0005739 (IDA/EXP)
annotations.

PMID:17402747 (Sorci et al. 2007) [PMID:17402747 "distinctive ordered ternary complex kinetic
mechanisms, substrate specificities, and metal ion preferences for the three isozymes of human
nicotinamide mononucleotide adenylyl-transferase (NMNAT, EC 2.7.7.1)"] and [PMID:17402747
"the opposite order is observed with the mitochondrial isozyme NMNAT3. Only the latter utilizes
ITP efficiently in place of ATP"]. Full initial-rate kinetics; Mg2+ cofactor (per UniProt);
distinctive substrate binding order for NMNAT3. Source of GO:0000309, GO:0004515 (EXP).

PMID:12574164 (Zhang et al. 2003) [PMID:12574164 "the identification and structural
characterization of a novel human PNAT (hsPNAT-3) that is located in the cytoplasm and
mitochondria"] and [PMID:12574164 "The characterization of the cytosolic human PNAT-3 provided
compelling evidence that the final steps of NAD biosynthesis pathways may exist in mammalian
cytoplasm and mitochondria"]. 1.9 Å X-ray structures (PDB 1NUP-1NUU) in complex with NMN, NAD,
ATP analog; homotetramer (SUBUNIT: Homotetramer, PubMed:12574164). Source of GO:0005739 (EXP)
localization.

## Subcellular location

Mitochondrion / mitochondrial matrix. UniProt SUBCELLULAR LOCATION:
[file:human/NMNAT3/NMNAT3-uniprot.txt "SUBCELLULAR LOCATION: Mitochondrion"].
Note some studies (Zhang 2003; Reactome R-HSA-200474) report both cytosolic and mitochondrial
pools; Reactome annotates the mitochondrial form. HTP mito-proteome (PMID:34800366) and HPA
immunofluorescence (GO_REF:0000052) corroborate mitochondrial localization.

## Chaperone / neuroprotection annotations — caveat

GO:0006457 (protein folding, IDA) and GO:0044183 (protein folding chaperone, IDA) are annotated
to human NMNAT3 citing PMID:18344983 (Zhai et al. 2008, Nature). That paper demonstrates the
chaperone function in **Drosophila NMNAT (DmNMNAT)**:
[PMID:18344983 "NMNAT displays chaperone function both in biochemical assays and cultured cells,
and it shares significant structural similarity with known chaperones."]. It does not assay
human NMNAT3 chaperone activity specifically. This is a family-/similarity-level attribution.
The chaperone activity is a real, well-documented NMNAT function in Drosophila, but for the
human mitochondrial NMNAT3 isoform it is not directly demonstrated and is peripheral to the
core mitochondrial NAD+-synthesis function. Marked KEEP_AS_NON_CORE (experimental IDA; do not
remove).

PMID:26616331 (Ruan et al. 2015, Nat Commun) is about **Drosophila Nmnat** splice variants; it
mentions human NMNAT3 splice variants only in passing
[PMID:26616331 "two splice variants of human NMNAT3 (v1 and V3-FKSG76) have been experimentally
identified"]. It is cited on a GO:0000309 (NMNAT activity, IDA) annotation. NMNAT activity is
unquestionably correct for human NMNAT3 (see 16118205, 17402747), so retained; the citation is
weaker than the two primary human enzymology papers.

## BP / process annotations

- GO:0009435 NAD+ biosynthetic process — core; well supported by UniProt PATHWAY
  [file:human/NMNAT3/NMNAT3-uniprot.txt "Cofactor biosynthesis; NAD(+) biosynthesis"].
- GO:0034355 NAD+ biosynthetic process via the salvage pathway (IBA) — NMNAT is the last,
  shared step of the salvage route (NMN from NAM via NAMPT -> NAD+); reasonable, kept.
- GO:0009165 nucleotide biosynthetic process (IEA/IC) — correct but a broad parent of NAD+
  biosynthesis; over-general.
- GO:0034612 response to tumor necrosis factor (IEA, GO_REF:0000107, from rat ortholog
  ENSRNOP00000018411) — electronic transfer from a rat ortholog; not supported for human
  NMNAT3 by any primary data here; over-annotation.

## CC annotations from neuronal-orthology electronic transfer

- GO:0030424 axon and GO:0043025 neuronal cell body (IEA, GO_REF:0000107, from rat ortholog)
  — these are neuronal-compartment localizations transferred electronically from a rat ortholog.
  NMNAT2 (Golgi/axon) is the axonally-transported neuroprotective isoform in mammals; NMNAT3 is
  mitochondrial. These axonal/neuronal-body localizations are not supported for human NMNAT3 and
  look like mis-transfer / over-annotation. Kept but flagged.

## Molecular function — assignment

Core MF: the two catalytic activities directly demonstrated by human enzymology:
- GO:0000309 nicotinamide-nucleotide adenylyltransferase activity (EC 2.7.7.1) — NMN + ATP -> NAD+
- GO:0004515 nicotinate-nucleotide adenylyltransferase activity (EC 2.7.7.18) — NaMN + ATP -> NaAD

Both are strictly supported by IDA/EXP (16118205, 17402747) and match the UniProt CATALYTIC
ACTIVITY / EC assignments. Broad parents GO:0016779 (nucleotidyltransferase activity) and
GO:0003824 (catalytic activity) are IEA over-generalizations.

ATP binding (GO:0005524) appears in the UniProt DR GO block (IEA UniProtKB-KW) but is NOT in the
GOA TSV rows seeded into the review, so it is not reviewed as an existing annotation.

## Core function summary

NMNAT3 is a mitochondrial NAD+ biosynthetic enzyme supplying the mitochondrial NAD+/NADH pool by
adenylylating NMN (-> NAD+) and NaMN (-> NaAD), the final shared step of both the de novo/
Preiss-Handler and salvage routes to NAD+.
</content>
</invoke>
