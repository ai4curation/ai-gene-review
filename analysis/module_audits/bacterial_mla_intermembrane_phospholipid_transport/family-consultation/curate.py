"""Apply explicit family-scope adjudications to the captured original documents."""

import copy
import json
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
BASE = json.loads((HERE / "baseline.json").read_text())
DOCS = {
    Path(p).parent.name: copy.deepcopy(v["document"])
    for p, v in BASE["reviews"].items()
}
ARCHIVE = []
CURRENT = []
CHANGES = []


def term(family, go, reason, scope="UNRESOLVED"):
    t = next(
        t for t in DOCS[family]["term_assessments"] if t["assessed_term"]["id"] == go
    )
    CHANGES.append(
        {"family": family, "term": go, "before": copy.deepcopy(t), "new_scope": scope}
    )
    for exception in t.get("member_exceptions", []):
        ARCHIVE.append(
            {
                "family": family,
                "term": go,
                "original_exception": copy.deepcopy(exception),
            }
        )
        supported = family == "PTHR30188" and go == "GO:0005886"
        CURRENT.append(
            {
                "family": family,
                "term": go,
                "member": exception["member"],
                "status": "CURRENT_SUPPORTED_NEGATIVE"
                if supported
                else "WITHDRAWN_TO_UNRESOLVED",
                "assessment": "LOSS_SUPPORTED" if supported else "UNRESOLVED",
                "reason": (
                    "TGD1 has experimentally supported chloroplast-envelope localization. The original live LOSS_SUPPORTED IRD at PTN001575509 remains unchanged; a family-wide plasma-membrane grant cannot cover the other 49 plant leaves. Production does not allow member_exceptions under UNRESOLVED, so this current ledger preserves the member judgment while PAINT retains the loss."
                    if supported
                    else "The characterized alternate cargo or compartment does not establish absence of a secondary phospholipid activity. GO0120010 does not require a bacterial diderm envelope. The original negative object is archived exactly, but it is not retained as a biological loss claim."
                ),
                "supported_by": copy.deepcopy(exception.get("supported_by", [])),
            }
        )
    t["scope"] = scope
    t["scope_reason"] = reason
    t.pop("applicable_subfamilies", None)
    t.pop("member_exceptions", None)


def node(family, ptn, go, reason, assessment="UNRESOLVED"):
    n = next(
        n
        for n in DOCS[family]["node_assessments"]
        if n["node_id"] == "PANTHER:" + ptn and n["asserted_term"]["id"] == go
    )
    n["assessment"] = assessment
    n["assessment_reason"] = reason


def sub(family, sf):
    return next(
        s for s in DOCS[family]["subfamilies"] if s["subfamily_id"].endswith(":" + sf)
    )


def add_ref(family, pmid):
    doc = DOCS[family]
    rid = "PMID:" + pmid
    if any(r["id"] == rid for r in doc["references"]):
        return
    text = (ROOT / f"publications/PMID_{pmid}.md").read_text()
    meta = yaml.safe_load(text.split("---", 2)[1])
    doc["references"].append({"id": rid, "title": meta["title"]})


def support(pmid, quote):
    return {"reference_id": "PMID:" + pmid, "supporting_text": quote}


# A: the positive MlaA clade is real, but the divergent SF1 is not a demonstrated loss.
a = DOCS["PTHR30035"]
a["summary"] = (
    "MlaA/VacJ-related proteins include canonical outer-membrane MlaA lipoproteins in SF3 and a divergent, longer SF1 group with an alpha/beta-hydrolase-fold region. E. coli MlaA forms a phospholipid-handling channel with OmpC/OmpF and loads the soluble carrier MlaC. Pseudomonas and Bordetella exemplars have compatible MlaA domain assignments, but their exact porin partner and native transfer kinetics are not established by the E. coli assays. SF1 function remains unresolved; its different architecture is not a demonstrated loss of every Mla-associated function."
)
a["coherence_reason"] = (
    "The official reference tree places the existing intermembrane-transfer IBD at PTN001247191 on the 12 SF3 leaves, outside the three SF1 leaves. This supports the positive MlaA clade without making an unsupported negative assertion about SF1. Broader classification counts are not experimental evidence."
)
for go in ["GO:0120010", "GO:0009279"]:
    term(
        "PTHR30035",
        go,
        "Canonical SF3 MlaA has positive structural, localization and lipid-handling evidence, including the E. coli source and reviewed Pseudomonas/Bordetella homologs. SF1 has different architecture and an unresolved function. Because SUBFAMILY_ONLY would also exclude any true assertion outside SF3, universal scope is left unresolved rather than converting lack of characterization into a loss. Use exact positive MlaA members, domain architecture and compatible envelope context; the existing SF3 PAINT gain remains SOUND.",
    )
