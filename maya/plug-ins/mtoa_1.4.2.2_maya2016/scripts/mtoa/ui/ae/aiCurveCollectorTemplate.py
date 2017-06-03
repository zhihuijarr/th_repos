import maya.cmds as cmds
import pymel.core as pm
import mtoa.ui.ae.templates as templates
import mtoa.utils as utils
from mtoa.ui.ae.shaderTemplate import ShaderAETemplate


class AEaiCurveCollectorTemplate(ShaderAETemplate):

    def setup(self):
        self.beginScrollLayout()
        self.beginLayout("Curves Settings", collapse=False)
        self.addControl('aiMode', label='Mode')
        
        self.addControl('aiCurveWidth', label='Width')
        pm.mel.AEaddRampControl(self.nodeName + '.aiWidthProfile')
        self.addSeparator()
        self.addControl('aiSampleRate', label='Sample Rate')

        self.addControl('aiCurveShader', label='Shader')
        self.addControl('aiExportRefPoints', label='Export Reference Points')

        self.addControl('aiMinPixelWidth', label='Min Pixel Width')
        self.addSeparator()
        
        self.addControl("aiExportHairIDs", label="Export Hair IDs")
        self.addControl("aiUserOptions", label="User Options")
        self.addSeparator()

        self.addControl("aiSelfShadows", label="Self Shadows")
        self.addControl("aiOpaque", label="Opaque")
        self.addControl("aiVisibleInDiffuse", label="Visible In Diffuse")
        self.addControl("aiVisibleInGlossy", label="Visible In Glossy")
        self.addControl("aiMatte", label="Matte")
        self.addControl("aiTraceSets", label="Trace Sets")

        self.addSeparator()
        self.addControl("primaryVisibility")
        self.addControl("castsShadows")
        

        self.endLayout()

        self.beginLayout('Object Display', collapse=True)
        self.addControl('visibility')
        self.addControl('template')
        self.addControl('ghosting')
        self.addControl('intermediateObject')
        self.endLayout()
        
        self.beginLayout('Draw Override', collapse=True)
        self.addControl('overrideDisplayType')
        self.addControl('overrideLevelOfDetail')
        self.addControl('overrideShading')
        self.addControl('overrideTexturing')
        self.addControl('overridePlayback')
        self.addControl('overrideEnabled')
        self.addControl('useObjectColor')
        self.addControl('objectColor')
        self.endLayout()
    

        # include/call base class/node attributes
        pm.mel.AEdependNodeTemplate(self.nodeName)
        
        self.suppress('blackBox')
        self.suppress('containerType')
        self.suppress('templateName')
        self.suppress('viewName')
        self.suppress('iconName')
        self.suppress('templateVersion')
        self.suppress('uiTreatment')
        self.suppress('customTreatment')
        self.suppress('creator')
        self.suppress('creationDate')
        self.suppress('rmbCommand')
        self.suppress('templatePath')
        self.suppress('viewMode')
        self.suppress('ignoreHwShader')
        self.suppress('boundingBoxScale')
        self.suppress('featureDisplacement')
        self.suppress('boundingBoxScale')
        self.suppress('initialSampleRate')
        self.suppress('extraSampleRate')
        self.suppress('textureThreshold')
        self.suppress('normalThreshold')
        self.suppress('lodVisibility')
        self.suppress('ghostingControl')
        self.suppress('ghostPreSteps')
        self.suppress('ghostPostSteps')
        self.suppress('ghostStepSize')
        self.suppress('ghostRangeStart')
        self.suppress('ghostRangeEnd')
        self.suppress('ghostDriver')
        self.suppress('ghostFrames')
        self.suppress('ghosting')
        self.suppress('ghostCustomSteps')
        self.suppress('ghostColorPreA')
        self.suppress('ghostColorPre')
        self.suppress('ghostColorPostA')
        self.suppress('ghostColorPost')
        self.suppress('tweak')
        self.suppress('relativeTweak')
        self.suppress('currentUVSet')
        self.suppress('displayImmediate')
        self.suppress('displayColors')
        self.suppress('displayColorChannel')
        self.suppress('currentColorSet')
        self.suppress('smoothShading')
        self.suppress('drawOverride')
        self.suppress('shadingSamples')
        self.suppress('maxVisibilitySamplesOverride')
        self.suppress('maxVisibilitySamples')
        self.suppress('antialiasingLevel')
        self.suppress('maxShadingSamples')
        self.suppress('shadingSamplesOverride')
        self.suppress('geometryAntialiasingOverride')
        self.suppress('antialiasingLevel')
        self.suppress('volumeSamplesOverride')
        self.suppress('volumeSamples')
        self.suppress('depthJitter')
        self.suppress('ignoreSelfShadowing')
        self.suppress('controlPoints')
        self.suppress('colorSet')
        self.suppress('uvSet')
        self.suppress('weights')
        self.suppress('renderInfo')
        self.suppress('renderLayerInfo')
        self.suppress('compInstObjGroups')
        self.suppress('instObjGroups')
        self.suppress('collisionOffsetVelocityIncrement')
        self.suppress('collisionOffsetVelocityMultiplier')
        self.suppress('collisionDepthVelocityMultiplier')
        self.suppress('collisionDepthVelocityIncrement')
    

        self.addExtraControls()        
        self.endScrollLayout()