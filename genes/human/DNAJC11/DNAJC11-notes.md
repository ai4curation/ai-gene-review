# DNAJC11 research notes

## Identity
- UniProt Q9NVH1 (DJC11_HUMAN), 559 aa. HGNC:25570. N-terminal J domain (14-82); C-terminal
  DNAJC11-specific beta-barrel + coiled-coil. Belongs to the DNAJC11 family.
- Note: unlike canonical J proteins, DNAJC11's functional role is structural (cristae/MICOS) rather than
  a classic cytosolic HSP70 co-chaperone; no demonstrated HSP70 ATPase stimulation. HSPA9 (mortalin) is
  part of the larger MIB assembly but DNAJC11's MF is not well-defined as a co-chaperone.

## Localization
- Mitochondrion; isoform 1 (full-length, 63 kDa) is in the mitochondrial OUTER membrane (peripheral
  membrane protein); other isoforms differential submitochondrial.
  [PMID:25111180 "The full length 63 kDa isoform of human DNAJC11 was shown to localize in the periphery
  of the mitochondrial outer membrane whereas putative additional isoforms displayed differential
  submitochondrial localization."]
  [file:human/DNAJC11/DNAJC11-uniprot.txt "SUBCELLULAR LOCATION: [Isoform 1]: Mitochondrion outer membrane
  ...; Peripheral membrane protein"]

## Function: MICOS/SAM/MIB & cristae
- Required for mitochondrial inner membrane organization; functions through association with MICOS and
  the SAM complex. [file:human/DNAJC11/DNAJC11-uniprot.txt "Required for mitochondrial inner membrane
  organization. Seems to function through its association with the MICOS complex and the mitochondrial
  outer membrane sorting assembly machinery (SAM) complex."]
- Part of the MIB (mitochondrial intermembrane space bridging) complex spanning both mito membranes.
  [uniprot SUBUNIT "The MICOS and SAM complexes together with DNAJC11 are part of a large protein complex
  spanning both mitochondrial membranes termed the mitochondrial intermembrane space bridging (MIB)
  complex."]
- Originally found in mitofilin (IMMT)/SAM50/metaxin complex. [PMID:17624330 - mitofilin complex with
  SAM50, metaxins 1/2, CHCHD3/6 and DnaJC11] (uniprot ref, not in GOA).
- Mouse hypomorph: motor neuron pathology with cristae disorganization, mitochondria losing proper inner
  membrane organization. [PMID:25111180 "motor neuron pathology associated with cristae disorganization"
  ; "mitochondria that had lost their proper inner membrane organization"]
- DNAJC11 assembled in a high MW complex; mitofilin/SAM50 downregulation affects DNAJC11 levels.
  [PMID:25111180 "DNAJC11 is assembled in a high molecular weight complex, similarly to mitofilin and
  that downregulation of mitofilin or SAM50 affected the levels of DNAJC11"]
- MICOS subunit context [PMID:25997101 QIL1/MICOS]; DNAJC11 associates with the MICOS complex.

## GOA WITH-partner key (bare protein binding rows)
- P42858=HTT (huntingtin), Q8IYS1=PM20D2, Q8N1B4=VPS52, Q9BS40=LXN, Q9NVT9=ARMC1. These are mostly
  isolated high-throughput interactors not clearly tied to the MICOS/cristae function.

## Review logic
CORE:
- MIB complex (GO:0140275, IDA part_of PMID:25997101): ACCEPT, CORE CC.
- cristae formation (GO:0042407, IBA/IEA): ACCEPT, CORE BP.
- inner mitochondrial membrane organization (GO:0007007, IC): ACCEPT, CORE BP.
- mitochondrial outer membrane (GO:0005741, EXP/IEA isoform 1): ACCEPT, CORE CC.
- mitochondrion (GO:0005739, IDA/IEA/HTP): ACCEPT (general, but mito OM is more precise).
Non-core / over-annotated:
- protein binding (GO:0005515, IPI x several HTT/PM20D2/VPS52/LXN/ARMC1): bare term KEEP_AS_NON_CORE.
- No classic HSP70 co-chaperone MF to assign; J domain present but cristae role is structural.
