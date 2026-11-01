# Curation Notes: Bacteriophage T4 gene 20 (gp20; UniProt P13334)

## Identity and Nomenclature
- **Gene symbol**: `20`
- **Protein**: Portal protein gp20 (524 aa, ~60.9 kDa)
- **UniProt**: `P13334` (`PORT_BPT4`)
- **Taxon**: `NCBITaxon:10665` (*Tequatrovirus T4*)

## Biological Function Summary
1. **Dodecameric portal vertex of the prolate icosahedral capsid**:
   - gp20 forms a 12-subunit (homododecameric) ring (~660 kDa, ~120 Å long, 90-170 Å outer diameter, 28-44 Å internal channel) occupying the unique fivefold vertex of the T4 prolate icosahedral capsid in place of a gp24 pentamer (Sun et al. 2015, PubMed 26144253; PDB: 3JA7).
   - Each monomer comprises four domains: clip (residues 279-358, exposed outside the capsid to bind the gp17 packaging motor and later the gp13/gp14 neck), stem (helices alpha5 and alpha7 lining the channel), wing (residues 70-254 and 378-450, contacting the inner surface of surrounding gp23* hexamers), and crown (residues 451-524, projecting into the capsid interior).
2. **Prohead assembly initiation at the host inner membrane**:
   - Unlike most phage portals, gp20 initiates T4 prohead morphogenesis at the cytoplasmic face of the *Escherichia coli* inner membrane, assisted by host chaperones (DnaK, Trigger factor, GroEL), host membrane insertase YidC, and phage membrane-spanning helper gp40 (Quinten & Kuhn 2012, PubMed 22855489; Hsiao & Black 1978, PubMed 629829). It nucleates the gp22-containing scaffolding core and the surrounding gp23 major capsid shell.
3. **Viral genome packaging and ejection conduit**:
   - After prohead release from the inner membrane and gp21-mediated maturation cleavage, the gp20 clip domain docks the pentameric gp17 large terminase ATPase motor via electrostatic interactions (residues N291, M292, R295, K296 of gp20). Basic channel-entrance residues (R338, K342), the channel loop (residues 350-359), and the flexible tunnel loop (residues 374-398) actively participate in translocating ~171 kb of dsDNA into the head and preventing DNA slippage at high internal pressure (Sun et al. 2015, PubMed 26144253; Padilla-Sanchez et al. 2014).
   - Once packaging completes, gp17 dissociates and the neck proteins gp13 (dodecamer) and gp14 (hexamer) bind the gp20 portal to seal the head and allow tail attachment. During infection, the portal channel serves as the exit conduit for viral genome ejection through the tail tube into the host cell.

## Review of Existing GOA Annotations
- `GO:0046798` (`viral portal complex`, IDA `PMID:26144253`): **ACCEPT**. Directly demonstrated by the 3.6 Å cryo-EM structure of the dodecameric gp20 portal assembly and 10 Å structure in the T4 head.
- `GO:0019028` (`viral capsid`, IEA `GO_REF:0000120`): **MODIFY** -> `GO:0046798` (`viral portal complex`). gp20 specifically forms the dodecameric portal vertex (`GO:0046798`), a more precise child component already annotated on this gene.
- `GO:0019072` (`viral genome packaging`, IEA `GO_REF:0000104`): **ACCEPT**. gp20 forms the translocation channel, docks the gp17 terminase ATPase, and stabilizes packaged DNA via its tunnel loops.
- `GO:0099000` (`symbiont genome ejection through host cell envelope, contractile tail mechanism`, IEA `GO_REF:0000120`): **ACCEPT**. The gp20 portal channel is the conduit through which packaged dsDNA exits the capsid into the tail tube during infection.
- `GO:0046718` (`symbiont entry into host cell`, IEA `GO_REF:0000043`): **MODIFY** -> `GO:0099000` (`symbiont genome ejection through host cell envelope, contractile tail mechanism`). Overly broad keyword mapping; T4 enters via contractile-tail-mediated genome ejection (`GO:0099000`).
- `GO:0020002` (`host cell plasma membrane`, IEA `GO_REF:0000044` and IDA `PMID:22855489`): **KEEP_AS_NON_CORE** (both rows). Quinten & Kuhn (2012, PubMed 22855489) demonstrated that nascent gp20 is escorted by DnaK, trigger factor, and GroEL to dock at YidC on the cytoplasmic face of the *E. coli* inner (plasma) membrane to nucleate prohead assembly before detaching into the cytoplasm as part of the maturing virion.
- `GO:0019076` (`viral release from host cell`, IEA `GO_REF:0000104`): **REMOVE**. Over-annotation from UniProt keyword `Viral release from host cell`; gp20 is the capsid portal protein involved in prohead assembly, genome packaging, and genome ejection, not host cell lysis or viral release.
- **New annotations (`NEW`)**:
  - `GO:0039660` (`structural constituent of virion`): gp20 is an essential structural subunit forming the dodecameric portal vertex of the mature virion.
  - `GO:0019069` (`viral capsid assembly`): gp20 is the essential initiator vertex required to nucleate assembly of the scaffolding core and gp23 capsid lattice.
