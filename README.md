# SR7420 kmod 软件源

本仓库保留 SR7420 **r1** 开发构建的 **1109 个 kmod APK、1 个 kernel APK 和签名索引**。已核对包签名、索引签名、AArch64 架构、vermagic 和全局模块依赖；尚未逐个做硬件或安装组合测试。

内核 ABI：`6.18.60~b608e4c72ecf314fc3955d48ca497c9f-r1`。架构：`aarch64_cortex-a53`。

只能用于来自同次内核配置、同一 ABI 的 SR7420 镜像，不能忽略 APK 的 kernel 依赖强制安装。USB44 实验镜像已经内置本仓库公钥和精确 ABI 软件源地址。

- 软件包、`packages.adb` 与重签后 SHA256 清单：`aarch64_cortex-a53/6.18.60~b608e4c72ecf314fc3955d48ca497c9f-r1/`。
- 公钥：`keys/public-key.pem`，私钥不在仓库中。
- 功能与 403 个未选中项说明：[KMODS.md](KMODS.md)。
- 构建和检查证据：`reports/`；对应固件源码提交见 `status.json`。

`reports/all-kmods44-report.json` 中原始构建 APK 的哈希与重签后的 APK 不同，发布文件以同目录 `manifest.json` 为准。固件源码仓库同时提供全量选择、模块审计与软件源签名工具。

## r1 索引地址修正

2026-11-18 修正文档中的 ABI 路径拼写。现有 1110 个 APK 与签名 `packages.adb` 原样保留；没有删除、替换或重签。可直接使用 `repositories/sr7420-r1.list` 中的完整索引地址。此版本 apk 使用的索引名是 `packages.adb`，无需创建 `package.db`。

r2 固件使用独立的 `sr7420-kmods-r2` 仓库。r1/r2 必须匹配各自的完整 kernel ABI；这里的代际名称与 APK 包版本末尾的 `-r1` 不是同一概念。
