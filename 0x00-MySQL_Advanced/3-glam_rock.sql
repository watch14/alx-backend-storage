-- bands
SELECT band_name,
       IFNULL(YEAR(2022) - CAST(SUBSTRING_INDEX(lifespan, '-', 1) AS UNSIGNED), 0) AS lifespan
FROM metal_bands
WHERE FIND_IN_SET('Glam rock', main_style)
ORDER BY lifespan DESC;
