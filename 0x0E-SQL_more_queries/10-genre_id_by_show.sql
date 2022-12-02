-- Import the database dump from hbtn_0d_tvshows to our MySql server.
-- Lists all shows contained in hbtn_0d_tvshows that have atleast one genre linkes.i
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.show_id >= 1
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
