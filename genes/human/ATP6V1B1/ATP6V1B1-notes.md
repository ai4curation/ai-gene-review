# ATP6V1B1 (V-type proton ATPase subunit B, kidney isoform; VATB1_HUMAN, P15313)

## Summary

ATP6V1B1 encodes the B1 (kidney/tissue-restricted) isoform of the non-catalytic B
subunit of the V1 peripheral domain of the vacuolar H+-ATPase (V-ATPase). The V1
domain hydrolyzes ATP, and this chemical energy drives proton translocation through
the membrane-embedded V0 domain, acidifying intracellular compartments and, in
specialized cells, the extracellular space.

## Core identity and function

- Non-catalytic V1 subunit: "Non-catalytic subunit of the V1 complex of vacuolar(H+)-
  ATPase (V-ATPase), a multisubunit enzyme composed of a peripheral complex (V1) that
  hydrolyzes ATP and a membrane integral complex (V0) that translocates protons"
  [UniProt P15313 FUNCTION, "Non-catalytic subunit of the V1 complex of vacuolar(H+)-ATPase"].
- The B subunits form three AB catalytic heterodimers that constitute the V1
  heterohexamer: "The V1 complex consists of three catalytic AB heterodimers that form
  a heterohexamer" [UniProt P15313 SUBUNIT]. B subunits hold non-catalytic nucleotide
  (ATP) sites; UniProt annotates an ATP-binding residue at position 394 (by similarity
  to P21281) [UniProt P15313 FT BINDING 394 "ligand=ATP"].
- Essential for assembly/activity: "Essential for the proper assembly and activity of
  V-ATPase" [UniProt P15313 FUNCTION].
- Renal proton secretion: "In renal intercalated cells, mediates secretion of protons
  (H+) into the urine thereby ensuring correct urinary acidification" [UniProt P15313
  FUNCTION].

## Structural / complex membership (V1 domain)

- Cryo-EM of complete human V-ATPase places B subunits in the V1 ATP-hydrolytic head:
  "V-ATPases ... comprised of a cytoplasmic V1 complex for ATP hydrolysis and a
  membrane-embedded Vo complex for proton transfer... The V1 ATPase is composed of
  three copies of subunits A, B, E, and G, and one copy of subunit C, D, F, and H"
  [PMID:33065002 "The V 1 ATPase is composed of three copies of subunits A, B, E, and G"].
  This is the IDA support for GO:0000221 (V-ATPase V1 domain).

## Disease and physiology

- Loss-of-function mutations cause autosomal recessive distal renal tubular acidosis
  with sensorineural deafness (DRTA2): "mutations in ATP6B1, encoding the B-subunit of
  the apical proton pump mediating distal nephron acid secretion, cause distal renal
  tubular acidosis... Patients with ATP6B1 mutations also have sensorineural hearing
  loss; consistent with this finding, we demonstrate expression of ATP6B1 in cochlea
  and endolymphatic sac" [PMID:9916796].
- Mechanism of disease variants — assembly and apical trafficking defects:
  "GFP-B1WT formed complexes with other H+ -ATPase subunits (c, H, and E), whereas
  GFP-B1M did not. Proteins that were immunoprecipitated... from GFP-B1WT cells had
  ATPase activity, whereas proteins from GFP-B1M cells did not. Proton pump-mediated
  intracellular pH transport was inhibited in GFP-B1M-transfected cells... B1 point
  mutations prevent normal assembly of the H+ -ATPase and also may act as an inhibitor
  of H+ -ATPase function by competing with endogenous intact H+ -ATPase for trafficking"
  [PMID:16769747]. This grounds: V-ATPase complex assembly (GO:0070072), proton
  transmembrane transport (GO:1902600), pH reduction (GO:0045851), apical plasma
  membrane localization (GO:0016324).
- Renal acid secretion / urinary acidification (regulation of pH, renal tubular
  secretion): "Defects in the B1 subunit gene ATP6V1B1... cause rdRTA with deafness...
  apical H(+)-ATPase that cause rdRTA" [PMID:12414817].
- Hearing: clinical genetic studies link ATP6V1B1 mutations to early-onset
  sensorineural hearing loss and enlarged vestibular aqueduct (EVA):
  "Mutations in ATP6V1B1 are associated with early onset SNHL... confirms the
  association of EVA and mutations in the ATP6V1B1 gene" [PMID:19639346]; "a significant
  percentage of the children with DRTA had sensorineural hearing loss and mutation in
  ATP6V1B1 gene" [PMID:20622307].

