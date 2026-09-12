# EEFSEC (eEFSec / SelB) — gene review notes

UniProt: P57772 (SELB_HUMAN). Gene symbol EEFSEC (HGNC:24614); synonym SELB. 596 aa. Human (NCBITaxon:9606).

## Summary of function

EEFSEC encodes eEFSec (also called eukaryotic elongation factor, selenocysteine-tRNA-specific;
SelB in prokaryotes), the dedicated translation elongation factor for co-translational
incorporation of the 21st amino acid selenocysteine (Sec) at in-frame UGA codons.

- "Translation factor required for the incorporation of the rare amino acid selenocysteine
  encoded by UGA codons" [file:human/EEFSEC/EEFSEC-uniprot.txt "Translation factor required for the incorporation of the rare"].
- It is a GTP-binding translational GTPase of the EF-Tu/eEF1A-related SelB subfamily:
  "Belongs to the TRAFAC class translation factor GTPase superfamily. Classic translation
  factor GTPase family. SelB subfamily." [file:human/EEFSEC/EEFSEC-uniprot.txt "SelB subfamily"].
- Mechanistic role, per UniProt FUNCTION: eEFSec "Replaces the eRF1-eRF3-GTP ternary complex
  for the insertion of selenocysteine directed by the UGA codon"; insertion is mediated by
  SECISBP2 (SBP2) and EEFSEC — SBP2 binds the SECIS element and contacts eS31/RPS27A of the
  40S, then "GTP-bound EEFSEC then delivers selenocysteinyl-tRNA(Sec) to the 80S ribosome and
  adopts a preaccommodated state conformation", and "After GTP hydrolysis, EEFSEC dissociates
  from the assembly, selenocysteinyl-tRNA(Sec) accommodates, and peptide bond synthesis and
  selenoprotein elongation occur" [file:human/EEFSEC/EEFSEC-uniprot.txt].
- Catalytic activity: GTP + H2O = GDP + phosphate + H(+) (Rhea:RHEA:19669); EC 3.6.5.-.
  Cofactor Mg(2+) (also Mn(2+) in crystals) [file:human/EEFSEC/EEFSEC-uniprot.txt].

## Key primary literature (cached, full text available)

### PMID:27708257 (Dobosz-Bartoszek et al., Nat Commun 2016) — crystal structures of human eEFSec
- eEFSec is "A specialized translation elongation factor, eEFSec in eukaryotes and SelB in
  prokaryotes, promotes selenocysteine incorporation into selenoproteins"
  [PMID:27708257 "promotes selenocysteine incorporation into selenoproteins"].
- "eEFSec is a translational GTPase that binds Sec-tRNASec with high affinity and stringent
  specificity, and plays a pivotal role during decoding19 by delivering Sec-tRNASec to the
  site of translation in response to a particular in-frame UGA codon"
  [PMID:27708257 "eEFSec is a translational GTPase that binds Sec-tRNASec with high affinity and stringent specificity"].
- GTPase site: composed of P-loop, switch 1, switch 2 (92DxxGH96), guanine-binding sequence
  (146NKxD149), divalent metal ion; His96 is the presumed catalytic residue whose repositioning
  by the ribosome stimulates GTP hydrolysis. Mutagenesis: T48A, D92A, H96A bind GTP/GDP but
  "cannot promote the UGA codon read-through and selenoprotein synthesis in vitro"; "we conclude
  that Thr48, Asp92 and His96 are important for GTP hydrolysis"
  [PMID:27708257 "important for GTP hydrolysis"].
- Sec-binding pocket residues (Asp229, His230, Arg285); each single substitution "obliterated
  the ability of eEFSec to promote Sec incorporation" (supports IDA for selenocysteine
  incorporation and Sec-tRNA(Sec) recognition) [PMID:27708257 "obliterated the ability of eEFSec to promote Sec incorporation"].
- Non-canonical mechanism: unlike EF-Tu, GTP-to-GDP exchange induces a swing of C-terminal
  domain 4 rather than a rotation of domain 1.

