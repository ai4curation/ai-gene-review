# ospC1 (Shigella flexneri, Q8VSJ7) — curation notes

## Literature search record

No deep-research provider is available in this environment, so the search below was
done by hand over the cached publication set and the UniProt record.

Sources checked:

- `genes/SHIFL/ospC1/ospC1-uniprot.txt` (Swiss-Prot Q8VSJ7, entry version 113,
  2026-09-02): curated FUNCTION, CATALYTIC ACTIVITY, SUBUNIT, SUBCELLULAR
  LOCATION, DISRUPTION PHENOTYPE, MUTAGEN features, OspC family note.
- Every PMID cited by the GOA rows, fetched into `publications/`:
  PMID:16988276, PMID:23684308, PMID:32657447, PMID:34409271, PMID:34671164,
  PMID:35338844, PMID:35568036.
- Context read for mechanism (not edited): a calmodulin/CaMKII pathway module
  and reviews of the two OspC GO-CAMs, proposed in ai4curation/ai-gene-review#5904
  and not part of this branch; nothing in this review rests on them. The cached
  models themselves, `gocams/62b4ffe300005467/62b4ffe300005467-src.yaml` and
  `gocams/62b4ffe300005437/62b4ffe300005437-src.yaml`, are on main and were read.
- GO term checks against the local GO build (OakOracle / oaklib `sqlite:obo:go`),
  2026-11-04: labels and definitions of GO:0005516, GO:0030430, GO:0042025,
  GO:0005576, GO:0052029, GO:0075135, GO:0052041, GO:0140740, GO:0140311,
  GO:0140886; `GO:0075135` and `GO:0140886` confirmed as `is_a` descendants of
  `GO:0052029`; `GO:0140311` confirmed to sit under `GO:0140313 molecular
  sequestering activity`, i.e. a lateral re-typing relative to `GO:0005516`.

## What the protein is

OspC1 is one of three paralogous OspC-family type III secretion system effectors
encoded on the Shigella virulence plasmid (pCP301 / pWR100 / pMYSH6000). It is
470 aa, with an N-terminal catalytic region and a C-terminal ankyrin-repeat
region (ANK 1-3, residues 363-467 in UniProt). It is secreted through the T3SS
and delivered into the host cell, where it is found in both cytoplasm and
nucleus.

## Two separable activities

### 1. Arginine ADP-riboxanase (NAD+-dependent lyase, EC 4.3.99.-)

