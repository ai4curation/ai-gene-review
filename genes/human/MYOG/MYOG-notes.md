# MYOG curation notes

Deep-research provider status: all API-backed providers were unavailable in this
workspace, and the installed `claude_code` provider failed with `Not logged in`.
The review therefore uses cached GOA PMIDs, Reactome summaries, UniProt, and
manual reading recorded here rather than a generated
`MYOG-deep-research-<provider>.md` file.

MYOG is the human `PTHR11534:SF5` member of the PANTHER myogenic-factor family.
The fetched PAINT slice has no IRD/IKR loss on the human MYOG lineage. Like the
other vertebrate myogenic bHLH factors, it inherits the broad `PTN000164853`
gains for nuclear Pol II DNA-binding transcription-factor biology. A more recent
MYOG-specific PAINT gain at `PTN002609884` supports positive regulation of
transcription by RNA polymerase II from mouse, chicken, rat, and human myogenin
seeds.

UniProt summarizes MYOG as a transcriptional activator for muscle-specific
targets, terminal myoblast differentiation, FACT recruitment, and late promoters
opened by MYOD1. It also records homodimerization and E12 heterodimerization as
the basis for MYOG DNA-binding and transcriptional activity. PMID:11076940
provides direct EMSA evidence that recombinant Myf4/myogenin and Myf6 bind the
novel GCCTGTCA cis-element in the human ACCbeta promoter.

Most MYOG protein-binding rows are large-scale IntAct imports from BioPlex or
HuRI-style screens. The exact interaction pairs are retained as UniProt
`CC:INTERACTION` evidence where present, but the GOA rows themselves are removed
because bare `GO:0005515` is not an informative GO molecular function for
myogenin. The single TCF12 row is refined to bHLH transcription factor binding.
