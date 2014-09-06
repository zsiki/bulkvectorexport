# -*- coding: utf-8 -*-
"""
/***************************************************************************
 BulkVectorExportDialog
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
"""

from PyQt4 import QtCore, QtGui
from ui_bulkvectorexport import Ui_BulkVectorExportDialog
from osgeo import ogr
# create the dialog for zoom to point


class BulkVectorExportDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_BulkVectorExportDialog()
        self.ui.setupUi(self)
        # dir button push event
        QtCore.QObject.connect(self.ui.dirButton, QtCore.SIGNAL('clicked()'), self.getDir)
        self.unsupportedDriverList = ['Memory', 'PostgreSQL', 'MySQL', 'ODBC', \
            'S57']

    def showEvent(self, event):
        if self.ui.formatBox.count() == 0:
            # get available ogr driver names which can be created
            #driverNameList = qgis.core.QgsVectorFileWriter.ogrDriverList()
            driverNameList = []
            for i in range(ogr.GetDriverCount()):
                name = ogr.GetDriver(i).GetName()
                if not name in driverNameList and \
                    not name in self.unsupportedDriverList and \
                    ogr.GetDriver(i).TestCapability(ogr.ODrCCreateDataSource):
                    driverNameList.append(name)
            self.ui.formatBox.addItems(sorted(driverNameList))

    def getDir(self):
        dirName = str(QtGui.QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.ui.dirEdit.setText(dirName)
