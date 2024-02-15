-- Listing all genres in the db
-- hbtn_0d_tvshows_rate by their rating.
SELECT g.name, SUM(r.rate) AS rating
FROM (tv_genres AS g
	JOIN tv_show_genres AS tg ON g.id = tg.genre_id)
JOIN tv_show_ratings AS r ON tg.show_id = r.show_id
GROUP BY g.name ORDER BY rating DESC;
