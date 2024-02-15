-- Listing all shows contained in hbtn_0d_tvshows
SELECT sh.title, shg.genre_id FROM tv_shows AS sh
INNER JOIN tv_show_genres AS shg ON
	sh.id = shg.show_id
ORDER BY sh.title, shg.genre_id ASC;
