detik = int(input())
hari = detik // 86400
sisa = detik % 86400
jam = sisa // 3600
sisa %= 3600
menit = sisa // 60
detik = sisa % 60

if hari > 0:
    print(f"{hari} hari {jam:02d}:{menit:02d}:{detik:02d}")
else:
    print(f"{jam:02d}:{menit:02d}:{detik:02d}")