[PMID:34671164 "OspC3, but not its paralogues OspC1 and 2, covalently modified
caspase-11/4; although it used the NAD+ donor, this modification was not
ADP-ribosylation."] and, decisively for OspC1,
[PMID:34671164 "The enzymatic activity was shared by OspC1 and 2, whose
ankyrin-repeat domains, unlike that of OspC3, could not recognize caspase-11/4."]
So the catalytic chemistry is a family property; what distinguishes OspC3 is that
its ANK domain recognises caspase-4/11. UniProt records the reaction with
experimental evidence from two papers (Rhea:RHEA:69500,
ECO:0000269|PubMed:34671164 and ECO:0000269|PubMed:35338844), and mutating
Asp172 or Asp226 abolishes activity
[file:SHIFL/ospC1/ospC1-uniprot.txt "D->A: Abolished ADP-riboxanase activity and ability to inhibit host cell caspases."].

The host targets of OspC1's riboxanase activity are the apoptotic caspases, not
the LPS-sensing ones: UniProt's curated FUNCTION states ADP-riboxanation of CASP3,
CASP8 and CASP9 prevents their activation (ECO:0000269 from PMID:32657447 and
PMID:35338844), and explicitly that OspC1 "Does not catalyze ADP-riboxanation of
host CASP4/CASP11 (PubMed:34671164)".

Cell-biological consequence, from the only full-text paper on this arm:
[PMID:32657447 "We identified a dual inhibitory mechanism in which apoptosis is prevented by the Shigella T3SS effector OspC1 and necroptosis by the OspD3 effector."]
[PMID:32657447 "Intriguingly, the reduction in the levels of MLKL phosphorylation and cytotoxicity in cells infected with ΔospC1ΔospD3 was rescued by ospC1 gene complementation (ΔospC1ΔospD3/ospC1), indicating that OspC1‐mediated caspase‐8 inhibition induced necroptosis (Fig 5A and B)."]
[PMID:32657447 "Taken together, these data reveal the order of sequential cell death inhibition by Shigella; OspC3 acts first to prevent pyroptosis, followed by OspC1‐mediated inhibition of apoptosis and OspD3‐mediated inhibition of necroptosis."]

Note that the proximate target of OspC1's anti-apoptotic effect was not
identified in the infection work: [PMID:35568036 "OspC1 targets an unknown host factor to inhibit Caspase 3/7-mediated apoptosis (Ashida et al., 2020), whereas OspC3 binds Caspase 4/11 to inhibit pyroptosis via its ADP-riboxanase activity (Kobayashi et al., 2013; Li et al., 2021; Oh et al., 2021)."]

### 2. Sequestration of Ca2+-free calmodulin, blocking interferon signalling

This is a separate, catalysis-independent activity
[PMID:35568036 "Therefore, these findings establish that OspC effectors inhibit cell death and IFN signaling by distinct biochemical mechanisms."].

- Binding: a yeast two-hybrid screen with full-length OspC1/2/3 as bait against a
  human macrophage library, plus calmodulin-bead pulldowns from lysates of cells
  expressing GFP-tagged effectors, with EDTA in the pulldown and CaCl2 elution so
  the apo form is what is captured. All three paralogs bind
  [PMID:35568036 "However, all three OspC effectors interacted with Apo-CaM"],
  but only two inhibit
  [PMID:35568036 "pCaMKII binding to CaM was similarly inhibited by OspC1 or OspC3 but not OspC2"].
- Mechanism as the authors state it:
  [PMID:35568036 "This suggests a model whereby OspC recruits and sequesters CaM in the absence of Ca2+, thus preventing its downstream activation of CaMKII."]
- Downstream: [PMID:35568036 "T286 phosphorylation was reduced upon expression of OspC1 or OspC3 but not OspC2 (Figure 3F)."],
  [PMID:35568036 "Expression of OspC1 and OspC3 completely abolished STAT1 phosphorylation in response to IFNβ treatment (Figures 4H and S5F)."],
  and in infection [PMID:35568036 "Moreover, although HeLa cells infected with WT Shigella exhibited little to no CaMKII phosphorylation, those infected with strains lacking either OspC1 or OspC3 demonstrated evidence of T286 phosphorylation that was further increased within cells infected with ΔospC1/C3 Shigella (Figure 3H, quantification Figure S5D)."]
- Breadth of the interferon block: [PMID:35568036 "We found that OspC1 and OspC3 blocked signaling downstream of increasing concentrations of IFNs from all 3 families (Figure 1E)."]
  This is why the review modifies the generic `GO:0052029` row to
  `GO:0140886 symbiont-mediated suppression of host interferon-mediated signaling
  pathway` rather than to the type-I-specific child `GO:0039502`.
- Epistasis placing the target upstream of the kinase:
  [PMID:35568036 "However, in the presence of active GFP-CaMKII, OspC1 and OspC3 were no longer able to significantly block ISRE activation (Figure 4K, black bars)."]
- Virulence: [PMID:35568036 "The growth of Shigella lacking OspC1 and OspC3 was attenuated in epithelial cells and in a murine model of infection."]

## Localisation

[PMID:16988276 "We transformed S. flexneri with a plasmid that expresses a two-hemagglutinin tag (2HA) in frame with OspF or OspC1 and verified that these proteins are secreted in a T3SS-dependent manner."]
[PMID:16988276 "Immunofluorescence of HeLa cells infected with S. flexneri expressing OspF-2HA or OspC1-2HA revealed that both proteins localize in the nucleus and cytoplasm of host cells."]

So host cytoplasm and host nucleus are both directly observed. Every known
activity of OspC1 (calmodulin sequestration, caspase modification) is cytosolic;
nothing is known to happen in the nucleus, so the nuclear row is kept as
non-core. Secretion into the medium is a transit state detected in the
T3SS-secretion assay, so `GO:0005576` is likewise non-core.

An older phenotype, not reducible to either mechanism above: a ΔospC1 mutant
shows reduced PMN transepithelial migration and reduced ERK1/2 phosphorylation
in infected T84 cells [PMID:16988276 "in the polymorphonuclear (PMN) cell migration assay, a decrease in neutrophil migration was observed for both mutants in comparison to the migration of wild-type bacteria"].
No molecular mechanism has been attached to this, and it is a whole-infection
phenotype, so no process term is proposed from it.

## Reference-level problem found

The GOA row `GO:0030430 host cell cytoplasm` (IDA) is keyed to PMID:34409271,
"Shigella OspC3 suppresses murine cytosolic LPS sensing". The cached full text of
that paper (`publications/PMID_34409271.md`, `full_text_available: true`) does
not contain the string "OspC1" anywhere; it is an OspC3 study. The location claim
is nevertheless true and directly shown elsewhere (PMID:16988276). The same
mis-keyed reference appears in GO-CAM gomodel:62b4ffe300005467, where
PMID:34409271 carries the `ECO:0000314` `occurs_in` evidence — consistent with
the OspC1 model having been cloned from the OspC3 model 62b4ffe300005437.
Recorded here as a `source_defects` entry on the row, with the row itself
accepted.

## Calmodulin binding versus sequestration

This review keeps the IDA `GO:0005516` row (the binding is directly assayed and the
partner is informative) and adds `GO:0140311` as a NEW row, since the paper's own
conclusion is sequestration of the apo form and that is the claim with mechanistic
content. OspC2 is the family's informative negative and would merit a NOT
annotation on its own entry; it is out of scope here.
