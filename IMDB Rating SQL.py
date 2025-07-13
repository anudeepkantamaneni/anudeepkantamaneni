SELECT i.Title, i.Rating
FROM IMDB i
JOIN genre g ON i.Movie_id = g.Movie_id
WHERE i.Title LIKE '%(2014)%'
  AND g.genre LIKE 'C%'
  AND i.Budget > 40000000;
