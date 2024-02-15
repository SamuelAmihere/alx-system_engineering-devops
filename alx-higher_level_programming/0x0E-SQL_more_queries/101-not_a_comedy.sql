-- Listing all shows without the genre
-- Comedy in the db hbtn_0d_tvshows
SELECT s.title FROM tv_shows AS s
WHERE s.title NOT IN 
	(SELECT s.title
	FROM (tv_genres AS g JOIN tv_show_genres AS tg ON g.id = tg.genre_id)
	JOIN tv_shows AS s ON tg.show_id = s.id
	WHERE g.name = "Comedy")
ORDER BY s.title ASC;
