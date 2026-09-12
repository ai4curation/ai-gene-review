# DHODH (human, UniProtKB:Q02127) — review notes

Reviewed GO annotations for human **DHODH** — dihydroorotate dehydrogenase (quinone),
mitochondrial (EC 1.3.5.2; PYRD_HUMAN). Grounded in the cached UniProt record
(`DHODH-uniprot.txt`), the seeded GOA (`DHODH-goa.tsv`), cached `publications/PMID_*.md`,
cached Reactome entries, and the pre-existing `DHODH-deep-research-falcon.md` (generated
2025-12-27; falcon is currently out of credits so no new deep-research run was made).

## Verified biology
- Class 2 (type 2) flavoenzyme; catalyses the **4th and only mitochondrial step** of de
  novo pyrimidine biosynthesis: FMN-dependent oxidation of **(S)-dihydroorotate → orotate**,
  passing electrons to **ubiquinone** [file:human/DHODH/DHODH-uniprot.txt "Reaction=(S)-dihydroorotate + a quinone = orotate + a quinol"; EC=1.3.5.2].
- Cofactor **FMN**, 1 per subunit [file:... "Name=FMN; Xref=ChEBI:CHEBI:58210"; PMID:10673429].
- Kinetics of recombinant human enzyme: Km 4 µM (DHO), 9.9 µM (ubiquinone-50)
  [PMID:8925840 "Km values for dihydroorotate and ubiquinone-50 were found to be 4 microM and 9.9 microM"].
- **Mitochondrion inner membrane**, single-pass; catalytic TIM-barrel domain faces the
  intermembrane space; N-terminal helices form the lipophilic ubiquinone/inhibitor tunnel
  [file:... "Mitochondrion inner membrane"; PMID:10673429 "an alpha-helical domain that forms the opening of a tunnel"].
- Disease: **Postaxial acrofacial dysostosis / Miller syndrome** (MIM:263750), biallelic
  loss-of-function [PMID:19915526 via UniProt DISEASE].
- Drug target: leflunomide/teriflunomide (A77 1726, IC50 ~1 µM), brequinar
  [PMID:8925840 "An IC50 value of 1 microM was determined for A77 1726"].
- Ferroptosis: DHODH reduces ubiquinone to ubiquinol in the IMM as a parallel
  (GPX4/FSP1-independent) radical-trapping antioxidant defence [PMID:33981038].

## Curation decisions of note
- **GO:0004151 dihydroorotase activity (IEA, GO_REF:0000107 Ensembl Compara)** → **REMOVE**.
  This is a *different* enzyme (EC 3.5.2.3, the DHO domain of trifunctional CAD, step 3 of
  the pathway). DHODH is EC 1.3.5.2 (step 4). Clearly-wrong orthology-transfer IEA (mouse
  ortholog O35435 mis-mapped). Endorsed by task brief.
- **GO:0005737 cytoplasm (IEA, InterPro IPR005720)** → **REMOVE**. Domain-based electronic
  inference mislocalising a strictly IMM-anchored protein whose catalytic domain faces the
  intermembrane space. (HPA reports a cytosol IDA in the UniProt DR block, but that is not
  in the GOA TSV under review.)
- **GO:0005515 protein binding (IPI ×2, PMID:32296183 HuRI)** → both **MARK_AS_OVER_ANNOTATED**
  (NOT removed, per curation policy for bare protein-binding IPIs). WITH/FROM P49638 (TTPA)
  and Q6ZMZ0 (RNF19B); both are single high-throughput Y2H interactions, uninformative and
  unvalidated. The seeded review only had one GO:0005515 entry; added the second GOA row.
- Generic parents (GO:0016020 membrane, GO:0016491 oxidoreductase activity, GO:0016627
  oxidoreductase acting on CH-CH) → **MARK_AS_OVER_ANNOTATED** (more specific terms present).
- **NEW** annotations added (not in GOA): GO:0010181 FMN binding (structural + fluorimetric
  evidence), GO:0048038 quinone binding (ubiquinone tunnel), GO:0110076 negative regulation
  of ferroptosis (Mao et al. 2021 Nature).

## Reference-format housekeeping
- Converted all UniProt supporting_text from `reference_id: UniProt:Q02127` to the
  `file:human/DHODH/DHODH-uniprot.txt` convention and added a matching top-level references
  entry. Trimmed four UniProt quotes that had combined non-adjacent `CC` lines so each is
  now a genuine verbatim substring of the record.
- All PMID/DOI supporting_text verified verbatim (whitespace-normalized) against cached
  publications. Reactome titles left exactly as fetched.

Final: `just validate human DHODH` → ✓ Valid.
