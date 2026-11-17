#!/usr/bin/env python3
"""Create a signed APK repository from one successful, isolated build."""
import argparse,hashlib,json,re,shutil,subprocess
from pathlib import Path
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--topdir',type=Path,required=True)
p.add_argument('--output',type=Path,required=True)
p.add_argument('--private-key',type=Path,required=True)
p.add_argument('--public-key',type=Path,required=True)
a=p.parse_args();s=a.topdir.resolve();out=a.output.resolve()
assert not out.exists(), 'Use a new output directory'
apk=s/'staging_dir/host/bin/apk';assert apk.is_file()
packages=sorted((s/'bin/targets/zte/zx279133/packages').glob('*.apk'))
packages=[x for x in packages if x.name.startswith(('kernel-','kmod-'))]
assert len(packages)>100, 'All-kmods feed requires more than the historical small test set'
keys=out/'keys';keys.mkdir(parents=True);shutil.copy2(a.public_key,keys/a.public_key.name)
def run(args):return subprocess.run([str(x) for x in args],capture_output=True,text=True,check=True)
versions=set();records=[]
for f in packages:
    meta=run([apk,'adbdump',f]).stdout
    for v in re.findall(r'kernel=([^\s"\x27,\]]+)',meta):versions.add(v)
assert len(versions)==1, 'Mixed kernel ABIs are forbidden'
abi=versions.pop();feed=out/'aarch64_cortex-a53'/abi;feed.mkdir(parents=True)
for f in packages:
    q=feed/f.name;shutil.copy2(f,q)
    # Normalize signatures with the same project key used by the matching image.
    run([apk,'--allow-untrusted','adbsign','--sign-key',a.private_key,q])
    run([apk,'--keys-dir',keys,'verify',q])
    records.append({'file':q.name,'bytes':q.stat().st_size,'sha256':hashlib.sha256(q.read_bytes()).hexdigest()})
run([apk,'mkndx','--sign-key',a.private_key,'--description','SR7420 '+abi,'--output',feed/'packages.adb',*sorted(feed.glob('*.apk'))])
run([apk,'--keys-dir',keys,'verify',feed/'packages.adb'])
(feed/'manifest.json').write_text(json.dumps({'kernel_abi':abi,'packages':records,'all_signatures_verified':True},indent=2)+'\n')
print(json.dumps({'kernel_abi':abi,'package_count':len(records)}))
