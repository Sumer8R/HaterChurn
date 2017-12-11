SELECT A.id, A.createddate,
SUM(CASE WHEN eventdate BETWEEN A.createddate AND DATEADD(day, 1 , A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 1 , A.createddate) AND DATEADD(day, 2 , A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 2 , A.createddate) AND DATEADD(day, 3 , A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 3, A.createddate) AND DATEADD(day, 4, A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 4 , A.createddate) AND DATEADD(day, 5, A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 5 , A.createddate) AND DATEADD(day, 6 , A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 6 , A.createddate) AND DATEADD(day, 7 , A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 7 , A.createddate) AND DATEADD(day, 8 , A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 8 , A.createddate) AND DATEADD(day, 9 , A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 9 , A.createddate) AND DATEADD(day, 10 , A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 10 , A.createddate) AND DATEADD(day, 11 , A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 11 , A.createddate) AND DATEADD(day, 12, A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 12, A.createddate) AND DATEADD(day, 13, A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 13, A.createddate) AND DATEADD(day, 14, A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 14, A.createddate) AND DATEADD(day, 15, A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 15, A.createddate) AND DATEADD(day, 16, A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 16, A.createddate) AND DATEADD(day, 17, A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 17, A.createddate) AND DATEADD(day, 18, A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 18, A.createddate) AND DATEADD(day, 19, A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 19, A.createddate) AND DATEADD(day, 20, A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 20, A.createddate) AND DATEADD(day, 21, A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 21, A.createddate) AND DATEADD(day, 22, A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 22, A.createddate) AND DATEADD(day, 23, A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 23, A.createddate) AND DATEADD(day, 24, A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 24, A.createddate) AND DATEADD(day, 25, A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 25, A.createddate) AND DATEADD(day, 26, A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 26, A.createddate) AND DATEADD(day, 27, A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 27, A.createddate) AND DATEADD(day, 28, A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 28, A.createddate) AND DATEADD(day, 29, A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 29, A.createddate) AND DATEADD(day, 30, A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 30, A.createddate) AND DATEADD(day, 31, A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 31, A.createddate) AND DATEADD(day, 32, A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 32, A.createddate) AND DATEADD(day, 33, A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 33, A.createddate) AND DATEADD(day, 34, A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 34, A.createddate) AND DATEADD(day, 35, A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 35, A.createddate) AND DATEADD(day, 36, A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 36, A.createddate) AND DATEADD(day, 37, A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 37, A.createddate) AND DATEADD(day, 38, A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 38, A.createddate) AND DATEADD(day, 39, A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 39, A.createddate) AND DATEADD(day, 40, A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 40, A.createddate) AND DATEADD(day, 41, A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 41, A.createddate) AND DATEADD(day, 42, A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 42, A.createddate) AND DATEADD(day, 43, A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 43, A.createddate) AND DATEADD(day, 44, A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 44, A.createddate) AND DATEADD(day, 45, A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 45, A.createddate) AND DATEADD(day, 46, A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 46, A.createddate) AND DATEADD(day, 47, A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 47, A.createddate) AND DATEADD(day, 48, A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 48, A.createddate) AND DATEADD(day, 49, A.createddate)
THEN 1 ELSE 0 END),
SUM(CASE WHEN eventdate BETWEEN DATEADD(day, 49, A.createddate) AND DATEADD(day, 50, A.createddate)
THEN 1 ELSE 0 END)
FROM hater.mit.event
INNER JOIN hater.mit.appuser A ON A.id = hater.mit.event.userid
WHERE
A.createddate BETWEEN '2017-07-15' AND '2017-9-10'
GROUP BY A.id, A.createddate
ORDER BY A.createddate