sub("PTHR30035", "SF1")["divergence_description"] = (
    "SF1 differs in architecture (longer proteins with an alpha/beta-hydrolase-fold region and without the canonical PF04333 match). Its physiological function, localization and possible relationship to adjacent SF3 paralogs remain unresolved. This is not a negative assay or a phylogenetic loss assertion."
)
a["notes"] = (
    "2026-11-07 audit: official tree/MSA and exact target membership are captured in analysis/module_audits/bacterial_mla_intermembrane_phospholipid_transport/family-consultation. The original PAINT node object is preserved. Classification as SF3 does not by itself prove a compatible complete transport panel or a universal OmpC/OmpF partner."
)

# C: positive carrier chemistry is firm; reference-family coverage is not exclusively bacterial.
c = DOCS["PTHR36573"]
c["functional_coherence"] = "MOSTLY_COHERENT"
c["summary"] = (
    "MlaC-family proteins include the soluble periplasmic phospholipid carriers of characterized bacterial Mla systems. Their hydrophobic cavity shields lipid acyl chains, and contacts with outer-membrane lipid-loading complexes and the MlaD-containing inner-membrane complex support transfer. E. coli, P. putida KT2440 and P. aeruginosa PAO1 structures or ligand measurements support carrier function; PAO1 Ttg2D can carry two diacyl phospholipids or one cardiolipin. Cargo occupancy, individual handoff and ATP-biased transfer are distinct measurements. The reference family also contains non-bacterial-labelled leaves, so neither a bacterial periplasm nor the complete Mla route is automatically licensed across the entire family."
)
c["coherence_reason"] = (
    "The 13-leaf official reference tree includes Nematostella A8DVR8 and the inactive Ricinus accession B9TGW9, both in SF1. Current UniProt confirms the A8DVR8 classification but does not establish a bacterial periplasm or Mla pathway for it. These may involve annotation or assembly issues; they are unresolved, not experimentally established alternative activities. Bacterial carrier positives remain intact."
)
for go in ["GO:0120010", "GO:0030288", "GO:0005543"]:
    term(
        "PTHR36573",
        go,
        "Positive bacterial MlaC/Ttg2D exemplars have independent structural, ligand-binding and transfer evidence. The family/SF1 reference tree also contains non-bacterial-labelled A8DVR8 and inactive B9TGW9; their cellular context and activity are unresolved. Do not raise a bacterial periplasm or route assertion to the family root solely from the shared pocket or one-subfamily classification. This does not negate the positive bacterial members or infer loss on the unresolved leaves.",
    )
for go in ["GO:0030288", "GO:0120010"]:
    node(
        "PTHR36573",
        "PTN002195249",
        go,
        "The existing gain covers the three enterobacterial reference leaves (E. coli, Salmonella and Yersinia), consistent with the experimentally characterized periplasmic carrier. Retain this placement. Positive Pseudomonas carrier evidence supports those targets independently, but does not justify moving the gain indiscriminately to a root containing unresolved non-bacterial-labelled leaves.",
        "SOUND",
    )
