
#------------------------------------------------------------------------------
# Copyright 2014 Esri
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# UpdateDefensivePositionDomain.py
# Created on: 2013-08-06 09:56:31.00000
#   (generated by ArcGIS/ModelBuilder)
# Description:
# Updates the Defensive Positions domain used in the drop down while creating weapon positions.
# ---------------------------------------------------------------------------

# Import arcpy module
import sys, traceback
import arcpy
from arcpy import env

try:
    #Set local parameters
    domTable = arcpy.GetParameterAsText(0)
    codeField = arcpy.GetParameterAsText(1)
    descField = arcpy.GetParameterAsText(1)
    dWorkspace = arcpy.GetParameterAsText(2)
    domName = "Def_POS_Description"
    updateOption = "REPLACE"

    # Process: Create a domain from an existing table
    arcpy.TableToDomain_management(domTable, codeField, descField, dWorkspace, domName, update_option=updateOption)

except arcpy.ExecuteError:
    # Get the tool error messages
    msgs = arcpy.GetMessages()
    arcpy.AddError(msgs)
    #print msgs #UPDATE
    print(msgs)

except:
    tb = sys.exc_info()[2]
    #print "Line %i" % tb.tb_lineno #UPDATE
    print("Line %i" % tb.tb_lineno)
    #print e.message #UPDATE
    print(e.message)

    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]

    # Concatenate information together concerning the error into a message string
    pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
    msgs = "\nArcPy ERRORS:\n" + arcpy.GetMessages() + "\n"

    # Return python error messages for use in script tool or Python Window
    arcpy.AddError(pymsg)
    arcpy.AddError(msgs)

    # Print Python error messages for use in Python / Python Window
    #print pymsg + "\n" #UPDATE
    print(pymsg + "\n")
    #print msgs #UPDATE
    print(msgs)



