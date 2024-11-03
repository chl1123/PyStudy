"""
外观模式
"""


class VideoFile:
    def __init__(self, name):
        self.name = name

    def play(self):
        print("playing video file: ", self.name)


class MPEG4CompressionCodec:
    def compress(self, video_file: VideoFile):
        print("compressing video file: ", video_file.name)


class OggCompressionCodec:
    def compress(self, video_file: VideoFile):
        print("compressing video file: ", video_file.name)


class CodecFactory:
    @staticmethod
    def extract(video_file: VideoFile):
        name, ext = video_file.name.split('.')
        if ext == 'mp4':
            return MPEG4CompressionCodec()
        else:
            return OggCompressionCodec()


class BitrateReader:
    @staticmethod
    def read(video_file, codec):
        print("reading video file")
        return video_file

    @staticmethod
    def convert(buffer, codec):
        print("converting video file")
        return buffer


class AudioMixer:
    @staticmethod
    def fix(buffer):
        print("fixing audio in video file")
        return buffer


class VideoConverter:
    @staticmethod
    def convert(filename, format):
        video_file = VideoFile(filename)
        source_codec = CodecFactory.extract(video_file)
        destination_codec = None
        if format == 'mp4':
            destination_codec = MPEG4CompressionCodec()
        else:
            destination_codec = OggCompressionCodec()

        buffer = BitrateReader.read(video_file, source_codec)
        result = BitrateReader.convert(buffer, destination_codec)
        result = AudioMixer.fix(result)

        return result


if __name__ == '__main__':
    VideoConverter.convert('funny-cats-video.ogg', 'mp4')
    VideoConverter.convert('funny-cats-video.mp4', 'ogg')
