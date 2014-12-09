directory structure:

  element/
    |---- element.ini
    |---- movie_info.xml
    |
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
	<nation>it</nation>
	<year>1998</year>
	<links>
		<wikipedia>http://en.wikipedia.org/wiki/The_Matrix</wikipedia>
		<wikipedia lang="zh">http://zh.wikipedia.org/wiki/黑客帝国</wikipedia>
		<imdb>http://www.imdb.com/title/tt0133093/?ref_=fn_al_tt_1</imdb>
		<metacritic>http://www.metacritic.com/movie/the-legend-of-1900</metacritic>
		<box-office-mojo>http://www.boxofficemojo.com/movies/?id=legendof1900.htm</box-office-mojo>
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
1. vc-1				VC-1
2. 

audio-format:
1. dts				DTS

channels:
1. 5.1
2. 2.0

aspect-ratio:
1. 16:9
2. 

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
16f
20
24
24f
32
32f
64f
