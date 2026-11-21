# PR6138 evidence follow-up

The review identified a real inconsistency between the two FliI reviews and
several places where the supporting evidence was weaker than the claim. The
corrections distinguish these from disagreements resolved by current ontology
definitions. Original annotation payloads, ordering and prior NEW proposals are
preserved; only review judgments, synthesis and source assessments change.

## Independently supported FliI claims

Salmonella FliI retains ATP hydrolysis (GO:0016887) and membership of the type III
secretion system complex (GO:0030257) as ACCEPT. The current GO graph does not
make the transport activity GO:0008564 a descendant of the ATP-hydrolysis term,
nor the flagellar secretion apparatus GO:0120102 a descendant of that complex.
The two supported claims therefore remain alongside the other terms, consistent
with the E. coli review. This is not an assertion that the transport activity
lacks ATP hydrolysis: its definition explicitly consumes ATP and water.

E. coli FliI self-association remains ACCEPT because oligomerization is part of
the functional ATPase ring. Core synthesis now states that relationship. The
independent mechanistic evidence is attributed to its Salmonella experiments;
it is not represented as a recovered E. coli interaction table. The unresolved
source-specific IPI evidence and the integrated conserved-function judgment
are recorded separately.

## Chemotaxis: motor execution versus apparatus construction

Chemotaxis requires movement guided by a chemical concentration gradient.
Neither generic swimming nor an inability to construct a flagellum alone
establishes that process. The three export-component claims (ECOLI FliI,
SALTY FliJ and PSEPK FliJ) are now MARK_AS_OVER_ANNOTATED: the cited sources
identify export and assembly work, without identifying these proteins as
executing propulsion, steering or gradient-dependent motor regulation. This
does not claim that every possible secondary role has been disproved.

The stators are different: they perform the mechanical work while the motor
executes the chemotactic response. Their KEEP_AS_NON_CORE decisions now have
positive gradient context, rather than resting on generic movement alone:

- PMID32766440 directly measures KT2440 responses in chemical gradients and
  identifies run-time bias in the wrapped mode. PMID36409076 independently
  connects MotAB loss to wrapped-mode/motor-bias changes and shows that MotCD
  can support wrapped mode under increased load. These are complementary
  studies, not a single stator-specific gradient experiment.
- MotCD deletion leaves liquid swimming speed unaffected but promotes sessile
  clustering. Its reduced semisolid spreading must not be presented as a
  chemotaxis defect; the conditional motor contribution is a separate inference.
- PMID27439872 measures Vibrio alginolyticus YM4 in microfluidic gradients while
  varying sodium-dependent swimming performance. PMID17376072 establishes
  CheY-controlled polar-motor behavior. These support a species-level PomA
  mechanical-effector inference, not a PomA gradient-knockout assay or direct
  CheY binding to PomA. YM4 is not silently equated with the selected reference
  or structural construct. The full PMC methods of PMID27439872 were read;
  the immutable local cache remains abstract-only.

The FliG chemotaxis decision remains ACCEPT with the explicit comparative
CheY-P/FliM/FliN-to-FliG switching quotation restored. Its rotor–stator interface
quotation is also restored. Domain and residue numbering stays attributed to
the comparative source, rather than being reassigned to KT2440.

The UNDECIDED enum permits general evidential uncertainty and additionally
requires that action when relevant publications cannot be accessed. The export
decisions change because the sources support an assembly assignment rather
than guided-movement participation, not because UNDECIDED is restricted to
inaccessible sources.

## Current ontology and specificity

Current QuickGO places GO:0140605 under GO:0003774, whose definition explicitly
includes electrochemical-gradient-powered flagellar rotation. The FliF/FliG
refinements therefore remain, with the verified ancestry stated explicitly.
The older rationale describing the wrong kind of motor would be incorrect.
The contribution of an assembled rotor is not autonomous proton translocation.

GO:0009422 is not a descendant of extracellular region GO:0005576. FlgK/L
reasons now call this an anatomical replacement without claiming ontology
ancestry. In contrast, hook GO:0009424 does descend from bacterial flagellum
GO:0009288; that refinement remains valid.

Salmonella FliJ synthesis now separates its FlhA export-gate activation from
its specific enzyme-activator role in promoting the FliI ATPase ring. The latter
is GO:0008047 and has an explicit stimulation quotation from PMID21934659.
Neither core assigns ATP hydrolysis to FliJ. The existing NEW activator row is
preserved and its target boundary is explained.

## Descriptions and reference findings

FlgB/C/F and FlgD descriptions are standalone biological summaries; evidence
and cross-species limitations remain in reasons and reference assessments.
Unused PMID39766194 findings were removed from FlgD/FliG because the selected
quotation did not identify either protein. Missing spaces were corrected in
reviewer-authored prose without modifying quotations or raw sources.

Focused checks and renewed full validation must cover the revised science
before it is published. The earlier full run remains historical evidence for
the earlier revision, not a substitute for the new run.
