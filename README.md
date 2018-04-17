# EPSG:900913 to EPSG:4326 Polygon Converter

## Project Description

This Python script (written in **Python 3.6.5**) converts an EPSG:900913 polygon to an EPSG:4326 polygon. The input polygon uses the EPSG:900913 map projection which works with (x,y) coordinates. The output polygon uses the EPSG:4326 map projection which works with longitude and latitude values.

## Usage

    python polygon_epsg900913_to_epsg4326.py  

## Examples

**Example input:** 

POLYGON((-437396.91611144005\_6962698.374744099,
-437396.91611144005\_6965220.7966772,
-433555.95544064\_6965220.7966772,
-433555.95544064\_6962698.3747441005,
-437396.91611144005\_6962698.374744099))

**Example ouput:** 

POLYGON((-3.929203350243457 52.89011715234372,
-3.929203350243457 52.903786385493476,
-3.894699413475837 52.903786385493476,
-3.894699413475837 52.89011715234372,
-3.929203350243457 52.8901171523437))

