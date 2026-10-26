# Bacterial 2,3-butanediol and acetoin catabolism audit

## 2026-10-26 — comparative audit begins

The starting module describes an optional butanediol oxidation followed by E1 cleavage/reductive lipoyl acetylation, E2 acetyl transfer to CoA and E3 lipoyl reoxidation. Its representatives mix KT2440, PpG2, Cupriavidus H16 and Pelobacter proteins, and most individual steps and all three connections lack direct literature evidence. The initial five KT2440 reviews need a full audit; the cross-taxon representatives need their own individual reviews. An AcoL from Pelobacter must not be presented as the identified native E3 of KT2440.

Boundary questions to resolve from sources:

- Which named native complexes are fully characterized, and which KT2440 activities remain orthology-based? A broad family with representative examples does not restrict the selected protein to those examples.
- Which butanediol stereoisomers and pyridine-nucleotide cofactors are measured for each enzyme? Biosynthetic reduction and physiological catabolic oxidation must remain distinct claims even when chemically reversible.
- Does the E1 assay establish reductive lipoyl acetylation or only activity with artificial DCPIP? The alpha and beta subunits contribute to the assembled activity.
- Which E3 is experimentally linked to a native system? A ubiquitous lipoamide dehydrogenase reaction does not identify its physiological complex partner.
- AcoX/PP_0556 remains accessory context until direct biochemical evidence establishes its role; a locus association or necessity phenotype cannot manufacture a catalytic function.

Literature searches on 2026-10-26 found the integrated review PMID:17558661, Acetoin metabolism in bacteria; the stereochemistry review PMID:37644496; primary PAO1 catabolism PMID:30058099; a Bacillus subtilis primary study at DOI:10.1128/jb.181.12.3837-3841.1999; and 2026 KT2440 engineering work PMID:42046433, DOI:10.1021/acssynbio.6c00243. The latter may clarify native deletion phenotypes, but heterologous production enzymes are not automatically native pathway members. Retrieval and full-text assessment are in progress; search summaries alone are not annotation evidence.

The audit uses a separate worktree based on main 77121ffa32. One annotation reviewer owns the existing KT2440 panel and verified PpG2 comparators. A second owns Cupriavidus/Pelobacter components and assesses whether a Bacillus implementation adds meaningful taxonomic coverage. Module edits will follow the source-level boundary decision.

## 2026-10-26 — comparative mechanism and stereoisomer audit

The former mixed-species E1/E2/E3 chain is replaced by four native alternatives.
Direct Pelobacter reconstitution is distinguished from native Bacillus genetics
and H16/Pseudomonas component inference. The H16/Pseudomonas lipoyl-plus-hydrolase
AcoC architecture differs from canonical E2; no common catalytic fold is assumed.
KT2440 and H16 E3 identities remain required unresolved roles. A foreign AcoL
cannot silently supply the native complex.

Three reviews and eight primary references now have manual assessments and 22
mined findings. Evidence is attached to every activity and connection, including
cofactor regeneration and the optional entry reactions. The direct KT2440 PP0552
study closes the old stereochemistry/cofactor gap: R,R/meso substrates and NAD,
with no detected NADP activity in its Table 2. The same paper supplies native
S,S entry evidence for PedE/PedH, so the audit expands to these two members rather
than omit a known alternative. Its reversed lanthanide-switch sentence is flagged;
original metal/switch experiments and the source's own growth results govern the
interpretation. Both PQQ entry roles require metal/expression/electron-transfer
context; neither a native cytochrome partner nor acetoin transporter is assigned.

Independent scientific QA corrected an absence claim about inaccessible PpG2
assays and caught the primary-alcohol scope of GO:0052934. Secondary butanediol
oxidation uses GO:0016614 with specific reaction descriptors. Twenty-seven route
and condition cases pass, including mixed-species negatives and metal-dependent
entry checks. These predicates test modeled evidence coverage, not native flux.

Normal module deep-research attempts failed with provider authentication/quota
errors. Manual literature retrieval and normally fetched sources supply the
curation; no provider report was authored by hand. The completed original
18-member panel preserves 59 original rows with three justified AcoB MF
contributions. PedE/PedH extend the intended panel to 20; their final validation
and repository-wide validation are recorded when completed.

All twenty member reviews are now complete: 83 original rows are preserved and
three AcoB MF contributions bring the final panel to 86. Two inherited proposals
are explicitly retired without deleting their historical payloads. Forty raw
source-file hashes are preserved, including the canonical PedE directory rename.
Full repository validation started once on the stable panel (session 40946,
`acetoin-validate-all.log`) and is still pending; no PR has been opened.

The verified Bacillus AcoL placement in PTHR22912:SF219 exposed an omission in
the existing family review. Primary architecture evidence and explicit PAINT
inheritance from the already curated PTN000530299 support adding SF219 only to
E3 chemistry and FAD scopes. No other partner-complex use or new ancestral node
is inferred. The exact subfamily grounding is retained rather than weakened.
