/* MySQL */
/* to simplify the following queries */
/* first create a new view to simplify the datetime to dates */
/* and convert the latitude,longitude into regions by calculation */
CREATE VIEW 'daily' AS
SELECT CAST('gps'.'datetime' AS DATE) AS 'day', 'gps'.'user_id' AS 'user_id', (((('gps'.'longitude' - 138) DIV 1) * 4) + (('gps'.'latitude' - 38) DIV 0.5)) AS 'region'
FROM 'gps'
ORDER BY CAST('gps'.'datetime' AS DATE) , 'gps'.'user_id' , (((('gps'.'longitude' - 138) DIV 1) * 4) + (('gps'.'latitude' - 38) DIV 0.5));

/* SQL query of Q1 */
/* the population of residential area would be */
SELECT lt.region, count(lt.user_id) as Residents
FROM (
SELECT user_id, ((longitude-138) DIV 1)*4+((latitude-38) DIV 0.5) as region, count(datetime) as Count 
FROM gps 
GROUP BY user_id, region 
ORDER BY user_id,region) lt
left join (
SELECT user_id, ((longitude-138) DIV 1)*4+((latitude-38) DIV 0.5) as region, count(datetime) as Count 
FROM gps 
GROUP BY user_id, region 
ORDER BY user_id,region) rt on lt.user_id=rt.user_id AND lt.Count<rt.Count
WHERE rt.Count IS NULL
GROUP BY lt.region
ORDER BY lt.region;

/* to figure out the residential area of each user */
/* we need another view almost the same with Q1 */
CREATE VIEW 'residence' AS
SELECT 'lt'.'user_id' AS 'user_id', 'lt'.'region' AS 'region'
FROM ((SELECT 'daily'.'user_id' AS 'user_id', 'daily'.'region' AS 'region', COUNT('daily'.'day') AS 'count'
       FROM 'daily'
       GROUP BY 'daily'.'user_id' , 'daily'.'region') 'lt'
LEFT JOIN (SELECT 'daily'.'user_id' AS 'user_id', 'daily'.'region' AS 'region', COUNT('daily'.'day') AS 'count'
       FROM 'daily'
       GROUP BY 'daily'.'user_id' , 'daily'.'region') 'rt' 
ON ((('lt'.'user_id' = 'rt'.'user_id') AND ('lt'.'count' < 'rt'.'count'))))
WHERE ('rt'.'count' IS NULL)
ORDER BY 'lt'.'user_id' , 'lt'.'region'

/*SQL query of Q2*/
SELECT day, count(stay) AS stays, region
FROM (
SELECT D.day, count(DISTINCT D.user_id) AS stay, D.region, D.user_id
FROM daily D LEFT JOIN residence R ON R.user_id = D.user_id
WHERE R.region <> D.region
GROUP BY D.day, D.region, D.user_id HAVING count(D.user_id) >= 10
ORDER BY D.day, D.region, D.user_id) AS st
GROUP BY day, region