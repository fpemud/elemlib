directory structure:

  element/
    |---- element.ini
    |---- movie_info.xml
    |---- data1/
    |       |---- video files
    |---- data2/
            |---- video files

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

	<data directory="data1">
		<original/>
		<defects>
			<watermark/>
			<embed-subtitles/>
			<shot-version/>
			<incomplete/>
			<trim-needed/>
			<ts-without-par2/>
		</defects>
	</data>
</movie-info>
