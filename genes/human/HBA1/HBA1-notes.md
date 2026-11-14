# HBA1 curation notes

## 2026-11-14 — primary-source review

The native pipeline fetched human alpha-globin P69905 and seeded 85 annotation
contexts. All original terms, evidence codes, references, partners, qualifiers and
isoform/negation fields are preserved. The initial complete draft has 27 ACCEPT,
37 KEEP_AS_NON_CORE, 10 MODIFY, 10 UNDECIDED and 1 MARK_AS_OVER_ANNOTATED; no NEW,
REMOVE or retired annotations. It remains DRAFT.

Research used primary publications, native UniProt/Reactome records, retained
PAINT sources and live ontology/interaction services. The configured Falcon
authentication and fallback-provider quota were already unavailable in this
campaign; no new HBA1 provider attempt or provider-named report is claimed.
Annotation-reviewer and core-function-synthesizer guidance was applied, with
read-only independent helpers and one checkout writer.

### Shared protein and respiratory-gas function

P69905 represents both HBA1 and HBA2. Protein assays and PAINT rows labeled HBA2
do not establish a different alpha-chain sequence or an HBA1-specific regulatory
effect. The mature alpha chain, residues 2–142 (PRO_0000052653), associates with
beta-like globins in adult, fetal and embryonic hemoglobins.

- PMID:11307949 measures recombinant HbA2 oxygen affinity, cooperativity and
  tetramer/dimer behavior. The accessible abstract supports the shared alpha
  chain's gas-carrier role without converting mutant properties into wild-type
  claims.
- PMID:16765986 presents human oxy/deoxy/carbonmonoxy structures and explicitly
  describes the oxygen ligand and distal histidine in both alpha and beta chains.
- PMID:1552945 describes alpha-beta dimers; PMID:15835899 describes their relative
  rotations; PMID:30833564 directly discusses alpha-beta heterodimer particles.
  These support a specific assembly refinement for the direct structural contexts.
- Reactome R-HSA-1237325 describes “chemical reaction (carbamation) of the
  N-terminal valines of HbA by CO2”. R-HSA-1247668 describes pulmonary CO2/O2
  exchange. The globin participates through its own reversible binding chemistry;
  carbonic-anhydrase catalysis is not assigned to HBA1.

One core unit captures oxygen carrier activity in cytosolic hemoglobin, directly
involved in oxygen and carbon dioxide transport. Carbon monoxide binding is not
used as evidence of carbon dioxide transport. The developmental IBA remains
non-core; globin imbalance affecting maturation does not establish a developmental
transcription-factor activity.

### Interactions and contextual chemistry

Ten direct structural/assembly protein-binding contexts are refined to
GO:0046982 protein heterodimerization activity. Live QuickGO defines it as binding
a nonidentical protein to form a heterodimer. Screening-partner names alone are
not used for that refinement.

Supported generic interactions are retained as non-core under the user's ClinGen
policy. AHSP is the alpha-chain chaperone, while alpha-globin is its client.
Endothelial CYB5R3 and NOS3 interactions do not make alpha-globin a reductase or
establish direct inhibition of NOS3 catalysis. Live IntAct PSICQUIC queries on
2026-11-14 independently verified the publication-linked P69905 pairs for
PMIDs:16169070, 25416956, 29997244, 32296183 and 37398436, including all eight
partners in the 32296183 contexts. Example query:
https://www.ebi.ac.uk/Tools/webservices/psicquic/intact/webservices/current/search/query/id%3AP69905%20AND%20pubid%3A32296183?format=tab25&firstResult=0&maxResults=100
Interaction identifiers are recorded in the relevant review reasons.

PMID:19740759 supports Hb-Hp peroxidase chemistry and reports “induce intracellular
oxidative stress” and “Hb-Hp aggregates cause cytotoxicity to macrophages”. The
peroxidase, peroxide-response/consumption, haptoglobin binding and inflammatory
contexts remain non-core, with both native `contributes_to` qualifiers preserved.
The IEA inference from peroxidase activity to protective cellular oxidant
detoxification is marked over-annotated. Consuming peroxide does not necessarily
reduce its biological toxicity under the experimental conditions.

Extracellular and endosomal scavenging locations are retained as contextual
locations, without implying secretion, membrane insertion or a role in the
proteolytic machinery that consumes hemoglobin. GO:0005576 remains current;
GO:0005615 is obsolete in the live ontology and is not proposed as a refinement.

### Ten unresolved contexts

- PMID:12072504: the complete cached paper includes human hemoglobin experiments,
  but binding assays concern E7 mRNA. E7 protein is a translation readout, and
  mechanistic mapping uses rabbit alpha-globin/cytokeratin 7. The native E7-protein
  partner is preserved with UNDECIDED; no rabbit-only or wrong-gene allegation is
  made and no human alpha-chain RNA activity is inferred from whole-Hb assays.
