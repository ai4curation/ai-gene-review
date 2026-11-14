# ManX (EIIAB-Man) - Research Notes

## Summary

ManX (P69797) is the cytoplasmic EIIAB phosphorylating subunit of the mannose-specific PTS in E. coli K12. It is encoded by the manXYZ operon (b1817).

## Key findings

### Domain structure and phosphorylation
- ManX is a bifunctional protein with N-terminal EIIA domain (residues 2-124) and C-terminal EIIB domain (residues 157-320), connected by a flexible hinge [PMID:2681202 "Domain structure and function of the phosphorylating subunit"]
- EIIA domain is phosphorylated by HPr at His-10 (tele-phosphohistidine) [PMID:2681202, PMID:8262947]
- EIIB domain is phosphorylated at His-175 (pros-phosphohistidine) by EIIA [PMID:2681202, PMID:8262947]
- His-86 is involved in phosphoryl transfer between domains [PMID:8262947 "H86N mutation abolishes activity"]

### Dimerization
- ManX forms stable homodimers [PMID:2999119 "IIIMan, a 35-kDa protein, exists as a dimer"]
- H10C mutation abolishes dimerization [PMID:8262947]
- NMR structure of IIAMan-HPr complex (PDB: 1VRC) shows 48 kDa complex [PMID:15788390]

### Localization
- Dual localization: found both membrane-associated and free in cytoplasm [PMID:2999119]
- Peripheral membrane protein associated with inner membrane [PMID:16079137]

### Substrate specificity
- Primary substrates: mannose, glucose (2-deoxyglucose)
- Secondary substrates: fructose [PMID:4153999, PMID:4154035], N-acetylglucosamine [PMID:6252281]

### Regulation
- manXYZ operon positively regulated by cAMP-CRP complex [PMID:9484892]
- Negatively regulated by Mlc transcriptional repressor [PMID:9484892]
- Weakly repressed by NagC [PMID:11361067]

### Additional functions
- ManXYZ complex serves as chemoreceptor for sugar chemotaxis [PMID:4604906]
- ManXYZ required for phage lambda DNA injection, but ManY/ManZ alone sufficient [PMID:353494, PMID:2951378]

## Review decisions
- Removed GO:0005515 (protein binding) - uninformative per curation guidelines
- Marked GO:0016301 (kinase activity) as over-annotated - too broad for PTS phosphotransferase
- Core MF: GO:0022870 (mannose PTS transporter activity)
- Secondary substrates (fructose, GlcNAc, glucose) kept as non-core


## 2026-11-07 complete annotation re-review

All existing annotations and genuine Falcon research were re-read. No source file was refreshed. Historical notes above are retained; this audit supersedes their broad-term decisions and unsupported source attributions. General membrane/cytoplasm and ManX enzyme genera now refine to supported specific terms. ManX allows intra- and intersubunit phosphotransfer [PMID:2681202, PMID:8262947]; ManYZ supplies direct substrate-binding/translocation work, with contributes_to core rather than autonomous phosphorylation [PMID:31209249, PMID:2951378]. No new rows were added; historical complex NEW rows remain intact.

Source/construct scope, exact short quotations, access failures and ontology snapshots: `analysis/module_audits/bacterial_mannose_pts/ecoli-consultation/evidence.md`. In particular,1985IIMan is not uniquely modern ManZ,1996single-anchor ManZ topology is superseded by2019structure, and lambda membrane-component sufficiency does not establish a ManX pore. The2019ManYZ assay is counterflow in liposomes, not the complete PEP/ManX reaction; sequence-exact K-12 proteins were expressed recombinantly in knockoutBL21. Early sugar experimental annotations are retained with independent substrate corroboration and explicit inaccessible-table limits. All PAINT checks reported no IRD/IKR on the recovered target lineages.

## 2026-11-07 coupled-transporter core representation follow-up

The core GO:0022870 slot is now contributes_to_molecular_function because the schema reserves molecular_function for independently enabled activity and the coupled membrane-transport reaction requires ManY/ManZ. ManX still performs the directly demonstrated sugar-phosphorylation chemistry. All annotation actions and original enables payloads remain unchanged. This is a complex-level core representation correction, not a denial of catalytic activity. The original frozen handoff is retained; the additive core-contribution-followup receipt records this bounded supersession.

The four broad MF refinement rows now retain mannose, glucose, fructose and GlcNAc-specific coupled activities, rather than narrowing to mannose alone. Current QuickGO glucose/fructose terms leave phosphate position unspecified; PMID9864311 Figure1 explicitly supplies GlcNAc6-phosphate for GO0022880. The new publication was normally fetched without refreshing existing caches; full external primary acquisition and scope are recorded in the additive follow-up. All original payloads and action enums remain unchanged.
