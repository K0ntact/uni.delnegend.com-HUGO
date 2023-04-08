import os
import sys
import shutil
import math
import subprocess as sp

class VARIABLES:
    SPRITE_IMG = "sprite.webp"
    SPRITE_VTT = "sprite.vtt"
    THUMBNAIL_WIDTH = 320
    THUMBNAIL_HEIGHT = 180
    GAP = 5
    COVER_IMG = "cover.webp"
    VIDEO_FILE_NAME = "video.mp4"

class VTT_MOSAIC:
    __image_path, __output_path = '', ''
    __duration, __gap, __width, __height, __tile_size = 0, 0, 0, 0, 0
    __eol = "\r"

    def __init__(self, image_path: str, output_path: str, duration: int, gap: int, width: int, height: int, tile_size: int) -> None:
        self.__image_path = image_path
        self.__output_path = output_path
        self.__duration = duration
        self.__gap = gap
        self.__width = width
        self.__height = height
        self.__tile_size = tile_size

    def __appendFileSync(self, output_path: str, string: str) -> None:
        with open(output_path, "a") as f:
            f.write(string)

    def __secondsToHRTime(self, timeInSeconds: int) -> str:
        if timeInSeconds > 0:
            hours = timeInSeconds // 3600
            minutes = (timeInSeconds % 3600) // 60
            seconds = timeInSeconds % 60
            if seconds < 10:
                seconds = '0' + str(seconds)
            if minutes < 10:
                minutes = '0' + str(minutes)
            if hours > 0:
                hours = str(hours) + ':'
            else:
                hours = ''
            return hours + str(minutes) + ':' + str(seconds) + '.000'
        elif timeInSeconds == 0:
            return '00:00:00.000'
        else:
            return ''
    def create(self) -> None:
        # delete VTT file if already exists
        os.remove(self.__output_path) if os.path.exists(self.__output_path) else None

        # append our initial VTT data for spec compliance
        initial_data = f"WEBVTT{self.__eol}{self.__eol}"
        self.__appendFileSync(self.__output_path, initial_data)

        # initial variables values for our loop
        item_number = math.floor(self.__duration / self.__gap) + 1
        current_time = 0
        x_coordinates = 0
        y_coordinates = 0
        thumbnail_size_string = f",{self.__width},{self.__height}{self.__eol}"

        for i in range(item_number):
            if current_time > self.__duration:
                break
            start_time = self.__secondsToHRTime(current_time)
            current_time += self.__gap
            end_time = self.__secondsToHRTime(current_time)
            if not start_time or not end_time:
                print('Error: could not determine startTime or endTime for VTT item number ' + str(i) + ' - exit')
                return
            vtt_data = f"{i + 1}{self.__eol}{start_time} --> {end_time}{self.__eol}{os.path.basename(self.__image_path)}#xywh={x_coordinates},{y_coordinates}{thumbnail_size_string}{self.__eol}"
            self.__appendFileSync(self.__output_path, vtt_data)
            x_coordinates += self.__width
            if x_coordinates >= self.__width * self.__tile_size:
                x_coordinates = 0
                y_coordinates += self.__height

class IMG_MOSAIC:
    __tile_size, __inputPath, __outputPath = '', '', ''

    def __init__(self, inputPath: str, outputPath: str, duration: int, gap: int) -> None:
        self.__inputPath = inputPath
        self.__outputPath = outputPath
        self.__tile_size = math.ceil(math.sqrt(duration / gap))

    def create(self) -> None:
        os.remove(self.__outputPath) if os.path.exists(self.__outputPath) else None
        # command = f"ffmpeg -i {self.__inputPath} -filter_complex \"select='not(mod(n,120))',scale=320:180,tile={f'{self.__tile_size}x{self.__tile_size}'}\" -frames:v 1 -qscale:v 3 -an {self.__outputPath}"
        command = f"ffmpeg -i {self.__inputPath} -filter_complex \"select='not(mod(n,120))',scale={VARIABLES.THUMBNAIL_WIDTH}:{VARIABLES.THUMBNAIL_HEIGHT},tile={f'{self.__tile_size}x{self.__tile_size}'}\" -frames:v 1 -qscale:v 3 -an {VARIABLES.SPRITE_IMG}"
        sp.check_output(command, shell=True)

    def getTileSize(self) -> int:
        return self.__tile_size

class VIDEO:
    __inputPath = ""

    def __init__(self, inputPath: str) -> None:
        self.__inputPath = inputPath

    def getDurationInSeconds(self) -> int:
        command = f"ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 {self.__inputPath}"
        output = sp.check_output(command, shell=True)
        return int(float(output))

    def split(self, outputPath: str) -> None:
        # create a folder if not exists
        os.makedirs(outputPath, exist_ok=True)
        # delete all files in the folder
        for file in os.listdir(outputPath):
            os.remove(os.path.join(outputPath, file))
        # split the video
        # sp.check_output(f"ffmpeg -i {self.__inputPath} -c copy -start_number 0 -hls_time 5 -hls_list_size 0 -f hls {os.path.join(outputPath, '_.m3u8')}", shell=False)
        sp.call(f"ffmpeg -i {self.__inputPath} -c copy -start_number 0 -hls_time 5 -hls_list_size 0 -f hls {os.path.join(outputPath, '_.m3u8')}", shell=False, stdout=sp.DEVNULL, stderr=sp.DEVNULL)
def main() -> None:

    inputVideo = sys.argv[1]
    video = VIDEO(inputVideo)
    duration = video.getDurationInSeconds()
    imgMosaic = IMG_MOSAIC(inputVideo, VARIABLES.SPRITE_IMG, duration, VARIABLES.GAP)
    imgMosaic.create()
    vtt = VTT_MOSAIC(VARIABLES.SPRITE_IMG, VARIABLES.SPRITE_VTT, duration, VARIABLES.GAP, VARIABLES.THUMBNAIL_WIDTH, VARIABLES.THUMBNAIL_HEIGHT, imgMosaic.getTileSize())
    vtt.create()

    video.split(os.path.join(os.path.dirname(inputVideo), "video"))

    # Rename the video file to VARIABLES.VIDEO_FILE_NAME (default: video.mp4)
    os.rename(inputVideo, os.path.dirname(inputVideo) + "/" + VARIABLES.VIDEO_FILE_NAME)


if __name__ == "__main__":
    if not shutil.which("ffmpeg"):
        print("ffmpeg not found in path")
        sys.exit(1)
    if not shutil.which("ffprobe"):
        print("ffprobe not found in path")
        sys.exit(1)
    main()