c["notes"] = (
    "2026-11-07 audit distinguishes measured binding from transfer: PMID28388411 uses biolayer interferometry for MlaC interaction with MlaFEDB and MlaA-OmpF; its handoff sentence is a model. PMID34873038 directly tests lipid exchange and ATP-dependent retrograde bias. PMID33837253 distinguishes native PAO1 periplasmic cargo from heterologous structural material. Pseudomonas and Bordetella target classifications are independently recorded; lack of a curated reference-tree leaf is not lack of family membership."
)
add_ref("PTHR36573", "34873038")

# F: keep ABC ATP chemistry, distinguish substrate scope and the real SF4 branch.
f = DOCS["PTHR43023"]
f["summary"] = (
    "Stand-alone ABC nucleotide-binding proteins include MlaF, the shared mycobacterial MceG ATPase, plant TGD3 and additional ABC proteins. MlaF supplies ATP-dependent energy to MlaE-containing phospholipid transport assemblies; E. coli MlaB stabilizes the ATPase and supports complex assembly, whereas Bordetella has a characterized F/E/D/A/C locus without an identifiable MlaB. MceG supports fatty-acid and cholesterol uptake systems and TGD3 acts in chloroplast lipid transport. These positive cargo examples do not establish absence of secondary activities. The official SF4 reference branch and current UniProt assignments disagree for some proteins, so neither lipid specificity nor a universal six-component architecture follows from the family label."
)
f["coherence_reason"] = (
    "The ABC fold and ATP motifs are conserved in the official MSA: all 90 extant reference sequences have a Walker-A candidate, and all four SF4 leaves also have LSGGQ. Cargo and partners differ, and SF4 is not an empty branch. Reference-tree classifications of Q9F3K7 and Q2FVL4 as PTHR43023:SF4 disagree with current UniProt PTHR43166 classifications; both sources are retained without an override."
)
sub("PTHR43023", "SF4")["description"] = (
    "The official PANTHER19 tree has four SF4 leaves: Streptomyces atrC Q9F3K7, Bradyrhizobium Q89T24, Staphylococcus Q2FVL4 and Yersinia yecC A0A3N4B1K8. The MSA preserves ABC Walker-A and signature motifs. Current UniProt assigns Q9F3K7 and Q2FVL4 to PTHR43166, a source disagreement rather than evidence that the PANTHER tree is absent. Exact lipid substrate and Mla participation are not established for this branch."
)
sub("PTHR43023", "SF3")["divergence_description"] = (
    "Plant TGD3 and bacterial paralogs share SF3. TGD3 has organellar localization and basal ATPase activity; its chloroplast lipid route differs from bacterial Mla. GO0120010 itself permits transfer between organellar membranes, so TGD3 cannot be excluded merely because it is not in a bacterial diderm. Bacterial SF3 paralogs do not inherit a chloroplast location from their subfamily name."
)
term(
    "PTHR43023",
    "GO:0006869",
    "MlaF, MceG and TGD3 positively support lipid transport in their respective systems, but the official SF4 reference branch includes additional ABC proteins and source-disputed classifications. Their exact cargo is unresolved here; ATPase architecture does not establish lipid transport for every member.",
)
for go in ["GO:0120014", "GO:0120010"]:
    term(
        "PTHR43023",
        go,
        "MlaF supplies the ATP-dependent contribution to phospholipid transport in its assembled transporter; an isolated ATPase is not thereby a complete aqueous-phase carrier. MceG fatty-acid/cholesterol chemistry and TGD3 organellar context neither establish the same Mla role nor prove absence of secondary phospholipid function. SF6 mixes MlaF/MceG, SF3 mixes TGD3/bacterial proteins and SF4 has additional ABC members. No supported universal gain or substrate-loss boundary follows from those labels. GO0120010 is not restricted to bacterial diderms.",
    )