### PMID:35709277 (Hilal et al., Science 2022) — cryo-EM of the mammalian "selenosome" decoding Sec UGA
- "A complex between the noncoding Sec-insertion sequence (SECIS), SECIS-binding protein 2
  (SBP2), and 40S ribosomal subunit enables Sec-specific elongation factor eEFSec to deliver Sec"
  [PMID:35709277 "enables Sec-specific elongation factor eEFSec to deliver Sec"].
- Ternary complex eEFSec•GTP•(Ser/Sec)-tRNASec captured in preaccommodated state; "the anticodon
  loop is properly positioned in the A site of the DC, which suggests that we captured the
  preaccommodated state of the selenosome with the tRNASec in the A/T conformation"
  [PMID:35709277 "preaccommodated state of the selenosome"].
- eEFSec uses all domains to engage tRNASec: "Human eEFSec uses all its domains to engage the
  tRNASec" [PMID:35709277 "Human eEFSec uses all its domains to engage the tRNASec"] (supports
  tRNA/Sec-tRNA binding).
- GTPase: GTPase-defective His96->Ala mutant used to avoid GTP hydrolysis; "GTP is bound to the
  GTPase pocket in D1, but the side chains of switch 2 are disordered, which confirms the
  catalytically incompetent conformation of eEFSec-H96A"
  [PMID:35709277 "the catalytically incompetent conformation of eEFSec-H96A"]. H96A mutagenesis
  in UniProt: "H->A: Abolished GTPase activity" [file:human/EEFSEC/EEFSEC-uniprot.txt "Abolished GTPase activity"].
- D4 of eEFSec engages the SECIS apical loop; eEFSec and SBP2 do not interact directly.
- eEFSec is indiscriminate toward L-serine and can misincorporate Ser at Sec UGA codons.

### PMID:39753114 (Laugwitz et al., Am J Hum Genet 2025) — EEFSEC deficiency disease (not cached)
- UniProt DISEASE: biallelic EEFSEC variants cause "Neurodevelopmental disorder with progressive
  spasticity and brain abnormalities (NEDPSB) [MIM:621102]" — autosomal recessive, infancy/early
  childhood onset, global developmental delay, intellectual disability, spasticity, ataxia,
  seizures, cerebral/cerebellar hypoplasia [file:human/EEFSEC/EEFSEC-uniprot.txt].
- Pathogenic variants (P194T, R285Q, D390A, 426-596del) show "decreased selenocysteine
  incorporation in selenoproteins" [file:human/EEFSEC/EEFSEC-uniprot.txt "decreased"]; A35V is
  likely benign with no effect. Disease name = "EEFSEC deficiency: A selenopathy with early-onset
  neurodegeneration."

## Localization
- UniProt SUBCELLULAR LOCATION: "Cytoplasm {ECO:0000305}. Nucleus {ECO:0000305}"
  [file:human/EEFSEC/EEFSEC-uniprot.txt]. Both are ECO:0000305 (inferred), not direct
  experimental. A predicted nuclear localization signal is present (residues 547-553). The
  functional site of action is cytoplasmic (co-translational Sec insertion at the 80S ribosome).

## Annotation review reasoning

Core functions well supported by structure/biochemistry (PMID:27708257, PMID:35709277) and
UniProt:
- MF: translation elongation factor activity (GO:0003746); GTPase activity (GO:0003924);
  GTP binding (GO:0005525); Sec-tRNA(Sec)/tRNA binding (GO:0000049 tRNA binding is the closest
  GOA-supported MF; more specific would be aminoacyl-tRNA / Sec-tRNA(Sec) binding).
- BP: selenocysteine incorporation (GO:0001514) is the specific, defining process; it is a
  specialization of translational elongation.

Location annotations (cytoplasm GO:0005737, nucleus GO:0005634) are IEA from UniProt SubCell
(ECO:0000305). Cytoplasm is the functional site. Nucleus is inferred (NLS present) but no
demonstrated nuclear function; keep as non-core.

The GTP binding IEA (GO:0005525) and GTPase activity IEA (GO:0003924) are redundant with the
IDA GTPase annotations; the IDA (experimental) versions are the primary evidence.
