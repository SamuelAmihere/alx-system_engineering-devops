-- List all shows, and all genres linked to
-- that show, from db hbtn_0d_tvshows
SELECT s.title, g.name FROM (
	tv_shows AS s
	LEFT JOIN tv_show_genres AS tg ON
		s.id = tg.show_id)
LEFT JOIN tv_genres AS g ON tg.genre_id = g.id
ORDER BY s.title, g.name ASC;
