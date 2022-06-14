let express = require("express");
let app = express();

let port = 3000

app.use(function(req, res, next){
	console.log(req.method + " request for " + req.url);
	next();
});

app.use(express.static("../static"));

app.listen(port, function(){
	console.log("webServer started on port " + port);
})