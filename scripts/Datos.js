var xlsx_json = require('xlsx-to-json/')

xlsx_json({
  input:'/home/hadoop/datos/Datos.xlsx',
  output: '/home/hadoop/json/Datos.json'
 
}, function(err, result) {
  if(err) {
    console.error(err);
  }else {
    console.log(result);
  }

});

