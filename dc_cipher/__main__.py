import sys
from itertools import cycle
from string import ascii_uppercase as ABC
from typing import Literal


def cipher(message: str, keyword: str, mode: Literal["cipher", "decipher"] = "cipher") -> str:
    match mode:
        case "cipher":
            op = 1
        case "decipher":
            op = -1
        case _:
            raise ValueError(f'Parameter `mode` expected "cipher" or "decipher", got "{mode}"')

    out = ""
    key = ""
    keyword = keyword.strip().upper()
    message = message.strip().upper()

    for char in cycle(list(keyword)):
        key += char
        if len(key) == len(message):
            break

    msg_idx = 0
    key_idx = 0
    while True:
        if msg_idx == len(message):
            break
        char = message[msg_idx]
        if char not in ABC:
            out += char
            msg_idx += 1
            continue
        char_rank = ABC.index(message[msg_idx])
        key_rank = ABC.index(key[key_idx])
        out += ABC[(char_rank + op * key_rank) % 26]
        msg_idx += 1
        key_idx += 1
    return out


if __name__ == "__main__":
    msg = """
Yvtd wo nzjwc ospyjrwylheif yc elya nzj glxs lulm hzrspbww.

Hsp uhujnbr pma ix yvp emlbgtb, ess aujyv mffjcfl vze,
hdy etcy dkwfdtktyu qm onhs eva laxwyr hexwx.
Ktev zykyffnhepw soeffwf vngldhalk wsnzfzyv jons mauj,
yvp pbz ck sslcwja.

Dtbrtbc zgw dplqa, qw ffp schxasu ess hcfj hzrspbww.
Wy mspqwjb ess zynfgelheif fbo nfqgtqwyr vkjw,
7 nbotjexmfzd lrrufhs ezkwlvx o qlwjn dnuse.

Ka ujj ppswjx lmsx.

Ofauehoenval'k isnwonulncy, ncjpahhtzb,
whv kwcx JEMATB ez famltfp eva jdfbpe cb faks.
    """
    out = cipher(msg, (sys.argv[2:3] or ["Followus"])[0], (sys.argv[1:2] or ["decipher"])[0])
    print(out)
