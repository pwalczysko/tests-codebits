Examples:

```
python operetta-metadata.py --well G03 --plate ML-BE001-01
```

will return all the images in "Well G03" and "Plate ML-BE001-01" and the line from the metadata CSV pertaining to this Well.

```
python operetta-metadata.py --imagename r03c03f25p01-ch4sk1fk1fl1.tiff --plate ML-BE001-01
```
will return all the images in "Well C03" (i.e. all the images belonging to the same well as the image passed on input) and "Plate ML-BE001-01" and the line from the metadata CSV pertaining to this Well.
