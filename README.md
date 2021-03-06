[![Planned Issues](https://badge.waffle.io/Esri/solutions-geoprocessing-toolbox.png?label=0%20-%20backlog&title=In%20Backlog)](https://waffle.io/Esri/solutions-geoprocessing-toolbox)
[![Issues in Progress](https://badge.waffle.io/Esri/solutions-geoprocessing-toolbox.png?label=2%20-%20In%20Progress&title=In%20Progress)](https://waffle.io/Esri/solutions-geoprocessing-toolbox)
[![Issues waiting for Verification](https://badge.waffle.io/Esri/solutions-geoprocessing-toolbox.png?label=3%20-%20Verify&title=For%20Verification)](https://waffle.io/Esri/solutions-geoprocessing-toolbox)
[![Code Climate](https://codeclimate.com/github/Esri/solutions-geoprocessing-toolbox/badges/gpa.svg)](https://codeclimate.com/github/Esri/solutions-geoprocessing-toolbox)
# solutions-geoprocessing-toolbox

The ArcGIS Solutions Geoprocessing Toolbox is a collection of models, scripts, and tools for use in [ArcGIS for Desktop](http://www.esri.com/software/arcgis/arcgis-for-desktop) and [ArcGIS Pro](http://www.esri.com/en/software/arcgis-pro). These tools provide specialized processing, workflows, and analysis for defense, intelligence, emergency management, and other solutions domains. With these tools you can determine visibility from a specific viewpoint, create search grids, and analyze event data. They are included with many of Esri's [Solutions Templates](http://solutions.arcgis.com/), but developers can use this repository to download and contribute to the tool development process.

![Image of the toolbox](solutions-geoprocessing-toolbox-thumbnail007.png)


###Repository Owner: [Matt](https://github.com/mfunk)

* Merge Pull Requests
* Creates Releases and Tags
* Manages Milestones
* Manages and Assigns Issues

###Secondary: [Chris](https://github.com/csmoore)

* Backup when the Owner is away

Additional information is available in the repository's [Wiki](https://github.com/Esri/solutions-geoprocessing-toolbox/wiki).

## Sections

* [Features](#features)
* [Requirements](#requirements)
* [A Tale of Two Toolboxes](#a-tale-of-two-toolboxes)
* [Instructions To Get Started](#instructions-to-get-started)
	* [General Help](#general-help)
	* [Getting Started with the tools](#getting-started-with-the-tools)
	* [Downloading Test Data](#downloading-test-data)
	* [Running Verification Tests](#running-verification-tests)
* [Resources](#resources)
* [Issues](#issues)
* [Contributing](#contributing)
* [Credits](#credits)
* [Licensing](#licensing)

## Features

* Specialized geoprocessing models and tools for general defense and intelligence analysis tasks including
  * Tools for visibility and range analysis
  * Tools for analyzing the battlefield environment
  * Tools for data management and coordinates 

* The [**capability**](./capability/README.md) folder contains:
  * ERG (Emergency Resources Guide) Tools
  * Helicopter Landing Zone Tools
  * Point Of Origin Tools

* The [**data_management**](./data_management/README.md) folder contains:
  * Adjust Sample Data Dates Tools
  * CADRG ECRG Tools
  * CIB Tools
  * Elevation Tools
  * Geonames Tools
  * Import and Conversion Tools - formerly Position Analysis Tools
  * LiDAR Elevation Tools
  * Network Data Preparation Tools
  * Patrol Data Capture Tools
  * Publishable Task Tools

* The [**operational_graphics**](./operational_graphics/README.md) folder contains:
  * Clearing Operations Tools
  * Range Card Tools
  
* The [**patterns**](./patterns/README.md) folder contains:
  * Incident Analysis Tools
  * Movement Analysis Tools

* The [**suitability**](./suitability/README.md) folder contains:
  * Maritime Decision Aid Tools
  * Military Aspects of Terrain Tools
  * Military Aspects of Weather Tools
  * Path Slope Tools

* The [**visibility**](./visibility/README.md) folder contains:
  * Sun Position Analysis Tools
  * Visibility and Range Tools
  * Visibility Data Prep Tools

## Requirements

* ArcGIS Desktop 10.4+ or ArcGIS Pro 1.1+
    * Check [Releases](https://github.com/Esri/solutions-geoprocessing-toolbox/releases) for tools for previous versions of ArcGIS Desktop
* Apache Ant - used to download and extract dependent data and run test drivers
* Java Runtime Environment (JRE) or Developer Kit (JDK) (required by Ant)
* Some tools require additional licenses (these tools will be disabled if license is unavailable), see READMEs for more information: 
    * ArcGIS Desktop Advanced (ArcInfo)
    * ArcGIS Spatial Analyst Extension
    * ArcGIS 3D Analyst Extension
    * ArcGIS Network Analyst Extension
    * For example these tools require Desktop Advanced and Spatial Analyst:
        * Path Slope Tools.tbx\Path Slope
        * Visibility and Range Tools.tbx\Range Fan

## A Tale of Two Toolboxes

The solutions-geoprocessing-toolbox repo is now supporting toolboxes for both ArcMap/ArcCatalog/ArcGlobe/ArcScene (collectively called ArcGIS for Desktop) and also ArcGIS Pro. Toolboxes that are modified in ArcGIS Pro are not
backwards compatible with other ArcGIS Desktop applications (ArcMap), so most toolboxes are duplicated for one or the other. The naming of these toolboxes is as follows:

* Toolboxes that are for ArcGIS Desktop 10.4 will include *_10.4* after the toolbox name. For example: **Visibility and Range Tools_10.4.tbx**
* Toolboxes with a 'unversioned' name are for ArcGIS Pro 1.1. For example: **Visibility and Range Tools.tbx**


Please note that some toolboxes are for ArcGIS Pro only, or ArcGIS Desktop 10.4 only. These toolboxes will follow the above naming convention, but will not have a duplicate.

* [Product info for ArcGIS Pro](http://www.esri.com/software/arcgis-pro)
* [Help for ArcGIS Pro](http://pro.arcgis.com/en/pro-app/)


## Instructions To Get Started

### General Help
[New to Github? Get started here.](http://htmlpreview.github.com/?https://github.com/Esri/esri.github.com/blob/master/help/esri-getting-to-know-github.html)

[Downloading Test Data](#downloading-test-data) and [Running Verification Tests](#running-verification-tests) are only available through the GitHub repository, and are not available from other download versions of the repository.

### Getting Started with the tools

* Download the Github repository
    * If repository was downloaded as a zip, extract the zip file
    * Make note of this directory, the steps below assume it will be called "solutions-geoprocessing-toolbox"

### Downloading Test Data

**This section is under reconstruction, per issue [#371](https://github.com/Esri/solutions-geoprocessing-toolbox/issues/371)** 

### Running Verification Tests

**This section is under reconstruction, per issue [#371](https://github.com/Esri/solutions-geoprocessing-toolbox/issues/371)**

## Resources

* Learn more about [ArcGIS Solutions](http://solutions.arcgis.com/).
* Learn more about [ArcGIS for the Military](http://solutions.arcgis.com/military/).
* Learn more about [ArcGIS for Intelligence](http://solutions.arcgis.com/intelligence/).
* Learn more about [ArcGIS for Emergency Management](http://solutions.arcgis.com/emergency-management/).
* Learn more about [ArcGIS Pro](http://pro.arcgis.com/en/pro-app/).

## Issues

* Find a bug or want to request a new feature?  Please let us know by submitting an issue.

## Contributing

Esri welcomes contributions from anyone and everyone through GitHub. Please see Esri's [guidelines for contributing](https://github.com/esri/contributing).

When you contribute to this repository we ask that you follow the guidelines below. If you've got questions, or you get stuck, please ask the [Repository Owner](#repository-owner). We are here to help! Thanks.

### Fork and Clone the Repo
Start contributing to the solutions-geoprocessing-toolbox repo by making a fork and cloning it to your local machine.

* Fork the **dev** branch from the repo on github.com with ![fork button](ForkButtonIcon.png)
* Clone your remote onto your local system ![clone button](CloneInDesktopButtonIcon.png)
* Get the *mdcs-py* submodule:
	* `> git submodule init`
	* `> git submodule update`

### Set Your Upstream
Setting the parent repo to get changes from.

* `> git remote -v`

if no *upstream* is listed continue with:

* `> git remote add upstream https://github.com/Esri/solutions-geoprocessing-toolbox`
* `> git remote set-url upstream --push no_push`

check that an *upstream* is registered:

* `> git remote -v`

### Getting Changes from Upstream
The solutions-geoprocessing-toolbox repo changes often, so make sure you are getting the latest updates often.

* `> git fetch upstream`
* `> git merge upstream/dev`
*

### Share Your Mods
If you've made changes to the repo that you want to share with the community.

* Commit your changes to your local
* Sync local with your remote fork
* Make a **Pull Request** from your remote fork on github.com ![New Pull Request](NewPullRequestButtonIcon.png)


### Notes On Contributing
* Always work in the **dev** branch, never in *master*. This helps us keep our releases clean.
* Never merge Pull Requests. The [Repository Owner](#repository-owner) needs to test any updates to make sure the repo is stable.
* Always log an [Issue](https://github.com/Esri/solutions-geoprocessing-toolbox/issues) for problems you find, though you should check through the existing issues to make sure it wasn't already logged. 


## Credits
Mosaic Dataset Configuration Scripts (MDCS) is an Esri repo available at [https://github.com/Esri/mdcs-py](https://github.com/Esri/mdcs-py) and [licensed](https://github.com/Esri/mdcs-py/blob/master/license.txt) under Apache License Version 2.0, January 2004.

## Licensing

Copyright 2015 Esri

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

A copy of the license is available in the repository's
[license.txt](license.txt) file.

[](Esri Tags: ArcGIS Defense and Intelligence Military Emergency Management National Security)
[](Esri Language: Python)
