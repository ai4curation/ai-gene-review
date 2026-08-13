# LRBA literature notes

## Evidence hierarchy and working model

The strongest direct human mechanism is selective endosomal sorting rather than a
generic claim that LRBA is an integral membrane protein or a lysosomal enzyme. LRBA
helps route CTLA4 toward Rab11 recycling compartments and away from lysosomal
degradation: [PMID:33960403, "These results show that LRBA is required for effective
CTLA-4 recycling by delivering CTLA-4 to Rab11 recycling compartments, and in its
absence, CTLA-4 fails to recycle and undergoes degradation."] The earlier patient study
independently anchors the degradation phenotype: [PMID:26206937, "In LRBA-deficient
cells, inhibition of lysosome degradation with chloroquine prevented CTLA4 loss."]

This CTLA4 mechanism should not be expanded into a universal Rab11-residency claim.
The newer cell-biological study reports: [PMID:39325073, "We show that LRBA, however,
only slightly colocalizes with Rab11. Instead, LRBA is recruited by members of the
small GTPase Arf protein family to the TGN and to Rab4+ endosomes, where it controls
intracellular traffic."] The two studies can be reconciled if LRBA acts upstream of
Rab11 in cargo commitment rather than as a constitutive Rab11-compartment component.

## Endosome, lysosome, and Golgi boundaries

Direct localization evidence places LRBA at the trans-Golgi network and endosomes.
Mononuclear-phagocyte experiments specifically distinguish endosomal localization
from strong lysosome residency: [PMID:31883622, "LRBA was identified in early, late
endosomes but did not colocalize strongly with lysosomal markers."] Patient-fibroblast
work shows consequences downstream in the endolysosome system rather than proving
that LRBA is a lysosomal resident: [PMID:39325073, "In patient-derived fibroblasts,
loss of LRBA led to defects in the endosomal pathway promoting the accumulation of
enlarged endolysosomes and lysosome secretion."]

The founding LBA fusion-protein study reported vesicular, trans-Golgi and partial
lysosomal localization after LPS stimulation, but its cached abstract does not clearly
assign those assays to the human ortholog: [PMID:11254716, "Strikingly, LBA-green-fluorescent protein (GFP) fusion proteins are localized to vesicles after LPS
stimulation. Confocal microscopy indicates this protein is colocalized with the
trans-Golgi complex and some lysosomes."] Treat this as foundational model/ortholog
evidence, not as unqualified direct human compartment evidence.

## BEACH-domain and scaffold boundaries

LRBA is a large BEACH-family protein with a PH-BEACH tandem and WD40 repeats, but a
domain name is not a molecular-function annotation. The purified human LRBA PH domain
did not show phospholipid binding: [PMID:15554694, "However, our binding assays
demonstrate that the PH domain in the BEACH proteins cannot bind phospholipids."] The
same abstract reports PH-BEACH affinity for FAN, another BEACH-family protein; that
numeric affinity must not be transferred to LRBA.

There is direct evidence for an activation-dependent A-kinase anchoring role in human
B cells: [PMID:32592188, "Furthermore, in primary human B cells, LRBA was induced
after CD40L and IL-4 stimulation, and under such activation, we found that LRBA
interacts with RIIα and RIIβ, suggesting that LRBA acts as an AKAP and binds RII
subunits."] This supports a PKA regulatory-subunit scaffold/anchor role in that
context, not enzymatic kinase activity or a universal stable LRBA-PKA complex.

BioID/AP-MS places LRBA near TOM1 and TOLLIP: [PMID:31263572, "LRBA interacted with
both TOM1 and TOLLIP but had molecular context mainly in the Golgi/trans-Golgi
transport."] Because this is proximity/interaction evidence, it should not be used to
assert a stoichiometric stable complex without orthogonal biochemical support.

## Autophagy and mitophagy boundary

The direct ATG4 study supports an LRBA requirement in ATG9A-vesicle trafficking toward
damaged mitochondria: [PMID:33773106, "ATG4 proximity networks reveal a role for ATG4s
and their proximity partners, including the immune-disease protein LRBA, in ATG9A
vesicle trafficking to mitochondria."] The cache is abstract-only, so detailed claims
about the precise phagophore stage should defer to the experimental curator. Patient
genetics also associates LRBA loss with autophagy defects, but those phenotypes do not
by themselves define LRBA's direct molecular activity: [PMID:22608502, "We conclude
that mutations in LRBA cause an immune deficiency characterized by defects in B cell
activation and autophagy and by susceptibility to apoptosis, all of which are
associated with a clinical phenotype of hypogammaglobulinemia and autoimmunity."]

## Species, cell-type, disease, isoform, and screen boundaries

- Human LRBA loss causes immunodeficiency/autoimmunity and defects in B-cell activation,
  plasmablast formation, and immunoglobulin secretion, but these disease phenotypes
  are downstream constraints rather than molecular activities [PMID:22608502,
  "Individuals with homozygous LRBA mutations had no LRBA, had disturbed B cell
  development, defective in vitro B cell activation, plasmablast formation, and
  immunoglobulin secretion, and had low proliferative responses."]
- The CTLA4 phenotype depends on species and cellular context: [PMID:33960403,
  "Interestingly, the importance of LRBA in regulating CTLA‐4 appears to vary in
  different species and cell types as LRBA KO mice showed limited pathology [38, 39].
  Accordingly, we found that loss of LRBA in Jurkat cells had a much greater effect on
  CTLA‐4 than in HeLa cells."] Mouse knockout results therefore should not overrule
  the strong human disease/cell evidence.
- The original study found three tissue-dependent LBA transcripts
  [PMID:11254716, "In addition, lba is expressed in many other tissues in the body and
  has three distinct mRNA isoforms that are differentially expressed in various
  tissues."], whereas the current reviewed human UniProt record has two protein
  isoforms. A tested isoform does not imply an isoform-specific function.
- PMID:19946888 is a membrane proteome, and PMIDs 33961781 and 40205054 are large-scale
  interaction/cell-map studies. Their LRBA calls are dataset-level evidence. In
  particular, GOA/IntAct maps the latter two to CTLA4 (P16410), but the cached narrative
  does not expose the LRBA-CTLA4 row. These sources cannot establish direct binding or
  stable-complex membership on their own.

## Reference-phase scope

PubMed/current-primary-literature search was performed directly; project deep research
was skipped as permitted. Publication caches were fetched with the project
`fetch-pmid` command. No provider-named deep-research file was created. Annotation
reviews, synthesis, and status were intentionally left untouched during this phase.
