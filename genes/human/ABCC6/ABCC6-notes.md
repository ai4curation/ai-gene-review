# ABCC6 functional annotation review

## Scope and evidence access

Human ABCC6/MRP6 is UniProt O95255. This is a new review of all 69 seeded GOA
annotations, preserving their terms, references, evidence codes, qualifiers,
partner IDs and alternative-product records. Annotation-reviewer and
core-function-synthesizer procedures were applied. No NEW assertion is added.

Primary publication records were fetched by the supported repository tooling.
PMIDs 11880368, 12414644 and 12901863 are abstract-only but explicitly report the
positive human-protein assays used below. PMID:24277820 remained abstract-only
after XML/HTML/PDF retrieval attempts; source-specific intracellular-phosphate
inference is consequently left unresolved. Other mechanistic papers noted as
full text below were read in the machine-generated cache. No cache, GOA,
UniProt record or provider report was hand-edited.

## Canonical transport and physiological substrate

[PMID:11880368](https://pubmed.ncbi.nlm.nih.gov/11880368/) expressed full-length
human ABCC6 in Sf9 cells and measured membrane ATP binding and ATP-dependent
transport of leukotriene C4 and N-ethylmaleimide-glutathione. PXE variants
retained MgATP binding but lost measured conjugate transport. Its abstract
states: "human ABCC6 is a primary active transporter for organic anions."
[PMID:12414644](https://pubmed.ncbi.nlm.nih.gov/12414644/) independently reports
human MRP6-mediated glutathione-conjugate/BQ123 transport in CHO vesicles and
limited resistance to several anticancer agents. These establish catalytic
capability, not the principal endogenous cargo. Drug resistance and leukotriene
transport are retained as contextual functions. The older ARA sequence in
PMID:8912525 was partial; its small predicted size is not full-length ABCC6
architecture.

[PMID:24277820](https://pubmed.ncbi.nlm.nih.gov/24277820/) explicitly reports
ABCC6-dependent nucleotide release while distinguishing that result from direct
NTP transport. [PMID:24969777](https://pubmed.ncbi.nlm.nih.gov/24969777/), read in
full, combines inducible **rat** ABCC6 in human HEK293/HeLa cells, **mouse**
hepatocytes/liver perfusion, and **human** patient plasma PPi. ATP is largely
converted within the liver vasculature to AMP and PPi. The investigators could
not demonstrate NTP transport in vesicles and allow missing cofactors or an
indirect ATP-release route. Therefore the existing ATP-transport **process**
rows remain valid for ABCC6-dependent release, without manufacturing a direct
ATP-transporter molecular function. ATP used as energy and ATP released as a
metabolite are distinct claims.

## PPi, phosphate and mineralization

[PMID:28592560](https://pubmed.ncbi.nlm.nih.gov/28592560/) was read in full,
including patient fibroblast, conditional mouse and biochemical results.
ABCC6 affects the extracellular nucleotide/PPi system, and patient cells show
changes in ENPP1, CD73 and TNAP. The paper proposes possible AMP secretion and
explicitly says PPi secretion is not directly inferred from the data. These
hypotheses are not established ABCC6 cargo identities. Changes in expression of
those enzymes do not make ABCC6 a transcription/translation component, and
extracellular metabolites do not place ABCC6 protein in extracellular space.
The corresponding gene-expression and extracellular-region rows are marked
as over-annotated on this full-source assessment.

QuickGO donor tracing of mouse Q9R1S7 recovered:

| Human propagated process | Mouse experimental source | Assessment |
|---|---|---|
| Inorganic diphosphate transport | PMID:28701330 IDA/IMP | Oral absorption/rescue does not assign the PPi transport step to ABCC6 |
| Intracellular phosphate homeostasis | PMID:24277820 IMP | Relevant full-text experiment inaccessible; UNDECIDED |
| Response to magnesium / sodium phosphate | PMID:24732453 | Combined dietary challenge; contextual phenotype |
| Phosphate homeostasis | PMIDs 28652107, 28701330 plus human-derived 28592560 | PPi/mineralization is not a measured phosphate-ion steady state |
| Calcium homeostasis | PMIDs 24732453, 28701330, 28592560 | Deposition phenotype does not separately establish calcium-ion steady state |
| Inhibition of non-skeletal mineralization | PMIDs 24732453, 28652107 | Conserved central physiological role |

[PMID:28701330](https://pubmed.ncbi.nlm.nih.gov/28701330/) directly studies oral
PPi uptake and protection from calcification, including in Abcc6-deficient
mice. Neither oral absorption nor rescue establishes ABCC6-mediated movement
of PPi. The propagated PPi-transport row therefore has a source-level role
conflation. [PMID:24732453](https://pubmed.ncbi.nlm.nih.gov/24732453/) uses a diet
simultaneously enriched in phosphate and reduced in magnesium. Its compared
groups have unchanged serum calcium, phosphate and PPi despite substantial
nephrocalcinosis; this is not a direct ABCC6 ion-transport assay. Both calcium-ion and phosphate-ion homeostasis are marked as over-annotated: deposition/PPi readouts do not separately establish a free-ion steady-state mechanism.

[PMID:28652107](https://pubmed.ncbi.nlm.nih.gov/28652107/) shows that human ENPP1
expression normalizes the Enpp1 mouse phenotype but does not completely rescue
Abcc6-deficient mice despite increased plasma PPi. Together with local-cell
results in PMID:28592560, this bounds any claim that circulating PPi alone
explains every manifestation. The core anti-mineralization role remains strong.
The ortholog record contains independent mouse experiments as well as transfers
from human; it is not labeled circular merely because a human source appears.

## Localization, alternatives and disease

[PMID:12901863](https://pubmed.ncbi.nlm.nih.gov/12901863/) establishes basolateral
human ABCC6 in polarized MDCKII host cells. Full
[PMID:23625951](https://pubmed.ncbi.nlm.nih.gov/23625951/) independently uses
native human/mouse liver sections, multiple antibodies and compartment markers
to localize full-length ABCC6 to basolateral membrane, challenging an earlier
MAM assignment. [PMID:35307651](https://pubmed.ncbi.nlm.nih.gov/35307651/) directly
identifies human MRP6 at Sertoli basal membranes and peritubular myoid cells.

The short URG7 alternative product O95255-2 differs substantially from the
canonical transporter. The abstract of
[PMID:23912081](https://pubmed.ncbi.nlm.nih.gov/23912081/) explicitly demonstrates
ER localization and N-lumen/C-cytosol topology in HepG2 expression/mapping
experiments. Its proposed anti-apoptotic partner-retention mechanism is not
promoted to a new GO function. The ER mapping is retained as non-core and
explicitly scoped to URG7; the unflagged original GOA tuple is preserved.
Canonical ABCC6 may also transit the ER during biosynthesis: the isoform scope
is not a claim that full-length protein can never enter the ER.

[PMID:10835642](https://pubmed.ncbi.nlm.nih.gov/10835642/) identifies human PXE
mutations. [PMID:22209248](https://pubmed.ncbi.nlm.nih.gov/22209248/) establishes
overlap between GACI and PXE, including biallelic ABCC6 cases. Monoallelic
findings in some patients are not used to assert dominant causation. The
standalone description focuses on biallelic disease and the transport/PPi
mechanism, not treatment recommendations or clinical-trial status.

## Partner-specific PDZ source audit

The full [PMID:36115835](https://pubmed.ncbi.nlm.nih.gov/36115835/) paper and
publisher **Supplementary Dataset 1** were inspected directly. This study assays
10-residue peptides and isolated PDZ domains, not simply intact proteins in
cells. The ABCC6 entry is `O95255`, peptide `YRLAQESGLV`, residues 1494–1503.
Its complete source has 133 assayed domains. Results for all 22 seeded partner
proteins are in [ABCC6-pdz-source-audit.tsv](ABCC6-pdz-source-audit.tsv).

Primary workbook:
https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-022-33018-0/MediaObjects/41467_2022_33018_MOESM4_ESM.xlsx

SHA-256: `ada912921164f0a79630c6a714b9ff264a7217ad3e646153ef498eb456206795`.
Sheet `PDZ-PBM interactome`; row numbers in the audit are one-based Excel rows.
Columns identify `PDZ`, `PBM`, `PBM_uniprot`, `natural_10mer`, assay intensities,
and `COMP_neglogKd`. The legend defines COMP as the affinity from the most
reliable holdup method. The source was read with openpyxl in read-only/data-only
mode; only the first 36 substantive columns are needed.

Five GOA partner proteins have quantified positive domains:

| Partner | Dataset domain | Row | Composite pKd |
|---|---|---|---|
| DLG4/P78352 | DLG4_2 | 16646 | 3.54875336 |
| PDZK1/Q5T2W1 | NHERF3_1 | 12780 | 3.76290369 |
| MAGI2/Q86UL8 | MAGI2_4; MAGI2_5 | 10921; 15495 | 3.88906699; 3.60702952 |
| PDZD3/Q86UT5 | NHERF4_1 | 17477 | 3.50938756 |
| WHRN/Q9P202 | DFNB31_3 | 10236 | 3.94072220 |

These five protein-binding rows are MODIFY to GO:0030165, PDZ domain binding.
The live QuickGO definition is binding to a PDZ domain. No full-length cellular
complex, physiological partner necessity, or new trafficking process is inferred.
[PMID:24840500](https://pubmed.ncbi.nlm.nih.gov/24840500/) shows that ABCC6 tail
deletions affect stability/localization, but does not identify which of the
screened partners mediates that phenotype.

The remaining 17 partners have only zero composite pKd entries among the
assayed domains. The study explicitly distinguishes measurable affinity from
values below quantification, and finite domain coverage cannot exclude binding
by an untested domain or in another context. These are **UNDECIDED**, not
universal negative-binding assertions and not a generic-term penalty.

For comparison, the IntAct PSICQUIC primary export was retrieved on 2026-09-26:
https://www.ebi.ac.uk/Tools/webservices/psicquic/intact/webservices/current/search/query/id:O95255?format=tab27

Filtering its MITAB field 9 for PMID:36115835 yielded 121 records; their negative
flags are all `false`, and most carry `kd:1.0x10(molar)` rather than a quantified
micromolar affinity. The TSV preserves matching IntAct/IMEx IDs. For example,
WHRN record EBI-67080694 / IM-30294-20660 carries 114.624591252214 µM, matching
its positive workbook result. GRID2IP records EBI-67692406 / EBI-67898890 and
MAGI1 records EBI-67480403 / EBI-67730683 carry the 10-molar representation while
the corresponding source-domain values are zero. This is a concrete unresolved
export/threshold issue, not evidence that all these intact proteins never bind.
The original GOA IPI evidence/partner tuples remain unchanged. No automatic
annotation was rewritten from these database flags.

## Research provenance and checks

The Falcon request ran concurrently with publication caching, with a 1200-second
timeout. It completed successfully in **776.51 seconds** and produced the
unaltered report, source artifact and image. No Perplexity retry was attempted
because the coordinator had already established insufficient quota. The report
was read in full; its ATP-release/direct-substrate distinction is corroborated
by primary sources. Its unidentified-journal citation, trial-status claims and
absence-of-structure claim are not independent primary evidence and were not
adopted. It remains UNVERIFIED as an evidence source rather than being inserted
into annotation quotes solely to remove a validation advisory.

Live QuickGO definitions were checked for the proposed PDZ term, ABC mechanism,
ATP/PPi transport, phosphate/calcium homeostasis and anti-mineralization. All
23 propagated rows have source_entities; IBA entries use their ancestral PTN
identifiers, not donor counts. The 69 original annotation tuples compare equal
to the deterministic seed. Targeted validation passes with one intentional
unused-provider-report advisory. The coordinator's repository baseline passed
4,975 reviews; shared project tracking remains coordinator-owned.

The publisher's [December 2022 correction](https://www.nature.com/articles/s41467-022-35177-6)
was also inspected. It repairs omitted or misplaced figure labels/legends in
Figures 2, 4 and 5; it does not report a replacement of the affinity workbook
or resolve the zero-affinity export issue described above.

### Independent review follow-up

The coordinator independently inspected all 69 decisions and flagged the initial
asymmetry between non-core calcium homeostasis and over-annotated phosphate
homeostasis. Reinspection of the full PMID:28592560 source recovered calcification,
micro-CT and calcium-phosphate deposition endpoints, not a distinct free-Ca-ion
steady-state measurement. PMID:24732453 measures acid-extracted deposited calcium
and unchanged serum Ca/Pi. Live GO:0055074 and GO:0055062 have parallel steady-state
ion definitions. Both calcium rows are therefore now MARK_AS_OVER_ANNOTATED,
without denying their well-supported mineralization phenotype; the initial calcium
NON_CORE assessment is superseded. Source explanations were also tightened so ARA
partial-sequence, PAINT and mutant-Reactome caveats appear only on their relevant
rows.
