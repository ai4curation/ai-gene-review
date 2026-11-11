# EBP source-audit results

The executed saved-input replay reads 596 IntAct records and selects 527 records from the two cited interaction studies: 524 HuRI records and 3 disease-variant-screen records. It reconstructs 172 review-source joins. Historical annotation 11 is the three-record CREB3 aggregate; annotation 12 retains the 524-record heterogeneous HuRI aggregate; annotation 13 requires the three literal EBP self-pair records. The remaining 169 pair rows keep their exact imported partner identities.

Of 1,054 selected interactor-side occurrences, 1,045 reproduce their literal ROGIDs: 1,042 from current official sequences and 3 from archived UniSave 253 SLC3A2 isoform4. Nine IntAct-only clone-side occurrences remain unresolved. The archived 661-aa SLC3A2 sequence is independently reconstructed, and its assayed 133–661 region equals current 529-aa isoform2. This resolves the historical label without replacing the imported accession or inferring full-fusion equivalence.

The 263-node PTHR14207 tree and 263-sequence MSA contain the exact 230-aa human EBP sequence at PTN002494278. The literal family IBD/IRD lines are retained with their target-path placement. IRDs on the EBPL branch do not lie on the EBP target path. Tree GO-slim display strings are not substituted for the original GAF assertions. Current donor scope is discussed in the source guide; a donor count is not a measure of phylogenetic evidence strength.

Both modeled Reactome reactions join through catalyst 195674 and entity 195697 to human Q15125 residues 2–230 at the ER membrane. Explicit substrates/products describe sterol Delta8-to-Delta7 chemistry even where the catalyst carries a broader or mismatched GO label. The companion term projection preserves the current exact definitions used in the review.

The 59 partner-class refinements are documented in [the manual classification table](partner-classes.md). The assay establishes association to an independently classified partner, not transfer of that partner's catalytic or signaling activity to EBP. Generic positive associations remain non-core under the explicit project policy when no warranted specific class was established.

The partner-class refinements describe the limited specificity of positive binding assays, not a ranking of physiological importance. Sterol-pathway partners such as ERG28 and INSIG2 remain positive non-core associations and motivate explicit follow-up questions and experiments. The core remains the directly established sterol-isomerase reaction.
