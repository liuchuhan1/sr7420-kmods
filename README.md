# SR7420 kmod 软件源

本仓库提供当前 SR7420 开发构建的 **1109 个 kmod APK、1 个 kernel APK 和签名索引**。已核对包签名、索引签名、AArch64 架构、vermagic 和全局模块依赖；尚未逐个做硬件或安装组合测试。

内核 ABI：`6.18.60~b608e4c72ecf314fc4035d48ca497c9f-r1`。架构：`aarch64_cortex-a53`。

只能用于来自同次内核配置、同一 ABI 的 SR7420 镜像，不能忽略 APK 的 kernel 依赖强制安装。USB44 实验镜像已经内置本仓库公钥和精确 ABI 软件源地址。

- 软件包、`packages.adb` 与重签后 SHA256 清单：`aarch64_cortex-a53/6.18.60~b608e4c72ecf314fc4035d48ca497c9f-r1/`。
- 公钥：`keys/public-key.pem`，私钥不在仓库中。
- 功能与 403 个未选中项说明：[KMODS.md](KMODS.md)。
- 构建和检查证据：`reports/`；对应固件源码提交见 `status.json`。

`reports/all-kmods44-report.json` 中原始构建 APK 的哈希与重签后的 APK 不同，发布文件以同目录 `manifest.json` 为准。固件源码仓库同时提供全量选择、模块审计与软件源签名工具。