term(
    "PTHR43023",
    "GO:0009507",
    "The original Viridiplantae PAINT node PTN005140750 remains SOUND, with positive TGD3 localization. SF3 also contains bacterial proteins, so a whole-SF3 chloroplast grant would be wrong. A taxon-qualified clade cannot be represented as an entire subfamily here; universal scope is unresolved, not a withdrawal of plant localization evidence.",
)
node(
    "PTHR43023",
    "PTN000655692",
    "GO:0120014",
    "The root contains ABC ATPases with different partners/cargo and a source-disputed SF4 branch. MlaF provides an ATP-coupled complex contribution; it is not an autonomous aqueous-phase lipid carrier. MceG fatty-acid/cholesterol activity does not independently establish a phospholipid-loss node. Retain the IBD payload but leave the scope and any proposed pruning unresolved.",
)
node(
    "PTHR43023",
    "PTN000655692",
    "GO:0006869",
    "MlaF, TGD3 and MceG are positive lipid-transport anchors. The actual root also contains four SF4 reference leaves whose cargo is not established here and whose current UniProt classifications partly disagree with the tree. Keep the source assertion unchanged, but do not license every ABC protein as lipid-transporting on the basis of those three anchors alone.",
)
node(
    "PTHR43023",
    "PTN000655704",
    "GO:0120010",
    "This node covers 18 SF6 reference leaves, including MlaF and MceG. E. coli transport evidence supports MlaF; MceG has positive fatty-acid/cholesterol roles but no target-negative phospholipid assay establishing a loss. GO0120010 describes transfer between membranes without imposing a diderm-only or bacterial-only restriction. Pruning requires a supported functional boundary, which is unresolved here.",
)
for pm in ["32602838", "36518166"]:
    add_ref("PTHR43023", pm)
f["notes"] = (
    "2026-11-07: original PAINT payloads, dates and unrelated plant-location/P-type-term judgments are preserved. Current tree/MSA and classification disagreements are archived in the consultation. ATP motifs support the conserved ATPase genus, not substrate specificity. Former substrate-based member exceptions are archived exactly and reassessed as unresolved secondary activity. MlaB requirement is lineage/context-dependent: E. coli assembly phenotypes and Bordetella no-identifiable-B architecture are distinct evidence. No universal B dispensability or whole-pathway direction is inferred."
)

# E: preserve the genuine plant localization loss, not an invented phospholipid loss.
e = DOCS["PTHR30188"]
e["summary"] = (
    "MlaE-related polytopic permeases form membrane components of ABC-associated lipid transport assemblies. E. coli MlaE pairs with MlaF ATPases and the MlaD ring; the mycobacterial YrbE paralogs occur in fatty-acid/cholesterol uptake systems, and plant TGD1 acts at the chloroplast envelope. The family and SF4 therefore mix cargo and cellular contexts. Characterized alternate substrates are positive biology, not proof that every secondary phospholipid activity is absent. Bacterial Mla roles require a compatible cargo, partner and envelope context in addition to classification."
)
sub("PTHR30188", "SF14")["description"] = (
    "The official reference tree contains Brassica campestris M4EAG1 and Brassica napus A0A078JTY8 in SF14; current UniProt confirms M4EAG1. They lie below the existing plant plasma-membrane IRD. The earlier empty-branch assumption was incorrect; exact transporter substrate in these members is not newly assayed here."
)
term(
    "PTHR30188",
    "GO:0005886",
    "Bacterial MlaE/YrbE plasma-membrane localization remains supported, and the original plant LOSS_SUPPORTED IRD PTN001575509 is retained unchanged. Its actual 50-leaf plant clade spans SF4 and SF14. A family-wide grant with one Arabidopsis exception would falsely license other plants, while an entire-SF exclusion would lose bacterial positives. The exact Q8L4R0 negative remains CURRENT_SUPPORTED_NEGATIVE in the consultation ledger because production forbids live member_exceptions under UNRESOLVED. The PAINT loss remains machine-readable in this review.",
)
for go in ["GO:0015914", "GO:0120010"]:
    term(
        "PTHR30188",
        go,
        "Canonical MlaE contributes to phospholipid transport and TGD1 participates in chloroplast lipid transport. Mycobacterial YrbE1A/4A have positive fatty-acid/cholesterol uptake evidence, which does not prove absence of all secondary phospholipid transport. GO0120010 is not defined as bacterial diderm maintenance. SF4 mixes these contexts, SF3 has other bacterial paralogs and SF14 contains plant members; no exclusive subfamily or loss boundary is established here.",
    )
