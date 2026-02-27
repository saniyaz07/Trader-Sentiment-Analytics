# Trader-Sentiment-Analytics

Insight :
  1 : Traders usually perfrom better during greed periods than in fear periods, this shows that postive market sentiment helps increase profit.
  2 : During fear periods , traders are more careful, less trading frequency , less position sizes . while during greed periods , traders are more risky and more active.
  3 : Their is noticeable shift in behaviour more sell positions during fear, more buy positions during greed . this shows that the traders react emotionally to market sentimnet.
  4 : Frequent traders perform better on average high trade size traders have higher variance that is risk and rewards consitent traders have more stable returns.

Strategies :
  1. Fear Mode (When the market is scared and dropping)
    
    Take much smaller positions
    Use much lower leverage (or no leverage at all – 1x to 3x maximum)
    Sit on Cash or Stablecoins and wait
    
    Reason: When the market is in a Fear phase, prices are moving wildly downwards, and there is a lot of selling due to panic selling. Taking a much smaller position means you will lose much less even if you’re wrong. Sitting on Cash means you’re safe and can trade another day.
  2. Greed Mode (When everyone is excited, and prices are pumping)
  
    Do more trades
    Mostly use BUY / Long positions
    Some leverage is okay (like 8x to 15x – when you’re feeling good)
    
    Reason: Greed means strong buying pressure, strong uptrends, and high volume. Long positions are more likely to win here, and making more trades allows you to win on many parts of the uptrend.
  3. Trader Type Rule (Custom Rules Based on Trading Style)
    
    If you’re a consistent and frequent trader who usually does well… then you should be given room to make even more money when the market is right.
    If you’re the risky type and have big losses, engage in revenge trading, and over-leverage… then you should be locked down hard:
    Risk only 1-2% per trade
    Max leverage 5x
    Stop trading for the day if you hit -8% or -10% loss
    
    Reason: Good traders should be given room to make even more money when the market is right. Risky traders should be locked down hard to prevent blowing up their accounts; they’re like guardrails on a dangerous road.

Methodology :
  We examined the impact of Bitcoin's Fear & Greed Index (0 = extreme fear, 100 = extreme greed) on trader performance, utilizing actual historical trading data.
  How to:
  Clean the trading data (filter duplicates, incorrect data, and invalid data)
  Associate trading data with the daily Fear & Greed Index based on the date
  Compute essential metrics:
    Profit and Loss (PnL)
    Win Rate
    Trade Frequency
    Average Return
    Risk per Trade
    Segment the market based on Fear (<= 50) and Greed (>= 50)
    Compare trader behavior and performance in both phases
  
  From this, we recognized the following:
    In Fear, win rates were lower, and losses were larger when over-leveraged.
    In Greed, win rates were higher for long positions, and trading was more profitable and frequent.
  
  From this, we created 3 straightforward trading strategies based on sentiment to boost performance and minimize blow-ups:
    Risk Adjustment in Fear
    Momentum Trading in Greed
    Trader Segmentation
