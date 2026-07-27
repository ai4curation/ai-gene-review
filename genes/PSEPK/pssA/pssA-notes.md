# pssA review notes

## Identity and scope

- Target: `pssA`, PP_3664, UniProt Q88GQ4, *Pseudomonas putida* KT2440.
- Reviewed files: `pssA-ai-review.yaml`, `pssA-goa.tsv`, and `pssA-uniprot.txt`.
- Consecutive-reaction context was checked against the target `psd` record Q88DB9.

## Exact provenance

### UniProt PssA record

Source: `file:PSEPK/pssA/pssA-uniprot.txt`.

- `"DE   SubName: Full=CDP-diacylglycerol--serine O-phosphatidyltransferase"`
- `"DE            EC=2.7.8.8"`
- `"GN   OrderedLocusNames=PP_3664"`
- `"DR   GO; GO:0003882; F:CDP-diacylglycerol-serine O-phosphatidyltransferase activity; IEA:UniProtKB-EC."`
- `"DR   GO; GO:0008444; F:CDP-diacylglycerol-glycerol-3-phosphate 3-phosphatidyltransferase activity; IEA:InterPro."`
- `"DR   GO; GO:0032049; P:cardiolipin biosynthetic process; IEA:InterPro."`

The last two lines conflict with the submitted PssA name and EC assignment.

### Consecutive Psd reaction

Source: `file:PSEPK/psd/psd-uniprot.txt`.

- `"CC   -!- FUNCTION: Catalyzes the formation of phosphatidylethanolamine (PtdEtn)"`
- `"CC       from phosphatidylserine (PtdSer)."`
- `"CC       biosynthesis; phosphatidylethanolamine from CDP-diacylglycerol: step"`
- `"CC       2/2."`

Normalized curation statements used as exact YAML support:

- `"PssA uses L-serine to form phosphatidylserine; GO:0008444 instead denotes transfer to glycerol-3-phosphate."`
- `"PssA forms phosphatidylserine, which is the substrate for the consecutive Psd decarboxylation reaction."`

## Reaction discrimination

- PssA/EC 2.7.8.8: CDP-diacylglycerol + L-serine -> phosphatidylserine + CMP.
- PgsA/GO:0008444: CDP-diacylglycerol + glycerol-3-phosphate -> phosphatidylglycerophosphate + CMP.
- Psd/EC 4.1.1.65: phosphatidylserine -> phosphatidylethanolamine + CO2.

These are distinct reactions. The PgsA activity and cardiolipin process are not broad parents of PssA; they are incorrect cross-mappings and are removed.

## Curation conclusions

- Accept GO:0003882 and phosphatidylethanolamine biosynthesis as core.
- Retain the seeded cytosol annotation, but record plasma membrane as the core
  catalytic location because the type-I enzyme is active at the inner
  membrane surface and inactive in its cytosolic state
  [PMID:39693441, "the active state of PssA is associated with the inner membrane surface, contributing to PS synthesis, while the cytosolic form is inactive in this synthesis process"].
- Remove GO:0008444 and GO:0032049.

## OpenScientist reconciliation

The generated OpenScientist report correctly identifies Q88GQ4 as the
phosphatidylserine-forming PLD-superfamily enzyme, but it calls that
architecture "type II." Bacterial PssA literature uses the opposite
architecture labels: PLD-superfamily peripheral-membrane PssA is type I,
whereas integral-membrane CDP-alcohol phosphatidyltransferase PssA is type II.
The module follows the primary-literature nomenclature
[PMID:39693441, "Type I PssA belongs to the phospholipase D (PLD) superfamily"].

UniProt's statement that Q88GQ4 belongs to the CDP-alcohol
phosphatidyltransferase "class-II family" uses a separate family-classification
axis. It does not contradict the type-I PssA architecture defined by
PMID:39693441.

Normalized curation statement used as exact YAML support:

- `"The OpenScientist report supports the phosphatidylserine-synthase reaction and PLD architecture of Q88GQ4, while primary literature establishes that this bacterial architecture is type I."`
