var _ = require('underscore');

var range = _.range(1,101);

var numl = [1]

var cascade_add = function (num, index, inner) {
  if (numl[index] === undefined) { numl[index] = 0 }
  var res = inner ? numl[index] + num : num
  if (res < 10) {
    numl[index] = res
  }
  else {
    numl[index] = Number(String(res).slice(-1));
    cascade_add(Math.floor(res/10), index + 1, true)
  }
}

_.each(range, function (i) {
    var rev_num = numl.slice(0).reverse();
    _.each(rev_num, function (d, d_place) {
      var num_place = rev_num.length - d_place - 1;
      var res = d * i;
      cascade_add(res, num_place);
    });
});

console.log(_.reduce(numl, function (memo, i) { return memo + i},0));
