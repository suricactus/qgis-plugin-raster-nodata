## About

The QGIS Raster nodata plugin allows for manipulating the nodata values in a raster files directly in QGIS with the help of GDAL.

## Current version and branches

The [master branch](https://github.com/kbgg/qgis-stac-browser/tree/master) is the active development version of the plugin. It is currently version **0.2** of the plugin. The 
[releases](https://github.com/suricactus/qgis-raster-nodata/releases) is where you can find stable versions of this plugin. 
Whenever `master` stabilizes a release is cut and then a new release is produced. So master is not very stable and should be used with caution.
It is possible that there may be small releases in quick succession, especially if they are nice improvements that do 
not require lots of updating.

## Install

The plugin can be directly installed by downloading the latest version from [releases](https://github.com/suricactus/qgis-raster-nodata/releases). The zip must be then extracted and copied to the plugins directory.

### Linux

Ususally the plugins directory is located in ~/.local/share/QGIS/QGIS3/profiles/default/python/plugins.

## Building

To build the plugin and deploy to your plugin directory you will need the [pb_tool](http://g-sherman.github.io/plugin_build_tool/) CLI tool.

To compile the plugin run the following command in the root directory of this repository:
 
    pb_tool compile
     
Compiling is needed any time the resources.py file needs to be rebuilt. 

To deploy the application to your QGIS plugins directory run the following command and reload the plugin within QGIS:

    pb_tool deploy 

It's recommended to use the Plugin Reloader plugin within QGIS to easily reload the plugin during development.

