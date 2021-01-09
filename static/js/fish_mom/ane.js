var aneObj=function(){
	this.rootx=[];//save ane's root行坐标
	this.headx = [];//save ane's head ,in fact, rootx = headx;
	this.heady = [];//海葵头部的纵坐标
	this.alpha = 0;//ane shake angle海葵摆动角度
	this.amp = [];//ane shake fu_du海葵摆动振幅
}
aneObj.prototype.num=50;
aneObj.prototype.init=function(){
	for(var i=0;i<this.num;i++){
		this.rootx[i]=i * 16 + Math.random() * 20;
		this.headx[i] = this.rootx[i];
		this.heady[i] = canHeight - 250 + Math.random() * 50;
		this.amp[i] = Math.random() * 50 + 30;
	}
}
aneObj.prototype.draw=function(){
	this.alpha += deltaTime * 0.0008;
	var l =Math.sin(this.alpha);
	ctx2.save();
	ctx2.globalAlpha=0.6;
	ctx2.lineWidth=20;
	ctx2.lineCap="round";
	ctx2.strokeStyle="#3b154e";
	for(var i=0;i<this.num;i++){
		ctx2.beginPath();
		ctx2.moveTo(this.rootx[i],canWidth);
		this.headx[i] = this.rootx[i] + l * this.amp[i];
		ctx2.quadraticCurveTo(this.rootx[i], canHeight - 100, this.headx[i], this.heady[i]);
		ctx2.stroke();
	}
	ctx2.restore();
}