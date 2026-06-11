# FAF2 (UBXD8/ETEA) review notes

UniProt: Q96CS3 (FAF2_HUMAN), 445 aa. Synonyms: ETEA, UBXD8, UBXN3B, KIAA0887.
Domain architecture: N-terminal UBA domain (12-48), UAS domain (thioredoxin-like, CDD cd02991 UAS_ETEA),
coiled-coil (275-350), C-terminal UBX domain (357-439). The UBX domain binds p97/VCP; the UBA domain binds ubiquitin.

## Core biology
FAF2 is a membrane-anchored UBX-domain p97/VCP cofactor. It recruits the VCP segregase to the ER membrane
and to lipid droplets, where it functions both in ERAD substrate extraction/retrotranslocation and in
lipid-droplet / fatty-acid metabolism.

### p97/VCP cofactor + UBX/UBA
[PMID:18775313 "p97 assembles with all of the 13 mammalian UBX-domain proteins. The UBX proteins that bind ubiquitin conjugates also interact with dozens of E3 ubiquitin ligases"]
- UBXD8/FAF2 is one of the 13 UBX-domain p97 cofactors; UBX binds p97, UBA binds ubiquitin conjugates.
- UniProt IntAct: VCP NbExp=16; UBAC2 NbExp=8. ComplexPortal CPX-8104 "VCP-NPL4-UFD1-FAF2 AAA ATPase complex".

### ERAD
[PMID:18711132 "We identified AUP1, UBXD8, UBC6e, and OS9 as functionally important components of this degradation complex"]
- FAF2/UBXD8 is part of the SEL1L/HRD1 ERAD dislocation complex (with SEL1L, OS9, AUP1, UBE2J1).
[PMID:24215460 "UBXD8 is an endoplasmic membrane protein involved in the translocation of ubiquitinated ERAD substrates, UBQLN2 likely cooperates with UBXD8 to transport defective proteins from the endoplasmic reticulum to the cytosol"]
- Implicated in retrotranslocation/dislocation of ERAD substrates (e.g. NHK alpha-1-antitrypsin, PMID:25660456).

### Lipid droplet / ATGL regulation
[PMID:23297223 "UBXD8-mediated recruitment of p97/VCP to LDs increases LD size by inhibiting the activity of adipose triglyceride lipase (ATGL), the rate-limiting enzyme in triacylglycerol hydrolysis. Our findings show that UBXD8 binds directly to ATGL and promotes dissociation of its endogenous coactivator, CGI-58"]
[PMID:23297223 "association of UBXD8 with the ER-resident rhomboid pseudoprotease UBAC2 specifically restricts trafficking of UBXD8 to LDs"]
- FAF2 binds PNPLA2/ATGL (lipase binding), inhibits it (lipase inhibitor activity), promotes CGI-58/ABHD5 dissociation -> inhibits lipolysis, increases LD size.
- UBAC2 interaction restricts ER->LD trafficking of FAF2.
- LD localization independently confirmed by lipid-droplet proteomics [PMID:14741744] (HuH7 LD fraction).

### Stress granule disassembly
[PMID:34739333 "ubiquitinated G3BP1 interacted with the endoplasmic reticulum–associated protein FAF2, which engaged the ubiquitin-dependent segregase p97/VCP"]
- On heat shock, FAF2 binds ubiquitinated G3BP1 and recruits VCP to extract G3BP1 -> stress granule disassembly. FAF2 here acts as a protein-macromolecule adaptor bridging ubiquitinated substrate to VCP.

## Annotation assessment summary
- Core MF: ubiquitin binding (GO:0043130, UBA), ubiquitin protein ligase binding (GO:0031625), protein-macromolecule adaptor activity (GO:0030674) — these capture the informative p97-cofactor/adaptor function.
- Core CC: ER (GO:0005783), lipid droplet (GO:0005811), VCP-NPL4-UFD1 complex (GO:0034098).
- Core BP: ERAD pathway (GO:0036503), retrograde protein transport ER to cytosol (GO:0030970), lipid droplet organization (GO:0034389), stress granule disassembly (GO:0035617).
- lipase binding (GO:0035473) / lipase inhibitor activity (GO:0055102): specific, experimentally supported (PMID:23297223) — keep.
- Reactome extracellular region / azurophil granule lumen (neutrophil degranulation, R-HSA-6798751): bulk proteomic neutrophil-granule annotations; not the core ER/LD function — KEEP_AS_NON_CORE.
- The many bare "protein binding" (GO:0005515) IPI annotations: KEEP_AS_NON_CORE (uninformative term), though several map to informative interactions captured by specific terms.
- ATPase complex (GO:1904949) NAS / proteasomal protein catabolic process (GO:0010498) IEA: generic parents; keep non-core.
</content>
