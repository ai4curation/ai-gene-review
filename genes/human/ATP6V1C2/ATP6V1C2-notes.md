# ATP6V1C2 (V-type proton ATPase subunit C 2) review notes

UniProt: Q8NEY4 (VATC2_HUMAN), 427 AA. Gene HGNC:18264, chromosome 2.

## Identity and family

- ATP6V1C2 encodes the "C" subunit of the V1 peripheral domain of the vacuolar
  H+-ATPase (V-ATPase), a multisubunit rotary proton pump. It is one of two human
  paralogs of subunit C (the other being ATP6V1C1) [file:human/ATP6V1C2/ATP6V1C2-uniprot.txt
  "Belongs to the V-ATPase C subunit family"].
- The protein was cloned as a tissue-specific isoform of the human V-ATPase C subunit
  [PMID:12384298 "Molecular cloning and characterization of novel tissue-specific
  isoforms of the human vacuolar H(+)-ATPase C, G and d subunits"].
- Two splice isoforms exist: Q8NEY4-1 (displayed, 427 AA) and Q8NEY4-2 (VSP_024883,
  residues 276-321 missing) [file:human/ATP6V1C2/ATP6V1C2-uniprot.txt ALTERNATIVE PRODUCTS].

## Molecular function and structural role

- Subunit C of V-ATPase sits at the interface between the catalytic V1 head and the
  membrane-embedded V0 sector, as part of/anchoring the peripheral stator stalk. UniProt:
  "Subunit C is necessary for the assembly of the catalytic sector of the enzyme and is
  likely to have a specific function in its catalytic activity"
  [file:human/ATP6V1C2/ATP6V1C2-uniprot.txt FUNCTION, By similarity to P21282/P21283/P31412].
- The V1 complex "consists of three catalytic AB heterodimers ... three peripheral stalks
  each consisting of EG heterodimers, one central rotor including subunits D and F, and the
  regulatory subunits C and H" [file:human/ATP6V1C2/ATP6V1C2-uniprot.txt SUBUNIT].
- Subunit C is a key regulator of reversible V1-V0 assembly/disassembly: it is released from
  both V1 and V0 when the holoenzyme disassembles, and re-binding of subunit C is required for
  reassembly (well established for yeast Vma5p and the mammalian ortholog; the human protein is
  annotated By similarity). This makes subunit C a regulatory hub for controlling V-ATPase
  activity in response to signals.
- The protein is a structural/regulatory subunit; it does not itself hydrolyze ATP or
  translocate protons, but participates in the rotary catalytic mechanism as part of the V1
  domain. GO_Central IBA assigns enables proton-transporting ATPase activity, rotational
  mechanism (GO:0046961) to the whole C-subunit family by descent
  [file:human/ATP6V1C2/ATP6V1C2-goa.tsv IBA GO_REF:0000033].

## Localization

- As a V1 subunit, it is cytosolic/peripheral-membrane-associated; the free pool of subunit C
  (after disassembly) is cytosolic [Reactome TAS GO:0005829 cytosol].
- Detected by proteomics in lysosomal membrane fractions of human placenta
  [PMID:17897319 "In membranes purified from placental lysosomes, we identified 58 proteins ...
  These included 17 polypeptides comprising or associated with the vacuolar adenosine
  triphosphatase"] - consistent with V-ATPase residing on the lysosomal/endolysosomal membrane.
- Detected in human urinary exosomes by large-scale proteomics
  [PMID:19056867 "we used LC-MS/MS to profile the proteome of human urinary exosomes ...
  identified 1132 proteins"] - a high-throughput catalog hit, not evidence of a primary
  exosomal function.

## Physiological roles / pathway context

- V-ATPase acidifies intracellular compartments (endosomes, lysosomes, Golgi, secretory
  vesicles) and, in some cells, the extracellular space; ATP6V1C2 contributes to this as a
  V1 subunit [file:human/ATP6V1C2/ATP6V1C2-uniprot.txt FUNCTION].
- V-ATPase-mediated acidification is required for Wnt/beta-catenin signaling; the prorenin
  receptor (ATP6AP2/PRR) acts as an adaptor between Wnt receptors and the V-ATPase complex
  [PMID:20093472 "PRR functions in a renin-independent manner as an adaptor between Wnt
  receptors and the vacuolar H+-adenosine triphosphatase (V-ATPase) complex. Moreover, PRR
  and V-ATPase were required to mediate Wnt signaling"]. The IMP annotation of
  GO:0030177 (positive regulation of Wnt signaling) to ATP6V1C2 derives from this work; it
  reflects a downstream consequence of V-ATPase acidification rather than a subunit-specific
  Wnt function. Keep as non-core.
- A NAS annotation links the gene to regulation of macroautophagy via PMID:22982048, a study of
  lipofuscin formation and lysosomal/autophagy activity in senescent fibroblasts
  [PMID:22982048 "macroautophagy is responsible for the uptake of lipofuscin into the
  lysosomes"]. This paper does not establish a direct ATP6V1C2 role in autophagy regulation;
  the link is indirect (V-ATPase dependent lysosomal acidification supports autophagic
  degradation). Keep as non-core / over-annotation.
- Reactome maps the protein into many acidification and mTORC1-amino-acid-sensing reactions
  (endosome acidification, phagosomal pH lowering, transferrin recycling, v-ATPase:Ragulator
  signaling), all consistent with general V-ATPase function; the associated GO annotations are
  all cytosol (GO:0005829) location calls.

## Tissue specificity

- Originally reported as kidney and placenta enriched [file:human/ATP6V1C2/ATP6V1C2-uniprot.txt
  TISSUE SPECIFICITY, PubMed:12384298]; HPA reports tissue-enhanced expression in epididymis,
  salivary gland and skin. Often described as the lung/kidney-enriched isoform relative to the
  ubiquitous ATP6V1C1.

## Annotation assessment summary

- ACCEPT core: GO:0046961 (proton-transporting ATPase activity, rotational mechanism, IBA),
  GO:0033180 (V1 domain part_of, IEA) as a structural membership term, GO:1902600 (proton
  transmembrane transport).
- GO:0015078 (proton transmembrane transporter activity, IEA): broad InterPro transfer;
  subunit C is not itself the transporter. Mark as over-annotated / keep as non-core.
- GO:0042802 (identical protein binding, IPI from PMID:21356312): the cited paper expressed and
  purified isoforms including C2 but the abstract does not demonstrate C2 self-association; this
  is an uninformative binding term. Mark as over-annotated.
- GO:0030177 (positive regulation of Wnt signaling, IMP): indirect/pathway-level; keep as
  non-core.
- GO:0016241 (regulation of macroautophagy, NAS): weakly supported, indirect; mark as
  over-annotated.
- GO:0070062 (extracellular exosome, HDA): proteomic catalog hit; mark as over-annotated.
- GO:0005765 (lysosomal membrane, HDA): consistent with V-ATPase localization; keep as
  non-core.
- GO:0005829 (cytosol, TAS Reactome, x12): valid for the free/peripheral V1 pool; keep as
  non-core (representative).
