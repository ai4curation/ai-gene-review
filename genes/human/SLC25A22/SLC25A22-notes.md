# SLC25A22 (Mitochondrial glutamate carrier 1, GC-1) — review notes

UniProt: Q9H936 (GHC1_HUMAN). HGNC:19954. Gene = SLC25A22, synonym GC1.

## Identity and core function

SLC25A22 is a member of the mitochondrial carrier family (SLC25 / TC 2.A.29). It is a
multi-pass integral protein of the **mitochondrial inner membrane** with the canonical
tripartite mitochondrial-carrier architecture (three Solcar repeats, six transmembrane
helices) [file:human/SLC25A22/SLC25A22-uniprot.txt "Belongs to the mitochondrial carrier
(TC 2.A.29) family"; six `TRANSMEM` features; three `REPEAT ... Solcar` features].

Its function is a **glutamate/H+ symporter**: it imports L-glutamate from the cytosol into
the matrix together with a proton (electroneutral H+/glutamate symport, i.e. glutamate
co-transported with H+ or exchanged for OH-).

- UniProt FUNCTION: [file:human/SLC25A22/SLC25A22-uniprot.txt "Mitochondrial glutamate/H(+)
  symporter. Responsible for the"] and [file:human/SLC25A22/SLC25A22-uniprot.txt "transport
  of glutamate from the cytosol into the mitochondrial matrix"].
- UniProt names: [file:human/SLC25A22/SLC25A22-uniprot.txt "AltName: Full=Glutamate/H(+)
  symporter 1;"].
- UniProt CATALYTIC ACTIVITY (Rhea RHEA:70955): [file:human/SLC25A22/SLC25A22-uniprot.txt
  "Reaction=L-glutamate(in) + H(+)(in) = L-glutamate(out) + H(+)(out);"]. This is a
  transport reaction, not an enzymatic/bond-forming reaction — the protein is a transporter,
  not a catalytic enzyme.

Primary experimental characterization: Fiermonte et al. 2002 (PMID:11897791). The two human
glutamate carrier isoforms (GC1 = SLC25A22, GC2 = SLC25A18) were bacterially expressed,
reconstituted into liposomes, and shown to be **glutamate/H+ symporters**
[PMID:11897791 "Glutamate is co-transported with H(+) (or exchanged for OH(-))"] and
[PMID:11897791 "the two proteins are isoforms of the glutamate/H(+) symporter described in
the past in whole mitochondria"]. KM ~4.85 mM for glutamate [file:...SLC25A22-uniprot.txt
"KM=4.85 mM for glutamate"]. This is the source of the IDA MF/BP/CC annotations
(GO:0005313 L-glutamate transmembrane transporter activity; GO:0005280 amino acid:proton
symporter activity; GO:0015813 L-glutamate transmembrane transport; GO:0005743
mitochondrial inner membrane).

The paper notes the two ESTs are **related to** the aspartate-glutamate carrier
[PMID:11897791 "related to \nthe aspartate-glutamate carrier, a member of the carrier
family"], but the demonstrated activity is glutamate/H+ symport, not aspartate transport.

## Aspartate annotations are over-annotations

GC1 is a glutamate-specific (glutamate/H+) symporter. The aspartate transporter/transport
annotations (GO:0015183 L-aspartate transmembrane transporter activity IBA; GO:0015810
aspartate transmembrane transport IBA; GO:0070778 L-aspartate transmembrane transport IEA)
arise from phylogenetic (IBA) propagation across the broader mitochondrial-carrier /
aspartate-glutamate-carrier clade and inter-ontology inference, not from measured aspartate
transport by SLC25A22. Neither the UniProt FUNCTION/CATALYTIC ACTIVITY nor the Fiermonte
primary paper attributes aspartate transport to GC1; UniProt records only the glutamate/H+
reaction. Marked as over-annotated (aspartate transport belongs to the aspartate-glutamate
carriers SLC25A12/SLC25A13, not to the glutamate carriers).

## Malate-aspartate shuttle

GC1 participates in the malate-aspartate shuttle indirectly by carrying the glutamate/H+
import leg. Reactome's MAS description makes this the glutamate coimport step
[R-HSA-9856872 "aspartate (L-Asp) gets exported and transaminated to glutamate (L-Glu),
which subsequently gets coimported with a proton and transaminated back"]. Kept as a
non-core downstream/pathway process (the core molecular activity is glutamate/H+ symport).

## Neurotransmitter transport

GO:0006836 (neurotransmitter transport, TAS Reactome:R-HSA-442660) is an over-annotation.
The Reactome node R-HSA-442660 is about the SLC6 family plasma-membrane neurotransmitter
transporters [R-HSA-442660 "The SLC6 gene family encodes proteins that mediate
neurotransmitter uptake thus terminating a synaptic signal"], a different process from
SLC25A22's mitochondrial inner-membrane glutamate/H+ symport. GC1 handles glutamate as a
mitochondrial metabolite, not as a synaptic neurotransmitter being cleared from the cleft.

## Insulin secretion / proton transport

- GO:0050796 regulation of insulin secretion (ISS/IEA, By similarity to rat A0A0G2K5L2):
  UniProt: [file:human/SLC25A22/SLC25A22-uniprot.txt "Plays a role\nin the control of
  glucose-stimulated insulin secretion (By similarity)"]. Non-core (physiological role by
  similarity; expressed in pancreas).
- GO:1902600 proton transmembrane transport (IEA, inferred from GO:0005280): consistent with
  the co-transported proton in the symport reaction; non-core mechanistic component.
- GO:0055085 transmembrane transport (IEA InterPro): correct but generic; non-core.

## Localization

Mitochondrion inner membrane [file:human/SLC25A22/SLC25A22-uniprot.txt "SUBCELLULAR
LOCATION: Mitochondrion inner membrane"], multi-pass. Supported by IDA (PMID:11897791),
ISS, IEA, Reactome TAS, and HTP mitochondrial-proteome mass-spec (PMID:34800366, HTP =>
mitochondrion). GO:0005743 (mitochondrial inner membrane) is the specific, core location;
GO:0005739 (mitochondrion) is the less-specific HTP location.

## Tissue expression and disease

- Expressed at high levels in brain, liver, pancreas [file:human/SLC25A22/SLC25A22-uniprot.txt
  "Expressed at high levels in brain, liver, and\npancreas"].
- Disease: Developmental and epileptic encephalopathy 3 (DEE3 / EIEE3; MIM:609304), autosomal
  recessive, a severe early-onset neonatal epilepsy (migrating partial seizures of infancy /
  neonatal myoclonic epilepsy) [file:human/SLC25A22/SLC25A22-uniprot.txt "Developmental and
  epileptic encephalopathy 3 (DEE3)"]. The DEE3 variant Pro206Leu disrupts L-glutamate
  transport [file:human/SLC25A22/SLC25A22-uniprot.txt "P -> L (in DEE3; disrupts L-glutamate
  transporter"], establishing loss of glutamate/H+ transport as the disease mechanism
  (Molinari et al. 2005, PMID:15592994; UniProt reference [8]). PMID:15592994 is not in the
  local publications cache, so it is cited from the UniProt record rather than quoted.

## Core function synthesis

- Core MF (mechanism): GO:0005280 amino acid:proton symporter activity (captures the coupled
  H+/glutamate symport; under symporter activity / solute:proton symporter activity).
- Core MF (substrate specificity): GO:0005313 L-glutamate transmembrane transporter activity.
- Core BP: GO:0015813 L-glutamate transmembrane transport.
- Core location: GO:0005743 mitochondrial inner membrane.

No dedicated "glutamate:proton symporter activity" GO term exists (checked OLS), so the pair
GO:0005280 + GO:0005313 is the most specific available representation. No catalytic/enzymatic
MF is assigned — SLC25A22 is a transporter.
