# MOCS3 (human) — gene review notes

UniProt: O95396 (MOCS3_HUMAN); gene MOCS3, synonym UBA4; 460 aa; chromosome 20.
Two-domain, bifunctional enzyme: EC 2.7.7.80 (adenylyltransferase) + EC 2.8.1.11
(sulfurtransferase). HAMAP rule MF_03049 (MOCS3_Uba4 family).

## Domain architecture (from UniProt file:human/MOCS3/MOCS3-uniprot.txt)
- N-terminal HesA/MoeB/ThiF (E1-like / MoeB) adenylation domain, UBA4 subfamily.
  [file:human/MOCS3/MOCS3-uniprot.txt "In the N-terminal section; belongs to the HesA/MoeB/ThiF
  family. UBA4 subfamily."]
- C-terminal Rhodanese-like domain (RLD), residues 347..458 (PROSITE RHODANESE_3).
  X-ray structure 3I2V (1.25 Å) of residues 335-460.
- ACT_SITE 239: "Glycyl thioester intermediate; for adenylyltransferase activity".
- ACT_SITE 412: "Cysteine persulfide intermediate; for sulfurtransferase activity"
  [file:human/MOCS3/MOCS3-uniprot.txt "Cysteine persulfide intermediate; for"].
- ATP-binding residues (92,113,120-124,137,181-182); Zn(2+) binding (222,225,297,300),
  1 Zn per subunit. Disulfide 316-324.

## Core mechanism (bifunctional sulfur-carrier activation)
MOCS3 activates the C-terminal Gly-Gly of two β-grasp sulfur-carrier proteins,
MOCS2A (MoCo pathway) and URM1 (tRNA-thiolation / urmylation), by a two-step
mechanism: (1) N-terminal adenylation domain forms an acyl-adenylate (-COAMP) at the
C-terminus; (2) C-terminal rhodanese-like domain transfers persulfide sulfur (from
Cys412) to form a thiocarboxylate (-COSH).
[file:human/MOCS3/MOCS3-uniprot.txt "Its N-terminus first activates URM1
and MOCS2A as acyl-adenylates (-COAMP), then the persulfide sulfur on
the catalytic cysteine is transferred to URM1 and MOCS2A to form
thiocarboxylation"]
- The physiological sulfur donor is the L-cysteine desulfurase NFS1, NOT thiosulfate.
  [file:human/MOCS3/MOCS3-uniprot.txt "Does not use thiosulfate as sulfur donor; NFS1 acting
  as a sulfur donor for thiocarboxylation reactions"]

## Two pathways served
1. Molybdenum cofactor (Moco) biosynthesis: MOCS3 thiocarboxylates MOCS2A, the small
   subunit of molybdopterin (MPT) synthase; MPT synthase converts cPMP to MPT (dithiolene
   that coordinates Mo). [PMID:15073332 "the sulfurated form of MOCS3-RLD was able to
   provide the sulfur for the thiocarboxylation of MOCS2A, the small MPT synthase
   subunit in humans"]
2. Cytosolic tRNA 2-thiolation (mcm5s2U34) for tRNA-Lys, tRNA-Glu, tRNA-Gln: MOCS3
   thiocarboxylates URM1, which donates sulfur to the tRNA C2 position.
   [file:human/MOCS3/MOCS3-uniprot.txt "Plays a central role in 2-thiolation of mcm(5)S(2)U at tRNA
   wobble positions of cytosolic tRNA(Lys), tRNA(Glu) and tRNA(Gln)"]

## Key experimental references (all abstract-only in cache except PMID:23593335)
- PMID:15073332 (Matthies 2004, PNAS): physiological role; MOCS3-RLD transfers sulfur
  thiosulfate→cyanide; sulfurated RLD provides sulfur for MOCS2A thiocarboxylation;
  C412 persulfide-forming active-site cysteine essential; MOCS3 and MPT synthase are
  cytosolic. IDA/IMP anchor for GO:0061604, GO:0006777, GO:0005829.
  ["Mutation of the putative persulfide-forming active-site cysteine residue C412
  abolished the sulfurtransferase activity of MOCS3-RLD completely"]
- PMID:15910006 (Matthies 2005, Biochemistry): MS identifies persulfide on C412; disulfide
  C316-C324; only C412 conserved / catalytic. IDA anchor for GO:0016783.
  ["direct evidence for the formation of a persulfide group that is exclusively formed on C412"]
- PMID:17459099 (Krepinsky 2007, FEBS J): active-site loop mutagenesis of RLD; Asp417
  charge controls thiosulfate activity; thiosulfate is NOT the physiologic sulfur donor
  in eukaryotes. IMP anchor for GO:0016783.
  ["in humans and most eukaryotes thiosulfate is not the physiologic sulfur donor for MOCS3"]
- PMID:18650437 (Marelja 2008, JBC): NFS1 is cytosolic sulfur donor for MOCS3; NFS1
  interacts specifically with MOCS3-RLD; sulfur from L-Cys via Nfs1 persulfide.
  EXP/IDA anchor for GO:0061604, GO:0061605, GO:0016783, GO:0006777; IPI with NFS1(Q9Y697).
  ["Nfs1 interacted specifically with MOCS3-RLD and that sulfur is transferred from
  L-cysteine to MOCS3-RLD via an Nfs1-bound persulfide intermediate"]
- PMID:18491921 (Schmitz 2008, Biochemistry): yeast Uba4 (MOCS3 ortholog) N-terminal domain
  adenylates MOCS2A/Urm1 (acyl-adenylate), then persulfurated Uba4 forms thiocarboxylate.
  ISO source (with UniProtKB:P38820 = yeast UBA4) for GO:0061605.
  ["The N-terminal domain of Uba4 catalyzes the activation of either MOCS2A or Urm1 by
  formation of an acyl-adenylate bond"]
- PMID:19017811 (Schlieker 2008, PNAS): links URM1 to tRNA thiolation; URM1 activated to
  thiocarboxylate that serves as sulfur donor in tRNA thiolation. IDA anchor for
  GO:0002098, GO:0016779, GO:0016783, GO:0034227, GO:0042292.
  ["Urm1 is activated by an unusual mechanism to yield a thiocarboxylate intermediate
  that serves as sulfur donor in tRNA thiolation reactions"]
- PMID:22453920 (Chowdhury 2012, JBC): DUAL role; MOCS3 activates both MOCS2A and URM1 by
  adenylation + sulfur transfer forming C-terminal thiocarboxylate; deletion of terminal
  Gly abolishes interaction; C-terminus extension relocalizes MOCS3 cytosol→nucleus.
  EXP/IDA anchor for GO:0061604, GO:0061605, GO:0070566, GO:0002143, GO:0006777, GO:0005829.
  ["MOCS3 activates both MOCS2A and URM1 by adenylation and a subsequent sulfur transfer
  step for the formation of the thiocarboxylate group at the C terminus of each protein"]
- PMID:23593335 (Marelja 2013, PLoS ONE; FULL TEXT): NFS1 localized in cytosol; direct
  NFS1-MOCS3 interaction in cytosol; interaction site is C-terminal RLD (KD ~28 nM).
  IDA GO:0005829; IPI with NFS1(Q9Y697).
  ["these results show that NFS1 interacts with MOCS3 in the cytosol"]
- PMID:30817134 (Neukranz 2019, Biochemistry): MOCS3 CRISPR knockout in HEK293T abolishes
  sulfite oxidase activity (no Moco) and mcm5s2U thio-modified tRNAs; confirms dual role
  in vivo. IMP anchor for GO:0006777, GO:0034227.
  ["mcm5s2U thio-modified tRNAs were not detectable"]

## Interactors (protein binding IPI — bare GO:0005515, marked over-annotated)
- URM1 (Q9BTM9) — PMID:21209336 (IntAct). Functionally meaningful substrate/partner but
  the bare "protein binding" term is uninformative; specific MF captured as URM1 activating
  enzyme activity and adenylyltransferase/sulfurtransferase activities.
- NFS1 (Q9Y697) — PMID:18650437, PMID:23593335 (sulfur donor; RLD interaction).
- ATXN1 (P54253), TARDBP/TDP-43 (Q13148) — PMID:32814053 (large-scale ND interactome Y2H).
  MOCS3 appears as a candidate interactor in a neurodegeneration network; no dedicated
  functional characterization for MOCS3; likely low functional relevance.

## Disease
Molybdenum cofactor deficiency type B2 (MOCODB2, MIM:621373), autosomal recessive; variants
Val-109, Thr-257, del459-460. Consistent with essential MoCo-biosynthesis role.
[PMID:28544736, PMID:33897766]

## Curation decisions (summary)
- Core catalytic MFs: GO:0061605 (MPT-synthase adenylyltransferase) and GO:0061604
  (MPT-synthase sulfurtransferase) — the two named EC activities of MOCS3, well supported
  by EXP/IDA/IMP. GO:0042292 (URM1 activating enzyme activity) — direct IDA (PMID:19017811),
  the URM1-pathway counterpart of the adenylyltransferase activity. ACCEPT these as core.
- GO:0016783 sulfurtransferase (parent) and GO:0070566 adenylyltransferase (parent),
  GO:0016779 nucleotidyltransferase (parent): correct-but-general parents of the specific
  MFs above → KEEP_AS_NON_CORE (generic) / the specific children are the core.
- GO:0004792 thiosulfate:cyanide sulfurtransferase activity (IBA): MOCS3-RLD has this
  activity in vitro but at ~1000-fold lower rate than bovine rhodanese, and thiosulfate is
  NOT the physiological donor (PMID:17459099, PMID:18650437, UniProt) — MARK_AS_OVER_ANNOTATED.
- GO:0008641 ubiquitin-like modifier activating enzyme activity (IEA, InterPro): family-level
  E1-like inference; MOCS3 activates URM1 (a Ubl) as a sulfur carrier, not classic Ubl
  conjugation cascade → the specific GO:0042292 is preferred → MARK_AS_OVER_ANNOTATED.
- BP: GO:0006777 (MoCo biosynthesis), GO:0002143 (tRNA wobble uridine thiolation),
  GO:0034227 (tRNA thio-modification) — ACCEPT as core; GO:0002098 (tRNA wobble uridine
  modification) is a broader parent → KEEP_AS_NON_CORE; GO:0032447 protein urmylation (IBA)
  — MOCS3 is a component of the urmylation machinery (activates URM1) → KEEP_AS_NON_CORE.
- CC: cytosol/cytoplasm ACCEPT (well supported by IDA + subcellular fractionation).
- bare protein binding (GO:0005515 IPI): MARK_AS_OVER_ANNOTATED (never REMOVE per policy).
</content>
</invoke>
