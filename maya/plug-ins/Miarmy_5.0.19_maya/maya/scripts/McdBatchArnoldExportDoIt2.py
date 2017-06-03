## +
## ===================================================================
## Copyright(C) 2010 - 2014 Basefount Software Limited.
## and/or its licensors.  All rights reserved.
##
## The coded instructions, statements, computer programs, and/or
## related material (collectively the "Data") in these files contain
## unpublished information proprietary to Basefount Technology
## Limitd. ("Basefount") and/or its licensors, which is
## protected by Chinese copyright law and by international treaties.
##
## The Data is provided for use exclusively by You. You have the right 
## to use, modify, and incorporate this Data into other products for 
## purposes authorized by the Basefount software license agreement, 
## without fee.
##
## The copyright notices in the Software and this entire statement, 
## including the above license grant, this restriction and the 
## following disclaimer, must be included in all copies of the 
## Software, in whole or in part, and all derivative works of 
## the Software, unless such copies or derivative works are solely 
## in the form of machine-executable object code generated by a 
## source language processor.
##
## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND. 
## BASEFOUNT DOES NOT MAKE AND HEREBY DISCLAIMS ANY EXPRESS OR
## IMPLIED WARRANTIES INCLUDING, BUT NOT LIMITED TO, THE WARRANTIES
## OF NON-INFRINGEMENT, MERCHANTABILITY OR FITNESS FOR A PARTICULAR 
## PURPOSE, OR ARISING FROM A COURSE OF DEALING, USAGE, OR 
## TRADE PRACTICE. IN NO EVENT WILL BASEFOUNT AND/OR ITS LICENSORS 
## BE LIABLE FOR ANY LOST REVENUES, DATA, OR PROFITS, OR SPECIAL, 
## DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES, EVEN IF BASEFOUNTAIN 
## AND/OR ITS LICENSORS HAS BEEN ADVISED OF THE POSSIBILITY 
## OR PROBABILITY OF SUCH DAMAGES.
##
## ===================================================================
## -

## +
## ===================================================================
##  Module Name: McdAutoGenAgentCache.py
##
##  Description:
##    Generate agent cache in command line
##
## ===================================================================
## -

import maya.cmds as cmds
import maya.mel as mel
from McdGeneral import *
import os

## +
## ===================================================================
## Copyright(C) 2010 - 2014 Basefount Software Limited.
## and/or its licensors.  All rights reserved.
##
## The coded instructions, statements, computer programs, and/or
## related material (collectively the "Data") in these files contain
## unpublished information proprietary to Basefount Technology
## Limitd. ("Basefount") and/or its licensors, which is
## protected by Chinese copyright law and by international treaties.
##
## The Data is provided for use exclusively by You. You have the right 
## to use, modify, and incorporate this Data into other products for 
## purposes authorized by the Basefount software license agreement, 
## without fee.
##
## The copyright notices in the Software and this entire statement, 
## including the above license grant, this restriction and the 
## following disclaimer, must be included in all copies of the 
## Software, in whole or in part, and all derivative works of 
## the Software, unless such copies or derivative works are solely 
## in the form of machine-executable object code generated by a 
## source language processor.
##
## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND. 
## BASEFOUNT DOES NOT MAKE AND HEREBY DISCLAIMS ANY EXPRESS OR
## IMPLIED WARRANTIES INCLUDING, BUT NOT LIMITED TO, THE WARRANTIES
## OF NON-INFRINGEMENT, MERCHANTABILITY OR FITNESS FOR A PARTICULAR 
## PURPOSE, OR ARISING FROM A COURSE OF DEALING, USAGE, OR 
## TRADE PRACTICE. IN NO EVENT WILL BASEFOUNT AND/OR ITS LICENSORS 
## BE LIABLE FOR ANY LOST REVENUES, DATA, OR PROFITS, OR SPECIAL, 
## DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES, EVEN IF BASEFOUNTAIN 
## AND/OR ITS LICENSORS HAS BEEN ADVISED OF THE POSSIBILITY 
## OR PROBABILITY OF SUCH DAMAGES.
##
## ===================================================================
## -

## +
## ===================================================================
##  Module Name: McdAutoGenAgentCache.py
##
##  Description:
##    Generate agent cache in command line
##
## ===================================================================
## -

import maya.cmds as cmds
import maya.mel as mel
from McdGeneral import *
from McdRenderARFunctions import *

def McdBatchArnoldExportDoIt2(folderStr, nameStr, arFolderStr, arNameStr, dsoFolderStr, saveAsStr):
    # ---------------------------------------
    # place agent out
    # turn off mesh drive and agent cache
    # go back to start frame
    # make agent cache
    # ---------------------------------------
    
    # # find the locator which name is MiarmyProLocator2016168
    # proLoc = cmds.ls("MiarmyProLocator2016019988")
    # if proLoc == [] or proLoc == None:
    #     raise Exception("You don't have license, pleaes buy Miarmy Pro")
    
    # place agent out
    cmd = "McdPlacementCmd -am 3 -ign 0;"
    mel.eval(cmd)
    McdAfterPlaceFunction()
    
    # turn off mesh drive and agent cache
    allGlb = cmds.ls(type = "McdGlobal")
    if McdIsBlank(allGlb):
        raise Exception("No found McdGlobal Node.")
        return
    
    for i in range(len(allGlb)):
        cmds.setAttr(allGlb[i] + ".enableMeshDrv", 0)
        cmds.setAttr(allGlb[i] + ".selectionCallback", 1)
        cmds.setAttr(allGlb[i] + ".enableCache", 1)
        
        cmds.setAttr(allGlb[i] + ".cacheFolder", folderStr, type = "string")
        cmds.setAttr(allGlb[i] + ".cacheName", nameStr, type = "string")
        
        cmds.setAttr(allGlb[i] + ".outARFd", arFolderStr, type = "string")
        cmds.setAttr(allGlb[i] + ".outARNm", arNameStr, type = "string")
        cmds.setAttr(allGlb[i] + ".arProc", dsoFolderStr, type = "string")
        
    
    # export ass
    McdARSetupAllFrame();
    
    # add render
    McdBuildArnoldStandin(allGlb[0])
    

    # save scene as a new one!
    fileType = cmds.file(q = True, type = True)[0]
    cmds.file(rename = saveAsStr)
    cmds.file( save = True, type = fileType )
    
    
    

def McdBuildArnoldStandin(globalNode):
    
    dExpFolder = cmds.getAttr(globalNode + ".outARFd")
    dExpName = cmds.getAttr(globalNode + ".outARNm")
    
    # create arnold standin:
    nodeName = "Mcd" + dExpName + "AssStandinShape"
    nodeParentName = "Mcd" + dExpName
    cmds.createNode("aiStandIn", n = nodeName)

    fillFile = dExpFolder + '/' + dExpName + '/assStandin/assStandin.####.ass'
    cmds.setAttr(nodeName + ".dso", fillFile, type = "string")
    
    cmds.connectAttr("time1.outTime", nodeName + ".frameNumber")
    
    cmds.setAttr(nodeName + ".deferStandinLoad", 0)
    
    cmds.sets(nodeName, e = True, fe = "defaultLightSet")

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    