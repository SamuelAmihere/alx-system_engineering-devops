-- Listing all genres from hbtn_0d_tvshow
SELECT g.name AS genre, COUNT(tg.genre_id) AS number_of_shows
FROM tv_genres AS g
JOIN tv_show_genres AS tg ON
	g.id = tg.genre_id
GROUP BY g.name HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
