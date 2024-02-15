-- Listing all shows contained in hbtn_0d_tvshows
-- without a genre linked
SELECT s.title, g.genre_id FROM tv_shows AS s
LEFT JOIN tv_show_genres AS g ON
	s.id = g.show_id WHERE g.show_id IS NULL
ORDER BY s.title, g.genre_id ASC;
