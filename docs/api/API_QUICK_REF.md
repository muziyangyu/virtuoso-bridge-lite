# SKILL API 快速参考卡

> 常用 API 速查

---

## 常用前缀说明

| 前缀 | 功能领域 | 示例 |
|------|----------|------|
| `axl` | ADE XL 相关 | `axlSDBDebugPrint`, `axlToolSetOpPointInfo` |
| `ci` | Circuit / Constraint | `ciCommonGateIterator`, `ciAPRCascodeIterator` |
| `vdr` | Voltage Domain / 电压域 | `vdrSetNetVoltageRange`, `vdrRunSanityChecker` |
| `db` | Database / 数据库 | `dbIsInstTransparent`, `dbSetInstTransparent` |
| `ge` | Graphics Editor / 图形编辑 | `geToggleDisplayResolution` |
| `tech` | Technology / 技术文件 | `techGetFabricType`, `techSetFabricType` |
| `hi` | Host Interface / GUI | `hiInsertBlankCIWOutputPage` |
| `cst` | Constraints / 约束 | `cstGetFoundryCGName`, `cstGetFoundryConstraintGroup` |
| `ocn` | Ocean / 仿真 | `ocnPrintTMIReliabilityResults` |
| `mg` | Module Generator | `mgFreezeFGR`, `mgUnfreezeFGR` |
| `au` | Analog Utility | `auCdlPrintAdditionalCommentsOnFileHeader` |

---

## 使用方法

在 Virtuoso CIW 中调用 SKILL 函数:

```skill
; 示例: 调用 ADE XL 相关函数
axlSDBDebugPrint(t)

; 示例: 检查会话只读状态
axlIsSessionReadOnly()

; 示例: 电压域检查
vdrRunSanityChecker()
```

---

## 文档查找

1. 首先在本文件中找到函数名
2. 查看对应的文档文件路径
3. 在 `/mnt/data/eda_tool/cadence/ICAD_201/doc/` 目录下找到对应 HTML 文件
4. 使用浏览器或 `grep` 查找锚点位置获取详细文档

