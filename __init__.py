# -*- coding: utf-8 -*-
"""
/***************************************************************************
 RasterNodata
                                 A QGIS plugin
 Set, update, remove nodata value for raster
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2019-01-19
        copyright            : (C) 2019 by suricactus
        email                : suricactus@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

__author__ = 'suricactus'
__date__ = '2019-01-19'
__copyright__ = '(C) 2019 by suricactus'


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load RasterNodata class from file RasterNodata.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .raster_nodata import RasterNodataPlugin
    return RasterNodataPlugin()
