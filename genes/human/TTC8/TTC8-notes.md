# TTC8 (BBS8) — Gene Review Notes

UniProt: Q8TAM2 | HGNC:20087 | Gene: TTC8 (synonym BBS8) | 541 aa | Chr 14

## Summary of function

TTC8/BBS8 is a tetratricopeptide-repeat (TPR) superhelical protein and one of the eight
core subunits of the **BBSome** (BBS1, BBS2, BBS4, BBS5, BBS7, BBS8/TTC8, BBS9, BBIP10/BBIP1).
The BBSome is a coat-like, octameric adaptor that traffics specific membrane/signaling
proteins (GPCRs and other cargo) into and out of the primary cilium, coupled to intraflagellar
transport (IFT) and the small GTPase ARL6/BBS3. It also cooperates with the Rab8 GEF
Rabin8/RAB3IP to promote ciliary membrane biogenesis. Loss of function causes Bardet–Biedl
syndrome type 8 (BBS8, MIM:615985) and nonsyndromic retinitis pigmentosa 51 (RP51, MIM:613464).

## Key evidence

- **BBSome subunit / coat for ciliary trafficking**: The BBSome is a complex of seven highly
  conserved BBS proteins (later eight, with BBIP10) that localizes to centriolar satellites in
  the cytoplasm and to the ciliary membrane; required for ciliogenesis but dispensable for
  centriolar satellite function. [PMID:17574030 "Here we identify a complex composed of seven
  highly conserved BBS proteins. This complex, the BBSome, localizes to nonmembranous centriolar
  satellites in the cytoplasm but also to the membrane of the cilium."] BBS8/TTC8 is one of the
  identified subunits (by MS) in that paper. The BBSome's ciliogenic function involves the Rab8
  GEF (Rabin8/RAB3IP) at the basal body. [PMID:17574030 "This ciliogenic function is mediated in
  part by the Rab8 GDP/GTP exchange factor... Rab8(GTP) enters the primary cilium and promotes
  extension of the ciliary membrane."]

- **BBIP10/BBSome paper confirms TTC8 as subunit, ciliary localization**: [PMID:19081074 "seven
  highly conserved BBS proteins form a stable complex, the BBSome, that functions in membrane
  trafficking to and inside the primary cilium... BBIP10 localizes to the primary cilium"].
  ComplexPortal curated this annotation (BBSome part_of; ciliary membrane IDA).

- **BBS8 cloning, ciliary/basal body localization, situs defects**: [PMID:14520415 "We have
  cloned a new BBS gene, BBS8, which encodes a protein with a prokaryotic domain, pilF...
  In one family, a homozygous null BBS8 mutation leads to BBS with randomization of left-right
  body axis symmetry, a known defect of the nodal cilium. We have also found that BBS8 localizes
  specifically to ciliated structures, such as the connecting cilium of the retina and columnar
  epithelial cells in the lung. In cells, BBS8 localizes to centrosomes and basal bodies and
  interacts with PCM1"]. This supports cilium, centrosome, basal body localization (all IDA),
  PCM1 interaction (IPI), and the left-right asymmetry / establishment of structure orientation
  phenotype (IMP, GO:0048560).

- **LZTFL1 regulates BBSome ciliary trafficking**: BBSome (incl. TTC8) cytoplasmic localization
  and ciliary trafficking; LZTFL1 controls SMO and BBSome ciliary entry. [PMID:22072986 "LZTFL1
  regulates ciliary trafficking of the BBSome and Smoothened."] Supports cytoplasm (EXP) and
  BBSome/SHH-pathway role.

- **NPHP5/Cep290 regulate BBSome integrity; BBS8 interacts with NPHP5/IQCB1**: Depletion of
  Cep290 causes dissociation/loss of ciliary BBS8. [PMID:25552655 "Depletion of Cep290... causes
  additional dissociation of BBS8 and loss of ciliary BBS8."] BBS8–IQCB1(NPHP5) interaction is
  the basis of the IPI protein-binding annotation (WITH UniProtKB:Q15051) and an IntAct entry.

- **AZI1/CEP131 (Q9UPN4) interacts with BBS4, regulates BBSome trafficking**: [PMID:24550735]
  BBSome IDA and a TTC8–CEP131 IPI (WITH Q9UPN4).

- **PKD1 interaction / ciliary trafficking of polycystin-1**: BBS1 and BBS3 regulate ciliary
  trafficking of PKD1; TTC8 IPI annotations WITH P98161(PKD1), Q8N3I7, Q8NFJ9, Q96RK4. [PMID:24939912]

- **CCDC28B interaction**: BBS8 interacts with CCDC28B (Q9BUN5) in oligogenic BBS epistasis
  study. [PMID:16327777] Basis of IPI (WITH Q9BUN5).

- **Transcriptional regulation (BBS7-centric)**: BBS7 has a nuclear role and interacts with the
  PcG member RNF2; "our data supports a similar role for other BBS proteins." [PMID:22302990
  "BBS7... interacts physically with the polycomb group (PcG) member RNF2 and regulate its protein
  levels... our data supports a similar role for other BBS proteins."] The TTC8 IPI annotation to
  RNA Pol II transcription factor binding (GO:0061629, WITH RNF2/Q99496, assigned by MGI) derives
  from this. The abstract foregrounds BBS7; full text reportedly assays additional BBS proteins.
  Treat as peripheral/non-core, not a core MF.

- **PCM1 recruitment / DISC1-BBS4**: [PMID:18762586] is primarily about PCM1 recruitment by DISC1
  and BBS4; the TTC8 IPI (WITH PCM1/Q9NRI5, assigned SYSCILIA_CCNET) reflects the BBS8–PCM1
  interaction (consistent with PMID:14520415).

- **BBSome assembly chaperonins**: BBS6/BBS10/BBS12 + CCT/TRiC mediate BBSome assembly; TTC8 is a
  BBSome component (IDA). [PMID:20080638]

- **Mitochondrion (HTP)**: [PMID:34800366] is a high-throughput human mitochondrial proteome study.
  TTC8 is a cytoplasmic/ciliary BBSome subunit; a single HTP hit in a mito-proteome screen is most
  plausibly a contaminant/co-purification, not a genuine mitochondrial localization. Not core.

## Isoforms

Five isoforms (Q8TAM2-1..-6). A retina-specific exon is important in photoreceptors; a splice-site
mutation in a retina-specific exon causes nonsyndromic RP51 [UniProt; PMID:20451172]. GOA
annotations are not isoform-tagged, so no isoform field is added per-annotation.

## Curation reasoning highlights

- Core: BBSome (GO:0034464, part_of) — strongly supported by multiple IDA/IPI; this is THE defining
  molecular context of the protein.
- Core CC: ciliary basal body, cilium/ciliary membrane, centrosome/centriolar satellite — well
  supported by IDA (PMID:14520415, ComplexPortal PMID:19081074).
- Core BP: cilium assembly / non-motile cilium assembly, protein transport into cilium (cargo
  trafficking). Establishment of structure orientation (left-right asymmetry) is a real but
  downstream/developmental consequence of nodal cilium function → KEEP_AS_NON_CORE.
- `protein binding` (GO:0005515) IPI entries: uninformative MF per guidelines; keep but mark as
  over-annotated (do not promote as core MF). The interactions themselves (NPHP5, CEP131, PCM1,
  CCDC28B, PKD1) are biologically real and inform the adaptor/trafficking role.
- GO:0061629 (RNA Pol II TF binding): peripheral, BBS7-driven study; mark over-annotated/non-core.
- Mitochondrion HTP: likely contaminant; mark over-annotated.
- Reactome cytosol TAS (×5): acceptable cellular location of the soluble BBSome assembly steps;
  keep as non-core (BBSome assembles in cytosol before ciliary delivery).
- fat cell differentiation (Ensembl IEA orthology) & sensory perception/anatomical structure
  morphogenesis (ARBA IEA): plausible organismal/ciliopathy phenotypes but electronic and
  non-core; keep as non-core.
