# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CreateDate
                                 A QGIS plugin
 This plugin supports entering dates into the attribute table
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-06-30
        copyright            : (C) 2020 by Mateusz Orylski
        email                : matory@st.amu.edu.pl
        git sha              : $Format:%H$
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


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load CreateDate class from file CreateDate.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .create_date import CreateDate
    return CreateDate(iface)
