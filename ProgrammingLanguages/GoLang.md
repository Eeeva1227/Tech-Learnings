# GoLang

### go.sum and go.mod
Module is go support for dependency management. A module by definition is a collection of related packages with go.mod at its root.

The **go.mod** file defines
- Module import path
- The version of go with which the module is created
- Dependency requirements of the module for a successful build. It defines both project's dependencies requirements and also locks them to their correct version.


**go.sum**
This file lists down the checksum of direct and indirect dependency required along with the version.

The checksum present in **go.sum** file is used to validate the checksum of each of direct and indirect dependency to confirm that none of them has been modified.


# Makefile in GoLang