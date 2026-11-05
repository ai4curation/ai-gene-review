# DZA28_17840 (A0ABY3D9I3): notes for dashboard gene NZ_CP015876.1_2730

Dashboard: https://gene-annotate-dashboard.kbase.us/review/NZ_CP015876.1_2730 (P. putida
SJTE-1, tier B, "Prior-annotated", aux).
Mapping: the query is 98.8% identical (407/412, ungapped) to A0ABY3D9I3, from P. alloputida
B2017 (UniRef90_A0A7L9GCG7). The exact UniParc entries were deleted. In SJTE-1 the query is
A210_RS13675 / WP_014756724.1, and its RefSeq translation is identical to the dashboard
sequence.
Analysis: BERIL run `20261030T213529Z-dza28-17840-domains-homology-context`
(`DZA28_17840-bioinformatics/`, `just all`). All numbers below come from `results.json`.

## Conclusion

This is an uncharacterized polytopic inner-membrane protein. Its molecular function and
biological process are unknown.

- **Domains.** A divergent MgtC/SapB/SrpB/YhiD N-terminal domain (PF02308, residues 11-129) is
  fused to DUF4010 (PF13194, residues 177-387).
  - The PF02308 score is 58.3. The same model scores 136.0 on Salmonella MgtC, 131.5 on E. coli
    YhiD and 117.8 on M. tuberculosis MgtC.
  - The protein lacks the cytoplasmic C-terminal domain of canonical MgtC.
- **MgtC family.** Salmonella MgtC is not a Mg2+ transporter. It is a virulence factor that binds
  the a subunit of F1Fo ATP synthase and inhibits it (PMID:23827679). This protein shares only
  about 31% identity with it over about 220 residues. That activity, and the "Mg2+ transport"
  label carried by COG3174 and STRING, should not be transferred.
- **Closest studied relative.** This is P. aeruginosa PA0043 (Q9I789): 42.0% identity over 362
  residues, phmmer E = 8.4e-35. It is the dashboard's "34.3%" PaperBLAST homolog.
  - Lee et al. 2016 (PMID:27150578) found PA0043 alleles (Trp4Arg, Gly35Stop) in
    in vitro-evolved colistin-resistant lineages. They call it a hypothetical protein of unknown
    function, and MICs changed little in the deletion mutants.
  - This is a phenotype association, not a function.
- **Topology.** DeepTMHMM predicts 13 TM helices (5 in the MgtC-N module and 6 in DUF4010) and
  no signal peptide. Phobius (UniProt) predicts 7.
- **Genomic context (SJTE-1).**
  - The gene is directly downstream of the Crp/Fnr-family regulator fnrC on the same strand,
    with a 16-bp overlap, so the two are probably co-transcribed. STRING links the 90%
    homolog to a Crp/Fnr regulator too.
  - Universal stress protein genes are nearby, and so is the paa phenylacetate cluster.
  - There is no integrase, transposase, phage gene or tRNA within 25 kb. Gene GC is 60.6%
    against a CDS mean of 61.8% (z = -0.3).
  - So there is no genomic-island signature. The gene is nonetheless accessory: phmmer in the
    mapping step found no homolog in KT2440, NBRC 14164, P. putida UP000218731 or
    P. plecoglossicida.
  - In the homologs' neighbourhoods (P. fluorescens N2C3 and N2E2), a cation-transporting P-type
    ATPase sits next to the gene. This is weakly reminiscent of the mgtCB pairing. It is
    context only.

## Dashboard verdict

Recommended verdict: **supported**. Corrected annotation:

> Uncharacterized integral inner-membrane protein, MgtC N-terminal domain (divergent) fused
> to DUF4010; molecular function unknown.

- The architecture and topology are right. The call correctly refuses to transfer Mg2+
  transport, Sap peptide uptake or colistin resistance.
- Quibbles:
  - "substrate undetermined" implies a transporter, which nothing supports. The canonical
    family member is a protein-protein inhibitor, not a transporter.
  - The call does not mention that the canonical MgtC C-terminal domain is missing.
- GO:0005886 plasma membrane is **COR** (confidence 2). It is novel, because GOA is empty.

## Caveats

- There is no fitness data. This protein has no KT2440 homolog, so `fetch-fitness` has nothing to
  look up. It also failed independently: there is no FEBA mapping for 9PSED, and
  fit.genomics.lbl.gov returns 403.
- The dashboard JSON has no fitness phenotypes for any homolog. Its only Fitness Browser hit is
  Cupriavidus basilensis FW507-4G11 (39.7%, "hypothetical protein"), and no phenotype is
  shown.
- The 50%-identity homologs in the P. fluorescens and P. simiae Fitness Browser strains were
  not checked, because the Fitness Browser and BERDL are unreachable from here.
- The deep-research report guesses that a KT2440 ortholog probably exists. That is wrong (see
  the mapping above).
- The report also says Phobius gives 7 TM helices. DeepTMHMM gives 13.

## Tooling

- `just fetch-gene 9PSED DZA28_17840 --uniprot-id A0ABY3D9I3` worked for the 9PSED taxon
  without workarounds.
- `fetch-gene-pmids` found no PMIDs, because the UniProt entry cites none.
- `fetch-fitness` failed: there is no FEBA orgId for 9PSED, and the Fitness Browser returns 403.
- PaperBLAST web is behind a Cloudflare challenge. The colistin paper was identified from
  the dashboard summary text instead (PMID:27150578).
- No local BLAST or HMMER binaries were available, so pyhmmer and Biopython from the repo venv
  were used. The large downloads (the PAO1 proteome and the SJTE-1 GenBank) are re-fetched
  by `just fetch` and git-ignored.

## QC

`just validate` passed with 2 warnings: no core_functions, and the deep-research file is not
cited in an annotation. `validate-references`, `validate-terms`, `validate-predictions` (0
errors, 2 quotes verified) and `validate-history` all passed. `render` produced the HTML.
