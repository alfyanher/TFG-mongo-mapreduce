var xlsx_json = require('xlsx-to-json/')

xlsx_json({
  input:'/home/hadoop/datos/Lecturas 24.xlsx',
  output: '/home/hadoop/json/Lecturas_24.json'
 
}, function(err, result) {
  if(err) {
    console.error(err);
  }else {
    console.log(result);
  }

});
