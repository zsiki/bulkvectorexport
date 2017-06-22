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
"""
# Import the PyQt and QGIS libraries
from PyQt4 import QtCore, QtGui
from osgeo import ogr
from qgis.core import *
import qgis.utils
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from bulkvectorexportdialog import BulkVectorExportDialog


class BulkVectorExport:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = QtCore.QFileInfo(QgsApplication.qgisUserDbFilePath()).path() + "/python/plugins/bulkvectorexport"
        # initialize locale
        localePath = ""
        locale = QtCore.QSettings().value("locale/userLocale")[0:2]

        if QtCore.QFileInfo(self.plugin_dir).exists():
            localePath = self.plugin_dir + "/i18n/bulkvectorexport_" + \
                locale + ".qm"

        if QtCore.QFileInfo(localePath).exists():
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QtCore.QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = BulkVectorExportDialog()

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QtGui.QAction( \
            QtGui.QIcon(":/plugins/bulkvectorexport/icon.png"), \
            u"Export map contents to specified format and CRS", \
            self.iface.mainWindow())
        # connect the action to the run method
        QtCore.QObject.connect(self.action, QtCore.SIGNAL("triggered()"), self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&Bulk vector export", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&Bulk vector export", self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def run(self):
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
            # get target directory
            dirName = self.dlg.ui.dirEdit.text().strip()
            if len(dirName) == 0:
                QtGui.QMessageBox.critical(self.dlg, "BulkVectorExport", \
                    "No directory entered")
                return
            if dirName[len(dirName)-1] != "/":
                dirName = dirName + "/"
            if not QtCore.QFileInfo(dirName).isDir():
                QtGui.QMessageBox.critical(self.dlg, "BulkVectorExport", \
                    "No such directory : " + dirName)
                return
            # get ogr driver name
            ogr_driver_name = self.dlg.ui.formatBox.currentText()
            print"Driver ogr name: " + ogr_driver_name
            layers = qgis.utils.iface.mapCanvas().layers()
            for layer in layers:
                layerType = layer.type()
                if layerType == QgsMapLayer.VectorLayer:
                    print 'Writing:' + layer.name()
                    layer_filename = dirName + layer.name()
                    print 'Filename: ' + layer_filename
                    if self.dlg.ui.layerCrsButton.isChecked():
                        crs = layer.crs()
                    else:
                        crs = qgis.utils.iface.mapCanvas().mapRenderer().destinationCrs()
                    print "CRS selected: " + crs.description()
                    result2 = qgis.core.QgsVectorFileWriter.writeAsVectorFormat(layer, layer_filename, layer.dataProvider().encoding(), crs, ogr_driver_name)
                    print "Status: " + str(result2)
                    if result2 != 0:
                        QtGui.QMessageBox.warning(self.dlg, "BulkVectorExport",\
                            "Failed to export: " + layer.name() + \
                            " Status: " + str(result2))
