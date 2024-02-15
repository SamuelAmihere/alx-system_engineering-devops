-- Using the hbtn_0d_tvshows db to list
-- all genres not linked to the show Dexter
SELECT name FROM tv_genres AS g
WHERE name NOT IN
	(SELECT name FROM tv_genres AS g
	LEFT JOIN tv_show_genres AS tg ON g.id = tg.genre_id
	LEFT JOIN tv_shows As s ON tg.show_id = s.id
	WHERE s.title = "Dexter")
GROUP BY name ORDER BY name ASC;
