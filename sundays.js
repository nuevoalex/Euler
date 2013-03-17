var _ = require('underscore');

var month_map = [31, null, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

count_sundays = function (day, syear, eyear) {
    var counter = 0;
    _.each(_.range(syear, eyear), function (year) {
        _.each(_.range(12), function (month_index) {
            days_in_month = month_map[month_index];
            if (days_in_month == null) {
                days_in_month = (year % 100 != 0 && year % 4 == 0 && year % 400 == 0) ? 29 : 28;
            }
            _.each(_.range(days_in_month), function (mday) {
                if (mday == 0 && day == 6) { counter += 1; }
                day += 1;
                day = day > 6 ? 0 : day;
            });
        });
    });
    return counter;
}

console.log(count_sundays(1, 1901, 2001));
