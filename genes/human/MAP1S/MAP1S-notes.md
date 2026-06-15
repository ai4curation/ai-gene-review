# MAP1S (Microtubule-associated protein 1S; C19orf5; MAP8; VCY2IP1) — review notes

UniProt: Q66K74 (MAP1S_HUMAN), 1059 aa, HGNC:15715. Processed into a heavy chain
(1-829) and a light chain (830-1059), like other MAP1 family members.

## Summary of function

MAP1S is the short, ubiquitously expressed member of the MAP1 family (paralogs MAP1A/MAP1B
are neuron-restricted). Like MAP1A/B it is synthesized as a precursor that is proteolytically
cleaved into heavy and light chains that re-associate as a heterodimer; both chains bind
microtubules and the light chain binds actin [UniProt SUBUNIT]. Its established core
molecular activity is binding to microtubules/tubulin and cross-linking/bundling them
[PMID:12762840 beta-tubulin binding; PMID:15528209 "Microtubule-associated protein 1S ... member of the microtubule-associated protein 1 family", microtubule binding/bundle formation].

The functionally distinctive role of MAP1S, and the reason it is of high interest, is as
a bridge that couples the autophagy machinery to the microtubule cytoskeleton and
mitochondria. MAP1S isoforms bind LC3 (the MAP1A/B light chain 3 / Atg8 homolog) and
recruit it to stable microtubules, and MAP1S binds the mitochondrion-associated protein
LRPPRC (which itself interacts with the mitophagy initiator Parkin); Map1s-knockout mice
show accumulation of defective mitochondria and severe defects in the nutritive-stress
response, indicating defects in autophagosomal biogenesis and clearance
[PMID:21262964 "MAP1S isoforms interacted with the autophagosome-associated light chain 3 of MAP1A/B (LC3) ... and recruited it to stable microtubules ... MAP1S interacted with mitochondrion-associated leucine-rich PPR-motif containing protein (LRPPRC) ... MAP1S isoforms may play positive roles in integration of autophagic components with microtubules and mitochondria in both autophagosomal biogenesis and degradation"].
This is the basis of the TAS autophagy annotation (GO:0006914) and is the core distinctive
function to highlight.

MAP1S also has cytoskeletal/mitotic roles: it anchors the microtubule-organizing center
to centrosomes, and its depletion causes mitotic abnormalities (failure to form a stable
metaphase plate, lagging chromosomes, multipolar spindles)
[PMID:17234756 "Depletion of ... C19ORF5/MAP1S causes mitotic abnormalities"].
It interacts with RASSF1A and stabilizes microtubules [PMID:15753381, PMID:15899810],
with the estrogen receptor ESR1, the NMDAR subunit NR3A/GRIN3A [PMID:17658481],
with LRPPRC [PMID:11827465, PMID:12762840], and with WDR47/Nemitin [PMID:22523538].

## DNA binding / nuclease
MAP1S was reported to bind DNA [PMID:15907802 "C19ORF5 is a DNA binding protein"], hence
the IDA DNA binding (GO:0003677) annotation. The same study reported it is NOT a DNA
nuclease — captured correctly as a NOT (negated) annotation to GO:0004536. There is a
nucleus localization (it shuttles), but the dominant functional pool is cytoplasmic/
cytoskeletal/mitochondrial.

## Localization
Cytoplasm/cytosol, cytoskeleton (microtubules, spindle, mitotic spindle microtubules),
centrosome/microtubule organizing center, perinuclear region (mitochondrial aggregates),
nucleus/nucleoplasm/nucleolus, cell projection/synapse (neuronal). The neuronal-process
annotations (synapse, dendrite, neuronal cell body, axonogenesis, dendrite development,
brain/nervous system development) are largely IBA/ISS transferred from the neuronal
paralogs MAP1A/B or from mouse orthologs; MAP1S is ubiquitous and these neuronal roles
are secondary/peripheral for the human gene.

## Annotation assessment highlights
- Core MF: microtubule binding (GO:0008017), tubulin binding (GO:0015631), beta-tubulin
  binding (GO:0048487) - ACCEPT (well-supported by IDA).
- Core CC: microtubule (GO:0005874), cytosol/cytoskeleton, microtubule associated complex
  (GO:0005875) - ACCEPT/KEEP.
- Core BP: autophagy (GO:0006914, TAS PMID:21262964) - ACCEPT as the distinctive function;
  microtubule cytoskeleton organization, microtubule bundle formation - ACCEPT/KEEP.
- actin binding (GO:0003779 IBA) and actin filament binding (GO:0051015 IDA, PMID:15528209)
  are positive; note there is also a NOT actin filament binding (GO:0051015 IDA,
  PMID:12762840) - a real curated negation from a different study/construct. Both are
  retained (the IDA-positive vs IDA-negated reflect different experimental contexts).
- NOT DNA nuclease activity (GO:0004536, negated, PMID:15907802) - ACCEPT the negation.
- DNA binding (GO:0003677 IDA) - KEEP_AS_NON_CORE (real but secondary).
- mitochondrion transport along microtubule (GO:0047497 TAS) and perinuclear region -
  consistent with the mitochondria/autophagy bridging role; KEEP/ACCEPT.
- Neuronal/developmental IBA/ISS terms - KEEP_AS_NON_CORE (transferred from paralogs/orthologs).
- Bare protein binding IPI entries - KEEP_AS_NON_CORE; informative partners captured elsewhere.
- WD40-repeat domain binding (GO:0071987, IPI, PMID:22523538, WDR47/Nemitin) - informative
  MF; KEEP_AS_NON_CORE.
- nucleolus/nucleoplasm (HPA IDA) - KEEP_AS_NON_CORE (shuttling pool, no nucleolar function).
