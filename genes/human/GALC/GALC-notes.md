# GALC (Galactocerebrosidase / Galactosylceramidase) review notes

UniProt: P54803 (GALC_HUMAN); HGNC:4115; EC 3.2.1.46; gene on chr14.
Glycosyl hydrolase family GH59 (CAZy GH59; Pfam PF02057).

## Core biology (verified)

GALC is a **lysosomal glycosidase** of glycosphingolipid catabolism. It hydrolyses the
terminal galactose from **galactosylceramide (galactocerebroside)** to yield **ceramide +
D-galactose** (EC 3.2.1.46, RHEA:14297), and also hydrolyses **galactosylsphingosine
(psychosine)** and other galactolipids.

- UniProt FUNCTION: "Hydrolyzes the galactose ester bonds of glycolipids such as
  galactosylceramide and galactosylsphingosine" ... "responsible for the lysosomal
  catabolism of galactosylceramide, a major lipid in myelin, kidney and epithelial cells
  of small intestine and colon" [PMID:8281145, PMID:8399327].
- Gene-structure paper: "This enzyme catalyzes the lysosomal hydrolysis of specific
  galactolipids including galactosylceramide (galactocerebroside) and galactosylsphingosine
  (psychosine)" [PMID:7601472].
- Enzyme purified from human urine, EC 3.2.1.46, low abundance, acid pH optimum (4.0-4.4),
  KM=10 uM for N-acyl-beta-D-galactosylsphingosine [PMID:8399327].
- cDNA cloned + expressed in COS-1; N-terminal sequence from 51 kDa human brain band
  [PMID:8281145].

## Cofactor / mechanism

Requires **saposin A (SapA, from PSAP)** for lipid presentation. GALC-SapA crystal
structure (murine) = 2:2 heterotetramer; open channel from GALC active site to SapA
hydrophobic cavity presents the polar glycosyl headgroup to the active site while shielding
the acyl chains. "This enzyme requires the saposin SapA for lipid processing and defects in
either of these proteins causes a severe neurodegenerative disorder, Krabbe disease"
[PMID:29323104]. Active-site residues (UniProt): proton donor/acceptor His... actually
ACT_SITE 198 (proton donor/acceptor), 274 (nucleophile). GH59 retaining glycosidase.

## Localization

Lysosome / lysosomal lumen. GO IC annotations place it in endolysosome lumen (GO:0036021),
inferred from the general finding that endolysosomes are the principal sites of acid
hydrolase activity [PMID:27498570] combined with GALC's acid-hydrolase MF (GO:0004336).
PMID:27498570 is a general endolysosome study and does NOT mention GALC by name; the
endolysosome-lumen call is a curator inference (IC). Lysosome localization is well
established (subcellular location "Lysosome"; typical acid hydrolase, mannose-6-phosphate
pathway implied).

## Disease

Deficiency causes **Krabbe disease / globoid cell leukodystrophy (KRB; MIM:245200)**,
autosomal recessive. Psychosine (galactosylsphingosine) accumulation is neurotoxic and
drives demyelination. Many pathogenic missense variants across the gene (UniProt lists
dozens of KRB variants). Four clinical forms; infantile form ~90% of cases.

## Annotation review decisions

GOA MF term present and current: **GO:0004336 galactosylceramidase activity** (verified via
OLS, not obsolete). This is the core MF used in core_functions.
Core BP: **GO:0006683 galactosylceramide catabolic process** (verified current).
Locations: **GO:0005764 lysosome**, **GO:0043202 lysosomal lumen** (both verified current).