node(
    "PTHR30188",
    "PTN000766204",
    "GO:0015914",
    "The root includes bacterial MlaE, mycobacterial YrbE and plant TGD1. The positive Mla/TGD phospholipid evidence is retained. YrbE1A fatty-acid and YrbE4A cholesterol uptake do not demonstrate inability to transport phospholipids, so the earlier proposed substrate-loss pruning is not justified by those assays alone. Resolve substrate scope without inventing an IRD; retain the exact source payload.",
)
e["notes"] = (
    "2026-11-07 official tree/MSA audit preserves the exact plasma-membrane gain and plant LOSS_SUPPORTED objects. The supported TGD1 negative is current in the member ledger, not merely historical. Prior substrate-negative exception objects are archived with explicit reassessment. P-type GO1990531 exclusion remains unchanged. Family/subfamily membership is separate from exact Mla route licensing."
)

# D: MCE assembly and measured binding are not universal full-carrier chemistry.
d = DOCS["PTHR33371"]
d["summary"] = (
    "MCE-domain proteins include the MlaD hexameric phospholipid-binding component and the differentiated MceA-F proteins of mycobacterial lipid import assemblies. E. coli MlaD binds phospholipids, contacts MlaC and caps the MlaE membrane component; the assembled system supports transfer and ATP-dependent retrograde bias. Mycobacterial Mce complexes have distinct fatty-acid/cholesterol uptake roles and extended envelope-spanning architecture. SF4 contains both MlaD and mycobacterial MceD, so an MCE domain or shared subfamily does not identify the Mla substrate or compatible partners. Positive alternate cargo does not establish a secondary phospholipid loss."
)
term(
    "PTHR33371",
    "GO:0005319",
    "A lipid carrier must directly bind lipid and deliver it to an acceptor. MlaD binding and complex transfer are supported, but individual roles in differentiated Mce heteroassemblies cannot all be equated with an autonomous carrier from the shared MCE fold. Preserve positive complex contribution and measured binding; universal individual carrier activity is unresolved.",
)
for go in ["GO:0005543", "GO:0120014", "GO:0120010"]:
    term(
        "PTHR33371",
        go,
        "E. coli MlaD has measured phospholipid binding and participates in lipid handoff through the Mla complex. Positive Mce1 fatty-acid and Mce4 cholesterol roles do not by themselves establish a secondary phospholipid-negative assay or a loss at the mixed SF4 boundary. GO0120014 describes membrane removal, aqueous shielding and delivery; complete activity is assigned at the assembled-system level with positive subunit contributions, rather than rejected from an inert enables qualifier. No exclusive subfamily grant or substrate-loss boundary is currently warranted.",
    )
term(
    "PTHR33371",
    "GO:0009274",
    "Retain the existing actinobacterial cell-wall PAINT node unchanged. Its 30 reference leaves include the five specialized subfamilies AND six SF4 MceD relatives; excluding all SF4 would contradict the node. The mixed SF4 also contains periplasmic MlaD proteins. A full-subfamily grant/exclusion cannot express this clade, so universal term scope is unresolved while the supported clade assertion remains intact.",
)
for go in ["GO:0120014", "GO:0120010"]:
    node(
        "PTHR33371",
        "PTN002120837",
        go,
        "The root includes MlaD and differentiated mycobacterial Mce proteins. E. coli binding and transfer work positively supports the MlaD contribution. Fatty-acid/cholesterol uptake by other Mce assemblies does not establish loss of secondary phospholipid function, and GO0120010 has no diderm-only restriction. Keep the original IBD payload; the substrate-specific universal scope and proposed pruning are unresolved, not disproved by donor counts or by absence of an isolated-subunit assay.",
    )
