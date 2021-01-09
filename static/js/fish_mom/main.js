//两个画布
var can1;
var can2;
//两个场景
var ctx1;
var ctx2;

var canWidth;
var canHeight;

var bgPic=new Image();
var ane;
var fruit;
var mom;
var baby;

var mx;//
var my;//

var babyTail = [];//baby's tail frame
var babyEye = [];//baby's eye frame
var babyBody = [];//baby's body color

var momTail = [];
var momEye = [];
var momBodyOra = [];
var momBodyBlue = [];

var data;//score fen_shu
var lastTime;//上一帧被执行的时间
var deltaTime;//两帧间隔时间差

var wave;//te_xiao eat
var halo;//te_xiao feed

var dust;//漂浮物
var dustPic = [];//存放漂浮物的图片

document.body.onload = game;
function game(){
	init();
	lastTime = Date.now();
	deltaTime=0;
	gameloop();
}

function init(){
	can1=document.getElementById("canvas1");//fishes,dust,UI,circle
	ctx1=can1.getContext("2d");
	can2=document.getElementById("canvas2");//canvas相当于画布background,anemone,fruit
	ctx2=can2.getContext("2d");
	
	can1.addEventListener("mousemove", onMouseMove, false);//canvas listen mouse_move
	
	bgPic.src="../../static/img/fish_mom/background.jpg";
	
	canWidth=can1.width;
	canHeight=can1.height;
	
	ane=new aneObj();
	ane.init();
	
	fruit=new fruitObj();
	fruit.init();
	
	mom=new momObj();
	mom.init();
	
	baby=new babyObj();
	baby.init();
	
	mx=canWidth*0.5;
	my=canHeight*0.5;
	
	for(var i=0;i<8;i++){
		babyTail[i] = new Image();
		babyTail[i].src="../../static/img/fish_mom/babyTail"+i+".png";
	}
	
	for(var i=0;i<2;i++){
		babyEye[i]=new Image();
		babyEye[i].src="../../static/img/fish_mom/babyEye"+i+".png";
	}
	
	for(var i = 0;i < 20;i++){
		babyBody[i] = new Image();
		babyBody[i].src = "../../static/img/fish_mom/babyFade"+i+".png";
	}
	
	for(var i = 0; i < 8; i++){
		momTail[i] = new Image();
		momTail[i].src = "../../static/img/fish_mom/bigTail" + i + ".png";
	}
	
	for(var i=0;i < 2;i++){
		momEye[i] = new Image();
		momEye[i].src = "../../static/img/fish_mom/bigEye" + i + ".png";
	}
	
	data = new dataObj();
	
	for(var i=0;i < 8;i++){
		momBodyOra[i] = new Image();
		momBodyBlue[i] = new Image();
		momBodyOra[i].src = "../../static/img/fish_mom/bigSwim" + i + ".png";
		momBodyBlue[i].src = "../../static/img/fish_mom/bigSwimBlue" + i + ".png";
	}
	
	ctx1.font = "30px Verdana";
	ctx1.textAlign = "center";
	
	wave = new waveObj();
	wave.init();
	
	halo = new haloObj();
	halo.init();
	
	for(var i = 0;i < 7;i++){
		dustPic[i] = new Image();
		dustPic[i].src = "../../static/img/fish_mom/dust"+i+".png";
	}
	dust = new dustObj;
	dust.init();
}

function gameloop(){
	window.requestAnimFrame(gameloop);//这个方法不同的浏览器需要进行配饰，也就是适应不同浏览器，这个放在在commonFunctions.js里可以找到。
	var now=Date.now();
	deltaTime=now-lastTime;
	lastTime=now;
	if(deltaTime>40) deltaTime=40;
	
	drawBackground();
	ane.draw();
	fruitMonit();
	fruit.draw();
	
	ctx1.clearRect(0, 0, canWidth, canHeight);
	mom.draw();
	baby.draw();
	momFruitsCollision();
	momBabyCollision();
	
	data.draw();
	wave.draw();
	halo.draw();
	dust.draw();
}

function onMouseMove(e){
	if(!data.gameOver){
		if(e.offsetX||e.layerX){
			mx=e.offsetX==undefined?e.layerX:e.offsetX;
			my=e.offsetY==undefined?e.layerY:e.offsetY;
		}		
	}
}