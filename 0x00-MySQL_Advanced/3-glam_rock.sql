-- bands
SELECT band_name, 
       IF(split = 0, 2022 - formed, 2022 - split) AS lifespan
FROM metal_bands
WHERE main_style = 'Glam rock'
ORDER BY lifespan DESC;