Notes on individual annotations:
- PMID:15657896 is a *review* on GALC in cancer, annotated IDA to GO:0006683. IDA on a
  review is unusual, but it does correctly describe GALC degrading galactosylcerebroside to
  ceramide. Not a core-defining primary experiment; keep as non-core / accept the biology
  but flag the evidence type. Per policy do NOT REMOVE (can't see full curator context) —
  accept the biology, note the review nature.
- GO:0030149 sphingolipid catabolic process (IDA, PMID:8281145): broader parent-type BP;
  GALC does act in sphingolipid catabolism (galactosylceramide is a glycosphingolipid).
  Keep as non-core (galactosylceramide catabolic process is the precise term).
- GO:0046479 glycosphingolipid catabolic process (TAS, Reactome): correct, broader than the
  precise galactosylceramide catabolic process; keep as non-core.
- Reactome/GO_REF/IEA/ISS/IBA MF and BP annotations all consistent; accept.

## Deep research

Falcon deep research is OUT OF CREDITS (HTTP 402) — no -deep-research-falcon.md generated.
Review grounded in GALC-uniprot.txt, GALC-goa.tsv, and cached publications/PMID_*.md.


## 2026-11-02 — source-context and enzyme-mechanism review

The preceding text is an unchanged historical journal. Its older numerical kinetic statements and quote-to-claim associations are not automatically adopted. The current [source guide](GALC-source-guide.md) records what was actually read and the review YAML contains the present judgments.

Positive human purification and COS-1 expression support GALC's defining galactosylceramidase function. Cat RNA in the cloning workflow was only a probe intermediate. Full original assay Methods were not recovered, so numerical pH/Km details are omitted from current reasons ([PMID:8281145](https://pubmed.ncbi.nlm.nih.gov/8281145/), [PMID:8399327](https://pubmed.ncbi.nlm.nih.gov/8399327/)). The human gene paper supports established lysosomal hydrolysis as background; it is not a direct imaging assay ([PMID:7601472](https://pubmed.ncbi.nlm.nih.gov/7601472/)).

Selected GALC-SapA original text supports an acidic-compartment lipid-presentation mechanism. The principal structure uses mouse proteins, with a separate limited human pull-down; substrate placement is modeled rather than resolved in that complex. General hydrolase-active endolysosome physiology supports the IC location without pretending that GALC itself was imaged. A single precise endolysosome-lumen core avoids repeating its ancestor compartment ([PMID:29323104](https://pubmed.ncbi.nlm.nih.gov/29323104/), [PMID:27498570](https://pubmed.ncbi.nlm.nih.gov/27498570/)).

All 20 current contexts are retained. The 19-row parser forecast collapses the unextended activity assertion and a separately assigned three-atom substrate/product context. The planned twentieth row restores that existing context, not a new assertion, and leaves the unextended row intact. The original two assignments, literal conjunction and old mapping ambiguity remain explicit. The current InterPro reference differs from an older combined-inference reference; both are preserved in their respective versions.

The three actual IBA placements descend from the verified ancestral node. Mouse donor papers provide positive cDNA-expression and mutant biochemical grounding, with abstract-only access limits retained; a donor's title foregrounding SapA does not demonstrate a curator error ([PMID:8769874](https://pubmed.ncbi.nlm.nih.gov/8769874/), [PMID:11371512](https://pubmed.ncbi.nlm.nih.gov/11371512/), [PMID:11734583](https://pubmed.ncbi.nlm.nih.gov/11734583/)). The primary catalytic and pathway claims remain independently supported in human.

The current four products have exact official sequences of 685, 662, 659 and 589 residues. Sequence verification does not prove equivalent activity or trafficking. Historical 669-residue cDNAs, alternative initiation and protein fragments are not silently assigned current suffixes ([PMID:8297359](https://pubmed.ncbi.nlm.nih.gov/8297359/), [PMID:9434153](https://pubmed.ncbi.nlm.nih.gov/9434153/)). Variant-expression studies corroborate activity sensitivity but do not create extra biological processes or product equivalence.

Two source inconsistencies are explicitly recorded: Reactome's modeled glucose output disagrees with the same reaction's galactose definition, and UniProt's ester-bond phrase disagrees with glycosidic chemistry. The model's human GALC identity and lumen assignment remain verified; all fetched source bytes are preserved. Eight current excerpt occurrences are checked against retained source bytes. All 30 inherited associations remain historical provenance. No NEW annotation, provider report or canonical acquisition has been generated during this private review. Genuine native acquisition, context restoration and targeted validation remain future work.

## 2026-11-02 — genuine native reconciliation

The authorized existing lane refreshed GALC with the native no-seed command while preserving the inherited review. All 20 original contexts and every field of the 16-column export matched the retained current records. Fourteen normal sources were reused unchanged and 19 missing publications were acquired, completing the 33-source union. The genuine native 19-row seed is preserved separately without edits. Its collapsed activity pair is represented here as two original contexts: raw3 remains unextended at review1; raw4 is restored at review19 with its exact substrate/two-product conjunction. This is source-context restoration, not a NEW annotation. Explicit joins supplement the strict matcher, which does not check assignedBy or extension identity.

All four native product declarations and sequences agree; source titles and availability flags were reconciled, and all eight current excerpts match the actual normal caches. PMID:20886637 and PMID:34449528 now have full caches, but their manual assessments retain the actual abstract reading scope. PMID:8940268 remains abstract-only after failed publisher-restricted XML/HTML/PDF fallbacks. The 20 approved judgments, one core, 36 manual assessments, two source defects and all 30 historical quotation associations remain intact. Native EDIT history and targeted validation follow.

## 2026-11-02 — targeted checks and finalization

Native validation passed with zero advisories; strict GOA matching passed, and computed status is COMPLETE for all 20 reviewed original contexts. No NEW annotation was added. The first validation diagnostic is preserved: three extension predicates initially used descriptive objects, while the schema requires CURIE strings. Only those wrappers were projected to their exact RO identifiers; labels and the literal source conjunction remain in the archive. All 33 scientific source files remain unchanged. The initial INITIALIZED-versus-COMPLETE status diagnostic is retained. Native EDIT history, private rendering/link checks and scoped whitespace checks accompany this candidate.

## 2026-11-02 — retain informative lysosome annotations

The explicit root-organelle policy includes lysosome and prohibits replacing a supported organelle claim with a subcompartment. The three lysosome rows (IBA, UniProt location mapping and TAS) are therefore retained as ACCEPT. Their source-specific evidence remains unchanged. The IBA placement is sound, so the previous granularity-failure classification is withdrawn. Existing lysosomal-lumen and endolysosome-lumen annotations, the precise core location, all original contexts and the eight current excerpts remain intact. This corrects the policy application in the preceding dated review; the earlier journal and history remain unchanged. The current tally is 18 ACCEPT and two MODIFY, with the latter confined to broad catabolic-process refinements. Target validation passed with zero advisories, strict GOA matching passed for all 20 original contexts, and computed status remains COMPLETE. A genuine new EDIT history, private rendering/link checks and scoped whitespace checks passed; all 33 scientific sources and the complete context/evidence archive remain unchanged.


## 2026-11-02: substrate breadth and curated-source follow-up

The earlier two process refinements are superseded: both broad sphingolipid and glycosphingolipid catabolism are retained because the curated human record covers both GalCer and psychosine hydrolysis (UniProt P54803, CC:CATALYTIC ACTIVITY, RHEA:14297 and RHEA:43908; PMID:8399327). Production GO-CAM 696022cd00002259 explicitly includes the GALC activity under sphingolipid catabolism with PMID:8281145. Its deliberate context is now acknowledged, and the independent second substrate supplies the reason the broader terms remain informative. The GalCer-specific MF core is not relabeled as psychosine activity; an expert/ontology question records that separate reaction.

The authentic original abstract remains the inspected scope for PMID:8399327. This does not invalidate curated UniProt kinetic and acid-pH evidence. The N-acyl substrate Km and pH optimum are now distinguished from original full-Methods verification, and a short record-section-labelled pH excerpt supports the acid-hydrolase setting. The FUNCTION chemistry defect is represented as WRONG_STATEMENT/CHECK with its full sentence, preserving all source bytes. Reader-facing identifiers and spacing were corrected; no historical journal or history record was rewritten.

The source archive now exposes the exact GO-CAM activity and retains all 20 originals, the separate restored three-atom context, four sequences and 30 historical quotation associations. Current support has nine excerpt occurrences; the additional full UniProt sentence is counted separately in the same source quotation budget. Target validation passed with zero advisories, strict GOA matching passed for all 20 original contexts, and computed status remains COMPLETE. The genuine EDIT history, private render/link checks and scoped whitespace checks passed. All 33 scientific sources and every original machine context remain unchanged. The first follow-up check caught a scalar record_section where the schema requires a list; the scalar was normalized to a one-item list, then the string was explicitly quoted for YAML parser compatibility. Both diagnostics are preserved. The pH wording, source and scientific judgments did not change.
