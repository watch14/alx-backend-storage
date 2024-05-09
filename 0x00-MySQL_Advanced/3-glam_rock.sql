-- bands
SELECT band_name, IFNULL(split, 2022) - formed AS lifespan
FROM metal_bands
WHERE main_style = 'Glam rock'
ORDER BY lifespan DESC;
