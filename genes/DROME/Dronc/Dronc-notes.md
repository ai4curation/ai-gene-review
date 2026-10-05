# Dronc notes

## 2026-09-30 APOPTOSIS manual review

Dronc is the Drosophila long-prodomain initiator caspase. Its core pathway is
the Dark apoptosome branch: Dark recruits Dronc through CARD-mediated contacts
and promotes Dronc autoprocessing; the active initiator caspase then cleaves
effector caspases such as DrICE [PMID:21220123, "Dark-Dronc complex cleaves
DrICE"; PMID:25644603, "Dronc is efficiently activated"]. The structural
activation rows are well supported: autocleavage increases activity and yields a
stable Dronc homodimer [PMID:16446367, "The autocleaved Dronc forms a
homodimer"], and the Dronc-CARD/Dark contacts are needed for activation
[PMID:25644603, "nearby Dark protomer are indispensable for Dronc activation"].

The generic `protein binding` rows divide cleanly by partner. DrICE rows were
recast as `GO:0008656 cysteine-type endopeptidase activator activity involved
in apoptotic process`, because the informative activity is effector-procaspase
cleavage. Dark rows were recast as `GO:0050700 CARD domain binding`. DIAP1 rows
were removed from the Dronc side: DIAP1 really binds and ubiquitinates Dronc,
but the row asserts only uninformative binding by the inhibited substrate
[PMID:12021771, "targeting caspases for ubiquitination"; PMID:14517550,
"DIAP1 recognizes Dronc"].

Broad `GO:0006915 apoptotic process` rows for the core RHG/DIAP1/Dark-Dronc
branch were tightened to `GO:2001235 positive regulation of apoptotic signaling
pathway`, matching the existing PAINT import without forcing the fly pathway
into the mammalian cytochrome-c/CASP9 intrinsic-signaling term. Eiger/TNF rows
were kept as non-core where the source tied Dronc/Dark to a context-specific
Eiger/JNK apoptosis branch [PMID:12176339, "requires the caspase-9 homolog
DRONC"; PMID:31409797, "apoptosis and necrosis establish a two-layered defense
system"].

Dronc is also reused in direct nonapoptotic or atypical death outputs. ARK- and
HID-dependent Dronc activation occurs at spermatid individualization sites, a
nonlethal cystic-bulge process [PMID:14737191, "activation of DRONC occurs at
sites of spermatid individualization"]. Dark-dependent caspase activity cleaves
the Shaggy/GSK-3beta isoform Sgg46 and contributes to sensory-organ precursor
and chaeta patterning without killing the cells [PMID:16222340, "is cleaved by
the Dark-dependent caspase"]. p53-dependent spermatogonial programmed necrosis
uses Dronc atypically, independent of catalytic activity and Dark, so it is real
but not part of the core apoptosome caspase model [PMID:28945745,
"Dronc/Caspase 9"].

Rows backed only by abstracts were kept cautious. The local cache does not show
Dronc-specific evidence for NOPO/Eiger, neuron-remodeling, dendrite
morphogenesis, melanization-defense, salivary-gland histolysis, compound-eye
retinal-cell death, or the DrICE/DIAP1 execution-phase row, so those exact rows
are `UNDECIDED` pending full-text or FlyBase figure-level confirmation rather
than being removed from incomplete evidence.
