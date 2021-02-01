#!/usr/bin/python3

import pytest

def test_init(UniswapRouter, WETH, DAI, USDC, USDT, TUSD, USDN, sUSD, sETH, BUSD, CRV3, renBTC, WBTC, cDAI, cUSDC, yDAI, yUSDC, yUSDT, yTUSD, yDAI_BUSD, yUSDC_BUSD, yUSDT_BUSD, yBUSD, _compoundvolgauge, compoundpool, _threepoolvolgauge, threepool, _yvolgauge, ypool, _usdnvolgauge, usdnpool, _renvolgauge, renpool, _susdvolgauge, susdpool, _sethvolgauge, sethpool, _busdvolgauge, busdpool, accounts):
    UniswapRouter.swapETHForExactTokens(4000 * 10 ** 18, [WETH, DAI], accounts[0], 2 ** 256 - 1, {'from' : accounts[0], 'value': 15 * 10 ** 18})
    UniswapRouter.swapETHForExactTokens(4000 * 10 ** 6 , [WETH, USDC], accounts[0], 2 ** 256 - 1, {'from' : accounts[0], 'value': 15 * 10 ** 18})
    UniswapRouter.swapETHForExactTokens(4000 * 10 ** 6 , [WETH, USDT], accounts[0], 2 ** 256 - 1, {'from' : accounts[0], 'value': 10 * 10 ** 18})
    UniswapRouter.swapETHForExactTokens(2000 * 10 ** 18 , [WETH, TUSD], accounts[0], 2 ** 256 - 1, {'from' : accounts[0], 'value': 10 * 10 ** 18})
    UniswapRouter.swapETHForExactTokens(1000 * 10 ** 18 , [WETH, USDN], accounts[0], 2 ** 256 - 1, {'from' : accounts[0], 'value': 5 * 10 ** 18})
    UniswapRouter.swapETHForExactTokens(1000 * 10 ** 18 , [WETH, sUSD], accounts[0], 2 ** 256 - 1, {'from' : accounts[0], 'value': 5 * 10 ** 18})
    UniswapRouter.swapETHForExactTokens(2000 * 10 ** 18 , [WETH, BUSD], accounts[0], 2 ** 256 - 1, {'from' : accounts[0], 'value': 5 * 10 ** 18})
    UniswapRouter.swapETHForExactTokens(10 * 10 ** 18 , [WETH, sETH], accounts[0], 2 ** 256 - 1, {'from' : accounts[0], 'value': 15 * 10 ** 18})
    UniswapRouter.swapETHForExactTokens(10 ** 7, [WETH, renBTC], accounts[0], 2 ** 256 - 1, {'from' : accounts[0], 'value': 10 * 10 ** 18})
    UniswapRouter.swapETHForExactTokens(10 ** 7, [WETH, WBTC], accounts[0], 2 ** 256 - 1, {'from' : accounts[0], 'value': 10 * 10 ** 18})

    DAI.approve(cDAI, 2 ** 256 - 1, {'from' : accounts[0]})
    USDC.approve(cUSDC, 2 ** 256 - 1, {'from' : accounts[0]})
    cDAI.mint(1000 * 10 ** 18, {'from' : accounts[0]})
    cUSDC.mint(1000 * 10 ** 6, {'from' : accounts[0]})

    DAI.approve(_compoundvolgauge, 2 ** 256 - 1, {'from' : accounts[0]})
    USDC.approve(_compoundvolgauge, 2 ** 256 - 1, {'from' : accounts[0]})
    cDAI.approve(_compoundvolgauge, 2 ** 256 - 1, {'from' : accounts[0]})
    cUSDC.approve(_compoundvolgauge, 2 ** 256 - 1, {'from' : accounts[0]})

    DAI.approve(compoundpool, 2 ** 256 - 1, {'from' : accounts[0]})
    USDC.approve(compoundpool, 2 ** 256 - 1, {'from' : accounts[0]})
    cDAI.approve(compoundpool, 2 ** 256 - 1, {'from' : accounts[0]})
    cUSDC.approve(compoundpool, 2 ** 256 - 1, {'from' : accounts[0]})

    DAI.approve(_threepoolvolgauge, 2 ** 256 - 1, {'from' : accounts[0]})
    USDC.approve(_threepoolvolgauge, 2 ** 256 - 1, {'from' : accounts[0]})
    USDT.approve(_threepoolvolgauge, 2 ** 256 - 1, {'from' : accounts[0]})

    DAI.approve(threepool, 2 ** 256 - 1, {'from' : accounts[0]})
    USDC.approve(threepool, 2 ** 256 - 1, {'from' : accounts[0]})
    USDT.approve(threepool, 2 ** 256 - 1, {'from' : accounts[0]})

    DAI.approve(yDAI, 2 ** 256 - 1, {'from' : accounts[0]})
    USDC.approve(yUSDC, 2 ** 256 - 1, {'from' : accounts[0]})
    USDT.approve(yUSDT, 2 ** 256 - 1, {'from' : accounts[0]})
    TUSD.approve(yTUSD, 2 ** 256 - 1, {'from' : accounts[0]})
    yDAI.deposit(1000 * 10 ** 18, {'from' : accounts[0]})
    yUSDC.deposit(1000 * 10 ** 6, {'from' : accounts[0]})
    yUSDT.deposit(1000 * 10 ** 6, {'from' : accounts[0]})
    yTUSD.deposit(1000 * 10 ** 18, {'from' : accounts[0]})

    DAI.approve(_yvolgauge, 2 ** 256 - 1, {'from' : accounts[0]})
    USDC.approve(_yvolgauge, 2 ** 256 - 1, {'from' : accounts[0]})
    USDT.approve(_yvolgauge, 2 ** 256 - 1, {'from' : accounts[0]})
    TUSD.approve(_yvolgauge, 2 ** 256 - 1, {'from' : accounts[0]})
    yDAI.approve(_yvolgauge, 2 ** 256 - 1, {'from' : accounts[0]})
    yUSDC.approve(_yvolgauge, 2 ** 256 - 1, {'from' : accounts[0]})
    yUSDT.approve(_yvolgauge, 2 ** 256 - 1, {'from' : accounts[0]})
    yTUSD.approve(_yvolgauge, 2 ** 256 - 1, {'from' : accounts[0]})

    DAI.approve(ypool, 2 ** 256 - 1, {'from' : accounts[0]})
    USDC.approve(ypool, 2 ** 256 - 1, {'from' : accounts[0]})
    USDT.approve(ypool, 2 ** 256 - 1, {'from' : accounts[0]})
    TUSD.approve(ypool, 2 ** 256 - 1, {'from' : accounts[0]})
    yDAI.approve(ypool, 2 ** 256 - 1, {'from' : accounts[0]})
    yUSDC.approve(ypool, 2 ** 256 - 1, {'from' : accounts[0]})
    yUSDT.approve(ypool, 2 ** 256 - 1, {'from' : accounts[0]})
    yTUSD.approve(ypool, 2 ** 256 - 1, {'from' : accounts[0]})

    threepool.add_liquidity([0, 0, 1000 * 10 ** 6], 0, {'from' : accounts[0]})

    USDN.approve(_usdnvolgauge, 2 ** 256 - 1, {'from' : accounts[0]})
    CRV3.approve(_usdnvolgauge, 2 ** 256 - 1, {'from' : accounts[0]})
    DAI.approve(_usdnvolgauge, 2 ** 256 - 1, {'from' : accounts[0]})
    USDC.approve(_usdnvolgauge, 2 ** 256 - 1, {'from' : accounts[0]})
    USDT.approve(_usdnvolgauge, 2 ** 256 - 1, {'from' : accounts[0]})

    USDN.approve(usdnpool, 2 ** 256 - 1, {'from' : accounts[0]})
    CRV3.approve(usdnpool, 2 ** 256 - 1, {'from' : accounts[0]})
    DAI.approve(usdnpool, 2 ** 256 - 1, {'from' : accounts[0]})
    USDC.approve(usdnpool, 2 ** 256 - 1, {'from' : accounts[0]})
    USDT.approve(usdnpool, 2 ** 256 - 1, {'from' : accounts[0]})

    renBTC.approve(_renvolgauge, 2 ** 256 - 1, {'from' : accounts[0]})
    WBTC.approve(_renvolgauge, 2 ** 256 - 1, {'from' : accounts[0]})

    renBTC.approve(renpool, 2 ** 256 - 1, {'from' : accounts[0]})
    WBTC.approve(renpool, 2 ** 256 - 1, {'from' : accounts[0]})

    DAI.approve(_susdvolgauge, 2 ** 256 - 1, {'from' : accounts[0]})
    USDC.approve(_susdvolgauge, 2 ** 256 - 1, {'from' : accounts[0]})
    USDT.approve(_susdvolgauge, 2 ** 256 - 1, {'from' : accounts[0]})
    sUSD.approve(_susdvolgauge, 2 ** 256 - 1, {'from' : accounts[0]})

    DAI.approve(susdpool, 2 ** 256 - 1, {'from' : accounts[0]})
    USDC.approve(susdpool, 2 ** 256 - 1, {'from' : accounts[0]})
    USDT.approve(susdpool, 2 ** 256 - 1, {'from' : accounts[0]})
    sUSD.approve(susdpool, 2 ** 256 - 1, {'from' : accounts[0]})

    sETH.approve(_sethvolgauge, 2 ** 256 - 1, {'from' : accounts[0]})
    sETH.approve(sethpool, 2 ** 256 - 1, {'from' : accounts[0]})

    DAI.approve(yDAI_BUSD, 2 ** 256 - 1, {'from' : accounts[0]})
    USDC.approve(yUSDC_BUSD, 2 ** 256 - 1, {'from' : accounts[0]})
    USDT.approve(yUSDT_BUSD, 2 ** 256 - 1, {'from' : accounts[0]})
    BUSD.approve(yBUSD, 2 ** 256 - 1, {'from' : accounts[0]})
    yDAI_BUSD.deposit(1000 * 10 ** 18, {'from' : accounts[0]})
    yUSDC_BUSD.deposit(1000 * 10 ** 6, {'from' : accounts[0]})
    yUSDT_BUSD.deposit(1000 * 10 ** 6, {'from' : accounts[0]})
    yBUSD.deposit(1000 * 10 ** 18, {'from' : accounts[0]})

    DAI.approve(_busdvolgauge, 2 ** 256 - 1, {'from' : accounts[0]})
    USDC.approve(_busdvolgauge, 2 ** 256 - 1, {'from' : accounts[0]})
    USDT.approve(_busdvolgauge, 2 ** 256 - 1, {'from' : accounts[0]})
    BUSD.approve(_busdvolgauge, 2 ** 256 - 1, {'from' : accounts[0]})
    yDAI_BUSD.approve(_busdvolgauge, 2 ** 256 - 1, {'from' : accounts[0]})
    yUSDC_BUSD.approve(_busdvolgauge, 2 ** 256 - 1, {'from' : accounts[0]})
    yUSDT_BUSD.approve(_busdvolgauge, 2 ** 256 - 1, {'from' : accounts[0]})
    yBUSD.approve(_busdvolgauge, 2 ** 256 - 1, {'from' : accounts[0]})

    DAI.approve(busdpool, 2 ** 256 - 1, {'from' : accounts[0]})
    USDC.approve(busdpool, 2 ** 256 - 1, {'from' : accounts[0]})
    USDT.approve(busdpool, 2 ** 256 - 1, {'from' : accounts[0]})
    BUSD.approve(busdpool, 2 ** 256 - 1, {'from' : accounts[0]})
    yDAI_BUSD.approve(busdpool, 2 ** 256 - 1, {'from' : accounts[0]})
    yUSDC_BUSD.approve(busdpool, 2 ** 256 - 1, {'from' : accounts[0]})
    yUSDT_BUSD.approve(busdpool, 2 ** 256 - 1, {'from' : accounts[0]})
    yBUSD.approve(busdpool, 2 ** 256 - 1, {'from' : accounts[0]})