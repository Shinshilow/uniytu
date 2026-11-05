#!/usr/bin/env python3
"""Package the truthful partial rebuild; never call it 24 completed projects."""
from pathlib import Path
import hashlib,json,zipfile
ROOT=Path(__file__).resolve().parents[1]
TOOLS=['build_native_intro.py','build_native_scripting.py','build_native_scripting8.py','build_native_collisions.py','build_native_prefabs.py','build_native_mobile22.py','build_native_scenes23.py','build_book_materials.py','inspect_unity_assets.py','validate_native_projects.py','requirements-validation.txt','package_native_progress.py']

def main():
    destination=ROOT/'deliverables/Unity24_rebuild_partial.zip'
    files=[ROOT/'REBUILD_STATUS.md']
    files.extend(p for p in (ROOT/'rebuild').rglob('*') if p.is_file() and '__pycache__' not in p.parts)
    files.extend(p for p in (ROOT/'audit').glob('*') if p.suffix in ['.json','.md'])
    files.extend(ROOT/'tools'/name for name in TOOLS if (ROOT/'tools'/name).exists())
    with zipfile.ZipFile(destination,'w',zipfile.ZIP_DEFLATED) as z:
        for p in sorted(set(files)):z.write(p,Path('Unity24_rebuild_partial')/p.relative_to(ROOT))
    with zipfile.ZipFile(destination) as z:
        assert z.testzip() is None
        archived={int(n.split('/')[2][4:]) for n in z.namelist() if n.startswith('Unity24_rebuild_partial/rebuild/Hour') and '/Assets/Scenes/' in n and n.endswith('.unity')}
    sha=hashlib.sha256(destination.read_bytes()).hexdigest()
    print(json.dumps({'archive':str(destination),'source_hours':sorted(archived),'sha256':sha,'unity_checks':'UNRUN','all24_complete':False},ensure_ascii=False))
if __name__=='__main__':main()
