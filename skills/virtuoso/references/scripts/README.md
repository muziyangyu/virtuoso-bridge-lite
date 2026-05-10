# 参考脚本归档

从 opamp_two_stage 前仿真到后仿真流程中使用的参考脚本。

## 核心脚本

| 脚本 | 用途 |
|------|------|
| `run_opamp_ac_dc.py` | 完整前仿真流程：读取原理图 → 提取参数 → 构建测试平台 → 运行 Spectre → 解析结果 → 生成 Bode 图 |
| `run_post_sim.py` | 后仿真流程：上传 DSPF → 构建测试平台 → 运行 Spectre → 下载结果 → 解析 AC/DC → 生成 Bode 图 + 对比汇总 |
| `parse_post_sim.py` | 解析后仿真结果 + 生成对比 Bode 图（REF vs RCE） |
| `test_rce_debug.py` | RCE DSPF 诊断脚本：运行单个 DSPF 并输出完整 Spectre 日志用于调试 |

## 使用方法

```bash
# 前仿真：读取原理图并运行 AC/DC
cd virtuoso-bridge-lite/output
python run_opamp_ac_dc.py

# 后仿真：同时运行 REF 和 RCE DSPF
python run_post_sim.py

# 解析结果（单独运行）
python parse_post_sim.py
```

## 关键注意事项

1. 所有脚本假设 `.venv` 虚拟环境已激活
2. 后仿真需要 SSH 连接到远程服务器，通过 `host` 和 `user` 变量配置
3. DSPF 端口顺序必须从 `.SUBCKT` 行读取并匹配实例化顺序
4. PDK 模型路径硬编码，需要修改为实际环境路径
