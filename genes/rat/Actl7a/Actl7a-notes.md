# Actl7a (rat, Q641W9) review notes

## 2026-10-28 session

- `just fetch-gene rat Actl7a` resolved Q641W9 (Swiss-Prot ACL7A_RAT, RGD:1304697, GeneID 298017).
  34 GOA rows; two identical nucleus ISS rows (Q9QY84) collapsed to one in the seeded review (33).
- Only one paper is cited by GOA for rat: PMID:21278383 (full text cached). The rat material in it is
  the Tes co-IP from rat testis extracts [PMID:21278383 "Arp7A, Tes, and Mena are complexed to each
  other in rat testes extracts"]. Immunofluorescence used mouse testes; pulldowns and the crystal
  structure used human Arp7A.
  - Consequence: the rat `cytoplasm` EXP row (UniProt, PMID:21278383) has no rat cytoplasmic
    observation behind it; the cytoplasmic observation is GFP-human-Arp7A in HeLa ("data not shown")
    or mouse sections. Recorded as a WRONG_EVIDENCE_CODE source defect (CHECK). The claim itself is
    true (perinuclear theca is_a cytoskeleton, part_of cytoplasm).
  - The IDA `protein-containing complex` row is genuinely rat (co-IP in rat testis): ACCEPT.
- Mouse donor (Q9QY84, MGI:1343051) annotations checked in QuickGO 2026-10-28: perinuclear theca IDA
  PMID:41169243; male germ cell nucleus IDA and motile cilium IDA PMID:12672658 (MGI); acrosome
  assembly IMP PMID:32923619 + PMID:36734600; spermatid development IMP PMID:37667331; fertilization
  IMP PMID:32923619 + PMID:35921706; Golgi colocalizes_with IDA PMID:21278383.
- Decisions follow the human ACTL7A review for consistency:
  - acrosomal vesicle -> MODIFY to perinuclear theca (protein is in the subacrosomal layer, on the
    nuclear side of the inner acrosomal membrane, not inside the acrosome) [PMID:21278383 "all three
    proteins are actually localized in the subacrosomal layer that links the acrosome to the nuclear
    envelope"]. WRONG_TERM source defects (CHECK) on the ISS (UniProt) and ISO (RGD) rows.
  - male germ cell nucleus ISO -> KEEP_AS_NON_CORE.
  - nucleus -> MODIFY to male germ cell nucleus (already on the gene by ISO; only germ cells express
    it).
  - cytoplasm, cytoskeleton -> MODIFY to perinuclear theca (+ Golgi apparatus for cytoplasm).
  - Golgi apparatus -> KEEP_AS_NON_CORE (root organelle; transient association during acrosome
    biogenesis; mouse IDA source holds).
  - motile cilium -> UNDECIDED (only the 2003 abstract mentions tails; full text not cached; 2023
    study reports a connecting-piece pool, which GO does not place in the flagellum).
  - acrosome assembly, spermatid development, perinuclear theca, structural molecule activity,
    protein-containing complex -> ACCEPT.
  - fertilization -> KEEP_AS_NON_CORE (knock-out necessity; downstream of the sperm-head structural
    role, no fertilization step performed by Actl7a).
  - ND biological_process -> REMOVE (superseded by process rows), per rat-batch precedent.
- NEW: GO:0030274 LIM domain binding (ISS from human, PMID:21278383). The Tes-binding segment
  (human 28-45 = rat 33-50, LQTASLRDGPAKRAVWVR) is identical; rat co-IP shows the complex in rat
  testis. This is an MF, not a process. No NEW process terms (actin cytoskeleton organization, egg
  activation) were added: the evidence for them is mouse/human mutant phenotype only.
