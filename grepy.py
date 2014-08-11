################################################################################
#                                                                              #
# grepy                                                                        #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program provides regular expression utilities in Python.                #
#                                                                              #
# copyright (C) 2014 William Breaden Madden                                    #
#                                                                              #
# This software is released under the terms of the GNU General Public License  #
# version 3 (GPLv3).                                                           #
#                                                                              #
# This program is free software: you can redistribute it and/or modify it      #
# under the terms of the GNU General Public License as published by the Free   #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# This program is distributed in the hope that it will be useful, but WITHOUT  #
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or        #
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for    #
# more details.                                                                #
#                                                                              #
# For a copy of the GNU General Public License, see                            #
# <http://www.gnu.org/licenses/>.                                              #
#                                                                              #
################################################################################

import os
import re
import sys

def fileMatch(fileName, regexPattern):
    try:
        file = open(fileName, "rt")
    except IOError:
        return
    for i, line in enumerate(file):
        if regexPattern.search(line):
            lineIndex = i + 1
            return [fileName, lineIndex, line]
    file.close()

def grep(
    directory = None,
    pattern = None
    ):
    regexPattern = re.compile(pattern)
    results = []
    for directoryPath, directoryNames, fileNames in os.walk(directory):
        for fileName in fileNames:
            pathAndFileName = os.path.join(directoryPath, fileName)
            result = fileMatch(pathAndFileName, regexPattern)
            if result:
                results.append(result)
    return(results)