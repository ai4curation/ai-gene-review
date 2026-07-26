# ACAN (human aggrecan) — curation notes

UniProt P16112. HGNC:319. PANTHER PTHR22804 (hyaluronan-binding proteoglycan / lectican family:
ACAN, VCAN, NCAN, BCAN plus the HAPLN link proteins).

## What the protein is

A very large secreted chondroitin-sulfate proteoglycan with a tridomain architecture: an N-terminal
G1 (Ig + two Link modules) that binds hyaluronan, a G2 (two further Link modules), a huge central
keratan-sulfate/chondroitin-sulfate attachment region, and a C-terminal G3 (EGF + C-type lectin +
CCP/Sushi).

[file:human/ACAN/ACAN-uniprot.txt "CC   -!- DOMAIN: Two globular domains, G1 and G2, comprise the N-terminus of the"]

[file:human/ACAN/ACAN-uniprot.txt "CC   -!- FUNCTION: This proteoglycan is a major component of extracellular"]
[file:human/ACAN/ACAN-uniprot.txt "CC       resist compression in cartilage. It binds avidly to hyaluronic acid via"]

Secreted; UniProt subcellular location is extracellular matrix, and expression is essentially
restricted to cartilage plus a distinct CNS pool in perineuronal nets.

[file:human/ACAN/ACAN-uniprot.txt "CC   -!- SUBCELLULAR LOCATION: Secreted, extracellular space, extracellular"]
[file:human/ACAN/ACAN-uniprot.txt "CC       (PubMed:36213313). Restricted to cartilage (PubMed:7524681)."]

## Core biology

**Aggregate formation is the function.** Many aggrecan monomers bind a single hyaluronan filament
through G1, each junction stabilised by a HAPLN link protein, generating >200 MDa assemblies. The
dense negative charge of the ~100 chondroitin-sulfate chains draws in water; the resulting swelling
pressure, restrained by the collagen II network, is what makes cartilage resist compression.

[PMID:25701227 "is the principal load-bearing proteoglycan of cartilage"]
[PMID:25701227 "These large aggregates generate a densely-packed, hydrated gel enmeshed in a network of reinforcing collagen fibrils and other proteoglycans"]
[PMID:25701227 "The G1/hyaluronan/link protein ternary complex is very stable thereby immobilizing the aggrecan into enormous complexes that maintain a stable network and provide mechanical properties to cartilage."]
[PMID:27068509 "Negatively charged glycans on the surface of aggrecan attract water and therefore confer resistance to compression."]

**Hyaluronan binding is now structurally and biophysically nailed down for the human protein.**
Otsuka et al. 2025 solved the cocrystal structure of the human ACAN G1 region with an HA
decasaccharide and measured the affinity by biolayer interferometry. This matters for curation:
GOA still carries hyaluronic acid binding only as an InterPro IEA.

[PMID:40273987 "Amino acid numbering corresponds to human ACAN (UniProt ID# P16112)"]
[PMID:40273987 "We demonstrate that the single immunoglobulin domain and the two Link modules that comprise the G1 region form a single structural unit, and that HA is clamped inside a groove that spans the length of the tandem Link domains."]
[PMID:40273987 "In these experiments, ACAN binds to immobilized HA with an affinity of 234 nM, which is consistent with the value of 226 nM reported in an earlier study using surface plasmon resonance"]

**The G3 C-type lectin binds other matrix proteins.** Tenascins, fibulins, sulfated glycolipids.
Human missense variants in this repeat cause familial osteochondritis dissecans and both reduce
secretion and reduce ligand binding.

[PMID:25701227 "Moreover, the G3 domain of aggrecan interacts with tenascins, fibulins and sulfated glycolipids"]
[PMID:20137779 "Binding studies with recombinant mutated and wild-type G3 proteins showed loss of fibulin-1, fibulin-2, and tenascin-R interactions for the V2303M protein."]
[PMID:35338222 "The variant proteins also showed decreased binding to known cartilage extracellular matrix ligands."]
[PMID:35338222 "Functional studies showed that neither recombinant variant proteins, nor full-length variant aggrecan proteoglycan from heterozygous patient cartilage, were secreted to the same level as wild-type aggrecan."]

**COMP is a validated partner.** Solid-phase binding, calcium-dependent on COMP's side, mediated
partly through aggrecan's GAG chains.

[PMID:17588949 "Using a solid-phase binding assay, we have shown that COMP/TSP5 can bind aggrecan."]
[PMID:17588949 "Soluble glycosaminoglycans (GAGs) partially inhibited binding, suggesting that the interaction was mediated in part through aggrecan GAG side chains."]

**The CNS pool is perineuronal nets.** Aggrecan is the lectican most specific to PNNs, and human
G1 and G1-G2 fragments bind PNNs on cortical neurons. Notably, HA binding contributes to but is not
required for PNN incorporation, so there is a second, still-unidentified anchoring activity.

