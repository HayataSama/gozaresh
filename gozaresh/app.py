import jdatetime
from flask import Flask, render_template, request, redirect


def mainFunc(lesson, activity, homework, reading):
    tarikh = jdatetime.date.today()
    weekdays = ['شنبه', 'یک شنبه', 'دوشنبه',
                'سه شنبه', 'چهارشنبه', 'پنج شنبه', 'جمعه']
    weekday = weekdays[tarikh.weekday()]
    day = str(tarikh.day)
    if len(day) == 1:
        day = '0' + day
    month = str(tarikh.month)

    if len(month) == 1:
        month = '0' + month
    tarikhvalid = ('%s-%s-%s' % (day, month, tarikh.year))

    dars = lesson
    moalem = ''
    lessons = [['انسان و محیط زیست', 'طاهری'], ['فیزیک', 'صفایی'], ['زبان', 'چراغی'], ['دینی', 'مقدادیان'], ['شیمی', 'عباسی'], ['حسابان', 'داوودی'], ['آمار', 'براتی'], ['فارسی', 'هادی'], [
        'نگارش', 'هادی'], ['کار آفرینی', 'مشهدی محمد'], ['عربی', 'خلیلی'], ['زیست', 'اسبقی'], ['ریاضی', 'جهان بخش'], ['تاریخ', 'جلالی'], ['زمین شناسی', 'کیان پور'], ['حیله', 'قیومی']]

    for lesson in lessons:
        if dars == lesson[0]:
            moalem = lesson[1]

    tadris = activity

    taklif = homework
    if taklif == '1':
        taklif = '-----'
    elif taklif == 'مدبر':
        taklif = 'به مدبر مراجعه شود'
    motalee = reading
    if motalee == '1':
        motalee = '-----'
    elif motalee == 'مرور':
        motalee = 'مرور مطالب تدریس شده'

    # output_str = f'''
    # 💫 برنامه {weekday} {tarikhvalid}
    # ✅ پایه یازدهم تجربی
    # 👈  درس {dars} کلاس آنلاین جناب آقای {moalem}
    # ✍️ تدریس {tadris}
    # 🔺 تکلیف: {taklif}
    # 🔺 مطالعه: {motalee}
    # '''

    # output_str = f'💫 برنامه {weekday} {tarikhvalid} \n ✅ پایه یازدهم تجربی \n 👈  درس {dars} کلاس آنلاین جناب آقای {moalem} \n ✍️ تدریس {tadris} \n 🔺 تکلیف: {taklif} \n 🔺 مطالعه: {motalee}'
    return weekday, tarikhvalid, dars, moalem, tadris, taklif, motalee


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit')
def submit():
    lesson = request.args.get('lesson')
    activity = request.args.get('activity')
    homework = request.args.get('homework')
    reading = request.args.get('reading')
    weekday, tarikhvalid, dars, moalem, tadris, taklif, motalee = mainFunc(
        lesson, activity, homework, reading)
    return render_template('result.html', weekday=weekday, tarikhvalid=tarikhvalid, dars=dars, moalem=moalem, tadris=tadris, taklif=taklif, motalee=motalee)


if __name__ == '__main__':
    app.run(debug=True)
