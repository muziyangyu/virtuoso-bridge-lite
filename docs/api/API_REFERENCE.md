# Cadence ICADVM20.1 SKILL API 补充文档

> **数据源**: `api_more_info.tgf`  
> **版本**: ICADVM20.1  
> **生成日期**: 2026-04-28  
> **总函数数**: 3856

---

## 目录

- [概述](#概述)
- [API 分类索引](#api-分类索引)
- [主要 API 分类详情](#主要-api-分类详情)
- [其他函数](#其他函数)
- [使用说明](#使用说明)

---

## 概述

本文档整理了 Cadence Virtuoso ICADVM20.1 版本中的 **3856 个补充 SKILL API 函数**。
这些函数涵盖了 ADE XL 仿真、约束管理、版图编辑、电路分析、电压域检查等各个功能领域。

### 主要功能分类

| 分类 | 前缀 | 说明 | 函数数 |
|------|------|------|--------|
| 约束/电路 | `ci*` | Constraint / Circuit Interface | 466 |
| ADE XL 仿真 | `axl*` | Analog Design Environment XL | 283 |
| GUI 界面 | `hi*` | Host Interface | 180 |
| 数据库操作 | `db*` | Database Functions | 165 |
| 波形显示 | `awv*` | Analog Waveform Viewer | 152 |
| Ocean XL | `ocnxl*` | Ocean Simulation XL | 132 |
| 参数化单元 | `pc*` | Parameterized Cell | 135 |
| 版图编辑 | `le*`, `ge*` | Layout / Graphics Editor | 26 + 44 |
| 版图验证 | `vdr*`, `vfo*` | Voltage Domain / Fill | 18 + 25 |

---

## API 分类索引

- [CI API](#ci-api) (466 个函数)
- [AXL API](#axl-api) (283 个函数)
- [HI API](#hi-api) (180 个函数)
- [DB API](#db-api) (165 个函数)
- [AWV API](#awv-api) (152 个函数)
- [PC API](#pc-api) (135 个函数)
- [OCNXL API](#ocnxl-api) (132 个函数)
- [HNL API](#hnl-api) (128 个函数)
- [MAE API](#mae-api) (105 个函数)
- [VERIF API](#verif-api) (87 个函数)
- [NL API](#nl-api) (68 个函数)
- [SIM API](#sim-api) (63 个函数)
- [ABS API](#abs-api) (61 个函数)
- [PAR API](#par-api) (50 个函数)
- [ROD API](#rod-api) (47 个函数)
- [VSA API](#vsa-api) (45 个函数)
- [GE API](#ge-api) (44 个函数)
- [GPE API](#gpe-api) (39 个函数)
- [AMS API](#ams-api) (38 个函数)
- [AEL API](#ael-api) (34 个函数)
- [TECH API](#tech-api) (34 个函数)
- [MG API](#mg-api) (33 个函数)
- [ILG API](#ilg-api) (32 个函数)
- [LX API](#lx-api) (32 个函数)
- [ISE API](#ise-api) (27 个函数)
- [WSP API](#wsp-api) (27 个函数)
- [SLA API](#sla-api) (27 个函数)
- [LE API](#le-api) (26 个函数)
- [VFO API](#vfo-api) (25 个函数)
- [LNT API](#lnt-api) (25 个函数)
- [ENV API](#env-api) (24 个函数)
- [IPC API](#ipc-api) (24 个函数)
- [MPT API](#mpt-api) (24 个函数)
- [ASI API](#asi-api) (21 个函数)
- [DD API](#dd-api) (20 个函数)
- [CST API](#cst-api) (19 个函数)
- [FNL API](#fnl-api) (18 个函数)
- [OCN API](#ocn-api) (18 个函数)
- [XOAS API](#xoas-api) (18 个函数)
- [VDR API](#vdr-api) (18 个函数)
- [PKX API](#pkx-api) (18 个函数)
- [CAL API](#cal-api) (16 个函数)
- [EDIFOUT API](#edifout-api) (15 个函数)
- [PHASE API](#phase-api) (14 个函数)
- [CC API](#cc-api) (14 个函数)
- [TE API](#te-api) (13 个函数)
- [EYE API](#eye-api) (13 个函数)
- [PHO API](#pho-api) (13 个函数)
- [PTE API](#pte-api) (13 个函数)
- [EAD API](#ead-api) (12 个函数)
- [VIA API](#via-api) (12 个函数)
- [SK API](#sk-api) (11 个函数)
- [CPF API](#cpf-api) (11 个函数)
- [SPD API](#spd-api) (11 个函数)
- [OPC API](#opc-api) (10 个函数)
- [SCH API](#sch-api) (9 个函数)
- [RELX API](#relx-api) (9 个函数)
- [VHMS API](#vhms-api) (8 个函数)
- [PO API](#po-api) (8 个函数)
- [PI API](#pi-api) (8 个函数)
- [RF API](#rf-api) (7 个函数)
- [CPH API](#cph-api) (7 个函数)
- [WE API](#we-api) (7 个函数)
- [DRD API](#drd-api) (7 个函数)
- [HDB API](#hdb-api) (7 个函数)
- [LOB API](#lob-api) (7 个函数)
- [VPM API](#vpm-api) (7 个函数)
- [VHDL API](#vhdl-api) (6 个函数)
- [AU API](#au-api) (6 个函数)
- [RDB API](#rdb-api) (6 个函数)
- [VRF API](#vrf-api) (6 个函数)
- [LCE API](#lce-api) (5 个函数)
- [TPA API](#tpa-api) (5 个函数)
- [其他函数](#其他函数) (721 个函数)

---

## 主要 API 分类详情

### CI API

**466 个函数**，文档位置：

- `constraintsSKILL/constskillFunctions.html` (440 个函数)
- `constraintsSKILL/designIntentSKILL.html` (12 个函数)
- `"ciRegisterCustomDeviceFilter"` (1 个函数)
- `"ciCommonGateAndSourceIterator"` (1 个函数)
- `"ciDeviceInfoRegisterTerminals"` (1 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `ciAPRCascodeIterator` | `constraintsSKILL/constskillFunctions.html` | `ciAPRCascodeIterator` |
| `ciAPRXYInstSymmetricIterator` | `constraintsSKILL/constskillFunctions.html` | `ciAPRXYInstSymmetricIterator` |
| `ciActiveSameCellAndSizeIterator` | `constraintsSKILL/constskillFunctions.html` | `ciActiveSameCellAndSizeIterator"   HTML` |
| `ciAddHierarchicalNotes` | `constraintsSKILL/constskillFunctions.html` | `ciAddHierarchicalNotes` |
| `ciAddLeadingSlash` | `constraintsSKILL/constskillFunctions.html` | `ciAddLeadingSlash` |
| `ciAddProcessRules` | `constraintsSKILL/constskillFunctions.html` | `ciAddProcessRules` |
| `ciAddRuleGroup` | `constraintsSKILL/constskillFunctions.html` | `ciAddRuleGroup` |
| `ciAddStructArg` | `constraintsSKILL/constskillFunctions.html` | `ciAddStructArg` |
| `ciAddTrailingSlash` | `constraintsSKILL/constskillFunctions.html` | `ciAddTrailingSlash` |
| `ciAlignPinsOnCellSide` | `constraintsSKILL/constskillFunctions.html` | `ciAlignPinsOnCellSide` |
| `ciAllCellViewsInHierarchy` | `constraintsSKILL/constskillFunctions.html` | `ciAllCellViewsInHierarchy` |
| `ciAxisCreate` | `constraintsSKILL/constskillFunctions.html` | `ciAxisCreate` |
| `ciAxisDelete` | `constraintsSKILL/constskillFunctions.html` | `ciAxisDelete` |
| `ciAxisExists` | `constraintsSKILL/constskillFunctions.html` | `ciAxisExists` |
| `ciAxisListCon` | `constraintsSKILL/constskillFunctions.html` | `ciAxisListCon` |
| `ciAxisListParams` | `constraintsSKILL/constskillFunctions.html` | `ciAxisListParams` |
| `ciAxisReplaceParams` | `constraintsSKILL/constskillFunctions.html` | `ciAxisReplaceParams` |
| `ciBasicGetParamValue` | `constraintsSKILL/constskillFunctions.html` | `ciBasicGetParamValue` |
| `ciBlockResistorArrayIterator` | `constraintsSKILL/constskillFunctions.html` | `ciBlockResistorArrayIterator` |
| `ciBuildModgenParams` | `constraintsSKILL/constskillFunctions.html` | `ciBuildModgenParams` |
| `ciBundleSignalsIterator` | `constraintsSKILL/constskillFunctions.html` | `ciBundleSignalsIterator` |
| `ciCPRegistrationFromLAM` | `constraintsSKILL/constskillFunctions.html` | `ciCPRegistrationFromLAM` |
| `ciCacheCallbackRegister` | `constraintsSKILL/constskillFunctions.html` | `ciCacheCallbackRegister` |
| `ciCacheCallbackUnregister` | `constraintsSKILL/constskillFunctions.html` | `ciCacheCallbackUnregister` |
| `ciCacheCallbackUpdate` | `constraintsSKILL/constskillFunctions.html` | `ciCacheCallbackUpdate` |
| `ciCacheCellName` | `constraintsSKILL/constskillFunctions.html` | `ciCacheCellName` |
| `ciCacheConstraintCellName` | `constraintsSKILL/constskillFunctions.html` | `ciCacheConstraintCellName` |
| `ciCacheConstraintLibName` | `constraintsSKILL/constskillFunctions.html` | `ciCacheConstraintLibName` |
| `ciCacheConstraintViewName` | `constraintsSKILL/constskillFunctions.html` | `ciCacheConstraintViewName` |
| `ciCacheDiscardEdits` | `constraintsSKILL/constskillFunctions.html` | `ciCacheDiscardEdits` |
| `ciCacheFind` | `constraintsSKILL/constskillFunctions.html` | `ciCacheFind` |
| `ciCacheGet` | `constraintsSKILL/constskillFunctions.html` | `ciCacheGet` |
| `ciCacheGetAllNetNames` | `constraintsSKILL/constskillFunctions.html` | `ciCacheGetAllNetNames` |
| `ciCacheGetCellView` | `constraintsSKILL/constskillFunctions.html` | `ciCacheGetCellView` |
| `ciCacheGetEnabledNotifications` | `constraintsSKILL/constskillFunctions.html` | `ciCacheGetEnabledNotifications` |
| `ciCacheIsLayout` | `constraintsSKILL/constskillFunctions.html` | `ciCacheIsLayout` |
| `ciCacheIsModified` | `constraintsSKILL/constskillFunctions.html` | `ciCacheIsModified` |
| `ciCacheIsWritable` | `constraintsSKILL/constskillFunctions.html` | `ciCacheIsWritable` |
| `ciCacheLCV` | `constraintsSKILL/constskillFunctions.html` | `ciCacheLCV` |
| `ciCacheLibName` | `constraintsSKILL/constskillFunctions.html` | `ciCacheLibName` |
| `ciCacheListAxesNames` | `constraintsSKILL/constskillFunctions.html` | `ciCacheListAxesNames` |
| `ciCacheListCon` | `constraintsSKILL/constskillFunctions.html` | `ciCacheListCon` |
| `ciCacheListConstrainedObjectNames` | `constraintsSKILL/constskillFunctions.html` | `ciCacheListConstrainedObjectNames` |
| `ciCacheListConstrainedObjects` | `constraintsSKILL/constskillFunctions.html` | `ciCacheListConstrainedObjects` |
| `ciCacheListTemplates` | `constraintsSKILL/constskillFunctions.html` | `ciCacheListTemplates` |
| `ciCacheListTypeNames` | `constraintsSKILL/constskillFunctions.html` | `ciCacheListTypeNames` |
| `ciCacheListTypes` | `constraintsSKILL/constskillFunctions.html` | `ciCacheListTypes` |
| `ciCacheMakeEditable` | `constraintsSKILL/constskillFunctions.html` | `ciCacheMakeEditable` |
| `ciCacheMakeReadOnly` | `constraintsSKILL/constskillFunctions.html` | `ciCacheMakeReadOnly` |
| `ciCacheNeedRefresh` | `constraintsSKILL/constskillFunctions.html` | `ciCacheNeedRefresh` |
| `ciCacheNotifications` | `constraintsSKILL/constskillFunctions.html` | `ciCacheNotifications` |
| `ciCachePurge` | `constraintsSKILL/constskillFunctions.html` | `ciCachePurge` |
| `ciCacheSave` | `constraintsSKILL/constskillFunctions.html` | `ciCacheSave` |
| `ciCacheTopCellName` | `constraintsSKILL/constskillFunctions.html` | `ciCacheTopCellName` |
| `ciCacheTopLibName` | `constraintsSKILL/constskillFunctions.html` | `ciCacheTopLibName` |
| `ciCacheTopViewName` | `constraintsSKILL/constskillFunctions.html` | `ciCacheTopViewName` |
| `ciCacheTransfer` | `constraintsSKILL/constskillFunctions.html      "ciCacheTransfer"` | `HTML` |
| `ciCacheTransferSelection` | `constraintsSKILL/constskillFunctions.html` | `ciCacheTransferSelection` |
| `ciCacheViewName` | `constraintsSKILL/constskillFunctions.html` | `ciCacheViewName` |
| `ciCachep` | `constraintsSKILL/constskillFunctions.html` | `ciCachep` |
| `ciCanCGBeUsed` | `constraintsSKILL/constskillFunctions.html` | `ciCanCGBeUsed` |
| `ciCategoryListFinderNames` | `constraintsSKILL/constskillFunctions.html` | `ciCategoryListFinderNames` |
| `ciCheckConstraints` | `constraintsSKILL/constskillFunctions.html` | `ciCheckConstraints` |
| `ciClearNetSuperTypes` | `constraintsSKILL/constskillFunctions.html` | `ciClearNetSuperTypes` |
| `ciClusterBoundaryForCluster` | `constraintsSKILL/constskillFunctions.html` | `ciClusterBoundaryForCluster` |
| `ciCollectDeviceInfo` | `constraintsSKILL/constskillFunctions.html` | `ciCollectDeviceInfo` |
| `ciCombineInstNetsPins` | `constraintsSKILL/constskillFunctions.html` | `ciCombineInstNetsPins` |
| `ciCommonGateAndSourceIterator   $constraintsSKILL/constskillFunctions.html` | `"ciCommonGateAndSourceIterator"` | `HTML` |
| `ciCommonGateIterator` | `constraintsSKILL/constskillFunctions.html` | `ciCommonGateIterator` |
| `ciCommonSourceIterator` | `constraintsSKILL/constskillFunctions.html` | `ciCommonSourceIterator` |
| `ciConAppendOneMember` | `constraintsSKILL/constskillFunctions.html` | `ciConAppendOneMember` |
| `ciConBaseName` | `constraintsSKILL/constskillFunctions.html` | `ciConBaseName` |
| `ciConBaseName` | `constraintsSKILL/constskillFunctions.html` | `ciConBaseName` |
| `ciConCallbackIsRegistered` | `constraintsSKILL/constskillFunctions.html` | `ciConCallbackIsRegistered` |
| `ciConCreate` | `constraintsSKILL/constskillFunctions.html` | `ciConCreate` |
| `ciConCreateExpanded` | `constraintsSKILL/constskillFunctions.html` | `ciConCreateExpanded` |
| `ciConDelete` | `constraintsSKILL/constskillFunctions.html` | `ciConDelete` |
| `ciConFind` | `constraintsSKILL/constskillFunctions.html` | `ciConFind` |
| `ciConGetAxisName` | `constraintsSKILL/constskillFunctions.html` | `ciConGetAxisName` |
| `ciConGetCache` | `constraintsSKILL/constskillFunctions.html` | `ciConGetCache` |
| `ciConGetComment` | `constraintsSKILL/constskillFunctions.html` | `ciConGetComment` |
| `ciConGetCreatedTime` | `constraintsSKILL/constskillFunctions.html` | `ciConGetCreatedTime` |
| `ciConGetMembersOfType` | `constraintsSKILL/constskillFunctions.html` | `ciConGetMembersOfType` |
| `ciConGetName` | `constraintsSKILL/constskillFunctions.html` | `ciConGetName` |
| `ciConGetNote` | `constraintsSKILL/constskillFunctions.html` | `ciConGetNote` |
| `ciConGetOwner` | `constraintsSKILL/constskillFunctions.html` | `ciConGetOwner` |
| `ciConGetPriority` | `constraintsSKILL/constskillFunctions.html` | `ciConGetPriority` |
| `ciConGetStatus` | `constraintsSKILL/constskillFunctions.html` | `ciConGetStatus` |
| `ciConGetType` | `constraintsSKILL/constskillFunctions.html` | `ciConGetType` |
| `ciConIsInContext` | `constraintsSKILL/constskillFunctions.html` | `ciConIsInContext` |
| `ciConIsOutOfContext` | `constraintsSKILL/constskillFunctions.html` | `ciConIsOutOfContext` |
| `ciConIsOverridden` | `constraintsSKILL/constskillFunctions.html` | `ciConIsOverridden` |
| `ciConIsWritable` | `constraintsSKILL/constskillFunctions.html` | `ciConIsWritable` |
| `ciConListMemberNames` | `constraintsSKILL/constskillFunctions.html` | `ciConListMemberNames` |
| `ciConListMembers` | `constraintsSKILL/constskillFunctions.html` | `ciConListMembers` |
| `ciConListParamNames` | `constraintsSKILL/constskillFunctions.html` | `ciConListParamNames` |
| `ciConListParams` | `constraintsSKILL/constskillFunctions.html` | `ciConListParams` |
| `ciConListRemoveMembers` | `constraintsSKILL/constskillFunctions.html` | `ciConListRemoveMembers` |
| `ciConListResetAllParams` | `constraintsSKILL/constskillFunctions.html` | `ciConListResetAllParams` |
| `ciConListResetParams` | `constraintsSKILL/constskillFunctions.html` | `ciConListResetParams` |
| `ciConListTemplates` | `constraintsSKILL/constskillFunctions.html` | `ciConListTemplates` |
| `ciConRegisterCallback` | `constraintsSKILL/constskillFunctions.html` | `ciConRegisterCallback` |
| `ciConRemoveMembers` | `constraintsSKILL/constskillFunctions.html` | `ciConRemoveMembers` |
| `ciConResetAllParams` | `constraintsSKILL/constskillFunctions.html` | `ciConResetAllParams` |
| `ciConResetParams` | `constraintsSKILL/constskillFunctions.html` | `ciConResetParams` |
| `ciConSetAxis` | `constraintsSKILL/constskillFunctions.html` | `ciConSetAxis` |
| `ciConSetNote` | `constraintsSKILL/constskillFunctions.html` | `ciConSetNote` |
| `ciConSetPriority` | `constraintsSKILL/constskillFunctions.html` | `ciConSetPriority` |
| `ciConSetStatus` | `constraintsSKILL/constskillFunctions.html` | `ciConSetStatus` |
| `ciConTypeHasNamedParameter` | `constraintsSKILL/constskillFunctions.html` | `ciConTypeHasNamedParameter` |
| `ciConUnregisterCallback` | `constraintsSKILL/constskillFunctions.html` | `ciConUnregisterCallback` |
| `ciConUpdateCallback` | `constraintsSKILL/constskillFunctions.html` | `ciConUpdateCallback` |
| `ciConUpdateMemberParams` | `constraintsSKILL/constskillFunctions.html` | `ciConUpdateMemberParams` |
| `ciConUpdateMembers` | `constraintsSKILL/constskillFunctions.html` | `ciConUpdateMembers` |
| `ciConUpdateParams` | `constraintsSKILL/constskillFunctions.html` | `ciConUpdateParams` |
| `ciConUprevCellBoundary` | `constraintsSKILL/constskillFunctions.html` | `ciConUprevCellBoundary` |
| `ciConVerify` | `constraintsSKILL/constskillFunctions.html` | `ciConVerify` |
| `ciConp` | `constraintsSKILL/constskillFunctions.html` | `ciConp` |
| `ciConstraintLCV` | `constraintsSKILL/constskillFunctions.html` | `ciConstraintLCV` |
| `ciConstraintViewLessp` | `constraintsSKILL/constskillFunctions.html` | `ciConstraintViewLessp` |
| `ciConstraintsForType` | `constraintsSKILL/constskillFunctions.html` | `ciConstraintsForType` |
| `ciConvertNestedNetClassToNetClassHierGroup` | `constraintsSKILL/constskillFunctions.html` | `ciConvertNestedNetClassToNetClassHierGroup` |
| `ciConvertParamsDPLToParams` | `constraintsSKILL/constskillFunctions.html` | `ciConvertParamsDPLToParams` |
| `ciConvertParamsToDPL` | `constraintsSKILL/constskillFunctions.html` | `ciConvertParamsToDPL` |
| `ciConvertToConArg` | `constraintsSKILL/constskillFunctions.html` | `ciConvertToConArg` |
| `ciCreateFilter` | `constraintsSKILL/constskillFunctions.html` | `ciCreateFilter` |
| `ciCreateGuardRing` | `constraintsSKILL/constskillFunctions.html` | `ciCreateGuardRing` |
| `ciCreateModgen` | `constraintsSKILL/constskillFunctions.html` | `ciCreateModgen` |
| `ciCreateModgenDummy` | `constraintsSKILL/constskillFunctions.html` | `ciCreateModgenDummy` |
| `ciCreateModgenForStructure` | `constraintsSKILL/constskillFunctions.html` | `ciCreateModgenForStructure` |
| `ciCreateRoutePriorityCon` | `constraintsSKILL/constskillFunctions.html` | `ciCreateRoutePriorityCon` |
| `ciCreateRoutingLayerEnumString` | `constraintsSKILL/constskillFunctions.html` | `ciCreateRoutingLayerEnumString` |
| `ciCurrentPathIterator` | `constraintsSKILL/constskillFunctions.html` | `ciCurrentPathIterator` |
| `ciDefaultParamToMatchFilter` | `constraintsSKILL/constskillFunctions.html` | `ciDefaultParamToMatchFilter` |
| `ciDeleteClusterMembersWithinModgens` | `constraintsSKILL/constskillFunctions.html` | `ciDeleteClusterMembersWithinModgens` |
| `ciDeleteGuardRing` | `constraintsSKILL/constskillFunctions.html` | `ciDeleteGuardRing` |
| `ciDeleteModgenTopologies` | `constraintsSKILL/constskillFunctions.html` | `ciDeleteModgenTopologies` |
| `ciDeleteRuleGroup` | `constraintsSKILL/constskillFunctions.html` | `ciDeleteRuleGroup` |
| `ciDeleteStructArg` | `constraintsSKILL/constskillFunctions.html` | `ciDeleteStructArg` |
| `ciDeleteSymmetriesWithinModgens` | `constraintsSKILL/constskillFunctions.html` | `ciDeleteSymmetriesWithinModgens` |
| `ciDeleteUnreferencedObjects` | `constraintsSKILL/constskillFunctions.html` | `ciDeleteUnreferencedObjects` |
| `ciDesignLCV` | `constraintsSKILL/constskillFunctions.html` | `ciDesignLCV` |
| `ciDevGroupBoxIterator` | `constraintsSKILL/designIntentSKILL.html` | `ciDevGroupBoxIterator` |
| `ciDeviceInfoGetRegisteredParams` | `constraintsSKILL/constskillFunctions.html` | `ciDeviceInfoGetRegisteredParams` |
| `ciDeviceInfoGetRegisteredTerminals` | `constraintsSKILL/constskillFunctions.html` | `ciDeviceInfoGetRegisteredTerminals` |
| `ciDeviceInfoRegisterParams` | `constraintsSKILL/constskillFunctions.html` | `ciDeviceInfoRegisterParams` |
| `ciDeviceInfoRegisterTerminals   $constraintsSKILL/constskillFunctions.html` | `"ciDeviceInfoRegisterTerminals"` | `HTML` |
| `ciDeviceInfoRegistry` | `constraintsSKILL/constskillFunctions.html` | `ciDeviceInfoRegistry` |
| `ciDeviceInfoRestoreDefaultParamNames` | `constraintsSKILL/constskillFunctions.html` | `ciDeviceInfoRestoreDefaultParamNames` |
| `ciDeviceInfoRestoreDefaultTerminalNames` | `constraintsSKILL/constskillFunctions.html` | `ciDeviceInfoRestoreDefaultTerminalNames` |
| `ciDeviceInfoTerminalsAreValid   $constraintsSKILL/constskillFunctions.html` | `"ciDeviceInfoTerminalsAreValid"` | `HTML` |
| `ciDiMinMaxVPropertyCallback` | `constraintsSKILL/designIntentSKILL.html` | `ciDiMinMaxVPropertyCallback` |
| `ciDiReportGenReport` | `constraintsSKILL/designIntentSKILL.html` | `ciDiReportGenReport` |
| `ciEnableAssistant` | `constraintsSKILL/constskillFunctions.html` | `ciEnableAssistant` |
| `ciEnableAutoConstraintNotes` | `constraintsSKILL/constskillFunctions.html` | `ciEnableAutoConstraintNotes` |
| `ciEvaluateGeneratorArgs` | `constraintsSKILL/constskillFunctions.html` | `ciEvaluateGeneratorArgs` |
| `ciExpandAndRepeatName` | `constraintsSKILL/constskillFunctions.html` | `ciExpandAndRepeatName` |
| `ciExpandIteratedDeviceInfo` | `constraintsSKILL/constskillFunctions.html` | `ciExpandIteratedDeviceInfo` |
| `ciExpandMembers` | `constraintsSKILL/constskillFunctions.html` | `ciExpandMembers` |
| `ciExpandName` | `constraintsSKILL/constskillFunctions.html` | `ciExpandName` |
| `ciExtractRowNumber` | `constraintsSKILL/constskillFunctions.html` | `ciExtractRowNumber` |
| `ciFindDeviceArraysForDev` | `constraintsSKILL/constskillFunctions.html` | `ciFindDeviceArraysForDev` |
| `ciFindObjectInHier` | `constraintsSKILL/constskillFunctions.html` | `ciFindObjectInHier` |
| `ciFindOpenCellView` | `constraintsSKILL/constskillFunctions.html` | `ciFindOpenCellView` |
| `ciFindOpenCellViews` | `constraintsSKILL/constskillFunctions.html` | `ciFindOpenCellViews` |
| `ciGUIArgsToConArgs` | `constraintsSKILL/constskillFunctions.html` | `ciGUIArgsToConArgs` |
| `ciGenerateArrayChannelDesc` | `constraintsSKILL/constskillFunctions.html` | `ciGenerateArrayChannelDesc` |
| `ciGenerateBestFitPattern` | `constraintsSKILL/constskillFunctions.html` | `ciGenerateBestFitPattern` |
| `ciGenerateCascodedCurrentMirrorChannelDesc` | `constraintsSKILL/constskillFunctions.html` | `ciGenerateCascodedCurrentMirrorChannelDesc` |
| `ciGenerateCascodedCurrentMirrorPattern` | `constraintsSKILL/constskillFunctions.html` | `ciGenerateCascodedCurrentMirrorPattern` |
| `ciGenerateConstraintGroup` | `constraintsSKILL/constskillFunctions.html` | `ciGenerateConstraintGroup` |
| `ciGenerateCurrentMirrorChannelDesc` | `constraintsSKILL/constskillFunctions.html` | `ciGenerateCurrentMirrorChannelDesc` |
| `ciGenerateCurrentMirrorPattern` | `constraintsSKILL/constskillFunctions.html` | `ciGenerateCurrentMirrorPattern` |
| `ciGenerateDiffPairChannelDesc` | `constraintsSKILL/constskillFunctions.html` | `ciGenerateDiffPairChannelDesc` |
| `ciGenerateDiffPairPattern` | `constraintsSKILL/constskillFunctions.html` | `ciGenerateDiffPairPattern` |
| `ciGenerateLargeMfactorPattern   $constraintsSKILL/constskillFunctions.html` | `"ciGenerateLargeMfactorPattern"` | `HTML` |
| `ciGeneratorCheckInstsNetsPinsInstTerms` | `constraintsSKILL/constskillFunctions.html` | `ciGeneratorCheckInstsNetsPinsInstTerms` |
| `ciGeneratorForInstSymmetry` | `constraintsSKILL/constskillFunctions.html` | `ciGeneratorForInstSymmetry` |
| `ciGeneratorForNetSymmetry` | `constraintsSKILL/constskillFunctions.html` | `ciGeneratorForNetSymmetry` |
| `ciGetAction` | `constraintsSKILL/constskillFunctions.html` | `ciGetAction` |
| `ciGetCPSelectedResults` | `constraintsSKILL/constskillFunctions.html` | `ciGetCPSelectedResults` |
| `ciGetCellTermDefaultNetName` | `constraintsSKILL/constskillFunctions.html` | `ciGetCellTermDefaultNetName` |
| `ciGetCellView` | `constraintsSKILL/constskillFunctions.html` | `ciGetCellView` |
| `ciGetCellViewForObjectPath` | `constraintsSKILL/constskillFunctions.html` | `ciGetCellViewForObjectPath` |
| `ciGetConnectedInsts` | `constraintsSKILL/constskillFunctions.html` | `ciGetConnectedInsts` |
| `ciGetConstraintGroupsEnum` | `constraintsSKILL/constskillFunctions.html` | `ciGetConstraintGroupsEnum` |
| `ciGetCustomFilterNames` | `constraintsSKILL/constskillFunctions.html` | `ciGetCustomFilterNames` |
| `ciGetDefaultNetName` | `constraintsSKILL/constskillFunctions.html` | `ciGetDefaultNetName` |
| `ciGetDeviceBulkTermName` | `constraintsSKILL/constskillFunctions.html` | `ciGetDeviceBulkTermName` |
| `ciGetDeviceInfo` | `constraintsSKILL/constskillFunctions.html` | `ciGetDeviceInfo` |
| `ciGetDeviceNames` | `constraintsSKILL/constskillFunctions.html` | `ciGetDeviceNames` |
| `ciGetDeviceTermName` | `constraintsSKILL/constskillFunctions.html` | `ciGetDeviceTermName` |
| `ciGetFinder` | `constraintsSKILL/constskillFunctions.html` | `ciGetFinder` |
| `ciGetFirstDeviceTermName` | `constraintsSKILL/constskillFunctions.html` | `ciGetFirstDeviceTermName` |
| `ciGetFluidGuardRingDeviceEnum   $constraintsSKILL/constskillFunctions.html` | `"ciGetFluidGuardRingDeviceEnum"` | `HTML` |
| `ciGetFoundryRules` | `constraintsSKILL/constskillFunctions.html` | `ciGetFoundryRules` |
| `ciGetGenerator` | `constraintsSKILL/constskillFunctions.html` | `ciGetGenerator` |
| `ciGetGuardRing` | `constraintsSKILL/constskillFunctions.html` | `ciGetGuardRing` |
| `ciGetGuardRingMPPName` | `constraintsSKILL/constskillFunctions.html` | `ciGetGuardRingMPPName` |
| `ciGetIterator` | `constraintsSKILL/constskillFunctions.html` | `ciGetIterator` |
| `ciGetLAMComponentTypes` | `constraintsSKILL/constskillFunctions.html` | `ciGetLAMComponentTypes` |
| `ciGetMappedDeviceNames` | `constraintsSKILL/constskillFunctions.html` | `ciGetMappedDeviceNames` |
| `ciGetMatchParam2DList` | `constraintsSKILL/constskillFunctions.html` | `ciGetMatchParam2DList` |
| `ciGetMembersOfType` | `constraintsSKILL/constskillFunctions.html` | `ciGetMembersOfType` |
| `ciGetNetNames` | `constraintsSKILL/constskillFunctions.html` | `ciGetNetNames` |
| `ciGetNetSubTypes` | `constraintsSKILL/constskillFunctions.html` | `ciGetNetSubTypes` |
| `ciGetNetSuperTypes` | `constraintsSKILL/constskillFunctions.html` | `ciGetNetSuperTypes` |
| `ciGetObjectCellView` | `constraintsSKILL/constskillFunctions.html` | `ciGetObjectCellView` |
| `ciGetOpenCellViews` | `constraintsSKILL/constskillFunctions.html` | `ciGetOpenCellViews` |
| `ciGetParamMapping` | `constraintsSKILL/constskillFunctions.html` | `ciGetParamMapping` |
| `ciGetParamName` | `constraintsSKILL/constskillFunctions.html` | `ciGetParamName` |
| `ciGetParamValFromParameters` | `constraintsSKILL/constskillFunctions.html` | `ciGetParamValFromParameters` |
| `ciGetParamValue` | `constraintsSKILL/constskillFunctions.html` | `ciGetParamValue` |
| `ciGetParamValueOrDefault` | `constraintsSKILL/constskillFunctions.html` | `ciGetParamValueOrDefault` |
| `ciGetParamValues` | `constraintsSKILL/constskillFunctions.html` | `ciGetParamValues` |
| `ciGetRoutingLayer` | `constraintsSKILL/constskillFunctions.html` | `ciGetRoutingLayer` |
| `ciGetRoutingLayers` | `constraintsSKILL/constskillFunctions.html` | `ciGetRoutingLayers` |
| `ciGetRule` | `constraintsSKILL/constskillFunctions.html` | `ciGetRule` |
| `ciGetRuleGroupByName` | `constraintsSKILL/constskillFunctions.html` | `ciGetRuleGroupByName` |
| `ciGetRuleGroupName` | `constraintsSKILL/constskillFunctions.html` | `ciGetRuleGroupName` |
| `ciGetRuleGroups` | `constraintsSKILL/constskillFunctions.html` | `ciGetRuleGroups` |
| `ciGetStructArg` | `constraintsSKILL/constskillFunctions.html` | `ciGetStructArg` |
| `ciGetStructArgs` | `constraintsSKILL/constskillFunctions.html` | `ciGetStructArgs` |
| `ciGetStructGeneratorExpressions` | `constraintsSKILL/constskillFunctions.html` | `ciGetStructGeneratorExpressions` |
| `ciGetStructPDKMult` | `constraintsSKILL/constskillFunctions.html` | `ciGetStructPDKMult` |
| `ciGetStructure` | `constraintsSKILL/constskillFunctions.html` | `ciGetStructure` |
| `ciGetTechFile` | `constraintsSKILL/constskillFunctions.html` | `ciGetTechFile` |
| `ciGetTechMPPNames` | `constraintsSKILL/constskillFunctions.html` | `ciGetTechMPPNames` |
| `ciGetTermNames` | `constraintsSKILL/constskillFunctions.html` | `ciGetTermNames` |
| `ciGetWidgetProperties` | `constraintsSKILL/constskillFunctions.html` | `ciGetWidgetProperties` |
| `ciGuardRingForCluster` | `constraintsSKILL/constskillFunctions.html` | `ciGuardRingForCluster` |
| `ciGuardRingForModgen` | `constraintsSKILL/constskillFunctions.html` | `ciGuardRingForModgen` |
| `ciHasCellAnyRegTerm` | `constraintsSKILL/constskillFunctions.html` | `ciHasCellAnyRegTerm` |
| `ciHaveSameBulkNets` | `constraintsSKILL/constskillFunctions.html` | `ciHaveSameBulkNets` |
| `ciHaveSameParamValues` | `constraintsSKILL/constskillFunctions.html` | `ciHaveSameParamValues` |
| `ciHierCompareConstraint` | `constraintsSKILL/constskillFunctions.html` | `ciHierCompareConstraint` |
| `ciHierCompareConstraints` | `constraintsSKILL/constskillFunctions.html` | `ciHierCompareConstraints` |
| `ciHierUpdateConstraints` | `constraintsSKILL/constskillFunctions.html` | `ciHierUpdateConstraints` |
| `ciHierarchicalSeriesIterator` | `constraintsSKILL/constskillFunctions.html` | `ciHierarchicalSeriesIterator` |
| `ciHighestLevelNet` | `constraintsSKILL/constskillFunctions.html` | `ciHighestLevelNet` |
| `ciIgnoreDevice` | `constraintsSKILL/constskillFunctions.html` | `ciIgnoreDevice` |
| `ciInstGetSplitFingers` | `constraintsSKILL/constskillFunctions.html` | `ciInstGetSplitFingers` |
| `ciInstIterator` | `constraintsSKILL/constskillFunctions.html` | `ciInstIterator` |
| `ciInstListSplitFingers` | `constraintsSKILL/constskillFunctions.html` | `ciInstListSplitFingers` |
| `ciInstSetSplitFingers` | `constraintsSKILL/constskillFunctions.html` | `ciInstSetSplitFingers` |
| `ciInstTermIterator` | `constraintsSKILL/constskillFunctions.html` | `ciInstTermIterator` |
| `ciInstsNetsPinsFromSelSet` | `constraintsSKILL/constskillFunctions.html` | `ciInstsNetsPinsFromSelSet` |
| `ciIsDevice` | `constraintsSKILL/constskillFunctions.html` | `ciIsDevice` |
| `ciIsNet` | `constraintsSKILL/constskillFunctions.html` | `ciIsNet` |
| `ciIsNetSuperType` | `constraintsSKILL/constskillFunctions.html` | `ciIsNetSuperType` |
| `ciListAllCategoryNames` | `constraintsSKILL/constskillFunctions.html` | `ciListAllCategoryNames` |
| `ciListAllFinderNames` | `constraintsSKILL/constskillFunctions.html` | `ciListAllFinderNames` |
| `ciListAllGeneratorNames` | `constraintsSKILL/constskillFunctions.html` | `ciListAllGeneratorNames` |
| `ciListAllIteratorNames` | `constraintsSKILL/constskillFunctions.html` | `ciListAllIteratorNames` |
| `ciListAllStructureNames` | `constraintsSKILL/constskillFunctions.html` | `ciListAllStructureNames` |
| `ciListEditors` | `constraintsSKILL/constskillFunctions.html` | `ciListEditors` |
| `ciListGeneratableConstraintGroups` | `constraintsSKILL/constskillFunctions.html` | `ciListGeneratableConstraintGroups` |
| `ciListProcessRules` | `constraintsSKILL/constskillFunctions.html` | `ciListProcessRules` |
| `ciListStructGeneratorExpressions` | `constraintsSKILL/constskillFunctions.html` | `ciListStructGeneratorExpressions` |
| `ciListStructPDKMults` | `constraintsSKILL/constskillFunctions.html` | `ciListStructPDKMults` |
| `ciListStructTypes` | `constraintsSKILL/constskillFunctions.html` | `ciListStructTypes` |
| `ciListTemplateTypes` | `constraintsSKILL/constskillFunctions.html` | `ciListTemplateTypes` |
| `ciListTypes` | `constraintsSKILL/constskillFunctions.html` | `ciListTypes` |
| `ciLoadConfigXML` | `constraintsSKILL/constskillFunctions.html` | `ciLoadConfigXML` |
| `ciLoadConfigXMLFromString` | `constraintsSKILL/constskillFunctions.html` | `ciLoadConfigXMLFromString` |
| `ciLoadConstrFrom` | `constraintsSKILL/constskillFunctions.html` | `ciLoadConstrFrom` |
| `ciLoadDotCadenceFiles` | `constraintsSKILL/constskillFunctions.html` | `ciLoadDotCadenceFiles` |
| `ciLoadIcon` | `constraintsSKILL/constskillFunctions.html` | `ciLoadIcon` |
| `ciLoadIcons` | `constraintsSKILL/constskillFunctions.html` | `ciLoadIcons` |
| `ciLxComparisonReport` | `constraintsSKILL/constskillFunctions.html` | `ciLxComparisonReport` |
| `ciMOSActiveLoadStructIterator` | `constraintsSKILL/constskillFunctions.html` | `ciMOSActiveLoadStructIterator` |
| `ciMOSCascodeIterator` | `constraintsSKILL/constskillFunctions.html` | `ciMOSCascodeIterator` |
| `ciMOSCascodedCurrentMirrorStructIterator` | `constraintsSKILL/constskillFunctions.html` | `ciMOSCascodedCurrentMirrorStructIterator` |
| `ciMOSCascodedCurrentMirrorStructIterator2` | `constraintsSKILL/constskillFunctions.html` | `ciMOSCascodedCurrentMirrorStructIterator2` |
| `ciMOSCommonGateStructIterator` | `constraintsSKILL/constskillFunctions.html` | `ciMOSCommonGateStructIterator` |
| `ciMOSCrossCoupledDifferentialPairStructIterator` | `constraintsSKILL/constskillFunctions.html` | `ciMOSCrossCoupledDifferentialPairStructIterator` |
| `ciMOSCrossCoupledQuadStructIterator` | `constraintsSKILL/constskillFunctions.html` | `ciMOSCrossCoupledQuadStructIterator` |
| `ciMOSCurrentMirrorStructIterator` | `constraintsSKILL/constskillFunctions.html` | `ciMOSCurrentMirrorStructIterator` |
| `ciMOSDifferentialPairStructIterator` | `constraintsSKILL/constskillFunctions.html` | `ciMOSDifferentialPairStructIterator` |
| `ciMOSInverterStructIterator` | `constraintsSKILL/constskillFunctions.html` | `ciMOSInverterStructIterator` |
| `ciMOSParallelStructIterator` | `constraintsSKILL/constskillFunctions.html` | `ciMOSParallelStructIterator` |
| `ciMOSTransmissionGateStructIterator` | `constraintsSKILL/constskillFunctions.html` | `ciMOSTransmissionGateStructIterator` |
| `ciMakeHierContext` | `constraintsSKILL/constskillFunctions.html` | `ciMakeHierContext` |
| `ciMakeObjectInfo` | `constraintsSKILL/constskillFunctions.html` | `ciMakeObjectInfo` |
| `ciMapParam` | `constraintsSKILL/constskillFunctions.html` | `ciMapParam` |
| `ciMapTerm` | `constraintsSKILL/constskillFunctions.html` | `ciMapTerm` |
| `ciMatchedFingerWidth` | `constraintsSKILL/constskillFunctions.html` | `ciMatchedFingerWidth` |
| `ciMatchedParametersForCurrent_Mirror    $constraintsSKILL/constskillFunctions.html` | `"ciMatchedParametersForCurrent_Mirror"` | `HTML` |
| `ciMatchedParamsForInstanceSymmetry` | `constraintsSKILL/constskillFunctions.html` | `ciMatchedParamsForInstanceSymmetry` |
| `ciMatchedParamsForSameSizeInstances` | `constraintsSKILL/constskillFunctions.html` | `ciMatchedParamsForSameSizeInstances` |
| `ciMemberIndexToModgenPatternSymbol` | `constraintsSKILL/constskillFunctions.html` | `ciMemberIndexToModgenPatternSymbol` |
| `ciMergeParams` | `constraintsSKILL/constskillFunctions.html` | `ciMergeParams` |
| `ciModgenDummyNetName` | `constraintsSKILL/constskillFunctions.html` | `ciModgenDummyNetName` |
| `ciModgenForSameCellSizeAndBulk` | `constraintsSKILL/constskillFunctions.html` | `ciModgenForSameCellSizeAndBulk` |
| `ciModgenListFingerSplitCons` | `constraintsSKILL/constskillFunctions.html` | `ciModgenListFingerSplitCons` |
| `ciModgenMergeLayersFromArgs` | `constraintsSKILL/constskillFunctions.html` | `ciModgenMergeLayersFromArgs` |
| `ciModgenRefreshStorage` | `constraintsSKILL/constskillFunctions.html` | `ciModgenRefreshStorage` |
| `ciModgenSplitFingers` | `constraintsSKILL/constskillFunctions.html` | `ciModgenSplitFingers` |
| `ciModgenTemplateFingerSplitPreDestroy` | `constraintsSKILL/constskillFunctions.html` | `ciModgenTemplateFingerSplitPreDestroy` |
| `ciNetIterator` | `constraintsSKILL/constskillFunctions.html` | `ciNetIterator` |
| `ciNetNames` | `constraintsSKILL/constskillFunctions.html` | `ciNetNames` |
| `ciNetOnTerm` | `constraintsSKILL/constskillFunctions.html` | `ciNetOnTerm` |
| `ciNetPredicates` | `constraintsSKILL/constskillFunctions.html` | `ciNetPredicates` |
| `ciNetRegexs` | `constraintsSKILL/constskillFunctions.html` | `ciNetRegexs` |
| `ciNextConName` | `constraintsSKILL/constskillFunctions.html` | `ciNextConName` |
| `ciNextObjName` | `constraintsSKILL/constskillFunctions.html` | `ciNextObjName` |
| `ciNextTemplateName` | `constraintsSKILL/constskillFunctions.html` | `ciNextTemplateName` |
| `ciNumDevices` | `constraintsSKILL/constskillFunctions.html` | `ciNumDevices` |
| `ciNumTermsEQ2` | `constraintsSKILL/constskillFunctions.html` | `ciNumTermsEQ2` |
| `ciObjectIsInContext` | `constraintsSKILL/constskillFunctions.html` | `ciObjectIsInContext` |
| `ciObjectListCon` | `constraintsSKILL/constskillFunctions.html` | `ciObjectListCon` |
| `ciObjectPathAndName` | `constraintsSKILL/constskillFunctions.html` | `ciObjectPathAndName` |
| `ciOpenCellView` | `constraintsSKILL/constskillFunctions.html` | `ciOpenCellView` |
| `ciOpenPanicCellView` | `constraintsSKILL/constskillFunctions.html` | `ciOpenPanicCellView` |
| `ciOrientationForModgen` | `constraintsSKILL/constskillFunctions.html` | `ciOrientationForModgen` |
| `ciPadModgenPattern` | `constraintsSKILL/constskillFunctions.html` | `ciPadModgenPattern` |
| `ciParallelNetResistorArrayIterator` | `constraintsSKILL/constskillFunctions.html` | `ciParallelNetResistorArrayIterator` |
| `ciParallelResistorArrayIterator` | `constraintsSKILL/constskillFunctions.html` | `ciParallelResistorArrayIterator` |
| `ciPinIterator` | `constraintsSKILL/constskillFunctions.html` | `ciPinIterator` |
| `ciPlacerControlledWellGeneration` | `constraintsSKILL/constskillFunctions.html` | `ciPlacerControlledWellGeneration` |
| `ciPrintMappedDefaultNetNames    $constraintsSKILL/constskillFunctions.html` | `"ciPrintMappedDefaultNetNames"` | `HTML` |
| `ciPrintMappedDeviceNames` | `constraintsSKILL/constskillFunctions.html` | `ciPrintMappedDeviceNames` |
| `ciPrintMappedNetNames` | `constraintsSKILL/constskillFunctions.html` | `ciPrintMappedNetNames` |
| `ciPrintMappedParams` | `constraintsSKILL/constskillFunctions.html` | `ciPrintMappedParams` |
| `ciPrintMappedTerminals` | `constraintsSKILL/constskillFunctions.html` | `ciPrintMappedTerminals` |
| `ciPrintReport` | `constraintsSKILL/constskillFunctions.html` | `ciPrintReport` |
| `ciPullConstraint` | `constraintsSKILL/constskillFunctions.html` | `ciPullConstraint` |
| `ciPullConstraints` | `constraintsSKILL/constskillFunctions.html` | `ciPullConstraints` |
| `ciPushConstraint` | `constraintsSKILL/constskillFunctions.html` | `ciPushConstraint` |
| `ciPushConstraints` | `constraintsSKILL/constskillFunctions.html` | `ciPushConstraints` |
| `ciRefreshCellView` | `constraintsSKILL/constskillFunctions.html` | `ciRefreshCellView` |
| `ciRegTypeBindingParameter` | `constraintsSKILL/constskillFunctions.html` | `ciRegTypeBindingParameter` |
| `ciRegexReplaceStructArgs` | `constraintsSKILL/constskillFunctions.html` | `ciRegexReplaceStructArgs` |
| `ciRegisterAction` | `constraintsSKILL/constskillFunctions.html` | `ciRegisterAction` |
| `ciRegisterAssistant` | `constraintsSKILL/constskillFunctions.html` | `ciRegisterAssistant` |
| `ciRegisterConstraintEditor` | `constraintsSKILL/constskillFunctions.html` | `ciRegisterConstraintEditor` |
| `ciRegisterConstraintGenerator` | `constraintsSKILL/constskillFunctions.html` | `ciRegisterConstraintGenerator` |
| `ciRegisterCustomDeviceFilter    $constraintsSKILL/constskillFunctions.html` | `"ciRegisterCustomDeviceFilter"` | `HTML` |
| `ciRegisterDefaultNetName` | `constraintsSKILL/constskillFunctions.html` | `ciRegisterDefaultNetName` |
| `ciRegisterDevice` | `constraintsSKILL/constskillFunctions.html` | `ciRegisterDevice` |
| `ciRegisterDevicesForPDKCategory` | `constraintsSKILL/constskillFunctions.html` | `ciRegisterDevicesForPDKCategory` |
| `ciRegisterDynamicParamDef` | `constraintsSKILL/constskillFunctions.html` | `ciRegisterDynamicParamDef` |
| `ciRegisterFinder` | `constraintsSKILL/constskillFunctions.html` | `ciRegisterFinder` |
| `ciRegisterIterator` | `constraintsSKILL/constskillFunctions.html` | `ciRegisterIterator` |
| `ciRegisterNet` | `constraintsSKILL/constskillFunctions.html` | `ciRegisterNet` |
| `ciRegisterNetNames` | `constraintsSKILL/constskillFunctions.html` | `ciRegisterNetNames` |
| `ciRegisterNetPredicate` | `constraintsSKILL/constskillFunctions.html` | `ciRegisterNetPredicate` |
| `ciRegisterNetRegexs` | `constraintsSKILL/constskillFunctions.html` | `ciRegisterNetRegexs` |
| `ciRegisterNetSuperType` | `constraintsSKILL/constskillFunctions.html` | `ciRegisterNetSuperType` |
| `ciRegisterStructure` | `constraintsSKILL/constskillFunctions.html` | `ciRegisterStructure` |
| `ciReinitStructTemplateDefs` | `constraintsSKILL/constskillFunctions.html` | `ciReinitStructTemplateDefs` |
| `ciRemoveConstrainedPinNetsFromRails` | `constraintsSKILL/constskillFunctions.html` | `ciRemoveConstrainedPinNetsFromRails` |
| `ciRemoveHierarchicalNotes` | `constraintsSKILL/constskillFunctions.html` | `ciRemoveHierarchicalNotes` |
| `ciRemoveLeadingSlash` | `constraintsSKILL/constskillFunctions.html` | `ciRemoveLeadingSlash` |
| `ciRemoveProcessRules` | `constraintsSKILL/constskillFunctions.html` | `ciRemoveProcessRules` |
| `ciRemoveSymmetricPinAlignments` | `constraintsSKILL/constskillFunctions.html` | `ciRemoveSymmetricPinAlignments` |
| `ciRemoveTrailingSlash` | `constraintsSKILL/constskillFunctions.html` | `ciRemoveTrailingSlash` |
| `ciReopenCellView` | `constraintsSKILL/constskillFunctions.html` | `ciReopenCellView` |
| `ciReorderAssistants` | `constraintsSKILL/constskillFunctions.html` | `ciReorderAssistants` |
| `ciReplaceStructArg` | `constraintsSKILL/constskillFunctions.html` | `ciReplaceStructArg` |
| `ciResistorArrayUpdateRowColVal` | `constraintsSKILL/constskillFunctions.html` | `ciResistorArrayUpdateRowColVal` |
| `ciResolveBulkNet` | `constraintsSKILL/constskillFunctions.html` | `ciResolveBulkNet` |
| `ciResolveNet` | `constraintsSKILL/constskillFunctions.html` | `ciResolveNet` |
| `ciRunFinder` | `constraintsSKILL/constskillFunctions.html` | `ciRunFinder` |
| `ciRunFindersAndGenerators` | `constraintsSKILL/constskillFunctions.html` | `ciRunFindersAndGenerators` |
| `ciRunGenerator` | `constraintsSKILL/constskillFunctions.html` | `ciRunGenerator` |
| `ciRunMatchingConstraintsGenerator` | `constraintsSKILL/constskillFunctions.html` | `ciRunMatchingConstraintsGenerator` |
| `ciRunPrecondition` | `constraintsSKILL/constskillFunctions.html` | `ciRunPrecondition` |
| `ciSameCellIterator` | `constraintsSKILL/constskillFunctions.html` | `ciSameCellIterator` |
| `ciSaveConstraintGenerator` | `constraintsSKILL/constskillFunctions.html` | `ciSaveConstraintGenerator` |
| `ciSelectedConstraints` | `constraintsSKILL/constskillFunctions.html` | `ciSelectedConstraints` |
| `ciSelectedTemplates` | `constraintsSKILL/constskillFunctions.html` | `ciSelectedTemplates` |
| `ciSeparateInstsNetsPins` | `constraintsSKILL/constskillFunctions.html` | `ciSeparateInstsNetsPins` |
| `ciSeriesResistorArrayIterator` | `constraintsSKILL/constskillFunctions.html` | `ciSeriesResistorArrayIterator` |
| `ciSetCMCGSKILLCallbacks` | `constraintsSKILL/constskillFunctions.html` | `ciSetCMCGSKILLCallbacks` |
| `ciSetDefaultConstraintEditor    $constraintsSKILL/constskillFunctions.html` | `"ciSetDefaultConstraintEditor"` | `HTML` |
| `ciSetHaloOptions` | `constraintsSKILL/constskillFunctions.html` | `ciSetHaloOptions` |
| `ciSetHaloPolicy` | `constraintsSKILL/constskillFunctions.html` | `ciSetHaloPolicy` |
| `ciSetMaxHaloGroupSize` | `constraintsSKILL/constskillFunctions.html` | `ciSetMaxHaloGroupSize` |
| `ciSetModgenTopology` | `constraintsSKILL/constskillFunctions.html` | `ciSetModgenTopology` |
| `ciSetStructArgVal` | `constraintsSKILL/constskillFunctions.html` | `ciSetStructArgVal` |
| `ciSetStructArgs` | `constraintsSKILL/constskillFunctions.html` | `ciSetStructArgs` |
| `ciSetStructGeneratorExpressions` | `constraintsSKILL/constskillFunctions.html` | `ciSetStructGeneratorExpressions` |
| `ciSetStructPDKMult` | `constraintsSKILL/constskillFunctions.html` | `ciSetStructPDKMult` |
| `ciSetSymmetricAxes` | `constraintsSKILL/constskillFunctions.html` | `ciSetSymmetricAxes` |
| `ciSigTypeMatchesNetType` | `constraintsSKILL/constskillFunctions.html` | `ciSigTypeMatchesNetType` |
| `ciSignalIterator` | `constraintsSKILL/constskillFunctions.html` | `ciSignalIterator` |
| `ciSimpleName` | `constraintsSKILL/constskillFunctions.html` | `ciSimpleName` |
| `ciSortDeviceInfoByFingerWidth   $constraintsSKILL/constskillFunctions.html` | `"ciSortDeviceInfoByFingerWidth"` | `HTML` |
| `ciSortDeviceInfoByMfactor` | `constraintsSKILL/constskillFunctions.html` | `ciSortDeviceInfoByMfactor` |
| `ciSortDeviceInfoByX` | `constraintsSKILL/constskillFunctions.html` | `ciSortDeviceInfoByX` |
| `ciSortDeviceInfoByXY` | `constraintsSKILL/constskillFunctions.html` | `ciSortDeviceInfoByXY` |
| `ciSortDeviceInfoByY` | `constraintsSKILL/constskillFunctions.html` | `ciSortDeviceInfoByY` |
| `ciSortDeviceInfoByYX` | `constraintsSKILL/constskillFunctions.html` | `ciSortDeviceInfoByYX` |
| `ciSortedOpenCellViews` | `constraintsSKILL/constskillFunctions.html` | `ciSortedOpenCellViews` |
| `ciTemplateAddCons` | `constraintsSKILL/constskillFunctions.html` | `ciTemplateAddCons` |
| `ciTemplateChangeDIProfile` | `constraintsSKILL/designIntentSKILL.html` | `ciTemplateChangeDIProfile` |
| `ciTemplateCreate` | `constraintsSKILL/constskillFunctions.html` | `ciTemplateCreate` |
| `ciTemplateCreateDI` | `constraintsSKILL/designIntentSKILL.html` | `ciTemplateCreateDI` |
| `ciTemplateCreateDefinition` | `constraintsSKILL/constskillFunctions.html` | `ciTemplateCreateDefinition` |
| `ciTemplateCreateExpanded` | `constraintsSKILL/constskillFunctions.html` | `ciTemplateCreateExpanded` |
| `ciTemplateDIProfileName` | `constraintsSKILL/designIntentSKILL.html` | `ciTemplateDIProfileName` |
| `ciTemplateDIPropDef` | `constraintsSKILL/designIntentSKILL.html` | `ciTemplateDIPropDef` |
| `ciTemplateDIPropGroupDef` | `constraintsSKILL/designIntentSKILL.html` | `ciTemplateDIPropGroupDef` |
| `ciTemplateDIPropValue` | `constraintsSKILL/designIntentSKILL.html` | `ciTemplateDIPropValue` |
| `ciTemplateDefinitionExists` | `constraintsSKILL/constskillFunctions.html` | `ciTemplateDefinitionExists` |
| `ciTemplateDelete` | `constraintsSKILL/constskillFunctions.html` | `ciTemplateDelete` |
| `ciTemplateDeleteCons` | `constraintsSKILL/constskillFunctions.html` | `ciTemplateDeleteCons` |
| `ciTemplateFind` | `constraintsSKILL/constskillFunctions.html` | `ciTemplateFind` |
| `ciTemplateGetCache` | `constraintsSKILL/constskillFunctions.html` | `ciTemplateGetCache` |
| `ciTemplateGetComment` | `constraintsSKILL/constskillFunctions.html` | `ciTemplateGetComment` |
| `ciTemplateGetCreatedTime` | `constraintsSKILL/constskillFunctions.html` | `ciTemplateGetCreatedTime` |
| `ciTemplateGetDefName` | `constraintsSKILL/constskillFunctions.html` | `ciTemplateGetDefName` |
| `ciTemplateGetName` | `constraintsSKILL/constskillFunctions.html` | `ciTemplateGetName` |
| `ciTemplateGetNote` | `constraintsSKILL/constskillFunctions.html` | `ciTemplateGetNote` |
| `ciTemplateGetStatus` | `constraintsSKILL/constskillFunctions.html` | `ciTemplateGetStatus` |
| `ciTemplateGetType` | `constraintsSKILL/constskillFunctions.html` | `ciTemplateGetType` |
| `ciTemplateIsKindOfDI` | `constraintsSKILL/designIntentSKILL.html` | `ciTemplateIsKindOfDI` |
| `ciTemplateListCon` | `constraintsSKILL/constskillFunctions.html` | `ciTemplateListCon` |
| `ciTemplateListDIProps` | `constraintsSKILL/designIntentSKILL.html` | `ciTemplateListDIProps` |
| `ciTemplateListParamNames` | `constraintsSKILL/constskillFunctions.html` | `ciTemplateListParamNames` |
| `ciTemplateListParams` | `constraintsSKILL/constskillFunctions.html` | `ciTemplateListParams` |
| `ciTemplateResetAllParams` | `constraintsSKILL/constskillFunctions.html` | `ciTemplateResetAllParams` |
| `ciTemplateResetParams` | `constraintsSKILL/constskillFunctions.html` | `ciTemplateResetParams` |
| `ciTemplateSetNote` | `constraintsSKILL/constskillFunctions.html` | `ciTemplateSetNote` |
| `ciTemplateSetStatus` | `constraintsSKILL/constskillFunctions.html` | `ciTemplateSetStatus` |
| `ciTemplateSortParamDefs` | `constraintsSKILL/constskillFunctions.html` | `ciTemplateSortParamDefs` |
| `ciTemplateUpdateDIProps` | `constraintsSKILL/designIntentSKILL.html` | `ciTemplateUpdateDIProps` |
| `ciTemplateUpdateParams` | `constraintsSKILL/constskillFunctions.html` | `ciTemplateUpdateParams` |
| `ciTemplatep` | `constraintsSKILL/constskillFunctions.html` | `ciTemplatep` |
| `ciToFloat` | `constraintsSKILL/constskillFunctions.html` | `ciToFloat` |
| `ciTransferConstraintsInProgress` | `constraintsSKILL/constskillFunctions.html` | `ciTransferConstraintsInProgress` |
| `ciTypeBindingParameter` | `constraintsSKILL/constskillFunctions.html` | `ciTypeBindingParameter` |
| `ciTypeHasBindingParameter` | `constraintsSKILL/constskillFunctions.html` | `ciTypeHasBindingParameter` |
| `ciTypeIsType` | `constraintsSKILL/constskillFunctions.html` | `ciTypeIsType` |
| `ciTypeIsUserDefined` | `constraintsSKILL/constskillFunctions.html` | `ciTypeIsUserDefined` |
| `ciTypeListCon` | `constraintsSKILL/constskillFunctions.html` | `ciTypeListCon` |
| `ciUnRegisterTerm` | `constraintsSKILL/constskillFunctions.html` | `ciUnRegisterTerm` |
| `ciUnexpandDeviceInfo` | `constraintsSKILL/constskillFunctions.html` | `ciUnexpandDeviceInfo` |
| `ciUnexpandIteratedDeviceInfo    $constraintsSKILL/constskillFunctions.html` | `"ciUnexpandIteratedDeviceInfo"` | `HTML` |
| `ciUnexpandPhysicalDeviceInfo    $constraintsSKILL/constskillFunctions.html` | `"ciUnexpandPhysicalDeviceInfo"` | `HTML` |
| `ciUniqueMembers` | `constraintsSKILL/constskillFunctions.html` | `ciUniqueMembers` |
| `ciUnregisterAssistant` | `constraintsSKILL/constskillFunctions.html` | `ciUnregisterAssistant` |
| `ciUnregisterConstraintEditor    $constraintsSKILL/constskillFunctions.html` | `"ciUnregisterConstraintEditor"` | `HTML` |
| `ciUnregisterConstraintGenerator` | `constraintsSKILL/constskillFunctions.html` | `ciUnregisterConstraintGenerator` |
| `ciUnregisterIterator` | `constraintsSKILL/constskillFunctions.html` | `ciUnregisterIterator` |
| `ciUnregisterNetSuperType` | `constraintsSKILL/constskillFunctions.html` | `ciUnregisterNetSuperType` |
| `ciUpdateHierarchicalNotes` | `constraintsSKILL/constskillFunctions.html` | `ciUpdateHierarchicalNotes` |
| `ciUpdateModgenParamsAndMembers` | `constraintsSKILL/constskillFunctions.html` | `ciUpdateModgenParamsAndMembers` |
| `ciUprevEAConstrs` | `constraintsSKILL/constskillFunctions.html` | `ciUprevEAConstrs` |
| `ciUtilsAddNTimes` | `constraintsSKILL/constskillFunctions.html` | `ciUtilsAddNTimes` |
| `ciUtilsAddQuotes` | `constraintsSKILL/constskillFunctions.html` | `ciUtilsAddQuotes` |
| `ciUtilsBuildString` | `constraintsSKILL/constskillFunctions.html` | `ciUtilsBuildString` |
| `ciUtilsGetArgVal` | `constraintsSKILL/constskillFunctions.html` | `ciUtilsGetArgVal` |
| `ciUtilsMakeNumberRange` | `constraintsSKILL/constskillFunctions.html` | `ciUtilsMakeNumberRange` |
| `ciUtilsMakeUnique` | `constraintsSKILL/constskillFunctions.html` | `ciUtilsMakeUnique` |
| `ciUtilsRemoveNils` | `constraintsSKILL/constskillFunctions.html` | `ciUtilsRemoveNils` |
| `ciUtilsRepeatNTimes` | `constraintsSKILL/constskillFunctions.html` | `ciUtilsRepeatNTimes` |
| `ciUtilsReplaceNils` | `constraintsSKILL/constskillFunctions.html` | `ciUtilsReplaceNils` |
| `ciVariantInfoForFingersAndFingerWidth` | `constraintsSKILL/constskillFunctions.html` | `ciVariantInfoForFingersAndFingerWidth` |
| `ciWithinConstraint` | `constraintsSKILL/constskillFunctions.html` | `ciWithinConstraint` |
| `ciXYInstSymmetricIterator` | `constraintsSKILL/constskillFunctions.html` | `ciXYInstSymmetricIterator` |
| `ciXYNetSymmetricIterator` | `constraintsSKILL/constskillFunctions.html` | `ciXYNetSymmetricIterator` |
| `ciXYPinSymmetricIterator` | `constraintsSKILL/constskillFunctions.html` | `ciXYPinSymmetricIterator` |
| `ciXYSortInsts` | `constraintsSKILL/constskillFunctions.html` | `ciXYSortInsts` |
| `ciXYSymmetricIterator` | `constraintsSKILL/constskillFunctions.html` | `ciXYSymmetricIterator` |


### AXL API

**283 个函数**，文档位置：

- `adexlSKILLref/setupDB.html` (62 个函数)
- `adexlSKILLref/runRelated.html` (34 个函数)
- `adexlSKILLref/jobPolicy.html` (29 个函数)
- `adexlSKILLref/sessionIl.html` (25 个函数)
- `adexlSKILLref/measures.html` (22 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `axlAddJobPolicy` | `adexlSKILLref/jobPolicy.html` | `axlAddJobPolicy` |
| `axlAddModelPermissibleSectionLists  $adexlSKILLref/modelRelated.html` | `"axlAddModelPermissibleSectionLists"` | `HTML` |
| `axlAddOutputExpr` | `adexlSKILLref/measures.html` | `axlAddOutputExpr` |
| `axlAddOutputSignal` | `adexlSKILLref/measures.html` | `axlAddOutputSignal` |
| `axlAddOutputs` | `adexlSKILLref/measures.html` | `axlAddOutputs` |
| `axlAddOutputsColumn` | `adexlSKILLref/measures.html` | `axlAddOutputsColumn` |
| `axlAddSpecToOutput` | `adexlSKILLref/specRelated.html` | `axlAddSpecToOutput` |
| `axlAttachJobPolicy` | `adexlSKILLref/jobPolicy.html` | `axlAttachJobPolicy` |
| `axlCloseSession` | `adexlSKILLref/sessionIl.html` | `axlCloseSession` |
| `axlCloseSessionInWindow` | `adexlSKILLref/sessionIl.html` | `axlCloseSessionInWindow` |
| `axlCloseSetupDB` | `adexlSKILLref/setupDB.html` | `axlCloseSetupDB` |
| `axlCommitSetupDB` | `adexlSKILLref/setupDB.html` | `axlCommitSetupDB` |
| `axlCommitSetupDBAndHistoryAs` | `adexlSKILLref/setupDB.html` | `axlCommitSetupDBAndHistoryAs"  HTML` |
| `axlCommitSetupDBas` | `adexlSKILLref/setupDB.html` | `axlCommitSetupDBas` |
| `axlCorners` | `adexlSKILLref/cornersRelated.html  "axlCorners"` | `HTML` |
| `axlCreateSession` | `adexlSKILLref/sessionIl.html` | `axlCreateSession` |
| `axlCustomADETestName` | `adexlSKILLref/testRelated.html` | `axlCustomADETestName` |
| `axlDeleteJobPolicy` | `adexlSKILLref/jobPolicy.html` | `axlDeleteJobPolicy` |
| `axlDeleteNote` | `adexlSKILLref/setupDB.html` | `axlDeleteNote` |
| `axlDeleteOutput` | `adexlSKILLref/measures.html` | `axlDeleteOutput` |
| `axlDeleteOutputsColumn` | `adexlSKILLref/measures.html` | `axlDeleteOutputsColumn` |
| `axlDetachJobPolicy` | `adexlSKILLref/jobPolicy.html` | `axlDetachJobPolicy` |
| `axlDiffSetup` | `adexlSKILLref/setupDB.html` | `axlDiffSetup` |
| `axlExportOutputView` | `adexlSKILLref/runRelated.html` | `axlExportOutputView` |
| `axlExportSetup` | `adexlSKILLref/setupDB.html` | `axlExportSetup` |
| `axlGetActiveSetup` | `adexlSKILLref/setupDB.html` | `axlGetActiveSetup` |
| `axlGetAllCornersEnabled` | `adexlSKILLref/cornersRelated.html  "axlGetAllCornersEnabled"` | `HTML` |
| `axlGetAllParametersDisabled` | `adexlSKILLref/ParameterRelated.html    "axlGetAllParametersDisabled"` | `HTML` |
| `axlGetAllSweepsEnabled` | `adexlSKILLref/runRelated.html` | `axlGetAllSweepsEnabled` |
| `axlGetAllVarsDisabled` | `adexlSKILLref/varRelated.html` | `axlGetAllVarsDisabled` |
| `axlGetAttachedJobPolicy` | `adexlSKILLref/jobPolicy.html` | `axlGetAttachedJobPolicy` |
| `axlGetCopyRefResultsOption` | `adexlSKILLref/setupDB.html` | `axlGetCopyRefResultsOption"    HTML` |
| `axlGetCorner` | `adexlSKILLref/cornersRelated.html  "axlGetCorner"` | `HTML` |
| `axlGetCornerCountForName` | `adexlSKILLref/cornersRelated.html  "axlGetCornerCountForName"` | `HTML` |
| `axlGetCornerDisabledTests` | `adexlSKILLref/cornersRelated.html  "axlGetCornerDisabledTests"` | `HTML` |
| `axlGetCornerNameForCurrentPointInRun` | `adexlSKILLref/cornersRelated.html  "axlGetCornerNameForCurrentPointInRun"` | `HTML` |
| `axlGetCorners` | `adexlSKILLref/cornersRelated.html  "axlGetCorners"` | `HTML` |
| `axlGetCornersForATest` | `adexlSKILLref/testRelated.html` | `axlGetCornersForATest` |
| `axlGetCurrentHistory` | `adexlSKILLref/historyRelated.html  "axlGetCurrentHistory"` | `HTML` |
| `axlGetCurrentResultSimulationHost   $adexlSKILLref/sessionIl.html` | `"axlGetCurrentResultSimulationHost"` | `HTML` |
| `axlGetCurrentRunMode` | `adexlSKILLref/runRelated.html` | `axlGetCurrentRunMode` |
| `axlGetElementParent` | `adexlSKILLref/setupDB.html` | `axlGetElementParent` |
| `axlGetEnabled` | `adexlSKILLref/setupDB.html` | `axlGetEnabled` |
| `axlGetEnabledGlobalVarPerTest` | `adexlSKILLref/testRelated.html` | `axlGetEnabledGlobalVarPerTest" HTML` |
| `axlGetEnabledTests` | `adexlSKILLref/testRelated.html` | `axlGetEnabledTests` |
| `axlGetHistory` | `adexlSKILLref/historyRelated.html  "axlGetHistory"` | `HTML` |
| `axlGetHistoryCheckpoint` | `adexlSKILLref/historyRelated.html  "axlGetHistoryCheckpoint"` | `HTML` |
| `axlGetHistoryEntry` | `adexlSKILLref/historyRelated.html  "axlGetHistoryEntry"` | `HTML` |
| `axlGetHistoryGroup` | `adexlSKILLref/historyRelated.html  "axlGetHistoryGroup"` | `HTML` |
| `axlGetHistoryGroupChildren` | `adexlSKILLref/setupDB.html` | `axlGetHistoryGroupChildren"    HTML` |
| `axlGetHistoryGroupChildrenEntry` | `adexlSKILLref/setupDB.html` | `axlGetHistoryGroupChildrenEntry` |
| `axlGetHistoryLock` | `adexlSKILLref/historyRelated.html  "axlGetHistoryLock"` | `HTML` |
| `axlGetHistoryName` | `adexlSKILLref/historyRelated.html  "axlGetHistoryName"` | `HTML` |
| `axlGetHistoryPrefix` | `adexlSKILLref/historyRelated.html  "axlGetHistoryPrefix"` | `HTML` |
| `axlGetHistoryResults` | `adexlSKILLref/historyRelated.html  "axlGetHistoryResults"` | `HTML` |
| `axlGetJobPolicy` | `adexlSKILLref/jobPolicy.html` | `axlGetJobPolicy` |
| `axlGetJobPolicyTypes` | `adexlSKILLref/jobPolicy.html` | `axlGetJobPolicyTypes` |
| `axlGetLocalResultsDir` | `adexlSKILLref/setupDB.html` | `axlGetLocalResultsDir` |
| `axlGetMainSetupDB` | `adexlSKILLref/sessionIl.html` | `axlGetMainSetupDB` |
| `axlGetModel` | `adexlSKILLref/modelRelated.html    "axlGetModel"` | `HTML` |
| `axlGetModelBlock` | `adexlSKILLref/modelRelated.html    "axlGetModelBlock"` | `HTML` |
| `axlGetModelFile` | `adexlSKILLref/modelRelated.html    "axlGetModelFile"` | `HTML` |
| `axlGetModelGroup` | `adexlSKILLref/modelRelated.html    "axlGetModelGroup"` | `HTML` |
| `axlGetModelGroupName` | `adexlSKILLref/modelRelated.html    "axlGetModelGroupName"` | `HTML` |
| `axlGetModelGroups` | `adexlSKILLref/modelRelated.html    "axlGetModelGroups"` | `HTML` |
| `axlGetModelSection` | `adexlSKILLref/modelRelated.html    "axlGetModelSection"` | `HTML` |
| `axlGetModelSections` | `adexlSKILLref/modelRelated.html` | `axlGetModelSections` |
| `axlGetModelTest` | `adexlSKILLref/modelRelated.html    "axlGetModelTest"` | `HTML` |
| `axlGetModels` | `adexlSKILLref/modelRelated.html    "axlGetModels"` | `HTML` |
| `axlGetNominalCornerTestEnabled` | `adexlSKILLref/cornersRelated.html  "axlGetNominalCornerTestEnabled"` | `HTML` |
| `axlGetNote` | `adexlSKILLref/historyRelated.html  "axlReEvaluateHistory"` | `HTML` |
| `axlGetOrigTestToolArgs` | `adexlSKILLref/testRelated.html` | `axlGetOrigTestToolArgs` |
| `axlGetOutputNotation` | `adexlSKILLref/measures.html` | `axlGetOutputNotation` |
| `axlGetOutputSignificantDigits` | `adexlSKILLref/measures.html` | `axlGetOutputSignificantDigits` |
| `axlGetOutputSuffix` | `adexlSKILLref/measures.html` | `axlGetOutputSuffix` |
| `axlGetOutputUnits` | `adexlSKILLref/measures.html` | `axlGetOutputUnits` |
| `axlGetOutputUserDefinedData` | `adexlSKILLref/measures.html` | `axlGetOutputUserDefinedData"   HTML` |
| `axlGetOverwriteHistory` | `adexlSKILLref/historyRelated.html  "axlGetOverwriteHistory"` | `HTML` |
| `axlGetParameter` | `adexlSKILLref/ParameterRelated.html    "axlGetParameter"` | `HTML` |
| `axlGetParameterValue` | `adexlSKILLref/ParameterRelated.html    "axlGetParameterValue"` | `HTML` |
| `axlGetParameters` | `adexlSKILLref/ParameterRelated.html    "axlGetParameters"` | `HTML` |
| `axlGetParasiticParaLCV` | `adexlSKILLref/runRelated.html` | `axlGetParasiticParaLCV` |
| `axlGetParasiticRunMode` | `adexlSKILLref/runRelated.html` | `axlGetParasiticRunMode` |
| `axlGetParasiticSchLCV` | `adexlSKILLref/runRelated.html` | `axlGetParasiticSchLCV` |
| `axlGetParasiticViewName` | `parasimSKILL/parasimSKILLFunctions.html` | `axlGetParasiticViewName` |
| `axlGetPointNetlistDir` | `adexlSKILLref/setupDB.html` | `axlGetPointNetlistDir` |
| `axlGetPointPsfDir` | `adexlSKILLref/setupDB.html` | `axlGetPointPsfDir` |
| `axlGetPointRunDir` | `adexlSKILLref/setupDB.html` | `axlGetPointRunDir` |
| `axlGetPointTroubleshootDir` | `adexlSKILLref/setupDB.html` | `axlGetPointTroubleshootDir"    HTML` |
| `axlGetPreRunScript` | `adexlSKILLref/runRelated.html` | `axlGetPreRunScript` |
| `axlGetReferenceHistoryItemName` | `adexlSKILLref/setupDB.html` | `axlGetReferenceHistoryItemName` |
| `axlGetResultsLocation` | `adexlSKILLref/setupDB.html` | `axlGetResultsLocation` |
| `axlGetReuseNetlist` | `adexlSKILLref/setupDB.html` | `axlGetReuseNetlist` |
| `axlGetRoHistSetupDB` | `adexlSKILLref/maestroSKILL.html    "axlGetRoHistSetupDB"` | `HTML` |
| `axlGetRunData` | `adexlSKILLref/runRelated.html` | `axlGetRunData` |
| `axlGetRunDistributeOptions` | `adexlSKILLref/runRelated.html` | `axlGetRunDistributeOptions"    HTML` |
| `axlGetRunMode` | `adexlSKILLref/runRelated.html` | `axlGetRunMode` |
| `axlGetRunModes` | `adexlSKILLref/runRelated.html` | `axlGetRunModes` |
| `axlGetRunOption` | `adexlSKILLref/runRelated.html` | `axlGetRunOption` |
| `axlGetRunOptionName` | `adexlSKILLref/runRelated.html` | `axlGetRunOptionName` |
| `axlGetRunOptionValue` | `adexlSKILLref/runRelated.html` | `axlGetRunOptionValue` |
| `axlGetRunOptions` | `adexlSKILLref/runRelated.html` | `axlGetRunOptions` |
| `axlGetRunStatus` | `adexlSKILLref/runRelated.html` | `axlGetRunStatus` |
| `axlGetScript` | `adexlSKILLref/setupDB.html` | `axlGetScript` |
| `axlGetScriptPath` | `adexlSKILLref/setupDB.html` | `axlGetScriptPath` |
| `axlGetScripts` | `adexlSKILLref/setupDB.html` | `axlGetScripts` |
| `axlGetSessionCellName` | `adexlSKILLref/sessionIl.html` | `axlGetSessionCellName` |
| `axlGetSessionFromSetupDB` | `adexlSKILLref/setupDB.html` | `axlGetSessionFromSetupDB` |
| `axlGetSessionLibName` | `adexlSKILLref/sessionIl.html` | `axlGetSessionLibName` |
| `axlGetSessionViewName` | `adexlSKILLref/sessionIl.html` | `axlGetSessionViewName` |
| `axlGetSessionWindowNumber` | `adexlSKILLref/sessionIl.html` | `axlGetSessionWindowNumber` |
| `axlGetSetupDBDir` | `adexlSKILLref/setupDB.html` | `axlGetSetupDBDir` |
| `axlGetSetupInfo` | `adexlSKILLref/setupDB.html` | `axlGetSetupInfo` |
| `axlGetSpec` | `adexlSKILLref/specRelated.html` | `axlGetSpec` |
| `axlGetSpecData` | `adexlSKILLref/specRelated.html` | `axlGetSpecData` |
| `axlGetSpecWeight` | `adexlSKILLref/specRelated.html` | `axlGetSpecWeight` |
| `axlGetSpecs` | `adexlSKILLref/specRelated.html` | `axlGetSpecs` |
| `axlGetStatVars` | `adexlSKILLref/cornersRelated.html  "axlGetStatVars"` | `HTML` |
| `axlGetTemperatureForCurrentPointInRun   $adexlSKILLref/measures.html` | `"axlGetTemperatureForCurrentPointInRun"` | `HTML` |
| `axlGetTest` | `adexlSKILLref/testRelated.html` | `axlGetTest` |
| `axlGetTestToolArgs` | `adexlSKILLref/testRelated.html` | `axlGetTestToolArgs` |
| `axlGetTests` | `adexlSKILLref/testRelated.html` | `axlGetTests` |
| `axlGetToolSession` | `adexlSKILLref/sessionIl.html` | `axlGetToolSession` |
| `axlGetTopLevel` | `adexlSKILLref/setupDB.html` | `axlGetTopLevel` |
| `axlGetUseIncremental` | `adexlSKILLref/setupDB.html` | `axlGetUseIncremental` |
| `axlGetUserDefinedOutputsColumns` | `adexlSKILLref/measures.html` | `axlGetUserDefinedOutputsColumns` |
| `axlGetVar` | `adexlSKILLref/varRelated.html` | `axlGetVar` |
| `axlGetVarValue` | `adexlSKILLref/varRelated.html` | `axlGetVarValue` |
| `axlGetVars` | `adexlSKILLref/varRelated.html` | `axlGetVars` |
| `axlGetWCCCorner` | `adexlSKILLref/cornersRelated.html  "axlGetWCCCorner"` | `HTML` |
| `axlGetWCCHistory` | `adexlSKILLref/cornersRelated.html  "axlGetWCCHistory"` | `HTML` |
| `axlGetWCCRangeBound` | `adexlSKILLref/cornersRelated.html  "axlGetWCCRangeBound"` | `HTML` |
| `axlGetWCCResult` | `adexlSKILLref/cornersRelated.html  "axlGetWCCResult"` | `HTML` |
| `axlGetWCCSpec` | `adexlSKILLref/cornersRelated.html  "axlGetWCCSpec"` | `HTML` |
| `axlGetWCCSpecs` | `adexlSKILLref/cornersRelated.html  "axlGetWCCSpecs"` | `HTML` |
| `axlGetWCCTest` | `adexlSKILLref/cornersRelated.html  "axlGetWCCTest"` | `HTML` |
| `axlGetWCCTime` | `adexlSKILLref/cornersRelated.html  "axlGetWCCTime"` | `HTML` |
| `axlGetWCCVar` | `adexlSKILLref/cornersRelated.html  "axlGetWCCVar"` | `HTML` |
| `axlGetWCCVarMonotonicity` | `adexlSKILLref/cornersRelated.html  "axlGetWCCVarMonotonicity"` | `HTML` |
| `axlGetWCCVars` | `adexlSKILLref/cornersRelated.html  "axlGetWCCVars"` | `HTML` |
| `axlGetWYCSigmaTargetLimit` | `adexlSKILLref/optimize.html` | `axlGetWYCSigmaTargetLimit` |
| `axlGetWindowSession` | `adexlSKILLref/sessionIl.html` | `axlGetWindowSession` |
| `axlImportPreRunScript` | `adexlSKILLref/runRelated.html` | `axlImportPreRunScript` |
| `axlImportSetup` | `adexlSKILLref/setupDB.html` | `axlImportSetup` |
| `axlIsICRPProcess` | `adexlSKILLref/jobPolicy.html` | `axlIsICRPProcess` |
| `axlIsLocalResultsDir` | `adexlSKILLref/setupDB.html` | `axlIsLocalResultsDir` |
| `axlIsSessionReadOnly` | `adexlSKILLref/sessionIl.html` | `axlIsSessionReadOnly` |
| `axlIsSessionReadOnly` | `adexlSKILLref/measures.html` | `axlIsSessionReadOnly` |
| `axlIsSimUsingStatParams` | `adexlSKILLref/runRelated.html` | `axlIsSimUsingStatParams` |
| `axlIsValidAXLSession` | `adexlSKILLref/sessionIl.html` | `axlIsValidAXLSession` |
| `axlJPGUICustDiffer` | `adexlSKILLref/jobPolicy.html` | `axlJPGUICustDiffer` |
| `axlJPGUICustHIFields` | `adexlSKILLref/jobPolicy.html` | `axlJPGUICustHIFields` |
| `axlJPGUICustOffset` | `adexlSKILLref/jobPolicy.html` | `axlJPGUICustOffset` |
| `axlJPGUICustReadFromForm` | `adexlSKILLref/jobPolicy.html` | `axlJPGUICustReadFromForm` |
| `axlJPGUICustSelected` | `adexlSKILLref/jobPolicy.html` | `axlJPGUICustSelected` |
| `axlJPGUICustWriteToForm` | `adexlSKILLref/jobPolicy.html` | `axlJPGUICustWriteToForm` |
| `axlJobIntfcDebugPrintf` | `adexlSKILLref/jobPolicy.html` | `axlJobIntfcDebugPrintf` |
| `axlJobIntfcDebugToFile` | `adexlSKILLref/jobPolicy.html` | `axlJobIntfcDebugToFile` |
| `axlJobIntfcDebugp` | `adexlSKILLref/jobPolicy.html` | `axlJobIntfcDebugp` |
| `axlJobIntfcExitMethod` | `adexlSKILLref/jobPolicy.html` | `axlJobIntfcExitMethod` |
| `axlJobIntfcHealthMethod` | `adexlSKILLref/jobPolicy.html` | `axlJobIntfcHealthMethod` |
| `axlJobIntfcSetDebug` | `adexlSKILLref/jobPolicy.html` | `axlJobIntfcSetDebug` |
| `axlJobIntfcStartMethod` | `adexlSKILLref/jobPolicy.html` | `axlJobIntfcStartMethod` |
| `axlLoadCorners` | `adexlSKILLref/cornersRelated.html  "axlLoadCorners"` | `HTML` |
| `axlLoadCornersFromPcfToSetupDB` | `adexlSKILLref/cornersRelated.html  "axlLoadCornersFromPcfToSetupDB"` | `HTML` |
| `axlLoadHistory` | `adexlSKILLref/historyRelated.html  "axlLoadHistory"` | `HTML` |
| `axlLoadSetupState` | `adexlSKILLref/setupDB.html` | `axlLoadSetupState` |
| `axlMainAppSaveSetup` | `adexlSKILLref/sessionIl.html` | `axlMainAppSaveSetup` |
| `axlMakeROHistory` | `adexlSKILLref/maestroSKILL.html    "axlMakeROHistory"` | `HTML` |
| `axlMakeViewHistory` | `adexlSKILLref/maestroSKILL.html    "axlMakeViewHistory"` | `HTML` |
| `axlMapInstTermToNet` | `parasimSKILL/parasimSKILLFunctions.html` | `axlMapInstTermToNet` |
| `axlNewSetupDB` | `adexlSKILLref/setupDB.html` | `axlNewSetupDB` |
| `axlNewSetupDBLCV` | `adexlSKILLref/setupDB.html` | `axlNewSetupDBLCV` |
| `axlNoSession` | `adexlSKILLref/sessionIl.html` | `axlNoSession` |
| `axlOpenResDB` | `adexlSKILLref/historyRelated.html  "axlOpenResDB"` | `HTML` |
| `axlOutputResult` | `adexlSKILLref/measures.html` | `axlOutputResult` |
| `axlOutputsExportToFile` | `adexlSKILLref/measures.html` | `axlOutputsExportToFile` |
| `axlOutputsImportFromFile` | `adexlSKILLref/measures.html` | `axlOutputsImportFromFile` |
| `axlPlotAcrossDesignPoints` | `adexlSKILLref/cornersRelated.html  "axlPlotAcrossDesignPoints"` | `HTML` |
| `axlPutCorner` | `adexlSKILLref/cornersRelated.html  "axlPutCorner"` | `HTML` |
| `axlPutDisabledCorner` | `adexlSKILLref/cornersRelated.html  "axlPutDisabledCorner"` | `HTML` |
| `axlPutHistoryEntry` | `adexlSKILLref/historyRelated.html  "axlPutHistoryEntry"` | `HTML` |
| `axlPutModel` | `adexlSKILLref/modelRelated.html    "axlPutModel"` | `HTML` |
| `axlPutModelGroup` | `adexlSKILLref/modelRelated.html    "axlPutModelGroup"` | `HTML` |
| `axlPutNote` | `adexlSKILLref/setupDB.html` | `axlPutNote` |
| `axlPutOutputNotation` | `adexlSKILLref/measures.html` | `axlPutOutputNotation` |
| `axlPutOutputSignificantDigits` | `adexlSKILLref/measures.html` | `axlPutOutputSignificantDigits` |
| `axlPutOutputSuffix` | `adexlSKILLref/measures.html` | `axlPutOutputSuffix` |
| `axlPutOutputUnits` | `adexlSKILLref/measures.html` | `axlPutOutputUnits` |
| `axlPutRunOption` | `adexlSKILLref/runRelated.html` | `axlPutRunOption` |
| `axlPutScript` | `adexlSKILLref/setupDB.html` | `axlPutScript` |
| `axlPutTest` | `adexlSKILLref/setupDB.html` | `axlPutTest` |
| `axlPutVar` | `adexlSKILLref/varRelated.html` | `axlPutVar` |
| `axlReEvaluateHistory                $adexlSKILLref/historyRelated.html` | `"axlReEvaluateHistory"` | `HTML` |
| `axlReadHistoryResDB` | `adexlSKILLref/runRelated.html` | `axlReadHistoryResDB` |
| `axlReadResDB` | `adexlSKILLref/runRelated.html` | `axlReadResDB` |
| `axlRegisterCustomDeviceFilter` | `adexlSKILLref/ParameterRelated.html    "axlRegisterCustomDeviceFilter"` | `HTML` |
| `axlRegisterJobIntfc` | `adexlSKILLref/jobPolicy.html` | `axlRegisterJobIntfc` |
| `axlRegisteredJobIntfcNames` | `adexlSKILLref/jobPolicy.html` | `axlRegisteredJobIntfcNames` |
| `axlRemoveElement` | `adexlSKILLref/setupDB.html` | `axlRemoveElement` |
| `axlRemoveSetupState` | `adexlSKILLref/sessionIl.html` | `axlRemoveSetupState` |
| `axlRenameOutputsColumn` | `adexlSKILLref/measures.html` | `axlRenameOutputsColumn` |
| `axlResetActive` | `adexlSKILLref/setupDB.html` | `axlResetActive` |
| `axlRestoreHistory` | `adexlSKILLref/historyRelated.html  "axlRestoreHistory"` | `HTML` |
| `axlRunAllTests` | `adexlSKILLref/runRelated.html` | `axlRunAllTests` |
| `axlRunAllTestsWithCallback` | `adexlSKILLref/runRelated.html` | `axlRunAllTestsWithCallback"    HTML` |
| `axlRunSimulation` | `adexlSKILLref/runRelated.html` | `axlRunSimulation` |
| `axlSDBDebugPrint` | `adexlSKILLref/setupDB.html` | `axlSDBDebugPrint` |
| `axlSDBGetChild` | `adexlSKILLref/setupDB.html` | `axlSDBGetChild` |
| `axlSDBGetChildVal` | `adexlSKILLref/setupDB.html` | `axlSDBGetChildVal` |
| `axlSDBGetChildren` | `adexlSKILLref/setupDB.html` | `axlSDBGetChildren` |
| `axlSDBGetExtension` | `adexlSKILLref/setupDB.html` | `axlSDBGetExtension` |
| `axlSDBGetName` | `adexlSKILLref/setupDB.html` | `axlSDBGetName` |
| `axlSDBGetValue` | `adexlSKILLref/setupDB.html` | `axlSDBGetValue` |
| `axlSDBHp` | `adexlSKILLref/setupDB.html` | `axlSDBHp` |
| `axlSDBPutExtension` | `adexlSKILLref/setupDB.html` | `axlSDBPutExtension` |
| `axlSDBSetChild` | `adexlSKILLref/setupDB.html` | `axlSDBSetChild` |
| `axlSDBSetMultipleEntry` | `adexlSKILLref/setupDB.html` | `axlSDBSetMultipleEntry` |
| `axlSDBSetValue` | `adexlSKILLref/setupDB.html` | `axlSDBSetValue` |
| `axlSaveJobPolicy` | `adexlSKILLref/jobPolicy.html` | `axlSaveJobPolicy` |
| `axlSaveSetup` | `adexlSKILLref/setupDB.html` | `axlSaveSetup` |
| `axlSaveSetupState` | `adexlSKILLref/sessionIl.html` | `axlSaveSetupState` |
| `axlSaveSetupToLib` | `adexlSKILLref/setupDB.html` | `axlSaveSetupToLib` |
| `axlSessionConnect` | `adexlSKILLref/sessionIl.html` | `axlSessionConnect` |
| `axlSessionDisconnect` | `adexlSKILLref/sessionIl.html` | `axlSessionDisconnect` |
| `axlSessionRegisterCreationCallback  $adexlSKILLref/sessionIl.html` | `"axlSessionRegisterCreationCallback"` | `HTML` |
| `axlSessionSignalList` | `adexlSKILLref/sessionIl.html` | `axlSessionSignalList` |
| `axlSessionSignalSignature` | `adexlSKILLref/sessionIl.html` | `axlSessionSignalSignature` |
| `axlSetAllCornersEnabled` | `adexlSKILLref/cornersRelated.html  "axlSetAllCornersEnabled"` | `HTML` |
| `axlSetAllParametersDisabled` | `adexlSKILLref/ParameterRelated.html` | `axlSetAllParametersDisabled` |
| `axlSetAllSweepsEnabled` | `adexlSKILLref/setupDB.html` | `axlSetAllSweepsEnabled` |
| `axlSetAllVarsDisabled` | `adexlSKILLref/varRelated.html` | `axlSetAllVarsDisabled` |
| `axlSetCopyRefResultsOption` | `adexlSKILLref/setupDB.html` | `axlSetCopyRefResultsOption"    HTML` |
| `axlSetCornerName` | `adexlSKILLref/cornersRelated.html  "axlSetCornerName"` | `HTML` |
| `axlSetCornerTestEnabled` | `adexlSKILLref/cornersRelated.html  "axlSetCornerTestEnabled"` | `HTML` |
| `axlSetCurrentRunMode` | `adexlSKILLref/runRelated.html` | `axlSetCurrentRunMode` |
| `axlSetDefaultVariables` | `adexlSKILLref/varRelated.html` | `axlSetDefaultVariables` |
| `axlSetDesignVariablePerTest` | `adexlSKILLref/varRelated.html` | `axlSetDesignVariablePerTest"   HTML` |
| `axlSetEnabled` | `adexlSKILLref/setupDB.html` | `axlSetEnabled` |
| `axlSetHistoryLock` | `adexlSKILLref/historyRelated.html  "axlSetHistoryLock"` | `HTML` |
| `axlSetHistoryName` | `adexlSKILLref/historyRelated.html  "axlSetHistoryName"` | `HTML` |
| `axlSetJobPolicyProperty` | `adexlSKILLref/jobPolicy.html` | `axlSetJobPolicyProperty` |
| `axlSetMainSetupDB` | `adexlSKILLref/sessionIl.html` | `axlSetMainSetupDB` |
| `axlSetMainSetupDBLCV` | `adexlSKILLref/sessionIl.html` | `axlSetMainSetupDBLCV` |
| `axlSetModelBlock` | `adexlSKILLref/modelRelated.html    "axlSetModelBlock"` | `HTML` |
| `axlSetModelFile` | `adexlSKILLref/modelRelated.html    "axlSetModelFile"` | `HTML` |
| `axlSetModelGroupName` | `adexlSKILLref/modelRelated.html    "axlSetModelGroupName"` | `HTML` |
| `axlSetModelSection` | `adexlSKILLref/modelRelated.html    "axlSetModelSection"` | `HTML` |
| `axlSetModelTest` | `adexlSKILLref/modelRelated.html    "axlSetModelTest"` | `HTML` |
| `axlSetNominalCornerTestEnabled` | `adexlSKILLref/cornersRelated.html  "axlSetNominalCornerTestEnabled"` | `HTML` |
| `axlSetOutputUserDefinedData` | `adexlSKILLref/measures.html` | `axlSetOutputUserDefinedData"   HTML` |
| `axlSetOverwriteHistory` | `adexlSKILLref/historyRelated.html  "axlSetOverwriteHistory"` | `HTML` |
| `axlSetParameter` | `adexlSKILLref/ParameterRelated.html    "axlSetParameter"` | `HTML` |
| `axlSetParasiticRunMode` | `adexlSKILLref/runRelated.html` | `axlSetParasiticRunMode` |
| `axlSetParasiticViewName` | `parasimSKILL/parasimSKILLFunctions.html` | `axlSetParasiticViewName` |
| `axlSetPreRunScript` | `adexlSKILLref/runRelated.html` | `axlSetPreRunScript` |
| `axlSetPreRunScriptEnabled` | `adexlSKILLref/runRelated.html` | `axlSetPreRunScriptEnabled` |
| `axlSetReferenceHistoryItemName` | `adexlSKILLref/setupDB.html` | `axlSetReferenceHistoryItemName` |
| `axlSetReuseNetlistOption` | `adexlSKILLref/setupDB.html` | `axlSetReuseNetlistOption` |
| `axlSetRunDistributeOptions` | `adexlSKILLref/runRelated.html` | `axlSetRunDistributeOptions"    HTML` |
| `axlSetRunOptionName` | `adexlSKILLref/runRelated.html` | `axlSetRunOptionName` |
| `axlSetRunOptionValue` | `adexlSKILLref/runRelated.html` | `axlSetRunOptionValue` |
| `axlSetScriptPath` | `adexlSKILLref/setupDB.html` | `axlSetScriptPath` |
| `axlSetTestToolArgs` | `adexlSKILLref/testRelated.html` | `axlSetTestToolArgs` |
| `axlSetUseIncremental` | `adexlSKILLref/setupDB.html` | `axlSetUseIncremental` |
| `axlSetWCCTime` | `adexlSKILLref/cornersRelated.html  "axlSetWCCTime"` | `HTML` |
| `axlSetWYCSigmaTargetLimit` | `adexlSKILLref/optimize.html` | `axlSetWYCSigmaTargetLimit` |
| `axlSetupStates` | `adexlSKILLref/sessionIl.html` | `axlSetupStates` |
| `axlShowPersistedQuestionDialog` | `adexlSKILLref/sessionIl.html` | `axlShowPersistedQuestionDialog` |
| `axlStop` | `adexlSKILLref/runRelated.html` | `axlStop` |
| `axlStopAll` | `adexlSKILLref/runRelated.html` | `axlStopAll` |
| `axlStopAllJobs` | `adexlSKILLref/jobPolicy.html` | `axlStopAllJobs` |
| `axlStopJob` | `adexlSKILLref/jobPolicy.html` | `axlStopJob` |
| `axlSuppressPersistedQuestionDialog` | `adexlSKILLref/sessionIl.html` | `axlSuppressPersistedQuestionDialog` |
| `axlToolSetOriginalSetupOptions` | `adexlSKILLref/testRelated.html` | `axlToolSetOriginalSetupOptions` |
| `axlToolSetSetupOptions` | `adexlSKILLref/testRelated.html` | `axlToolSetSetupOptions` |
| `axlViewHistoryResults` | `adexlSKILLref/historyRelated.html  "axlViewHistoryResults"` | `HTML` |
| `axlViewResDB` | `adexlSKILLref/runRelated.html` | `axlViewResDB` |
| `axlWriteDatasheet` | `adexlSKILLref/setupDB.html` | `axlWriteDatasheet` |
| `axlWriteDatasheetForm` | `adexlSKILLref/setupDB.html` | `axlWriteDatasheetForm` |
| `axlWriteOceanScriptLCV` | `adexlSKILLref/testRelated.html` | `axlWriteOceanScriptLCV` |
| `axlregisteredJPGUICust` | `adexlSKILLref/jobPolicy.html` | `axlregisteredJPGUICust` |
| `axlregisteredJobIntfcNames` | `adexlSKILLref/jobPolicy.html` | `axlregisteredJobIntfcNames"    HTML` |


### HI API

**180 个函数**，文档位置：

- `skuiref/chap2.html` (64 个函数)
- `skuiref/chap5.html` (37 个函数)
- `skuiref/chap3.html` (30 个函数)
- `skuiref/chap4.html` (28 个函数)
- `skuiref/chap9.html` (5 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `hiAddExtraRepeatCommand` | `skuiref/chap2.html` | `hiAddExtraRepeatCommand` |
| `hiAddIconOverrides` | `skuiref/chap7.html` | `hiAddIconOverrides"           HTML` |
| `hiAddMenuItem` | `skuiref/chap3.html` | `hiAddMenuItem` |
| `hiAddNonRepeatPrefix` | `skuiref/chap2.html` | `hiAddNonRepeatPrefix` |
| `hiAddToolbarItem` | `skuiref/chap4.html` | `hiAddToolbarItem` |
| `hiAddToolbarItems` | `skuiref/chap4.html` | `hiAddToolbarItems` |
| `hiAdvanceProgressBarOneStep` | `skuiref/chap5.html` | `hiAdvanceProgressBarOneStep"   HTML` |
| `hiBoxCenter` | `skuiref/chap2.html` | `hiBoxCenter` |
| `hiCancelProgressBox` | `skuiref/chap5.html` | `hiCancelProgressBox` |
| `hiCheckAbort` | `skuiref/chap2.html` | `hiCheckAbort` |
| `hiClearClipboard` | `skuiref/chap14.html` | `hiClearClipboard` |
| `hiCreate2DMenu` | `skuiref/chap3.html` | `hiCreate2DMenu` |
| `hiCreateAction` | `skuiref/chap4.html` | `hiCreateAction` |
| `hiCreateHorizontalFixedMenu` | `skuiref/chap3.html` | `hiCreateHorizontalFixedMenu"   HTML` |
| `hiCreateMenu` | `skuiref/chap3.html` | `hiCreateMenu` |
| `hiCreateMenuItem` | `skuiref/chap3.html` | `hiCreateMenuItem` |
| `hiCreatePulldownMenu` | `skuiref/chap3.html` | `hiCreatePulldownMenu` |
| `hiCreateSeparatorMenuItem` | `skuiref/chap3.html` | `hiCreateSeparatorMenuItem` |
| `hiCreateSimpleMenu` | `skuiref/chap3.html` | `hiCreateSimpleMenu` |
| `hiCreateSliderMenuItem` | `skuiref/chap3.html` | `hiCreateSliderMenuItem` |
| `hiCreateToolbar` | `skuiref/chap4.html` | `hiCreateToolbar` |
| `hiCreateToolbarComboBox` | `skuiref/chap4.html` | `hiCreateToolbarComboBox` |
| `hiCreateToolbarSeparator` | `skuiref/chap4.html` | `hiCreateToolbarSeparator` |
| `hiCreateToolbarTypein` | `skuiref/chap4.html` | `hiCreateToolbarTypein` |
| `hiCreateTypeinMenuItem` | `skuiref/chap3.html` | `hiCreateTypeinMenuItem` |
| `hiCreateVerticalFixedMenu` | `skuiref/chap3.html` | `hiCreateVerticalFixedMenu` |
| `hiDBoxCancel` | `skuiref/chap5.html` | `hiDBoxCancel` |
| `hiDBoxOK` | `skuiref/chap5.html` | `hiDBoxOK` |
| `hiDeleteMenu` | `skuiref/chap3.html` | `hiDeleteMenu` |
| `hiDeleteMenuItem` | `skuiref/chap3.html` | `hiDeleteMenuItem` |
| `hiDeleteToolbar` | `skuiref/chap4.html` | `hiDeleteToolbar` |
| `hiDeleteToolbarBreak` | `skuiref/chap4.html` | `hiDeleteToolbarBreak` |
| `hiDeleteToolbarItem` | `skuiref/chap4.html` | `hiDeleteToolbarItem` |
| `hiDeleteToolbarItems` | `skuiref/chap4.html` | `hiDeleteToolbarItems` |
| `hiDisableMenuItem` | `skuiref/chap3.html` | `hiDisableMenuItem` |
| `hiDisplayAppDBox` | `skuiref/chap5.html` | `hiDisplayAppDBox` |
| `hiDisplayBlockingDBox` | `skuiref/chap5.html` | `hiDisplayBlockingDBox` |
| `hiDisplayColorDialog` | `skuiref/chap5.html` | `hiDisplayColorDialog` |
| `hiDisplayFileDialog` | `skuiref/chap5.html` | `hiDisplayFileDialog` |
| `hiDisplayFixedMenu` | `skuiref/chap3.html` | `hiDisplayFixedMenu` |
| `hiDisplayHistory` | `skuiref/chap2.html` | `hiDisplayHistory` |
| `hiDisplayMenu` | `skuiref/chap3.html` | `hiDisplayMenu` |
| `hiDisplayModalDBox` | `skuiref/chap5.html` | `hiDisplayModalDBox` |
| `hiDisplayModelessDBox` | `skuiref/chap5.html` | `hiDisplayModelessDBox` |
| `hiDisplayProgressBox` | `skuiref/chap5.html` | `hiDisplayProgressBox` |
| `hiDisplaySaveForRestoreDialog` | `skuiref/chap2.html` | `hiDisplaySaveForRestoreDialog" HTML` |
| `hiDisplayUserDBox` | `skuiref/chap5.html` | `hiDisplayUserDBox` |
| `hiDisplayWindowMenu` | `skuiref/chap3.html` | `hiDisplayWindowMenu` |
| `hiEditfile` | `skuiref/chap2.html` | `hiEditfile` |
| `hiEnableMenuItem` | `skuiref/chap3.html` | `hiEnableMenuItem` |
| `hiEndLog` | `skuiref/chap2.html` | `hiEndLog` |
| `hiEnqueueCmd` | `skuiref/chap2.html` | `hiEnqueueCmd` |
| `hiFileDialogDone` | `skuiref/chap5.html` | `hiFileDialogDone` |
| `hiFileDialogSelection` | `skuiref/chap5.html` | `hiFileDialogSelection` |
| `hiFileDialogSetSelection` | `skuiref/chap5.html` | `hiFileDialogSetSelection` |
| `hiFixedMenuDown` | `skuiref/chap3.html` | `hiFixedMenuDown` |
| `hiFlush` | `skuiref/chap2.html` | `hiFlush` |
| `hiFlushCIW` | `skuiref/chap2.html` | `hiFlushCIW` |
| `hiFlushInfo` | `skdfref/chap2.html             "hiFlushInfo"` | `HTML` |
| `hiFlushLogFile` | `skuiref/chap2.html` | `hiFlushLogFile` |
| `hiFocusToCIW` | `skuiref/chap2.html` | `hiFocusToCIW` |
| `hiFocusToToolbarItem` | `skuiref/chap4.html` | `hiFocusToToolbarItem"          HTML` |
| `hiGetAnyFile` | `skuiref/chap5.html` | `hiGetAnyFile` |
| `hiGetAttention` | `skuiref/chap2.html` | `hiGetAttention` |
| `hiGetBBoxResource` | `skuiref/chap2.html` | `hiGetBBoxResource` |
| `hiGetBannerPoint` | `skuiref/chap2.html` | `hiGetBannerPoint` |
| `hiGetBeepVolume` | `skuiref/chap2.html` | `hiGetBeepVolume` |
| `hiGetCIWindow` | `skuiref/chap2.html` | `hiGetCIWindow` |
| `hiGetChoiceStrings` | `skuiref/chap8.html` | `hiGetChoiceStrings` |
| `hiGetCommandPoint` | `skuiref/chap2.html` | `hiGetCommandPoint` |
| `hiGetCurrentEnterFunPoints` | `skuiref/chap9.html` | `hiGetCurrentEnterFunPoints` |
| `hiGetCyclicValueString` | `skuiref/chap8.html` | `hiGetCyclicValueString` |
| `hiGetDBoxDefaultLocation` | `skuiref/chap5.html` | `hiGetDBoxDefaultLocation` |
| `hiGetDisplayName` | `skuiref/chap2.html` | `hiGetDisplayName` |
| `hiGetExistingDirectory` | `skuiref/chap5.html` | `hiGetExistingDirectory` |
| `hiGetExistingFile` | `skuiref/chap5.html` | `hiGetExistingFile` |
| `hiGetExistingFiles` | `skuiref/chap5.html` | `hiGetExistingFiles` |
| `hiGetFont` | `skuiref/chap2.html` | `hiGetFont` |
| `hiGetFontInfo` | `skuiref/chap2.html` | `hiGetFontInfo` |
| `hiGetGeometryResource` | `skuiref/chap2.html` | `hiGetGeometryResource` |
| `hiGetIconOverrides` | `skuiref/chap7.html` | `hiGetIconOverrides"           HTML` |
| `hiGetLogFileName` | `skuiref/chap2.html` | `hiGetLogFileName` |
| `hiGetMenuItems` | `skuiref/chap3.html` | `hiGetMenuItems` |
| `hiGetMouseMoveSampleRate` | `skuiref/chap2.html` | `hiGetMouseMoveSampleRate` |
| `hiGetMouseStopDetectTime` | `skuiref/chap2.html` | `hiGetMouseStopDetectTime` |
| `hiGetMultiClickTime` | `skuiref/chap2.html` | `hiGetMultiClickTime` |
| `hiGetNonRepeatPrefixes` | `skuiref/chap2.html` | `hiGetNonRepeatPrefixes` |
| `hiGetPoint` | `skuiref/chap2.html` | `hiGetPoint` |
| `hiGetProgress` | `skuiref/chap5.html` | `hiGetProgress` |
| `hiGetProgressBarCurrentStep` | `skuiref/chap5.html` | `hiGetProgressBarCurrentStep"   HTML` |
| `hiGetProgressBarTotalSteps` | `skuiref/chap5.html` | `hiGetProgressBarTotalSteps"    HTML` |
| `hiGetProgressTotalSteps` | `skuiref/chap5.html` | `hiGetProgressTotalSteps` |
| `hiGetRadioValueString` | `skuiref/chap8.html` | `hiGetRadioValueString` |
| `hiGetRepeatCommand` | `skuiref/chap2.html` | `hiGetRepeatCommand` |
| `hiGetScreenSize` | `skuiref/chap2.html` | `hiGetScreenSize` |
| `hiGetSharedIcon` | `skuiref/chap4.html` | `hiGetSharedIcon` |
| `hiGetStringResource` | `skuiref/chap2.html` | `hiGetStringResource` |
| `hiGetTextWidth` | `skuiref/chap2.html` | `hiGetTextWidth` |
| `hiGetToolbarObjName` | `skuiref/chap4.html` | `hiGetToolbarObjName` |
| `hiGetUserAbort` | `skuiref/chap2.html` | `hiGetUserAbort` |
| `hiGetWindowMenu` | `skuiref/chap3.html` | `hiGetWindowMenu` |
| `hiGetWindowToolbars` | `skuiref/chap4.html` | `hiGetWindowToolbars` |
| `hiGetXFontName` | `skuiref/chap2.html` | `hiGetXFontName` |
| `hiGraphicMode` | `skuiref/chap2.html` | `hiGraphicMode` |
| `hiHasToolbarBreak` | `skuiref/chap4.html` | `hiHasToolbarBreak` |
| `hiHideProgressBar` | `skuiref/chap5.html` | `hiHideProgressBar` |
| `hiHideToolbar` | `skuiref/chap4.html` | `hiHideToolbar` |
| `hiInsertMenuItem` | `skuiref/chap3.html` | `hiInsertMenuItem` |
| `hiInsertToolbar` | `skuiref/chap4.html` | `hiInsertToolbar` |
| `hiInsertToolbarBreak` | `skuiref/chap4.html` | `hiInsertToolbarBreak` |
| `hiInsertToolbarItem` | `skuiref/chap4.html` | `hiInsertToolbarItem` |
| `hiInsertToolbarItems` | `skuiref/chap4.html` | `hiInsertToolbarItems` |
| `hiIs2DMenu` | `skuiref/chap3.html` | `hiIs2DMenu` |
| `hiIsExtraRepeatCommand` | `skuiref/chap2.html` | `hiIsExtraRepeatCommand"            HTML` |
| `hiIsIcon` | `skuiref/chap3.html` | `hiIsIcon` |
| `hiIsInReplay` | `skuiref/chap2.html` | `hiIsInReplay` |
| `hiIsMenu` | `skuiref/chap3.html` | `hiIsMenu` |
| `hiIsMenuItemEnabled` | `skuiref/chap3.html` | `hiIsMenuItemEnabled` |
| `hiIsProgressBoxCancelled` | `skuiref/chap5.html` | `hiIsProgressBoxCancelled` |
| `hiListFocusableToolbarItems` | `skuiref/chap4.html` | `hiListFocusableToolbarItems"   HTML` |
| `hiLogDragEvents` | `skuiref/chap2.html` | `hiLogDragEvents` |
| `hiPlaceToolbar` | `skuiref/chap4.html` | `hiPlaceToolbar` |
| `hiPlaceToolbarBreak` | `skuiref/chap4.html` | `hiPlaceToolbarBreak` |
| `hiPrintToLogFile` | `skuiref/chap2.html` | `hiPrintToLogFile` |
| `hiQueryFont` | `skuiref/chap2.html` | `hiQueryFont` |
| `hiQuit` | `skuiref/chap2.html` | `hiQuit` |
| `hiReattachToolbar` | `skuiref/chap4.html` | `hiReattachToolbar` |
| `hiRegTimer` | `skuiref/chap2.html` | `hiRegTimer` |
| `hiRemoveExtraRepeatCommand` | `skuiref/chap2.html` | `hiRemoveExtraRepeatCommand` |
| `hiRemoveIconOverrides` | `skuiref/chap7.html` | `hiRemoveIconOverrides"        HTML` |
| `hiRemoveNonRepeatPrefix` | `skuiref/chap2.html` | `hiRemoveNonRepeatPrefix` |
| `hiRepeat` | `skuiref/chap2.html` | `hiRepeat` |
| `hiReplayFile` | `skuiref/chap2.html` | `hiReplayFile` |
| `hiResetAbort` | `skuiref/chap2.html` | `hiResetAbort` |
| `hiResetProgressBox` | `skuiref/chap5.html` | `hiResetProgressBox` |
| `hiSaveForRestore` | `skuiref/chap2.html` | `hiSaveForRestore` |
| `hiScaleBox` | `skuiref/chap2.html` | `hiScaleBox` |
| `hiSetAbort` | `skuiref/chap2.html` | `hiSetAbort` |
| `hiSetActionChecked` | `skuiref/chap4.html` | `hiSetActionChecked` |
| `hiSetBeepVolume` | `skuiref/chap2.html` | `hiSetBeepVolume` |
| `hiSetClipboard` | `skuiref/chap14.html` | `hiSetClipboard` |
| `hiSetDBoxDefaultLocation` | `skuiref/chap5.html` | `hiSetDBoxDefaultLocation` |
| `hiSetFilter` | `skuiref/chap2.html` | `hiSetFilter` |
| `hiSetFilterOptions` | `skuiref/chap2.html` | `hiSetFilterOptions` |
| `hiSetFont` | `skuiref/chap2.html` | `hiSetFont` |
| `hiSetMenuItemCallback` | `skuiref/chap3.html` | `hiSetMenuItemCallback` |
| `hiSetMenuItemStatusTip` | `skuiref/chap3.html` | `hiSetMenuItemStatusTip` |
| `hiSetMenuItemText` | `skuiref/chap3.html` | `hiSetMenuItemText` |
| `hiSetMouseMoveSampleRate` | `skuiref/chap2.html` | `hiSetMouseMoveSampleRate` |
| `hiSetMouseStopDetectTime` | `skuiref/chap2.html` | `hiSetMouseStopDetectTime` |
| `hiSetMultiClickTime` | `skuiref/chap2.html` | `hiSetMultiClickTime` |
| `hiSetProgress` | `skuiref/chap5.html` | `hiSetProgress` |
| `hiSetProgressAndText` | `skuiref/chap5.html` | `hiSetProgressAndText` |
| `hiSetProgressBannerText` | `skuiref/chap5.html` | `hiSetProgressBannerText` |
| `hiSetProgressBar` | `skuiref/chap5.html` | `hiSetProgressBar` |
| `hiSetProgressButtonText` | `skuiref/chap5.html` | `hiSetProgressButtonText` |
| `hiSetProgressLabel` | `skuiref/chap5.html` | `hiSetProgressLabel` |
| `hiSetProgressText` | `skuiref/chap5.html` | `hiSetProgressText` |
| `hiSetProgressTotalSteps` | `skuiref/chap5.html` | `hiSetProgressTotalSteps` |
| `hiSetToolbarObjName` | `skuiref/chap4.html` | `hiSetToolbarObjName` |
| `hiSetTypeinMenuItemCompleterList    $skuiref/chap3.html` | `"hiSetTypeinMenuItemCompleterList"` | `HTML` |
| `hiSetUserPreferences` | `skuiref/chap2.html` | `hiSetUserPreferences` |
| `hiSetWindowDefaultPrompt` | `skuiref/chap2.html` | `hiSetWindowDefaultPrompt` |
| `hiSetWindowFocus` | `skuiref/chap2.html` | `hiSetWindowFocus` |
| `hiSetWindowMenu` | `skuiref/chap3.html` | `hiSetWindowMenu` |
| `hiShowProgressBar` | `skuiref/chap5.html` | `hiShowProgressBar` |
| `hiShowToolbar` | `skuiref/chap4.html` | `hiShowToolbar` |
| `hiStartLog` | `skuiref/chap2.html` | `hiStartLog` |
| `hiSynchronize` | `skuiref/chap2.html` | `hiSynchronize` |
| `hiTextWidth` | `skuiref/chap2.html` | `hiTextWidth` |
| `hiViewTextFile` | `skuiref/chap14.html` | `hiViewTextFile"               HTML` |
| `hiViewfile` | `skuiref/chap14.html` | `hiViewfile"                   HTML` |
| `hiWorldViewFit` | `skuiref/chap9.html` | `hiWorldViewFit"                HTML` |
| `hiWorldViewRedraw` | `skuiref/chap9.html` | `hiWorldViewRedraw"             HTML` |
| `hiWorldViewZoomIn` | `skuiref/chap9.html` | `hiWorldViewZoomIn"             HTML` |
| `hiWorldViewZoomOut` | `skuiref/chap9.html` | `hiWorldViewZoomOut"            HTML` |
| `histo_OCEAN` | `oceanref/chap10.html` | `histo` |
| `histogram2D_OCEAN` | `oceanref/chap10.html` | `histogram2D` |
| `histogram2D_ViVA_SKILL` | `vivaxlug/appD.html` | `histogram2D` |
| `history_OCEAN` | `oceanref/chap5.html` | `history` |


### DB API

**165 个函数**，文档位置：

- `skdfref/placement.html` (46 个函数)
- `skdfref/chap2.html` (20 个函数)
- `skdfref/inplacecoverobs.html` (20 个函数)
- `skdfref/generator.html` (15 个函数)
- `skdfref/photonic.html` (10 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `db10_OCEAN` | `oceanref/chap10.html` | `db10` |
| `db20_OCEAN` | `oceanref/chap10.html` | `db20` |
| `dbAddPlaceAreaBackgroundDef` | `skdfref/placement.html` | `dbAddPlaceAreaBackgroundDef` |
| `dbAddRowBackgroundDef` | `skdfref/placement.html` | `dbAddRowBackgroundDef` |
| `dbAttachRowRegionToPRBoundary` | `skdfref/placement.html` | `dbAttachRowRegionToPRBoundary` |
| `dbCanonicalizeAnyAngleTransform` | `skdfref/chap2.html` | `dbCanonicalizeAnyAngleTransform"   HTML` |
| `dbCellViewHasEquivalentConnectivityTime` | `skdfref/connect.html` | `dbCellViewHasEquivalentConnectivityTime` |
| `dbCellViewHasPhotonicPinFig` | `skdfref/photonic.html` | `dbCellViewHasPhotonicPinFig` |
| `dbCellViewResetAllColorLockTypes        $skdfref/mpt.html` | `"dbCellViewResetAllColorLockTypes"` | `HTML` |
| `dbClearPcellCache` | `skpcellref/xpcellFunctions.html` | `dbClearPcellCache` |
| `dbCompressionPlot_OCEAN` | `oceanref/chap8.html` | `dbCompressionPlot` |
| `dbConvertAnyAngleTransformFromDbToMY` | `skdfref/chap2.html` | `dbConvertAnyAngleTransformFromDbToMY"             HTML` |
| `dbCreateBackgroundDef` | `skdfref/placement.html` | `dbCreateBackgroundDef` |
| `dbCreateBackgroundDefByAttr` | `skdfref/placement.html` | `dbCreateBackgroundDefByAttr` |
| `dbCreateCompTypeSetDefByAttr` | `skdfref/placement.html` | `dbCreateCompTypeSetDefByAttr` |
| `dbCreateInPlaceCoverObstruction` | `skdfref/inplacecoverobs.html` | `dbCreateInPlaceCoverObstruction` |
| `dbCreateMultipleCurvedPolygons` | `skdfref/vrf.html` | `dbCreateMultipleCurvedPolygons` |
| `dbCreateNamedSubNet` | `skdfref/connect.html` | `dbCreateNamedSubNet` |
| `dbCreateRailDefByAttr` | `skdfref/placement.html` | `dbCreateRailDefByAttr` |
| `dbCreateRowRegion` | `skdfref/placement.html` | `dbCreateRowRegion` |
| `dbCreateRowRegionSpec` | `skdfref/placement.html` | `dbCreateRowRegionSpec` |
| `dbCreateRuler` | `skdfref/chap2.html` | `dbCreateRuler"                             HTML` |
| `dbDestroyInPlaceCoverObstruction` | `skdfref/inplacecoverobs.html` | `dbDestroyInPlaceCoverObstruction` |
| `dbDetachPRBoundaryFromRowRegion` | `skdfref/placement.html` | `dbDetachPRBoundaryFromRowRegion` |
| `dbFeaturePrintInfo` | `skdfref/cvio.html` | `dbFeaturePrintInfo"                HTML` |
| `dbFindRowRegion` | `skdfref/placement.html` | `dbFindRowRegion` |
| `dbFindRowRegionSpec` | `skdfref/placement.html` | `dbFindRowRegionSpec` |
| `dbFlattenRowRegion` | `skdfref/placement.html` | `dbFlattenRowRegion` |
| `dbGet` | `skdfref/attrib.html` | `dbGet` |
| `dbGetBackgroundDefAttr` | `skdfref/placement.html` | `dbGetBackgroundDefAttr` |
| `dbGetCellViewBackgroundDef` | `skdfref/placement.html` | `dbGetCellViewBackgroundDef` |
| `dbGetCellViewEquivalentConnectivityTime` | `skdfref/connect.html` | `dbGetCellViewEquivalentConnectivityTime` |
| `dbGetCellViewRailDef` | `skdfref/placement.html` | `dbGetCellViewRailDef` |
| `dbGetCellViewRowRegionSpecs` | `skdfref/placement.html` | `dbGetCellViewRowRegionSpecs` |
| `dbGetCellViewRowRegions` | `skdfref/placement.html` | `dbGetCellViewRowRegions` |
| `dbGetCompTypeSetDefAttr` | `skdfref/placement.html` | `dbGetCompTypeSetDefAttr` |
| `dbGetCompTypeSetDefCompFilters` | `skdfref/placement.html` | `dbGetCompTypeSetDefCompFilters` |
| `dbGetFluidShapeName` | `skdfref/chap2.html` | `dbGetFluidShapeName` |
| `dbGetFluidShapes` | `skdfref/chap2.html` | `dbGetFluidShapes` |
| `dbGetHierColorOverride` | `skdfref/mpt.html` | `dbGetHierColorOverride` |
| `dbGetInPlaceCoverObstructionBloat` | `skdfref/inplacecoverobs.html` | `dbGetInPlaceCoverObstructionBloat` |
| `dbGetInPlaceCoverObstructionBlockageAttributeValue` | `skdfref/inplacecoverobs.html` | `dbGetInPlaceCoverObstructionBlockageAttributeValue` |
| `dbGetInPlaceCoverObstructionBlockageModel` | `skdfref/inplacecoverobs.html` | `dbGetInPlaceCoverObstructionBlockageModel` |
| `dbGetInPlaceCoverObstructionDoughnutHalo` | `skdfref/inplacecoverobs.html` | `dbGetInPlaceCoverObstructionDoughnutHalo` |
| `dbGetInPlaceCoverObstructionLayers` | `skdfref/inplacecoverobs.html` | `dbGetInPlaceCoverObstructionLayers` |
| `dbGetInPlaceCoverObstructionMaxMask` | `skdfref/inplacecoverobs.html` | `dbGetInPlaceCoverObstructionMaxMask` |
| `dbGetInPlaceCoverObstructionMinMask` | `skdfref/inplacecoverobs.html` | `dbGetInPlaceCoverObstructionMinMask` |
| `dbGetInPlaceCoverObstructionNeedsRemodeling` | `skdfref/inplacecoverobs.html` | `dbGetInPlaceCoverObstructionNeedsRemodeling` |
| `dbGetInPlaceCoverObstructionPinRemodeling` | `skdfref/inplacecoverobs.html` | `dbGetInPlaceCoverObstructionPinRemodeling` |
| `dbGetInPlaceCoverObstructionSpacingModel` | `skdfref/inplacecoverobs.html` | `dbGetInPlaceCoverObstructionSpacingModel` |
| `dbGetPatchType` | `skdfref/chap2.html` | `dbGetPatchType` |
| `dbGetPatternRegionCommittedPatternShiftColor` | `skdfref/wsp.html` | `dbGetPatternRegionCommittedPatternShiftColor` |
| `dbGetPhotonicPinFigAngle` | `skdfref/photonic.html` | `dbGetPhotonicPinFigAngle` |
| `dbGetPhotonicPinFigRadius` | `skdfref/photonic.html` | `dbGetPhotonicPinFigRadius` |
| `dbGetPhotonicPinFigWidth` | `skdfref/photonic.html` | `dbGetPhotonicPinFigWidth` |
| `dbGetPlaceAreaBackgroundDef` | `skdfref/placement.html` | `dbGetPlaceAreaBackgroundDef` |
| `dbGetPlaceRowVersion` | `skdfref/placement.html` | `dbGetPlaceRowVersion` |
| `dbGetPowerDomainClusters` | `skdfref/connect.html` | `dbGetPowerDomainClusters"          HTML` |
| `dbGetRailDefAttr` | `skdfref/placement.html` | `dbGetRailDefAttr` |
| `dbGetRailDefFigType` | `skdfref/placement.html` | `dbGetRailDefFigType` |
| `dbGetRouteAuthor` | `skdfref/chap2.html` | `dbGetRouteAuthor` |
| `dbGetRowBackgroundDef` | `skdfref/placement.html` | `dbGetRowBackgroundDef` |
| `dbGetRowRegionAttachedToPRBoundary` | `skdfref/placement.html` | `dbGetRowRegionAttachedToPRBoundary` |
| `dbGetRowRegionPlaceRows` | `skdfref/placement.html` | `dbGetRowRegionPlaceRows` |
| `dbGetRowRegionPoints` | `skdfref/placement.html` | `dbGetRowRegionPoints` |
| `dbGetRowRegionRowRegionSpec` | `skdfref/placement.html` | `dbGetRowRegionRowRegionSpec` |
| `dbGetRowRegionSpecRowRegions` | `skdfref/placement.html` | `dbGetRowRegionSpecRowRegions` |
| `dbGetRowRegionUsesPartialRowSpec` | `skdfref/placement.html` | `dbGetRowRegionUsesPartialRowSpec` |
| `dbGetRowRegionVersion` | `skdfref/placement.html` | `dbGetRowRegionVersion` |
| `dbGetShapeColorLockType                 $skdfref/mpt.html` | `"dbGetShapeColorLockType"` | `HTML` |
| `dbGetShapeEffectiveColorLockType        $skdfref/mpt.html` | `"dbGetShapeEffectiveColorLockType"` | `HTML` |
| `dbGetShapeTrimFillType` | `skdfref/chap2.html` | `dbGetShapeTrimFillType` |
| `dbGetShapeTrimFillType` | `skdfref/chap2.html` | `dbGetShapeTrimFillType` |
| `dbGetViaLayer` | `skdfref/chap2.html` | `dbGetViaLayer` |
| `dbGetViaLayerColorLockType              $skdfref/mpt.html` | `"dbGetViaLayerColorLockType"` | `HTML` |
| `dbGetViaLayerControl` | `skdfref/mpt.html` | `dbGetViaLayerControl` |
| `dbGetViaLayerNumColorMasks` | `skdfref/mpt.html` | `dbGetViaLayerNumColorMasks` |
| `dbGetq` | `skdfref/attrib.html` | `dbGetq` |
| `dbHasAutoSavedFile` | `skdfref/cvio.html` | `dbHasAutoSavedFile` |
| `dbHasPanicFile` | `skdfref/cvio.html` | `dbHasPanicFile` |
| `dbInPlaceCoverObstructionExists` | `skdfref/inplacecoverobs.html` | `dbInPlaceCoverObstructionExists` |
| `dbInstGetLayerShifts2` | `skdfref/mpt.html` | `dbInstGetLayerShifts2` |
| `dbInstSetLayerShifts2` | `skdfref/mpt.html` | `dbInstSetLayerShifts2` |
| `dbIsCellViewPhysicalOnly` | `skdfref/connect.html` | `dbIsCellViewPhysicalOnly` |
| `dbIsFluidPcell` | `skpcellref/xpcellFunctions.html` | `dbIsFluidPcell` |
| `dbIsFluidPcell` | `skdfref/chap2.html` | `dbIsFluidPcell` |
| `dbIsFluidShape` | `skdfref/chap2.html` | `dbIsFluidShape ` |
| `dbIsImplicit` | `skdfref/placement.html` | `dbIsImplicit` |
| `dbIsInRowRegion` | `skdfref/placement.html` | `dbIsInRowRegion` |
| `dbIsInstTransparent                 $skdfref/instance.html` | `"dbIsInstTransparent"` | `HTML` |
| `dbIsMultiTechEnabled` | `skdfref/vrf.html` | `dbIsMultiTechEnabled` |
| `dbIsNetOptical` | `skdfref/chap2.html` | `dbIsNetOptical` |
| `dbIsRowRegion` | `skdfref/placement.html` | `dbIsRowRegion` |
| `dbIsRowRegionAttachedToPRBoundary` | `skdfref/placement.html` | `dbIsRowRegionAttachedToPRBoundary` |
| `dbIsVRFInfraEnabled` | `skdfref/vrf.html` | `dbIsVRFInfraEnabled"               HTML` |
| `dbIsViaColorStateLayerLocked` | `skdfref/mpt.html` | `dbIsViaColorStateLayerLocked` |
| `dbOpenParamCellView` | `skdfref/cvio.html` | `dbOpenParamCellView` |
| `dbRebuildRowRegion` | `skdfref/placement.html` | `dbRebuildRowRegion` |
| `dbRemovePlaceAreaBackgroundDef` | `skdfref/placement.html` | `dbRemovePlaceAreaBackgroundDef` |
| `dbRemoveRowBackgroundDef` | `skdfref/placement.html` | `dbRemoveRowBackgroundDef` |
| `dbRestoreAndOpenAutoSavedFile` | `skdfref/cvio.html` | `dbRestoreAndOpenAutoSavedFile` |
| `dbRestoreAndOpenPanicFile` | `skdfref/cvio.html` | `dbRestoreAndOpenPanicFile` |
| `dbRowRegionMatchesSpec` | `skdfref/placement.html` | `dbRowRegionMatchesSpec` |
| `dbRowRegionPointsCutOut` | `skdfref/placement.html             "dbRowRegionPointsCutOut"` | `HTML` |
| `dbSavePcellCache` | `skpcellref/xpcellFunctions.html` | `dbSavePcellCache` |
| `dbSavePcellCacheForCV` | `skpcellref/xpcellFunctions.html` | `dbSavePcellCacheForCV` |
| `dbSavePcellCacheForCVOnly` | `skpcellref/xpcellFunctions.html` | `dbSavePcellCacheForCVOnly` |
| `dbSet` | `skdfref/attrib.html` | `dbSet` |
| `dbSetBeginPatch` | `skdfref/chap2.html` | `dbSetBeginPatch` |
| `dbSetCellViewEquivalentConnectivityTime` | `skdfref/connect.html` | `dbSetCellViewEquivalentConnectivityTime` |
| `dbSetCompTypeSetDefCompFilters` | `skdfref/placement.html` | `dbSetCompTypeSetDefCompFilters` |
| `dbSetEndPatch` | `skdfref/chap2.html` | `dbSetEndPatch` |
| `dbSetFluidShape` | `skdfref/chap2.html` | `dbSetFluidShape` |
| `dbSetFullPatch` | `skdfref/chap2.html` | `dbSetFullPatch` |
| `dbSetGlobalGridDefaultRepeatMode` | `skdfref/wsp.html` | `dbSetGlobalGridDefaultRepeatMode` |
| `dbSetGlobalGridRepeatMode` | `skdfref/wsp.html` | `dbSetGlobalGridRepeatMode` |
| `dbSetInPlaceCoverObstructionBloat` | `skdfref/inplacecoverobs.html` | `dbSetInPlaceCoverObstructionBloat` |
| `dbSetInPlaceCoverObstructionBlockageAttributeValue` | `skdfref/inplacecoverobs.html` | `dbSetInPlaceCoverObstructionBlockageAttributeValue` |
| `dbSetInPlaceCoverObstructionBlockageModel` | `skdfref/inplacecoverobs.html` | `dbSetInPlaceCoverObstructionBlockageModel` |
| `dbSetInPlaceCoverObstructionDoughnutHalo` | `skdfref/inplacecoverobs.html` | `dbSetInPlaceCoverObstructionDoughnutHalo` |
| `dbSetInPlaceCoverObstructionNeedsRemodeling` | `skdfref/inplacecoverobs.html` | `dbSetInPlaceCoverObstructionNeedsRemodeling` |
| `dbSetInPlaceCoverObstructionPinRemodeling` | `skdfref/inplacecoverobs.html` | `dbSetInPlaceCoverObstructionPinRemodeling` |
| `dbSetInPlaceCoverObstructionSpacingModel` | `skdfref/inplacecoverobs.html` | `dbSetInPlaceCoverObstructionSpacingModel` |
| `dbSetInstTransparent                $skdfref/instance.html` | `"dbSetInstTransparent"` | `HTML` |
| `dbSetOccShapeColorLockType              $skdfref/mpt.html` | `"dbSetOccShapeColorLockType"` | `HTML` |
| `dbSetPatchType` | `skdfref/chap2.html` | `dbSetPatchType` |
| `dbSetPatternRegionShiftColor` | `skdfref/wsp.html` | `dbSetPatternRegionShiftColor` |
| `dbSetPhotonicPinFigAngle` | `skdfref/photonic.html` | `dbSetPhotonicPinFigAngle` |
| `dbSetPhotonicPinFigRadius` | `skdfref/photonic.html` | `dbSetPhotonicPinFigRadius` |
| `dbSetPhotonicPinFigWidth` | `skdfref/photonic.html` | `dbSetPhotonicPinFigWidth` |
| `dbSetRailDefFigType` | `skdfref/placement.html` | `dbSetRailDefFigType` |
| `dbSetRouteAuthor` | `skdfref/chap2.html` | `dbSetRouteAuthor` |
| `dbSetRowRegionPoints` | `skdfref/placement.html` | `dbSetRowRegionPoints` |
| `dbSetRowRegionRowRegionSpec` | `skdfref/placement.html` | `dbSetRowRegionRowRegionSpec` |
| `dbSetRowRegionUsesPartialRowSpec` | `skdfref/placement.html` | `dbSetRowRegionUsesPartialRowSpec` |
| `dbSetShapeColorLockType                 $skdfref/mpt.html` | `"dbSetShapeColorLockType"` | `HTML` |
| `dbSetViaColorInfo` | `skdfref/mpt.html` | `dbSetViaColorInfo` |
| `dbSetViaColorStateLayerLocked` | `skdfref/mpt.html` | `dbSetViaColorStateLayerLocked` |
| `dbSetViaLayerColorLockType              $skdfref/mpt.html` | `"dbSetViaLayerColorLockType"` | `HTML` |
| `dbSetViaLayerControl` | `skdfref/mpt.html` | `dbSetViaLayerControl` |
| `dbSetq` | `skdfref/attrib.html` | `dbSetq` |
| `dbStartGenAnyInstToInstTerm` | `skdfref/generator.html` | `dbStartGenAnyInstToInstTerm` |
| `dbStartGenInstHeader` | `skdfref/generator.html` | `dbStartGenInstHeader` |
| `dbStartGenInstHeaderToAnyInst` | `skdfref/generator.html` | `dbStartGenInstHeaderToAnyInst` |
| `dbStartGenLPPHeaderToShape` | `skdfref/generator.html` | `dbStartGenLPPHeaderToShape` |
| `dbStartGenLPToShape` | `skdfref/generator.html` | `dbStartGenLPToShape` |
| `dbStartGenMarker` | `skdfref/generator.html` | `dbStartGenMarker` |
| `dbStartGenNet` | `skdfref/generator.html` | `dbStartGenNet` |
| `dbStartGenNetToInstTerm` | `skdfref/generator.html` | `dbStartGenNetToInstTerm` |
| `dbStartGenNetToRoute` | `skdfref/generator.html` | `dbStartGenNetToRoute` |
| `dbStartGenRoute` | `skdfref/generator.html` | `dbStartGenRoute` |
| `dbStartGenShape` | `skdfref/generator.html` | `dbStartGenShape` |
| `dbStartGenTerm` | `skdfref/generator.html` | `dbStartGenTerm` |
| `dbStartGenViaHeader` | `skdfref/generator.html` | `dbStartGenViaHeader` |
| `dbStartGenViaHeaderToVia` | `skdfref/generator.html` | `dbStartGenViaHeaderToVia` |
| `dbStopGen` | `skdfref/generator.html` | `dbStopGen` |
| `dbUnabutGroup` | `skdfref/chap2.html` | `dbUnabutGroup"                     HTML` |
| `dbUnsetCellViewEquivalentConnectivityTime` | `skdfref/connect.html` | `dbUnsetCellViewEquivalentConnectivityTime` |
| `dbUnsetCellViewPhysicalOnly` | `skdfref/connect.html` | `dbUnsetCellViewPhysicalOnly` |
| `dbUnsetCompTypeSetDefCompFilters` | `skdfref/placement.html` | `dbUnsetCompTypeSetDefCompFilters` |
| `dbUnsetPhotonicPinFigAngle` | `skdfref/photonic.html` | `dbUnsetPhotonicPinFigAngle` |
| `dbUnsetPhotonicPinFigRadius` | `skdfref/photonic.html` | `dbUnsetPhotonicPinFigRadius` |
| `dbUnsetPhotonicPinFigWidth` | `skdfref/photonic.html` | `dbUnsetPhotonicPinFigWidth` |
| `dbUpdatePcellCache` | `skpcellref/xpcellFunctions.html` | `dbUpdatePcellCache` |
| `dbm_OCEAN` | `oceanref/chap10.html` | `dbm` |


### AWV API

**152 个函数**，文档位置：

- `vivaxlskill/chap2.html` (142 个函数)
- `vivaxlskill/chap3.html` (6 个函数)
- `oceanref/chap10.html` (3 个函数)
- `vivaxlskill/chap2.html     "awvGetSelectedTraceWaveforms"` (1 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `awvAddSubwindow_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvAddSubwindow` |
| `awvAnalog2Digital_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvAnalog2Digital` |
| `awvAppendExpression_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvAppendExpression` |
| `awvAppendList_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvAppendList` |
| `awvAppendWaveform_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvAppendWaveform` |
| `awvClearPlotWindow_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvClearPlotWindow` |
| `awvClearSubwindowHistory_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvClearSubwindowHistory` |
| `awvClearWindowHistory_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvClearWindowHistory` |
| `awvCloseCalculator_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvCloseCalculator` |
| `awvCloseWindowMenuCB_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvCloseWindowMenuCB` |
| `awvCloseWindow_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvCloseWindow` |
| `awvCreateBusFromWaveList_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvCreateBusFromWaveList` |
| `awvCreateBus_OCEAN` | `oceanref/chap10.html` | `awvCreateBus` |
| `awvCreateBus_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvCreateBus` |
| `awvCreatePlotWindow_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvCreatePlotWindow` |
| `awvDeleteAllWaveforms_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvDeleteAllWaveforms` |
| `awvDeleteMarker_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvDeleteMarker` |
| `awvDeleteSubwindow_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvDeleteSubwindow` |
| `awvDeleteWaveform_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvDeleteWaveform` |
| `awvDigital2Analog_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvDigital2Analog` |
| `awvDisableRedraw_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvDisableRedraw` |
| `awvDisplayDate_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvDisplayDate` |
| `awvDisplayGrid_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvDisplayGrid` |
| `awvDisplaySubwindowTitle_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvDisplaySubwindowTitle` |
| `awvDisplayTitle_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvDisplayTitle` |
| `awvEraseWindowMenuCB_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvEraseWindowMenuCB` |
| `awvEval_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvEval` |
| `awvExitWindowFunctionAdd_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvExitWindowFunctionAdd` |
| `awvExitWindowFunctionDel_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvExitWindowFunctionDel` |
| `awvExitWindowFunctionGet_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvExitWindowFunctionGet` |
| `awvEyeCross_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvEyeCross"                   HTML` |
| `awvGetAssertName_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvGetAssertName` |
| `awvGetCurrentSubwindow_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvGetCurrentSubwindow` |
| `awvGetCurrentWindow_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvGetCurrentWindow` |
| `awvGetDisplayMode_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvGetDisplayMode` |
| `awvGetDrawStatus_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvGetDrawStatus` |
| `awvGetHiWindow_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvGetHiWindow` |
| `awvGetInitializationTimeout_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvGetInitializationTimeout"   HTML` |
| `awvGetOnSubwindowList_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvGetOnSubwindowList` |
| `awvGetPlotStyle_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvGetPlotStyle` |
| `awvGetSavePromptNeeded_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvGetSavePromptNeeded` |
| `awvGetScalarFromWave_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvGetScalarFromWave` |
| `awvGetSelectedTraceWaveforms_ViVA_SKILL` | `vivaxlskill/chap2.html     "awvGetSelectedTraceWaveforms"` | `HTML` |
| `awvGetSmithModeType_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvGetSmithModeType` |
| `awvGetSubwindowList_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvGetSubwindowList` |
| `awvGetSubwindowTitle_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvGetSubwindowTitle` |
| `awvGetUnusedEntityList_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvGetUnusedEntityList` |
| `awvGetWaveNameList_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvGetWaveNameList` |
| `awvGetWindowList_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvGetWindowList` |
| `awvGetWindowTitle_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvGetWindowTitle` |
| `awvGetXAxisLabel_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvGetXAxisLabel` |
| `awvGetXAxisMajorDivisions_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvGetXAxisMajorDivisions` |
| `awvGetXAxisMinorDivisions_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvGetXAxisMinorDivisions` |
| `awvGetXAxisStepValue_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvGetXAxisStepValue` |
| `awvGetXAxisUseStepValue_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvGetXAxisUseStepValue` |
| `awvGetXMarkerNames_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvGetXMarkerNames` |
| `awvGetYAxisLabel_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvGetYAxisLabel` |
| `awvGetYAxisMajorDivisions_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvGetYAxisMajorDivisions` |
| `awvGetYAxisMinorDivisions_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvGetYAxisMinorDivisions` |
| `awvGetYAxisStepValue_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvGetYAxisStepValue` |
| `awvGetYAxisUseStepValue_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvGetYAxisUseStepValue` |
| `awvGetYMarkerNames_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvGetYMarkerNames` |
| `awvInitWindowFunctionAdd_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvInitWindowFunctionAdd` |
| `awvInitWindowFunctionDel_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvInitWindowFunctionDel` |
| `awvInitWindowFunctionGet_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvInitWindowFunctionGet` |
| `awvIsPlotWindow_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvIsPlotWindow` |
| `awvLoadCustomCalcFunction_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvLoadCustomCalcFunction` |
| `awvLoadEyeMask_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvLoadEyeMask` |
| `awvLoadMenuCB_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvLoadMenuCB` |
| `awvLoadSharedCustomFunctionsFile_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvLoadSharedCustomFunctionsFile` |
| `awvLoadWindow_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvLoadWindow` |
| `awvLogXAxis_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvLogXAxis` |
| `awvLogYAxis_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvLogYAxis` |
| `awvPlaceAMarker_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvPlaceAMarker"               HTML` |
| `awvPlaceBMarker_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvPlaceBMarker"               HTML` |
| `awvPlaceBookMark_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvPlaceBookMark` |
| `awvPlaceBookmark_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvPlaceBookMark` |
| `awvPlaceWaveformLabel_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvPlaceWaveformLabel` |
| `awvPlaceWindowLabel_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvPlaceWindowLabel` |
| `awvPlaceXMarker_OCEAN` | `oceanref/chap10.html` | `awvPlaceXMarker` |
| `awvPlaceXMarker_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvPlaceXMarker` |
| `awvPlaceYMarker_OCEAN` | `oceanref/chap10.html` | `awvPlaceYMarker` |
| `awvPlaceYMarker_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvPlaceYMarker` |
| `awvPlotExpression_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvPlotExpression` |
| `awvPlotList_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvPlotList` |
| `awvPlotSignals_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvPlotSignals` |
| `awvPlotSimpleExpression_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvPlotSimpleExpression` |
| `awvPlotWaveformOption_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvPlotWaveformOption` |
| `awvPlotWaveform_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvPlotWaveform` |
| `awvPrintWaveform_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvPrintWaveform` |
| `awvRedisplaySubwindow_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvRedisplaySubwindow` |
| `awvRedisplayWindow_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvRedisplayWindow` |
| `awvRedrawWindowMenuCB_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvRedrawWindowMenuCB` |
| `awvRemoveDate_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvRemoveDate` |
| `awvRemoveLabel_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvRemoveLabel` |
| `awvRemoveSubwindowTitle_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvRemoveSubwindowTitle` |
| `awvRemoveTitle_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvRemoveTitle` |
| `awvResetAllWindows_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvResetAllWindows` |
| `awvResetWindow_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvResetWindow` |
| `awvResumeViVA_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvResumeViVA` |
| `awvRfLoadPull_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvRfLoadPull` |
| `awvSaveMenuCB_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvSaveMenuCB` |
| `awvSaveToCSV_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvSaveToCSV` |
| `awvSaveWindowImage_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvSaveWindowImage` |
| `awvSaveWindow_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvSaveWindow` |
| `awvSetCurrentSubwindow_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvSetCurrentSubwindow` |
| `awvSetCurrentWindow_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvSetCurrentWindow` |
| `awvSetCursorPrompts_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvSetCursorPrompts` |
| `awvSetDisplayMode_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvSetDisplayMode` |
| `awvSetDisplayStatus_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvSetDisplayStatus` |
| `awvSetInitializationTimeout_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvSetInitializationTimeout"   HTML` |
| `awvSetLegendWidth_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvSetLegendWidth"             HTML` |
| `awvSetOptionDefault_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvSetOptionDefault` |
| `awvSetOptionValue_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvSetOptionValue` |
| `awvSetOrigin_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvSetOrigin` |
| `awvSetPlotStyle_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvSetPlotStyle` |
| `awvSetSavePromptNeeded_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvSetSavePromptNeeded` |
| `awvSetSmithModeType_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvSetSmithModeType` |
| `awvSetSmithXLimit_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvSetSmithXLimit` |
| `awvSetSmithYLimit_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvSetSmithYLimit` |
| `awvSetUpdateStatus_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvSetUpdateStatus` |
| `awvSetWaveNameList_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvSetWaveNameList` |
| `awvSetWaveformDisplayStatus_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvSetWaveformDisplayStatus"   HTML` |
| `awvSetXAxisLabel_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvSetXAxisLabel` |
| `awvSetXAxisMajorDivisions_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvSetXAxisMajorDivisions` |
| `awvSetXAxisMinorDivisions_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvSetXAxisMinorDivisions` |
| `awvSetXAxisStepValue_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvSetXAxisStepValue` |
| `awvSetXAxisUseStepValue_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvSetXAxisUseStepValue` |
| `awvSetXLimit_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvSetXLimit` |
| `awvSetXScale_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvSetXScale` |
| `awvSetYAxisLabel_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvSetYAxisLabel` |
| `awvSetYAxisMajorDivisions_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvSetYAxisMajorDivisions` |
| `awvSetYAxisMinorDivisions_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvSetYAxisMinorDivisions` |
| `awvSetYAxisStepValue_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvSetYAxisStepValue` |
| `awvSetYAxisUseStepValue_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvSetYAxisUseStepValue` |
| `awvSetYLimit_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvSetYLimit` |
| `awvSetYRange_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvSetYRange` |
| `awvSimplePlotExpression_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvSimplePlotExpression` |
| `awvSmithAxisMenuCB_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvSmithAxisMenuCB` |
| `awvTableSignals_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvTableSignals` |
| `awvUpdateAllWindows_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvUpdateAllWindows` |
| `awvUpdateWindow_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvUpdateWindow` |
| `awvZoomFit_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvZoomFit` |
| `awvZoomGraphXY_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvZoomGraphXY` |
| `awvZoomGraphX_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvZoomGraphX` |
| `awvZoomGraphY_ViVA_SKILL` | `vivaxlskill/chap2.html` | `awvZoomGraphY` |
| `awviEditMenuCB_ViVA_SKILL` | `vivaxlskill/chap3.html` | `awviEditMenuCB` |
| `awviMakeActiveMenuCB_ViVA_SKILL` | `vivaxlskill/chap3.html` | `awviMakeActiveMenuCB` |
| `awviPLoadMenuCB_ViVA_SKILL` | `vivaxlskill/chap3.html` | `awviPLoadMenuCB` |
| `awviPSaveMenuCB_ViVA_SKILL` | `vivaxlskill/chap3.html` | `awviPSaveMenuCB` |
| `awviPUpdateMenuCB_ViVA_SKILL` | `vivaxlskill/chap3.html` | `awviPUpdateMenuCB` |
| `awviShowOutputMenuCB_ViVA_SKILL` | `vivaxlskill/chap3.html` | `awviShowOutputMenuCB` |


### PC API

**135 个函数**，文档位置：

- `skpcellref/graphicalFunctions.html` (121 个函数)
- `skpcellref/skillPcellFunctions.html` (4 个函数)
- `sklangref/stringfunc.html` (3 个函数)
- `"pcHIDefineInheritedParameter"` (1 个函数)
- `"pcHIDefineParameterizedShape"` (1 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `pcColinearPoints` | `skpcellref/graphicalFunctions.html` | `pcColinearPoints` |
| `pcConcatOrient` | `skpcellref/graphicalFunctions.html` | `pcConcatOrient` |
| `pcDefineCondition` | `skpcellref/graphicalFunctions.html` | `pcDefineCondition` |
| `pcDefineInheritParam` | `skpcellref/graphicalFunctions.html` | `pcDefineInheritParam` |
| `pcDefinePCell` | `skpcellref/graphicalFunctions.html` | `pcDefinePCell` |
| `pcDefinePPCell` | `skpcellref/graphicalFunctions.html` | `pcDefinePPCell` |
| `pcDefineParamCell` | `skpcellref/graphicalFunctions.html` | `pcDefineParamCell` |
| `pcDefineParamLabel` | `skpcellref/graphicalFunctions.html` | `pcDefineParamLabel` |
| `pcDefineParamLayer` | `skpcellref/graphicalFunctions.html` | `pcDefineParamLayer` |
| `pcDefineParamPath` | `skpcellref/graphicalFunctions.html` | `pcDefineParamPath` |
| `pcDefineParamPolygon` | `skpcellref/graphicalFunctions.html` | `pcDefineParamPolygon` |
| `pcDefineParamProp` | `skpcellref/graphicalFunctions.html` | `pcDefineParamProp` |
| `pcDefineParamRect` | `skpcellref/graphicalFunctions.html` | `pcDefineParamRect` |
| `pcDefineParamRefPointObject` | `skpcellref/graphicalFunctions.html` | `pcDefineParamRefPointObject` |
| `pcDefineParamSlot` | `skpcellref/graphicalFunctions.html` | `pcDefineParamSlot` |
| `pcDefinePathRefPointObject` | `skpcellref/graphicalFunctions.html` | `pcDefinePathRefPointObject` |
| `pcDefineRepeat` | `skpcellref/graphicalFunctions.html` | `pcDefineRepeat` |
| `pcDefineSteppedObject` | `skpcellref/graphicalFunctions.html` | `pcDefineSteppedObject` |
| `pcDefineStretchLine` | `skpcellref/graphicalFunctions.html` | `pcDefineStretchLine` |
| `pcDeleteCondition` | `skpcellref/graphicalFunctions.html` | `pcDeleteCondition` |
| `pcDeleteParam` | `skpcellref/graphicalFunctions.html` | `pcDeleteParam` |
| `pcDeleteParamLayer` | `skpcellref/graphicalFunctions.html` | `pcDeleteParamLayer` |
| `pcDeleteParamProp` | `skpcellref/graphicalFunctions.html` | `pcDeleteParamProp` |
| `pcDeleteParamShape` | `skpcellref/graphicalFunctions.html` | `pcDeleteParamShape` |
| `pcDeleteRefPoint` | `skpcellref/graphicalFunctions.html` | `pcDeleteRefPoint` |
| `pcDeleteRepeat` | `skpcellref/graphicalFunctions.html` | `pcDeleteRepeat` |
| `pcDeleteSteppedObject` | `skpcellref/graphicalFunctions.html` | `pcDeleteSteppedObject` |
| `pcDraw` | `skpcellref/graphicalFunctions.html` | `pcDraw` |
| `pcExprToProp` | `skpcellref/graphicalFunctions.html` | `pcExprToProp` |
| `pcExprToString` | `skpcellref/skillPcellFunctions.html` | `pcExprToString` |
| `pcFilterPoints` | `skpcellref/graphicalFunctions.html` | `pcFilterPoints` |
| `pcFix` | `skpcellref/graphicalFunctions.html` | `pcFix` |
| `pcGetBendAngle` | `skpcellref/graphicalFunctions.html` | `pcGetBendAngle` |
| `pcGetCodeParamNames` | `skpcellref/graphicalFunctions.html` | `pcGetCodeParamNames` |
| `pcGetCodeParamValue` | `skpcellref/graphicalFunctions.html` | `pcGetCodeParamValue` |
| `pcGetConditions` | `skpcellref/graphicalFunctions.html` | `pcGetConditions` |
| `pcGetDefaultParamsFromClass` | `skpcellref/graphicalFunctions.html` | `pcGetDefaultParamsFromClass` |
| `pcGetInheritParamDefn` | `skpcellref/graphicalFunctions.html` | `pcGetInheritParamDefn` |
| `pcGetInheritParams` | `skpcellref/graphicalFunctions.html` | `pcGetInheritParams` |
| `pcGetOffsetPath` | `skpcellref/graphicalFunctions.html` | `pcGetOffsetPath` |
| `pcGetOffsetPolygon` | `skpcellref/graphicalFunctions.html` | `pcGetOffsetPolygon` |
| `pcGetParamLabelDefn` | `skpcellref/graphicalFunctions.html` | `pcGetParamLabelDefn` |
| `pcGetParamLabels` | `skpcellref/graphicalFunctions.html` | `pcGetParamLabels` |
| `pcGetParamLayerDefn` | `skpcellref/graphicalFunctions.html` | `pcGetParamLayerDefn` |
| `pcGetParamLayers` | `skpcellref/graphicalFunctions.html` | `pcGetParamLayers` |
| `pcGetParamProps` | `skpcellref/graphicalFunctions.html` | `pcGetParamProps` |
| `pcGetParamShapeDefn` | `skpcellref/graphicalFunctions.html` | `pcGetParamShapeDefn` |
| `pcGetParamShapes` | `skpcellref/graphicalFunctions.html` | `pcGetParamShapes` |
| `pcGetParamSlotType` | `skpcellref/graphicalFunctions.html` | `pcGetParamSlotType` |
| `pcGetParamSlotValue` | `skpcellref/graphicalFunctions.html` | `pcGetParamSlotValue` |
| `pcGetParameters` | `skpcellref/graphicalFunctions.html` | `pcGetParameters` |
| `pcGetPathRefPoint` | `skpcellref/graphicalFunctions.html` | `pcGetPathRefPoint` |
| `pcGetRefPointDefn` | `skpcellref/graphicalFunctions.html` | `pcGetRefPointDefn` |
| `pcGetRefPoints` | `skpcellref/graphicalFunctions.html` | `pcGetRefPoints` |
| `pcGetRepeatDefn` | `skpcellref/graphicalFunctions.html` | `pcGetRepeatDefn` |
| `pcGetRepeats` | `skpcellref/graphicalFunctions.html` | `pcGetRepeats` |
| `pcGetStepDirection` | `skpcellref/graphicalFunctions.html` | `pcGetStepDirection` |
| `pcGetSteppedObjectDefn` | `skpcellref/graphicalFunctions.html` | `pcGetSteppedObjectDefn` |
| `pcGetSteppedObjects` | `skpcellref/graphicalFunctions.html` | `pcGetSteppedObjects` |
| `pcGetStretchDefn` | `skpcellref/graphicalFunctions.html` | `pcGetStretchDefn` |
| `pcGetStretchSummary` | `skpcellref/graphicalFunctions.html` | `pcGetStretchSummary` |
| `pcGetStretches` | `skpcellref/graphicalFunctions.html` | `pcGetStretches` |
| `pcGrowBox` | `skpcellref/graphicalFunctions.html` | `pcGrowBox` |
| `pcGrowPoints` | `skpcellref/graphicalFunctions.html` | `pcGrowPoints` |
| `pcHICompileToSkill` | `skpcellref/graphicalFunctions.html` | `pcHICompileToSkill` |
| `pcHIDefineCondition` | `skpcellref/graphicalFunctions.html` | `pcHIDefineCondition` |
| `pcHIDefineInheritedParameter    $skpcellref/graphicalFunctions.html` | `"pcHIDefineInheritedParameter"` | `HTML` |
| `pcHIDefineLabel` | `skpcellref/graphicalFunctions.html` | `pcHIDefineLabel` |
| `pcHIDefineLayer` | `skpcellref/graphicalFunctions.html` | `pcHIDefineLayer` |
| `pcHIDefineParamCell` | `skpcellref/graphicalFunctions.html` | `pcHIDefineParamCell` |
| `pcHIDefineParamRefPointObject   $skpcellref/graphicalFunctions.html` | `"pcHIDefineParamRefPointObject"` | `HTML` |
| `pcHIDefineParameterizedShape    $skpcellref/graphicalFunctions.html` | `"pcHIDefineParameterizedShape"` | `HTML` |
| `pcHIDefinePathRefPointObject    $skpcellref/graphicalFunctions.html` | `"pcHIDefinePathRefPointObject"` | `HTML` |
| `pcHIDefineProp` | `skpcellref/graphicalFunctions.html` | `pcHIDefineProp` |
| `pcHIDefineRepeat` | `skpcellref/graphicalFunctions.html` | `pcHIDefineRepeat` |
| `pcHIDefineSteppedObject` | `skpcellref/graphicalFunctions.html` | `pcHIDefineSteppedObject` |
| `pcHIDefineStretch` | `skpcellref/graphicalFunctions.html` | `pcHIDefineStretch` |
| `pcHIDeleteCondition` | `skpcellref/graphicalFunctions.html` | `pcHIDeleteCondition` |
| `pcHIDeleteLayer` | `skpcellref/graphicalFunctions.html` | `pcHIDeleteLayer` |
| `pcHIDeleteParameterizedShape    $skpcellref/graphicalFunctions.html` | `"pcHIDeleteParameterizedShape"` | `HTML` |
| `pcHIDeleteProp` | `skpcellref/graphicalFunctions.html` | `pcHIDeleteProp` |
| `pcHIDeleteRefPointObject` | `skpcellref/graphicalFunctions.html` | `pcHIDeleteRefPointObject` |
| `pcHIDeleteRepeat` | `skpcellref/graphicalFunctions.html` | `pcHIDeleteRepeat` |
| `pcHIDeleteSteppedObject` | `skpcellref/graphicalFunctions.html` | `pcHIDeleteSteppedObject` |
| `pcHIDisplayCondition` | `skpcellref/graphicalFunctions.html` | `pcHIDisplayCondition` |
| `pcHIDisplayInheritedParameter   $skpcellref/graphicalFunctions.html` | `"pcHIDisplayInheritedParameter"` | `HTML` |
| `pcHIDisplayLayer` | `skpcellref/graphicalFunctions.html` | `pcHIDisplayLayer` |
| `pcHIDisplayParameterizedShape   $skpcellref/graphicalFunctions.html` | `"pcHIDisplayParameterizedShape"` | `HTML` |
| `pcHIDisplayParams` | `skpcellref/graphicalFunctions.html` | `pcHIDisplayParams` |
| `pcHIDisplayProp` | `skpcellref/graphicalFunctions.html` | `pcHIDisplayProp` |
| `pcHIDisplayRefPointObject` | `skpcellref/graphicalFunctions.html` | `pcHIDisplayRefPointObject` |
| `pcHIDisplayRepeat` | `skpcellref/graphicalFunctions.html` | `pcHIDisplayRepeat` |
| `pcHIDisplaySteppedObject` | `skpcellref/graphicalFunctions.html` | `pcHIDisplaySteppedObject` |
| `pcHIEditParameters` | `skpcellref/graphicalFunctions.html` | `pcHIEditParameters` |
| `pcHIModifyCondition` | `skpcellref/graphicalFunctions.html` | `pcHIModifyCondition` |
| `pcHIModifyLabel` | `skpcellref/graphicalFunctions.html` | `pcHIModifyLabel` |
| `pcHIModifyLayer` | `skpcellref/graphicalFunctions.html` | `pcHIModifyLayer` |
| `pcHIModifyParams` | `skpcellref/graphicalFunctions.html` | `pcHIModifyParams` |
| `pcHIModifyRefPointObject` | `skpcellref/graphicalFunctions.html` | `pcHIModifyRefPointObject` |
| `pcHIModifyRepeat` | `skpcellref/graphicalFunctions.html` | `pcHIModifyRepeat` |
| `pcHIModifySteppedObject` | `skpcellref/graphicalFunctions.html` | `pcHIModifySteppedObject` |
| `pcHIModifyStretchLine` | `skpcellref/graphicalFunctions.html` | `pcHIModifyStretchLine` |
| `pcHIQualifyStretchLine` | `skpcellref/graphicalFunctions.html` | `pcHIQualifyStretchLine` |
| `pcHIRedefineStretchLine` | `skpcellref/graphicalFunctions.html` | `pcHIRedefineStretchLine` |
| `pcHISummarizeParams` | `skpcellref/graphicalFunctions.html` | `pcHISummarizeParams` |
| `pcIsParamSlot` | `skpcellref/graphicalFunctions.html` | `pcIsParamSlot` |
| `pcModifyParam` | `skpcellref/graphicalFunctions.html` | `pcModifyParam` |
| `pcRedefineStretchLine` | `skpcellref/graphicalFunctions.html` | `pcRedefineStretchLine` |
| `pcRestrictStretchToObjects` | `skpcellref/graphicalFunctions.html` | `pcRestrictStretchToObjects` |
| `pcRound` | `skpcellref/graphicalFunctions.html` | `pcRound` |
| `pcSetFTermWidth` | `skpcellref/graphicalFunctions.html` | `pcSetFTermWidth` |
| `pcSetParamSlotValue` | `skpcellref/graphicalFunctions.html` | `pcSetParamSlotValue` |
| `pcSetParamSlotsFromMaster` | `skpcellref/graphicalFunctions.html` | `pcSetParamSlotsFromMaster` |
| `pcSkillGen` | `skpcellref/graphicalFunctions.html` | `pcSkillGen` |
| `pcStepAlongShape` | `skpcellref/graphicalFunctions.html` | `pcStepAlongShape` |
| `pcTechFile` | `skpcellref/skillPcellFunctions.html` | `pcTechFile` |
| `pcUserAdjustParameters` | `skpcellref/graphicalFunctions.html` | `pcUserAdjustParameters` |
| `pcUserGenerateArray` | `skpcellref/graphicalFunctions.html` | `pcUserGenerateArray` |
| `pcUserGenerateInstance` | `skpcellref/graphicalFunctions.html` | `pcUserGenerateInstance` |
| `pcUserGenerateInstancesOfMaster` | `skpcellref/graphicalFunctions.html` | `pcUserGenerateInstancesOfMaster"   HTML` |
| `pcUserGenerateLPP` | `skpcellref/graphicalFunctions.html` | `pcUserGenerateLPP` |
| `pcUserGeneratePin` | `skpcellref/graphicalFunctions.html` | `pcUserGeneratePin` |
| `pcUserGenerateProperty` | `skpcellref/graphicalFunctions.html` | `pcUserGenerateProperty` |
| `pcUserGenerateShape` | `skpcellref/graphicalFunctions.html` | `pcUserGenerateShape` |
| `pcUserGenerateTerminal` | `skpcellref/graphicalFunctions.html` | `pcUserGenerateTerminal` |
| `pcUserInitRepeat` | `skpcellref/graphicalFunctions.html` | `pcUserInitRepeat` |
| `pcUserPostProcessCellView` | `skpcellref/graphicalFunctions.html` | `pcUserPostProcessCellView` |
| `pcUserPostProcessObject` | `skpcellref/graphicalFunctions.html` | `pcUserPostProcessObject` |
| `pcUserPreProcessCellView` | `skpcellref/graphicalFunctions.html` | `pcUserPreProcessCellView` |
| `pcUserSetTermNetName` | `skpcellref/graphicalFunctions.html` | `pcUserSetTermNetName` |
| `pcfix` | `skpcellref/skillPcellFunctions.html` | `pcfix` |
| `pcreGetRecursionLimit` | `sklangref/stringfunc.html` | `pcreGetRecursionLimit` |
| `pcreSetRecursionLimit` | `sklangref/stringfunc.html` | `pcreSetRecursionLimit` |
| `pcreSubpatCount` | `sklangref/stringfunc.html` | `pcreSubpatCount` |
| `pcround` | `skpcellref/skillPcellFunctions.html` | `pcround` |


### OCNXL API

**132 个函数**，文档位置：

- `ocnxl/ocnxlcommands.html` (130 个函数)
- `"ocnxlSetAllVariablePSetsDisabled"` (1 个函数)
- `"ocnxlSetAllParameterPSetsDisabled"` (1 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `ocnxlAddOrUpdateOutput` | `ocnxl/ocnxlcommands.html` | `ocnxlAddOrUpdateOutput` |
| `ocnxlAddRelxSetup` | `ocnxl/ocnxlcommands.html` | `ocnxlAddRelxSetup` |
| `ocnxlBeginTest` | `ocnxl/ocnxlcommands.html` | `ocnxlBeginTest` |
| `ocnxlConjugateGradientOptions` | `ocnxl/ocnxlcommands.html` | `ocnxlConjugateGradientOptions" HTML` |
| `ocnxlCorner` | `ocnxl/ocnxlcommands.html` | `ocnxlCorner` |
| `ocnxlCornerVars` | `ocnxl/ocnxlcommands.html` | `ocnxlCornerVars` |
| `ocnxlDeleteNote` | `ocnxl/ocnxlcommands.html` | `ocnxlDeleteNote` |
| `ocnxlDisableCorner` | `ocnxl/ocnxlcommands.html` | `ocnxlDisableCorner` |
| `ocnxlDisableCornerForTest` | `ocnxl/ocnxlcommands.html` | `ocnxlDisableCornerForTest` |
| `ocnxlDisableRelxSetup` | `ocnxl/ocnxlcommands.html` | `ocnxlDisableRelxSetup` |
| `ocnxlDisableSweepParam` | `ocnxl/ocnxlcommands.html` | `ocnxlDisableSweepParam` |
| `ocnxlDisableSweepVar` | `ocnxl/ocnxlcommands.html` | `ocnxlDisableSweepVar` |
| `ocnxlDisableTest` | `ocnxl/ocnxlcommands.html` | `ocnxlDisableTest` |
| `ocnxlEADAddMeasurement` | `ocnxl/ocnxlcommands.html` | `ocnxlEADAddMeasurement` |
| `ocnxlEADAddMeasurement` | `ocnxl/ocnxlcommands.html` | `ocnxlEADAddMeasurement` |
| `ocnxlEADCreateDataSet` | `ocnxl/ocnxlcommands.html` | `ocnxlEADCreateDataSet` |
| `ocnxlEADCreateDataSet` | `ocnxl/ocnxlcommands.html` | `ocnxlEADCreateDataSet` |
| `ocnxlEADEnableLiveProcessing` | `ocnxl/ocnxlcommands.html` | `ocnxlEADEnableLiveProcessing` |
| `ocnxlEADEnableLiveProcessing` | `ocnxl/ocnxlcommands.html` | `ocnxlEADEnableLiveProcessing` |
| `ocnxlEADSelectAllSignals` | `ocnxl/ocnxlcommands.html` | `ocnxlEADSelectAllSignals` |
| `ocnxlEADSelectAllSignals` | `ocnxl/ocnxlcommands.html` | `ocnxlEADSelectAllSignals` |
| `ocnxlEADSetDutMaster` | `ocnxl/ocnxlcommands.html` | `ocnxlEADSetDutMaster` |
| `ocnxlEADSetDutMaster` | `ocnxl/ocnxlcommands.html` | `ocnxlEADSetDutMaster` |
| `ocnxlEADSetHierarchyLevel` | `ocnxl/ocnxlcommands.html` | `ocnxlEADSetHierarchyLevel` |
| `ocnxlEADSetHierarchyLevel` | `ocnxl/ocnxlcommands.html` | `ocnxlEADSetHierarchyLevel` |
| `ocnxlEADSetWaveFormClipping` | `ocnxl/ocnxlcommands.html` | `ocnxlEADSetWaveFormClipping` |
| `ocnxlEADSetWaveFormClipping` | `ocnxl/ocnxlcommands.html` | `ocnxlEADSetWaveFormClipping` |
| `ocnxlEnableCorner` | `ocnxl/ocnxlcommands.html` | `ocnxlEnableCorner` |
| `ocnxlEnableCornerForTest` | `ocnxl/ocnxlcommands.html` | `ocnxlEnableCornerForTest` |
| `ocnxlEnableSweepParam` | `ocnxl/ocnxlcommands.html` | `ocnxlEnableSweepParam` |
| `ocnxlEnableSweepVar` | `ocnxl/ocnxlcommands.html` | `ocnxlEnableSweepVar` |
| `ocnxlEnableTest` | `ocnxl/ocnxlcommands.html` | `ocnxlEnableTest` |
| `ocnxlEndTest` | `ocnxl/ocnxlcommands.html` | `ocnxlEndTest` |
| `ocnxlEndXLMode` | `ocnxl/ocnxlcommands.html` | `ocnxlEndXLMode` |
| `ocnxlExportOutputView` | `ocnxl/ocnxlcommands.html` | `ocnxlExportOutputView` |
| `ocnxlFeasibilityAnalysisOptions` | `ocnxl/ocnxlcommands.html` | `ocnxlFeasibilityAnalysisOptions` |
| `ocnxlGetBestPointParams` | `ocnxl/ocnxlcommands.html` | `ocnxlGetBestPointParams` |
| `ocnxlGetCorners` | `ocnxl/ocnxlcommands.html` | `ocnxlGetCorners` |
| `ocnxlGetCurrentHistory` | `ocnxl/ocnxlcommands.html` | `ocnxlGetCurrentHistory` |
| `ocnxlGetCurrentHistoryId` | `ocnxl/ocnxlcommands.html` | `ocnxlGetCurrentHistoryId` |
| `ocnxlGetHistory` | `ocnxl/ocnxlcommands.html` | `ocnxlGetHistory` |
| `ocnxlGetJobId` | `ocnxl/ocnxlcommands.html` | `ocnxlGetJobId` |
| `ocnxlGetOverwriteHistory` | `ocnxl/ocnxlcommands.html` | `ocnxlGetOverwriteHistory` |
| `ocnxlGetOverwriteHistoryName` | `ocnxl/ocnxlcommands.html` | `ocnxlGetOverwriteHistoryName"  HTML` |
| `ocnxlGetPointId` | `ocnxl/ocnxlcommands.html` | `ocnxlGetPointId` |
| `ocnxlGetReferenceHistory` | `ocnxl/ocnxlcommands.html` | `ocnxlGetReferenceHistory` |
| `ocnxlGetRunDistributeOptions` | `ocnxl/ocnxlcommands.html` | `ocnxlGetRunDistributeOptions"  HTML` |
| `ocnxlGetSession` | `ocnxl/ocnxlcommands.html` | `ocnxlGetSession` |
| `ocnxlGetSpecs` | `ocnxl/ocnxlcommands.html` | `ocnxlGetSpecs` |
| `ocnxlGetTests` | `ocnxl/ocnxlcommands.html` | `ocnxlGetTests` |
| `ocnxlGlobalOptimizationOptions` | `ocnxl/ocnxlcommands.html` | `ocnxlGlobalOptimizationOptions` |
| `ocnxlHistoryPrefix` | `ocnxl/ocnxlcommands.html` | `ocnxlHistoryPrefix` |
| `ocnxlJobSetup` | `ocnxl/ocnxlcommands.html` | `ocnxlJobSetup` |
| `ocnxlLoadCurrentEnvironment` | `ocnxl/ocnxlcommands.html` | `ocnxlLoadCurrentEnvironment"   HTML` |
| `ocnxlLoadSetupState` | `ocnxl/ocnxlcommands.html` | `ocnxlLoadSetupState` |
| `ocnxlLocalOptimizationOptions` | `ocnxl/ocnxlcommands.html` | `ocnxlLocalOptimizationOptions` |
| `ocnxlMCIterNum` | `ocnxl/ocnxlcommands.html` | `ocnxlMCIterNum` |
| `ocnxlMTSBlock` | `ocnxl/ocnxlcommands.html` | `ocnxlMTSBlock` |
| `ocnxlMTSEnable` | `ocnxl/ocnxlcommands.html` | `ocnxlMTSEnable` |
| `ocnxlMainSimSession` | `ocnxl/ocnxlcommands.html` | `ocnxlMainSimSession` |
| `ocnxlMaxJobFail` | `ocnxl/ocnxlcommands.html` | `ocnxlMaxJobFail` |
| `ocnxlModelGroup` | `ocnxl/ocnxlcommands.html` | `ocnxlModelGroup` |
| `ocnxlMonteCarloOptions` | `ocnxl/ocnxlcommands.html` | `ocnxlMonteCarloOptions` |
| `ocnxlOpenResults` | `ocnxl/ocnxlcommands.html` | `ocnxlOpenResults` |
| `ocnxlOutputAreaGoal` | `ocnxl/ocnxlcommands.html` | `ocnxlOutputAreaGoal` |
| `ocnxlOutputExpr` | `ocnxl/ocnxlcommands.html` | `ocnxlOutputExpr` |
| `ocnxlOutputMatExpr` | `ocnxl/ocnxlcommands.html` | `ocnxlOutputMatExpr` |
| `ocnxlOutputMatlabScript` | `ocnxl/ocnxlcommands.html` | `ocnxlOutputMatlabScript` |
| `ocnxlOutputOceanScript` | `ocnxl/ocnxlcommands.html` | `ocnxlOutputOceanScript` |
| `ocnxlOutputOpRegion` | `ocnxl/ocnxlcommands.html` | `ocnxlOutputOpRegion` |
| `ocnxlOutputSignal` | `ocnxl/ocnxlcommands.html` | `ocnxlOutputSignal` |
| `ocnxlOutputSpiceScript` | `ocnxl/ocnxlcommands.html` | `ocnxlOutputSpiceScript` |
| `ocnxlOutputSummary` | `ocnxl/ocnxlcommands.html` | `ocnxlOutputSummary` |
| `ocnxlOutputTerminal` | `ocnxl/ocnxlcommands.html` | `ocnxlOutputTerminal` |
| `ocnxlOutputViolations` | `ocnxl/ocnxlcommands.html` | `ocnxlOutputViolations` |
| `ocnxlParametricSet` | `ocnxl/ocnxlcommands.html` | `ocnxlParametricSet` |
| `ocnxlPreRunScript` | `ocnxl/ocnxlcommands.html` | `ocnxlPreRunScript` |
| `ocnxlProjectDir` | `ocnxl/ocnxlcommands.html` | `ocnxlProjectDir` |
| `ocnxlPutChecksAsserts` | `ocnxl/ocnxlcommands.html` | `ocnxlPutChecksAsserts` |
| `ocnxlPutChecksAsserts` | `ocnxl/ocnxlcommands.html` | `ocnxlPutChecksAsserts` |
| `ocnxlPutChecksAssertsTest` | `ocnxl/ocnxlcommands.html` | `ocnxlPutChecksAssertsTest` |
| `ocnxlPutChecksAssertsTest` | `ocnxl/ocnxlcommands.html` | `ocnxlPutChecksAssertsTest` |
| `ocnxlPutEnabledChecksAssertsCellViews` | `ocnxl/ocnxlcommands.html` | `ocnxlPutEnabledChecksAssertsCellViews` |
| `ocnxlPutEnabledChecksAssertsCellViews` | `ocnxl/ocnxlcommands.html` | `ocnxlPutEnabledChecksAssertsCellViews` |
| `ocnxlPutGreaterthanSpec` | `ocnxl/ocnxlcommands.html` | `ocnxlPutGreaterthanSpec` |
| `ocnxlPutInfoSpec` | `ocnxl/ocnxlcommands.html` | `ocnxlPutInfoSpec` |
| `ocnxlPutLessthanSpec` | `ocnxl/ocnxlcommands.html` | `ocnxlPutLessthanSpec` |
| `ocnxlPutMaxSpec` | `ocnxl/ocnxlcommands.html` | `ocnxlPutMaxSpec` |
| `ocnxlPutMinSpec` | `ocnxl/ocnxlcommands.html` | `ocnxlPutMinSpec` |
| `ocnxlPutNote` | `ocnxl/ocnxlcommands.html` | `ocnxlPutNote` |
| `ocnxlPutRangeSpec` | `ocnxl/ocnxlcommands.html` | `ocnxlPutRangeSpec` |
| `ocnxlPutToleranceSpec` | `ocnxl/ocnxlcommands.html` | `ocnxlPutToleranceSpec` |
| `ocnxlRemoveSpec` | `ocnxl/ocnxlcommands.html` | `ocnxlRemoveSpec` |
| `ocnxlRenameCurrentHistory` | `ocnxl/ocnxlcommands.html` | `ocnxlRenameCurrentHistory` |
| `ocnxlResultsLocation` | `ocnxl/ocnxlcommands.html` | `ocnxlResultsLocation` |
| `ocnxlRun` | `ocnxl/ocnxlcommands.html` | `ocnxlRun` |
| `ocnxlRunCalibration` | `ocnxl/ocnxlcommands.html` | `ocnxlRunCalibration` |
| `ocnxlRunSetupSummary` | `ocnxl/ocnxlcommands.html` | `ocnxlRunSetupSummary` |
| `ocnxlSamplingOptions` | `ocnxl/ocnxlcommands.html` | `ocnxlSamplingOptions` |
| `ocnxlSaveSetupAs` | `ocnxl/ocnxlcommands.html` | `ocnxlSaveSetupAs` |
| `ocnxlSelectTest` | `ocnxl/ocnxlcommands.html` | `ocnxlSelectTest` |
| `ocnxlSensitivityOptions` | `ocnxl/ocnxlcommands.html` | `ocnxlSensitivityOptions` |
| `ocnxlSensitivityVars` | `ocnxl/ocnxlcommands.html` | `ocnxlSensitivityVars` |
| `ocnxlSetAllParameterPSetsDisabled   $ocnxl/ocnxlcommands.html` | `"ocnxlSetAllParameterPSetsDisabled"` | `HTML` |
| `ocnxlSetAllParametersDisabled` | `ocnxl/ocnxlcommands.html` | `ocnxlSetAllParametersDisabled` |
| `ocnxlSetAllVariablePSetsDisabled    $ocnxl/ocnxlcommands.html` | `"ocnxlSetAllVariablePSetsDisabled"` | `HTML` |
| `ocnxlSetAllVarsDisabled` | `ocnxl/ocnxlcommands.html` | `ocnxlSetAllVarsDisabled` |
| `ocnxlSetCalibration` | `ocnxl/ocnxlcommands.html` | `ocnxlSetCalibration` |
| `ocnxlSetDesignVariablePerTest` | `ocnxl/ocnxlcommands.html` | `ocnxlSetDesignVariablePerTest" HTML` |
| `ocnxlSetMCdut` | `ocnxl/ocnxlcommands.html` | `ocnxlSetMCdut` |
| `ocnxlSetMCignore` | `ocnxl/ocnxlcommands.html` | `ocnxlSetMCignore` |
| `ocnxlSetOverwriteHistory` | `ocnxl/ocnxlcommands.html` | `ocnxlSetOverwriteHistory` |
| `ocnxlSetOverwriteHistoryName` | `ocnxl/ocnxlcommands.html` | `ocnxlSetOverwriteHistoryName"  HTML` |
| `ocnxlSetPreRunScriptEnabled` | `ocnxl/ocnxlcommands.html` | `ocnxlSetPreRunScriptEnabled"   HTML` |
| `ocnxlSetReferenceHistory` | `ocnxl/ocnxlcommands.html` | `ocnxlSetReferenceHistory` |
| `ocnxlSetRelxAnalysisEnabled` | `ocnxl/ocnxlcommands.html` | `ocnxlSetRelxAnalysisEnabled"   HTML` |
| `ocnxlSetRunDistributeOptions` | `ocnxl/ocnxlcommands.html` | `ocnxlSetRunDistributeOptions"  HTML` |
| `ocnxlSetupLocation` | `ocnxl/ocnxlcommands.html` | `ocnxlSetupLocation` |
| `ocnxlSimResultsLocation` | `ocnxl/ocnxlcommands.html` | `ocnxlSimResultsLocation` |
| `ocnxlSizeOverCornersOptions` | `ocnxl/ocnxlcommands.html` | `ocnxlSizeOverCornersOptions` |
| `ocnxlStartingPoint` | `ocnxl/ocnxlcommands.html` | `ocnxlStartingPoint` |
| `ocnxlStimuliData` | `ocnxl/ocnxlcommands.html` | `ocnxlStimuliData` |
| `ocnxlSweepParam` | `ocnxl/ocnxlcommands.html` | `ocnxlSweepParam` |
| `ocnxlSweepVar` | `ocnxl/ocnxlcommands.html` | `ocnxlSweepVar` |
| `ocnxlSweepsAndCornersOptions` | `ocnxl/ocnxlcommands.html` | `ocnxlSweepsAndCornersOptions"  HTML` |
| `ocnxlTargetCellView` | `ocnxl/ocnxlcommands.html` | `ocnxlTargetCellView` |
| `ocnxlUpdatePointVariable` | `ocnxl/ocnxlcommands.html` | `ocnxlUpdatePointVariable` |
| `ocnxlWaitUntilDone` | `ocnxl/ocnxlcommands.html` | `ocnxlWaitUntilDone` |
| `ocnxlWorstCaseCornersOptions` | `ocnxl/ocnxlcommands.html` | `ocnxlWorstCaseCornersOptions"  HTML` |
| `ocnxlWriteDatasheet` | `ocnxl/ocnxlcommands.html` | `ocnxlWriteDatasheet` |
| `ocnxlYieldEstimationOptions` | `ocnxl/ocnxlcommands.html` | `ocnxlYieldEstimationOptions"   HTML` |
| `ocnxlYieldImprovementOptions` | `ocnxl/ocnxlcommands.html` | `ocnxlYieldImprovementOptions"  HTML` |


### HNL API

**128 个函数**，文档位置：

- `netlistsimulateref/ossFunctions.html` (89 个函数)
- `sktransrefOA/skcdlout.html` (28 个函数)
- `netlistsimulateref/netlisterFunctions.html` (10 个函数)
- `"hnlCatIncrementalNetlistFiles"` (1 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `hnlAbortNetlist` | `netlistsimulateref/ossFunctions.html` | `hnlAbortNetlist` |
| `hnlAddExtraParameters` | `netlistsimulateref/ossFunctions.html` | `hnlAddExtraParameters` |
| `hnlCDLPrintBJTElement` | `sktransrefOA/skcdlout.html` | `hnlCDLPrintBJTElement` |
| `hnlCDLPrintBSIM3SOIElement` | `sktransrefOA/skcdlout.html` | `hnlCDLPrintBSIM3SOIElement"    HTML` |
| `hnlCDLPrintCapElement` | `sktransrefOA/skcdlout.html` | `hnlCDLPrintCapElement` |
| `hnlCDLPrintCapacitorElement` | `sktransrefOA/skcdlout.html` | `hnlCDLPrintCapacitorElement"   HTML` |
| `hnlCDLPrintCds_Thru` | `sktransrefOA/skcdlout.html` | `hnlCDLPrintCds_Thru` |
| `hnlCDLPrintDiodeElement` | `sktransrefOA/skcdlout.html` | `hnlCDLPrintDiodeElement` |
| `hnlCDLPrintGeneralElement` | `sktransrefOA/skcdlout.html` | `hnlCDLPrintGeneralElement` |
| `hnlCDLPrintICIsrcElement` | `sktransrefOA/skcdlout.html` | `hnlCDLPrintICIsrcElement` |
| `hnlCDLPrintICVsrcElement` | `sktransrefOA/skcdlout.html` | `hnlCDLPrintICVsrcElement` |
| `hnlCDLPrintInductorElement` | `sktransrefOA/skcdlout.html` | `hnlCDLPrintInductorElement"    HTML` |
| `hnlCDLPrintInstPropVal` | `sktransrefOA/skcdlout.html` | `hnlCDLPrintInstPropVal` |
| `hnlCDLPrintIsrcElement` | `sktransrefOA/skcdlout.html` | `hnlCDLPrintIsrcElement` |
| `hnlCDLPrintJfetElement` | `sktransrefOA/skcdlout.html` | `hnlCDLPrintJfetElement` |
| `hnlCDLPrintMultiCNPNElement` | `sktransrefOA/skcdlout.html` | `hnlCDLPrintMultiCNPNElement"   HTML` |
| `hnlCDLPrintMultiCPNPElement` | `sktransrefOA/skcdlout.html` | `hnlCDLPrintMultiCPNPElement"   HTML` |
| `hnlCDLPrintMultiENPNElement` | `sktransrefOA/skcdlout.html` | `hnlCDLPrintMultiENPNElement"   HTML` |
| `hnlCDLPrintMultiEPNPElement` | `sktransrefOA/skcdlout.html` | `hnlCDLPrintMultiEPNPElement"   HTML` |
| `hnlCDLPrintNMOSfetElement` | `sktransrefOA/skcdlout.html` | `hnlCDLPrintNMOSfetElement` |
| `hnlCDLPrintNPNElement` | `sktransrefOA/skcdlout.html` | `hnlCDLPrintNPNElement` |
| `hnlCDLPrintPMOSfetElement` | `sktransrefOA/skcdlout.html` | `hnlCDLPrintPMOSfetElement` |
| `hnlCDLPrintPNPElement` | `sktransrefOA/skcdlout.html` | `hnlCDLPrintPNPElement` |
| `hnlCDLPrintResElement` | `sktransrefOA/skcdlout.html` | `hnlCDLPrintResElement` |
| `hnlCDLPrintResistorElement` | `sktransrefOA/skcdlout.html` | `hnlCDLPrintResistorElement"    HTML` |
| `hnlCDLPrintSchottkyTranElement` | `sktransrefOA/skcdlout.html` | `hnlCDLPrintSchottkyTranElement` |
| `hnlCDLPrintTlineElement` | `sktransrefOA/skcdlout.html` | `hnlCDLPrintTlineElement` |
| `hnlCDLPrintVCIsrcElement` | `sktransrefOA/skcdlout.html` | `hnlCDLPrintVCIsrcElement` |
| `hnlCDLPrintVCVsrcElement` | `sktransrefOA/skcdlout.html` | `hnlCDLPrintVCVsrcElement` |
| `hnlCDLPrintVsrcElement` | `sktransrefOA/skcdlout.html` | `hnlCDLPrintVsrcElement` |
| `hnlCatIncrementalNetlistFiles   $netlistsimulateref/ossFunctions.html` | `"hnlCatIncrementalNetlistFiles"` | `HTML` |
| `hnlCellExtracted` | `netlistsimulateref/ossFunctions.html` | `hnlCellExtracted` |
| `hnlCellInAllCells` | `netlistsimulateref/ossFunctions.html` | `hnlCellInAllCells` |
| `hnlCloseCellFiles` | `netlistsimulateref/ossFunctions.html` | `hnlCloseCellFiles` |
| `hnlCloseMasterList` | `netlistsimulateref/ossFunctions.html` | `hnlCloseMasterList` |
| `hnlCompletePrint` | `netlistsimulateref/ossFunctions.html` | `hnlCompletePrint` |
| `hnlDeRegPostNetlistTrigger` | `netlistsimulateref/ossFunctions.html` | `hnlDeRegPostNetlistTrigger` |
| `hnlDeRegPreNetlistTrigger` | `netlistsimulateref/ossFunctions.html` | `hnlDeRegPreNetlistTrigger` |
| `hnlDoInstBased` | `netlistsimulateref/ossFunctions.html` | `hnlDoInstBased` |
| `hnlDoNetBased` | `netlistsimulateref/ossFunctions.html` | `hnlDoNetBased` |
| `hnlEMHGetDigitaGlobalNets` | `netlistsimulateref/ossFunctions.html` | `hnlEMHGetDigitaGlobalNets` |
| `hnlEMHGetDigitalNetlistFileName` | `netlistsimulateref/ossFunctions.html` | `hnlEMHGetDigitalNetlistFileName"   HTML` |
| `hnlEMHSetVerbosityLevel` | `netlistsimulateref/ossFunctions.html` | `hnlEMHSetVerbosityLevel` |
| `hnlFindAllCells` | `netlistsimulateref/ossFunctions.html` | `hnlFindAllCells` |
| `hnlFindAllInstInCell` | `netlistsimulateref/ossFunctions.html` | `hnlFindAllInstInCell` |
| `hnlGenIncludeFile` | `netlistsimulateref/ossFunctions.html` | `hnlGenIncludeFile` |
| `hnlGetCellHdbProps` | `netlistsimulateref/ossFunctions.html` | `hnlGetCellHdbProps` |
| `hnlGetGlobalModelMappedName` | `netlistsimulateref/ossFunctions.html` | `hnlGetGlobalModelMappedName` |
| `hnlGetGlobalNetMappedName` | `netlistsimulateref/ossFunctions.html` | `hnlGetGlobalNetMappedName` |
| `hnlGetInstanceCount` | `netlistsimulateref/ossFunctions.html` | `hnlGetInstanceCount` |
| `hnlGetMappedInstNames` | `netlistsimulateref/ossFunctions.html` | `hnlGetMappedInstNames` |
| `hnlGetMappedModelNames` | `netlistsimulateref/ossFunctions.html` | `hnlGetMappedModelNames` |
| `hnlGetMappedNames` | `netlistsimulateref/ossFunctions.html` | `hnlGetMappedNames` |
| `hnlGetMappedNetNames` | `netlistsimulateref/ossFunctions.html` | `hnlGetMappedNetNames` |
| `hnlGetMasterCells` | `netlistsimulateref/ossFunctions.html` | `hnlGetMasterCells` |
| `hnlGetPrintLinePrefix` | `netlistsimulateref/ossFunctions.html` | `hnlGetPrintLinePrefix` |
| `hnlGetPropVal` | `netlistsimulateref/ossFunctions.html` | `hnlGetPropVal` |
| `hnlGetRoundProp` | `netlistsimulateref/ossFunctions.html` | `hnlGetRoundProp` |
| `hnlGetScaleCapacitance` | `netlistsimulateref/ossFunctions.html` | `hnlGetScaleCapacitance` |
| `hnlGetScaleMarginalDelay` | `netlistsimulateref/ossFunctions.html` | `hnlGetScaleMarginalDelay` |
| `hnlGetScaleTimeUnit` | `netlistsimulateref/ossFunctions.html` | `hnlGetScaleTimeUnit` |
| `hnlGetSimulator` | `netlistsimulateref/ossFunctions.html` | `hnlGetSimulator` |
| `hnlGetSourceFile` | `netlistsimulateref/ossFunctions.html` | `hnlGetSourceFile` |
| `hnlGetSourceFileModels` | `netlistsimulateref/ossFunctions.html` | `hnlGetSourceFileModels` |
| `hnlGetSymbolPropVal` | `netlistsimulateref/ossFunctions.html` | `hnlGetSymbolPropVal` |
| `hnlGetTermByName` | `netlistsimulateref/ossFunctions.html` | `hnlGetTermByName` |
| `hnlGetTermNameOfSig` | `netlistsimulateref/ossFunctions.html` | `hnlGetTermNameOfSig` |
| `hnlIfNoProcedure` | `netlistsimulateref/ossFunctions.html` | `hnlIfNoProcedure` |
| `hnlIgnoreTerm` | `netlistsimulateref/ossFunctions.html` | `hnlIgnoreTerm` |
| `hnlIngoreTerm` | `netlistsimulateref/ossFunctions.html` | `hnlIngoreTerm` |
| `hnlInitMap` | `netlistsimulateref/ossFunctions.html` | `hnlInitMap` |
| `hnlInitPrint` | `netlistsimulateref/ossFunctions.html` | `hnlInitPrint` |
| `hnlIsAPatchCord` | `netlistsimulateref/ossFunctions.html` | `hnlIsAPatchCord` |
| `hnlIsAStoppingCell` | `netlistsimulateref/ossFunctions.html` | `hnlIsAStoppingCell` |
| `hnlIsCellNetlistable` | `netlistsimulateref/ossFunctions.html` | `hnlIsCellNetlistable` |
| `hnlIsCurrentInstStopping` | `netlistsimulateref/ossFunctions.html` | `hnlIsCurrentInstStopping` |
| `hnlMakeNetlistFileName` | `netlistsimulateref/ossFunctions.html` | `hnlMakeNetlistFileName` |
| `hnlMapCellModuleName` | `netlistsimulateref/ossFunctions.html` | `hnlMapCellModuleName` |
| `hnlMapCellName` | `netlistsimulateref/ossFunctions.html` | `hnlMapCellName` |
| `hnlMapInstName` | `netlistsimulateref/ossFunctions.html` | `hnlMapInstName` |
| `hnlMapModelName` | `netlistsimulateref/ossFunctions.html` | `hnlMapModelName` |
| `hnlMapName` | `netlistsimulateref/ossFunctions.html` | `hnlMapName` |
| `hnlMapNetName` | `netlistsimulateref/ossFunctions.html` | `hnlMapNetName` |
| `hnlMapTermName` | `netlistsimulateref/ossFunctions.html` | `hnlMapTermName` |
| `hnlMultipleCells` | `netlistsimulateref/ossFunctions.html` | `hnlMultipleCells` |
| `hnlNameOfSignal` | `netlistsimulateref/ossFunctions.html` | `hnlNameOfSignal` |
| `hnlNetNameOnTerm` | `netlistsimulateref/ossFunctions.html` | `hnlNetNameOnTerm` |
| `hnlNetNameOnTermName` | `netlistsimulateref/ossFunctions.html` | `hnlNetNameOnTermName` |
| `hnlNmpSetNameSpaces` | `netlistsimulateref/ossFunctions.html` | `hnlNmpSetNameSpaces` |
| `hnlOpenTopCell` | `netlistsimulateref/ossFunctions.html` | `hnlOpenTopCell` |
| `hnlPcellIsParamOverridden` | `netlistsimulateref/ossFunctions.html` | `hnlPcellIsParamOverridden` |
| `hnlPostNetlistTriggerList` | `netlistsimulateref/ossFunctions.html` | `hnlPostNetlistTriggerList` |
| `hnlPreNetlistTriggerList` | `netlistsimulateref/ossFunctions.html` | `hnlPreNetlistTriggerList` |
| `hnlPrintDevices` | `netlistsimulateref/ossFunctions.html` | `hnlPrintDevices` |
| `hnlPrintMessage` | `netlistsimulateref/ossFunctions.html` | `hnlPrintMessage` |
| `hnlPrintNetlist` | `netlistsimulateref/ossFunctions.html` | `hnlPrintNetlist` |
| `hnlPrintSignal` | `netlistsimulateref/ossFunctions.html` | `hnlPrintSignal` |
| `hnlPrintString` | `netlistsimulateref/ossFunctions.html` | `hnlPrintString` |
| `hnlRegPostNetlistTrigger` | `netlistsimulateref/ossFunctions.html` | `hnlRegPostNetlistTrigger` |
| `hnlRegPreNetlistTrigger` | `netlistsimulateref/ossFunctions.html` | `hnlRegPreNetlistTrigger` |
| `hnlRunNetlister` | `netlistsimulateref/ossFunctions.html` | `hnlRunNetlister` |
| `hnlScaleCapacitance` | `netlistsimulateref/ossFunctions.html` | `hnlScaleCapacitance` |
| `hnlScaleMarginalDelay` | `netlistsimulateref/ossFunctions.html` | `hnlScaleMarginalDelay` |
| `hnlScaleTimeUnit` | `netlistsimulateref/ossFunctions.html` | `hnlScaleTimeUnit` |
| `hnlSetCellFiles` | `netlistsimulateref/ossFunctions.html` | `hnlSetCellFiles` |
| `hnlSetDef` | `netlistsimulateref/ossFunctions.html` | `hnlSetDef` |
| `hnlSetMappingType` | `netlistsimulateref/ossFunctions.html` | `hnlSetMappingType` |
| `hnlSetPrintLinePrefix` | `netlistsimulateref/ossFunctions.html` | `hnlSetPrintLinePrefix` |
| `hnlSetPseudoTermDir` | `netlistsimulateref/ossFunctions.html` | `hnlSetPseudoTermDir` |
| `hnlSetVars` | `netlistsimulateref/ossFunctions.html` | `hnlSetVars` |
| `hnlSortTerms` | `netlistsimulateref/ossFunctions.html` | `hnlSortTerms` |
| `hnlSortTermsToNets` | `netlistsimulateref/ossFunctions.html` | `hnlSortTermsToNets` |
| `hnlStartNetlist` | `netlistsimulateref/ossFunctions.html` | `hnlStartNetlist` |
| `hnlStopNetlist` | `netlistsimulateref/ossFunctions.html` | `hnlStopNetlist` |
| `hnlStringToList` | `netlistsimulateref/ossFunctions.html` | `hnlStringToList` |
| `hnlVerilogPrintBehaveModel` | `netlistsimulateref/netlisterFunctions.html` | `hnlVerilogPrintBehaveModel` |
| `hnlVerilogPrintBidiXfr` | `netlistsimulateref/netlisterFunctions.html` | `hnlVerilogPrintBidiXfr` |
| `hnlVerilogPrintBufif0Notif0` | `netlistsimulateref/netlisterFunctions.html` | `hnlVerilogPrintBufif0Notif0` |
| `hnlVerilogPrintBufif1Notif1` | `netlistsimulateref/netlisterFunctions.html` | `hnlVerilogPrintBufif1Notif1` |
| `hnlVerilogPrintCmos` | `netlistsimulateref/netlisterFunctions.html` | `hnlVerilogPrintCmos` |
| `hnlVerilogPrintLibraryModel` | `netlistsimulateref/netlisterFunctions.html` | `hnlVerilogPrintLibraryModel` |
| `hnlVerilogPrintLogGate` | `netlistsimulateref/netlisterFunctions.html` | `hnlVerilogPrintLogGate` |
| `hnlVerilogPrintNmosPmos` | `netlistsimulateref/netlisterFunctions.html` | `hnlVerilogPrintNmosPmos` |
| `hnlVerilogPrintPrimGate` | `netlistsimulateref/netlisterFunctions.html` | `hnlVerilogPrintPrimGate` |
| `hnlVerilogPrintVhdlImport` | `netlistsimulateref/netlisterFunctions.html` | `hnlVerilogPrintVhdlImport` |
| `hnlWriteBlockControlFile` | `netlistsimulateref/ossFunctions.html` | `hnlWriteBlockControlFile` |
| `hnlWriteMap` | `netlistsimulateref/ossFunctions.html` | `hnlWriteMap` |
| `hnllsCVInUserStopCVList` | `netlistsimulateref/ossFunctions.html` | `hnllsCVInUserStopCVList` |


### MAE API

**105 个函数**，文档位置：

- `maeSKILLref/maestroSKILL.html` (78 个函数)
- `maeSKILLref/maestroSKILLFSA.html` (8 个函数)
- `maeSKILLref/maestroSKILL.html      "maePlotWithPlottingTemplate"` (1 个函数)
- `maeSKILLref/maestroSKILL.html            "maeStmImportOasisStimulus"` (1 个函数)
- `maeSKILLref/maestroSKILL.html            "maeStmGenerateWaveforms"` (1 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `maeAddOutput` | `maeSKILLref/maestroSKILL.html` | `maeAddOutput` |
| `maeClearAllTestJobPolicies` | `maeSKILLref/maestroSKILL.html            "maeClearAllTestJobPolicies"` | `HTML` |
| `maeClearExistingFaultsForRevalidation` | `maeSKILLref/maestroSKILLFSA.html           "maeClearExistingFaultsForRevalidation"` | `HTML` |
| `maeCloseResults` | `maeSKILLref/maestroSKILL.html` | `maeCloseResults` |
| `maeCloseSession` | `maeSKILLref/maestroSKILL.html` | `maeCloseSession` |
| `maeConvertAndCombineMultiADELToAssembler` | `maeSKILLref/maestroSKILL.html` | `maeConvertAndCombineMultiADELToAssembler` |
| `maeCreateTest` | `maeSKILLref/maestroSKILL.html` | `maeCreateTest` |
| `maeDeleteCorner` | `maeSKILLref/maestroSKILL.html` | `maeDeleteCorner` |
| `maeDeleteFaultGroup` | `maeSKILLref/maestroSKILLFSA.html           "maeDeleteFaultGroup"` | `HTML` |
| `maeDeleteOutput` | `maeSKILLref/maestroSKILL.html` | `maeDeleteOutput` |
| `maeDeleteParameter` | `maeSKILLref/maestroSKILL.html` | `maeDeleteParameter` |
| `maeDeleteVar` | `maeSKILLref/maestroSKILL.html` | `maeDeleteVar` |
| `maeEnableFaults` | `maeSKILLref/maestroSKILLFSA.html           "maeEnableFaults"` | `HTML` |
| `maeExportOutputView` | `maeSKILLref/maestroSKILL.html` | `maeExportOutputView` |
| `maeExportSetupForExplorer` | `maeSKILLref/maestroSKILL.html` | `maeExportSetupForExplorer` |
| `maeGetAnalysis` | `maeSKILLref/maestroSKILL.html` | `maeGetAnalysis` |
| `maeGetCurrentRunMode` | `maeSKILLref/maestroSKILL.html` | `maeGetCurrentRunMode` |
| `maeGetCurrentRunPlanName` | `maeSKILLref/maestroSKILLFSA.html` | `maeGetCurrentRunPlanName` |
| `maeGetEnabledAnalysis` | `maeSKILLref/maestroSKILL.html` | `maeGetEnabledAnalysis` |
| `maeGetEnabledRuns` | `maeSKILLref/maestroSKILLFSA.html` | `maeGetEnabledRuns` |
| `maeGetEnvOption` | `maeSKILLref/maestroSKILL.html` | `maeGetEnvOption` |
| `maeGetExplorerTestName` | `maeSKILLref/maestroSKILL.html` | `maeGetExplorerTestName` |
| `maeGetGlobalFaultOptions` | `maeSKILLref/maestroSKILLFSA.html           "maeGetGlobalFaultOptions"` | `HTML` |
| `maeGetHistoryNameForCurrentRunInRunPlan` | `maeSKILLref/maestroSKILLFSA.html           "maeGetHistoryNameForCurrentRunInRunPlan"` | `HTML` |
| `maeGetJobPolicy` | `maeSKILLref/maestroSKILL.html` | `maeGetJobPolicy` |
| `maeGetJobPolicyByName` | `maeSKILLref/maestroSKILL.html` | `maeGetJobPolicyByName` |
| `maeGetMTSBlock` | `maeSKILLref/maestroSKILL.html` | `maeGetMTSBlock` |
| `maeGetMTSMode` | `maeSKILLref/maestroSKILL.html` | `maeGetMTSMode` |
| `maeGetNBestDesignPoints` | `maeSKILLref/maestroSKILL.html` | `maeGetNBestDesignPoints` |
| `maeGetNumberOfExecutedRuns` | `maeSKILLref/maestroSKILLFSA.html` | `maeGetNumberOfExecutedRuns` |
| `maeGetNumberOfUndetectedFaultsFromHistory` | `maeSKILLref/maestroSKILLFSA.html           "maeGetNumberOfUndetectedFaultsFromHistory"` | `HTML` |
| `maeGetOutputValue` | `maeSKILLref/maestroSKILL.html` | `maeGetOutputValue` |
| `maeGetOverallYield` | `maeSKILLref/maestroSKILL.html` | `maeGetOverallYield` |
| `maeGetParamConditions` | `maeSKILLref/maestroSKILL.html` | `maeGetParamConditions` |
| `maeGetParameter` | `maeSKILLref/maestroSKILL.html` | `maeGetParameter` |
| `maeGetResultOutputs` | `maeSKILLref/maestroSKILL.html` | `maeGetResultOutputs` |
| `maeGetResultTests` | `maeSKILLref/maestroSKILL.html` | `maeGetResultTests` |
| `maeGetRunPlan` | `maeSKILLref/maestroSKILL.html` | `maeGetRunPlan` |
| `maeGetSessions` | `maeSKILLref/maestroSKILL.html` | `maeGetSessions` |
| `maeGetSetup` | `maeSKILLref/maestroSKILL.html` | `maeGetSetup` |
| `maeGetSimOption` | `maeSKILLref/maestroSKILL.html` | `maeGetSimOption` |
| `maeGetSimulationMessages` | `maeSKILLref/maestroSKILL.html` | `maeGetSimulationMessages` |
| `maeGetSpecStatus` | `maeSKILLref/maestroSKILL.html` | `maeGetSpecStatus` |
| `maeGetStressFile` | `maeSKILLref/maestroSKILL.html` | `maeGetStressFile` |
| `maeGetStressFile` | `maeSKILLref/maestroSKILL.html` | `maeGetStressFile` |
| `maeGetTestEnvVar` | `maeSKILLref/maestroSKILL.html` | `maeGetTestEnvVar` |
| `maeGetTestOutputs` | `maeSKILLref/maestroSKILL.html            "maeGetTestOutputs"` | `HTML` |
| `maeGetTestSession` | `maeSKILLref/maestroSKILL.html` | `maeGetTestSession` |
| `maeGetTestVar` | `maeSKILLref/maestroSKILL.html` | `maeGetTestVar` |
| `maeGetVar` | `maeSKILLref/maestroSKILL.html` | `maeGetVar` |
| `maeHasTestJobPolicy` | `maeSKILLref/maestroSKILLFSA.html           "maeHasTestJobPolicy"` | `HTML` |
| `maeImportHistory` | `maeSKILLref/maestroSKILLFSA.html           "maeImportHistory"` | `HTML` |
| `maeImportSetupForExplorer` | `maeSKILLref/maestroSKILL.html` | `maeExportSetupForExplorer` |
| `maeIsFinalRunCompleted` | `maeSKILLref/maestroSKILLFSA.html` | `maeIsFinalRunCompleted` |
| `maeIsFirstRunInRunPlan` | `maeSKILLref/maestroSKILLFSA.html` | `maeIsFirstRunInRunPlan` |
| `maeIsSingleTest` | `maeSKILLref/maestroSKILL.html` | `maeIsSingleTest` |
| `maeIsValidMaestroSession` | `maeSKILLref/maestroSKILL.html` | `maeIsValidMaestroSession` |
| `maeLoadSetup` | `maeSKILLref/maestroSKILL.html` | `maeLoadSetup` |
| `maeLoadSetup` | `maeSKILLref/maestroSKILL.html` | `maeLoadSetup` |
| `maeLoadSetupState` | `maeSKILLref/maestroSKILL.html` | `maeLoadSetupState` |
| `maeLoadStateForTest` | `maeSKILLref/maestroSKILL.html` | `maeLoadStateForTest` |
| `maeMergeFaultHistories` | `maeSKILLref/maestroSKILLFSA.html` | `maeMergeFaultHistories` |
| `maeMigrateADELStateToMaestro` | `maeSKILLref/maestroSKILL.html` | `maeMigrateADELStateToMaestro` |
| `maeMigrateADEXLToMaestro` | `maeSKILLref/maestroSKILL.html` | `maeMigrateADEXLToMaestro` |
| `maeOpenLogViewer                    $maeSKILLref/maestroSKILL.html` | `"maeOpenLogViewer"` | `HTML` |
| `maeOpenResults` | `maeSKILLref/maestroSKILL.html` | `maeOpenResults` |
| `maeOpenSetup` | `maeSKILLref/maestroSKILL.html` | `maeOpenSetup` |
| `maePlotWithPlottingTemplate` | `maeSKILLref/maestroSKILL.html      "maePlotWithPlottingTemplate"` | `HTML` |
| `maePrintFaultDroppingStatistics` | `maeSKILLref/maestroSKILLFSA.html` | `maePrintFaultDroppingStatistics` |
| `maeReadResDB` | `maeSKILLref/maestroSKILL.html` | `maeReadResDB` |
| `maeRestoreHistory` | `maeSKILLref/maestroSKILL.html` | `maeRestoreHistory` |
| `maeRunSimulation` | `maeSKILLref/maestroSKILL.html` | `maeRunSimulation` |
| `maeSaveFaultsRunCount` | `maeSKILLref/maestroSKILLFSA.html` | `maeSaveFaultsRunCount` |
| `maeSaveSetup` | `maeSKILLref/maestroSKILL.html` | `maeSaveSetup` |
| `maeSaveSetupState` | `maeSKILLref/maestroSKILL.html` | `maeSaveSetupState` |
| `maeSensDeleteModel` | `maeSKILLref/maestroSKILL.html            "maeSensDeleteModel"` | `HTML` |
| `maeSensDeleteModelGroup` | `maeSKILLref/maestroSKILL.html            "maeSensDeleteModelGroup"` | `HTML` |
| `maeSensDeleteParameter` | `maeSKILLref/maestroSKILL.html            "maeSensDeleteParameter"` | `HTML` |
| `maeSetAnalysis` | `maeSKILLref/maestroSKILL.html` | `maeSetAnalysis` |
| `maeSetCorner` | `maeSKILLref/maestroSKILL.html` | `maeSetCorner` |
| `maeSetCurrentRunMode` | `maeSKILLref/maestroSKILL.html` | `maeSetCurrentRunMode` |
| `maeSetDUTForFaults` | `maeSKILLref/maestroSKILLFSA.html           "maeSetDUTForFaults"` | `HTML` |
| `maeSetEnableTestVar` | `maeSKILLref/maestroSKILL.html` | `maeSetEnableTestVar` |
| `maeSetEnvOption` | `maeSKILLref/maestroSKILL.html` | `maeSetEnvOption` |
| `maeSetJobPolicy` | `maeSKILLref/maestroSKILL.html` | `maeSetJobPolicy` |
| `maeSetMTSBlock` | `maeSKILLref/maestroSKILL.html` | `maeSetMTSBlock` |
| `maeSetMTSMode` | `maeSKILLref/maestroSKILL.html` | `maeSetMTSMode` |
| `maeSetParameter` | `maeSKILLref/maestroSKILL.html` | `maeSetParameter` |
| `maeSetPreRunScript` | `maeSKILLref/maestroSKILL.html` | `maeSetPreRunScript` |
| `maeSetRunOption` | `maeSKILLref/maestroSKILL.html` | `maeSetRunOption` |
| `maeSetSetup` | `maeSKILLref/maestroSKILL.html` | `maeSetSetup` |
| `maeSetSimOption` | `maeSKILLref/maestroSKILL.html` | `maeSetSimOption` |
| `maeSetSpec` | `maeSKILLref/maestroSKILL.html` | `maeSetSpec` |
| `maeSetTestEnvVar` | `maeSKILLref/maestroSKILL.html` | `maeSetTestEnvVar` |
| `maeSetTestVar` | `maeSKILLref/maestroSKILL.html` | `maeSetTestVar` |
| `maeSetVar` | `maeSKILLref/maestroSKILL.html` | `maeSetVar` |
| `maeStmGenerateWaveforms` | `maeSKILLref/maestroSKILL.html            "maeStmGenerateWaveforms"` | `HTML` |
| `maeStmImportOasisStimulus` | `maeSKILLref/maestroSKILL.html            "maeStmImportOasisStimulus"` | `HTML` |
| `maeStopSimulation` | `maeSKILLref/maestroSKILL.html` | `maeStopSimulation` |
| `maeSuspendSimulation` | `maeSKILLref/maestroSKILL.html` | `maeSuspendSimulation` |
| `maeSwitchActiveFaultGroupForCurrentRun` | `maeSKILLref/maestroSKILLFSA.html           "maeSwitchActiveFaultGroupForCurrentRun"` | `HTML` |
| `maeWaitUntilDone` | `maeSKILLref/maestroSKILL.html` | `maeWaitUntilDone` |
| `maeWriteDatasheet` | `maeSKILLref/maestroSKILL.html` | `maeWriteDatasheet` |
| `maeWriteScript` | `maeSKILLref/maestroSKILL.html` | `maeWriteScript` |
| `maeWriteSetup` | `maeSKILLref/maestroSKILL.html` | `maeWriteSetup` |


### VERIF API

**87 个函数**，文档位置：

- `verifierSkillRef/requirements.html` (26 个函数)
- `verifierSkillRef/simResults.html` (18 个函数)
- `verifierSkillRef/sessionSetup.html` (15 个函数)
- `verifierSkillRef/implementations.html` (11 个函数)
- `verifierSkillRef/mappings.html` (5 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `verifAddImp` | `verifierSkillRef/implementations.html` | `verifAddImp` |
| `verifAddImpSet` | `verifierSkillRef/simResults.html` | `verifAddImpSet` |
| `verifAddImpToImpSet` | `verifierSkillRef/simResults.html` | `verifAddImpToImpSet` |
| `verifAddReq` | `verifierSkillRef/requirements.html` | `verifAddReq` |
| `verifCheckForChanges` | `verifierSkillRef/implementations.html` | `verifCheckForChanges` |
| `verifCloseSession` | `verifierSkillRef/sessionSetup.html` | `verifCloseSession` |
| `verifCopyAndUpdateResultsFromUserDefinedDirectory` | `verifierSkillRef/simResults.html` | `verifCopyAndUpdateResultsFromUserDefinedDirectory` |
| `verifCreateBatchScript` | `verifierSkillRef/sessionSetup.html` | `verifCreateBatchScript` |
| `verifCreateRandomId` | `verifierSkillRef/requirements.html` | `verifCreateRandomId` |
| `verifDeleteReqSignoff` | `verifierSkillRef/requirements.html` | `verifDeleteReqSignoff` |
| `verifDisableDebug` | `verifierSkillRef/debug.html` | `verifDisableDebug` |
| `verifDownloadFromVManager` | `verifierSkillRef/requirements.html           "verifDownloadFromVManager"` | `HTML` |
| `verifEnableDebug` | `verifierSkillRef/debug.html` | `verifEnableDebug` |
| `verifEvaluateResults` | `verifierSkillRef/simResults.html` | `verifEvaluateResults` |
| `verifExportJson` | `verifierSkillRef/simResults.html` | `verifExportJson` |
| `verifExportMapping` | `verifierSkillRef/mappings.html` | `verifExportMapping` |
| `verifExportReqsToFile` | `verifierSkillRef/requirements.html` | `verifExportReqsToFile` |
| `verifGetAllSessions` | `verifierSkillRef/sessionSetup.html` | `verifGetAllSessions` |
| `verifGetCallbacks` | `verifierSkillRef/sessionSetup.html` | `verifGetCallbacks` |
| `verifGetCellViewSession` | `verifierSkillRef/sessionSetup.html` | `verifGetCellViewSession` |
| `verifGetCustomFieldNames` | `verifierSkillRef/requirements.html` | `verifGetCustomFieldNames` |
| `verifGetCustomFieldValue` | `verifierSkillRef/requirements.html` | `verifGetCustomFieldValue` |
| `verifGetDebug` | `verifierSkillRef/debug.html` | `verifGetDebug` |
| `verifGetImpData` | `verifierSkillRef/implementations.html` | `verifGetImpData` |
| `verifGetImpMapping` | `verifierSkillRef/mappings.html` | `verifGetImpMapping` |
| `verifGetImpSets` | `verifierSkillRef/simResults.html` | `verifGetImpSets` |
| `verifGetImpTestOutputs` | `verifierSkillRef/implementations.html` | `verifGetImpTestOutputs` |
| `verifGetImpTests` | `verifierSkillRef/implementations.html` | `verifGetImpTests` |
| `verifGetImportedFiles` | `verifierSkillRef/requirements.html` | `verifGetImportedFiles` |
| `verifGetImps` | `verifierSkillRef/implementations.html` | `verifGetImps` |
| `verifGetImpsInImpSet` | `verifierSkillRef/simResults.html` | `verifGetImpsInImpSet` |
| `verifGetMappableType` | `verifierSkillRef/implementations.html` | `verifGetMappableType` |
| `verifGetOptionVal` | `verifierSkillRef/sessionSetup.html` | `verifGetOptionVal` |
| `verifGetOptions` | `verifierSkillRef/sessionSetup.html` | `verifGetOptions` |
| `verifGetReferencedCellViews` | `verifierSkillRef/requirements.html` | `verifGetReferencedCellViews` |
| `verifGetReqCustomFieldNames` | `verifierSkillRef/requirements.html` | `verifGetReqCustomFieldNames` |
| `verifGetReqCustomFieldValue` | `verifierSkillRef/requirements.html` | `verifGetReqCustomFieldValue` |
| `verifGetReqMapping` | `verifierSkillRef/mappings.html` | `verifGetReqMapping` |
| `verifGetReqParent` | `verifierSkillRef/requirements.html` | `verifGetReqParent` |
| `verifGetReqProp` | `verifierSkillRef/requirements.html` | `verifGetReqProp` |
| `verifGetReqProps` | `verifierSkillRef/requirements.html` | `verifGetReqProps` |
| `verifGetReqSignoff` | `verifierSkillRef/requirements.html` | `verifGetReqSignoff` |
| `verifGetReqStatus` | `verifierSkillRef/requirements.html` | `verifGetReqStatus` |
| `verifGetReqs` | `verifierSkillRef/requirements.html` | `verifGetReqs` |
| `verifGetResultDataForImp` | `verifierSkillRef/simResults.html` | `verifGetResultDataForImp` |
| `verifGetResultDataForReq` | `verifierSkillRef/simResults.html` | `verifGetResultDataForReq` |
| `verifGetVManagerProjects` | `verifierSkillRef/requirements.html           "verifGetVManagerProjects"` | `HTML` |
| `verifGetWindow` | `verifierSkillRef/sessionSetup.html` | `verifGetWindow` |
| `verifImpIsRun` | `verifierSkillRef/simResults.html` | `verifImpIsRun` |
| `verifImportFile` | `verifierSkillRef/requirements.html` | `verifImportFile` |
| `verifImportMapping` | `verifierSkillRef/mappings.html` | `verifImportMapping` |
| `verifIsBatchRunProcess` | `verifierSkillRef/simResults.html` | `verifIsBatchRunProcess` |
| `verifIsSessionModified` | `verifierSkillRef/simResults.html` | `verifIsSessionModified` |
| `verifIsSessionReadOnly` | `verifierSkillRef/sessionSetup.html` | `verifIsSessionReadOnly` |
| `verifIsVManagerConnected` | `verifierSkillRef/requirements.html           "verifIsVManagerConnected"` | `HTML` |
| `verifIsVManagerEnabled` | `verifierSkillRef/requirements.html           "verifIsVManagerEnabled"` | `HTML` |
| `verifIsValidSession` | `verifierSkillRef/simResults.html` | `verifIsValidSession` |
| `verifMapping` | `verifierSkillRef/mappings.html` | `verifMapping` |
| `verifMoveImp` | `verifierSkillRef/implementations.html` | `verifMoveImp` |
| `verifMoveReq` | `verifierSkillRef/requirements.html` | `verifMoveReq` |
| `verifOpenCellView` | `verifierSkillRef/sessionSetup.html` | `verifOpenCellView` |
| `verifOverwriteSpec` | `verifierSkillRef/implementations.html` | `verifOverwriteSpec` |
| `verifPostResultsToVManager` | `verifierSkillRef/requirements.html           "verifPostResultsToVManager"` | `HTML` |
| `verifPublishHTML` | `verifierSkillRef/verificationReports.html` | `verifPublishHTML` |
| `verifRegisterCallback` | `verifierSkillRef/sessionSetup.html` | `verifRegisterCallback` |
| `verifReloadAllRes` | `verifierSkillRef/implementations.html` | `verifReloadAllRes` |
| `verifRemoveCallback` | `verifierSkillRef/sessionSetup.html` | `verifRemoveCallback` |
| `verifRemoveImp` | `verifierSkillRef/implementations.html` | `verifRemoveImp` |
| `verifRemoveImpFromImpSet` | `verifierSkillRef/simResults.html` | `verifRemoveImpFromImpSet` |
| `verifRemoveImpSet` | `verifierSkillRef/simResults.html` | `verifRemoveImpSet` |
| `verifRemoveReq` | `verifierSkillRef/requirements.html` | `verifRemoveReq` |
| `verifRemoveVManager` | `verifierSkillRef/requirements.html           "verifRemoveVManager"` | `HTML` |
| `verifRun` | `verifierSkillRef/simResults.html` | `verifRun` |
| `verifRunImpSet` | `verifierSkillRef/simResults.html` | `verifRunImpSet` |
| `verifSaveSession` | `verifierSkillRef/sessionSetup.html` | `verifSaveSession` |
| `verifSaveSessionAs` | `verifierSkillRef/sessionSetup.html` | `verifSaveSessionAs` |
| `verifSetCustomFieldValue` | `verifierSkillRef/requirements.html` | `verifSetCustomFieldValue` |
| `verifSetImpSetName` | `verifierSkillRef/simResults.html` | `verifSetImpSetName` |
| `verifSetOptionVal` | `verifierSkillRef/sessionSetup.html` | `verifSetOptionVal` |
| `verifSetReqCellviewHolder` | `verifierSkillRef/requirements.html           "verifSetReqCellviewHolder"` | `HTML` |
| `verifSetReqCustomFieldValue` | `verifierSkillRef/requirements.html` | `verifSetReqCustomFieldValue` |
| `verifSetReqGoalType` | `verifierSkillRef/requirements.html` | `verifSetReqGoalType` |
| `verifSetReqId` | `verifierSkillRef/requirements.html` | `verifSetReqId` |
| `verifSetReqTitle` | `verifierSkillRef/requirements.html` | `verifSetReqTitle` |
| `verifSetReqType` | `verifierSkillRef/requirements.html` | `verifSetReqType` |
| `verifSignOffReq` | `verifierSkillRef/requirements.html` | `verifSignOffReq` |
| `verifUploadToVManager` | `verifierSkillRef/requirements.html           "verifUploadToVManager"` | `HTML` |


### NL API

**68 个函数**，文档位置：

- `skartistref/chap4.html` (68 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `nlDisplayOption` | `skartistref/chap4.html` | `nlDisplayOption` |
| `nlError` | `skartistref/chap4.html` | `nlError` |
| `nlGetCurrentSwitchMaster` | `skartistref/chap4.html` | `nlGetCurrentSwitchMaster` |
| `nlGetDesign` | `skartistref/chap4.html` | `nlGetDesign` |
| `nlGetFormatter` | `skartistref/chap4.html` | `nlGetFormatter` |
| `nlGetGlobalNets` | `skartistref/chap4.html` | `nlGetGlobalNets` |
| `nlGetId` | `skartistref/chap4.html` | `nlGetId` |
| `nlGetModelName` | `skartistref/chap4.html` | `nlGetModelName` |
| `nlGetNetlistDir` | `skartistref/chap4.html` | `nlGetNetlistDir` |
| `nlGetNetlister` | `skartistref/chap4.html` | `nlGetNetlister` |
| `nlGetNumberOfBits` | `skartistref/chap4.html` | `nlGetNumberOfBits` |
| `nlGetOption` | `skartistref/chap4.html` | `nlGetOption` |
| `nlGetOptionNameList` | `skartistref/chap4.html` | `nlGetOptionNameList` |
| `nlGetPCellParamSource` | `skartistref/chap4.html` | `nlGetPCellParamSource` |
| `nlGetParamList` | `skartistref/chap4.html` | `nlGetParamList` |
| `nlGetParamStringValue` | `skartistref/chap4.html` | `nlGetParamStringValue` |
| `nlGetScratchInstance` | `skartistref/chap4.html` | `nlGetScratchInstance` |
| `nlGetSignalList` | `skartistref/chap4.html` | `nlGetSignalList` |
| `nlGetSimName` | `skartistref/chap4.html` | `nlGetSimName` |
| `nlGetSimTerminalNets` | `skartistref/chap4.html` | `nlGetSimTerminalNets` |
| `nlGetSwitchViewList` | `skartistref/chap4.html` | `nlGetSwitchViewList` |
| `nlGetTerminalList` | `skartistref/chap4.html` | `nlGetTerminalList` |
| `nlGetTerminalNets` | `skartistref/chap4.html` | `nlGetTerminalNets` |
| `nlGetToolName` | `skartistref/chap4.html` | `nlGetToolName` |
| `nlGetTopCellName` | `skartistref/chap4.html` | `nlGetTopCellName` |
| `nlGetTopLibName` | `skartistref/chap4.html` | `nlGetTopLibName` |
| `nlGetTopViewName` | `skartistref/chap4.html` | `nlGetTopViewName` |
| `nlIncludeDbDSPFTextFile` | `skartistref/chap4.html` | `nlIncludeDbDSPFTextFile` |
| `nlIncludePspiceFile` | `skartistref/chap4.html` | `nlIncludePspiceFile` |
| `nlIncludeSrcFile` | `skartistref/chap4.html` | `nlIncludeSrcFile` |
| `nlIncludeVerilogFile` | `skartistref/chap4.html` | `nlIncludeVerilogFile` |
| `nlIncludeVerilogaFile` | `skartistref/chap4.html` | `nlIncludeVerilogaFile` |
| `nlInfo` | `skartistref/chap4.html` | `nlInfo` |
| `nlInitialize` | `skartistref/chap4.html` | `nlInitialize` |
| `nlIsModelNameInherited` | `skartistref/chap4.html` | `nlIsModelNameInherited"    HTML` |
| `nlMapGlobalNet` | `skartistref/chap4.html` | `nlMapGlobalNet` |
| `nlObjError` | `skartistref/chap4.html` | `nlObjError` |
| `nlPrintComment` | `skartistref/chap4.html` | `nlPrintComment` |
| `nlPrintComments` | `skartistref/chap4.html` | `nlPrintComments` |
| `nlPrintFooter` | `skartistref/chap4.html` | `nlPrintFooter` |
| `nlPrintHeader` | `skartistref/chap4.html` | `nlPrintHeader` |
| `nlPrintHeaderComments` | `skartistref/chap4.html` | `nlPrintHeaderComments` |
| `nlPrintIndentString` | `skartistref/chap4.html` | `nlPrintIndentString` |
| `nlPrintInst` | `skartistref/chap4.html` | `nlPrintInst` |
| `nlPrintInstComments` | `skartistref/chap4.html` | `nlPrintInstComments` |
| `nlPrintInstEnd` | `skartistref/chap4.html` | `nlPrintInstEnd` |
| `nlPrintInstName` | `skartistref/chap4.html` | `nlPrintInstName` |
| `nlPrintInstParameters` | `skartistref/chap4.html` | `nlPrintInstParameters` |
| `nlPrintInstSignals` | `skartistref/chap4.html` | `nlPrintInstSignals` |
| `nlPrintModelName` | `skartistref/chap4.html` | `nlPrintModelName` |
| `nlPrintString` | `skartistref/chap4.html` | `nlPrintString` |
| `nlPrintStringNoFold` | `skartistref/chap4.html` | `nlPrintStringNoFold` |
| `nlPrintSubcktBegin` | `skartistref/chap4.html` | `nlPrintSubcktBegin` |
| `nlPrintSubcktEnd` | `skartistref/chap4.html` | `nlPrintSubcktEnd` |
| `nlPrintSubcktFooter` | `skartistref/chap4.html` | `nlPrintSubcktFooter` |
| `nlPrintSubcktFooterComments` | `skartistref/chap4.html` | `nlPrintSubcktFooterComments` |
| `nlPrintSubcktHeader` | `skartistref/chap4.html` | `nlPrintSubcktHeader` |
| `nlPrintSubcktHeaderComments` | `skartistref/chap4.html` | `nlPrintSubcktHeaderComments` |
| `nlPrintSubcktName` | `skartistref/chap4.html` | `nlPrintSubcktName` |
| `nlPrintSubcktParameters` | `skartistref/chap4.html` | `nlPrintSubcktParameters` |
| `nlPrintSubcktTerminalList` | `skartistref/chap4.html` | `nlPrintSubcktTerminalList` |
| `nlPrintTopCellFooter` | `skartistref/chap4.html` | `nlPrintTopCellFooter` |
| `nlPrintTopCellFooterComments` | `skartistref/chap4.html` | `nlPrintTopCellFooterComments` |
| `nlPrintTopCellHeader` | `skartistref/chap4.html` | `nlPrintTopCellHeader` |
| `nlPrintTopCellHeaderComments` | `skartistref/chap4.html` | `nlPrintTopCellHeaderComments` |
| `nlSetOption` | `skartistref/chap4.html` | `nlSetOption` |
| `nlTranslateFlatIEPathName` | `skartistref/chap4.html` | `nlTranslateFlatIEPathName` |
| `nlWarning` | `skartistref/chap4.html` | `nlWarning` |


### SIM API

**63 个函数**，文档位置：

- `netlistsimulateref/ossFunctions.html` (62 个函数)
- `oceanref/chap6.html` (1 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `simAddProbeCapByName` | `netlistsimulateref/ossFunctions.html` | `simAddProbeCapByName` |
| `simAddProbeCapByScreen` | `netlistsimulateref/ossFunctions.html` | `simAddProbeCapByScreen` |
| `simAddProbeCapForBusBit` | `netlistsimulateref/ossFunctions.html` | `simAddProbeCapForBusBit` |
| `simCheckExist` | `netlistsimulateref/ossFunctions.html` | `simCheckExist` |
| `simCheckHeader` | `netlistsimulateref/ossFunctions.html` | `simCheckHeader` |
| `simCheckVariables` | `netlistsimulateref/ossFunctions.html` | `simCheckVariables` |
| `simCheckViewConfig` | `netlistsimulateref/ossFunctions.html` | `simCheckViewConfig` |
| `simCleanRun` | `netlistsimulateref/ossFunctions.html` | `simCleanRun` |
| `simDateStamp` | `netlistsimulateref/ossFunctions.html` | `simDateStamp` |
| `simDeleteRunDirFile` | `netlistsimulateref/ossFunctions.html` | `simDeleteRunDirFile` |
| `simDesignVarCdsNameExtName` | `netlistsimulateref/ossFunctions.html` | `simDesignVarCdsNameExtName` |
| `simDesignVarExtNameCdsName` | `netlistsimulateref/ossFunctions.html` | `simDesignVarExtNameCdsName` |
| `simDrain` | `netlistsimulateref/ossFunctions.html` | `simDrain` |
| `simEditFileWithName` | `netlistsimulateref/ossFunctions.html` | `simEditFileWithName` |
| `simExecute` | `netlistsimulateref/ossFunctions.html` | `simExecute` |
| `simFindFile` | `netlistsimulateref/ossFunctions.html` | `simFindFile` |
| `simFlattenWithArgs` | `netlistsimulateref/ossFunctions.html` | `simFlattenWithArgs` |
| `simGetLoginName` | `netlistsimulateref/ossFunctions.html` | `simGetLoginName` |
| `simGetTermList` | `netlistsimulateref/ossFunctions.html` | `simGetTermList` |
| `simIfNoProcedure` | `netlistsimulateref/ossFunctions.html` | `simIfNoProcedure` |
| `simIlSleep` | `netlistsimulateref/ossFunctions.html` | `simIlSleep` |
| `simInWithArgs` | `netlistsimulateref/ossFunctions.html` | `simInWithArgs` |
| `simInitControl` | `netlistsimulateref/ossFunctions.html` | `simInitControl` |
| `simInitEnv` | `netlistsimulateref/ossFunctions.html` | `simInitEnv` |
| `simInitEnvWithArgs` | `netlistsimulateref/ossFunctions.html` | `simInitEnvWithArgs` |
| `simInitRaw` | `netlistsimulateref/ossFunctions.html` | `simInitRaw` |
| `simInitRunDir` | `netlistsimulateref/ossFunctions.html` | `simInitRunDir` |
| `simInitSimulator` | `netlistsimulateref/ossFunctions.html` | `simInitSimulator` |
| `simInstCdsNameExtName` | `netlistsimulateref/ossFunctions.html` | `simInstCdsNameExtName` |
| `simInstExtNameCdsName` | `netlistsimulateref/ossFunctions.html` | `simInstExtNameCdsName` |
| `simJobMonitor` | `netlistsimulateref/ossFunctions.html` | `simJobMonitor` |
| `simLoadNetlisterFiles` | `netlistsimulateref/ossFunctions.html` | `simLoadNetlisterFiles` |
| `simLoadSimulatorFiles` | `netlistsimulateref/ossFunctions.html` | `simLoadSimulatorFiles` |
| `simNetCdsNameExtName` | `netlistsimulateref/ossFunctions.html` | `simNetCdsNameExtName` |
| `simNetExtNameCdsName` | `netlistsimulateref/ossFunctions.html` | `simNetExtNameCdsName` |
| `simNetlistWithArgs` | `netlistsimulateref/ossFunctions.html` | `simNetlistWithArgs` |
| `simNoNetlist` | `netlistsimulateref/ossFunctions.html` | `simNoNetlist` |
| `simOutWithArgs` | `netlistsimulateref/ossFunctions.html` | `simOutWithArgs` |
| `simPostNameConvert` | `netlistsimulateref/ossFunctions.html` | `simPostNameConvert` |
| `simPreNameConvert` | `netlistsimulateref/ossFunctions.html` | `simPreNameConvert` |
| `simPrintEnvironment` | `netlistsimulateref/ossFunctions.html` | `simPrintEnvironment` |
| `simPrintError` | `netlistsimulateref/ossFunctions.html` | `simPrintError` |
| `simPrintErrorLine` | `netlistsimulateref/ossFunctions.html` | `simPrintErrorLine` |
| `simPrintMessage` | `netlistsimulateref/ossFunctions.html` | `simPrintMessage` |
| `simPrintTermList` | `netlistsimulateref/ossFunctions.html` | `simPrintTermList` |
| `simReadNetCapFile` | `netlistsimulateref/ossFunctions.html` | `simReadNetCapFile` |
| `simRunDirInfile` | `netlistsimulateref/ossFunctions.html` | `simRunDirInfile` |
| `simRunDirLoad` | `netlistsimulateref/ossFunctions.html` | `simRunDirLoad` |
| `simRunDirOutfile` | `netlistsimulateref/ossFunctions.html` | `simRunDirOutfile` |
| `simRunNetAndSim` | `netlistsimulateref/ossFunctions.html` | `simRunNetAndSim` |
| `simRunNetAndSimWithArgs` | `netlistsimulateref/ossFunctions.html` | `simRunNetAndSimWithArgs` |
| `simRunNetAndSimWithCmd` | `netlistsimulateref/ossFunctions.html` | `simRunNetAndSimWithCmd` |
| `simSetDef` | `netlistsimulateref/ossFunctions.html` | `simSetDef` |
| `simSetDefWithNoWarn` | `netlistsimulateref/ossFunctions.html` | `simSetDefWithNoWarn` |
| `simStringsToList` | `netlistsimulateref/ossFunctions.html` | `simStringsToList` |
| `simSubProbeCapByName` | `netlistsimulateref/ossFunctions.html` | `simSubProbeCapByName` |
| `simSubProbeCapByScreen` | `netlistsimulateref/ossFunctions.html` | `simSubProbeCapByScreen` |
| `simVertToHoriz` | `netlistsimulateref/ossFunctions.html` | `simVertToHoriz` |
| `simViewFileWithArgs` | `netlistsimulateref/ossFunctions.html` | `simViewFileWithArgs` |
| `simWaveOpen` | `netlistsimulateref/ossFunctions.html` | `simWaveOpen` |
| `simin` | `netlistsimulateref/ossFunctions.html` | `simin` |
| `simout` | `netlistsimulateref/ossFunctions.html` | `simout` |
| `simulator_OCEAN` | `oceanref/chap6.html` | `simulator` |


### ABS API

**61 个函数**，文档位置：

- `abstract/abstract_skill.html` (56 个函数)
- `oceanref/chap10.html` (2 个函数)
- `vivaxlug/appD.html` (1 个函数)
- `"absDeleteBinMoveCellsTo"` (1 个函数)
- `abstract/abstract_skill.html       "absImportOasis"` (1 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `absAbstract` | `abstract/abstract_skill.html` | `absAbstract` |
| `absAttachTechLib` | `abstract/abstract_skill.html` | `absAttachTechLib` |
| `absCopyBinOptions` | `abstract/abstract_skill.html` | `absCopyBinOptions` |
| `absDeleteBin` | `abstract/abstract_skill.html` | `absDeleteBin` |
| `absDeleteBinMoveCellsTo    $abstract/abstract_skill.html` | `"absDeleteBinMoveCellsTo"` | `HTML` |
| `absDeselectAllBins` | `abstract/abstract_skill.html` | `absDeselectAllBins` |
| `absDeselectBin` | `abstract/abstract_skill.html` | `absDeselectBin` |
| `absDeselectBinFrom` | `abstract/abstract_skill.html` | `absDeselectBinFrom` |
| `absDeselectCell` | `abstract/abstract_skill.html` | `absDeselectCell` |
| `absDeselectCellFrom` | `abstract/abstract_skill.html` | `absDeselectCellFrom` |
| `absDeselectCells` | `abstract/abstract_skill.html` | `absDeselectCells` |
| `absDeselectCellsInList` | `abstract/abstract_skill.html` | `absDeselectCellsInList"    HTML` |
| `absDisableUpdate` | `abstract/abstract_skill.html` | `absDisableUpdate` |
| `absDistributeCells` | `abstract/abstract_skill.html` | `absDistributeCells` |
| `absEnableUpdate` | `abstract/abstract_skill.html` | `absEnableUpdate` |
| `absExit` | `abstract/abstract_skill.html` | `absExit` |
| `absExportLEF` | `abstract/abstract_skill.html` | `absExportLEF` |
| `absExportOptions` | `abstract/abstract_skill.html` | `absExportOptions` |
| `absExportReport` | `abstract/abstract_skill.html` | `absExportReport` |
| `absExtract` | `abstract/abstract_skill.html` | `absExtract` |
| `absGetBinOption` | `abstract/abstract_skill.html` | `absGetBinOption` |
| `absGetBinType` | `abstract/abstract_skill.html` | `absGetBinType` |
| `absGetBins` | `abstract/abstract_skill.html` | `absGetBins` |
| `absGetCellProp` | `abstract/abstract_skill.html` | `absGetCellProp` |
| `absGetLibrary` | `abstract/abstract_skill.html` | `absGetLibrary` |
| `absGetOption` | `abstract/abstract_skill.html` | `absGetOption` |
| `absGetSelectedBins` | `abstract/abstract_skill.html` | `absGetSelectedBins` |
| `absGetSelectedCells` | `abstract/abstract_skill.html` | `absGetSelectedCells` |
| `absGetTerminalProp` | `abstract/abstract_skill.html` | `absGetTerminalProp` |
| `absImportCTLF` | `abstract/abstract_skill.html` | `absImportCTLF` |
| `absImportDEF` | `abstract/abstract_skill.html` | `absImportDEF` |
| `absImportGDS` | `abstract/abstract_skill.html` | `absImportGDS` |
| `absImportLEF` | `abstract/abstract_skill.html` | `absImportLEF` |
| `absImportLogical` | `abstract/abstract_skill.html` | `absImportLogical` |
| `absImportOasis` | `abstract/abstract_skill.html       "absImportOasis"` | `HTML` |
| `absImportOptions` | `abstract/abstract_skill.html` | `absImportOptions` |
| `absImportVerilog` | `abstract/abstract_skill.html` | `absImportVerilog` |
| `absMoveSelectedCellsToBin` | `abstract/abstract_skill.html` | `absMoveSelectedCellsToBin` |
| `absNewBin` | `abstract/abstract_skill.html` | `absNewBin` |
| `absPins` | `abstract/abstract_skill.html` | `absPins` |
| `absRenameBin` | `abstract/abstract_skill.html` | `absRenameBin` |
| `absRevalidateSelectedCells` | `abstract/abstract_skill.html` | `absRevalidateSelectedCells` |
| `absSelect` | `abstract/abstract_skill.html` | `absSelect` |
| `absSelectAllBins` | `abstract/abstract_skill.html` | `absSelectAllBins` |
| `absSelectBin` | `abstract/abstract_skill.html` | `absSelectBin` |
| `absSelectBinFrom` | `abstract/abstract_skill.html` | `absSelectBinFrom` |
| `absSelectCell` | `abstract/abstract_skill.html` | `absSelectCell` |
| `absSelectCellFrom` | `abstract/abstract_skill.html` | `absSelectCellFrom` |
| `absSelectCells` | `abstract/abstract_skill.html` | `absSelectCells` |
| `absSelectCellsInList` | `abstract/abstract_skill.html` | `absSelectCellsInList` |
| `absSetBinOption` | `abstract/abstract_skill.html` | `absSetBinOption` |
| `absSetCellProp` | `abstract/abstract_skill.html` | `absSetCellProp` |
| `absSetLibrary` | `abstract/abstract_skill.html` | `absSetLibrary` |
| `absSetOption` | `abstract/abstract_skill.html` | `absSetOption` |
| `absSetTerminalProp` | `abstract/abstract_skill.html` | `absSetTerminalProp` |
| `absSort` | `abstract/abstract_skill.html` | `absSort` |
| `absVerify` | `abstract/abstract_skill.html` | `absVerify` |
| `absVersion` | `abstract/abstract_skill.html` | `absVersion` |
| `abs_OCEAN` | `oceanref/chap10.html` | `abs` |
| `abs_jitter_OCEAN` | `oceanref/chap10.html` | `abs_jitter` |
| `abs_jitter_ViVA_SKILL` | `vivaxlug/appD.html` | `abs_jitter` |


### PAR API

**50 个函数**，文档位置：

- `parasimSKILL/parasimSKILLFunctions.html` (26 个函数)
- `skpcellref/parasimSKILLFunctions.html` (22 个函数)
- `oceanref/chap11.html` (2 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `parCacheFind` | `parasimSKILL/parasimSKILLFunctions.html` | `parCacheFind` |
| `parCacheFind` | `skpcellref/parasimSKILLFunctions.html` | `parCacheFind` |
| `parCacheGet` | `parasimSKILL/parasimSKILLFunctions.html` | `parCacheGet` |
| `parCacheGet` | `skpcellref/parasimSKILLFunctions.html` | `parCacheGet` |
| `parCacheListFilters` | `parasimSKILL/parasimSKILLFunctions.html` | `parCacheListFilters` |
| `parCacheListFilters` | `skpcellref/parasimSKILLFunctions.html` | `parCacheListFilters` |
| `parCacheListModels` | `parasimSKILL/parasimSKILLFunctions.html` | `parCacheListModels` |
| `parCacheListModels` | `skpcellref/parasimSKILLFunctions.html` | `parCacheListModels` |
| `parCachePurge` | `parasimSKILL/parasimSKILLFunctions.html` | `parCachePurge` |
| `parCachePurge` | `skpcellref/parasimSKILLFunctions.html` | `parCachePurge` |
| `parCacheSave` | `parasimSKILL/parasimSKILLFunctions.html` | `parCacheSave` |
| `parCacheSave` | `skpcellref/parasimSKILLFunctions.html` | `parCacheSave` |
| `parDelete` | `parasimSKILL/parasimSKILLFunctions.html` | `parDelete` |
| `parDelete` | `skpcellref/parasimSKILLFunctions.html` | `parDelete` |
| `parFilterCreate` | `parasimSKILL/parasimSKILLFunctions.html` | `parFilterCreate` |
| `parFilterCreate` | `skpcellref/parasimSKILLFunctions.html` | `parFilterCreate` |
| `parFind` | `parasimSKILL/parasimSKILLFunctions.html` | `parFind` |
| `parFind` | `skpcellref/parasimSKILLFunctions.html` | `parFind` |
| `parModelCreateCustom` | `parasimSKILL/parasimSKILLFunctions.html` | `parModelCreateCustom` |
| `parModelCreateCustom` | `skpcellref/parasimSKILLFunctions.html` | `parModelCreateCustom` |
| `parModelCreateNetC` | `parasimSKILL/parasimSKILLFunctions.html` | `parModelCreateNetC` |
| `parModelCreateNetC` | `skpcellref/parasimSKILLFunctions.html` | `parModelCreateNetC` |
| `parModelCreateNetK` | `parasimSKILL/parasimSKILLFunctions.html` | `parModelCreateNetK` |
| `parModelCreateNetK` | `skpcellref/parasimSKILLFunctions.html` | `parModelCreateNetK` |
| `parModelCreateNetL` | `parasimSKILL/parasimSKILLFunctions.html` | `parModelCreateNetL` |
| `parModelCreateNetL` | `skpcellref/parasimSKILLFunctions.html` | `parModelCreateNetL` |
| `parModelCreateNetR` | `parasimSKILL/parasimSKILLFunctions.html` | `parModelCreateNetR` |
| `parModelCreateNetR` | `skpcellref/parasimSKILLFunctions.html` | `parModelCreateNetR` |
| `parModelListSimParams` | `parasimSKILL/parasimSKILLFunctions.html` | `parModelListSimParams` |
| `parModelListSimParams` | `skpcellref/parasimSKILLFunctions.html` | `parModelListSimParams` |
| `parModelListSimSweeps` | `parasimSKILL/parasimSKILLFunctions.html` | `parModelListSimSweeps` |
| `parModelListSimSweeps` | `skpcellref/parasimSKILLFunctions.html` | `parModelListSimSweeps` |
| `parModelUpdateSimParams` | `parasimSKILL/parasimSKILLFunctions.html` | `parModelUpdateSimParams` |
| `parModelUpdateSimParams` | `skpcellref/parasimSKILLFunctions.html` | `parModelUpdateSimParams` |
| `parModelUpdateSimSweeps` | `parasimSKILL/parasimSKILLFunctions.html` | `parModelUpdateSimSweeps` |
| `parModelUpdateSimSweeps` | `skpcellref/parasimSKILLFunctions.html` | `parModelUpdateSimSweeps` |
| `parObjectListFilters` | `parasimSKILL/parasimSKILLFunctions.html` | `parObjectListFilters` |
| `parObjectListFilters` | `skpcellref/parasimSKILLFunctions.html` | `parObjectListFilters` |
| `parObjectListModels` | `parasimSKILL/parasimSKILLFunctions.html` | `parObjectListModels` |
| `parObjectListModels` | `skpcellref/parasimSKILLFunctions.html` | `parObjectListModels` |
| `parRemoveMembers` | `parasimSKILL/parasimSKILLFunctions.html` | `parRemoveMembers` |
| `parRemoveMembers` | `skpcellref/parasimSKILLFunctions.html` | `parRemoveMembers` |
| `parResetAllParams` | `parasimSKILL/parasimSKILLFunctions.html` | `parResetAllParams` |
| `parResetAllParams` | `skpcellref/parasimSKILLFunctions.html` | `parResetAllParams` |
| `parResetParams` | `parasimSKILL/parasimSKILLFunctions.html` | `parResetParams` |
| `parSetNote` | `parasimSKILL/parasimSKILLFunctions.html` | `parSetNote` |
| `parUpdateMembers` | `parasimSKILL/parasimSKILLFunctions.html` | `parUpdateMembers` |
| `parUpdateParams` | `parasimSKILL/parasimSKILLFunctions.html` | `parUpdateParams` |
| `paramAnalysis_OCEAN` | `oceanref/chap11.html` | `paramAnalysis` |
| `paramRun_OCEAN` | `oceanref/chap11.html` | `paramRun` |


### ROD API

**47 个函数**，文档位置：

- `rodskillref/chap1.html` (35 个函数)
- `rodskillref/chap2.html` (12 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `rodAddMPPChopHole` | `rodskillref/chap1.html` | `rodAddMPPChopHole` |
| `rodAddPoints` | `rodskillref/chap1.html` | `rodAddPoints` |
| `rodAddSubPart` | `rodskillref/chap1.html` | `rodAddSubPart` |
| `rodAddToX` | `rodskillref/chap1.html` | `rodAddToX` |
| `rodAddToY` | `rodskillref/chap1.html` | `rodAddToY` |
| `rodAlign` | `rodskillref/chap1.html` | `rodAlign` |
| `rodAssignHandleToParameter` | `rodskillref/chap1.html` | `rodAssignHandleToParameter"    HTML` |
| `rodCheck` | `rodskillref/chap1.html` | `rodCheck` |
| `rodCheckAllMPPsInCellView` | `rodskillref/chap1.html` | `rodCheckAllMPPsInCellView` |
| `rodCheckMPPs` | `rodskillref/chap1.html` | `rodCheckMPPs` |
| `rodCoordBisect` | `rodskillref/chap2.html` | `rodCoordBisect` |
| `rodCoordCreate` | `rodskillref/chap2.html` | `rodCoordCreate` |
| `rodCoordDefineGrid` | `rodskillref/chap2.html` | `rodCoordDefineGrid` |
| `rodCoordFix` | `rodskillref/chap2.html` | `rodCoordFix` |
| `rodCoordGetGrid` | `rodskillref/chap2.html` | `rodCoordGetGrid` |
| `rodCoordIsOnGrid` | `rodskillref/chap2.html` | `rodCoordIsOnGrid` |
| `rodCoordParseString` | `rodskillref/chap2.html` | `rodCoordParseString` |
| `rodCoordPartition` | `rodskillref/chap2.html` | `rodCoordPartition` |
| `rodCoordSnap` | `rodskillref/chap2.html` | `rodCoordSnap` |
| `rodCoordToFloat` | `rodskillref/chap2.html` | `rodCoordToFloat` |
| `rodCoordToInt` | `rodskillref/chap2.html` | `rodCoordToInt` |
| `rodCoordToString` | `rodskillref/chap2.html` | `rodCoordToString` |
| `rodCreateHandle` | `rodskillref/chap1.html` | `rodCreateHandle` |
| `rodCreatePath` | `rodskillref/chap1.html` | `rodCreatePath` |
| `rodCreatePolygon` | `rodskillref/chap1.html` | `rodCreatePolygon` |
| `rodCreateRect` | `rodskillref/chap1.html` | `rodCreateRect` |
| `rodDeleteHandle` | `rodskillref/chap1.html` | `rodDeleteHandle` |
| `rodDeleteSubPart` | `rodskillref/chap1.html` | `rodDeleteSubPart` |
| `rodFillBBoxWithRects` | `rodskillref/chap1.html` | `rodFillBBoxWithRects` |
| `rodFillWithRects` | `rodskillref/chap1.html` | `rodFillWithRects` |
| `rodGetBBox` | `rodskillref/chap1.html` | `rodGetBBox` |
| `rodGetHandle` | `rodskillref/chap1.html` | `rodGetHandle` |
| `rodGetNamedShapes` | `rodskillref/chap1.html` | `rodGetNamedShapes` |
| `rodGetObj` | `rodskillref/chap1.html` | `rodGetObj` |
| `rodGetSubPart` | `rodskillref/chap1.html` | `rodGetSubPart` |
| `rodIsFigNameUnused` | `rodskillref/chap1.html` | `rodIsFigNameUnused` |
| `rodIsHandle` | `rodskillref/chap1.html` | `rodIsHandle` |
| `rodIsMasterChoppable` | `rodskillref/chap1.html` | `rodIsMasterChoppable` |
| `rodIsObj` | `rodskillref/chap1.html` | `rodIsObj` |
| `rodNameObject` | `rodskillref/chap1.html` | `rodNameObject` |
| `rodNameShape` | `rodskillref/chap1.html` | `rodNameShape` |
| `rodPointX` | `rodskillref/chap1.html` | `rodPointX` |
| `rodPointY` | `rodskillref/chap1.html` | `rodPointY` |
| `rodSetMasterChoppable` | `rodskillref/chap1.html` | `rodSetMasterChoppable` |
| `rodSubPoints` | `rodskillref/chap1.html` | `rodSubPoints` |
| `rodUnAlign` | `rodskillref/chap1.html` | `rodUnAlign` |
| `rodUnNameShape` | `rodskillref/chap1.html` | `rodUnNameShape` |


### VSA API

**45 个函数**，文档位置：

- `voltusFIXL/appB_functions.html` (22 个函数)
- `vpsl/emrulespec.html` (21 个函数)
- `voltusFIXL/appB_functions.html         "vsaShowAllResistors"` (1 个函数)
- `vpsl/voltagesrc.html` (1 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `vsaConnectToVsaplot` | `vpsl/emrulespec.html` | `vsaConnectToVsaplot` |
| `vsaCreateMarker` | `voltusFIXL/appB_functions.html` | `vsaCreateMarker` |
| `vsaDbType` | `vpsl/emrulespec.html` | `vsaDbType` |
| `vsaDefVariable` | `vpsl/emrulespec.html` | `vsaDefVariable` |
| `vsaEMGetQRCDirAndRunName` | `vpsl/emrulespec.html` | `vsaEMGetQRCDirAndRunName` |
| `vsaEMGetSimDirAndAnalysisType` | `vpsl/emrulespec.html` | `vsaEMGetSimDirAndAnalysisType" HTML` |
| `vsaError` | `vpsl/emrulespec.html` | `vsaError` |
| `vsaGetNode` | `vpsl/emrulespec.html` | `vsaGetNode` |
| `vsaGetR` | `vpsl/emrulespec.html` | `vsaGetR` |
| `vsaGetVariable` | `vpsl/emrulespec.html` | `vsaGetVariable` |
| `vsaIRGetSimDirAndAnalysisType` | `vpsl/emrulespec.html` | `vsaIRGetSimDirAndAnalysisType" HTML` |
| `vsaLoadEM` | `voltusFIXL/appB_functions.html` | `vsaLoadEM` |
| `vsaLoadIR` | `voltusFIXL/appB_functions.html` | `vsaLoadIR` |
| `vsaLoadNets` | `voltusFIXL/appB_functions.html` | `vsaLoadNets` |
| `vsaLoadSecondaryLayers` | `voltusFIXL/appB_functions.html` | `vsaLoadSecondaryLayers` |
| `vsaNetlistProc` | `vpsl/voltagesrc.html` | `vsaNetlistProc` |
| `vsaNodeGetIR` | `vpsl/emrulespec.html` | `vsaNodeGetIR` |
| `vsaOpenLayout` | `voltusFIXL/appB_functions.html` | `vsaOpenLayout` |
| `vsaRegisterEMDataFile` | `vpsl/emrulespec.html` | `vsaRegisterEMDataFile` |
| `vsaRegisterLayerMapFile` | `vpsl/emrulespec.html` | `vsaRegisterLayerMapFile` |
| `vsaRegisterQrcTechFile` | `vpsl/emrulespec.html` | `vsaRegisterQrcTechFile` |
| `vsaResGetIavg` | `vpsl/emrulespec.html` | `vsaResGetIavg` |
| `vsaResGetIpeak` | `vpsl/emrulespec.html` | `vsaResGetIpeak` |
| `vsaResGetIrms` | `vpsl/emrulespec.html` | `vsaResGetIrms` |
| `vsaResGetLayer` | `vpsl/emrulespec.html` | `vsaResGetLayer` |
| `vsaResGetX` | `vpsl/emrulespec.html` | `vsaResGetX` |
| `vsaResGetY` | `vpsl/emrulespec.html` | `vsaResGetY` |
| `vsaSelectFailedNets` | `voltusFIXL/appB_functions.html` | `vsaSelectFailedNets` |
| `vsaSetDfiiLayerMapFileName` | `voltusFIXL/appB_functions.html` | `vsaSetDfiiLayerMapFileName"    HTML` |
| `vsaSetEMIRConfig` | `voltusFIXL/appB_functions.html` | `vsaSetEMIRConfig` |
| `vsaSetEMLayerMapFileName` | `voltusFIXL/appB_functions.html` | `vsaSetEMLayerMapFileName` |
| `vsaSetEMOnlyICTFile` | `voltusFIXL/appB_functions.html` | `vsaSetEMOnlyICTFile` |
| `vsaSetEMPlot` | `voltusFIXL/appB_functions.html` | `vsaSetEMPlot` |
| `vsaSetEMResultsFile` | `voltusFIXL/appB_functions.html` | `vsaSetEMResultsFile` |
| `vsaSetEMTechFileName` | `voltusFIXL/appB_functions.html` | `vsaSetEMTechFileName` |
| `vsaSetEMTypes` | `voltusFIXL/appB_functions.html` | `vsaSetEMTypes` |
| `vsaSetIRPlot` | `voltusFIXL/appB_functions.html` | `vsaSetIRPlot` |
| `vsaSetIRResultsFile` | `voltusFIXL/appB_functions.html` | `vsaSetIRResultsFile` |
| `vsaSetIRThreshold` | `voltusFIXL/appB_functions.html` | `vsaSetIRThreshold` |
| `vsaSetInputType` | `voltusFIXL/appB_functions.html` | `vsaSetInputType` |
| `vsaSetLRPShortedLayers` | `voltusFIXL/appB_functions.html` | `vsaSetLRPShortedLayers` |
| `vsaSetLayersToMergeDuringResultsLoading` | `voltusFIXL/appB_functions.html` | `vsaSetLayersToMergeDuringResultsLoading` |
| `vsaSetQRCData` | `voltusFIXL/appB_functions.html` | `vsaSetQRCData` |
| `vsaShowAllResistors` | `voltusFIXL/appB_functions.html         "vsaShowAllResistors"` | `HTML` |
| `vsaWarn` | `vpsl/emrulespec.html` | `vsaWarn` |


### GE API

**44 个函数**，文档位置：

- `skdfref/chap1.html` (22 个函数)
- `skoopref/genericfunc.html` (7 个函数)
- `skdevref/debug.html` (4 个函数)
- `skdevref/context.html` (3 个函数)
- `oceanref/chap7.html` (2 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `geAddHilightCurvedPath` | `skdfref/chap1.html` | `geAddHilightCurvedPath` |
| `geAddHilightCurvedPolygon` | `skdfref/chap1.html` | `geAddHilightCurvedPolygon` |
| `geAddHilightSlicedCircle` | `skdfref/chap1.html` | `geAddHilightSlicedCircle` |
| `geAddHilightSlicedDonut` | `skdfref/chap1.html` | `geAddHilightSlicedDonut` |
| `geClearIgnoreProp` | `skdfref/chap1.html` | `geClearIgnoreProp` |
| `geClearNetNameDisplayFilter` | `skdfref/chap1.html` | `geClearNetNameDisplayFilter` |
| `geClearProbeNetFilter` | `skdfref/chap1.html` | `geClearProbeNetFilter` |
| `geDeselectFigs` | `skdfref/chap1.html` | `geDeselectFigs` |
| `geEnableNetNameDisplay` | `skdfref/chap1.html` | `geEnableNetNameDisplay` |
| `geGetNetNameDisplayFilter` | `skdfref/chap1.html` | `geGetNetNameDisplayFilter` |
| `geGetProbeNetFilter` | `skdfref/chap1.html` | `geGetProbeNetFilter` |
| `geIsNetNameDisplayActiveOnWindow` | `skdfref/chap1.html` | `geIsNetNameDisplayActiveOnWindow` |
| `geIsNetNameDisplayEnabled` | `skdfref/chap1.html` | `geIsNetNameDisplayEnabled` |
| `geIsObjectPartiallySelected` | `skdfref/chap1.html` | `geIsObjectPartiallySelected` |
| `geNetNameDisplayOptionForm` | `skdfref/chap1.html` | `geNetNameDisplayOptionForm` |
| `geSaveNetNameDisplayFilter` | `skdfref/chap1.html` | `geSaveNetNameDisplayFilter` |
| `geSaveProbeNetFilter` | `skdfref/chap1.html` | `geSaveProbeNetFilter` |
| `geSelectBy2PointsLine` | `skdfref/chap1.html` | `geSelectBy2PointsLine` |
| `geSetNetNameDisplayFilter` | `skdfref/chap1.html` | `geSetNetNameDisplayFilter` |
| `geSetProbeNetFilter` | `skdfref/chap1.html` | `geSetProbeNetFilter` |
| `geSwitchInContext` | `skdfref/chap1.html` | `geSwitchInContext` |
| `geToggleDisplayResolution` | `skdfref/chap1.html` | `geToggleDisplayResolution"    HTML` |
| `getAllLoadedFiles` | `skdevref/debug.html` | `getAllLoadedFiles` |
| `getApplicableMethods` | `skoopref/genericfunc.html` | `getApplicableMethods` |
| `getAsciiWave_OCEAN` | `oceanref/chap8.html` | `getAsciiWave` |
| `getAsciiWave_ViVA_SKILL` | `vivaxlug/appD.html` | `getAsciiWave` |
| `getCallingFunction` | `skdevref/debug.html` | `getCallingFunction` |
| `getCompatContextVersion` | `skdevref/context.html` | `getCompatContextVersion` |
| `getCurSaveContextVersion` | `skdevref/context.html` | `getCurSaveContextVersion` |
| `getData_OCEAN` | `oceanref/chap7.html` | `getData` |
| `getDependents` | `skoopref/dmp.html` | `getDependents` |
| `getFunctions` | `skdevref/debug.html` | `getFunctions` |
| `getGFbyClass` | `skdevref/debug.html` | `getGFbyClass` |
| `getGFbyClass` | `skoopref/genericfunc.html` | `getGFbyClass` |
| `getGFproxy` | `skoopref/genericfunc.html` | `getGFproxy` |
| `getMethodName` | `skoopref/genericfunc.html` | `getMethodName` |
| `getMethodRole` | `skoopref/genericfunc.html` | `getMethodRole` |
| `getMethodSpec` | `skoopref/genericfunc.html` | `getMethodSpec` |
| `getMethodSpecializers` | `skoopref/genericfunc.html` | `getMethodSpecializers` |
| `getMuffleWarnings` | `sklangref/core.html` | `getMuffleWarnings` |
| `getNativeContextVersion` | `skdevref/context.html` | `getNativeContextVersion` |
| `getResult_OCEAN` | `oceanref/chap7.html` | `getResult` |
| `getSimRunInfo` | `maeSKILLref/maestroSKILL.html` | `getSimRunInfo` |
| `gets_OCEAN` | `oceanref/chap14.html` | `gets` |


### GPE API

**39 个函数**，文档位置：

- `sklayoutref/modgen.html` (23 个函数)
- `sklayoutref/modgen.html         "gpeSetGridText"` (1 个函数)
- `sklayoutref/modgen.html         "gpeSetOrientText"` (1 个函数)
- `sklayoutref/modgen.html         "gpeAddDummy"` (1 个函数)
- `sklayoutref/modgen.html         "gpeSboxp"` (1 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `gpeAddDummy` | `sklayoutref/modgen.html         "gpeAddDummy"` | `HTML` |
| `gpeAddDummySurround` | `sklayoutref/modgen.html` | `gpeAddDummySurround` |
| `gpeAddInstance` | `sklayoutref/modgen.html` | `gpeAddInstance` |
| `gpeAddMatchGroups` | `sklayoutref/modgen.html         "gpeAddMatchGroups"` | `HTML` |
| `gpeAddStrapEntries` | `sklayoutref/modgen.html         "gpeAddStrapEntries"` | `HTML` |
| `gpeCancelSandbox` | `sklayoutref/modgen.html` | `gpeCancelSandbox"        HTML` |
| `gpeClearMatchGroups` | `sklayoutref/modgen.html         "gpeClearMatchGroups"` | `HTML` |
| `gpeClearPresetGenerators` | `sklayoutref/modgen.html` | `gpeClearPresetGenerators` |
| `gpeClearTopo` | `sklayoutref/modgen.html         "gpeClearTopo"` | `HTML` |
| `gpeCopyColAbutment` | `sklayoutref/modgen.html` | `gpeCopyColAbutment` |
| `gpeCopyRowAbutment` | `sklayoutref/modgen.html` | `gpeCopyRowAbutment` |
| `gpeCreateAlignmentAndSpacing` | `sklayoutref/modgen.html        "gpeCreateAlignmentAndSpacing"` | `HTML` |
| `gpeDeleteSandbox` | `sklayoutref/modgen.html         "gpeDeleteSandbox"` | `HTML` |
| `gpeExtractReuseTemplate` | `sklayoutref/modgen.html` | `gpeExtractReuseTemplate` |
| `gpeFinishSandbox` | `sklayoutref/modgen.html         "gpeFinishSandbox"` | `HTML` |
| `gpeGetGridEntry` | `sklayoutref/modgen.html        "gpeGetGridEntry"` | `HTML` |
| `gpeGetGridSelection` | `sklayoutref/modgen.html` | `gpeGetGridSelection` |
| `gpeGetGridValue` | `sklayoutref/modgen.html` | `gpeGetGridValue` |
| `gpeGetSelection` | `sklayoutref/modgen.html` | `gpeGetSelection` |
| `gpeInsertEmptyColumns` | `sklayoutref/modgen.html        "gpeInsertEmptyColumns"` | `HTML` |
| `gpeInsertEmptyRows` | `sklayoutref/modgen.html        "gpeInsertEmptyRows"` | `HTML` |
| `gpeIsPresetGenDisplayable` | `sklayoutref/modgen.html` | `gpeIsPresetGenDisplayable` |
| `gpeIsRegisteredPresetGen` | `sklayoutref/modgen.html` | `gpeIsRegisteredPresetGen` |
| `gpeMove` | `sklayoutref/modgen.html` | `gpeMove` |
| `gpeRegisterPresetGen` | `sklayoutref/modgen.html` | `gpeRegisterPresetGen` |
| `gpeRemoveInstance` | `sklayoutref/modgen.html    "gpeRemoveInstance"` | `HTML` |
| `gpeRunPresetGen` | `sklayoutref/modgen.html` | `gpeRunPresetGen` |
| `gpeSboxp` | `sklayoutref/modgen.html         "gpeSboxp"` | `HTML` |
| `gpeSelect` | `sklayoutref/modgen.html` | `gpeSelect` |
| `gpeSetGridText` | `sklayoutref/modgen.html         "gpeSetGridText"` | `HTML` |
| `gpeSetGridValue` | `sklayoutref/modgen.html` | `gpeSetGridValue` |
| `gpeSetGridValue` | `sklayoutref/modgen.html` | `gpeSetGridValue` |
| `gpeSetOrientText` | `sklayoutref/modgen.html         "gpeSetOrientText"` | `HTML` |
| `gpeSetSize` | `sklayoutref/modgen.html` | `gpeSetSize` |
| `gpeStacksAreCompressed` | `sklayoutref/modgen.html` | `gpeStacksAreCompressed"        HTML` |
| `gpeStacksCompress` | `sklayoutref/modgen.html` | `gpeStacksCompress` |
| `gpeStacksUncompress` | `sklayoutref/modgen.html` | `gpeStacksUncompress` |
| `gpeStartSandbox` | `sklayoutref/modgen.html      "gpeStartSandbox"` | `HTML` |
| `gpeUnregisterPresetGen` | `sklayoutref/modgen.html` | `gpeUnregisterPresetGen` |


### AMS API

**38 个函数**，文档位置：

- `amsskillref/amsnetlisting.html` (30 个函数)
- `amsskillref/amsdesigner.html` (7 个函数)
- `"amsUpdateTextviews"` (1 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `amsCheckCV` | `amsskillref/amsdesigner.html` | `amsCheckCV` |
| `amsError` | `amsskillref/amsnetlisting.html` | `amsError` |
| `amsGetInstanceName` | `amsskillref/amsnetlisting.html` | `amsGetInstanceName` |
| `amsGetNetlister` | `amsskillref/amsnetlisting.html` | `amsGetNetlister` |
| `amsGetPortExpr` | `amsskillref/amsnetlisting.html` | `amsGetPortExpr` |
| `amsGetUniqueName` | `amsskillref/amsnetlisting.html` | `amsGetUniqueName` |
| `amsInfo` | `amsskillref/amsnetlisting.html` | `amsInfo` |
| `amsIsPresent` | `amsskillref/amsdesigner.html` | `amsIsPresent` |
| `amsMapName` | `amsskillref/amsnetlisting.html` | `amsMapName` |
| `amsMtlinePrintParams` | `amsskillref/amsnetlisting.html` | `amsMtlinePrintParams` |
| `amsMtlineTermOrder` | `amsskillref/amsnetlisting.html` | `amsMtlineTermOrder` |
| `amsNetlist` | `amsskillref/amsdesigner.html` | `amsNetlist` |
| `amsNportTermOrder` | `amsskillref/amsnetlisting.html` | `amsNportTermOrder` |
| `amsPrint` | `amsskillref/amsnetlisting.html` | `amsPrint` |
| `amsPrintAlias` | `amsskillref/amsnetlisting.html` | `amsPrintAlias` |
| `amsPrintAliases` | `amsskillref/amsnetlisting.html` | `amsPrintAliases` |
| `amsPrintAttribute` | `amsskillref/amsnetlisting.html` | `amsPrintAttribute` |
| `amsPrintAttributes` | `amsskillref/amsnetlisting.html` | `amsPrintAttributes` |
| `amsPrintIO` | `amsskillref/amsnetlisting.html` | `amsPrintIO` |
| `amsPrintIOs` | `amsskillref/amsnetlisting.html` | `amsPrintIOs` |
| `amsPrintInstance` | `amsskillref/amsnetlisting.html` | `amsPrintInstance` |
| `amsPrintInstanceMasterName` | `amsskillref/amsnetlisting.html` | `amsPrintInstanceMasterName"    HTML` |
| `amsPrintInstanceParameter` | `amsskillref/amsnetlisting.html` | `amsPrintInstanceParameter` |
| `amsPrintInstanceParameters` | `amsskillref/amsnetlisting.html` | `amsPrintInstanceParameters"    HTML` |
| `amsPrintInstancePorts` | `amsskillref/amsnetlisting.html` | `amsPrintInstancePorts` |
| `amsPrintParameter` | `amsskillref/amsnetlisting.html` | `amsPrintParameter` |
| `amsPrintParameters` | `amsskillref/amsnetlisting.html` | `amsPrintParameters` |
| `amsPrintPort` | `amsskillref/amsnetlisting.html` | `amsPrintPort` |
| `amsPrintPorts` | `amsskillref/amsnetlisting.html` | `amsPrintPorts` |
| `amsPrintWire` | `amsskillref/amsnetlisting.html` | `amsPrintWire` |
| `amsPrintWires` | `amsskillref/amsnetlisting.html` | `amsPrintWires` |
| `amsProcessCellViews` | `amsskillref/amsdesigner.html` | `amsProcessCellViews` |
| `amsSpectreToVams` | `amsskillref/amsnetlisting.html` | `amsSpectreToVams` |
| `amsUIOptionsForm` | `amsskillref/amsdesigner.html` | `amsUIOptionsForm` |
| `amsUIRunNetlisterForm` | `amsskillref/amsdesigner.html` | `amsUIRunNetlisterForm` |
| `amsUpdateTextviews` | `amsskillref/amsdesigner.html` | `amsUpdateTextviews` |
| `amsUpdateTextviews       $skartistref/chap16.html` | `"amsUpdateTextviews"` | `HTML` |
| `amsWarning` | `amsskillref/amsnetlisting.html` | `amsWarning` |


### AEL API

**34 个函数**，文档位置：

- `aelref/chap2.html` (30 个函数)
- `parasimSKILL/parasimSKILLFunctions.html` (2 个函数)
- `skpcellref/parasimSKILLFunctions.html` (2 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `aelCheckRange` | `aelref/chap2.html` | `aelCheckRange` |
| `aelDisplayOPParam` | `parasimSKILL/parasimSKILLFunctions.html` | `aelDisplayOPParam` |
| `aelDisplayOPParam` | `skpcellref/parasimSKILLFunctions.html` | `aelDisplayOPParam` |
| `aelEngNotation` | `aelref/chap2.html` | `aelEngNotation` |
| `aelEnvCompile` | `aelref/chap2.html` | `aelEnvCompile` |
| `aelEnvCreate` | `aelref/chap2.html` | `aelEnvCreate` |
| `aelEnvExecute` | `aelref/chap2.html` | `aelEnvExecute` |
| `aelEnvFreeCompExpr` | `aelref/chap2.html` | `aelEnvFreeCompExpr` |
| `aelEnvGetErrStr` | `aelref/chap2.html` | `aelEnvGetErrStr` |
| `aelEnvGetGlobal` | `aelref/chap2.html` | `aelEnvGetGlobal` |
| `aelEnvGetStr` | `aelref/chap2.html` | `aelEnvGetStr` |
| `aelEnvInterpret` | `aelref/chap2.html` | `aelEnvInterpret` |
| `aelEnvListDeferredFuncs` | `aelref/chap2.html` | `aelEnvListDeferredFuncs` |
| `aelEnvListDeferredGlobals` | `aelref/chap2.html` | `aelEnvListDeferredGlobals` |
| `aelEnvListExprFuncs` | `aelref/chap2.html` | `aelEnvListExprFuncs` |
| `aelEnvListExprGlobals` | `aelref/chap2.html` | `aelEnvListExprGlobals` |
| `aelEnvListFuncs` | `aelref/chap2.html` | `aelEnvListFuncs` |
| `aelEnvListGlobals` | `aelref/chap2.html` | `aelEnvListGlobals` |
| `aelEnvListGlobalsValues` | `aelref/chap2.html` | `aelEnvListGlobalsValues` |
| `aelEnvName` | `aelref/chap2.html` | `aelEnvName` |
| `aelEnvSetGlobalList` | `aelref/chap2.html` | `aelEnvSetGlobalList` |
| `aelEnvSetGlobals` | `aelref/chap2.html` | `aelEnvSetGlobals` |
| `aelGetSignifDigits` | `aelref/chap2.html` | `aelGetSignifDigits` |
| `aelNumber` | `aelref/chap2.html` | `aelNumber` |
| `aelPopSignifDigits` | `aelref/chap2.html` | `aelPopSignifDigits` |
| `aelPopSignifdigits` | `aelref/chap2.html` | `aelPopSignifdigits` |
| `aelPushSignifDigits` | `aelref/chap2.html` | `aelPushSignifDigits` |
| `aelSetLineage` | `aelref/chap2.html` | `aelSetLineage` |
| `aelSignum` | `aelref/chap2.html` | `aelSignum` |
| `aelStrDblNotation` | `aelref/chap2.html` | `aelStrDblNotation` |
| `aelSuffixNotation` | `aelref/chap2.html` | `aelSuffixNotation` |
| `aelSuffixWithUnits` | `aelref/chap2.html` | `aelSuffixWithUnits` |
| `aelSumOPParam` | `parasimSKILL/parasimSKILLFunctions.html` | `aelSumOPParam` |
| `aelSumOPParam` | `skpcellref/parasimSKILLFunctions.html` | `aelSumOPParam` |


### TECH API

**34 个函数**，文档位置：

- `sktechfile/chap14.html` (6 个函数)
- `sktechfile/chap3.html` (5 个函数)
- `sktechfile/chap9.html` (3 个函数)
- `sktechfile/chap1.html` (1 个函数)
- `sktechfile/chap7.html` (1 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `techCreateFingerDef` | `sktechfile/chap17.html` | `techCreateFingerDef` |
| `techCreateGenViaDef` | `sktechfile/chap8.html               “techCreateGenViaDef"` | `HTML` |
| `techCreateGenViaVariant` | `sktechfile/chap8.html               “techCreateGenViaVariant"` | `HTML` |
| `techCreateWaveguideDef` | `sktechfile/chap9.html` | `techCreateWaveguideDef` |
| `techCreateWireProfile` | `sktechfile/chap17.html             "techCreateWireProfile"` | `HTML` |
| `techCreateWireProfileGroup` | `sktechfile/chap17.html             "techCreateWireProfileGroup"` | `HTML` |
| `techDeleteFingerDef` | `sktechfile/chap17.html         "techDeleteFingerDef"` | `HTML` |
| `techDeleteRelatedSnapPatterns` | `sktechfile/chap14.html` | `techDeleteRelatedSnapPatterns` |
| `techDeleteWaveguideDef` | `sktechfile/chap9.html` | `techDeleteWaveguideDef` |
| `techDeleteWidthSpacingPattern` | `sktechfile/chap14.html` | `techDeleteWidthSpacingPattern` |
| `techDeleteWidthSpacingPatternGroup` | `sktechfile/chap14.html` | `techDeleteWidthSpacingPatternGroup` |
| `techDeleteWireProfile` | `sktechfile/chap17.html             "techDeleteWireProfile"` | `HTML` |
| `techDeleteWireProfileGroup` | `sktechfile/chap17.html             "techDeleteWireProfileGroup"` | `HTML` |
| `techExportWireProfileSet` | `sktechfile/chap17.html             "techExportWireProfileSet"` | `HTML` |
| `techFindWaveguideDefByLP` | `sktechfile/chap9.html` | `techFindWaveguideDefByLP` |
| `techFindWireProfile` | `sktechfile/chap17.html             "techFindWireProfile"` | `HTML` |
| `techFindWireProfileGroup` | `sktechfile/chap17.html             "techFindWireProfileGroup"` | `HTML` |
| `techGetCellViewSiteDefs` | `sktechfile/chap7.html` | `techGetCellViewSiteDefs` |
| `techGetFabricType` | `sktechfile/chap2.html              "techGetFabricType"` | `HTML` |
| `techGetLPProp` | `sktechfile/chap3.html` | `techGetLPProp` |
| `techGetLPProp` | `sktechfile/chap3.html` | `techGetLPProp` |
| `techGetLayerAnalysisAttribute` | `sktechfile/chap3.html` | `techGetLayerAnalysisAttribute" HTML` |
| `techGetTrimmedLayers` | `sktechfile/chap15.html               "techGetTrimmedLayers"` | `HTML` |
| `techGetWidthSpacingPatternAllowedRepeatMode` | `sktechfile/chap14.html` | `techGetWidthSpacingPatternAllowedRepeatMode` |
| `techGetWidthSpacingPatternDefaultRepeatMode` | `sktechfile/chap14.html` | `techGetWidthSpacingPatternDefaultRepeatMode` |
| `techHasLayerAnalysisAttribute` | `sktechfile/chap3.html` | `techHasLayerAnalysisAttribute" HTML` |
| `techHasWaveguideDefMinBendRadius    $sktechfile/chap9.html` | `"techHasWaveguideDefMinBendRadius"` | `HTML` |
| `techImportWireProfileSet` | `sktechfile/chap17.html             "techImportWireProfileSet"` | `HTML` |
| `techSaveTechFile` | `sktechfile/chap1.html` | `techSaveTechFile` |
| `techSetFabricType` | `sktechfile/chap2.html              "techSetFabricType"` | `HTML` |
| `techSetLayerAnalysisAttribute` | `sktechfile/chap3.html` | `techSetLayerAnalysisAttribute" HTML` |
| `techSetWaveguideDefMinBendRadius    $sktechfile/chap9.html` | `"techSetWaveguideDefMinBendRadius"` | `HTML` |
| `techSetWidthSpacingPatternRepeatMode` | `sktechfile/chap14.html` | `techSetWidthSpacingPatternRepeatMode` |
| `techSupportsLayerAnalysisAttributes` | `sktechfile/chap3.html              "techSupportsLayerAnalysisAttributes"` | `HTML` |


### MG API

**33 个函数**，文档位置：

- `sklayoutref/modgen.html` (19 个函数)
- `sklayoutref/modgen.html    "mgGetStrapDirection"` (1 个函数)
- `sklayoutref/modgen.html    "mgSetStrapLongOffset2"` (1 个函数)
- `sklayoutref/modgen.html    "mgGetStrapLongOffset2"` (1 个函数)
- `sklayoutref/modgen.html    "mgSetStrapHasDirection"` (1 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `mgAddShapeToTopo` | `sklayoutref/modgen.html` | `mgAddShapeToTopo` |
| `mgAddTopologyToModgen` | `sklayoutref/modgen.html` | `mgAddTopologyToModgen` |
| `mgCreateMatchGroupInModgen` | `sklayoutref/modgen.html` | `mgCreateMatchGroupInModgen` |
| `mgFGREnterHandEdit` | `sklayoutref/modgen.html` | `mgFGREnterHandEdit` |
| `mgFGRExitHandEdit` | `sklayoutref/modgen.html` | `mgFGRExitHandEdit` |
| `mgFGRIsHandEdit` | `sklayoutref/modgen.html` | `mgFGRIsHandEdit` |
| `mgGetChannelTrunks` | `sklayoutref/modgen.html    "mgGetChannelTrunks"` | `HTML` |
| `mgGetIsLocalTrunk` | `sklayoutref/modgen.html` | `mgGetIsLocalTrunk` |
| `mgGetModgenConstraintFromTopology` | `sklayoutref/modgen.html` | `mgGetModgenConstraintFromTopology` |
| `mgGetModgenFigGroupFromTopology` | `sklayoutref/modgen.html` | `mgGetModgenFigGroupFromTopology` |
| `mgGetStrapDirection` | `sklayoutref/modgen.html    "mgGetStrapDirection"` | `HTML` |
| `mgGetStrapHasDirection` | `sklayoutref/modgen.html    "mgGetStrapHasDirection"` | `HTML` |
| `mgGetStrapHasOffset` | `sklayoutref/modgen.html    "mgGetStrapHasOffset"` | `HTML` |
| `mgGetStrapLongOffset1` | `sklayoutref/modgen.html    "mgGetStrapLongOffset1"` | `HTML` |
| `mgGetStrapLongOffset2` | `sklayoutref/modgen.html    "mgGetStrapLongOffset2"` | `HTML` |
| `mgGetStrapOffset` | `sklayoutref/modgen.html    "mgGetStrapOffset"` | `HTML` |
| `mgGetTopoShapes` | `sklayoutref/modgen.html` | `mgGetTopoShapes` |
| `mgGetTopoTrunkShapes` | `sklayoutref/modgen.html` | `mgGetTopoTrunkShapes` |
| `mgGetTrunkChannel` | `sklayoutref/modgen.html` | `mgGetTrunkChannel` |
| `mgGetTrunkRefLPPEnclosure` | `sklayoutref/modgen.html` | `mgGetTrunkRefLPPEnclosure` |
| `mgGetTrunkTopo` | `sklayoutref/modgen.html    "mgGetTrunkTopo"` | `HTML` |
| `mgIsTopologyInsideModgen` | `sklayoutref/modgen.html` | `mgIsTopologyInsideModgen` |
| `mgModgenHasTopology` | `sklayoutref/modgen.html` | `mgModgenHasTopology` |
| `mgRegenerateModgen` | `sklayoutref/modgen.html` | `mgRegenerateModgen` |
| `mgRemoveTopologyFromModgen` | `sklayoutref/modgen.html` | `mgRemoveTopologyFromModgen` |
| `mgSetIsLocalTrunk` | `sklayoutref/modgen.html` | `mgSetIsLocalTrunk` |
| `mgSetRowRoutingChannelWidth` | `sklayoutref/modgen.html` | `mgSetRowRoutingChannelWidth` |
| `mgSetStrapDirection` | `sklayoutref/modgen.html    "mgSetStrapDirection"` | `HTML` |
| `mgSetStrapHasDirection` | `sklayoutref/modgen.html    "mgSetStrapHasDirection"` | `HTML` |
| `mgSetStrapHasOffset` | `sklayoutref/modgen.html    "mgSetStrapHasOffset"` | `HTML` |
| `mgSetStrapLongOffset1` | `sklayoutref/modgen.html    "mgSetStrapLongOffset1"` | `HTML` |
| `mgSetStrapLongOffset2` | `sklayoutref/modgen.html    "mgSetStrapLongOffset2"` | `HTML` |
| `mgSetStrapOffset` | `sklayoutref/modgen.html    "mgSetStrapOffset"` | `HTML` |


### ILG API

**32 个函数**，文档位置：

- `skdevref/skillide.html` (32 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `ilgAddRecentFiles` | `skdevref/skillide.html` | `ilgAddRecentFiles` |
| `ilgAppendText` | `skdevref/skillide.html` | `ilgAppendText` |
| `ilgCopy` | `skdevref/skillide.html` | `ilgCopy` |
| `ilgCut` | `skdevref/skillide.html` | `ilgCut` |
| `ilgFindIdent` | `skdevref/skillide.html` | `ilgFindIdent` |
| `ilgFindParenthesis` | `skdevref/skillide.html` | `ilgFindParenthesis` |
| `ilgFoldLine` | `skdevref/skillide.html` | `ilgFoldLine` |
| `ilgGetCursorLocation` | `skdevref/skillide.html` | `ilgGetCursorLocation` |
| `ilgGetEditLock` | `skdevref/skillide.html` | `ilgGetEditLock` |
| `ilgGetHighlight` | `skdevref/skillide.html` | `ilgGetHighlight` |
| `ilgGetSelectedLocation` | `skdevref/skillide.html` | `ilgGetSelectedLocation` |
| `ilgGetText` | `skdevref/skillide.html` | `ilgGetText` |
| `ilgInvokeIDE` | `skdevref/skillide.html` | `ilgInvokeIDE` |
| `ilgLastDir` | `skdevref/skillide.html` | `ilgLastDir` |
| `ilgPaste` | `skdevref/skillide.html` | `ilgPaste` |
| `ilgPositionInComment` | `skdevref/skillide.html` | `ilgPositionInComment` |
| `ilgRegisterSelectionCB` | `skdevref/skillide.html` | `ilgRegisterSelectionCB` |
| `ilgResetErrorMarker` | `skdevref/skillide.html` | `ilgResetErrorMarker` |
| `ilgResetHighlight` | `skdevref/skillide.html` | `ilgResetHighlight` |
| `ilgResetWarningMarker` | `skdevref/skillide.html` | `ilgResetWarningMarker` |
| `ilgRunSKILLIDE` | `skdevref/skillide.html` | `ilgRunSKILLIDE` |
| `ilgScrollToLocation` | `skdevref/skillide.html` | `ilgScrollToLocation` |
| `ilgSearchText` | `skdevref/skillide.html` | `ilgSearchText` |
| `ilgSelectText` | `skdevref/skillide.html` | `ilgSelectText` |
| `ilgSetColor` | `skdevref/skillide.html` | `ilgSetColor` |
| `ilgSetCursorLocation` | `skdevref/skillide.html` | `ilgSetCursorLocation` |
| `ilgSetEditLock` | `skdevref/skillide.html` | `ilgSetEditLock` |
| `ilgSetErrorMarker` | `skdevref/skillide.html` | `ilgSetErrorMarker` |
| `ilgSetHighlight` | `skdevref/skillide.html` | `ilgSetHighlight` |
| `ilgSetWarningMarker` | `skdevref/skillide.html` | `ilgSetWarningMarker` |
| `ilgUnfoldLine` | `skdevref/skillide.html` | `ilgUnfoldLine` |
| `ilgUnregisterSelectionCB` | `skdevref/skillide.html` | `ilgUnregisterSelectionCB` |


### LX API

**32 个函数**，文档位置：

- `sklayoutref/lx.html` (22 个函数)
- `sklayoutref/vdp.html` (8 个函数)
- `sklayoutref/vcp.html` (1 个函数)
- `sklayoutref/lx.html        "lxHiIChain"` (1 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `lxCreateSynchronousClonesFromFigGroups` | `sklayoutref/lx.html` | `lxCreateSynchronousClonesFromFigGroups` |
| `lxGetAvailablePinLPPs` | `sklayoutref/lx.html` | `lxGetAvailablePinLPPs` |
| `lxGetConnRef` | `sklayoutref/lx.html` | `lxGetConnRef` |
| `lxGetSource` | `sklayoutref/lx.html` | `lxGetSource` |
| `lxHiAdjustAreaBoundary` | `sklayoutref/vdp.html` | `lxHiAdjustAreaBoundary` |
| `lxHiAdjustBoundary` | `sklayoutref/vdp.html` | `lxHiAdjustBoundary` |
| `lxHiCreateVirtGroup` | `sklayoutref/vdp.html` | `lxHiCreateVirtGroup` |
| `lxHiDetach` | `sklayoutref/vdp.html` | `lxHiDetach` |
| `lxHiEmbed` | `sklayoutref/vdp.html` | `lxHiEmbed` |
| `lxHiGenerateSelectedFromLayout` | `sklayoutref/lx.html` | `lxHiGenerateSelectedFromLayout"          HTML` |
| `lxHiGenerateVirtualHierarchy` | `sklayoutref/vdp.html` | `lxHiGenerateVirtualHierarchy` |
| `lxHiIChain` | `sklayoutref/lx.html        "lxHiIChain"` | `HTML` |
| `lxHiPlaceBoundaryCell` | `sklayoutref/vcp.html` | `lxHiPlaceBoundaryCell` |
| `lxHiRemaster` | `sklayoutref/vdp.html` | `lxHiRemaster` |
| `lxHiSwap` | `sklayoutref/lx.html` | `lxHiSwap` |
| `lxHiVirtHierOptions` | `sklayoutref/vdp.html` | `lxHiVirtHierOptions` |
| `lxHierCheck` | `sklayoutref/lx.html` | `lxHierCheck` |
| `lxHierCheckAgainstSource` | `sklayoutref/lx.html` | `lxHierCheckAgainstSource` |
| `lxHierUpdateComponentsAndNets` | `sklayoutref/lx.html` | `lxHierUpdateComponentsAndNets` |
| `lxLaunchLayoutEXL` | `sklayoutref/lx.html` | `lxLaunchLayoutEXL` |
| `lxMakeDummy` | `sklayoutref/lx.html` | `lxMakeDummy"              HTML` |
| `lxRegPostUpdateComponentsAndNets` | `sklayoutref/lx.html` | `lxRegPostUpdateComponentsAndNets` |
| `lxRunCmdInXL` | `sklayoutref/lx.html` | `lxRunCmdInXL` |
| `lxSelectedSelectAttachedGlobalNets` | `sklayoutref/lx.html` | `lxSelectedSelectAttachedGlobalNets` |
| `lxSelectedSelectAttachedSignalNets` | `sklayoutref/lx.html` | `lxSelectedSelectAttachedSignalNets"    HTML` |
| `lxSelectedSelectExternalGlobalNets` | `sklayoutref/lx.html` | `lxSelectedSelectExternalGlobalNets"    HTML` |
| `lxSelectedSelectExternalSignalNets` | `sklayoutref/lx.html` | `lxSelectedSelectExternalSignalNets"    HTML` |
| `lxSelectedSelectInternalGlobalNets` | `sklayoutref/lx.html` | `lxSelectedSelectInternalGlobalNets"    HTML` |
| `lxSelectedSelectInternalSignalNets` | `sklayoutref/lx.html` | `lxSelectedSelectInternalSignalNets"    HTML` |
| `lxShapeSlotting` | `sklayoutref/lx.html` | `lxShapeSlotting` |
| `lxUnSlotVia` | `sklayoutref/lx.html` | `lxUnSlotVia` |
| `lxUnfold` | `sklayoutref/lx.html` | `lxUnfold` |


### ISE API

**27 个函数**，文档位置：

- `netlistsimulateref/ossFunctions.html` (27 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `iseCloseSchWindow` | `netlistsimulateref/ossFunctions.html` | `iseCloseSchWindow` |
| `iseCloseSimWindow` | `netlistsimulateref/ossFunctions.html` | `iseCloseSimWindow` |
| `iseCompleteInteractive` | `netlistsimulateref/ossFunctions.html` | `iseCompleteInteractive` |
| `iseEnterNodeNamesList` | `netlistsimulateref/ossFunctions.html` | `iseEnterNodeNamesList` |
| `iseExitSimulator` | `netlistsimulateref/ossFunctions.html` | `iseExitSimulator` |
| `iseGetExtName` | `netlistsimulateref/ossFunctions.html` | `iseGetExtName` |
| `iseGetInputFromEncapWindow` | `netlistsimulateref/ossFunctions.html` | `iseGetInputFromEncapWindow` |
| `iseGetMappedProbeList` | `netlistsimulateref/ossFunctions.html` | `iseGetMappedProbeList` |
| `iseGetProbeList` | `netlistsimulateref/ossFunctions.html` | `iseGetProbeList` |
| `iseInitSchematicWindow` | `netlistsimulateref/ossFunctions.html` | `iseInitSchematicWindow` |
| `iseInitSimWindow` | `netlistsimulateref/ossFunctions.html` | `iseInitSimWindow` |
| `iseNetExtNameCdsName` | `netlistsimulateref/ossFunctions.html` | `iseNetExtNameCdsName` |
| `iseOpenWindows` | `netlistsimulateref/ossFunctions.html` | `iseOpenWindows` |
| `isePrintName` | `netlistsimulateref/ossFunctions.html` | `isePrintName` |
| `isePrintNameCB` | `netlistsimulateref/ossFunctions.html` | `isePrintNameCB` |
| `isePrintSimulatorCommand` | `netlistsimulateref/ossFunctions.html` | `isePrintSimulatorCommand` |
| `iseReleaseNodeFrom` | `netlistsimulateref/ossFunctions.html` | `iseReleaseNodeFrom` |
| `iseSearchForASchWindow` | `netlistsimulateref/ossFunctions.html` | `iseSearchForASchWindow` |
| `iseSendOutputToEncapHistory` | `netlistsimulateref/ossFunctions.html` | `iseSendOutputToEncapHistory` |
| `iseSetEncapBindKeys` | `netlistsimulateref/ossFunctions.html` | `iseSetEncapBindKeys` |
| `iseSetNodeTo` | `netlistsimulateref/ossFunctions.html` | `iseSetNodeTo` |
| `iseSimulate` | `netlistsimulateref/ossFunctions.html` | `iseSimulate` |
| `iseStartInteractive` | `netlistsimulateref/ossFunctions.html` | `iseStartInteractive` |
| `iseStartSimulator` | `netlistsimulateref/ossFunctions.html` | `iseStartSimulator` |
| `iseUpdateNetlist` | `netlistsimulateref/ossFunctions.html` | `iseUpdateNetlist` |
| `iseUpdateStimulus` | `netlistsimulateref/ossFunctions.html` | `iseUpdateStimulus` |
| `iseUpdatelist` | `netlistsimulateref/ossFunctions.html` | `iseUpdatelist` |


### WSP API

**27 个函数**，文档位置：

- `sklayoutref/layout.html` (3 个函数)
- `sklayoutref/layout.html    "wspCreateWSP"` (1 个函数)
- `sklayoutref/layout.html    "wspCreateWSPByAttr"` (1 个函数)
- `sklayoutref/layout.html    "wspCreateWSPGroup"` (1 个函数)
- `sklayoutref/layout.html    "wspCreateWSSPDef"` (1 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `wspCheckActive` | `sklayoutref/layout.html` | `wspCheckActive` |
| `wspCreateWSP` | `sklayoutref/layout.html    "wspCreateWSP"` | `HTML` |
| `wspCreateWSPByAttr` | `sklayoutref/layout.html    "wspCreateWSPByAttr"` | `HTML` |
| `wspCreateWSPGroup` | `sklayoutref/layout.html    "wspCreateWSPGroup"` | `HTML` |
| `wspCreateWSSPDef` | `sklayoutref/layout.html    "wspCreateWSSPDef"` | `HTML` |
| `wspCreateWSSPDefByAttr` | `sklayoutref/layout.html    "wspCreateWSSPDefByAttr"` | `HTML` |
| `wspDeleteMetalFill` | `sklayoutref/layout.html    "wspDeleteMetalFill"` | `HTML` |
| `wspDumpToFile` | `sklayoutref/layout.html    "wspDumpToFile"` | `HTML` |
| `wspGetWSSPDefLP` | `sklayoutref/layout.html` | `wspGetWSSPDefLP` |
| `wspMetalFillTrim` | `sklayoutref/layout.html    "wspMetalFillTrim"` | `HTML` |
| `wspRegionFindByLayer` | `sklayoutref/layout.html    "wspRegionFindByLayer"` | `HTML` |
| `wspRegionFindByWSSPDef` | `sklayoutref/layout.html    "spRegionFindByWSSPDef"` | `HTML` |
| `wspRegionGetActivePattern` | `sklayoutref/layout.html` | `wspRegionGetActivePattern` |
| `wspRegionGetWSSPDef` | `sklayoutref/layout.html    "wspRegionGetWSSPDef"` | `HTML` |
| `wspSPDefFind` | `sklayoutref/layout.html    "wspSPDefFind"` | `HTML` |
| `wspSetWSSPDefRegionPurpose` | `sklayoutref/layout.html    "wspSetWSSPDefRegionPurpose"` | `HTML` |
| `wspWSPFindByName` | `sklayoutref/layout.html    "wspWSPFindByName"` | `HTML` |
| `wspWSPGetFlatAttr` | `sklayoutref/layout.html    "wspWSPGetFlatAttr"` | `HTML` |
| `wspWSPGroupFindByName` | `sklayoutref/layout.html    "wspWSPGroupFindByName"` | `HTML` |
| `wspWSSPDefAddToEnabled` | `sklayoutref/layout.html    "wspWSSPDefAddToEnabled"` | `HTML` |
| `wspWSSPDefFind` | `sklayoutref/layout.html    "wspWSSPDefFind"` | `HTML` |
| `wspWSSPDefFindByName` | `sklayoutref/layout.html    "wspWSSPDefFindByName "` | `HTML` |
| `wspWSSPDefGetActivePattern` | `sklayoutref/layout.html    "wspWSSPDefGetActivePattern"` | `HTML` |
| `wspWSSPDefGetAttr` | `sklayoutref/layout.html    "wspWSSPDefGetAttr"` | `HTML` |
| `wspWSSPDefRemoveFromAllowedPatterns` | `sklayoutref/layout.html    "wspWSSPDefRemoveFromAllowedPatterns"` | `HTML` |
| `wspWSSPDefRename` | `sklayoutref/layout.html    "wspWSSPDefRename"` | `HTML` |
| `wspWSSPDefSetActivePattern` | `sklayoutref/layout.html    "wspWSSPDefSetActivePattern"` | `HTML` |


### SLA API

**27 个函数**，文档位置：

- `verifierSkillRef/setupLibrary.html` (27 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `slaAddCornerModelFile` | `verifierSkillRef/setupLibrary.html` | `slaAddCornerModelFile` |
| `slaAddCornerVariable` | `verifierSkillRef/setupLibrary.html` | `slaAddCornerVariable` |
| `slaAddDocument` | `verifierSkillRef/setupLibrary.html` | `slaAddDocument` |
| `slaAddSweepVariable` | `verifierSkillRef/setupLibrary.html` | `slaAddSweepVariable` |
| `slaCreateCornerSetup` | `verifierSkillRef/setupLibrary.html` | `slaAddSweepVariable` |
| `slaCreateSweepSetup` | `verifierSkillRef/setupLibrary.html` | `slaCreateSweepSetup` |
| `slaCreateVerificationSpace` | `verifierSkillRef/setupLibrary.html` | `slaCreateVerificationSpace` |
| `slaGetAllDocuments` | `verifierSkillRef/setupLibrary.html` | `slaGetAllDocuments` |
| `slaGetCornerModels` | `verifierSkillRef/setupLibrary.html` | `slaGetCornerModels` |
| `slaGetCornerSetupCorners` | `verifierSkillRef/setupLibrary.html` | `slaGetCornerSetupCorners` |
| `slaGetCornerSetups` | `verifierSkillRef/setupLibrary.html` | `slaGetCornerSetups` |
| `slaGetCornerVars` | `verifierSkillRef/setupLibrary.html` | `slaGetCornerVars` |
| `slaGetDocumentAbsolutePath` | `verifierSkillRef/setupLibrary.html` | `slaGetDocumentAbsolutePath` |
| `slaGetSweepSetupVars` | `verifierSkillRef/setupLibrary.html` | `slaGetSweepSetupVars` |
| `slaGetSweepSetups` | `verifierSkillRef/setupLibrary.html` | `slaGetSweepSetups` |
| `slaGetVerificationSpaces` | `verifierSkillRef/setupLibrary.html` | `slaGetVerificationSpaces` |
| `slaImportCorners` | `verifierSkillRef/setupLibrary.html` | `slaImportCorners` |
| `slaImportSweeps` | `verifierSkillRef/setupLibrary.html` | `slaImportSweeps` |
| `slaOpenOrCreateView` | `verifierSkillRef/setupLibrary.html` | `slaOpenOrCreateView` |
| `slaRemoveCorner` | `verifierSkillRef/setupLibrary.html` | `slaRemoveCorner` |
| `slaRemoveCornerModel` | `verifierSkillRef/setupLibrary.html` | `slaRemoveCornerModel` |
| `slaRemoveCornerSetup` | `verifierSkillRef/setupLibrary.html` | `slaRemoveCornerSetup` |
| `slaRemoveCornerVariable` | `verifierSkillRef/setupLibrary.html` | `slaRemoveCornerVariable` |
| `slaRemoveSweepSetup` | `verifierSkillRef/setupLibrary.html` | `slaRemoveSweepSetup` |
| `slaRemoveSweepVariable` | `verifierSkillRef/setupLibrary.html` | `slaRemoveSweepVariable` |
| `slaRemoveVerificationSpace` | `verifierSkillRef/setupLibrary.html` | `slaRemoveVerificationSpace` |
| `slaSaveAndCloseView` | `verifierSkillRef/setupLibrary.html` | `slaSaveAndCloseView` |


### LE API

**26 个函数**，文档位置：

- `sklayoutref/layout.html` (17 个函数)
- `vivaxlskill/chap4.html` (1 个函数)
- `sklayoutref/wire.html` (1 个函数)
- `sklayoutref/layout.html    "leIsLayoutViewerAppEnabled"` (1 个函数)
- `sklayoutref/layout.html    "leIsLayoutViewerWindow"` (1 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `leClearAllMeasurement` | `sklayoutref/layout.html` | `leClearAllMeasurement` |
| `leConvertMosaicToModgen` | `sklayoutref/layout.html    "leConvertMosaicToModgen"` | `HTML` |
| `leConvertSelectedDynamicShapes` | `sklayoutref/layout.html` | `leConvertSelectedDynamicShape` |
| `leCopyTemplatesToCellView` | `sklayoutref/layout.html` | `leCopyTemplatesToCellView` |
| `leCreateMeasurement` | `sklayoutref/layout.html` | `leCreateMeasurement` |
| `leCreateNetField` | `sklayoutref/layout.html    "leCreateNetField"` | `HTML` |
| `leDecrementStopLevelByOne` | `sklayoutref/layout.html` | `leDecrementStopLevelByOne` |
| `leGetWirebondProfileVisible` | `sklayoutref/layout.html` | `leGetWirebondProfileVisible` |
| `leHiClearMeasurement` | `sklayoutref/layout.html` | `leHiClearMeasurement` |
| `leHiClearMeasurementInHier` | `sklayoutref/layout.html` | `leHiClearMeasurementInHier` |
| `leHiConvertMosaicToModgen` | `sklayoutref/layout.html    "leHiConvertMosaicToModgen"` | `HTML` |
| `leHiCreateMPP` | `sklayoutref/layout.html` | `leHiCreateMPP` |
| `leHiCreateMeasurement` | `sklayoutref/layout.html` | `leHiCreateMeasurement` |
| `leHiCreateStrandedWire` | `sklayoutref/wire.html` | `leHiCreateStrandedWire` |
| `leHiIncrementalViolation` | `sklayoutref/layout.html    "leHiIncrementalViolation"` | `HTML` |
| `leIsLayoutViewerAppEnabled` | `sklayoutref/layout.html    "leIsLayoutViewerAppEnabled"` | `HTML` |
| `leIsLayoutViewerWindow` | `sklayoutref/layout.html    "leIsLayoutViewerWindow"` | `HTML` |
| `leMarkNetGetNumThreads` | `sklayoutref/layout.html` | `leMarkNetGetNumThreads` |
| `leMicroEdit` | `sklayoutref/layout.html` | `leMicroEdit` |
| `leQuickAlignToggleMode` | `sklayoutref/layout.html` | `leQuickAlignToggleMode` |
| `leRegisterPPNetNameFn` | `skylayoutref/layout.html` | `leRegisterPPNetNameFn"         HTML` |
| `leRulerCycleDisplayType` | `sklayoutref/layout.html` | `leRulerCycleDisplayType` |
| `leSetWirebondProfileVisible` | `sklayoutref/layout.html` | `leSetWirebondProfileVisible` |
| `leToggleAutoZoomPan` | `sklayoutref/layout.html` | `leToggleAutoZoomPan` |
| `leafValue_ViVA_SKILL` | `vivaxlskill/chap4.html` | `leafValue` |
| `leiHiCreateMeasurement` | `sklayoutref/layout.html` | `leiHiCreateMeasurement` |


### VFO API

**25 个函数**，文档位置：

- `sklayoutref/fgr.html` (24 个函数)
- `"vfoGRCleanVersionCache"` (1 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `vfoCreateObstructions` | `sklayoutref/fgr.html` | `vfoCreateObstructions` |
| `vfoGRCleanVersionCache          $sklayoutref/fgr.html` | `"vfoGRCleanVersionCache"` | `HTML` |
| `vfoGRDisableVersionCache` | `sklayoutref/fgr.html` | `vfoGRDisableVersionCache` |
| `vfoGREnableVersionCache` | `sklayoutref/fgr.html` | `vfoGREnableVersionCache` |
| `vfoGRUpdateCreateFormSize` | `sklayoutref/fgr.html` | `vfoGRUpdateCreateFormSize` |
| `vfoGRUpdateTunnelLPPs` | `sklayoutref/fgr.html` | `vfoGRUpdateTunnelLPPs` |
| `vfoGRUpdateTunnelOptions` | `sklayoutref/fgr.html` | `vfoGRUpdateTunnelOptions` |
| `vfoGRUpdateVersionCache` | `sklayoutref/fgr.html` | `vfoGRUpdateVersionCache` |
| `vfoGetInstWithMissingCache` | `sklayoutref/fgr.html` | `vfoGetInstWithMissingCache` |
| `vfoPostChopCBHandler` | `sklayoutref/fgr.html` | `vfoPostChopCBHandler` |
| `vfoPostReshapeCBHandler` | `sklayoutref/fgr.html` | `vfoPostReshapeCBHandler` |
| `vfoPostSplitCBHandler` | `sklayoutref/fgr.html` | `vfoPostSplitCBHandler` |
| `vfoPostStretchCBHandler` | `sklayoutref/fgr.html` | `vfoPostStretchCBHandler` |
| `vfoRotateInstance` | `sklayoutref/fgr.html` | `vfoRotateInstance` |
| `vfoSupportsConvertToPolygon?` | `sklayoutref/fgr.html` | `vfoSupportsConvertToPolygon?` |
| `vfoSupportsCreateObstruction?` | `sklayoutref/fgr.html` | `vfoSupportsCreateObstruction?` |
| `vfoSupportsCreateObstructions?` | `sklayoutref/fgr.html` | `vfoSupportsCreateObstructions?` |
| `vfoSupportsCreateObstructions?` | `sklayoutref/fgr.html` | `vfoSupportsCreateObstructions?` |
| `vfoSupportsDeleteObstruction?` | `sklayoutref/fgr.html` | `vfoSupportsDeleteObstruction?` |
| `vfoSupportsMerge?` | `sklayoutref/fgr.html` | `vfoSupportsMerge?` |
| `vfoSupportsRotation` | `sklayoutref/fgr.html` | `vfoSupportsRotation` |
| `vfoSupportsUpdateModelShape?` | `sklayoutref/fgr.html` | `vfoSupportsUpdateModelShape?` |
| `vfoSupportsVersionCache` | `sklayoutref/fgr.html` | `vfoSupportsVersionCache` |
| `vfoTransformFluidShape` | `sklayoutref/fgr.html` | `vfoTransformFluidShape` |
| `vfoUpdateModelShape` | `sklayoutref/fgr.html` | `vfoUpdateModelShape` |


### LNT API

**25 个函数**，文档位置：

- `sklayoutref/lx.html` (25 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `lntClearNeighbors` | `sklayoutref/lx.html` | `lntClearNeighbors` |
| `lntComputeNeighbors` | `sklayoutref/lx.html` | `lntComputeNeighbors` |
| `lntContSteps` | `sklayoutref/lx.html` | `lntContSteps` |
| `lntGetAllTraces` | `sklayoutref/lx.html` | `lntGetAllTraces` |
| `lntGetCurrentStep` | `sklayoutref/lx.html` | `lntGetCurrentStep` |
| `lntGetTailVal` | `sklayoutref/lx.html` | `lntGetTailVal` |
| `lntGetTraceInfo` | `sklayoutref/lx.html` | `lntGetTraceInfo` |
| `lntHiNetTracer` | `sklayoutref/lx.html` | `lntHiNetTracer` |
| `lntHideNeighbors` | `sklayoutref/lx.html` | `lntHideNeighbors` |
| `lntIsNeighborsVisible` | `sklayoutref/lx.html` | `lntIsNeighborsVisible` |
| `lntIsStepTrace` | `sklayoutref/lx.html` | `lntIsStepTrace` |
| `lntNeighbors` | `sklayoutref/lx.html` | `lntNeighbors` |
| `lntNextStep` | `sklayoutref/lx.html` | `lntNextStep` |
| `lntNextToSetStep` | `sklayoutref/lx.html` | `lntNextToSetStep` |
| `lntPrevStep` | `sklayoutref/lx.html` | `lntPrevStep` |
| `lntRemoveAll` | `sklayoutref/lx.html` | `lntRemoveAll` |
| `lntRemoveAllTraces` | `sklayoutref/lx.html` | `lntRemoveAllTraces` |
| `lntRemoveTrace` | `sklayoutref/lx.html` | `lntRemoveTrace` |
| `lntSaveTraces` | `sklayoutref/lx.html` | `lntSaveTraces` |
| `lntSetCurrentStep` | `sklayoutref/lx.html` | `lntSetCurrentStep` |
| `lntSetTailVal` | `sklayoutref/lx.html` | `lntSetTailVal` |
| `lntSetTraceColor` | `sklayoutref/lx.html` | `lntSetTraceColor` |
| `lntSetTraceVisibility` | `sklayoutref/lx.html` | `lntSetTraceVisibility` |
| `lntShowHideAllTraces` | `sklayoutref/lx.html` | `lntShowHideAllTraces` |
| `lntShowNeighbors` | `sklayoutref/lx.html` | `lntShowNeighbors` |


### ENV API

**24 个函数**，文档位置：

- `skuiref/chap2.html` (23 个函数)
- `oceanref/chap6.html` (1 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `envCyclicIndexToString` | `skuiref/chap2.html` | `envCyclicIndexToString` |
| `envCyclicStringToIndex` | `skuiref/chap2.html` | `envCyclicStringToIndex` |
| `envEditorStart` | `skuiref/chap2.html` | `envEditorStart` |
| `envGetAvailableTools` | `skuiref/chap2.html` | `envGetAvailableTools` |
| `envGetDefVal` | `skuiref/chap2.html` | `envGetDefVal` |
| `envGetLoadedTools` | `skuiref/chap2.html` | `envGetLoadedTools` |
| `envGetModifiedTools` | `skuiref/chap2.html` | `envGetModifiedTools` |
| `envGetVal` | `skuiref/chap2.html` | `envGetVal` |
| `envGetVarType` | `skuiref/chap2.html` | `envGetVarType` |
| `envIsToolModified` | `skuiref/chap2.html` | `envIsToolModified` |
| `envIsVal` | `skuiref/chap2.html` | `envIsVal` |
| `envLoadFile` | `skuiref/chap2.html` | `envLoadFile` |
| `envLoadVals` | `skuiref/chap2.html` | `envLoadVals` |
| `envOption_OCEAN` | `oceanref/chap6.html` | `envOption` |
| `envRegLoadDumpTrigger` | `skuiref/chap2.html` | `envRegLoadDumpTrigger` |
| `envRegSetTrigger` | `skuiref/chap2.html` | `envRegSetTrigger` |
| `envSetToolCurrValToDefault` | `skuiref/chap2.html` | `envSetToolCurrValToDefault"    HTML` |
| `envSetToolDefaultToCurrVal` | `skuiref/chap2.html` | `envSetToolDefaultToCurrVal"    HTML` |
| `envSetVal` | `skuiref/chap2.html` | `envSetVal` |
| `envSetVarCurrValToDefault` | `skuiref/chap2.html` | `envSetVarCurrValToDefault` |
| `envSetVarDefaultToCurrVal` | `skuiref/chap2.html` | `envSetVarDefaultToCurrVal` |
| `envStoreEnv` | `skuiref/chap2.html` | `envStoreEnv` |
| `envUnregLoadDumpTrigger` | `skuiref/chap2.html` | `envUnregLoadDumpTrigger` |
| `envUnregSetTrigger` | `skuiref/chap2.html` | `envUnregSetTrigger` |


### IPC API

**24 个函数**，文档位置：

- `skipcref/ipcskill.html` (24 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `ipcActivateBatch` | `skipcref/ipcskill.html` | `ipcActivateBatch` |
| `ipcActivateMessages` | `skipcref/ipcskill.html` | `ipcActivateMessages` |
| `ipcBatchProcess` | `skipcref/ipcskill.html` | `ipcBatchProcess` |
| `ipcBeginProcess` | `skipcref/ipcskill.html` | `ipcBeginProcess` |
| `ipcCloseProcess` | `skipcref/ipcskill.html` | `ipcCloseProcess` |
| `ipcContProcess` | `skipcref/ipcskill.html` | `ipcContProcess` |
| `ipcGetExitStatus` | `skipcref/ipcskill.html` | `ipcGetExitStatus` |
| `ipcGetPid` | `skipcref/ipcskill.html` | `ipcGetPid` |
| `ipcGetPriority` | `skipcref/ipcskill.html` | `ipcGetPriority` |
| `ipcIsActiveProcess` | `skipcref/ipcskill.html` | `ipcIsActiveProcess` |
| `ipcIsAliveProcess` | `skipcref/ipcskill.html` | `ipcIsAliveProcess` |
| `ipcKillAllProcesses` | `skipcref/ipcskill.html` | `ipcKillAllProcesses` |
| `ipcKillProcess` | `skipcref/ipcskill.html` | `ipcKillProcess` |
| `ipcReadProcess` | `skipcref/ipcskill.html` | `ipcReadProcess` |
| `ipcSetPriority` | `skipcref/ipcskill.html` | `ipcSetPriority` |
| `ipcSignalProcess` | `skipcref/ipcskill.html` | `ipcSignalProcess` |
| `ipcSkillProcess` | `skipcref/ipcskill.html` | `ipcSkillProcess` |
| `ipcSleep` | `skipcref/ipcskill.html` | `ipcSleep` |
| `ipcSleepMilli` | `skipcref/ipcskill.html` | `ipcSleepMilli` |
| `ipcSoftInterrupt` | `skipcref/ipcskill.html` | `ipcSoftInterrupt` |
| `ipcStopProcess` | `skipcref/ipcskill.html` | `ipcStopProcess` |
| `ipcWait` | `skipcref/ipcskill.html` | `ipcWait` |
| `ipcWaitForProcess` | `skipcref/ipcskill.html` | `ipcWaitForProcess` |
| `ipcWriteProcess` | `skipcref/ipcskill.html` | `ipcWriteProcess` |


### MPT API

**24 个函数**，文档位置：

- `sklayoutref/mpt.html` (21 个函数)
- `sklayoutref/mpt.html    "mptColorRemastering"` (1 个函数)
- `sklayoutref/mpt.html    "mptGetTrackPatternPattern"` (1 个函数)
- `sklayoutref/mpt.html    "mptSetTrackPatternPattern"` (1 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `mptCheckFlow` | `sklayoutref/mpt.html` | `mptCheckFlow` |
| `mptCheckHierarchicalLocks` | `sklayoutref/mpt.html` | `mptCheckHierarchicalLocks ` |
| `mptCleanClusters` | `sklayoutref/mpt.html` | `mptCleanClusters` |
| `mptColorRemastering` | `sklayoutref/mpt.html    "mptColorRemastering"` | `HTML` |
| `mptDefineFlow` | `sklayoutref/mpt.html` | `mptDefineFlow` |
| `mptDoColorChecks` | `sklayoutref/mpt.html` | `mptDoColorChecks` |
| `mptDoToolbarAction` | `sklayoutref/mpt.html` | `mptDoToolbarAction` |
| `mptGetColorShiftingLayers` | `sklayoutref/mpt.html` | `mptGetColorShiftingLayers` |
| `mptGetFlowNames` | `sklayoutref/mpt.html` | `mptGetFlowNames` |
| `mptGetFlowSettings` | `sklayoutref/mpt.html` | `mptGetFlowSettings` |
| `mptGetOutdatedDesigns` | `sklayoutref/mpt.html` | `mptGetOutdatedDesigns` |
| `mptGetTrackPatternPattern` | `sklayoutref/mpt.html    "mptGetTrackPatternPattern"` | `HTML` |
| `mptGetUpToDateDesigns` | `sklayoutref/mpt.html` | `mptGetUpToDateDesigns` |
| `mptLockAll` | `sklayoutref/mpt.html` | `mptLockAll` |
| `mptMarkersToColoredBlockages` | `sklayoutref/mpt.html` | `mptMarkersToColoredBlockages` |
| `mptPurgePcell` | `sklayoutref/mpt.html` | `mptPurgePcell` |
| `mptReColorFromShapes` | `sklayoutref/mpt.html` | `mptReColorFromShapes` |
| `mptReportCurrentSettings` | `sklayoutref/mpt.html` | `mptReportCurrentSettings` |
| `mptSetFlow` | `sklayoutref/mpt.html` | `mptSetFlow` |
| `mptSetTrackPatternPattern` | `sklayoutref/mpt.html    "mptSetTrackPatternPattern"` | `HTML` |
| `mptSetupComplianceChecker` | `sklayoutref/mpt.html` | `mptSetupComplianceChecker` |
| `mptUnlockAll` | `sklayoutref/mpt.html` | `mptUnlockAll` |
| `mptUnpropagateLocks` | `sklayoutref/mpt.html` | `mptUnpropagateLocks` |
| `mptUpdateColor` | `sklayoutref/mpt.html` | `mptUpdateColor` |


### ASI API

**21 个函数**，文档位置：

- `skartistref/chap2.html` (7 个函数)
- `skartistref/chap3.html` (6 个函数)
- `vivaxlug/appD.html` (2 个函数)
- `skartistref/chap9.html` (2 个函数)
- `oceanref/chap10.html` (1 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `asiChangeAnalysisField` | `skartistref/chap9.html` | `asiChangeAnalysisField` |
| `asiChangeAnalysisOption` | `skartistref/chap9.html` | `asiChangeAnalysisOption` |
| `asiCreateCdsenvFile` | `skartistref/chap3.html` | `asiCreateCdsenvFile` |
| `asiCreateFormatter` | `skartistref/chap3.html` | `asiCreateFormatter` |
| `asiCreateIncludeStatementFile` | `skartistref/chap7.html` | `asiCreateIncludeStatementFile` |
| `asiDigitalSimAutoloadProc` | `vsvn/appFunctions.html` | `asiDigitalSimAutoloadProc` |
| `asiFormatSpecialParameterForRel` | `maeSKILLref/maestroSKILL.html` | `asiFormatSpecialParameterForRel` |
| `asiGetFormatter` | `skartistref/chap3.html` | `asiGetFormatter` |
| `asiGetNetlistFormatterClass` | `skartistref/chap3.html` | `asiGetNetlistFormatterClass` |
| `asiGetSimInputFileName` | `skartistref/chap3.html` | `asiGetSimInputFileName` |
| `asiGetSimInputFileSuffix` | `skartistref/chap3.html` | `asiGetSimInputFileSuffix` |
| `asiInit<yourSimulator>` | `skartistref/chap2.html` | `asiInit<yourSimulator>` |
| `asiInitAdvAnalysis` | `skartistref/chap2.html` | `asiInitAdvAnalysis` |
| `asiInitAnalysis` | `skartistref/chap2.html` | `asiInitAnalysis` |
| `asiInitDataAccessFunction` | `skartistref/chap2.html` | `asiInitDataAccessFunction` |
| `asiInitEnvOption` | `skartistref/chap2.html` | `asiInitEnvOption` |
| `asiInitSimOption` | `skartistref/chap2.html` | `asiInitSimOption` |
| `asiRegisterTool` | `skartistref/chap2.html` | `asiRegisterTool` |
| `asin_OCEAN` | `oceanref/chap10.html` | `asin` |
| `asin_ViVA_SKILL` | `vivaxlug/appD.html` | `asin` |
| `asinh_ViVA_SKILL` | `vivaxlug/appD.html` | `asinh` |


### DD API

**20 个函数**，文档位置：

- `skdfref/chap3.html` (6 个函数)
- `skuiref/chap8.html` (6 个函数)
- `amsskillref/amsdesigner.html` (3 个函数)
- `skuiref/chap4.html` (3 个函数)
- `skdfref/chap3.html                      "ddsHiSaveData"` (1 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `ddGetCombineValue` | `skdfref/chap3.html` | `ddGetCombineValue` |
| `ddGetDisplayValue` | `skdfref/chap3.html` | `ddGetDisplayValue` |
| `ddHiCreateCellComboField` | `skuiref/chap8.html` | `ddHiCreateCellComboField` |
| `ddHiCreateCellToolbarComboBox` | `skuiref/chap4.html` | `ddHiCreateCellToolbarComboBox` |
| `ddHiCreateLibraryComboField` | `skuiref/chap8.html` | `ddHiCreateLibraryComboField` |
| `ddHiCreateLibraryToolbarComboBox` | `skuiref/chap4.html` | `ddHiCreateLibraryToolbarComboBox` |
| `ddHiCreateViewComboField` | `skuiref/chap8.html` | `ddHiCreateViewComboField` |
| `ddHiCreateViewToolbarComboBox` | `skuiref/chap4.html` | `ddHiCreateViewToolbarComboBox` |
| `ddHiLinkFields` | `skuiref/chap8.html` | `ddHiLinkFields` |
| `ddIsHiddenCell` | `skdfref/chap3.html` | `ddIsHiddenCell` |
| `ddRegHiddenCellsFunc                $skdfref/chap3.html` | `"ddRegHiddenCellsFunc"` | `HTML` |
| `ddoAccepts` | `skuiref/chap8.html` | `ddoAccepts` |
| `ddoPreferred` | `skuiref/chap8.html` | `ddoPreferred` |
| `ddsCvtAMSTranslateCell` | `amsskillref/amsdesigner.html` | `ddsCvtAMSTranslateCell` |
| `ddsCvtAMSTranslateLib` | `amsskillref/amsdesigner.html` | `ddsCvtAMSTranslateLib` |
| `ddsCvtToolBoxAMS` | `amsskillref/amsdesigner.html` | `ddsCvtToolBoxAMS` |
| `ddsHiCloseData` | `skdfref/chap3.html` | `ddsHiCloseData` |
| `ddsHiSaveData` | `skdfref/chap3.html                      "ddsHiSaveData"` | `HTML` |
| `ddsRegPostRefreshTrigger` | `skdfref/chap3.html` | `ddsRegPostRefreshTrigger` |
| `ddsRegPreRefreshTrigger` | `skdfref/chap3.html` | `ddsRegPreRefreshTrigger` |


### CST API

**19 个函数**，文档位置：

- `constraintsSKILL/skillcstFunctions.html` (17 个函数)
- `"cstGetFoundryConstraintGroup"` (1 个函数)
- `"cstGetUnreferencedConstraints"` (1 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `cstAddToConstraintGroup` | `constraintsSKILL/skillcstFunctions.html` | `cstAddToConstraintGroup` |
| `cstCreateConstraint` | `constraintsSKILL/skillcstFunctions.html` | `cstCreateConstraint` |
| `cstCreateConstraintGroupIn` | `constraintsSKILL/skillcstFunctions.html` | `cstCreateConstraintGroupIn` |
| `cstCreateConstraintGroupOn` | `constraintsSKILL/skillcstFunctions.html` | `cstCreateConstraintGroupOn` |
| `cstDeleteConstraint` | `constraintsSKILL/skillcstFunctions.html` | `cstDeleteConstraint` |
| `cstDeleteConstraintGroup` | `constraintsSKILL/skillcstFunctions.html` | `cstDeleteConstraintGroup` |
| `cstFindConstraintGroupIn` | `constraintsSKILL/skillcstFunctions.html` | `cstFindConstraintGroupIn` |
| `cstFindConstraintGroupOn` | `constraintsSKILL/skillcstFunctions.html` | `cstFindConstraintGroupOn` |
| `cstFindFirstConstraint` | `constraintsSKILL/skillcstFunctions.html` | `cstFindFirstConstraint` |
| `cstGet1DTableValue` | `constraintsSKILL/skillcstFunctions.html` | `cstGet1DTableValue` |
| `cstGet2DTableValue` | `constraintsSKILL/skillcstFunctions.html` | `cstGet2DTableValue` |
| `cstGetConstraintGroups` | `constraintsSKILL/skillcstFunctions.html` | `cstGetConstraintGroups` |
| `cstGetDefaultConstraintGroupName` | `constraintsSKILL/skillcstFunctions.html` | `cstGetDefaultConstraintGroupName` |
| `cstGetFoundryCGName` | `constraintsSKILL/skillcstFunctions.html` | `cstGetFoundryCGName` |
| `cstGetFoundryConstraintGroup    $constraintsSKILL/skillcstFunctions.html` | `"cstGetFoundryConstraintGroup"` | `HTML` |
| `cstGetTwoWidthTableValue` | `constraintsSKILL/skillcstFunctions.html` | `cstGetTwoWidthTableValue` |
| `cstGetUnreferencedConstraints   $constraintsSKILL/skillcstFunctions.html` | `"cstGetUnreferencedConstraints"` | `HTML` |
| `cstIsId` | `constraintsSKILL/skillcstFunctions.html` | `cstIsId` |
| `cstSetDefaultConstraintGroupName` | `constraintsSKILL/skillcstFunctions.html` | `cstSetDefaultConstraintGroupName` |


### FNL API

**18 个函数**，文档位置：

- `netlistsimulateref/ossFunctions.html` (18 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `fnlAbortNetlist` | `netlistsimulateref/ossFunctions.html` | `fnlAbortNetlist` |
| `fnlCurrentCell` | `netlistsimulateref/ossFunctions.html` | `fnlCurrentCell` |
| `fnlCurrentCellCdsName` | `netlistsimulateref/ossFunctions.html` | `fnlCurrentCellCdsName` |
| `fnlCurrentInst` | `netlistsimulateref/ossFunctions.html` | `fnlCurrentInst` |
| `fnlCurrentInstCdsName` | `netlistsimulateref/ossFunctions.html` | `fnlCurrentInstCdsName` |
| `fnlCurrentIteration` | `netlistsimulateref/ossFunctions.html` | `fnlCurrentIteration` |
| `fnlCurrentModelExtName` | `netlistsimulateref/ossFunctions.html` | `fnlCurrentModelExtName` |
| `fnlCurrentSig` | `netlistsimulateref/ossFunctions.html` | `fnlCurrentSig` |
| `fnlCurrentSigPathName` | `netlistsimulateref/ossFunctions.html` | `fnlCurrentSigPathName` |
| `fnlGetGlobalSigNames` | `netlistsimulateref/ossFunctions.html` | `fnlGetGlobalSigNames` |
| `fnlInstCdsNameExtName` | `netlistsimulateref/ossFunctions.html` | `fnlInstCdsNameExtName` |
| `fnlPathList` | `netlistsimulateref/ossFunctions.html` | `fnlPathList` |
| `fnlPrint` | `netlistsimulateref/ossFunctions.html` | `fnlPrint` |
| `fnlSearchPropString` | `netlistsimulateref/ossFunctions.html` | `fnlSearchPropString` |
| `fnlSigCdsNameExtName` | `netlistsimulateref/ossFunctions.html` | `fnlSigCdsNameExtName` |
| `fnlTermCdsNameExtName` | `netlistsimulateref/ossFunctions.html` | `fnlTermCdsNameExtName` |
| `fnlTermExtName` | `netlistsimulateref/ossFunctions.html` | `fnlTermExtName` |
| `fnlTopCell` | `netlistsimulateref/ossFunctions.html` | `fnlTopCell` |


### OCN API

**18 个函数**，文档位置：

- `oceanref/chap6.html` (9 个函数)
- `oceanref/chap8.html` (5 个函数)
- `oceanref/chap7.html` (2 个函数)
- `oceanref/chap5.html` (1 个函数)
- `ocnxl/ocnxlcommands.html` (1 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `ocnAmsSetOSSNetlister_OCEAN` | `oceanref/chap6.html` | `ocnAmsSetOSSNetlister` |
| `ocnAmsSetUnlNetlister_OCEAN` | `oceanref/chap6.html` | `ocnAmsSetUnlNetlister` |
| `ocnCloseSession_OCEAN` | `oceanref/chap6.html` | `ocnCloseSession` |
| `ocnDisplay_OCEAN` | `oceanref/chap6.html` | `ocnDisplay` |
| `ocnDspfFile_OCEAN` | `oceanref/chap6.html` | `ocnDspfFile` |
| `ocnGenNoiseSummary_OCEAN` | `oceanref/chap8.html` | `ocnGenNoiseSummary` |
| `ocnGetAdjustedPath_OCEAN` | `oceanref/chap6.html` | `ocnGetAdjustedPath` |
| `ocnGetInstancesModelName_OCEAN` | `oceanref/chap6.html` | `ocnGetInstancesModelName` |
| `ocnHelp_OCEAN` | `oceanref/chap7.html` | `ocnHelp` |
| `ocnPrint_OCEAN` | `oceanref/chap8.html` | `ocnPrint` |
| `ocnPspiceFile_OCEAN` | `oceanref/chap6.html` | `ocnPspiceFile` |
| `ocnResetResults_OCEAN` | `oceanref/chap7.html` | `ocnResetResults` |
| `ocnSetAttrib_OCEAN` | `oceanref/chap8.html` | `ocnSetAttrib` |
| `ocnSetSilentMode_OCEAN` | `oceanref/chap5.html` | `ocnSetSilentMode` |
| `ocnSetXLMode` | `ocnxl/ocnxlcommands.html` | `ocnSetXLMode` |
| `ocnSpefFile_OCEAN` | `oceanref/chap6.html` | `ocnSpefFile` |
| `ocnWriteLsspToFile_OCEAN` | `oceanref/chap8.html` | `ocnWriteLsspToFile` |
| `ocnYvsYplot_OCEAN` | `oceanref/chap8.html` | `ocnYvsYplot` |


### XOAS API

**18 个函数**，文档位置：

- `sktransrefOA/skxoasis.html` (17 个函数)
- `sktransrefOA/skxstream.html` (1 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `xoasInDoTranslate` | `sktransrefOA/skxoasis.html` | `xoasInDoTranslate` |
| `xoasInGetField` | `sktransrefOA/skxoasis.html` | `xoasInGetField` |
| `xoasInOnCancelCB` | `sktransrefOA/skxstream.html` | `xoasInOnCancelCB` |
| `xoasInOnCompletionCB` | `sktransrefOA/skxoasis.html` | `xoasInOnCompletionCB` |
| `xoasInOnTranslateCB` | `sktransrefOA/skxoasis.html` | `xoasInOnTranslateCB` |
| `xoasInSetField` | `sktransrefOA/skxoasis.html` | `xoasInSetField` |
| `xoasOutDoTranslate` | `sktransrefOA/skxoasis.html` | `xoasOutDoTranslate` |
| `xoasOutGetField` | `sktransrefOA/skxoasis.html` | `xoasOutGetField` |
| `xoasOutOnCancelCB` | `sktransrefOA/skxoasis.html` | `xoasOutOnCancelCB` |
| `xoasOutOnCompletionCB` | `sktransrefOA/skxoasis.html` | `xoasOutOnCompletionCB` |
| `xoasOutOnTranslateCB` | `sktransrefOA/skxoasis.html` | `xoasOutOnTranslateCB` |
| `xoasOutSetField` | `sktransrefOA/skxoasis.html` | `xoasOutSetField` |
| `xoasisInOnCancel` | `sktransrefOA/skxoasis.html` | `xoasisInOnCancel` |
| `xoasisInOnCompletion` | `sktransrefOA/skxoasis.html` | `xoasisInOnCompletion` |
| `xoasisInOnTranslate` | `sktransrefOA/skxoasis.html` | `xoasisInOnTranslate` |
| `xoasisOutOnCancel` | `sktransrefOA/skxoasis.html` | `xoasisOutOnCancel` |
| `xoasisOutOnCompletion` | `sktransrefOA/skxoasis.html` | `xoasisOutOnCompletion` |
| `xoasisOutOnTranslate` | `sktransrefOA/skxoasis.html` | `xoasisOutOnTranslate` |


### VDR API

**18 个函数**，文档位置：

- `vvdrflow/appC.html` (16 个函数)
- `"vdrCreateVoltageLabelEx"` (1 个函数)
- `"vdrSanityCheckerGUI"` (1 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `vdrCheckVoltageLabels` | `vvdrflow/appC.html` | `vdrCheckVoltageLabels` |
| `vdrCreateVSyncConstraintsFromFile` | `vvdrflow/appC.html` | `vdrCreateVSyncConstraintsFromFile` |
| `vdrCreateVoltageLabel` | `vvdrflow/appC.html` | `vdrCreateVoltageLabel` |
| `vdrCreateVoltageLabelEx             $vvdrflow/appC.html` | `"vdrCreateVoltageLabelEx"` | `HTML` |
| `vdrCreateVoltageLabelOnNets` | `vvdrflow/appC.html` | `vdrCreateVoltageLabelOnNets` |
| `vdrCreateVoltageMarkers` | `vvdrflow/appC.html` | `vdrCreateVoltageMarkers` |
| `vdrCreateVoltageMarkersOnNets` | `vvdrflow/appC.html` | `vdrCreateVoltageMarkersOnNets` |
| `vdrDeleteLabels` | `vvdrflow/appC.html` | `vdrDeleteLabels` |
| `vdrGenerateLabelsGUI` | `vvdrflow/appC.html` | `vdrGenerateLabelsGUI` |
| `vdrGenerateVSyncShapes` | `vvdrflow/appC.html` | `vdrGenerateVSyncShapes` |
| `vdrGetValidLayers` | `vvdrflow/appC.html` | `vdrGetValidLayers` |
| `vdrRunSanityChecker` | `vvdrflow/appC.html` | `vdrRunSanityChecker` |
| `vdrRunVSyncSanityChecker` | `vvdrflow/appC.html` | `vdrRunVSyncSanityChecker` |
| `vdrSanityCheckerGUI                 $vvdrflow/appC.html` | `"vdrSanityCheckerGUI"` | `HTML` |
| `vdrSetNetVoltageRange` | `vvdrflow/appC.html` | `vdrSetNetVoltageRange` |
| `vdrSetValidLayers` | `vvdrflow/appC.html` | `vdrSetValidLayers` |
| `vdrTransferVSyncConstraints` | `vvdrflow/appC.html` | `vdrTransferVSyncConstraints` |
| `vdrVsyncVisualizerGUI` | `vvdrflow/appC.html` | `vdrVsyncVisualizerGUI` |


### PKX API

**18 个函数**，文档位置：

- `"pkxFindFuncDefPin"` (2 个函数)
- `"pkxAddFuncDefPin"` (1 个函数)
- `"pkxCreateCompDef"` (1 个函数)
- `"pkxCreateCompDefPin"` (1 个函数)
- `"pkxCreateFuncDef"` (1 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `pkxAddFuncDefPin                    $skdfref/vrf.html` | `"pkxAddFuncDefPin"` | `HTML` |
| `pkxCreateCompDef                    $skdfref/vrf.html` | `"pkxCreateCompDef"` | `HTML` |
| `pkxCreateCompDefPin                 $skdfref/vrf.html` | `"pkxCreateCompDefPin"` | `HTML` |
| `pkxCreateFuncDef                    $skdfref/vrf.html` | `"pkxCreateFuncDef"` | `HTML` |
| `pkxCreateFuncDefPin                 $skdfref/vrf.html` | `"pkxCreateFuncDefPin"` | `HTML` |
| `pkxDeleteCompDef                    $skdfref/vrf.html` | `"pkxDeleteCompDef"` | `HTML` |
| `pkxFindCompDef                      $skdfref/vrf.html` | `"pkxFindCompDef"` | `HTML` |
| `pkxFindCompDefPin` | `skdfref/vrf.html` | `pkxFindCompDefPin` |
| `pkxFindFuncDef                      $skdfref/vrf.html` | `"pkxFindFuncDef"` | `HTML` |
| `pkxFindFuncDefPin                   $skdfref/vrf.html` | `"pkxFindFuncDefPin"` | `HTML` |
| `pkxFindFuncDefPin                   $skdfref/vrf.html` | `"pkxFindFuncDefPin"` | `HTML` |
| `pkxGetCompDefPins                   $skdfref/vrf.html` | `"pkxGetCompDefPins"` | `HTML` |
| `pkxGetCompDefs                      $skdfref/vrf.html` | `"pkxGetCompDefs"` | `HTML` |
| `pkxGetFuncDefPins                   $skdfref/vrf.html` | `"pkxGetFuncDefPins"` | `HTML` |
| `pkxGetFuncDefs                      $skdfref/vrf.html` | `"pkxGetFuncDefs"` | `HTML` |
| `pkxGetProp                          $skdfref/vrf.html` | `"pkxGetProp"` | `HTML` |
| `pkxGetProps                         $skdfref/vrf.html` | `"pkxGetProps"` | `HTML` |
| `pkxSetProp                          $skdfref/vrf.html` | `"pkxSetProp"` | `HTML` |


### CAL API

**16 个函数**，文档位置：

- `vivaxlskill/chap4.html` (11 个函数)
- `skdevref/context.html` (2 个函数)
- `skoopref/genericfunc.html` (2 个函数)
- `adexlSKILLref/measures.html` (1 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `calCalcInput_ViVA_SKILL` | `vivaxlskill/chap4.html` | `calCalcInput` |
| `calCalculatorFormCB_ViVA_SKILL` | `vivaxlskill/chap4.html` | `calCalculatorFormCB` |
| `calCreateSpecialFunction_ViVA_SKILL` | `vivaxlskill/chap4.html` | `calCreateSpecialFunction` |
| `calCreateSpecialFunctionsForm_ViVA_SKILL` | `vivaxlskill/chap4.html` | `calCreateSpecialFunctionsForm" HTML` |
| `calGetBuffer_ViVA_SKILL` | `vivaxlskill/chap4.html` | `calGetBuffer` |
| `calRegisterSpecialFunction_ViVA_SKILL` | `vivaxlskill/chap4.html` | `calRegisterSpecialFunction"    HTML` |
| `calSetBuffer_ViVA_SKILL` | `vivaxlskill/chap4.html` | `calSetBuffer` |
| `calSetCurrentTest_ViVA_SKILL` | `vivaxlskill/chap4.html` | `calSetCurrentTest` |
| `calSpecialFunctionInput_ViVA_SKILL` | `vivaxlskill/chap4.html` | `calSpecialFunctionInput` |
| `calcVal` | `adexlSKILLref/measures.html` | `calcVal` |
| `caliModeToggle_ViVA_SKILL` | `vivaxlskill/chap4.html` | `caliModeToggle` |
| `caliRestoreDefaultWindowSize_ViVA_SKILL` | `vivaxlskill/chap4.html` | `caliRestoreDefaultWindowSize"  HTML` |
| `callAs` | `skoopref/genericfunc.html` | `callAs` |
| `callInitProc` | `skdevref/context.html` | `callInitProc` |
| `callNextMethod` | `skoopref/genericfunc.html` | `callNextMethod` |
| `callUserAutoInitProc` | `skdevref/context.html` | `callUserAutoInitProc` |


### EDIFOUT API

**15 个函数**，文档位置：

- `edifinref/chap2.html` (15 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `edifoutAddCellInfo` | `edifinref/chap2.html` | `edifoutAddCellInfo` |
| `edifoutAddInstInfo` | `edifinref/chap2.html` | `edifoutAddInstInfo` |
| `edifoutAddInterfaceInfo` | `edifinref/chap2.html` | `edifoutAddInterfaceInfo` |
| `edifoutAddLibraryInfo` | `edifinref/chap2.html` | `edifoutAddLibraryInfo` |
| `edifoutAddNetInfo` | `edifinref/chap2.html` | `edifoutAddNetInfo` |
| `edifoutAddPortInfo` | `edifinref/chap2.html` | `edifoutAddPortInfo` |
| `edifoutAddViewInfo` | `edifinref/chap2.html` | `edifoutAddViewInfo` |
| `edifoutEditCellProperty` | `edifinref/chap2.html` | `edifoutEditCellProperty` |
| `edifoutEditInstProperty` | `edifinref/chap2.html` | `edifoutEditInstProperty` |
| `edifoutEditLibProperty` | `edifinref/chap2.html` | `edifoutEditLibProperty` |
| `edifoutEditNetProperty` | `edifinref/chap2.html` | `edifoutEditNetProperty` |
| `edifoutEditPortProperty` | `edifinref/chap2.html` | `edifoutEditPortProperty` |
| `edifoutEditProperty` | `edifinref/chap2.html` | `edifoutEditProperty` |
| `edifoutEditViewProperty` | `edifinref/chap2.html` | `edifoutEditViewProperty` |
| `edifoutMakeRenameString` | `edifinref/chap2.html` | `edifoutMakeRenameString` |


### PHASE API

**14 个函数**，文档位置：

- `vivaxlug/appD.html` (7 个函数)
- `oceanref/chap10.html` (6 个函数)
- `oceanref/chap7.html` (1 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `phaseDegUnwrapped_OCEAN` | `oceanref/chap10.html` | `phaseDegUnwrapped` |
| `phaseDegUnwrapped_ViVA_SKILL` | `vivaxlug/appD.html` | `phaseDegUnwrapped` |
| `phaseDeg_OCEAN` | `oceanref/chap10.html` | `phaseDeg` |
| `phaseDeg_ViVA_SKILL` | `vivaxlug/appD.html` | `phaseDeg` |
| `phaseMargin_OCEAN` | `oceanref/chap10.html` | `phaseMargin` |
| `phaseMargin_ViVA_SKILL` | `vivaxlug/appD.html` | `phaseMargin` |
| `phaseNoise_OCEAN` | `oceanref/chap7.html` | `phaseNoise` |
| `phaseNoise_ViVA_SKILL` | `vivaxlug/appD.html` | `phaseNoise` |
| `phaseRadUnwrapped_OCEAN` | `oceanref/chap10.html` | `phaseRadUnwrapped` |
| `phaseRadUnwrapped_ViVA_SKILL` | `vivaxlug/appD.html` | `phaseRadUnwrapped` |
| `phaseRad_OCEAN` | `oceanref/chap10.html` | `phaseRad` |
| `phaseRad_ViVA_SKILL` | `vivaxlug/appD.html` | `phaseRad` |
| `phase_OCEAN` | `oceanref/chap10.html` | `phase` |
| `phase_ViVA_SKILL` | `vivaxlug/appD.html` | `phase` |


### CC API

**14 个函数**，文档位置：

- `skdfref/photonic.html` (10 个函数)
- `caiskill/cdsCopy.html` (2 个函数)
- `caiskill/cdsCopy.html    "ccpDmHasRename"` (1 个函数)
- `caiskill/cdsCopy.html    "ccpDmRename"` (1 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `ccCopyFig` | `skdfref/photonic.html` | `ccCopyFig` |
| `ccCreateConnectorWidthExpressionList` | `skdfref/photonic.html` | `ccCreateConnectorWidthExpressionList` |
| `ccCreateLineSegment` | `skdfref/photonic.html` | `ccCreateLineSegment` |
| `ccCreatePolygon` | `skdfref/photonic.html` | `ccCreatePolygon` |
| `ccGenOffsetFig` | `skdfref/photonic.html` | `ccGenOffsetFig` |
| `ccGetPolyCurveMinRadius` | `skdfref/photonic.html` | `ccGetPolyCurveMinRadius` |
| `ccMoveFig` | `skdfref/photonic.html` | `ccMoveFig` |
| `ccOffsetPolyCurve` | `skdfref/photonic.html` | `ccOffsetPolyCurve` |
| `ccRenameFacet` | `skdfref/photonic.html` | `ccRenameFacet` |
| `ccWideConnector` | `skdfref/photonic.html` | `ccWideConnector` |
| `ccpDmHasRename` | `caiskill/cdsCopy.html    "ccpDmHasRename"` | `HTML` |
| `ccpDmRename` | `caiskill/cdsCopy.html    "ccpDmRename"` | `HTML` |
| `ccpGetAutoRename` | `caiskill/cdsCopy.html` | `ccpGetAutoRename` |
| `ccpSetAutoRename` | `caiskill/cdsCopy.html` | `ccpSetAutoRename` |


### TE API

**13 个函数**，文档位置：

- `text_editor/app_te_api.html` (11 个函数)
- `oceanref/chap6.html` (1 个函数)
- `sktransrefOA/skxstream.html` (1 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `teDiscardEdits` | `text_editor/app_te_api.html` | `teDiscardEdits` |
| `teGetCursorPosition` | `text_editor/app_te_api.html` | `teGetCursorPosition` |
| `teIsModified` | `text_editor/app_te_api.html` | `teIsModified` |
| `teRegPostExtractTrigger` | `text_editor/app_te_api.html` | `teRegPostExtractTrigger` |
| `teRegPreExtractTrigger` | `text_editor/app_te_api.html` | `teRegPreExtractTrigger"        HTML` |
| `teSave` | `text_editor/app_te_api.html` | `teSave` |
| `teSaveWithDerivedData` | `text_editor/app_te_api.html` | `teSaveWithDerivedData` |
| `teSetCursor` | `text_editor/app_te_api.html` | `teSetCursor` |
| `teSetEditMode` | `text_editor/app_te_api.html` | `teSetEditMode` |
| `teUnRegPostExtractTrigger` | `text_editor/app_te_api.html` | `teUnRegPostExtractTrigger"     HTML` |
| `teUnRegPreExtractTrigger` | `text_editor/app_te_api.html` | `teUnRegPreExtractTrigger"      HTML` |
| `temp_OCEAN` | `oceanref/chap6.html` | `temp` |
| `textFontMap` | `sktransrefOA/skxstream.html` | `textFontMap` |


### EYE API

**13 个函数**，文档位置：

- `vivaxlskill/chap2.html` (6 个函数)
- `oceanref/chap10.html` (5 个函数)
- `vivaxlug/appD.html` (2 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `eyeAperture_OCEAN` | `oceanref/chap10.html` | `eyeAperture` |
| `eyeAperture_ViVA_SKILL` | `vivaxlug/appD.html` | `eyeAperture` |
| `eyeBERLeftApprox_ViVA_SKILL` | `vivaxlskill/chap2.html` | `eyeBERLeftApprox` |
| `eyeBERLeft_ViVA_SKILL` | `vivaxlskill/chap2.html` | `eyeBERLeft` |
| `eyeBERRightApprox_ViVA_SKILL` | `vivaxlskill/chap2.html` | `eyeBERRightApprox` |
| `eyeBERRight_ViVA_SKILL` | `vivaxlskill/chap2.html` | `eyeBERRight` |
| `eyeDiagram_OCEAN` | `oceanref/chap10.html` | `eyeDiagram` |
| `eyeDiagram_ViVA_SKILL` | `vivaxlug/appD.html` | `eyeDiagram` |
| `eyeHeightAtXY_OCEAN` | `oceanref/chap10.html` | `eyeHeightAtXY` |
| `eyeMaskViolationPeriodCount_ViVA_SKILL` | `vivaxlskill/chap2.html` | `eyeMaskViolationPeriodCount` |
| `eyeMask_ViVA_SKILL` | `vivaxlskill/chap2.html` | `eyeMask` |
| `eyeMeasurement_OCEAN` | `oceanref/chap10.html` | `eyeMeasurement` |
| `eyeWidthAtXY_OCEAN` | `oceanref/chap10.html` | `eyeWidthAtXY` |


### PHO API

**13 个函数**，文档位置：

- `skipcref/phoIPC.html` (9 个函数)
- `skdfref/photonic.html` (2 个函数)
- `skdfref/photonic.html     "phoCreatePort"` (1 个函数)
- `skdfref/photonic.html     "phoGenWaveguide"` (1 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `phoAddWaveguidePorts` | `skdfref/photonic.html` | `phoAddWaveguidePorts` |
| `phoCreatePort` | `skdfref/photonic.html     "phoCreatePort"` | `HTML` |
| `phoGenWaveguide` | `skdfref/photonic.html     "phoGenWaveguide"` | `HTML` |
| `phoIPCGetMessageProcessor` | `skipcref/phoIPC.html` | `phoIPCGetMessageProcessor` |
| `phoIPCGetServerCheck` | `skipcref/phoIPC.html` | `phoIPCGetServerCheck` |
| `phoIPCProcessMarkers` | `skipcref/phoIPC.html` | `phoIPCProcessMarkers` |
| `phoIPCProcessPorts` | `skipcref/phoIPC.html` | `phoIPCProcessPorts` |
| `phoIPCProcessServerMessage` | `skipcref/phoIPC.html` | `phoIPCProcessServerMessage` |
| `phoIPCProcessShapes` | `skipcref/phoIPC.html` | `phoIPCProcessShapes` |
| `phoIPCRegisterMessageProcessor` | `skipcref/phoIPC.html` | `phoIPCRegisterMessageProcessor` |
| `phoIPCRegisterServerCheck` | `skipcref/phoIPC.html` | `phoIPCRegisterServerCheck` |
| `phoIPCServerCheck` | `skipcref/phoIPC.html` | `phoIPCServerCheck` |
| `phoTechIsModePropLocalOnly` | `skdfref/photonic.html` | `phoTechIsModePropLocalOnly"        HTML` |


### PTE API

**13 个函数**，文档位置：

- `sklayoutref/layout.html` (12 个函数)
- `sklayoutref/layout.html    "pteShowLegalLPP"` (1 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `pteGetActiveScopeModes` | `sklayoutref/layout.html` | `pteGetActiveScopeModes` |
| `pteGetMPTSupportMode` | `sklayoutref/layout.html` | `pteGetMPTSupportMode` |
| `pteLoadDefaults` | `sklayoutref/layout.html` | `pteLoadDefaults` |
| `pteLoadLayerSet` | `sklayoutref/layout.html` | `pteLoadLayerSet` |
| `pteSaveAsSynchronizedLayerSet` | `sklayoutref/layout.html` | `pteSaveAsSynchronizedLayerSet` |
| `pteSaveLayerSetListInRepository` | `sklayoutref/layout.html` | `pteSaveLayerSetListInRepository` |
| `pteSetFindModeOn` | `sklayoutref/layout.html` | `pteSetFindModeOn` |
| `pteSetMPTSupportMode` | `sklayoutref/layout.html` | `pteSetMPTSupportMode` |
| `pteSetOnlySelectableWithDepth` | `sklayoutref/layout.html` | `pteSetOnlySelectableWithDepth` |
| `pteSetOnlyVisibleWithDepth` | `sklayoutref/layout.html` | `pteSetOnlyVisibleWithDepth` |
| `pteSetSelectableWithDepth` | `sklayoutref/layout.html` | `pteSetSelectableWithDepth` |
| `pteSetVisibleWithDepth` | `sklayoutref/layout.html` | `pteSetVisibleWithDepth` |
| `pteShowLegalLPP` | `sklayoutref/layout.html    "pteShowLegalLPP"` | `HTML` |


### EAD API

**12 个函数**，文档位置：

- `vead/appC.html` (12 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `eadAddNetsToNetGroup` | `vead/appC.html` | `eadAddNetsToNetGroup` |
| `eadCreateNetGroup` | `vead/appC.html` | `eadCreateNetGroup` |
| `eadDeleteNetGroup` | `vead/appC.html` | `eadDeleteNetGroup` |
| `eadGetNetsInNetGroup` | `vead/appC.html` | `eadGetNetsInNetGroup` |
| `eadGetTriggerDesc` | `vead/appC.html` | `eadGetTriggerDesc` |
| `eadJobClose` | `vead/appC.html` | `eadJobClose` |
| `eadJobStatus` | `vead/appC.html` | `eadJobStatus` |
| `eadJobSubmit` | `vead/appC.html` | `eadJobSubmit` |
| `eadRegTrigger` | `vead/appC.html` | `eadRegTrigger` |
| `eadRemoveNetsFromNetGroup` | `vead/appC.html` | `eadRemoveNetsFromNetGroup` |
| `eadRemoveParasitics` | `vead/appC.html` | `eadRemoveParasitics` |
| `eadUnregTrigger` | `vead/appC.html` | `eadUnregTrigger` |


### VIA API

**12 个函数**，文档位置：

- `sklayoutref/layout.html` (12 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `viaFindTransitions` | `sklayoutref/layout.html` | `viaFindTransitions` |
| `viaGenerateViasAtPoint` | `sklayoutref/layout.html` | `viaGenerateViasAtPoint` |
| `viaGenerateViasFromShapes` | `sklayoutref/layout.html` | `viaGenerateViasFromShapes` |
| `viaGenerateViasInArea` | `sklayoutref/layout.html` | `viaGenerateViasInArea` |
| `viaGetViaOptions` | `sklayoutref/layout.html` | `viaGetViaOptions` |
| `viaLoadViaVariants` | `sklayoutref/layout.html` | `viaLoadViaVariants` |
| `viaRecomputeVias` | `sklayoutref/layout.html` | `viaRecomputeVias` |
| `viaRecomputeViasAtPoint` | `sklayoutref/layout.html` | `viaRecomputeViasAtPoint` |
| `viaRecomputeViasInArea` | `sklayoutref/layout.html` | `viaRecomputeViasInArea` |
| `viaRegisterPostViaServerCallback` | `sklayoutref/layout.html` | `viaRegisterPostViaServerCallback` |
| `viaSaveViaVariants` | `sklayoutref/layout.html` | `viaSaveViaVariants` |
| `viaUnregisterPostViaServerCallback` | `sklayoutref/layout.html` | `viaUnregisterPostViaServerCallback"    HTML` |


### SK API

**11 个函数**，文档位置：

- `skdevref/lint.html` (6 个函数)
- `skdevref/debug.html` (2 个函数)
- `skdevref/tabulator.html` (2 个函数)
- `sktransrefOA/skxoasis.html` (1 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `skDisableMessage` | `skdevref/lint.html` | `skDisableMessage` |
| `skDisableMessageBlock` | `skdevref/lint.html` | `skDisableMessageBlock` |
| `skEnableMessageBlock` | `skdevref/lint.html` | `skEnableMessageBlock` |
| `skIgnoreMessage` | `skdevref/lint.html` | `skIgnoreMessage` |
| `skTabulate` | `skdevref/tabulator.html` | `skTabulate` |
| `skTabulateSKILL` | `skdevref/tabulator.html` | `skTabulateSKILL` |
| `skUnignoreMessage` | `skdevref/lint.html` | `skUnignoreMessage` |
| `skillDebugger` | `skdevref/debug.html` | `skillDebugger` |
| `skillDevStatus` | `skdevref/debug.html` | `skillDevStatus` |
| `sklint` | `skdevref/lint.html` | `sklint` |
| `skspicein` | `sktransrefOA/skxoasis.html` | `skspicein` |


### CPF API

**11 个函数**，文档位置：

- `skcompref/CPF_SKILL.html` (11 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `cpfGetExcludeLibsForSpecialCellRegistration` | `skcompref/CPF_SKILL.html` | `cpfGetExcludeLibsForSpecialCellRegistration` |
| `cpfGetInfoAsWarningList` | `skcompref/CPF_SKILL.html` | `cpfGetInfoAsWarningList` |
| `cpfGetInfoAsWarningList` | `skcompref/CPF_SKILL.html` | `cpfGetInfoAsWarningList` |
| `cpfGetPortRelatedPGNets` | `skcompref/CPF_SKILL.html` | `cpfGetPortRelatedPGNets` |
| `cpfGetStdLibCells` | `skcompref/CPF_SKILL.html` | `cpfGetStdLibCells` |
| `cpfGetWarningAsInfoList` | `skcompref/CPF_SKILL.html` | `cpfGetWarningAsInfoList` |
| `cpfReportInfoAsWarning` | `skcompref/CPF_SKILL.html` | `cpfReportInfoAsWarning` |
| `cpfReportWarningAsInfo` | `skcompref/CPF_SKILL.html` | `cpfReportWarningAsInfo` |
| `cpfSetExcludeLibsForSpecialCellRegistration` | `skcompref/CPF_SKILL.html` | `cpfSetExcludeLibsForSpecialCellRegistration` |
| `cpfSetPortRelatedPGNets` | `skcompref/CPF_SKILL.html` | `cpfSetPortRelatedPGNets` |
| `cpfSetStdLibCells` | `skcompref/CPF_SKILL.html` | `cpfSetStdLibCells` |


### SPD API

**11 个函数**，文档位置：

- `sklayoutref/spd.html` (11 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `spdCalcOdSpacingWithPoly` | `sklayoutref/spd.html` | `spdCalcOdSpacingWithPoly` |
| `spdGetAbutName` | `sklayoutref/spd.html` | `spdGetAbutName` |
| `spdGetAbutStrategy` | `sklayoutref/spd.html` | `spdGetAbutStrategy` |
| `spdGetSymDeviceInfo` | `sklayoutref/spd.html` | `spdGetSymDeviceInfo` |
| `spdGetUserAbutProc` | `sklayoutref/spd.html` | `spdGetUserAbutProc` |
| `spdGetUserFlowProc` | `sklayoutref/spd.html` | `spdGetUserFlowProc` |
| `spdPerformAbutment` | `sklayoutref/spd.html` | `spdPerformAbutment` |
| `spdRegUserAbutProc` | `sklayoutref/spd.html` | `spdRegUserAbutProc` |
| `spdRegUserFlowProc` | `sklayoutref/spd.html` | `spdRegUserFlowProc` |
| `spdUnregUserAbutProc` | `sklayoutref/spd.html` | `spdUnregUserAbutProc` |
| `spdUnregUserFlowProc` | `sklayoutref/spd.html` | `spdUnregUserFlowProc` |


### OPC API

**10 个函数**，文档位置：

- `skcompref/chap2.html` (10 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `opcAddListToSet` | `skcompref/chap2.html` | `opcAddListToSet` |
| `opcAddObjectToSet` | `skcompref/chap2.html` | `opcAddObjectToSet` |
| `opcAllSetsInCellView` | `skcompref/chap2.html` | `opcAllSetsInCellView` |
| `opcClearSet` | `skcompref/chap2.html` | `opcClearSet` |
| `opcCreatePersistentSet` | `skcompref/chap2.html` | `opcCreatePersistentSet` |
| `opcCreateTransientSet` | `skcompref/chap2.html` | `opcCreateTransientSet` |
| `opcDestroySet` | `skcompref/chap2.html` | `opcDestroySet` |
| `opcFindSet` | `skcompref/chap2.html` | `opcFindSet` |
| `opcReleaseSet` | `skcompref/chap2.html` | `opcReleaseSet` |
| `opcRemoveObjectFromSet` | `skcompref/chap2.html` | `opcRemoveObjectFromSet` |


### SCH API

**9 个函数**，文档位置：

- `skcompref/chap2.html` (7 个函数)
- `skcompref/chap1.html` (1 个函数)
- `"schCreateSplitPrimarySymbol"` (1 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `schAttachLibToPackageTech` | `skcompref/chap2.html` | `schAttachLibToPackageTech` |
| `schClearConn` | `skcompref/chap2.html` | `schClearConn` |
| `schCreateSplitPrimarySymbol         $skcompref/chap2.html` | `"schCreateSplitPrimarySymbol"` | `HTML` |
| `schHiSetOrigin` | `skcompref/chap1.html` | `schHiSetOrigin` |
| `schIsFlightLine` | `skcompref/chap2.html` | `schIsFlightLine` |
| `schIsInCheckHier` | `skcompref/chap2.html` | `schIsInCheckHier` |
| `schIsWire` | `skcompref/chap2.html` | `schIsWire` |
| `schRegisterFixedMenu` | `skcompref/chap2.html` | `schRegisterFixedMenu` |
| `schSetOrigin` | `skcompref/chap2.html` | `schSetOrigin` |


### RELX API

**9 个函数**，文档位置：

- `maeSKILLref/maestroSKILL.html` (9 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `relxAddSetupRelxOption` | `maeSKILLref/maestroSKILL.html` | `relxAddSetupRelxOption` |
| `relxCreateCustomizedTab` | `maeSKILLref/maestroSKILL.html` | `relxCreateCustomizedTab` |
| `relxCustomizeDisplayOrEnableStatus` | `maeSKILLref/maestroSKILL.html` | `relxCustomizeDisplayOrEnableStatus` |
| `relxDisplayDiscField` | `maeSKILLref/maestroSKILL.html` | `relxDisplayDiscField` |
| `relxEnableDiscField` | `maeSKILLref/maestroSKILL.html` | `relxEnableDiscField` |
| `relxEnableFormTab` | `maeSKILLref/maestroSKILL.html` | `relxEnableFormTab` |
| `relxGetCustomTabName` | `maeSKILLref/maestroSKILL.html` | `relxGetCustomTabName` |
| `relxHideAgeCalculationApproachField` | `maeSKILLref/maestroSKILL.html` | `relxHideAgeCalculationApproachField` |
| `relxInitOptionsInCdsenv` | `maeSKILLref/maestroSKILL.html` | `relxInitOptionsInCdsenv` |


### VHMS API

**8 个函数**，文档位置：

- `netlistsimulateref/vhdlToolboxFunctions.html` (8 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `vhmsCompilationFailure` | `netlistsimulateref/vhdlToolboxFunctions.html` | `vhmsCompilationFailure` |
| `vhmsDefaultEdit` | `netlistsimulateref/vhdlToolboxFunctions.html` | `vhmsDefaultEdit` |
| `vhmsGetCellParameters` | `netlistsimulateref/vhdlToolboxFunctions.html` | `vhmsGetCellParameters` |
| `vhmsPinListToVHDLAMS` | `netlistsimulateref/vhdlToolboxFunctions.html` | `vhmsPinListToVHDLAMS` |
| `vhmsSaveFile` | `netlistsimulateref/vhdlToolboxFunctions.html` | `vhmsSaveFile` |
| `vhmsSymbolToPinListGen` | `netlistsimulateref/vhdlToolboxFunctions.html` | `vhmsSymbolToPinListGen` |
| `vhmsToPinList` | `netlistsimulateref/vhdlToolboxFunctions.html` | `vhmsToPinList` |
| `vhmsUpdateCellCDFParams` | `netlistsimulateref/vhdlToolboxFunctions.html` | `vhmsUpdateCellCDFParams` |


### PO API

**8 个函数**，文档位置：

- `sktransrefOA/skxstream.html` (6 个函数)
- `oceanref/chap10.html` (1 个函数)
- `vivaxlug/appD.html` (1 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `poCellNameMap` | `sktransrefOA/skxstream.html` | `poCellNameMap` |
| `poLayerMap` | `sktransrefOA/skxstream.html` | `poLayerMap` |
| `poParamCellNameMap` | `sktransrefOA/skxstream.html` | `poParamCellNameMap` |
| `poPostTranslate` | `sktransrefOA/skxstream.html` | `poPostTranslate` |
| `poPreTranslate` | `sktransrefOA/skxstream.html` | `poPreTranslate` |
| `poTextMap` | `sktransrefOA/skxstream.html` | `poTextMap` |
| `pow_OCEAN` | `oceanref/chap10.html` | `pow` |
| `pow_ViVA_SKILL` | `vivaxlug/appD.html` | `pow` |


### PI API

**8 个函数**，文档位置：

- `sktransrefOA/skxstream.html` (6 个函数)
- `oceanref/chap10.html` (1 个函数)
- `vivaxlug/appD.html` (1 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `piCellNameMap` | `sktransrefOA/skxstream.html` | `piCellNameMap` |
| `piLayerMap` | `sktransrefOA/skxstream.html` | `piLayerMap` |
| `piPostTranslate` | `sktransrefOA/skxstream.html` | `piPostTranslate` |
| `piPreTranslate` | `sktransrefOA/skxstream.html` | `piPreTranslate` |
| `piTextMap` | `sktransrefOA/skxstream.html` | `piTextMap` |
| `pipoDisplay` | `sktransrefOA/skxstream.html` | `pipoDisplay` |
| `pir_OCEAN` | `oceanref/chap10.html` | `pir` |
| `pir_ViVA_SKILL` | `vivaxlug/appD.html` | `pir` |


### RF API

**7 个函数**，文档位置：

- `vivaxlskill/chap4.html` (4 个函数)
- `vivaxlskill/chap4.html             "rfEdgePhaseNoise"` (1 个函数)
- `vivaxlskill/chap4.html           "rfJc"` (1 个函数)
- `vivaxlskill/chap4.html           "rfJcc"` (1 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `rfEdgePhaseNoise_ViVA_SKILL` | `vivaxlskill/chap4.html             "rfEdgePhaseNoise"` | `HTML` |
| `rfGetMinDampFactor_ViVA_SKILL` | `vivaxlskill/chap4.html` | `rfGetMinDampFactor` |
| `rfInputNoise_ViVA_SKILL` | `vivaxlskill/chap4.html` | `rfInputNoise` |
| `rfJc_ViVA_SKILL` | `vivaxlskill/chap4.html           "rfJc"` | `HTML` |
| `rfJcc_ViVA_SKILL` | `vivaxlskill/chap4.html           "rfJcc"` | `HTML` |
| `rfOutputNoise_ViVA_SKILL` | `vivaxlskill/chap4.html` | `rfOutputNoise` |
| `rfTransferFunction_ViVA_SKILL` | `vivaxlskill/chap4.html` | `rfTransferFunction` |


### CPH API

**7 个函数**，文档位置：

- `sklayoutref/cph.html` (7 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `cphChangeEditMode` | `sklayoutref/cph.html` | `cphChangeEditMode` |
| `cphGetSchInstPhysicalBinding` | `sklayoutref/cph.html` | `cphGetSchInstPhysicalBinding"          HTML` |
| `cphGetTopCellName` | `sklayoutref/cph.html` | `cphGetTopCellName` |
| `cphGetTopLibName` | `sklayoutref/cph.html` | `cphGetTopLibName` |
| `cphGetTopViewName` | `sklayoutref/cph.html` | `cphGetTopViewName` |
| `cphIsReadOnly` | `sklayoutref/cph.html` | `cphIsReadOnly` |
| `cphSetOccurParamToCheck` | `sklayoutref/cph.html` | `cphSetOccurParamToCheck` |


### WE API

**7 个函数**，文档位置：

- `sklayoutref/wire.html` (3 个函数)
- `sklayoutref/wire.fm` (1 个函数)
- `sklayoutref/wire.html    "weHiInteractiveRouting"` (1 个函数)
- `sklayoutref/wire.html    "weHiCycleViaDefDown"` (1 个函数)
- `sklayoutref/wire.html    "weHiCycleViaDefUp"` (1 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `weAddCustomTransitionMenuItem` | `sklayoutref/wire.html` | `weAddCustomTransitionMenuItem` |
| `weCycleCutColorVia` | `sklayoutref/wire.fm` | `weCycleCutColorVia` |
| `weGetCustomTransitionMenuItems` | `sklayoutref/wire.html` | `weGetCustomTransitionMenuItems` |
| `weHiCycleViaDefDown` | `sklayoutref/wire.html    "weHiCycleViaDefDown"` | `HTML` |
| `weHiCycleViaDefUp` | `sklayoutref/wire.html    "weHiCycleViaDefUp"` | `HTML` |
| `weHiInteractiveRouting` | `sklayoutref/wire.html    "weHiInteractiveRouting"` | `HTML` |
| `weRemoveCustomTransitionMenuItem` | `sklayoutref/wire.html` | `weRemoveCustomTransitionMenuItem` |


### DRD API

**7 个函数**，文档位置：

- `sklayoutref/drd.html` (5 个函数)
- `sklayoutref/drd.html    "drdOptionsSet"` (1 个函数)
- `sklayoutref/drd.html    "drdOptionUpdateLayer"` (1 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `drdGetAllowedWidth` | `sklayoutref/drd.html` | `drdGetAllowedWidth` |
| `drdGetMinSpacing` | `sklayoutref/drd.html` | `drdGetMinSpacing` |
| `drdGetMinSpanLengthSpacing` | `sklayoutref/drd.html` | `drdGetMinSpanLengthSpacing` |
| `drdGetMinVoltageSpacing` | `sklayoutref/drd.html` | `drdGetMinVoltageSpacing` |
| `drdOptionUpdateLayer` | `sklayoutref/drd.html    "drdOptionUpdateLayer"` | `HTML` |
| `drdOptionsSet` | `sklayoutref/drd.html    "drdOptionsSet"` | `HTML` |
| `drdToggleSmartSnapModeForDiscreteSpacing` | `sklayoutref/drd.html` | `drdToggleSmartSnapModeForDiscreteSpacing` |


### HDB API

**7 个函数**，文档位置：

- `skdfref/chap2.html` (6 个函数)
- `"hdbBindBit"` (1 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `hdbBindBit                          $skdfref/chap2.html` | `"hdbBindBit"` | `HTML` |
| `hdbBitHasRules` | `skdfref/chap2.html` | `hdbBitHasRules` |
| `hdbHasIterInstBitRules` | `skdfref/chap2.html` | `hdbHasIterInstBitRules` |
| `hdbIsIterInst` | `skdfref/chap2.html` | `hdbIsIterInst` |
| `hdbIterInstHasBitRules` | `skdfref/chap2.html` | `hdbIterInstHasBitRules` |
| `hdbPushBitCell` | `skdfref/chap2.html` | `hdbPushBitCell` |
| `hdbSaveACopy` | `skdfref/chap2.html` | `hdbSaveACopy` |


### LOB API

**7 个函数**，文档位置：

- `autodevicelayoutflow/APIs.html` (5 个函数)
- `"lobRegisterTapFillDefsProc"` (1 个函数)
- `sklayoutref/vplacer.html` (1 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `lobAddCopyFill` | `autodevicelayoutflow/APIs.html` | `lobAddCopyFill` |
| `lobBaseLayerDummyFillCB` | `autodevicelayoutflow/APIs.html` | `lobBaseLayerDummyFillCB` |
| `lobBaseLayerDummyFillWrapperCB` | `autodevicelayoutflow/APIs.html` | `lobBaseLayerDummyFillWrapperCB"    HTML` |
| `lobIsCopyFill` | `autodevicelayoutflow/APIs.html` | `lobIsCopyFill` |
| `lobRegisterTapFillDefsProc          $sklayoutref/vplacer.html` | `"lobRegisterTapFillDefsProc"` | `HTML` |
| `lobRemoveCopyFill` | `autodevicelayoutflow/APIs.html` | `lobRemoveCopyFill` |
| `lobUnRegisterTapFillDefsProc` | `sklayoutref/vplacer.html` | `lobUnRegisterTapFillDefsProc"          HTML` |


### VPM API

**7 个函数**，文档位置：

- `vpm/VPM_SKILL.html` (2 个函数)
- `vpm/VPM_SKILL.html                "vpmImportPowerIntent"` (1 个函数)
- `vpm/VPM_SKILL.html                "vpmExtractPowerIntent"` (1 个函数)
- `vpm/VPM_SKILL.html                "vpmExportPowerModel"` (1 个函数)
- `"vpmLoadInDesignViolations"` (1 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `vpmExportDotLib` | `vpm/VPM_SKILL.html` | `vpmExportDotLib` |
| `vpmExportPowerIntent` | `vpm/VPM_SKILL.html` | `vpmExportPowerIntent` |
| `vpmExportPowerModel` | `vpm/VPM_SKILL.html                "vpmExportPowerModel"` | `HTML` |
| `vpmExtractPowerIntent` | `vpm/VPM_SKILL.html                "vpmExtractPowerIntent"` | `HTML` |
| `vpmImportPowerIntent` | `vpm/VPM_SKILL.html                "vpmImportPowerIntent"` | `HTML` |
| `vpmLoadInDesignViolations               $vpm/VPM_SKILL.html` | `"vpmLoadInDesignViolations"` | `HTML` |
| `vpmRunInDesignChecks` | `vpm/VPM_SKILL.html             "vpmRunInDesignChecks"` | `HTML` |


### VHDL API

**6 个函数**，文档位置：

- `netlistsimulateref/vhdlToolboxFunctions.html` (6 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `vhdlHiImport` | `netlistsimulateref/vhdlToolboxFunctions.html` | `vhdlHiImport` |
| `vhdlHiInvokeToolBox` | `netlistsimulateref/vhdlToolboxFunctions.html` | `vhdlHiInvokeToolBox` |
| `vhdlImport` | `netlistsimulateref/vhdlToolboxFunctions.html` | `vhdlImport` |
| `vhdlPinListToVHDL` | `netlistsimulateref/vhdlToolboxFunctions.html` | `vhdlPinListToVHDL` |
| `vhdlRegisterSimulator` | `netlistsimulateref/vhdlToolboxFunctions.html` | `vhdlRegisterSimulator` |
| `vhdlToPinList` | `netlistsimulateref/vhdlToolboxFunctions.html` | `vhdlToPinList` |


### AU API

**6 个函数**，文档位置：

- `sktransrefOA/skcdlout.html` (2 个函数)
- `parasimSKILL/parasimSKILLFunctions.html` (1 个函数)
- `skpcellref/parasimSKILLFunctions.html` (1 个函数)
- `skpcellref/graphicalFunctions.html` (1 个函数)
- `"auCdlPrintCommentsOnFileFooter"` (1 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `auCdlAlwaysAddPrefixInInstName` | `sktransrefOA/skcdlout.html` | `auCdlAlwaysAddPrefixInInstName` |
| `auCdlPrintAdditionalCommentsOnFileHeader` | `sktransrefOA/skcdlout.html` | `auCdlPrintAdditionalCommentsOnFileHeader` |
| `auCdlPrintCommentsOnFileFooter                  $sktransrefOA/skcdlout.html` | `"auCdlPrintCommentsOnFileFooter"` | `HTML` |
| `auHiUltraPCell` | `skpcellref/graphicalFunctions.html` | `auHiUltraPCell` |
| `auLvsGetLabelSuffix` | `parasimSKILL/parasimSKILLFunctions.html` | `auLvsGetLabelSuffix` |
| `auLvsGetLabelSuffix` | `skpcellref/parasimSKILLFunctions.html` | `auLvsGetLabelSuffix` |


### RDB API

**6 个函数**，文档位置：

- `vivaxlskill/chap5.html` (6 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `rdbLoadResults_ViVA_SKILL` | `vivaxlskill/chap5.html` | `rdbLoadResults` |
| `rdbReloadResults_ViVA_SKILL` | `vivaxlskill/chap5.html` | `rdbReloadResults` |
| `rdbSetCurrentDirectory_ViVA_SKILL` | `vivaxlskill/chap5.html` | `rdbSetCurrentDirectory` |
| `rdbShowDialog_ViVA_SKILL` | `vivaxlskill/chap5.html` | `rdbShowDialog` |
| `rdbUnloadResults_ViVA_SKILL` | `vivaxlskill/chap5.html` | `rdbUnloadResults` |
| `rdbWriteToFormat_ViVA_SKILL` | `vivaxlskill/chap5.html` | `rdbWriteToFormat` |


### VRF API

**6 个函数**，文档位置：

- `vrf/VRF_SKILL.html` (5 个函数)
- `"vrfExportPackage"` (1 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `vrfExportPackage                $vrf/VRF_SKILL.html` | `"vrfExportPackage"` | `HTML` |
| `vrfLowerPriority` | `vrf/VRF_SKILL.html` | `vrfLowerPriority` |
| `vrfRaisePriority` | `vrf/VRF_SKILL.html` | `vrfRaisePriority` |
| `vrfSipGet` | `vrf/VRF_SKILL.html` | `vrfSipGet` |
| `vrfSipSet` | `vrf/VRF_SKILL.html` | `vrfSipSet` |
| `vrfTLineAbut` | `vrf/VRF_SKILL.html` | `vrfTLineAbut` |


### LCE API

**5 个函数**，文档位置：

- `sklayoutref/lx.html` (5 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `lceAddSimpleStopLayers` | `sklayoutref/lx.html` | `lceAddSimpleStopLayers` |
| `lceDestroyVoidShapes` | `sklayoutref/lx.html` | `lceDestroyVoidShapes` |
| `lceRegenerateVoidShapes` | `sklayoutref/lx.html` | `lceRegenerateVoidShapes` |
| `lceShortLocatorChaseAndSave` | `sklayoutref/lx.html` | `lceShortLocatorChaseAndSave` |
| `lceShortLocatorRaiseForm` | `sklayoutref/lx.html` | `lceShortLocatorRaiseForm` |


### TPA API

**5 个函数**，文档位置：

- `sklayoutref/layout.html` (3 个函数)
- `sklayoutref/layout.html    "tpaSelectWSSPDef"` (2 个函数)

**函数列表:**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `tpaSelectWSSPDef` | `sklayoutref/layout.html` | `tpaSelectWSSPDef` |
| `tpaSelectWSSPDef` | `sklayoutref/layout.html    "tpaSelectWSSPDef"` | `HTML` |
| `tpaSelectWSSPDef` | `sklayoutref/layout.html    "tpaSelectWSSPDef"` | `HTML` |
| `tpaSetAllDefsVisible` | `sklayoutref/layout.html` | `tpaSetAllDefsVisible` |
| `tpaSetFilterByName` | `sklayoutref/layout.html` | `tpaSetFilterByName` |


### 其他函数

**721 个函数**

| 函数名 | 文档文件 | HTML锚点 |
|--------|----------|----------|
| `1/x_ViVA_SKILL` | `vivaxlug/appD.html` | `1/x` |
| `10**x_ViVA_SKILL` | `vivaxlug/appD.html` | `10**x` |
| `;caar, caaar, caadr, cadr, caddr, cdar, cddr, ..` | `sklangref/list.html` | `caar` |
| `;case` | `sklangref/controlflow.html` | `case` |
| `;case` | `sklangref/controlflow.html` | `case` |
| `;getIsObjectPartiallySelected` | `skdfref/chap1.html` | `getIsObjectPartiallySelected` |
| `;hnlGetInstanceCount` | `skartistref/chap4.html` | `hnlGetInstanceCount` |
| `;vi, vii, vim` | `sklangref/environment.html` | `vi` |
| `ALIAS` | `adexlSKILLref/measures.html` | `ALIAS` |
| `ERC` | `netlistsimulateref/ossFunctions.html` | `ERC` |
| `Mu_ViVA_SKILL` | `vivaxlskill/chap4.html` | `muC` |
| `Mu_prime_ViVA_SKILL` | `vivaxlskill/chap4.html` | `muprimeC` |
| `OS_ViVA_SKILL` | `vivaxlskill/chap2.html` | `OS` |
| `OT_ViVA_SKILL` | `vivaxlskill/chap2.html` | `OT` |
| `PN_OCEAN` | `oceanref/chap10.html` | `PN` |
| `PN_ViVA_SKILL` | `vivaxlug/appD.html` | `PN` |
| `Refreshes_OCEAN` | `oceanref/chap10.html` | `Refreshes` |
| `Rn_ViVA_SKILL` | `vivaxlug/appD.html` | `Rn` |
| `SaveGraphImage_OCEAN` | `oceanref/chap8.html` | `SaveGraphImage` |
| `a2d_ViVA_SKILL` | `vivaxlug/appD.html` | `a2d` |
| `aaSP_ViVA_SKILL` | `vivaxlskill/chap4.html` | `aaSP` |
| `abGetCurrentIncompleteNetFilter` | `sklayoutref/lx.html` | `abGetCurrentIncompleteNetFilter` |
| `abHiFindMarker` | `sklayoutref/lx.html` | `abHiFindMarker` |
| `abSetIncompleteNetFilter` | `sklayoutref/lx.html` | `abSetIncompleteNetFilter` |
| `abeLayerFromCellView` | `sklayoutref/abe.html` | `abeLayerFromCellView` |
| `abeLayerToBlockages` | `sklayoutref/abe.html` | `abeLayerToBlockages` |
| `abeLayerToCellView` | `sklayoutref/abe.html` | `abeLayerToCellview` |
| `ac_OCEAN` | `oceanref/chap6.html` | `ac` |
| `acdlArtPrintIncludedNetlist` | `skartistref/chap4.html` | `acdlArtPrintIncludedNetlist"            HTML` |
| `acos_OCEAN` | `oceanref/chap10.html` | `acos` |
| `acos_ViVA_SKILL` | `vivaxlug/appD.html` | `acos` |
| `acosh_ViVA_SKILL` | `vivaxlug/appD.html` | `acosh` |
| `add1_OCEAN` | `oceanref/chap10.html` | `add1` |
| `addDependent` | `skoopref/dmp.html` | `addDependent` |
| `addSubwindowTitle_OCEAN` | `oceanref/chap8.html` | `addSubwindowTitle` |
| `addSubwindow_OCEAN` | `oceanref/chap8.html` | `addSubwindow` |
| `addTitle_OCEAN` | `oceanref/chap8.html` | `addTitle` |
| `addWaveLabel_OCEAN` | `oceanref/chap8.html` | `addWaveLabel` |
| `addWindowLabel_OCEAN` | `oceanref/chap8.html` | `addWindowLabel` |
| `adtFFT_ViVA_SKILL` | `vivaxlskill/chap4.html` | `adtFFT` |
| `adtIFFT_ViVA_SKILL` | `vivaxlskill/chap4.html` | `adtIFFT` |
| `allocateInstance` | `skoopref/classesinstances.html` | `allocateInstance` |
| `analog2Digital_ViVA_SKILL` | `vivaxlug/appD.html` | `analog2Digital` |
| `analysis_OCEAN` | `oceanref/chap6.html` | `analysis` |
| `angle_ViVA_SKILL` | `vivaxlug/appD.html` | `angle` |
| `annLoadAnnotationData           $skcompref/chap2.html` | `"annLoadAnnotationData"` | `HTML` |
| `annRetrieveFromEffectiveCDF` | `skartistref/chap16.html` | `annRetrieveFromEffectiveCDF` |
| `annSaveAnnotationData           $skcompref/chap2.html` | `"annSaveAnnotationData"` | `HTML` |
| `ansiDefmethod` | `skoopref/genericfunc.html` | `ansiDefmethod` |
| `apPlaceAuto` | `autodevicelayoutflow/APIs.html` | `apPlaceAuto` |
| `apSnapInsts` | `autodevicelayoutflow/APIs.html` | `apSnapInsts` |
| `api_more_info_default` | `customhome_ch/customhome_chTOC.html` | `top` |
| `append` | `sklangref/list.html` | `append` |
| `append1` | `sklangref/list.html` | `append1` |
| `appendPath_OCEAN` | `oceanref/chap5.html` | `appendPath` |
| `appendWaves_ViVA_SKILL` | `vivaxlskill/chap3.html` | `appendWaves` |
| `argmax_ViVA_SKILL` | `vivaxlug/appD.html` | `argmax` |
| `argmin_ViVA_SKILL` | `vivaxlug/appD.html` | `argmin` |
| `armSetCalc_ViVA_SKILL` | `vivaxlskill/chap4.html` | `armSetCalc` |
| `assoc` | `sklangref/datastruct.html` | `assoc` |
| `assq` | `sklangref/datastruct.html` | `assoc` |
| `assv` | `sklangref/datastruct.html` | `assoc` |
| `atan_OCEAN` | `oceanref/chap10.html` | `atan` |
| `atan_ViVA_SKILL` | `vivaxlug/appD.html` | `atan` |
| `atanh_ViVA_SKILL` | `vivaxlug/appD.html` | `atanh` |
| `average_OCEAN` | `oceanref/chap10.html` | `average` |
| `average_ViVA_SKILL` | `vivaxlug/appD.html` | `average` |
| `b1f_OCEAN` | `oceanref/chap10.html` | `b1f` |
| `b1f_ViVA_SKILL` | `vivaxlug/appD.html` | `b1f` |
| `bandwidth_OCEAN` | `oceanref/chap10.html` | `bandwidth` |
| `bandwidth_ViVA_SKILL` | `vivaxlug/appD.html` | `bandwidth` |
| `baseLine_ViVA_SKILL` | `vivaxlskill/chap4.html` | `baseLine` |
| `break` | `skdevref/debug.html` | `break` |
| `breakpt` | `skdevref/debug.html` | `breakpt` |
| `breakptMethod` | `skdevref/debug.html` | `breakptMethod` |
| `busTransition_ViVA_SKILL` | `vivaxlug/appD.html` | `bustransition` |
| `cPwrContour_OCEAN` | `oceanref/chap10.html` | `cPwrContour` |
| `cReflContour_OCEAN` | `oceanref/chap10.html` | `cReflContour` |
| `caaar` | `sklangref/list.html` | `caar` |
| `caadr` | `sklangref/list.html` | `caar` |
| `caar` | `sklangref/list.html` | `caar` |
| `caar, caaar, caadr, cadr, caddr, cdar, cddr, ...` | `sklangref/list.html` | `caar` |
| `caddr` | `sklangref/list.html` | `caar` |
| `cadr` | `sklangref/list.html` | `caar` |
| `case` | `sklangref/controlflow.html` | `case` |
| `case_OCEAN` | `oceanref/chap13.html` | `case` |
| `caseq` | `sklangref/controlflow.html` | `caseq` |
| `cat` | `netlistsimulateref/ossFunctions.html` | `cat` |
| `cdar` | `sklangref/list.html` | `caar` |
| `cddr` | `sklangref/list.html` | `caar` |
| `cdfEnableScaleFactorRetentionForZero` | `skartistref/chap21.html` | `cdfEnableScaleFactorRetentionForZero` |
| `cdsGetNetlistMode` | `netlistsimulateref/ossFunctions.html` | `cdsGetNetlistMode` |
| `cdsSetNetlistMode` | `netlistsimulateref/ossFunctions.html` | `cdsSetNetlistMode` |
| `changeClass` | `skoopref/classesinstances.html` | `changeClass` |
| `checkContextBit` | `skdevref/context.html` | `checkContextBit` |
| `className` | `skoopref/classesinstances.html` | `className` |
| `classOf` | `skoopref/classesinstances.html` | `classOf` |
| `classp` | `skoopref/classesinstances.html` | `classp` |
| `clear` | `skdevref/debug.html` | `clear` |
| `clearAll_OCEAN` | `oceanref/chap8.html` | `clearAll` |
| `clearSubwindow_OCEAN` | `oceanref/chap8.html` | `clearSubwindow` |
| `clipX_OCEAN` | `oceanref/chap10.html` | `clipX` |
| `clip_OCEAN` | `oceanref/chap10.html` | `clip` |
| `clip_ViVA_SKILL` | `vivaxlug/appD.html` | `clip` |
| `closeResults_OCEAN` | `oceanref/chap10.html` | `closeResults` |
| `close_OCEAN` | `oceanref/chap14.html` | `close` |
| `compare_OCEAN` | `oceanref/chap10.html` | `compare` |
| `compare_ViVA_SKILL` | `vivaxlug/appD.html` | `compare` |
| `complex_OCEAN` | `oceanref/chap10.html` | `complex` |
| `complexp_OCEAN` | `oceanref/chap10.html` | `complexp` |
| `compressionVRICurves_OCEAN` | `oceanref/chap10.html` | `compressionVRICurves` |
| `compressionVRI_OCEAN` | `oceanref/chap10.html` | `compressionVRI` |
| `compressionVRI_ViVA_SKILL` | `vivaxlug/appD.html` | `compressionVRI` |
| `compression_OCEAN` | `oceanref/chap10.html` | `compression` |
| `compression_ViVA_SKILL` | `vivaxlug/appD.html` | `compression` |
| `cond_OCEAN` | `oceanref/chap13.html` | `cond` |
| `conjugate_OCEAN` | `oceanref/chap10.html` | `conjugate` |
| `conjugate_ViVA_SKILL` | `vivaxlug/appD.html` | `conjugate` |
| `conn2Sch` | `importconnref/conn2sch.html` | `conn2Sch` |
| `conn2SchImpHdlDisplay` | `importconnref/conn2sch.html` | `conn2SchImpHdlDisplay` |
| `conn2SchStartUp` | `importconnref/conn2sch.html` | `conn2SchStartUp` |
| `connectRules_OCEAN` | `oceanref/chap6.html` | `connectRules` |
| `cont` | `skdevref/debug.html` | `cont` |
| `cont, continue` | `skdevref/debug.html` | `cont` |
| `continue` | `skdevref/debug.html` | `cont` |
| `converge_OCEAN` | `oceanref/chap6.html` | `converge` |
| `convolve_OCEAN` | `oceanref/chap10.html` | `convolve` |
| `convolve_ViVA_SKILL` | `vivaxlug/appD.html` | `convolve` |
| `cos_OCEAN` | `oceanref/chap10.html` | `cos` |
| `cos_ViVA_SKILL` | `vivaxlug/appD.html` | `cos` |
| `cosh_ViVA_SKILL` | `vivaxlug/appD.html` | `cosh` |
| `count` | `skdevref/debug.html` | `count` |
| `createFinalNetlist_OCEAN` | `oceanref/chap6.html` | `createFinalNetlist` |
| `createNetlist_OCEAN` | `oceanref/chap6.html` | `createNetlist` |
| `cross_OCEAN` | `oceanref/chap10.html` | `cross` |
| `cross_ViVA_SKILL` | `vivaxlug/appD.html` | `cross` |
| `currentSubwindow_OCEAN` | `oceanref/chap8.html` | `currentSubwindow` |
| `currentWindow_OCEAN` | `oceanref/chap8.html` | `currentWindow` |
| `d2a_ViVA_SKILL` | `vivaxlug/appD.html` | `d2a` |
| `dB10_ViVA_SKILL` | `vivaxlug/appD.html` | `dB10` |
| `dB20_ViVA_SKILL` | `vivaxlug/appD.html` | `dB20` |
| `dBm_ViVA_SKILL` | `vivaxlug/appD.html` | `dBm` |
| `dataTypes_OCEAN` | `oceanref/chap7.html` | `dataTypes` |
| `dc_OCEAN` | `oceanref/chap6.html` | `dc` |
| `dcmatchSummary_OCEAN` | `oceanref/chap8.html` | `dcmatchSummary` |
| `deBeginConfigurePlugins` | `skdfref/chap3.html` | `deBeginConfigurePlugins` |
| `deEndConfigurePlugins` | `skdfref/chap3.html` | `deEndConfigurePlugins` |
| `debugQuit` | `skdevref/debug.html` | `debugQuit` |
| `debugStatus` | `skdevref/debug.html` | `debugStatus` |
| `decode` | `sklangref/controlflow.html         "decode"` | `HTML` |
| `defCapDepends` | `skdevref/context.html` | `defCapDepends` |
| `defCapPrefixes` | `skdevref/context.html` | `defCapPrefixes` |
| `defInitProc` | `skdevref/context.html` | `defInitProc` |
| `defclass` | `skoopref/classesinstances.html` | `defclass` |
| `defgeneric` | `skoopref/genericfunc.html` | `defgeneric` |
| `definPostTranslate` | `sktransrefOA/sklefdef.html` | `definPostTranslate` |
| `definPreTranslate` | `sktransrefOA/sklefdef.html` | `definPreTranslate` |
| `definitionFile_OCEAN` | `oceanref/chap6.html` | `definitionFile` |
| `defmethod` | `skoopref/genericfunc.html` | `defmethod` |
| `defoutPostTranslate` | `sktransrefOA/sklefdef.html` | `defoutPostTranslate` |
| `defoutPreTranslate` | `sktransrefOA/sklefdef.html` | `defoutPreTranslate` |
| `defsetf` | `sklangref/funcprog.html` | `defsetf` |
| `delayMeasure_ViVA_SKILL` | `vivaxlug/appD.html` | `delayMeasure` |
| `delay_OCEAN` | `oceanref/chap10.html` | `delay` |
| `delay_ViVA_SKILL` | `vivaxlug/appD.html` | `delay` |
| `deleteJob_OCEAN` | `oceanref/chap12.html` | `deleteJob` |
| `deleteOpPoint_OCEAN` | `oceanref/chap6.html` | `deleteOpPoint` |
| `deleteSubckt_OCEAN` | `oceanref/chap7.html` | `deleteSubckt` |
| `deleteSubwindow_OCEAN` | `oceanref/chap8.html` | `deleteSubwindow` |
| `deleteWaveform_OCEAN` | `oceanref/chap8.html` | `deleteWaveform` |
| `delete_OCEAN` | `oceanref/chap6.html` | `delete` |
| `deriv_OCEAN` | `oceanref/chap10.html` | `deriv` |
| `desVar_OCEAN` | `oceanref/chap6.html` | `desVar` |
| `describe` | `sklangref/core.html` | `describe` |
| `design_OCEAN` | `oceanref/chap6.html` | `design` |
| `dft_OCEAN` | `oceanref/chap10.html` | `dft` |
| `dft_ViVA_SKILL` | `vivaxlug/appD.html` | `dft` |
| `dftbb_OCEAN` | `oceanref/chap10.html` | `dftbb` |
| `dftbb_ViVA_SKILL` | `vivaxlug/appD.html` | `dftbb` |
| `digitalHostMode_OCEAN` | `oceanref/chap12.html` | `digitalHostMode` |
| `digitalHostName_OCEAN` | `oceanref/chap12.html` | `digitalHostName` |
| `discipline_OCEAN` | `oceanref/chap6.html` | `discipline` |
| `displayMode_OCEAN` | `oceanref/chap8.html` | `displayMode` |
| `displayNetlist_OCEAN` | `oceanref/chap6.html` | `displayNetlist` |
| `displaySubckt_OCEAN` | `oceanref/chap7.html` | `displaySubckt` |
| `dlGetRasterTextWidth                                $skuiref/appA.html` | `"dlGetRasterTextWidth"` | `HTML` |
| `dlQueryRasterFont                                   $skuiref/appA.html` | `"dlQueryRasterFont"` | `HTML` |
| `dnl_OCEAN` | `oceanref/chap10.html` | `dnl` |
| `dnl_ViVA_SKILL` | `vivaxlug/appD.html` | `dnl` |
| `dplp` | `skuiref/chap2.html` | `dplp` |
| `drplRFValueAt` | `skartistref/DirectPlotSkillFunctions.html` | `drplRFValueAt` |
| `dump` | `skdevref/debug.html` | `dump` |
| `dutyCycle_OCEAN` | `oceanref/chap10.html` | `dutyCycle` |
| `dutycycle_ViVA_SKILL` | `vivaxlug/appD.html` | `dutycycle` |
| `edgeTriggeredEyeDiagram_OCEAN` | `oceanref/chap10.html` | `edgeTriggeredEyeDiagram` |
| `ediFinishStatus` | `edifinref/chap1.html` | `ediFinishStatus` |
| `edifDisplay` | `edifinref/chap2.html` | `edifDisplay` |
| `edifLayerNumMap` | `edifinref/chap1.html` | `edifLayerNumMap` |
| `edifinDisplay` | `edifinref/chap1.html` | `edifinDisplay` |
| `edifinMakeRenameString` | `edifinref/chap1.html` | `edifinMakeRenameString` |
| `elecGetCurrentData` | `vead/appC.html` | `elecGetCurrentData` |
| `elecGetDataSetNames` | `vead/appC.html` | `elecGetDataSetNames` |
| `elecGetDataSetParamsPropValue` | `vead/appC.html` | `elecGetDataSetParamsPropValue` |
| `elecTransferDataSets` | `vead/appC.html` | `elecTransferDataSets` |
| `eliCheckOutAndLock` | `skdfref/chap3.html` | `eliCheckOutAndLock` |
| `enterFunNestLevel` | `skuiref/chap12.html` | `enterFunNestLevel` |
| `evcdFile_OCEAN` | `oceanref/chap6.html` | `evcdFile` |
| `evcdInfoFile_OCEAN` | `oceanref/chap6.html` | `evcdInfoFile` |
| `evmQAM_OCEAN` | `oceanref/chap10.html` | `evmQAM` |
| `evmQAM_ViVA_SKILL` | `vivaxlug/appD.html` | `evmQAM` |
| `evmQpsk_OCEAN` | `oceanref/chap10.html` | `evmQpsk` |
| `evmQpsk_ViVA_SKILL` | `vivaxlug/appD.html` | `evmQpsk` |
| `exp_OCEAN` | `oceanref/chap10.html` | `exp` |
| `exp_ViVA_SKILL` | `vivaxlug/appD.html` | `exp` |
| `expr_ViVA_SKILL` | `vivaxlskill/chap4.html` | `expr` |
| `fallTime_OCEAN` | `oceanref/chap10.html` | `fallTime` |
| `fallTime_ViVA_SKILL` | `vivaxlug/appD.html` | `fallTime` |
| `famEval_ViVA_SKILL` | `vivaxlskill/chap4.html` | `famEval` |
| `fdoc` | `sklangref/core.html` | `fdoc` |
| `findClass` | `skoopref/classesinstances.html` | `findClass` |
| `firstVal_ViVA_SKILL` | `vivaxlskill/chap2.html` | `firstVal` |
| `flip_OCEAN` | `oceanref/chap10.html` | `flip` |
| `flip_ViVA_SKILL` | `vivaxlug/appD.html` | `flip` |
| `fndResetDb` | `skdevref/finder.html` | `fndResetDb` |
| `for_OCEAN` | `oceanref/chap13.html` | `for` |
| `forcenode_OCEAN` | `oceanref/chap6.html` | `forcenode` |
| `foreach_OCEAN` | `oceanref/chap13.html` | `foreach` |
| `fourEval_OCEAN` | `oceanref/chap10.html` | `fourEval` |
| `fourEval_ViVA_SKILL` | `vivaxlug/appD.html` | `fourEval` |
| `freq_OCEAN` | `oceanref/chap10.html` | `freq` |
| `freq_ViVA_SKILL` | `vivaxlug/appD.html` | `freq` |
| `freq_jitter_OCEAN` | `oceanref/chap10.html` | `freq_jitter` |
| `freq_jitter_ViVA_SKILL` | `vivaxlug/appD.html` | `freq_jitter` |
| `frequency_OCEAN` | `oceanref/chap10.html` | `frequency` |
| `frequency_ViVA_SKILL` | `vivaxlug/appD.html` | `frequency` |
| `fscanf_OCEAN` | `oceanref/chap14.html` | `fscanf` |
| `ga_OCEAN` | `oceanref/chap10.html` | `ga` |
| `ga_ViVA_SKILL` | `vivaxlug/appD.html` | `ga` |
| `gac_OCEAN` | `oceanref/chap10.html` | `gac` |
| `gac_freq_ViVA_SKILL` | `vivaxlug/appD.html` | `gac_freq` |
| `gac_gain_ViVA_SKILL` | `vivaxlug/appD.html` | `gac_gain` |
| `gainBwProd_OCEAN` | `oceanref/chap10.html` | `gainBwProd` |
| `gainBwProd_ViVA_SKILL` | `vivaxlug/appD.html` | `gainBwProd` |
| `gainMargin_OCEAN` | `oceanref/chap10.html` | `gainMargin` |
| `gainMargin_ViVA_SKILL` | `vivaxlug/appD.html` | `gainMargin` |
| `gcsummary` | `skdevref/debug.html` | `gcsummary` |
| `globalSigAlias_OCEAN` | `oceanref/chap6.html` | `globalSigAlias` |
| `globalSignal_OCEAN` | `oceanref/chap6.html` | `globalSignal` |
| `gmax_OCEAN` | `oceanref/chap10.html` | `gmax` |
| `gmax_ViVA_SKILL` | `vivaxlug/appD.html` | `gmax` |
| `gmin_OCEAN` | `oceanref/chap10.html` | `gmin` |
| `gmin_ViVA_SKILL` | `vivaxlug/appD.html` | `gmin` |
| `gmsg_OCEAN` | `oceanref/chap10.html` | `gmsg` |
| `gmsg_ViVA_SKILL` | `vivaxlug/appD.html` | `gmsg` |
| `gmux_OCEAN` | `oceanref/chap10.html` | `gmux` |
| `gmux_ViVA_SKILL` | `vivaxlug/appD.html` | `gmux` |
| `gp_OCEAN` | `oceanref/chap10.html` | `gp` |
| `gp_ViVA_SKILL` | `vivaxlug/appD.html` | `gp` |
| `gpc_OCEAN` | `oceanref/chap10.html` | `gpc` |
| `gpc_freq_ViVA_SKILL` | `vivaxlug/appD.html` | `gpc_freq` |
| `gpc_gain_ViVA_SKILL` | `vivaxlug/appD.html` | `gpc_gain` |
| `graphicsOff_OCEAN` | `oceanref/chap8.html` | `graphicsOff` |
| `graphicsOn_OCEAN` | `oceanref/chap8.html` | `graphicsOn` |
| `groupDelay_OCEAN` | `oceanref/chap10.html` | `groupDelay` |
| `groupDelay_ViVA_SKILL` | `vivaxlug/appD.html` | `groupDelay` |
| `gt_OCEAN` | `oceanref/chap10.html` | `gt` |
| `gt_ViVA_SKILL` | `vivaxlug/appD.html` | `gt` |
| `hardCopyOptions_OCEAN` | `oceanref/chap8.html` | `hardCopyOptions` |
| `hardCopy_OCEAN` | `oceanref/chap8.html` | `hardCopy` |
| `harmonicFreqList_OCEAN` | `oceanref/chap10.html` | `harmonicFreqList` |
| `harmonicFreq_ViVA_SKILL` | `vivaxlug/appD.html` | `harmonicFreq` |
| `harmonicList_OCEAN` | `oceanref/chap10.html` | `harmonicList` |
| `harmonic_OCEAN` | `oceanref/chap10.html` | `harmonic` |
| `harmonic_ViVA_SKILL` | `vivaxlug/appD.html` | `harmonic` |
| `hedRegUICustomFunc` | `cdshiereditor/appB.html` | `hedRegUICustomFunc` |
| `hlcheck_OCEAN` | `oceanref/chap6.html` | `hlcheck` |
| `hostMode_OCEAN` | `oceanref/chap12.html` | `hostMode` |
| `hostName_OCEAN` | `oceanref/chap12.html` | `hostName` |
| `i_OCEAN` | `oceanref/chap7.html` | `i` |
| `iagCreateMenuItem` | `abstract/abstract_skill.html` | `iagCreateMenuItem` |
| `iagGenAbstract` | `abstract/abstract_skill.html` | `iagGenAbstract` |
| `ic_OCEAN` | `oceanref/chap6.html` | `ic` |
| `iclicCheckOutAndLock` | `skdfref/chap3.html` | `iclicCheckOutAndLock` |
| `if_OCEAN` | `oceanref/chap13.html` | `if` |
| `ifreq_OCEAN` | `oceanref/chap10.html` | `ifreq` |
| `ifreq_ViVA_SKILL` | `vivaxlug/appD.html` | `ifreq` |
| `ih_OCEAN` | `oceanref/chap10.html` | `ih` |
| `ih_ViVA_SKILL` | `vivaxlug/appD.html` | `ih` |
| `iim_OCEAN` | `oceanref/chap9.html` | `iim` |
| `iinteg_OCEAN` | `oceanref/chap10.html` | `iinteg` |
| `iinteg_ViVA_SKILL` | `vivaxlug/appD.html` | `iinteg` |
| `ilAddTopLevelErrorHandler` | `skdevref/debug.html` | `ilAddTopLevelErrorHandler` |
| `ilArgMatchesSpecializer` | `skoopref/genericspecializer.html   "ilArgMatchesSpecializer"` | `HTML` |
| `ilDebugCountLevels` | `skdevref/debug.html` | `ilDebugCountLevels` |
| `ilEquivalentSpecializers` | `skoopref/genericspecializer.html   "ilEquivalentSpecializers"` | `HTML` |
| `ilGenerateSpecializer` | `skoopref/genericspecializer.html   "ilGenerateSpecializer"` | `HTML` |
| `ilGetGFbyClass` | `skdevref/debug.html` | `ilGetGFbyClass` |
| `ilGetIdeSessionWindow` | `skdevref/debug.html` | `ilGetIdeSessionWindow` |
| `ilGetTCovFiles` | `skdevref/debug.html` | `ilGetTCovFiles` |
| `ilMergeTCovData` | `skdevref/debug.html` | `ilMergeTCovData` |
| `ilRemoveMethod` | `skdevref/debug.html` | `ilRemoveMethod` |
| `ilRemoveTopLevelErrorHandler` | `skdevref/debug.html` | `ilRemoveTopLevelErrorHandler"  HTML` |
| `ilSlotBoundp` | `skdevref/debug.html` | `ilSlotBoundp` |
| `ilSpecMoreSpecificp` | `skoopref/genericspecializer.html   "ilSpecMoreSpecificp"` | `HTML` |
| `ilToolBox` | `skdevref/debug.html` | `ilToolBox` |
| `im_OCEAN` | `oceanref/chap9.html` | `im` |
| `imag_OCEAN` | `oceanref/chap10.html` | `imag` |
| `imag_ViVA_SKILL` | `vivaxlug/appD.html` | `imag` |
| `impHdlDisplay` | `importconnref/importTools.html` | `impHdlDisplay` |
| `inNext` | `skdevref/debug.html` | `inNext` |
| `inStepOut` | `skdevref/debug.html` | `inStepOut` |
| `includeFile_OCEAN` | `oceanref/chap6.html` | `includeFile` |
| `infile_OCEAN` | `oceanref/chap14.html` | `infile` |
| `initializeInstance` | `skoopref/classesinstances.html` | `initializeInstance` |
| `inl_OCEAN` | `oceanref/chap10.html` | `inl` |
| `inl_ViVA_SKILL` | `vivaxlug/appD.html` | `inl` |
| `installDebugger` | `skdevref/debug.html` | `installDebugger` |
| `int_OCEAN` | `oceanref/chap10.html` | `int` |
| `int_ViVA_SKILL` | `vivaxlug/appD.html` | `int` |
| `integ_OCEAN` | `oceanref/chap10.html` | `integ` |
| `integ_ViVA_SKILL` | `vivaxlug/appD.html` | `integ` |
| `intersect_OCEAN` | `oceanref/chap10.html` | `intersect` |
| `intersect_ViVA_SKILL` | `vivaxlug/appD.html` | `intersect` |
| `ip3Plot_OCEAN` | `oceanref/chap8.html` | `ip3Plot` |
| `ip_OCEAN` | `oceanref/chap9.html` | `ip` |
| `ipnVRICurves_OCEAN` | `oceanref/chap10.html` | `ipnVRICurves` |
| `ipnVRI_OCEAN` | `oceanref/chap10.html` | `ipnVRI` |
| `ipnVRI_ViVA_SKILL` | `vivaxlug/appD.html` | `ipnVRI` |
| `ipn_OCEAN` | `oceanref/chap10.html` | `ipn` |
| `ipn_ViVA_SKILL` | `vivaxlug/appD.html` | `ipn` |
| `iqCreateDummyCell` | `draciaref/chap1.html` | `iqCreateDummyCell` |
| `ir_OCEAN` | `oceanref/chap9.html` | `ir` |
| `isClass` | `skoopref/classesinstances.html` | `isClass` |
| `isContextLoaded` | `skdevref/context.html` | `isContextLoaded` |
| `isGeneric` | `skoopref/genericfunc.html` | `isGeneric` |
| `itime_OCEAN` | `oceanref/chap10.html` | `itime` |
| `itime_ViVA_SKILL` | `vivaxlug/appD.html` | `itime` |
| `kf_OCEAN` | `oceanref/chap10.html` | `kf` |
| `kf_ViVA_SKILL` | `vivaxlug/appD.html` | `kf` |
| `killJob_OCEAN` | `oceanref/chap12.html` | `killJob` |
| `lastVal_ViVA_SKILL` | `vivaxlskill/chap2.html` | `lastVal` |
| `ldtrDefReadOA` | `sktransrefOA/sklefdef.html` | `ldtrDefReadOA` |
| `ldtrDefWriteOA` | `sktransrefOA/sklefdef.html` | `ldtrDefWriteOA` |
| `ldtrLefReadOA` | `sktransrefOA/sklefdef.html` | `ldtrLefReadOA` |
| `ldtrLefWriteOA` | `sktransrefOA/sklefdef.html` | `ldtrLefWriteOA` |
| `linRg_OCEAN` | `oceanref/chap10.html` | `linRg` |
| `listAlias` | `skdevref/debug.html` | `listAlias` |
| `listFunctions` | `skdevref/debug.html` | `listFunctions` |
| `listVariables` | `skdevref/debug.html` | `listVariables` |
| `ln_OCEAN` | `oceanref/chap10.html` | `ln` |
| `ln_ViVA_SKILL` | `vivaxlug/appD.html` | `ln` |
| `loadContext` | `skdevref/context.html` | `loadContext` |
| `loadTopContextForms` | `skdevref/context.html` | `loadTopContextForms` |
| `load_OCEAN` | `oceanref/chap14.html` | `load` |
| `loadpull_ViVA_SKILL` | `vivaxlug/appD.html` | `loadpull` |
| `log10_OCEAN` | `oceanref/chap10.html` | `log10` |
| `log10_ViVA_SKILL` | `vivaxlug/appD.html` | `log10` |
| `logRg_OCEAN` | `oceanref/chap10.html` | `logRg` |
| `log_OCEAN` | `oceanref/chap10.html` | `log` |
| `lsb_OCEAN` | `oceanref/chap10.html` | `lsb` |
| `lsb_ViVA_SKILL` | `vivaxlug/appD.html` | `lsb` |
| `lshift_OCEAN` | `oceanref/chap10.html` | `lshift` |
| `lshift_ViVA_SKILL` | `vivaxlug/appD.html` | `lshift` |
| `mag_OCEAN` | `oceanref/chap10.html` | `mag` |
| `mag_ViVA_SKILL` | `vivaxlug/appD.html` | `mag` |
| `makeInstance` | `skoopref/classesinstances.html` | `makeInstance` |
| `max_OCEAN` | `oceanref/chap10.html` | `max` |
| `memoryAllocated` | `skdevref/debug.html` | `memoryAllocated` |
| `memq` | `sklangref/logicalrel.html` | `member` |
| `memv` | `sklangref/logicalrel.html` | `member` |
| `min_OCEAN` | `oceanref/chap10.html` | `min` |
| `mod_OCEAN` | `oceanref/chap10.html` | `mod` |
| `modelFile_OCEAN` | `oceanref/chap6.html` | `modelFile` |
| `monitor_OCEAN` | `oceanref/chap12.html` | `monitor` |
| `mspsMapNetName` | `parasimSKILL/parasimSKILLFunctions.html` | `mspsMapNetName` |
| `mu_ViVA_SKILL` | `vivaxlskill/chap4.html` | `mu` |
| `mu_prime_ViVA_SKILL` | `vivaxlskill/chap4.html` | `muprime` |
| `muffleWarnings` | `sklangref/core.html` | `muffleWarnings` |
| `nameToColor` | `skuiref/chap7.html` | `nameToColor` |
| `nc_OCEAN` | `oceanref/chap10.html` | `nc` |
| `nc_freq_ViVA_SKILL` | `vivaxlug/appD.html` | `nc_freq` |
| `nc_gain_ViVA_SKILL` | `vivaxlug/appD.html` | `nc_gain` |
| `nearlyEqual` | `sklangref/arithmetic.html` | `nearlyEqual` |
| `netlist` | `netlistsimulateref/ossFunctions.html` | `netlist` |
| `newWindow_OCEAN` | `oceanref/chap8.html` | `newWindow` |
| `newline_OCEAN` | `oceanref/chap14.html` | `newline` |
| `next` | `skdevref/debug.html` | `next` |
| `nextMethodp` | `skoopref/genericfunc.html` | `nextMethodp` |
| `nf_ViVA_SKILL` | `vivaxlug/appD.html` | `nf` |
| `nfmin_ViVA_SKILL` | `vivaxlug/appD.html` | `nfmin` |
| `nmpSpectreHDLToSysVerilog` | `caiskill/nmp.html` | `nmpSpectreHDLToSysVerilog` |
| `nodeset_OCEAN` | `oceanref/chap6.html` | `nodeset` |
| `noiseSummary_OCEAN` | `oceanref/chap8.html` | `noiseSummary` |
| `noise_OCEAN` | `oceanref/chap6.html` | `noise` |
| `normalQQ_OCEAN` | `oceanref/chap10.html` | `normalQQ` |
| `normalQQ_ViVA_SKILL` | `vivaxlug/appD.html` | `normalQQ` |
| `numConv_ViVA_SKILL` | `vivaxlug/appD.html` | `numConv` |
| `occpClose` | `skdfref/hierarchy.html` | `occpClose` |
| `occpCreateProp` | `skdfref/hierarchy.html` | `occpCreateProp"                         HTML` |
| `occpGetBestProp` | `skdfref/hierarchy.html` | `occpGetBestProp` |
| `occpGetBitInstProp` | `skdfref/hierarchy.html` | `occpGetBitInstProp` |
| `occpGetCellProp` | `skdfref/hierarchy.html` | `occpGetCellProp` |
| `occpGetDefaultProp` | `skdfref/hierarchy.html` | `occpGetDefaultProp` |
| `occpGetInstProp` | `skdfref/hierarchy.html` | `occpGetInstProp` |
| `occpGetPathProp` | `skdfref/hierarchy.html` | `occpGetPathProp` |
| `occpOpen` | `skdfref/hierarchy.html` | `occpOpen` |
| `occpRmBitInstProp` | `skdfref/hierarchy.html` | `occpRmBitInstProp` |
| `occpRmCellProp` | `skdfref/hierarchy.html` | `occpRmCellProp` |
| `occpRmDefaultProp` | `skdfref/hierarchy.html` | `occpRmDefaultProp` |
| `occpRmInstProp` | `skdfref/hierarchy.html` | `occpRmInstProp` |
| `occpRmPathProp` | `skdfref/hierarchy.html` | `occpRmPathProp` |
| `occpSave` | `skdfref/hierarchy.html` | `occpSave` |
| `occpSetBitInstProp` | `skdfref/hierarchy.html` | `occpSetBitInstProp` |
| `occpSetCellProp` | `skdfref/hierarchy.html` | `occpSetCellProp` |
| `occpSetDefaultProp` | `skdfref/hierarchy.html` | `occpSetDefaultProp` |
| `occpSetInstProp` | `skdfref/hierarchy.html` | `occpSetInstProp` |
| `occpSetPathProp` | `skdfref/hierarchy.html` | `occpSetPathProp` |
| `odcRegRowRegion` | `sklayoutref/odc.html` | `odcRegRowRegion` |
| `odcRegVirtualFigGroup` | `sklayoutref/odc.html` | `odcRegVirtualFigGroup` |
| `off_OCEAN` | `oceanref/chap6.html` | `off` |
| `openResults_OCEAN` | `oceanref/chap7.html` | `openResults` |
| `option_OCEAN` | `oceanref/chap6.html` | `option` |
| `outfile_OCEAN` | `oceanref/chap14.html` | `outfile` |
| `outputParams_OCEAN` | `oceanref/chap7.html` | `outputParams` |
| `outputs_OCEAN` | `oceanref/chap7.html` | `outputs` |
| `overshoot_OCEAN` | `oceanref/chap10.html` | `overshoot` |
| `overshoot_ViVA_SKILL` | `vivaxlug/appD.html` | `overshoot` |
| `path_OCEAN` | `oceanref/chap5.html` | `path` |
| `pavg_OCEAN` | `oceanref/chap10.html` | `pavg` |
| `pavg_ViVA_SKILL` | `vivaxlug/appD.html` | `pavg` |
| `peakToPeak_OCEAN` | `oceanref/chap10.html` | `peakToPeak` |
| `peakToPeak_ViVA_SKILL` | `vivaxlug/appD.html` | `peakToPeak` |
| `peak_OCEAN` | `oceanref/chap10.html` | `peak` |
| `peak_ViVA_SKILL` | `vivaxlug/appD.html` | `peak` |
| `perfDiagInstall` | `skuiref/chap2.html` | `perfDiagInstall` |
| `period_jitter_OCEAN` | `oceanref/chap10.html` | `period_jitter` |
| `period_jitter_ViVA_SKILL` | `vivaxlug/appD.html` | `period_jitter` |
| `pfile_OCEAN` | `oceanref/chap14.html` | `pfile` |
| `pgssDRC                     $skdfref/pegasusint.html` | `"pgssDRC"` | `HTML` |
| `plotStyle_OCEAN` | `oceanref/chap8.html` | `plotStyle` |
| `plot_OCEAN` | `oceanref/chap8.html` | `plot` |
| `pmNoise_OCEAN` | `oceanref/chap10.html` | `pmNoise` |
| `pmNoise_ViVA_SKILL` | `vivaxlug/appD.html` | `pmNoise` |
| `pn_OCEAN` | `oceanref/chap10.html` | `pn` |
| `pn_ViVA_SKILL` | `vivaxlug/appD.html` | `pn` |
| `pp` | `skdevref/debug.html` | `pp` |
| `prependPath_OCEAN` | `oceanref/chap5.html` | `prependPath` |
| `printFunctions` | `skdevref/debug.html` | `printFunctions` |
| `printGraph_OCEAN` | `oceanref/chap8.html` | `printGraph` |
| `printObject` | `skdevref/debug.html` | `printObject` |
| `printVariables` | `skdevref/debug.html` | `printVariables` |
| `printf_OCEAN` | `oceanref/chap14.html` | `printf` |
| `println_OCEAN` | `oceanref/chap14.html` | `println` |
| `printself` | `skoopref/classesinstances.html` | `printself` |
| `printstruct` | `skdevref/debug.html` | `printstruct` |
| `prms_OCEAN` | `oceanref/chap10.html` | `prms` |
| `prms_ViVA_SKILL` | `vivaxlug/appD.html` | `prms` |
| `profile` | `skdevref/profiler.html` | `profile` |
| `profileReset` | `skdevref/profiler.html` | `profileReset` |
| `profileSummary` | `skdevref/profiler.html` | `profileSummary` |
| `psd_OCEAN` | `oceanref/chap10.html` | `psd` |
| `psd_ViVA_SKILL` | `vivaxlug/appD.html` | `psd` |
| `psdbb_OCEAN` | `oceanref/chap10.html` | `psdbb` |
| `psdbb_ViVA_SKILL` | `vivaxlug/appD.html` | `psdbb` |
| `pstddev_OCEAN` | `oceanref/chap10.html` | `pstddev` |
| `pstddev_ViVA_SKILL` | `vivaxlug/appD.html` | `pstddev` |
| `pv_OCEAN` | `oceanref/chap7.html` | `pv` |
| `pvi_OCEAN` | `oceanref/chap10.html` | `pvi` |
| `pvi_ViVA_SKILL` | `vivaxlug/appD.html` | `pvi` |
| `pvifreq_ViVA_SKILL` | `vivaxlskill/chap2.html` | `pvifreq` |
| `pvr_OCEAN` | `oceanref/chap10.html` | `pvr` |
| `pvr_ViVA_SKILL` | `vivaxlug/appD.html` | `pvr` |
| `pvrfreq_ViVA_SKILL` | `vivaxlskill/chap2.html` | `pvrfreq` |
| `pvsApplyDRC` | `skdfref/pegasusint.html.html` | `pvsApplyDRC` |
| `pzFrequencyAndRealFilter_OCEAN` | `oceanref/chap8.html` | `pzFrequencyAndRealFilter` |
| `pzPlot_OCEAN` | `oceanref/chap8.html` | `pzPlot` |
| `pzSummary_OCEAN` | `oceanref/chap8.html` | `pzSummary` |
| `pzbode_OCEAN` | `oceanref/chap10.html` | `pzbode` |
| `pzbode_ViVA_SKILL` | `vivaxlug/appD.html` | `pzbode` |
| `pzfilter_OCEAN` | `oceanref/chap10.html` | `pzfilter` |
| `pzfilter_ViVA_SKILL` | `vivaxlug/appD.html` | `pzfilter` |
| `random_OCEAN` | `oceanref/chap10.html` | `random` |
| `rapidIIPN_OCEAN` | `oceanref/chap10.html` | `rapidIIPN` |
| `rapidIPNCurves_OCEAN` | `oceanref/chap10.html` | `rapidIPNCurves` |
| `rdeRemoveChamferFill` | `sklayoutref/vsr.fm` | `rdeRemoveChamferFill` |
| `real_OCEAN` | `oceanref/chap10.html` | `real` |
| `real_ViVA_SKILL` | `vivaxlug/appD.html` | `real` |
| `remoteDir_OCEAN` | `oceanref/chap12.html` | `remoteDir` |
| `removeDependent` | `skoopref/dmp.html` | `removeDependent` |
| `removeLabel_OCEAN` | `oceanref/chap8.html` | `removeLabel` |
| `removeListDuplicates` | `sklangref/list.html     "removeListDuplicates"` | `HTML` |
| `removeMethod` | `skdevref/debug.html` | `removeMethod` |
| `removeMethod` | `skoopref/genericfunc.html` | `removeMethod` |
| `report_OCEAN` | `oceanref/chap8.html` | `report` |
| `restore_OCEAN` | `oceanref/chap6.html` | `restore` |
| `resultParam_OCEAN` | `oceanref/chap7.html` | `resultParam` |
| `resultsDir_OCEAN` | `oceanref/chap6.html` | `resultsDir` |
| `results_OCEAN` | `oceanref/chap7.html` | `results` |
| `resume` | `skdevref/debug.html` | `resume` |
| `resumeJob_OCEAN` | `oceanref/chap12.html` | `resumeJob` |
| `riseTime_OCEAN` | `oceanref/chap10.html` | `riseTime` |
| `risetime_ViVA_SKILL` | `vivaxlug/appD.html` | `risetime` |
| `rmsNoise_OCEAN` | `oceanref/chap10.html` | `rmsNoise` |
| `rmsNoise_ViVA_SKILL` | `vivaxlug/appD.html` | `rmsNoise` |
| `rmsVoltage_OCEAN` | `oceanref/chap10.html` | `rmsVoltage` |
| `rmsVoltage_ViVA_SKILL` | `vivaxlug/appD.html` | `rmsVoltage` |
| `rms_OCEAN` | `oceanref/chap10.html` | `rms` |
| `rms_ViVA_SKILL` | `vivaxlug/appD.html` | `rms` |
| `rms_jitter_ViVA_SKILL` | `vivaxlug/appD.html` | `rms_jitter` |
| `rn_ViVA_SKILL` | `vivaxlug/appD.html` | `rn` |
| `root_OCEAN` | `oceanref/chap10.html` | `root` |
| `root_ViVA_SKILL` | `vivaxlug/appD.html` | `root` |
| `round_OCEAN` | `oceanref/chap10.html` | `round` |
| `rshift_OCEAN` | `oceanref/chap10.html` | `rshift` |
| `rshift_ViVA_SKILL` | `vivaxlug/appD.html` | `rshift` |
| `run_OCEAN` | `oceanref/chap6.html` | `run` |
| `runsim` | `netlistsimulateref/ossFunctions.html` | `runsim` |
| `s11_ViVA_SKILL` | `vivaxlug/appD.html` | `s11` |
| `s12_ViVA_SKILL` | `vivaxlug/appD.html` | `s12` |
| `s21_ViVA_SKILL` | `vivaxlug/appD.html` | `s21` |
| `s22_ViVA_SKILL` | `vivaxlug/appD.html` | `s22` |
| `sample_OCEAN` | `oceanref/chap10.html` | `sample` |
| `sample_ViVA_SKILL` | `vivaxlug/appD.html` | `sample` |
| `saveContext` | `skdevref/context.html` | `saveContext` |
| `saveGraphImage_OCEAN` | `oceanref/chap8.html` | `saveGraphImage` |
| `saveOpPoint_OCEAN` | `oceanref/chap6.html` | `saveOpPoint` |
| `saveOption_OCEAN` | `oceanref/chap6.html` | `saveOption` |
| `saveSubckt_OCEAN` | `oceanref/chap7.html` | `saveSubckt` |
| `save_OCEAN` | `oceanref/chap6.html` | `save` |
| `scanf` | `sklangref/inputoutput.html` | `fscanf` |
| `selectResult_OCEAN` | `oceanref/chap7.html` | `selectResult` |
| `setContext` | `skdevref/context.html` | `setContext` |
| `setSaveContextVersion` | `skdevref/context.html` | `setSaveContextVersion` |
| `setSlotValue` | `skoopref/classesinstances.html` | `setSlotValue` |
| `setf_getqq` | `sklangref/appC.html` | `setf_getqq` |
| `settlingTime_OCEAN` | `oceanref/chap10.html` | `settlingTime` |
| `settlingTime_ViVA_SKILL` | `vivaxlug/appD.html` | `settlingTime` |
| `setup_OCEAN` | `oceanref/chap5.html` | `setup` |
| `sevGetSessionType` | `skartistref/chap20.html` | `sevGetSessionType` |
| `sevRemovePlotWindow` | `skartistref/chap20.html` | `sevRemovePlotWindow` |
| `sh` | `sklangref/environment.html` | `sh` |
| `sharedInitialize` | `skoopref/classesinstances.html` | `sharedInitialize` |
| `shell` | `sklangref/environment.html` | `sh` |
| `sin_OCEAN` | `oceanref/chap10.html` | `sin` |
| `sin_ViVA_SKILL` | `vivaxlug/appD.html` | `sin` |
| `sinh_ViVA_SKILL` | `vivaxlug/appD.html` | `sinh` |
| `sipImportLgaBgaTextSkill` | `skcompref/vsdp.html` | `sipImportLgaBgaTextSkill` |
| `slewRate_OCEAN` | `oceanref/chap10.html` | `slewRate` |
| `slewrate_ViVA_SKILL` | `vivaxlug/appD.html` | `slewrate` |
| `slotBoundp` | `skoopref/classesinstances.html` | `slotBoundp` |
| `slotUnbound` | `skoopref/classesinstances.html` | `slotUnbound` |
| `slotValue` | `skoopref/classesinstances.html` | `slotValue` |
| `sltSetContextSpecificationCells` | `sklayoutref/wire.html    "sltSetContextSpecificationCells"` | `HTML` |
| `smithType_OCEAN` | `oceanref/chap10.html` | `smithType` |
| `solver_OCEAN` | `oceanref/chap6.html` | `solver` |
| `sp_OCEAN` | `oceanref/chap7.html` | `sp` |
| `spcinGuiDisplay` | `sktransrefOA/skxoasis.html` | `spcinGuiDisplay` |
| `spectralPower_OCEAN` | `oceanref/chap10.html` | `spectralPower` |
| `spectralPower_ViVA_SKILL` | `vivaxlug/appD.html` | `spectralPower` |
| `spectrumMeas_OCEAN` | `oceanref/chap10.html` | `spectrumMeas` |
| `spectrumMeas_ViVA_SKILL` | `vivaxlug/appD.html` | `spectrumMeas` |
| `spectrumMeasurement` | `oceanref/chap10.html` | `spectrumMeasurement` |
| `spm_OCEAN` | `oceanref/chap10.html` | `spm` |
| `spm_ViVA_SKILL` | `vivaxlug/appD.html` | `spm` |
| `sqrt_OCEAN` | `oceanref/chap10.html` | `sqrt` |
| `srandom_OCEAN` | `oceanref/chap10.html` | `srandom` |
| `ssb_OCEAN` | `oceanref/chap10.html` | `ssb` |
| `ssb_ViVA_SKILL` | `vivaxlug/appD.html` | `ssb` |
| `sscanf` | `sklangref/inputoutput.html` | `fscanf` |
| `stacktrace` | `skdevref/debug.html` | `stacktrace` |
| `startFinder` | `skdevref/finder.html` | `startFinder` |
| `stddev_OCEAN` | `oceanref/chap10.html` | `stddev` |
| `stddev_ViVA_SKILL` | `vivaxlug/appD.html` | `stddev` |
| `step` | `skdevref/debug.html` | `step` |
| `stepend` | `skdevref/debug.html` | `stepend` |
| `stepout` | `skdevref/debug.html` | `stepout` |
| `stimulusFile_OCEAN` | `oceanref/chap6.html` | `stimulusFile` |
| `store_OCEAN` | `oceanref/chap6.html` | `store` |
| `sub1_OCEAN` | `oceanref/chap10.html` | `sub1` |
| `subclassesOf` | `skoopref/subsuperclass.html` | `subclassesOf` |
| `subclassp` | `skoopref/subsuperclass.html` | `subclassp` |
| `superclassesOf` | `skoopref/subsuperclass.html` | `superclassesOf` |
| `suspendJob_OCEAN` | `oceanref/chap12.html` | `suspendJob` |
| `swapSweep_ViVA_SKILL` | `vivaxlskill/chap4.html` | `swapSweep` |
| `sweepNames_OCEAN` | `oceanref/chap7.html` | `sweepNames` |
| `sweepValues_OCEAN` | `oceanref/chap7.html` | `sweepValues` |
| `sweepVarValues_OCEAN` | `oceanref/chap7.html` | `sweepVarValues` |
| `sweepVarVlaues_OCEAN` | `oceanref/chap7.html` | `sweepVarVlaues` |
| `tan_OCEAN` | `oceanref/chap10.html` | `tan` |
| `tan_ViVA_SKILL` | `vivaxlug/appD.html` | `tan` |
| `tangent_OCEAN` | `oceanref/chap10.html` | `tangent` |
| `tangent_ViVA_SKILL` | `vivaxlug/appD.html` | `tangent` |
| `tanh_ViVA_SKILL` | `vivaxlug/appD.html` | `tanh` |
| `tfEditTechfile` | `techfileuser/chap5.html` | `tfEditTechfile` |
| `thd_OCEAN` | `oceanref/chap10.html` | `thd` |
| `thd_ViVA_SKILL` | `vivaxlug/appD.html` | `thd` |
| `thd_fd_OCEAN` | `oceanref/chap10.html` | `thd_fd` |
| `topBaseLine_ViVA_SKILL` | `vivaxlskill/chap4.html` | `topBaseLine` |
| `topLine_ViVA_SKILL` | `vivaxlskill/chap4.html` | `topLine` |
| `toplevel` | `skdevref/debug.html` | `toplevel` |
| `totalNoise_OCEAN` | `oceanref/chap10.html` | `totalNoise` |
| `totalNoise_ViVA_SKILL` | `vivaxlug/appD.html` | `totalNoise` |
| `tracef` | `skdevref/debug.html` | `tracef` |
| `tracelevlimit` | `skdevref/debug.html` | `tracelevlimit` |
| `tracelevunlimit` | `skdevref/debug.html` | `tracelevunlimit` |
| `tracep` | `skdevref/debug.html` | `tracep` |
| `tracev` | `skdevref/debug.html` | `tracev` |
| `tran_OCEAN` | `oceanref/chap6.html` | `tran` |
| `transCdlOutDisplay` | `sktransrefOA/skcdlout.html` | `transCdlOutDisplay` |
| `type` | `sklangref/datastruct.html` | `type` |
| `typep` | `sklangref/datastruct.html` | `type` |
| `unbindVar` | `sklangref/core.html` | `unbindVar` |
| `unbreakpt` | `skdevref/debug.html` | `unbreakpt` |
| `unbreakptMethod` | `skdevref/debug.html` | `unbreakptMethod` |
| `uncount` | `skdevref/debug.html` | `uncount` |
| `uninstallDebugger` | `skdevref/debug.html` | `uninstallDebugger` |
| `unityGainFreq_OCEAN` | `oceanref/chap10.html` | `unityGainFreq` |
| `unityGainFreq_ViVA_SKILL` | `vivaxlug/appD.html` | `unityGainFreq` |
| `unless_OCEAN` | `oceanref/chap13.html` | `unless` |
| `unprofile` | `skdevref/profiler.html` | `unprofile` |
| `untrace` | `skdevref/debug.html` | `untrace` |
| `untracep` | `skdevref/debug.html` | `untracep` |
| `untracev` | `skdevref/debug.html` | `untracev` |
| `unwatch` | `skdevref/debug.html` | `unwatch` |
| `updateDependent` | `skoopref/dmp.html` | `updateDependent` |
| `updateInstanceForDifferentClass` | `skoopref/genericfunc.html` | `updateInstanceForDifferentClass` |
| `updateInstanceForRedefinedClass` | `skoopref/genericfunc.html` | `updateInstanceForRedefinedClass` |
| `v_OCEAN` | `oceanref/chap7.html` | `v` |
| `valueAt_ViVA_SKILL` | `vivaxlskill/chap2.html` | `valueAt` |
| `value_OCEAN` | `oceanref/chap10.html` | `value` |
| `value_ViVA_SKILL` | `vivaxlug/appD.html` | `value` |
| `vcdFile_OCEAN` | `oceanref/chap6.html` | `vcdFile` |
| `vcdInfoFile_OCEAN` | `oceanref/chap6.html` | `vcdInfoFile` |
| `vcpPlaceBoundaryCells` | `sklayoutref/vcp.html` | `vcpPlaceBoundaryCells` |
| `vcpfePlaceBoundaryCells` | `sklayoutref/vcp.html` | `vcpfePlaceBoundaryCells` |
| `vcpfePlaceFillers` | `sklayoutref/vcp.html` | `vcpfePlaceFillers` |
| `vcpfePlaceTapCells` | `sklayoutref/vcp.html` | `vcpfePlaceTapCells"          HTML` |
| `vdb_OCEAN` | `oceanref/chap9.html` | `vdb` |
| `vecFile_OCEAN` | `oceanref/chap6.html` | `vecFile` |
| `vfpPtLoadPinResizeFile` | `sklayoutref/vfp.html         "vfpPtLoadPinResizeFile"` | `HTML` |
| `vfreq_OCEAN` | `oceanref/chap10.html` | `vfreq` |
| `vfreq_ViVA_SKILL` | `vivaxlug/appD.html` | `vfreq` |
| `vh_OCEAN` | `oceanref/chap10.html` | `vh` |
| `vh_ViVA_SKILL` | `vivaxlug/appD.html` | `vh` |
| `vi, vii, vil` | `sklangref/environment.html` | `vi` |
| `vicOpenVlogCallBack` | `netlistsimulateref/netlisterFunctions.html` | `vicOpenVlogCallBack` |
| `vil` | `sklangref/environment.html` | `vi` |
| `vim_OCEAN` | `oceanref/chap9.html` | `vim` |
| `vivaInitBindkeys_ViVA_SKILL` | `vivaxlskill/chap5.html` | `vivaInitBindkeys` |
| `vlVicCrossSelectionForm` | `netlistsimulateref/netlisterFunctions.html` | `vlVicCrossSelectionForm` |
| `vlVicPSForm` | `netlistsimulateref/netlisterFunctions.html` | `vlVicPSForm` |
| `vm_OCEAN` | `oceanref/chap9.html` | `vm` |
| `vmsUpdateCellViews` | `amsskillref/amsdesigner.html` | `vmsUpdateCellViews` |
| `vmtLibImport` | `vmtUser/VMT_SKILL.html` | `vmtLibImport` |
| `vmtcsvInstallCsvFile` | `vmtUser/VMT_SKILL.html           "vmtcsvInstallCsvFile"` | `HTML` |
| `vosHiDisplayNetlist` | `netlistsimulateref/vhdlToolboxFunctions.html` | `vosHiDisplayNetlist` |
| `vosLaunchIrunSimulation` | `netlistsimulateref/vhdlToolboxFunctions.html` | `vosLaunchIrunSimulation` |
| `vp_OCEAN` | `oceanref/chap9.html` | `vp` |
| `vr_OCEAN` | `oceanref/chap9.html` | `vr` |
| `vsdpiRunDieExport` | `skcompref/vsdp.html` | `vsdpiRunDieExport` |
| `vsdpiSaveXML` | `skcompref/vsdp.html` | `vsdpiSaveXML` |
| `vsdpiWriteCDF` | `skcompref/vsdp.html` | `vsdpiWriteCDF` |
| `vsrDeletePreset` | `sklayoutref/vsr.html` | `vsrDeletePreset` |
| `vsrLoadPreset` | `sklayoutref/vsr.html` | `vsrLoadPreset` |
| `vsrSavePreset` | `sklayoutref/vsr.html` | `vsrSavePreset` |
| `vswr_OCEAN` | `oceanref/chap7.html` | `vswr` |
| `vtime_OCEAN` | `oceanref/chap10.html` | `vtime` |
| `vtime_ViVA_SKILL` | `vivaxlug/appD.html` | `vtime` |
| `vvDisplayBrowser_ViVA_SKILL` | `vivaxlskill/chap5.html` | `vvDisplayBrowser` |
| `vvDisplayCalculator_ViVA_SKILL` | `vivaxlskill/chap4.html` | `vvDisplayCalculator` |
| `wait_OCEAN` | `oceanref/chap12.html` | `wait` |
| `watch` | `skdevref/debug.html` | `watch` |
| `waveVsWave_ViVA_SKILL` | `vivaxlskill/chap3.html` | `waveVsWave` |
| `when_OCEAN` | `oceanref/chap13.html` | `when` |
| `where` | `skdevref/debug.html` | `where` |
| `whereIs` | `skdevref/debug.html` | `whereIs` |
| `while_OCEAN` | `oceanref/chap13.html` | `while` |
| `x**2_ViVA_SKILL` | `vivaxlug/appD.html` | `x**2` |
| `xLimit_OCEAN` | `oceanref/chap8.html` | `xLimit` |
| `xdvReplaceInstWithVias` | `skdfref/chap2.html` | `xdvReplaceInstWithVias` |
| `xmax_OCEAN` | `oceanref/chap10.html` | `xmax` |
| `xmax_ViVA_SKILL` | `vivaxlug/appD.html` | `xmax` |
| `xmin_OCEAN` | `oceanref/chap10.html` | `xmin` |
| `xmin_ViVA_SKILL` | `vivaxlug/appD.html` | `xmin` |
| `xor_OCEAN` | `oceanref/chap10.html` | `xor` |
| `xpcDumpCache` | `skpcellref/xpcellFunctions.html` | `xpcDumpCache` |
| `xpcEnableExpressPcell` | `skpcellref/xpcellFunctions.html` | `xpcEnableExpressPcell` |
| `xstGetField` | `sktransrefOA/skxstream.html` | `xstGetField` |
| `xstInDoTranslate` | `sktransrefOA/skxstream.html` | `xstInDoTranslate` |
| `xstInGetField` | `sktransrefOA/skxstream.html` | `xstInGetField` |
| `xstInGetVMLibs` | `sktransrefOA/skxstream.html` | `xstInGetVMLibs` |
| `xstInOnCancel` | `sktransrefOA/skxstream.html` | `xstInOnCancel` |
| `xstInOnCancelCB` | `sktransrefOA/skxstream.html` | `xstInOnCancelCB` |
| `xstInOnCompletion` | `sktransrefOA/skxstream.html` | `xstInOnCompletion` |
| `xstInOnCompletionCB` | `sktransrefOA/skxstream.html` | `xstInOnCompletionCB` |
| `xstInOnTranslate` | `sktransrefOA/skxstream.html` | `xstInOnTranslate` |
| `xstInOnTranslateCB` | `sktransrefOA/skxstream.html` | `xstInOnTranslateCB` |
| `xstInSaveVMLib` | `sktransrefOA/skxstream.html` | `xstInSaveVMLib` |
| `xstInSetField` | `sktransrefOA/skxstream.html` | `xstInSetField` |
| `xstOutDoTranslate` | `sktransrefOA/skxstream.html` | `xstOutDoTranslate` |
| `xstOutOnCancel` | `sktransrefOA/skxstream.html` | `xstOutOnCancel` |
| `xstOutOnCancelCB` | `sktransrefOA/skxstream.html` | `xstOutOnCancelCB` |
| `xstOutOnCompletion` | `sktransrefOA/skxstream.html` | `xstOutOnCompletion` |
| `xstOutOnCompletionCB` | `sktransrefOA/skxstream.html` | `xstOutOnCompletionCB` |
| `xstOutOnTranslate` | `sktransrefOA/skxstream.html` | `xstOutOnTranslate` |
| `xstOutOnTranslateCB` | `sktransrefOA/skxstream.html` | `xstOutOnTranslateCB` |
| `xstSetField` | `sktransrefOA/skxstream.html` | `xstSetField` |
| `xval_OCEAN` | `oceanref/chap10.html` | `xval` |
| `xval_ViVA_SKILL` | `vivaxlug/appD.html` | `xval` |
| `y**2_ViVA_SKILL` | `vivaxlug/appD.html` | `y**2` |
| `yLimit_OCEAN` | `oceanref/chap8.html` | `yLimit` |
| `ymax_OCEAN` | `oceanref/chap10.html` | `ymax` |
| `ymax_ViVA_SKILL` | `vivaxlug/appD.html` | `ymax` |
| `ymin_OCEAN` | `oceanref/chap10.html` | `ymin` |
| `ymin_ViVA_SKILL` | `vivaxlug/appD.html` | `ymin` |
| `ypm_OCEAN` | `oceanref/chap10.html` | `ypm` |
| `ypm_ViVA_SKILL` | `vivaxlug/appD.html` | `ypm` |
| `zm_OCEAN` | `oceanref/chap7.html` | `zm` |
| `zpm_OCEAN` | `oceanref/chap10.html` | `zpm` |
| `zpm_ViVA_SKILL` | `vivaxlug/appD.html` | `zpm` |
| `zref_OCEAN` | `oceanref/chap7.html` | `zref` |


---

## 使用说明

### 1. 查找函数文档

1. 在本文档中搜索函数名
2. 找到对应的 `文档文件` 和 `HTML锚点`
3. 在 Virtuoso 文档目录下查找:
   ```bash
   cd /mnt/data/eda_tool/cadence/ICAD_201/doc/
   grep -l "函数名" */*.html
   ```

### 2. 在 Virtuoso CIW 中调用

```skill
; 示例1: 数据库操作
cv = geGetEditCellView()
dbIsInstTransparent(cv)

; 示例2: ADE XL 操作
axlToolSetOpPointInfo()

; 示例3: 电压域检查
vdrRunSanityChecker()
```

### 3. 获取函数帮助

```skill
; 在 CIW 中获取函数签名
help(函数名)

; 示例
help(dbCreateRect)
help(axlIsSessionReadOnly)
```

---

## 注意事项

⚠️ **重要提醒**

1. 部分函数需要特定的 License 才能使用
2. 部分函数仅在特定模式下可用（如版图编辑模式）
3. 建议在使用前先在 CIW 中测试 `help(函数名)`
4. 所有函数均为 SKILL 语言函数，区分大小写

---

*文档生成完成*
