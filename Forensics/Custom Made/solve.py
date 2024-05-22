import sys
import struct
if len(sys.argv) < 2:
    sys.exit("Must provide file as first argument!")

file_path = sys.argv[1]

H = 5333  # image height

with open(file_path, 'rb') as f:
    sgi_data = f.read()

sc_offsets = sgi_data[512:512 + 5333 * 4 * 4]
sc_lens = sgi_data[512 + 5333 * 4 * 4:512 + 5333 * 4 * 4 * 2]

offs = list(struct.unpack('>%dI' % (5333 * 4), sc_offsets))
lens = list(struct.unpack('>%dI' % (5333 * 4), sc_lens))

hidden_data = b''
for i in range((5333 * 4) - 1):
    gap = offs[i + 1] - offs[i]
    extra = gap - lens[i]
    if extra > 0:
        hidden_data += sgi_data[offs[i] + lens[i]:offs[i] + lens[i] + extra]

print('Flag:', hidden_data.decode("utf-8"))