- PMIDs:25156257 and 40205054: AHSP association is established independently, but
  the specific source-linked assertions were not reconstructed. The former
  accessible abstract foregrounds HSP70; the latter specific pair was not found
  in the available full text or queried interaction records. Neither establishes
  a citation error.
- PMIDs:6683087 and 9441940: the accessible abstracts do not expose the specific
  binding experiments. Their titles or emphasis do not justify rejecting the
  curators' full-text judgments.
- PMID:8292032: the abstract establishes heme-NO binding; directed NO transport
  remains unresolved. Scavenging, binding, generation and transport are distinct.
- PMIDs:19946888, 20458337, 23533145 and 22516433: the exact protein/peptide evidence
  for the membrane, exosome and blood-microvesicle contexts was not recovered.
  These four remain UNDECIDED rather than accepting an unverified localization or
  alleging contamination. One full article was accessible, but its HBA1-specific
  supplementary identification was not.

### Endothelial chemistry and processing boundaries

PMID:23123858 supports human and mouse endothelial alpha-globin expression and
redox-sensitive NO availability. PMID:28800253 includes human pulmonary endothelial
cocultures and lung tissue, alongside mouse vascular experiments. PMID:30295646
separates purified-protein redox interactions from mouse knockout physiology.
PMID:36302779 explicitly assays purified human alpha-globin with nitrite; its
vascular knockout/exercise evidence is mouse. Oxygenated NO scavenging and
deoxygenated nitrite reduction are distinct chemical contexts. These observations
inform the biological description and questions; no unsupported NO-transport
replacement or extra process annotation is manufactured.

The UniProt hemopressin segment is residues 96–104, PRO_0000455882, PVNFKLLSH.
PMID:18077343's accessible abstract identifies the rat sequence PVNFKFLSH.
PMID:20505104 tests the human/mouse-sequence nine-mer pharmacologically in rodents;
therefore sequence mismatch does not dismiss every nine-mer study. Neither
establishes an endogenous human appetite or pain-regulation function.
PMID:22952224 identifies longer pepcans in human plasma and reports negative
allosteric modulation; PMID:19380512 identifies extended mouse-brain peptides and
reports agonist effects in its assays. Peptide length, sequence and assay context
must remain explicit. Structured processing records separate the mature carrier
from the annotated internal peptide, and the knowledge gap concerns physiological
human nine-mer abundance and activity. No acid-extraction-artifact claim is made.

### Family evidence and source preservation

Native InterPro fetching initially stopped with a transient 503 after a partial
membership result. The native retry completed all 41 pages: 810 unique reviewed
members including P69905. The family prose is marked unchecked machine-generated
by its source and is not used as scientific evidence. The official PANTHER family
name is HEMOGLOBIN FAMILY MEMBER; SF48 is HEMOGLOBIN SUBUNIT ALPHA.

Existing PAINT 19.0 source caches were reused. The native slice contains 412 mapped
nodes and eight IBD assertions. Six positive IBDs at PTN000154218 match all six
seeded IBA contexts; TreeGrafter maps that node to PTHR11442:AN0. The P69905 leaf
rows use HBA2, consistent with the shared protein record. Human self-inclusion is
legitimate descendant evidence, not circular support. The newer PAINT donor/date
fields do not replace original GOA fields. No NOT was found in the retained family
slice/closure, but finer topology was not retrieved from the live tree service;
no unverified loss boundary is claimed. GO:0031721 on other family nodes is not
transferred to P69905. The retained GO-CAM index contained no P69905 match.

All source caches were produced by native tools or retained byte-for-byte from
Git. No UniProt, GOA or publication body was hand-edited. Supporting snippets are
matched to retained text with whitespace normalization. Formal schema, ontology,
reference, quote, history and rendering checks follow this draft.

### Completed local checks

Schema/ontology validation passed with 16 expected warnings for supported generic
protein binding retained under the user exception. Reference validation checked
94 snippets and 43 titles with no issues; 54 non-PMID snippets were skipped there
and were included in the independent quote check, which verified all 148
occurrences with zero unchecked. Canonical rendering succeeded in memory without
writing an HTML file or performing graphical inspection. Independent scientific
QA found no material blockers and prompted a wording correction so the knowledge
gap does not presuppose endogenous human nine-mer occurrence.

The extracellular-term replacement is also documented in upstream
[GO issue31545](https://github.com/geneontology/go-ontology/issues/31545),
[the March ontology commit](https://github.com/geneontology/go-ontology/commit/f297a4aea51f48e1023f76e53fecf89a179f95c9),
and [the April removal of the outdated recommendation](https://github.com/geneontology/go-ontology/commit/1fb09f6d67dbaa312ac6c4616263a6c180ac098c).
Older local ontology tables or annotation rows are not evidence that the former
term remains current.
