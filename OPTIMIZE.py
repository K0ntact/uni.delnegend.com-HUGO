import subprocess as sp
import os
import sys
import shutil

def checkInPath(command: str) -> bool:
    return shutil.which(command) is not None

def humanReadableSize(size) -> str:
    unit = ['B', 'KB', 'MB', 'GB', 'TB']
    for i in range(5):
        if size < 1024:
            return str(round(size, 2)) + unit[i]
        size /= 1024

# list files recursively
def listFiles(path: str, ext: list) -> list:
    files = []
    for root, _, filenames in os.walk(path):
        for filename in filenames:
            if os.path.splitext(filename)[1] in ext:
                files.append(os.path.normpath(os.path.join(root, filename)))
    return files

def convert(input: str, output: str) -> None:
    format = os.path.splitext(output)[1]
    match (format):
        case ".avif":
            if checkInPath("avifenc"):
                command = f"avifenc -y 444 -d 10 -c aom --min 0 --max 63 --minalpha 0 --maxalpha 63 -a aq-mode=1 -a cq-level=18 -a enable-chroma-deltaq=1 -a tune=ssim {input} {output}"
            else:
                command = f"ffmpeg -y -i {input} -c:v libaom-av1 -b:v 0 -qmin 0 -qmax 63 -crf 18 -cpu-used 6 -aq-mode 1 -pix_fmt yuv444p10le -aom-params enable-chroma-deltaq=1 {output}"
        case ".webp":
            command = f"ffmpeg -i {input} -lossless 1 -compression_level 6 {output}"
        case ".png":
            command = f"ffmpeg -i {input} -compression_level 100 {output}"
    sp.run(command, shell=True, stderr=sp.DEVNULL, stdout=sp.DEVNULL)

def report(old: str, new: str) -> str:
    ext_old = os.path.splitext(old)[1]
    ext_new = os.path.splitext(new)[1]
    size_old = os.path.getsize(old)
    size_new = os.path.getsize(new)
    ratio = round(size_new / size_old * 100, 2)
    return f"{old} | {ext_old} -> {ext_new} | {humanReadableSize(size_old)} -> {humanReadableSize(size_new)} | {ratio}%"

def main():
    print("==> Converting png to webp and avif")
    for f in listFiles("./content", [".png"]):
        os.remove(f.replace(".png", ".webp")) if os.path.exists(f.replace(".png", ".webp")) else None
        os.remove(f.replace(".png", ".avif")) if os.path.exists(f.replace(".png", ".avif")) else None
        if not os.path.exists(f.replace(".png", ".avif")):
            convert(f, f.replace(".png", ".avif"))
            print(report(f, f.replace(".png", ".avif")))
        if not os.path.exists(f.replace(".png", ".webp")):
            convert(f, f.replace(".png", ".webp"))
            print(report(f, f.replace(".png", ".webp")))
        os.remove(f)

    print("\n==> Converting webp to avif")
    for f in listFiles("./content", [".webp"]):
        if not os.path.exists(f.replace(".webp", ".avif")):
            convert(f, f.replace(".webp", ".png"))
            convert(f.replace(".webp", ".png"), f.replace(".webp", ".avif"))
            os.remove(f.replace(".webp", ".png"))
            print(report(f, f.replace(".webp", ".avif")))

    print("\n==> Removing obsolete avif")
    for f in listFiles("./content", [".avif"]):
        if not os.path.exists(f.replace(".avif", ".webp")):
            print(f"Removing {f}")
            os.remove(f)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "stats":
        total_webp_size = 0
        total_avif_size = 0
        for f in listFiles("./content", [".webp", ".avif"]):
            size = os.path.getsize(f)
            if f.endswith(".webp"):
                total_webp_size += size
            else:
                total_avif_size += size
        print(f"Total WEBP size: {humanReadableSize(total_webp_size)}")
        print(f"Total AVIF size: {humanReadableSize(total_avif_size)}")
        print(f"Total AVIF savings: {100 - round(total_avif_size / total_webp_size * 100, 2)}%")
    else:
        main()