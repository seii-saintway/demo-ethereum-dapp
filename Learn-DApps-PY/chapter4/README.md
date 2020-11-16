# 理解状态与交易

以太坊是一个巨大的分布式状态机，交易则是驱动这个状态机的力量。

在运行预置代码之前，请首先在1#终端启动节点仿真器：

```
~$ ganache-cli
```

## 查看账户余额

在终端运行Python脚本：

```
~/repo/chapter4$ python3 balance.py
```

## 进行单位换算

在终端运行Python脚本：

```
~/repo/chapter4$ python3 units.py
```

## 执行普通交易

在终端运行Python脚本：

```
~/repo/chapter4$ python3 transaction-only.py
```

## 执行普通交易并等待回执

在终端运行Python脚本：

```
~/repo/chapter4$ python3 transaction-receipt.py
```

## 估算交易gas用量

在终端运行Python脚本：

```
~/repo/chapter4$ python3 estimate-gas.py
```

## 执行裸交易

在终端运行Python脚本：

```
~/repo/chapter4$ python3 raw-transaction.py
```