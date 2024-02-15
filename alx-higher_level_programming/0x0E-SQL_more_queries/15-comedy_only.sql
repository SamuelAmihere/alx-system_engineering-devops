-- Listing all Comedy shows in db hbtn_0d_tvshows
SELECT s.title FROM (
	tv_genres AS g
	JOIN tv_show_genres As tg ON
	g.id = tg.genre_id)
JOIN tv_shows AS s ON
	tg.show_id = s.id WHERE g.name = "Comedy"
ORDER BY s.title ASC;
