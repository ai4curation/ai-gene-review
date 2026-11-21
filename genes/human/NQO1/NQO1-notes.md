# NQO1 notes

Automated deep-research attempts with `perplexity-lite` and `falcon` failed for
NQO1, and the `PTHR10204` family Falcon deep-research attempt also failed. The
review was therefore grounded manually from UniProt P15559, the 44 QuickGO rows,
PANTHER `PTHR10204`, Reactome, and the GOA-cited primary papers cached under
`publications/`.

NQO1 is the canonical human NAD(P)H quinone reductase in this two-human-member
PANTHER family. The purified human enzyme reduces alpha-tocopherolquinone to
alpha-tocopherolhydroquinone with NADH or NADPH [PMID:9271353, "reactions with
purified human NQO1, TQ was reduced to TQH2"], and older DT-diaphorase assays
measured direct reduction of menadione by human enzyme [PMID:8999809,
"DT-diaphorase of human"]. The FAD cofactor is integral to that hydride-transfer
cycle: the P187S structural/biophysical study directly measured FAD-bound wild
type and variant NQO1 [PMID:28291250, "FAD binding to NQO1 WT causes larger
changes in hydrodynamic volume"]. This supports the core function as a cytosolic
FAD-dependent homodimer that uses NADH/NADPH to reduce quinones to
hydroquinones/quinols.

`PTHR10204` has one human NQO1 member in `PTHR10204:SF1` and one human NQO2
member in `PTHR10204:SF33`. PAINT currently places `GO:0003955 NAD(P)H
dehydrogenase (quinone) activity` and `GO:0005829 cytosol` at the family root.
The root call is exact for NQO1. NQO2 has shifted its efficient donor to NRH, but
its existing review keeps weak NADH turnover as real and non-core, so no
NQO2-specific PAINT loss is needed.

Several biological-process rows are true substrate branches or outcomes of the
same quinone-reductase chemistry rather than separate core functions. NQO1 can
reduce ubiquinone, alpha-tocopherolquinone and vitamin K/menadione-like
substrates; it detoxifies benzene-derived quinones [PMID:10393963, "protected
against HQ-induced apoptosis"] and can bioactivate quinone-containing prodrugs
[PMID:8999809, "cytotoxic drug CB 1954"]. The in vitro superoxide-scavenging
activity is also real [PMID:15102952, "The addition of NQO1 in combination with
NAD(P)H resulted in inhibition"], but it is retained as a secondary antioxidant
activity relative to the quinone reductase core.

The mouse-derived Ensembl Compara rows for protein polyubiquitination,
proteasomal protein catabolism, lipopolysaccharide response and innate immune
response trace through the source MGI annotations to PMID:29934320. The full
text shows a specific macrophage mechanism in which Nqo1 bridges PDLIM2 to
I-kappa-B-zeta and promotes ubiquitin-dependent degradation after TLR
stimulation [PMID:29934320, "NQO1 augmented the association"], so these rows are
kept as a non-core immune-regulatory branch rather than dismissed as generic
stress annotations. This branch is distinct from the older noncatalytic role in
which human NQO1 stabilizes TP53, TP73, ING1 and PDLIM4/RIL by protecting them
from ubiquitin-independent 20S proteasomal degradation [PMID:15687255, "NQO1
physically interacts with p53 and p73 in an NADH-dependent manner"].

Three legacy PINC TAS rows cite PMID:9579781 for cytochrome-b5 reductase
activity, nitric-oxide biosynthesis and cholinergic synaptic transmission. The
abstract is a monkey/human cortex histochemistry study of m2-muscarinic
receptor, acetylcholinesterase and NADPH-diaphorase markers [PMID:9579781,
"NADPH-d enzyme activity with m2 immunoreactivity in the monkey and human
brain"]. It does not study NQO1 or these GO claims, so the rows are removed with
confirmed `WRONG_REFERENCE` source defects, and the synapse IEA derived from the
unsupported cholinergic row is removed too.

The HDA RNA-binding row comes from a HeLa mRNA interactome-capture atlas
[PMID:22658674, "interactome capture,"] with no NQO1 follow-up. It is marked
over-annotated. Bare `GO:0005515 protein binding` rows are removed under the
local protein-binding policy while retaining the mechanistic protein-stability
process rows they support.
