# glaH (CsiD) — Glutarate 2-hydroxylase — *Pseudomonas putida* KT2440 (PSEPK)

UniProt: Q88IU0 | Gene: glaH (synonym csiD) | Locus: PP_2909 | EC 1.14.11.64

## Function summary

GlaH (also called CsiD) is a soluble, non-heme Fe(II)/2-oxoglutarate-dependent
dioxygenase that catalyzes the hydroxylation of glutarate to L-2-hydroxyglutarate
(L2HG). In the canonical reaction it couples glutarate hydroxylation to the
oxidative decarboxylation of 2-oxoglutarate (2-ketoglutarate, 2KG), producing
succinate and CO2 and consuming one molecule of O2. This reaction is the key
step of the CoA-independent route of glutarate (and downstream L-lysine)
catabolism in *P. putida*, channeling carbon into central metabolism: the L2HG
produced is re-oxidized to 2KG by LghO (PP_2910), regenerating the cosubstrate
and leaving succinate as the net carbon input to the TCA cycle.

The enzyme is a homotetramer that binds one Fe(2+) per subunit. It is extremely
specific for glutarate as the hydroxylation substrate but is promiscuous in its
2-oxoacid cosubstrate, able to use either 2-oxoglutarate or 2-oxoadipate (2OA);
when 2OA is used the co-product is glutarate rather than succinate, providing a
possible biochemical link between the D- and L-lysine catabolic pathways.

## Evidence / provenance

### Catalytic activity and mechanism
- [UniProt "Acts as an alpha-ketoglutarate-dependent dioxygenase catalyzing hydroxylation of glutarate (GA) to L-2-hydroxyglutarate (L2HG) (PubMed:31064836)."]
- [UniProt "Reaction=glutarate + 2-oxoglutarate + O2 = (S)-2-hydroxyglutarate + succinate + CO2; Xref=Rhea:RHEA:13821"]
- [UniProt "EC=1.14.11.64"]
- [PMID:31064836 "They described a cyclic reaction cascade wherein a novel 2KG-dependent nonheme Fe(II) oxygenase, PP_2909 (CsiD), hydroxylates glutarate to form 2HG and succinate using 2KG as a cosubstrate."]
- [PMID:31064836 "We also purified csiD and confirmed that it hydroxylated glutarate in a 2KG-dependent manner"]
- [PMID:31064836 "HPLC analysis demonstrated that as glutarate was consumed, equimolar quantities of succinate and l-2HG were produced"]

### Cofactor (ferrous iron)
- [UniProt "Name=Fe(2+); Xref=ChEBI:CHEBI:29033"]
- [UniProt "Note=Binds 1 Fe(2+) ion per subunit."]
- [UniProt "KW   Dioxygenase; Iron; Metal-binding; Oxidoreductase; Reference proteome."]

### Substrate specificity / cosubstrate promiscuity
- [UniProt "Is extremely specific for glutarate, but it can use both 2-oxoglutarate and 2-oxoadipate (2OA) as a cosubstrate for L2HG formation (PubMed:31064836)."]
- [PMID:31064836 "Although extremely specific for the hydroxylation substrate, all three CsiD homologs could utilize both 2OA and 2KG, but not oxaloacetate, as a cosubstrate for l-2HG formation"]
- [PMID:31064836 "we probed the activity of the homologs against a panel of 3 to 6 carbon fatty acids and diacids in the presence of 2KG and found that only glutarate served as a hydroxylation substrate"]

### Biological process — L-lysine / glutarate catabolism
- [UniProt "Functions in a L-lysine degradation pathway that proceeds via cadaverine, glutarate and L-2-hydroxyglutarate (By similarity)."]
- [PMID:31064836 "PP_2910 (LghO), a putative l-2HG oxidase, then subsequently converts l-2HG to 2KG, regenerating the 2KG consumed in the initial reaction. These reactions result in the net incorporation of succinate into central metabolism"]
- [UniProt "PATHWAY: Amino-acid degradation."]

### Induction and disruption phenotype
- [UniProt "Induced when grown on glutarate, and also moderately up-regulated by 5-aminovalerate (5AVA) and L-lysine."]
- [UniProt "Deletion mutant shows an increased lag time when grown on either L-lysine or 5-aminovalerate (5AVA)."]
- [PMID:31064836 "a csiD deletion mutant showed an increased lag time when grown on either l-lysine or 5AVA"]

### Structure / family
- [UniProt "SUBUNIT: Homotetramer."]
- [UniProt "SIMILARITY: Belongs to the glutarate hydroxylase family."]
- Fe-binding residues (His160, Asp162, His292 — 2-His-1-carboxylate facial triad typical of non-heme Fe(II) dioxygenases) per UniProt BINDING features.

## Annotation review rationale

- GO:0106343 (glutarate dioxygenase activity) — most specific MF; ACCEPT. There is an
  EXP-supported instance (PMID:31064836) and an IEA instance; both core.
- GO:0008198 (ferrous iron binding) — specific, supported by COFACTOR Fe(2+); ACCEPT as core.
- GO:0005506 (iron ion binding) — correct but less specific than ferrous iron binding;
  MARK_AS_OVER_ANNOTATED (more specific GO:0008198 present).
- GO:0016706 (2-oxoglutarate-dependent dioxygenase activity) — true parent activity but
  less specific than glutarate dioxygenase activity; MARK_AS_OVER_ANNOTATED.
- GO:0050498 (oxidoreductase activity, acting on paired donors ... 2-oxoglutarate as one
  donor ...) — even more general parent; MARK_AS_OVER_ANNOTATED.
- GO:0019477 (L-lysine catabolic process) — correct BP, the physiological role; ACCEPT.
</content>
