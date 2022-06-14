const WebSocket = require("ws");
const fs = require("fs");
var path = require("path");

serverport = 3001

const wss = new WebSocket.Server({port: serverport});
console.log("server started on port " + serverport);

const folder = "tester";
const filepath = __dirname + "/" + folder;
var files;
var length;
var counter = 0;

fs.readdir(filepath, (err, file)=>{
	if(err) throw err;
	files = file;
	//console.log(file);
	length = file.length;
	console.log("files from folder " + folder + " have been succesfully loaded");
});



wss.on("connection", ws =>{
	console.log("connection established");

	ws.on("message", data =>{
		const msg = JSON.parse(data);
		console.log("message received: " + msg.type);
		//console.log(msg);
		if(msg.type === "HAND_DATA"){
			fs.writeFile(
				"recording - " + Date.now() + ".json", 
				JSON.stringify(msg.payload), 
				(err) =>{
					if(err) throw err;
				console.log("data saved");
			});
		}
		if(msg.type === "REQUEST"){
			fs.readFile(filepath + "/" + files[counter], (err, data) => {
				if (err) throw err;
				let frames = JSON.parse(data);
				framies = JSON.stringify({type: "FRAMES", payload: frames})
				//console.log(framies);
				ws.send(framies);
				//ws.send(JSON.stringify({type: "FRAMES", payload: frames}));
			});
			console.log("data sent");
			console.log("file: " + files[counter] + " has been read");
			counter = (counter === length-1)? 0: counter+1;
		}
	});


	ws.on("close", ()=>{
		console.log("connection ended");
	});
});

