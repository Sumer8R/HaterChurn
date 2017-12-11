SELECT A.id, 
SUM(CASE WHEN eventname LIKE '%Message%' AND eventdate BETWEEN A.createddate AND DATEADD(day, 7 , A.createddate)
THEN 1 ELSE 0 END) AS totalmessages, 
A.createddate, A.sex,  
SUM(CASE WHEN (eventname LIKE 'Dater - Match' or eventname LIKE 'Dater - Match - v2') AND eventdate BETWEEN A.createddate AND DATEADD(day, 7 , A.createddate)
THEN 1 ELSE 0 END) AS matches, 
SUM(CASE WHEN eventname LIKE '%User photo t%' AND eventdate BETWEEN A.createddate AND DATEADD(day, 7 , A.createddate)
THEN 1 ELSE 0 END) AS photoview,
SUM(CASE WHEN eventname LIKE '%View P%' AND eventdate BETWEEN A.createddate AND DATEADD(day, 7 , A.createddate)
THEN 1 ELSE 0 END) AS viewprofile,
SUM(CASE WHEN eventname LIKE '%No recommendation%' AND eventdate BETWEEN A.createddate AND DATEADD(day, 7 , A.createddate)
THEN 1 ELSE 0 END) AS norec,
SUM(CASE WHEN eventname LIKE '%Icebreaker%' AND eventdate BETWEEN A.createddate AND DATEADD(day, 7 , A.createddate)
THEN 1 ELSE 0 END) AS icebreaker,
SUM(CASE WHEN eventname LIKE '%Add ph%' AND eventdate BETWEEN A.createddate AND DATEADD(day, 7 , A.createddate)
THEN 1 ELSE 0 END) AS addphoto,
SUM(CASE WHEN eventname LIKE '%topic ans%' AND eventdate BETWEEN A.createddate AND DATEADD(day, 7 , A.createddate)
THEN 1 ELSE 0 END) AS topicansw,
SUM(CASE WHEN eventname LIKE '%Recommendation ans%' AND eventdate BETWEEN A.createddate AND DATEADD(day, 7 , A.createddate)
THEN 1 ELSE 0 END) AS recansw,
SUM(CASE WHEN eventname LIKE '%Datemode v%' AND eventdate BETWEEN A.createddate AND DATEADD(day, 7 , A.createddate)
THEN 1 ELSE 0 END) AS visits,
SUM(CASE WHEN eventname LIKE '%_start' AND eventdate BETWEEN A.createddate AND DATEADD(day, 7 , A.createddate)
THEN 1 ELSE 0 END) AS returners,
SUM(CASE WHEN eventdate BETWEEN A.createddate AND DATEADD(day, 7 , A.createddate)
THEN 1 ELSE 0 END) AS uses,
SUM(CASE WHEN eventname LIKE '%_start' AND eventdate > DATEADD(day, 7, A.createddate) 
THEN 1 ELSE 0 END) AS comeback,
SUM(CASE WHEN eventname LIKE '%Datemode v%' AND eventdate > DATEADD(day, 7, A.createddate) 
THEN 1 ELSE 0 END) AS comebackDate,
SUM(CASE WHEN eventname LIKE '%Message%' AND eventdate > DATEADD(day, 7, A.createddate) 
THEN 1 ELSE 0 END) AS comebackMessage,
SUM(CASE WHEN eventname LIKE '%topic ans%' AND eventdate > DATEADD(day, 7, A.createddate) 
THEN 1 ELSE 0 END) AS comebackTopic,
SUM(CASE WHEN eventname LIKE '%Recommendation ans%' AND eventdate > DATEADD(day, 7, A.createddate) 
THEN 1 ELSE 0 END) AS comebackRec,
SUM(CASE WHEN eventdate > DATEADD(day, 7, A.createddate) 
THEN 1 ELSE 0 END) AS comebackuses
FROM hater.mit.event
INNER JOIN hater.mit.appuser A ON A.id = hater.mit.event.userid
WHERE
A.createddate BETWEEN '2017-08-20' AND '2017-10-20'
GROUP BY A.id, A.createddate, A.sex, a.totallikes, A.totalreaction, 
A.attractiveness
ORDER BY A.id
;