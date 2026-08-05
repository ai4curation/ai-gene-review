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
