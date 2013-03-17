var _ = require('underscore');
var fs = require('fs');

var name_val = function (name) {
  return _.reduce(name, function (total, c) {
    return total + c.charCodeAt() - 96;
  }, 0);
};

fs.readFile('/root/euler/assets/names.txt', 'ascii', function(err, data) {
  var names = data.trimRight().split(',');
  names = _.map(names, function (name) {
    return name.toLowerCase().replace(/\"/g, '');
  }).sort();
  console.log(_.reduce(names, function (total, name, index){
    return total + ((index+1) * (name_val(name)));
  }, 0));
});