d["notes"] = (
    "2026-11-07 audit targets Mla-specific functional boundaries. Exact original PAINT payloads and unrelated plasma-membrane, actinobacterial cell-wall and host-entry node judgments are retained; the older host-entry judgment is not independently re-adjudicated in this bounded Mla consultation. Former phospholipid-negative exceptions are archived and explicitly withdrawn to uncertainty. Pqi/Let and generic MCE architecture are not substitutes for positively qualified MlaD. No causal specificity residues are inferred from the alignment."
)

# B: correct contribution reasoning and lineage-specific requirement; keep unrelated negative judgment.
b = DOCS["PTHR35849"]
b["summary"] = (
    "Small STAS-domain proteins include MlaB, an assembly and regulatory component of characterized bacterial Mla transporters, and a broader unresolved group. E. coli MlaB binds and stabilizes MlaF and supports transporter assembly and ATPase behavior; this provides a positive contribution to the lipid-transfer system without making MlaB a lipid-binding carrier. Overexpressed MlaF can compensate MlaB deletion under tested E. coli conditions. Bordetella has a characterized five-gene Mla locus without an identifiable MlaB, so neither universal B dependence nor universal dispensability follows. Pseudomonas Ttg2E now has an official SF1 classification, while its function is still a target-scoped ortholog inference."
)
b["coherence_reason"] = (
    "The reference tree separates seven SF1 MlaB leaves from nine SF2 leaves of unresolved physiology. Current UniProt now classifies Q88P90 in SF1, unlike the immutable older target flatfile. STAS architecture does not by itself establish Mla participation for every member or exclude it outside the characterized branch."
)
term(
    "PTHR35849",
    "GO:0120010",
    "E. coli MlaB supplies real assembly/ATPase support to the Mla process; the contribution is not inferred merely from being necessary or from complex membership alone. Canonical SF1 positives and current Q88P90 classification support target-scoped inference. Uncharacterized SF2 physiology and cross-lineage B-independent architectures prevent a universal or exclusionary subfamily grant; neither proves absence of Mla-related function in every SF2 member.",
)
term(
    "PTHR35849",
    "GO:0120014",
    "MlaB binds/stabilizes MlaF and supports assembly and ATPase behavior, providing a positive complex-level contribution. It is not known to execute the complete GO0120014 sequence of lipid removal, aqueous shielding and delivery as a carrier. This distinction rests on measured physical roles and the term definition, not the inert enables qualifier or a requirement for an isolated-subunit assay. Universal full transfer activity across the mixed STAS family is unresolved.",
)
node(
    "PTHR35849",
    "PTN002185077",
    "GO:0120014",
    "The SF1 MlaB clade is compatible with a positive assembly/ATPase contribution to Mla-mediated transfer. The exact term describes lipid removal, aqueous shielding and delivery; MlaB is a MlaF-binding assembly/regulatory component, not a demonstrated lipid carrier. Retain the original assertion as source history while leaving the full activity scope unresolved; do not argue from inert qualifier wording alone.",
)
for pm in ["32602838", "36518166"]:
    add_ref("PTHR35849", pm)
b["notes"] = (
    "2026-11-07 current official Q88P90 record assigns PTHR35849:SF1; the older immutable target flatfile has no PANTHER DR line. Both are recorded in the consultation with dates/hashes, without refreshing source caches. ECOLI and PSEPK representatives therefore have current SF1 support, but STAS membership is not an activity license. The original DNA-damage negative node/term judgment and P-type-complex exclusion are preserved, outside the bounded Mla-role revision. No claim is made that Bordetella lacks every possible functional substitute for MlaB."
)

