# SKILL API 快速参考卡

> 按功能领域分类的常用函数速查

---

## 电路/约束

**466 个函数**

```
ciAPRCascodeIterator               ciAPRXYInstSymmetricIterator       
ciActiveSameCellAndSizeIterator    ciAddHierarchicalNotes             
ciAddLeadingSlash                  ciAddProcessRules                  
ciAddRuleGroup                     ciAddStructArg                     
ciAddTrailingSlash                 ciAlignPinsOnCellSide              
ciAllCellViewsInHierarchy          ciAxisCreate                       
ciAxisDelete                       ciAxisExists                       
ciAxisListCon                      ciAxisListParams                   
ciAxisReplaceParams                ciBasicGetParamValue               
ciBlockResistorArrayIterator       ciBuildModgenParams                
ciBundleSignalsIterator            ciCPRegistrationFromLAM            
ciCacheCallbackRegister            ciCacheCallbackUnregister          
ciCacheCallbackUpdate              ciCacheCellName                    
ciCacheConstraintCellName          ciCacheConstraintLibName           
ciCacheConstraintViewName          ciCacheDiscardEdits                

```

## ADE XL 仿真

**283 个函数**

```
axlAddJobPolicy                    axlAddModelPermissibleSectionLists  $adexlSKILLref/modelRelated.html
axlAddOutputExpr                   axlAddOutputSignal                 
axlAddOutputs                      axlAddOutputsColumn                
axlAddSpecToOutput                 axlAttachJobPolicy                 
axlCloseSession                    axlCloseSessionInWindow            
axlCloseSetupDB                    axlCommitSetupDB                   
axlCommitSetupDBAndHistoryAs       axlCommitSetupDBas                 
axlCorners                         axlCreateSession                   
axlCustomADETestName               axlDeleteJobPolicy                 
axlDeleteNote                      axlDeleteOutput                    
axlDeleteOutputsColumn             axlDetachJobPolicy                 
axlDiffSetup                       axlExportOutputView                
axlExportSetup                     axlGetActiveSetup                  
axlGetAllCornersEnabled            axlGetAllParametersDisabled        
axlGetAllSweepsEnabled             axlGetAllVarsDisabled              

```

## GUI 界面操作

**180 个函数**

```
hiAddExtraRepeatCommand            hiAddIconOverrides                 
hiAddMenuItem                      hiAddNonRepeatPrefix               
hiAddToolbarItem                   hiAddToolbarItems                  
hiAdvanceProgressBarOneStep        hiBoxCenter                        
hiCancelProgressBox                hiCheckAbort                       
hiClearClipboard                   hiCreate2DMenu                     
hiCreateAction                     hiCreateHorizontalFixedMenu        
hiCreateMenu                       hiCreateMenuItem                   
hiCreatePulldownMenu               hiCreateSeparatorMenuItem          
hiCreateSimpleMenu                 hiCreateSliderMenuItem             
hiCreateToolbar                    hiCreateToolbarComboBox            
hiCreateToolbarSeparator           hiCreateToolbarTypein              
hiCreateTypeinMenuItem             hiCreateVerticalFixedMenu          
hiDBoxCancel                       hiDBoxOK                           
hiDeleteMenu                       hiDeleteMenuItem                   

```

## 数据库操作

**185 个函数**

```
db10_OCEAN                         db20_OCEAN                         
dbAddPlaceAreaBackgroundDef        dbAddRowBackgroundDef              
dbAttachRowRegionToPRBoundary      dbCanonicalizeAnyAngleTransform    
dbCellViewHasEquivalentConnectivityTimedbCellViewHasPhotonicPinFig        
dbCellViewResetAllColorLockTypes        $skdfref/mpt.htmldbClearPcellCache                  
dbCompressionPlot_OCEAN            dbConvertAnyAngleTransformFromDbToMY
dbCreateBackgroundDef              dbCreateBackgroundDefByAttr        
dbCreateCompTypeSetDefByAttr       dbCreateInPlaceCoverObstruction    
dbCreateMultipleCurvedPolygons     dbCreateNamedSubNet                
dbCreateRailDefByAttr              dbCreateRowRegion                  
dbCreateRowRegionSpec              dbCreateRuler                      
dbDestroyInPlaceCoverObstruction   dbDetachPRBoundaryFromRowRegion    
dbFeaturePrintInfo                 dbFindRowRegion                    
dbFindRowRegionSpec                dbFlattenRowRegion                 
dbGet                              dbGetBackgroundDefAttr             

```

