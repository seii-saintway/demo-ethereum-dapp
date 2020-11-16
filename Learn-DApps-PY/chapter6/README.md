# 过滤器与事件

使用过滤器来检测以太坊区块链上感兴趣的事件。

在运行预置代码之前，请首先在1#终端启动节点仿真器：

```
~$ ganache-cli
```

## 监听新块的生成

在2#终端启动触发脚本：

```
~/repo/chapter6$ python3 block-filter-trigger.py
```

在3#终端启动监听脚本：

```
~/repo/chapter6$ python3 block-monitor.py
```

## 监听新交易的生成

在2#终端启动触发脚本：

```
~/repo/chapter6$ python3 block-filter-trigger.py
```

在3#终端启动监听脚本：

```
~/repo/chapter6$ python3 transaction-monitor.py
```

## 监听待定交易的生成

在2#终端启动触发脚本：

```
~/repo/chapter6$ python3 block-filter-trigger.py
```

在3#终端启动监听脚本：

```
~/repo/chapter6$ python3 pending-tx-monitor.py
```

## 监听合约事件产生的日志

首先编译、部署代币合约：

```
~/repo/chapter6$ python3 build-contract.py
~/repo/chapter6$ python3 deploy-contract.py
```

在2#终端启动触发脚本：

```
~/repo/chapter6$ python3 contract-trigger.py
```

在3#终端启动监听脚本：

```
~/repo/chapter6$ python3 contract-log-monitor.py
```
## 使用主题过滤日志

首先编译、部署代币合约：

```
~/repo/chapter6$ python3 build-contract.py
~/repo/chapter6$ python3 deploy-contract.py
```

在2#终端启动触发脚本：

```
~/repo/chapter6$ python3 contract-trigger.py
```

在3#终端启动监听脚本：

```
~/repo/chapter6$ python3 contract-log-monitor-topic.py
```

## 监听合约日志并解码日志参数

首先编译、部署代币合约：

```
~/repo/chapter6$ python3 build-contract.py
~/repo/chapter6$ python3 deploy-contract.py
```

在2#终端启动触发脚本：

```
~/repo/chapter6$ python3 contract-trigger.py
```

在3#终端启动监听脚本：

```
~/repo/chapter6$ python3 contract-log-monitor-decode.py
```

## 监听合约事件

首先编译、部署代币合约：

```
~/repo/chapter6$ python3 build-contract.py
~/repo/chapter6$ python3 deploy-contract.py
```

在2#终端启动触发脚本：

```
~/repo/chapter6$ python3 contract-trigger.py
```

在3#终端启动监听脚本：

```
~/repo/chapter6$ python3 contract-event-monitor.py
```
