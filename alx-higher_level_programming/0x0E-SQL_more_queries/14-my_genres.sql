-- Using the hbtn_0d_tvshows db to
-- lists all genres of the show Dexter
SELECT g.name FROM (
	tv_shows As s 
	JOIN tv_show_genres AS tg ON 
		s.id = tg.show_id)
JOIN tv_genres AS g ON tg.genre_id = g.id
WHERE s.title = "Dexter"
ORDER BY g.name ASC;