[PMID:25701227 "Aggrecan is also expressed in the brain, and unlike other hyalectans, is expressed primarily in the perineuronal nets"]
[PMID:40273987 "both fragments of ACAN bound highly and very specifically to PNNs on cultured cortical neurons"]
[PMID:40273987 "Thus, these results suggest that ACAN can be recruited into PNNs independently of its HA-binding activity."]

**Aggrecan is a protease substrate, not a protease.** The interglobular domain between G1 and G2
carries the aggrecanase (ADAMTS4/5) site; cleavage at Glu373-Ala374 releases the GAG-bearing bulk of
the molecule into synovial fluid in osteoarthritis, leaving the G1 tethered to hyaluronan.

[PMID:1569188 "This NH2 terminus results from cleavage of the human aggrecan core protein at the Glu 373-Ala 374 bond within the interglobular domain between the G1 and G2 domains."]
[PMID:25701227 "An interglobular region, between G1 and G2, has a rod-like structure and harbors several protease-sensitive sites involved in the partial degradation of aggrecan in arthritis and other inflammatory diseases."]
[file:human/ACAN/ACAN-uniprot.txt "CC       stages of human osteoarthritis is the result of cleavage by"]

## WITH/FROM resolution (the highest-yield check)

IPI partners:

| accession | gene | verdict |
|---|---|---|
| UniProtKB:P49747 | COMP | real, direct solid-phase binding (PMID:17588949); an ECM ligand |
| UniProtKB:P05067 | APP | yeast-two-hybrid neurodegeneration interactome screen (PMID:32814053); no orthogonal validation, no functional follow-up |

IBA donors (resolved via the Alliance API):

| id | gene | species |
|---|---|---|
| MGI:MGI:99602 | Acan | mouse |
| MGI:MGI:1096385 | Bcan | mouse |
| MGI:MGI:104694 | Ncan | mouse |
| MGI:MGI:1337006 | Hapln1 | mouse |
| MGI:MGI:2679531 | Hapln4 | mouse |
| RGD:68358 | Acan | rat |
| RGD:2194 | Bcan | rat |
| RGD:619940 | Vcan | rat |
| RGD:619941 | Ncan | rat |
| ZFIN:ZDB-GENE-030131-2185 | vcanb | zebrafish |

Every IBA row includes at least one true ACAN ortholog (mouse or rat Acan), so none of them is a
pure paralog transfer. The problems that remain are term-scoping, not donor choice.

## Annotation problems found

1. **`involved_in GO:0006508 proteolysis` (NAS, PMID:1569188) is backwards.** The cited paper shows
   aggrecan being *cleaved* by a cartilage proteinase. Being a substrate is not participating in
   proteolysis; the agents are ADAMTS4/ADAMTS5 and the MMPs. Substrate-as-agent role conflation.
2. **`involved_in GO:0007155 cell adhesion` (IEA, InterPro:IPR000538).** The Link-domain family
   mapping carries both hyaluronic acid binding and cell adhesion. The cell-adhesion half comes from
   the cell-surface HA receptors in the family (CD44, TSG-6), not from the secreted lecticans.
   Aggrecan is not a cell adhesion molecule and has no membrane anchor.
3. **`is_active_in GO:0045202 synapse` (IBA).** GO deliberately places perineuronal net outside the
   synapse: GO:0072534's ancestors run perisynaptic extracellular matrix (GO:0098966) →
   synapse-associated extracellular matrix (GO:0099535) → specialized extracellular matrix
   (GO:0140047)/extracellular matrix, and GO:0045202 is not among them (checked via QuickGO
   `/ontology/go/terms/GO:0072534/ancestors`). The same IBA batch already gives the precise term.
4. **Reactome reaction-level export dominates the record.** 14 of 40 rows are `located_in Golgi
   lumen` and 6 are `located_in extracellular region`, one per keratan-sulfate biosynthesis reaction.
   Five of the Golgi rows come from *defective*-enzyme disease reactions (R-HSA-3656230,
   R-HSA-3656258, R-HSA-3656269, R-HSA-9035949, R-HSA-9035950), where the biology being modelled is
   a congenital disorder of glycosylation, not aggrecan function.
5. **No correct biological process is annotated at all.** After removing proteolysis and cell
   adhesion, GOA's only BP terms are two broad development terms. Nothing states that aggrecan
   builds the matrix — extracellular matrix organization (GO:0030198) / assembly (GO:0085029) is the
   obvious gap.
6. **`GO:0005540 hyaluronic acid binding` is still only IEA** despite a 2025 human cocrystal
   structure and BLI affinity measurement (PMID:40273987). Straightforward IDA/IPI upgrade.
7. UniProt's DR block lists `GO:0005615 extracellular space` (IBA), `GO:0030246 carbohydrate binding`
   and `GO:0046872 metal ion binding` (both `IEA:UniProtKB-KW`), none of which appear in the GOA TSV
   snapshot. The keyword-derived pair is expected — GO_REF:0000043 SPKW annotations were withdrawn.

