SELECT 
    a."Year-Month", 
    a."Atvinnulausir", 
    a."Starfandi", 
    s."Value" as gengisvísitala 
FROM 
    atvinnuleysi a
JOIN 
    sedlabanki s 
    ON TO_CHAR(s."Date"::date, 'YYYY-MM-01') = a."Year-Month"
ORDER BY 
    a."Year-Month";