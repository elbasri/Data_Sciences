var m = msg.payload.split(',');
var H = { payload: parseFloat(m[0]) };
var T = { payload: parseFloat(m[1]) };

return [H, T];