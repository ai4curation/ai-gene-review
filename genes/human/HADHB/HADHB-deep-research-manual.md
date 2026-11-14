# HADHB: targeted evidence reconciliation

Reviewed 2026-11-12 for human HADHB, UniProt P55084. This supplements the
unchanged, previously generated Falcon report. It is a manual source assessment.

## Catalytic specificity

The human liver preparation in [PMID:1550553](https://pubmed.ncbi.nlm.nih.gov/1550553/)
shows activity on C6 and longer substrates but no detectable C4 activity. The
C10–C16 maximum described in that abstract concerns the dehydrogenase assay;
it is not an exclusive substrate boundary for HADHB. Human subunit expression
in [PMID:8135828](https://pubmed.ncbi.nlm.nih.gov/8135828/) assigns thiolase to
beta and hydratase/dehydrogenase to alpha. Patient-complex destabilization can
reduce all three activities without transferring the alpha catalytic sites to beta.

The newer [PMID:31980458 full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC7049979/)
reports a contrasting recombinant-protein experiment. Its Methods state:
“Thiolase activity of HADHB was measured using acetoacetyl-CoA and CoASH as substrates”.
The human HADHB reagent was commercial AdooQ AP4092; no added HADHA was described.
The assay followed substrate absorbance at 303 nm, with 100 micromolar of each
substrate and 10 nM HADHB. The reported apparent turnover was approximately
2 per second. Main-text controls included viperin titration and a viperin mutant;
they did not supply a HADHB catalytic mutant, saturation kinetics across chain
lengths, or orthogonal product identification. Supplementary material was not
inspected. Neither preparation-specific result is silently discarded. The review
leaves the specific C4 function UNDECIDED and asks for matched comparative assays.
The local PMID cache remains abstract-only despite normal fetch and provider-chain
attempts; this short Methods quotation was checked in the primary full-text page.

QuickGO distinguishes [GO:0003985](https://www.ebi.ac.uk/QuickGO/term/GO:0003985)
(the C4 reaction) from [GO:0003988](https://www.ebi.ac.uk/QuickGO/term/GO:0003988)
(general 3-oxoacyl-CoA thiolysis). The condensation direction used in these
definitions does not invalidate physiological reverse thiolysis. The C16 reaction
GO:0050633 is a supported capability, not an exclusive substrate requirement.

## RNA and inflammatory context

[PMID:32513690](https://pmc.ncbi.nlm.nih.gov/articles/PMC7322040/) studies mouse
macrophages and lncFAO. It supports RNA association and metabolic involvement in
late LPS responses, with Hadhb knockdown and lncFAO epistasis affecting inflammatory
transcripts. Its acetoacetyl-CoA assay uses cell lysates and cannot alone identify
which thiolase produces the signal. Official QuickGO donor records link the mouse
Q99JY0 annotations for lncRNA binding, gene expression and LPS response to this paper.

[PMID:41816300](https://pmc.ncbi.nlm.nih.gov/articles/PMC12972699/) studies human
THP-1-derived macrophages and MALAT1. Its RIP-based association and cell-level
metabolic/perturbation measurements are relevant, but the authors explicitly
acknowledge that direct, specific RNA–protein binding is unestablished. FAOBlue
fluorescence should not be described as purified HADHB turnover. No new immune
process, RNA-binding core function or specific MALAT1 affinity is asserted here.

## Location and provenance limits

The abstract of PMID:21527675 describes viperin redistribution. It does not establish
HADHB ER topology, fractionation outcomes, an import intermediate or an infection
requirement for every curated location. ER and outer-membrane annotations are
left UNDECIDED without those extra claims. The abstract of
PMID:18063578 discusses nucleoid-associated metabolic proteins collectively; it
does not establish HADHB-specific cross-linking results. The nucleoid row remains
UNDECIDED pending the relevant target-specific results.

The GO:0044877 transfer traces to rat Q60587 and PMID:20132223, a
PPARalpha/peroxisomal thiolase study. The explicit peroxisomal identity and
antibody-peptide comparison contradict the HADHB donor assignment. Remove the
derived human IEA while retaining a CHECK/PROBABLE source-defect request.
Selecting a unique replacement is unnecessary for rejecting this transfer;
this does not assert that HADHB cannot bind protein complexes.

The source-identity check used official UniProt sequences on 2026-11-12:

| Protein | Antibody peptide core VHGRRTPIGRAGRGG | FASTA SHA256 |
|---|---|---|
| [Rat HADHB Q60587](https://rest.uniprot.org/uniprotkb/Q60587.fasta) | Absent; residues 41–56 are TKSKKTLAKPNLKNIV | `ca223afbc71cc93ee2b5a3c58c7dcfc97e93dcb23252df50e6b5e6e1151f88f0` |
| [Rat ACAA1b P07871](https://rest.uniprot.org/uniprotkb/P07871.fasta) | Matches residues 41–55 | `8c7596779b77216eae3d8ad4c7ad83b18d7e7e9cb4373142ea6de1032a35ff83` |
| [Rat ACAA1a F1LPD6](https://rest.uniprot.org/uniprotkb/F1LPD6.fasta) | Matches residues 51–65 | `cec96de2e3169ce37bad86a8a19fd24c0d825a3158b01b02131c37855d1efef1` |

The paper reports a terminal cysteine beyond this core; its origin is not assumed.
This comparison supports a probable mapping problem, not a unique corrected donor.

## Scope and source checks

The refreshed QuickGO file contains 63 rows. Seeding preserves six older contexts,
giving 69 review entries; none is deleted merely because it disappeared from the
new export. The six absent records carry `retired: true` and retain their original
review blocks as historical judgments, including superseded reasoning; the current
biological synthesis does not endorse that reasoning. Source term IDs, evidence codes, references, qualifiers and supporting
entities are preserved. No new annotation is proposed.

The PAINT-loss helper used the retained IBD cache (SHA256
`0c672914e10c1f79d3fb365077d843a92e518eb6eee2aac00c67150274adf569`)
and a freshly fetched compact PTHR18919 tree. No IRD/IKR loss was reported on
P55084's lineage in these inputs. This does not establish the state of later unseen
PAINT updates, nor justify inventing a pruning node for the uncertain C4 reaction.

## 2026-11-14 UTC — Review follow-up

The inspected official [mouse Rsad2/Q8CBB9 record](https://www.uniprot.org/uniprotkb/Q8CBB9/entry)
classifies the partner as a radical-SAM enzyme with CTP-dehydration activity
(RHEA:65944). This supports enzyme binding without transferring human
construct-specific kinetics. Positive mouse lncFAO association evidence is now
quoted alongside the distinct human MALAT1 direct-binding limitation.

Native UniProt curates RHEA:18161:
`Reaction=tetradecanoyl-CoA + acetyl-CoA = 3-oxohexadecanoyl-CoA + CoA;`
This supports all six current GO:0050633 rows. Its reaction list contains C6 and
longer 3-oxoacyl-CoA reactions but no acetoacetyl-CoA/two-acetyl-CoA reaction.
That records coverage, not proved curator rejection or universal C4 inactivity.

Both IEA and both IDA disputed compartment rows remain UNDECIDED. Absence of
annotated SIGNAL/TRANSMEM features does not exclude peripheral recruitment.
Official PMC ID conversion found no PMCID for PMID:21527675; Europe PMC reports
no PMC/open-full-text record. An indexed original-paper passage mentioning
inner/outer membrane detection and Fig. S11 is a lead only: neither the full
article nor that figure was retrieved or inspected. No cleavage or import
mechanism is asserted.
