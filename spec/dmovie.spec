directory structure:

  element/
    |---- element.ini
    |---- movie_info.xml
    |---- video & audio files
    |---- subtitle files
    |
    |---- degradated/
    |       |---- video & audio files
    |---- other/
            |---- video & audio files

element.ini example:



movie_info.xml example:

<?xml version="1.0" encoding="UTF-8"?>
<movie-info>
	<runtime>165</runtime>
	<year>1998</year>
	<links>
		<wikipedia>http://en.wikipedia.org/wiki/The_Matrix</wikipedia>
		<wikipedia lang="zh">http://zh.wikipedia.org/wiki/黑客帝国</wikipedia>
		<imdb>http://www.imdb.com/title/tt0133093/?ref_=fn_al_tt_1</imdb>
	</links>
	<video>
		<format>vc-1</format>
		<aspect-ratio>16:9</aspect-ratio>
		<width>1920</width>
		<height>1080</height>
		<frame-rate>23.976</frame-rate>
		<bit-rate>variable</bit-rate>
	</video>
	<audio lang="en">
		<format>dts</format>
		<channels>5.1</channels>
		<sampling-rate>48000</sampling-rate>
		<bit-depth>16</bit-depth>
		<bit-rate></bit-rate>
	</audio>
	<subtitle lang="en"></subtitle>
	<subtitle lang="zh_CN"></subtitle>
	<defects>
		<inconsistent/>
		<watermark/>
		<embed-subtitles/>
		<shot-version/>
		<incomplete/>
		<trim-needed/>
		<ts-without-par2/>
	</defects>
</movie-info>


priority:
1. geometry
2. video codec
3. audio codec

video-format:
1. h264				H.264 (MPEG-4 AVC, MPEG-4 Part 10)
1. vc-1				VC-1
2. mpeg-2			MPEG-2

audio-format:
1. lpcm				Linear PCM																						lossless
1. truehd			Dolby True HD																					lossless
1. dts-hd-ma	DTS-HD Master Audio																		lossless
2. dts-hd-hra	DTS-HD High Resolution Audio
3. e-ac-3			Dolby Digital Plus (Dolby Enhanced AC-3)
4. dts				DTS
5. ac-3				Dolby Surround Audio Coding-3

channels:
1. 7.1
2. 6.1
3. 5.1
4. 2.1
5. 2.0
6. 1.0

aspect-ratio:
1. 16:9
2. 4:3

bit-rate:
1. Nkbps
2. variable			

sampling-rate(unit, hz):
8000
11025
16000
22050
32000
44056
44100				44.1KHz		Audio CD
47250
48000				48.0KHz
50000
50400
88200
96000
176400
192000
352800
2822400
4564800

bit-depth:
8
10
11
16
16f			16-bit float
20
24
24f			24-bit float
32
32f			32-bit float
64f			64-bit float


H264 bitrate settings

size geometry bitrate-suggeested
480P 720X480 1800Kbps 
720P 1280X720 3500Kbps 
1080P 1920X1080 8500Kbps 

Project formula 192X144 320X240 480X360 640X480 1280X720 1920X1080
very-low （width X height X 3）/ 4 30kb/s 60kb/s 120kps 250kbps 500kbps 1mbps
low （width X height X 3）/ 2 60kb/s 120kb/s 250kbps 500kbps 1mbps 2mbps
medium （width X height X 3) 120kb/s 250kb/s 500kbps 1mbps 2mbps 4mbps 
high （width X height X 3）X 2 250kb/s 500kb/s 1mbps 2mbps 4mbps 8mps
very-high （width X height X 3）X4 500kb/s 1mb/s 2mbps 4mbps 8mbps 16mbps


 
