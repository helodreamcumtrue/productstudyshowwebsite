import urllib.request
import re
import os

base_url = 'https://framerusercontent.com/sites/2Lchxi9LzakPkRuMF1bj1g/'
target_dir = 'framer_dist'
os.makedirs(f'{target_dir}/modules', exist_ok=True)
os.makedirs(f'{target_dir}/assets', exist_ok=True)

# Initial list of known modules
modules_to_download = {
    'script_main.DbzaP8xY.mjs',
    'react.DPSbHZgg.mjs',
    'rolldown-runtime.hBrq4iGT.mjs',
    'framer.BKMhELoL.mjs',
    'motion.Bx7l5byu.mjs',
    'shared-lib.CkP6a30Y.mjs',
    'eatq50cQ4.DuUEK3pB.mjs',
    'WgPd0YgpsKd_P_scHQyMrt7TAQrTrP-a8Af-rXEZqm8.B8fPFAfj.mjs',
    'GZCikEng2ds9ljEaHPZsUI30jMSOPStZY2CH5DyKZ9A.IDe8msX-.mjs',
    'myhI0-08C-ClskNgBwlYvOEKrmClI8C-UvfOyvgbf5A.CEsPxajT.mjs',
    'bC-w1eXlnDtcD8dTgiGqGYaFnEyKFrJsPyLixxTbeUo.BhFa0sjD.mjs',
    'xf_bRlhjSoLp6IPIQcdMDYYpIbo_Gls7DXQ3eHEAUkc.n4980hUk.mjs',
    '86PpqxcwmzHSbIrTOp5ihgU7PacPG4vo6Z4lvGHQKfQ.CRoSUva-.mjs',
    'iFWdbipkl9DlsPj4WFA9OYmH03wtXXP2xe_nYHbzyis.NsKbRseU.mjs',
    'c_rRS3uMuNQZ0ldr1aYw9jMFP3GWzyScuXI-8YRezk8.oEgXP2N8.mjs',
    'PX9hIOIVM.BGlTy4YE.mjs',
    'SitesNotFoundPage.js@1.4.BEwvtgkH.mjs',
    'kHuZ4CJhuwNZKcy-4f1NNR3KGbeEc4_upzrtxONkOUA.BCJ01uPr.mjs'
}

downloaded = set()

while modules_to_download:
    mod = modules_to_download.pop()
    if mod in downloaded:
        continue
    downloaded.add(mod)
    
    file_path = os.path.join(target_dir, mod)
    url = base_url + mod
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp:
            content = resp.read().decode('utf-8')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Downloaded {mod} ({len(content)} bytes)")
        
        # Check for any relative imports like ./XYZ.mjs
        rel_imports = re.findall(r'from\s*[\"\']\./([^\"\']+\.mjs)[\"\']|import\s*\([\s*\"\'\./]*([^\"\'\)]+\.mjs)[\s*\"\'\)]*\)', content)
        for imp in rel_imports:
            target = imp[0] or imp[1]
            if target and target.startswith('./'):
                target = target[2:]
            if target and target not in downloaded:
                modules_to_download.add(target)
    except Exception as e:
        print(f"Error downloading {mod}: {e}")

print(f"Total modules downloaded: {len(downloaded)}")