sub("PTHR36573", "SF1")["description"] = (
    "The only classified subfamily includes experimentally characterized bacterial MlaC/Ttg2D carriers, as well as unresolved non-bacterial-labelled reference leaves. Shared pocket architecture supports comparison; periplasmic localization and full-route participation remain context dependent."
)
sub("PTHR35849", "SF1")["description"] = (
    "Canonical MlaB STAS proteins include the E. coli MlaF-binding assembly/regulatory component and current UniProt-classified Q88P90. Requirement depends on expression and lineage; ATPase overexpression rescue and Bordetella architecture preclude an unconditional family-level essentiality claim."
)
term(
    "PTHR35849",
    "GO:0006974",
    "The full E. coli PMID20128927 study measures genotoxic survival with wild-type bacteriostatic susceptibility controls and complementation. This is real evidence, but whether MlaB executes a damage-response step or supplies constitutive envelope protection is unresolved. The broad GO definition is not limited to direct DNA repair, and neither protein localization nor lack of a DNA-binding domain disproves it. Do not propagate a universal positive or negative across the STAS family.",
)
node(
    "PTHR35849",
    "PTN002185077",
    "GO:0006974",
    "The inherited E. coli stress study provides actual genotoxic survival and complementation evidence, not a demonstrated negative assay. It does not resolve whether MlaB participates in a damage-triggered response or provides constitutive envelope protection. GO0006974 is broader than direct DNA repair. Retain the exact IBD payload but withdraw the categorical WRONG_NODE judgment to UNRESOLVED; no loss or family-wide exclusion is established.",
)
b["notes"] = b["notes"].replace(
    "The original DNA-damage negative node/term judgment and P-type-complex exclusion are preserved, outside the bounded Mla-role revision.",
    "The original DNA-damage negative node/term judgments are archived exactly and explicitly superseded by uncertainty after full-source reassessment; the P-type-complex exclusion is preserved.",
)

# Add source-exact evidence for new contextual claims, preserving all existing supports.
for fam in ["PTHR43023", "PTHR35849"]:
    for pm, quote in [
        ("36518166", "we were not able to identify an MlaB homologue in B. pertussis"),
        ("32602838", "can be rescued by overexpression of either WT MlaB or MlaF"),
    ]:
        r = next(r for r in DOCS[fam]["references"] if r["id"] == "PMID:" + pm)
        target = next(
            t
            for t in DOCS[fam]["term_assessments"]
            if t["assessed_term"]["id"] == "GO:0120010"
        )
        target.setdefault("supported_by", []).append(support(pm, quote))

# Append verified target exemplars without changing any existing member object.
for fam, sf, accession, org, gene in [
    ("PTHR30035", "SF3", "Q7VSZ7", "BORPE", "BP3760"),
    ("PTHR36573", "SF1", "Q7VSZ6", "BORPE", "BP3761"),
    ("PTHR36573", "SF1", "Q9HVW4", "PSEAE", "ttg2D"),
    ("PTHR43023", "SF6", "Q7VT00", "BORPE", "BP3757"),
    ("PTHR30188", "SF4", "Q7VSZ9", "BORPE", "BP3758"),
    ("PTHR33371", "SF4", "Q7VSZ8", "BORPE", "BP3759"),
    ("PTHR35849", "SF1", "Q88P90", "PSEPK", "ttg2E"),
]:
    ref = {
        "id": "UniProtKB:" + accession,
        "gene_symbol": gene,
        "organism": {
            "BORPE": "Bordetella pertussis (strain Tohama I)",
            "PSEAE": "Pseudomonas aeruginosa (strain PAO1)",
            "PSEPK": "Pseudomonas putida (strain KT2440)",
        }[org],
        "gene_review": f"genes/{org}/{gene}/{gene}-ai-review.yaml",
    }
    sub(fam, sf).setdefault("representative_members", []).append(ref)

for fam, doc in DOCS.items():
    path = ROOT / f"interpro/panther/{fam}/{fam}-review.yaml"
    path.write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=True, width=100))
(HERE / "original-member-exceptions.json").write_text(
    json.dumps(ARCHIVE, indent=2) + "\n"
)
(HERE / "current-member-assessments.json").write_text(
    json.dumps(CURRENT, indent=2) + "\n"
)
(HERE / "scope-changes.json").write_text(json.dumps(CHANGES, indent=2) + "\n")
print(
    "updated",
    len(DOCS),
    "scope changes",
    len(CHANGES),
    "archived exceptions",
    len(ARCHIVE),
)
