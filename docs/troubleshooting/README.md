# 故障排除文档

## 概述

本目录包含 virtuoso-bridge-lite 项目常见问题的诊断与解决方案。

## 文档列表

| 文档 | 描述
|---|---
| ⭐ [SPECTRE_OPAMP_DEBUG_NOTES.md](./SPECTRE_OPAMP_DEBUG_NOTES.md) | 运放 AC 调试日志 - -600dB 增益问题完整修复过程
| [SPECTRE_TROUBLESHOOTING.md](./SPECTRE_TROUBLESHOOTING.md) | Spectre 常见问题 - 网表语法、AC反馈、DC偏置、PSF解析

---

## SPECTRE_OPAMP_DEBUG_NOTES.md - 运放 AC 调试

### 经典问题：-600dB 增益

**症状：**
```
AC 分析结果显示增益为 -600dB，完全不合理
```

**根本原因：**
1. 错误的 `mag=` 参数语法
2. 高阻抗节点缺少泄放电阻
3. 反馈配置错误

**正确 vs 错误：**
```spectre
* ❌ 错误
ac start=1k stop=10G mag=1

* ✅ 正确
ac start=1k stop=10G amplitude=1
```

**高阻抗节点泄放：**
```spectre
* 在高阻节点添加 GOhm 级泄放电阻
Rbleed (Vout 0) 1G
```

### 相位裕度计算

```python
# 正确计算相位裕度
gain_db = 20 * log10(abs(Vout/Vin))
phase_deg = angle(Vout/Vin) * 180/pi
pm = 180 + phase_deg[gain_crossing_idx]
```

---

## SPECTRE_TROUBLESHOOTING.md - 常见问题

### 网表语法错误
- 缺少分号或引号
- 单位不匹配（V vs mV）
- 节点名称大小写敏感

### AC 反馈配置
- 反馈环路断开检查
- 激励源位置错误
- 初始条件设置

### DC 偏置修复
- 直流工作点不收敛
- 添加 `.options gmin=1e-12`
- 逐步提高电源电压

### PSF 解析问题
- 波形数据缺失
- 结果文件损坏
- 使用 `psfascii` 格式替代

---

## 快速排查清单

1. **检查网表语法** → `spectre -c input.scs`
2. **检查 DC 工作点** → `.op` 分析
3. **检查单位** → SI 单位一致性
4. **查看仿真日志** → 搜索 `error` / `warning`
5. **启用详细输出** → `+loglevel=ALL`

## 更多帮助

| 资源 | 位置
|---|---
| Virtuoso Skill 故障排除 | [../sub_skills/virtuoso/troubleshooting.md](../sub_skills/virtuoso/troubleshooting.md)
| Sub Skills 主索引 | [../sub_skills/](../sub_skills/)

*最后更新：2026-04-30*