## 版图编辑

**117 个函数**

```
geAddHilightCurvedPath             geAddHilightCurvedPolygon          
geAddHilightSlicedCircle           geAddHilightSlicedDonut            
geClearIgnoreProp                  geClearNetNameDisplayFilter        
geClearProbeNetFilter              geDeselectFigs                     
geEnableNetNameDisplay             geGetNetNameDisplayFilter          
geGetProbeNetFilter                geIsNetNameDisplayActiveOnWindow   
geIsNetNameDisplayEnabled          geIsObjectPartiallySelected        
geNetNameDisplayOptionForm         geSaveNetNameDisplayFilter         
geSaveProbeNetFilter               geSelectBy2PointsLine              
geSetNetNameDisplayFilter          geSetProbeNetFilter                
geSwitchInContext                  geToggleDisplayResolution          
getAllLoadedFiles                  getApplicableMethods               
getAsciiWave_OCEAN                 getAsciiWave_ViVA_SKILL            
getCallingFunction                 getCompatContextVersion            
getCurSaveContextVersion           getData_OCEAN                      

```

## 波形查看

**152 个函数**

```
awvAddSubwindow_ViVA_SKILL         awvAnalog2Digital_ViVA_SKILL       
awvAppendExpression_ViVA_SKILL     awvAppendList_ViVA_SKILL           
awvAppendWaveform_ViVA_SKILL       awvClearPlotWindow_ViVA_SKILL      
awvClearSubwindowHistory_ViVA_SKILLawvClearWindowHistory_ViVA_SKILL   
awvCloseCalculator_ViVA_SKILL      awvCloseWindowMenuCB_ViVA_SKILL    
awvCloseWindow_ViVA_SKILL          awvCreateBusFromWaveList_ViVA_SKILL
awvCreateBus_OCEAN                 awvCreateBus_ViVA_SKILL            
awvCreatePlotWindow_ViVA_SKILL     awvDeleteAllWaveforms_ViVA_SKILL   
awvDeleteMarker_ViVA_SKILL         awvDeleteSubwindow_ViVA_SKILL      
awvDeleteWaveform_ViVA_SKILL       awvDigital2Analog_ViVA_SKILL       
awvDisableRedraw_ViVA_SKILL        awvDisplayDate_ViVA_SKILL          
awvDisplayGrid_ViVA_SKILL          awvDisplaySubwindowTitle_ViVA_SKILL
awvDisplayTitle_ViVA_SKILL         awvEraseWindowMenuCB_ViVA_SKILL    
awvEval_ViVA_SKILL                 awvExitWindowFunctionAdd_ViVA_SKILL
awvExitWindowFunctionDel_ViVA_SKILLawvExitWindowFunctionGet_ViVA_SKILL

```

## 仿真控制

**213 个函数**

```
ocnAmsSetOSSNetlister_OCEAN        ocnAmsSetUnlNetlister_OCEAN        
ocnCloseSession_OCEAN              ocnDisplay_OCEAN                   
ocnDspfFile_OCEAN                  ocnGenNoiseSummary_OCEAN           
ocnGetAdjustedPath_OCEAN           ocnGetInstancesModelName_OCEAN     
ocnHelp_OCEAN                      ocnPrint_OCEAN                     
ocnPspiceFile_OCEAN                ocnResetResults_OCEAN              
ocnSetAttrib_OCEAN                 ocnSetSilentMode_OCEAN             
ocnSetXLMode                       ocnSpefFile_OCEAN                  
ocnWriteLsspToFile_OCEAN           ocnYvsYplot_OCEAN                  
ocnxlAddOrUpdateOutput             ocnxlAddRelxSetup                  
ocnxlBeginTest                     ocnxlConjugateGradientOptions      
ocnxlCorner                        ocnxlCornerVars                    
ocnxlDeleteNote                    ocnxlDisableCorner                 
ocnxlDisableCornerForTest          ocnxlDisableRelxSetup              
ocnxlDisableSweepParam             ocnxlDisableSweepVar               

```

## 参数化单元

**240 个函数**

