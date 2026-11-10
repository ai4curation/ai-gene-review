# Por (rat NADPH--cytochrome P450 reductase, P00388): manual literature synthesis

No deep-research API was available for this review. This file summarises the cached
publications (`publications/PMID_*.md`) and the UniProt record, read by the reviewer.
Most cached papers are abstract-only; PMID:19152507, PMID:19077323 and PMID:17446262
have full text.

## Identity and structure

- Rat liver CPR (Por, UniProt P00388, RGD:68335, GeneID 29441) is the protein whose
  crystal structure defined the diflavin reductase fold
  [PMID:9237990 "The structure of rat liver CPR, expressed in Escherichia coli and solubilized by limited trypsinolysis, has been determined by x-ray crystallography at 2.6 A resolution."].
- Domain order: FMN-binding (flavodoxin-like), connecting, FAD- and NADPH-binding
  domains [PMID:9237990 "The molecule is composed of four structural domains: (from the N- to C- termini) the FMN-binding domain, the connecting domain, and the FAD- and NADPH-binding domains."].
- It is one of two mammalian FAD+FMN enzymes, the other being NOS
  [PMID:9237990 "Microsomal NADPH-cytochrome P450 reductase (CPR) is one of only two mammalian enzymes known to contain both FAD and FMN, the other being nitric-oxide synthase."].
- Membrane anchoring through an N-terminal hydrophobic segment; cleavage at Lys56-Ile57
  releases a soluble catalytic domain that no longer reduces P450
  [PMID:15823091 "NADPH-cytochrome P450 reductase (CPR) is a membrane-bound flavoprotein that interacts with the membrane via its N-terminal hydrophobic sequence (residues 1-56)."].
- UniProt: single-pass ER membrane protein, cytoplasmic side (HAMAP MF_03212).

## Catalytic function

- Electron transfer from NADPH via FAD and FMN to all microsomal P450s
  [PMID:19171935 "NADPH-cytochrome P450 oxidoreductase (CYPOR) catalyzes the transfer of electrons to all known microsomal cytochromes P450."].
  The FMN domain swings away from FAD in an open conformation to dock with partners
  [PMID:19171935].
- Partners besides P450: heme oxygenase-1 [PMID:16928691, PMID:15516695], cytochrome b5
  [PMID:16055078 "Electron transfer to b5 is rapid within this complex (>30 s(-1) at 23 degrees C), as fast as to cytochrome c."],
  and the artificial acceptor cytochrome c used in the standard assay [PMID:9774150].
- Partner docking surface near FMN [PMID:9237990 "The bowl-shaped surface near the FMN-binding site is likely the docking site of cytochrome c and the physiological redox partners, including cytochromes P450 and b5 and heme oxygenase."].
- Binding to P450s measured directly [PMID:15680923; PMID:17446262 (rat CPR with human CYP2C9); PMID:11350928 (mitochondria-targeted CYP1A1 helix G residues)].

## Side reactions and system-level roles

- Organic nitrate (GTN) reduction to nitrite by purified CPR [PMID:16527817 "Therefore, CPR catalyzes organic nitrate reduction, producing nitrite, whereas CP can mediate further nitrite reduction to NO."; PMID:9774150].
- Oxidative aldehyde deformylation is driven by CPR-generated H2O2, not hydrolysis [PMID:16226717].
- NO consumption by rat brain membranes requires CPR and is inhibited by P450 inhibitors;
  purified CPR alone needs Trolox, so a partner (probably a P450) performs the NO chemistry
  [PMID:19152507 "Hence, it appears that, during the purification process, CYPOR becomes separated from a partner needed for NO consumption."].
- Steroidogenesis: POR expression raises aromatase output of estrone in COS-7 cells and is
  induced by gonadotropins/FSH in rat ovary and granulosa cells [PMID:19077323].
- Chondrocyte siRNA knockdown reduces proliferation/differentiation via loss of cholesterol
  and Ihh, an indirect consequence of impaired sterol synthesis [PMID:19264869].

## Regulation of expression (IEP-type data)

- Induced by dexamethasone mainly via PXR [PMID:27856527]; reduced by hypophysectomy and
  restored by thyroxine [PMID:2495435]; altered by anesthetics [PMID:19265259] and by
  L-carnitine [PMID:16616465].
