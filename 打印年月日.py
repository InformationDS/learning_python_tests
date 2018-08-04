#将以数制定年月日的日期打印出来
months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'Octorber',
          'November',
          'December']

#一个包含日期数字结尾的得列表
endings = ['st','nd','rd'] + 17 * ['th'] + ['st','nd','rd']\
          + 7 * ['th'] + ['st']

#输入年月日
year  = input('year:')
month = input('month:')
day   = input('day:')

#将月、日换算成数字
month_number = (int)(month)
day_number   = (int)(day)

#变成英文表示
month_name = months[month_number-1]
day_name   = day+endings[day_number-1]

#输出
print(month_name + ' ' + day_name + ',' + year)


