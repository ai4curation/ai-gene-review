# MYF5 curation notes

Deep-research provider status: all API-backed providers were unavailable in this
workspace, and the installed `claude_code` provider failed with `Not logged in`.
The review therefore uses cached GOA PMIDs, Reactome summaries, UniProt, and
manual reading recorded here rather than a generated
`MYF5-deep-research-<provider>.md` file.

MYF5 is the human `PTHR11534:SF3` member of the PANTHER myogenic-factor family.
The fetched PAINT slice has no IRD/IKR loss on the human MYF5 lineage. Its IBA
rows come from the same core myogenic-factor gains used for MYOD1 and MYOG:
`PTN000164853` carries the nuclear and Pol II DNA-binding transcription-factor
functions, and `PTN000164854` carries skeletal-muscle differentiation and the
RNA polymerase II transcription regulator complex.

The reviewed UniProt MYF5 record is a compact source for the human protein's
myogenic transcription-factor biology: it describes MYF5 as a muscle-specific
target-gene activator involved in muscle differentiation and notes that efficient
DNA binding requires dimerization with another bHLH protein. Conerly et al. give
the best mechanistic split from MYOD1: Myf5 binds the same genome-wide E-box
sites as MyoD but weakly induces the shared target genes and instead primes
bound loci by inducing local histone H4 acetylation [PMID:26906734, "Myf5
induces local H4Ac, despite its lack of transcriptional induction"]. The early
human MYF5 cDNA paper, PMID:2721498, is cached only as an abstract, so the
review keeps the old TAS developmental rows but does not build new claims from
the unread full text.

PMID:19829708 directly reports DUX4c/MYF5 co-immunoprecipitation in an FSHD
study. That supports a physical interaction but not a stable MYF5 molecular
function beyond a generic protein-binding edge, so the row is removed under the
bare-protein-binding policy.
