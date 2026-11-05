# /// script
# requires-python = ">=3.10"
# dependencies = ["gemmi"]
# ///
"""Count contacts between C. elegans uS13 (RPS-18, O18240) and RNA chains in PDB 9CAI.

Usage: uv run --script us13_contacts.py [path/to/9CAI.cif.gz]
If no path is given, the mmCIF is downloaded from RCSB into a temporary directory.
The uS13 chain is identified from the mmCIF entity/UniProt mapping (O18240), not hardcoded.
"""
import sys, tempfile, urllib.request, os, collections
import gemmi

PDB = "9CAI"
ACC = "O18240"
CUTOFF = 4.0

def get_path():
    if len(sys.argv) > 1:
        return sys.argv[1]
    d = tempfile.mkdtemp()
    p = os.path.join(d, f"{PDB}.cif.gz")
    urllib.request.urlretrieve(f"https://files.rcsb.org/download/{PDB}.cif.gz", p)
    return p

path = get_path()
doc = gemmi.cif.read(path)
block = doc.sole_block()
# map entity id -> UniProt accession via struct_ref
ref = block.find("_struct_ref.", ["entity_id", "pdbx_db_accession", "db_name"])
ent_acc = {r[0]: r[1] for r in ref}
# map entity -> description
ent = block.find("_entity.", ["id", "pdbx_description", "type"])
ent_desc = {r[0]: (r[1], r[2]) for r in ent}
poly = block.find("_entity_poly.", ["entity_id", "type"])
ent_polytype = {r[0]: r[1] for r in poly}

st = gemmi.make_structure_from_block(block)
st.setup_entities()
model = st[0]
target_entity = [e for e, a in ent_acc.items() if a == ACC]
print(f"Entities mapped to {ACC}: {target_entity} {[ent_desc.get(e) for e in target_entity]}")
chain_entity = {}
for e in st.entities:
    for sub in e.subchains:
        chain_entity[sub] = e.name
target_chains = set()
rna_chains = {}
for ch in model:
    sub = ch.get_polymer().subchain_id() if len(ch.get_polymer()) else None
    en = chain_entity.get(sub)
    if en in target_entity:
        target_chains.add(ch.name)
    if en and "ribonucleotide" in ent_polytype.get(en, ""):
        rna_chains[ch.name] = ent_desc.get(en, ("?",))[0]
print(f"uS13 chain(s): {sorted(target_chains)}")
print(f"RNA chains: {rna_chains}")

ns = gemmi.NeighborSearch(model, st.cell, 5).populate()
contacts = collections.defaultdict(set)  # rna chain -> set of uS13 residues
nts = collections.defaultdict(set)
for ch in model:
    if ch.name not in target_chains:
        continue
    for res in ch:
        for atom in res:
            for m in ns.find_atoms(atom.pos, "\0", radius=CUTOFF):
                cra = m.to_cra(model)
                if cra.chain.name in rna_chains:
                    contacts[cra.chain.name].add((res.seqid.num, res.name))
                    nts[cra.chain.name].add(cra.residue.seqid.num)
for c, rs in contacts.items():
    print(f"RNA chain {c} ({rna_chains[c]}): {len(rs)} uS13 residues within {CUTOFF} A of "
          f"{len(nts[c])} nucleotides")
    print("  uS13 residues:", " ".join(f"{n}{r}" for r, n in sorted(rs)))
if not contacts:
    print("No RNA contacts found (inconclusive).")
