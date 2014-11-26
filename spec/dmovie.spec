directory structure:

  element/
    |---- element.ini
    |---- movie_info.xml
    |---- movie-data-file


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
		<split-file/>
		<watermark/>
		<embed-subtitles/>
		<shot-version/>
		<incomplete/>
		<trim-needed/>
		<no-ts-par2/>
	</defects>
</movie-info>
