SELECT 
    a.`Year-Month`, 
    a.`Atvinnulausir`, 
    a.`Starfandi`, 
    s.`Value` as gengisvísitala 
FROM 
    atvinnuleysi a
JOIN 
    sedlabanki s 
    ON DATE_FORMAT(s.`Date`, '%Y-%m-01') = a.`Year-Month`
ORDER BY 
    a.`Year-Month`;