import pandas as pd
from datetime import datetime, timedelta
import calendar

# 假设的总预算
total_budget = float(input("Enter total budget: "))

# 获取当前日期，并重置时间为当天的开始
current_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

# 获取当前月份的最后一天
_, last_day_of_month = calendar.monthrange(current_date.year, current_date.month)
end_date = datetime(current_date.year, current_date.month, last_day_of_month)

# 创建一个日期范围，从今天到月底
dates = pd.date_range(start=current_date, end=end_date)

# 创建一个空的DataFrame存储日期、每日预算和实际花费
data = []

# 计算每天的预算（保留一位小数）
remaining_days = (end_date - current_date).days + 1  # 包括今天
daily_budget = round(total_budget / remaining_days, 1)

# 填充数据：日期、每日预算、实际花费（实际花费为空）
for date in dates:
    data.append([date.strftime('%Y-%m-%d'), daily_budget, ''])  # 实际花费列为空

# 转换为DataFrame
df = pd.DataFrame(data, columns=["日期", "每日预算", "实际花费"])

# 将DataFrame保存到Excel文件
excel_filename = f"{current_date.strftime('%Y-%m')}_monthly_budget_planner.xlsx"
df.to_excel(excel_filename, index=False)

print(f"Excel表格已生成: {excel_filename}")
