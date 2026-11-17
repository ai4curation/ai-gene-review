# PR6169 gene consultation: mapping scope and ImuA activities

## DnaE2 exonuclease inference

The 2026-11-07 InterPro API records identify IPR004805 as “Error-prone DNA polymerase/DNA polymerase III subunit alpha DnaE/PolC” and IPR011708 as “Bacterial DNA polymerase III, alpha subunit, NTPase domain”. Both descriptions discuss exonuclease activity of DNA polymerase III. The source identifiers for the existing GO:0008408 rows are IPR004805 and IPR011708 in CAUVC, PSEPK and MYCTU. That source trace identifies the inference under review; it is not biological evidence for the activity.

[PMID:20615954](https://doi.org/10.1073/pnas.1002614107), whose cached full text was reread, explicitly contrasts conserved exonuclease-associated residues in M. tuberculosis DnaE1 with missing key residues in its DnaE2. This demonstrates that nuclease chemistry cannot be assumed uniformly from these broad polymerase classifications. It does **not** establish the corresponding substitutions or a negative exonuclease assay in Caulobacter Q9A3J3 or Pseudomonas Q88I82. No target alignment or ancestral loss is claimed here.

The CAUVC/PSEPK rows therefore become MARK_AS_OVER_ANNOTATED: the mapping overstates what broad classification establishes. Their actual nuclease capacity remains unresolved. MYCTU already carries that action with additional target-specific published sequence evidence and remains unchanged. UNDECIDED is not restricted to inaccessible papers; the reviewer's categorical policy claim is incorrect, even though the mapping warning is warranted here.

The accepted DNA-polymerase inference is not based on the same evidence as the disputed nuclease subactivity. Specific DnaE2 assignment, target genetic context, conserved synthetic function and the mycobacterial catalytic-site experiment jointly support synthesis. The broad classifications span members with differing nuclease machinery. Error-prone behavior alone is not a reason to reject proofreading.

## Myxococcus ImuA inhibition and process participation

The full [2021 primary article](https://journals.asm.org/doi/10.1128/aem.00919-21) was independently reread, including Results and Figure 4. ImuA associates with RecA1, reduces new DNA–protein complex formation and inhibits RecA1-mediated joined-DNA formation. Preformed RecA-coated DNA did not show clear RecA dissociation after adding ImuA. Thus inhibition is supported; active filament dismantling is not established. The native genetic results support facilitation of mutagenic lesion bypass, while loss of ImuA does not abolish it. The unchanged publication cache remains abstract-only.

Current GO:0004857 enzyme inhibitor activity describes reduction of catalytic activity and fits the measured RecA1 inhibition. It supplies a supported regulatory core without a new GO proposal or annotation row. The existing lesion-bypass process association is placed on this regulatory core, together with negative regulation of DNA recombination. It is removed from the ATPase core: the protein's participation in lesion bypass does not establish that its measured ATPase cycle performs that particular step.

The full cached [2024 primary article, PMID:38591662](https://doi.org/10.1002/pro.4981) supports DNA-enhanced ATP hydrolysis and nucleotide-sensitive DNA binding. It describes assembly/disassembly interpretations as hypotheses. These measured activities remain separate cores; neither is erased because its mechanistic coupling is unresolved. No ImuA activity is transferred to divergent mycobacterial ImuA′.

## Additional 2024 construct-identity corroboration

The pre-existing 2021 promoter/genome/CDS sequence bridge remains unchanged in `myxococcus-consultation/RESULTS.md`. `verify_evidence.py` now independently parses the seeded Q1D5A2 sequence and checks:

- 290 residues and the UniProt sequence-record mass of 30,274 Da, matching the 2024 paper's rounded 30.3-kDa monomer;
- residues 71–72 are R,T, matching the experimentally tested positions;
- the reported 223–290 self-interaction interval ends at the actual sequence terminus.

These converging checks materially strengthen attribution of the 2024 observations to MXAN_3991/Q1D5A2. They are not an exact full-construct sequence match: the complete synthetic construct/accession was not supplied in the retrieved supplement. The interaction interval is an experimental mapping result, not a conserved sequence motif inferred from these checks.