```
maeAddOutput                       maeClearAllTestJobPolicies         
maeClearExistingFaultsForRevalidationmaeCloseResults                    
maeCloseSession                    maeConvertAndCombineMultiADELToAssembler
maeCreateTest                      maeDeleteCorner                    
maeDeleteFaultGroup                maeDeleteOutput                    
maeDeleteParameter                 maeDeleteVar                       
maeEnableFaults                    maeExportOutputView                
maeExportSetupForExplorer          maeGetAnalysis                     
maeGetCurrentRunMode               maeGetCurrentRunPlanName           
maeGetEnabledAnalysis              maeGetEnabledRuns                  
maeGetEnvOption                    maeGetExplorerTestName             
maeGetGlobalFaultOptions           maeGetHistoryNameForCurrentRunInRunPlan
maeGetJobPolicy                    maeGetJobPolicyByName              
maeGetMTSBlock                     maeGetMTSMode                      
maeGetNBestDesignPoints            maeGetNumberOfExecutedRuns         

```

## 验证/检查

**130 个函数**

```
vdrCheckVoltageLabels              vdrCreateVSyncConstraintsFromFile  
vdrCreateVoltageLabel              vdrCreateVoltageLabelEx             $vvdrflow/appC.html
vdrCreateVoltageLabelOnNets        vdrCreateVoltageMarkers            
vdrCreateVoltageMarkersOnNets      vdrDeleteLabels                    
vdrGenerateLabelsGUI               vdrGenerateVSyncShapes             
vdrGetValidLayers                  vdrRunSanityChecker                
vdrRunVSyncSanityChecker           vdrSanityCheckerGUI                 $vvdrflow/appC.html
vdrSetNetVoltageRange              vdrSetValidLayers                  
vdrTransferVSyncConstraints        vdrVsyncVisualizerGUI              
verifAddImp                        verifAddImpSet                     
verifAddImpToImpSet                verifAddReq                        
verifCheckForChanges               verifCloseSession                  
verifCopyAndUpdateResultsFromUserDefinedDirectoryverifCreateBatchScript             
verifCreateRandomId                verifDeleteReqSignoff              
verifDisableDebug                  verifDownloadFromVManager          

```

## 技术文件

**34 个函数**

```
techCreateFingerDef                techCreateGenViaDef                
techCreateGenViaVariant            techCreateWaveguideDef             
techCreateWireProfile              techCreateWireProfileGroup         
techDeleteFingerDef                techDeleteRelatedSnapPatterns      
techDeleteWaveguideDef             techDeleteWidthSpacingPattern      
techDeleteWidthSpacingPatternGroup techDeleteWireProfile              
techDeleteWireProfileGroup         techExportWireProfileSet           
techFindWaveguideDefByLP           techFindWireProfile                
techFindWireProfileGroup           techGetCellViewSiteDefs            
techGetFabricType                  techGetLPProp                      
techGetLPProp                      techGetLayerAnalysisAttribute      
techGetTrimmedLayers               techGetWidthSpacingPatternAllowedRepeatMode
techGetWidthSpacingPatternDefaultRepeatModetechHasLayerAnalysisAttribute      
techHasWaveguideDefMinBendRadius    $sktechfile/chap9.htmltechImportWireProfileSet           
techSaveTechFile                   techSetFabricType                  

```

## 模块生成

**33 个函数**

```
mgAddShapeToTopo                   mgAddTopologyToModgen              
mgCreateMatchGroupInModgen         mgFGREnterHandEdit                 
mgFGRExitHandEdit                  mgFGRIsHandEdit                    
mgGetChannelTrunks                 mgGetIsLocalTrunk                  
mgGetModgenConstraintFromTopology  mgGetModgenFigGroupFromTopology    
mgGetStrapDirection                mgGetStrapHasDirection             
mgGetStrapHasOffset                mgGetStrapLongOffset1              
mgGetStrapLongOffset2              mgGetStrapOffset                   
mgGetTopoShapes                    mgGetTopoTrunkShapes               
mgGetTrunkChannel                  mgGetTrunkRefLPPEnclosure          
mgGetTrunkTopo                     mgIsTopologyInsideModgen           
mgModgenHasTopology                mgRegenerateModgen                 
mgRemoveTopologyFromModgen         mgSetIsLocalTrunk                  
mgSetRowRoutingChannelWidth        mgSetStrapDirection                
mgSetStrapHasDirection             mgSetStrapHasOffset                

```