## Things deliberately *not* annotated

- The three UniProt DISEASE entries (SEDK, SEMDAG, SSOAOD) are disease associations, not GO
  processes. Short stature is a phenotype of haploinsufficiency.
- The affinage narrative is dominated by *regulators of ACAN transcription* — SOX9, the SOX trio,
  SHOX2, TET1, SIRT1, HDAC2, miR-140, mTOR/4E-BP1. Being a transcriptional target of SOX9 is not an
  ACAN function; those findings belong on the regulators.
- Two affinage findings rest on bioRxiv preprints with no PMID. One of them (the G1-HA cocrystal /
  PNN integration study) has since been published as PMID:40273987 and is used here in its published
  form; the other (Amigo2-Acan CA2 conditional knockout) has not been, and is not used.

## Follow-up checks prompted by PR review

**The GO:0072534 ancestor claim, re-verified in both directions** (the reviewer could not run this
without network access, and the synapse MODIFY rests entirely on it).

`GET /ontology/go/terms/GO:0072534/ancestors?relations=is_a,part_of` returns exactly:

```
GO:0099535  synapse-associated extracellular matrix
GO:0140047  specialized extracellular matrix
GO:0072534  perineuronal net
GO:0098966  perisynaptic extracellular matrix
GO:0031012  extracellular matrix
GO:0110165  cellular anatomical structure
GO:0030312  external encapsulating structure
GO:0005576  extracellular region
GO:0005575  cellular_component
```

`GO:0045202` is absent. The reciprocal query confirms it:
`GET /ontology/go/terms/GO:0045202/descendants?relations=is_a,part_of` returns 143 descendants, and
`GO:0072534`, `GO:0098966` and `GO:0099535` are all absent from that set. So the exclusion is
symmetric and deliberate, not an artifact of one traversal direction.

**GO:0085029 usage precedent.** QuickGO annotation search (`goId=GO:0085029&taxonId=9606`) returns 94
annotations over 40 gene products. Matrix *structural constituents* are well represented, not just
remodelling enzymes and signalling proteins: ELN (elastin), FBLN5, EFEMP2, EMILIN1, MFAP4, COL8A1,
COL8A2, TNXB. Elastic-fibre assembly by elastin and the fibulins is the direct analogue of
proteoglycan-aggregate assembly by aggrecan, so the proposed NEW annotation is consistent with
established usage. Enzymes and regulators (HAS1/2/3, LOX, PXDN, QSOX1/2, TGFB1, SMAD3/4, TGFBR1/3)
are also present, but the term is clearly not reserved for them.

**The proteolysis harm is concrete, not hypothetical.** All four of the following carry the identical
term with the identical qualifier, so in any process-based query the substrate is indistinguishable
from the three enzymes that destroy it:

| gene | accession | GO:0006508 evidence |
|---|---|---|
| ACAN | P16112 | NAS (PMID:1569188) — the substrate |
| ADAMTS4 | O75173 | IEA, IBA, TAS (PMID:10751421) |
| ADAMTS5 | Q9UNA0 | IEA, IBA, TAS (PMID:10438522) |
| HTRA1 | Q92743 | ISS, IBA, IEA |

**Anticipated objection to the proposed cartilage-matrix component term.** GO:0062023
"collagen-containing extracellular matrix" was obsoleted, which might look like a precedent against
tissue-scoped ECM components. It is not: the obsoletion comment reads "This term was obsoleted
because it was not clearly defined and usage has been inconsistent." That term was
*composition*-scoped and unbounded. GO:0140047 continues to carry many *tissue- or structure*-scoped
children — perineuronal net, interphotoreceptor matrix, hyaline layer, cuticular extracellular
matrix, egg coat, pollen coat, middle lamella, chitin-based extracellular matrix, organomineral
extracellular matrix. Cartilage matrix is anatomically bounded in the way "collagen-containing" never
was.

**Domain architecture verified against the UniProt feature table** rather than against the affinage
narrative, since the provider is unreliable on domain assignment:

```
SIGNAL 1..16 ; no TRANSMEM ; no LIPID/GPI anchor
G1 = Ig-like V-type 34..147 + Link 1 153..248 + Link 2 254..350
G2 = Link 3 478..573 + Link 4 579..675
KS 677..849 ; CS-1 852..1612 ; CS-2 1613..2277
G3 = EGF-like 2279..2314 + C-type lectin 2327..2441 + Sushi 2445..2505
```

The absence of a transmembrane segment and of any GPI anchor is what underpins the cell-adhesion
REMOVE. The Glu373-Ala374 aggrecanase site falls between Link 2 (ends 350) and Link 3 (starts 478),
confirming it is genuinely interglobular as PMID:1569188 states.
