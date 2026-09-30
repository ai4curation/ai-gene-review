# BAG3 review notes

## 2026-04-26

- Confirmed identity: human BAG3 / BAG family molecular chaperone regulator 3, UniProt O95817.
- Core function synthesis: BAG3 is best treated as an HSP70-family co-chaperone and modular adaptor, not as a generic protein-binding protein. Its BAG domain supports HSP70 nucleotide exchange, while other motifs link HSP70/HSC70 to small heat shock proteins such as HSPB8 [PMID:24318877 "Proteins with Bcl2-associated anthanogene (BAG) domains act as nucleotide exchange factors"; PMID:27884606 "BAG3 is a modular, scaffolding factor to bring together sHsps and Hsp70s"].
- CASA/aggrephagy is central to the review. BAG3 coordinates Hsc70/HSPB8 with CHIP/STUB1 and p62 in chaperone-assisted selective autophagy, which is explicitly distinct from canonical chaperone-mediated autophagy [PMID:20060297 "CASA is thus distinct from chaperone-mediated autophagy"].
- BAG3 also couples HSP70 clients to dynein and aggresome targeting, supporting the aggresome, aggresome assembly, protein transport along microtubule, and dynein intermediate chain binding annotations [PMID:21252941 "BAG3, which interacts with the microtubule-motor dynein and selectively directs Hsp70 substrates"].
- Muscle/Z-disc annotations are justified through CASA-mediated maintenance of mechanically stressed muscle structures, especially damaged filamin handling in Z-disc/mechanotransduction contexts [PMID:20060297 "Impaired CASA results in Z disk disintegration"; PMID:23434281 "The CASA complex... senses the mechanical unfolding of the actin-crosslinking protein filamin"].
- HSF1 nuclear shuttling and BCL2-related anti-apoptotic activity are supported, but they are non-core relative to the HSP70/sHSP/CASA proteostasis axis [PMID:26159920 "BAG3 rapidly translocalized to the nucleus upon heat stress"; PMID:10597216 "Bis itself exerted only weak anti-apoptotic activity"].
- Marked generic protein binding annotations as over-annotated or modified to more informative terms when the source supported a clear chaperone-binding, adaptor, NEF, or dynein-binding interpretation.

## 2026-09-30 — ClinGen Mendelian campaign audit

This audit revisits all source assertions in the earlier COMPLETE review. The
raw GOA contains 168 distinct annotation objects when qualifier and interaction
partner are retained. The older review contained 77; deterministic expansion
restored the other 91 before manual reassessment. All source terms, evidence
codes, reference identifiers, qualifiers and supporting entities are preserved.
The preceding journal is retained as historical reasoning; the decisions below
supersede its generic-interaction dispositions and several overly strong
rejections.

### Identity and main activities

Human BAG3 is UniProt O95817 (BAG3_HUMAN), HGNC:939, NCBI Gene 9531 and
ENSG00000151929. The existing source and provider files were retained unchanged.
The Falcon report was read critically; current trial, patent or secondary-review
claims in that report were not treated as primary evidence for GO annotations.

Three activity-centered core units capture the supported biology. BAG-domain
nucleotide-exchange activity regulates the Hsp70 cycle. Modular adaptor activity
links Hsp70 and small heat-shock proteins and connects the CASA scaffold with
muscle maintenance and autophagosome machinery. Protein-carrier activity couples
Hsp70-associated clients to dynein and accompanies them to aggresomes. These roles
are distinct from Hsp70 ATP hydrolysis, dynein motor activity, membrane fusion,
or lysosomal degradation [PMID:24318877; PMID:27884606; PMID:20060297;
PMID:23434281; PMID:21252941].

### Primary evidence and important limits

PMID:27884606 was assessed from its available main Introduction, Results,
Discussion and relevant Methods. BAG3's IPV motifs bind small heat-shock proteins
and its BAG domain binds the Hsp70 nucleotide-binding domain. Reconstituted
binding and size-exclusion experiments support simultaneous ternary assemblies.
The two-small-HSP-subunit/one-BAG3 model was tested with a truncated Hsp27 domain;
it is not a universal native stoichiometry. The nucleotide-release assay used
fluorescent ATP, so it is not relabeled as a direct ADP-release assay. Functional
effects depend on concentration and the chaperone combination: BAG3 can support
productive refolding at suitable ratios and inhibit it at high concentration.
Figure images, supplementary raw data and every individual partner-screen
record were not independently inspected.

PMID:30559338 was assessed from the available main Introduction, Results,
Discussion and selected Methods. P209L retained HSPA8 association and
fluorescent-nucleotide release while disrupting productive Hsp70-dependent
client processing. Its soluble non-native oligomers and chaperone-dependent
client trapping distinguish it from simple loss of all binding or exchange
activity. Complete loss of small-HSP binding did not reproduce every P209L
effect. Genetic or pharmacological disruption of the mutant BAG3-Hsp70
interaction reduced aggregation in the tested systems; no clinical-treatment
conclusion is drawn. Original images and supplementary raw data were not read.

PMID:19085932 was assessed from the complete abstract and available main
Introduction, Methods and Results. Normal human muscle localizes BAG3 at the
Z-disc and sarcolemma. This supports the broad membrane annotation, because
membrane-associated proteins need not span the bilayer. Patient muscle pathology
and apoptotic nuclei support disease relevance but do not define a single
autonomous anti-apoptotic mechanism.

