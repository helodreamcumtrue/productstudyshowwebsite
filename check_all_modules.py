import urllib.request
import re

modules = {
    'home': 'WgPd0YgpsKd_P_scHQyMrt7TAQrTrP-a8Af-rXEZqm8.B8fPFAfj.mjs',
    'about': 'GZCikEng2ds9ljEaHPZsUI30jMSOPStZY2CH5DyKZ9A.IDe8msX-.mjs',
    'enterprise': 'myhI0-08C-ClskNgBwlYvOEKrmClI8C-UvfOyvgbf5A.CEsPxajT.mjs',
    'show-me-money': 'bC-w1eXlnDtcD8dTgiGqGYaFnEyKFrJsPyLixxTbeUo.BhFa0sjD.mjs',
    'you-are-okay': 'xf_bRlhjSoLp6IPIQcdMDYYpIbo_Gls7DXQ3eHEAUkc.n4980hUk.mjs',
    'ca-founder': '86PpqxcwmzHSbIrTOp5ihgU7PacPG4vo6Z4lvGHQKfQ.CRoSUva-.mjs',
    '8club': 'iFWdbipkl9DlsPj4WFA9OYmH03wtXXP2xe_nYHbzyis.NsKbRseU.mjs',
    'custom-access': 'c_rRS3uMuNQZ0ldr1aYw9jMFP3GWzyScuXI-8YRezk8.oEgXP2N8.mjs'
}

base_url = 'https://framerusercontent.com/sites/2Lchxi9LzakPkRuMF1bj1g/'

for name, mod in modules.items():
    url = base_url + mod
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        content = resp.read().decode('utf-8')
    
    pinks = re.findall(r'#[dD]5546[dD]|#[eE]28799|#[fF][fF][aA]8[bB]9|rgba?\(\s*213\s*,\s*84\s*,\s*109|rgba?\(\s*179\s*,\s*45\s*,\s*71', content)
    print(f"Module {name} ({mod}): length={len(content)}, pink matches={len(pinks)}")
