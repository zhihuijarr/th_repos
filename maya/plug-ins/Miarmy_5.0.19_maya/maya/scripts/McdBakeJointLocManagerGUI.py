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
## TRADE PRACTICE. IN NO EVENT WILL BASEFOUNTAIN AND/OR ITS LICENSORS 
## BE LIABLE FOR ANY LOST REVENUES, DATA, OR PROFITS, OR SPECIAL, 
## DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES, EVEN IF BASEFOUNTAIN 
## AND/OR ITS LICENSORS HAS BEEN ADVISED OF THE POSSIBILITY 
## OR PROBABILITY OF SUCH DAMAGES.
##
## ===================================================================
## -

## +
## ===================================================================
##  Module Name: Bake joint locator manager
##
##  Description:
##    For managing Particle in scene, globally.
##
## ===================================================================
## -

import maya.cmds as cmds
from McdGeneral import *
from McdSimpleCmd import *

import McdBakeJointLocManager
reload(McdBakeJointLocManager)
from McdBakeJointLocManager import *


def McdBakeJointLocManagerGUI():
    
    winName = "McdBakeJointLocManager"
    if cmds.window(winName, ex = True):
        cmds.deleteUI(winName)
    cmds.window(winName, title = "Bake Joint Locator Manager",rtf =True,menuBar=True, width=200)
    
    cmds.menu( label='Options')
    cmds.menuItem( label='Refresh contents', c = "McdRefreshBakeJointLocManager()")
    cmds.menuItem( label='Help' )
    cmds.menuItem( divider=True )
    cmds.menuItem( label='Exit', c = "McdExitBakeJointLocManager()" )
    
    form = cmds.formLayout()
    tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
    cmds.formLayout( form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)) )
    
    #-------------------------  Initialize  -------------------------#
    ## get contents here:
    info = McdBakeRecInit()
    
    globalNode = McdGetMcdGlobalNode()
    try:
        bkScDef = cmds.getAttr(globalNode + ".bkScaleD")
    except:
        bkScDef = 1.0
    
    #--------------------------  Main GUI  --------------------------#
    child0 = cmds.columnLayout(adj = True)
    cmds.rowColumnLayout(nc = 6, cw = [(1,120),(2,10),(3,120),(4, 10),(5, 100), (6, 100)])
    cmds.button(l = "Expand", c = "McdExpandBakeRec()")
    cmds.text(l = "")
    cmds.button(l = "Delete", c = "McdDeleteBakeRec()")
    cmds.text(l = "")
    cmds.text(l = "Default Scale")
    cmds.floatField("scaleD_bk", v = bkScDef, cc = "changeBKManagerSD(\"" + globalNode + "\")")

    cmds.setParent("..")
    
    
    cmds.rowColumnLayout(nc = 5, cw = [(1,100),(2,100),(3,80),(4,80),(5,80)])
    cmds.text(l = "Bone Name", align = "left", font = "smallBoldLabelFont")
    cmds.text(l = "Action Name", align = "left", font = "smallBoldLabelFont")
    cmds.text(l = "Start", align = "left", font = "smallBoldLabelFont")
    cmds.text(l = "End", align = "left", font = "smallBoldLabelFont")
    cmds.text(l = "ScaleX", align = "left", font = "smallBoldLabelFont")
    
    # fill contents here:
    if info != []:
        for i in range(len(info) / 5):
            stri = str(i)
            cmds.textField("boneName_bktf" + stri, tx = info[i*5], cc = "changeBKManagerBN("+stri+", \"" + globalNode + "\")")
            cmds.textField("actionName_bktf" + stri, tx = info[i*5+1], cc = "changeBKManagerAN("+stri+", \"" + globalNode + "\")")
            cmds.intField("startFrame_bkff" + stri, v = info[i*5+2], cc = "changeBKManagerSF("+stri+", \"" + globalNode + "\")")
            cmds.intField("endFrame_bkff" + stri, v = info[i*5+3], cc = "changeBKManagerEF("+stri+", \"" + globalNode + "\")")
            cmds.floatField("scaleX_bkff" + stri, v = info[i*5+4], cc = "changeBKManagerSX("+stri+", \"" + globalNode + "\")")
    
    cmds.setParent("..")
    
    cmds.text(l = "")
    cmds.button(l = "Generate Locator and Bake...", h = 40, c = "bakeJointActionInfoToLocator()")
    
    cmds.setParent("..")
    
    
    #------------------------------- Cricial Help --------------------------------#
    child1 = cmds.columnLayout(adj = True)
    cmds.text(l = "* List all the agent emitter in scene", fn = "smallBoldLabelFont", align = "left")
    
    cmds.separator(h = 10)
    cmds.button(l = "Check detailed help")
    
    cmds.setParent( '..' )
    
    
    cmds.tabLayout( tabs, edit=True,tabLabel=((child0, "Agent Emitter in Scene"),(child1, "Quick Tips")))
    cmds.showWindow(winName)



def McdRefreshBakeJointLocManager():
    McdBakeJointLocManagerGUI()

def McdExitBakeJointLocManager():
    try:
        cmds.deleteUI("McdBakeJointLocManager")
    except:
        pass


