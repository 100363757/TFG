const WebSocket = require("ws");
const fs = require("fs");
const {PythonShell} = require('python-shell')
//var path = require("path");

serverport = 3001

const wss = new WebSocket.Server({port: serverport});
console.log("server started on port " + serverport);

for(let i = 0; i<4; i++){
	let newFolder = __dirname + "/" + i + "/";
	if(!fs.existsSync(newFolder)){
		fs.mkdirSync(newFolder);
	}
}

let folder = -1;
let filepath;
let savePath;
var files;
var length;
var counter = 0;
var saveFolder = -1;
var isRecording = false;
var trainning = false;

function readFolder(filepath){
fs.readdir(filepath, (err, file)=>{
	if(err) throw err;
	files = file;
	length = file.length;
	console.log("files from folder " + folder + " have been succesfully loaded");
});
}


wss.on("connection", ws =>{
	console.log("connection established");
	saveFolder = (saveFolder == 3)? 0: saveFolder + 1;
	folder = (folder == 3)? 0: folder + 1;
	filepath =__dirname + "/" + folder;
	counter = 0;
	readFolder(filepath);
	console.log("saving on label " + saveFolder);
	ws.on("message", data =>{
		const msg = JSON.parse(data);
		console.log("message received: " + msg.type);
		//console.log(msg);
		if(msg.type === "HAND_DATA"){
			if(isRecording == false){
				isRecording = true;
				savePath = __dirname + "/" + saveFolder + "/";
			}
			fs.writeFile(
				savePath + "recording - " + Date.now() + ".json", 
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
			counter = (counter == length-1)? 0: counter + 1;
		}
		if(msg.type === "TRAIN"){
				console.log("starting trainning");
				PythonShell.run("cnnImplementation.py", null, function(err, results){
					console.log("model Trained")
					ws.send(JSON.stringify({type: "READY", payload: "models/fast2/model.json"}));
				});
		}
	});


	ws.on("close", ()=>{
		console.log("connection ended");
		isRecording = false;
		files.length = 0;
	});
});

