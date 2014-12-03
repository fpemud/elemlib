directory structure:

  element/
    |---- element.ini
    |---- movie_info.xml
    |---- video & audio files
    |---- subtitle files
    |
    |---- degradated-video1/
    |       |---- video files
    |---- degradated-video2/
    |       |---- video files
    |---- degradated-audio1/
    |       |---- audio files
    |---- degradated-audio2/
    |       |---- audio files
    |---- other-data1
    |       |---- video & audio files
    |---- other-data2
            |---- video & audio files

element.ini example:



movie_info.xml example:

<?xml version="1.0" encoding="UTF-8"?>
<movie-info>
	<runtime>165</runtime>
	<aspect-ratio>2.35:1</aspect-ratio>
	<links>
		<wikipedia>http://en.wikipedia.org/wiki/The_Matrix</wikipedia>
		<wikipedia lang="zh">http://zh.wikipedia.org/wiki/黑客帝国</wikipedia>
		<imdb>http://www.imdb.com/title/tt0133093/?ref_=fn_al_tt_1</imdb>
	</links>
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