## Localization / tissue specificity

- Apical membrane in kidney intercalated cells and early distal nephron (TAL, DCT):
  "the B1 subunit is expressed in the apical membrane domains of TAL, macula densa, and
  DCT in human and rodent kidney. Furthermore, by immunoelectron microscopy the subunit
  is localized to the apical plasma membrane in the DCT" [PMID:29993276]. Apical
  localization also documented in [PMID:16769747] ("GFP-B1WT and GFP-B1M are present in
  the apical membrane").
- Tissue-restricted: kidney/testis (mouse) and cochlea/endolymphatic sac; murine
  ortholog 93% identical: "Northern blotting detects a 2.2-kb Atp6v1b1 transcript in the
  kidney and testis, but not other major organs. In mouse kidney, the B1-subunit
  localizes to intercalated cells" [PMID:14585495]. The human ISS localization
  annotations (cytoplasm, microvillus, basolateral/lateral membrane) are transferred
  from this mouse ortholog (Q91YH6).
- HPA: "Group enriched (kidney, salivary gland)" [UniProt P15313 DR HPA].

## PDZ interactions / apical targeting

- C-terminal PDZ-binding motif (residues 510–513) mediates interaction with NHERF1 and
  the bicarbonate transporter SLC4A7/NBC3: "The PDZ-binding motif mediates interactions
  with NHERF1 and SCL4A7" [UniProt P15313 DOMAIN]; "Forms a complex with NHERF1 and
  SCL4A7" [UniProt P15313 SUBUNIT]. Mutagenesis L513G abolishes these interactions
  [UniProt P15313 FT MUTAGEN 513]. (Primary ref PubMed:12444018 not cached locally; the
  interaction is documented in the UniProt record.)

## Notes on weaker / peripheral annotations

- GO:0005515 protein binding (IPI, PMID:32814053): bare "protein binding" from a
  large-scale neurodegeneration interactome screen (IntAct pairwise hits with ATXN1,
  TARDBP, WFS1, HSPB1, etc.). Uninformative for molecular function; the biologically
  meaningful binding (PDZ→NHERF1/SLC4A7, AB hexamer assembly) is captured by complex
  membership and domain annotations.
- GO:0070062 extracellular exosome (HDA; PMID:23533145, PMID:19199708, PMID:19056867):
  proteomic detection in urinary/parotid/prostatic-secretion exosomes; consistent with
  V-ATPase delivery to/recycling from the apical plasma membrane but a bystander
  localization, not a core function.
- GO:0016241 regulation of macroautophagy (NAS, PMID:22982048): the cited paper is
  about lipofuscin formation in senescent fibroblasts being independent of
  macroautophagy/lysosomal activity; weak NAS link, V-ATPase-driven lysosomal
  acidification supports autophagy generally but this is a generic V-ATPase property,
  not specific to the B1 subunit. Non-core at best.
- GO:0001503 ossification (IMP, PMID:16433694): the cited paper is a clinical genetics
  study of dRTA/deafness families (rickets noted as a downstream consequence of
  acidosis); not direct evidence that B1 functions in ossification. Over-annotation /
  indirect.
- GO:0055074 calcium ion homeostasis (IMP, PMID:20622307): the cited paper is a
  hearing-loss clinical correlation report; no direct calcium-homeostasis experiment.
  Likely downstream/indirect (urinary calcium handling in dRTA).
- GO:0016928804 (PMID:16928804): apical plasma membrane IDA — this paper is about RhCG
  ammonia transporter; H+-ATPase used only as a co-localization marker. Localization
  consistent but weak primary evidence for B1 specifically.
- Various IEA Ensembl orthology transfers (synaptic vesicle lumen acidification,
  extrinsic component of synaptic vesicle membrane, adult behavior, olfactory behavior,
  chloride/potassium/sodium homeostasis, prostaglandin metabolism, etc.) derive from
  rodent orthologs and broad V-ATPase biology; the B1 isoform is kidney/inner-ear/
  epididymis restricted, so neuronal synaptic-vesicle roles are properties of other B
  isoforms (B2) rather than B1. Treat as non-core / over-annotation.
- Reactome cytosol (TAS) annotations: generic "cytosol" placement for V1 subunits in
  many Reactome pathways; the V1 domain is cytoplasmic, so cytosol is acceptable but
  low-information and largely redundant.
