_ = require('underscore');

var sum = function (iter) {
    return _.reduce(iter, function (memo, num) { return memo + num;}, 0);
}

var divs = function (num) {
    dvs = [1]
    _.each(_.range(2, Math.floor(Math.sqrt(num)+1)), function (pd) {
      if (num % pd == 0) {
        dvs.push(pd);
        if (num/pd != pd) {
            dvs.push(num/pd);
        }
      }
    });
    return _.uniq(dvs);
};

var is_abundant = function (num) {
    return sum(divs(num)) > num;
};

var abundant_numbers = _.filter(_.range(1, 28124), is_abundant);

console.log(abundant_numbers.length);

var abundant_sums = {};
_.each(abundant_numbers, function (num) {
    _.each(abundant_numbers, function (inum) {
        abundant_sums[num + inum] = true;
    });
});

console.log(_.keys(abundant_sums).length);

var nsum = _.reduce(_.range(0, 28124), function (memo, num) {
    return memo + (abundant_sums[num] ? 0 : num);
}, 0);

console.log(nsum);
