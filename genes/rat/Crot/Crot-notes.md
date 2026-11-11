# Crot notes

- UniProtKB:P11466 states: FUNCTION: Beta-oxidation of fatty acids. The highest activity concerns the C6 to C10 chain length substrate. [UniProtKB:P11466].
- Core interpretation: peroxisomal medium-chain acyl-CoA transfer to carnitine during fatty acid beta-oxidation.
- Accepted direct GO terms include: carnitine O-octanoyltransferase activity, carnitine metabolic process, fatty acid beta-oxidation, medium-chain fatty acid metabolic process, medium-chain fatty acid transport.
- Non-core/context terms are mostly localization, binding/cofactor, inferred pathway context, or exposure-response annotations; generic parent terms are modified when a specific catalytic term is available.

## Re-review 2026-10-10

GOA changes: three new ISO rows from human CROT (UniProtKB:Q9UKG9) for GO:0005777 peroxisome, GO:0006631 fatty acid metabolic process and GO:0008458 carnitine O-octanoyltransferase activity, donor-splits of existing mouse-Crot (MGI:1921364) ISO rows. No retired rows. 32 rows total.

- PENDING resolved: all three human-donor ISO rows ACCEPT, each with a propagation_review naming the human donor.
- GO:0005777 peroxisome (IBA, IEA, ISO, IDA PMID:6630173): KEEP_AS_NON_CORE -> ACCEPT. Peroxisome is the defining location [PMID:6630173 "COT was found in peroxisomes and the soluble compartment but not in mitochondria"; PMID:7495866 "a C-terminal peroxisomal targeting sequence (Ala-His-Leu)"]; added as core-function location.
- GO:0009410 response to xenobiotic stimulus (IDA PMID:11023836): kept MARK_AS_OVER_ANNOTATED with a precise reason. The paper shows that COT is the target of etomoxir [PMID:11023836 "is irreversibly inhibited by the hypoglycaemia-inducing drug etomoxir"], which is not a response process carried out by Crot.
- GO:0071874 cellular response to norepinephrine stimulus (HEP PMID:14618266): kept MARK_AS_OVER_ANNOTATED; the evidence is microarray co-clustering only.
- The UniProt FUNCTION quote ("Beta-oxidation of fatty acids. The highest activity concerns the C6 to C10 chain length substrate.") is still present in the refreshed flat file (checker reports 0 stale). On the localization and experimental rows it was replaced with the SUBCELLULAR LOCATION line or with paper quotes, because it does not support those claims.
- Description rewritten as standalone biology. Status COMPLETE.

Open question (now also in `suggested_questions`): the transport annotations (GO:0001579 accepted, GO:0015908 MODIFY to it; GO:0015909 now MARK_AS_OVER_ANNOTATED, see 2026-10-17 follow-up) treat acylcarnitine formation as part of medium-chain fatty acid transport out of peroxisomes. That matches the TAS source wording, but the membrane carrier that moves the acylcarnitine is a different protein.

Review follow-up 2026-10-17 (PR #4619):
- The carnitine metabolic process (GO:0009437) and coenzyme A metabolic process (GO:0015936) rows (ISS, ISO) now cite the UniProt reaction "Reaction=octanoyl-CoA + (R)-carnitine = O-octanoyl-(R)-carnitine + CoA;" instead of the generic FUNCTION quote.
- Long-chain fatty acid transport (GO:0015909, TAS PMID:11790793) went from MODIFY -> GO:0001579 to MARK_AS_OVER_ANNOTATED. The long-chain half of the source sentence describes CPT I. GO:0001579 is a sibling term that the gene already carries from the same paper. Purified COT is active up to C20 [PMID:6630173], so the row is marked rather than removed.
- The conflict over malonyl-CoA is now recorded. PMID:6630173 has a finding "Malonyl-CoA inhibited CPT but not COT." with finding_review DISPUTED, superseded_by PMID:11790793.
- The open question about the acylcarnitine carrier was moved to suggested_questions.
