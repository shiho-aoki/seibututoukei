function enc_weather (dec_data) {
    let data = [];
    　switch( dec_data ) {
         case '快晴':
           data.push(1);
           break;
         case '晴':
           data.push(2);
           break;
         case '曇':
           data.push(3);
           break;
         case '薄雲':
           data.push(4);
           break;
         case '大風':
           data.push(5);
           break;
         case '霧':
           data.push(6);
           break;
         case '霧雨':
           data.push(7);
           break;
         case '雨':
           data.push(8);
           break;
         case '大雨':
           data.push(9);
           break;
         case '雨，大風を伴う':
           data.push(10);
           break;
         case '暴風雨':
           data.push(11);
           break;
         case 'みぞれ':
           data.push(12);
           break;
         case '雪':
           data.push(13);
           break;
         case '大雪':
           data.push(14);
           break;
         case '暴風雪':
           data.push(15);
           break;
         case '地ふぶき':
           data.push(16);
           break;
         case 'ふぶき':
           data.push(17);
           break;
         case 'ひょう':
           data.push(18);
           break;
         case 'あられ':
           data.push(19);
           break;
         case '雷':
           data.push(20);
           break;
         default:
           data.push(0);
       };
     return data;
  };
  function weather() {
    var spr = SpreadsheetApp.openById('16h6qMCyy25rzr6j5SEoGCNqUfLI3xSU0b4O13VT5ZBI');//**need to chnage
    var sheet  = spr.getSheets()[0];
    
    var weather = sheet.getRange(1,8,sheet.getLastRow() - 1,1).getValues();
    var data = []
    for (let i=1; i < weather.length; i++ ) {
      let weather_data = String(weather[i][0]);
      let TOKIDOKI_index = weather_data.indexOf('時々');
      let ICHIZI_index = weather_data.indexOf('一時');
      if (TOKIDOKI_index !== -1){
       let before = weather_data.substr(0,TOKIDOKI_index);
       let after = weather_data.substr(TOKIDOKI_index+2);
       let before_status = enc_weather(before)[0];
       let after_status = enc_weather(after)[0]/4;
       let enc_data_ = before_status + after_status;
       data.push(enc_data_);
  
      }else if (ICHIZI_index !== -1){
        let before = weather_data.substr(0,ICHIZI_index);
       let after = weather_data.substr(ICHIZI_index+2);
       let before_status = enc_weather(before)[0];
       let after_status = enc_weather(after)[0]/4;
       let enc_data__ = before_status + after_status;
       data.push(enc_data__);
  
      }else{
      　let enc_data = enc_weather(weather_data);
       data.push(enc_data[0]);
      }
    };
    for (let i=1; i < weather.length; i++ ) {
      sheet.getRange(i+1,9).setValue(data[i-1])
    };
  }  