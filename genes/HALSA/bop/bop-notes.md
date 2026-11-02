# bop (bacteriorhodopsin, P02945, Halobacterium salinarum NRC-1) - review notes

Automated deep research was UNAVAILABLE for this gene (no `bop-deep-research-*.md`
was generated). These notes come from my own reading of the cached PubMed records
(`publications/PMID_*.md`, all abstract-only), the UniProt record (`bop-uniprot.txt`)
and QuickGO/OLS queries made on 2026-10-15.

## Gene product

- bop (VNG_1467G) encodes bacterio-opsin; with covalently bound retinal it forms
  bacteriorhodopsin (BR), the only protein of the purple membrane.
  [PMID:4517939 "The purple membrane of Halobacterium halobium contains only one protein,
  bacteriorhodopsin, which closely resembles the visual pigments of animals."]
- Precursor with a 13-residue N-terminal propeptide; mature chain 14-262 (UniProt).
  [PMID:6706999 "the precursor contains 13 additional amino acids at the NH2 terminus of
  bacteriorhodopsin"]
- Seven transmembrane helices; homotrimers packed into a 2D crystalline lattice (purple
  membrane) with lipids. [PMID:10452895 "Contacts between the trimers in the membrane plane
  are mediated almost exclusively by lipids."]
- Retinal is bound as a protonated Schiff base on Lys216 (mature numbering; Lys229 in the
  UniProt precursor numbering). [PMID:6794028 "the retinyl residue is covalently attached to
  Lys-216"]

## Function: light-driven outward proton pump

- Discovery of the pump: [PMID:4517939 "Starved or anaerobic cells containing purple
  membrane, in the absence of any apparent source of energy, generate and maintain a proton
  gradient across the cell membrane as long as they are exposed to light."]
- Photophosphorylation in vivo: [PMID:4524635 "These results indicate that the purple
  membrane functions as a lightdriven proton pump and the cells use the resulting
  chemiosmotic gradient for ATP synthesis."]
- Reconstitution with ATP synthase: Racker & Stoeckenius 1974 (PMID:4272126, title only in
  cache: "Reconstitution of purple membrane vesicles catalyzing light-driven proton uptake
  and adenosine triphosphate formation.").
- Mutagenesis of the proton path: [PMID:3288985 "The Asp-85----Asn mutant showed not
  detectable proton pumping, the Asp-96----Asn and Asp-212----Glu mutants showed less than
  10% and the Asp-115----Glu mutant showed approximately equal to 30% of the normal proton
  pumping."]
- Mechanism: [PMID:10949309 "Upon illumination, retinal is isomerized. The Schiff base then
  releases a proton to the extracellular medium, and is subsequently reprotonated from the
  cytoplasm."]; [PMID:10452895 "the proton acceptor Asp85"; "the proton donor Asp96"].
- Review: [PMID:14977418 "the proton transport cycle of the light-driven pump,
  bacteriorhodopsin"].

## Secondary role: photoreception via the proton motive force

- BR alone (in a strain lacking HR, SRI, SRII) supports phototaxis, but via Delta-mu-H+
  rather than a dedicated signalling partner. [PMID:8415720 "We conclude that the
  BR-mediated photoreception is due to the light-dependent generation of delta mu H+."]
  This is the only evidence I found that rescues GO:0007602 phototransduction; the cited
  paper for that row (PMID:4517939) describes energy conversion.

## Regulation (context, not annotated)

- bop is induced by low oxygen and light, under the Bat activator.
  [PMID:1856168 "bat gene expression is induced under conditions of low oxygen tension and
  the bat gene product activates bop gene expression"]; [PMID:11226271 "Halobacterium sp.
  NRC-1 can grow phototrophically by means of light-driven proton pumping by
  bacteriorhodopsin in the purple membrane."]

## GO landscape checks (QuickGO/OLS, 2026-10-15)

- GO:0015454 light-driven active monoatomic ion transmembrane transporter activity is a
  leaf; there is no proton-specific child (no "light-driven proton pump" term). bop
  (FlyBase, IDA, PMID:4517939) is the ONLY annotation to GO:0015454 in all of GOA.
- No archaeal protein carries GO:0016918 retinal binding or GO:0009881 photoreceptor activity.
  Bovine RHO carries GO:0005502 11-cis retinal binding by IDA, so opsins do get retinal
  binding terms.
- No GO CC term for "purple membrane" exists (searched OLS/QuickGO).
- InterPro2GO maps IPR018229 (Rhodopsin_retinal_BS) to GO:0005216 monoatomic ion channel
  activity. This hits every microbial rhodopsin I checked: halorhodopsins P0DMH7, P15647,
  P33742, sensory rhodopsin II P42196 and proteorhodopsin Q9F7P4. None of these is a
  channel (channelrhodopsins are algal). Proteorhodopsin additionally gets GO:0010461
  light-activated monoatomic ion channel activity from IPR017402.
- GO:0042777 proton motive force-driven plasma membrane ATP synthesis: experimental
  annotations are on ATP synthase subunits (plus Pyrococcus mbh subunits); the proton
  pump that generates the gradient is conventionally not annotated, so I do not propose it
  for bop.

## Decisions (summary)

- REMOVE GO:0005216 channel (bR is a pump).
- ACCEPT plasma membrane (EXP, IEA) and GO:0015454 (IDA, core).
- MODIFY membrane -> plasma membrane; ion transport / ion transmembrane transport ->
  GO:1902600 proton transmembrane transport.
- KEEP_AS_NON_CORE phototransduction (secondary photoreception via PMF, PMID:8415720).
- NEW: GO:0015078 proton transmembrane transporter activity (IDA, PMID:3288985);
  GO:0016918 retinal binding (IDA, PMID:6794028).
- Proposed new terms: light-driven proton transmembrane transporter activity; purple
  membrane (CC).
