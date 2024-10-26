#  Copyright (c) 2022. Generated by Gu.
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

goog = pd.read_csv(r'D:\Python\PycharmProjects\Project1\jupyter\Pandas\data\GOOG.csv')
goog.set_index('Date', inplace=True)

index = pd.DatetimeIndex(goog.index)
close = goog.Close
goog1 = pd.Series(close.values, index=index)
sns.set()

# Google收盘价随时间变化的趋势
goog1.plot()

# Google股票收盘价进行重新取样
goog1.plot(alpha=0.5, style='-')
goog1.resample('BA').mean().plot(style=':')
goog1.asfreq('BA').plot(style='--')
plt.legend(['input', 'resample', 'asfreq'],
           loc='upper left')
plt.show()

# 工作日数据按天进行重新取样
fig, ax = plt.subplots(2, sharex=True)
data = goog1.iloc[:10]
data.asfreq('D').plot(ax=ax[0], marker='o')
data.asfreq('D', method='bfill').plot(ax=ax[1], style='-o')
data.asfreq('D', method='ffill').plot(ax=ax[1], style='--o')
ax[1].legend(["back-fill", "forward-fill"])
plt.show()

# 工作日数据按天进行重新取样
fig, ax = plt.subplots(2, sharex=True)
data = goog1.iloc[:10]
data.asfreq('D').plot(ax=ax[0], marker='o')
data.asfreq('D', method='bfill').plot(ax=ax[1], style='-o')
data.asfreq('D', method='ffill').plot(ax=ax[1], style='--o')
ax[1].legend(["back-fill", "forward-fill"])

# 法让数据迁移900天
fig, ax = plt.subplots(3, sharey=True)
# 对数据应用时间频率,用向后填充解决缺失值
goog1 = goog1.asfreq('D', method='pad')
goog1.plot(ax=ax[0])
goog1.shift(900).plot(ax=ax[1])
goog1.tshift(900).plot(ax=ax[2])
# 设置图例与标签
local_max = pd.to_datetime('2017-11-05')
offset = pd.Timedelta(900, 'D')
ax[0].legend(['input'], loc=2)
ax[0].get_xticklabels()[4].set(weight='heavy', color='red')
ax[0].axvline(local_max, alpha=0.3, color='red')
ax[1].legend(['shift(900)'], loc=2)
ax[1].get_xticklabels()[4].set(weight='heavy', color='red')
ax[1].axvline(local_max + offset, alpha=0.3, color='red')
ax[2].legend(['tshift(900)'], loc=2)
ax[2].get_xticklabels()[1].set(weight='heavy', color='red')
ax[2].axvline(local_max + offset, alpha=0.3, color='red')
plt.show()

# 一年期的投资回报率
ROI = 100 * (goog1.tshift(-365) / goog1 - 1)
ROI.plot()
plt.ylabel('% Return on Investment')
plt.figure(640 * 480)
plt.show()

# Google股票收盘价的一年期移动平均值和标准差
rolling = goog1.rolling(365, center=True)
data = pd.DataFrame({'input': goog1,
                     'one-year rolling_mean': rolling.mean(),
                     'one-year rolling_std': rolling.std()})
ax = data.plot(style=['-', '--', ':'])
ax.lines[0].set_alpha(0.3)
plt.show()
