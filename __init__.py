# -*- coding: utf-8 -*-
"""
/***************************************************************************
 BulkVectorExport
                                 A QGIS plugin
 Export map contents to specified format and CRS
                             -------------------
        begin                : 2013-01-21
        copyright            : (C) 2013 by ViaMap Ltd.
        email                : info@viamap.hu
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

def classFactory(iface):
    # load BulkVectorExport class from file BulkVectorExport
    from bulkvectorexport import BulkVectorExport
    return BulkVectorExport(iface)
