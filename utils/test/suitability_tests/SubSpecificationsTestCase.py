# coding: utf-8
# -----------------------------------------------------------------------------
# Copyright 2015 Esri
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
# -----------------------------------------------------------------------------

# ==================================================
# SubSpecificationsTestCase.py
# --------------------------------------------------
# requirements:
# * ArcGIS Desktop 10.X+ or ArcGIS Pro 1.X+
# * Python 2.7 or Python 3.4
#
# author: ArcGIS Solutions
# company: Esri
#
# ==================================================
# history:
# 3/1/2016 - JH - initial creation
# ==================================================

import unittest
import arcpy
import os
import UnitTestUtilities
import Configuration
import DataDownload

class SubSpecificationsTestCase(unittest.TestCase):
    ''' Test all tools and methods related to the Sub Specifications tool
    in the Maritime Decision Aid toolbox'''
    
    def setUp(self):
        if Configuration.DEBUG == True: print("     SubSpecificationsTestCase.setUp")
    
    def tearDown(self):
        if Configuration.DEBUG == True: print("     SubSpecificationsTestCase.tearDown")
    
    def test_sub_specifications_desktop(self):
        arcpy.AddMessage("Testing Sub Specifications (Desktop).")
        self.test_sub_specifications(Configuration.maritime_DesktopToolboxPath)
        
    def test_sub_specifications_pro(self):
        arcpy.AddMessage("Testing Sub Depth Restriction Suitability (Desktop).")
        self.test_sub_specifications(Configuration.maritime_ProToolboxPath)
        
    def test_sub_specifications(self, toolboxPath):
        try:
            if Configuration.DEBUG == True: print("     SubSpecificationsTestCase.test_sub_specifications")
                
            runToolMessage = "Running tool (Sub Specifications)"
            arcpy.AddMessage(runToolMessage)
            Configuration.Logger.info(runToolMessage)
            
            
        except arcpy.ExecuteError:
            UnitTestUtilities.handleArcPyError()
            
        except:
            UnitTestUtilities.handleGeneralError()
            