PMID:21252941 was assessed from its complete available main text and Methods.
BAG3 accompanies Hsp70-associated clients during dynein- and microtubule-dependent
aggresome targeting. The protein-carrier assertion is retained, while the
description specifies Hsp70-dependent client recognition; direct BAG3 contact
with every misfolded client was not demonstrated. Dynein intermediate-chain
association is supported by pull-down and coimmunoprecipitation experiments,
without a claim of purified binary binding. Cargo, aggresome and tissue
experiments used different systems, including HEK293, COS7 and mouse tissue.
The studied transport pathway can operate without substrate ubiquitination;
that does not establish ubiquitin independence of all CASA. The source's
statement about two WW domains is not adopted: BAG3 has one WW domain.

PMID:19229298 was assessed from the abstract and relevant initial Results on
human fibroblast aging, perturbation, autophagic flux and SQSTM1 association.
The entire Discussion and supplementary material were not inspected. The
results support the shift from BAG1/proteasome-associated disposal to BAG3-linked
autophagy and do not make BAG3 itself a degradation enzyme.

For PMID:18006506, PMID:20060297, PMID:23434281 and PMID:24318877, the complete
cached abstracts were available, but the full primary bodies were unavailable.
Their mechanistic conclusions were bounded accordingly. Protein stabilization
includes prevention of aggregation, so directing some clients for disposal does
not contradict stabilization of others. The experimental stabilization assertion
was retained with independent chaperone-function support; its precise original
assay was not reconstructed. CASA is distinguished from canonical
chaperone-mediated autophagy. The latter process term is refined to the
supported positive regulation of aggrephagy.

The complete abstracts of PMID:26159920, PMID:10597216 and PMID:9873016 support
stress-phase-dependent BAG3/HSF1 shuttling, BAG3/BCL2 survival cooperation and
concentration-dependent Hsp70 regulation. HSF1 association does not assign
DNA-binding activity to BAG3; altered shuttling does not establish a general
nuclear transport receptor.

### Partner-specific interactions and unresolved assertions

Independent annotation consultation assessed all 112 generic-binding source
objects. Nineteen are refined using the actual partner: HSPB8 and DNAJB6 to
protein-folding chaperone binding, HSPB1/Hsp27 to Hsp27 protein binding, HSPA1A,
HSPA1B and HSPA8 to Hsp70 protein binding, HSF1 to DNA-binding transcription
factor binding, and SYNPO2 to adaptor activity. Primary PMID:22366786 supports
association of human DNAJB6b and BAG3 constructs in COS-1 cells; this replaces
the provider-report placeholder and does not imply purified binary binding.
The individual HSPA1B assay is not visible in the available PMID:24318877
abstract, so the retained specific interaction defers to experimental curation.

Q8TEU7 is RAPGEF6, while Q9UMS6 is SYNPO2. The former row's inherited SYNPO2
description is corrected without altering the source partner. Mechanistic
results for HSPB5 or HSPB1 are not copied to different small-HSP partners CRYAA
or HSPB2. The remaining 93 generic interactions are retained as non-core:
uninformative binding alone does not show an assertion to be false under the
supplied ActionEnum. Individual screen supplement records were unavailable;
the absence of a BAG3 mention from an abstract is not evidence of misattribution.

Three annotations remain UNDECIDED. The rat stress-fiber localization traces to
PMID:23434281, whose accessible abstract does not expose the specific IDA
localization experiment. Z-disc localization does not contradict stress fibers.
The rat spinal-cord-development assertion traces to developmental radial-glial
expression in PMID:19415333, not an ALS study; expression timing alone does not
identify a developmental step performed by BAG3. The cadherin-binding HDA in
PMID:25468996 is based on E-cadherin proximity proteomics with selected follow-up
validation. The abstract and relevant BioID main-text discussion were read, but
the BAG3-specific supplementary evidence was not; proximity alone does not
resolve the specific binding activity.

The rat mitochondrial-localization annotation is narrower than general protein
import. PMID:21561597 reports BAG3-dependent cytosolic BAX retention and BAX
redistribution after depletion in rat C6 glioma cells. It is retained as a
non-core regulatory role. Human tumor immunohistochemistry in that study is
separate from the rat mechanistic assays. Two source-cache records are being
added to substantiate these propagation findings; their final access scope is
recorded in the completion addendum.

The current proposal has 34 ACCEPT, 21 MODIFY, 110 KEEP_AS_NON_CORE and three
UNDECIDED decisions, with no NEW or REMOVE assertions. All 168 original source
objects remain distinct. Short exact excerpts are placed once where most useful,
with reference identifiers connecting related claims elsewhere. The existing
notes above are preserved; no new long quotations are added here.


### Source completion and final review scope

Both additional normal reference records are now present and remain marked
abstract-only. PMID:19415333 was checked against the official PubMed identity
and complete abstract; the developmental expression evidence leaves the
spinal-cord-development assignment UNDECIDED. PMID:21561597 was checked against
PubMed and PMC3124067. In addition to its cached abstract, the official primary
figure captions and indexed PMC cell-culture/coimmunoprecipitation Methods and
relevant BAX Results were read. These identify rat C6 cells as the mechanistic
system. Human tumor expression and human-cell survival assays are separate.
This supports retaining the BAX-localization annotation as non-core. Full
primary bodies were not recovered into either cache, and no complete-paper or
supplementary-data assessment is claimed for these two references.

The two references and short exact abstract anchors complete the evidence
links without changing any annotation decision or core function. The review
has 41 references and all 168 source assertions, including three explicit
UNDECIDED annotations. Existing source and provider files remain unchanged.
