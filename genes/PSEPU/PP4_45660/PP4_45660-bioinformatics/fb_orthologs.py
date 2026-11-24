"""Extract Fitness Browser homologs of dashboard query NZ_KZ987399.1_4576 from the
pipeline tarball caches (FB neighbourhood cache and FB aaseqs hit cache), plus the
query topology/domain summary. Writes JSON to $BERIL_RUN_DIR/data/ (or cwd).

Usage: python3 -I fb_orthologs.py <tarball>
"""
import json, os, sys, tarfile

QID = "aux__NZ_KZ987399.1_4576"
MEMBERS = {
    "neigh": "run/.cache/kblh/batch_results/run_kblh_fb_neighborhoods.json",
    "aaseqs": "run/.cache/generic_sources/batch_results/run_fitnessbrowser_aaseqs.json",
}

def main(tarball):
    out = {"query": QID, "tarball": tarball}
    with tarfile.open(tarball, "r:gz") as tf:
        for key, member in MEMBERS.items():
            f = tf.extractfile(member)
            d = json.load(f)
            entries = d.get(QID, [])
            if key == "neigh":
                out["fb_neighbourhood_homologs"] = [
                    {"organism": e["organism"], "target_id": e["target_id"],
                     "pident": round(e["pident"], 1),
                     "upstream": [(u["locus_id"], u.get("seed_desc", "")) for u in e.get("upstream", [])],
                     "downstream": [(u["locus_id"], u.get("seed_desc", "")) for u in e.get("downstream", [])]}
                    for e in entries]
            else:
                out["fb_aaseqs_hits_shown"] = [
                    {"organism": e["organism"], "target_id": e["target_id"],
                     "pident": round(e["pident"], 1)} for e in entries]
    shown = {h["target_id"] for h in out["fb_aaseqs_hits_shown"]}
    out["close_fb_orthologs_not_in_aaseqs_block"] = [
        h["target_id"] for h in out["fb_neighbourhood_homologs"]
        if h["pident"] >= 70 and h["target_id"] not in shown]
    outdir = os.path.join(os.environ.get("BERIL_RUN_DIR", "."), "data")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "fb_orthologs.json"), "w") as fh:
        json.dump(out, fh, indent=2)
    print(json.dumps(out, indent=2))

if __name__ == "__main__":
    main(sys.argv[1])
